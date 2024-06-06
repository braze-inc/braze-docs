---
nav_title: Notes de version
article_title: Notes de version
page_order: 4
layout: dev_guide
guide_top_header: "Notes de version"
guide_top_text: "C’est là que vous trouverez toutes les mises à jour de la plateforme Braze, avec <a href='/docs/help/release_notes/#most-recent'>les dernières mises à jour de la plateforme</a> suivantes. Vous pouvez également consulter notre <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>Journal de modifications du SDK </a>."
page_type: landing
search_rank: 1
description: "Cette page d’accueil contient les notes de version de Braze. C’est là que vous trouverez toutes les mises à jour de notre plateforme et de nos SDK Braze ainsi que la liste des fonctionnalités retirées."

guide_featured_title: "Notes de version"
guide_featured_list:
  - name: 2023
    link: /docs/help/release_notes/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/help/release_notes/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/help/release_notes/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/help/release_notes/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/help/release_notes/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/help/release_notes/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/help/release_notes/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/help/release_notes/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Obsolescences
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: Journaux de modifications SDK
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Notes de version Braze les plus récentes {#most-recent}

> Braze publie des informations sur les mises à jour du produit à une cadence mensuelle, en s’alignant sur les versions majeures du produit, bien que le produit soit mis à jour avec des améliorations diverses sur une base hebdomadaire.
> <br>
> <br>
> Pour plus d’informations sur les mises à jour listées dans cette section, contactez votre gestionnaire de compte ou [créez un ticket de support][support]. Vous pouvez également consulter [notre Journal de modifications du SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) pour voir plus d’informations sur nos versions, mises à jour et améliorations mensuelles du SDK.

## Version du 4 avril 2023

### Fil d’Ariane de la documentation 
Vous remarquerez peut-être que le site Braze Docs dispose désormais d’un fil d’Ariane en haut de chaque article pour vous montrer où vous vous trouvez sur le site. Il ne s’agit là que d’une autre option pour vous aider à naviguer !

![Un fil d’Ariane de navigation depuis User Guide > Message Building by Channel > In-App Messages > Templates > Simple Survey (Guide de l’utilisateur > Création de messages par canal > Messages in-app > Modèles > Enquête simple)][1]{: style="max-width:55%"}

### Créer des catalogues dans le navigateur
Vous pouvez utiliser des catalogues pour référencer des données non-utilisateurs dans vos campagnes de Braze via Liquid. Braze vous permet désormais de créer un catalogue directement dans votre navigateur au lieu d’importer un fichier CSV. Reportez-vous à la section [Créer un catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog) pour plus d’informations.

### SQL personnalisé dans le générateur de requêtes
Avec le générateur de requêtes, vous pouvez générer des rapports en utilisant les données Braze dans Snowflake. Vous pouvez désormais [utiliser du SQL personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/custom_sql) pour débloquer de nouveaux insights.

{% alert important %}
L’éditeur SQL est en accès anticipé. Si vous souhaitez participer à l’accès anticipé, contactez votre gestionnaire du succès des clients.
{% endalert %}

### FAQ sur les indicateurs de fonctionnalité
Nous avons répondu à quelques [questions fréquemment posées pour les indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/faq).

### Balise Liquid « Message extras » pour Currents
À l’aide de la [balise Liquid `message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras), vous pouvez annoter vos événements d’envoi avec des données dynamiques à partir du Contenu connecté, des attributs personnalisés (tels que la langue, le pays) et des propriétés d’entrée Canvas. Cette balise Liquid ajoute des paires clé-valeur à l’événement d’envoi correspondant dans Currents.

{% alert important %}
Cette balise Liquid est actuellement en version bêta pour les événements d’envoi d’e-mails, de SMS et de notifications push. Contactez votre gestionnaire du succès des clients Braze si vous souhaitez participer à la bêta.
{% endalert %}

### Nouveaux événements Currents : users_campaigns_abort et users_canvas_abort
Deux nouveaux événements ont été ajoutés au glossaire Currents : [événements d’abandon de message Canvas]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#canvas-abort-message-events) et [événements d’abandon de message de campagne]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#campaign-abort-message-events).

### Nouveaux endpoints de l’API : Catalogues
Utilisez les endpoints [Mettre à jour un produit du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item/) et [Mettre à jour des produits du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items/) pour mettre à jour un ou plusieurs produits de votre catalogue.

### Remplissage de l'historique de Shopify
Le [remplissage d’historique Shopify](https://www.braze.com/docs/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_backfill/) permet à Braze d’importer tous les clients, commandes et événements d’achat des 90 jours avant la connexion de l’intégration Shopify.

### WhatsApp
La messagerie WhatsApp est une plateforme de messagerie pair-à-pair populaire utilisée dans le monde entier et qui propose une messagerie basée sur les conversations pour les entreprises. Le [canal de communication WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp) offre un moyen direct d’engager les utilisateurs sur la plateforme WhatsApp par le biais de campagnes, d’abonnements et de désabonnements, de réponses rapides, etc.

#### Objet API WhatsApp
Dans le cadre de la prise en charge de WhatsApp par Braze, l’objet `whats_app` vous permet de modifier ou de créer des messages WhatsApp via nos [endpoints d’envoi de messages]({{site.baseurl}}/api/endpoints/messaging). Voir la [documentation de l’objet `whats_app`]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object) pour la spécification complète.

### Nouveaux partenariats Braze

#### Merkury - Analytique
L'intégration de Braze et [Merkury]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/merkury) vous permet de tirer parti du `MerkuryID` pour augmenter les taux de reconnaissance des visiteurs du site pour les clients Braze.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Cordova 3.0.0](https://github.com/Appboy/appboy-cordova-sdk/blob/3.0.0/CHANGELOG.md)
- [SDK Swift 5.11.1-5.13.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Android 24.3.0](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md)
- [SDK React Native v3.0.0-v4.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [SDK Flutter 4.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Plug-in Expo v1.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [SDK Web 4.7.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## Version du 7 mars 2023

### Suppression de la prise en charge de la duplication des expériences originales Canvas

Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’expérience Canvas d’origine. Braze recommande aux clients qui utilisent l’expérience Canvas d’origine de passer à Canvas Flow. Il s’agit d’une expérience d’édition améliorée permettant de mieux créer et gérer les Canvas. En savoir plus sur le [clonage de vos Canvas en Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).

### Activités en direct pour iOS (accès anticipé)

Les [activités en direct]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/) sont des notifications interactives persistantes affichées sur votre écran de verrouillage, vous permettant de garder un œil sur les choses en temps réel. Comme elles apparaissent sur l’écran de verrouillage, les activités en direct garantissent que vos notifications ne seront pas manquées. Comme elles sont persistantes, vous pouvez afficher du contenu à jour pour vos utilisateurs sans même leur demander de déverrouiller leur téléphone.

{% alert important %}
Les activités en direct sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer.
{% endalert %}

### Création de cartes pour les cartes de contenu

Vous pouvez désormais choisir quand Braze évalue l’éligibilité et la personnalisation de l’audience pour les nouvelles campagnes de cartes de contenu en spécifiant quand la carte est créée.

Les options suivantes sont disponibles :

- **Au lancement de la campagne :** Le comportement par défaut précédent pour les cartes de contenu. Braze calcule l’éligibilité et la personnalisation de l’audience au lancement de la campagne, puis crée la carte et la stocke jusqu’à ce que l’utilisateur ouvre votre application.
- **À la première impression :** Lorsque l’utilisateur ouvre ensuite votre application (c’est-à-dire qu’il démarre une nouvelle session), Braze détermine les cartes de contenu auxquelles l’utilisateur est éligible, modélise les personnalisations telles que le Liquid ou le contenu connecté, puis crée la carte.

Pour plus d’informations, reportez-vous à la section [Création de la carte]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/).

### Réinitialiser les styles pour le message in-app de l’éditeur Drag & Drop

Dans l’éditeur Drag & Drop pour messages in-app, vous pouvez désormais réinitialiser rapidement les styles par défaut après avoir apporté des modifications. Pour plus d’informations, reportez-vous à la [réinitialisation des styles par défaut]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create/#resetting-styles-to-default).

### Domaines personnalisés pour raccourcir les liens

Le raccourcissement de lien vous permet également d’utiliser votre propre domaine pour personnaliser l’apparence de vos URL raccourcies et présenter une image de marque cohérente. Une fois configurés, les [domaines personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#custom-domains) peuvent être attribués à un ou plusieurs groupes d’abonnement SMS.

### Notification push Web Safari Mobile

Safari v16.4 prend en charge les notifications push Web mobiles, ce qui signifie que vous pouvez désormais réengager les utilisateurs mobiles avec des notifications push sur iOS et iPadOS. Suivez notre guide dédié pour connaître les étapes à suivre pour prendre en charge les [notifications push Web sur Safari pour iOS et iPadOS]({{site.baseurl}}/developer_guide/platform_integration_guides/web/push_notifications/safari_mobile_push/).

### Cas d’utilisation des composants de mise à jour utilisateur

Le composant Mise à jour utilisateur dans Canvas vous permet de mettre à jour les attributs, les événements et les achats d’un utilisateur dans un compositeur JSON, mais vous ne savez pas trop comment tirer le meilleur parti de cette fonctionnalité ? Nous avons ajouté [trois exemples de cas d’utilisation]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/#use-cases) pour vous donner quelques idées.

### Recherche d’utilisateur

Ce nouvel article décrit comment utiliser la [recherche d’utilisateur]({{site.baseurl}}/user_guide/engagement_tools/segments/user_lookup) pour rechercher un utilisateur spécifique directement à partir du compositeur afin de vérifier si vos filtres et segments sont correctement configurés. Cela peut également être utile lors de la résolution des problèmes d’une campagne ou d’un Canvas qui n’envoie pas comme prévu : par exemple, si les utilisateurs ne reçoivent pas de message alors qu’ils le devraient.

La recherche d’utilisateur est disponible lors de :

- La création d’un segment
- La configuration d’une campagne ou d’une audience Canvas
- La configuration d’une étape de Parcours d'audience

### Liste d’interdiction ou suppression des données personnalisées

Ce nouvel article décrit comment retirer un objet de données personnalisé en [mettant en liste de blocage ou en supprimant des données personnalisées]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/blocklist_delete_custom_data/).

Vous pouvez occasionnellement identifier des attributs personnalisés, des événements personnalisés ou des événements d’achat qui consomment trop de points de données, sont devenus obsolètes pour votre stratégie marketing ou ont été enregistrés par erreur. Pour empêcher l’envoi de ces données à Braze, vous pouvez bloquer un objet Données personnalisées pendant que votre équipe d’ingénierie travaille à le supprimer du backend de votre application ou de votre site Web.

### Nouveaux partenariats Braze

#### Données Sisu - Aide à la décision

L’intégration de [Sisu Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/business_intelligence/sisu_data/) et Braze vous permet de comprendre dans toutes les campagnes ou au niveau de la campagne pourquoi les indicateurs (par ex., taux d’ouverture, taux de clics, taux de conversion, etc.) changent et ce qui génère les résultats les plus optimaux. Une fois ces segments identifiés, les utilisateurs de Braze peuvent matérialiser les sorties dans leur entrepôt de données ou les envoyer directement de Sisu vers Braze pour recibler et réengager les utilisateurs.

#### Loplat - Emplacement contextuel

L’intégration de Braze et de [loplat]({{site.baseurl}}/partners/message_personalization/location/loplat/) vous permet d’utiliser les services de localisation de loplat (stockage de POI et geofence personnalisé) pour déclencher des campagnes de marketing géocontextuel et créer des événements personnalisés à l’aide de la segmentation hors ligne. Lorsque les utilisateurs visitent l’emplacement ciblé que vous avez défini dans loplat X, les informations de campagne et de localisation sont envoyées immédiatement à Braze.

#### ActionIQ - Plateforme de données client

L’intégration de Braze et [ActionIQ]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/actioniq/) permet aux marques de synchroniser et de mapper leurs données ActionIQ directement dans Braze, ce qui permet de fournir des expériences client extraordinaires basées sur l’ensemble de leurs données client. L’intégration permet aux utilisateurs de :

- Mapper des segments d’audience ou des attributs personnalisés dans Braze directement à partir d’ActionIQ
- Transmettre les événements suivis par ActionIQ vers Braze en temps réel pour déclencher des campagnes personnalisées et ciblées

#### Komo - Contenu dynamique

L’intégration de Braze et [Komo]({{site.baseurl}}/partners/message_personalization/dynamic_content/komo/) vous permet de collecter des données zero et first-party via les hubs d’engagement Komo. Ces hubs sont des microsites dynamiques qui proposent un contenu interactif et des fonctionnalités de gamification. Les données utilisateur collectées à partir de ces hubs sont ensuite transmises à l’API Braze.

- Ingérez en temps réel de données utilisateur zero et first-party collectées depuis Komo vers Braze
- Ingérez des données d’études de marché et de préférences utilisateurs lorsqu’ils répondent à des enquêtes, des sondages et des questionnaires
- Construisez progressivement des profils d’utilisateur dans Braze, car l’utilisateur continue à s’engager et à partager plus de données sur lui-même
- Standardisez l’aspect et la convivialité des e-mails transactionnels envoyés par Braze

#### Phrase - Localisation

L’intégration [Phrase]({{site.baseurl}}/partners/message_personalization/localization/phrase/) et Braze vous permet de traduire des modèles d’e-mails et des blocs de contenu sans quitter l’interface Braze. Grâce à l’intégration TMS Phrase pour Braze, vous pouvez augmenter l’engagement client et stimuler la croissance sur de nouveaux marchés à l’aide d’une localisation harmonieuse.

#### Nift - Fidélité

L’intégration de Braze et [Nift]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/nift/) vous permet de déclencher automatiquement des messages de « remerciements » contenant des cadeaux Nift à des moments clés du cycle de vie du client, ainsi que d’identifier les clients qui ont utilisé leur cadeau. Les cartes-cadeaux Nift peuvent être utilisées pour accéder aux produits et aux services fournis par les marques qui s’appuient sur la technologie de mise en relation de Nift pour acquérir de nouveaux clients de manière rentable et à grande échelle.

#### Sageflo - Modèles de messages

L’intégration Braze et [Sageflo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/sageflo/) permet aux équipes locales d’envoyer facilement leurs propres e-mails à l’aide de modèles, d’images et de segments d’audience approuvés par le marketing via des intégrations API avec Braze.

#### Airbyte - Automatisation des flux de travail

L’intégration de Braze et [Airbyte]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/airbyte/) vous permet de créer un pipeline de données pour collecter et analyser les données de Braze en connectant toutes vos applications et bases de données à un entrepôt central. Une fois ces données collectées dans l’entrepôt, les équipes de données peuvent explorer efficacement les données de Braze en utilisant leurs outils d’aide à la décision préférés.

#### Flywheel - Automatisation des flux de travail

L’intégration de Braze et [Flywheel]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/flywheel/) vous permet de segmenter les données client directement à partir de l’entrepôt de données et de les envoyer à Braze, garantissant ainsi que les utilisateurs peuvent optimiser l’ensemble de fonctionnalités approfondies de Braze en tandem avec une source unique de vérité. Rationalisez les efforts marketing pour la segmentation et l’activation des clients, en réduisant le temps nécessaire pour segmenter, lancer, tester et mesurer les résultats des campagnes ciblées envoyées à Braze.

#### Mozart Data - Automatisation des flux de travail

L’intégration de Braze et [Mozart Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/mozart_data/) vous permet de :

- Utilisez Fivetran pour importer des données Braze dans Snowflake
- Créer des transformations en combinant les données Braze avec d’autres données d’applications et analyser efficacement les comportements des utilisateurs
- Importer des données de Snowflake dans Braze pour créer de nouvelles opportunités d’engagement client
- Combinez les données Braze avec d’autres données d’applications pour obtenir une compréhension plus globale des comportements utilisateur
- Intégrez avec un outil d’aide à la décision pour explorer plus en détail les données stockées dans Snowflake

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Swift 5.10.0-5.11.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Web 4.6.2-4.6.3](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Segment iOS SDK 4.6.1](https://github.com/Appboy/appboy-segment-ios/releases)
- [SDK iOS AppboyKit 4.5.4](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.5.4)
- [React Native SDK 2.0.0-2.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [SDK Xamarin 1.27.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
- [ExpoPlugin 1.0.0-1.1.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
   - Nécessite désormais le SDK React Native de Braze v2.1.0+.
   - Met à jour la version par défaut de Kotlin vers la 1.8.10 pour la compatibilité Expo 48. Cette valeur est remplacée par la propriété `android.kotlinVersion` dans `app.json`.
- [SDK Roku 0.1.3](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)

## Version du 7 février 2023

### Créer des messages accessibles

Le contenu marketing qui exclut les personnes présentant un handicap, même involontairement, peut empêcher des millions de personnes d’interagir avec votre marque. L’accessibilité dans le marketing consiste à faciliter l’utilisation de celui-ci, à recevoir et à comprendre vos communications, et de permettre à tous de s’investir ou de devenir fan de votre produit, service ou marque. Reportez-vous à la section [Créer des messages accessibles dans Braze]({{site.baseurl}}/help/accessibility#building-accessible-messages-in-braze) pour obtenir des conseils.

### Accès anticipé au générateur de requêtes

Avec le [générateur de requêtes]({{site.baseurl}}/user_guide/data_and_analytics/query_builder#query-builder
), vous pouvez générer des rapports en utilisant les données Braze dans Snowflake. Le générateur de requêtes est livré avec des modèles de requête SQL préconstruits pour commencer. Actuellement, seules les requêtes modélisées sont autorisées. La prise en charge des requêtes SQL personnalisées suivra.

Cette fonctionnalité est actuellement disponible en accès anticipé. Si vous souhaitez participer à l’accès anticipé, contactez votre gestionnaire du succès des clients.

### Indicateurs de fonctionnalité version bêta

[Les indicateurs de fonctionnalité]({{site.baseurl}}/developer_guide/platform_wide/feature_flags) vous permettent d’activer ou de désactiver à distance la fonctionnalité d’une sélection d’utilisateurs. Ils vous permettent d’activer et de désactiver une fonctionnalité en production sans déploiement supplémentaire de codes ou mises à jour d’applications. Cela vous permet de déployer de nouvelles fonctionnalités en toute sécurité et en toute confiance.

Cette fonctionnalité est actuellement en version bêta. Si vous souhaitez participer à la phase bêta, contactez votre gestionnaire du succès des clients.

### Nouveaux événements Currents

Les événements Currents suivants ont récemment été publiés et ajoutés aux glossaires [ des événements d’engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) et des [événements utilisateur et de comportement des clients]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events) :

Événements d’interruption de message :
- `users.messages.contentcard.abort`
- `users.messages.email.abort`
- `users.messages.inappmessage.abort`
- `users.messages.newsfeedcard.abort`
- `users.messages.pushnotification.abort`
- `users.messages.sms.abort`
- `users.messages.webhook.abort`

Événements de clic sur lien court SMS :
- `users.messages.sms.ShortLinkClick`

Événement de changement de statut d’abonnement global :
- `users.behaviors.subscription.GlobalStateChange`

Événement de changement de statut du groupe d’abonnement :
- `users.behaviors.subscriptiongroup.StateChange`

Événements de sortie Canvas :
- `users.canvas.exit.PerformedEvent`
- `users.canvas.exit.MatchedAudience`

### Variante personnalisée

Lors de l’envoi d’un test A/B, vous pouvez envoyer aux utilisateurs une variante personnalisée, en leur envoyant la variante avec laquelle ils sont le plus susceptibles de s’engager. Reportez-vous à [Analyse multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant) pour en savoir plus sur la façon dont les variantes personnalisées sont sélectionnées et comment les exploiter dans vos campagnes. 

### Accès anticipé aux SQL Segment Extensions

Les [Segment Extensions]({{site.baseurl}}/sql_segments/) vous permettent de générer un Segment Extension à l’aide des requêtes SQL Snowflake des données Snowflake. Le SQL peut vous aider à déverrouiller de nouveaux cas d’utilisation de segments parce qu’il offre la flexibilité nécessaire pour décrire les relations entre les données de manières qui ne sont pas réalisables par d’autres fonctionnalités de segmentation.

### Liste de contrôle avant et après lancement pour Canvas

Avant et après le lancement d’un Canvas, vous devez vérifier plusieurs détails :
- Assurez-vous que vos envois de messages et heures d’envoi correspondent aux préférences de votre audience
- Tenez compte des différences de fuseaux horaires, de paramètres d’entrée, etc.
- Révisez et ajustez votre Canvas en cas de divergences après le lancement sur la base de ces scénarios

Utilisez cette [liste de contrôle]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist#pre-and-post-launch-checklist) comme guide pour affiner ces domaines en fonction de votre cas d’utilisation pour contribuer à la réussite de votre Canvas. 

### Nouveau endpoint API : Mettre à jour l’alias d’utilisateur

Utilisez l’[endpoint Mettre à jour l’alias d'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) pour mettre à jour les alias d’utilisateur existants.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 4.6.0-4.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#461)
- [SDK Android 24.1.0-24.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2420)
- [SDK iOS AppboyKit 4.5.3](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.5.3)
- [SDK Swift 5.9.0-5.9.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#591)
  - Élève la cible minimale de déploiement vers iOS 11.0 et tvOS 11.0.
  - Élève la version Xcode vers 14.1 (14B47b).
- [SDK Flutter 3.1.0](https://pub.dev/packages/braze_plugin/changelog)
  - Le pont Android natif utilise le SDK Android de Braze 24.2.0.
  - Le pont iOS natif utilise le SDK iOS de Braze 5.9.0.
  - La cible minimale de déploiement iOS est 11.0.
- [SDK Cordova 2.33.0](https://github.com/Appboy/appboy-cordova-sdk/blob/2.33.0/CHANGELOG.md#2330)
  - Migration du plug-in iOS pour utiliser le nouveau SDK Braze Swift (5.8.1).
  - L’IU du Fil d'actualité n’est plus prise en charge sur iOS.

## Version du 10 janvier 2023

### Composant de mise à jour de l’utilisateur pour Canvas Flow

Le composant [User Update (Mise à jour de l’utilisateur)]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) vous permet de mettre à jour les attributs, événements et achats d’un utilisateur dans un éditeur JSON. Il n’est donc pas nécessaire d’inclure des informations sensibles, par exemple des clés API.

### Mettre en place des groupes d’abonnement par API

Lorsque vous créez de nouveaux utilisateurs au moyen de l’endpoint [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), vous pouvez définir des groupes d'abonnement dans l’objet attributs d’utilisateur, ce qui vous permet de créer un utilisateur et de définir l’état du groupe d’abonnement dans un seul appel API.

### Accès anticipé au tableau de bord des conversions

Le [tableau de bord de conversions]({{site.baseurl}}/user_guide/data_and_analytics/analytics/conversions_dashboard/) vous permet d’analyser les conversions entre les campagnes, les Canvas et les canaux en utilisant des méthodes d’attribution différentes. Vous pouvez suivre ces méthodes d’attribution spécifiquement :

- **Conversions d’ouverture :** Les conversions qui se sont produites après qu’un utilisateur a ouvert le message
- **Conversions de clic :** Les conversions qui se sont produites après qu’un utilisateur a cliqué le message
- **Conversions reçues :** Les conversions qui se sont produites après qu’un utilisateur a reçu le message
- **Conversions au dernier clic :** Les conversions qui se sont produites après qu’un utilisateur a cliqué le message, si ce message était le plus récent cliqué par l’utilisateur (cette fonctionnalité est actuellement testée par un petit groupe de clients en accès anticipé)

Cette fonctionnalité est actuellement disponible en accès anticipé. Si vous souhaitez participer à l’accès anticipé, contactez votre gestionnaire du succès des clients.

### Événements de sortie Canvas pour Currents de Braze

Vous pouvez suivre le moment où vos utilisateurs quittent un Canvas en effectuant un événement ou en faisant correspondre une audience. Consultez la section [Événements d’engagement de message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/) dans le Glossaire d’événements Currents pour plus d’informations.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 4.5.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [SDK iOS AppboyKit 4.5.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.5.2)
- [SDK Swift 5.8.0–5.8.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#580)
  - Renomme la classe `BrazeLocation` en `BrazeLocationProvider` pour éviter de mettre dans l’ombre le module du même nom.
- [SDK Flutter 3.0.1](https://pub.dev/packages/braze_plugin/changelog)
- [SDK Android 24.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
  - La fonctionnalité de positionnement et de geofence a été déplacée dans un nouveau module appelé `com.braze:android-sdk-location`.
  - Les classes et les fichiers Appboy ont tous été déplacés vers Braze.
  - Modification du comportement par défaut de `DefaultContentCardsUpdateHandler` pour utiliser la date de création au lieu de la date de dernière mise à jour lors du tri des cartes de contenu.
  - Suppression de BrazeUser.setFacebookData() et BrazeUser.setTwitterData().

## Version du 13 décembre 2022

### Le Fil d’actualité est obsolète
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.

### Nouveaux endpoints de l’API : Catalogues
Utilisez les [endpoints des catalogues API de Braze]({{site.baseurl}}/api/endpoints/catalogs) pour ajouter, éditer et gérer vos [catalogues]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) et vos détails de produits du catalogue. Vous pouvez utiliser des endpoints de catalogue asynchrones pour faire des modifications en gros de votre catalogue.

### Attributs HTML pour les liens dans l’éditeur Drag & Drop pour les e-mails
Vous pouvez maintenant [ajouter des attributs HTML]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#creative-details/) à toute URL des blocs éditeur `Image`, `Button`, or `Text` dans l’éditeur Drag & Drop pour les e-mails. Grâce aux attributs personnalisés, vous pouvez facilement ajouter des informations supplémentaires aux balises HTML dans les e-mails. Ceci peut être particulièrement utile dans le cadre de la personnalisation, de la segmentation et de la mise en page de messages.

### Afficher la bascule Heatmap
Vous pouvez maintenant utiliser la [bascule Show Heatmap (Afficher Heatmap)]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#heatmaps) pour afficher une vue visuelle de vos **analytiques de message** qui montre la fréquence globale et l’emplacement des clics dans la durée de vie de la campagne e-mail. Vous pouvez également télécharger une copie de vos heatmaps pour référence ultérieure.

### Paramètres e-mail mis à jour
L’ancienne section **General Email Settings (Paramètres e-mail globaux)** a été divisée en deux sections : **Sending Configuration (Configuration d’envoi)** et **Subscription Pages and Footers (Pages et pieds de page d’abonnement).** Pour plus d’informations sur les paramétrages individuels, consultez les [paramétrages e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#sending-configuration).

### Générer des images d’IA pour votre bibliothèque multimédia
Vous pouvez générer des images pour votre bibliothèque multimédia en utilisant DALL E 2, un système IA d’OpenAI qui peut créer des images et des représentations artistiques réalistes à partir d’une description en langage naturel. Apprenez-en plus sur [Générer une image en utilisant l’IA]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#generate-ai).

### Améliorations des attributs personnalisés imbriqués
Vous pouvez utiliser des attributs personnalisés imbriqués pour envoyer des objets en tant que nouveau type de données pour des attributs personnalisés.
- Vous pouvez [déclencher lorsqu’un objet d’attribut personnalisé imbriqué est modifié]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#trigger-nested-custom-attribute-changes).
- Vous pouvez maintenant également [personnaliser vos messages en utilisant un objet d’attribut personnalisé et du Liquid]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/#personalization).

### Nouveau bloc vidéo
Un nouveau bloc de contenu pour la [vidéo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/#video) a été ajouté à l’éditeur Drag & Drop pour l’e-mail.

### Identifiant optionnel pour la collection de vendeurs - Swift
Dans les versions antérieures du SDK Swift iOS de Braze, le champ IDFV (identifiant du vendeur) était renseigné automatiquement à partir de l’ID de l’appareil de l’utilisateur. À partir du SDK Swift v5.7.0, le champ IDFV peut être désactivé facultativement et, à la place, Braze générera un UUID aléatoire en tant qu’ID de l’appareil. Pour plus d’informations, consultez [Recueillir les IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/swift_idfv/).

### Comptes Lecture Snowflake
Les comptes Lecture Snowflake donnent accès aux utilisateurs aux mêmes données et fonctionnalités que le [Snowflake Data Sharing (Partage de données Snowflake)]({{site.baseurl}}/partners/snowflake/), sans nécessiter de compte ou de relation client avec Snowflake. Avec les comptes Lecture, Braze créera et partagera vos données dans un compte et vous donnera les identifiants pour vous connecter et accéder à vos données. Tous les partages et facturations de données seront alors gérés intégralement par Braze.

Contactez votre gestionnaire du succès des clients pour en savoir plus.

### Intégration Shopify mise à jour
L’[intégration Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) vous permet maintenant de recueillir les abonnements e-mail et SMS de votre boutique Shopify et de les assigner à un groupe d’abonnements dans Braze.



### Nouveaux partenariats Braze

#### Ada - Sondages
Les intégrations d’[Ada]({{site.baseurl}}/partners/message_orchestration/channel_extensions/surveys/ada/) et de Braze vous permettent d’augmenter les profils d’utilisateurs avec les données collectées à partir de vos conversations automatisées Ada. Vous pouvez définir des attributs utilisateur personnalisés en fonction des informations que vous collectez lors d'un chat Ada et enregistrer des événements personnalisés dans Braze à des moments spécifiés d'une conversation Ada. En connectant votre chatbot Ada à Braze, vous pouvez en savoir plus sur vos consommateurs en fonction des questions qu'ils posent sur votre marque ou en entamant de manière proactive des conversations avec eux avec des questions qui vous permettent d'en savoir plus sur leurs intérêts et leurs préférences.

#### B.Layer - Modèles de messages
L’intégration de [B.Layer]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/blayer) et de Braze vous permet de tirer parti du générateur de messages in-app B.Layer pour vous aider à créer des messages in-app intégrés à la marque qui peuvent être exportés sous forme de fichier zip ou HTML intégré vers Braze. Cette intégration ne nécessite pas de ressources de développement supplémentaires, ce qui vous permet d'économiser du temps et de l'argent.

#### Contentsquare - Analytiques
L’intégration de [Contentsquare]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/contentsquare/) et de Braze vous permet d’envoyer des signaux en direct (fraude, signaux de frustration, etc.) en tant qu’événements personnalisés dans Braze. Tirez parti des insights sur l'expérience Contentsquare pour améliorer la pertinence et les taux de conversion de vos campagnes en ciblant les messages en fonction de l'expérience numérique et du langage corporel de vos clients.

#### Dynamic Yield - Contenu dynamique
Le partenariat entre [Dynamic Yield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/) et Braze vous permet de tirer parti du moteur de recommandations et de segmentations de Dynamic Yield pour créer des blocs d’expérience pouvant être intégrés à des messages Braze. Les blocs d’expérience peuvent être constitués des éléments suivants :
- **Blocs de recommandations** : Définissez des algorithmes et appliquez des filtres au contenu personnalisé des utilisateurs se propageant lors que l’e-mail est ouvert.
- **Blocs de contenu dynamique** : Adaptez les promotions et les messages aux différents utilisateurs ciblés. Le ciblage peut être réalisé en fonction de l’affinité ou de l’audience. Dynamic Yield détermine quelle expérience personnalisée offrir lorsque l’e-mail est ouvert.

#### Octolis - Analytiques
L’intégration d’[Octolis]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/contentsquare/) et de Braze fait office de middleware entre vos sources de données brutes et Braze, ce qui vous permet d’extraire et d’unifier les données provenant de diverses sources en ligne et hors-ligne.

#### Phrasee - Test A/B
[Phrasee React]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/phrasee/phrasee_react/), de Phrasee X, tire profit de Currents Braze et du Contenu connecté pour collecter les informations de suivi des clics de vos utilisateurs abonnés à l’aide de webhooks. Phrasee associe ensuite ces événements à vos variantes de langue pour optimiser la langue en temps réel.

#### Sheetlabs - Contenu dynamique
L’intégration de [Sheetlabs]({{site.baseurl}}/partners/message_personalization/dynamic_content/sheetlabs/) et de Braze vous permet de tirer parti de [Contenu connecté](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) pour inclure les API de Sheetlabs dans vos campagnes de marketing Braze. Cette fonction est généralement utilisée pour faire le lien entre une feuille de calcul Google (qui est mise à jour directement par l'équipe marketing) et les modèles de Braze. Cela vous permet d'obtenir plus de résultats avec les modèles Braze, comme des traductions ou des ensembles plus importants d'attributs personnalisés.

#### Tellius - Analytiques
L’intégration de [Tellius]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/tellius/) et de Braze permet aux utilisateurs d’exploiter les données, sans avoir recours à des ingénieurs BI, pour créer des tableaux de bord et générer des insights afin de prendre de meilleures décisions marketing.

#### ThoughtSpot - Analytiques
L’intégration de [ThoughtSpot]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/thoughtspot/) et de Braze s’appuie sur les ThoughtSpot TML Blocks qui permettent aux utilisateurs de Braze d’accélérer leurs analyses du comportement des utilisateurs grâce à des modèles préétablis de feuilles de travail et de modèles. Cette intégration permet aux utilisateurs d'effectuer des recherches illimitées dans leurs données d'interaction Braze et de découvrir des insights exploitables.

#### Wunderkind - Analytiques
L’intégration de [Wunderkind]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/wunderkind/) et de Braze vous permet d’analyser l’amélioration des performances et d’identifier davantage d’utilisateurs anonymes, en mettant à l’échelle 1 pour 1 de manière significative les messages envoyés via Braze et les contacts ajoutés directement à Braze.


### Mises à jour SDK
Les mises à jour SDK suivantes ont été publiées. Les dernières modifications sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK iOS Swift 5.6.3–5.7.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Flutter 3.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Le pont iOS natif utilise maintenant le [nouveau SDK Swift de Braze, version 5.6.4](https://github.com/braze-inc/braze-swift-sdk). La cible minimale de déploiement pour iOS est 10.0.
    - Durant la migration, mettez à jour votre projet avec les changements suivants :
        - Pour initialiser Braze, [suivez ces étapes d’intégration pour créer un objet de configuration](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/a2-configure-braze). Ajoutez ensuite ce code pour terminer le paramétrage : `let braze = BrazePlugin.initBraze(configuration)`
        - Pour continuer à utiliser `SDWebImage` en tant que dépendance, ajoutez cette ligne au `/ios/Podfile` de votre projet : `pod 'SDWebImage', :modular_headers => true`. Suivez ensuite [ces instructions de configuration](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
        - Pour obtenir de l’aide pour d’autres changements tels que recevoir des messages in-app et des données de carte de contenu, référez-vous à notre exemple de [`AppDelegate.swift`](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift).
- [SDK React Native 1.41.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [SDK Web 4.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

#### Nouvelle bibliothèque SDK : SDK Segment.io Kotlin
Segment.io a mis à jour sa bibliothèque avec une nouvelle approche faisant passer Kotlin en premier et appelée Segment.io Kotlin. Braze vient de sortir une nouvelle bibliothèque pour notre propre travail relatif à ce nouveau paradigme de bibliothèque. Consultez la [version initiale sur GitHub.](https://github.com/braze-inc/braze-segment-kotlin)

## Version du 15 novembre 2022

### Nouvel éditeur Drag & Drop pour messages in-app

Avec le nouvel [éditeur Drag & Drop pour messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop), vous pouvez créer des messages in-app entièrement personnalisés et personnalisés sans avoir besoin de connaître le langage HTML. L’éditeur Drag & Drop sera déployé pour tous les clients au cours des prochains mois. Si vous souhaitez demander un accès plus tôt, contactez votre gestionnaire du succès des clients.

### Mises à jour de l’éditeur Drag & Drop pour les e-mails

#### Nouveaux blocs d’éditeur

Deux nouveaux blocs d’éditeur ont été ajoutés à l’éditeur Drag & Drop pour les e-mails : [Blocs de paragraphe]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/#paragraph) et [Blocs de liste]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_editor_blocks/#list).

{% alert important %}
Le bloc de texte existant est désormais obsolète, mais tous les e-mails existants contenant des blocs de texte continueront d’être pris en charge.
{% endalert %}

#### Aperçu du mode sombre

Lors de la [prévisualisation et du test de vos e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_campaign/#step-3b-preview-and-test-your-message) dans l’éditeur Drag & Drop, vous pouvez désormais activer **l’aperçu du mode sombre** pour voir à quoi ressemble votre e-mail pour les utilisateurs du mode sombre.

### Accès anticipé à Winning Path

Disponible dans le cadre d’Experiment Paths dans Canvas, [Winning Path]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/#step-2-turn-on-winning-path-optional) vous permet d’automatiser vos tests A/B. Lorsque Winning Path est activé, après une période spécifiée, tous les utilisateurs suivants seront envoyés sur le chemin avec le taux de conversion le plus élevé.

Cette fonctionnalité est actuellement disponible en accès anticipé. Si vous souhaitez participer à l’accès anticipé, contactez votre gestionnaire du succès des clients.

### Messages in-app et cartes de contenu pour tvOS

Ce nouvel article couvre les nuances de l’intégration des [messages in-app et des cartes de contenu sur tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/tvos/in-app_messaging), disponibles via le SDK Swift de Braze.

### Nouveau cas d’utilisation de Liquid

Nous avons ajouté un nouveau cas d’utilisation à la [Bibliothèque de cas d’utilisation de Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#misc-personalize-content) concernant la façon d’utiliser le statut d’abonnement d’un client pour personnaliser le contenu des messages. Avec ce cas d’utilisation, les clients abonnés à un groupe d’abonnement spécifique recevront un message exclusif pour les groupes d’abonnement par e-mail et SMS.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Il n’y a pas de mises à jour récentes avec ces versions. Vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 23.3.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2330)
- [SDK Web 4.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#440)
- [SDK Unity 3.11.0](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md#3110)
- [SDK Xamarin 1.26.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#1260)
- [SDK iOS Swift 5.6.0–5.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#562)
- [SDK Flutter 2.6.1](https://pub.dev/packages/braze_plugin/changelog#261)

## Version du 18 octobre 2022

### Historique d’envoi de messages du profil utilisateur

L’onglet **Message History (Historique d’envoi de messages)** du profil utilisateur affiche les événements récents liés à la messagerie (environ 40) pour un utilisateur individuel au cours des 30 derniers jours. Ces événements comprennent les messages que l’utilisateur a envoyés, reçus, avec lesquels il a interagi, etc. Reportez-vous à [Profils utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#messaging-history-tab) pour en savoir plus.

### Blocs de contenu de l’éditeur Drag & Drop

Les blocs de contenu utilisés exclusivement dans l’éditeur Drag & Drop ont des fonctionnalités similaires aux [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) utilisés sur différents canaux. Ils servent d’emplacement centralisé pour la conservation d’informations qui peuvent être référencées dans diverses campagnes par e-mail. Il peut s’agir de regrouper des en-têtes de courriels, des pointeurs promotionnels et plus encore, le tout sur une seule ligne réutilisable.

### ScriptTag Shopify

L’[intégration de Braze et Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify) vous permet désormais d’implanter notre intégration SDK Web via ScriptTag dans votre boutique Shopify. L'implémentation de notre SDK Web via ScriptTag permet de suivre les éléments suivants :
- Suivi des utilisateurs anonymes pour suivre l’activité des clients dans votre magasin
- Suivi des utilisateurs actifs par mois étant donné que le SDK Web est capable de suivre les données de session des visiteurs de votre boutique
- Option pour obtenir les données utilisateur Shopify qui compteront dans votre consommation de point de données
- Option pour activer messages dans le navigateur comme canal sur votre boutique Shopify

### Endpoint SCIM

Utilisez les endpoints SCIM de Braze suivants pour gérer le provisionnement automatisé des utilisateurs :
- [DELETE : supprimer le compte utilisateur de tableau de bord]({{site.baseurl}}/api/endpoints/scim/delete_existing_dashboard_user/)
- [GET : rechercher un compte utilisateur de tableau de bord existant]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information/)
- [POST : créer un nouveau compte utilisateur de tableau de bord]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/)
- [PUT : mettre à jour le compte utilisateur de tableau de bord]({{site.baseurl}}/api/endpoints/scim/put_update_existing_user_account/)

### Désabonnements vagues par SMS

Le [Désabonnement vague]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/fuzzy_opt_out#fuzzy-opt-out) tente de déterminer lorsqu’un message SMS entrant ne correspond pas à un mot-clé de désabonnement, mais en indique l’intention. Si le désabonnement vague est activé et qu’une réponse de mot-clé entrante est considérée comme « vague », Braze répondra automatiquement en demandant à l’utilisateur de confirmer son intention.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK  23.2.0-23.2.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2321)
- [SDK iOS Objective-C 4.5.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#451)
- [SDK iOS Swift 5.5.0S-SDK 5.5.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#550)
- [SDK Cordova 2.31.0](https://github.com/Appboy/appboy-cordova-sdk/blob/master/CHANGELOG.md#2310)
  - Mis à jour vers [SDK Android de Braze 23.0.1](https://github.com/braze-inc/braze-android-sdk/releases/tag/v23.0.1).
- [Unity 3.10.0](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md#3100)
- [SDK React v1.39.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1400)
  - Mise à jour du SDK Android natif vers 23.2.0.
  - Renommer la variable de modèle gradle `kotlin_versio` en `kotlinVersion`
- [SDK Flutter 2.6.0](https://pub.dev/packages/braze_plugin/changelog#260)
  - Le pont Android natif utilise le SDK Android de Braze 23.2.0.
  - Le pont iOS natif utilise le SDK iOS de Braze 4.5.1.
  - `process(inAppMessage)` est renommé en `processInAppMessage(inAppMessage)` dans la couche iOS.
- [Segment iOS 4.6.0](https://github.com/Appboy/appboy-segment-ios/blob/master/CHANGELOG.md#460)
  - Mis à jour pour [le SDK iOS de Braze 4.5.1+](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#451).

## Version du 20 septembre 2022

### Guide de l’API
Consultez le [Guide de l’API Braze]({{site.baseurl}}/docs/api/home) pour rechercher des endpoints en fonction des types d’endpoints, ce qui vous aide à affiner le glossaire.

### Variantes personnalisées
Utilisez des [variantes personnalisées]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#optimizations) pour envoyer à chaque utilisateur de votre segment cible la variante avec laquelle il est le plus susceptible d’interagir.

### Test de Canvas
Après avoir créé votre Canvas, vous pouvez effectuer plusieurs vérifications avant le lancement, en fonction de détails tels que la taille de votre audience ou le nombre de filtres de segmentation. Consultez [Envoyer des Canvas de test]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) pour obtenir des conseils.

### Liquid 5
Pour les utilisateurs de Braze existants, Liquid 5 est généralement disponible. En savoir plus sur les [nouveautés de Liquid 5]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#whats-new-with-liquid-5).

### Nouveaux partenariats Braze

#### Shopify
Braze et [Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) vous permettent de mettre à jour les profils utilisateur existants ou d’en créer de nouveaux dans Braze pour les prospects, les inscriptions et les enregistrements de compte capturés dans votre boutique Shopify.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 23.1.0–23.12](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SDK React Native v1.38.0–v1.38.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
  - Mise à jour du pont Android natif vers le SDK Android de Braze 23.0.1.
  - Mise à jour du pont iOS natif vers le SDK iOS de Braze 4.5.0.
  - Le SDK React Native Android de Braze nécessite désormais directement Kotlin pour la compilation.
- [Plug-in Expo de Braze 0.4.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
  - Renommer la prop `fcmSenderID` en `firebaseCloudMessagingSenderId`.
- [Unity 3.9.0](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md)
  - Mise à jour du plugin Android pour utiliser le SDK Android de Braze 23.1.0.
  - Ajout de la possibilité de demander des autorisations de notification push sur les appareils Android 13+ via`Appboy.AppboyBinding.PromptUserForPushPermissions(false)`.
- [SDK Swift 5.3.0–5.4.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#540)

[support]: {{site.baseurl}}/support_contact/

[1]: {% image_buster /assets/img/doc-breadcrumbs.png %} 

<br><br>
