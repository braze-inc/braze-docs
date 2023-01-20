---
nav_title: "POST : Mettre à jour le modèle d’e-mail"
article_title: "POST : Mettre à jour les modèles d’e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: référence
description: "Cet article présente en détail l’endpoint Braze Mettre à jour les modèles d’e-mail."

---
{% api %}
# Mettre à jour les modèles d’e-mail existants
{% apimethod post %}
/templates/email/update
{% endapimethod %}

Utilisez cet endpoint pour mettre à jour des modèles d’e-mail sur le tableau de bord de Braze. Vous pouvez accéder à un `email_template_id` de modèle d’e-mail en allant sur la page **Templates & Media (Modèles et médias)**. L’[endpoint Créer un modèle d’e-mail]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) renvoie également une référence `email_template_id`.

Tous les champs autres que l’`email_template_id` sont facultatifs, mais vous devez spécifier au moins un champ à mettre à jour.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email_template_id": (required, string) votre identifiant API du modèle d’e-mail,
  "template_name": (optional, string) le nom de votre modèle d’e-mail,
  "subject": (optional, string) la ligne d’objet du modèle d’e-mail,
  "body": (optional, string) le corps du modèle d’e-mail pouvant inclure du HTML,
  "plaintext_body": (optional, string) une version en texte brut du corps du modèle d’e-mail,
  "preheader": (optional, string) l’accroche d’e-mail utilisée pour générer des aperçus chez certains clients,
  "tags": (optional, array of Strings) tags doit déjà exister.,
  "should_inline_css": (optional, Boolean) une valeur « vrai » ou « faux » est attendue
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
| --------- | ---------| --------- | ----------- |
|`email_template_id`| Requis |String|Votre [identifiant API du modèle d’e-mail]({{site.baseurl}}/api/identifier_types/).|
|`template_name`|Facultatif|String|Nom de votre modèle d’e-mail|
|`subject`|Facultatif|String|Ligne Objet du modèle d’e-mail.|
|`body`|Facultatif|String|Corps du modèle d’e-mail pouvant inclure du HTML.|
|`plaintext_body`|Facultatif|String|Une version en texte brut du corps du modèle d’e-mail.|
|`preheader`|Facultatif|String|Accroche d’e-mail utilisée pour générer des aperçus chez certains clients.|
|`tags`|Facultatif|String|[Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) doit déjà exister.|
|`should_inline_css`|Facultatif|Boolean|Active ou désactive la fonction `inline_css` par modèle. Si non renseigné, Braze utilisera le paramètre par défaut de l’AppGroup. `true` ou `false` est attendu.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Lettre d’information hebdomadaire",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "Il s’agit du texte du corps de mon e-mail et voici un lien vers hhttps://www.braze.com/.",
  "preheader": "We want you to have the best looks this Summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## Erreurs possibles

Le tableau suivant répertorie les erreurs renvoyées possibles et les étapes de résolution des problèmes associées, le cas échéant.

| Erreur | Résolution des problèmes |
| --- | --- |
| Le nom du modèle est obligatoire | Saisissez un nom de modèle. |
| Les balises doivent être un tableau | Les balises doivent être un array de strings, par exemple `["marketing", "promotional", "transactional"]`. |
| Toutes les balises doivent être des chaînes de caractères | Assurez-vous que vos balises sont comprises entre des guillemets (`""`). |
| Certaines balises sont introuvables | Pour ajouter une balise lors de la création d’un modèle d’e-mail, la balise doit déjà exister dans Braze. |
| Valeur non valide pour `should_inline_css`. `true` ou `false` est attendu | Ce paramètre accepte uniquement les valeurs booléennes (vrai ou faux). Assurez-vous que la valeur de `should_inline_css` n’est pas comprise entre des guillemets (`""`), sinon la valeur est envoyée comme chaîne de caractères. |
{: .reset-td-br-1 .reset-td-br-2}

{% endapi %}
