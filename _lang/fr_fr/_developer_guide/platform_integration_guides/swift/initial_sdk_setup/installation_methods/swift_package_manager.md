---
nav_title: Gestionnaire de paquets Swift
article_title: Intégration du Gestionnaire de paquets Swift pour iOS
platform: Swift
page_order: 1
description: "Ce tutoriel traite de l'installation du SDK Swift de Braze à l'aide du Gestionnaire de paquets Swift pour iOS."

---

# Intégration du Gestionnaire de paquets Swift

> L'installation du SDK Swift via le [Gestionnaire de paquets Swift](https://swift.org/package-manager/) (SPM) permet d’automatiser la majeure partie du processus d'installation. Avant de commencer ce processus, vérifiez les [informations relatives à la version](https://github.com/braze-inc/braze-swift-sdk#version-information) pour vous assurer que votre environnement est pris en charge par Braze.

## Ajouter la dépendance à votre projet

### Importer la version SDK

Ouvrez votre projet et naviguez vers les paramètres de votre projet. Sélectionnez l'onglet **Paquets Swift** et cliquez sur le bouton d'ajout <i class="fas fa-plus"></i> sous la liste des paquets.

![]({% image_buster /assets/img/swiftpackages.png %})

{% alert note %}
À partir de la version 7.4.0, le SDK Braze Swift dispose de canaux de distribution supplémentaires sous la forme de [XCFrameworks statiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-static) et de [XCFrameworks dynamiques](https://github.com/braze-inc/braze-swift-sdk-prebuilt-dynamic). Si vous souhaitez utiliser l'un de ces formats à la place, suivez les instructions d'installation de leur dépôt respectif.
{% endalert %}

Saisissez l'URL de notre référentiel de SDK Swift iOS `https://github.com/braze-inc/braze-swift-sdk` dans le champ de texte. Dans la section **Dependency Rule (Règle de dépendance)**, sélectionnez la version du SDK. Enfin, cliquez sur **Ajouter un paquet**.

![]({% image_buster /assets/img/importsdk_example.png %})

### Sélectionner les paquets

Le SDK Swift de Braze sépare les fonctionnalités en bibliothèques autonomes pour offrir aux développeurs un meilleur contrôle sur les fonctionnalités à importer dans leurs projets.

| Offre | Détails |
| ------- | ------- |
| `BrazeKit` | Bibliothèque SDK principale avec prise en charge des analyses et des notifications push. |
| `BrazeLocation` | Bibliothèque de localisations avec prise en charge des analyses de localisation et de la surveillance des géorepérages. |
| `BrazeUI` | Bibliothèque d'interface utilisateur fournie par Braze pour les messages in-app et les cartes de contenu. |
{: .ws-td-nw-1}

#### Bibliothèques d'extension

{% alert warning %}
[BrazeNotificationService](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b2-rich-push-notifications) et [BrazePushStory](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/b3-push-stories) sont des modules d'extension qui fournissent des fonctionnalités supplémentaires et ne doivent pas être ajoutés directement à la cible de votre application principale. Suivez plutôt les guides liés pour les intégrer séparément dans leurs extensions cibles respectives.
{% endalert %}

| Offre | Détails |
| ------- | ------- |
| `BrazeNotificationService` | Bibliothèque d'extension du service de notification prenant en charge les notifications push riches. |
| `BrazePushStory` | Bibliothèque d'extension de contenu de notification fournissant un support pour les contenus push. |
{: .ws-td-nw-1}

 Sélectionnez le paquet qui correspond le mieux à vos besoins et cliquez sur **Ajouter un paquet**. Veillez à sélectionner au moins `BrazeKit`.

![]({% image_buster /assets/img/add_package.png %})

## Étapes suivantes

Suivez les instructions pour [terminer l'intégration]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/completing_integration/).

