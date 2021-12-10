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

> [Segment][5]{:target="_blank"} est un concentrateur d'analyse de données qui vous permet de suivre vos utilisateurs et acheminer ces données vers une grande variété de fournisseurs d'analyse utilisateur, comme le Brésil.

Nous offrons [les deux](#integration-options) une intégration de SDK côte à côte pour votre Android, iOS, et les applications web et une intégration de serveur à serveur pour vos services de backend afin que vous puissiez commencer à créer des profils d'utilisateurs plus riches.

Si vous recherchez des informations sur l'intégration des courants avec Segment, reportez-vous à [Segment for Currents]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_for_currents/). Si vous recherchez plus d'informations sur [Segment Personas]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment_personas/), qui vous permet de construire des segments dans Segment et de passer à Braze comme un attribut personnalisé par rapport à un profil utilisateur.

## Aperçu de la configuration

Pour vous lancer dans votre intégration Segment/Braze,
1. Prenez note et préparez-vous à votre intégration en suivant [les exigences et les conditions préalables](#prerequisites).
2. Configurez [Braze comme une Destination](#connection-settings) en accord avec [le type d'intégration que vous avez choisi](#integration-options).
3. Si vous êtes un nouveau client de Braze, vous pouvez relayer des données historiques à Braze en utilisant [Segment Replays](#segment-replays).
4. Configurez [mappings](#methods) pour votre intégration.
5. [Testez votre intégration](#step-3-test-your-integration) pour vous assurer que les données s'écoulent sans heurts entre Braze et Segment.

## Pré-requis

| Exigences                                                  | Origine | Accès                                                                                                                                | Libellé                                                                                                                                                                                                                                                                                                                         |
| ---------------------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Segment Compte & Informations sur le Compte                | Segment | [https://app.segment.com/login](https://app.segment.com/login){:target="_blank"}                                                     | Vous devez avoir un compte de segment actif pour utiliser leurs services avec le Brésil.                                                                                                                                                                                                                                        |
| Bibliothèques de source et de segment de source installées | Segment | [https://segment.com/docs/sources/](https://segment.com/docs/sources/){:target="_blank"}                                             | L'origine de toutes les données envoyées dans Segment, telles que les applications mobiles, les sites Web ou les serveurs d'arrière-plan. <br> <br> Vous devez installer les bibliothèques dans votre application, site, ou serveur avant d'être en mesure de configurer un flux `Source -> Destination` réussi. |
| Intégration de Braze SDK                                   | Brasero | Pour plus de détails concernant les SDK de Braze, veuillez vous référer à notre documentation [iOS][34], [Android][35] et [Web][38]. | Braze doit être installé avec succès sur votre application ou votre site.                                                                                                                                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

## Étape 1 : Configurer les paramètres Braze dans le segment {#connection-settings}

![Paramètres de connexion de destination]({% image_buster /assets/img/segment_destination_braze.png %}){: style="float:right;height:50%;width:50%;margin-left:15px;"} Après avoir configuré avec succès vos intégrations Braze et Segment individuellement, vous devrez configurer [Braze comme une destination depuis le segment](https://segment.com/docs/destinations/){:target="_blank"}. Vous aurez de nombreuses options pour personnaliser le flux de données entre Braze et Segment en utilisant les paramètres de connexion décrits dans le tableau ci-dessous.

| Nom                                      | Libellé                                                                                                                                                                                                                                                     |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| App Identifier                           | Appelée précédemment la clé d'API. Trouvé dans la [Console développeur](https://dashboard.braze.com/app_settings/developer_console) sous l'onglet `Paramètres API`.                                                                                         |
| Clé API REST                             | Précédemment appelé le "Identifiant de groupe d'application". Trouvé dans la [Console développeur](https://dashboard.braze.com/app_settings/developer_console) sous l'onglet `Paramètres API`.                                                              |
| API Endpoint                             | Trouvez et entrez votre [point d'extrémité de Braze SDK]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/) dans notre documentation. <br> <br> Format sans le `https` comme `sdk.iad-01.braze.com`.                     |
| Appboy Datacenter                        | Votre grappe de Braze. Sélectionnez et saisissez votre [Instance Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/) à partir de la liste déroulante.                                                                          |
| Log Achat quand le Revenu est présent    | Choisissez quand enregistrer les achats.                                                                                                                                                                                                                    |
| Point de terminaison de l'API REST Braze | Trouvez et entrez votre [point d'extrémité REST Braze]({{site.baseurl}}/user_guide/administrative/access_braze/braze_instances/) dans notre documentation. Assurez-vous d'inclure le `https` pour qu'il ressemble à `https://rest.iad-01.braze.com`.        |
| ID Push du site Safari                   | Safari nécessite un identifiant Push du site Web pour envoyer push. [Plus d'infos sur ceci ici]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/integration/#step-5-configure-safari-push).                             |
| Version du SDK Web Braze                 | Quelle version du Braze Web SDK vous avez intégré. Vous auriez dû le découvrir lors de votre processus initial d'intégration, mais si vous n'êtes pas sûr, contactez votre responsable de compte ou le support [de Braze]({{site.baseurl}}/braze_support/). |
{: .reset-td-br-1 .reset-td-br-2}

{% détails des paramètres de connexion supplémentaires que vous pouvez voir lors de votre intégration. %}
| Nom                                                               | Options                        | Libellé                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------- | ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Autoriser l'activité Crawler                                      | Activer/Désactiver (True/Faux) | Les Crawlers Web sont des programmes automatiques qui visitent des sites Web, lisent alors et recueillent des informations qui pourraient être importantes pour un indice de moteur de recherche. Vous pouvez autoriser ou interdire cela depuis votre page Web intégrée ou votre application. Braze ne l'autorise pas par défaut. |
| Envoyer automatiquement des messages dans l'application           | Activer/Désactiver (True/Faux) | Braze vous permet automatiquement d'envoyer des messages push à vos utilisateurs lors d'une intégration appropriée.                                                                                                                                                                                                                |
| Ne pas charger la police géniale                                  | Activer/Désactiver (True/Faux) | Braze utilise FontAwesome pour nos icônes de messages dans l'application, mais vous pouvez interdire cette fonctionnalité à tout moment.                                                                                                                                                                                           |
| Activer les messages HTML dans l'application                      | Activer/Désactiver (True/Faux) | Permet aux utilisateurs de la plateforme Braze d'écrire des messages HTML dans l'application. Plus d'informations dans les [Docs JS](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.initialize).                                                                                                                  |
| Activer la journalisation                                         | Activer/Désactiver (True/Faux) | [Connectez-vous par défaut à la console JavaScript](https://js.appboycdn.com/web-sdk/2.0/doc/module-appboy.html#.setLogger).                                                                                                                                                                                                       |
| Intervalle minimum entre les actions de déclenchement en secondes | N'importe quel nombre          | Par défaut, les actions de déclenchement ne se déclencheront que si 30 secondes se sont écoulées depuis la dernière action de déclenchement.                                                                                                                                                                                       |
| Ouvrir les messages dans l'application dans un nouvel onglet      | Activer/Désactiver (True/Faux) | Par défaut, les liens à partir du message dans l'application cliquent charger dans l'onglet actuel ou un nouvel onglet comme spécifié dans la plateforme Braze.                                                                                                                                                                    |
| Ouvrir les fiches de nouvelles dans un nouvel onglet              | Activer/Désactiver (True/Faux) | Par défaut, les liens des cartes de flux d'actualités ou des cartes de contenu se chargent dans l'onglet actuel ou dans un nouvel onglet tel que spécifié dans la plateforme Braze.                                                                                                                                                |
| Expiration de la session en secondes                              | N'importe quel nombre          | Par défaut, les sessions sortent après 30 minutes d'inactivité.                                                                                                                                                                                                                                                                    |
| Suivre toutes les pages                                           | Activer/Désactiver (True/Faux) | Envoie tous les [appels de la page du segment](https://segment.com/docs/spec/page/){:target="_blank"} à Braze en tant qu'événement de la page.                                                                                                                                                                                     |
| Piste uniquement pages nommées                                    | Activer/Désactiver (True/Faux) | Envoie tous les [appels de la page Segment nommée](https://segment.com/docs/spec/page/){:target="_blank"} à Braze                                                                                                                                                                                                                  |
| Mettre à jour uniquement les utilisateurs existants               | Activer/Désactiver (True/Faux) | Cela ne s'applique qu'aux intégrations côté serveur. Ceci détermine si tous les utilisateurs vs les utilisateurs existants seront mis à jour. La valeur par défaut est `false`.                                                                                                                                                    |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
{% enddetails %}

<br>

## Étape 2 : Choisissez le type d'intégration et l'implémentation {#integration-options}

Vous pouvez intégrer les sources Web de Segment (Analytics.js) et les bibliothèques natives côté client avec Braze en utilisant soit une intégration côte à côte ("Device-mode") ou une intégration de serveur-à-serveur ("Cloud-mode").

| Intégration                                                     | Détails du produit                                                                                                                                                        |
| --------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Côte-à-côte / Mode Appareil](#side-by-side-sdk-integration)    | Maps Segment SDK to Braze's, permettant d'accéder à des fonctionnalités plus profondes et une utilisation plus complète de Braze que l'intégration serveur-serveur.       |
| [Serveur à Serveur / Mode Nuage](#server-to-server-integration) | Transfère les données du segment vers le [point de terminaison utilisateur/piste de Braze]({{site.baseurl}}/api/endpoints/user_data?redirected=true#user-track-endpoint). |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Vous pouvez en apprendre plus sur les options d'intégration de segment (Modes de connexion), y compris les avantages de chacun, [ici](https://segment.com/docs/destinations/#connection-modes){:target="_blank"}.
{% endalert %}

### Intégration de SDK côte à côte

Aussi appelée "Mode Périphérique", cette intégration fait correspondre le SDK de Segment et les [méthodes](#methods) à Braze, permettant d'accéder à des fonctionnalités plus profondes et une utilisation plus complète de Braze que l'intégration serveur-serveur.

{% tabs %}
{% tab Android %}

Voir et configurer [mappings](#methods) au SDK de Segment pour [Android](https://github.com/appboy/appboy-segment-android) sur Github de Brase.

Pour compléter l'intégration côte à côte, veuillez vous référer aux instructions détaillées de Segment pour [Android](https://segment.com/docs/connections/destinations/catalog/braze/#android){:target="_blank"}.

{% endtab %}
{% tab iOS %}

Voir et configurer [mappings](#methods) au SDK de Segment pour [iOS](https://github.com/appboy/appboy-segment-ios){:target="_blank"} sur Github de Braze.

Pour compléter l'intégration côte-à-côte, reportez-vous aux instructions détaillées de Segment pour [iOS](https://segment.com/docs/connections/destinations/catalog/braze/#ios){:target="_blank"}.

{% endtab %}
{% tab Web or Javascript %}

Voir et configurer [mappings](#methods) au SDK de Segment pour [Web / Analytics.js (Segment's JavaScript SDK)](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) sur le Github de Braze.

Pour le Web SDK de Braze, [Analyses du segment. s bibliothèque](https://github.com/segmentio/analytics.js-integrations/tree/master/integrations/appboy) intègre et initialise dynamiquement notre SDK Web lorsque vous ajoutez Braze comme destination sur votre tableau de bord Segment. Cependant, pour utiliser les fonctionnalités de notification de navigateur de Braze, veuillez vous référer à la documentation [Web](https://segment.com/docs/connections/destinations/catalog/braze/#web)de Segment {:target="_blank"}.

{% endtab %}
{% endtabs %}

### Intégration du serveur à serveur

Aussi appelé "Cloud-mode", cette intégration transfère les données de Segment à l'API REST de Braze.

Cette intégration est **seule** utilisée en association avec les [bibliothèques côté serveur][36]de Segment, comme leurs SDK Ruby ou Go.

Activez l'intégration en définissant la clé d'API REST de votre [Groupe d'applications][39] et le point de terminaison [REST API Braze][40] de votre centre de données correspondant (cluster) dans votre [Paramètres de connexion sur le tableau de bord du segment](#connection-settings).

Similaire à l'intégration côte à côte, vous devrez mapper les méthodes [du segment](#methods) au Brésil.

Contrairement à l'intégration côte à côte, cependant, l'intégration du serveur à serveur ne prend en charge **ne** aucune des fonctionnalités de l'interface utilisateur de Braze, comme la messagerie intégrée, le fil d'actualités ou les notifications push.

Certaines données [capturées automatiquement][25] ne sont disponibles que via l'intégration côte à côte. Les données suivantes ne sont pas __disponibles via l'intégration serveur-serveur__:
- Sessions
- Première application utilisée
- Dernière application utilisée

#### Activation des notifications push

Actuellement, l'intégration du serveur à serveur de Braze avec le segment __ne supporte pas__ les méthodes pour les jetons push. Afin d'activer les notifications push au Brésil, vous devez importer des jetons push via le [User Attribute Object][18] de notre [User Data][19] REST API. Vous pouvez également compter sur l'intégration [côte à côte](#side-by-side-sdk-integration) pour la capture de jetons push et le mapping.


## Étape 2b: Méthodes de mappage {#methods}

Braze supporte les méthodes [Identifier](https://segment.com/docs/spec/identify/){:target="_blank"}, [Tracer](https://segment.com/docs/spec/track/){:target="_blank"}, et [Page](https://segment.com/docs/connections/sources/catalog/libraries/website/javascript/#page){:target="_blank"} (web) Segment methods; , nos APIs REST vous demandent d'inclure un [ID d'utilisateur][41]{:target="_blank"} lors de ces appels. Braze prend également en charge le mapping d'attributs personnalisés en utilisant la méthode [Group](https://segment.com/docs/spec/group/){:target="_blank"} de Segment.

### Identifier

Lorsque vous [identifiez](https://segment.com/docs/connections/destinations/catalog/braze/#identify){:target="_blank"} un utilisateur, nous enregistrerons des informations pour cet utilisateur avec `userId` comme identifiant d'utilisateur externe.

| Champ Segment    | Champ de Braze   |
| ---------------- | ---------------- |
| `prénom`         | `prénom`         |
| `Nom de famille` | `nom_de famille` |
| `anniversaire`   | `chien`          |
| `avatar`         | `url de l'image` |
| `Ville`          | `ville_domicile` |
| `Pays`           | `Pays`           |
| `Sexe`           | `Sexe`           |
{: .reset-td-br-1 .reset-td-br-2}

Tous les autres traits seront enregistrés en tant qu' [attributs personnalisés][14].

| Méthode de segment                                           | Méthode de Braze                       | Exemple <br> segment `` > `braze`                                                                      |
| ------------------------------------------------------------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| Identifier avec l'identifiant de l'utilisateur               | Définir un ID externe                  | analytics.identify("dawei");    appboy.changeUser("dawei")                                                   |
| S'identifier avec les traits réservés                        | Définir les attributs de l'utilisateur | analytics.identify({email: "dawei@braze.com"});    appboy.getUser().setEmail("dawei@braze.com");             |
| Identifier avec des traits personnalisés                     | Définir les attributs personnalisés    | analytics.identify({fav_cartoon: "Naruto"}); appboy.getUser().setCustomAttribute("fav_cartoon": "Naruto"); |
| Identifier avec l'identifiant et les traits de l'utilisateur | Définir l'ID externe et l'attribut     | Combiner les méthodes ci-dessus.                                                                             |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert important %}
Lorsque vous passez des données d'attribut utilisateur, vérifiez que vous ne passez que des valeurs pour les attributs qui ont changé depuis la dernière mise à jour. Cela vous assurera de ne pas consommer inutilement des points de données vers votre allogue.
{% endalert %}

### Groupes

Lorsque vous appelez le groupe __ dans le segment, nous enregistrerons un attribut personnalisé nommé `ab_segment_group_<groupId>`, où `groupId` est l'ID du groupe dans les paramètres de la méthode. Par exemple, si l'ID du groupe est `1234`, alors le nom de l'attribut personnalisé sera `ab_segment_group_1234`. La valeur de l'attribut personnalisé sera définie à `true`.

### Piste

Lorsque vous _suivez_ un événement, nous enregistrerons cet événement comme un [événement personnalisé][13] en utilisant le nom fourni.

| Méthode de segment                                                               | Méthode de Braze                                                                                                                                 | Exemple <br> segment `` > `braze`                                                                                                                    |
| -------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Track](https://segment.com/docs/spec/track/){:target="_blank"}                  | Connecté en tant qu' [événement personnalisé][13].                                                                                               | `analytics.track("played_game");` > `appboy.logCustomEvent("played_game");`                                                                                |
| [Suivre avec Propriétés](https://segment.com/docs/spec/track/){:target="_blank"} | Connecté en tant que [propriété d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties). | `analytics.track("played_game", {name: "BotW", weapon: "boomerang"});` > `appboy.logCustomEvent("played_game", { "name": "BotW", "weapon": "boomerang"});` |
| [Suivre avec le produit](https://segment.com/docs/spec/track/){:target="_blank"} | Connecté en tant qu' [Événement d'Achat]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/).         | `analytics.track("achat", {products: [product_id: "ab12", price: 19]});` > `appboy.logPurchase("ab12", 19);`                                               |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

#### Commande terminée {#order-completed}

Lorsque vous _suivez_ un événement avec le nom `Commande terminée` en utilisant le format décrit dans [l'API ECommerce][4]{:target="_blank"}, nous enregistrerons les produits que vous avez énumérés comme [achats][28].

### Page {#page}

L'appel [page](https://segment.com/docs/spec/page/){:target="_blank"} vous permet d'enregistrer chaque fois qu'un utilisateur voit une page de votre site web, avec toutes les propriétés optionnelles à propos de la page.

| Méthode de segment                                                            | Méthode de Braze                                  | Exemple <br> segment `` > `braze`                                          |
| ----------------------------------------------------------------------------- | ------------------------------------------------- | -------------------------------------------------------------------------------- |
| [Page](https://segment.com/docs/spec/page/){:target="_blank"} __sans nom__    | Connecté en tant qu' [événement personnalisé][13] | `analytics.page();` >     `appboy.logCustomEvent("Chargé une page");`            |
| [Page](https://segment.com/docs/spec/page/){:target="_blank"} __avec le nom__ | Connecté en tant qu' [événement personnalisé][13] | `analytics.page("Accueil");`    > `appboy.logCustomEvent("Page d'accueil vue");` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Étape 3 : Testez votre intégration

La plupart de vos métriques [Aperçu][27] (sessions à vie, MAU, DAU, adhésivité, Les sessions quotidiennes, et les sessions quotidiennes par MAU) seront vides même si Braze reçoit des données de Segment.

Vous pouvez consulter vos données dans les pages [Événements personnalisés][22] ou [Revenus][28] ou en [créant un segment][23]. La page **Événements Personnalisés** du tableau de bord vous permet de visualiser le nombre d'événements personnalisés au fil du temps. Notez que vous ne serez pas en mesure d'utiliser les formules [][24] qui incluent les statistiques MAU et DAU.

Si vous envoyez des données d'achat à Braze (voir [Commande Terminée](#order-completed)), la page [Revenu][28] vous permet de visualiser des données sur les revenus ou les achats sur des périodes spécifiques ou sur les revenus totaux de votre application.

[La création d'un segment][26] vous permet de filtrer vos utilisateurs en fonction des données d'événement personnalisées et des données d'attributs personnalisés.

{% alert important %}
Si vous utilisez une intégration de serveur à serveur, les filtres liés aux données de session automatiquement collectées (comme "première application utilisée" et "dernière application utilisée") ne fonctionneront pas. Si vous voulez les utiliser dans votre intégration Segment/Braze, utilisez une intégration côte à côte.
{% endalert %}

## Suppression et suppression de l'utilisateur

Si vous avez besoin de supprimer ou supprimer des utilisateurs, Notez que la fonctionnalité de suppression d'utilisateur du segment [est](https://segment.com/docs/privacy/user-deletion-and-suppression/#which-destinations-can-i-send-deletion-requests-to){:target="_blank"} __est__ associée à notre [terminaison Utilisateurs/Supprimer]({{site.baseurl}}/api/endpoints/user_data/#user-delete-endpoint). Veuillez noter que la vérification de ces suppressions peut prendre jusqu'à 30 jours.

Vous devez vous assurer que vous sélectionnez un identifiant utilisateur commun entre Braze et Segment (comme dans l'ID de l'utilisateur ou l'ID externe). Une fois que vous avez initié une demande de suppression avec Segment, vous serez alors en mesure de voir le statut et la façon dont il affecte chacune de vos Destinations.


## Rediffusions de segment

Segment fournit un service aux clients pour "Rejouer" toutes les données historiques à un nouveau partenaire technologique. Les nouveaux clients de Braze qui veulent importer toutes les données historiques pertinentes peuvent le faire par Segment.

Le segment se connectera à notre [point de terminaison des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint) pour importer les données utilisateur dans Braze au nom du client.

{% alert important %}
Si les utilisateurs n'ont pas d'ID externe, ils ne seront pas importés en Brésil. Notre point de terminaison de suivi des utilisateurs nécessite un identifiant utilisateur si un identifiant Braze ou un alias d'utilisateur n'est pas fourni. Actuellement, Segment ne correspond pas à Braze ID de Braze ou à l'alias de l'utilisateur, donc toutes les données anonymes ne seront pas "rejouées".
{% endalert %}

## Meilleures pratiques

{% détails Examiner les cas d'utilisation pour éviter les dépassements de données. %}

Le segment __n'a pas__ de limite sur le nombre d'éléments de données que les clients leur envoyent. Segment vous permet d'envoyer tout ou d'activer les événements que vous allez envoyer à Braze. Plutôt que d'envoyer tous vos événements en utilisant Segment, Nous vous suggérons d'examiner les cas d'utilisation avec vos équipes de marketing et de rédaction pour déterminer quels événements vous allez envoyer à Braze pour éviter les dépassements de données.

{% enddetails %}

{% détails Comprenez la différence entre le « Point de terminaison de l'API personnalisée » vs « Point de terminaison de l'API REST personnalisée ». %}

| Terminologie de Braze           | Équivalent du segment                            |
| ------------------------------- | ------------------------------------------------ |
| Point de terminaison Braze SDK  | Point de terminaison de l'API personnalisée      |
| Point de terminaison REST Braze | Point de terminaison de l'API REST personnalisée |
{: .reset-td-br-1 .reset-td-br-2}

Your Braze API Endpoint (called the "Custom API Endpoint" in Segment) is the SDK endpoint that Braze sets up for your SDK (for example, `sdk.iad-03.braze.com`). Votre point de terminaison de l'API REST de Braze (appelé le « point d'extrémité de l'API REST personnalisée » dans Segment) est le point de terminaison de l'API REST (par exemple, `https://rest.iad-03.braze.com`)
{% enddetails %}

{% details Assurez-vous que le « Point d'extrémité de l'API personnalisée » est entré dans le segment correctement. %}

| Terminologie de Braze           | Équivalent du segment                            |
| ------------------------------- | ------------------------------------------------ |
| Point de terminaison Braze SDK  | Point de terminaison de l'API personnalisée      |
| Point de terminaison REST Braze | Point de terminaison de l'API REST personnalisée |
{: .reset-td-br-1 .reset-td-br-2}

Pour vous assurer que vous saisissez votre point de terminaison Braze SDK correctement, le format approprié doit être respecté. Votre point de terminaison Braze SDK ne doit pas inclure `https://` (par exemple, `sdk.iad-03.braze.com`), sinon l'intégration de Braze se brisera. Ceci est requis car le segment ajoute automatiquement votre point de terminaison avec `https://`, ce qui entraîne l'initialisation de Braze avec un point de terminaison invalide `https://sdk.iad-03.braze.com`.

{% enddetails %}

{% details Assurez-vous que la clé API est correctement saisie. %}

> 'Identifiant de l'application' vs. 'Clé API REST'

Le « Identifiant de l'application» est la clé API trouvée dans la page `Gérer les paramètres` ou `Console développeur` sur le tableau de bord de Braze. Ce champ est nécessaire pour que les intégrations SDK puissent fonctionner. La « clé API REST » est la clé REST API du tableau de bord pour effectuer des appels API. Make sure the key has permission to access `users/track` endpoint.

{% enddetails %}


{% détails Certaines données ne sont pas en correspondance avec le Brésil. %}

Segment permet d'utiliser différents types de données et structures, ce qui peut conduire à des problèmes où les données ne passeront pas de Segment à Braze comme prévu.

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
[13]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-events
[14]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
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
[28]: {{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data
[34]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/
[35]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/
[36]: https://segment.com/docs/sources/#server
[38]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/initial_sdk_setup/
[39]: {{site.baseurl}}/developer_guide/rest_api/basics/#app-group-rest-api-keys
[40]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[41]: https://segment.com/docs/spec/identify/#user-id
