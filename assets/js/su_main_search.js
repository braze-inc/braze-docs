// su_main_search.js
document.addEventListener("DOMContentLoaded", function () {
  function bindSearchForm(container) {
    const form = container.querySelector("form");
    const queryInput = container.querySelector("#search-box-autocomplete");
    const searchButton = container.querySelector(".su__search_btn");
    const clearButton = container.querySelector(".su__input-close");

    if (!form || form.dataset.listenerAdded) return;

    // Prevent form submit
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      e.stopImmediatePropagation();
      handleSearch(queryInput);
    });

    // Search button click
    if (searchButton) {
      searchButton.setAttribute("type", "button");
      searchButton.addEventListener("click", function (e) {
        e.preventDefault();
        e.stopImmediatePropagation();
        handleSearch(queryInput);
      });
    }

    // Enter key
    if (queryInput) {
      queryInput.addEventListener("keypress", function (e) {
        if (e.key === "Enter") {
          e.preventDefault();
          e.stopImmediatePropagation();
          handleSearch(queryInput);
        }
      });
      queryInput.setAttribute("placeholder", "Search Everything...");
    }

    // Clear icon click
    if (queryInput) {
      // Use event delegation in case the icon is added later
      container.addEventListener("click", function (e) {
        if (e.target.closest(".su__input-close")) {
          queryInput.value = "";
          queryInput.focus(); 
        }
      });
    }

    form.dataset.listenerAdded = "true";
    
  }

  function handleSearch(queryInput) {
    if (queryInput && queryInput.value.trim() !== "") {
      const query = queryInput.value.trim();
      const targetUrl = "/docs/search/?searchString=" + encodeURIComponent(query);
      console.log("Redirecting to:", targetUrl);
      window.location.href = targetUrl;
    } else {
      console.warn("Search input empty → no redirect");
      if (queryInput) queryInput.focus();
    }
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
