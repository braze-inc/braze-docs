---
nav_title: Judo
article_title: Judo
description: "Cet article de référence décrit le partenariat entre Braze et Judo, une plateforme d'interface utilisateur sans code pilotée par serveur qui vous permet d'ajouter un contexte de localisation et un suivi à vos applications iOS et Android."
alias: /partners/judo/
page_type: partner
search_tag: Partner

---

# Judo

> [Judo](https://judo.app) est une plateforme d'interface utilisateur pilotée par un serveur qui permet aux éditeurs de fournir efficacement des expériences utilisateur riches et engageantes dans l'application sans mises à jour de l'application.

_Cette intégration est maintenue par Judo._

## À propos de l'intégration

L'intégration de Braze et Judo offre des expériences sur mesure dans vos campagnes et Canvases. Au lieu d'une simple expérience de page de destination modélisée, une campagne Braze peut incorporer du contenu comprenant plusieurs écrans, modales, vidéos, polices personnalisées et paramètres de support tels que le mode sombre et l'accessibilité construits sans code et déployés sans mises à jour de l'application. Les données de Braze peuvent également être utilisées pour soutenir le contenu personnalisé dans une expérience Judo. Les événements utilisateur et les données de l'expérience peuvent être réinjectés dans Braze pour l'attribution et le ciblage.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte de judo | Un compte [Judo](https://www.judo.app/) est requis pour profiter de ce partenariat. |
| SDK de Judo | Le SDK Judo doit être intégré dans vos applications [iOS](https://github.com/judoapp/judo-ios/) et/ou [Android](https://github.com/judoapp/judo-android). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

**Onboarding** : Les éditeurs d'applications utilisant Judo créent et déploient des expériences d'onboarding riches et natives. Ces expériences peuvent désormais être un élément d'un parcours d'onboarding cross-canal personnalisé coordonné via Braze. Les expériences peuvent être personnalisées et rapidement mises à jour sans aucune mise à jour de l'application pour tester l'efficacité des différents flux dans l'application.

**Conversion** : Les éditeurs d'applications peuvent utiliser les données de Braze pour créer une expérience riche et personnalisée sur l'application afin de stimuler les achats intégrés, les abonnements payants ou le merchandising contextuel en utilisant des hooks d'intégration dans Judo. L'accès à ces expériences peut être déclenché via des campagnes de marketing d'engagement créées dans Braze.

**Contenu piloté par les événements**: Une utilisation principale du judo dans le sport et le divertissement est de créer des expériences riches pour prévisualiser, promouvoir et récapituler des événements. Cette capacité peut être utilisée dans d'autres secteurs pour le contenu saisonnier et axé sur l'actualité. Lier l'envoi de messages pour promouvoir ou mettre en avant des événements en temps opportun à des expériences riches dans l'application permet aux éditeurs de stimuler l'engagement en étant contextuellement pertinents.

## intégration SDK côte à côte

Judo propose des bibliothèques supplémentaires qui automatisent une partie de l'effort nécessaire pour intégrer les SDK Judo et Braze côte à côte dans vos applications mobiles. 

### Étape 1 : Installez la bibliothèque d'intégration Judo-Braze

Installez et configurez la bibliothèque d'intégration Judo-Braze dans vos applications. Cela activera automatiquement le suivi des événements.

- [installation iOS
instructions](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Installation d'Android
instructions](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Étape 2 : Configurer l'envoi de messages dans l'application

Cette étape impliquera la création de déploiements `ABKInAppMessageControllerDelegate` et `IInAppMessageManagerListener` personnalisés pour iOS et Android.

Consultez la documentation de configuration des messages in-app fournie pour chacune des bibliothèques d'intégration :

- [Messagerie intégrée iOS
configuration](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Messagerie in-app Android
Configuration](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Grâce à cette intégration

Une fois que vous avez terminé l'intégration côté application, vous pouvez la tester en lançant une campagne de messages in-app de test Braze pour une expérience Judo afin de vérifier qu'elle fonctionne comme prévu.

### Étape 1 : Créer une campagne de message in-app avec code personnalisé

Depuis la plateforme Braze, créez une campagne de message in-app Braze avec un type de message **Code personnalisé**. Ensuite, sélectionnez **HTML Upload** comme type personnalisé. Assurez-vous de remplir le contenu du message avec les champs de base de l'envoi de messages dans l'application ; ce contenu ne sera pas affiché à l'utilisateur.

![Image du tableau de bord lors de la sélection du type de message "Code personnalisé".]({% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %})

Ensuite, utilisez l'extrait de code HTML suivant pour valider le formulaire : 
```
<a href="appboy://close">X</a>
```

Notez que cela ne sera pas affiché dans l’environnement de production sur votre appareil car Judo réécrira et remplacera cela par une expérience Judo.

![Une image montrant le code de validation du formulaire ajouté à l'étape de composition de votre campagne.]({% image_buster /assets/img/judo/braze-html-boilerplate.png %})

### Étape 2 : Définir une paire clé-valeur pour Judo
![Cette image montre la paire clé-valeur nécessaire à cette intégration, la "clé" étant "judo-experience" et la "valeur" étant votre lien avec le judo.]({% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}){: style="float:right;max-width:50%;margin-left:15px;"}

Définir une [paire clé-valeur personnalisée]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) sur la campagne avec une clé de `judo-experience`. Fournissez l'URL de l'expérience de judo que vous souhaitez montrer ici. La bibliothèque d'intégration Judo-Braze détectera alors cette paire clé-valeur dans le gestionnaire et l'utilisera pour injecter votre expérience Judo à la place de l'interface utilisateur standard du message in-app de Braze.
<br><br>
### Étape 3 : Terminer la campagne

Enfin, terminez la campagne, configurez un déclencheur pour la campagne et sélectionnez les utilisateurs via les segments dans les sections **Distribution** et **Utilisateur cible**. Consultez notre [article]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) sur les messages in-app pour en savoir plus sur les différents composants d'un message in-app Braze.


