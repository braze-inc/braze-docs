---
nav_title: Notes de version
article_title: Notes de version
page_order: 4
layout: featured
guide_top_header: "Notes de version"
guide_top_text: "C’est là que vous trouverez toutes les mises à jour de la plateforme Braze, avec <a href='/docs/help/release_notes/#most-recent'>les dernières mises à jour de la plateforme</a> suivantes. Vous pouvez également consulter notre <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>Journal de modifications du SDK </a>."
page_type: landing
search_rank: 1
description: "Cette page d’accueil contient les notes de version de Braze. C’est là que vous trouverez toutes les mises à jour de notre plateforme et de nos SDK Braze ainsi que la liste des fonctionnalités retirées."

guide_featured_title: "Notes de version"
guide_featured_list:
  - name: 2023
    link: /docs/help/release_notes/2023/
    fa_icon: fas fa-calendar-alt
  - name: 2022
    link: /docs/help/release_notes/2022/
    fa_icon: fas fa-calendar-alt
  - name: 2021
    link: /docs/help/release_notes/2021/
    fa_icon: fas fa-calendar-alt
  - name: 2020
    link: /docs/help/release_notes/2020/
    fa_icon: fas fa-calendar-alt
  - name: 2019
    link: /docs/help/release_notes/2019/
    fa_icon: fas fa-calendar-alt
  - name: 2018
    link: /docs/help/release_notes/2018/
    fa_icon: fas fa-calendar-alt
  - name: 2017
    link: /docs/help/release_notes/2017/
    fa_icon: fas fa-calendar-alt
  - name: 2016
    link: /docs/help/release_notes/2016/
    fa_icon: fas fa-calendar-alt
  - name: Obsolescences
    link: /docs/help/release_notes/deprecations/
    fa_icon: far fa-calendar-times
  - name: Journaux de modifications SDK
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    fa_icon: fas fa-file-code

---

# Notes de version Braze les plus récentes {#most-recent}

> Braze publie des informations sur les mises à jour du produit à une cadence mensuelle, en s’alignant sur les versions majeures du produit, bien que le produit soit mis à jour avec des améliorations diverses sur une base hebdomadaire.
> <br>
> <br>
> Pour plus d’informations sur les mises à jour listées dans cette section, contactez votre gestionnaire de compte ou [créez un ticket de support][support]. Vous pouvez également consulter [notre Journal de modifications du SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) pour voir plus d’informations sur nos versions, mises à jour et améliorations mensuelles du SDK.

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

Les événements Currents suivants ont récemment été publiés et ajoutés au [glossaire des événements d’engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) :

Événements d’interruption de message :
- `users_campaigns_abort`
- `users_canvas_abort`
- `users_messages_contentcard_abort`
- `users_messages_email_abort`
- `users_messages_inappmessage_abort`
- `users_messages_newsfeedcard_abort`
- `users_messages_pushnotification_abort`
- `users_messages_sms_abort`
- `users_messages_webhook_abort`

Événements de clic sur lien court SMS :
- `users.messages.sms.ShortLinkClick`

Événement de changement de statut d’abonnement global :
- `users.behaviors.subscription.GlobalStateChange`

Événement de changement de statut du groupe d’abonnement :
- `users.behaviors.subscriptiongroup.StateChange`

Événements de sortie Canvas :
- `users_canvas_exit_PerformedEvent`
- `users_canvas_exit_PerformedEvent_Details`
- `users_canvas_exit_MatchedAudience`
- `users_canvas_exit_MatchedAudience_Details`

### Variante personnalisée

Lors de l’envoi d’un test A/B, vous pouvez envoyer aux utilisateurs une variante personnalisée, en leur envoyant la variante avec laquelle ils sont le plus susceptibles de s’engager. Reportez-vous à [Analyse multivariée]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/multivariate_analytics/#personalized-variant) pour en savoir plus sur la façon dont les variantes personnalisées sont sélectionnées et comment les exploiter dans vos campagnes. 

### Accès anticipé aux SQL Segment Extensions

Les [Segment Extensions]({{site.baseurl}}/sql_segments/) vous permettent de générer un Segment Extension à l’aide des requêtes SQL Snowflake des données Snowflake. Le SQL peut vous aider à déverrouiller de nouveaux cas d’utilisation de segments parce qu’il offre la flexibilité nécessaire pour décrire les relations entre les données de manières qui ne sont pas réalisables par d’autres fonctionnalités de segmentation.

### Liste de contrôle avant et après lancement pour Canvas

Avant et après le lancement d’un Canvas, vous devez vérifier plusieurs détails :
- Assurez-vous que vos messages et heures d’envoi correspondent aux préférences de votre audience.
- Tenez compte des différences de fuseaux horaires, de paramètres d’entrée, etc.
- Révisez et ajustez votre Canvas en cas de divergences après le lancement sur la base de ces scénarios.

Utilisez cette [liste de contrôle]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist#pre-and-post-launch-checklist) comme guide pour affiner ces domaines en fonction de votre cas d’utilisation pour contribuer à la réussite de votre Canvas. 

### Nouveau endpoint API : Mettre à jour l’alias d’utilisateur

Utilisez le [endpoint mettre à jour l’alias d'utilisateur]({{site.baseurl}}/api/endpoints/user_data/post_users_alias_update/) pour mettre à jour les alias d’utilisateur existants.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 4.6.0-4.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#461)
- [SDK Android 24.1.0-24.2.0](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2420)
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
- [SDK iOS AppboyKit 4.5.2](https://github.com/Appboy/appboy-ios-sdk/releases/tag/4.5.2)
- [SDK Swift 5.8.0–5.8.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#580)
  - Renomme la classe `BrazeLocation` en `BrazeLocationProvider` pour éviter de mettre dans l’ombre le module du même nom.
- [SDK Flutter 3.0.1](https://pub.dev/packages/braze_plugin/changelog)
- [SDK Android 24.0.0](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md)
  - La fonctionnalité de positionnement et de geofence a été déplacée dans un nouveau module appelé `com.braze:android-sdk-location`.
  - Les classes et les fichiers Appboy ont tous été déplacés vers Braze.
  - Modification du comportement par défaut de `DefaultContentCardsUpdateHandler` pour utiliser la date de création au lieu de la date de dernière mise à jour lors du tri des cartes de contenu.
  - Suppression de BrazeUser.setFacebookData() et BrazeUser.setTwitterData().

## Version du 13 décembre 2022

### Le Fil d’actualité est obsolète
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.

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
Dans les versions antérieures du SDK Swift iOS de Braze, le champ IDFV (identifiant du vendeur) était renseigné automatiquement à partir de l’ID de l’appareil de l’utilisateur. À partir du SDK Swift v5.7.0, le champ IDFV peut être désactivé facultativement et, à la place, Braze générera un UUID aléatoire en tant qu’ID de l’appareil. Pour plus d’informations, consultez [Recueillir les IDFV]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/other_sdk_customizations/swift_idfv/).

### Comptes Lecture Snowflake
Les comptes Lecture Snowflake donnent accès aux utilisateurs aux mêmes données et fonctionnalités que le [Snowflake Data Sharing]({{site.baseurl}}/partners/snowflake/) (Partage de données Snowflake), sans nécessiter de compte ou de relation client avec Snowflake. Avec les comptes Lecture, Braze créera et partagera vos données dans un compte et vous donnera les identifiants pour vous connecter et accéder à vos données. Tous les partages et facturations de données seront alors gérés intégralement par Braze.

Contactez votre gestionnaire du succès des clients pour en savoir plus.

### Intégration Shopify mise à jour
L’[intégration Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) vous permet maintenant de recueillir les abonnements e-mail et SMS de votre boutique Shopify et de les assigner à un groupe d’abonnements dans Braze.



### Nouveaux partenariats Braze

#### Ada - Sondages
Les intégrations d’[Ada]({{site.baseurl}}/partners/message_orchestration/channel_extensions/surveys/ada/) et de Braze vous permettent d'augmenter les profils d'utilisateurs avec les données collectées à partir de vos conversations automatisées Ada. Vous pouvez définir des attributs utilisateur personnalisés en fonction des informations que vous collectez lors d'un chat Ada et enregistrer des événements personnalisés dans Braze à des moments spécifiés d'une conversation Ada. En connectant votre chatbot Ada à Braze, vous pouvez en savoir plus sur vos consommateurs en fonction des questions qu'ils posent sur votre marque ou en entamant de manière proactive des conversations avec eux avec des questions qui vous permettent d'en savoir plus sur leurs intérêts et leurs préférences.

#### B.Layer - Modèles de messages
L'intégration de [B.Layer]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/blayer) et de Braze vous permet de tirer parti du générateur de messages in-app B.Layer pour vous aider à créer des messages in-app intégrés à la marque qui peuvent être exportés sous forme de fichier zip ou HTML intégré vers Braze. Cette intégration ne nécessite pas de ressources de développement supplémentaires, ce qui vous permet d'économiser du temps et de l'argent.

#### Contentsquare - Analytiques
L'intégration de [Contentsquare]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/contentsquare/) et de Braze vous permet d'envoyer des signaux en direct (fraude, signaux de frustration, etc.) en tant qu'événements personnalisés dans Braze. Tirez parti des insights sur l'expérience Contentsquare pour améliorer la pertinence et les taux de conversion de vos campagnes en ciblant les messages en fonction de l'expérience numérique et du langage corporel de vos clients.

#### Dynamic Yield - Contenu dynamique
Le partenariat entre [Dynamic Yield]({{site.baseurl}}/partners/message_personalization/dynamic_content/dynamic_yield/) et Braze vous permet de tirer parti du moteur de recommandations et de segmentations de Dynamic Yield pour créer des blocs d’expérience pouvant être intégrés à des messages Braze. Les blocs d’expérience peuvent être constitués des éléments suivants :
- **Blocs de recommandations** : Définissez des algorithmes et appliquez des filtres au contenu personnalisé des utilisateurs se propageant lors que l’e-mail est ouvert.
- **Blocs de contenu dynamique** : Adaptez les promotions et les messages aux différents utilisateurs ciblés. Le ciblage peut être réalisé en fonction de l’affinité ou de l’audience. Dynamic Yield détermine quelle expérience personnalisée offrir lorsque l’e-mail est ouvert.

#### Octolis - Analytiques
L’intégration d’[Octolis]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/contentsquare/) et de Braze fait office de middleware entre vos sources de données brutes et Braze, ce qui vous permet d’extraire et d’unifier les données provenant de diverses sources en ligne et hors-ligne.

#### Phrasee - Test A/B
[Phrasee React]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/phrasee/phrasee_react/), de Phrasee X, tire profit de Currents Braze et du Contenu connecté pour collecter les informations de suivi des clics de vos utilisateurs abonnés à l’aide de webhooks. Phrasee associe ensuite ces événements à vos variantes de langue pour optimiser la langue en temps réel.

#### Sheetlabs - Contenu dynamique
L'intégration de [Sheetlabs]({{site.baseurl}}/partners/message_personalization/dynamic_content/sheetlabs/) et de Braze vous permet de tirer parti de [Contenu connecté](https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) pour inclure les API de Sheetlabs dans vos campagnes de marketing Braze. Cette fonction est généralement utilisée pour faire le lien entre une feuille de calcul Google (qui est mise à jour directement par l'équipe marketing) et les modèles de Braze. Cela vous permet d'obtenir plus de résultats avec les modèles Braze, comme des traductions ou des ensembles plus importants d'attributs personnalisés.

#### Tellius - Analytiques
L'intégration de [Tellius]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/tellius/) et de Braze permet aux utilisateurs d'exploiter les données, sans avoir recours à des ingénieurs BI, pour créer des tableaux de bord et générer des insights afin de prendre de meilleures décisions marketing.

#### ThoughtSpot - Analytiques
L'intégration de [ThoughtSpot]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/thoughtspot/) et de Braze s'appuie sur les ThoughtSpot TML Blocks qui permettent aux utilisateurs de Braze d'accélérer leurs analyses du comportement des utilisateurs grâce à des modèles préétablis de feuilles de travail et de modèles. Cette intégration permet aux utilisateurs d'effectuer des recherches illimitées dans leurs données d'interaction Braze et de découvrir des insights exploitables.

#### Wunderkind - Analytiques
L'intégration de [Wunderkind]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/wunderkind/) et de Braze vous permet d'analyser l’amélioration des performances et d'identifier davantage d'utilisateurs anonymes, en mettant à l'échelle 1 pour 1 de manière significative les messages envoyés via Braze et les contacts ajoutés directement à Braze.


### Mises à jour SDK
Les mises à jour SDK suivantes ont été publiées. Les dernières modifications sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK iOS Swift 5.6.3–5.7.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Flutter 3.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Le pont iOS natif utilise maintenant le [nouveau SDK Swift de Braze, version 5.6.4](https://github.com/braze-inc/braze-swift-sdk).The La cible minimale de déploiement pour iOS est 10.0.
    - Durant la migration, mettez à jour votre projet avec les changements suivants :
        - Pour initialiser Braze, [suivez ces étapes d’intégration pour créer un objet Configuration](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/a2-configure-braze). Ajoutez ensuite ce code pour terminer la configuration : `let braze = BrazePlugin.initBraze(configuration)`
        - Pour continuer à utiliser `SDWebImage` en tant que dépendance, ajoutez cette ligne au `/ios/Podfile` de votre projet : `pod 'SDWebImage', :modular_headers => true`. Suivez ensuite [ces instructions de configuration](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
        - Pour obtenir de l’aide pour d’autres changements tels que recevoir des messages in-app et des données de carte de contenu, référez-vous à notre [`AppDelegate.swift`](https://github.com/braze-inc/braze-flutter-sdk/blob/master/example/ios/Runner/AppDelegate.swift). proposé en échantillon.
- [SDK React Native 1.41.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [SDK Web 4.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

#### Nouvelle bibliothèque SDK : SDK Segment.io Kotlin
Segment.io a mis à jour sa bibliothèque avec une nouvelle approche faisant passer Kotlin en premier et appelée Segment.io Kotlin. Braze vient de sortir une nouvelle bibliothèque pour notre propre travail relatif à ce nouveau paradigme de bibliothèque. Consultez la [version initiale sur GitHub](https://github.com/braze-inc/braze-segment-kotlin)

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

- [SDK Android 23.3.0](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2330)
- [SDK Web 4.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#440)
- [SDK Unity 3.11.0](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md#3110)
- [SDK Xamarin 1.26.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#1260)
- [SDK iOS Swift 5.6.0–5.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#562)
- [SDK Flutter 2.6.1](https://pub.dev/packages/braze_plugin/changelog#261)

## Version du 18 octobre 2022

### Historique d’envoi de messages du profil utilisateur

L’onglet **Message History (Historique d’envoi de messages)** du profil utilisateur affiche les événements récents liés à la messagerie (environ 40) pour un utilisateur individuel au cours des 30 derniers jours. Ces événements comprennent les messages que l’utilisateur a envoyés, reçus, avec lesquels il a interagi, etc. Reportez-vous à [Profils utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#messaging-history-tab) pour en savoir plus.

### Blocs de contenu de l’éditeur Drag & Drop

Les blocs de contenu utilisés exclusivement dans l’éditeur Drag & Drop ont des fonctionnalités similaires aux [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) utilisés sur différents canaux. Ils servent d’emplacement centralisé pour la conservation d’informations qui peuvent être référencées dans diverses campagnes par e-mail. Il peut s’agir de regrouper des en-têtes de courriels, des pointeurs promotionnelles et plus encore, le tout sur une seule ligne réutilisable.

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

- [SDK  23.2.0-23.2.1](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2321)
- [SDK iOS Objective-C 4.5.1](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#451)
- [SDK iOS Swift 5.5.0S-SDK 5.5.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#550)
- [SDK Cordova 2.31.0](https://github.com/Appboy/appboy-cordova-sdk/blob/master/CHANGELOG.md#2310)
  - Mis à jour vers [SDK Android de Braze 23.0.1](https://github.com/Appboy/appboy-android-sdk/releases/tag/v23.0.1).
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
Braze et [Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) vous permettent de mettre à jour les profils utilisateurs existants ou d’en créer de nouveaux dans Braze pour les prospects, les inscriptions et les enregistrements de compte capturés dans votre boutique Shopify.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 23.1.0–23.12](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md)
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

## Version du 23 août 2022

### Portail développeur

Connectez-vous, apprenez et inspirez-vous des autres développeurs qui bâtissent avec Braze. Consultez notre [portail développeur](https://www.braze.com/dev-portal) et rejoignez la communauté des développeurs Braze sur Slack.

### Archivage des messages

La fonctionnalité additionnelle [Archivage des messages]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/) vous permet d’enregistrer une copie des messages envoyés aux utilisateurs à des fins d’archivage ou de conformité dans votre compartiment S3.

### Propriétés d’entrée et propriétés de l’événement Canvas

Bien que leur nom soit similaire, les propriétés d’entrée et les propriétés de l’événement Canvas fonctionnent différemment dans vos flux de travail Canvas. En savoir plus sur le moment d’utilisation de chaque propriété et les différences de comportement dans les [propriétés d’entrée et les propriétés de l’événement Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties).

### Alias de liens suivis

Vous pouvez désormais afficher tous les alias de lien que vous suivez dans vos e-mails depuis **Manage Settings** > **Email Settings** > **Link Aliasing Settings (Gérer les paramètres > Paramètres e-mail > Paramètres d’aliasage de lien)**. Consultez les [Liens de suivi]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#tracking-links) pour plus d’informations.

### Liquid 5

Braze a mis à jour sa prise en charge de Liquid jusqu’au et y compris **Liquid 5 de Shopify**. Pour les nouveaux utilisateurs de Braze, Liquid 5 est généralement disponible. Pour les utilisateurs Braze existants, Liquid 5 est en accès anticipé. En savoir plus sur les [nouveautés de Liquid 5]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#whats-new-with-liquid-5).

### Bonnes pratiques relatives aux campagnes et à Canvas

La création de campagnes et de Canvas réussis peut être complexe, alors consultez notre liste de bonnes pratiques à connaître pour tirer le meilleur parti de vos envois de messages.

- [Bonnes pratiques relatives aux campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/best_practices/)
- [Bonnes pratiques relatives à Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/best_practices/)

### Recherche de campagnes

Saviez-vous que vous pouvez rechercher une campagne en utilisant son identifiant API ? En savoir plus à ce sujet et sur d’autres façons de filtrer et de trouver des campagnes dans [Rechercher des campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/).

### Nouveaux partenariats Braze

#### IAM Studio - Modèles de messages

Avec l’intégration Braze et [IAM Studio]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/), vous pouvez facilement insérer des modèles de messages in-app personnalisables dans vos messages in-app Braze, proposant le remplacement d’image, la modification de texte, les paramètres de lien profond, les attributs personnalisés et les paramètres d’événement. Grâce à IAM Studio, vous pouvez réduire le temps de production des messages et consacrer plus de temps à la planification du contenu.

#### actionable.me - Analytique

L’intégration Braze et [actionable.me]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/actionableme/) vous permet de déployer un service vous permettant de suivre vos progrès dans l’utilisation de Braze. Grâce à une combinaison d’outils et de processus, ils évalueront rapidement vos performances CRM, identifieront de nouvelles opportunités et fourniront des recommandations sur la façon d’améliorer vos performances.

#### Storyly - Importation de la cohorte

L’intégration Braze et [Storyly]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/storyly/) vous permet d’utiliser vos segments dans Braze en tant qu’audience sur la plateforme Storyly. Grâce à cette intégration, vous pouvez :

- Ciblez vos segments avec du contenu spécifique
- Utilisez les attributs des utilisateurs pour personnaliser le contenu de vos articles

#### Lokalise - Localisation

L’intégration Braze et [Lokalise]({{site.baseurl}}/partners/message_personalization/localization/lokalise/) exploite le contenu connecté pour vous permettre d’insérer facilement du contenu traduit dans vos campagnes Braze en fonction des paramètres de langue de l’utilisateur.

#### Quikly - Reciblage

Le partenariat Braze et [Quikly]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/quikly/) vous permet d’accélérer les conversions sur les événements au sein d’un parcours client Braze. Pour ce faire, Quikly utilise la psychologie de l'urgence pour motiver les consommateurs de manière amusante et instantanée. Par exemple, les marques peuvent utiliser Quikly pour acquérir immédiatement de nouveaux utilisateurs abonnés par e-mail et SMS directement dans Braze ou pour motiver d'autres objectifs marketing clés comme le téléchargement de votre application mobile.

#### DataGrail - Confidentialité et conformité des données

L’intégration Braze et [DataGrail]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/datagrail/) vous permet de détecter les données des consommateurs collectées et stockées dans Braze pour traiter rapidement les DSR (demandes d’accès, de suppression et de non-vente). Braze sera ajouté à un plan précis de l'emplacement des données des consommateurs dans votre organisation avec un mappage automatisé des données. Plus besoin d'enquêtes ou de feuilles de calcul pour maintenir un cadre de confidentialité ou produire un enregistrement des activités de traitement (RoPA).

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 4.2.0–4.2.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#421)
- [iOS 4.5.0](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#450) (Objective-C)
- [iOS Swift 5.1.0–5.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#520)
- [Android 23.0.0–23.0.1](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2301)
    - `BaseContentCardView.bindViewHolder()` prend désormais `Card` au lieu du type générique.

[support]: {{site.baseurl}}/support_contact/

<br><br>
