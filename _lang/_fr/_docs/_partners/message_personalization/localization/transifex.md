---
nav_title: Transifex
article_title: Transifex
alias: /fr/partners/transifex/
description: "Cet article décrit le partenariat entre Braze et Transifex, une plateforme de localisation qui vous permet d'automatiser la traduction et de libérer vos équipes pour leur offrir des expériences clients brillantes."
page_tpe: partenaire
search_tag: Partenaire
---

# Transifex

> Transifex permet une localisation robuste à travers votre base d'utilisateurs, quelle que soit la langue.

L'effet de levier de l'intégration Transifex et Braze du contenu connecté, vous permettant d'inclure une chaîne source dans vos messages au lieu de lignes de mise en forme conditionnelle basée sur le langage. Cela permet d'automatiser la traduction et de libérer vos équipes pour leur permettre de réaliser de brillantes expériences clients.

## Pré-requis

| Exigences        | Origine   | Accès                                                                 | Libellé                                                                                           |
| ---------------- | --------- | --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| Compte Transifex | Transifex | [https://www.transifex.com/login/](https://www.transifex.com/signin/) | Vous devez d'abord avoir un compte Transifex pour accéder à leurs informations d'intégration SDK. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Configurer l'authentification de base

Pour configurer l'authentification de base de votre compte, accédez à la plateforme Braze, sous __Gérer les paramètres__, ouvrez l'onglet __Contenu connecté__. Ici vous fournirez les identifiants utilisés pour tous les appels de contenu connecté à Transifex.

!\[Gestion des identifiants d'authentification de base\]\[34\]

Cliquez sur __Nouveaux identifiants__, nommez votre identifiant, et ajoutez votre nom d'utilisateur et votre mot de passe pour votre compte Transifex.

!\[Création d'authentification basique\]\[35\]

### Étape 2 : Contenu connecté

L'intégration de Transifex utilise la traduction [strings API][31] de Transifex. Le cURL suivant vous permettra de voir si votre compte Transifex a des valeurs de contexte associées aux traductions. Entrez les `<PROJECT_NAME>` et `<RESOURCE_NAME>` trouvés dans votre compte Transifex.

```
curl -i -L --user username:password -X GET https://www.transifex.com/api/2/project/<PROJECT_NAME>/resource/<RESOURCE_NAME>/translation/fr/strings
```

Par exemple, si votre projet Transifex est situé à `https://www.transifex. om/appboy-3/french2/french_translationspo/`, le `project_name` sera "french2" et le `resource_name` sera "french_translationspo".

Un exemple de réponse avec un champ de contexte vide est illustré ci-dessous:

!\[Terminal response\]\[33\]{: style="max-width:60%;"}

## Exemple de message de contenu connecté

Cet exemple de code snippet utilise l'API Transifex Strings et l'attribut `language` de l'utilisateur.

{% raw %}
```
{% assign key = "<API_KEY>" %}
{% assign context = "<CONTENT>" %}
{% assign source_string = key | append: ':' | append: context %}
{% assign project = "<PROJECT_NAME>" %}
{% assigner ressource = "<RESOURCE_NAME>" %}
{% assigner source_hash = source_string | md5 %}

{% if {{${language}}} == "en" ou {{${language}}} == "it" ou {{${language}}} == "de" ou {{${language}}} == "another_language_you_support" %} %}
{% connected_content https://www. ransifex. om/api/2/project/{{project}}/resource/{{resource}}/translation/{{${language}}}/string/{{source_hash}}/ :basic_auth <Insert Basic Auth Credential Name Here> :save strings %}
{% endif %}

{% if {{strings}} ! null et {{strings.translation}} != "" et {{${language}}} ! null %}
  {{strings.translation}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}

{% alert tip %}
Vous pouvez également tirer parti de l'utilisateur {% raw %}`{{${most_recent_locale}}}`{% endraw %} si vous voulez inclure une variation basée sur la version spécifique d'un utilisateur d'une langue telle que `zh_CN` ou `pt_BR`.
{% endalert %}
[32]: {% image_buster /assets/img_archive/TransifexUI.png %} [33]: {% image_buster /assets/img_archive/terminal. ng %} [34]: {% image_buster /assets/img_archive/basic_auth_mgmt.png %} [35]: {% image_buster /assets/img_archive/basic_auth_token.png %}

[31]: https://docs.transifex.com/api/translation-strings
