---
nav_title: Erstellen von Feature-Flags
article_title: Erstellen von Feature-Flags
page_order: 20
description: "Dieser Referenzartikel beschreibt, wie Sie Feature-Flags erstellen, um die Einführung neuer Features zu koordinieren."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Erstellen von Feature-Flags

> Mit Feature-Flags können Sie Funktionen für eine ausgewählte Nutzergruppe remote aktivieren oder deaktivieren. Erstellen Sie ein neues Feature-Flag im des Braze-Dashboard. Geben Sie einen Namen und eine `ID`, eine Zielgruppe und einen Prozentsatz der Nutzer an, für die dieses Feature aktiviert werden soll. Dann können Sie mit der gleichen `ID` im Code Ihrer Anwendung oder Website bestimmte Teile Ihrer Geschäftslogik bedingt ausführen. Mehr über Feature-Flags und wie Sie sie in Braze verwenden können, erfahren Sie unter [Über Feature-Flags]({{site.baseurl}}/developer_guide/feature_flags/).

## Voraussetzungen

### SDK-Version

Wenn Sie Feature-Flags verwenden möchten, stellen Sie sicher, dass Ihre SDKs mit den folgenden Mindestversionen auf dem neuesten Stand sind:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Braze-Berechtigungen

Um Feature-Flags im Dashboard zu verwalten, müssen Sie entweder Administrator sein oder über die folgenden [Berechtigungen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) verfügen:

| Erlaubnis                                                                    | Was Sie tun können                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **Feature-Flags verwalten**                                                      | Betrachten, erstellen und bearbeiten Sie Feature-Flags.     |
| **Zugang zu Kampagnen, Leinwänden, Karten, Feature-Flags, Segmenten, Mediathek** | Sehen Sie sich die Liste der verfügbaren Funktionskennzeichen an. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Erstellen eines Feature-Flags

### Schritt 1: Neues Feature-Flag erstellen

Gehen Sie zu **Messaging** > **Funktionskennzeichen** und wählen Sie dann **Funktionskennzeichen erstellen**.

![Liste zuvor erstellter Feature-Flags im Braze-Dashboard]({% image_buster /assets/img/feature_flags/feature-flags-list.png %}){: style="max-width:75%"}

### Schritt 2: Details angeben

Geben Sie unter **Details** einen Namen, eine ID und eine Beschreibung für Ihr Feature-Flag ein.

| Feld        | Beschreibung                                                                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Name         | Ein von Menschen lesbarer Titel für Ihre Vermarkter und Administratoren.                                                                                                                                                       |
| ID           | Die eindeutige ID, die Sie in Ihrem Code verwenden werden, um zu prüfen, ob diese Funktion [für einen Benutzer aktiviert](#enabled) ist. Diese ID kann später nicht mehr geändert werden. Informieren Sie sich daher über unsere [bewährten Verfahren zur Benennung von IDs](#naming-conventions), bevor Sie fortfahren. |
| Beschreibung  | Eine optionale Beschreibung, die etwas Kontext über Ihr Feature-Flag liefert.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Schritt 3: Benutzerdefinierte Eigenschaften erstellen

Unter **Eigenschaften** erstellen Sie benutzerdefinierte Eigenschaften, auf die Ihre App über das Braze SDK zugreifen kann, wenn Ihre Funktion aktiviert ist. Sie können jeder Variablen einen String-, booleschen, Bild-, Zeitstempel-, JSON- oder Zahlenwert zuweisen sowie einen Standardwert festlegen.

{% tabs local %}
{% tab Beispiel %}
Im folgenden Beispiel zeigt das Feature-Flag ein Banner für ein E-Commerce-Geschäft, das nicht mehr vorrätig ist und die aufgeführten benutzerdefinierten Eigenschaften verwendet: 

|Eigenschaftsname|Typ|Wert|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
|`homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
|`account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
|`footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|

{% alert tip %}
Sie können beliebig viele Eigenschaften hinzufügen. Die Eigenschaften eines Feature-Flags sind jedoch auf insgesamt 10 KB begrenzt. Sowohl die Eigenschaftswerte als auch die Schlüssel sind auf eine Länge von 255 Zeichen begrenzt.
{% endalert %}
{% endtab %}
{% endtabs %}

### Schritt 4: Wählen Sie Segmente für Ihre Zielgruppe

Bevor Sie ein Feature-Flag einführen, müssen Sie ein [Nutzersegment]({{site.baseurl}}/user_guide/engagement_tools/segments/) als Zielgruppe auswählen. Verwenden Sie das Dropdown-Menü **Filter hinzufügen**, um Nutzer aus Ihrer Zielgruppe herauszufiltern. Fügen Sie mehrere Filter hinzu, um Ihre Zielgruppe weiter einzugrenzen.

![Zwei Dropdown-Menüs. Das erste lautet: Zielgruppen nach Segment zusammenstellen. Das zweite lautet: Zusätzliche Filter.]({% image_buster /assets/img/feature_flags/feature-flags-targeting.png %})

### Schritt 5: Rollout-Traffic festlegen {#rollout}

Standardmäßig sind Feature-Flags immer deaktiviert. Dadurch haben Sie die Möglichkeit, das Release-Datum Ihres Features von der gesamten Nutzeraktivierung zu trennen. Um mit dem Rollout zu beginnen, verwenden Sie den Schieberegler **Rollout Traffic** oder geben Sie einen Prozentsatz in das Textfeld ein, um den Prozentsatz der zufälligen Benutzer in Ihrem ausgewählten Segment festzulegen, die diese neue Funktion erhalten sollen.

![Schieberegler mit der Bezeichnung "Rollout-Traffic", der zwischen 0 und 100 verschoben werden kann.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.png %}){: style="max-width:75%;"}

{% alert important %}
Legen Sie den Rollout-Traffic erst dann auf einen Wert über 0 % fest, wenn Sie bereit sind, Ihr neues Feature freizuschalten. Wenn Sie mit der Definition Ihres Feature-Flags im Dashboard beginnen, lassen Sie diese Einstellung auf 0 %.
{% endalert %}

## Verwendung des Felds "aktiviert" für Feature-Flags {#enabled}

Nachdem Sie Ihr Feature-Flag definiert haben, konfigurieren Sie Ihre App oder Website, um zu überprüfen, ob das Feature-Flag für einen bestimmten Nutzer aktiviert ist oder nicht. Ist es aktiviert, legen Sie eine Aktion fest oder referenzieren die Variablen-Eigenschaften des Feature-Flags je nach Ihrem Anwendungsfall. Das Braze SDK stellt Getter-Methoden bereit, um den Status des Feature-Flags und seine Eigenschaften in Ihre App einzubinden. 

Feature-Flags werden beim Sitzungsstart automatisch aktualisiert, sodass Sie jeweils die aktuellste Version Ihres Features anzeigen können. Das SDK speichert diese Werte im Cache, sodass sie auch offline verwendet werden können. 

{% alert note %}
Vergewissern Sie sich, dass Sie [Feature-Flag-Impressionen](#impressions) protokollieren.
{% endalert %}

Nehmen wir an, Sie wollen einen neuen Typ von Benutzerprofil für Ihre App einführen. Sie können die `ID` als `expanded_user_profile` einstellen. Dann würden Sie Ihre Anwendung prüfen lassen, ob sie dieses neue Benutzerprofil einem bestimmten Benutzer anzeigen soll. Zum Beispiel:

{% tabs %}
{% tab JavaScript %}

```javascript
const featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Swift %}

```swift
let featureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")
if featureFlag?.enabled == true {
  print("expanded_user_profile is enabled")
} else {
  print("expanded_user_profile is not enabled")
}
```
{% endtab %}
{% tab Java %}
```java
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.getEnabled()) {
  Log.i(TAG, "expanded_user_profile is enabled");
} else {
  Log.i(TAG, "expanded_user_profile is not enabled");
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlag = braze.getFeatureFlag("expanded_user_profile")
if (featureFlag?.enabled == true) {
  Log.i(TAG, "expanded_user_profile is enabled.")
} else {
  Log.i(TAG, "expanded_user_profile is not enabled.")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const featureFlag = await Braze.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```

{% endtab %}
{% tab Unity %}
```csharp
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");
if (featureFlag != null && featureFlag.Enabled) {
  Console.WriteLine("expanded_user_profile is enabled");
} else {
  Console.WriteLine("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Cordova %}
```javascript
const featureFlag = await BrazePlugin.getFeatureFlag("expanded_user_profile");
if (featureFlag?.enabled) {
  console.log(`expanded_user_profile is enabled`);  
} else {
  console.log(`expanded_user_profile is not enabled`);
}
```
{% endtab %}
{% tab Flutter %}
```dart
BrazeFeatureFlag? featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");
if (featureFlag?.enabled == true) {
  print("expanded_user_profile is enabled");
} else {
  print("expanded_user_profile is not enabled");
}
```
{% endtab %}

{% tab Roku %}
```brightscript
featureFlag = m.braze.getFeatureFlag("expanded_user_profile")
if featureFlag <> invalid and featureFlag.enabled
  print "expanded_user_profile is enabled"
else
  print "expanded_user_profile is not enabled"
end if
```
{% endtab %}
{% endtabs %}

### Protokollierung einer Feature-Flag-Impression {#impressions}

Tracken Sie eine Feature-Flag-Impression, wenn ein Nutzer die Gelegenheit hatte, mit dem neuen Feature zu interagieren, oder wenn er bei deaktiviertem Feature __hätte interagieren können__ (im Fall einer Kontrollgruppe in einem A/B-Test). Feature-Flag Impressionen werden nur einmal pro Sitzung protokolliert. 

Normalerweise können Sie diese Codezeile direkt unterhalb der Stelle einfügen, an der Sie das Feature-Flag in Ihrer App referenzieren:

{% tabs %}
{% tab JavaScript %}

```javascript
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.logFeatureFlagImpression(id: "expanded_user_profile")
```

{% endtab %}
{% tab Java %}

```java
braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.logFeatureFlagImpression("expanded_user_profile")
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.logFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.LogFeatureFlagImpression("expanded_user_profile");
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Flutter %}
```dart
braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.logFeatureFlagImpression("expanded_user_profile");
```
{% endtab %}
{% endtabs %}

### Zugriff auf Eigenschaften {#accessing-properties}

Um auf die Eigenschaften eines Feature-Flags zuzugreifen, verwenden Sie je nach dem im Dashboard definierten Typ eine der folgenden Methoden.

Wenn eine Eigenschaft, die Sie referenziert haben, nicht existiert, geben diese Methoden `null` zurück.

{% tabs %}
{% tab JavaScript %}

```javascript
// Returns the Feature Flag instance
const featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
const stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
const booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
const numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
const imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a FeatureFlagJsonPropertyValue
const jsonProperty = featureFlag.getJsonProperty("footer_settings");
```

{% endtab %}
{% tab Swift %}

```swift
// Returns the Feature Flag instance
let featureFlag: FeatureFlag = braze.featureFlags.featureFlag(id: "expanded_user_profile")

// Returns the String property
let stringProperty: String? = featureFlag.stringProperty(key: "color")

// Returns the boolean property
let booleanProperty: Bool? = featureFlag.boolProperty(key: "expanded")

// Returns the number property as a double
let numberProperty: Double? = featureFlag.numberProperty(key: "height")

// Returns the Unix UTC millisecond timestamp property as an integer
let timestampProperty : Int? = featureFlag.timestampProperty(key: "account_start")

// Returns the image property as a String of the image URL
let imageProperty : String? = featureFlag.imageProperty(key: "homepage_icon")

// Returns the JSON object property as a [String: Any] dictionary
let jsonObjectProperty : [String: Any]? = featureFlag.jsonObjectProperty(key: "footer_settings")
```

{% endtab %}
{% tab Java %}

```java
// Returns the Feature Flag instance
FeatureFlag featureFlag = braze.getFeatureFlag("expanded_user_profile");

// Returns the String property
String stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
Boolean booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
Number numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
Long timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
String imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
JSONObject jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Kotlin %}

```kotlin
// Returns the Feature Flag instance
val featureFlag = braze.getFeatureFlag("expanded_user_profile")

// Returns the String property
val stringProperty: String? = featureFlag.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = featureFlag.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = featureFlag.getNumberProperty("height")

// Returns the Unix UTC millisecond timestamp property as a long
val timestampProperty: Long? = featureFlag.getTimestampProperty("account_start")

// Returns the image property as a String of the image URL
val imageProperty: String?  = featureFlag.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% tab React Native %}

```javascript
// Returns the String property
const stringProperty = await Braze.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await Braze.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await Braze.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await Braze.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await Braze.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await Braze.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Unity %}

```csharp
// Returns the Feature Flag instance
var featureFlag = Appboy.AppboyBinding.GetFeatureFlag("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.GetStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.GetBooleanProperty("expanded");

// Returns the number property as an integer
var integerProperty = featureFlag.GetIntegerProperty("height");

// Returns the number property as a double
var doubleProperty = featureFlag.GetDoubleProperty("height");

// Returns the Unix UTC millisecond timestamp property as a long
var timestampProperty = featureFlag.GetTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.GetImageProperty("homepage_icon");

// Returns the JSON object property as a JSONObject
var jsonObjectProperty = featureFlag.GetJSONProperty("footer_settings");
```

{% endtab %}
{% tab Cordova %}

```javascript
// Returns the String property
const stringProperty = await BrazePlugin.getFeatureFlagStringProperty("expanded_user_profile", "color");

// Returns the boolean property
const booleanProperty = await BrazePlugin.getFeatureFlagBooleanProperty("expanded_user_profile", "expanded");

// Returns the number property
const numberProperty = await BrazePlugin.getFeatureFlagNumberProperty("expanded_user_profile", "height");

// Returns the Unix UTC millisecond timestamp property as a number
const timestampProperty = await BrazePlugin.getFeatureFlagTimestampProperty("expanded_user_profile", "account_start");

// Returns the image property as a String of the image URL
const imageProperty = await BrazePlugin.getFeatureFlagImageProperty("expanded_user_profile", "homepage_icon");

// Returns the JSON object property as an object
const jsonObjectProperty = await BrazePlugin.getFeatureFlagJSONProperty("expanded_user_profile", "footer_settings");
```

{% endtab %}
{% tab Flutter %}

```dart
// Returns the Feature Flag instance
BrazeFeatureFlag featureFlag = await braze.getFeatureFlagByID("expanded_user_profile");

// Returns the String property
var stringProperty = featureFlag.getStringProperty("color");

// Returns the boolean property
var booleanProperty = featureFlag.getBooleanProperty("expanded");

// Returns the number property
var numberProperty = featureFlag.getNumberProperty("height");

// Returns the Unix UTC millisecond timestamp property as an integer
var timestampProperty = featureFlag.getTimestampProperty("account_start");

// Returns the image property as a String of the image URL
var imageProperty = featureFlag.getImageProperty("homepage_icon");

// Returns the JSON object property as a Map<String, dynamic> collection
var jsonObjectProperty = featureFlag.getJSONProperty("footer_settings");
```

{% endtab %}
{% tab Roku %}

```brightscript
' Returns the String property
color = featureFlag.getStringProperty("color")

' Returns the boolean property
expanded = featureFlag.getBooleanProperty("expanded")

' Returns the number property
height = featureFlag.getNumberProperty("height")

' Returns the Unix UTC millisecond timestamp property
account_start = featureFlag.getTimestampProperty("account_start")

' Returns the image property as a String of the image URL
homepage_icon = featureFlag.getImageProperty("homepage_icon")

' Returns the JSON object property
footer_settings = featureFlag.getJSONProperty("footer_settings")
```

{% endtab %}
{% endtabs %}

### Abrufen einer Liste aller Feature-Flags {#get-list-of-flags}

{% tabs %}
{% tab JavaScript %}

```javascript
const features = getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Swift %}

```swift
let features = braze.featureFlags.featureFlags
for let feature in features {
  print("Feature: \(feature.id)", feature.enabled)
}
```

{% endtab %}
{% tab Java %}

```java
List<FeatureFlag> features = braze.getAllFeatureFlags();
for (FeatureFlag feature: features) {
  Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
}
```

{% endtab %}
{% tab Kotlin %}

```kotlin
val featureFlags = braze.getAllFeatureFlags()
featureFlags.forEach { feature ->
  Log.i(TAG, "Feature: ${feature.id} ${feature.enabled}")
}
```

{% endtab %}
{% tab React Native %}

```javascript
const features = await Braze.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```

{% endtab %}
{% tab Unity %}

```csharp
List<FeatureFlag> features = Appboy.AppboyBinding.GetAllFeatureFlags();
foreach (FeatureFlag feature in features) {
  Console.WriteLine("Feature: {0} - enabled: {1}", feature.ID, feature.Enabled);
}
```

{% endtab %}
{% tab Cordova %}
```javascript
const features = await BrazePlugin.getAllFeatureFlags();
for(const feature of features) {
  console.log(`Feature: ${feature.id}`, feature.enabled);
}
```
{% endtab %}
{% tab Flutter %}
```dart
List<BrazeFeatureFlag> featureFlags = await braze.getAllFeatureFlags();
featureFlags.forEach((feature) {
  print("Feature: ${feature.id} ${feature.enabled}");
});
```
{% endtab %}
{% tab Roku %}
```brightscript
features = m.braze.getAllFeatureFlags()
for each feature in features
      print "Feature: " + feature.id + " enabled: " + feature.enabled.toStr()
end for
```
{% endtab %}
{% endtabs %}

### Aktualisieren von Feature-Flags {#refreshing}

Sie können die Feature-Flags des aktuellen Nutzers während der Sitzung aktualisieren, um die neuesten Werte aus Braze zu beziehen.

{% alert tip %}
Die Aktualisierung erfolgt automatisch beim Start der Sitzung. Eine Aktualisierung ist nur vor wichtigen Benutzeraktionen erforderlich, z. B. vor dem Laden einer Kassenseite, oder wenn Sie wissen, dass ein Feature-Flag referenziert werden wird.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
braze.refreshFeatureFlags(() => {
  console.log(`Feature flags have been refreshed.`);
}, () => {
  console.log(`Failed to refresh feature flags.`);
});
```

{% endtab %}
{% tab Swift %}

```swift
braze.featureFlags.requestRefresh { result in
  switch result {
  case .success(let features):
    print("Feature flags have been refreshed:", features)
  case .failure(let error):
    print("Failed to refresh feature flags:", error)
  }
}
```

{% endtab %}
{% tab Java %}

```java
braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.refreshFeatureFlags()
```

{% endtab %}
{% tab React Native %}

```javascript
Braze.refreshFeatureFlags();
```

{% endtab %}
{% tab Unity %}

```csharp
Appboy.AppboyBinding.RefreshFeatureFlags();
```

{% endtab %}
{% tab Cordova %}
```javascript
BrazePlugin.refreshFeatureFlags();
```
{% endtab %}
{% tab Flutter %}
```dart
braze.refreshFeatureFlags();
```
{% endtab %}
{% tab Roku %}
```brightscript
m.Braze.refreshFeatureFlags()
```
{% endtab %}
{% endtabs %}

### Auf Veränderungen achten {#updates}

Sie können das Braze SDK so konfigurieren, dass es Ihre App abhört und aktualisiert, wenn das SDK Feature-Flags aktualisiert.

Dies ist nützlich, wenn Sie Ihre App aktualisieren möchten, wenn ein Benutzer nicht mehr für eine Funktion in Frage kommt. Dazu können Sie z. B. einen Status in Ihrer App festlegen, der darauf basiert, ob ein Feature aktiviert ist oder einer seiner Eigenschaftswerte vorliegt.

{% tabs %}
{% tab JavaScript %}

```javascript
// Register an event listener
const subscriptionId = braze.subscribeToFeatureFlagsUpdates((features) => {
  console.log(`Features were updated`, features);
});
// Unregister this event listener
braze.removeSubscription(subscriptionId);
```

{% endtab %}
{% tab Swift %}

```swift
// Create the feature flags subscription
// - You must keep a strong reference to the subscription to keep it active
let subscription = braze.featureFlags.subscribeToUpdates { features in
  print("Feature flags were updated:", features)
}
// Cancel the subscription
subscription.cancel()
```

{% endtab %}
{% tab Java %}

```java
braze.subscribeToFeatureFlagsUpdates(event -> {
  Log.i(TAG, "Feature flags were updated.");
  for (FeatureFlag feature: event.getFeatureFlags()) {
    Log.i(TAG, "Feature: ", feature.getId(), feature.getEnabled());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
braze.subscribeToFeatureFlagsUpdates() { event ->
  Log.i(TAG, "Feature flags were updated.")
  event.featureFlags.forEach { feature ->
    Log.i(TAG, "Feature: ${feature.id}")
  }
}
```

{% endtab %}
{% tab React Native %}

```javascript
// Register an event listener
Braze.addListener(braze.Events.FEATURE_FLAGS_UPDATED, (featureFlags) => {
  console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```

{% endtab %}
{% tab Unity %}

Um auf Änderungen zu warten, setzen Sie die Werte für **Game Object Name** und **Callback Method Name** unter **Braze Configuration** > **Feature Flags** auf die entsprechenden Werte in Ihrer Anwendung.

{% endtab %}
{% tab Cordova %}
```javascript
// Register an event listener
BrazePlugin.subscribeToFeatureFlagUpdates((featureFlags) => {
    console.log(`featureFlagUpdates`, JSON.stringify(featureFlags));
});
```
{% endtab %}
{% tab Flutter %}

Verwenden Sie im Dart-Code in Ihrer Anwendung den folgenden Beispielcode:

```dart
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();
```

Nehmen Sie diese Änderungen dann auch in der nativen iOS-Ebene vor. Beachten Sie, dass auf der Android-Ebene keine weiteren Schritte erforderlich sind.

1. Implementieren Sie `featureFlags.subscribeToUpdates`, um wie in der Dokumentation [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoupdates(_:)) beschrieben Feature-Flag-Updates zu abonnieren.

2. Ihre `featureFlags.subscribeToUpdates` Callback-Implementierung muss `BrazePlugin.processFeatureFlags(featureFlags)` aufrufen.

Ein Beispiel finden Sie [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) in unserer Beispiel-App.

{% endtab %}
{% tab Roku %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab React-Hook %}
```typescript
import { useEffect, useState } from "react";
import {
  FeatureFlag,
  getFeatureFlag,
  removeSubscription,
  subscribeToFeatureFlagsUpdates,
} from "@braze/web-sdk";

export const useFeatureFlag = (id: string): FeatureFlag => {
  const [featureFlag, setFeatureFlag] = useState<FeatureFlag>(
    getFeatureFlag(id)
  );

  useEffect(() => {
    const listener = subscribeToFeatureFlagsUpdates(() => {
      setFeatureFlag(getFeatureFlag(id));
    });
    return () => {
      removeSubscription(listener);
    };
  }, [id]);

  return featureFlag;
};
```
{% endtab %}
{% endtabs %}

## Anzeigen des Changelogs

Um das Änderungsprotokoll eines Feature-Flags anzuzeigen, öffnen Sie ein Feature-Flag und wählen Sie **Änderungsprotokoll**.

![Seite "Bearbeiten" eines Feature-Flags mit dem hervorgehobenen Button "Changelog"]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

Hier können Sie nachsehen, wann eine Änderung stattgefunden hat, wer die Änderung vorgenommen hat, zu welcher Kategorie sie gehört und vieles mehr.

![Changelog des ausgewählten Feature-Flags]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}){: style="max-width:90%;"}

## Segmentieren mit Feature-Flags {#segmentation}

Braze merkt sich automatisch, welche Benutzer derzeit für ein Feature-Flag aktiviert sind. Mit dem [Filter **Feature-Flag**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#feature-flags) können Sie ein Segment oder ein gezieltes Messaging erstellen. Weitere Informationen zum Filtern nach Segmenten finden Sie unter [Erstellen eines Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

![Der Bereich "Filter" mit dem in die Suchleiste des Filters eingegebenen Suchbegriff "Feature-Flag"]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
Um rekursive Segmente zu vermeiden, ist es nicht möglich, ein Segment zu erstellen, das andere Feature-Flags referenziert.
{% endalert %}

## Bewährte Praktiken

### Kombinieren Sie Rollouts nicht mit Canvases oder Experimenten

Um zu vermeiden, dass Benutzer durch unterschiedliche Einstiegspunkte aktiviert und deaktiviert werden, sollten Sie entweder den Schieberegler für die Rollouts auf einen Wert größer als Null setzen ODER das Feature-Flag in einem Canvas oder Experiment aktivieren. Wenn Sie ein Feature-Flag in einem Canvas oder Experiment verwenden möchten, sollten Sie den Rollout-Prozentsatz auf Null setzen.

### Benennungskonventionen

Um Ihren Code übersichtlich und einheitlich zu halten, empfiehlt es sich, bei der Benennung der Feature-Flag-ID das folgende Format zu verwenden:

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

Ersetzen Sie Folgendes:

| Platzhalter | Beschreibung                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | Das Verhalten der Funktion. Achten Sie in Ihrem Code darauf, dass das Verhalten standardmäßig deaktiviert ist und vermeiden Sie Ausdrücke wie `disabled` im Namen des Feature-Flags. |
| `PRODUCT`   | Das Produkt, zu dem das Merkmal gehört.                                                                                       |
| `FEATURE`    | Der Name der Funktion.                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Hier ist ein Beispiel für ein Feature-Flag, wobei `show` das Verhalten, `animation_profile` das Produkt und `driver` das Feature ist:

```plaintext
show_animation_profile_driver
```

### Vorausplanen

Gehen Sie immer auf Nummer sicher. Wenn Sie neue Features in Betracht ziehen, die möglicherweise einen Aus-Schalter erfordern, ist es besser, neuen Code mit einem Feature-Flag zu veröffentlichen und ihn doch nicht zu benötigen, als festzustellen, dass ein neues App-Update erforderlich ist.

### Beschreibend sein

Fügen Sie eine Beschreibung zu Ihrem Feature-Flag hinzu. Dies ist zwar ein optionales Feld in Braze, aber es kann helfen, Fragen zu beantworten, die andere beim Durchsuchen der verfügbaren Feature-Flags haben könnten.

- Kontaktinformationen zu den Personen, die für die Aktivierung und das Verhalten dieser Flagge verantwortlich sind
- Wann dieses Flag deaktiviert werden sollte
- Links zur Dokumentation oder zu Notizen über die neue Funktion, die dieses Flag steuert
- Etwaige Abhängigkeiten oder Hinweise zur Verwendung der Funktion

### Alte Feature-Flags bereinigen

Grundsätzlich sollte davon abgesehen werden, Features länger als nötig bei einem Rollout-Prozentsatz von 100 % zu belassen.

Um Ihren Code (und das Braze Dashboard) sauber zu halten, entfernen Sie permanente Funktionsflags aus Ihrer Codebasis, nachdem alle Benutzer ein Upgrade durchgeführt haben und Sie die Option zur Deaktivierung der Funktion nicht mehr benötigen. Auf diese Weise lässt sich die Komplexität der Entwicklungsumgebung verringern, während gleichzeitig die Liste der Feature-Flags übersichtlich gehalten wird.

