---
nav_title: Mai
page_order: 8
noindex: true
page_type: update
description: "Dieser Artikel enthält Versionshinweise für Mai 2020."
---
# Mai 2020

## Google Tag Manager

Dokumentation und Beispiele für die Bereitstellung und Verwaltung des Android SDK von Braze mit [Google Tag Manager]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=android):in hinzugefügt.

## Neuer E-Mail API Endpunkt für schwarze Listen

Sie können jetzt E-Mail-Adressen über die Braze API [auf eine schwarze Liste setzen]({{site.baseurl}}/api/endpoints/email/post_blacklist/). Wenn Sie eine E-Mail-Adresse auf die schwarze Liste setzen, wird der Nutzer:innen von E-Mails abgemeldet und als "hart gebounced" markiert.

## Änderung der API-Schlüssel für Braze APIs Endpunkte

Ab Mai 2020 hat Braze die Art und Weise, wie wir API-Schlüssel lesen, geändert, um mehr Sicherheit zu gewährleisten. Jetzt sollten API-Schlüssel als Anfrage-Header übergeben werden. Beispiele finden Sie auf den einzelnen Endpunktseiten unter **Beispielanfrage** sowie in der **Erklärung der API-Schlüssel**.

Braze unterstützt weiterhin die `api_key`, die über den Body der Anfrage und die URL-Parameter übergeben wird, wird aber irgendwann auslaufen (TBD). **Aktualisieren Sie Ihre API-Aufrufe entsprechend.** Diese Änderungen sind in [Postman](https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro) aktualisiert worden.
{% details API-Schlüssel Erläuterung %}
{% tabs %}
{% tab GET-Anfrage %}
Dieses Beispiel verwendet den Endpunkt `/email/hard_bounces`.

**Vorher: API-Schlüssel im Körper der Anfrage**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?api_key={YOUR_REST_API_KEY}&start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
```
**Jetzt: API-Schlüssel im Header**
```
curl --location --request GET 'https://rest.iad-01.braze.com/email/hard_bounces?start_date=2019-01-01&end_date=2019-02-01&limit=100&offset=1&email=foo@braze.com' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endtab %}
{% tab POST-Anfrage %}
Dieses Beispiel verwendet den Endpunkt `/user/track`.

**Vorher: API-Schlüssel im Körper der Anfrage**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--data-raw '{
	"api_key": YOUR-API-KEY-HERE ,
	"attributes": [ 
 	{
 	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
**Jetzt: API-Schlüssel im Header**
```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
	"attributes": [ 
 	{
	  "external_id":"user_id",
      "string_attribute": "sherman",
      "boolean_attribute_1": true,
      "integer_attribute": 25,
      "array_attribute": ["banana", "apple"]
    }
    ]
}'
```
{% endtab %}
{% endtabs %}
{% enddetails %}


