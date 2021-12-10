---
nav_title: Intégration de Carthage
article_title: Intégration de Carthage pour iOS
platform: iOS
page_order: 1
description: "Cet article de référence montre comment intégrer le Braze SDK en utilisant Carthage pour iOS."
---

# Intégration de Carthage

À partir de la version `4.4.0`, le Braze SDK prend en charge XCFrameworks lors de l'intégration via Carthage. Pour importer le SDK complet, inclure ces lignes dans votre `Cartfile`:
```
binaire "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Veuillez consulter le [guide de démarrage rapide de Carthage][1] pour plus d'instructions sur l'importation du SDK.

Lors de la migration d'une version antérieure à `4.4.0`, suivez le guide de migration [Carthage pour XCFrameworks][2].

{% alert note %}

Pour plus de détails sur la syntaxe du `Cartfile` ou des fonctionnalités telles que l'épinglage de version, consultez <a href="https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile">la documentation de Carthage</a>. Pour une utilisation spécifique à la plate-forme de Carthage, reportez-vous à leur <a href="https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos">guide utilisateur</a>.

{% endalert %}

### Versions précédentes

Pour les versions `3.24.0` à `4.3.4`, incluez simplement cette ligne dans votre `Cartfile`:
```
binaire "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

Pour importer des versions antérieures à `3.24.0`, incluez ce qui suit dans votre `Cartfile`:
```
github "Appboy/Appboy-iOS-SDK"<BRAZE_IOS_SDK_VERSION>"
```

Assurez-vous de remplacer `<BRAZE_IOS_SDK_VERSION>` par la version appropriée du SDK Braze iOS au format "x.y.z". Les versions de version sont disponibles [ici][4].

## Étapes suivantes

Suivez les instructions pour [Compléter l'intégration][5].

## Intégration des noyaux uniquement
Si vous voulez utiliser le SDK du Core sans composant d'interface utilisateur ou dépendances, installez la version de base du framework Braze Carthage en incluant la ligne suivante dans votre Cartfile :

```
binaire "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

[1]: https://github.com/Carthage/Carthage#quick-start
[2]: https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks
[4]: https://github.com/Appboy/appboy-ios-sdk/releases
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/
