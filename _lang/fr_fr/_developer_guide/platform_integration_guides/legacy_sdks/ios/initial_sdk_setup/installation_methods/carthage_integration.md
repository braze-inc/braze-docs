---
nav_title: Carthage
article_title: Intégration de Carthage pour iOS
platform: iOS
page_order: 1
description: "Cet article de référence montre comment intégrer le SDK Braze à l’aide de Carthage pour iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Intégration de Carthage

## Importer le SDK

À partir de la version `4.4.0`, le SDK Braze prend en charge XCFrameworks lors de l’intégration via Carthage. Pour importer le SDK complet, incluez ces lignes dans votre `Cartfile` :
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Consultez le [Guide de démarrage rapide de Carthage](https://github.com/Carthage/Carthage#quick-start) pour plus d'instructions sur l'importation du SDK.

Lors de la migration à partir d'une version antérieure à `4.4.0`, suivez le [Guide de migration de Carthage pour XCFrameworks](https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks).

{% alert note %}
Pour plus de détails sur la syntaxe du `Cartfile` ou des fonctionnalités telles que le verrouillage de version, consultez la [documentation de Carthage](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile).
Pour l'utilisation spécifique à la plateforme de Carthage, consultez leur [guide de l'utilisateur](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos).
{% endalert %}

### Versions précédentes

Pour les versions `3.24.0` à `4.3.4`, incluez les éléments suivants dans votre `Cartfile` :
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_full.json"
```

Pour importer des versions antérieures à `3.24.0`, incluez les éléments suivants dans votre `Cartfile` :
```
github "Appboy/Appboy-iOS-SDK" "<BRAZE_IOS_SDK_VERSION>"
```

Assurez-vous de remplacer `<BRAZE_IOS_SDK_VERSION>` par la [version appropriée](https://github.com/Appboy/appboy-ios-sdk/releases) du SDK iOS de Braze au format "x.y.z".

## Étapes suivantes

Suivez les instructions pour [compléter l'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

## Intégration principale uniquement

Si vous souhaitez utiliser le SDK Core sans composants ou dépendances de l’interface utilisateur, installez la version principale de l’infrastructure Carthage de Braze en incluant la ligne suivante dans votre `Cartfile` :

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

