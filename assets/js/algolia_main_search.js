function mainDocSubmit(){
  window.location = base_url + '/search/?query=' + encodeURIComponent($('#doc-search-home .aa-Form .aa-Input').val());
  return false;
}
$(document).ready(function () {
  var lab_intialized = true;
  function parseDocSearch(item){
    var content = "";
    var description = "";
    var title = "";
    var type = "";
    var category = "";
    var tags_list = "";
    var heading = "";
    lab_intialized = true;
    var result_template = '';
    if (item.__autocomplete_id) {
      result_template += '<hr />';
    }

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

    if ("headings" in item) {
      if (item["headings"]) {
        heading =
          item["headings"][item["headings"].length - 1];
      }
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

    if (search_msg.length > 200) {
      search_msg = search_msg.substring(0, 200);
      search_msg += "...";
    }
    var url = item.url;
    if (heading) {
      url += "#" + string_to_slug(heading);
    }
    result_template += '<a href="' +
        base_url + url + '"><div class="title">' +
        title + ' <div class="category">' +
        tags_list + article_path +
        '</div></div> <div class="content">' +
        search_msg +
        "</div></a>";
    return result_template;
  };
  function parseLABSearch(item){
    var description = '';
    var title = '';
    var url = '';
    var tags_list = '<span class="search_tags" style="background-color: #3accdd;">LAB</span>';
    var lab_image = "<img src='" + base_url + "/assets/img/lab.png' width='45px' /> ";
    var result_template = '';
    if (lab_intialized) {
      result_template = '<div class="lab_header">Learning at Braze ' + lab_image + '</div><hr />';
      lab_intialized = false;
    }

    if (item['category']) {
      var tags = item['category'];
      if (Array.isArray(tags)) {
        for (var its = 0; its < tags.length; its++) {
          tags_list += '<span class="search_tags" style="background-color: #3accdd;">' +
            tags[its].upCaseWord().mapReplace(custom_word_mapping) + '</span>';
        }
      }
      else {
        tags_list += '<span class="search_tags" style="background-color: #3accdd;">' +
          tags.upCaseWord().mapReplace(custom_word_mapping) + '</span>';
      }
    }


    if ("title" in item) {
      title = item.title
        .replaceUnder()
        .replace(/<(.|\n)*?>/g, "");
    }

    if ("description" in item) {
      description = item.description
        .replaceUnder()
        .replace(/<(.|\n)*?>/g, "");
    }

    if (description.length > 200) {
      description = description.substring(0, 200);
      description += "...";
    }
    var url = item.url;

    result_template += '<a href="' +
        url + '" target="_blank"><div class="title lab_title">' +
        title + ' <i class="fas fa-external-link-alt"></i> <div class="category">' +
        tags_list +
        '</div></div> <div class="content">' +
        description +
        "</div><hr /></a>";
    return result_template;
  };
  autocomplete({
    container: "#doc-search-home",
    panelContainer: "#doc-search-panel",
    debug: algolia_debug,
    plugins: [algoliaInsightsPluginMain],
    placeholder: "Search everything",
    onSubmit(e){
      var query = e.state.query;
      window.location = base_url + '/search/?query=' + encodeURIComponent(query);
    },
    classNames: {
      detachedContainer: 'algolia_detached',
      detachedOverlay: 'algolia_overlay'
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
                  indexName: algolia_doc_index,
                  query,
                  params: {
                    hitsPerPage: 4,
                    attributesToSnippet: ["description:24"],
                    snippetEllipsisText: " ...",
                    clickAnalytics: true,
                  },
                },
                {
                  indexName: algolia_lab_index,
                  query,
                  params: {
                    hitsPerPage: 2,
                    attributesToSnippet: ["description:24"],
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
              __html: '<div id="algolia_footer">' +
                '<div id="algolia-docsearch-advanced"><a href="#" onclick="return mainDocSubmit();">Advanced Search</a></div></div>',
              },
            })
          },
          item({ item, createElement }) {
            var result_template = '';
            switch(item['__autocomplete_indexName']) {
              case 'LABSearch':
                result_template = parseLABSearch(item);
                break;
              default:
                result_template = parseDocSearch(item);
                break;
            }
            return createElement("div", {
              dangerouslySetInnerHTML: {
                __html: result_template,
              },
            });
          },
        },
      }];
    },
  });
});
