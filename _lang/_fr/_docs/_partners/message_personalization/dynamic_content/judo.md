---
nav_title: Judo
page_order: 1
description: "Cet article décrit le partenariat entre Braze et Judo, une plate-forme d'interface utilisateur sans code qui vous permet d'ajouter un contexte de localisation et un suivi à vos applications iOS et Android."
alias: /fr/partners/judo/
page_type: partenaire
search_tag: Partenaire
---

# Judo

> [Judo](https://judo.app) est une plate-forme d'interface utilisateur pilotée par le serveur qui permet aux éditeurs de fournir efficacement des expériences utilisateur riches et engageantes sans mises à jour d'applications.

L'intégration de Braze et Judo vous offre des expériences sur mesure dans vos campagnes et vos Canvases. Au lieu d'une simple expérience de page d'accueil tempérée, une campagne Braze peut incorporer du contenu comportant plusieurs écrans, modaux, , des polices personnalisées et des paramètres de prise en charge tels que le mode sombre et l'accessibilité construit sans code et déployé sans mises à jour d'applications. Les données provenant de Braze peuvent également être utilisées pour soutenir le contenu personnalisé dans une expérience de Judo. Les événements utilisateur et les données de l'expérience peuvent donner des commentaires sur Braze pour l'attribution et le ciblage.

## Pré-requis

| Exigences   | Origine | Accès                                                                                                               | Libellé                                                                                      |
| ----------- | ------- | ------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Compte Judo | Judo    | [Judo](https://www.judo.app/)                                                                                       | Vous aurez besoin d'un compte Judo pour héberger des Expériences pour le lancement de Braze. |
| SDK Judo    | Judo    | [Judo iOS SDK](https://github.com/judoapp/judo-ios/) et [Judo Android SDK](https://github.com/judoapp/judo-android) | Vous aurez besoin des SDK Judo intégrés dans vos applications iOS et/ou Android.             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Cas d'utilisation

**Intégration**: Les éditeurs d'applications utilisant Judo construisent et déploient des expériences d'intégration riches et natives. Ces expériences peuvent maintenant être un élément d’un voyage personnalisé d’intégration transversale coordonné par le biais du Brésil. Les expériences peuvent être personnalisées et mises à jour rapidement sans mise à jour des applications pour tester l'efficacité de différents flux dans l'application.

**Conversion**: Les éditeurs d'applis peuvent utiliser les données de Braze pour créer une expérience personnalisée et enrichissante dans l'application pour faciliter les achats dans l'application, des abonnements payants, ou du merchandising contextuel en utilisant des crochets d'intégration dans le Judo. L'accès à ces expériences peut être déclenché par des campagnes de marketing d'engagement créées au Brésil.

**Contenu axé sur l'événement**: Une utilisation principale du Judo dans le sport et le divertissement consiste à construire de riches expériences pour prévisualiser, promouvoir et récapituler des événements. Cette capacité a de vastes applications dans d'autres verticales pour des contenus saisonniers et à base de nouvelles. Lier la messagerie pour promouvoir ou mettre en valeur les événements de manière opportune à des expériences riches dans l'application permet aux éditeurs de stimuler l'engagement en étant contextuellement pertinents.

## Intégration de SDK côte à côte

Judo propose des bibliothèques supplémentaires qui automatisent certains des efforts nécessaires pour intégrer les SDK Judo et Braze côte à côte dans vos applications mobiles.

### Étape 1 : Installez la bibliothèque d'intégration de Judo-Braze

Installez et configurez la bibliothèque d'intégration Judo-Braze dans vos applications. Cela activera automatiquement le suivi des événements.

- [Instructions d'installation iOS ](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Instructions d'installation d'Android ](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Étape 2 : Configurer la messagerie dans l'application

Cette étape impliquera de créer des implémentations personnalisées `ABKInAppMessageControllerDelegate` et `IInAppMessageManagerListener` pour iOS et Android.

Reportez-vous à la documentation de configuration des messages intégrée pour chacune des bibliothèques d'intégration :

- [Configuration de la messagerie iOS In-App ](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Messagerie In-App Android Configuration](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Utiliser cette intégration

Une fois que vous avez terminé l'intégration de l'application, vous pouvez le tester en lançant une campagne de message de test Braze dans l'application pour une expérience Judo pour vérifier qu'elle fonctionne comme prévu.

### Étape 1 : Créer une campagne de message dans l'application de code personnalisé

À partir de la plateforme Braze, créez une campagne de message Braze dans l'application avec un type de message __Code personnalisé__. Ensuite, sélectionnez __HTML Upload__ comme type personnalisé. Assurez-vous de remplir le contenu du message avec les champs de messagerie de base dans l'application; ce contenu ne sera pas affiché à l'utilisateur.

!\[Campagne de Code personnalisé Braze\]\[2\]

Ensuite, utilisez le snippet HTML minimal suivant pour satisfaire la validation du formulaire :
```
<a href="appboy://close">X</a>
```

Notez que cela ne sera pas affiché en production sur votre appareil car Judo réécrira et remplacera cela par une Expérience Judo.

!\[Braze HTML Snippet\]\[3\]

### Étape 2 : Définissez une paire clé-valeur pour Judo
!\[Braze Campaign Extras Configuration\]\[4\]{: style="float:right;max-width:50%;margin-left:15px;"}

Définissez une paire [de valeur clé personnalisée]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) sur la campagne avec une clé de `judo-experience`. Fournissez l'URL de l'expérience de Judo que vous souhaitez afficher ici. La bibliothèque d'intégration de Judo-Braze détectera ensuite cette paire de valeurs clés dans le gestionnaire et l'utiliser pour injecter votre Judo Experience à la place de l'interface de messagerie standard Braze dans l'application. <br><br>
### Étape 3 : Finalisation de la campagne

Enfin, terminer la campagne, mettre en place un déclencheur pour la campagne et sélectionner des utilisateurs via des segments dans les sections __Delivery__ et __Target User__. Visitez notre message dans l'application [article]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) sur les différents composants d'un message Braze dans l'application.
[2]: {% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %} [3]: {% image_buster /assets/img/judo/braze-html-boilerplate.png %} [4]: {% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}