---
nav_title: Messages In-App
article_title: Messages in-app pour tvOS
platform: tvOS
page_type: reference
description: "Cet article de référence couvre les directives d’intégration de messagerie in-app pour la plateforme tvOS."
page_order: 3
---

# Intégration de messages in-app et de cartes de contenu

> Cet article explique comment configurer des messages in-app et des cartes de contenu pour tvOS. Notez que l’assistance pour les messages in-app et les cartes de contenu pour tvOS n’est disponible qu’à l‘aide de notre Swift SDK.

Sur tvOS vous pouvez exécuter un envoi de message sur les canaux de messages in-app et de cartes de contenus en intégrant le [SDK Swift de Braze][swift-sdk]. Après avoir ajouté Braze SDK à votre projet Xcode pour votre application tvOS, notez les informations suivantes au cours de votre configuration :

**1\.** Créer une nouvelle application IOS sous **Manage Settings** dans le tableau de bord de Braze de votre application tvOS.<br>![][1]{: style="width:70%"}<br>
{% alert warning %}
Ne choisissez pas tvOS dans la liste des cases à cocher car ceci vous empêchera de bénéficier des Cartes de contenus ou des messages in-app.
{% endalert %}

**2\.** Utilisez la clé API répertoriée dans **Manage Settings** lorsque vous référencez la clé API au cours de votre configuration SDK dans votre projet Xcode.<br>![][2]{: style="width:70%"}

## Personnalisation

Braze ne fournit pas d’interfaces utilisateur par défaut pour les cartes de contenu ou les messages in-app sur tvOS.

Référencez notre [Interface utilisateur personnalisées messages in-app](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization) et les articles [Interface personnalisée des Cartes de contenu](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization) pour ajouter des éléments de personnalisation à ces canaux sur tvOS lors de l’intégration. Nous proposons également des [projets exemples](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples) pour référencer et aider au processus d’intégration. 

[1]: {% image_buster /assets/img/tvos.png %} 
[2]: {% image_buster /assets/img/tvos1.png %} 
[swift-sdk]: https://github.com/braze-inc/braze-swift-sdk
