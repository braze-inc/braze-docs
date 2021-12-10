---
nav_title: iOS
article_title: Intégration de SDK iOS pour l'unité
platform:
  - Unité
  - iOS
page_order: 0
description: "Cet article de référence couvre l'intégration du SDK iOS pour la plate-forme Unity."
---

# Intégration de SDK iOS

Suivez les instructions ci-dessous pour faire fonctionner Braze dans votre application Unity. Si vous effectuez une transition depuis une intégration manuelle, veuillez lire les instructions sur [Transitioning From a Manual to an Automated Integration][5].

## Étape 1 : Choisissez votre paquet Braze Unity

Braze [`.unitypackage`][41] regroupe des liaisons natives pour les plates-formes Android et iOS, ainsi qu'une interface C# .

Il y a plusieurs paquets Braze Unity disponibles pour le téléchargement sur la [Page des versions de Braze Unity][42]:

* `Pack Appboy.unity`
    - Ce paquet contient les SDK Braze Android et iOS ainsi que la dépendance [SDWebImage][unity-1] pour le SDK iOS, qui est nécessaire pour la bonne fonctionnalité de la messagerie In-App de Braze, et des cartes de contenu sur iOS. Le framework [SDWebImage][unity-1] est utilisé pour télécharger et afficher des images, y compris des GIFs. Si vous avez l'intention d'utiliser toutes les fonctionnalités de Braze, téléchargez et importez ce paquet.<br>
* `Appboy-nodeps.unitypackage`
    - Ce paquet est similaire à `Appboy.unitypackage` sauf que le framework [SDWebImage][unity-1] n'est pas présent. Ce package est utile si vous ne voulez pas du framework [SDWebImage][unity-1] présent dans votre application iOS. <br><br>

> iOS: Pour voir si vous avez besoin de la dépendance [SDWebImage][unity-1] pour votre projet iOS, veuillez visiter la \[Documentation de Message In-App iOS\]\[unity-4\].<br><br>Android : Depuis Unity 2.6.0, l'artefact fourni par Braze Android SDK nécessite des dépendances  [AndroidX][unity-3] d'AndroidX. Si vous utilisiez précédemment un `paquet d'unité jetifié`, vous pouvez alors passer en toute sécurité au `paquet d'unité correspondant` ci-dessus.

## Étape 2 : Importer le paquet

1. Dans l'éditeur Unity, importez le paquet dans votre projet Unity en naviguant vers `Assets > Importer Paquet > Paquet personnalisé`.
2. Cliquez sur __Importer__.

Sinon, suivez les instructions de l'unité pour [Importation de paquets d'actifs][41] pour un guide plus détaillé sur l'importation de paquets Unity personnalisés.

{% alert note %}
Si vous souhaitez seulement importer le plugin iOS/Android, désélectionnez le sous-répertoire `Plugins/Android`/`Plugins/iOS` lors de l'importation de Braze `. nitypackage`.
{% endalert %}

## Étape 3b: Définissez votre clé API

Braze fournit une solution native Unity pour automatiser l'intégration d'Unity iOS. Cette solution modifie le projet Xcode construit en utilisant Unity [`PostProcessBuildAttribute`](http://docs.unity3d.com/ScriptReference/Callbacks.PostProcessBuildAttribute.html)) et sous-classe l'UnityAppController en utilisant la macro `IMPL_APP_CONTROLLER_SUBCLASS`.

1. Dans l'éditeur d'unité, ouvrez les paramètres de configuration de Braze en naviguant sur Braze > Braze Configuration.
2. Cochez la case "Automate Unity iOS Integration".
3. Dans le champ "Braze API Key", entrez la clé API de votre application à partir de la page [Paramètres](https://dashboard-01.braze.com/app_settings/app_settings) dans le tableau de bord de Braze. Vos paramètres de configuration de Braze devraient ressembler à ceci :

![Éditeur de configuration Braze]({% image_buster /assets/img_archive/unity-ios-appboyconfig.png %})

> Si votre application utilise déjà une autre sous-classe `UnityAppController` , vous devrez fusionner l'implémentation de votre sous-classe avec `AppboyAppDelegate.mm`.

## Intégration de base du SDK terminée

Braze devrait maintenant collecter des données de votre application et votre intégration de base devrait être complète.

- __Push__: Voir la documentation push [Android][53] ou [iOS][50] pour des informations sur l'intégration de push.
- __Messages In-App__: Voir la documentation [Message In-App][34] pour des informations sur l'intégration des messages dans l'application.
- __Cartes de Contenu__: Voir la documentation [Cartes de Contenu][40] pour des informations sur l'intégration des Cartes de Contenu.
- __Flux d'actualités__: Voir la [documentation du flux d'actualité][35] pour des informations sur l'intégration du flux d'actualités.

## Extension du SDK (iOS)

Pour étendre les comportements du SDK, fork notre projet [Braze Unity SDK Github](https://github.com/appboy/appboy-unity-sdk) et apporter les changements nécessaires.

Pour publier votre code modifié en tant que package Unity, voir [Cas d'Utilisation Avancés]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Advanced_Use_Cases/advanced_use_cases).

## Passage de l'intégration manuelle à l'intégration automatique (iOS)

Pour tirer parti de l'intégration automatique d'iOS offerte dans le SDK Braze Unity, suivre ces étapes pour passer d'un manuel à une intégration automatisée.

1. Supprimez tout le code brésilien de la sous-classe `UnityAppController` de votre projet Xcode.
2. Retirez les bibliothèques iOS de Braze de votre projet Unity ou Xcode (i.e., `Appboy_iOS_SDK.framework` et `SDWebImage. ramework`) et [importez le paquet Braze Unity](#step-1-importing-the-braze-unity-package) dans votre projet Unity.
3. Suivez les instructions d'intégration sur [la configuration de votre clé API via Unity](#step-2-setting-your-api-key).
[unity-4]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/

[5]: #transitioning-from-manual-to-automated-integration
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/in-app_messaging/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/news_feed/
[40]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/content_cards/
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[41]: https://docs.unity3d.com/Manual/AssetPackages.html
[42]: https://github.com/Appboy/appboy-unity-sdk/releases
[50]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/ios/
[53]: {{site.baseurl}}/developer_guide/platform_integration_guides/unity/push_notifications/android/
[unity-1]: https://github.com/SDWebImage/SDWebImage
[unity-3]: https://developer.android.com/jetpack/androidx