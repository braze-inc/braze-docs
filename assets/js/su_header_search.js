document.addEventListener("DOMContentLoaded", function () {
  function bindSearchForm(form) {
    if (form && !form.dataset.listenerAdded) {
      form.addEventListener("submit", function (e) {
        e.preventDefault();

        var queryInput = document.getElementById("search-box-autocomplete");
        if (queryInput && queryInput.value.trim() !== "") {
          var query = queryInput.value.trim();
          window.location.href =
            "/docs/search/?searchString=" + encodeURIComponent(query);
        } else {
          console.warn("SearchUnify input not found or empty.");
        }
      });

      form.dataset.listenerAdded = "true";
    }
  }

  const observer = new MutationObserver(() => {
    var form = document.getElementById("searchForm");
    if (form) {
      bindSearchForm(form);
    }
  });

  observer.observe(document.body, { childList: true, subtree: true });

  var initialForm = document.getElementById("searchForm");
  if (initialForm) {
    bindSearchForm(initialForm);
  }

  // 🔹 Handle placeholder + autocomplete toggle
  const input = document.getElementById("search-box-autocomplete");
  if (input) {
    input.setAttribute("placeholder", "Search Everything");
  

    input.addEventListener("focus", () => {
      input.setAttribute("placeholder", "Search Everything");
     
    });

    input.addEventListener("blur", () => {
      input.setAttribute("placeholder", "Search Everything");
      
    });
  }
});