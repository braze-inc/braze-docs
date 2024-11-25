---
nav_title: Exemples d’applications
article_title: Exemples d’applications pour iOS
platform: Swift
page_order: 9
search_rank: 2
description: "Cet article décrit des exemples d'applications du SDK Swift pour iOS."

---

# Exemples d’applications

> Les SDK de Braze sont tous accompagnés d'exemples d'applications dans le référentiel pour vous faciliter la tâche. Chacune de ces applications est entièrement modulable afin que vous puissiez tester les fonctionnalités de Braze et les implémenter dans vos propres applications. 

Tester le comportement dans votre propre application par rapport au comportement attendu et aux chemins de code des exemples d’applications est un excellent moyen de déboguer les problèmes que vous pourriez rencontrer.

## Exemples de navigation

Plusieurs applications de test sont disponibles dans le dossier `Examples` du [référentiel GitHub du SDK Swift](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples). Le fichier README décrit toutes les différentes permutations des exemples d’intégrations, telles que :

1. Types d'intégration (gestionnaire de paquets swift, CocoaPods, manuel)
2. Langages de codage (Swift et Objective-C)
3. Plateformes (iOS, tvOS, Mac Catalyst, etc.)
4. Fonctionnalités (messages in-app, cartes de contenu, emplacement/localisation, push riche, contenus push, etc.)
5. Types de personnalisation (interface utilisateur par défaut, interface utilisateur entièrement personnalisée)

## Applications de test de conception

Suivez ces instructions pour concevoir et exécuter nos applications de test.

1. Créez un nouvel [espace de travail]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) et notez la clé API de l'identifiant de l'app et son endpoint.
2. En fonction de votre méthode d'intégration (gestionnaire de paquets swift, CocoaPods, manuel), sélectionnez le fichier `xcodeproj` approprié à ouvrir.
3. Placez votre clé API et votre endpoint dans le champ approprié du fichier `Credentials`.

