---
nav_title: Création d’indicateurs de fonctionnalité
article_title: Création d’indicateurs de fonctionnalité
page_order: 20
description: "Cet article de référence explique comment créer des indicateurs de fonctionnalité pour coordonner les déploiements de nouvelles fonctionnalités."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web

---

# Création d’indicateurs de fonctionnalité

> Les indicateurs de fonctionnalité vous permettent d’activer ou de désactiver à distance la fonctionnalité d’une sélection d’utilisateurs. Créez un indicateur de fonctionnalité dans le tableau de bord de Braze. Donnez un nom et un `ID`, une audience cible et un pourcentage d’utilisateurs pour lesquels vous pouvez activer cette fonction. Ensuite, en utilisant `ID` dans votre application ou le code du site Internet, vous pouvez exécuter certaines parties de votre logique commerciale. Pour en savoir plus sur les indicateurs de fonctionnalité et leur utilisation dans Braze, consultez la section [À propos des indicateurs de fonctionnalité.]({{site.baseurl}}/developer_guide/feature_flags/)

## Conditions préalables

### Version du SDK

Pour utiliser des indicateurs de fonctionnalité, assurez-vous que vos SDK sont à jour avec au moins ces versions minimales :

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

### Permissions de Braze

Pour gérer les indicateurs de fonctionnalité dans le tableau de bord, vous devez être un gestionnaire ou disposer des [autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) suivantes :

| Autorisation                                                                    | Ce que vous pouvez faire                           |
|-------------------------------------------------------------------------------|-------------------------------------------|
| **Gérer les étiquettes de fonctionnalité**                                                      | Affichez, créez et modifiez des drapeaux de fonctionnalité.     |
| **Campagnes d'accès, canvas, cartes, indicateurs de fonctionnalités, segments, bibliothèque multimédia** | Consultez la liste des drapeaux de fonctionnalité disponibles. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Création d'un drapeau de fonctionnalité

### Étape 1 : Créer un nouvel indicateur de fonctionnalité

Allez dans **Messagerie** > **Indicateurs de fonctionnalité**, puis sélectionnez **Créer un indicateur de fonctionnalité**.

![Une liste des indicateurs de fonctionnalité créés précédemment sur le tableau de bord de Braze]({% image_buster /assets/img/feature_flags/feature-flags-list.png %}){: style="max-width:75%"}

### Étape 2 : Fournir les informations demandées

Sous **Détails**, saisissez un nom, un ID et une description pour votre indicateur de fonctionnalité.

| Champ        | Description                                                                                                                                                                                                         |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Nom         | Un titre lisible par l'homme pour vos marketeurs et administrateurs.                                                                                                                                                       |
| ID           | L'ID unique que vous utiliserez dans votre code pour vérifier si cette fonctionnalité est [activée pour un utilisateur](#enabled). Cet ID ne pourra pas être modifié ultérieurement. Consultez donc nos [bonnes pratiques en matière d'attribution de noms d'ID](#naming-conventions) avant de continuer. |
| Description  | Une description facultative qui donne un peu de contexte à votre indicateur de fonctionnalité.                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Étape 3 : Créer des propriétés personnalisées

Sous **Propriétés**, créez des propriétés personnalisées auxquelles votre application peut accéder via le SDK de Braze lorsque votre fonctionnalité est activée. Vous pouvez assigner une chaîne de caractères, une valeur booléenne, une image, un horodatage, une valeur JSON ou un nombre à chaque variable, ainsi que définir une valeur par défaut.

{% tabs local %}
{% tab exemple %}
Dans l'exemple suivant, le témoin de fonctionnalité affiche une bannière de rupture de stock pour un magasin de commerce électronique utilisant les propriétés personnalisées répertoriées : 

|Nom de la propriété|Type|Valeur|
|--|--|--|
|`banner_height`|`number`|`75`|
|`banner_color`|`string`|`blue`|
|`banner_text`|`string`|`Widgets are out of stock until July 1.`|
|`dismissible`|`boolean`|`false`|
|`homepage_icon`|`image`|`http://s3.amazonaws.com/[bucket_name]/`|
|`account_start`|`timestamp`|`2011-01-01T12:00:00Z`|
|`footer_settings`|`JSON`|`{ "colors": [ "red", "blue", "green" ], "placement": 123 }`|

{% alert tip %}
Il n'y a pas de limite au nombre de propriétés que vous pouvez ajouter. Toutefois, les propriétés d'un indicateur de fonctionnalité sont limitées à un total de 10 Ko. Les valeurs des propriétés et les clés sont limitées à 255 caractères.
{% endalert %}
{% endtab %}
{% endtabs %}

### Étape 4 : Choisissez les segments à cibler

Avant de déployer un indicateur de fonctionnalité, vous devez choisir un [segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) d’utilisateurs à cibler. Utilisez le menu déroulant **Ajouter un filtre** pour filtrer les utilisateurs de votre audience cible. Ajoutez plusieurs filtres pour restreindre davantage votre audience.

![Deux menus déroulants. Le premier indique les utilisateurs cibles par segment. La seconde mentionne les filtres supplémentaires.]({% image_buster /assets/img/feature_flags/feature-flags-targeting.png %})

### Étape 5 : Définir le trafic de déploiement {#rollout}

Par défaut, les indicateurs de fonctionnalité sont toujours désactivés, ce qui vous permet de séparer la date de publication de vos fonctionnalités du nombre total d'utilisateurs activés. Pour commencer votre déploiement, utilisez le curseur **Trafic de déploiement**, ou entrez un pourcentage dans la zone de texte, pour choisir le pourcentage d'utilisateurs aléatoires dans votre segmentation sélectionnée qui recevront cette nouvelle fonctionnalité.

![Un curseur intitulé "Rollout Traffic", compris entre 0 et 100.]({% image_buster /assets/img/feature_flags/feature-flags-rollout.png %}){: style="max-width:75%;"}

{% alert important %}
Ne définissez pas votre trafic de déploiement au-dessus de 0 % jusqu’à ce que vous soyez prêt à lancer votre nouvelle fonctionnalité. Lorsque vous définissez initialement votre indicateur de fonctionnalité dans le tableau de bord, laissez ce paramètre à 0 %.
{% endalert %}

## Utilisation du champ "enabled" pour vos indicateurs de fonctionnalité {#enabled}

Une fois que vous avez défini votre indicateur de fonctionnalité, configurez votre application ou site pour vérifier si elle est activée ou non pour un utilisateur particulier. Lorsqu’il est activé, vous allez définir une action ou référencer les propriétés variables de l’indicateur d’entité en fonction de votre cas d’utilisation. Le SDK Braze fournit des méthodes de gestion de l’état de l’indicateur de fonctionnalité et de ses propriétés dans votre application. 

Les indicateurs de fonctionnalité sont actualisés automatiquement au début de la session afin que vous puissiez afficher la version la plus récente de votre fonction au moment du lancement. Le SDK cache ces valeurs afin qu’elles puissent être utilisées hors ligne. 

{% alert note %}
Veillez à enregistrer les [impressions des drapeaux de fonctionnalité](#impressions).
{% endalert %}

Imaginons que vous deviez déployer un nouveau type de profil utilisateur pour votre application. Vous pouvez définir `ID` comme `expanded_user_profile`. Ensuite, votre application vérifie si elle doit afficher ce nouveau profil utilisateur à un utilisateur particulier. Par exemple :

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

### Enregistrement de l'impression d'un indicateur de fonctionnalité {#impressions}

Suivez l'impression d'un indicateur de fonctionnalité chaque fois qu'un utilisateur a eu l'occasion d'interagir avec votre nouvelle fonctionnalité, ou lorsqu'il aurait __pu__ interagir si la fonctionnalité était désactivée (dans le cas d'un groupe de contrôle lors d'un test A/B). Les impressions des drapeaux de fonctionnalité ne sont enregistrées qu'une seule fois par session. 

En général, vous pouvez placer cette ligne de code directement sous l'endroit où vous faites référence à votre drapeau de fonctionnalité dans votre application :

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

### Accès aux propriétés {#accessing-properties}

Pour accéder aux propriétés d’un indicateur de fonctionnalité, utilisez l’une des méthodes suivantes en fonction du type que vous avez défini dans le tableau de bord.

Si une propriété que vous avez référencée n'existe pas, ces méthodes renvoient `null`.

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

### Création d’une liste de tous les indicateurs de fonctionnalités {#get-list-of-flags}

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

### Actualisation des indicateurs de fonctionnalités {#refreshing}

Vous pouvez actualiser la mi-session de l’utilisateur actuel pour extraire les dernières valeurs de Braze.

{% alert tip %}
L’actualisation se produit automatiquement au début de la session. Vous n’avez besoin que d’une actualisation avant d’effectuer des actions importantes, comme avant de charger une page de paiement, ou si vous savez qu’un indicateur de fonctionnalité sera référencé.
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

### Écoute des changements {#updates}

Vous pouvez configurer le SDK de Braze pour qu'il écoute et mette à jour votre application lorsque le SDK actualise des indicateurs de fonctionnalités.

Cela est utile si vous souhaitez mettre à jour votre application si un utilisateur n’est plus admissible à une entité. Par exemple, en définissant un état dans votre application, en fonction de l’activation ou non d’une fonctionnalité ou de l’une de ses valeurs de propriété.

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

Pour écouter les changements, définissez les valeurs de **Nom de l'objet de jeu** et **Nom de la méthode de rappel** sous **Configuration de Braze** > **Drapeaux de fonctionnalité** aux valeurs correspondantes dans votre application.

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

Dans le code Dart de votre application, utilisez l'exemple de code suivant :

```dart
// Create stream subscription
StreamSubscription featureFlagsStreamSubscription;

featureFlagsStreamSubscription = braze.subscribeToFeatureFlags((featureFlags) {
  print("Feature flags were updated");
});

// Cancel stream subscription
featureFlagsStreamSubscription.cancel();
```

Ensuite, effectuez également ces changements dans la couche native d'iOS. Notez qu'aucune étape supplémentaire n'est nécessaire sur la couche Android.

1. Implémentez `featureFlags.subscribeToUpdates` pour vous abonner aux mises à jour des indicateurs de fonctionnalités comme décrit dans la documentation [subscribeToUpdates](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/featureflags-swift.class/subscribetoupdates(_:)).

2. Votre implémentation de fonction de rappel `featureFlags.subscribeToUpdates` doit appeler `BrazePlugin.processFeatureFlags(featureFlags)`.

Consultez [AppDelegate.swift](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift) dans notre exemple d'application.

{% endtab %}
{% tab Roku %}
```brightscript
' Define a function called `onFeatureFlagChanges` to be called when feature flags are refreshed
m.BrazeTask.ObserveField("BrazeFeatureFlags", "onFeatureFlagChanges")
```
{% endtab %}

{% tab React Hook %}
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

## Consulter le journal des modifications

Pour afficher le journal des modifications d'un indicateur de fonctionnalité, ouvrez cet indicateur et sélectionnez **Journal des modifications**.

![Page "Modifier" d'un drapeau de fonctionnalité, avec le bouton "Journal des modifications" en surbrillance.]({% image_buster /assets/img/feature_flags/changelog/open_changelog.png %}){: style="max-width:60%;"}

Vous pouvez y consulter la date d'une modification, son auteur, la catégorie à laquelle elle appartient, et bien d'autres choses encore.

![Le journal des modifications de l'indicateur de fonctionnalité sélectionné.]({% image_buster /assets/img/feature_flags/changelog/changelog.png %}){: style="max-width:90%;"}

## Segmentation avec les indicateurs de fonctionnalités {#segmentation}

Braze garde automatiquement la trace des utilisateurs qui sont actuellement activés pour un indicateur de fonctionnalité. Vous pouvez créer un segment ou un envoi de messages ciblés à l'aide du [filtre**Drapeau de fonctionnalité**]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/#feature-flags). Pour plus d'informations sur le filtrage sur les segments, voir [Créer un segment]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/).

![La section "Filtres" avec "Indicateur de fonctionnalité" tapé dans la barre de recherche des filtres.]({% image_buster /assets/img/feature_flags/feature-flags-filter-name.png %}){: style="max-width:75%;"}

{% alert note %}
Pour éviter les segments récursifs, il n'est pas possible de créer un segment faisant référence à d'autres drapeaux de fonctionnalité.
{% endalert %}

## Bonnes pratiques

### Ne combinez pas les déploiements avec des canevas ou des expériences

Pour éviter que les utilisateurs soient activés et désactivés par différents points d'entrée, vous devez soit régler le curseur des déploiements sur une valeur supérieure à zéro, soit activer le drapeau de fonctionnalité dans un Canvas ou une expérience. Si vous prévoyez d'utiliser un indicateur de fonctionnalité dans le cadre d'un Canvas ou d'une expérience, veillez à ce que le pourcentage de déploiement soit nul.

### Conventions de nommage

Pour que votre code soit clair et cohérent, pensez à utiliser le format suivant lors de l’attribution d’un nom à l'ID de votre indicateur de fonctionnalité :

```plaintext
BEHAVIOR_PRODUCT_FEATURE
```

Remplacez les éléments suivants :

| Marque substitutive | Description                                                                                                               |
|-------------|---------------------------------------------------------------------------------------------------------------------------|
| `BEHAVIOR`  | Le comportement de la fonctionnalité. Dans votre code, assurez-vous que le comportement est désactivé par défaut et évitez d'utiliser des expressions telles que `disabled` dans le nom de l'indicateur de fonctionnalité. |
| `PRODUCT`   | Le produit auquel appartient la fonctionnalité.                                                                                       |
| `FEATURE`    | Le nom de la fonctionnalité.                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Voici un exemple d'indicateur de fonctionnalité où `show` est le comportement, `animation_profile` est le produit et `driver` est la fonctionnalité :

```plaintext
show_animation_profile_driver
```

### Planifier à l’avance

Jouez toujours la carte de la sécurité. Lorsque vous envisagez de nouvelles fonctionnalités qui pourraient nécessiter un interrupteur, il est préférable de publier un nouveau code avec un indicateur de fonctionnalité et de ne pas en avoir besoin plutôt que de réaliser qu'une nouvelle mise à jour de l'application est nécessaire.

### Soyez descriptif

Ajoutez une description à votre indicateur de fonctionnalité. Bien qu’il s’agisse d’un champ facultatif dans Braze, il peut aider à répondre aux questions que d’autres peuvent avoir lors de la navigation entre les indicateurs de fonctionnalité disponibles.

- Coordonnées de la personne responsable de l’activation et du comportement de cet indicateur
- Quand cet indicateur doit être désactivé
- Liens vers la documentation ou les notes sur la nouvelle fonctionnalité contrôlée par cet indicateur
- Dépendances ou remarques sur l’utilisation de la fonctionnalité

### Nettoyer les anciens indicateurs de fonctionnalité

Nous sommes tous coupables de laisser les fonctionnalités activées à 100 % plus longtemps que nécessaire.

Pour que votre code (et le tableau de bord de Braze) reste propre, supprimez les drapeaux de fonctionnalité permanents de votre base de code une fois que tous les utilisateurs ont effectué la mise à niveau et que vous n'avez plus besoin de l'option de désactivation de la fonctionnalité. Cela permet de réduire la complexité de votre environnement de développement, mais aussi de garder votre liste d’indicateurs de fonctionnalités bien ordonnée.

