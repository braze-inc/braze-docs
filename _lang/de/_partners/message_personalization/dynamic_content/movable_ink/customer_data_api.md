---
nav_title: Verbinden mit der Kundendaten-API
article_title: Verbinden mit der Movable Ink Kundendaten-API
description: "Dieser Referenzartikel beschreibt, wie Sie eine Verbindung zu den in Braze gespeicherten Daten von Kundenereignissen herstellen, um mithilfe der Kundendaten-API personalisierte Inhalte in Movable Ink zu erstellen."
page_type: partner
search_tag: Partner
---

# Verbinden mit der Movable Ink Kundendaten-API

> Die Integration der Kundendaten-API von Braze und Movable Ink ermöglicht es Marketingfachleuten, in Braze gespeicherte Kundenereignisdaten zu aktivieren, um personalisierte Inhalte in Movable Ink zu erstellen.

Movable Ink ist in der Lage, Verhaltensereignisse von Braze über seine Kundendaten-API aufzunehmen. Die Ereignisse werden auf der Grundlage der eindeutigen Benutzer-ID (UUID), die an Movable Ink übergeben wird, in den Benutzerprofilen gespeichert.

Weitere Informationen über Stories, die Movable Ink-Kundendaten-API und die Nutzung von Verhaltensdaten durch Movable Ink finden Sie in den folgenden Support Center-Artikeln:

- [Nutzen Sie Inhalte mit Verhaltensdaten](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Kundendaten-API Einführung und Leitfaden](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ: Kundendaten-API](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Movable Ink Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Movable Ink-Konto. |
| Movable Ink API-Anmeldeinformationen | Das Lösungsteam von Movable Ink wird für Sie API-Zugangsdaten erstellen. Die API-Anmeldedaten bestehen aus:{::nomarkdown}<ul><li>Eine Endpunkt-URL (an die die Daten gesendet werden)</li><li>Benutzername und Passwort (für die Authentifizierung der API)</li></ul>{:/} Falls gewünscht, kann Movable Ink den Benutzernamen und das Passwort als base64-kodierten Wert bereitstellen, der als grundlegender Autorisierungs-Header-Wert verwendet werden kann. |
| Nutzdaten für Verhaltensereignisse | Sie müssen Ihre Ereignis-Payloads mit Ihrem Movable Ink Client Experience Team teilen. Weitere Informationen finden Sie unter [Gemeinsame Nutzung von Ereignis-Payloads](#event-payloads) mit Movable Ink. |
| Kreative Assets und Geschäftslogik | Sie müssen Movable Ink Ihre kreativen Assets zur Verfügung stellen, einschließlich Adobe Photoshop (PSD)-Dateien, die Movable Ink zeigen, wie der Block aufgebaut werden soll, und ein Ersatzbild. Sie müssen auch eine Geschäftslogik dafür bereitstellen, wie und wann der vom Partner aktivierte Inhaltsblock angezeigt werden soll. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Webhook-Kampagne in Braze

#### Schritt 1a: Erstellen Sie eine neue Kampagne

1. [Erstellen Sie][1] in Braze [eine Webhook-Kampagne][1].
2. Geben Sie Ihrer Kampagne einen Namen und eine optionale Beschreibung.
3. Wählen Sie **Leere Vorlage** als Ihre Vorlage.

#### Schritt 1b: Fügen Sie Ihre Kundendaten-API-Anmeldedaten hinzu

1. Geben Sie in das Feld **Webhook URL** die URL des Movable Ink-Endpunkts ein.

![Registerkarte Compose des Webhook-Composers in Braze mit der Movable Ink-Endpunkt-URL und dem Request Body, der auf JSON Key/Value Pairs eingestellt ist.][img1]{: style="max-width:75%" }

{:start="2"}
2\. Wählen Sie die Registerkarte **Einstellungen**.
3\. Fügen Sie die folgenden Anfrage-Header als Schlüssel-Wert-Paare hinzu:

| Schlüssel | Wert |
| --- | --- |
| Inhalt-Typ | anwendung/json |
| Autorisierung | Geben Sie die Basisauthentifizierung ein, die Sie von Movable Ink erhalten haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Registerkarte Einstellungen des Webhook-Composers in Braze mit Schlüssel-Wert-Paaren für Content-Type und Authorization.][img2]{: style="max-width:75%" }

#### Schritt 1c: Konfigurieren Sie Ihre Nutzlast

1. Kehren Sie zur Registerkarte **Verfassen** zurück.
2. Für Ihren **Request Body** erstellen Sie entweder Ihren eigenen Request Body mit JSON-Schlüssel-Wert-Paaren oder Sie geben Ihre Ereignis-Nutzdaten als Rohtext ein. Beispiele für Standard-E-Commerce-Ereignisse finden Sie in den [Beispiel-Payloads](#sample-payloads).

![Registerkarte Compose des Webhook-Composers in Braze mit JSON-Schlüssel-Wert-Paaren für ID, Zeitstempel, Benutzer-ID und Ereignistyp.][img3]{: style="max-width:75%" }

#### Schritt 1d: Testen Sie Ihren Webhook {#step-1d}

Sie müssen eine Beispiel-Nutzlast mit Ihrem Movable Ink Client Experience Team teilen. Sie können diese Nutzdaten auf der Registerkarte **Test** auf der Grundlage der von Ihnen erstellten Nutzdaten generieren.

{% alert important %}
Movable Ink empfiehlt, mit dem Testen Ihres Webhooks in Braze zu warten, bis Ihr Movable Ink Client Experience Team bestätigt hat, dass es das Mapping abgeschlossen hat und bereit ist, einen Test zu empfangen. Wenn diese Zuordnung nicht vollständig ist, werden Sie beim Testen wahrscheinlich eine Fehlermeldung erhalten.
{% endalert %}

Um Ihren Webhook zu testen, gehen Sie wie folgt vor:

1. Wählen Sie die Registerkarte **Test**.
2. Zeigen Sie eine Vorschau der Nachricht als Benutzer an, um ein Beispiel für die Nutzdaten dieses Benutzers zu sehen. Sie können zwischen einer Vorschau als zufälliger Benutzer, als bestimmter Benutzer oder als benutzerdefinierter Benutzer wählen.
3. Wenn alles gut aussieht, klicken Sie auf **Test senden**, um eine Testanfrage zu senden.

![Webhook-Antwortnachricht in Braze, die eine 200 OK-Antwort zeigt.][img4]{: style="max-width:75%" }

### Schritt 2: Beenden Sie die Einrichtung Ihrer Kampagne

#### Schritt 2a: Planen Sie Ihre Kampagne

Wenn Sie mit dem Verfassen und Testen des Webhooks fertig sind, [planen Sie Ihre Kampagne][2]. 

Braze unterstützt geplante, aktionsbasierte und API-ausgelöste Lieferungen. [Die aktionsbasierte Bereitstellung][3] ist in der Regel die beste Lösung für die meisten verhaltensorientierten Ereignisse. Wenn Sie Fragen dazu haben, was für Ihren Anwendungsfall sinnvoll ist, wenden Sie sich an Ihre Braze- und Movable Ink-Kundenbetreuer.

Für eine handlungsorientierte Lieferung:

1. Geben Sie die Auslöseaktion an. Dies ist das Ereignis, das den Webhook für Movable Ink auslöst.
2. Vergewissern Sie sich, dass die **Zeitplanverzögerung** auf **Sofort** eingestellt ist. Ereignisdaten sollten sofort nach Eintreten des Ereignisses an Movable Ink gesendet werden, ohne Verzögerung.
3. Legen Sie die Dauer der Kampagne fest, indem Sie eine Startzeit angeben. Eine Endzeit ist wahrscheinlich nicht zutreffend, kann aber festgelegt werden, wenn dies für den Anwendungsfall erforderlich ist.

{% alert note %}
Um sicherzustellen, dass die Daten in Echtzeit an Movable Ink übertragen werden, wählen Sie nicht die Option **Kampagne an Benutzer in ihrer lokalen Zeitzone senden**.
{% endalert %}

#### Schritt 2b: Bestimmen Sie Ihr Publikum

Bestimmen Sie als nächstes, welche Benutzer Sie für diese Kampagne ansprechen möchten. Einzelheiten finden Sie unter [Benutzer anvisieren][4].

Stellen Sie sicher, dass Sie keine A/B-Tests in Ihrer Kampagne verwenden, indem Sie das **Kontrollgruppen-Kontrollkästchen** deaktivieren. Wenn eine Kontrollgruppe enthalten ist, werden bei einem bestimmten Prozentsatz der Benutzer keine Daten an Movable Ink gesendet. Ihr gesamtes Publikum sollte sich für die Variante entscheiden und nicht für die Kontrollgruppe.

![A/B-Test-Panel in einer Braze-Kampagne mit einer 100%igen Verteilung der Variante 1 und keiner Kontrollgruppe.][img5]

#### Schritt 2c: Wählen Sie Konvertierungsereignisse (optional)

Falls gewünscht, können Sie dieser Kampagne in Braze Konvertierungsereignisse zuweisen.

Da der Webhook jedoch nur zum Streamen von Daten gedacht ist, ist die Zuordnung auf dieser Ebene wahrscheinlich weniger nützlich als die Zuordnung auf Kampagnenebene, nachdem die Verhaltensdaten von Braze zur Personalisierung von Inhalten verwendet wurden.

### Schritt 3: Starten Sie die Kampagne

Überprüfen Sie Ihre Webhook-Einstellungen und starten Sie Ihre Kampagne.

## Überlegungen

### Ausrichten auf eine eindeutige Benutzerkennung

Vergewissern Sie sich, dass der Wert der eindeutigen Benutzerkennung (UUID), den Sie als `mi_u` verwenden, in Braze verfügbar ist und in die an Movable Ink gesendeten Ereignis-Nutzdaten aufgenommen werden kann.

Dadurch wird sichergestellt, dass die Verhaltensereignisse, auf die Movable Ink bei der Erstellung eines Bildes verweist, mit demselben Kunden verbunden sind, für den sie die Verhaltensereignisse erhalten haben. Wenn der UUID-Wert nicht mit dem von Braze `external_id` übereinstimmt, muss die UUID erfasst und an Braze als Attribut oder in den Ereigniseigenschaften eines Braze-Ereignisses übergeben werden, um diese Kennung zu nutzen.

Braze verfolgt das Nutzerverhalten über mehrere Plattformen hinweg (z.B. Web und mobile App), so dass ein einzelner Nutzer mehrere verschiedene anonyme IDs haben kann. Diese IDs können zu einem einzigen bekannten Stories-Benutzerprofil zusammengeführt werden, wenn ein `identify` -Ereignis an Movable Ink gesendet wird, solange das `identify` -Ereignis sowohl einen anonymen Identifikator als auch den einzigen bekannten Identifikator enthält.

Sobald Movable Ink eine `user_id` für einen einzelnen Benutzer erhält, müssen alle zukünftigen Ereignisse für diesen Benutzer dieselbe `user_id` enthalten.

### Gemeinsame Nutzung von Ereignis-Payloads mit Movable Ink {#event-payloads}

Bevor Sie den Konnektor für die Kundendaten-API von Movable Ink einrichten, sollten Sie Ihre Ereignis-Payloads mit Ihrem Movable Ink Client Experience Team teilen. Dadurch kann Movable Ink Ihre Ereignisse dem Ereignisschema zuordnen und verhindert, dass API-Aufrufe abgelehnt werden oder fehlschlagen.

Sie können in Braze eine Ereignis-Nutzlast mit beliebigen Ereigniseigenschaften erzeugen. Generieren Sie eine Beispiel-Nutzlast für einen zufälligen Benutzer oder durch Suche nach einer bestimmten Benutzer-ID. Siehe [Schritt 1d](#step-1d) oben für Details.

Teilen Sie diese Beispiel-Nutzlast mit Ihrem Movable Ink Client Experience Team. Vergewissern Sie sich, dass sich keine sensiblen, persönlich identifizierbaren Informationen in der Nutzlast der Probe befinden (z. B. E-Mail-Adresse, Telefonnummer oder vollständige Geburtsdaten). 

Weitere Informationen über benutzerdefinierte Ereigniseigenschaften und das erwartete Format der in den Eigenschaften enthaltenen Daten finden Sie unter [Benutzerdefinierte Ereigniseigenschaften][5].

### Bekannte versus anonyme Benutzer

In Braze können Ereignisse unter einem anonymen Benutzerprofil aufgezeichnet werden. Welche Identifikatoren während der Ereignisprotokollierung mit dem Benutzerprofil verknüpft werden, hängt davon ab, wie der Benutzer erstellt wurde (über das Braze SDK oder die APIs) und in welcher Phase des Benutzerlebenszyklus er sich befindet.

#### Nur Weiterleitung von Braze-Ereignissen für bekannte Benutzer

Verwenden Sie in Ihrer Webhook-Kampagne den Filter `External User ID`, um nur Benutzer anzusprechen, die eine `external_id` mit dem Filter `External User ID` `is not blank` haben.

#### Weiterleitung von Braze-Ereignissen für anonyme und bekannte Benutzer

Wenn Sie Braze-Ereignisse von anonymen Benutzern weiterleiten möchten (Benutzer, denen noch kein `external_id` zugewiesen wurde), müssen Sie entscheiden, welchen Identifikator Sie als `anonymous_id` für Movable Ink verwenden möchten, bis ein `external_id` verfügbar ist. Wählen Sie eine `anonymous_id`, die in Ihrem Braze-Benutzerprofil konstant bleiben wird. Sie können die Liquid-Logik im Webhook-Body verwenden, um zu entscheiden, ob ein `anonymous_id` oder ein `user_id` übergeben werden soll.

Weitere Informationen finden Sie in den Beispiel-Webhooks unter [Beispiel-Nutzdaten](#sample-payloads).

## Beispiel-Nutzdaten

### Ereignis Produktansicht

{% tabs local %}
{% tab Beispiel Lötauslöser-Ereignis %}

{% raw %}

```json
{
  "events": [
    {
      "email": "test@braze.com",
      "name": "Product Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "categories": [
          {
            "id": "Bathroom",
            "url": "https://example.com/cat/bathroom"
          }
        ],
        "meta": {
          "color": "green"
        },
        "title": "All-Purpose Cleaning Wipes",
        "price": 1.99,
        "id": "56544",
        "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Erwartete Nutzdaten der Anfrage für bewegliche Tinte %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "Bathroom",
        "url": "https://example.com/cat/bathroom"
      }
    ],
    "meta": {
      "color": "green"
    },
    "title": "All-Purpose Cleaning Wipes",
    "price": 1.99,
    "id": "56544",
    "url": "https://www.example.com/variants_id/5f08cb918dcc595aa74b0fbc"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'

```

{% endraw %}
{% endtab %}
{% tab Beispiel Webhook %}

In diesem Beispiel wird eine gehashte E-Mail-Adresse als `anonymous_id` für Benutzer verwendet, die nicht über eine `external_id` verfügen.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

// Condition logic to determine which identifier to use. If an external_id is available use that, otherwise use the anonymous_id
{% if {{${user_id}}} %}
{% capture user_identifier %}"user_id": "{{${user_id}}}"{% endcapture %}
{% else %}
{% capture user_identifier %}"anonymous_id": "{{anon_id}}"{% endcapture %}
{% endif %}

{
  {{user_identifier}}
  "event": "product_viewed",
  "properties": {
    "categories": [
      {
        "id": "{{event_properties.${categories}[0].id}}",
        "url": "{{event_properties.${categories}[0].url}}"
      }
    ],
    "meta": {
      "color": "{{event_properties.${meta}.color}}"
    },
    "title": "{{event_properties.${title}}}",
    "price": "{{event_properties.${price}}}",
    "id": "{{event_properties.${id}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
}

```

{% endraw %}
{% endtab %}
{% endtabs %}

### Ereignis Kategorieansicht

{% tabs local %}
{% tab Beispiel Lötauslöser-Ereignis %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Category Viewed",
      "time": "2023-12-06T19:20:45+01:00",
      "properties": {
        "id": "bathroom-1",
        "title": "Bathroom Stuff",
        "url": "https://www.example.com/categories/bathroom"
      }
    }
  ]
}
```

{% endraw %}

{% endtab %}
{% tab Erwartete Nutzdaten der Anfrage für bewegliche Tinte %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "123-abc-678",
  "event": "category_viewed",
  "properties": {
    "id": "bathroom-1",
    "title": "Bathroom Stuff",
    "url": "https://www.example.com/categories/bathroom"
  },
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "track",
  "user_id": "5c3aa83113dd490100d3d8d7"
}'
```

{% endraw %}

{% endtab %}
{% tab Beispiel Webhook %}

Dieses Beispiel zeigt einen Webhook, der nur Ereignisse für bekannte Benutzer (Benutzer mit einem `external_id`) verfolgt.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

{
  "event": "category_viewed",
  "properties": {
    "id": "{{event_properties.${id}}}",
    "title": "{{event_properties.${title}}}",
    "url": "{{event_properties.${url}}}"
  },
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "track",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}

### Ereignis identifizieren

{% tabs local %}
{% tab Beispiel Lötauslöser-Ereignis %}

{% raw %}

```json
{
  "events": [
    {
      "external_id": "123456789",
      "name": "Account Created",
      "time": "2023-12-06T19:20:45+01:00"
    }
  ]
}
```

{% endraw %}
{% endtab %}
{% tab Erwartete Nutzdaten der Anfrage für bewegliche Tinte %}

{% raw %}

```
curl --location --request POST 'https://collector.movableink-dmz.com/behavioral/{{key}}' \
--header 'Authorization: Basic {{authorization}}' \
--header 'Content-Type: application/json' \
--data-raw '{
  "anonymous_id": "jg0iq5gd30dqpwn8zmx05p06mzjmjir4r8",
  "timestamp": 1257894000000,
  "timezone": "America/New_York",
  "type": "identify",
  "user_id": "mycustomerid123"
}'
```

{% endraw %}
{% endtab %}
{% tab Beispiel Webhook %}

In diesem Beispiel wird eine gehashte E-Mail-Adresse als `anonymous_id` für Benutzer verwendet, die nicht über eine `external_id` verfügen.

{% raw %}

```liquid
// Converts the timestamp of "now" to seconds since 1970 and assigns it to a local variable "timestamp"
{% assign timestamp = "now" | date: "%s" %}

// Example of md5 hashing the email address to use as the anonymous_id
{% assign anon_id = {{${email_address}}} | md5 %}

{
  "anonymous_id": "{{anon_id}}",
  "timestamp": "{{timestamp}}",
  "timezone": "{{${time_zone}}}",
  "type": "identify",
  "user_id": "{{${user_id}}}"
}

```

{% endraw %}

{% endtab %}
{% endtabs %}



[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[2]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types
[3]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/
[4]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[img1]: {% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}
[img2]: {% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}
[img3]: {% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}
[img4]: {% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}
[img5]: {% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %}
