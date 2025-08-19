---
nav_title: Aperçu de l’intégration
article_title: Aperçu de l’intégration
page_order: 2
description: "Cet article donne un aperçu du processus d'onboarding."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}Démarrage : Présentation de l’intégration

> Cet article donne un aperçu du processus d'onboarding.

![Un diagramme de Venn de quatre cercles - découverte, intégration, assurance qualité et maintenance - centré sur le "time to value".]({% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}){: style="max-width:50%;float:right;margin-left:15px;border:none;"} 

En tant que ressource technique, vous donnerez à votre équipe les moyens d'agir en intégrant Braze dans votre pile technologique. L'onboarding se divise globalement en quatre étapes :
* [Découverte et planification](#discovery): Travaillez avec votre équipe pour vous aligner sur la portée, planifier une structure pour les données et les campagnes, et créer une structure d'espace de travail appropriée. 
* [Intégration](#integration) : Exécutez votre plan en intégrant le SDK et l'API, en activant les canaux de communication et en configurant l'importation et l'exportation des données. 
* [Assurance qualité](#qa) : Confirmez que la boucle de données et d'envoi de messages entre la plateforme Braze et votre app ou site fonctionne comme prévu.
* [Entretien](#maintenance): Une fois que vous aurez transmis Braze à votre équipe marketing, vous continuerez à veiller à ce que tout se passe bien.

<br>
{% alert tip %}
Nous sommes conscients que chaque organisation a des besoins distincts, et Braze est créé pour répondre à une gamme variée d'options de personnalisation qui peuvent être adaptées à vos exigences spécifiques. Les délais d'intégration varient en fonction de votre cas d'utilisation. 
{% endalert %}

## Découverte et planification {#discovery}

Au cours de cette phase, vous travaillerez avec votre équipe pour définir les tâches d'onboarding et veiller à ce que toutes les parties prenantes s'alignent sur un objectif commun. 

Votre équipe effectuera une planification de bout en bout de vos cas d'utilisation pour s'assurer que tout peut être créé comme prévu, avec les bonnes données disponibles pour le faire. Cette phase inclut votre chef de projet, votre responsable CRM, l'ingénierie frontale et back-end, les propriétaires de produits et les marketeurs. 

La phase de découverte et de planification dure en moyenne six semaines. Les responsables de l'ingénierie peuvent s'attendre à passer de 2 à 4 heures par semaine au cours de cette phase. Les développeurs qui travaillent avec le produit peuvent s'attendre à passer 10 à 20 heures par semaine sur Braze pendant la phase de découverte et de planification. 

{% alert tip %}
Pendant la période d'onboarding de votre entreprise, Braze organisera des séances de présentation technique. Nous recommandons vivement aux ingénieurs de participer à ces sessions. Les sessions de présentation technique vous donnent l'occasion d’aborder l'évolutivité de l'architecture de la plateforme et de voir des exemples pratiques de la façon dont certaines entreprises de votre taille ont précédemment réussi avec des cas d'utilisation similaires.
{% endalert %}

![Icônes pour différents canaux, tels que l'e-mail, le panier d'achat, les images, la géolocalisation, etc.]({% image_buster /assets/img/getting-started/data-graphic-2.png %}){: style="max-width:40%;float:right;margin-left:15px;"} 

### Planification de la campagne

Votre équipe CRM planifiera les cas d'utilisation des communications que vous lancerez dans un avenir proche. Ceci inclut les éléments suivants :
* [Canal]({{site.baseurl}}/user_guide/message_building_by_channel) (par exemple, notifications push ou messages in-app).
* [Méthode de réception/distribution]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types) (par exemple, livraison planifiée ou livraison par événement)
* [Audience cible]({{site.baseurl}}/user_guide/engagement_tools/segments)
* [Indicateurs de réussite]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)

Par exemple, une campagne destinée aux nouveaux clients pourrait consister en un e-mail envoyé tous les jours à 10 heures à un segment de clients qui ont enregistré leur première session hier. L'événement de conversion (indicateur de réussite) consiste à enregistrer une session.

<br>
{% alert important %}
L'intégration ne peut pas commencer tant que l'étape de planification de la campagne n'est pas terminée. Cette étape permettra de déterminer quelles parties et pièces de Braze doivent être configurées au cours de la phase d'intégration.
{% endalert %}

### Créer des exigences en matière de données

Ensuite, votre équipe CRM doit définir les données nécessaires pour lancer les campagnes qu'elle a planifiées, en créant des exigences en matière de données. 

De nombreux types courants d'attributs utilisateur, tels que le nom, l'e-mail, la date de naissance, le pays et autres, font automatiquement l’objet d’un suivi après l'intégration du SDK Braze. Les autres types de données devront être définis comme des données personnalisées.

En tant que développeur, vous travaillerez avec votre équipe pour définir les données supplémentaires et personnalisées qu'il serait judicieux de suivre. Vos données personnalisées auront un impact sur la façon dont votre base d'utilisateurs sera classée et segmentée. Vous mettrez en place une taxonomie d'événements à travers votre outil de croissance, en structurant vos données de manière à ce qu'elles soient compatibles avec vos systèmes lorsqu'elles entrent et sortent de Braze.

{% alert tip %}
Veillez à ce que la nomenclature des données soit cohérente d'un outil à l'autre. Par exemple, votre entrepôt de données peut enregistrer « offre d’achat à durée limitée » d'une manière particulière. Vous devrez décider si un événement personnalisé est nécessaire dans Braze pour correspondre à ce format.
{% endalert %}

En savoir plus sur les [données collectées automatiquement et les données personnalisées]({{site.baseurl}}/developer_guide/analytics/).

### Planification des personnalisations

Discutez avec vos marketeurs des personnalisations qu'ils souhaitent. Par exemple, souhaitez-vous implémenter les cartes de contenu par défaut de Braze ? Souhaitez-vous modifier légèrement leur apparence pour qu'elles correspondent à votre charte graphique ? Voulez-vous développer une toute nouvelle interface utilisateur pour un composant et faire en sorte que Braze suive son analyse/analytique ? Différents niveaux de personnalisation nécessitent différents niveaux de portée.

### Obtenir l'accès au tableau de bord

Le tableau de bord de Braze constitue notre interface utilisateur sur le Web. Les marketeurs utiliseront le tableau de bord pour faire leur travail et créer du contenu. Les développeurs peuvent utiliser le tableau de bord pour gérer les paramètres d’intégration des applications, comme les clés API et les informations d’identification de notifications push.

L'administrateur de votre équipe doit vous ajouter (ainsi que tous les autres membres de l'équipe qui ont besoin d'accéder à Braze) en tant qu'utilisateurs sur votre tableau de bord.

### Espaces de travail et clés API

L'administrateur de votre équipe créera également différents [espaces de travail]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/). Les espaces de travail regroupent vos données (utilisateurs, segments, clés API) en un seul emplacement/localisation. Nous vous conseillons de ne regrouper que les différentes versions d'une même application ou d'applications très similaires au sein d'un même espace de travail. 

Fait important, les espaces de travail fournissent des clés API pour plusieurs plateformes (comme iOS et Android). Vous utiliserez les clés API corrélées pour associer les données du SDK à un espace de travail particulier. Naviguez vers vos espaces de travail pour accéder à la clé API de chacune de vos applications. Assurez-vous que chaque clé API dispose des autorisations nécessaires pour effectuer le travail que vous avez défini. Pour plus de détails, consultez l'[article sur le provisionnement de l'API pour]({{site.baseurl}}/api/basics/#rest-api-key).

{% alert important %}
Il est important que vous mettiez en place des environnements différents pour le développement et la production. La mise en place d'un environnement de test vous évitera de dépenser de l'argent réel lors de l'onboarding et de l'assurance qualité. Pour créer un environnement de test, configurez un espace de travail de test et veillez à utiliser sa clé API afin de ne pas alimenter votre espace de travail de production avec des données de test.
{% endalert %}  

## Intégration {#integration}

![Graphique pyramidal abstrait conseillant le flux d'informations d'une source de données à un appareil d'utilisateur.]({% image_buster /assets/img/getting-started/data-graphic.png %}){: style="max-width:45%;float:right;margin-left:15px;"} 

Braze prend en charge les applis iOS, les applis Android, les applis Web, et bien plus encore. Vous pouvez également opter pour l'utilisation d'un SDK wrapper multiplateforme, comme React Native ou Unity. En règle générale, les clients intègrent le système en 1 à 6 semaines. De nombreux clients ont intégré Braze avec un seul ingénieur, en fonction de l'étendue de ses compétences techniques et de la bande passante. Cela dépend entièrement de votre périmètre d'intégration spécifique et du temps que votre équipe consacre au projet Braze. 

Vous aurez besoin de développeurs capables de :
* Travailler dans la couche native de votre application ou de votre site
* Créer des processus pour utiliser notre API REST
* Tests d'intégration 
* Authentification par jeton web JSON
* Compétences générales en matière de gestion des données
* Configuration des enregistrements DNS

### Partenaires d'intégration de la CDP

De nombreux clients profitent de l'onboarding de Braze pour réaliser également une intégration avec une plateforme de données client (CDP) en tant que partenaire d'intégration. Braze assure le suivi et l'analyse des données, tandis qu'un CDP peut fournir un acheminement et une orchestration supplémentaires des données. Braze offre une intégration fluide/sans heurts avec de nombreux CDP, tels que [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle/) et [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment/). 

Si vous effectuez une intégration côte à côte avec un CDP, vous mapperez les appels du SDK de votre CDP vers le SDK de Braze. Globalement, vous devrez :
* Mappez les appels d'identification sur `changeUser` [(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)) et définissez les attributs.
* Appels de flux de données cartographiques vers `requestImmediateDataFlush` [(Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush()), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush()), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush)).
* Enregistrer les événements personnalisés ou les achats.

Des exemples d'intégration entre le SDK de Braze et la CDP de votre choix peuvent être disponibles, en fonction de la plateforme que vous avez choisie. Pour plus d’informations, consultez notre [liste de partenaires technologiques de CDP]({{site.baseurl}}/partners/data_and_analytics/). 

### Intégration SDK de Braze

Le SDK de Braze fournit deux fonctionnalités essentielles : il collecte et synchronise les données des utilisateurs dans un profil utilisateur consolidé, et alimente les canaux d'envoi de messages tels que les notifications push, les messages in-app et les cartes de contenu. 

{% alert tip %}
Lorsqu'il est entièrement intégré à votre application ou à votre site, le SDK de Braze offre un niveau de sophistication marketing entièrement réalisé. Si vous différez l'intégration du SDK de Braze, certaines des fonctionnalités décrites dans la documentation ne seront pas disponibles.
{% endalert %}

Au cours de l’implémentation du SDK :

* Rédigez un code d'intégration SDK pour chaque plateforme que vous souhaitez prendre en charge.
* Activez les canaux d'envoi de messages pour chaque plateforme, en veillant à ce que le SDK de Braze suive les données issues de vos interactions avec vos clients par e-mail, SMS, notifications push et autres canaux.
* Créez toutes les personnalisations prévues pour les composants de l'interface utilisateur (par exemple, les cartes de contenu personnalisées). Pour un contenu entièrement personnalisé, vous devrez enregistrer les analyses, étant donné que la collecte automatique des données du SDK n’aura pas connaissance de vos nouveaux composants. Vous pouvez reproduire cette implémentation sur nos composants par défaut.

### Utiliser l'API de Braze

Vous utiliserez notre API REST pour différentes tâches à différents moments de votre utilisation de Braze. L'API de Braze est utile pour :

1. l'importation de données historiques ; et
2. Des mises à jour continues qui ne sont pas déclenchées dans Braze. Par exemple, un profil utilisateur passe au niveau VIP sans qu'il se connecte à une application, l'API doit donc communiquer cette information à Braze.

Commencez à utiliser l'[API de Braze]({{site.baseurl}}/api/basics).

{% alert important %}
Lorsque vous utilisez l'API, veillez à grouper vos demandes et à n'envoyer que des valeurs delta. Braze réécrit chaque attribut envoyé. Ne mettez pas à jour un attribut personnalisé si sa valeur n'a pas changé.
{% endalert %}

### Mise en place d'une analyse des produits

Braze est une plateforme orientée données. Les données dans Braze sont stockées sur le profil utilisateur. 

Les points de données constituent une structure qui vous permet de vous assurer que vous capturez les bonnes données pour vos marketeurs, et pas seulement « n'importe quelle » donnée que vous avez la possibilité d’aspirer. Familiarisez-vous avec les [points de données]({{site.baseurl}}/user_guide/data/data_points/).

### Migration des données utilisateur existantes

Vous pouvez utiliser le logiciel Braze [`/users/track endpoint`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) pour migrer des données historiques qui ont été enregistrées en dehors de Braze. Les jetons de notification push et les achats passés sont des exemples de données couramment importées. Cet endpoint peut être utilisé pour des importations ponctuelles ou des mises à jour régulières par lots. 

Vous pouvez également importer des utilisateurs et mettre à jour les valeurs des attributs personnalisés en chargeant une seule fois un [fichier CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-a-csv) dans le tableau de bord. Le chargement de fichiers CSV peut être utile pour les marketeurs, tandis que notre API REST permet une plus grande flexibilité.

### Mise en place d'un suivi de session

Le SDK Braze génère des points de données « session ouverte » et « session fermée ». Le SDK Braze efface également les données à intervalles réguliers. Consultez ces liens pour connaître les valeurs par défaut du suivi de session, qui peuvent toutes être personnalisées[(Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=swift), [web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions/?tab=web)).

### Suivi des événements personnalisés, des attributs et des événements d'achat

Coordonnez avec votre équipe la mise en place de votre schéma de données planifié, y compris les événements personnalisés, les attributs utilisateurs et les événements d'achat. Votre [schéma de données personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_events/) sera saisi à l'aide du tableau de bord et doit correspondre exactement à ce que vous avez mis en œuvre lors de l'intégration SDK.

{% alert tip %}
Les ID des utilisateurs, appelés `external_id`dans Braze, doivent être définis pour tous les utilisateurs connus. Ces éléments doivent être immuables et accessibles lorsque l'utilisateur ouvre l'application, vous permettant de suivre vos utilisateurs sur différents appareils et plateformes. Consultez l'article sur le [cycle de vie de l'utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/) pour connaître les meilleures pratiques.
{% endalert %}

### Autres outils

En fonction de votre cas d'utilisation, il se peut que vous ayez besoin de mettre en place d'autres outils. Par exemple, vous pourriez avoir besoin de configurer un outil comme les [géorepérages]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/) pour mettre en place vos témoignages d'utilisateurs. Nous avons constaté que les clients qui ont la possibilité de configurer ces outils supplémentaires après avoir effectué les étapes essentielles de l'intégration sont ceux qui réussissent le mieux.

## Assurance qualité {#qa}
Au fur et à mesure de l'exécution de votre intégration, vous fournirez une assurance qualité afin de vous assurer que tout ce que vous mettez en place fonctionne comme prévu. Cette assurance qualité se divise en deux catégories générales : l'ingestion de données et les canaux de communication.

{% alert important %}
Assurez-vous que vos environnements de production et de test sont configurés avant de commencer l'assurance qualité.
{% endalert %}

| **Ingestion de données pour l'assurance qualité**  | **Envoi de messages pour l'assurance qualité**                                              |
|---------------------------|---------------------------------------------------------------|
| Vous assurerez la qualité de l'ingestion, du stockage et de l'exportation des données. | Vous vous assurerez que vos messages sont envoyés correctement à vos utilisateurs et que tout se présente bien. |
| Effectuez des tests pour confirmer que les données sont stockées correctement. | Créez des segmentations d'utilisateurs. |
| Confirmez que les données de la session sont correctement attribuées à l'espace de travail prévu dans Braze. | Lancez des campagnes et des canevas avec succès. |
| Confirmez que les débuts et les fins de session sont enregistrés. | Confirmez que les bonnes campagnes sont diffusées aux bons segments d'utilisateurs. |
| Confirmez que les informations relatives aux attributs des utilisateurs sont correctement enregistrées dans les profils utilisateurs. | Confirmez que les jetons de notification push sont correctement enregistrés. |
| Testez que les données personnalisées sont correctement enregistrées par rapport aux profils utilisateurs. | Confirmez que les jetons de poussée sont correctement retirés. |
| Créez des profils utilisateurs anonymes. | Testez que les campagnes push sont correctement envoyées aux appareils et que l'engagement est enregistré. |
| Confirmez que les profils utilisateurs anonymes deviennent des profils utilisateurs connus lorsque la méthode `changeUser()` est appelée. | Testez que les messages in-app sont envoyés et que les indicateurs sont enregistrés. |
|                           | Vérifier que les cartes de contenu sont distribuées et que les indicateurs sont enregistrés. |
|                           | Faciliter le contenu connecté (par exemple, Accuweather). |
|                           | Confirmez que toutes les intégrations des canaux de communication fonctionnent correctement. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert note %}
Lors de l'assurance qualité de votre intégration SDK, utilisez le [débogueur SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) pour résoudre les problèmes sans avoir à activer l'enregistrement des données pour votre application.
{% endalert %}

### Transmission de Braze aux marketeurs

Une fois que vous avez intégré votre plateforme ou votre site, vous devriez impliquer votre équipe marketing pour lui transmettre la propriété de la plateforme. Ce processus est différent d'une entreprise à l'autre, mais il peut comprendre les éléments suivants :

* Composer une [logique liquide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid) complexe
* Faciliter le [réchauffement d'adresses IP des e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)
* S'assurer que les autres parties prenantes comprennent le type de données qui font l'objet d'un suivi

### Développer pour l'avenir

Vous est-il déjà arrivé d'hériter d'une base de code et de n'avoir aucune idée de ce à quoi pensait le développeur initial ? Pire encore, avez-vous déjà écrit du code, l'avez compris parfaitement, puis vous êtes senti complètement déconcerté lorsque vous y êtes revenu un an plus tard ? 

Lors de l'onboarding de Braze, les décisions collectives que vous prenez concernant les données, les profils utilisateurs, les intégrations qui étaient ou non dans le champ d'application, la façon dont les personnalisations sont censées fonctionner, et plus encore, vous sembleront fraîches dans votre esprit et donc évidentes. Lorsque votre équipe souhaite développer Braze ou lorsque d'autres ressources techniques sont affectées à votre projet Braze, ces informations seront masquées.

Créez une ressource pour cimenter les informations que vous avez apprises au cours de vos séances de présentation technique. Cette ressource vous aidera à réduire le temps nécessaire à l'onboarding des nouveaux développeurs qui rejoignent votre équipe (ou vous servira d'aide-mémoire lorsque vous devrez étendre votre implémentation actuelle de Braze). 

## Maintenance {#maintenance}

Après le transfert à vos marketeurs, vous continuerez à servir de ressource pour la maintenance. Vous serez attentif aux mises à jour d'iOS et d'Android susceptibles d'avoir un impact sur le SDK Braze et vous vous assurerez que vos fournisseurs tiers sont à jour. 

Vous assurerez le suivi des mises à jour de la plateforme Braze via le [référentiel GitHub](https://github.com/braze-inc/) de Braze. Occasionnellement, votre administrateur recevra également des e-mails concernant des mises à jour urgentes et des corrections de bogues directement de Braze. 

## Limites de débit du SDK 

### Utilisateurs actifs par mois CY 24-25 

Pour les clients qui ont acheté Utilisateurs actifs mensuels - CY 24-25, Braze applique des limites de débit côté serveur sur les requêtes API utilisées par nos SDK pour mettre à jour les sessions, les attributs utilisateurs, les événements et d'autres données de profil utilisateur. Ceci afin d'assurer la stabilité de la plateforme et de maintenir un service rapide et fiable. 

* Les limites de débit horaire sont fixées en fonction du trafic SDK prévu sur votre compte, qui peut correspondre au nombre d'utilisateurs actifs mensuels (MAU) que vous avez acheté, au secteur d'activité, à la saisonnalité ou à d'autres facteurs. Lorsque la limite de débit horaire est atteinte, Braze étrangle les demandes jusqu'à l'heure suivante.
* Toutes les demandes à débit limité sont automatiquement relancées par le SDK.
* Les demandes de SDK sont en corrélation avec la quantité de données personnalisées collectées dans le cadre de votre mise en œuvre. Si vous êtes constamment proche ou à la limite de votre débit horaire, réfléchissez :
    * Révision de l'intégration SDK afin de réduire la collecte excessive de données.
    * Bloquer les données personnalisées qui ne sont pas essentielles pour vos cas d'utilisation marketing.
* Les limites de débit en rafale sont des limites de débit de courte durée qui s'appliquent lorsqu'un volume important de demandes arrive dans un laps de temps très court (c'est-à-dire en l'espace de quelques secondes). Vous n'avez pas besoin d'agir lorsque des limites de rafales se produisent, et le SDK réessayera peu de temps après.

### Trouver vos limites de débit

Pour connaître les limites actuelles basées sur le débit attendu du SDK, allez dans **Paramètres** > **API et identifiants** > **Limites API et SDK**.

Pour connaître l'historique de l'utilisation, allez dans **Paramètres** > **API et identifiants** > **Tableau de bord API et SDK**.

### Changements et soutien

Braze peut modifier les limites de débit afin de protéger la stabilité du système ou de permettre une augmentation du débit de données sur votre compte. Contactez l'assistance Braze ou votre gestionnaire satisfaction client pour toute question ou préoccupation concernant les limites de débit et leur impact sur votre entreprise.
