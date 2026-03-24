Si una [redirección que has configurado]({{site.baseurl}}/contributing/content_management/redirecting_urls/) en el archivo de redirección global (`assets/js/broken_redirect_list.js`) no funciona, comprueba que la cadena de tu URL no contenga caracteres en mayúsculas. Si encuentras alguno, conviértelo a minúsculas (aunque el nombre del archivo correspondiente en el directorio `_docs` contenga caracteres en mayúsculas).

{% tabs local %}
{% tab before %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/contributing/home/';
```
{% endtab %}

{% tab after %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/contributing/home/';
```
{% endtab %}
{% endtabs %}
