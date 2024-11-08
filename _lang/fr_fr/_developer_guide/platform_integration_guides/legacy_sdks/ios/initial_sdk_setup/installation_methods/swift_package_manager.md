---
nav_title: Gestionnaire de paquets Swift
article_title: Intégration du Gestionnaire de paquets Swift pour iOS
platform: iOS
page_order: 3
description: "Ce didacticiel couvre le SDK Braze en utilisant le Gestionnaire de paquets Swift pour iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration du Gestionnaire de paquets Swift

L’installation du SDK iOS via le [Gestionnaire de paquets Swift (SPM)](https://swift.org/package-manager/) permet d’automatiser la majeure partie du processus d’installation. Avant de commencer ce processus, assurez-vous que vous utilisez Xcode 12 ou supérieur.

{% alert note %}
tvOS n’est pas disponible actuellement via le gestionnaire de paquets Swift.
{% endalert %}

## Étape 1 : Ajouter la dépendance à votre projet

### Importer la version SDK

Ouvrez votre projet et naviguez vers les paramètres de votre projet. Sélectionnez l'onglet **Paquets Swift** et cliquez sur le bouton d'ajout <i class="fas fa-plus"></i> sous la liste des paquets.

![]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

Lors de l’importation de la version SDK `3.33.1` ou ultérieure, saisissez l’URL de notre référentiel SDK iOS (`https://github.com/braze-inc/braze-ios-sdk`) dans le champ de texte et cliquez sur **Suivant**. 

Pour les versions de `3.29.0` à `3.32.0`, utilisez l’URL `https://github.com/Appboy/Appboy-ios-sdk`.

![]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

Dans l'écran suivant, sélectionnez la version du SDK et cliquez sur **Suivant**. Les versions `3.29.0` et suivantes sont compatibles avec le gestionnaire de paquets Swift.

![]({% image_buster /assets/img/ios/spm/select_version.png %})

### Sélectionner les paquets

Sélectionnez la formule qui correspond le mieux à vos besoins et cliquez sur **Terminer**. Assurez-vous de sélectionner `AppboyKit` ou `AppboyUI`. L’inclusion des deux paquets peut entraîner un comportement indésirable :

- `AppboyUI`
  - Convient mieux si vous prévoyez d’utiliser des composants d’interface utilisateur fournis par Braze.
  - Inclut automatiquement `AppboyKit`.
- `AppboyKit`
  - Convient mieux si vous n’avez pas besoin d’utiliser les composants de l’interface utilisateur fournis par Braze (par ex., cartes de contenu, messages in-app, etc.).
- `AppboyPushStory`
  - Incluez ce paquet si vous avez intégré Push Stories dans votre application. Cela est pris en charge à partir de la version `3.31.0`.
  - Dans le menu déroulant `Add to Target`, sélectionnez votre cible `ContentExtension` plutôt que de la cible de votre application principale. 

![]({% image_buster /assets/img/ios/spm/add_package.png %})

## Étape 2 : Configuration de votre projet

Naviguez ensuite jusqu’aux **paramètres de création** de votre projet et ajoutez l’indicateur `-ObjC` au paramètre **Autres indicateurs de lien**. Cet indicateur doit être ajouté et toutes les [erreurs](https://developer.apple.com/library/archive/qa/qa1490/_index.html) résolues pour pouvoir mieux intégrer le SDK.

![]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
Si vous n’ajoutez pas l’indicateur `-ObjC`, des parties de l’API pourront manquer et le comportement ne sera pas défini. Vous pouvez rencontrer des erreurs inattendues telles qu’un « sélecteur non reconnu envoyé à la classe », des pannes de l’application et d’autres problèmes.
{% endalert %}

## Étape 3 : Modification du schéma de la cible
{% alert important %}
Si vous utilisez Xcode 12.5 ou une version plus récente, ignorez cette étape.
{% endalert %}

Si vous utilisez Xcode 12.4 ou une version antérieure, modifiez le schéma de la cible, y compris le paquet Appboy (élément de menu **Produit > Schéma > Modifier le schéma**) :
1. Développez le menu **Créer** et sélectionnez **Post-actions**. Appuyez sur le bouton plus (+) et sélectionnez **Nouvelle action de script d'exécution**.
2. Dans le menu déroulant **Fournir des paramètres de création à partir de**, sélectionnez la cible de votre application.
3.  Copiez ce script dans le champ ouvert :
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## Étapes suivantes

Suivez les instructions pour [terminer l'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

