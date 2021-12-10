---
nav_title: Gestionnaire de paquets Swift
article_title: Intégration du Gestionnaire de Paquets Swift pour iOS
platform: iOS
page_order: 3
description: "Ce tutoriel explique comment installer Braze SDK en utilisant Swift Package Manager pour iOS."
---

# Intégration du gestionnaire de paquets Swift

## Exigences

Installer le SDK iOS via [Swift Package Manager][1] (SPM) automatise la majorité du processus d'installation pour vous. Avant de commencer ce processus, assurez-vous que vous utilisez Xcode 12 ou plus.

{% alert note %}
tvOS n'est actuellement pas disponible via Swift Package Manager.
{% endalert %}


## Étape 1 : Ajout de la dépendance à votre projet

Ouvrez votre projet et accédez aux paramètres de votre projet. Sélectionnez l'onglet nommé **Packages Swift** et cliquez sur le bouton ajouter (+) en bas à gauche.

!\[Gestionnaire de paquets Swift : Menu 1\]\[2\]

Lors de l'importation de la version SDK `3.33.1` et supérieure, entrez l'URL de notre dépôt de SDK iOS (`https://github. om/braze-inc/braze-ios-sdk`) dans le champ de texte et cliquez sur **Suivant**.

{% alert note %}
Pour les versions `3.29.0` à `3.32.0`, utilisez l'URL `https://github.com/Appboy/Appboy-ios-sdk`.
{% endalert %}

!\[Gestionnaire de paquets Swift : Menu 2\]\[3\]

Sur l'écran suivant, sélectionnez la version du SDK et cliquez sur **Suivant**.

{% alert note %}
Les versions 3.29.0 et supérieures sont compatibles avec Swift Package Manager.
{% endalert %}

!\[Gestionnaire de paquets Swift : Menu 3\]\[4\]

Sélectionnez le forfait qui correspond le mieux à vos besoins et cliquez sur **Terminer**:
- `AppboyUI`
  - Le mieux adapté si vous prévoyez d'utiliser les composants de l'interface utilisateur fournis par Braze.
  - Inclut `AppboyKit` automatiquement.
- `AppboyKit`
  - Idéal si vous n'avez pas besoin d'utiliser l'un des composants de l'interface utilisateur fournis par Braze (par exemple, Cartes de contenu, Messages In-App, etc.).
- `AppboyPushStory`
  - Inclure ce package si vous avez intégré Push Stories dans votre application. Ceci est supporté depuis la version 3.31.0.
  - Dans le menu déroulant sous `Ajouter à la cible`, sélectionnez votre cible `ContentExtension` au lieu de la cible de votre application principale.

> Assurez-vous de sélectionner **soit** `AppboyKit` **ou** `AppboyUI`. Inclure les deux paquets peut conduire à un comportement indésirable.

!\[Gestionnaire de paquets Swift : Menu 4\]\[5\]

## Étape 2 : Configurer votre projet

Ensuite, accédez aux paramètres de construction de votre projet et ajoutez le drapeau `-ObjC` au paramètre **Autres drapeaux de lien**.

{% alert important %}
Ce drapeau __doit être ajouté et toutes les [erreurs](https://developer.apple.com/library/archive/qa/qa1490/_index.html) résolues__ afin d'intégrer davantage le SDK.
{% endalert %}

!\[Gestionnaire de paquets Swift : Menu 5\]\[6\]

{% alert note %}
Si vous n'ajoutez pas le drapeau `-ObjC` , certaines parties de l'API peuvent devenir manquantes et le comportement sera indéfini. Vous pouvez rencontrer des erreurs inattendues telles que "un sélecteur non reconnu envoyé à la classe", des plantages de l'application et d'autres problèmes.
{% endalert %}

## Étape 3 : Modifier le schéma de la cible

Si vous utilisez Xcode 12. ou plus tôt modifier le schéma de la cible, y compris le paquet Appboy (_Produit > Schéma > Editer l'élément de menu_ Schéma:
- Développez le menu **Build** et sélectionnez **Post-actions**. Appuyez sur le bouton plus (+) et sélectionnez **Nouvelle action de script d'exécution**.
- Dans la liste déroulante **Fournissez les paramètres de compilation de** , sélectionnez la cible de votre application.
- Copiez ce script dans le champ ouvert :
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (si applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

{% alert note %}
Vous n'avez pas besoin d'effectuer cette étape si vous utilisez Xcode 12.5 ou une version plus récente.
{% endalert %}

!\[Gestionnaire de paquets Swift : Menu 7\]\[7\]

## Étapes suivantes

Suivez les instructions pour [Compléter l'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).
[2]: {% image_buster /assets/img/ios/spm/swiftpackages.png %} [3]: {% image_buster /assets/img/ios/spm/importsdk_example.png %} [4]: {% image_buster /assets/img/ios/spm/select_version. ng %} [5]: {% image_buster /assets/img/ios/spm/add_package.png %} [6]: {% image_buster /assets/img/ios/spm/buildsettings. ng %} [7]: {% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %}

[1]: https://swift.org/package-manager/
