---
nav_title: "POST: E-Mail-Template erstellen"
article_title: "POST: E-Mail Templates erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts E-Mail-Vorlagen erstellen von Braze."
---
{% api %}
# E-Mail-Template erstellen
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um E-Mail-Templates auf dem Braze-Dashboard zu erstellen.

Diese Templates werden auf der Seite **Templates und Medien** verfügbar sein. Die Antwort von diesem Endpunkt enthält ein Feld für `email_template_id`, das zum Update des Templates in nachfolgenden API-Aufrufen verwendet werden kann.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Voraussetzungen
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `templates.email.create`.

## Rate-Limits

{% multi_lang_include rate_limits.md endpoint='default' %}

## Anfragetext

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
   "template_name": (required, string) The name of your email template,
   "subject": (required, string) The email template subject line,
   "body": (required, string) The email template body that may include HTML,
   "plaintext_body": (optional, string) A plaintext version of the email template body,
   "preheader": (optional, string) The email preheader used to generate previews in some clients,
   "tags": (optional, Array of Strings) Tags must already exist,
   "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature is used on this template.
 }
```

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`template_name`|Erforderlich|String|Name des Templates für Ihre E-Mail.|
|`subject`|Erforderlich|String|E-Mail Template Betreffzeile.|
|`body`|Erforderlich|String|Körper einer E-Mail-Vorlage, die HTML enthalten kann.|
|`plaintext_body`|Optional|String|Eine Klartextversion des Body der E-Mail-Vorlage.|
|`preheader`|Optional|String|Ein Preheader für E-Mails, der in einigen Clients zur Erstellung von Vorschauen verwendet wird.|
|`tags`|Optional|String|[Tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) müssen bereits existieren.|
|`should_inline_css`|Optional|Boolesch|Aktiviert oder deaktiviert das Feature `inline_css` pro Template. Wenn Sie keine Angaben machen, verwendet Braze die Standard-Einstellung für die App-Gruppe. Erwartet wird eines von `true` oder `false`.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }


## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/create' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "template_name": "email_template_name",
  "subject": "Welcome to my email template!",
  "body": "This is the text within my email body and https://www.braze.com/ here is a link to Braze.com.",
  "plaintext_body": "This is the text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "My preheader is pretty cool.",
  "tags": ["Tag1", "Tag2"]
}'
```

## Beispielhafte Antwort

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": "232b6d29-7e41-4106-a0ab-1c4fe915d701",
  "message": "success"
}
```

## Fehlersuche

In der folgenden Tabelle sind die möglichen zurückgegebenen Fehler und die dazugehörigen Schritte zur Fehlerbehebung aufgelistet, falls zutreffend.

| Fehler | Fehlersuche |
| --- | --- |
| Template-Name ist erforderlich | Geben Sie einen Template-Namen ein. |
| Tags müssen ein Array sein | Tags müssen als String-Array formatiert werden, zum Beispiel `["marketing", "promotional", "transactional"]`. |
| Alle Tags müssen Strings sein | Achten Sie darauf, dass Ihre Tags in Anführungszeichen (`""`) eingeschlossen sind. |
| Einige Tags konnten nicht gefunden werden | Wenn Sie beim Erstellen einer E-Mail-Vorlage einen Tag hinzufügen möchten, muss dieser bereits in Braze vorhanden sein. |
| E-Mails müssen gültige Content-Block-Namen haben | Die E-Mail könnte Content-Blöcke enthalten, die in dieser Umgebung nicht vorhanden sind. |
| Ungültiger Wert für `should_inline_css`. Eine von `true` oder `false` wurde erwartet. | Dieser Parameter akzeptiert nur boolesche Werte (true oder false). Vergewissern Sie sich, dass der Wert für `should_inline_css` nicht in Anführungszeichen (`""`) eingeschlossen ist, wodurch der Wert stattdessen als String gesendet wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
