const { test } = require("node:test");
const assert = require("node:assert/strict");
const { buildPath, cleanAnswers } = require("../script.js");
const base = {
  document: "Degree",
  country: "UAE",
  purpose: "Employment",
  issue: "No problem",
};
test("unknown records never silently become a degree", () => {
  const path = buildPath({ ...base, document: "Other" });
  assert.ok(!path.some((x) => x.title.startsWith("HEC")));
  assert.ok(path.some((x) => x.title.startsWith("Relevant authority")));
});
test("diploma requires an issuer review", () => {
  const path = buildPath({ ...base, document: "Diploma" });
  assert.ok(path.some((x) => x.title === "Qualification and issuer review"));
});
test("reported issues come before authentication", () => {
  for (const issue of [
    "Name mismatch",
    "Spelling mistake",
    "Father’s name mismatch",
    "Date-of-birth mismatch",
    "Rejected document",
    "Missing document",
    "Not sure",
  ]) {
    assert.equal(
      buildPath({ ...base, issue })[0].title,
      "First: review your reported issue",
    );
  }
});
test("country choices do not produce guaranteed treaty or embassy claims", () => {
  for (const country of [
    "UAE",
    "Saudi Arabia",
    "Qatar",
    "Oman",
    "Bahrain",
    "Kuwait",
    "UK",
    "Germany",
    "France",
    "Italy",
    "Europe",
    "Canada",
    "Australia",
    "USA",
    "Other",
  ]) {
    const path = buildPath({ ...base, country });
    assert.ok(
      path.some(
        (x) => x.title === "Apostille or embassy route · confirm applicability",
      ),
    );
    assert.ok(
      !JSON.stringify(path).includes(
        "embassy or consular attestation is required",
      ),
    );
  }
});
test("purpose changes the practical preparation guidance", () => {
  assert.match(
    buildPath({ ...base, purpose: "Study" })[1].text,
    /direct issuer/,
  );
  assert.match(buildPath({ ...base, purpose: "Legal" })[1].text, /court/);
});
test("rejects incomplete and untrusted handoff inputs", () => {
  assert.throws(() => buildPath({ ...base, document: "<script>" }));
  assert.deepEqual(
    cleanAnswers({ document: "Degree", name: "Private", country: "Invalid" }),
    { document: "Degree" },
  );
});
test("all document categories produce distinct valid paths", () => {
  for (const document of [
    "Degree",
    "Diploma",
    "Transcript",
    "Marriage Certificate",
    "Birth Certificate",
    "PCC",
    "FRC",
    "Commercial",
    "Power of Attorney",
    "Other",
  ]) {
    const path = buildPath({ ...base, document });
    assert.equal(path.length, 6);
    assert.ok(path.every((x) => x.title && x.text));
  }
});

test("a mosadaqa verification query is treated as a record problem first", () => {
  const path = buildPath({ ...base, issue: "Mosadaqa / verification query" });
  assert.equal(path[0].title, "First: review your reported issue");
  assert.match(path[0].text, /record/);
  assert.match(path[0].text, /CNIC/);
});
test("every destination with published guidance is an accepted answer", () => {
  for (const country of ["Germany", "France", "Italy"]) {
    const path = buildPath({ ...base, country });
    assert.equal(path.length, 6);
    assert.ok(path.at(-1).title.includes(country));
  }
});
