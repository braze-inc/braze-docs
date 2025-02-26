---
nav_title: "POST: E-Mail-Vorlage aktualisieren"
article_title: "POST: E-Mail-Vorlagen aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze Endpunkts E-Mail-Vorlage aktualisieren."

---
{% api %}
# Vorhandene E-Mail-Vorlagen aktualisieren
{% apimethod post %}
/templates/email/update
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um E-Mail-Vorlagen auf dem Braze Dashboard zu aktualisieren.

Sie können auf die `email_template_id` einer E-Mail-Vorlage zugreifen, indem Sie auf der Seite **Vorlagen & Medien** zu ihr navigieren. Der [Endpunkt E-Mail-Vorlage erstellen]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/) gibt ebenfalls eine `email_template_id` Referenz zurück.

Alle Felder außer dem `email_template_id` sind optional, aber Sie müssen mindestens ein Feld angeben, das Sie aktualisieren möchten.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#afb25494-3350-458d-932d-5bf4220049fa {% endapiref %}

## Voraussetzungen
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `templates.email.update`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Körper der Anfrage

```
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "email_template_id": (required, string) Your email template's API Identifier,
  "template_name": (optional, string) The name of your email template,
  "subject": (optional, string) The email template subject line,
  "body": (optional, string) The email template body that may include HTML,
  "plaintext_body": (optional, string) A plaintext version of the email template body,
  "preheader": (optional, string) The email preheader used to generate previews in some clients,
  "tags": (optional, array of Strings) Tags must already exist,
  "should_inline_css": (optional, Boolean) If `true`, the `inline_css` feature will be applied to the template.
}
```

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`email_template_id`| Erforderlich |String|[Die API-Kennung]({{site.baseurl}}/api/identifier_types/) Ihrer [E-Mail-Vorlage]({{site.baseurl}}/api/identifier_types/).|
|`template_name`|Optional|String|Name Ihrer E-Mail-Vorlage.|
|`subject`|Optional|String|Betreffzeile der E-Mail-Vorlage.|
|`body`|Optional|String|E-Mail-Vorlagenkörper, der HTML enthalten kann.|
|`plaintext_body`|Optional|String|Eine Klartextversion des Textes der E-Mail-Vorlage.|
|`preheader`|Optional|String|E-Mail-Preheader, der in einigen Clients zur Erzeugung von Vorschauen verwendet wird.|
|`tags`|Optional|String|Die [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) müssen bereits vorhanden sein.|
|`should_inline_css`|Optional|Boolesche|Aktiviert oder deaktiviert die Funktion `inline_css` pro Vorlage. Wenn nicht angegeben, verwendet Braze die Standardeinstellung für die AppGroup. Erwartet wird eines von `true` oder `false`.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfrage
```
curl --location --request POST 'https://rest.iad-01.braze.com/templates/email/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "email_template_id": "email_template_id",
  "template_name": "Weekly Newsletter",
  "subject": "This Week'\''s Styles",
  "body": "Check out this week'\''s digital lookbook to inspire your outfits. Take a look at https://www.braze.com/",
  "plaintext_body": "This is the updated text within my email body and here is a link to https://www.braze.com/.",
  "preheader": "We want you to have the best looks this summer",
  "tags": ["Tag1", "Tag2"]
}'
```

## Fehlersuche

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die damit verbundenen Schritte zur Fehlerbehebung, falls zutreffend.

| Fehler | Fehlersuche |
| --- | --- |
| Name der Vorlage ist erforderlich | Geben Sie einen Vorlagennamen ein. |
| Tags müssen ein Array sein | Tags müssen als Array von Strings formatiert werden, zum Beispiel `["marketing", "promotional", "transactional"]`. |
| Alle Tags müssen Strings sein | Stellen Sie sicher, dass Ihre Tags in Anführungszeichen (`""`) eingeschlossen sind. |
| Einige Tags konnten nicht gefunden werden | Wenn Sie bei der Erstellung einer E-Mail-Vorlage ein Tag hinzufügen möchten, muss das Tag bereits in Braze vorhanden sein. |
| Ungültiger Wert für `should_inline_css`. Eine von `true` oder `false` wurde erwartet. | Dieser Parameter akzeptiert nur boolesche Werte (true oder false). Vergewissern Sie sich, dass der Wert für `should_inline_css` nicht in Anführungszeichen (`""`) eingeschlossen ist, wodurch der Wert stattdessen als String gesendet wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
