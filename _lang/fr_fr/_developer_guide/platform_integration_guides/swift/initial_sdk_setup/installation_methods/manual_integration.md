---
nav_title: Intégration manuelle
article_title: Intégration manuelle pour iOS
platform: Swift
page_order: 3
description: "Cet article de référence montre comment intégrer le SDK Braze Swift en utilisant l'installation manuelle."
toc_headers: "h2"
---

# Intégration manuelle

> Si vous n'avez pas accès à un gestionnaire de paquets, tel que le [Gestionnaire de paquets Swift]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/swift_package_manager/) ou [CocoaPods]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/installation_methods/cocoapods/), vous pouvez intégrer manuellement le SDK Swift.

## Étape 1 : Téléchargez le SDK Braze

Accédez à la [page du SDK Braze sur GitHub](https://github.com/braze-inc/braze-swift-sdk/releases), puis téléchargez `braze-swift-sdk-prebuilt.zip`.

![Page du SDK Braze sur GitHub.]({% image_buster /assets/img/swift/sdk_integration/download-braze-swift-sdk-prebuilt.png %})

## Étape 2 : Choisissez vos frameworks

Le SDK Swift Braze contient une série de XCFrameworks autonomes, ce qui vous donne la liberté d'intégrer les fonctionnalités que vous souhaitez sans avoir besoin de toutes les intégrer. Référez-vous au tableau suivant pour choisir vos XCFrameworks :

| Offre                    | Requis ? | Description                                                                                                                                                                                                                                                                                                              |
| -------------------------- | --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `BrazeKit`                 | Oui       | Bibliothèque SDK principale avec prise en charge des analyses et des notifications push.                                                                                                                                                                                                                                             |
| `BrazeLocation`            | Non        | Bibliothèque de localisations avec prise en charge des analyses de localisation et de la surveillance des géorepérages.                                                                                                                                                                                                                                   |
| `BrazeUI`                  | Non        | Bibliothèque d'interface utilisateur fournie par Braze pour les messages in-app et les cartes de contenu.                                                                                                                                                                                                                                             |
| `BrazeNotificationService` | Non        | Bibliothèque d'extension de service de notification qui fournit une prise en charge des notifications push enrichies. N'ajoutez pas cette bibliothèque directement à la cible de votre application principale, mais [ajoutez plutôt la bibliothèque `BrazeNotificationService` séparément](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications).     |
| `BrazePushStory`           | Non        | Bibliothèque d'extension de contenu de notification qui fournit une prise en charge des Push Stories. N'ajoutez pas cette bibliothèque directement à la cible de votre application principale, mais [ajoutez plutôt la bibliothèque `BrazePushStory` séparément](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories).                                     |
| `BrazeKitCompat`           | Non        | Bibliothèque de compatibilité contenant toutes les classes et méthodes `Appboy` et `ABK*` qui étaient disponibles dans le `Appboy-iOS-SDK` version 4.X.X. Pour plus de détails sur l'utilisation, reportez-vous au scénario de migration minimal dans le [guide de migration](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `BrazeUICompat`            | Non        | Bibliothèque de compatibilité contenant toutes les classes et méthodes `ABK*` qui étaient disponibles dans la bibliothèque `AppboyUI` du `Appboy-iOS-SDK` version 4.X.X. Pour plus de détails sur l'utilisation, reportez-vous au scénario de migration minimal dans le [guide de migration](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/appboy-migration-guide/). |
| `SDWebImage`               | Non        | Dépendance utilisée uniquement par `BrazeUICompat` dans le scénario de migration minimal. |

{: .ws-td-nw-1 .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 3 : Préparez vos fichiers

Décidez si vous souhaitez utiliser des XCFrameworks **statiques** ou **dynamiques**, puis préparez vos fichiers :

{% tabs %}
{% tab dynamiques %}
1. Créez un répertoire temporaire pour vos XCFrameworks.
2. Dans `braze-swift-sdk-prebuilt`, ouvrez le répertoire `dynamic` et déplacez `BrazeKit.xcframework` dans votre répertoire. Votre répertoire devrait être similaire à ce qui suit :
    ```bash
    temp_dir
    └── BrazeKit.xcframework
    ```
3. Déplacez chacun de vos [XCFrameworks choisis](#step-2-choose-your-frameworks) dans votre répertoire temporaire. Votre répertoire devrait être similaire à ce qui suit :
    ```bash
    temp_dir
    ├── BrazeKit.xcframework
    ├── BrazeKitCompat.xcframework
    ├── BrazeLocation.xcframework
    └── SDWebImage.xcframework
    ```
{% endtab %}

{% tab statiques %}
### Étape 3.1 : Préparez vos frameworks

1. Créez un répertoire temporaire pour vos XCFrameworks.
2. Dans `braze-swift-sdk-prebuilt`, ouvrez le répertoire `static` et déplacez `BrazeKit.xcframework` dans votre répertoire. Votre répertoire devrait être similaire à ce qui suit :
   ```bash
   temp_frameworks_dir
   └── BrazeKit.xcframework
   ```
3. Déplacez chacun de vos [XCFrameworks choisis](#step-2-choose-your-frameworks) dans votre répertoire temporaire. Votre répertoire devrait être similaire à ce qui suit :
   ```bash
   temp_frameworks_dir
   ├── BrazeKit.xcframework
   ├── BrazeKitCompat.xcframework
   ├── BrazeLocation.xcframework
   └── SDWebImage.xcframework
   ```

### Étape 3.2 : Préparez vos bundles

1. Créez un répertoire temporaire pour vos bundles.
2. Ouvrez le répertoire `bundles` et déplacez `BrazeKit.bundle` dans votre répertoire. Votre répertoire devrait être similaire à ce qui suit :
   ```bash
   temp_bundles_dir
   └── BrazeKit.bundle
   ```
3. Si vous utilisez les XCFrameworks `BrazeLocation`, `BrazeUI`, `BrazeUICompat` ou `SDWebImage`, déplacez leurs paquets correspondants dans votre répertoire temporaire. Votre répertoire devrait être similaire à ce qui suit :
   ```bash
   temp_bundles_dir
   ├── BrazeLocation.bundle
   ├── BrazeUI.bundle
   ├── BrazeUICompat.bundle
   └── SDWebImage.bundle
   ```
{% alert note %}
Déplacez uniquement les paquets pour les [frameworks que vous avez préparés](#step-31-prepare-your-frameworks).
{% endalert %}
{% endtab %}
{% endtabs %}

## Étape 4 : Intégrez vos frameworks

Ensuite, intégrez les XCFrameworks **dynamiques** ou **statiques** que vous [avez préparés précédemment](#step-3-prepare-your-files) :

{% tabs %}
{% tab dynamiques %}
Dans votre projet Xcode, sélectionnez votre cible de build, puis **Général**. Sous **Frameworks, bibliothèques et contenu intégré**, faites glisser et déposez les [fichiers que vous avez préparés précédemment](#step-3-prepare-your-files).

![Exemple de projet Xcode avec chaque bibliothèque Braze définie sur Intégrer et signer.]({% image_buster /assets/img/swift/sdk_integration/embed-and-sign.png %})

{% alert tip %}
Pour activer la prise en charge des GIF, ajoutez `SDWebImage.xcframework`, situé dans `braze-swift-sdk-prebuilt/dynamic`.
{% endalert %}
{% endtab %}

{% tab statiques %}
Dans votre projet Xcode, sélectionnez votre cible de build, puis **Général**. Sous **Frameworks, Libraries, and Embedded Content**, faites glisser et déposez les [frameworks que vous avez préparés précédemment](#step-31-prepare-your-frameworks). À côté de chaque framework, choisissez **Ne pas intégrer**. 

![Exemple de projet Xcode avec chaque bibliothèque Braze définie sur Ne pas intégrer.]({% image_buster /assets/img/swift/sdk_integration/do-not-embed-and-sign.png %})

{% alert tip %}
Pour activer la prise en charge des GIF, ajoutez `SDWebImage.xcframework`, situé dans `braze-swift-sdk-prebuilt/static`.
{% endalert %}

Dans votre cible de build, sélectionnez **Phases de création**. Sous **Copier les ressources du bundle**, faites glisser et déposez les [bundles que vous avez préparés précédemment](#step-32-prepare-your-bundles).

![Exemple de projet Xcode avec des bundles ajoutés sous Copier les ressources du bundle.]({% image_buster /assets/img/swift/sdk_integration/copy-bundle-resources.png %})
{% endtab %}
{% endtabs %}

## Erreurs courantes pour les projets Objective-C

Si votre projet Xcode ne contient que des fichiers Objective-C, il se peut que vous obteniez des erreurs de « symbole manquant » lorsque vous essayez de créer votre projet. Pour corriger ces erreurs, ouvrez votre projet et ajoutez un fichier Swift vide à votre arborescence de fichiers. Ceci obligera votre chaîne d'outils de création à intégrer [Swift Runtime](https://support.apple.com/kb/dl1998) et à lier les frameworks appropriés pendant le temps de création.

```bash
FILE_NAME.swift
```

Remplacez `FILE_NAME` par n'importe quelle chaîne sans espace. Votre fichier devrait ressembler à ce qui suit :

```bash
empty_swift_file.swift
```
