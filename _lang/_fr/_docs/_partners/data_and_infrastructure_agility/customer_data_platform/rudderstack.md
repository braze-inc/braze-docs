---
nav_title: RudderStack
article_title: RudderStack
page_order: 3
description: "Cet article décrit le partenariat entre Braze et RudderStack, une infrastructure de données client open-source qui offre une intégration transparente de Braze pour vos applications Android, iOS et web. Avec RudderStack, vous pouvez maintenant envoyer vos données d'événement client directement à Braze pour une analyse contextuelle."
alias: /partners/rudderstack/
page_type: partenaire
search_tag: Partenaire
---

# RudderStack

> [RudderStack][1] est une infrastructure de données client open-source pour collecter et acheminer les données des événements clients vers votre entrepôt de données préféré et des dizaines d'autres fournisseurs d'analyse, comme le Brésil. Il est prêt pour l'entreprise et offre un cadre de transformation robuste pour traiter vos données d'événement à la volée.

L'intégration de Braze et RudderStack offre une intégration SDK native pour votre Android, iOS, et les applications web, ainsi qu'une intégration de serveur à serveur à partir de vos services d'arrière-plan.

## Pré-requis

| Exigences                     | Libellé                                                                                                                                                                                                                                                               |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte RudderStack            | Un compte [RudderStack](https://app.rudderstack.com/) est requis pour profiter de ce partenariat.                                                                                                                                                                     |
| Source configurée             | Une [source][3] est essentiellement l'origine de toutes les données envoyées à RudderStack, telles que les sites Web, les applications mobiles ou les serveurs backend. Vous devez configurer la source avant de configurer Braze comme destination dans RudderStack. |
| Braze clé API REST            | Une clé API Braze REST avec `users.track`, `users.identify`, et `users.alias.new` permissions.<br><br>Ceci peut être créé dans le **tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API**                        |
| Touche de l'application Braze | Pour obtenir votre clé d'application, accédez au tableau de bord **Braze -> Console développeur -> Identification** et trouvez le nom de votre application. Enregistrer la chaîne d'identification associée.                                                          |
| Centre de données             | Votre centre de données s'aligne sur votre tableau de bord Braze [instance][15].                                                                                                                                                                                      |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

### Étape 1 : Ajouter une source

Pour commencer à envoyer des données à Braze, vous devez d'abord vous assurer qu'une source est configurée dans votre application RudderStack. Visitez [RudderStack](https://rudderstack.com/docs/connections/adding-source-and-destination-rudderstack/) pour apprendre comment configurer votre source de données.

### Étape 2 : Configurer la destination

Maintenant que votre source de données est configurée, dans le tableau de bord de RudderStack, sélectionnez **AJOUTER UNE DESTINATION** sous **Destinations**. Dans la liste des destinations disponibles, sélectionnez **Braze**et cliquez sur **Suivant**.

Dans la destination de Braze, fournissez la clé d'application, la clé API Braze REST, la grappe de données et l'option SDK native (mode appareil uniquement). L'option native SDK utilisera le SDK natif de Braze pour envoyer des événements si activé.

!\[Paramètres Braze\]\[0\]{: style="max-width:40%;margin-bottom:15px;"}

## Étape 3 : Choisissez le type d'intégration

Vous pouvez choisir d'intégrer les bibliothèques web et natives de RudderStack avec Braze en utilisant soit une intégration côte à côte (mode périphérique) soit une intégration de serveur à serveur (mode cloud).

- Type d'intégration
  - [Côte-à-côte / Mode Appareil](#device-mode): RudderStack enverra les données de l'événement à Braze directement à partir de votre client (navigateur ou application mobile).
  - [Serveur à Serveur / Mode Cloud](#cloud-mode): Le Braze SDK envoie les données d'événement directement à RudderStack, qui est ensuite transformée et routée vers Braze.

{% alert note %}
En savoir plus sur les [modes de connexion de RudderStack](https://rudderstack.com/docs/connections/rudderstack-connection-modes/) et les avantages de chacun.
{% endalert %}

### Étape 3 : Intégration côte à côte (mode appareil) {#device-mode}

Avec ce mode, vous pouvez envoyer vos événements à Braze en utilisant la configuration de Braze SDK sur votre site web ou l'application mobile.

Configurer les mappings au SDK RudderStack pour [Android](https://github.com/rudderlabs/rudder-integration-braze-android), [iOS](https://github.com/rudderlabs/rudder-integration-braze-ios), ou [React Native] sur le dépôt GitHub de Braze, comme décrit à l'étape 4.

Pour compléter l'intégration du mode appareil, veuillez vous référer aux instructions détaillées de RudderStack pour [ajouter Braze à votre projet](https://rudderstack.com/docs/destinations/marketing/braze/#adding-device-mode-integration).

### Étape 3b : Intégration du serveur à serveur (mode cloud) {#cloud-mode}

Avec ce mode, le Braze SDK envoie les données de l'événement directement à RudderStack. RudderStack transforme ensuite ces données et les achemine vers Braze dans le format attendu. La transformation se fait dans le backend de RudderStack.

Pour activer l'intégration, vous devrez associer les méthodes RudderStack à Braze, comme décrit à l'étape 4.

{% alert note %}
Les SDK côté serveur de RudderStack (Java, Python, Node.js, Go, Ruby) ne prennent en charge que le mode Cloud. Ceci est dû au fait que leurs SDK côté serveur fonctionnent dans le backend de RudderStack et ne peuvent charger aucun SDK spécifique à Brésil.
{% endalert %}

{% alert important %} L'intégration du serveur à serveur ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze, telles que les notifications push ou les messages dans l'application. Ces fonctionnalités sont toutefois prises en charge par l'intégration du Mode Périphérique.
{% endalert %}

## Étape 4: Méthodes SDK

Braze prend en charge les méthodes RudderStack pour identifier, suivre, page et groupe.

### Identifier

La RudderStack [`identifie la méthode`](https://rudderstack.com/docs/destinations/marketing/braze/#identify) associe un utilisateur à ses actions. RudderStack capture un identifiant utilisateur unique et des traits optionnels associés à cet utilisateur, tels que le nom, le courriel, l'adresse IP, etc.

### Piste

La méthode [`de RudderStack` trace </code>](https://rudderstack.com/docs/destinations/marketing/braze/#track) capture toutes les activités de l'utilisateur, ainsi que les propriétés associées à ces activités.

**Commande complétée**<br> Sur l'utilisation de l'API eCommerce [RudderStack][20] pour appeler la méthode de suivi pour un événement portant le nom `Commande terminée`, RudderStack envoie les produits énumérés dans ce cas à Braze en [`achetant`][21].

### Page

La méthode [`de RudderStack`](https://rudderstack.com/docs/destinations/marketing/braze/#page) vous permet d'enregistrer les pages vues de votre site Web. Il capture également toute autre information pertinente à propos de cette page.

### Groupes

La méthode [`du groupe` de RudderStack](https://rudderstack.com/docs/destinations/marketing/braze/#group) vous permet d'associer un utilisateur à un groupe.
[0]: {% image_buster /assets/img/RudderStack/braze_settings.png %}

[1]: https://rudderstack.com/
[3]: https://docs.rudderstack.com/how-to-guides/adding-source-and-destination-rudderstack
[15]: {{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/
[20]: https://docs.rudderstack.com/rudderstack-api-spec/rudderstack-ecommerce-events-specification
[21]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data