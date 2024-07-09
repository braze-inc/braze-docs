---
nav_title: RudderStack
article_title: RudderStack
description: "Cet article présente le partenariat entre Braze et RudderStack, une infrastructure open source de données client qui offre une intégration transparente de Braze pour vos applications Android, iOS et Web. Avec RudderStack, vous pouvez maintenant envoyer les données d’événements client de votre application directement à Braze pour effectuer des analyses contextuelles."
page_type: partner
search_tag: Partenaire

---

# RudderStack

> [RudderStack][1] est une infrastructure open source de données client conçue pour collecter et transférer les données d’événements client à votre entrepôt de données préféré et à des dizaines d’autres fournisseurs d’analyse, comme Braze. L’infrastructure est adaptée aux entreprises et offre un cadre de transformation robuste pour traiter vos données d’événements à la volée.

L’intégration de Braze et RudderStack inclut une intégration SDK native pour vos applications Android, iOS et Web, ainsi qu’une intégration serveur à serveur de vos services de back-end.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte RudderStack | Un [compte Rudderstack](https://app.rudderstack.com/) est requis pour profiter de ce partenariat. |
| Source configurée | Une [source][3] est essentiellement le point d’origine de toutes les données envoyées à RudderStack, telles que des sites Web, des applications mobiles ou des serveurs de back-end. Vous devez configurer la source avant de configurer Braze en tant que destination dans RudderStack. |
| Clé d’API REST Braze | Une clé API REST Braze avec des autorisations `users.track`, `users.identify` et `users.alias.new`.<br><br>Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Clé de l’application Braze | Pour obtenir la clé de votre application, naviguez jusqu’à **Tableau de bord de Braze > Developer Console > Identification** et cherchez le nom de votre application. Enregistrez la chaîne de caractères d’identification associée.
| Centre de données | Votre centre de données s’aligne sur l’[instance][15] de votre tableau de bord de Braze.  |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Ajouter une source

Pour commencer à envoyer des données à Braze, vous devez d’abord vous assurer qu’une source est configurée dans votre application RudderStack. Rendez-vous sur le site Web de [RudderStack][22] pour découvrir comment configurer votre source de données.

### Étape 2 : Configurer une destination

Maintenant que vous avez configuré votre source de données, dans le tableau de bord de RudderStack, sélectionnez **ADD DESTINATION (AJOUTER UNE DESTINATION)** sous **Destinations**. Dans la liste des destinations disponibles, sélectionnez **Braze** et cliquez sur **Next (Suivant)**.

Dans la destination Braze, fournissez la clé d’application, la clé API REST de Braze, le cluster de données et l’option du SDK natif (en mode appareil uniquement). L’option du SDK natif utilisera le SDK natif de Braze pour envoyer des événements si elle est activée. 

![][0]{: style="max-width:40%;margin-bottom:15px;"}

## Étape 3 : Choisir le type d’intégration

Vous pouvez choisir d’intégrer les bibliothèques Web et natives côté client de RudderStack avec Braze en utilisant une intégration côte à côte (mode appareil) ou une intégration serveur vers serveur (mode cloud).

- Type d’intégration
  - [Mode côte à côte/appareil](#device-mode) : RudderStack enverra les données d’événements à Braze directement à partir de votre client (navigateur ou application mobile).
  - [Mode serveur à serveur/cloud](#cloud-mode) : Le SDK de Braze envoie les données d’événements directement à RudderStack, qui sont ensuite transformées et transférées vers Braze.

{% alert note %} 
En savoir plus sur les différents [modes de connexion](https://www.rudderstack.com/docs/destinations/rudderstack-connection-modes/) de RudderStack et les avantages de chacun d’entre eux.
{% endalert %}

### Étape 3a : Intégration côte à côte (mode Appareil) {#device-mode}

Avec ce mode, vous pouvez envoyer vos événements à Braze en utilisant le kit SDK de Braze qui est installé sur votre site Internet ou votre application mobile.

Configurez les mappages au SDK de RudderStack pour [Android](https://github.com/rudderlabs/rudder-integration-braze-android), [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios) ou [React Native] sur le référentiel GiThub de Braze, comme décrit à l’étape 4. 

Pour terminer l’intégration du mode appareil, reportez-vous aux instructions détaillées de RudderStack pour [ajouter Braze à votre projet](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

### Étape 3b : Intégration serveur à serveur (mode cloud) {#cloud-mode}

Avec ce mode, le SDK Braze envoie directement les données d’événement au serveur RudderStack. RudderStack transforme ensuite ces données et les envoie à la destination souhaitée. Cette transformation se fait dans le backend RudderStack, via le module Transformer de RudderStack.

Pour activer l’intégration, vous devrez mapper les méthodes RudderStack vers Braze, comme décrit à l’étape 4.

{% alert note %} 
Les SDK côté serveur de RudderStack (Java, Python, Node.js, Go et Ruby) prennent uniquement en charge le mode cloud. En effet, les SDK côté serveur fonctionnent dans le back-end de RudderStack et ne peuvent charger aucun SDK spécifique à Braze. 
{% endalert %}

{% alert important %} L’intégration serveur à serveur ne prend pas en charge les fonctionnalités de l’interface utilisateur de Braze, telles que les notifications push ou les messages in-app. Ces fonctionnalités sont cependant prises en charge par l’intégration du mode appareil. 
{% endalert %}

## Étape 4 : Méthodes SDK

Braze prend en charge les méthodes RudderStack suivantes : identification, suivi, page et groupe.

### Identification

La [méthode `identify`](https://rudderstack.com/docs/destinations/marketing/braze/#identify) de RudderStack associe un utilisateur à ses actions. RudderStack collecte un ID utilisateur unique et des caractéristiques optionnelles associées à cet utilisateur, comme le nom, l’adresse e-mail, l’adresse IP, etc.

### Suivi

La [méthode `track`](https://rudderstack.com/docs/destinations/marketing/braze/#track) de RudderStack collecte toutes les activités de l’utilisateur, ainsi que les propriétés associées à ces activités.

**Commande terminée**<br>
En utilisant l’[API eCommerce de RudderStack][20] pour désigner la méthode de suivi d’un événement avec le nom `Order Completed`, RudderStack envoie les produits répertoriés dans cet événement à Braze [`purchases`][21].

### Page

La [méthode `page`](https://rudderstack.com/docs/destinations/marketing/braze/#page) de RudderStack vous permet d’enregistrer les vues des pages de votre site Internet. Elle collecte également toute autre information pertinente sur cette page.

### Groupe

La méthode [`group` de RudderStack](https://rudderstack.com/docs/destinations/marketing/braze/#group) vous permet d’associer un utilisateur à un groupe.

[0]: {% image_buster /assets/img/RudderStack/braze_settings.png %}
[1]: https://rudderstack.com/
[3]: https://docs.rudderstack.com/how-to-guides/adding-source-and-destination-rudderstack
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/
[20]: https://docs.rudderstack.com/rudderstack-api-spec/rudderstack-ecommerce-events-specification
[21]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[22]: https://www.rudderstack.com/docs/destinations/streaming-destinations/braze/#getting-started
