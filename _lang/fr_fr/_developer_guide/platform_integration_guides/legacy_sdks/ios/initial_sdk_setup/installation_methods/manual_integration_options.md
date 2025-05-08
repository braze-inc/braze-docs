---
nav_title: Manual (Manuel)
article_title: Options d’intégration manuelle pour iOS
platform: iOS
page_order: 4
description: "Cet article de référence montre comment intégrer manuellement le SDK Braze pour iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration manuelle

{% alert tip %}
Nous vous recommandons vivement d’implémenter le SDK via un gestionnaire de paquets tel que [Gestionnaire de paquets swift](../swift_package_manager/), [CocoaPods](../cocoapods/) ou [Carthage](../carthage_integration/). Cela vous fera gagner beaucoup de temps et automatisera une grande partie du processus. Cependant, si vous ne parvenez pas à le faire, vous pouvez terminer l’intégration manuellement en suivant les instructions.
{% endalert %}

## Étape 1 : Téléchargement du SDK Braze

### Option 1 : XCFramework dynamique

1. Téléchargez `Appboy_iOS_SDK.xcframework.zip` depuis la [page de publication](https://github.com/appboy/appboy-ios-sdk/releases) et extrayez le fichier.
2. Dans Xcode, faites glisser et déposez `.xcframework` dans votre projet.
3. Sous l'onglet **Général** du projet, sélectionnez **Embed & Sign** for `Appboy_iOS_SDK.xcframework`.

### Option 2 : XCFramework statique pour l’intégration statique

1. Téléchargez `Appboy_iOS_SDK.zip` à partir de la [page de version](https://github.com/appboy/appboy-ios-sdk/releases).<br><br>
2. Dans Xcode, à partir du navigateur de projet, sélectionnez le projet ou le groupe de destination pour Braze<br><br>
3. Sélectionnez **Fichier > Ajouter des fichiers > Nom_du_projet**.<br><br>
4. Ajoutez les dossiers `AppboyKit` et `AppboyUI` de votre projet en tant que groupe.
	- Assurez-vous que l'option **Copier les éléments dans le dossier du groupe de destination** est sélectionnée si vous effectuez l'intégration pour la première fois. Développez **Options** dans le sélecteur de fichiers pour sélectionner **Copier les éléments si nécessaire** et **Créer des groupes**.
	- Supprimer les répertoires `AppboyKit/include` et `AppboyUI/include`.<br><br>
5. (Facultatif) Si l’un des éléments suivants s’applique à vous :
  - Vous souhaitez uniquement bénéficier des fonctionnalités d'analyse de base du SDK et n'utilisez aucune fonctionnalité de l'interface utilisateur (par exemple, les messages in-app ou les cartes de contenu).
  - Vous disposez d'une interface utilisateur personnalisée pour les fonctionnalités de Braze UI et gérez vous-même le téléchargement des images.<br><br>Vous pouvez utiliser la version principale du SDK en supprimant le fichier `ABKSDWebImageProxy.m` et `Appboy.bundle`. Cela supprimera la dépendance du framework `SDWebImage` et toutes les ressources liées à l'interface utilisateur (par exemple, les fichiers Nib, les images, les fichiers de localisation) du SDK.

{% alert warning %}
Si vous essayez d'utiliser la version principale du SDK sans les fonctionnalités de l’IU de Braze, les messages in-app ne s'afficheront pas. Si vous essayez d'afficher l'interface utilisateur des cartes de contenu de Braze avec la version de base, vous risquez d'obtenir des résultats imprévisibles.
{% endalert %}

## Étape 2 : Ajouter les bibliothèques iOS requises

1. Cliquez sur la cible de votre projet (en utilisant la navigation de gauche), et sélectionnez l'onglet **Phases de création**.<br><br>
2. Cliquez sur le bouton <i class="fas fa-plus"></i> sous **Lien binaire avec les bibliothèques**.<br><br>
3. Dans le menu, sélectionnez `SystemConfiguration.framework`.<br><br>
4. Marquez cette bibliothèque comme requise à l’aide du menu déroulant à côté de `SystemConfiguration.framework`.<br><br>
5. Répétez l'opération pour ajouter chacun des frameworks suivants à votre projet, en les marquant comme « requis ».
	- `QuartzCore.framework`
	- `libz.tbd`
	- `CoreImage.framework`
	- `CoreText.framework`
	- `WebKit.framework`<br><br>
6. Ajoutez les infrastructures suivantes et marquez-les comme facultatif :
	- `CoreTelephony.framework`<br><br>
7. Sélectionnez l'onglet **Build Settings (Paramètres de création)**. Dans la section **Liaison**, localisez le paramètre **Autres indicateurs de lien** et ajoutez l’indicateur `-ObjC`.<br><br>
8. Le cadre `SDWebImage` est nécessaire pour les cartes de contenu et les messages in-app pour fonctionner correctement. `SDWebImage` est utilisé pour télécharger et afficher l’image, y compris les GIF. Si vous avez l’intention d’utiliser les cartes de contenu ou les messages in-app, suivez les étapes d’intégration SDWebImage.

### Intégration de SDWebImage

Pour installer `SDWebImage`, suivez les [instructions](https://github.com/SDWebImage/SDWebImage/wiki/Installation-Guide#build-sdwebimage-as-xcframework), puis faites glisser et déposez le `XCFramework` créé dans votre projet.

### Suivi facultatif de la localisation

1. Ajouter le `CoreLocation.framework` pour activer le suivi de la localisation.
2. Vous devez autoriser la localisation de vos utilisateurs à l’aide de `CLLocationManager` dans votre application.

## Étape 3 : Objective-C bridging header

{% alert note %}
Si votre projet utilise uniquement Objective-C, ignorez cette étape.
{% endalert %}

Si votre projet utilise Swift, vous aurez besoin d’un fichier d’en-tête de pont.

Si vous n'avez pas de fichier d'en-tête de pontage, créez-en un et nommez-le `your-product-module-name-Bridging-Header.h` en choisissant **Fichier > Nouveau > Fichier > (iOS ou OS X) > Source > Fichier d'en-tête.** Ajoutez ensuite la ligne de code suivante au haut de votre fichier d’en-tête de pont :
```
#import "AppboyKit.h"
```

Dans les **paramètres de création** de votre projet, ajoutez le chemin relatif de votre fichier d’en-tête au paramètre de création `Objective-C Bridging Header` sous `Swift Compiler - Code Generation`.

## Étapes suivantes

Suivez les instructions pour [terminer l'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).
