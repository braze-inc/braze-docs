---
nav_title: iOS
article_title: Intégration SDK iOS pour Unity
platform: 
  - Unity
  - iOS
page_order: 1
description: "Cet article de référence couvre l’intégration SDK iOS pour la plateforme Unity."
search_rank: .9
---

# Intégration SDK iOS

> Cet article de référence couvre l’intégration SDK iOS pour la plateforme Unity. Suivez ce guide pour utiliser Braze dans votre application Unity. 

Si vous passez d'une intégration manuelle à une intégration automatisée, lisez les instructions relatives à la [transition vers une intégration automatisée](#transitioning-from-manual-to-automated-integration-ios).

## Étape 1 : Choisissez votre package Braze Unity

Le [`.unitypackage`](https://docs.unity3d.com/Manual/AssetPackages.html) Braze regroupe des liaisons natives pour les plateformes Android et iOS, ainsi qu’une interface C#.

Le package Braze Unity est disponible au téléchargement sur la [page des versions de Braze Unity](https://github.com/Appboy/appboy-unity-sdk/releases) avec deux options d'intégration :

1. `Appboy.unitypackage` uniquement
  - Ce paquet regroupe les SDK Android et iOS de Braze sans aucune dépendance supplémentaire. Cette méthode d'intégration ne permet pas d’utiliser pleinement l’envoi de messages in-app et les fonctionnalités de cartes de contenu de Braze sur iOS. Si vous avez l'intention d'utiliser toutes les fonctionnalités de Braze sans code personnalisé, utilisez plutôt l'option ci-dessous.
  - Pour utiliser cette option d'intégration, assurez-vous que la case à côté de `Import SDWebImage dependency` est *décochée* dans l'interface utilisateur Unity sous Configuration Braze.
2. `Appboy.unitypackage` avec `SDWebImage`
  - Cette option d'intégration regroupe les SDK Android et iOS de Braze et la dépendance [SDwebimage](https://github.com/SDWebImage/SDWebImage) pour le SDK iOS, qui est nécessaire au bon fonctionnement de la messagerie in-app de Braze, et des fonctionnalités des cartes de contenu sur iOS. Le cadre `SDWebImage` est utilisé pour télécharger et afficher des images, y compris des GIF. Si vous avez l’intention d’utiliser la fonctionnalité Braze dans son intégralité, téléchargez et importez ce package.
  - Pour importer automatiquement `SDWebImage`, veillez à *cocher* la case à côté de `Import SDWebImage dependency` dans l'interface utilisateur Unity sous Configuration Braze.

**iOS**: Pour savoir si vous avez besoin de la dépendance [SDWebimage](https://github.com/SDWebImage/SDWebImage) pour votre projet iOS, consultez le site [iOS in-app message documentation]({{ site.baseurl }}/developer_guide/platform_integration_guides/swift/in-app_messaging/overview/).<br>
**Android**: À partir de la version 2.6.0 de Unity, l’artefact SDK groupé de Braze Android nécessite les dépendances [AndroidX](https://developer.android.com/jetpack/androidx). Si vous utilisiez auparavant un `jetified unitypackage`, alors vous pouvez effectuer une transition en toute sécurité vers le `unitypackage` correspondant.

## Étape 2 : Importer le package

Dans Unity Editor, importez le package dans votre projet Unity en sélectionnant **Actifs > Importer un package > Personnaliser le package**. Cliquez ensuite sur **Importer**.

Vous pouvez également suivre les instructions pour [Importer un package d’actifs Unity](https://docs.unity3d.com/Manual/AssetPackages.html) pour accéder à un guide plus détaillé sur l’importation des packages Unity personnalisés. 

{% alert note %}
Si vous souhaitez importer le plug-in iOS ou Android uniquement, désélectionnez le sous-répertoire `Plugins/Android` ou `Plugins/iOS` lors de l’importation du Braze `.unitypackage`.
{% endalert %}

## Étape 3 : Définir votre clé API

Braze fournit une solution Unity native pour l’automatisation de l’intégration Unity iOS. Cette solution modifie le projet Xcode conçu à l’aide du [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html) et des sous-classes `UnityAppController` de Unity avec la macro `IMPL_APP_CONTROLLER_SUBCLASS`.

1. Dans Unity Editor, ouvrez les paramètres de configuration de Braze en sélectionnant **Braze > Configuration Braze**.
2. Cochez la case **Automatiser l'intégration d'Unity iOS**.
3. Dans le champ **Clé API Braze**, saisissez la clé API de votre application qui se trouve dans **Gérer les paramètres.**

![]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

Si votre application utilise déjà une autre sous-classe `UnityAppController`, vous devrez fusionner votre implémentation de sous-classe avec `AppboyAppDelegate.mm`.

## Intégration SDK de base terminée

Braze devrait maintenant collecter des données depuis votre application et votre intégration de base devrait être terminée. Pour plus d'informations sur l'intégration des notifications push, consultez les articles suivants : [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/) et [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/), les [messages in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/) et les [cartes de contenu]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/).

Pour en savoir plus sur les options d'intégration SDK avancées, consultez la rubrique [Implémentation avancée]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/sdk_integration/advanced_use_cases/#ios-sdk-advanced).

