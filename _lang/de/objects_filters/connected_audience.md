---
nav_title: "Verbundenes Publikum Filter &amp; Objekt"
article_title: API Verbundenes Zielgruppen-Objekt
page_order: 3
page_type: reference
description: "Dieser Artikel erklärt die verschiedenen Komponenten des Objekts \"Verbundene Zielgruppe\" und die Filter, die es erstellen."

---

# Verbundenes Objekt der Zielgruppe

> Ein verbundenes Zielgruppen-Objekt ist ein SELEKTOR, der die Zielgruppe identifiziert, an die die Nachricht gesendet werden soll. 

Dieses Objekt besteht entweder aus einem einzelnen verbundenen Zielgruppen-Filter oder aus mehreren verbundenen Zielgruppen-Filtern in einem logischen Ausdruck unter Verwendung der Operatoren `AND` oder `OR`.

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

Die Kombination mehrerer angepasster Attribut-Filter ergibt einen Zielgruppen-Filter, der in Kombination mit den Operatoren `AND` und `OR` einen Filter für eine verbundene Zielgruppe erzeugt.

### Angepasste Attribute Filter

Mit diesem Filter können Sie auf der Grundlage eines angepassten Attributs eines Nutzers:innen segmentieren. Diese Filter enthalten bis zu drei Felder:

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

#### Erlaubte Vergleiche nach Datentyp

Der Datentyp des angepassten Attributs bestimmt die Vergleiche, die für einen bestimmten Filter gültig sind.

| Angepasstes Attribut Typ | Erlaubte Vergleiche |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numerisch | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolesch | `equals`, `does_not_equal`, `exists`, `does_not_exist` |
| Uhrzeit | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Vorbehalte beim Vergleich von Attributen

| Vergleich | Zusätzliche Überlegungen |
| --- | --- |
| `value` | Die Angabe `value` ist nicht erforderlich, wenn Sie die Vergleiche `exists` oder `does_not_exist` verwenden. `value` muss ein ISO 8601 datetime String sein, wenn Sie die Vergleiche `before` und `after` verwenden. |
|`matches_regex` | Wenn Sie den Vergleich `matches_regex` verwenden, muss der übergebene Wert ein String sein. Weitere Informationen über die Verwendung regulärer Ausdrücke mit Braze finden Sie unter [Reguläre Ausdrücke]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) und [angepasste Attribut-Datentypen]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
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

{
  "custom_attribute":
  {
    "custom_attribute_name": "favorite_foods",
    "comparison": "includes_value",
    "value": "pizza"
  }
}

{
  "custom_attribute":
  {
    "custom_attribute_name": "last_purchase_time",
    "comparison": "less_than_x_days_ago",
    "value": 2
  }
}
```
### Push-Filter für Abos

Dieser Filter erlaubt Ihnen eine Segmentierung auf der Grundlage des Status des Push-Abos eines Nutzers:innen.

#### Filter Gehäuse

```json
{
  "push_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Erlaubte Vergleiche:** `is`, `is_not`
- **Erlaubte Werte:** `opted_in`, `subscribed`, `unsubscribed`

### E-Mail Abo Filter

Mit diesem Filter können Sie auf der Grundlage des Status des E-Mail-Abos eines Nutzers:innen segmentieren.

#### Filter Gehäuse

```json
{
  "email_subscription_status":
  {
    "comparison": (String) one of the following allowed comparisons,
    "value": (String) one of the following allowed values
  }
}
```

- **Erlaubte Vergleiche:** `is`, `is_not`
- **Erlaubte Werte:** `opted_in`, `subscribed`, `unsubscribed`

### Zuletzt verwendeter App Filter

Dieser Filter lässt eine Segmentierung zu, die darauf basiert, wann der Nutzer:innen die App das letzte Mal benutzt hat. Diese Filter enthalten zwei Felder:

#### Filter Gehäuse
```json
{
  "last_used_app":
  {
    "comparison": (String) one of the allowed comparisons listed,
    "value": (String) the value to be compared using the provided comparison
  }
}
```

- **Erlaubte Vergleiche:** `after`, `before`
- **Zulässige Werte:** datetime (ISO 8601 String)

### Überlegungen

Verbundene Zielgruppen können Benutzer nicht nach Standardattributen, angepassten Events, Segmenten oder Customer-Engagement-Events filtern. Um diese Filter zu verwenden, empfehlen wir, sie in ein Zielgruppen-Segment einzubinden und dieses Segment dann im Parameter `segment_id` für den [Endpunkt`/messages/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages#request-parameters) anzugeben. Wenn Sie andere Endpunkte verwenden, müssen Sie das Segment zunächst im Braze-Dashboard zur API-getriggerten Kampagne oder zum Canvas hinzufügen.
