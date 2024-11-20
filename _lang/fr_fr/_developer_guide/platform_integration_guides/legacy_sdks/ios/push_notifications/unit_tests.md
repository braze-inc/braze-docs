---
nav_title: Tests d’unité (facultatif)
article_title: Tests de l’unité de notification Push pour iOS
platform: iOS
page_order: 29.5
description: "Cet article de référence décrit comment implémenter des tests d’unité facultatifs pour votre implémentation de notifications push iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Tests unitaires {#unit-tests}

Ce guide facultatif décrit comment mettre en œuvre quelques tests unitaires qui vérifieront si votre app delegate suit correctement les étapes décrites dans nos [instructions d'intégration push.]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/integration/) 

Si tous les tests sont réussis, généralement, cela signifie que la partie basée sur le code de votre configuration de notification push est fonctionnelle. Si un test échoue, cela peut signifier que vous n'avez pas suivi correctement une étape, ou cela peut résulter d'une personnalisation valide qui ne s'aligne pas précisément sur nos instructions par défaut.

Dans tous les cas, cette approche peut être utile pour vérifier que vous avez suivi les étapes d’intégration et pour aider à surveiller les éventuelles régressions.

## Étape 1 : Création d’une cible de tests d’unités

Ignorez cette étape si votre projet d’application en Xcode contient déjà un lot de tests d’unité.

Dans votre projet d’application, sélectionnez **Fichier > Nouveau > Cible** et ajoutez un nouveau « Unit Testing Bundle » (lot de tests d’unité). Ce lot peut utiliser Objective-C ou Swift et peut porter n’importe quel nom. Définissez la « Target to be Tested » (cible à tester) vers la cible de votre application principale.

## Étape 2 : Ajoutez le SDK Braze à vos tests d’unité

En utilisant la même méthode que celle utilisée initialement pour [installer le SDK de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/), assurez-vous que la même installation du SDK est également disponible pour votre cible de tests unitaires. Par exemple, en utilisant CocoaPods :

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## Étape 3 : Ajoutez OCMock à vos tests d’unité

Ajoutez [OCMock](https://ocmock.org/) à votre cible de test via CocoaPods, Carthage ou sa bibliothèque statique. Par exemple, en utilisant CocoaPods :

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## Étape 4 : Terminez la mise en place des bibliothèques ajoutées

Terminez l’installation du SDK Braze et d’OCMock. Par exemple, en utilisant CocoaPods, naviguez dans le répertoire de votre projet d'application Xcode dans votre terminal et exécutez la commande suivante :

```
pod install
```

À ce stade, vous devriez pouvoir ouvrir l’espace de travail du projet Xcode créé par CocoaPods.

## Étape 5 : Ajouter des tests de notification push

Créez un nouveau fichier Objectif-C dans votre cible de tests d’unité. 

Si la cible des tests d’unité est dans Swift, Xcode peut demander : « Souhaitez-vous configurer un en-tête de pontage Objectif-C ? » L'en-tête de transition étant facultatif, vous pouvez cliquer sur **Ne pas créer** et exécuter ces tests unitaires avec succès.

Ajoutez le contenu des [`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m) de l'exemple d’application HelloSwift au nouveau fichier.

## Étape 6 : Exécuter la suite de test

Exécutez les tests d’unité de votre application. Il peut s’agir d’une étape de vérification unique, ou vous pouvez l’inclure indéfiniment dans votre suite de tests pour vous aider à détecter toute régression.

