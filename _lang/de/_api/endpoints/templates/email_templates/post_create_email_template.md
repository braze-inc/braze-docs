---
nav_title: "POST: E-Mail-Vorlage erstellen"
article_title: "POST: E-Mail-Vorlagen erstellen"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel enthält Details zum Braze-Endpunkt E-Mail-Vorlagen erstellen."
---
{% api %}
# E-Mail-Vorlage erstellen
{% apimethod post %}
/templates/email/create
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um E-Mail-Vorlagen auf dem Braze Dashboard zu erstellen.

Diese Vorlagen werden auf der Seite **Vorlagen & Medien** verfügbar sein. Die Antwort von diesem Endpunkt enthält ein Feld für `email_template_id`, das zur Aktualisierung der Vorlage in nachfolgenden API-Aufrufen verwendet werden kann.

Der E-Mail-Abonnementstatus der Benutzer kann mit Braze über eine RESTful API aktualisiert und abgerufen werden. Sie können die API verwenden, um eine bidirektionale Synchronisierung zwischen Braze und anderen E-Mail-Systemen oder Ihrer eigenen Datenbank einzurichten. Alle API-Anfragen werden über HTTPS gestellt.

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#5eb1fe0d-2795-474d-aaf2-c4e2977dc94b {% endapiref %}

## Voraussetzungen
Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/api_key/) mit der Berechtigung `templates.email.create`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='default' %}

## Körper der Anfrage

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

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
| --------- | ---------| --------- | ----------- |
|`template_name`|Erforderlich|String|Name Ihrer E-Mail-Vorlage.|
|`subject`|Erforderlich|String|Betreffzeile der E-Mail-Vorlage.|
|`body`|Erforderlich|String|E-Mail-Vorlagenkörper, der HTML enthalten kann.|
|`plaintext_body`|Optional|String|Eine Klartextversion des Textes der E-Mail-Vorlage.|
|`preheader`|Optional|String|E-Mail-Preheader, der in einigen Clients zur Erzeugung von Vorschauen verwendet wird.|
|`tags`|Optional|String|Die [Tags]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/) müssen bereits vorhanden sein.|
|`should_inline_css`|Optional|Boolesche|Aktiviert oder deaktiviert die Funktion `inline_css` pro Vorlage. Wenn Sie keine Angaben machen, verwendet Braze die Standardeinstellung für die App-Gruppe. Erwartet wird eines von `true` oder `false`.|
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

## Mögliche Fehler

In der folgenden Tabelle finden Sie eine Liste möglicher zurückgegebener Fehler und die damit verbundenen Schritte zur Fehlerbehebung, falls zutreffend.

| Fehler | Fehlersuche |
| --- | --- |
| Name der Vorlage ist erforderlich | Geben Sie einen Vorlagennamen ein. |
| Tags müssen ein Array sein | Tags müssen als Array von Strings formatiert werden, zum Beispiel `["marketing", "promotional", "transactional"]`. |
| Alle Tags müssen Strings sein | Stellen Sie sicher, dass Ihre Tags in Anführungszeichen (`""`) eingeschlossen sind. |
| Einige Tags konnten nicht gefunden werden | Wenn Sie bei der Erstellung einer E-Mail-Vorlage ein Tag hinzufügen möchten, muss das Tag bereits in Braze vorhanden sein. |
| E-Mail muss gültige Inhaltsblocknamen enthalten | Die E-Mail könnte Inhaltsblöcke enthalten, die in dieser Umgebung nicht vorhanden sind. |
| Ungültiger Wert für `should_inline_css`. Eine von `true` oder `false` wurde erwartet. | Dieser Parameter akzeptiert nur boolesche Werte (true oder false). Vergewissern Sie sich, dass der Wert für `should_inline_css` nicht in Anführungszeichen (`""`) eingeschlossen ist, wodurch der Wert stattdessen als String gesendet wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endapi %}
