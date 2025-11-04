document.addEventListener("DOMContentLoaded", function () {

  function bindSearchForm(container) {
    const form = container.querySelector("form");
    const queryInput = container.querySelector("#search-box-autocomplete");
    const searchButton = container.querySelector(".su__search_btn");
    const clearButton = container.querySelector(".su__input-close");
    const langSelect = document.querySelector("#lang_select");

    if (!form || form.dataset.listenerAdded) return;

    // Prevent form submit
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      e.stopImmediatePropagation();
      handleSearch(queryInput, langSelect);
    });

    // Search button click
    if (searchButton) {
      searchButton.setAttribute("type", "button");
      searchButton.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        handleSearch(queryInput, langSelect);
      });
    }

    // Enter key
    if (queryInput) {
      queryInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch(queryInput, langSelect);
        }
      });

      const translations = {
        en: "Search everything",
        "pt-br": "Buscar tudo",
        ko: "전체 검색",
        fr: "Rechercher tout",
        es: "Buscar todo",
        de: "Alles durchsuchen",
        ja: "すべて検索"
      };

      let lang = document.documentElement.lang;
      let placeholderText = translations[lang] || translations.en;
      queryInput.setAttribute("placeholder", `${placeholderText}...`);

    }

    // Clear icon click
    if (queryInput) {
      container.addEventListener("click", function (e) {
        if (e.target.closest(".su__input-close")) {
          queryInput.value = "";
          queryInput.focus();
        }
      });
    }

    form.dataset.listenerAdded = "true";
  }

  function handleSearch(queryInput, langSelect) {
    const query = queryInput ? queryInput.value.trim() : "";
    const lang = langSelect ? langSelect.value : "en";

    const targetUrl = `/docs/${lang}/search?searchString=${encodeURIComponent(query)}`;
    window.location.href = targetUrl;
  }

  // Watch for dynamic content
  const targetNode = document.querySelector("#su_main_search");
  if (targetNode) {
    const observer = new MutationObserver(() => {
      const form = targetNode.querySelector("form");
      const input = targetNode.querySelector("#search-box-autocomplete");
      if (form && input) {
        bindSearchForm(targetNode);
      }
    });

    observer.observe(targetNode, { childList: true, subtree: true });
  }
});