function header_doc_submit(){
  window.location = base_url + '/search/?query=' + encodeURIComponent($('#header-search-form .aa-Form .aa-Input').val());
  return false;
}
$(document).ready(function () {
  function string_to_slug(str) {
    if (str) {
      str = str.toLowerCase().replace(/\s/g, '-').replace(/[^\w-]/g, '');
    }
    return str;
  }

  autocomplete({
    container: "#header-search-form",
    panelContainer: "#header-search-panel",
    debug: algolia_debug,
    placeholder: "Search",
    detachedMediaQuery: 'none',
    onSubmit(e){
      var query = e.state.query;
      window.location = base_url + '/search/?query=' + encodeURIComponent(query);
    },
    getSources() {
      return [{
          sourceId: "querySuggestions",
          getItemInputValue: ({ item }) => item.query,
          getItems({ query }) {
            return getAlgoliaResults({
              searchClient,
              queries: [
                {
                  indexName: "DocSearch",
                  query,
                  params: {
                    hitsPerPage: 5,
                    attributesToSnippet: ["description:12"],
                    snippetEllipsisText: " ..."
                  },
                },
              ],
            });
          },
          getItemUrl({ item }) {
           return base_url + item.url;
         },
         templates: {
           noResults({createElement}) {
             return createElement("div", {
               dangerouslySetInnerHTML: {
                 __html: '<div class="no_results">No results were found with your current search. Try to change the search query.</div>',
                 __id: 'abc'
                 },
               })
          },
          footer({createElement}){ return createElement("div", {
            dangerouslySetInnerHTML: {
              __html: '<div id="algolia_headersearch_footer">' +
              '<div id="algolia-headersearch-advanced"><a href="#" onclick="return header_doc_submit();">Advanced Search</a></div></div>',
              },
            })
          },
          item({ item, createElement }) {
            var content = "";
            var title = "";
            var type = "";
            var category = "";
            var platform = "";
            var subname = "";
            var heading = "";

            if ("nav_title" in item) {
              title = item.nav_title.replaceUnder();
            } else {
              title = item.title.replaceUnder();
            }
            if ("type" in item) {
              type = item.type.replaceUnder().upCaseWord();
            }
            if ("category" in item) {
              category = item.category.replaceUnder();
            }

            if ("platform" in item) {
              platform = item.platform.replaceUnder();
            }
            if ("headings" in item) {
              if (item["headings"]) {
                heading =
                  item["headings"][item["headings"].length - 1];
              }
            }
            if (platform || category) {
              subname = "(" + type + ": " + platform;
              if (platform) {
                subname += " - ";
              }
              subname += category.upCaseWord() + ")";
            }
            if ("content" in item._highlightResult) {
              if ("value" in item._highlightResult.content) {
                content = item._highlightResult.content.value
                  .replaceUnder()
                  .replace(/<(.|\n)*?>/g, "");
              }
            }

            if (content.length > 150) {
              content = content.substring(0, 150);
              content += "...";
            }
            var url = item.url;
            if (heading) {
              url += "#" + string_to_slug(heading);
            }
            var resulttemplate = '<a href="' +
                base_url + url + '"><div class="title">' +
                title + ' <div class="category">' +
                subname.replace(/\_/g, " ") +
                '</div></div> <div class="content">' +
                content +
                "</div><hr /></a>";

            return createElement("div", {
              dangerouslySetInnerHTML: {
                __html: resulttemplate,
              },
            });
          },
        },
      }];
    },
  });

  $('#header-search-form .aa-Form .aa-Input').focusin(function(e){
      $('#header_nav').addClass('search_focus');
  });
  $('#header-search-form .aa-Form .aa-Input').focusout(function(e){
      $('#header_nav').removeClass('search_focus');
  });
});
