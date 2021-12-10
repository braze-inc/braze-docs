---
nav_title: Récupération des données du profil utilisateur
article_title: Récupération des données du profil utilisateur dans les appels de contenu connectés
page_order: 5
description: "Cet article explique comment intégrer les profils des utilisateurs dans vos appels de contenu connecté et les meilleures pratiques concernant le modèle Liquid."
---

# Récupération des données du profil utilisateur dans les appels de contenu connecté

Si une réponse au contenu connecté contient des champs de profil utilisateur (à l'intérieur d'une étiquette de personnalisation Liquid), ces valeurs doivent être définies plus tôt dans le message via Liquid, avant l'appel de contenu connecté afin de rendre le mot de passe Liquid correctement. De même, le drapeau `:rerender` doit être inclus dans la requête.

{% alert note %}
Le drapeau `:rerender` est un seul niveau de profondeur, ce qui signifie qu'il ne s'appliquera pas aux balises de contenu connecté imbriquées.
{% endalert %}

Pour la personnalisation, Braze tire les champs du profil utilisateur avant de passer ce champ à Liquid—donc si la réponse du contenu connecté a des champs de profil d'utilisateur, il doit être défini au préalable.

Par exemple, s'il s'agit de l'appel de contenu connecté:
{% raw %}
```liquid
Bonjour ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
Et la réponse au contenu connecté est {% raw %}`Votre langue est ${language}`{% endraw %}, le contenu affiché dans ce scénario sera `Bonjour Jon, votre langue est`. La langue elle-même ne sera pas modélisée.

Afin de rendre le mot de passe Liquid correctement, vous devez mettre la balise {% raw %}`${language}`{%endraw%} n'importe où dans le corps, comme indiqué ci-dessous.
{%raw%}
```liquid
"Bonjour ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
N'oubliez pas que l'option du drapeau `:rerender` n'est qu'un niveau de profondeur. Si la réponse au contenu connecté a elle-même plus de balises de contenu connecté, Braze ne rendra pas ces balises supplémentaires.
{% endalert %}
