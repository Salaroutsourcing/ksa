const { test } = require("node:test");
const assert = require("node:assert/strict");
const { buildPath, cleanAnswers } = require("../script.js");

const base = {
  service: "Mosadaqa degree attestation",
  document: "Degree",
  country: "Saudi Arabia",
  issue: "No problem",
};
const services = [
  "Mosadaqa degree attestation",
  "Saudi Culture attestation",
  "Saudi Embassy attestation",
  "QVP attestation",
  "Apostille attestation",
  "Not sure yet",
];
const issues = [
  "Name mismatch",
  "Father’s name mismatch",
  "Spelling mistake",
  "Date-of-birth mismatch",
  "Mosadaqa or QVP query",
  "Rejected or refused",
  "Missing document",
  "Not sure",
];

test("an incomplete assessment is rejected", () => {
  assert.throws(() => buildPath({ service: "Apostille attestation" }));
  assert.throws(() => buildPath({ ...base, service: "<script>" }));
});

test("every accepted issue is handled before the stages", () => {
  for (const issue of issues) {
    const path = buildPath({ ...base, issue });
    assert.equal(path[0].title, "First: resolve the reported issue");
  }
});

test("a Mosadaqa or QVP query is treated as a record problem first", () => {
  const path = buildPath({ ...base, issue: "Mosadaqa or QVP query" });
  assert.match(path[0].text, /wording/);
  assert.match(path[0].text, /CNIC/);
  assert.match(path[0].text, /passport/);
});

test("the record comparison step always appears before the recipient", () => {
  for (const service of services) {
    const path = buildPath({ ...base, service });
    assert.ok(
      path.some((x) => x.title === "Records to compare before any stage"),
      service,
    );
    assert.match(
      path.find((x) => x.title === "Records to compare before any stage").text,
      /CNIC/,
    );
  }
});

test("each service is mapped to its own stage explanation", () => {
  assert.match(
    buildPath({ ...base, service: "Mosadaqa degree attestation" })[
      base.issue === "No problem" ? 0 : 1
    ].text,
    /education authority/,
  );
  assert.match(
    buildPath({ ...base, service: "QVP attestation" })[0].text,
    /qualification verification/,
  );
  assert.match(
    buildPath({ ...base, service: "Apostille attestation" })[0].text,
    /Convention/,
  );
  const unsure = buildPath({ ...base, service: "Not sure yet" })[0].text;
  assert.match(unsure, /Confirm which service/);
});

test("no service claims a guaranteed outcome or a fixed route", () => {
  for (const service of services) {
    const text = JSON.stringify(buildPath({ ...base, service }));
    assert.ok(!/guarantee|guaranteed|embassy or consular attestation is required/i.test(text));
  }
});

test("Saudi Arabia and other destinations produce different recipient steps", () => {
  assert.equal(
    buildPath({ ...base, country: "Saudi Arabia" }).at(-1).title,
    "Saudi-side requirement",
  );
  assert.match(
    buildPath({ ...base, country: "United Kingdom" }).at(-1).title,
    /Recipient in United Kingdom/,
  );
});

test("every destination in the selector produces a complete path", () => {
  for (const country of ["Saudi Arabia", "United Arab Emirates", "Qatar", "Kuwait", "Oman", "Bahrain", "United Kingdom", "Europe", "Canada", "Australia", "Other"]) {
    const path = buildPath({ ...base, country });
    assert.ok(path.length >= 4);
    assert.ok(path.every((x) => x.title && x.text));
    assert.ok(path.at(-1).title.includes(country) || country === "Saudi Arabia");
  }
});

test("untrusted handoff values are dropped, not echoed", () => {
  assert.deepEqual(
    cleanAnswers({
      service: "Apostille attestation",
      name: "Private",
      country: "Invalid",
      document: "<script>",
    }),
    { service: "Apostille attestation" },
  );
});
