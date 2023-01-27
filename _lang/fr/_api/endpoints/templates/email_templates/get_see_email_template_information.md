---
nav_title: "GET : Voir les informations sur les modèles d’e-mail"
article_title: "GET : Voir les informations sur les modèles d’e-mail"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Braze Afficher les modèles d’e-mail."

---
{% api %}
# Voir les informations sur les modèles d’e-mail
{% apimethod get %}
/templates/email/info
{% endapimethod %}

Utilisez cet endpoint pour obtenir des informations sur vos modèles d’e-mail.

{% alert important %}
Les modèles construits à l’aide de l’éditeur Drag & Drop ne sont pas acceptés
{% endalert %}

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#e98d2d5b-62fe-4358-b391-9fe9e460d0ac {% endapiref %}

## Limites de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `email_template_id`  | Requis | String | Voir [Identifiant API modèle e-mail]({{site.baseurl}}/api/identifier_types/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Exemple de demande
{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/templates/email/info?email_template_id={{email_template_id}}' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

## Réponse 

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "email_template_id": (string) votre identifiant API du modèle d’e-mail,
  "template_name": (string) le nom de votre modèle d’e-mail,
  "description": (string) la description du modèle d’e-mail,
  "subject": (string) la ligne d’objet du modèle d’e-mail,
  "preheader": (optional, string) l’accroche d’e-mail utilisée pour générer des aperçus chez certains clients.,
  "body": (optional, string) le corps du modèle d’e-mail pouvant inclure du HTML,
  "plaintext_body": (optional, string) une version en texte brut du corps du modèle d’e-mail,
  "should_inline_css": (optional, boolean) si du CSS doit être inséré dans le corps du modèle ; utilise par défaut la valeur d’insertion CSS du groupe d’apps,
  "tags": (string) noms des balises,
  "created_at": (string) le moment auquel l’e-mail a été créé en ISO 8601,
  "updated_at": (string) le moment auquel l’e-mail a été mis à jour en ISO 8601
}
```

Les images de cette réponse apparaîtront dans la variable `body` comme HTML.

{% endapi %}
