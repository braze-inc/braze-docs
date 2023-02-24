---
nav_title: iOS
article_title: Intégration SDK iOS pour Unity
platform: 
  - Unity
  - iOS
page_order: 0
description: "Cet article de référence couvre l’intégration SDK iOS pour la plateforme Unity."
search_rank: .9
---

# Intégration SDK iOS

Suivez ce guide pour utiliser Braze dans votre application Unity. Si vous effectuez une transition depuis une intégration manuelle, consultez les instructions sur la [Transition vers une intégration automatisée][5].

## Étape 1 : Choisissez votre package Braze Unity

Braze [`.unitypackage`][41] regroupe des liaisons natives pour les plateformes Android et iOS, ainsi qu’une interface C#.

Il existe plusieurs packages Braze Unity disponibles au téléchargement sur la [Page des versions de Braze Unity ][42] :
- `Appboy.unitypackage`
    - Ce package regroupe les SDK Android et iOS Braze et la dépendance [SDWebImage du SDK iOS][unity-1], nécessaire pour le fonctionnement approprié des messages in-app de Braze et des fonctionnalités de carte de contenu sur iOS. L’infrastructure SDWebImage est utilisée pour télécharger et afficher des images, y compris des GIF. Si vous avez l’intention d’utiliser la fonctionnalité Braze dans son intégralité, téléchargez et importez ce package.
- `Appboy-nodeps.unitypackage`
    - Ce package est similaire à `Appboy.unitypackage` à l’exception de l’infrastructure [SDWebImage ][unity-1]qui n’est pas présente. Ce package est utile si vous ne souhaitez pas que l’infrastructure SDWebImage soit présente dans votre application iOS.

**iOS**: Pour voir si vous avez besoin de la dépendance [SDWebImage][unity-1] pour votre projet iOS, consultez la [Documentation sur les messages in-app iOS][unity-4].<br>
**Android**: À partir d’Unity 2.6.0, l’artefact SDK groupé de Braze Android nécessite les dépendances [AndroidX][unity-3]. Si vous utilisiez auparavant un `jetified unitypackage`, alors vous pouvez effectuer une transition en toute sécurité vers le `unitypackage` correspondant.

## Étape 2 : Importer le package

Dans Unity Editor, importez le package dans votre projet Unity en naviguant vers **Actifs > Importer un package > Personnaliser le package**. Cliquez ensuite sur **Importer**.

Sinon, suivez les instructions pour [Importer un package d’actifs Unity ][41] pour un guide plus détaillé sur l’importation des packages Unity personnalisés. 

{% alert note %}
Si vous souhaitez importer le plug-in iOS ou Android uniquement, désélectionnez le sous-répertoire `Plugins/Android` ou `Plugins/iOS` lors de l’importation du Braze `.unitypackage`.
{% endalert %}

## Étape 3 : Définir votre clé API

Braze fournit une solution Unity native pour l’automatisation de l’intégration Unity iOS. Cette solution modifie le projet Xcode conçu à l’aide des unités [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) et des sous-classes `UnityAppController` utilisant la macro `IMPL_APP_CONTROLLER_SUBCLASS`.

1. Dans Unity Editor, ouvrez les paramètres de configuration de Braze en naviguant jusqu’à **Braze > Configuration Braze**.
2. Vérifiez la boîte **Automatiser l’intégration iOS Unity**.
3. Dans le champ « Clé API Braze », saisissez la clé API de votre application présente dans **Gérer les paramètres**.

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Si votre application utilise déjà une autre sous-classe `UnityAppController`, vous devrez fusionner votre implémentation de sous-classe avec `AppboyAppDelegate.mm`.

## Intégration SDK de base terminée

Braze devrait maintenant collecter des données depuis votre application et votre intégration de base devrait être terminée. Consultez les articles suivants pour plus d’informations sur l’intégration des notifications push ([Android][53] et [iOS][50]), [Messages in-app][34] et [Cartes de contenu][40].

## Options d’implémentation avancées supplémentaires

### Extension du SDK (iOS)

Pour étendre les comportements du SDK, bifurquez le [Projet Braze Unity SDK GitHub](https://github.com/appboy/appboy-unity-sdk) et effectuez les modifications nécessaires.

Pour publier votre code modifié en tant que package Unity, consultez nos [Cas d’utilisation avancés]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Advanced_Use_Cases/advanced_use_cases).

### Passer d’une intégration manuelle à une intégration automatisée (iOS)

Pour profiter de l’intégration automatisée iOS proposée dans le SDK Unity de Braze, suivez ces étapes pour passer d’un mode manuel à une intégration automatisée.

1. Supprimez tous les codes liés à Braze de votre sous-classe `UnityAppController` de projet Xcode.
2. Supprimez les bibliothèques iOS de Braze de votre projet Unity ou Xcode (c.-à-d., `Appboy_iOS_SDK.framework` et `SDWebImage.framework`) et [importer le package Unity Braze](#step-1-importing-the-braze-unity-package) dans votre projet Unity.
3. Suivez les instructions d’intégration dans [Configuration de votre clé API via Unity](#step-2-setting-your-api-key).

[5]: #transitioning-from-manual-to-automated-integration-ios
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-2]: https://firebase.google.com/docs/unity/setup
[unity-3]: https://developer.android.com/jetpack/androidx
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/overview/
