---
nav_title: Extraction des données de profil utilisateur
article_title: Extraction des données de profil utilisateur dans les appels de contenu connectés
page_order: 5
description: "Le présent article explique comment extraire les profils d’utilisateur dans vos appels de contenu connecté et les meilleures pratiques impliquant le placage des liquides."

---

# Extraction des données de profil utilisateur dans les appels de contenu connecté

Si une réponse de Contenu connecté contient des champs de profil utilisateur (dans une balise de personnalisation liquide), ces valeurs doivent être définies plus tôt dans le message par le biais de Liquide, avant l’appel Contenu connecté afin de rendre l’amplificateur liquide correctement. De même, le `:rerender` le drapeau doit être inclus dans la demande. 

{% alert note %}
Le `:rerender` l’indicateur n’est qu’un niveau profond, ce qui signifie qu’il ne s’applique pas aux balises de contenu connecté imbriquées.
{% endalert %}

Pour la personnalisation, Braze tire les champs de profil utilisateur avant de passer ce champ au liquide, donc si la réponse du contenu connecté comporte des champs de profil utilisateur, il doit être défini au préalable. 

Par exemple, s’il s’agissait de l’appel Contenu connecté :
{% raw %}
```liquid
Bonjour ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
La réponse du contenu connecté est {% raw %}`Your language is ${language}`{% endraw %}, le contenu affiché dans ce scénario sera `Hi Jon, your language is`. La langue elle-même ne sera pas plaquée.

Pour pouvoir afficher le renvoi Liquid correctement, vous devez mettre la balise {% raw %}`${language}`{%endraw%} n’importe où dans le corps, comme vous pouvez le voir dans l’extrait de code suivant.
{%raw%}
```liquid
"Bonjour ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
Rappelez-vous que `:rerender` l’option drapeau n’est qu’un niveau profond. Si la réponse du Contenu connecté lui-même comporte davantage de balises de Contenu connecté, Braze ne représentera pas ces balises supplémentaires.
{% endalert %}
