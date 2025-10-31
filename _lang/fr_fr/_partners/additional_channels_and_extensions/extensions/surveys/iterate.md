---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Cet article de référence présente le partenariat entre Braze et Iterate, qui vous permet d'enrichir les données des clients en utilisant des enquêtes pour ajouter des informations supplémentaires."
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com) facilite l'apprentissage auprès de vos clients, en proposant des outils de recherche intelligents et conviviaux, à l'image de votre marque.

_Cette intégration est maintenue par Iterate._

## À propos de l'intégration

L'intégration d'Iterate avec Braze vous permet de proposer des enquêtes Iterate de façon fluide au sein de votre produit ou de vos campagnes. Les réponses à l'enquête peuvent être enregistrées en tant qu'attributs personnalisés de l'utilisateur dans Braze, ce qui vous permet de créer une image complète de vos utilisateurs ou de créer de nouvelles audiences et de nouveaux segments puissants.

Avec le SDK de Braze installé dans votre application ou votre site web, vous pouvez utiliser les outils de segmentation et de ciblage disponibles dans Braze pour envoyer des enquêtes via des messages in-app à une partie spécifique de votre audience en fonction de n'importe quel déclencheur ou segment personnalisé. Les enquêtes Iterate peuvent également être intégrées directement dans vos campagnes d'e-mail ou incluses en tant que liens dans vos campagnes push ou autres.

## Conditions préalables

| Exigence | Origine |
|---|---|
|Compte Iterate | Un [compte Iterate](https://iteratehq.com) est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST de Braze avec des autorisations `users.track`. Pour envoyer des enquêtes via les messages in-app de Braze, vous devez également disposer de l'autorisation `kpi.mau.data_series`.<br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**.|
| Endpoint REST Braze  | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cas d'utilisation

Avec Iterate, vous pouvez collecter presque tous les types de données. Cela va des informations personnelles (nom, âge, e-mail) aux données de performance (Net Promoter, satisfaction des clients, classement par étoiles), en passant par les préférences (appareil préféré, fréquence de communication préférée) ou la personnalité (livre préféré, chien ou chat). Ce que vous requêtez dépend entièrement de vous, et du type de données que vous souhaitez collecter ou des audiences que vous souhaitez créer.

## Intégration

### Pour commencer : Connecter Braze à Iterate

Connectez-vous à votre compte Iterate et ajoutez votre endpoint REST Braze et votre clé API REST sur la page **Paramètres de l'entreprise**.

### Envoyez des enquêtes sous forme de message in-app.

#### Étape 1 : Créez votre enquête

Avant de créer votre sondage, activez la case à cocher **Activer les sondages par message in-app** dans vos paramètres Iterate.

Ensuite, créez une nouvelle enquête dans Iterate et ajoutez des questions pertinentes. Le cas échéant, vous pouvez également inclure un message d'envoi qui s'affichera avant l'enquête. Sélectionnez **Envoyer via un message in-app de Braze** comme type de sondage.

Une fois votre enquête terminée, dans l'onglet **Publier**, copiez l'extrait de code sous **Copier et collez votre code d'intégration**.

#### Étape 2 : Partagez votre enquête

Dans Braze, créez une nouvelle campagne de messages in-app, sélectionnez **Code personnalisé** comme type d'envoi, et collez votre extrait de code dans le message. Ensuite, sélectionnez **Attendre que l'utilisateur se retire** comme comportement du message au clic.

Continuez à configurer votre campagne comme vous le feriez pour n'importe quelle autre campagne de messages in-app, en choisissant une méthode de distribution et en ciblant une audience.

### Délivrer des enquêtes par e-mail ou push

#### Étape 1 : Créez votre enquête

Créez une nouvelle enquête par e-mail ou par lien dans Iterate et ajoutez des questions d'enquête pertinentes. Une fois que les questions ont été rédigées et que vous avez personnalisé la conception, sélectionnez **Envoyer l'enquête > Intégrations > Braze.**

Vous verrez alors les options de configuration pour envoyer des réponses à Braze. Basculez sur l'intégration pour permettre l'envoi des réponses de cette enquête dans Braze. 

#### Étape 2 : Partagez votre enquête

Votre enquête peut être partagée de deux manières : en intégrant la première question dans votre message ou en incluant un lien direct vers l'enquête sur la plateforme Iterate.

![Iterate link options]({% image_buster /assets/img/iterate.png %})

- **Intégrer le code**
  - Copiez l'extrait de code sous **Code d'intégration de l'e-mail** dans la section d'intégration de Braze de l'onglet **Envoyer le sondage**. Insérez le code dans le code HTML de votre e-mail Braze à l'endroit où vous souhaitez que le début de l'enquête apparaisse. 
  - Si vous avez des difficultés à afficher les questions de l'enquête ou si elles ne sont pas correctement formatées, vous devez aller dans l'onglet **Informations d'envoi du** compositeur de messages et décocher l'option **Inline CSS.**
- **Inclure un lien**
  - Copiez le lien sous **Lien de l'enquête** dans la section Intégration de Braze de l'onglet **Envoyer l'enquête.**  Notez que la balise Liquid figurant dans le lien {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} sera automatiquement remplacée pour chaque utilisateur lors de l'envoi.

### Prochaines étapes : Créer des campagnes de suivi

Au fur et à mesure que les utilisateurs répondent, des données en temps réel alimenteront leurs profils. Ces données peuvent être utilisées pour segmenter les utilisateurs et envoyer des campagnes de suivi personnalisées. Par exemple, si vous envoyez la question "Appréciez-vous nos produits ?", vous pouvez créer des segmentations d'utilisateurs ayant l'attribut utilisateur personnalisé `Do you enjoy our products?` qui ont répondu "Oui" ou "Non" et cibler ces utilisateurs.

## Événements personnalisés de Braze

Lorsqu'un utilisateur répond à une question de l'enquête, Iterate déclenche un événement personnalisé dans Braze nommé `survey-question-response`. Les événements personnalisés vous permettent de déclencher le nombre et le type de campagnes de suivi que vous souhaitez.

## Personnaliser les noms des attributs personnalisés

Par défaut, l'attribut utilisateur créé pour une question est le même que l'invite.
Dans certains cas, vous souhaiterez peut-être personnaliser cette procédure. Pour ce faire, cliquez sur le menu déroulant **Personnaliser les noms des attributs des utilisateurs** dans l'étape **Créer votre enquête** et saisissez les noms personnalisés que vous souhaitez.


