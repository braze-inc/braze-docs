Se um [redirecionamento configurado]({{site.baseurl}}/contributing/content_management/redirecting_urls/) no arquivo de redirecionamento global (`assets/js/broken_redirect_list.js`) não estiver funcionando, verifique se há caracteres maiúsculos na string do URL. Se encontrar algum, converta-o em letras minúsculas (mesmo que o nome de arquivo correspondente no diretório `_docs` contenha caracteres maiúsculos).

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
