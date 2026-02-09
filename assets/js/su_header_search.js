// search-form-handler.js

document.addEventListener("DOMContentLoaded", function () {
  /**
   * Bind submit + click listeners to search form
   * @param {HTMLFormElement} form
   */
  function bindSearchForm(form) {
    if (form && !form.dataset.listenerAdded) {
      const originalAction = form.getAttribute("action") || "";

      // Handle form submit
      form.addEventListener(
        "submit",
        function (e) {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch();
          return false;
        },
        true
      );

      // Handle search button click
      const searchButton = form.querySelector(".su__search_btn");
      if (searchButton) {
        searchButton.addEventListener(
          "click",
          function (e) {
            e.preventDefault();
            e.stopImmediatePropagation();
            handleSearch();
            return false;
          },
          true
        );
      }

      // Handle clear (×) button click
      const clearButton = form.querySelector(".su__input-close");
      if (clearButton) {
        clearButton.addEventListener("click", function (e) {
          e.preventDefault();
          e.stopImmediatePropagation();

          const input = form.querySelector("#search-box-autocomplete");
          if (input) {
            input.value = "";
            input.classList.remove("has-text");
            input.focus();
          }
        });
      }

      form.dataset.listenerAdded = "true";
      form.setAttribute("data-original-action", originalAction);
    }
  }

  /**
   * Handle search action
   */
  function handleSearch() {
    const queryInput = document.getElementById("search-box-autocomplete");
    const langSelect = document.getElementById("lang_select");
    const lang = langSelect ? langSelect.value : "en";

    if (queryInput && queryInput.value.trim() !== "") {
      const query = queryInput.value.trim();
      const targetUrl = `/docs/${lang}/search?searchString=${encodeURIComponent(
        query
      )}`;
      window.location.href = targetUrl;
    } else {
      console.warn("Search input not found or empty.");
      if (queryInput) queryInput.focus();
    }
  }

  /**
   * Set up placeholder, key events & has-text logic
   */
  function setupInputWatcher() {
    const input = document.getElementById("search-box-autocomplete");
    if (!input) return;

    const translations = {
      en: "Search everything",
      "pt-br": "Buscar tudo",
      ko: "전체 검색",
      fr: "Rechercher tout",
      es: "Buscar todo",
      de: "Alles durchsuchen",
      ja: "すべて検索",
    };

    const lang = document.documentElement.lang;
    const placeholderText = translations[lang] || translations.en;
    input.setAttribute("placeholder", placeholderText);

    // --- Function to toggle has-text class ---
    function toggleHasTextClass() {
      if (input.value && input.value.trim() !== "") {
        input.classList.add("has-text");
      } else {
        input.classList.remove("has-text");
      }
    }

    // --- Watch for typing or pasting ---
    input.addEventListener("input", toggleHasTextClass);
    input.addEventListener("blur", toggleHasTextClass);
    input.addEventListener("focus", toggleHasTextClass);

    // --- Handle Enter key manually ---
    input.addEventListener(
      "keypress",
      function (e) {
        if (e.key === "Enter") {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch();
          return false;
        }
      },
      true
    );

    // --- Run check immediately and periodically for autofill/preload ---
    const checkDelays = [0, 100, 300, 1000, 2000];
    checkDelays.forEach((delay) => setTimeout(toggleHasTextClass, delay));
  }

  /**
   * MutationObserver → waits for dynamic injection of searchForm or input
   */
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.addedNodes.length) {
        const form = document.getElementById("searchForm");
        if (form) bindSearchForm(form);

        const input = document.getElementById("search-box-autocomplete");
        if (input) setupInputWatcher();
      }
    });
  });

  observer.observe(document.body, {
    childList: true,
    subtree: true,
  });

  // Initial setup if already present
  const initialForm = document.getElementById("searchForm");
  if (initialForm) {
    setTimeout(() => bindSearchForm(initialForm), 100);
  }

  setupInputWatcher();

  // Override AngularJS form handling (if present)
  setTimeout(() => {
    const form = document.getElementById("searchForm");
    if (form) {
      form.removeAttribute("ng-submit");
      form.removeAttribute("data-ng-submit");
      bindSearchForm(form);
    }
  }, 500);
});
