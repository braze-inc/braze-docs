---
hidden: true
nav_title: Tests d’unité (facultatif)
article_title: Tests de l’unité de notification Push pour iOS
platform: iOS
page_order: 29.5
description: "Cet article décrit comment implémenter des tests d’unité facultatifs pour votre implémentation de notifications push iOS."
channel:
  - Notification push

---

# Tests unitaires {#unit-tests}

Ce guide facultatif décrit comment mettre en œuvre certains tests d’unité qui vérifieront si votre délégué d’application suit correctement les étapes décrites dans les [instructions d’intégration des notifications push][1] de Braze. 

Si tous les tests sont réussis, généralement, cela signifie que la partie basée sur le code de votre configuration de notification push est fonctionnelle. Si un test échoue, cela peut signifier que vous avez mal suivi une étape, ou cela peut résulter d’une personnalisation valide qui ne correspond pas précisément aux instructions par défaut de Braze.

Dans tous les cas, cette approche peut être utile pour vérifier que vous avez suivi les étapes d’intégration et pour aider à surveiller les éventuelles régressions.

## Étape 1 : Création d’une cible de tests d’unités

Ignorez cette étape si votre projet d’application en Xcode contient déjà un lot de tests d’unité.

Dans votre projet d’application, allez au menu **File > New > Target** (Fichier > Nouveau > Cible) et ajoutez un nouveau « Unit Testing Bundle » (Lot de test d’unité). Ce lot peut utiliser Objective-C ou Swift et peut porter n’importe quel nom. Définissez la « Target to be Tested » (cible à tester) vers la cible de votre application principale.

## Étape 2 : Ajoutez le SDK Braze à vos tests d’unité

En utilisant la même méthode que vous avez utilisée initialement pour [installer le SDK Braze][2], assurez-vous que la même installation du SDK est également disponible pour votre cible de tests d’unité. Par exemple, en utilisant Cocoapods :

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## Étape 3 : Ajoutez OCMock à vos tests d’unité

Ajoutez [OCMock][3] à votre cible de test via Cocoapods, Carthage ou sa bibliothèque statique. Par exemple, en utilisant Cocoapods :

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

Terminez l’installation du SDK Braze et d’OCMock. Par exemple en utilisant Cocoapod, accédez au répertoire de votre projet d’application Xcode au sein de votre terminal et exécutez la commande suivante :

```
pod install
```

À ce stade, vous devriez pouvoir ouvrir l’espace de travail du projet Xcode créé par CocoaPods.

## Étape 5 : Ajouter des tests de notification push

Créez un nouveau fichier Objectif-C dans votre cible de tests d’unité. 

Si la cible des tests d’unité est dans Swift, Xcode peut demander : « Souhaitez-vous configurer un en-tête de pontage Objectif-C ? » L’en-tête de pontage est facultatif, vous pouvez donc cliquer sur **Don't Create (Ne pas créer)** et exécuter ces tests d’unité avec succès.

Ajouter le contenu de l’application d’échantillon HelloSwift [`AppboyPushUnitTests.m`][4] au nouveau fichier.

## Étape 6 : Exécuter la suite de test

Exécutez les tests d’unité de votre application. Il peut s’agir d’une étape de vérification unique, ou vous pouvez l’inclure indéfiniment dans votre suite de tests pour vous aider à détecter toute régression.

[1]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/overview/
[3]: https://ocmock.org/
[4]: https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m