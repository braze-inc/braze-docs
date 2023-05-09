---
nav_title: "POST : Créer un modèle d’e-mail"
article_title: "POST : Créer des modèles d’e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Créer des modèles d’e-mail."
---
{% api %}
# Créer un modèle d’e-mail
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> Utilisez cet endpoint pour créer des modèles d’e-mail sur le tableau de bord de Braze. 

Ces modèles seront disponibles sur la page **Templates & Media (Modèles et médias)**. La réponse de cet endpoint comprend un champ pour `email_template_id`, qui peut être utilisé pour mettre à jour le modèle lors des appels d’API suivants.

Le statut de l’abonnement aux e-mails des utilisateurs peut être mis à jour et récupéré via Braze à l’aide d’une API RESTful. Vous pouvez utiliser l’API pour configurer une synchronisation bidirectionnelle entre Braze et d’autres systèmes de messagerie ou votre propre base de données. Toutes les demandes d’API sont faites sur HTTPS.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "template_name": (required, string) the name of your email template,
   "subject": (required, string) the email template subject line,
   "body": (required, string) the email template body that may include HTML,
   "plaintext_body": (optional, string) a plaintext version of the email template body,
   "preheader": (optional, string) the email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) One of 'true' or 'false' is expected
 }
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`template_name`|Required|String|Nom de votre modèle d’e-mail.|
|`subject`|Required|String|Ligne Objet du modèle d’e-mail.|
|`body`|Required|String|Corps du modèle d’e-mail pouvant inclure du HTML.|
|`plaintext_body`|Optional|String|Une version en texte brut du corps du modèle d’e-mail.|
|`preheader`|Optional|String|Accroche d’e-mail utilisé pour générer des aperçus chez certains clients.|
|`tags`|Optional|String|[Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) doit déjà exister.|
|`should_inline_css`|Optional|Boolean|Active ou désactive la fonction `inline_css` par modèle. Si non renseigné, Braze utilisera le paramètre par défaut de l’AppGroup. `true` ou `false` est attendu.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}


## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## Erreurs possibles

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées, le cas échéant.

| Erreur | Résolution des problèmes |
| --- | --- |
| Le nom du modèle est obligatoire | Saisissez un nom de modèle. |
| Les balises doivent être un tableau | Les balises doivent être un tableau de chaînes de caractères, par exemple `["marketing", "promotional", "transactional"]`. |
| Toutes les balises doivent être des chaînes de caractères | Assurez-vous que vos balises sont comprises entre des guillemets (`""`). |
| Certaines balises sont introuvables | Pour ajouter une balise lors de la création d’un modèle d’e-mail, la balise doit déjà exister dans Braze. |
| L’e-mail doit comporter des noms de bloc de contenu valides | L’e-mail peut contenir des blocs de contenu qui n’existent pas dans cet environnement. |
| Valeur non valide pour `should_inline_css`. `true` ou `false` était attendu | Ce paramètre accepte uniquement les valeurs booléennes true ou false. Assurez-vous que la valeur de `should_inline_css` n’est pas comprise entre des guillemets (`""`), sinon la valeur est envoyée comme chaîne de caractères. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
