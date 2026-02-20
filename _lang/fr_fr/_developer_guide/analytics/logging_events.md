---
nav_title: Consigner un événement personnalisé
article_title: Enregistrer des événements personnalisés via le SDK de Braze
page_order: 3.1
description: "Découvrez comment enregistrer des événements personnalisés via le SDK de Braze."

---

# Consigner un événement personnalisé

> Découvrez comment enregistrer des événements personnalisés via le SDK de Braze.

{% alert note %}
Pour les SDK wrapper non répertoriés, utilisez plutôt la méthode native Android ou Swift correspondante.
{% endalert %}

## Enregistrement d'un événement personnalisé

Pour enregistrer un événement personnalisé, utilisez la méthode d'enregistrement des événements suivante.

{% tabs %}
{% tab web %}
Pour une implémentation standard du SDK Web, vous pouvez utiliser la méthode suivante :

```javascript
braze.logCustomEvent("YOUR_EVENT_NAME");
```

Si vous souhaitez utiliser Google Tag Manager à la place, vous pouvez utiliser le type d'étiquette **Custom Event** pour appeler la [méthode`logCustomEvent` ](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent) et envoyer des événements personnalisés à Braze, en incluant éventuellement des propriétés d'événement personnalisées. Pour ce faire :

1. Saisissez le **nom de l'événement** en utilisant une variable ou en tapant un nom d'événement.
2. Utilisez le bouton **Ajouter une ligne** pour ajouter des propriétés d'événement.

![Une boîte de dialogue affichant les paramètres de configuration de la balise d’action de Braze. Les paramètres inclus sont le « type de balise » (événement personnalisé), « nom d’événement » (clic de bouton) et les « propriétés de l’événement ».]({% image_buster /assets/img/web-gtm/gtm-custom-event.png %})
{% endtab %}

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

{% tab flutter %}
```dart
braze.logCustomEvent('YOUR_EVENT_NAME');
```
{% endtab %}

{% tab infillion %}
Si vous avez intégré des [balises Infillion](https://infillion.com/software/beacons/) dans votre application Android, vous pouvez éventuellement utiliser `visit.getPlace()` pour enregistrer des événements spécifiques à l'emplacement/localisation. `requestImmediateDataFlush` vérifie que votre événement sera enregistré même si votre application est en arrière-plan.

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

{% tab react native %}
```javascript
Braze.logCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}

{% tab roku %}
```brightscript
m.Braze.logEvent("YOUR_EVENT_NAME")
```
{% endtab %}

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("YOUR_EVENT_NAME");
```
{% endtab %}
{% endtabs %}

## Ajouter des propriétés de métadonnées

Lorsque vous enregistrez un événement personnalisé, vous avez la possibilité d'ajouter des métadonnées sur cet événement personnalisé en transmettant un objet de propriétés avec l'événement. Les propriétés sont définies comme des paires clé-valeur. Les clés sont des chaînes de caractères et les valeurs peuvent être `string`, `numeric`, `boolean`, [`Date`](http://www.w3schools.com/jsref/jsref_obj_date.asp) des objets, des tableaux ou des objets JSON imbriqués.

Pour ajouter des propriétés d'événement, utilisez la méthode d'enregistrement des événements suivante.

{% tabs %}
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

{% tab flutter %}
```dart
braze.logCustomEvent('custom_event_with_properties', properties: {
    'key1': 'value1',
    'key2': ['value2', 'value3'],
    'key3': false,
});
```
{% endtab %}

{% tab react native %}
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

{% tab unity %}
```csharp
AppboyBinding.LogCustomEvent("event name", properties(Dictionary<string, object>));
```
{% endtab %}
{% endtabs %}

{% alert important %}
Les clés `time` et `event_name` sont réservées et ne peuvent pas être utilisées comme propriétés d'événement personnalisé.
{% endalert %}

## Bonnes pratiques

Il y a trois vérifications importantes à effectuer pour que vos propriétés d'événement personnalisé soient enregistrées comme prévu :

* [Déterminer les événements qui sont enregistrés](#verify-events)
* [Vérifier le journal](#verify-log)
* [Vérifier les valeurs](#verify-values)

Plusieurs propriétés peuvent être consignées chaque fois qu’un événement personnalisé est journalisé.

### Vérifier les événements

Vérifiez auprès de vos développeurs quelles propriétés d’événement sont suivies. Gardez à l’esprit que toutes les propriétés de l'événement sont sensibles à la casse. Pour plus d'informations sur le suivi des événements personnalisés, consultez ces articles en fonction de votre plateforme :

* [Android]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=android)
* [iOS]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=swift)
* [Web]({{site.baseurl}}/developer_guide/analytics/logging_events/?tab=web)

### Vérifier le journal

Pour confirmer que les propriétés de l'événement sont bien suivies, vous pouvez afficher toutes les propriétés de l'événement à partir de la page **Événements personnalisés**.

1. Sélectionnez **Paramètres des données** > **Événements personnalisés**.
2. Emplacement/localisation de votre événement personnalisé dans la liste.
3. Pour votre événement, sélectionnez **Gérer les propriétés** pour afficher les noms des propriétés associées à un événement.

### Vérifier les valeurs

Après avoir [ajouté votre utilisateur en tant qu'utilisateur test]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/#adding-test-users), suivez les étapes suivantes pour vérifier vos valeurs : 

1. Exécutez l'événement personnalisé dans l'application.
2. Attendez environ 10 secondes pour que les données se déversent.
3. Actualisez le [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/event_user_log_tab/) pour afficher l'événement personnalisé et la valeur de la propriété d'événement qui lui a été transmise.
