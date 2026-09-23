/* Pure preparation guidance. No official routes, eligibility, fees or dates are calculated. */
(function (root) {
  "use strict";
  const choices = {
    document: [
      "Degree / transcript",
      "Diploma / certificate",
      "Personal document",
      "Business / legal document",
      "Other / not sure",
    ],
    destination: ["Saudi Arabia", "United Arab Emirates", "Other / not sure"],
    issue: [
      "No known issue",
      "Name or identity difference",
      "Missing record",
      "University reply pending",
      "Previous rejection",
      "Not sure which process",
    ],
  };
  function clean(input) {
    const values = {};
    for (const [key, options] of Object.entries(choices))
      if (options.includes(input[key])) values[key] = input[key];
    return values;
  }
  function assess(input) {
    const a = clean(input);
    if (Object.keys(a).length !== 3)
      throw new Error("Complete all three questions.");
    const steps = [];
    const issues = {
      "Name or identity difference": [
        "Compare the records first",
        "Write down the exact difference and contact the responsible issuer about correction. Ask the recipient what supporting evidence it accepts. Do not alter a document yourself.",
      ],
      "Missing record": [
        "Identify the missing item",
        "Ask which exact record is needed. Contact its issuer about replacement, or the recipient about permitted alternatives, before making another application.",
      ],
      "University reply pending": [
        "Clarify the unanswered request",
        "Ask the relevant university office whether it has received the request and what information it needs. A pending reply is not automatically a rejection.",
      ],
      "Previous rejection": [
        "Start with the stated reason",
        "Read the actual query or rejection. Ask the deciding institution what action is required before resubmitting or paying another fee.",
      ],
      "Not sure which process": [
        "Identify the named requirement",
        "Ask the requesting organisation for the programme name, official link and intended purpose. Avoid selecting a service from an informal label alone.",
      ],
    };
    if (issues[a.issue])
      steps.push({ title: issues[a.issue][0], text: issues[a.issue][1] });
    const documents = {
      "Degree / transcript":
        "Confirm the awarding institution, qualification title and whether the request is academic verification, recognition or evidence for employment.",
      "Diploma / certificate":
        "Identify the exact qualification level and awarding body. A diploma or certificate does not automatically follow a university-degree process.",
      "Personal document":
        "Identify the civil or identity record and its issuer. Ask the recipient about accepted originals, copies, translations and any date-of-issue requirement.",
      "Business / legal document":
        "Confirm the document type, signatory and purpose. Ask the competent authority about execution and appearance requirements; seek qualified legal advice where needed.",
      "Other / not sure":
        "Clarify the exact document title and issuer before choosing a programme. An unknown document should not be treated as an academic qualification.",
    };
    steps.push({
      title: "Identify the document and its purpose",
      text: documents[a.document],
    });
    let destination =
      "Identify the specific country and receiving organisation, then obtain its current written instructions.";
    if (a.destination === "Saudi Arabia")
      destination =
        "Ask the Saudi recipient whether the request concerns an academic certificate, employment-related qualification checks or another process. Confirm the official programme and its scope.";
    if (a.destination === "United Arab Emirates")
      destination =
        "Obtain the UAE recipient’s written requirements. Check the current official service and relevant mission instructions for this document and issuer.";
    steps.push({
      title: "Confirm the recipient’s instructions",
      text: destination,
    });
    steps.push({
      title: "Keep official steps in the official channel",
      text: "Applicant-only steps, identity checks, account access and consent stay with the applicant or officially permitted provider. We do not issue authentication or claim appointed-agent status.",
    });
    steps.push({
      title: "Agree the scope before paid assistance",
      text: "Clarify the preparation work, current official charges and any separate assistance fee. No approval or completion date can be promised by this checker.",
    });
    return steps;
  }
  const api = { choices, clean, assess };
  if (typeof module !== "undefined" && module.exports) module.exports = api;
  else root.SKChecker = api;
})(typeof window !== "undefined" ? window : this);
