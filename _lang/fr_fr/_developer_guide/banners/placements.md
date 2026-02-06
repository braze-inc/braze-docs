---
nav_title: Gérer les placements
article_title: Gérer les placements de bannières pour le SDK de Braze
description: "Découvrez comment créer et gérer des placements de bannières dans le SDK de Braze, notamment en accédant à leurs propriétés uniques et en enregistrant les impressions."
page_order: 2
platform:
  - iOS
  - Android
  - Web
  - Flutter
  - React Native
---

# Gérer les placements de bannières

> Découvrez comment créer et gérer des placements de bannières dans le SDK de Braze, notamment en accédant à leurs propriétés uniques et en enregistrant les impressions. Pour plus d'informations générales, reportez-vous à la section [À propos des bannières]({{site.baseurl}}/developer_guide/banners).

## A propos des demandes de placement {#requests}

{% multi_lang_include banners/placement_requests.md %}

## Création d'un placement

### Conditions préalables

Il s'agit des versions minimales du SDK nécessaires pour créer des placements de bannières :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

{% multi_lang_include banners/creating_placements.md section="developer" %}

### Étape 2 : Actualiser les placements dans votre application {#requestBannersRefresh}

Les placements peuvent être actualisés en appelant les méthodes d'actualisation décrites ci-dessous. Ces placements seront automatiquement mis en cache à l'expiration de la session d'un utilisateur ou lorsque vous modifiez les utilisateurs identifiés à l'aide de la méthode `changeUser`.

{% alert tip %}
Actualisez les placements dès que possible afin d'éviter tout retard dans le téléchargement ou l'affichage des bannières.
{% endalert %}

{% tabs %}
{% tab Web %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
Braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Étape 3 : Écoutez les mises à jour {#subscribeToBannersUpdates}

{% alert tip %}
Si vous insérez des bannières à l'aide des méthodes du SDK décrites dans ce guide, tous les événements d'analyse/analytique (tels que les impressions et les clics) seront traités automatiquement, et les impressions ne seront enregistrées que lorsque la bannière sera visible.
{% endalert %}

{% tabs %}
{% tab Web %}
{% subtabs %}
{% subtab Javascript %}
Si vous utilisez du JavaScript vanille avec le SDK Web Braze, utilisez [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) pour écouter les mises à jour de placement, puis appelez [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) pour les récupérer.

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log("Banners were updated");
});

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}
{% subtab React %}
Si vous utilisez React avec le SDK de Braze, mettez en place [`subscribeToBannersUpdates`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#subscribetobannersupdates) à l'intérieur d'un crochet `useEffect` et appelez [`requestBannersRefresh`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestbannersrefresh) après avoir enregistré votre écouteur.

```typescript
import * as braze from "@braze/web-sdk";

useEffect(() => {
  const subscriptionId = braze.subscribeToBannersUpdates((banners) => {
    console.log("Banners were updated");
  });

  // always refresh after your subscriber function has been registered
  braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);

  // cleanup listeners
  return () => {
    braze.removeSubscription(subscriptionId);
  }
}, []);
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab Swift %}

```swift
let cancellable = brazeClient.braze()?.banners.subscribeToUpdates { banners in
  banners.forEach { placementId, banner in
    print("Received banner: \(banner) with placement ID: \(placementId)")
  }
}
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  (data) => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map((banner) => banner.placementId)
    );
  }
);
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}

```dart
StreamSubscription bannerStreamSubscription = braze.subscribeToBanners((List<BrazeBanner> banners) {
  for (final banner in banners) {
    print("Received banner: " + banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Étape 4 : Insertion à l'aide de l'ID de placement {#insertBanner}

{% alert tip %}
Pour un tutoriel complet étape par étape, consultez la page [Afficher une bannière par ID de placement]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners).
{% endalert %}

{% tabs %}
{% tab Web %}

Créez un élément conteneur pour la bannière. Veillez à définir sa largeur et sa hauteur.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

{% subtabs local %}
{% subtab JavaScript %}
Si vous utilisez du JavaScript vanille avec le SDK de Braze, appelez la méthode [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) pour remplacer le code HTML interne de l'élément conteneur.

```javascript
import * as braze from "@braze/web-sdk";

braze.initialize("sdk-api-key", {
  baseUrl: "sdk-base-url",
  allowUserSuppliedJavascript: true, // banners require you to opt-in to user-supplied javascript
});

braze.subscribeToBannersUpdates((banners) => {
  // get this placement's banner. If it's `null` the user did not qualify for one.
  const globalBanner = braze.getBanner("global_banner");
  if (!globalBanner) {
    return;
  }

  // choose where in the DOM you want to insert the banner HTML
  const container = document.getElementById("global-banner-container");

  // Insert the banner which replaces the innerHTML of that container
  braze.insertBanner(globalBanner, container);

  // Special handling if the user is part of a Control Variant
  if (globalBanner.isControl) {
    // hide or collapse the container
    container.style.display = "none";
  }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"]);
```
{% endsubtab %}

{% subtab React %}
Si vous utilisez React avec le SDK Braze, appelez la méthode [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) avec une adresse `ref` pour remplacer le code HTML interne de l'élément conteneur.

```tsx
import { useRef } from 'react';
import * as braze from "@braze/web-sdk";

export default function App() {
    const bannerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
       const globalBanner = braze.getBanner("global_banner");
       if (!globalBanner || globalBanner.isControl) {
           // hide the container
       } else {
           // insert the banner to the container node
           braze.insertBanner(globalBanner, bannerRef.current);
       }
    }, []);
    return <div ref={bannerRef}></div>
}
```
{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Pour suivre les impressions, veillez à appeler `insertBanner` pour `isControl`. Vous pouvez ensuite cacher ou fermer votre conteneur.
{% endalert %}

{% endtab %}
{% tab Swift %}

```swift
// To get access to the Banner model object:
let globalBanner: Braze.Banner?
AppDelegate.braze?.banners.getBanner(for: "global_banner", { banner in
  self.globalBanner = banner
})

// If you simply want the Banner view, you may initialize a `UIView` with the placement ID:
if let braze = AppDelegate.braze {
  let bannerUIView = BrazeBannerUI.BannerUIView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(
    placementId: "global_banner",
    braze: braze,
    // iOS does not perform automatic resizing or visibility changes.
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner according to your use case.
    processContentUpdates: { result in
      switch result {
      case .success(let updates):
        if let height = updates.height {
          // Adjust the visibility and/or height according to your parent controller.
        }
      case .failure(let error):
        // Handle the error.
      }
    }
  )
}
```

{% endtab %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}
Pour obtenir la bannière en code Java, utilisez :

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Vous pouvez créer des bannières dans vos vues Android en incluant ce XML :

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```
{% endsubtab %}

{% subtab Kotlin %}
Si vous utilisez Android Views, utilisez ce XML :

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

Si vous utilisez Jetpack Compose, vous pouvez utiliser ceci :

```kotlin
Banner(placementId = "global_banner")
```

Pour obtenir la bannière en Kotlin, utilisez :
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab React Native %}

Si vous utilisez la [nouvelle architecture de React Native](https://reactnative.dev/architecture/landing-page), vous devez enregistrer `BrazeBannerView` en tant que composant Fabric dans votre site `AppDelegate.mm`.

```swift
#ifdef RCT_NEW_ARCH_ENABLED
/// Register the `BrazeBannerView` for use as a Fabric component.
- (NSDictionary<NSString *,Class<RCTComponentViewProtocol>> *)thirdPartyFabricComponents {
  NSMutableDictionary * dictionary = [super thirdPartyFabricComponents].mutableCopy;
  dictionary[@"BrazeBannerView"] = [BrazeBannerView class];
  return dictionary;
}
#endif
```
Pour l'intégration la plus simple, ajoutez l'extrait de code JavaScript XML (JSX) suivant dans votre hiérarchie de vues, en fournissant uniquement l'ID de placement.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
```

Pour obtenir le modèle de données de la bannière dans React Native, ou pour vérifier la présence de ce placement dans le cache de votre utilisateur, utilisez :

```javascript
const banner = await Braze.getBanner("global_banner");
```

{% endtab %}
{% tab Unity %}

```csharp
This feature is not currently supported on Unity.
```

{% endtab %}
{% tab Cordova %}

```javascript
This feature is not currently supported on Cordova.
```

{% endtab %}
{% tab Flutter %}
Pour l'intégration la plus simple, ajoutez le widget suivant dans votre hiérarchie de vues, en fournissant uniquement l'ID de placement.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
To get the Banner's data model in Flutter, use:
```

Vous pouvez utiliser la méthode `getBanner` pour vérifier la présence de ce placement dans le cache de votre utilisateur.

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

{% endtab %}
{% tab Roku %}

```brightscript
This feature is not currently supported on Roku.
```

{% endtab %}
{% endtabs %}

### Étape 5 : Envoyer une bannière de test (facultatif) {#handling-test-cards}

Avant de lancer une campagne de bannières, vous pouvez [envoyer une bannière de test]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/) pour vérifier votre intégration. Les bannières de test seront stockées dans un cache en mémoire distinct et ne persisteront pas lors des redémarrages de l'application. Bien qu'aucune configuration supplémentaire ne soit nécessaire, votre appareil de test doit être capable de recevoir des notifications push au premier plan pour pouvoir afficher le test.

{% alert note %}
Les bannières de test sont comme toutes les autres bannières, sauf qu'elles sont retirées lors de la prochaine session de l'application.
{% endalert %}

## Enregistrement des impressions

Braze enregistre automatiquement les impressions des bannières visibles lorsque vous utilisez les méthodes du SDK pour insérer une bannière - il n'est donc pas nécessaire de suivre les impressions manuellement.

## Dimensions et taille

Voici ce que vous devez savoir sur les dimensions des bannières :

- Bien que le compositeur vous permette de prévisualiser les bannières dans différentes dimensions, cette information n'est pas enregistrée ou envoyée au SDK.
- Le code HTML occupera toute la largeur du conteneur dans lequel il est affiché.
- Nous vous recommandons de créer un élément de dimension fixe et de tester ces dimensions dans composer.

## Propriétés personnalisées {#custom-properties}

Vous pouvez utiliser les propriétés personnalisées de votre campagne Banner pour récupérer des données clé-valeur via le SDK et modifier le comportement ou l'apparence de votre application. Par exemple, vous pourriez :

- Envoyez des métadonnées pour vos analyses/analytiques tierces (si utilisées comme adjectifs).
- Utilisez des métadonnées telles qu'un objet `timestamp` ou JSON pour déclencher une logique conditionnelle.
- Contrôlez le comportement d'une bannière en fonction des métadonnées incluses comme `ratio` ou `format`.

### Conditions préalables

Vous devrez [ajouter des propriétés personnalisées]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#custom-properties) à votre campagne Banner. En outre, il s'agit des versions minimales du SDK requises pour accéder aux propriétés personnalisées :

{% sdk_min_versions swift:13.1.0 android:38.0.0 web:6.1.0 reactnative:17.0.0 flutter:15.1.0 %}

### Accès aux propriétés personnalisées

Pour accéder aux propriétés personnalisées d'une bannière, utilisez l'une des méthodes suivantes en fonction du type de propriété défini dans le tableau de bord. Si la clé ne correspond pas à une propriété de ce type ou n'existe pas, la méthode renvoie `null`.

{% tabs local %}
{% tab Web %}
```javascript
// Returns the Banner instance
const banner = braze.getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner) {

  // Returns the string property
  const stringProperty = banner.getStringProperty("color");

  // Returns the boolean property
  const booleanProperty = banner.getBooleanProperty("expanded");

  // Returns the number property
  const numberProperty = banner.getNumberProperty("height");

  // Returns the timestamp property (as a number)
  const timestampProperty = banner.getTimestampProperty("account_start");

  // Returns the image URL property as a string of the URL
  const imageProperty = banner.getImageProperty("homepage_icon");

  // Returns the JSON object property
  const jsonObjectProperty = banner.getJsonProperty("footer_settings");
}
```
{% endtab %}

{% tab Swift %}
```swift
// Passes the specified banner to the completion handler
AppDelegate.braze?.banners.getBanner(for: "placement_id_homepage_top") { banner in
  // Returns the string property
  let stringProperty: String? = banner.stringProperty(key: "color")

  // Returns the boolean property
  let booleanProperty: Bool? = banner.boolProperty(key: "expanded")

  // Returns the number property as a double
  let numberProperty: Double? = banner.numberProperty(key: "height")

  // Returns the Unix UTC millisecond timestamp property as an integer
  let timestampProperty: Int? = banner.timestampProperty(key: "account_start")

  // Returns the image property as a String of the image URL
  let imageProperty: String? = banner.imageProperty(key: "homepage_icon")

  // Returns the JSON object property as a [String: Any] dictionary
  let jsonObjectProperty: [String: Any]? = banner.jsonObjectProperty(key: "footer_settings")
}
```
{% endtab %}

{% tab Android %}
{% subtabs %}
{% subtab Java %}
```java
// Returns the Banner instance
Banner banner = Braze.getInstance(context).getBanner("placement_id_homepage_top");

// banner may be undefined or null
if (banner != null) {
  // Returns the string property
  String stringProperty = banner.getStringProperty("color");
  
  // Returns the boolean property
  Boolean booleanProperty = banner.getBooleanProperty("expanded");
  
  // Returns the number property
  Number numberProperty = banner.getNumberProperty("height");
  
  // Returns the timestamp property (as a Long)
  Long timestampProperty = banner.getTimestampProperty("account_start");
  
  // Returns the image URL property as a String of the URL
  String imageProperty = banner.getImageProperty("homepage_icon");
  
  // Returns the JSON object property as a JSONObject
  JSONObject jsonObjectProperty = banner.getJSONProperty("footer_settings");
}
```
{% endsubtab %}

{% subtab Kotlin %}
```kotlin
// Returns the Banner instance
val banner: Banner = Braze.getInstance(context).getBanner("placement_id_homepage_top") ?: return

// Returns the string property
val stringProperty: String? = banner.getStringProperty("color")

// Returns the boolean property
val booleanProperty: Boolean? = banner.getBooleanProperty("expanded")

// Returns the number property
val numberProperty: Number? = banner.getNumberProperty("height")

// Returns the timestamp property (as a Long)
val timestampProperty: Long? = banner.getTimestampProperty("account_start")

// Returns the image URL property as a String of the URL
val imageProperty: String? = banner.getImageProperty("homepage_icon")

// Returns the JSON object property as a JSONObject
val jsonObjectProperty: JSONObject? = banner.getJSONProperty("footer_settings")
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab React Native %}

```javascript
// Get the Banner instance
const banner = await Braze.getBanner('placement_id_homepage_top');
if (!banner) return;

// Get the string property
const stringProperty = banner.getStringProperty('color');

// Get the boolean property
const booleanProperty = banner.getBooleanProperty('expanded');

// Get the number property
const numberProperty = banner.getNumberProperty('height');

// Get the timestamp property (as a number)
const timestampProperty = banner.getTimestampProperty('account_start');

// Get the image URL property as a string
const imageProperty = banner.getImageProperty('homepage_icon');

// Get the JSON object property
const jsonObjectProperty = banner.getJSONProperty('footer_settings');
```

{% endtab %}
{% tab Flutter %}

```dart
// Fetch the banner asynchronously
_braze.getBanner(placementId).then(('placement_id_homepage_top') {
  // Get the string property
  final String? stringProperty = banner?.getStringProperty('color');
  
  // Get the boolean property
  final bool? booleanProperty = banner?.getBooleanProperty('expanded');
  
  // Get the number property
  final num? numberProperty = banner?.getNumberProperty('height');
  
  // Get the timestamp property
  final int? timestampProperty = banner?.getTimestampProperty('account_start');
  
  // Get the image URL property
  final String? imageProperty = banner?.getImageProperty('homepage_icon');
  
  // Get the JSON object propertyßß
  final Map<String, dynamic>? jsonObjectProperty = banner?.getJSONProperty('footer_settings');
  
  // Use these properties as needed in your UI or logic
});
```

{% endtab %}
{% endtabs %}
