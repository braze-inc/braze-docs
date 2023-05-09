---
hidden: true
nav_title: Carthage
article_title: Intégration de Carthage pour iOS
platform: iOS
page_order: 1
description: "Cet article de référence montre comment intégrer le SDK Braze à l’aide de Carthage pour iOS."

---

# Intégration de Carthage

## Importer le SDK

À partir de la version `4.4.0`, le SDK Braze prend en charge XCFrameworks lors de l’intégration via Carthage. Pour importer le SDK complet, incluez ces lignes dans votre `Cartfile` :
```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk.json"
github "SDWebImage/SDWebImage"
```

Consultez le [Guide de démarrage rapide de Carthage][1] pour plus d’instructions sur l’importation du SDK.

Lors de la migration d’une version antérieure à `4.4.0`, suivez le [Guide de migration de Carthage pour XCFrameworks][2].

{% alert note %}
Pour plus de détails sur la syntaxe du `Cartfile` ou des fonctionnalités telles que l’épinglage de la version, consultez la [Documentation de Carthage](https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile). 
Pour l’utilisation spécifique à la plateforme de Carthage, consultez leur [guide de l’utilisateur](https://github.com/Carthage/Carthage#if-youre-building-for-ios-tvos-or-watchos).
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

Assurez-vous de remplacer `<BRAZE_IOS_SDK_VERSION>` avec la [version appropriée][4] du SDK Braze pour iOS au format « x.y.z ».

## Étapes suivantes

Suivez les instructions pour [compléter l’intégration][5].

## Intégration principale uniquement

Si vous souhaitez utiliser le SDK Core sans composants ou dépendances de l’interface utilisateur, installez la version principale de l’infrastructure Carthage de Braze en incluant la ligne suivante dans votre `Cartfile` :

```
binary "https://raw.githubusercontent.com/Appboy/appboy-ios-sdk/master/appboy_ios_sdk_core.json"
```

[1]: https://github.com/Carthage/Carthage#quick-start
[2]: https://github.com/Carthage/Carthage#migrating-a-project-from-framework-bundles-to-xcframeworks
[4]: https://github.com/Appboy/appboy-ios-sdk/releases
[5]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/
[6]: https://github.com/Carthage/Carthage/blob/master/Documentation/Artifacts.md#cartfile
