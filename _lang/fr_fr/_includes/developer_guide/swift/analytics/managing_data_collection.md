## Le manifeste d'Apple sur la protection de la vie privée {#privacy-manifest}

### Qu'est-ce que les données de suivi ?

Apple définit les « données de suivi » comme des données collectées dans votre application à propos d'un utilisateur final ou d'un appareil qui sont liées à des données tierces (telles que la publicité ciblée) ou à un courtier en données. Pour une définition complète avec des exemples, voir [Apple: Suivi](https://developer.apple.com/app-store/app-privacy-details/#user-tracking).

Par défaut, le SDK de Braze ne recueille pas de données de suivi. Cependant, en fonction de la configuration de votre SDK Braze, vous devrez peut-être répertorier les données spécifiques à Braze dans le manifeste de confidentialité de votre application.

### Qu'est-ce qu'un manifeste de confidentialité ?

Un manifeste de confidentialité est un fichier dans votre projet Xcode qui décrit la raison pour laquelle votre application et les SDK tiers collectent des données, ainsi que leurs méthodes de collecte de données. Chacun de vos SDK tiers qui assure le suivi des données nécessite son propre manifeste de confidentialité. Lorsque vous [créez le rapport de confidentialité de votre application](https://developer.apple.com/documentation/bundleresources/privacy_manifest_files/describing_data_use_in_privacy_manifests#4239187), ces fichiers de manifeste de confidentialité sont automatiquement agrégés en un seul rapport.

### Domaines de données de suivi d'API

À partir d'iOS 17.2, Apple bloquera tous les points de suivi déclarés dans votre application jusqu'à ce que l'utilisateur final accepte une [invite de Transparence du Suivi des Publicités (ATT)](https://support.apple.com/en-us/HT212025). Braze fournit des endpoints de suivi pour acheminer vos données de suivi, tout en vous permettant d'acheminer les données first-party hors données de suivi vers l’endpoint d'origine. 

## Déclaration des données de suivi Braze

{% alert tip %}
Pour obtenir un guide complet, consultez le [tutoriel sur les données de suivi de la confidentialité](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking/).
{% endalert %}

### Conditions préalables

La version suivante du SDK de Braze est nécessaire pour mettre en œuvre cette fonctionnalité :

{% sdk_min_versions swift:9.0.0 %}

### Étape 1 : Examinez vos politiques actuelles

Examinez les politiques actuelles de collecte de données de votre SDK Braze avec votre équipe juridique pour déterminer si votre application collecte des données de suivi [telles que définies par Apple](#what-is-tracking-data). Si vous ne collectez aucune donnée de suivi, vous n'avez pas besoin de personnaliser votre manifeste de confidentialité pour le SDK Braze pour le moment. Pour plus d'informations sur les politiques de collecte de données du SDK Braze, voir [Collecte de données SDK]({{site.baseurl}}/user_guide/data/user_data_collection/sdk_data_collection/).

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

## Désactivation du suivi des données

Pour désactiver l'activité de suivi des données sur le SDK Swift, définissez la propriété [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled) à `false` sur votre instance Braze. Lorsque la propriété `enabled` est définie sur `false`, le SDK Braze ignore tous les appels à l'API publique. Le SDK annule également toutes les actions à la volée, telles que les requêtes réseau, le traitement des événements, etc. 

## Effacement des données précédemment stockées

Vous pouvez utiliser la méthode [`wipeData()`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/wipedata()) pour effacer complètement les données SDK stockées localement sur l'appareil d'un utilisateur.

Pour les versions 7.0.0 et ultérieures de Braze Swift, le SDK et la méthode `wipeData()` génèrent de manière aléatoire un UUID pour l'identifiant de l'appareil. Cependant, si votre `useUUIDAsDeviceId` est défini sur `false` _ou si_ vous utilisez la version 5.7.0 ou antérieure du SDK Swift, vous devrez également effectuer une demande d'envoi à [`/users/delete`]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/) car votre identifiant pour les fournisseurs (IDFV) sera automatiquement utilisé comme identifiant d'appareil de cet utilisateur.

## Reprise du suivi des données

Pour reprendre la collecte de données, définissez [`enabled`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/enabled/) sur `true`. Gardez à l'esprit que cette opération ne permet pas de restaurer les données précédemment effacées.

## Collection IDFV

Dans les versions antérieures du SDK iOS de Braze, le champ IDFV (identifiant du vendeur) était renseigné automatiquement à partir de l’ID de l’appareil de l’utilisateur. À partir du SDK Swift `v5.7.0`, le champ IDFV a été désactivé de manière facultative et, à la place, Braze définissait un UUID aléatoire comme identifiant de l'appareil. À partir du SDK Swift `v7.0.0`, le champ IDFV ne sera pas collecté par défaut, et un UUID sera défini comme identifiant de l'appareil à la place.

La fonctionnalité `useUUIDAsDeviceId` configure le [SDK Swift](https://github.com/braze-inc/braze-swift-sdk) pour qu'il définisse l'ID de l'appareil en tant qu’UUID. Traditionnellement, le SDK iOS attribuerait un ID d’appareil égal à la valeur IDFV générée par Apple. Avec cette fonctionnalité activée par défaut sur votre app iOS, tous les nouveaux utilisateurs créés via le SDK se verraient attribuer un ID d'appareil égal à un UUID.

Si vous souhaitez toujours collecter l'IDFV séparément, vous pouvez utiliser [`set(identifierforvendor:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/set(identifierforvendor:)).

### Considérations

#### Version du SDK

Dans le SDK Swift `v7.0.0+`, lorsque `useUUIDAsDeviceId` est activé (par défaut), tous les nouveaux utilisateurs créés se verront attribuer un identifiant d'appareil aléatoire. Tous les utilisateurs existants auparavant conserveront la même valeur d’ID d’appareil, qui peut avoir été un IDFV.

Si cette fonctionnalité n'est pas activée, les appareils continueront à se voir attribuer l'IDFV lors de leur création.

#### En aval 

**Partenaires technologiques** : Lorsque cette fonctionnalité est activée, tous les partenaires technologiques qui dérivent la valeur IDFV de l'ID de l'appareil Braze n'auront plus accès à ces données. Si la valeur IDFV dérivée de l'appareil est nécessaire pour l'intégration de votre partenaire, nous vous recommandons de régler cette fonctionnalité sur `false`.

**Currents** : lorsque `useUUIDAsDeviceId` est défini sur « true » (« vrai »), l'ID d'appareil envoyé dans Currents ne sera plus égal à la valeur IDFV.

### Foire aux questions

#### Ce changement aura-t-il un impact sur mes utilisateurs existants dans Braze ?

Non. Lorsqu’elle est activée, cette fonctionnalité n’écrase aucune donnée utilisateur dans Braze. Les nouveaux ID d'appareil UUID ne seront créés que pour les nouveaux appareils ou lorsque `wipedata()` est appelé.

#### Puis-je désactiver cette fonctionnalité après l’avoir activée ?

Oui, cette fonctionnalité peut être activée et désactivée à votre discrétion. Les ID d’appareil précédemment stockés ne seront jamais écrasés.

#### Puis-je toujours recueillir ailleurs la valeur IDFV via Braze ?

Oui, vous pouvez toujours facultativement recueillir l’IDFV via le SDK Swift (la collecte est désactivée par défaut). 
