---
nav_title: Dixa
article_title: Dixa
description: "Cet article présente le partenariat entre Braze et Dixa."
alias: /partners/dixa/
page_type: partner
search_tag: Partner

---

# Dixa

> [Dixa](https://www.dixa.com/) est une plateforme de service client conçue pour améliorer les expériences d'assistance en unifiant les canaux de communication tels que le chat, l'e-mail, le téléphone et les réseaux sociaux en une seule interface. Elle aide les entreprises à améliorer la satisfaction des clients et l'efficacité grâce au routage intelligent, à l'automatisation et aux informations sur les performances en temps réel.

L'intégration de Braze et Dixa offre une meilleure visibilité sur l'ensemble de vos utilisateurs en fournissant aux agents du service client des données Braze en temps réel.

## Conditions préalables

Avant de commencer, vous aurez besoin des éléments suivants :

| Prérequis          | Description                                                                                                                                                       |
|-----------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Un compte Dixa        | Un compte administrateur Dixa est nécessaire pour bénéficier de ce partenariat.                                                                                           |
| Une clé API REST Braze  | Une clé API REST Braze avec les autorisations `users.export.ids` et `email.status`.<br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Un endpoint REST Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance.              |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Affichez les données de Braze dans la vue de l'agent du service client tout en communiquant avec vos utilisateurs sur différents canaux de communication, tels que l'e-mail, la messagerie ou le chat. Vous pouvez également utiliser la transformation de données de Braze pour envoyer des données de Dixa vers Braze afin de mettre en pause le marketing pendant la résolution d'un problème utilisateur.

## Intégration

Vous devez être administrateur Dixa pour configurer les intégrations dans Dixa. Pour l'intégration Braze, dans Dixa, accédez à **Settings** > **Integrations** > **Braze**.

![La page de création du widget Braze dans Dixa où vous saisissez le nom du widget, l'URL de l'API et la clé API.]({% image_buster /assets/img/dixa/dixa-create-integration.png %}){: style="width:450px;"}

### Étape 1 : Créer l'intégration dans Dixa

Sur la page **Create Braze widget**, remplissez les champs obligatoires suivants pour créer l'intégration :

- **Widget name :** Il s'agit du nom de l'intégration qui sera utilisé ultérieurement dans la barre latérale de conversation comme titre.
- **API URL :** Il s'agit de l'URL de l'endpoint de l'API REST de Braze pour votre instance.
- **API Key :** Il s'agit de la clé API Braze que vous avez créée dans les conditions préalables.

### Étape 2 : Configurer l'intégration

Configurez ensuite l'intégration Braze et Dixa. Choisissez parmi les options suivantes pour ajuster l'affichage du widget Braze dans la barre latérale de conversation.

#### Afficher le widget dans la barre latérale de conversation

Ce paramètre permet d'afficher ou de masquer l'ensemble de l'intégration dans la barre latérale des conversations dans Dixa. 

Si vous êtes en train de configurer l'intégration, nous vous recommandons de désactiver cette option pendant que vous remplissez les champs obligatoires. Une fois la configuration terminée, vous pouvez la réactiver pour que les agents Dixa puissent utiliser l'intégration.

#### Afficher les détails du client

Choisissez d'afficher ou de masquer les détails de l'utilisateur. Ces détails contiennent des données sur la localisation, l'e-mail, le numéro de téléphone, l'état de l'abonnement à l'e-mail, l'état de l'abonnement aux notifications push et la durée d'appartenance à Braze. 

#### Afficher le bouton permettant de modifier l'état de l'abonnement à l'e-mail

Les boutons sont basés sur l'un des trois états d'abonnement de Braze : `subscribed`, `opted-in` et `unsubscribed`. Si un utilisateur est `subscribed`, l'agent peut choisir `opt-in` ou `unsubscribe`. Lorsqu'un utilisateur est `opted-in` ou `unsubscribed`, l'agent peut uniquement basculer entre les deux.

#### Afficher une liste d'attributs personnalisés

Choisissez d'afficher ou de masquer les attributs personnalisés Braze de l'utilisateur.

#### Afficher une liste d'événements personnalisés

Choisissez d'afficher ou de masquer les événements personnalisés Braze de l'utilisateur.

#### Afficher une liste d'achats

Choisissez d'afficher ou de masquer la liste des produits achetés par l'utilisateur. Vous pouvez y voir combien de fois l'utilisateur a acheté chaque produit. Pour afficher la première et la dernière date d'achat, survolez l'article. 

### Exemple d'intégration

Voici un exemple d'intégration :

![L'intégration Braze et Dixa dans Dixa qui affiche l'état de l'abonnement à l'e-mail d'un utilisateur, ses attributs personnalisés, ses événements personnalisés et ses achats.]({% image_buster /assets/img/dixa/dixa-braze-integration.png %}){: style="width:350px;"}

## Outil de transformation de données

Dixa utilise des webhooks pour envoyer des données à Braze. Vous devez être administrateur Dixa pour configurer les webhooks.

La première étape consiste à créer une transformation de données dans Braze. 

1. Accédez à **Data Settings** > **Data Transformations** > **Create transformation**.
2. Sélectionnez **Start from scratch**, sélectionnez la destination **POST: Track Users**, puis sélectionnez **Create transformation**.
3. Dans l'éditeur de transformation, copiez l'exemple de code de la section **Exemple d'outil de transformation** ci-dessous et insérez-le dans le champ **Transformation code**. Sélectionnez **Save**, copiez l'**URL du webhook**, puis ouvrez Dixa.
4. Dans Dixa, accédez à **Settings** > **Integrations** > **Webhooks** > **+ Outbound webhook**.
5. Sur la page des paramètres du webhook, collez l'URL provenant de Braze et activez les événements que vous souhaitez suivre. **Conversation created** est un bon point de départ pour suivre les conversations des clients. 
6. Sélectionnez **Save** pour terminer la configuration de Dixa.

### Exemple d'outil de transformation

```js
// Transforming the provided payload to match Braze /users/track endpoint specifications.

// Extracting necessary details from the payload
const requester = payload.data.conversation.requester;
const event = payload.data.conversation;

// Defining user attributes based on the provided payload, prioritizing email if available.
const userAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  _update_existing_only: false, // Set to false to create or update user profiles when identified by email
  organization: payload.organization.name, // Including an additional attribute for demonstration
};

// Defining event attributes based on the provided payload.
const eventAttributes = {
  email: requester.email, // Prioritizing email over external_id and user_alias
  name: payload.event_fqn, // The name of the event
  time: event.created_at, // ISO 8601 datetime format
  properties: { // Including additional event properties
    event_version: payload.event_version,
    conversation_status: event.status,
    conversation_channel: event.channel
  },
  _update_existing_only: false // Set to false to create or update user profiles when identified by email
};

// Constructing the final object to match Braze /users/track endpoint schema
const brazecall = {
  attributes: [userAttributes], // Wrapping userAttributes in an array as per specifications
  events: [eventAttributes] // Wrapping eventAttributes in an array as per specifications
};

// Returning the transformed data
return brazecall;
```
