/* ============================================
   SK ATTESTATIONS SERVICES — INTERACTIONS
   ============================================ */

(function () {
  'use strict';

  /* ── Mobile Menu ── */
  const toggle = document.querySelector('[data-menu-toggle]');
  const menu = document.getElementById('mobile-menu');

  if (toggle && menu) {
    toggle.addEventListener('click', function () {
      const isOpen = toggle.getAttribute('aria-expanded') === 'true';
      toggle.setAttribute('aria-expanded', String(!isOpen));
      menu.classList.toggle('is-open', !isOpen);
      document.body.style.overflow = isOpen ? '' : 'hidden';
    });

    menu.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () {
        toggle.setAttribute('aria-expanded', 'false');
        menu.classList.remove('is-open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ── FAQ Accordion ── */
  document.querySelectorAll('.faq__question').forEach(function (btn) {
    btn.addEventListener('click', function () {
      const item = btn.closest('.faq__item');
      const isOpen = item.classList.contains('is-open');

      // Close all others
      document.querySelectorAll('.faq__item.is-open').forEach(function (openItem) {
        if (openItem !== item) {
          openItem.classList.remove('is-open');
          openItem.querySelector('.faq__question').setAttribute('aria-expanded', 'false');
        }
      });

      item.classList.toggle('is-open', !isOpen);
      btn.setAttribute('aria-expanded', String(!isOpen));
    });
  });

  /* ── Assessment Tool ── */
  const form = document.querySelector('[data-assessment-form]');
  if (!form) return;

  const steps = form.querySelectorAll('.assessment__step');
  const result = form.querySelector('[data-step="result"]');
  const bar = form.querySelector('.assessment__bar');
  const pathwayOutput = form.querySelector('#pathway-output');
  const totalSteps = 4;
  let currentStep = 1;

  function showStep(n) {
    steps.forEach(function (s) { s.hidden = true; });
    if (result) result.hidden = true;

    if (n > totalSteps) {
      const data = new FormData(form);
      generatePathway(data);
      if (result) result.hidden = false;
      if (bar) bar.style.width = '100%';
      return;
    }

    const step = form.querySelector('[data-step="' + n + '"]');
    if (step) {
      step.hidden = false;
      if (bar) bar.style.width = ((n / (totalSteps + 1)) * 100) + '%';
      currentStep = n;
    }
  }

  function generatePathway(data) {
    const doc = data.get('document');
    const country = data.get('country');
    const issue = data.get('issue');
    const steps = [];

    const pathways = {
      degree: [
        { title: 'University Verification', text: 'Your university verifies the degree or transcript record.' },
        { title: 'HEC Attestation', text: 'HEC attests the degree after online application and scrutiny.' },
        { title: 'MOFA Attestation', text: 'MOFA authenticates the HEC signature and seal.' }
      ],
      matric: [
        { title: 'Board Verification', text: 'Your board verifies the Matric or Intermediate certificate.' },
        { title: 'IBCC Attestation', text: 'IBCC attests the certificate after board verification.' },
        { title: 'MOFA Attestation', text: 'MOFA authenticates the IBCC signature and seal.' }
      ],
      birth: [
        { title: 'NADRA / Union Council Verification', text: 'NADRA or the issuing Union Council verifies the certificate.' },
        { title: 'MOFA Attestation', text: 'MOFA authenticates the issuing authority seal.' }
      ],
      marriage: [
        { title: 'Union Council / NADRA Verification', text: 'The Nikah Registrar or NADRA verifies the certificate.' },
        { title: 'MOFA Attestation', text: 'MOFA authenticates the verifying authority seal.' }
      ],
      pcc: [
        { title: 'Police Verification', text: 'Your local police station issues and verifies the PCC.' },
        { title: 'MOFA Attestation', text: 'MOFA authenticates the police authority seal.' }
      ],
      commercial: [
        { title: 'Chamber of Commerce / Notary', text: 'Commercial documents are verified by the relevant Chamber or Notary.' },
        { title: 'MOFA Attestation', text: 'MOFA authenticates the Chamber or Notary seal.' }
      ]
    };

    const base = pathways[doc] || pathways.degree;
    base.forEach(function (s, i) {
      steps.push({ number: i + 1, title: s.title, text: s.text });
    });

    if (country) {
      const hague = ['uae', 'uk', 'germany', 'italy', 'france', 'canada', 'australia', 'usa'];
      const embassy = ['saudi-arabia', 'qatar', 'kuwait'];
      const label = country.replace(/-/g, ' ').replace(/\b\w/g, function (c) { return c.toUpperCase(); });

      if (hague.indexOf(country) !== -1) {
        steps.push({
          number: steps.length + 1,
          title: 'Apostille (if applicable)',
          text: 'For ' + label + ', an Apostille from Pakistan MOFA may be sufficient. Confirm current requirements.'
        });
      } else if (embassy.indexOf(country) !== -1) {
        steps.push({
          number: steps.length + 1,
          title: 'Embassy Legalization',
          text: 'For ' + label + ', embassy or consular attestation is required after MOFA.'
        });
      }
    }

    if (issue && issue !== 'none') {
      steps.push({
        number: steps.length + 1,
        title: 'Issue Resolution Required',
        text: 'Your document has a reported issue. The resolution path depends on the specific problem. We recommend a manual document review before proceeding.'
      });
    }

    if (pathwayOutput) {
      pathwayOutput.innerHTML = steps.map(function (s, i) {
        return '<div class="pathway-step" style="animation-delay:' + (i * 0.12) + 's">' +
          '<div class="pathway-step__number">' + s.number + '</div>' +
          '<div class="pathway-step__text"><strong>' + s.title + '</strong>' + s.text + '</div>' +
          '</div>';
      }).join('');
    }
  }

  form.addEventListener('click', function (e) {
    if (e.target.closest('[data-next]')) {
      const currentFieldset = form.querySelector('[data-step="' + currentStep + '"]');
      if (currentFieldset) {
        const inputs = currentFieldset.querySelectorAll('input[required]');
        let valid = true;
        inputs.forEach(function (input) {
          if (input.type === 'radio') {
            if (!form.querySelector('input[name="' + input.name + '"]:checked')) valid = false;
          } else if (!input.value) {
            valid = false;
          }
        });
        if (!valid) return;
      }
      showStep(currentStep + 1);
    }
    if (e.target.closest('[data-back]')) {
      showStep(currentStep - 1);
    }
  });

  // Visual selection state for option cards
  form.addEventListener('change', function (e) {
    if (e.target.type === 'radio') {
      const name = e.target.name;
      form.querySelectorAll('input[name="' + name + '"]').forEach(function (input) {
        input.closest('.option-card').classList.toggle('is-selected', input.checked);
      });

      if (e.target.name === 'document') {
        setTimeout(function () { showStep(2); }, 300);
      }
    }
  });

  // Contact form basic handling
  const contactForm = document.querySelector('[data-contact-form]');
  if (contactForm) {
    contactForm.addEventListener('submit', function (e) {
      e.preventDefault();
      const btn = contactForm.querySelector('button[type="submit"]');
      const original = btn.textContent;
      btn.textContent = 'Message ready — please email us directly';
      btn.disabled = true;
      setTimeout(function () {
        btn.textContent = original;
        btn.disabled = false;
      }, 4000);
    });
  }
})();
