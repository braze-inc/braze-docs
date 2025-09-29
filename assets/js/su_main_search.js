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

    if (queryInput && queryInput.value.trim() !== "") {
      const query = queryInput.value.trim();
      // Make sure we're redirecting to the correct URL
      const targetUrl = "/docs/su_search/?searchString=" + encodeURIComponent(query);

      console.log("Redirecting to:", targetUrl);
      
      // ✅ Always redirect when search triggered
      window.location.href = targetUrl;
    } else {
      console.warn("SearchUnify input not found or empty.");
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
    // Wait a bit to ensure AngularJS has finished processing
    setTimeout(() => bindSearchForm(initialForm), 100);
  }

  /**
   * Placeholder & key events
   */
  const input = document.getElementById("search-box-autocomplete");
  if (input) {
    const placeholderText = "Search Everything......";
    input.setAttribute("placeholder", placeholderText);

    input.addEventListener("focus", () => {
      input.setAttribute("placeholder", placeholderText);
    });

    input.addEventListener("blur", () => {
      input.setAttribute("placeholder", placeholderText);
    });

    // Enter key also triggers redirect - use capture phase
    input.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        e.stopImmediatePropagation(); // Prevent other handlers
        handleSearch();
        return false;
      }
    }, true); // Use capture phase
  }
  
  // Additional safety: override AngularJS form handling
  setTimeout(() => {
    const form = document.getElementById("searchForm");
    if (form) {
      // Remove any ng-submit or other Angular directives that might interfere
      form.removeAttribute('ng-submit');
      form.removeAttribute('data-ng-submit');
      
      // Re-bind our handlers
      bindSearchForm(form);
    }
  }, 500);
});
