---
nav_title: Options d'intégration manuelle
article_title: Options d'intégration manuelle pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence montre comment intégrer manuellement le Braze SDK pour iOS."
---

# Intégration manuelle

{% alert tip %}
Nous vous recommandons fortement d'implémenter le SDK via un gestionnaire de paquets tel que [Swift Package Manager](../swift_package_manager/), [CocoaPods](../cocoapods/), ou [Carthage](../carthage_integration/). Cela vous fera gagner beaucoup de temps et automatisera une grande partie du processus pour vous. Cependant, si vous n'êtes pas en mesure de le faire, vous pouvez compléter l'intégration manuellement en suivant les instructions ci-dessous.
{% endalert %}

## Étape 1 : Téléchargement du Braze SDK

### Option 1 : XCFramework dynamique

1. Téléchargez `Appboy_iOS_SDK.xcframework.zip` depuis la [page de publication](https://github.com/appboy/appboy-ios-sdk/releases) et extrayez le fichier.
2. Dans Xcode, faites glisser et déposez ce .xcframework dans votre projet.
3. Dans l'onglet **Général** du projet, sélectionnez **Embed & Sign** pour `Appboy_iOS_SDK.xcframework`.

### Option 2 : XCFramework statique ou Intégration statique

1. Téléchargez `Appboy_iOS_SDK.zip` depuis la page [release](https://github.com/appboy/appboy-ios-sdk/releases).
2. Dans Xcode, à partir du navigateur du projet, sélectionnez le projet ou le groupe de destination pour Braze
3. Naviguez vers **Fichier** > **Ajouter des fichiers** à « Nom du projet »
4. Ajoutez les dossiers `AppboyKit` et `AppboyUI` à votre projet en tant que groupe.
    - Assurez-vous que l'option **Copier les éléments dans le dossier du groupe de destination** est sélectionnée si vous intégrez pour la première fois. Développez **Options** dans le sélecteur de fichiers pour sélectionner **Copier des éléments si nécessaire** et **Créer des groupes**.
    - Supprimer les répertoires `AppboyKit/include` et `AppboyUI/include`
5. (Facultatif) Si vous êtes l'un des suivants :
  - Vous ne voulez que les fonctionnalités d'analyse de base du SDK et n'utilisez aucune fonctionnalité d'interface utilisateur (par exemple, les messages dans l'application ou les cartes de contenu)
  - Vous avez une interface utilisateur personnalisée pour les fonctionnalités de Braze et gérez le téléchargement de l'image vous-même

    Vous pouvez utiliser la version principale du SDK en supprimant le fichier `ABKSDWebImageProxy.m` et `Appboy.bundle`. Cela supprimera la dépendance du framework SDWebImage et toutes les ressources liées à l'interface utilisateur (par exemple les fichiers Nib, les images, les fichiers de localisation) du SDK.

{% alert warning %}
Si vous essayez d'utiliser la version principale du SDK sans les fonctionnalités de Braze, les messages dans l'application ne s'afficheront pas. Essayer d'afficher l'interface des Cartes de Contenu de Braze avec la version principale conduira à un comportement imprévisible.
{% endalert %}

## Étape 2 : Ajout des bibliothèques iOS requises

1. Cliquez sur la cible de votre projet (à l’aide de la navigation à gauche), et sélectionnez l’onglet **Étapes de construction**.
2. Cliquez sur le bouton <i class="fas fa-plus"></i> sous **Lier Binary With Libraries**.
3. Dans le menu, sélectionnez `SystemConfiguration.framework`.
4. Marquer cette bibliothèque comme nécessaire en utilisant le menu déroulant à côté de `SystemConfiguration.framework`.
5. Répétez pour ajouter chacun des frameworks requis suivants à votre projet, en le marquant comme « requis »
    - `QuartzCore.framework`
    - `libz.tbd`
    - `CoreImage.framework`
    - `CoreText.framework`
    - `WebKit.framework`
6. Ajouter les frameworks suivants et les marquer comme facultatifs :
    - `CoreTelephony.framework`
7. Sélectionnez l'onglet **Paramètres de compilation**. Dans la section **Lier** , localisez le paramètre **Autres drapeaux de lien** et ajoutez le drapeau `-ObjC`.
8. Le framework SDWebImage est requis pour que le flux de nouvelles de Braze, les cartes de contenu et la messagerie In-App fonctionnent correctement. SDWebImage est utilisé pour le téléchargement et l'affichage d'image, y compris les GIF. Si vous avez l'intention d'utiliser le fil d'actualité, les cartes de contenu ou les messages dans l'application, veuillez suivre les étapes ci-dessous.

### Intégration de SDWebImage

Pour installer SDWebImage, suivez [leurs instructions ici](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework) puis faites glisser et déposez le XCFramework résultant dans votre projet.

### Suivi de localisation optionnel

1. Ajouter le `CoreLocation.framework` pour activer le suivi de localisation
2. Vous devez autoriser la localisation de vos utilisateurs en utilisant `CLLocationManager` dans votre application

## Étape 3: Entête de pont Objective-C

Si votre projet utilise Swift, vous aurez besoin d'un fichier d'en-tête de passerelle.

Si vous n'avez pas de fichier d'en-tête de passerelle, créez-en un et nommez-le `votre-produit-nomde-module-Bridging-Header.` en choisissant **Fichier** > **Nouveau** > **Fichier** > (iOS ou OS X) > **Source** > **Fichier d'en-tête**. Ajoute ensuite la ligne de code suivante en haut de ton fichier d'en-tête de passerelle :
```
#import "AppboyKit.h"
```

Dans les paramètres de construction de votre projet, ajouter le chemin relatif de votre fichier d'en-tête au paramètre de compilation `Objective-C Bridging Header` sous `Swift Compiler - Code Generation`.

{% alert note %}
Vous n'avez pas besoin de suivre ces étapes si votre projet n'utilise que l'Objective-C.
{% endalert %}

## Étapes suivantes

Suivez les instructions pour [Compléter l'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).
