---
nav_title: Extraction des données de profil utilisateur
article_title: Extraction des données de profil utilisateur dans les appels de contenu connectés
page_order: 5
description: "Le présent article explique comment extraire les profils d’utilisateur dans vos appels de contenu connecté et les bonnes pratiques impliquant la modélisation de Liquid."

---

# Extraire des données de profil utilisateur

> Cette page explique comment intégrer les profils utilisateurs dans vos appels au contenu connecté et présente les meilleures pratiques en matière de création de modèles liquides. 

Si une réponse de contenu connecté contient des champs de profil utilisateur (dans une étiquette de personnalisation Liquid), ces valeurs doivent être définies plus tôt dans le message avec Liquid, avant l'appel de contenu connecté afin de rendre le passback Liquid correctement. De même, l’indicateur `:rerender` doit être inclus dans la requête. Prenez en compte le fait que l’indicateur `:rerender` a une profondeur d’un seul niveau, ce qui signifie qu’il ne s’applique pas aux balises de contenu connecté imbriquées.

Pour la personnalisation, Braze extrait les champs de profil utilisateur avant de transmettre ce champ au Liquid. Donc si la réponse du contenu connecté comporte des champs de profil utilisateur, il doit être défini au préalable. 

Par exemple, s’il s’agissait de l’appel de Contenu connecté :
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}
Et si la réponse du contenu connecté est {% raw %}`Your language is ${language}`{% endraw %}, le contenu affiché dans ce scénario sera `Hi Jon, your language is`. La langue elle-même ne sera pas modélisée. En effet, Braze doit savoir quels champs récupérer de l’utilisateur avant d’effectuer l’appel de contenu connecté.

Pour pouvoir afficher le renvoi Liquid correctement, vous devez insérer la balise {% raw %}`${language}`{%endraw%} n’importe où dans la demande, comme illustré dans l’extrait de code suivant. Le préprocesseur Liquid saura qu’il doit obtenir l’attribut « langue » de l’utilisateur pour l’avoir à disposition pour modéliser la réponse.
{%raw%}
```liquid
"Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}
{% alert important %}
Rappelez-vous que l’option d’indicateur `:rerender` a une profondeur d’un seul niveau. Si la réponse au contenu connecté comporte elle-même d'autres étiquettes de contenu connecté ou d'autres étiquettes de catalogue, Braze n'effectuera pas de nouveau le rendu de ces étiquettes supplémentaires.
{% endalert %}

## Bonnes pratiques

### Utilisez `json_escape` avec les étiquettes Liquid qui pourraient casser le format JSON

Lorsque vous utilisez `:rerender`, ajoutez le filtre `json_escape` à toutes les étiquettes Liquid qui pourraient potentiellement casser le format JSON. Si vos étiquettes Liquid contiennent des caractères qui ne respectent pas le format JSON, l'intégralité de la réponse au contenu connecté sera interprétée comme du texte et intégrée dans le message, et aucune des variables ne sera enregistrée.

Par exemple, si la propriété d'événement `message` dans l'exemple ci-dessous contient des caractères susceptibles de casser le format JSON, ajoutez le filtre `json_escape` comme dans cet exemple :

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}