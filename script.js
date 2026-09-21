/* Progressive enhancement. No analytics, uploads, cookies or browser storage. */
(function () {
  "use strict";
  const allowed = {
    document: [
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
    ],
    country: [
      "UAE",
      "Saudi Arabia",
      "Qatar",
      "Oman",
      "Bahrain",
      "Kuwait",
      "UK",
      "Europe",
      "Canada",
      "Australia",
      "USA",
      "Other",
    ],
    purpose: [
      "Employment",
      "Study",
      "Immigration",
      "Marriage",
      "Business",
      "Legal",
      "Other",
    ],
    issue: [
      "No problem",
      "Name mismatch",
      "Spelling mistake",
      "Father’s name mismatch",
      "Date-of-birth mismatch",
      "Rejected document",
      "Missing document",
      "Not sure",
    ],
  };
  function cleanAnswers(input) {
    const output = {};
    for (const [key, values] of Object.entries(allowed)) {
      if (values.includes(input[key])) output[key] = input[key];
    }
    return output;
  }
  function buildPath(input) {
    const a = cleanAnswers(input);
    if (Object.keys(a).length !== 4)
      throw new Error("Complete all four assessment questions.");
    const path = [];
    if (a.issue !== "No problem") {
      const copy =
        a.issue === "Missing document"
          ? "Identify the missing record and ask the issuer or requesting authority about replacement or accepted alternatives before submission."
          : a.issue === "Rejected document"
            ? "Review the authority’s stated reason before resubmitting. Additional stamps alone may not resolve the query."
            : a.issue === "Not sure"
              ? "Clarify the document and the receiving organisation’s request before selecting an authority or paying fees."
              : "Compare the source records. Ask the responsible issuer about correction or verification; do not alter documents yourself.";
      path.push({ title: "First: review your reported issue", text: copy });
    }
    path.push({
      title: a.document + " · identify the issuer",
      text: "Confirm the exact document title, issuing body and current record.",
    });
    const purposeNotes = {
      Employment:
        "Ask the employer whether authentication, professional recognition or both are required.",
      Study:
        "Ask the institution whether it needs direct issuer delivery, credential evaluation or authenticated documents.",
      Immigration:
        "Use the specific immigration authority’s written checklist; authentication does not determine eligibility.",
      Marriage:
        "Confirm the exact civil record, accepted translation and receiving authority’s requirements.",
      Business:
        "Identify the signatory, legal capacity and intended commercial use. Obtain professional advice where needed.",
      Legal:
        "Ask the receiving court or authority about execution, witnessing, personal appearance and accepted formats.",
      Other:
        "Clarify the intended use and the receiving organisation’s written requirements.",
    };
    path.push({
      title: "Verify requirements for " + a.purpose.toLowerCase(),
      text: purposeNotes[a.purpose],
    });
    let authority = "Relevant authority · confirm before proceeding";
    let detail =
      "Identify the competent authority for this document. Do not assume an educational route applies.";
    if (["Degree", "Transcript"].includes(a.document)) {
      authority = "HEC or relevant educational authority · check eligibility";
      detail =
        "For eligible higher-education records, check HEC. A transcript from a school or other issuer may follow a different route.";
    } else if (a.document === "Diploma") {
      authority = "Qualification and issuer review";
      detail =
        "Confirm whether IBCC, HEC or a technical awarding body is relevant. A diploma is not automatically assigned to one authority.";
    } else if (
      ["Marriage Certificate", "Birth Certificate", "FRC"].includes(a.document)
    ) {
      authority = "Civil or identity record issuer";
      detail =
        "Identify the specific record and issuing body. Confirm its verification requirements before further authentication.";
    } else if (a.document === "PCC") {
      authority = "Issuing police authority";
      detail =
        "Check the recipient’s requirements for the certificate, coverage period and any verification or freshness requirement.";
    } else if (["Commercial", "Power of Attorney"].includes(a.document)) {
      authority = "Competent commercial or legal authority";
      detail =
        "Confirm the document’s execution, signatory, prerequisite authentication and any personal appearance requirement.";
    }
    path.push({ title: authority, text: detail });
    path.push({
      title: "MOFA · check the applicable service",
      text: "Confirm prerequisites and whether attestation or an apostille service is applicable. These are not automatically two separate required steps.",
    });
    path.push({
      title: "Apostille or embassy route · confirm applicability",
      text: "Check the treaty relationship, document scope, official instructions and recipient. Country membership alone is not a complete determination.",
    });
    path.push({
      title:
        a.country === "Europe" || a.country === "Other"
          ? "Identify the specific destination"
          : "Receiving organisation in " + a.country,
      text: "Confirm accepted format, translations and any recognition or destination-side procedure before submitting.",
    });
    return path;
  }
  // The same pure logic is exercised by the dependency-free test suite.
  if (typeof module !== "undefined" && module.exports)
    module.exports = { buildPath, cleanAnswers };
  if (typeof document === "undefined") return;

  const menuButton = document.querySelector(".menu-toggle");
  const menu = document.querySelector(".nav-links");
  function closeMenu(restoreFocus) {
    if (!menuButton || !menu) return;
    menuButton.setAttribute("aria-expanded", "false");
    menu.classList.remove("open");
    if (restoreFocus) menuButton.focus();
  }
  if (menuButton && menu) {
    menuButton.addEventListener("click", () => {
      const open = menuButton.getAttribute("aria-expanded") !== "true";
      menuButton.setAttribute("aria-expanded", String(open));
      menu.classList.toggle("open", open);
    });
    menu.addEventListener("click", (event) => {
      if (event.target.closest("a")) closeMenu(false);
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && menu.classList.contains("open"))
        closeMenu(true);
    });
    document.addEventListener("click", (event) => {
      if (!event.target.closest(".topbar")) closeMenu(false);
    });
    matchMedia("(min-width: 851px)").addEventListener("change", () =>
      closeMenu(false),
    );
  }

  document.querySelectorAll("[data-doc]").forEach((button) => {
    button.addEventListener("click", () => {
      document
        .querySelectorAll("[data-doc]")
        .forEach((item) =>
          item.setAttribute("aria-pressed", String(item === button)),
        );
      const title = document.querySelector("[data-paper-title]");
      if (title)
        title.textContent =
          button.dataset.doc === "Degree"
            ? "Degree Certificate"
            : button.dataset.doc;
    });
  });
  document.querySelectorAll("[data-journey]").forEach((button) => {
    button.addEventListener("click", () => {
      document
        .querySelectorAll("[data-journey]")
        .forEach((item) =>
          item.setAttribute("aria-pressed", String(item === button)),
        );
      const stage = Number(button.dataset.journey);
      const journey = button.closest(".journey");
      journey.style.setProperty("--stage", stage);
      journey.style.setProperty("--column", stage % 3);
      journey.style.setProperty("--row", Math.floor(stage / 3));
      document.querySelector(".journey-detail p").textContent =
        button.dataset.description;
    });
  });
  document.querySelectorAll("[data-faq-filter]").forEach((button) => {
    button.addEventListener("click", () => {
      document
        .querySelectorAll("[data-faq-filter]")
        .forEach((item) =>
          item.setAttribute("aria-pressed", String(item === button)),
        );
      document.querySelectorAll("[data-faq-category]").forEach((item) => {
        item.hidden =
          button.dataset.faqFilter !== "All" &&
          item.dataset.faqCategory !== button.dataset.faqFilter;
      });
    });
  });
  const destination = document.querySelector("[data-destination]");
  if (destination) {
    let destinations;
    const copy = document.querySelector(".destination-copy");
    const guide = document.querySelector(".destination-guide");
    function showDestination() {
      const name = destination.value;
      if (destinations && destinations[name])
        copy.textContent = destinations[name];
      else
        copy.textContent =
          "For " +
          name +
          ", confirm the receiving organisation’s document-specific instructions and the applicable official route before submission.";
      if (name === "UAE" || name === "Saudi Arabia") {
        guide.href =
          "/countries/" + (name === "UAE" ? "uae" : "saudi-arabia") + "/";
        guide.innerHTML =
          'Explore destination <span aria-hidden="true">↗</span>';
      } else {
        guide.href = "/guides/apostille-vs-embassy-attestation/";
        guide.innerHTML =
          'Understand the routes <span aria-hidden="true">↗</span>';
      }
    }
    destination.addEventListener("change", showDestination);
    fetch("/assets/destinations.json")
      .then((r) => {
        if (!r.ok) throw new Error("Destination content unavailable");
        return r.json();
      })
      .then((data) => {
        destinations = data;
        showDestination();
      })
      .catch(() => showDestination());
  }

  document.querySelectorAll("[data-assessment]").forEach((form) => {
    // Validation is handled per visible step; no-JS visitors retain ordinary HTML controls.
    form.noValidate = true;
    let step = 0;
    const fields = Array.from(form.querySelectorAll("[data-step]"));
    const names = ["Document", "Destination", "Purpose", "Problem"];
    const result = form.querySelector(".result");
    const next = form.querySelector("[data-next]");
    const back = form.querySelector("[data-back]");
    const error = form.querySelector(".error");
    function showStep(number, moveFocus = true) {
      step = number;
      fields.forEach((field, i) => {
        field.hidden = i !== step;
        field.disabled = i !== step;
      });
      result.hidden = true;
      form.querySelector(".form-controls").hidden = false;
      form.querySelector("[data-step-label]").textContent =
        "0" + (step + 1) + " / " + names[step];
      form.querySelector("[data-step-count]").textContent =
        "Step " + (step + 1) + " of 4";
      form.querySelector(".progress i").style.width = (step + 1) * 25 + "%";
      form
        .querySelector(".progress")
        .setAttribute("aria-valuenow", String(step + 1));
      next.innerHTML =
        (step === 3 ? "See My Document Path" : "Continue") +
        ' <span aria-hidden="true">→</span>';
      back.hidden = step === 0;
      form.querySelector("[data-local-note]").hidden = step !== 0;
      error.textContent = "";
      if (moveFocus) fields[step].querySelector("legend").focus();
    }
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      const selection = fields[step].querySelector("input:checked");
      if (!selection) {
        error.textContent = "Choose an option to continue.";
        fields[step].querySelector("input").focus();
        return;
      }
      if (step < 3) {
        showStep(step + 1);
        return;
      }
      const answers = {};
      fields.forEach((field) => {
        const input = field.querySelector("input:checked");
        answers[input.name] = input.value;
      });
      const path = buildPath(answers);
      const list = form.querySelector(".result-path");
      list.replaceChildren();
      path.forEach((item) => {
        const li = document.createElement("li");
        const strong = document.createElement("strong");
        const p = document.createElement("p");
        strong.textContent = item.title;
        p.textContent = item.text;
        li.append(strong, p);
        list.append(li);
      });
      form.querySelector(".result-summary").textContent =
        answers.document +
        " · " +
        answers.country +
        " · " +
        answers.purpose +
        " · " +
        answers.issue;
      form.querySelector(".request-assessment").href =
        "/contact/#" + new URLSearchParams(answers).toString();
      fields.forEach((field) => {
        field.hidden = true;
        field.disabled = true;
      });
      form.querySelector(".form-controls").hidden = true;
      form.querySelector("[data-step-label]").textContent = "Your next steps";
      form.querySelector("[data-step-count]").textContent =
        "Assessment complete";
      error.textContent = "";
      result.hidden = false;
      result.querySelector("h3").focus();
    });
    back.addEventListener("click", () => showStep(Math.max(0, step - 1)));
    form.querySelector(".restart").addEventListener("click", () => {
      form.reset();
      showStep(0);
    });
    form.addEventListener("change", () => {
      error.textContent = "";
    });
  });

  const contact = document.querySelector("[data-contact]");
  if (contact) {
    const params = new URLSearchParams(location.hash.slice(1));
    const answers = cleanAnswers(Object.fromEntries(params));
    if (Object.keys(answers).length === 4) {
      contact.elements.message.value =
        "I would like a document assessment.\n\nDocument: " +
        answers.document +
        "\nDestination: " +
        answers.country +
        "\nPurpose: " +
        answers.purpose +
        "\nIssue: " +
        answers.issue +
        "\n\nPlease help me identify the applicable requirements and next steps.";
      // Keep the initial category-only handoff out of subsequent copied URLs.
      history.replaceState(null, "", location.pathname);
    }
    contact.addEventListener("submit", (event) => {
      event.preventDefault();
      if (!contact.reportValidity()) return;
      const message = contact.elements.message.value.trim();
      if (!message) {
        contact.querySelector(".contact-status").textContent =
          "Describe your situation before preparing the draft.";
        return;
      }
      const name = contact.elements.name.value.trim();
      const body = message + (name ? "\n\nFrom: " + name : "");
      contact.querySelector("[data-email-link]").href =
        "mailto:info@salaroutsourcing.com?subject=" +
        encodeURIComponent("Document assessment enquiry") +
        "&body=" +
        encodeURIComponent(body);
      contact.querySelector("[data-email-ready]").hidden = false;
      contact.querySelector(".contact-status").textContent =
        "Your draft is ready. Nothing has been sent. Open it below, review it and send from your email application.";
    });
    contact.addEventListener("input", () => {
      contact.querySelector("[data-email-ready]").hidden = true;
      contact.querySelector(".contact-status").textContent = "";
    });
  }
})();
