---
nav_title: Intégrer des cartes
article_title: Intégrer des cartes bannières pour le SDK de Braze
description: "Découvrez comment intégrer des cartes bannières au SDK de Braze."
platform:
  - iOS
  - Android
  - Web
  
---

# Intégrer des cartes bannières

> Apprenez à intégrer des cartes bannières à l'aide du SDK de Braze, afin d'engager les utilisateurs dans une expérience qui semble naturelle. Pour plus d'informations générales, voir [À propos des cartes bannières]({{site.baseurl}}/developer_guide/banner_cards/).

{% alert important %}
Les cartes bannières sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Conditions préalables

Il s'agit des versions minimales du SDK nécessaires pour commencer à utiliser les Banner Cards :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.8.1 reactnative:14.0.0 flutter:13.0.0 %}

## Intégrer une carte bannière

{% multi_lang_include banner_cards/creating_placements.md %}

### Étape 2 : Actualiser les placements dans votre application {#requestBannersRefresh}

Les placements peuvent être demandés à chaque session et seront automatiquement mis en cache à l'expiration de la session d'un utilisateur ou lorsque vous changez d'utilisateur identifié à l'aide de la méthode `changeUser`.

{% alert tip %}
Actualisez les placements dès que possible afin d'éviter tout retard dans le téléchargement ou l'affichage des bannières.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
```

{% endtab %}
{% tab Swift %}

```swift
AppDelegate.braze?.banners.requestRefresh(placementIds: ["global_banner", "navigation_square_banner"])
```
{% endtab %}
{% tab Java %}
```java
ArrayList<String> listOfBanners = new ArrayList<>();
listOfBanners.add("global_banner");
listOfBanners.add("navigation_square_banner");
Braze.getInstance(context).requestBannersRefresh(listOfBanners);
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).requestBannersRefresh(listOf("global_banner", "navigation_square_banner"))
```

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

### Étape 3 : Écoutez les mises à jour {#subscribeToBannersUpdates}

{% alert tip %}
Si vous insérez des bannières à l'aide des méthodes du SDK décrites dans ce guide, tous les événements d'analyse/analytique seront gérés automatiquement. Si vous souhaitez rendre manuellement le code HTML, [faites-le nous savoir.](mailto:banners-feedback@braze.com)
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
  console.log(`Banners were updated`);
})

// always refresh after your subscriber function has been registered
braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])
```

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
{% tab Java %}
```java
Braze.getInstance(context).subscribeToBannersUpdates(banners -> {
  for (Banner banner : banners.getBanners()) {
    Log.d(TAG, "Received banner: " + banner.getPlacementId());
  }
});
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).subscribeToBannersUpdates { update ->
  for (banner in update.banners) {
    Log.d(TAG, "Received banner: " + banner.placementId)
  }
}
```

{% endtab %}
{% tab React Native %}

```javascript
const bannerCardsSubscription = Braze.addListener(
  Braze.Events.BANNER_CARDS_UPDATED,
  data => {
    const banners = data.banners;
    console.log(
      `Received ${banners.length} Banner Cards with placement IDs:`,
      banners.map(banner => banner.placementId),
    );
  },
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

### Étape 4 : Intégrer à l'aide de l'ID de placement {#insertBanner}

{% tabs %}
{% tab JavaScript %}

Créez un élément conteneur pour la bannière. Veillez à définir sa largeur et sa hauteur.

```html
<div id="global-banner-container" style="width: 100%; height: 450px;"></div>
```

Ensuite, utilisez la méthode [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) pour remplacer le code HTML interne de l'élément conteneur.

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

    // Insert the banner which replacees the innerHTML of that container
    braze.insertBanner(globalBanner, container);

    // Special handling if the user is part of a Control Variant
    if (globalBanner.isControl) {
        // hide or collapse the container
        container.style.display = 'none';
    }
});

braze.requestBannersRefresh(["global_banner", "navigation_square_banner"])

```

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
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner Card according to your use case.
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
    // Use the `processContentUpdates` parameter to adjust the size and visibility of your Banner Card according to your use case.
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
{% tab Java %}
Pour obtenir la bannière en code Java, utilisez :

```java
Banner globalBanner = Braze.getInstance(context).getBanner("global_banner");
```

Vous pouvez créer des cartes bannières dans vos vues Android en incluant ce XML :

```xml
<com.braze.ui.banners.BannerView
    android:id="@+id/global_banner_id"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:placementId="global_banner" />
```

{% endtab %}
{% tab Kotlin %}
Pour obtenir la bannière en Kotlin, utilisez :
```kotlin
val banner = Braze.getInstance(context).getBanner("global_banner")
```

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

Pour obtenir le modèle de données de la carte bannière dans React Native, utilisez :

```javascript
const banner = await Braze.getBanner("global_banner");
```

Vous pouvez utiliser la méthode `getBanner` pour vérifier la présence de ce placement dans le cache de votre utilisateur. Toutefois, pour l'intégration la plus simple, ajoutez l'extrait de code JavaScript XML (JSX) suivant dans votre hiérarchie de vues, en fournissant uniquement l'ID de placement.

```javascript
<Braze.BrazeBannerView
  placementID='global_banner'
/>
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
Pour obtenir le modèle de données de la carte bannière dans Flutter, utilisez :

```dart
braze.getBanner("global_banner").then((banner) {
  if (banner == null) {
    // Handle null cases.
  } else {
    print(banner.toString());
  }
});
```

Vous pouvez utiliser la méthode `getBanner` pour vérifier la présence de ce placement dans le cache de votre utilisateur. Cependant, pour l'intégration la plus simple, ajoutez le widget suivant dans votre hiérarchie de vues, en fournissant uniquement l'ID de placement.

```dart
BrazeBannerView(
  placementId: "global_banner",
),
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

### Étape 5 : Envoyer une carte de test (facultatif) {#handling-test-cards}

Avant de [lancer une campagne Banner]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/) Card, vous pouvez envoyer une Banner Card de test pour vérifier l'intégration. Les cartes de test seront stockées dans une mémoire cache distincte et ne seront pas conservées lors des redémarrages de l'application. Bien qu'aucune configuration supplémentaire ne soit nécessaire, votre appareil de test doit être capable de recevoir des notifications push au premier plan pour pouvoir afficher la carte de test.

{% alert note %}
Les cartes bannières de test sont comme toutes les autres bannières, sauf qu'elles sont retirées lors de la prochaine session d'application.
{% endalert %}

## Enregistrer les analyses

Braze enregistre automatiquement les impressions lorsque vous utilisez les méthodes du SDK pour insérer une carte bannière - il n'est donc pas nécessaire de suivre les impressions manuellement. Si vous avez besoin d'analyser et de restituer le code HTML dans une vue personnalisée, contactez-nous à [banners-feedback@braze.com](mailto:banners-feedback@braze.com).

## Dimensions et taille

Voici ce qu'il faut savoir sur les dimensions des cartes bannières :

- Bien que le compositeur vous permette de prévisualiser les bannières dans différentes dimensions, ces informations ne sont pas enregistrées ni envoyées au SDK.
- Le code HTML occupera toute la largeur du conteneur dans lequel il est affiché.
- Nous vous recommandons de créer un élément de dimension fixe et de tester ces dimensions dans composer.
