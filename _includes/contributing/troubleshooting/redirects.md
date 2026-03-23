If a [redirect you set up](https://github.com/braze-inc/braze-docs/blob/develop/docs/contributing/content_management/redirecting_urls.md) in the global redirect file (`assets/js/broken_redirect_list.js`) isn't working, double-check your URL string for any uppercase characters. If you find any, convert them to lowercase (even if the corresponding filename in the `_docs` directory contains uppercase characters).

{% tabs local %}
{% tab before %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/feedback/';
```
{% endtab %}

{% tab after %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/feedback/';
```
{% endtab %}
{% endtabs %}
