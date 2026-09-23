(() => {
  "use strict";
  const root = document.documentElement;
  function savePreference(key, value) {
    try {
      localStorage.setItem(key, value);
    } catch (_) {}
  }
  const themeButton = document.querySelector("[data-theme-toggle]");
  function themeLabel() {
    const light = root.dataset.theme === "light";
    themeButton?.setAttribute("aria-pressed", String(light));
    themeButton?.setAttribute(
      "aria-label",
      light ? "Switch to dark theme" : "Switch to light theme",
    );
  }
  themeLabel();
  themeButton?.addEventListener("click", () => {
    root.dataset.theme = root.dataset.theme === "light" ? "dark" : "light";
    savePreference("sk-theme", root.dataset.theme);
    themeLabel();
  });
  const motionButton = document.querySelector("[data-motion-toggle]");
  const reduced = matchMedia("(prefers-reduced-motion: reduce)");
  function motionLabel() {
    const paused = root.dataset.motion === "paused" || reduced.matches;
    if (!motionButton) return;
    motionButton.setAttribute("aria-pressed", String(paused));
    motionButton.textContent = reduced.matches
      ? "Reduced motion enabled"
      : paused
        ? "Resume decorative motion"
        : "Pause decorative motion";
    motionButton.disabled = reduced.matches;
  }
  motionLabel();
  reduced.addEventListener("change", motionLabel);
  motionButton?.addEventListener("click", () => {
    root.dataset.motion =
      root.dataset.motion === "paused" ? "running" : "paused";
    savePreference("sk-motion", root.dataset.motion);
    motionLabel();
  });
  const menuButton = document.querySelector("[data-menu-toggle]");
  const menu = document.querySelector("#mobileMenu");
  function closeMenu(focus = false) {
    if (!menuButton || !menu) return;
    menu.hidden = true;
    menu.classList.remove("open");
    menuButton.setAttribute("aria-expanded", "false");
    menuButton.setAttribute("aria-label", "Open menu");
    if (focus) menuButton.focus();
  }
  menuButton?.addEventListener("click", () => {
    const open = menuButton.getAttribute("aria-expanded") !== "true";
    menu.hidden = !open;
    menu.classList.toggle("open", open);
    menuButton.setAttribute("aria-expanded", String(open));
    menuButton.setAttribute("aria-label", open ? "Close menu" : "Open menu");
  });
  document.addEventListener("keydown", (e) => {
    if (e.key === "Escape" && menu && !menu.hidden) closeMenu(true);
  });
  document.addEventListener("click", (e) => {
    if (!e.target.closest(".nav, .mobile-menu")) closeMenu();
  });
  menu?.addEventListener("click", (e) => {
    if (e.target.closest("a")) closeMenu();
  });
  matchMedia("(min-width:951px)").addEventListener("change", () => closeMenu());

  document.querySelectorAll(".tracker").forEach((tracker) => {
    tracker.querySelectorAll("[data-stage]").forEach((button) => {
      button.addEventListener("click", () => {
        tracker.querySelectorAll("[data-stage]").forEach((b) => {
          b.classList.toggle("active", b === button);
          b.setAttribute("aria-pressed", String(b === button));
        });
        tracker.querySelector(".track-detail h3").textContent =
          button.dataset.title;
        tracker.querySelector(".track-detail p").textContent =
          button.dataset.detail;
      });
    });
  });
  const search = document.querySelector("[data-blog-search]");
  const filter = document.querySelector("[data-blog-filter]");
  function filterBlogs() {
    const query = search.value.trim().toLocaleLowerCase();
    let count = 0;
    document.querySelectorAll("[data-blog-category]").forEach((card) => {
      const match =
        (filter.value === "All" ||
          card.dataset.blogCategory === filter.value) &&
        card.textContent.toLocaleLowerCase().includes(query);
      card.hidden = !match;
      if (match) count++;
    });
    document.querySelector(".filter-status").textContent =
      count + (count === 1 ? " article" : " articles");
    document.querySelector(".empty-message").hidden = count > 0;
  }
  search?.addEventListener("input", filterBlogs);
  filter?.addEventListener("change", filterBlogs);
  document.querySelectorAll("[data-faq-filter]").forEach((button) => {
    button.addEventListener("click", () => {
      document
        .querySelectorAll("[data-faq-filter]")
        .forEach((b) => b.setAttribute("aria-pressed", String(b === button)));
      document.querySelectorAll("[data-faq-category]").forEach((item) => {
        item.hidden =
          button.dataset.faqFilter !== "All" &&
          item.dataset.faqCategory !== button.dataset.faqFilter;
      });
    });
  });
  const checker = document.querySelector("[data-checker]");
  if (checker && window.SKChecker) {
    checker.noValidate = true;
    const fields = [...checker.querySelectorAll("[data-step]")];
    const next = checker.querySelector("[data-next]");
    const back = checker.querySelector("[data-back]");
    const error = checker.querySelector(".checker-error");
    const result = checker.querySelector(".checker-result");
    let step = 0;
    function showStep(n) {
      step = n;
      fields.forEach((field, i) => {
        field.hidden = i !== n;
        field.disabled = i !== n;
      });
      checker.querySelector("[data-step-name]").textContent = [
        "Document",
        "Destination",
        "Issue",
      ][n];
      checker.querySelector("[data-step-count]").textContent =
        `Step ${n + 1} of 3`;
      checker.querySelectorAll(".est-step-pip").forEach((pip, i) => {
        pip.classList.toggle("active", i === n);
        pip.classList.toggle("done", i < n);
      });
      checker.querySelector(".est-nav").hidden = false;
      result.hidden = true;
      back.hidden = n === 0;
      checker.querySelector("[data-local]").hidden = n !== 0;
      next.textContent = n === 2 ? "See my checklist" : "Continue";
      error.textContent = "";
      fields[n].querySelector("legend").focus();
    }
    checker.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!fields[step].querySelector("input:checked")) {
        error.textContent = "Choose an option to continue.";
        fields[step].querySelector("input").focus();
        return;
      }
      if (step < 2) {
        showStep(step + 1);
        return;
      }
      const answers = {};
      fields.forEach((field) => {
        const input = field.querySelector("input:checked");
        answers[input.name] = input.value;
      });
      const list = checker.querySelector(".result-steps");
      list.replaceChildren();
      window.SKChecker.assess(answers).forEach((item) => {
        const li = document.createElement("li"),
          title = document.createElement("strong"),
          text = document.createElement("p");
        title.textContent = item.title;
        text.textContent = item.text;
        li.append(title, text);
        list.append(li);
      });
      checker.querySelector(".result-summary").textContent =
        Object.values(answers).join(" · ");
      checker.querySelector("[data-case-contact]").href =
        "/contact/#" + new URLSearchParams(answers);
      fields.forEach((field) => {
        field.hidden = true;
        field.disabled = true;
      });
      checker.querySelector(".est-nav").hidden = true;
      error.textContent = "";
      result.hidden = false;
      checker.querySelector("[data-step-name]").textContent =
        "Preparation checklist";
      checker.querySelector("[data-step-count]").textContent = "Complete";
      checker.querySelectorAll(".est-step-pip").forEach((pip) => {
        pip.classList.remove("active");
        pip.classList.add("done");
      });
      result.querySelector("h2").focus();
    });
    back.addEventListener("click", () => showStep(Math.max(0, step - 1)));
    checker.addEventListener("change", () => {
      error.textContent = "";
    });
    checker.querySelector("[data-reset]").addEventListener("click", () => {
      checker.reset();
      showStep(0);
    });
  }
  const enquiry = document.querySelector("[data-enquiry]");
  if (enquiry && window.SKChecker) {
    const data = window.SKChecker.clean(
      Object.fromEntries(new URLSearchParams(location.hash.slice(1))),
    );
    if (Object.keys(data).length === 3) {
      enquiry.elements.message.value = `Hello, I would like independent document guidance.\n\nDocument: ${data.document}\nDestination: ${data.destination}\nIssue: ${data.issue}\n\nPlease help me clarify the current requirements and what preparation assistance is available.`;
      history.replaceState(null, "", location.pathname);
    }
    const status = enquiry.querySelector(".status");
    const ready = enquiry.querySelector("[data-contact-ready]");
    enquiry.addEventListener("submit", (e) => {
      e.preventDefault();
      if (!enquiry.reportValidity()) return;
      const message = enquiry.elements.message.value.trim();
      if (!message) {
        status.textContent =
          "Describe your question before preparing a message.";
        return;
      }
      const whatsapp = enquiry.querySelector("[data-whatsapp-draft]");
      const email = enquiry.querySelector("[data-email-draft]");
      whatsapp.href =
        whatsapp.href.split("?")[0] + "?text=" + encodeURIComponent(message);
      email.href =
        email.href.split("?")[0] +
        "?subject=" +
        encodeURIComponent("Document guidance enquiry") +
        "&body=" +
        encodeURIComponent(message);
      ready.hidden = false;
      status.textContent =
        "Your links are ready. Nothing has been sent. Choose a channel to review your message.";
    });
    enquiry.addEventListener("input", () => {
      ready.hidden = true;
      status.textContent = "";
    });
  }
})();
