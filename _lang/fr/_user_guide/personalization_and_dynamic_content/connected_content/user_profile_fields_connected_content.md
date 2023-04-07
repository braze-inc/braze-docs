---
nav_title: Extraction des données de profil utilisateur
article_title: Extraction des données de profil utilisateur dans les appels de contenu connectés
page_order: 5
description: "Le présent article explique comment extraire les profils d’utilisateur dans vos appels de contenu connecté et les bonnes pratiques impliquant la modélisation de Liquid."

---

# Extraction des données de profil utilisateur dans les appels de contenu connecté

Si une réponse de Contenu connecté contient des champs de profil utilisateur (dans une balise de personnalisation Liquid), ces valeurs doivent être définies plus tôt dans le message par le biais de Liquid, avant l’appel Contenu connecté afin d’interpréter correctement le retour Liquid. De même, l’indicateur `:rerender` doit être inclus dans la requête. 

{% alert note %}
L’indicateur `:rerender` a une profondeur d’un seul niveau, ce qui signifie qu’il ne s’applique pas aux balises de contenu connecté imbriquées.
{% endalert %}

Pour la personnalisation, Braze extrait les champs de profil utilisateur avant de transmettre ce champ au Liquid. Donc si la réponse du contenu connecté comporte des champs de profil utilisateur, il doit être défini au préalable. 

Par exemple, s’il s’agissait de l’appel de Contenu connecté :
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
La réponse du contenu connecté est {% raw %}`Your language is ${language}`{% endraw %}, le contenu affiché dans ce scénario sera `Hi Jon, your language is`. La langue elle-même ne sera pas modélisée.

Afin d’interpréter correctement le retour Liquid, vous devez placer la balise {% raw %}Balise `${language}`{%endraw%} n’importe où dans le corps, comme indiqué dans l’extrait de code suivant.
{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
Rappelez-vous que l’option d’indicateur `:rerender` a une profondeur d’un seul niveau. Si la réponse du Contenu connecté lui-même comporte davantage de balises de Contenu connecté, Braze n’interprètera pas à nouveau ces balises supplémentaires.
{% endalert %}
