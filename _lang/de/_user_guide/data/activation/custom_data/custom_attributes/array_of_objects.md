---
nav_title: Array von Objekten
article_title: Objekt-Array
alias: "/array_of_objects/"
page_order: 0
page_type: reference
description: "Dieser referenzierte Artikel behandelt die Verwendung eines Arrays von Objekten als Datentyp für angepasste Attribute, einschließlich Einschränkungen und Anwendungsbeispielen." 
---

# Array von Objekten

> Auf dieser Seite erfahren Sie, wie Sie ein Array von Objekten verwenden können, um verwandte Attribute zu gruppieren. Sie können z.B. eine Gruppe von Haustierobjekten, Liedobjekten und Kontoobjekten haben, die alle zu einem Nutzer:innen gehören. Diese Objekt-Arrays können verwendet werden, um Ihr Messaging mit Liquid zu personalisieren oder Segmente von Zielgruppen zu erstellen, wenn irgendein Element innerhalb eines Objekts den Kriterien entspricht.

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## Beschränkungen

- Arrays von Objekten sind für angepasste Attribute gedacht, die über die API gesendet werden. CSV-Uploads werden nicht unterstützt. Dies liegt daran, dass Kommas in der CSV-Datei als Spaltentrennzeichen interpretiert werden und Kommas in Werten zu Fehlern beim Parsen führen. 
- Arrays von Objekten haben keine Begrenzung der Anzahl von Artikeln, aber eine maximale Größe von 100 KB.
- Nicht alle Braze Partner unterstützen Arrays von Objekten. Lesen Sie in der [Dokumentation des Partners]({{site.baseurl}}/partners/home) nach, ob die Integration dieses Feature unterstützt.

Das Aktualisieren oder Entfernen von Artikeln in einem Array erfordert die Identifizierung des Artikels durch Schlüssel und Wert. Daher sollten Sie für jeden Artikel im Array einen eindeutigen Bezeichner angeben. Die Eindeutigkeit bezieht sich nur auf das Array und ist nützlich, wenn Sie bestimmte Objekte aus Ihrem Array aktualisieren und entfernen möchten. Dies wird von Braze nicht durchgesetzt.

{% alert tip %}
Weitere Informationen zur Verwendung von Objekt-Arrays für Nutzer:innen-Attribute finden Sie unter [Nutzer:innen-Attribute]({{site.baseurl}}/api/objects_filters/user_attributes_object).
{% endalert %}

## API Beispiel

{% tabs local %}
{% tab Create %}

Im Folgenden finden Sie ein `/users/track` Beispiel mit einem `pets` Array. Um die Eigenschaften der Haustiere zu erfassen, senden Sie eine API-Anfrage, die `pets` als Array von Objekten auflistet. Beachten Sie, dass jedem Objekt eine eindeutige `id` zugewiesen wurde, auf die Sie später bei Updates referenzieren können.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Add %}

Fügen Sie dem Array mit dem Operator `$add` einen weiteren Artikel hinzu. Das folgende Beispiel zeigt das Hinzufügen von drei weiteren Haustierobjekten zum `pets` Array des Nutzers:innen.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$add": [
          {
            "id": 3,
            "type": "dog",
            "breed": "corgi",
            "name": "Doug"
          },
          {
            "id": 4,
            "type": "fish",
            "breed": "salmon",
            "name": "Larry"
          },
           {
            "id": 5,
            "type": "bird",
            "breed": "parakeet",
            "name": "Mary"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Update %}

Aktualisieren Sie Werte für bestimmte Objekte innerhalb eines Arrays mit dem Parameter `_merge_objects` und dem Operator `$update`. Ähnlich wie bei Updates von einfachen [, verschachtelten]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) Objekten [mit angepassten Attributen]({{site.baseurl}}/nested_custom_attribute_support/#api-request-body) wird hier eine tiefe Zusammenführung durchgeführt.

Beachten Sie, dass `$update` nicht verwendet werden kann, um eine verschachtelte Eigenschaft aus einem Objekt innerhalb eines Arrays zu entfernen. Dazu müssen Sie den gesamten Artikel aus dem Array entfernen und dann das Objekt ohne diesen speziellen Schlüssel hinzufügen (mit einer Kombination aus `$remove` und `$add`).

Das folgende Beispiel zeigt das Update der Eigenschaft `breed` auf `goldfish` für das Objekt mit einer `id` von `4`. Dieses Anfrage-Beispiel aktualisiert auch das Objekt mit `id` gleich `5` mit einem neuen `name` von `Annette`. Da der Parameter `_merge_objects` auf `true` gesetzt ist, bleiben alle anderen Felder für diese beiden Objekte gleich.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```

{% alert warning %}
Sie müssen `_merge_objects` auf true setzen, sonst werden Ihre Objekte überschrieben. `_merge_objects` ist standardmäßig false.
{% endalert %}

{% endtab %}
{% tab Remove %}

Entfernen Sie Objekte aus einem Array mit dem Operator `$remove` in Kombination mit einem passenden Schlüssel (`$identifier_key`) und Wert (`$identifier_value`).

Das folgende Beispiel zeigt, wie Sie ein beliebiges Objekt aus dem Array `pets` entfernen, das ein `id` mit dem Wert `1`, ein `id` mit dem Wert `2` und ein `type` mit dem Wert `dog` hat. Wenn es mehrere Objekte mit dem Wert `type` von `dog` gibt, werden alle passenden Objekte entfernt.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

### Zeitstempel

Wenn Sie Felder wie Zeitstempel in ein Array von Objekten aufnehmen, verwenden Sie das Format `$time` anstelle von einfachen Strings oder Unix-Epochen-Ganzzahlen.

```json
{
  "attributes": [
    {
      "external_id": "user123",
      "purchases": [
        {
          "item_name": "T-shirt",
          "price": 19.99,
          "purchase_time": {
            "$time": "2020-05-28"
          }
        }
      ]
    }
  ]
}
```

{% alert tip %}
Weitere Informationen finden Sie unter [Verschachtelte angepasste Attribute]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support).
{% endalert %}

## SDK Beispiel

{% tabs local %}
{% tab Android SDK %}
{% subtabs %}
{% subtab Create %}
```kotlin
val json = JSONArray()
    .put(JSONObject()
        .put("id", 1)
        .put("type", "dog")
        .put("breed", "beagle")
        .put("name", "Gus"))
    .put(JSONObject()
        .put("id", 2)
        .put("type", "cat")
        .put("breed", "calico")
        .put("name", "Gerald")
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json)
}
```
{% endsubtab %}

{% subtab Add %}
```kotlin
val json = JSONObject()
    .put("\$add", JSONArray()
        .put(JSONObject()
            .put("id", 3)
            .put("type", "dog")
            .put("breed", "corgi")
            .put("name", "Doug"))
        .put(JSONObject()
            .put("id", 4)
            .put("type", "fish")
            .put("breed", "salmon")
            .put("name", "Larry"))
        .put(JSONObject()
            .put("id", 5)
            .put("type", "bird")
            .put("breed", "parakeet")
            .put("name", "Mary")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Update %}
```kotlin
val json = JSONObject()
    .put("\$update", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 4)
            .put("\$new_object", JSONObject()
                .put("breed", "goldfish")
            )
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 5)
            .put("\$new_object", JSONObject()
                .put("name", "Annette")
            )
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}

{% subtab Delete %}
```kotlin
val json = JSONObject()
    .put("\$remove", JSONArray()
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 1)
        )
        .put(JSONObject()
            .put("\$identifier_key", "id")
            .put("\$identifier_value", 2)
        )
        .put(JSONObject()
            .put("\$identifier_key", "type")
            .put("\$identifier_value", "dog")
        )
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("pets", json, true)
}
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Swift SDK %}
{% subtabs %}
{% subtab Create %}
```swift
let json: [[String: Any?]] = [
  [
    "id": 1,
    "type": "dog",
    "breed": "beagle",
    "name": "Gus"
  ],
  [
    "id": 2,
    "type": "cat",
    "breed": "calico",
    "name": "Gerald"
  ]
]

braze.user.setCustomAttribute(key: "pets", array: json)
```
{% endsubtab %}

{% subtab Add %}
```swift
let json: [String: Any?] = [
  "$add": [
    [
      "id": 3,
      "type": "dog",
      "breed": "corgi",
      "name": "Doug"
    ],
    [
      "id": 4,
      "type": "fish",
      "breed": "salmon",
      "name": "Larry"
    ],
    [
      "id": 5,
      "type": "bird",
      "breed": "parakeet",
      "name": "Mary"
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Update %}
```swift
let json: [String: Any?] = [
  "$update": [
    [
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": [
        "breed": "goldfish"
      ]
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": [
        "name": "Annette"
      ]
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}

{% subtab Delete %}
```swift
let json: [String: Any?] = [
  "$remove": [
    [
      "$identifier_key": "id",
      "$identifier_value": 1,
    ],
    [
      "$identifier_key": "id",
      "$identifier_value": 2,
    ],
    [
      "$identifier_key": "type",
      "$identifier_value": "dog",
    ]
  ]
]

braze.user.setCustomAttribute(key: "pets", dictionary: json, merge: true)
```
{% endsubtab %}
{% endsubtabs %}

{% alert important %}
Verschachtelte angepasste Attribute werden von AppboyKit nicht unterstützt.
{% endalert %}
{% endtab %}

{% tab Web SDK %}
{% subtabs local %}
{% subtab Create %}
```javascript
import * as braze from "@braze/web-sdk";
const json = [{
  "id": 1,
  "type": "dog",
  "breed": "beagle",
  "name": "Gus"
}, {
  "id": 2,
  "type": "cat",
  "breed": "calico",
  "name": "Gerald"
}];
braze.getUser().setCustomUserAttribute("pets", json);
```
{% endsubtab %}

{% subtab Add %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$add": [{
    "id":  3,
    "type":  "dog",
    "breed":  "corgi",
    "name":  "Doug",
  }, {
    "id":  4,
    "type":  "fish",
    "breed":  "salmon",
    "name":  "Larry",
  }, {
    "id":  5,
    "type":  "bird",
    "breed":  "parakeet",
    "name":  "Mary",
  }]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Update %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$update": [
    {
      "$identifier_key": "id",
      "$identifier_value": 4,
      "$new_object": {
        "breed": "goldfish"
      }
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 5,
      "$new_object": {
        "name": "Annette"
      }
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}

{% subtab Delete %}
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "$remove": [
    {
      "$identifier_key": "id",
      "$identifier_value": 1,
    },
    {
      "$identifier_key": "id",
      "$identifier_value": 2,
    },
    {
      "$identifier_key": "type",
      "$identifier_value": "dog",
    }
  ]
};
braze.getUser().setCustomUserAttribute("pets", json, true);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

## Liquid-Templates

Sie können dieses `pets` Array verwenden, um eine Nachricht zu personalisieren. Das folgende Liquid Template-Beispiel zeigt, wie Sie die angepassten Attribut-Objekteigenschaften referenzieren, die aus der vorangegangenen API-Anfrage gespeichert wurden, und sie in Ihren Nachrichten verwenden.

{% raw %}
```liquid
{% assign pets = {{custom_attribute.${pets}}} %} 
 
{% for pet in pets %}
I have a {{pet.type}} named {{pet.name}}! They are a {{pet.breed}}.
{% endfor %} 
```
{% endraw %}

In diesem Szenario können Sie Liquid verwenden, um eine Schleife durch das Array `pets` zu ziehen und für jedes Haustier eine Anweisung auszudrucken. [Weisen Sie]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) dem angepassten Attribut `pets` [eine Variable zu]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/#assigning-variables) und verwenden Sie die Punktnotation, um auf Eigenschaften eines Objekts zuzugreifen. Geben Sie den Namen des Objekts an, gefolgt von einem Punkt `.`, gefolgt von dem Namen der Eigenschaft.

## Segmentierung

Bei der Segmentierung von Nutzern:innen auf der Grundlage von Objekt-Arrays kommt ein Nutzer für das Segment in Frage, wenn irgendein Objekt in dem Array den Kriterien entspricht. 

Erstellen Sie ein neues Segment und wählen Sie **Verschachteltes angepasstes Attribut** als Filter. Suchen Sie dann den Namen Ihres Objekt-Arrays und wählen Sie ihn aus.

![Filter nach Array von Objekten.]({% image_buster /assets/img_archive/array_of_objects_segmenting_1.gif %})

Verwenden Sie die Punktschreibweise, um anzugeben, welches Feld im Array der Objekte Sie verwenden möchten. Beginnen Sie das Textfeld mit einem leeren Satz eckiger Klammern `[]`, um Braze mitzuteilen, dass Sie in einem Array von Objekten suchen. Fügen Sie danach einen Punkt `.` ein, gefolgt von dem Namen des Feldes, das Sie verwenden möchten.

Wenn Sie beispielsweise das Objekt-Array `pets` anhand des Feldes `type` filtern möchten, geben Sie `[].type` ein und wählen aus, nach welchem Haustiertyp Sie filtern möchten, z. B. `snake`.

![Filter nach Haustierart ist gleich Schlange.]({% image_buster /assets/img_archive/array_of_objects_segmenting_3.png %})

Oder Sie könnten nach Haustieren filtern, die eine `type` von `dog` haben. Hier hat ein Nutzer:innen mindestens einen Hund, so dass er sich für das Segment "alle Nutzer:innen, die mindestens ein Haustier vom Typ Hund haben" qualifiziert.

![Filter nach Haustierart ist gleich Hund.]({% image_buster /assets/img_archive/array_of_objects_segmenting_2.png %})

### Ebenen der Verschachtelung

Sie können ein Segment mit bis zu einer Ebene der Array-Schachtelung (Array innerhalb eines anderen Arrays) erstellen. Mit den folgenden Attributen können Sie zum Beispiel ein Segment für `pets[].name` enthält `Gus` erstellen, aber kein Segment für `pets[].nicknames[]` enthält `Gugu`.

{% raw %}
```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus",
          "nicknames": [
            "Gugu",
            "Gusto"
          ]
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald",
          "nicknames": [
            "GeGe",
            "Gerry"
          ]
        }
      ]
    }
  ]
}
```
{% endraw %}

## Datenpunkte

Datenpunkte werden unterschiedlich protokolliert, je nachdem, ob Sie eine Eigenschaft erstellen, aktualisieren oder entfernen.

{% tabs local %}
{% tab Create %}

Die Erstellung eines neuen Arrays protokolliert einen Datenpunkt für jedes Attribut in einem Objekt. Dieses Beispiel kostet acht Datenpunkte - jedes Haustierobjekt hat vier Attribute und es gibt zwei Objekte.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": [
        {
          "id": 1,
          "type": "dog",
          "breed": "beagle",
          "name": "Gus"
        },
        {
          "id": 2,
          "type": "cat",
          "breed": "calico",
          "name": "Gerald"
        }
      ]
    }
  ]
}
```
{% endtab %}
{% tab Update %}

Beim Update eines bestehenden Arrays wird für jede hinzugefügte Eigenschaft ein Datenpunkt protokolliert. Dieses Beispiel kostet zwei Datenpunkte, da es nur eine Eigenschaft in jedem der beiden Objekte aktualisiert.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "pets": {
        "$update": [
          {
            "$identifier_key": "id",
            "$identifier_value": 4,
            "$new_object": {
              "breed": "goldfish"
            }
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 5,
            "$new_object": {
              "name": "Annette"
            }
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% tab Remove %}

Das Entfernen eines Objekts aus einem Array protokolliert einen Datenpunkt für jedes Entfernungskriterium, das Sie senden. Dieses Beispiel kostet drei Datenpunkte, auch wenn Sie mit dieser Anweisung möglicherweise mehrere Hunde entfernen.

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "pets": {
        "$remove": [
          // Remove by ID
          {
            "$identifier_key": "id",
            "$identifier_value": 1
          },
          {
            "$identifier_key": "id",
            "$identifier_value": 2
          },
          // Remove any dog
          {
            "$identifier_key": "type",
            "$identifier_value": "dog"
          }
        ]
      }
    }
  ]
}
```
{% endtab %}
{% endtabs %}

