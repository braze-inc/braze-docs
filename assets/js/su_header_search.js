// search-form-handler.js

document.addEventListener("DOMContentLoaded", function () {
  /**
   * Bind submit + click listeners to search form
   * @param {HTMLFormElement} form
   */
  function bindSearchForm(form) {
    if (form && !form.dataset.listenerAdded) {
      const originalAction = form.getAttribute('action') || '';
      
      form.addEventListener("submit", function (e) {
        e.preventDefault();
        e.stopImmediatePropagation(); 
        handleSearch();
        return false;
      }, true); 

      const searchButton = form.querySelector(".su__search_btn");
      if (searchButton) {
        searchButton.addEventListener("click", function (e) {
          e.preventDefault();
          e.stopImmediatePropagation(); 
          handleSearch(); 
          return false;
        }, true); 
      }

      form.dataset.listenerAdded = "true";
      form.setAttribute('data-original-action', originalAction);
    }
  }

  function handleSearch() {
    const queryInput = document.getElementById("search-box-autocomplete");
    const langSelect = document.getElementById("lang_select");

    if (queryInput && queryInput.value.trim() !== "") {
      const query = queryInput.value.trim();
      const lang = langSelect ? langSelect.value : "en"; 
      const targetUrl = `/docs/${lang}/search?searchString=${encodeURIComponent(query)}`;
      console.log("Redirecting to:", targetUrl);
      
      window.location.href = targetUrl;
    } else {
      console.warn("Search input not found or empty.");
      if (queryInput) queryInput.focus();
    }
  }

  /**
   * MutationObserver → waits for dynamic injection of searchForm
   */
  const observer = new MutationObserver((mutations) => {
    mutations.forEach((mutation) => {
      if (mutation.addedNodes.length) {
        const form = document.getElementById("searchForm");
        if (form) bindSearchForm(form);
      }
    });
  });

  observer.observe(document.body, { 
    childList: true, 
    subtree: true,
    attributes: false,
    characterData: false
  });

  // Initial binding if form already exists
  const initialForm = document.getElementById("searchForm");
  if (initialForm) {
    setTimeout(() => bindSearchForm(initialForm), 100);
  }

  /**
   * Placeholder & key events
   */
  const input = document.getElementById("search-box-autocomplete");

  if (input) {
    const placeholderText = "Search Everything";
    input.setAttribute("placeholder", placeholderText);
  
    function toggleWidth(input) {
      if (input.value.trim() !== "") {
        input.classList.add("has-text"); 
        input.focus(); 
      } else {
        input.classList.remove("has-text"); 
      }
    }
  
    input.addEventListener("input", () => toggleWidth(input));
    input.addEventListener("blur", () => toggleWidth(input));
  
    input.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        e.stopImmediatePropagation();
        handleSearch();
        return false;
      }
    }, true);
  }
  
  // Override AngularJS form handling
  setTimeout(() => {
    const form = document.getElementById("searchForm");
    if (form) {
      form.removeAttribute('ng-submit');
      form.removeAttribute('data-ng-submit');
      bindSearchForm(form);
    }
  }, 500);
});
