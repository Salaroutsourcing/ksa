/* Progressive enhancement. No analytics, uploads, cookies or browser storage. */
(function () {
  "use strict";
  const allowed = {
    service: [
      "Mosadaqa degree attestation",
      "Saudi Culture attestation",
      "Saudi Embassy attestation",
      "Apostille attestation",
      "QVP attestation",
      "Not sure yet",
    ],
    document: [
      "Degree",
      "Diploma",
      "Transcript",
      "Certificate",
      "Other",
    ],
    country: [
      "Saudi Arabia",
      "United Arab Emirates",
      "Qatar",
      "Kuwait",
      "Oman",
      "Bahrain",
      "United Kingdom",
      "Europe",
      "Canada",
      "Australia",
      "Other",
    ],
    issue: [
      "No problem",
      "Name mismatch",
      "Father’s name mismatch",
      "Spelling mistake",
      "Date-of-birth mismatch",
      "Mosadaqa or QVP query",
      "Rejected or refused",
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
          ? "Identify the missing record and ask the issuing body or the receiving organisation about a replacement or an accepted alternative before submitting."
          : a.issue === "Rejected or refused"
            ? "Work from the stated reason. Another stamp or another courier usually does not resolve a query that names a record detail."
            : a.issue === "Mosadaqa or QVP query"
              ? "Read the exact wording of the query and compare the degree, transcript, CNIC and passport details. Ask the issuing body about correction or verification before paying for another stage."
              : a.issue === "Not sure"
                ? "Describe the document and the request you received before selecting a service or paying a fee."
                : "Compare the source records. Only the issuer of the incorrect record can correct it: the university for a degree, NADRA for the identity record, DGIP for the passport.";
      path.push({ title: "First: resolve the reported issue", text: copy });
    }
    const serviceNotes = {
      "Mosadaqa degree attestation":
        "Ask the requesting organisation whether it needs Mosadaqa verification, an authenticated original, or both, and keep its wording. The education authority stage normally comes before the foreign-affairs and Saudi-side stages.",
      "Saudi Culture attestation":
        "The cultural-mission stage follows the earlier education and foreign-affairs stages for eligible documents. Confirm current submission arrangements with the mission before sending anything.",
      "Saudi Embassy attestation":
        "The Saudi embassy stage is the last attestation step on the Pakistani side. Check whether your document needs it in addition to verification, translation or an electronic submission.",
      "QVP attestation":
        "QVP is qualification verification connected with Saudi work-permit processing. It checks the academic record rather than the stamps, so record details must match before submission.",
      "Apostille attestation":
        "Check whether the Apostille Convention applies to your document, your destination and the organisation receiving it. Apostille is not the same as Saudi-side attestation.",
      "Not sure yet":
        "Confirm which service applies before paying for anything. Send the exact wording of the request you received and we will map it to the stages.",
    };
    path.push({
      title: a.service + " · what this stage involves",
      text: serviceNotes[a.service],
    });
    path.push({
      title: a.document + " · confirm the record",
      text: "Check the exact document title, the issuing body and the current record. For degrees and diplomas the awarding institution holds the record.",
    });
    path.push({
      title: "Records to compare before any stage",
      text: "Degree or certificate, transcript where required, CNIC or NICOP, passport and any written request from the receiving organisation. Differences here are the most common cause of a query.",
    });
    path.push({
      title: a.country === "Saudi Arabia" ? "Saudi-side requirement" : "Recipient in " + a.country,
      text: a.country === "Saudi Arabia"
        ? "Confirm whether the request is Mosadaqa verification, QVP, employment attestation or a combination, and whether the original or an electronic submission is expected."
        : "Confirm the accepted format, translation and any authentication route with the organisation that will use the document.",
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
    const copy = document.querySelector(".destination-copy");
    const guide = document.querySelector(".destination-guide");
    // Guidance is read from the text list already in the page: no fetch, no
    // hidden content, and identical wording for scripts, search and assistants.
    function showDestination() {
      const name = destination.value;
      const row = name
        ? document.querySelector('[data-destination-key="' + name + '"]')
        : null;
      const source = row ? row.querySelector("dd") : null;
      if (copy) {
        if (source) {
          const text = source.cloneNode(true);
          const anchor = text.querySelector("a");
          if (anchor) anchor.remove();
          copy.textContent = text.textContent.trim();
        } else {
          copy.textContent = "";
        }
      }
      if (!guide) return;
      if (name === "UAE" || name === "Saudi Arabia") {
        guide.href =
          "/countries/" + (name === "UAE" ? "uae" : "saudi-arabia") + "/";
        guide.innerHTML =
          'Explore destination <span aria-hidden="true">↗</span>';
      } else if (name) {
        guide.href = "/guides/apostille-vs-embassy-attestation/";
        guide.innerHTML =
          'Understand the routes <span aria-hidden="true">↗</span>';
      }
    }
    destination.addEventListener("change", showDestination);
    showDestination();
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
        answers.service +
        " · " +
        answers.document +
        " · " +
        answers.country +
        " · " +
        answers.issue;
      form.querySelector(".request-assessment").href =
        "/contact/#" + new URLSearchParams(answers).toString();
      const wa = form.querySelector(".request-whatsapp");
      if (wa)
        wa.href =
          wa.dataset.waBase +
          encodeURIComponent(
            "Hello SK Immigration Services. Service: " +
              answers.service +
              " | Document: " +
              answers.document +
              " | Destination: " +
              answers.country +
              " | Issue: " +
              answers.issue,
          );
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
        "I would like help with the following.\n\nService: " +
        answers.service +
        "\nDocument: " +
        answers.document +
        "\nDestination: " +
        answers.country +
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
        "mailto:Services@salaroutsourcing.com?subject=" +
        encodeURIComponent("Attestation enquiry") +
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
