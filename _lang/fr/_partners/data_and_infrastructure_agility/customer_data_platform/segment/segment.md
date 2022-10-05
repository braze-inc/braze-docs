---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /partners/segment/
description: "Cet article présente le partenariat entre Braze et Segment, une plateforme de données client qui recueille et transfère des informations entre les différentes sources de votre pile marketing."
page_type: partner
search_tag: Partenaire

---

# Segment  

{% multi_lang_include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment][5] est une plateforme de données client qui vous aide à collecter, nettoyer et activer vos données client. 

L’intégration de Braze et de Segment vous permet de suivre vos utilisateurs et de transmettre des données à un grand nombre de fournisseurs d’analyse des utilisateurs. Segment vous permet de :
- Synchroniser des [Segment Personas]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/) (cohortes) dans Braze pour les utiliser dans des campagnes Braze et des segmentations de Canvas.
- [Importer des données sur les deux plateformes](#integration-options). Nous proposons une intégration SDK côte à côte pour vos applications Android, iOS et Web et une intégration serveur à serveur pour vos services de back-end.
- [Connecter les données sur Segment via Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/). 

## Conditions préalables

| Configuration requise | Description |
| ----------- | ----------- |
| Compte Segment | Un [compte Segment](https://app.segment.com/login) est requis pour profiter de ce partenariat. |
| [Bibliothèques](https://segment.com/docs/sources/) de la source installée et de la source Segment | L’origine de toutes les données envoyées dans Segment, comme des applications mobiles, des sites Web ou des serveurs de back-end.<br>
<br>
Vous devez installer les bibliothèques dans votre application, votre site ou votre serveur avant de pouvoir configurer un flux `Source > Destination`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Pour intégrer Braze et Segment, vous devez définir [Braze en tant que destination](#connection-settings), conformément au [type d’intégration que vous avez choisi](#integration-options). Si vous êtes un nouveau client de Braze, vous pouvez transmettre des données historiques à Braze en utilisant les [Segment Replays](#segment-replays). Ensuite, vous devez configurer les [mappages](#methods), et [tester votre intégration](#step-3-test-your-integration) pour assurer un flux de données régulier entre Braze et Segment.

### Étape 1 : Configurer les paramètres de Braze dans Segment {#connection-settings}

Après avoir configuré avec succès et individuellement vos intégrations de Braze et Segment, vous devrez configurer Braze comme [destination](https://segment.com/docs/destinations/) à partir de Segment. Les paramètres de connexion décrits dans le tableau suivant vous offrent de nombreuses options pour personnaliser le flux de données entre Braze et Segment.

Dans Segment, accédez à **Destinations > Braze > Réception depuis la [plateforme]**.

![]({% image_buster /assets/img/segment_destination_braze.png %})

Ensuite, remplissez les champs suivants dans la page de configuration :
- **Identifiant d’application** : Auparavant appelé clé API. Se trouve dans la **Developer Console** de Braze, sous **Settings (Paramètres)**.
- **Clé API REST du groupe d’apps** :  Clé API REST de Braze avec des autorisations `users/track`. Cela peut être créé dans le **Tableau de bord de Braze > Developer Console > REST API Key (Clé API REST) > Create New Api Key** (Créer une nouvelle clé API).
- **Endpoint du SDK Braze** : L’URL de votre endpoint SDK. Votre endpoint dépendra de [l’URL Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints).
- **Endpoint REST de Braze** : L’URL de votre endpoint REST. Votre endpoint dépendra de [l’URL Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints).
- **Centre de données Appboy** : Indiquez l’instance vers laquelle vos données Braze seront transférées.
- **Enregistrer l’achat lorsque le chiffre d’affaires est présent** : Choisissez quand enregistrer des achats.
- **ID push de site Web Safari** : Safari nécessite un [ID push de site Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-5-configure-safari-push) pour envoyer des notifications push.
- **Version du SDK Web de Braze** : Indiquez la version du SDK Web de Braze que vous avez intégré. Si vous n’êtes pas sûr, contactez votre gestionnaire de compte ou le [service d’assistance]({{site.baseurl}}/braze_support/) de Braze.

{% details Additional connection settings %}

|Nom|Options | Description|
|---|---|---|
|Autoriser les robots d’indexation| Activé/désactivé (True/False) | Les robots d’indexation sont des programmes automatiques qui visitent des sites Web, les lisent et collectent des informations qui peuvent être importantes pour l’index d’un moteur de recherche. Vous pouvez autoriser ou interdire ces robots à partir de votre page Web intégrée ou de votre application. Par défaut, Braze désactive les robots d’indexation. |
|Envoyer automatiquement des messages in-app| Activé/désactivé (True/False) | Braze vous permet automatiquement d’envoyer des notifications push à vos utilisateurs dès que l’intégration est effectuée avec succès. |
|Ne pas charger FontAwesome| Activé/désactivé (True/False) | Braze utilise FontAwesome pour les icônes de nos messages in-app, mais vous pouvez désactiver cette fonctionnalité à tout moment. |
|Activer les messages HTML in-app| Activé/désactivé (True/False) | Cette option permet aux utilisateurs de la plateforme Braze d’écrire des messages in-app au format HTML. Pour plus d’informations, consultez les [JS Docs](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#initialize).|
|Activer la connexion| Activé/désactivé (True/False) | [Se connecter à la console JavaScript](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#setlogger) par défaut. |
|Intervalle minimum en secondes entre les actions de déclenchement| N’importe quel chiffre | Par défaut, les actions de déclenchement ne s’activeront que si 30 secondes se sont écoulées depuis la dernière action de déclenchement. |
|Ouvrir les messages in-app dans un nouvel onglet | Activé/désactivé (True/False) | Par défaut, les liens des messages in-app se chargent dans l’onglet actuel ou un nouvel onglet comme indiqué sur la plateforme Braze. |
|Ouvrir les cartes de fil d’actualité dans un nouvel onglet | Activé/désactivé (True/False) | Par défaut, les liens des cartes de fil d’actualité ou des cartes de contenu se chargent dans l’onglet actuel ou un nouvel onglet comme indiqué sur la plateforme Braze. |
|Délai d’expiration de session en secondes| N’importe quel chiffre | Par défaut, les sessions expirent après 30 minutes d’inactivité. |
|Suivre toutes les pages | Activé/désactivé (True/False) | Envoie tous les [appels de pages Segment](https://segment.com/docs/spec/page/) à Braze en tant qu’événements de page.|
|Suivre uniquement les pages nommées | Activé/désactivé (True/False) | Envoie tous les [appels de page Segment nommés](https://segment.com/docs/spec/page/) à Braze
|Mettre à jour uniquement les utilisateurs existants| Activé/désactivé (True/False) | Cette option s’applique uniquement aux intégrations côté serveur. Elle détermine si tous les utilisateurs ou utilisateurs existants seront mis à jour. Par défaut, cette option est définie comme `false`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% enddetails %}

### Étape 2 : Choisir et implémenter un type d’intégration {#integration-options}

Vous pouvez intégrer les bibliothèques Web (Analytics.js) et les bibliothèques natives côté client de de Segment avec Braze en utilisant une intégration côte à côte (« mode périphérique ») ou une intégration serveur vers serveur (« mode cloud »).

| Intégration | Détails |
| ----------- | ------- |
| [Intégration côte à côte<br>
Mode périphérique"](#side-by-side-sdk-integration) | Ce mode mappe le SDK de Segment vers Braze, permettant d’accéder à des fonctions plus avancées et de tirer le meilleur parti de l’intégration serveur à serveur de Braze. |
| [Intégration serveur à serveur<br>
Mode cloud"](#server-to-server-integration) | Ce mode transfère les données de Segment vers l’[endpoint user/track]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint) de Braze. |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Vous pouvez en apprendre davantage sur les options d’intégration de Segment (modes de connexion) et les avantages de chaque mode [ici](https://segment.com/docs/destinations/#connection-modes).
{% endalert %}

#### Intégration SDK côte à côte

Également appelée « mode périphérique », cette intégration mappe le SDK et les [méthodes](#methods) de Segment vers Braze, permettant d’accéder à des fonctions plus avancées et de tirer le meilleur parti de l’intégration serveur à serveur de Braze.

{% tabs %}
{% tab Android %}

Trouvez et configurez des [mappages](#methods) au SDK de Segment pour [Android](https://github.com/appboy/appboy-segment-android) sur le GitHub de Braze.

Pour terminer l’intégration côte à côte, reportez-vous aux instructions détaillées de Segment pour [Android](https://segment.com/docs/connections/destinations/catalog/braze/#android).

{% endtab %}
{% tab iOS %}

Trouvez et configurez des [mappages](#methods) au SDK de Segment pour [iOS](https://github.com/appboy/appboy-segment-ios) sur le GitHub de Braze.

Pour terminer l’intégration côte à côte, reportez-vous aux instructions détaillées de Segment pour [iOS](https://segment.com/docs/connections/destinations/catalog/braze/#ios).

{% endtab %}
{% tab Web or Javascript %}

Trouvez et configurez des [mappages](#methods) au SDK de Segment pour le [Web / Analytics.js (SDK JavaScript de Segment)](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) sur le GitHub de Braze.

Pour le SDK Web de Braze, la [bibliothèque Analytics.js de Segment](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) s’insère dynamiquement et initialise notre SDK Web lorsque vous ajoutez Braze comme destination sur votre tableau de bord de Segment. Cependant, pour utiliser les capacités de notifications basées sur navigateur de Braze, reportez-vous à la documentation [Web](https://segment.com/docs/connections/destinations/catalog/braze/#web) de Segment.

{% endtab %}
{% endtabs %}

#### Intégration serveur à serveur

Également appelée « mode Cloud », cette intégration transfère les données de Segment vers l’API REST de Braze.

Cette intégration est **uniquement** utilisée en association avec les [bibliothèques côté serveur][36] de Segment comme son SDK Ruby ou Go.

Activez l’intégration en définissant la [clé API REST de votre groupe d’apps][39] et l’[endpoint API REST][40] de Braze pour votre centre de données (cluster) correspondant dans les [paramètres de connexion de votre tableau de bord Segment](#connection-settings).

Comme pour l’intégration côte à côte, vous devrez mapper les [méthodes](#methods) de Segment vers Braze.

Toutefois, contrairement à l’intégration côte à côte, l’intégration serveur à serveur ne prend **pas** en charge les fonctionnalités de l’interface utilisateur de Braze, telles que les messages in-app, les fils d’actualité ou les notifications push.

Certaines données [collectées automatiquement][25] ne sont disponibles qu’avec l’intégration côte à côte. Les données suivantes ne sont **pas disponibles via l’intégration serveur à serveur** :
- Sessions
- Première application utilisée
- Dernière application utilisée

##### Activation des notifications push

Actuellement, l’intégration serveur à serveur de Braze et Segment **ne prend pas en charge** les méthodes de jetons de notification push. Pour activer les notifications push dans Braze, vous devez importer des jetons de notification push via l’[objet d’attribut utilisateur][18] de notre API REST de [données utilisateur][19]. Vous pouvez également utiliser l’[intégration côte à côte](#side-by-side-sdk-integration) pour collecter et mapper des jetons de notification push.

### Étape 3 : Méthodes de mappage {#methods}

Braze prend en charge les méthodes [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page) (Web), [Identification](https://segment.com/docs/spec/identify/), et [Suivi](https://segment.com/docs/spec/track/), ainsi que les méthodes de Segment ; cependant, nos API REST exigent un [ID utilisateur][41] lors de ces appels. Braze prend également en charge le mappage d’attributs personnalisés à l’aide de la méthode [Groupe](https://segment.com/docs/spec/group/) de Segment.

{% tabs local %}
{% tab Page %}
#### Page {#page}

L’appel de [page](https://segment.com/docs/spec/page/) vous permet d’enregistrer chaque fois qu’un utilisateur voit une page sur votre site Web, ainsi que les propriétés facultatives de la page.

| Méthode Segment | Méthode Braze | Exemple |
|---|---|---|
| [Page](https://segment.com/docs/spec/page/) sans nom | Enregistré en tant qu’[événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) | Segment: `analytics.page();`<br>
Braze : `appboy.logCustomEvent("Loaded a Page");` |
| [Page](https://segment.com/docs/spec/page/) avec un nom | Enregistré en tant qu’[événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events)    | Segment: `analytics.page("Home")` ;<br>
Braze : `appboy.logCustomEvent("Viewed Home Page");` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}

{% tab Identify %}
#### Identification

Lorsque vous [identifiez](https://segment.com/docs/connections/destinations/catalog/braze/#identify) un utilisateur, nous enregistrerons les informations pour cet utilisateur avec `userId` en tant qu’ID de l’utilisateur externe.

| Champ de Segment | Champ de Braze |
| ------------- | ----------- |
| `firstName` | `first_name`
| `lastName` | `last_name`
| `birthday` | `dob`|
| `address.city` | `home_city`|
| `address.country` | `country` |
| `gender` | `gender` |
{: .reset-td-br-1 .reset-td-br-2}

Toutes les autres caractéristiques seront enregistrées en tant qu’[attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).

| Méthode Segment | Méthode Braze | Exemple |
|---|---|---|
| Identifier un utilisateur avec un ID utilisateur | Définir un ID externe | Segment:  `analytics.identify("dawei");`<br>
Braze : `appboy.changeUser("dawei")` |
| Identification avec des caractéristiques réservées | Définir les attributs utilisateur | Segment: `analytics.identify({email: "dawei@braze.com"});`<br>
 Braze : `appboy.getUser().setEmail("dawei@braze.com");`
| Identification avec des caractéristiques personnalisées | Définir des attributs personnalisés | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>
Braze : `appboy.getUser().setCustomAttribute("fav_cartoon": "Naruto")` ;
| Identification avec l’ID et les caractéristiques utilisateur | Segment: Définir l’ID externe et l’attribut | Combine les méthodes précédentes. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
Lorsque vous transmettez des données d’attribut utilisateur, assurez-vous de ne transmettre que les valeurs des attributs qui ont changé depuis la dernière mise à jour. Cela vous permettra de ne pas consommer inutilement vos points de données.
{% endalert %}
{% endtab %}

{% tab Track %}
#### Suivi

Lorsque vous  _suivez_  un événement, nous enregistrerons cet événement en tant qu’[événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) en utilisant le nom fourni.

| Méthode Segment | Méthode Braze | Exemple |
|---|---|---|
| [Suivi](https://segment.com/docs/spec/track/) | Enregistré en tant qu’[événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) | Segment: `analytics.track("played_game");` <br>
Braze : `appboy.logCustomEvent("played_game");`|
| [Suivre avec les propriétés](https://segment.com/docs/spec/track/) | Enregistré en tant que [propriété de l’événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties). | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>
Braze : `appboy.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Suivre avec le produit](https://segment.com/docs/spec/track/) | Enregistré en tant qu’[Événement d’achat]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/). | Segment: `analytics.track("purchase", {products: [product_id: "ab12", price: 19]});` <br>
Braze : `appboy.logPurchase("ab12", 19);` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

##### Commande terminée {#order-completed}

Lorsque vous  _suivez_  un événement avec le nom `Order Completed` en utilisant le format décrit dans l’[API Ecommerce](https://segment.com/docs/spec/ecommerce/v2/) de Segment, nous enregistrerons les produits que vous avez désignés comme [achats]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data).
{% endtab %}

{% tab group %}
#### Groupe

Lorsque vous appelez un  _groupe_  dans Segment, nous enregistrerons un [attribut personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) avec le nom `ab_segment_group_<groupId>`, où `groupId` correspond à l’ID du groupe dans les paramètres de la méthode. Par exemple, si l’ID du groupe est `1234`, alors le nom de l’attribut personnalisé sera `ab_segment_group_1234`. La valeur de l’attribut personnalisé sera définie sur `true`.

| Méthode Segment | Méthode Braze | Exemple |
|---|---|---|
| [Utilisateurs du groupe](https://segment.com/docs/connections/spec/group/) | Définir un attribut personnalisé | Segment:  `analytics.group("12345");`<br>
Braze : `appboy.getUser().setCustomAttribute("ab_segment_group_1234": true)` ; |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

### Étape 4 : Tester votre intégration

La plupart de vos mesures [Overview][27] (sessions à vie, utilisateur actif par mois, utilisateur actif par jour, adhérence, sessions quotidiennes et sessions quotidiennes par MAU) seront vides même si Braze reçoit des données de Segment.

Vous pouvez consulter vos données sur les pages [événements personnalisés][22] ou [chiffre d’affaires][28] ou encore en [créant un segment][23]. La page **Événements personnalisés** du tableau de bord vous permet de visualiser le décompte des événements personnalisés dans le temps. Notez que vous ne pourrez pas utiliser de [formules][24] qui incluent des statistiques sur les utilisateurs actifs par mois et les utilisateurs actifs par jour.

Si vous envoyez des données d’achat à Braze (voir Commande terminée dans l’onglet **Suivi** de l’[Étape 3](#methods)), la page [chiffre d’affaires][28] vous permet d’afficher des données sur le chiffre d’affaires ou les achats correspondants à des périodes spécifiques ou sur le chiffre d’affaires total de votre application.

[Créer un segment][26] vous permet de filtrer vos utilisateurs en fonction des données d’attribut et d’événement personnalisés.

{% alert important %}
Si vous utilisez une intégration serveur à serveur, les filtres liés aux données de session collectées automatiquement (par ex. « première application utilisée » et « dernière application utilisée ») ne fonctionneront pas. Utilisez une intégration côte à côte si vous souhaitez les utiliser dans votre intégration Segment et Braze.
{% endalert %}

## Effacer et supprimer des utilisateurs 

Si vous devez effacer ou supprimer des utilisateurs, notez que la [fonction de suppression d’utilisateurs de Segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) **est** mappée à l’endpoint[users/delete]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint) de Braze. Notez que la vérification de ces suppressions peut prendre jusqu’à 30 jours.

Assurez-vous de sélectionner un identifiant utilisateur qui est commun à Braze et Segment (comme dans l’ID utilisateur ou l’ID externe). Après avoir soumis une requête de suppression à travers Segment, vous pourrez voir le statut de la requête et la manière dont cela affecte chacune de vos destinations.

## Relectures de données via Segment

Segment fournit un service permettant de « relire » toutes les données historiques pour un nouveau partenaire de technologie. Les nouveaux clients de Braze qui souhaitent importer toutes leurs données historiques pertinentes peuvent le faire via Segment.

Segment se connectera à notre [endpoint Users Track]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour importer des données utilisateur dans Braze au nom du client.

{% alert important %}
Si les utilisateurs n’ont pas d’ID externe, ils ne seront pas importés dans Braze. Notre endpoint users/track exige un ID utilisateur si aucun ID Braze ou alias d’utilisateur n’est fourni. Actuellement, Segment ne mappe pas vers les ID ou alias d’utilisateur de Braze, ce qui signifie que les données anonymes ne seront pas « relues ».
{% endalert %}

## Bonnes pratiques

{% details Review use cases to avoid data overages. %}

Segment **ne** limite pas le nombre d’éléments de données que les clients peuvent leur envoyer. Segment vous permet d’envoyer toutes vos données ou de décider quels événements vous souhaitez envoyer à Braze. Au lieu d’envoyer tous vos événements à l’aide de Segment, nous vous suggérons de revoir les cas d’utilisation avec vos équipes marketing et éditoriales afin de déterminer quels événements vous allez envoyer à Braze pour éviter les dépassements de données.

{% enddetails %}

{% details Understand the difference between the custom API endpoint and the custom REST API endpoint. %}

| Terminologie Braze | Équivalent Segment |
| ----------------- | ------------------ |
| Endpoint du SDK Braze | Endpoint d’API personnalisé |
| Endpoint REST de Braze | Endpoint d’API REST personnalisé |
{: .reset-td-br-1 .reset-td-br-2}

Votre endpoint d’API Braze (appelé « endpoint d’API personnalisé » dans Segment) est l’endpoint SDK que Braze configure pour votre SDK (par exemple, `sdk.iad-03.braze.com`). Votre endpoint d’API REST de Braze (appelé « endpoint d’API REST personnalisé » dans Segment) est l’endpoint d’API REST (par exemple, `https://rest.iad-03.braze.com`).
{% enddetails %}

{% details Ensure ‘custom API endpoint’ is input into Segment correctly. %}

| Terminologie Braze | Équivalent Segment |
| ----------------- | ------------------ |
| Endpoint du SDK Braze | Endpoint d’API personnalisé |
| Endpoint REST de Braze | Endpoint d’API REST personnalisé |
{: .reset-td-br-1 .reset-td-br-2}

Le format approprié doit être respecté pour vous assurer de saisir correctement votre endpoint de SDK Braze. Votre endpoint SDK Braze ne doit pas inclure `https://` (par exemple, `sdk.iad-03.braze.com`), car cela invaliderait l’intégration de Braze. Ceci est requis parce que Segment précède automatiquement votre endpoint par `https://`, ce qui entraîne l’initialisation de Braze avec un endpoint non valide `https://https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Certain data is not mapping to braze. %}

Segment prend en charge différents types et structures de données, ce qui entraîne des problèmes de transmission des données de Segment à Braze.

Scénarios dans lesquels les données ne seront pas transmises comme prévu :
1. Les propriétés de l’événement incluent des matrices ou objets imbriqués.
  - Les connexions iOS, Android et Cloud prennent en charge des objets imbriqués dans les propriétés de l’événement. Le mode périphérique Web ne prend pas en charge ces fonctions. Braze travaille avec Segment pour mettre à jour le SDK du mode périphérique Web. 
2. Transfert de données anonymisées d’un serveur à l’autre.
  - Les clients peuvent utiliser les bibliothèques serveur à serveur de Segment pour faire transférer des données anonymes vers d’autres systèmes.

{% enddetails %}

{% details Customization of Braze initialization. %}

Il existe plusieurs façons de personnaliser Braze : les [notifications push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/), [les messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/overview/), [les cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/), et l’initialisation. L’intégration côte à côte vous permet de personnaliser les notifications push, les messages in-app et les cartes de contenu comme vous le feriez avec une intégration Braze directe.

Cependant, il peut être difficile, voire parfois impossible, de les personnaliser ou de définir des configurations d’initialisation lorsque le SDK de Braze est intégré. En effet, Segment initiera le SDK Braze pour vous lors de l’initialisation de Segment.

{% enddetails %}

[5]: https://segment.com
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events
[14]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[18]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[19]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[22]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data
[23]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[24]: {{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula
[25]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection
[26]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[27]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[36]: https://segment.com/docs/sources/#server
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[39]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[40]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[41]: https://segment.com/docs/spec/identify/#user-id
