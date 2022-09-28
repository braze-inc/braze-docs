---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Cet article présente le partenariat entre Braze et Iterate, ce qui vous permet d’enrichir les données client en utilisant des enquêtes pour ajouter des informations supplémentaires."
page_type: partner
search_tag: Partenaire

---

# Iterate

> [Iterate](https://iteratehq.com) facilite la connaissance de vos clients, offrant des outils de recherche intelligents et conviviaux qui ressemblent à votre marque et qui la reflètent.

L’intégration de Braze et Iterate vous permet d’inclure des liens d’enquête Iterate dans vos messages e-mail, notifications push ou in-app. Ces liens, une fois reçus, peuvent automatiquement enregistrer et attribuer les réponses à l’enquête Iterate en tant qu’attributs utilisateur personnalisés Braze, ce qui vous permet de créer de nouvelles audiences et de nouveaux segments puissants à utiliser dans vos campagnes. 

## Conditions préalables

| Configuration requise | Origine |
|---|---|
|Compte Iterate | Un [compte Iterate](https://iteratehq.com) est nécessaire pour tirer parti de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br>
<br>
 Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de [l’URL Braze pour votre instance][6]. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Cas d’utilisation

Avec Iterate, vous pouvez collecter presque n’importe quel type de données : des informations personnelles, des données de performances, des préférences ou des préférences utilisateur. C’est vous qui décidez la nature des requêtes et le type de public que vous souhaitez générer.

## Intégration

### Étape 1 : Connecter Braze à Iterate

Connectez-vous à votre compte Iterate et ajoutez votre endpoint REST de Braze et votre clé d’API REST à la page des paramètres de votre entreprise.

### Étape 2 : Créer votre enquête

Créez un lien d’enquête à envoyer. Une fois que les questions ont été écrites et que vous avez personnalisé la conception, sélectionnez **Send survey (Envoyer une enquête) > Integrations (Intégrations) > Braze**.

Vous afficherez ensuite les options de configuration pour l’envoi des réponses à Braze.
Activez l’intégration pour commencer à envoyer les réponses pour cette enquête vers Braze. 

Copiez le lien d’enquête fourni. Vous devrez inclure ce lien dans votre campagne Braze. Notez que la valeur Liquid incluse dans le lien {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} sera automatiquement remplacée pour chaque utilisateur lors de l’envoi.

### Étape 3 : Partager votre enquête

Votre enquête peut être partagée de deux manières : en intégrant la première question dans votre message ou en y incluant un lien direct vers l’enquête sur la plateforme Iterate.

![Options de liaison Iterate][2]

- **Incorporer le code**
  - Copiez l’extrait de code dans **Email embed code** (Code d’intro e-mail) dans la section d’intégration à Braze de l’onglet **Send survey** (Envoyer une enquête). Insérez le code dans le HTML de votre e-mail Braze où vous souhaitez que le début de l’enquête apparaisse. 
  - Si vous avez des difficultés à rendre les questions de l’enquête ou si elles ont l’air mal formatées, vous devrez aller dans l’onglet **Sending Info** (Envoi d’infos) dans le compositeur de messages et décocher **Inline CSS** (CSS inséré).
- **Inclure un lien**
  - Copiez le lien sous **Survey Link** (Lien vers l’enquête) dans la section d’intégration à Braze de l’onglet **Send survey** (Envoyer une enquête). 

## Étape 4 : Utilisateurs cibles

Lorsque les utilisateurs répondent, les données sont enregistrées sur leurs profils en temps réel. Ces données peuvent être utilisées pour segmenter les utilisateurs et envoyer des campagnes de suivi personnalisées. Par exemple, si vous avez envoyé une question « Aimez-vous nos produits ? », vous pourriez créer des segments d’utilisateurs qui ont l’attribut utilisateur personnalisé `Do you enjoy our products?`, qui ont répondu « Oui » ou « Non » et cibler ces utilisateurs.

## Personnaliser les noms d’attributs utilisateur

Par défaut, l’attribut utilisateur créé pour une question est le même que l’invite. 
Dans certains cas, vous pouvez le personnaliser. Pour cela, cliquez sur le menu déroulant **Customize user attribute names** (Personnaliser les noms d’attribut utilisateur) dans l’étape **Create your Survey** (Créer votre enquête) et entrez vos noms préférés.

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[2]: {% image_buster /assets/img/iterate.png %}
