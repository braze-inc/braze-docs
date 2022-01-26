---
nav_title: Segment
article_title: Segment
page_order: 1
alias: /fr/partners/segment/
description: "Cet article décrit le partenariat entre Braze et Segment, une plateforme de données client qui collecte et achemine des informations entre les sources de votre pile marketing."
page_type: partenaire
search_tag: Partenaire
---

# Segment

{% include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment][5] est une plate-forme de données client qui vous aide à collecter, nettoyer et activer vos données client.

L'intégration de Braze et Segment vous permet de suivre vos utilisateurs et d'acheminer les données vers une grande variété de fournisseurs d'analyse utilisateur. Le segment vous permet de :
- Synchronisez [Segment Personas]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/) (cohortes) à Braze pour une utilisation dans la campagne Braze et la segmentation Canvas .
- [Importez des données sur les deux plates-formes](#integration-options). Nous offrons une intégration de SDK côte à côte pour vos applications Android, iOS, web et une intégration de serveur à serveur pour vos services backend.
- [Connectez des données à la Segment à travers les courants]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/).

## Pré-requis

| Exigences                                                                       | Libellé                                                                                                                                                                                                                                                                                                                     |
| ------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte de segment                                                               | Un [compte de segment](https://app.segment.com/login) est requis pour tirer parti de ce partenariat.                                                                                                                                                                                                                        |
| Bibliothèques [source et Segment installées](https://segment.com/docs/sources/) | L'origine de toutes les données envoyées dans Segment, telles que les applications mobiles, les sites Web ou les serveurs d'arrière-plan.<br><br>Vous devez installer les bibliothèques dans votre application, site, ou serveur avant d'être en mesure de configurer un flux `Source > Destination` réussi. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Intégration

Pour intégrer Braze et Segment, vous devez définir [Braze comme une Destination](#connection-settings) en accord avec [le type d'intégration que vous avez choisi](#integration-options). Si vous êtes un nouveau client de Braze, vous pouvez relayer des données historiques à Braze en utilisant [Segment Replays](#segment-replays). Ensuite, vous devez configurer [mappings](#methods), et [tester votre intégration](#step-3-test-your-integration) pour assurer un flux de données fluide entre Braze et Segment.

### Étape 1 : Configurer les paramètres Braze dans le segment {#connection-settings}

Après avoir configuré vos intégrations de Braze et de Segment avec succès individuellement, vous devrez configurer Braze comme une [destination](https://segment.com/docs/destinations/) à partir de Segment. Vous aurez de nombreuses options pour personnaliser le flux de données entre Braze et Segment en utilisant les paramètres de connexion décrits dans le tableau ci-dessous.

Dans le segment, accédez à __Destinations > Braze > Réception de [platform]__.

![Paramètres de connexion de destination]({% image_buster /assets/img/segment_destination_braze.png %})

Ensuite, fournissez les champs suivants dans la page de configuration :
- __Identifiant de l'application__: précédemment appelé la clé API. Trouvé dans la __console de développement de Braze__ sous __Réglages__.
- __Groupe d'applications REST API key__: Braze REST API key with `users/track` permissions. Ceci peut être créé dans le tableau de bord __Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__
- __Fin de SDK Braze__: Votre URL de fin de SDK. Votre point de terminaison dépendra de l'URL [Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints).
- __Point de terminaison REST Braze__: Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints).
- __Appboy datacenter__: Spécifiez à quelle instance vos données Braze seront transmises.
- __Log purchase when revenue is present__: Choisissez quand enregistrer les achats.
- __ID push du site Safari__: Safari nécessite un [ID Push du site Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-5-configure-safari-push) pour envoyer push.
- __Braze web SDK version__: Indiquez quelle version du SDK web de braze vous avez intégré. Si vous n'êtes pas sûr, contactez votre responsable de compte ou le support [de Braze]({{site.baseurl}}/braze_support/).

{% details Additional connection settings %}

| Nom                                                               | Options                        | Libellé                                                                                                                                                                                                                                                                                                                               |
| ----------------------------------------------------------------- | ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Autoriser l'activité des robots d'exploration                     | Activer/Désactiver (True/Faux) | Les Crawlers Web sont des programmes automatiques qui visitent des sites Web, les lisent et recueillent des informations qui pourraient s'avérer importantes pour un index des moteurs de recherche. Vous pouvez autoriser ou interdire cela depuis votre page Web intégrée ou votre application. Braze ne l'autorise pas par défaut. |
| Envoyer automatiquement des messages dans l'application           | Activer/Désactiver (True/Faux) | Braze vous permet automatiquement d'envoyer des messages push à vos utilisateurs lors d'une intégration appropriée.                                                                                                                                                                                                                   |
| Ne pas charger la police géniale                                  | Activer/Désactiver (True/Faux) | Braze utilise FontAwesome pour nos icônes de messages dans l'application, mais vous pouvez interdire cette fonctionnalité à tout moment.                                                                                                                                                                                              |
| Activer les messages HTML dans l'application                      | Activer/Désactiver (True/Faux) | Permet aux utilisateurs de la plateforme Braze d'écrire des messages HTML dans l'application. Plus d'informations dans les [Docs JS](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize).                                                                                                                     |
| Activer les logs                                                  | Activer/Désactiver (True/Faux) | [Connectez-vous par défaut à la console JavaScript](https://js.appboycdn.com/web-sdk/2.0/doc/module-appboy.html#.setLogger).                                                                                                                                                                                                          |
| Intervalle minimum entre les actions de déclenchement en secondes | N'importe quel nombre          | Par défaut, les actions de déclenchement ne se déclencheront que si 30 secondes se sont écoulées depuis la dernière action de déclenchement.                                                                                                                                                                                          |
| Ouvrir les messages dans l'application dans un nouvel onglet      | Activer/Désactiver (True/Faux) | Par défaut, les liens à partir du message dans l'application cliquent charger dans l'onglet actuel ou un nouvel onglet spécifié sur la plateforme Braze.                                                                                                                                                                              |
| Ouvrir les fiches d'actualités dans un nouvel onglet              | Activer/Désactiver (True/Faux) | Par défaut, les liens des cartes de flux d'actualités ou des cartes de contenu se chargent dans l'onglet actuel ou dans un nouvel onglet tel que spécifié dans la plateforme Braze.                                                                                                                                                   |
| Délai de la session en secondes                                   | N'importe quel nombre          | Par défaut, les sessions sortent après 30 minutes d'inactivité.                                                                                                                                                                                                                                                                       |
| Suivre toutes les pages                                           | Activer/Désactiver (True/Faux) | Envoie tous les [appels de la page du segment](https://segment.com/docs/spec/page/) à Braze comme événements de la page.                                                                                                                                                                                                              |
| Suivre uniquement les pages nommées                               | Activer/Désactiver (True/Faux) | Envoie tous les [appels de la page Segment nommée](https://segment.com/docs/spec/page/) à Braze                                                                                                                                                                                                                                       |
| Mettre à jour les utilisateurs existants uniquement               | Activer/Désactiver (True/Faux) | Cela ne s'applique qu'aux intégrations côté serveur. Ceci détermine si tous les utilisateurs ou les utilisateurs existants seront mis à jour. La valeur par défaut est `false`.                                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% enddetails %}

### Étape 2 : Choisissez le type d'intégration et l'implémentation {#integration-options}

Vous pouvez intégrer les sources web de Segment (Analytics.js) et les bibliothèques natives côté client avec Braze en utilisant soit une intégration côte à côte ("Device-mode") ou une intégration de serveur-à-serveur ("Cloud-mode").

| Intégration                                                              | Détails du produit                                                                                                                                                        |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Coté à côte<br>"Mode appareil"](#side-by-side-sdk-integration)    | Maps Segment SDK to Braze's, permettant d'accéder à des fonctionnalités plus profondes et une utilisation plus complète de Braze que l'intégration serveur-serveur.       |
| [Serveur-à-serveur<br>"Mode Cloud"](#server-to-server-integration) | Transfère les données du segment vers le [point de terminaison utilisateur/piste de Braze]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint). |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Vous pouvez en savoir plus sur les options d'intégration de Segment (modes de connexion), y compris les avantages de chacun, [ici](https://segment.com/docs/destinations/#connection-modes).
{% endalert %}

#### Intégration de SDK côte à côte

Aussi appelée "device-mode", cette intégration fait correspondre le SDK de Segment et les [méthodes](#methods) à Braze, permettant d'accéder à des fonctionnalités plus profondes et une utilisation plus complète de Braze que l'intégration serveur-serveur.

{% tabs %}
{% tab Android %}

Voir et configurer [mappings](#methods) au SDK de Segment pour [Android](https://github.com/appboy/appboy-segment-android) sur Github de Brase.

Pour compléter l'intégration côte-à-côte, veuillez vous référer aux instructions détaillées de Segment pour [Android](https://segment.com/docs/connections/destinations/catalog/braze/#android).

{% endtab %}
{% tab iOS %}

Voir et configurer [mappings](#methods) au SDK de Segment pour [iOS](https://github.com/appboy/appboy-segment-ios) sur Github de Brase.

Pour compléter l'intégration côte-à-côte, veuillez vous référer aux instructions détaillées de Segment pour [iOS](https://segment.com/docs/connections/destinations/catalog/braze/#ios).

{% endtab %}
{% tab Web or Javascript %}

Voir et configurer [mappings](#methods) au SDK de Segment pour [Web / Analytics.js (Segment's JavaScript SDK)](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) sur le Github de Braze.

Pour le Web SDK de Braze, [Analyses du segment. s bibliothèque](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) intègre et initialise dynamiquement notre SDK Web lorsque vous ajoutez Braze comme destination sur votre tableau de bord Segment. Cependant, pour utiliser les fonctionnalités de notification de navigateur de Braze, veuillez vous référer à la documentation de [Web](https://segment.com/docs/connections/destinations/catalog/braze/#web) de Segment.

{% endtab %}
{% endtabs %}

#### Intégration du serveur à serveur

Aussi appelé "Cloud-mode", cette intégration transfère les données de Segment à l'API REST de Braze.

Cette intégration est **seule** utilisée en association avec les [bibliothèques côté serveur][36]de Segment, comme leurs SDK Ruby ou Go.

Activez l'intégration en définissant la clé REST API de votre groupe d'applications [][39] et le point de terminaison [REST API de Braze][40] pour votre centre de données correspondant (cluster) dans vos [paramètres de connexion sur le tableau de bord du segment](#connection-settings).

Similaire à l'intégration côte à côte, vous devrez mapper les méthodes [du segment](#methods) au Brésil.

Cependant, contrairement à l'intégration côte à côte, l'intégration du serveur à serveur ne supporte **aucune des fonctionnalités de l'interface utilisateur de Braze** comme la messagerie intégrée, le fil d'actualités ou les notifications push.

Certaines données [capturées automatiquement][25] ne sont disponibles que par une intégration côtière. Les données suivantes ne sont pas __disponibles via l'intégration serveur-serveur__:
- Sessions
- Première application utilisée
- Dernière application utilisée

##### Activation des notifications push

Actuellement, l'intégration du serveur à serveur de Braze avec le segment __ne supporte pas__ les méthodes pour les jetons push. Afin d'activer les notifications push au Brésil, vous devez importer des jetons push via l'objet [attribut utilisateur][18] de notre [API REST][19] de données utilisateur. Vous pouvez également compter sur l'intégration [côte à côte](#side-by-side-sdk-integration) pour la capture de jetons push et le mapping.


### Étape 2 : Méthodes de mappage {#methods}

Braze prend en charge les méthodes [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page) (web), [Identifier](https://segment.com/docs/spec/identify/), et [Track](https://segment.com/docs/spec/track/)et Segment ; cependant, nos APIs REST exigent que vous incluiez un [ID d'utilisateur][41] lors de ces appels. Braze prend également en charge le mapping d'attributs personnalisés en utilisant la méthode [Group](https://segment.com/docs/spec/group/) de Segment.

{% tabs local %}
{% tab Page %}
#### Page {#page}

L'appel à [page](https://segment.com/docs/spec/page/) vous permet d'enregistrer chaque fois qu'un utilisateur voit une page de votre site Web, ainsi que toute propriété facultative à propos de la page.

| Méthode de segment                                   | Méthode de Braze                                                                                                                       | Exemple                                                                                              |
| ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| [Page](https://segment.com/docs/spec/page/) sans nom | Connecté en tant qu' [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) | Segment: `analytics.page();`<br>Brésil : `appboy.logCustomEvent("Chargé une page");`           |
| [Page](https://segment.com/docs/spec/page/) avec nom | Connecté en tant qu' [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) | Segment: `analytics.page("Accueil")`;<br>Brésil : `appboy.logCustomEvent("Viewed Home Page");` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% endtab %}

{% tab Identify %}
#### Identifier

Lorsque vous [identifiez](https://segment.com/docs/connections/destinations/catalog/braze/#identify) un utilisateur, nous enregistrerons des informations pour cet utilisateur avec `userId` comme identifiant d'utilisateur externe.

| Champ de segment | Champ de Braze   |
| ---------------- | ---------------- |
| `prénom`         | `prénom`         |
| `Nom de famille` | `nom_de famille` |
| `anniversaire`   | `chien`          |
| `Ville`          | `ville_domicile` |
| `Pays`           | `Pays`           |
| `Sexe`           | `Sexe`           |
{: .reset-td-br-1 .reset-td-br-2}

Tous les autres traits seront enregistrés en tant qu' [attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/).

| Méthode de segment                                           | Méthode de Braze                            | Exemple                                                                                                                                   |
| ------------------------------------------------------------ | ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| Identifier avec l'ID de l'utilisateur                        | Définir un ID externe                       | Segment:  `analytics.identify("dawei");`<br>Braze: `appboy.changeUser("dawei")`                                                     |
| S'identifier avec des traits réservés                        | Définir les attributs utilisateur           | Segment: `analytics.identify({email: "dawei@braze.com"});`<br> Braze: `appboy.getUser().setEmail("dawei@braze.com");`               |
| Identifier avec des traits personnalisés                     | Définir les attributs personnalisés         | Segment: `analytics.identify({fav_cartoon: "Naruto"});`<br>Brésil : `appboy.getUser().setCustomAttribute("fav_cartoon": "Naruto")`; |
| Identifier avec l'identifiant et les traits de l'utilisateur | Segment: Définir l'ID externe et l'attribut | Combiner les méthodes ci-dessus.                                                                                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
Lorsque vous passez des données d'attribut utilisateur, vérifiez que vous ne passez que des valeurs pour les attributs qui ont changé depuis la dernière mise à jour. Cela vous assurera de ne pas consommer inutilement des points de données vers votre allogue.
{% endalert %}
{% endtab %}

{% tab Track %}
#### Piste

Lorsque vous _suivez_ un événement, nous enregistrerons cet événement comme un [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events) en utilisant le nom fourni.

| Méthode de segment                                                 | Méthode de Braze                                                                                                                                 | Exemple                                                                                                                                                                            |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Piste](https://segment.com/docs/spec/track/)                      | Connecté en tant qu' [événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events).          | Segment: `analytics.track("played_game");` <br>Brésil : `appboy.logCustomEvent("played_game");`                                                                              |
| [Suivre avec des propriétés](https://segment.com/docs/spec/track/) | Connecté en tant que [propriété d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties). | Segment: `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` <br>Braze: `appboy.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Suivre avec le produit](https://segment.com/docs/spec/track/)     | Connecté en tant qu' [Événement d'Achat]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/).         | Segment: `analytics.track("purchase", {products: [product_id: "ab12", price: 19]});` <br>Brésil : `appboy.logPurchase("ab12", 19);`                                          |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

##### Commande terminée {#order-completed}

Lorsque vous _suivez_ un événement avec le nom `Commande terminée` en utilisant le format décrit dans [l'API ECommerce][4]du segment nous enregistrerons les produits que vous avez énumérés comme [achats][28].
{% endtab %}

{% tab group %}
#### Groupes

Lorsque vous appelez le groupe __ dans le segment, nous enregistrerons un [attribut personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/) avec le nom `ab_segment_group_<groupId>`, où `groupId` est l'ID du groupe dans les paramètres de la méthode. Par exemple, si l'ID du groupe est `1234`, alors le nom de l'attribut personnalisé sera `ab_segment_group_1234`. La valeur de l'attribut personnalisé sera définie à `true`.

| Méthode de segment                                                         | Méthode de Braze                 | Exemple                                                                                                                       |
| -------------------------------------------------------------------------- | -------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| [Groupes d'utilisateurs](https://segment.com/docs/connections/spec/group/) | Définir un attribut personnalisé | Segment:  `analytics.group("12345");`<br>Brésil : `appboy.getUser().setCustomAttribute("ab_segment_group_1234": true)`; |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

### Étape 3 : Testez votre intégration

La plupart de vos [métriques][27] d'aperçu (sessions à vie, MAU, DAU, adhésivité, les sessions quotidiennes, et les sessions quotidiennes par MAU) seront vides même si Braze reçoit des données de Segment.

Vous pouvez afficher vos données dans les pages [événements personnalisés][22] ou [revenus][28] ou en [créant un segment][23]. La page __Événements Personnalisés__ du tableau de bord vous permet de voir le nombre d'événements personnalisés au fil du temps. Notez que vous ne serez pas en mesure d'utiliser les formules [][24] qui incluent les statistiques MAU et DAU.

Si vous envoyez des données d'achat à Braze (voir [commande complétée](#order-completed)), la page [revenus][28] vous permet de visualiser des données sur les revenus ou les achats sur des périodes spécifiques ou sur les revenus totaux de votre application.

[La création d'un segment][26] vous permet de filtrer vos utilisateurs en fonction de l'événement personnalisé et des données d'attributs.

{% alert important %}
Si vous utilisez une intégration de serveur à serveur, les filtres liés aux données de session automatiquement collectées (comme "première application utilisée" et "dernière application utilisée") ne fonctionneront pas. Utilisez une intégration côte à côte si vous voulez les utiliser dans votre intégration Segment et Braze.
{% endalert %}

## Suppression et suppression de l'utilisateur

Si vous avez besoin de supprimer ou supprimer des utilisateurs, Notez que la fonctionnalité de suppression d'utilisateur de [segment](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to) __est__ associée au point de terminaison Braze [utilisateurs/suppression]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint). Veuillez noter que la vérification de ces suppressions peut prendre jusqu'à 30 jours.

Vous devez vous assurer que vous sélectionnez un identifiant utilisateur commun entre Braze et Segment (comme dans l'ID de l'utilisateur ou l'ID externe). Une fois que vous avez initié une demande de suppression avec Segment, vous serez alors en mesure de voir le statut et la façon dont il affecte chacune de vos Destinations.

## Rediffusions de segment

Segment fournit un service aux clients pour "Rejouer" toutes les données historiques à un nouveau partenaire technologique. Les nouveaux clients de Braze qui veulent importer toutes les données historiques pertinentes peuvent le faire par Segment.

Le segment se connectera à notre [point de terminaison des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour importer les données utilisateur dans Braze au nom du client.

{% alert important %}
Si les utilisateurs n'ont pas d'ID externe, ils ne seront pas importés en Brésil. Nos utilisateurs/terminaux de parcours requièrent un identifiant utilisateur si un identifiant Braze ou un alias d'utilisateur n'est pas fourni. Actuellement, Segment ne correspond pas à Braze ID de Braze ou à l'alias de l'utilisateur, donc toutes les données anonymes ne seront pas "rejouées".
{% endalert %}

## Meilleures pratiques

{% détails Examiner les cas d'utilisation pour éviter les dépassements de données. %}

Le segment __ne limite pas__ le nombre d'éléments de données que les clients leur envoyent. Segment vous permet d'envoyer tout ou de décider quels événements vous allez envoyer au Brésil. Plutôt que d'envoyer tous vos événements en utilisant Segment, Nous vous suggérons d'examiner les cas d'utilisation avec vos équipes de marketing et de rédaction pour déterminer quels événements vous allez envoyer à Braze pour éviter les dépassements de données.

{% enddetails %}

{% détails Comprenez la différence entre le point de terminaison personnalisé de l'API et le point de terminaison personnalisé de l'API REST. %}

| Terminologie de Braze           | Segment équivalent                               |
| ------------------------------- | ------------------------------------------------ |
| Point de terminaison SDK Braze  | Point de terminaison de l'API personnalisée      |
| Point de terminaison REST Braze | Point de terminaison de l'API REST personnalisée |
{: .reset-td-br-1 .reset-td-br-2}

Your Braze API Endpoint (called the "Custom API Endpoint" in Segment) is the SDK endpoint that Braze sets up for your SDK (for example, `sdk.iad-03.braze.com`). Votre point de terminaison de l'API REST de Braze (appelé le « point d'extrémité de l'API REST personnalisée » dans Segment) est le point de terminaison de l'API REST (par exemple, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% détails Assurez-vous que le ‘point de terminaison de l'API personnalisée’ est entré dans le segment correctement. %}

| Terminologie de Braze           | Segment équivalent                               |
| ------------------------------- | ------------------------------------------------ |
| Point de terminaison SDK Braze  | Point de terminaison de l'API personnalisée      |
| Point de terminaison REST Braze | Point de terminaison de l'API REST personnalisée |
{: .reset-td-br-1 .reset-td-br-2}

Le format approprié doit être suivi pour vous assurer que vous saisissez votre point de terminaison Braze SDK correctement. Votre point de terminaison Braze SDK ne doit pas inclure `https://` (par exemple, `sdk.iad-03.braze.com`), sinon l'intégration de Braze se brisera. Ceci est requis car le segment ajoute automatiquement votre point de terminaison avec `https://`, ce qui entraîne l'initialisation de Braze avec un point de terminaison invalide `https://sdk.iad-03.braze.com`.

{% enddetails %}

{% détails Certaines données ne correspondent pas au brasier. %}

Segment permet d'utiliser différents types de données et structures, menant à des problèmes où les données ne passeront pas de Segment à Braze comme prévu.

Scénarios où les données ne passeront pas comme prévu:
1. Tableaux ou objets imbriqués dans les propriétés de l'événement.
  - Segment permet de créer des tableaux ou des objets imbriqués dans les propriétés de leurs événements de piste, qui correspondent soit à Braze, soit à l'achat de propriétés d'événement. Puisque nos propriétés ne prennent pas en charge ces types de données, nous rejetterons silencieusement ces appels.
2. Passage du serveur de données anonyme au serveur.
  - Les clients peuvent utiliser les bibliothèques serveur-serveur de Segment pour tromper des données anonymes vers d'autres systèmes.

{% enddetails %}

{% détaille la personnalisation de l'initialisation de Braze. %}

Braze peut être personnalisé de différentes manières : [pousser]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/), [messages dans l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/overview/), [Cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/), et initialisation. Avec une intégration côte à côte, vous pouvez toujours personnaliser les messages push, les messages dans l'application et les cartes de contenu comme vous le feriez avec une intégration directe de Braze.

Cependant, la personnalisation lorsque le SDK de Braze est intégré ou la configuration d'initialisation peut être difficile et parfois impossible. Ceci est dû au fait que le segment initialisera le SDK de Braze pour vous lorsque l'initialisation du segment aura lieu.

{% enddetails %}

[4]: https://segment.com/docs/spec/ecommerce/v2/
[5]: https://segment.com
[18]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-attributes-object-specification
[19]: {{site.baseurl}}/developer_guide/rest_api/user_data/#user-data
[22]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/export_custom_event_data/#custom-event-data
[23]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[24]: {{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula
[24]: {{site.baseurl}}/user_guide/data_and_analytics/creating_a_formula/#creating-a-formula
[25]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/#user-data-collection
[26]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[27]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[36]: https://segment.com/docs/sources/#server
[39]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[39]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[40]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[41]: https://segment.com/docs/spec/identify/#user-id