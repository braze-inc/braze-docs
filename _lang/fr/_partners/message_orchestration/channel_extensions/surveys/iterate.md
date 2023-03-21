---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Cet article de référence présente le partenariat entre Braze et Iterate, ce qui vous permet d’enrichir les données client en utilisant des enquêtes pour ajouter des informations supplémentaires."
page_type: partner
search_tag: Partenaire

---

# Iterate

> [Iterate](https://iteratehq.com) facilite la connaissance de vos clients, offrant des outils de recherche intelligents et conviviaux qui ressemblent à votre marque et qui la reflètent.

L'intégration d'Iterate à Braze vous permet de diffuser des enquêtes Iterate nativement et de manière harmonieuse dans votre produit ou vos campagnes. Les réponses aux enquêtes peuvent être enregistrées dans Braze en tant qu'attributs utilisateurs personnalisés, ce qui vous permet de dresser un tableau complet de vos utilisateurs ou de créer de nouvelles audiences et segments puissants.

Une fois le SDK de Braze installé dans votre application ou votre site web, vous pouvez utiliser les outils de segmentation et de ciblage disponibles dans Braze pour diffuser des enquêtes via des messages in-app à une partie spécifique de votre audience en fonction de n'importe quel déclencheur ou segment personnalisé. Les enquêtes d'Iterate peuvent également être intégrées directement dans vos campagnes de courrier électronique ou incluses comme liens dans vos campagnes de notifications push ou autres.

## Conditions préalables

| Condition | Origine |
|---|---|
|Compte Iterate | Un [compte Iterate](https://iteratehq.com) est nécessaire pour tirer parti de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. Pour envoyer des enquêtes via les messages in-app de Braze, vous devez également obtenir l'autorisation `kpi.mau.data_series`.<br><br> Cela peut être créé dans le **Tableau de bord de Braze > Developer Console (Console du développeur) > REST API Key (Clé API REST) > Create New Api Key (Créer une nouvelle clé API)**.|
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance][6]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Cas d’utilisation

Avec Iterate, vous pouvez collecter presque tous les types de données. Il peut s'agir d'informations personnelles (nom, âge, e-mail), de données sur les performances (NPS, satisfaction client, classements par étoiles), de préférences (appareil préféré, fréquence de communication préférée) ou de personnalité (livre préféré, chien ou chat préféré). Ce que vous demandez dépend entièrement de vous, du type de données que vous souhaitez collecter ou des audiences que vous voulez créer.

## Intégration

### Démarrage : Connecter Braze à Iterate

Connectez-vous à votre compte Iterate et ajoutez votre endpoint REST de Braze et votre clé d’API REST à la page **Company Settings (Paramètres de l’entreprise)**.

### Livrer les enquêtes sous forme de message in-app

#### Étape 1 : Créer votre enquête

Avant de créer votre enquête, activez **Enable in-app message surveys (Activer les enquêtes par message in-app)** dans vos paramètres Iterate.

Ensuite, créez une nouvelle enquête dans Iterate et ajoutez des questions pertinentes pour l’enquête. Le cas échéant, vous pouvez également inclure un message d'invite à afficher avant l'enquête. Sélectionnez **Send via Braze In-App Message (Envoyer via message in-app Braze)** comme type d'enquête.

Une fois votre enquête terminée, dans l'onglet **Publish (Publier)**, copiez l'extrait de code sous **Copy and paste your embed code (Copier et coller votre code d'intégration)**.

#### Étape 2 : Partager votre enquête

Dans Braze, créez une nouvelle campagne de communication in-app, sélectionnez **Custom Code (Code personnalisé)** comme type d’envoi de messages et collez votre extrait de code dans le message. Ensuite, sélectionnez **Wait for User to Dismiss (Attendre le rejet par l'utilisateur)** comme comportement lors du clic du message.

Continuez à configurer votre campagne comme vous le feriez pour toute autre campagne de communication in-app, en choisissant une méthode de diffusion et en ciblant une audience.

### Envoyer des enquêtes par courrier électronique ou par notification push

#### Étape 1 : Créer votre enquête

Créez un nouvel e-mail ou lien pour l’enquête dans Iterate et ajoutez des questions pertinentes pour l’enquête. Une fois que les questions ont été écrites et que vous avez personnalisé la conception, sélectionnez **Send survey (Envoyer une enquête) > Integrations (Intégrations) > Braze**.

Vous afficherez ensuite les options de configuration pour l’envoi des réponses à Braze. Activez l’intégration pour activer l’envoi des réponses pour cette enquête vers Braze. 

#### Étape 2 : Partager votre enquête

Votre enquête peut être partagée de deux manières : en intégrant la première question dans votre message ou en y incluant un lien direct vers l’enquête sur la plateforme Iterate.

![Options de liaison Iterate][2]

- **Incorporer le code**
  - Copiez l’extrait de code dans **Email embed code (Code d’intro e-mail)** dans la section d’intégration à Braze de l’onglet **Send survey (Envoyer une enquête)**. Insérez le code dans le HTML de votre e-mail Braze où vous souhaitez que le début de l’enquête apparaisse. 
  - Si vous avez des difficultés à rendre les questions de l’enquête ou si elles ont l’air mal formatées, vous devrez aller dans l’onglet **Sending Info (Envoi d’infos)** dans le compositeur de messages et décocher **Inline CSS (CSS inséré)**.
- **Inclure un lien**
  - Copiez le lien sous **Survey Link (Lien vers l’enquête)** dans la section d’intégration à Braze de l’onglet **Send survey (Envoyer une enquête)**. Notez que la valeur Liquid incluse dans le lien {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} sera automatiquement remplacée pour chaque utilisateur lors de l’envoi.

### Étapes suivantes : Créer des campagnes de suivi

Au fur et à mesure que les utilisateurs répondent, vous verrez des données en temps réel apparaître dans leurs profils. Ces données peuvent être utilisées pour segmenter les utilisateurs et envoyer des campagnes de suivi personnalisées. Par exemple, si vous avez envoyé la question « Aimez-vous nos produits ? », vous pourriez créer des segments d’utilisateurs qui ont l’attribut utilisateur personnalisé `Do you enjoy our products?`, qui ont répondu « Oui » ou « Non » et ciblé ces utilisateurs.

## Événements personnalisés Braze

Lorsqu'un utilisateur répond à une question d'enquête, Iterate déclenche un événement personnalisé dans Braze, nommé `survey-question-response`. Les événements personnalisés vous permettent de déclencher n'importe quels nombre et types de campagnes de suivi.

## Personnaliser les noms d’attributs utilisateur

Par défaut, l’attribut utilisateur créé pour une question est le même que l’invite. 
Dans certains cas, vous pouvez le personnaliser. Pour cela, cliquez sur le menu déroulant **Customize user attribute names (Personnaliser les noms d’attribut utilisateur)** dans l’étape **Create your Survey (Créer votre enquête)** et entrez vos noms préférés.

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[2]: {% image_buster /assets/img/iterate.png %}
