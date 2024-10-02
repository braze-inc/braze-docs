---
nav_title: Exemples d’applications
article_title: Exemples d’applications pour iOS
platform: iOS
page_order: 9
description: "Cet article couvre les exemples d’applications iOS."

---

{% multi_lang_include deprecations/objective-c.md %}

# Exemples d’applications

Les SDK de Braze sont tous livrés avec des exemples d’applications situés dans le référentiel pour plus de commodité. Chacune de ces applications est entièrement modulable afin que vous puissiez tester les fonctionnalités de Braze et les implémenter dans vos propres applications. Tester le comportement dans votre propre application par rapport au comportement attendu et aux chemins de code des exemples d’applications est un excellent moyen de déboguer les problèmes que vous pourriez rencontrer.

## Applications de test de conception
Plusieurs applications de test sont disponibles dans le [répertoire GitHub SDK iOS][1]. Suivez ces instructions pour concevoir et exécuter nos applications de test.

1. Créez un nouveau [groupe d’apps][25] et notez la clé API de l’identifiant d’application..
2. Placez votre clé API dans le champ approprié dans le fichier `AppDelegate.m`.

Les notifications push pour l’application de test iOS nécessitent une configuration supplémentaire. Consultez notre [Intégration des notifications push iOS][7] pour plus de détails.

[1]: https://github.com/appboy/appboy-ios-sdk "Appboy iOS GitHub Repository"
[25]: {{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps
[7]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
