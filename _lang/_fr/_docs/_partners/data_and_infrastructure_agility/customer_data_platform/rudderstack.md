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

> [RudderStack](https://rudderstack.com/) est une infrastructure de données client open-source pour la collecte et le routage des données d'événements clients vers votre entrepôt de données préféré et des dizaines d'autres fournisseurs d'analyse, comme le Brésil. Il est prêt pour l'entreprise et offre un cadre de transformation robuste pour traiter vos données d'événement à la volée.

RudderStack offre une intégration native de SDK pour vos applications Android, iOS, web, ainsi qu'une intégration de serveur à serveur pour vos services d'arrière-plan.  De cette façon, vous pouvez envoyer vos données d'événement client dans l'application à Braze directement pour une analyse contextuelle.

## Aperçu de la configuration

Intégrer RudderStack à Braze est très simple et rapide. Tout ce que vous avez à faire est de suivre ces étapes :

1. Veillez à ce que toutes les conditions d’intégration soient respectées et respectées.
2. Choisissez votre type d'intégration préféré et configurez Braze comme destination dans RudderStack.
3. Configurez les mappings requis pour votre intégration.

## Étape 1 : Prérequis

| Exigences                                    | Origine     | Accès                                                                                                                                                                                                                                                                                                                                                                                                                              | Libellé                                                                                                                                                                                                                                                                 |
| -------------------------------------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte RudderStack                           | RudderStack | [https://app.rudderstack.com/](https://app.rudderstack.com/)                                                                                                                                                                                                                                                                                                                                                                       | Un compte RudderStack est nécessaire pour mettre en place l’intégration de RudderStack-Braze.                                                                                                                                                                           |
| Source configurée                            | RudderStack | [Documentation de RudderStack](https://docs.rudderstack.com/how-to-guides/adding-source-and-destination-rudderstack)                                                                                                                                                                                                                                                                                                               | Une source est essentiellement l'origine de toutes les données envoyées à RudderStack, telles que les sites Web, les applications mobiles ou les serveurs d'arrière-plan. Vous devez configurer la source avant de configurer Braze comme destination dans RudderStack. |
| Intégration de Braze SDK avec votre appareil | Brasero     | Pour en savoir plus sur l'utilisation des SDK Braze, reportez-vous à notre documentation sur le [web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/), et [plateformes Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/). | Braze doit être installé sur votre site web ou application pour que l'intégration soit couronnée de succès.                                                                                                                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Étape 2 : Choisissez le type d'intégration

Vous pouvez choisir d'intégrer les bibliothèques web et natives de RudderStack avec Braze en utilisant soit une intégration côte à côte ("Device Mode") soit une intégration de serveur à serveur ("Cloud Mode").

| Type d'intégration             | Libellé                                                                                                                         |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------- |
| Côte-à-côte / Mode Appareil    | RudderStack enverra les données de l'événement à Braze directement à partir de votre client (navigateur ou application mobile). |
| Serveur à Serveur / Mode Nuage | Le Braze SDK envoie les données de l'événement directement à RudderStack, qui est ensuite transformé et acheminé vers Braze.    |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
En savoir plus sur les modes de connexion de RudderStack et les avantages de chaque [ici](https://rudderstack.com/docs/connections/rudderstack-connection-modes/).
{% endalert %}

### Étape 2.1a : Intégration côte à côte (mode périphérique)

Avec ce mode, vous pouvez envoyer vos événements à Braze en utilisant la configuration de Braze SDK sur votre site web ou l'application mobile.

{% tabs %}
  {% tab Android %}
    Configurez les mappings au [SDK RudderStack pour Android](https://github.com/rudderlabs/rudder-integration-braze-android) sur le dépôt GitHub de Brase, comme décrit à l'étape 3. <br> Pour compléter l'intégration du Mode Périphérique, reportez-vous aux instructions détaillées de RudderStack pour [ajouter Braze à votre projet Android](https://docs.rudderstack.com/destinations/braze#adding-device-mode-integration).
  {% endtab %}
  {% tab iOS %}
    Configurez les mappings au [SDK RudderStack pour iOS](https://github.com/rudderlabs/rudder-integration-braze-ios) sur le dépôt GitHub de Brase, comme décrit à l'étape 3. <br> Pour compléter l'intégration en Mode Périphérique, reportez-vous aux instructions détaillées de RudderStack pour [ajouter Braze à votre projet iOS](https://docs.rudderstack.com/destinations/braze#adding-device-mode-integration).
  {% endtab %}
  {% tab Web / JavaScript %}
    Configurez les mappings au [SDK RudderStack pour JavaScript](https://github.com/rudderlabs/rudder-sdk-js) sur le dépôt GitHub de Brase, comme décrit à l'étape 3. <br> Pour en savoir plus sur le fonctionnement du SDK web, reportez-vous aux instructions détaillées de RudderStack sur le [SDK JavaScript](https://docs.rudderstack.com/rudderstack-sdk-integration-guides/rudderstack-javascript-sdk).
  {% endtab %}
{% endtabs %}

### Étape 2.1b : Intégration du serveur à serveur (mode cloud)

Avec ce mode, le Braze SDK envoie les données de l'événement directement à RudderStack. RudderStack transforme ensuite ces données et les achemine vers Braze dans le format attendu. La transformation se fait dans le backend de RudderStack.

Pour activer l'intégration, configurez la clé d'API REST de votre groupe d'applications et le point de terminaison de l'API REST de Braze dans vos paramètres de connexion (reportez-vous à l'étape 2). ) sur le tableau de bord de RudderStack. Vous devrez également mapper les méthodes RudderStack à Braze (Référez-vous à l'étape 3).

{% alert note %}
Tous les SDK côté serveur de RudderStack (Java, Python, Node.js, Go, Ruby) ne prennent en charge que le mode Cloud. Ceci est dû au fait que leurs SDK côté serveur fonctionnent dans le backend de RudderStack, et ne peuvent pas charger de SDK spécifique à Brésil.
{% endalert %}

{% alert important %} L'intégration du serveur à serveur ne prend pas en charge les fonctionnalités de l'interface utilisateur de Braze, telles que les notifications push ou les messages dans l'application. Ces fonctionnalités sont toutefois prises en charge par l'intégration du Mode Périphérique. {% endalert %}

## Étape 2.2: Configurer les paramètres Braze dans RudderStack

Une fois que vous avez décidé du mode d'intégration et configuré avec succès la source et le Braze SDK sur votre appareil, vous devrez configurer Braze comme destination dans RudderStack. La configuration est assez simple - vous devrez entrer les champs requis suivants :

!\[Paramètres Braze\]\[0\]{: style="max-width:40%;margin-bottom:15px;"}

| Nom                  | Libellé                                                                                                                                                                                                                                                                                                                                    |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Clé de l'application | Peut être trouvé dans le [tableau de bord](https://dashboard.braze.com/app_settings/developer_console) sous <b> Paramètres</b> - <b>Gérer les paramètres</b>                                                                                                                                                                             |
| Clé API REST         | Ceci doit être créé dans le tableau de bord de Braze sous <b>Paramètres</b> - [Console développeur](https://dashboard.braze.com/app_settings/developer_console) - <b>Paramètres API</b>. Vous pouvez trouver les instructions détaillées [ici]({{site.baseurl}}/api/basics/?redirected=true#creating-and-managing-rest-api-keys). |
| Centre de données    | Vous devrez entrer les détails du Data Center comme fourni par Braze. Il est du format `INSTANCE`, comme expliqué dans le [guide des instances de Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/).                                                                                                        |
| SDK natif            | Vous pouvez activer ou désactiver cette option pour utiliser le SDK natif de Braze pour envoyer les événements (utilisez le Mode Périphérique).                                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

## Étape 3 : Utiliser l'intégration - configurer les mappings

Braze prend en charge les méthodes RudderStack [identifier](https://docs.rudderstack.com/rudderstack-api-spec), [piste](https://docs.rudderstack.com/rudderstack-api-spec)et [page](https://docs.rudderstack.com/rudderstack-api-spec).

### Identifier
La méthode `de RudderStack` associe un utilisateur à ses actions. RudderStack capture un identifiant utilisateur unique et les caractères optionnels associés à cet utilisateur tels que le nom, le courriel, l'adresse IP, etc.

Le mapping des champs est fait comme dans le tableau ci-dessous:

| Champ RudderStack | Champ de Braze   |
| ----------------- | ---------------- |
| `prénom`          | `prénom`         |
| `Nom de famille`  | `nom_de famille` |
| `anniversaire`    | `chien`          |
| `avatar`          | `url de l'image` |
| `Ville`           | `ville_domicile` |
| `Pays`            | `Pays`           |
| `Sexe`            | `Sexe`           |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Tous les autres traits seront enregistrés en tant qu' [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).
{% endalert %}

Vous pouvez en savoir plus sur la méthode d'identification de RudderStack dans leur [documentation](https://docs.rudderstack.com/destinations/braze#identify).

### Piste

La méthode `trace` de RudderStack capture toutes les activités de l'utilisateur, ainsi que les propriétés associées à ces activités.

Vous pouvez en savoir plus sur la méthode `track` de RudderStack dans leur [documentation](https://docs.rudderstack.com/destinations/braze#track).

#### Commande terminée
En utilisant [RudderStack eCommerce API](https://docs.rudderstack.com/rudderstack-api-spec/rudderstack-ecommerce-events-specification) pour appeler la méthode de suivi pour un événement avec le nom `Commande complétée`, RudderStack envoie les produits répertoriés dans ce cas à Braze sous la forme d'achats [``]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).

### Page

La méthode `de RudderStack` vous permet d'enregistrer les pages vues de votre site Web. Il capture également toute autre information pertinente à propos de cette page.

Vous pouvez en savoir plus sur la méthode `page` de RudderStack dans leur [documentation](https://docs.rudderstack.com/destinations/braze#page).
[0]: {% image_buster /assets/img/RudderStack/braze_settings.png %}

