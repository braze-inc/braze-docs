---
nav_title: CocoaPods
article_title: Intégration de CocoaPods pour iOS
platform: Swift
page_order: 2
description: "Cet article de référence montre comment intégrer le SDK Braze Swift à l’aide de CocoaPods pour iOS."

---

# Intégration de CocoaPods

## Étape 1 : Installer CocoaPods

L'installation du SDK iOS via [CocoaPods](http://cocoapods.org/) automatise la majeure partie du processus d'installation à votre place. Pour installer CocoaPods, reportez-vous au [guide de démarrage](https://guides.cocoapods.org/using/getting-started.html) de CocoaPods.

Exécutez la commande suivante pour démarrer :

```bash
$ sudo gem install cocoapods
```

Si vous rencontrez des problèmes concernant CocoaPods, reportez-vous au [guide de résolution des problèmes de CocoaPodsCocoaPods CocoaPods](http://guides.cocoapods.org/using/troubleshooting.html "Troubleshooting Guide (Guide de résolution des problèmes de")).

## Étape 2 : Construction du Podfile

Maintenant que vous avez installé le CocoaPods Ruby Gem, vous devez créer un fichier dans votre répertoire de projet Xcode nommé `Podfile`.

{% alert note %}
À partir de la version 7.4.0, le SDK Braze Swift dispose de canaux de distribution supplémentaires sous la forme de [XCFrameworks statiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) et de [XCFrameworks dynamiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Si vous souhaitez utiliser l'un de ces formats à la place, suivez les instructions d'installation de leur dépôt respectif.
{% endalert %}

Ajoutez la ligne suivante à votre Podfile :

```
target 'YourAppTarget' do
  pod 'BrazeKit'
end
```

`BrazeKit` contient la bibliothèque principale du SDK, avec la prise en charge des analyses et des notifications push.

Nous vous suggérons la version Braze afin que les mises à jour du pod récupèrent automatiquement tout ce qui est plus petit qu’une mise à jour mineure de la version. Cela ressemble à `pod 'BrazeKit' ~> Major.Minor.Build`. Si vous souhaitez intégrer automatiquement la dernière version de Braze SDK, même avec des modifications majeures, vous pouvez utiliser `pod 'BrazeKit'` dans votre Podfile.

#### Bibliothèques supplémentaires

Le SDK Swift de Braze sépare les fonctionnalités en bibliothèques autonomes pour offrir aux développeurs un meilleur contrôle sur les fonctionnalités à importer dans leurs projets. En plus de `BrazeKit`, vous pouvez ajouter les bibliothèques suivantes à votre Podfile :

| Bibliothèque | Détails |
| ------- | ------- |
| `pod 'BrazeLocation'` | Bibliothèque de localisations avec prise en charge des analyses de localisation et de la surveillance des géorepérages. |
| `pod 'BrazeUI'` | Bibliothèque d'interface utilisateur fournie par Braze pour les messages in-app et les cartes de contenu. |
{: .ws-td-nw-1}

##### Bibliothèques d'extension

[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) et [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sont des modules d'extension qui fournissent des fonctionnalités supplémentaires et ne doivent pas être ajoutés directement à la cible de votre application principale. Au lieu de cela, vous devrez créer des cibles d'extension distinctes pour chacun de ces modules et importer les modules Braze dans leurs cibles correspondantes.

| Bibliothèque | Détails |
| ------- | ------- |
| `pod 'BrazeNotificationService'` | Bibliothèque d'extension du service de notification prenant en charge les notifications push riches. |
| `pod 'BrazePushStory'` | Bibliothèque d'extension de contenu de notification fournissant un support pour les contenus push. |
{: .ws-td-nw-1}

## Étape 3 : Installer le SDK Braze

Pour installer le SDK Cocoapod Braze, accédez au répertoire de votre projet d’application Xcode au sein de votre terminal et exécutez la commande suivante :
```
pod install
```

À ce stade, vous devriez pouvoir ouvrir le nouvel espace de travail du projet Xcode créé par CocoaPods. Assurez-vous d’utiliser cet espace de travail Xcode au lieu de votre projet Xcode.

![Un dossier d'exemple de Braze agrandi pour montrer le nouveau `BrazeExample.workspace`.]({% image_buster /assets/img/braze_example_workspace.png %})

## Étapes suivantes

Suivez les instructions pour [terminer l'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

## Mettre à jour le SDK Braze par CocoaPods

Pour mettre à jour un Cocoapod, il vous suffit de lancer la commande suivante dans votre répertoire de projet :

```
pod update
```

