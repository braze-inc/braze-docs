---
nav_title: Intégration des cartes bannières
article_title: Intégration des cartes bannières
hidden: true
description: "Cet article de référence traite des cartes bannières et de l'intégration de cette fonctionnalité dans le SDK de Braze."
platform:
  - iOS
  - Android
  - Web
  
---

# Intégration des cartes bannières

Similaires aux [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about), les cartes bannières sont intégrées directement dans votre application ou votre site web afin que vous puissiez engager les utilisateurs avec une expérience sur type bannière. Ils constituent une solution rapide et fluide pour créer des messages personnalisés pour vos utilisateurs tout en étendant la portée d'autres canaux (tels que l'e-mail ou les notifications push).

{% alert important %}
Les cartes bannières sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

Cette fonctionnalité est disponible à partir des [versions suivantes du SDK]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions) :

{% sdk_min_versions swift:11.3.0 android:33.1.0 web:5.6.0 %}

## Conditions préalables pour le tableau de bord

### Définir les placements {#define-placements}

Avant de lancer une campagne Banner Card dans votre appli, vous devez configurer un placement dans le tableau de bord de Braze. Les emplacements/localisations sont des emplacements que vous définissez dans votre application et qui peuvent afficher des cartes bannières.

#### Étape 1 : Créer un nouveau placement

Allez dans **Settings** > **Banner Cards Placements**, puis sélectionnez **Create Placement**.

![Section Placement des cartes bannières pour créer des ID de placement.]({% image_buster /assets/img/banner_cards/create_placement.png %})

#### Étape 2 : Complétez les détails

Donnez un nom à votre placement et attribuez-lui un **ID de placement**. En option, vous pouvez ajouter une description de votre placement.

Travaillez avec votre équipe de marketeurs pour créer cet ID. C'est l'ID auquel vous ferez référence dans le code de votre application, et votre équipe marketing l'utilisera pour attribuer une campagne à l'emplacement/localisation dans votre application. 

{% alert important %}
Évitez de modifier votre ID de placement après le lancement, car cela peut rompre l'intégration avec votre app ou votre site web.
{% endalert %}

![Les détails de placement qui désignent une carte de promotion s'afficheront dans la barre latérale gauche pour les campagnes de promotion des soldes de printemps.]({% image_buster /assets/img/banner_cards/placement_details_example.png %})

Pour savoir comment lancer une campagne de cartes bannières, reportez-vous à la section [Créer une carte bannière]({{site.baseurl}}/create_banner_card/).

## Actualiser les placements dans votre application {#requestBannersRefresh}

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
This feature is not currently supported on React Native.
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
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Écoutez les mises à jour {#subscribeToBannersUpdates}

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
This feature is not currently supported on React Native.
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
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Obtenez et insérez une carte de bannière par ID de placement {#insertBanner}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

braze.subscribeToBannersUpdates((banners) => {
   
    // get this placement's banner. If it's `null` the user did not qualify for one.
    const globalBanner = braze.getBanner("global_banner");

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
  let bannerUIView = BrazeBannerUI.BannerUIView(placementId: "global_banner", braze: braze)
}

// Similarly, if you want a Banner view in SwiftUI, use the corresponding `BannerView` initializer:
if let braze = AppDelegate.braze {
  let bannerView = BrazeBannerUI.BannerView(placementId: "global_banner", braze: braze)
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

```javascript
This feature is not currently supported on React Native.
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
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

## Analyse

Vous n'avez pas à vous préoccuper du suivi manuel des impressions car Braze gère automatiquement l'enregistrement des impressions lorsque vous utilisez les méthodes du SDK pour insérer des cartes bannières.

Si vous avez besoin d'analyser et de rendre le HTML dans une vue personnalisée, [contactez-nous](mailto:banners-feedback@braze.com).

{% details Plus d'informations sur le suivi manuel des impressions %}

{% alert important %}
La personnalisation de votre intégration n'est probablement pas nécessaire, c'est pourquoi il convient d'examiner attentivement l'étape suivante.
{% endalert %}

{% tabs %}
{% tab JavaScript %}

```javascript
import * as braze from "@braze/web-sdk";

const banner = braze.getBanner("global_banner");
if (banner?.html) {
  // do something with the html
  // then log an impression when the HTML is in view
  braze.logBannerImpressions([banner.id]);
}
```

{% endtab %}
{% tab Swift %}

```swift
// First, get the Banner object:
var globalBanner: Braze.Banner?
brazeClient.braze()?.banners.getBanner(for: "global_banner", { banner in
  globalBanner = banner
})

// Then log the impression on the Banner.
globalBanner?.context?.logImpression()
```
{% endtab %}
{% tab Java %}
```java
Braze.getInstance(context).logBannerImpression(banner.getPlacementId());
```

{% endtab %}
{% tab Kotlin %}

```kotlin
Braze.getInstance(context).logBannerImpression(banner.placementId)
```

{% endtab %}
{% tab React Native %}

```javascript
This feature is not currently supported on React Native.
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
This feature is not yet available in Flutter.
```
{% endtab %}

{% tab Roku %}
```brightscript
This feature is not currently supported on Roku.
```
{% endtab %}
{% endtabs %}

{% enddetails %}

## Bonnes pratiques

### Dimensions de la carte bannière

- Aucune information sur les dimensions n'est envoyée par Braze.

{% alert note %}
Le compositeur permet à l'utilisateur de prévisualiser les bannières dans différentes dimensions. Ces informations ne sont ni enregistrées ni envoyées au SDK.
{% endalert %}

- Le code HTML occupera toute la largeur du conteneur dans lequel il est affiché.
- Nous vous recommandons de créer un élément de dimension fixe et de tester ces dimensions dans composer.
