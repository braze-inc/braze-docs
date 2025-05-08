---
nav_title: Exemples d’applications
article_title: Exemples d’applications pour iOS
platform: iOS
page_order: 9
description: "Cet article de référence couvre les exemples d’applications iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Exemples d’applications

Les SDK de Braze sont tous accompagnés d'exemples d'applications dans le référentiel pour vous faciliter la tâche. Chacune de ces applications est entièrement modulable afin que vous puissiez tester les fonctionnalités de Braze et les implémenter dans vos propres applications. Tester le comportement dans votre propre application par rapport au comportement attendu et aux chemins de code des exemples d’applications est un excellent moyen de déboguer les problèmes que vous pourriez rencontrer.

## Applications de test de conception
Plusieurs applications de test sont disponibles au sein du [référentiel GitHub du SDK iOS ](https://github.com/appboy/appboy-ios-sdk "(référentiel GitHub iOS Appboy)"). Suivez ces instructions pour concevoir et exécuter nos applications de test.

1. Créez un nouvel [espace de travail]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#creating-your-app-group-in-my-apps) et notez la clé API de l'identifiant de l'app.
2. Placez votre clé API dans le champ approprié dans le fichier `AppDelegate.m`.

Les notifications push pour l’application de test iOS nécessitent une configuration supplémentaire. Reportez-vous à notre [intégration iOS Push]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) pour plus de détails.

