---
nav_title: "Verbundenes Publikum Filter &amp; Objekt"
article_title: API Verbundenes Publikumsobjekt
page_order: 3
page_type: reference
description: "Dieser Artikel erklärt die verschiedenen Komponenten des Objekts Connected Audience und die Filter, die es erstellen."

---

# Verbundenes Publikumsobjekt

> Ein verbundenes Audience-Objekt ist ein Selektor, der das Publikum identifiziert, an das die Nachricht gesendet werden soll. 

Dieses Objekt besteht entweder aus einem einzelnen verbundenen Publikumsfilter oder aus mehreren verbundenen Publikumsfiltern in einem logischen Ausdruck unter Verwendung der Operatoren `AND` oder `OR`.

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

## Verbundene Publikumsfilter

Wenn Sie mehrere benutzerdefinierte Attributfilter kombinieren, entsteht ein Filter für verbundene Zielgruppen, der in Kombination mit den Operatoren `AND` und `OR` einen Filter für verbundene Zielgruppen erzeugt.

### Benutzerdefinierter Attributfilter

Mit diesem Filter können Sie auf der Grundlage eines benutzerdefinierten Attributs eines Benutzers segmentieren. Diese Filter enthalten bis zu drei Felder:

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

Der Datentyp des benutzerdefinierten Attributs bestimmt die Vergleiche, die für einen bestimmten Filter gültig sind.

| Benutzerdefiniertes Attribut Typ | Erlaubte Vergleiche |
| ---------------------| --------------- |
| String | `equals`, `not_equal`, `matches_regex`, `does_not_match_regex`, `exists`, `does_not_exist` |
| Array | `includes_value`, `does_not_include_value`, `exists`, `does_not_exist` |
| Numerisch | `equals`, `not_equal`, `greater_than`, `greater_than_or_equal_to`, `less_than`, `less_than_or_equal_to`, `exists`, `does_not_exist` |
| Boolesche | `equals`, `does_not_equal`, `exists`, `does_not_exist` |
| Zeit | `less_than_x_days_ago`, `greater_than_x_days_ago`, `less_than_x_days_in_the_future`, `greater_than_x_days_in_the_future`, `after`, `before`, `exists`, `does_not_exist` | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Vorbehalte beim Attributvergleich

| Vergleich | Zusätzliche Überlegungen |
| --- | --- |
| `value` | `value` ist nicht erforderlich, wenn Sie die Vergleiche `exists` oder `does_not_exist` verwenden. `value` muss ein ISO 8601 datetime string sein, wenn Sie die Vergleiche `before` und `after` verwenden. |
|`matches_regex` | Wenn Sie den Vergleich `matches_regex` verwenden, muss der übergebene Wert eine Zeichenkette sein. Weitere Informationen über die Verwendung regulärer Ausdrücke mit Braze finden Sie unter [Reguläre Ausdrücke]({{site.baseurl}}/user_guide/engagement_tools/segments/regex/#regex-with-braze) und [benutzerdefinierte Attributdatentypen]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-data-types). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Beispiel für ein benutzerdefiniertes Attribut

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
### Push-Abonnement-Filter

Mit diesem Filter können Sie auf der Grundlage des Push-Abonnementstatus eines Benutzers segmentieren.

#### Filtergehäuse

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

### Filter für E-Mail-Abonnements

Mit diesem Filter können Sie nach dem Status des E-Mail-Abonnements eines Benutzers segmentieren.

#### Filtergehäuse

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

### Zuletzt verwendeter App-Filter

Mit diesem Filter können Sie eine Segmentierung vornehmen, die darauf basiert, wann der Nutzer die App zuletzt verwendet hat. Diese Filter enthalten zwei Felder:

#### Filtergehäuse
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
- **Erlaubte Werte:** datetime (ISO 8601 string)

