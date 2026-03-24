Si une [redirection que vous avez définie]({{site.baseurl}}/contributing/content_management/redirecting_urls/) dans le fichier de redirection global (`assets/js/broken_redirect_list.js`) ne fonctionne pas, vérifiez que votre chaîne de caractères URL ne contient pas de majuscules. Si vous en trouvez, convertissez-les en minuscules (même si le nom de fichier correspondant dans le répertoire `_docs` contient des caractères majuscules).

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
