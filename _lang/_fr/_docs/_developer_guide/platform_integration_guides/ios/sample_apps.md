---
nav_title: Exemple d'applications
article_title: Exemple d'applications pour iOS
platform: iOS
page_order: 9
description: "Cet article couvre les exemples d'applications iOS."
---

# Exemple d'applications

Les SDK de Braze sont tous fournis avec des exemples d'applications dans le référentiel pour votre commodité. Chacune de ces applications est entièrement constructible pour que vous puissiez tester les fonctionnalités de Braze en plus de les implémenter dans vos propres applications. Tester le comportement dans votre propre application par rapport au comportement attendu et aux chemins de code dans les exemples d'applications est un excellent moyen de déboguer tous les problèmes que vous pouvez rencontrer.

## Construction des applications de test
Plusieurs applications de test sont disponibles dans le dépôt [iOS SDK Github][1]. Suivez les instructions ci-dessous pour construire et exécuter nos applications de test.

1. Créez un nouveau ["Groupe d'application"][25] et notez la clé API de production.
2. Placez votre clé API de production dans le champ approprié dans le fichier `AppDelegate.m`.

> Les notifications push pour l'application de test iOS nécessitent une configuration supplémentaire. Voir la [Documentation de Push iOS][7] pour plus de détails.

[1]: https://github.com/appboy/appboy-ios-sdk "Appboy iOS Github Repository"
[25]: {{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/
