function header_doc_submit(){
  window.location = base_url + '/search/?query=' + encodeURIComponent($('#header-search-form .aa-Form .aa-Input').val());
  return false;
}
$(document).ready(function () {
  autocomplete({
    container: "#header-search-form",
    panelContainer: "#header-search-panel",
    debug: algolia_debug,
    placeholder: "Search",
    plugins: [algoliaInsightsPluginHeader],
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
                    snippetEllipsisText: " ...",
                    clickAnalytics: true,
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
            var description = "";
            var title = "";
            var type = "";
            var category = "";
            var tags_list = "";
            var subname = "";
            var heading = "";

            if ("nav_title" in item) {
              title = item.nav_title.replaceUnder();
            } else {
              title = item.title.replaceUnder();
            }

            if ("article_title" in item) {
              title = item.article_title.replaceUnder();
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
            // Tag search
            for (var mp in search_color_mapping) {
              if (mp in item) {
                var i_tags = item[mp];
                if (Array.isArray(i_tags)) {
                  for (var its = 0; its < i_tags.length; its++) {
                    tags_list += '<span class="search_tags" style="background-color: ' + search_color_mapping[mp] +
                      ';">' + i_tags[its].upCaseWord().mapReplace(custom_word_mapping) + '</span>';
                  }
                }
                else {
                  tags_list += '<span class="search_tags" style="background-color: ' + search_color_mapping[mp] +
                    ';">' + i_tags.upCaseWord().mapReplace(custom_word_mapping) + '</span>';
                }
              }
            }
            // Navigational Heading
            var article_path = '';
            if ('url' in item) {
              var article_url = item['url'].split('/');
              // Remove 2 last item and first item
              article_url.pop();
              article_url.pop();
              article_url.shift();
              article_path = `<div class="article_path">${article_url.join(' > ').replaceUnder().upCaseWord().mapReplace(custom_word_mapping)}</div>`;
            }
            if ("content" in item) {
              content = item.content
                .replaceUnder()
                .replace(/<(.|\n)*?>/g, "");
            }

            if (!content && ('guide_top_text' in item)) {
              content = item.guide_top_text
                .replaceUnder()
                .replace(/<(.|\n)*?>/g, "");
            }

            if ("description" in item) {
              description = item.description
                .replaceUnder()
                .replace(/<(.|\n)*?>/g, "");
            }
            var search_msg = description || content;
            if (search_msg.length > 150) {
              search_msg = search_msg.substring(0, 150);
              search_msg += "...";
            }

            var url = item.url;
            if (heading) {
              url += "#" + string_to_slug(heading);
            }
            var resulttemplate = '<a href="' +
                base_url + url + '"><div class="title">' +
                title + '</div><div class="search_tag_header_div">' + tags_list + '</div>' + article_path + ' <div class="content">' +
                search_msg +
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
