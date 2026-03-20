---
nav_title: "Verbundener Zielgruppen-Filter und -Objekt"
article_title: API Verbundenes Zielgruppen-Objekt
page_order: 3
page_type: reference
description: "Dieser Artikel erklärt das verbundene Zielgruppen-Objekt, einschließlich seiner Funktionsweise, Anwendungsfälle und der verschiedenen Filter, aus denen es besteht."

---

# Verbundenes Zielgruppen-Objekt

> Ein verbundener Zielgruppen-Filter ist ein dynamischer Zielgruppen-Filter, den Sie direkt in Ihrer API-Anfrage definieren. So können Sie zum Sendezeitpunkt die richtigen Nutzer:innen ansprechen, ohne Segmente im Braze-Dashboard erstellen oder verwalten zu müssen.

Anstatt für jede mögliche Zielgruppenkombination vorab ein Segment zu erstellen, übergeben Sie die Filterkriterien direkt im `audience`-Parameter Ihres API-Aufrufs. Braze wertet jede:n Nutzer:in in Realtime anhand dieser Kriterien aus und stellt die Nachricht nur an Nutzer:innen zu, die den Kriterien entsprechen. Das bedeutet, dass eine einzelne Kampagne, ein Canvas oder eine reine API-Nachrichtendefinition eine unbegrenzte Anzahl von Zielgruppenvarianten bedienen kann – vollständig gesteuert durch Ihre Geschäftslogik.

## So funktioniert es

1. Definieren Sie Ihre Nachricht, indem Sie entweder eine API-getriggerte Kampagne oder ein Canvas im Braze-Dashboard erstellen, oder definieren Sie den Nachrichteninhalt vollständig inline mithilfe der [Messaging-Objekte]({{site.baseurl}}/api/objects_filters/#messaging-objects) in Ihrer API-Anfrage. Verwenden Sie [Trigger-Eigenschaften]({{site.baseurl}}/api/objects_filters/trigger_properties_object/) oder [Canvas-Kontext]({{site.baseurl}}/api/objects_filters/context_object/) für dynamische Personalisierung.
2. Rufen Sie einen unterstützten Endpunkt auf und fügen Sie den `audience`-Parameter mit Ihren Filterkriterien hinzu. Sie können nach angepassten Attributen, Push-Abo-Status, E-Mail-Abo-Status und dem Zeitpunkt der letzten App-Nutzung filtern.
3. Braze wertet die Filter zum Sendezeitpunkt aus und stellt die Nachricht nur an Nutzer:innen zu, die Ihren Kriterien entsprechen.

{% alert tip %}
Eine `campaign_id` ist bei Verwendung des `audience`-Parameters nicht erforderlich. Die Endpunkte [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) und [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/) ermöglichen es Ihnen, Nachrichteninhalte inline zu definieren, ohne eine vorab erstellte Kampagne. Wenn Sie jedoch Metriken auf Kampagnenebene (wie Sends, Klicks oder Absprünge) im Dashboard verfolgen möchten, fügen Sie eine `campaign_id` hinzu.
{% endalert %}

Da die Zielgruppe pro Anfrage definiert wird, können Ihre Backend-Systeme kontextuell relevante Nachrichten als Reaktion auf jedes Geschäftsereignis (eine Preisänderung, eine Wetterwarnung, ein Live-Spielstand-Update) triggern – ohne Eingriff im Dashboard.

### Kompatible Endpunkte

Sie können das verbundene Zielgruppen-Objekt mit dem `audience`-Parameter an diesen Endpunkten verwenden:

- [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)
- [`/canvas/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)
- [`/messages/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)
- [`/campaigns/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_campaigns/)
- [`/canvas/trigger/schedule/create`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_triggered_canvases/)

## Anwendungsfälle

Verwenden Sie verbundene Zielgruppen für Szenarien, in denen Ihre Backend-Systeme ein Ereignis erkennen und eine dynamisch bestimmte Gruppe von Nutzer:innen benachrichtigen müssen:

| Kategorie | Beispiel |
| --- | --- |
| Wetterwarnungen | Ein Wetterdatenanbieter erkennt ein schweres Wetterereignis und sendet Push-Benachrichtigungen an Nutzer:innen, deren Attribut `preferred_city` mit dem betroffenen Gebiet übereinstimmt. |
| Sport und Live-Events | Eine Sport-App sendet Realtime-Spielstand-Updates oder Spielbenachrichtigungen an Nutzer:innen, deren Attribut `favorite_team` mit einem der spielenden Teams übereinstimmt. |
| Inhalt und Unterhaltung | Ein Streaming-Dienst benachrichtigt Nutzer:innen, deren Array `favorite_shows` einen Serientitel enthält, sobald eine neue Folge veröffentlicht wird. |
| E-Commerce | Ein Online-Händler sendet Preissenkungen- oder Wieder-verfügbar-Benachrichtigungen an Nutzer:innen, deren Array `wishlisted_products` die entsprechende Produkt-ID enthält. |
| Reisen | Eine Reise-App sendet Flugverspätungs-Benachrichtigungen an Nutzer:innen, deren Attribut `booked_flight` mit der betroffenen Flugnummer übereinstimmt. |
| Finanzdienstleistungen | Eine Handelsplattform benachrichtigt Nutzer:innen, deren Array `watchlist` ein Aktiensymbol enthält, das eine Preisschwelle überschritten hat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

In jedem Fall verarbeitet eine einzelne Kampagne oder reine API-Nachrichtendefinition alle Varianten. Ihr Backend bestimmt die Filterwerte und übergibt sie in der API-Anfrage, sodass Sie kein separates Segment oder keine separate Kampagne für jedes Produkt, jede Sendung, jedes Team oder jeden Standort erstellen müssen.

## Beispielanfrage

Das folgende Beispiel verwendet den Endpunkt [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/), um Nutzer:innen anzusprechen, die eine bestimmte Sendung als Favorit gespeichert haben und für Push-Benachrichtigungen angemeldet sind:

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "audience": {
    "AND": [
      {
        "custom_attribute": {
          "custom_attribute_name": "favorite_shows",
          "comparison": "includes_value",
          "value": "Example Show"
        }
      },
      {
        "push_subscription_status": {
          "comparison": "is",
          "value": "opted_in"
        }
      }
    ]
  },
  "trigger_properties": {
    "show_title": "Example Show",
    "episode_title": "Season 3, Episode 1",
    "deep_link": "https://example.com/shows/example-show/s3e1"
  },
  "broadcast": false
}
```

## Objektstruktur

Das verbundene Zielgruppen-Objekt besteht entweder aus einem einzelnen verbundenen Zielgruppen-Filter oder aus mehreren verbundenen Zielgruppen-Filtern, die mit den Operatoren `AND` und `OR` kombiniert werden.

**Beispiel für mehrere Filter:**

```json
{
  "AND":
    [
      Connected Audience Filter,
      {
        "OR" :
          [
            Connected Audience Filter,
            Connected Audience Filter
          ]
      },
      Connected Audience Filter
    ]
}
```

## Verbundene Zielgruppen-Filter

Kombinieren Sie mehrere Filter mit den Operatoren `AND` und `OR`, um einen verbundenen Zielgruppen-Filter zu erstellen.

### Filter für angepasste Attribute

Mit diesem Filter können Sie auf der Grundlage eines angepassten Attributs einer:eines Nutzer:in segmentieren. Diese Filter enthalten bis zu drei Felder:

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": (String) the name of the custom attribute to filter on,
      "comparison": (String) one of the allowed comparisons to make against the provided value,
      "value": (String, Numeric, Boolean) the value to be compared using the provided comparison
    }
}
```

#### Zulässige Vergleiche nach Datentyp

Der Datentyp des angepassten Attributs bestimmt die Vergleiche, die für einen bestimmten Filter gültig sind.

| Angepasstes Attribut – Typ | Zulässige Vergleiche |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numerisch | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolescher Wert | `equals`, `not_equal`, `exists`, `does_not_exist` |
| Zeit | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Hinweise zum Attributvergleich

| Vergleich | Zusätzliche Hinweise |
| --- | --- |
| `value` | Die Angabe `value` ist nicht erforderlich, wenn Sie die Vergleiche `exists` oder `does_not_exist` verwenden. `value` muss ein ISO 8601 Datetime-String sein, wenn Sie die Vergleiche `before` und `after` verwenden. |
|`matches_regex` | Wenn Sie den Vergleich `matches_regex` verwenden, muss der übergebene Wert ein String sein. Weitere Informationen über die Verwendung regulärer Ausdrücke mit Braze finden Sie unter [Reguläre Ausdrücke]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) und [Angepasste Attribut-Datentypen]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Beispiel für ein angepasstes Attribut

```json
{
  "custom_attribute":
    {
      "custom_attribute_name": "eye_color",
      "comparison": "equals",
      "value": "blue"
    }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}
```

```json
{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### Push-Abo-Filter

Dieser Filter ermöglicht es Ihnen, auf der Grundlage des Push-Abo-Status einer:eines Nutzer:in zu segmentieren.

#### Filterstruktur

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Zulässige Vergleiche:** `is`, `is_not`
- **Zulässige Werte:** `opted_in`, `subscribed`, `unsubscribed`

### E-Mail-Abo-Filter

Dieser Filter ermöglicht es Ihnen, auf der Grundlage des E-Mail-Abo-Status einer:eines Nutzer:in zu segmentieren.

#### Filterstruktur

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Zulässige Vergleiche:** `is`, `is_not`
- **Zulässige Werte:** `opted_in`, `subscribed`, `unsubscribed`

### Filter für zuletzt verwendete App

Dieser Filter ermöglicht es Ihnen, basierend darauf zu segmentieren, wann die:der Nutzer:in die App zuletzt verwendet hat. Diese Filter enthalten zwei Felder:

#### Filterstruktur
```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Zulässige Vergleiche:** `after`, `before`
- **Zulässige Werte:** Datetime (ISO 8601 String)

### Hinweise

Verbundene Zielgruppen können Nutzer:innen nicht nach Standardattributen, angepassten Events, Segmenten oder Nachrichten-Engagement-Events filtern. Um diese Filter zu verwenden, empfehlen wir, sie in ein Zielgruppen-Segment zu integrieren und dieses Segment dann im `segment_id`-Parameter für den [`/messages/send`-Endpunkt]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters) anzugeben. Bei der Verwendung anderer Endpunkte müssen Sie das Segment zunächst zur API-getriggerten Kampagne oder zum Canvas im Braze-Dashboard hinzufügen.