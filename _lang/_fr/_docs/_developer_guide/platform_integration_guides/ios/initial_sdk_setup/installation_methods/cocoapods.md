---
nav_title: Intégration de CocoaPods
article_title: Intégration de CocoaPods pour iOS
platform: iOS
page_order: 2
description: "Cet article de référence montre comment intégrer le Braze SDK en utilisant CocoaPods pour iOS."
---

# Intégration de CocoaPods

## Étape 1 : Installer CocoaPods

Installer le SDK iOS via [CocoaPod][apple_initial_setup_1] automatise la majorité du processus d'installation pour vous. Avant de commencer ce processus, assurez-vous que vous utilisez [Ruby version 2.0.0][apple_initial_setup_2] ou plus. Ne vous inquiétez pas, la connaissance de la syntaxe de Ruby n'est pas nécessaire pour installer ce SDK.

Exécutez simplement la commande suivante pour commencer :

```bash
$ sudo gem install coapods
```

__Note__: Si vous êtes invité à écraser l'exécutable `rake` veuillez vous référer aux [Directions de démarrage sur CocoaPods. rg][apple_initial_setup_3] pour plus de détails.

__Note__: Si vous avez des problèmes concernant les CocoaPods, veuillez vous référer au [Guide de dépannage CocoaPods][apple_initial_setup_25].

## Étape 2 : Construire le podfile

Maintenant que vous avez installé la gemme Ruby de CocoaPods, vous allez avoir besoin de créer un fichier dans le répertoire de votre projet Xcode nommé `Podfile`.

Ajoutez la ligne suivante à votre fichier Podfile:

```
la cible 'YourAppTarget' fait
  pod 'Appboy-iOS-SDK'
fin
```

__Note__: Nous vous suggérons la version Braze afin que les mises à jour de pod saisissent automatiquement tout ce qui est plus petit qu'une mise à jour mineure. Cela ressemble à 'pod 'Appboy-iOS-SDK' ~> Major.Minor.Build'. Si vous voulez intégrer la dernière version de Braze SDK automatiquement même avec des changements majeurs, vous pouvez utiliser `pod 'Appboy-iOS-SDK'` dans votre Podfile.

> Nous recommandons aux intégrateurs d'importer notre SDK complet comme décrit ci-dessus. Cependant, si vous êtes certain que vous allez seulement intégrer une fonctionnalité particulière de Braze, alors vous avez la possibilité d'importer seulement la subspec de l'interface utilisateur désirée au lieu du SDK complet.

| Sous-spécification                  | Détails du produit                                                                                                        |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| `pod 'Appboy-iOS-SDK/InAppMessage'` | La sous-spécification `InAppMessage` contient l'interface de message In-App Braze et le SDK Core.                         |
| `pod 'Appboy-iOS-SDK/ContentCards'` | La sous-spécification `ContentCards` contient l'interface de la carte de contenu Braze et le SDK de base.                 |
| `pod 'Appboy-iOS-SDK/NewsFeed'`     | La sous-spécification `NewsFeed` contient l'interface du flux de Braze News et le SDK de base.                            |
| `pod 'Appboy-iOS-SDK/Core'`         | La sous-spécification `Core` contient le support des analytiques, tels que les événements personnalisés et les attributs. |
{: .ws-td-nw-1}

## Étape 3 : Installation du Braze SDK

Pour installer Braze SDK Cocoapod, accédez au répertoire de votre projet d'application Xcode dans votre terminal et exécutez la commande suivante :
```
Installation du pod
```

À ce stade, vous devriez être en mesure d'ouvrir le nouvel espace de travail du projet Xcode créé par CocoaPods. Assurez-vous d'utiliser cet espace de travail Xcode au lieu de votre projet Xcode.

!\[Nouveau espace de travail\]\[apple_initial_setup_15\]

## Étapes suivantes

Suivez les instructions pour [Compléter l'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/completing_integration/).

## Mise à jour du Braze SDK via CocoaPods

Pour mettre à jour une Cocoapod, exécutez simplement la commande suivante dans le répertoire de votre projet :

```
mise à jour du pod
```
[apple_initial_setup_15]: {% image_buster /assets/img_archive/podsworkspace.png %}

[apple_initial_setup_1]: http://cocoapods.org/
[apple_initial_setup_2]: https://www.ruby-lang.org/en/installation/
[apple_initial_setup_3]: http://guides.cocoapods.org/using/getting-started.html "CocoaPods Installation Directions"
[apple_initial_setup_25]: http://guides.cocoapods.org/using/troubleshooting.html "CocoaPods Troubleshooting Guide"
