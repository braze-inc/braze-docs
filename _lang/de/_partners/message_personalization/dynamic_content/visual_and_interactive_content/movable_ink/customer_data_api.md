---
nav_title: Verbindung mit der Kundendaten-API
article_title: Verbinden mit der Movable Ink Kundendaten API
description: "Dieser referenzierte Artikel beschreibt, wie Sie mit Hilfe der Kundendaten-API eine Verbindung zur Aktivierung von in Braze gespeicherten Kundendaten herstellen, um personalisierte Inhalte in Movable Ink zu generieren."
page_type: partner
search_tag: Partner
---

# Verbinden mit der Movable Ink Kundendaten API

> Die Integration der Kundendaten-APIs von Braze und Movable Ink ermöglicht Marketern, die in Braze gespeicherten Kundendaten zu aktivieren, um personalisierte Inhalte in Movable Ink zu generieren.

Movable Ink ist in der Lage, Verhaltensverhalten-Events von Braze über deren Kundendaten-API aufzunehmen. Die Ereignisse werden in den Nutzerprofilen auf der Grundlage der eindeutigen Nutzer:innen ID (UUID) gespeichert, die an Movable Ink übermittelt wird.

Weitere Informationen über Stories, die Movable Ink Customer Data API und darüber, wie Movable Ink Verhaltensdaten nutzt, finden Sie in den folgenden Support Center-Artikeln:

- [Leistungsstarke Inhalte mit Verhaltensdaten](https://support.movableink.com/hc/en-us/sections/360001239453-Power-content-with-behavioral-data)
- [Kundendaten API Einführung und Leitfaden](https://support.movableink.com/hc/en-us/articles/13815957200663-Customer-Data-API-introduction-and-guide)
- [FAQ: Kundendaten API](https://support.movableink.com/hc/en-us/articles/12423178752279-FAQ-Customer-Data-API)

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Movable Ink Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Movable Ink-Konto. |
| Movable Ink API-Zugangsdaten | Das Team von Movable Ink Solutions generiert für Sie API Zugangsdaten. Die API Zugangsdaten bestehen aus:{::nomarkdown}<ul><li>Eine Endpunkt-URL (an die die Daten gesendet werden)</li><li>Benutzername und Passwort (für die Authentifizierung der API)</li></ul>{:/} Falls gewünscht, kann Movable Ink den Benutzernamen und das Passwort als base64-kodierten Wert bereitstellen, der als Basisautorisierungs-Header-Wert verwendet werden kann. |
| Nutzdaten für Verhaltensereignisse | Sie müssen Ihre Ereignis-Payloads mit Ihrem Movable Ink Client Experience Team teilen. Weitere Informationen finden Sie unter [Gemeinsame Nutzung von Ereignis-Payloads](#event-payloads) mit Movable Ink. |
| Kreative Assets und Geschäftslogik | Sie müssen Movable Ink kreative Assets zur Verfügung stellen, einschließlich Adobe Photoshop (PSD)-Dateien, die Movable Ink zeigen, wie der Block zu erstellen ist, und ein Fallback-Bild. Sie müssen auch eine Geschäftslogik dafür bereitstellen, wie und wann der vom Partner aktivierte Content-Block angezeigt werden soll. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Erstellen Sie eine Webhook-Kampagne in Braze

#### Schritt 1a: Erstellen Sie eine neue Kampagne

1. [Erstellen Sie eine Webhook-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) in Braze.
2. Geben Sie Ihrer Kampagne einen Namen und eine optionale Beschreibung.
3. Wählen Sie als Template die **leere Vorlage** aus.

#### Schritt 1b: Fügen Sie Ihre Kundendaten API-Zugangsdaten hinzu

1. Geben Sie in das Feld **Webhook URL** die URL des Movable Ink Endpunkts ein.

![Tab des Webhook-Composers in Braze mit der URL des Movable Ink-Endpunkts und dem auf JSON Schlüssel-Wert-Paare eingestellten Request Body.]({% image_buster /assets/img/movable_ink/cd_api_webhook_url.png %}){: style="max-width:75%" }

{:start="2"}
2\. Wählen Sie den Tab **Einstellungen**.
3\. Fügen Sie die folgenden Anfrage-Header als Schlüssel-Wert-Paare hinzu:

| Schlüssel | Wert |
| --- | --- |
| Content-Typ | application/json |
| Autorisierung | Geben Sie die Basisauthentifizierung ein, die Sie von Movable Ink erhalten haben. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Tab Einstellungen des Webhook-Composers in Braze mit Schlüssel-Wert-Paaren für Content-Type und Authorization.]({% image_buster /assets/img/movable_ink/cd_api_webhook_settings.png %}){: style="max-width:75%" }

#### Schritt 1c: Konfigurieren Sie Ihre Nutzlast

1. Kehren Sie zum Tab **Verfassen** zurück.
2. Für Ihren **Anfragekörper** erstellen Sie entweder Ihren eigenen Anfragekörper mit JSON Schlüssel-Wert-Paaren oder geben Ihre Ereignis-Nutzdaten als Rohtext ein. Beispiele für E-Commerce-Standardereignisse finden Sie in den [Beispiel-Payloads](#sample-payloads).

![Tab des Webhook-Composers in Braze mit JSON Schlüssel-Wert-Paaren für ID, Zeitstempel, Nutzer:in und Ereignistyp.]({% image_buster /assets/img/movable_ink/cd_api_webhook_kvp.png %}){: style="max-width:75%" }

#### Schritt 1d: Testen Sie Ihren Webhook {#step-1d}

Sie müssen Ihrem Movable Ink Client Experience Team eine Beispiel-Nutzlast zur Verfügung stellen. Sie können diese Nutzdaten auf der Registerkarte **Test** auf der Grundlage der von Ihnen erstellten Nutzdaten generieren.

{% alert important %}
Movable Ink empfiehlt, mit dem Testen Ihres Webhooks in Braze zu warten, bis Ihr Movable Ink Client Experience Team bestätigt hat, dass es die Abbildung abgeschlossen hat und bereit ist, einen Test zu empfangen. Wenn diese Abbildung nicht vollständig ist, werden Sie beim Testen wahrscheinlich eine Fehlermeldung erhalten.
{% endalert %}

Um Ihren Webhook zu testen, gehen Sie wie folgt vor:

1. Wählen Sie die Registerkarte **Test**.
2. Vorschau der Nachricht als Nutzer:innen, um eine Beispiel-Nutzlast für diesen Nutzer zu sehen. Sie haben die Wahl zwischen einer Vorschau als zufälliger Benutzer, als bestimmter Benutzer oder als angepasster Nutzer:innen.
3. Wenn alles gut aussieht, klicken Sie auf **Test senden**, um eine Testanfrage zu senden.

![Webhook-Antwortnachricht in Braze mit einer 200 OK-Antwort.]({% image_buster /assets/img/movable_ink/cd_api_webhook_response.png %}){: style="max-width:75%" }

### Schritt 2: Schließen Sie die Einrichtung Ihrer Kampagne ab

#### Schritt 2a: Zeitplan für Ihre Kampagne

Wenn Sie den Webhook fertiggestellt und getestet haben, [planen Sie Ihre Kampagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types). 

Braze unterstützt geplante, aktionsbasierte und API-ausgelöste Zustellungen. Die [aktionsbasierte Zustellung]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/) ist in der Regel die beste Lösung für die meisten verhaltensorientierten Ereignisanwendungen. Wenn Sie Fragen dazu haben, was für Ihren Anwendungsfall sinnvoll ist, wenden Sie sich an Ihre Customer-Success-Manager von Braze und Movable Ink.

Für aktionsbasierte Zustellung:

1. Geben Sie die Aktion triggern an. Dies ist das Ereignis, das den Webhook für Movable Ink triggern wird.
2. Stellen Sie sicher, dass die **Zeitplan-Verzögerung** auf **Sofort** eingestellt ist. Die Daten eines Ereignisses sollten sofort nach dem Eintreten des Ereignisses an Movable Ink gesendet werden, ohne Verzögerung.
3. Legen Sie die Dauer der Kampagne fest, indem Sie eine Startzeit angeben. Eine Endzeit ist wahrscheinlich nicht zutreffend, kann aber bei Bedarf für den Anwendungsfall festgelegt werden.

{% alert note %}
Um sicherzustellen, dass die Daten in Echtzeit zu Movable Ink gestreamt werden, wählen Sie nicht die Option **Kampagne an Nutzer:innen in ihrer Ortszeit senden**.
{% endalert %}

#### Schritt 2b: Bestimmen Sie Ihre Zielgruppe

Bestimmen Sie als nächstes, welche Nutzer:innen Sie für diese Kampagne anvisieren möchten. Einzelheiten finden Sie unter [Targeting Nutzer:innen]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/).

Stellen Sie sicher, dass Sie keine A/B-Tests in Ihrer Kampagne verwenden, indem Sie das **Kontrollgruppen-Kontrollkästchen** deaktivieren. Wenn eine Kontrollgruppe enthalten ist, werden bei einem bestimmten Prozentsatz der Nutzer:innen keine Daten an Movable Ink gesendet. Alle Ihre Zielgruppen sollten sich für die Variante und nicht für die Kontrollgruppe entscheiden.

![A/B-Tests Panel in einer Braze-Kampagne mit 100%iger Verteilung der Variante 1 und ohne Kontrollgruppe.]({% image_buster /assets/img/movable_ink/cd_api_webhook_ab.png %})

#### Schritt 2c: Wählen Sie Konversions-Events (optional)

Falls gewünscht, können Sie dieser Kampagne innerhalb von Braze Konversions-Events zuweisen.

Da der Webhook jedoch nur zum Streamen von Daten gedacht ist, ist die Attribution auf dieser Ebene wahrscheinlich weniger nützlich als die Betrachtung der Attribution auf Kampagnenebene, nachdem die Verhaltensdaten von Braze zur Personalisierung von Inhalten verwendet wurden.

### Schritt 3: Kampagne starten

Überprüfen Sie Ihre Webhook-Einrichtung und starten Sie Ihre Kampagne.

## Überlegungen

### Ausrichten auf einen eindeutigen Nutzer:in Bezeichner

Stellen Sie sicher, dass der eindeutige Bezeichner (UUID), den Sie als `mi_u` verwenden, in Braze verfügbar ist und in die an Movable Ink gesendeten Ereignis-Payloads aufgenommen werden kann.

Dadurch wird sichergestellt, dass die Verhaltensereignisse, auf die Movable Ink bei der Erstellung eines Bildes referenziert, mit demselben Kundenverhalten verknüpft sind, für das sie die Verhaltensereignisse erhalten haben. Wenn der UUID-Wert nicht mit dem von Braze `external_id` übereinstimmt, muss die UUID erfasst und an Braze als Attribut oder in den Event-Eigenschaften eines Braze-Events übergeben werden, um diesen Bezeichner zu nutzen.

Braze trackt das Nutzerverhalten über mehrere Plattformen hinweg (z.B. Internet und mobile App), so dass ein einzelner Nutzer:innen mehrere verschiedene anonyme IDs haben kann. Diese IDs können in das einzige bekannte Stories Nutzerprofil zusammengeführt werden, wenn ein `identify` Ereignis an Movable Ink gesendet wird, solange das `identify` Ereignis sowohl einen anonymen Bezeichner als auch den einzigen bekannten Bezeichner enthält.

Sobald Movable Ink eine `user_id` für einen einzelnen Nutzer:innen erhält, müssen alle zukünftigen Ereignisse für diesen Nutzer:innen dieselbe `user_id` enthalten.

### Gemeinsame Nutzung von Ereignis-Payloads mit Movable Ink {#event-payloads}

Bevor Sie den Konnektor zur Kundendaten-API von Movable Ink einrichten, stellen Sie sicher, dass Sie Ihre Event-Payloads mit Ihrem Movable Ink Client Experience Team teilen. Dies ermöglicht Movable Ink die Abbildung Ihrer Ereignisse auf das Ereignisschema und verhindert, dass API-Aufrufe abgelehnt werden oder fehlschlagen.

Sie können in Braze eine Event-Nutzlast mit beliebigen Event-Eigenschaften erzeugen. Generieren Sie eine Beispiel-Nutzlast für einen zufälligen Nutzer oder durch die Suche nach einer bestimmten Nutzer:innen-ID. Siehe [Schritt 1d](#step-1d) oben für Details.

Teilen Sie diese Beispiel-Nutzlast mit Ihrem Movable Ink Client Experience Team. Vergewissern Sie sich, dass keine sensiblen persönlichen Bezeichner (wie z.B. E-Mail Adresse, Telefonnummer oder vollständige Geburtsdaten) in der Nutzlast der Probe enthalten sind. 

Wenn Sie mehr über angepasste Event-Eigenschaften und das erwartete Format der in den Eigenschaften enthaltenen Daten erfahren möchten, referenzieren Sie auf [Angepasste Event-Eigenschaften]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties).

### Bekannte versus anonyme Nutzer:innen

In Braze können Ereignisse unter einem anonymen Nutzerprofil aufgezeichnet werden. Welche Bezeichner bei der Ereignisprotokollierung mit dem Nutzerprofil verknüpft werden, hängt davon ab, wie der Nutzer erstellt wurde (über das Braze SDK oder die APIs) und in welcher Phase des Nutzer:in sich der Nutzer befindet.

#### Nur Braze-Ereignisse für bekannte Nutzer:innen weiterleiten

Verwenden Sie in Ihrer Webhook-Kampagne den Filter `External User ID`, um nur Nutzer:innen anzusprechen, die eine `external_id` mit dem Filter `External User ID` `is not blank` haben.

#### Weiterleitung von Braze-Ereignissen für anonyme und bekannte Nutzer:innen

Wenn Sie Braze-Ereignisse von anonymen Nutzer:innen (Nutzer:innen, deren Profil noch kein `external_id` zugewiesen wurde) weiterleiten möchten, müssen Sie entscheiden, welchen Bezeichner Sie als `anonymous_id` für Movable Ink verwenden möchten, bis ein `external_id` verfügbar ist. Wählen Sie eine `anonymous_id`, die in Ihrem Nutzerprofil auf Braze konstant bleibt. Sie können die Liquid-Logik im Körper des Webhooks verwenden, um zu entscheiden, ob ein `anonymous_id` oder ein `user_id` übergeben werden soll.

Weitere Informationen finden Sie in den Beispiel-Webhooks unter [Beispiel-Nutzdaten](#sample-payloads).

## Beispiel-Nutzdaten

### Ereignis Produktansicht

{% tabs local %}
{% tab Beispiel Braze Trigger-Ereignis %}

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
{% tab Erwartete Movable Ink Anfrage Payload %}

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

In diesem Beispiel wird eine gehashte E-Mail Adresse als `anonymous_id` für Nutzer:innen verwendet, die keine `external_id` haben.

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
{% tab Beispiel Braze Trigger-Ereignis %}

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
{% tab Erwartete Movable Ink Anfrage Payload %}

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

Dieses Beispiel zeigt einen Webhook, der nur Ereignisse für bekannte Nutzer:innen trackt (Nutzer:innen mit einem `external_id`).

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

### Ereignis bezeichnen

{% tabs local %}
{% tab Beispiel Braze Trigger-Ereignis %}

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
{% tab Erwartete Movable Ink Anfrage Payload %}

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

In diesem Beispiel wird eine gehashte E-Mail Adresse als `anonymous_id` für Nutzer:innen verwendet, die keine `external_id` haben.

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



