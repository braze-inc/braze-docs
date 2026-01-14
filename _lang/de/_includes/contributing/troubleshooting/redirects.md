Wenn eine [von Ihnen eingerichtete Weiterleitung]({{site.baseurl}}/contributing/content_management/redirecting_urls/) in der globalen Weiterleitungsdatei (`assets/js/broken_redirect_list.js`) nicht funktioniert, überprüfen Sie Ihren URL String auf Großbuchstaben. Wenn Sie welche finden, konvertieren Sie sie in Kleinbuchstaben (auch wenn der entsprechende Dateiname im Verzeichnis `_docs` Großbuchstaben enthält).

{% tabs local %}
{% tab vor %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/contributing/home/';
```
{% endtab %}

{% tab nach %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/contributing/home/';
```
{% endtab %}
{% endtabs %}
