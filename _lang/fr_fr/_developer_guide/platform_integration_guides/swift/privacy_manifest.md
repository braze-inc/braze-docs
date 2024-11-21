---
nav_title: Manifeste de confidentialité
article_title: Manifeste de confidentialité
page_order: 7
platform: Swift
description: "Apprenez à déclarer vos données de suivi Braze dans le manifeste de confidentialité de votre application."
---

# Manifeste de confidentialité

> Si votre SDK Braze collecte des données de suivi, Apple exige que vous ajoutiez un manifeste de confidentialité qui décrit votre raison et votre méthode de collecte des données de suivi.

## Qu'est-ce que les données de suivi ?

Apple définit les « données de suivi » comme des données collectées dans votre application à propos d'un utilisateur final ou d'un appareil qui sont liées à des données tierces (telles que la publicité ciblée) ou à un courtier en données. Pour une définition complète avec des exemples, voir [Apple: Suivi](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Par défaut, le SDK de Braze ne recueille pas de données de suivi. Cependant, en fonction de la configuration de votre SDK Braze, vous devrez peut-être répertorier les données spécifiques à Braze dans le manifeste de confidentialité de votre application.

## Qu'est-ce qu'un manifeste de confidentialité ?

Un manifeste de confidentialité est un fichier dans votre projet Xcode qui décrit la raison pour laquelle votre application et les SDK tiers collectent des données, ainsi que leurs méthodes de collecte de données. Chacun de vos SDK tiers qui assure le suivi des données nécessite son propre manifeste de confidentialité. Lorsque vous [créez le rapport de confidentialité de votre application](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), ces fichiers de manifeste de confidentialité sont automatiquement agrégés en un seul rapport.

## Domaines de données de suivi d'API

À partir d'iOS 17.2, Apple bloquera tous les points de suivi déclarés dans votre application jusqu'à ce que l'utilisateur final accepte une [invite de Transparence du Suivi des Publicités (ATT)](https://support.apple.com/en-us/HT212025). Braze fournit des endpoints de suivi pour acheminer vos données de suivi, tout en vous permettant d'acheminer les données first-party hors données de suivi vers l’endpoint d'origine. 

## Déclaration des données de suivi Braze

{% alert tip %}
Pour obtenir un guide complet, consultez le [tutoriel sur les données de suivi de la confidentialité](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Étape 1 : Examinez vos politiques actuelles

Examinez les politiques actuelles de collecte de données de votre SDK Braze avec votre équipe juridique pour déterminer si votre application collecte des données de suivi [telles que définies par Apple](#what-is-tracking-data). Si vous ne collectez aucune donnée de suivi, vous n'avez pas besoin de personnaliser votre manifeste de confidentialité pour le SDK Braze pour le moment. Pour plus d'informations sur les politiques de collecte de données du SDK Braze, voir [Collecte de données SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/).

{% alert important %}
Si l'un de vos SDK autres que Braze collecte des données de suivi, vous devrez examiner les politiques correspondantes séparément.
{% endalert %}

### Étape 2 : Créer un manifeste de confidentialité

Tout d'abord, vérifiez si vous disposez déjà d’un manifeste de confidentialité en recherchant la présence d’un fichier `PrivacyInfo.xcprivacy` dans votre projet Xcode. Si ce fichier existe, vous pouvez passer à l'étape suivante. Sinon, voir [Apple : Créer un manifeste de confidentialité](sdk-tracking.iad-01.braze.com).

### Étape 3 : Ajoutez votre point de terminaison au manifeste de confidentialité

Dans votre projet Xcode, ouvrez le fichier `PrivacyInfo.xcprivacy` de votre application, puis cliquez avec le bouton droit sur le tableau et cochez **Clés et valeurs brutes**.

{% alert note %}

{% endalert %}

![Un projet Xcode avec le menu contextuel ouvert et l’option « Clés et valeurs brutes » en surbrillance.]({% image_buster /assets/img/apple/privacy_manifest/check_raw_keys_and_values.png %})

Sous **Configuration de la confidentialité des applications**, choisissez **NSPrivacyTracking** et définissez sa valeur sur **OUI**.

![Le fichier 'PrivacyInfo.xcprivacy' s'ouvre avec "NSPrivacyTracking" réglé sur "OUI".]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytracking.png %})

Sous **Configuration de la confidentialité des applications**, choisissez **NSPrivacyTrackingDomains**. Dans le tableau des domaines, ajoutez un nouvel élément et définissez sa valeur sur le point de terminaison que vous [avez précédemment ajouté à votre `AppDelegate`]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/#update-your-app-delegate) préfixé par `sdk-tracking`.

![Le fichier PrivacyInfo.xcprivacy s'ouvre avec un endpoint de suivi Braze répertorié sous « NSPrivacyTrackingDomains ».]({% image_buster /assets/img/apple/privacy_manifest/add_nsprivacytrackingdomains.png %})

### Étape 4 : Déclarez vos données de suivi

Ensuite, ouvrez `AppDelegate.swift` puis listez chaque [propriété de suivi](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/configuration-swift.class/trackingproperty/) que vous souhaitez déclarer en créant une liste de suivi statique ou dynamique. Gardez à l'esprit qu'Apple bloquera ces propriétés jusqu'à ce que l'utilisateur final accepte l’invite ATT. Par conséquent, listez uniquement les propriétés que vous et votre équipe juridique envisagez pour le suivi. Par exemple :

{% tabs %}
{% tab exemple statique %}
Dans l'exemple suivant, `dateOfBirth`, `customEvent` et `customAttribute` sont déclarés comme des données de suivi dans une liste statique. 

```swift
import UIKit
import BrazeKit

@main
class AppDelegate: UIResponder, UIApplicationDelegate {

  static var braze: Braze? = nil

  func application(
    _ application: UIApplication,
    didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey: Any]?
  ) -> Bool {
    let configuration = Braze.Configuration(apiKey: brazeApiKey, endpoint: brazeEndpoint)
    // Declare which types of data you wish to collect for user tracking.
    configuration.api.trackingPropertyAllowList = [
      .dateOfBirth,
      .customEvent(["event-1"]),
      .customAttribute(["attribute-1", "attribute-2"])
    ]
    let braze = Braze(configuration: configuration)
    AppDelegate.braze = braze
    return true
  }
}
```
{% endtab %}

{% tab exemple dynamique %}
Dans l'exemple suivant, la liste de suivi est automatiquement mise à jour après que l'utilisateur final accepte l'invite ATT.

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
  // Request and check your user's tracking authorization status.
  ATTrackingManager.requestTrackingAuthorization { status in
    // Let Braze know whether user data is allowed to be collected for tracking.
    let enableAdTracking = status == .authorized
    AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)

    // Add the `.firstName` and `.lastName` properties, while removing the `.everything` configuration.
    AppDelegate.braze.updateTrackingAllowList(
      adding: [.firstName, .lastName],
      removing: [.everything]
    )
  }
}
```
{% endtab %}
{% endtabs %}

### Étape 5 : Empêcher les boucles de réessai infinies

Pour empêcher le SDK d'entrer dans une boucle d’essai infinie, utilisez la méthode `set(adTrackingEnabled: enableAdTracking)` afin de gérer les autorisations ATT. La propriété `adTrackingEnabled` dans votre méthode doit être traitée de manière similaire à ce qui suit :

```swift
func applicationDidBecomeActive(_ application: UIApplication) {
    // Request and check your user's tracking authorization status.
    ATTrackingManager.requestTrackingAuthorization { status in
      // Let Braze know whether user data is allowed to be collected for tracking.
      let enableAdTracking = status == .authorized
      AppDelegate.braze?.set(adTrackingEnabled: enableAdTracking)
    }
}
```
