---
nav_title: Enregistrement des événements personnalisés
article_title: "Enregistrement d'événements personnalisés via le SDK de Braze"
page_order: 3.1
description: "Découvrez comment enregistrer des événements personnalisés via le SDK de Braze."

---

# Journalisation des événements personnalisés

> Découvrez comment enregistrer des événements personnalisés via le SDK de Braze.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

## Enregistrement d'un événement personnalisé

Pour enregistrer un événement personnalisé, utilisez la méthode d'enregistrement des événements suivante.

{% tabs %}
{% tab android %}
Pour les versions natives d'Android, vous pouvez utiliser la méthode suivante :

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME);
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent(YOUR_EVENT_NAME)
```
{% endsubtab %}
{% endsubtabs %}

Si vous avez intégré des [balises Infillion](https://infillion.com/software/beacons/) dans votre application, vous pouvez également utiliser `visit.getPlace()` pour enregistrer des événements spécifiques à l'emplacement/localisation. `requestImmediateDataFlush` vérifie que votre événement sera enregistré même si votre application est en arrière-plan.

{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace());
Braze.getInstance(context).requestImmediateDataFlush();
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).logCustomEvent("Entered " + visit.getPlace())
Braze.getInstance(context).requestImmediateDataFlush()
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(name: "YOUR_EVENT_NAME")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR_EVENT_NAME"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
Pour une implémentation standard du SDK Web, vous pouvez utiliser la méthode suivante :

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Si vous souhaitez utiliser Google Tag Manager à la place, vous pouvez utiliser le type d'étiquette **Custom Event** pour appeler la [méthode`logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) et envoyer des événements personnalisés à Braze, en incluant éventuellement des propriétés d'événement personnalisées. Pour ce faire :

1. Saisissez le **nom de l'événement** en utilisant une variable ou en tapant un nom d'événement.
2. Utilisez le bouton **Ajouter une ligne** pour ajouter des propriétés d'événement.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont le "type d'étiquette" (événement personnalisé), le "nom de l'événement" (clic sur un bouton) et les "propriétés d'événement".]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

{% tab Flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab React native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab Unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab moteur irréel %}
```cpp
UBraze->LogCustomEvent(TEXT("YOUR_EVENT_NAME"));
```
{% endtab %}
{% endtabs %}

## Ajouter des propriétés de métadonnées

Lorsque vous enregistrez un événement personnalisé, vous avez la possibilité d'ajouter des métadonnées sur cet événement personnalisé en transmettant un objet de propriétés avec l'événement. Les propriétés sont définies comme des paires clé-valeur. Les clés sont des chaînes de caractères et les valeurs peuvent être des objets `string`, `numeric`, `boolean` ou [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp).

Pour ajouter des propriétés d'événement, utilisez la méthode d'enregistrement des événements suivante.

{% tabs %}
{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.logCustomEvent("YOUR-EVENT-NAME",
    new BrazeProperties(new JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", new Date())
        .put("or", new JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", new JSONObject()
            .put("deeply", new JSONArray()
                .put("nested")
                .put("json"))
        )
));
```
{% endsubtab %}
{% subtab kotlin %}
```kotlin
Braze.logCustomEvent("YOUR-EVENT-NAME",
    BrazeProperties(JSONObject()
        .put("you", "can")
        .put("pass", false)
        .put("orNumbers", 42)
        .put("orDates", Date())
        .put("or", JSONArray()
            .put("any")
            .put("array")
            .put("here"))
        .put("andEven", JSONObject()
            .put("deeply", JSONArray()
                .put("nested")
                .put("json"))
        )
))
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.logCustomEvent(
  name: "YOUR-EVENT-NAME",
  properties: [
    "you": "can",
    "pass": false,
    "orNumbers": 42,
    "orDates": Date(),
    "or": ["any", "array", "here"],
    "andEven": [
      "deeply": ["nested", "json"]
    ]
  ]
)
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze logCustomEvent:@"YOUR-EVENT-NAME"
                       properties:@{
  @"you": @"can",
  @"pass": @(NO),
  @"orNumbers": @42,
  @"orDates": [NSDate date],
  @"or": @[@"any", @"array", @"here"],
  @"andEven": @{
    @"deeply": @[@"nested", @"json"]
  }
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab web %}
```javascript
braze.logCustomEvent("YOUR-EVENT-NAME", {
  you: "can", 
  pass: false, 
  orNumbers: 42,
  orDates: new Date(),
  or: ["any", "array", "here"],
  andEven: {
     deeply: ["nested", "json"]
  }
});
```
{% endtab %}

{% tab Flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab React native %}
```javascript
Braze.logCustomEvent("custom_event_with_properties", {
    key1: "value1",
    key2: ["value2", "value3"],
    key3: false,
});
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME", {"stringPropKey" : "stringPropValue", "intPropKey" : Integer intPropValue})
```
{% endtab %}

{% tab Unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}

{% tab moteur irréel %}
```cpp
TMap<FString, FString> Properties;
Properties.Add(TEXT("you"), TEXT("can"));
Properties.Add(TEXT("pass"), TEXT("false"));
Properties.Add(TEXT("orNumbers"), FString::FromInt(42));
Properties.Add(TEXT("orDates"), FDateTime::Now().ToString());
Properties.Add(TEXT("or"), TEXT("any,array,here")); // Arrays are stored as comma-separated strings
Properties.Add(TEXT("andEven"), TEXT("deeply:nested,json"));

UBraze->LogCustomEventWithProperties(TEXT("YOUR_EVENT_NAME"), Properties);
```
{% endtab %}
{% endtabs %}

{% alert important %}
Les clés `time` et `event_name` sont réservées et ne peuvent pas être utilisées comme propriétés d'événement personnalisé.
{% endalert %}
