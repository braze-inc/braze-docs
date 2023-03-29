---
nav_title: Judo
article_title: Judo
description: "Cet article de référence présente le partenariat entre Braze et Judo, une plateforme d’IU basée sur serveur sans code qui vous permet d’ajouter un contexte de localisation et un suivi à vos applications iOS et Android."
alias: /partners/judo/
page_type: partner
search_tag: Partenaire

---

# Judo

> [Judo](https://judo.app) est une plateforme d’IU basée sur serveur qui permet aux éditeurs de proposer efficacement des expériences utilisateur in-app riches et engageantes sans mises à jour d’applications.

L’intégration de Braze et de Judo offre des expériences sur mesure dans vos campagnes et vos Canvas. Au lieu d’une expérience de page de destination simple et modélisée, une campagne Braze peut incorporer un contenu comprenant plusieurs écrans, des modales, des vidéos, des polices personnalisées et des paramètres de prise en charge tels que le mode sombre et l’accessibilité construits sans code et déployés sans mise à jour des applications. Les données Braze peuvent également être utilisées pour soutenir le contenu personnalisé dans une expérience Judo. Les événements et les données des utilisateurs de l’expérience peuvent faire l’objet d’un retour dans Braze pour l’attribution et le ciblage.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Judo | Un compte [Judo](https://www.judo.app/) est requis pour profiter de ce partenariat. |
| SDK Judo | Le SDK Judo doit être intégré à vos applications [iOS](https://github.com/judoapp/judo-ios/) et/ou [Android](https://github.com/judoapp/judo-android). |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

**Onboarding** : Les éditeurs d’applications utilisant Judo construisent et déploient des expériences d’onboarding riches et natives. Ces expériences peuvent désormais être un élément dans un parcours d’onboarding cross-canal personnalisé coordonné via Braze. Les expériences peuvent être personnalisées et rapidement mises à jour sans mises à jour d’applications pour tester l’efficacité des différents flux in-app.

**Conversion** : Les éditeurs d’applications peuvent utiliser les données Braze pour créer une expérience in-app riche et personnalisée pour piloter des achats dans l’application, des abonnements payants ou un merchandising contextuel utilisant des points d’intégration dans Judo. L’accès à ces expériences peut être déclenché via des campagnes marketing d’engagement créées dans Braze.

**Contenu axé sur les événements** : L’utilisation principale de Judo dans le domaine du sport et du divertissement crée des expériences riches pour prévisualiser, promouvoir et récapituler les événements. Cette capacité a des applications larges dans d’autres secteurs verticaux pour le contenu saisonnier et les contenus axés sur les actualités. L’incorporation de liens dans la communication pour promouvoir ou souligner les événements en temps opportun pour booster les expériences in-app permet aux éditeurs de stimuler l’engagement en étant contextuellement pertinents.

## Intégration SDK côte à côte

Judo propose des bibliothèques supplémentaires qui automatisent certains des efforts nécessaires pour intégrer les SDK Judo et Braze côte à côte à l’intérieur de vos applications mobiles. 

### Étape 1 : Installer la bibliothèque d’intégration Judo-Braze

Installez et configurez la bibliothèque d’intégration Judo-Braze dans vos applications. Cela permettra d’activer automatiquement le suivi des événements.

- [Instructions
d’installation iOS](https://github.com/judoapp/judo-braze-ios/wiki#installation)
- [Instructions
d’installation d’Android](https://github.com/judoapp/judo-braze-android/wiki#installation).

### Étape 2 : Configurer les messages in-app

Cette étape consiste à créer des mises en œuvre personnalisées de `ABKInAppMessageControllerDelegate` et de `IInAppMessageManagerListener` pour iOS et Android.

Consultez la documentation de configuration des messages in-app fournie pour chacune des bibliothèques d’intégration :

- [Messages in-app iOS
Configuration](https://github.com/judoapp/judo-braze-ios/wiki#in-app-messaging-setup)
- [Messages in-app Android
Configuration](https://github.com/judoapp/judo-braze-android/wiki#in-app-messaging-setup).

## Comment utiliser cette intégration

Une fois l’intégration des messages in-app terminée, vous pouvez tester cette option en exécutant une campagne Braze de messages in-app pour une expérience Judo pour vérifier que tout fonctionne comme prévu.

### Étape 1 : Créer une campagne de messages in-app avec code personnalisé

À partir de la plateforme Braze, créez une campagne Braze de messages in-app avec un type de message **Code personnalisé**. Ensuite, sélectionnez **HTML Upload (Chargement HTML)** comme type personnalisé. Assurez-vous de renseigner le contenu du message avec les champs de messages in-app de base ; ce contenu ne sera pas affiché par l’utilisateur.

![Image du tableau de bord lorsque vous sélectionnez le type de message « Code personnalisé ».][2]

Ensuite, utilisez l’extrait de code HTML minimum suivant pour satisfaire la validation du formulaire : 
```
<a href="appboy://close">X</a>
```

Notez que cela ne sera pas affiché sur votre appareil, car Judo le modifie et le remplace par une expérience Judo.

![Image montrant le code de validation du formulaire ajouté à l’étape de composition de votre campagne.][3]

### Étape 2 : Définir une paire clé-valeur pour Judo
![Cette image montre la paire clé-valeur nécessaire pour cette intégration avec la « clé » étant « judo-experience » et la « valeur » étant votre lien Judo.][4]{: style="float:right;max-width:50%;margin-left:15px;"}

Définissez une [paire clé-valeur personnalisée]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/) pour la campagne avec une clé `judo-experience`. Indiquez l’URL de l’expérience Judo que vous aimeriez afficher ici. La bibliothèque d’intégration de Judo-Braze détectera alors cette paire clé-valeur dans le gestionnaire et l’utilisera pour injecter votre expérience Judo à la place de l’IU du message in-app standard dans Braze.
<br><br>
### Étape 3 : Terminer la campagne

Enfin, terminez la campagne, en configurant un déclencheur pour la campagne et en sélectionnant les utilisateurs via les Segments dans les sections **Delivery (Livraison)** et **Target User (Utilisateur cible)**. Consultez notre [article]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) sur les différents composants d’un message in-app de Braze.


[2]: {% image_buster /assets/img/judo/braze-campaign-select-custom-type.png %}
[3]: {% image_buster /assets/img/judo/braze-html-boilerplate.png %}
[4]: {% image_buster /assets/img/judo/braze-campaign-extras-judo-experience.png %}
