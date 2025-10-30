---
nav_title: Extraction des données du profil utilisateur
article_title: Obtenir des données sur le profil utilisateur dans les appels de contenu connecté
page_order: 3
description: "Cet article explique comment intégrer les profils utilisateurs dans vos appels au contenu connecté et présente les meilleures pratiques en matière de création de modèles liquides."
toc_headers: h2
---

# Extraction des données du profil utilisateur

> Cette page explique comment intégrer les profils utilisateurs dans vos appels au contenu connecté et présente les meilleures pratiques en matière de création de modèles liquides. 

## Conditions préalables

Si une réponse de contenu connecté contient des champs de profil utilisateur (dans une étiquette de personnalisation Liquid), ces valeurs doivent être définies plus tôt dans le message avec Liquid, avant l'appel de contenu connecté afin de rendre le passback Liquid correctement. De même, le drapeau `:rerender` doit être inclus dans la demande. Notez que l'indicateur `:rerender` ne s'applique qu'à un seul niveau, ce qui signifie qu'il ne s'appliquera pas aux étiquettes de contenu connecté imbriquées.

## Le "Liquid Templating" dans les appels au contenu connecté

Pour la personnalisation, Braze extrait les champs de profil utilisateur avant de transmettre ce champ à Liquid - ainsi, si la réponse de Contenu connecté comporte des champs de profil utilisateur, elle doit être définie au préalable. 

Par exemple, s'il s'agit de l'appel Contenu connecté :
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

La réponse Contenu connecté est {% raw %}`Your language is ${language}`{% endraw %}. Le contenu affiché dans cet exemple est `Hi Jon, your language is`. 

La langue elle-même ne sera pas modélisée. En effet, Braze a besoin de savoir quels champs récupérer auprès de l'utilisateur avant de lancer l'appel au contenu connecté.

{% raw %}`${language}`{% endraw %} Pour que le rendu du passback Liquid soit correct, vous devez inclure l'étiquette Liquid n'importe où dans la requête, comme le montre l'extrait de code suivant. Le préprocesseur Liquid saura récupérer l'attribut "language" de l'utilisateur pour le préparer à la modélisation de la réponse.

{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
N'oubliez pas que l'option du drapeau `:rerender` n'a qu'un seul niveau de profondeur. Si la réponse au contenu connecté comporte elle-même d'autres étiquettes de contenu connecté ou d'autres étiquettes de catalogue, Braze n'effectuera pas de nouveau le rendu de ces étiquettes supplémentaires.
{% endalert %}

## Meilleures pratiques

### Utilisez `json_escape` avec les étiquettes Liquid qui pourraient casser le format JSON

Lorsque vous utilisez `:rerender`, ajoutez le filtre `json_escape` à toutes les étiquettes Liquid qui pourraient potentiellement casser le format JSON. Si vos étiquettes Liquid contiennent des caractères qui ne respectent pas le format JSON, l'intégralité de la réponse au contenu connecté sera interprétée comme du texte et intégrée dans le message, et aucune des variables ne sera enregistrée.

Par exemple, si la propriété d'événement `message` dans l'exemple ci-dessous contient des caractères susceptibles de rompre le format JSON, ajoutez le filtre `json_escape` comme dans cet exemple :

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}