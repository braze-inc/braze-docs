---
nav_title: "Katalogauswahlobjekt"
article_title: API-Katalog-Auswahlobjekt
page_order: 12
page_type: reference
description: "Dieser Referenzartikel erläutert die verschiedenen Komponenten des Objekts zur Auswahl des Katalogs."
tool: Catalogs

---

# Katalogauswahlobjekt

> Beim Erstellen einer Katalogauswahl können Sie ein Auswahlobjekt bereitstellen, um die Filter-, Sortier- und Einschränkungskriterien für die aus Ihrem Katalog zurückgegebenen Artikel zu definieren.

Mit`selection`diesem Objekt können Sie festlegen, welche Artikel aus Ihrem Katalog anhand von Filtern ausgewählt werden sollen, wie sie sortiert werden sollen und wie viele Ergebnisse zurückgegeben werden sollen. Verwenden Sie dieses Objekt, wenn Sie Katalogauswahlen über die API erstellen.

## Objektkörper

```json
{
  "selection": {
    "name": "Sale",
    "description": "Sales Collection",
    "external_id": "12345678",
    "source": "Shopify",
    "filters": [
      {
        "field": "collection",
        "operator": "includes value",
        "value": "Best Seller"
      },
      {
        "field": "collection",
        "operator": "does not include value",
        "value": "Sale"
      }
    ],
    "results_limit": 5,
    "sort_field": "id",
    "sort_order": "asc"
  }
}
```

## Objektdetails

| Schlüssel | Erforderlich | Datentyp | Beschreibung |
| --- | -------- | --------- | ----------- |
| `name` | Erforderlich | String | Der Name der Katalogauswahl, die ausgewählt wurde. |
| `description` | Optional | String | Eine Beschreibung der Auswahl der Kataloge. |
| `external_id` | Erforderlich | String | Ein eindeutiger Bezeichner für die Auswahl. |
| `source` | Erforderlich | String | Die Quelle der Katalogdaten. Für Shopify-Kataloge stellen Sie dies bitte auf ein`"Shopify"`. Für Nicht-Shopify-Kataloge verwenden Sie bitte einen beschreibenden String wie`"custom"`  oder den Namen Ihrer Integration. |
| `filters` | Optional | Array von Objekten | Ein Array von Filtern, die auf die Artikel angewendet werden sollen. Sie können bis zu vier Filter pro Anfrage festlegen. Wenn keine Filter angegeben werden, werden alle Artikel aus dem Katalog berücksichtigt. |
| `results_limit` | Optional | Integer | Die maximale Anzahl der zurückzugebenden Ergebnisse. Es muss sich um eine Zahl zwischen 1 und 50 handeln. |
| `sort_field` | Optional | String | Das Feld, nach dem die Ergebnisse sortiert werden sollen. Dies muss mit `sort_order`kombiniert werden. Wenn sowohl`sort_field`  als auch  `sort_order`nicht vorhanden sind, werden die Ergebnisse in zufälliger Reihenfolge zurückgegeben. |
| `sort_order` | Optional | String | Die Reihenfolge, in der die Ergebnisse sortiert werden sollen. Zulässige Werte sind`"asc"`(aufsteigend) oder`"desc"`(absteigend). Dies muss mit `sort_field`kombiniert werden. Wenn sowohl`sort_field`  als auch  `sort_order`nicht vorhanden sind, werden die Ergebnisse in zufälliger Reihenfolge zurückgegeben. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Filterobjekt

Jedes Filterobjekt im`filters`Array enthält die in der folgenden Tabelle beschriebenen Felder.

| Schlüssel | Erforderlich | Datentyp                                   | Beschreibung |
| --- | -------- | ------------------------------------------- | ----------- |
| `field`    | Erforderlich | String                                      | Das Katalogfeld, mit dem der Filter ausgelöst wird. |
| `operator` | Erforderlich | String                                      | Der Vergleichsoperator, der für die Filterung verwendet werden soll. Beispiele hierfür sind`"includes value"`und`"does not include value"`. |
| `value`    | Erforderlich | Variiert (String, Zahl, Boolescher Wert, Zeitangabe)     | Der Wert, mit dem verglichen werden soll. Dies muss mit dem Datentyp des zugrunde liegenden Katalogfelds übereinstimmen (z. B. String, Zahl, Boolescher Wert, Zeit). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Die API unterstützt maximal vier Filter pro Auswahlanfrage. Im Braze-Dashboard können Sie bis zu 10 Filter pro Auswahl hinzufügen. Filter werden in der Reihenfolge angewendet, in der sie im Array erscheinen.
{% endalert %}
