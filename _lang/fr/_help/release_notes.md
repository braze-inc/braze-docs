---
nav_title: Notes de version
article_title: Notes de version
page_order: 4
layout: featured
guide_top_header: "Notes de version"
guide_top_text: "C’est là que vous trouverez toutes les mises à jour de la plateforme Braze, avec <a href='/docs/help/release_notes/#most-recent'>les dernières mises à jour de la plateforme</a> suivantes. Vous pouvez également consulter notre <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>Journal de modifications du SDK </a>."
page_type: landing
description: "Cette page d’accueil contient les notes de version de Braze. C’est là que vous trouverez toutes les mises à jour de notre plateforme et de nos SDK ainsi que la liste des fonctionnalités retirées."

guide_featured_title: "Notes de version"
guide_featured_list:
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
- [SDK Xamarin 1.26.0](https://github.com/Appboy/appboy-xamarin-bindings/blob/master/CHANGELOG.md#1260)
- [SDK iOS Swift 5.6.0–5.6.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#562)
- [SDK Flutter 2.6.1](https://pub.dev/packages/braze_plugin/changelog#261)

## Version du 18 octobre 2022

### Historique d’envoi de messages du profil utilisateur

L’onglet **Message History (Historique d’envoi de messages)** du profil utilisateur affiche les événements récents liés à la messagerie (environ 40) pour un utilisateur individuel au cours des 30 derniers jours. Ces événements comprennent les messages que l’utilisateur a envoyés, reçus, avec lesquels il a interagi, etc. Reportez-vous à [Profils utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#messaging-history-tab) pour en savoir plus. 

### Blocs de contenu de l’éditeur Drag & Drop

Les blocs de contenu utilisés exclusivement dans l’éditeur Drag & Drop ont des fonctionnalités similaires aux [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) utilisés sur différents canaux. Ils servent d’emplacement centralisé pour la conservation d’informations qui peuvent être référencées dans diverses campagnes par e-mail. Il peut s’agir de regrouper des en-têtes de courriels, des pointeurs promotionnelles et plus encore, le tout sur une seule ligne réutilisable.

### ScriptTag Shopify

L’[intégration de Braze et Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify) vous permet désormais d’implanter notre intégration SDK Web via ScriptTag dans votre boutique Shopify. L’intégration de notre SDK Web via ScriptTag prend en charge le suivi des éléments suivants :
- Suivi anonyme des utilisateurs pour suivre l’activité des clients dans votre magasin
- Suivi des utilisateurs actifs par mois : le SDK Web est capable de suivre les données de session des visiteurs de votre boutique
- Option de collecte des activités sur le site de Shopify des utilisateurs qui compteront dans votre consommation de point de données
- Option pour autoriser l’implémentation des messages dans le navigateur comme canal sur votre boutique Shopify

### Endpoint SCIM

Utilisez les endpoints SCIM de Braze suivants pour gérer le provisionnement automatisé des utilisateurs :
- [DELETE: Supprimer le compte utilisateur de tableau de bord]({{site.baseurl}}/api/endpoints/scim/delete_existing_dashboard_user/)
- [GET: Rechercher un compte utilisateur de tableau de bord existant]({{site.baseurl}}/api/endpoints/scim/get_see_user_account_information/)
- [POST: Créer un nouveau compte utilisateur de tableau de bord]({{site.baseurl}}/api/endpoints/scim/post_create_user_account/)
- [PUT: Mettre à jour le compte utilisateur de tableau de bord]({{site.baseurl}}/api/endpoints/scim/put_update_existing_user_account/)

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
- [SDK React v1.39.0](https://github.com/Appboy/appboy-react-sdk/blob/master/CHANGELOG.md#1400)
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

La fonction additionnelle [Archivage des messages]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/message_archiving/) vous permet d’enregistrer une copie des messages envoyés aux utilisateurs à des fins d’archivage ou de conformité dans votre compartiment S3.

### Propriétés d’entrée et propriétés de l’événement Canvas

Bien que leur nom soit similaire, les propriétés d’entrée et les propriétés de l’événement Canvas fonctionnent différemment dans vos flux de travail Canvas. En savoir plus sur le moment d’utilisation de chaque propriété et les différences de comportement dans les [propriétés d’entrée et les propriétés de l’événement Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties).

### Alias de liens suivis

Vous pouvez désormais afficher tous les alias de lien que vous suivez dans vos e-mails depuis **Manage Settings** > **Email Settings** > **Link Aliasing Settings** (Gérer les paramètres > Paramètres e-mail > Paramètres d’aliasage de lien). Consultez les [Liens de suivi]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/#tracking-links) pour plus d’informations.

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
- Utilisez les attributs utilisateur pour personnaliser le contenu de votre histoire

#### Lokalise - Localisation

L’intégration Braze et [Lokalise]({{site.baseurl}}/partners/message_personalization/localization/lokalise/) exploite le contenu connecté pour vous permettre d’insérer facilement du contenu traduit dans vos campagnes Braze en fonction des paramètres de langue de l’utilisateur.

#### Quikly - Reciblage

Le partenariat Braze et [Quikly]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/quikly/) vous permet d’accélérer les conversions sur les événements au sein d’un parcours client Braze. Quikly y parvient en utilisant la psychologie basée sur l’urgence pour motiver les consommateurs de manière amusante et instantanée. Par exemple, les marques peuvent utiliser Quikly pour acquérir immédiatement de nouveaux utilisateurs abonnés aux e-mails et SMS directement dans Braze ou pour motiver d’autres objectifs marketing clés comme le téléchargement de votre application mobile.

#### DataGrail - Confidentialité et conformité des données

L’intégration Braze et [DataGrail]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/datagrail/) vous permet de détecter les données des consommateurs collectées et stockées dans Braze pour traiter rapidement les DSR (demandes d’accès, de suppression et de non-vente). Braze sera ajouté à un plan précis de l’emplacement des données des consommateurs dans votre organisation avec un mappage automatisé des données : plus besoin d’enquêtes ou de feuilles de calcul pour maintenir un cadre de confidentialité ou produire un enregistrement des activités de traitement (RoPA).

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 4.2.0–4.2.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#421)
- [iOS 4.5.0](https://github.com/Appboy/appboy-ios-sdk/blob/master/CHANGELOG.md#450) (Objective-C)
- [iOS Swift 5.1.0–5.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#520)
- [Android 23.0.0–23.0.1](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2301)
    - `BaseContentCardView.bindViewHolder()` prend désormais `Card` au lieu du type générique.

## Version du 26 juillet 2022

### Canvas Flow
La dernière version du produit Canvas, [Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#editing-a-step) est sortie. Avec Canvas Flow, vous avez accès à des [composants Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components) légers, des [propriétés d’entrées persistantes]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_persistent_entry_properties/), et [d’édition après lancement]({{site.baseurl}}/post-launch_edits).

![]({% image_buster /assets/img/canvas_flow.png %})

### Tableau d’objets
Utilisez un [ensemble d’objets]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/array_of_objects#array-of-objects) pour regrouper des attributs associés. Vous pouvez, par exemple, avoir un groupe d’objets « animaux de compagnie », un groupe d’objets « chansons » et un groupe d’objets « Compte » pour le même utilisateur. Ces array d’objets peuvent être utilisées pour personnaliser votre message avec Liquid, ou segmenter votre audience si un élément d’un objet correspond aux critères.

### Intégrations partenaires mises à jour
[Amplitude Recommend]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/amplitude/amplitude_recommend/) et [mParticle]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle/) ont désormais des étapes d’intégration mises à jour. Si vous choisissez d’utiliser ces partenaires, consultez leur documentation pour vous assurer que vous avez suivi la configuration la plus récente. 

### Exigences Shopify
- Les autorisations utilisateur requises répertoriées sous [les conditions préalables]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/#prerequisites) ont été mises à jour. 
- Les exemples de [charges utiles]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/#supported-shopify-events) Shopify qui incluent les propriétés `price`, `total_price`, `total_discounts` et `amount` ont été mis à jour pour formater ces propriétés sous forme de nombres au lieu de chaînes de caractères.

### Mises à jour des prédictions
La fenêtre de temps maximale pour les prédictions d’attrition et les prédictions d’achat est passée de 14 jours à 60 jours.  

### Mises à jour SDK
Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants. 
- [SDK Web 4.1.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#410)
- [SDK Cordova 2.30.1](https://github.com/Appboy/appboy-cordova-sdk/blob/master/CHANGELOG.md#2301)
- [SDK Unity 3.8.1](https://github.com/Appboy/appboy-unity-sdk/blob/master/CHANGELOG.md#381)
- [SDK Swift 5.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#501)
- [SDK Roku 0.1.2](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md#012)
- [SDK React Native 1.37.0](https://github.com/Appboy/appboy-react-sdk/blob/master/CHANGELOG.md#1370)
  - Le SDK React Native de Braze exporte désormais son objet par défaut en tant que module ES. Si vous importez actuellement le SDK à l’aide de `require()`, vous devrez maintenant l’importer en tant que module ES standard (par exemple, importer Braze à partir de "`react-native-appboy-sdk`").
- [SDK Android 22.0.0](https://github.com/Appboy/appboy-android-sdk/blob/master/CHANGELOG.md#2200)
  - `Appboy.java` est désormais `Braze.kt`. Les clients Kotlin devront mettre à jour leur code pour prendre en charge l’utilisation des propriétés Kotlin sur le singleton Braze si nécessaire.
    - `Braze.registerPushToken()`/`Braze.getRegisteredPushToken()` est désormais `Braze.setRegisteredPushToken()/Braze.getRegisteredPushToken()`. Si vous utilisez Kotlin, utilisez la propriété `Braze.registeredPushToken`.
    - `Braze.getDeviceId` est désormais simplement `Braze.deviceId` pour Kotlin.
    - `Braze.enableMockNetworkAppboyRequestsAndDropEventsMode` est désormais `Braze.enableMockNetworkRequestsAndDropEventsMode()`.
    - `Appboy.java` a été supprimé. Par exemple, les appels du type `Appboy.getInstance()` devront devenir `Braze.getInstance()` dans l’avenir.
    - Remplacé `setCustomAppboyNotificationFactory()` par `setCustomBrazeNotificationFactory()` / `customBrazeNotificationFactory`.
    - Renommé `enableMockAppboyNetworkRequestsAndDropEventsMode` par `enableMockNetworkRequestsAndDropEventsMode`.
  - Déplacé `com.appboy.IBrazeEndpointProvider` vers `com.braze.IBrazeEndpointProvider`.
  - Renommé `com.appboy.events.IEventSubscriber` par `com.braze.events.IEventSubscriber`.
  - Supprimé `Appboy.registerAppboyPushMessages()` / `Appboy.getAppboyPushMessageRegistrationId()`. Remplacé avec `getRegisteredPushToken()` / `setRegisteredPushToken()`.
  - Remplacé `IAppboyNotificationFactory` par `IBrazeNotificationFactory`.
  - Supprimé `com.appboy.ui.inappmessage.listeners.IHtmlInAppMessageActionListener`. Utilisez `com.braze.ui.inappmessage.listeners.IHtmlInAppMessageActionListener` à la place.

## Version du 28 juin 2022

### Validation de livraison pour les Étapes de message Canvas

Vous pouvez activer les validations de livraison dans vos [Étapes de message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) Canvas, pour mettre en place une vérification supplémentaire et confirmer que votre public répond aux critères de livraison pour l’envoi du message. Ce paramètre est recommandé si les options Heures calmes, Timing Intelligent ou Limitation du taux sont activées.

### Guide de mise à niveau du SDK pour Android 13

Android 13 a atteint son [jalon de stabilité de la plateforme](https://developer.android.com/about/versions/13/overview#platform_stability) le 8 juin 2022. Toutes les modifications ont donc été finalisées et les utilisateurs d’applications pourront bientôt mettre à niveau leurs périphériques. Pour en savoir plus sur les modifications pertinentes introduites dans Android 13 et sur les étapes de mise à niveau requises pour l’intégration SDK Braze pour Android, consultez notre [Guide de mise à niveau du SDK pour Android 13]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/).

### Guide de mise à jour SDK iOS 16

À partir d’iOS 16 Bêta 2 (22 juin 2022), aucune modification fonctionnelle ayant affecté votre intégration SDK Braze n’a été apportée à iOS 16. Cela peut changer, car Apple publie de nouvelles versions bêta d’iOS 16, donc nous recommandons de vérifier régulièrement notre [Guide de mise à niveau du SDK pour iOS 16]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_16/), qui décrit les modifications pertinentes introduites dans iOS 16.

### Être sûr avant d’envoyer : Guide pour les canaux

Lancez vos campagnes et Canvas en toute confiance ! Après avoir consulté notre Guide de prélancement, consultez [Être sûr avant d’envoyer : canaux]({{site.baseurl}}/help/help_articles/campaigns_and_canvas/know_before_send/) pour une liste finale des vérifications ou « pièges » pour les cartes de contenu, les e-mails, les messages In-App, les notifications push et les SMS.

### Comment les noms d’attributs et les ID des campagnes/Canvas diffèrent entre les sources

Les noms et ID de campagne, Canvas et Canvas Step sont tous disponibles dans Liquid, notre API REST et Currents. Ces attributs correspondent à la même valeur dans les trois sources, mais ils peuvent avoir des noms différents. Ce [nouvel article d’aide]({{site.baseurl}}/help/help_articles/api/attribute_name_id_across_sources/) vous aidera à vous y retrouver.

### Braze Learning

[Braze Learning](https://learning.braze.com/), anciennement Learning at Braze (LAB), propose des cours sur les concepts clés et les principes fondamentaux de Braze pour les marketeurs, les administrateurs et les développeurs. Guettez le logo Braze Learning sur certains articles, puis cliquez sur le lien pour en savoir plus sur le sujet en question.

![Logo d’apprentissage Braze sur l’article des attributs personnalisés, qui vous amène au cours d’apprentissage Braze sur les attributs personnalisés]({% image_buster /assets/img_archive/release_notes_brazelearning.png %})

## Version du 31 mai 2022

### Inbox Vision

Avec Inbox Vision, vous pouvez vérifier que vos campagnes d’e-mail en glisser-déposer sont cohérentes sur tous vos clients de messagerie et plateformes mobiles avant de les envoyer. Pour en savoir plus, consultez [Inbox Vision]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/).

### Moteur HTML mis à jour

Le moteur sous-jacent qui produit HTML à partir de l’éditeur Drag & Drop a été optimisé et mis à jour pour améliorer la compression et le rendu du fichier HTML. Pour plus de détails sur les mises à jour, consultez [Moteur HTML mis à jour]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#updated-html-engine/).

### Mise à jour des mots-clés de ciblage spécifique à la catégorie

Vous pouvez créer jusqu’à 25 de vos propres catégories de mots-clés SMS, ce qui vous permet d’identifier les mots-clés et réponses arbitraires pour les utiliser à des fins de filtrage et de reciblage. Pour en savoir plus sur les catégories de mots-clés SMS et comment les configurer, consultez notre article [Reciblage SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/). 

### Segmentation des propriétés de l’événement

L’[Event property segmentation]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/#event-property-segmentation/) (Segmentation des propriétés de l’événement) vous permet de cibler les utilisateurs en fonction de leurs événements personnalisés, mais aussi en fonction des propriétés associées à ces événements. Cette fonction ajoute des options de filtrage supplémentaires lors de la segmentation des achats et des événements personnalisés.

### Synchronisation du public avec Google

Le processus de synchronisation de l’audience de Braze vers Google a été simplifié, et Braze peut désormais accéder à plusieurs comptes Google Ads. Pour plus d’informations, consultez [Synchronisation de public avec Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/). 

### Nouveaux partenariats Braze

#### Amperity - Plateforme de données client

L’intégration entre Braze et [Amperity]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/amperity/) fournit une vue unifiée de vos clients sur les deux plateformes. Grâce à cette intégration, vous pouvez synchroniser les listes d’utilisateurs en mappant les données utilisateur Amity vers les comptes utilisateur Braze via la création d’une liste d’utilisateurs Amity. 

#### Dynamic 365 Customer Insights - Plateforme de données client

L’intégration entre Braze et [Dynamics 365 Customer Insights]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/dynamics_365_customer_insights/) vous permet d’exporter des segments de clients vers Braze pour les utiliser dans des campagnes ou des Canvas.

#### Extole - Fidélisation

Avec l’intégration entre Braze et [Extole]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/extole/), vous pouvez transférer dans Braze les événements et les attributs des clients provenant des programmes Extole de parrainage et de croissance, ce qui vous permet de créer des campagnes de marketing plus personnalisées qui stimulent l’acquisition, l’engagement et la fidélité des clients. Vous pouvez également extraire dynamiquement des attributs de contenu Extole, tels que des codes de partage et des liens personnalisés, dans les communications de Braze.

#### Heap - Importation de la cohorte

L’intégration entre Braze et [Heap]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/heap/) vous permet d’importer des données de Heap vers Braze, de créer des cohortes d’utilisateurs et d’exporter des données de Braze vers Heap pour créer des segments.

#### Hightouch - Automatisation du flux de travail

L’intégration entre Braze et [Hightouch]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/) vous permet d’importer des cohortes d’utilisateurs dans Braze, en envoyant des campagnes ciblées basées sur des données qui n’existent peut-être que dans votre entrepôt.

#### Peak - Contenu dynamique

L’intégration entre Braze et [Peak]({{site.baseurl}}/partners/message_personalization/dynamic_content/peak/) vous permet de prendre la probabilité et les attributs de prédiction du taux d’attrition en fonction des comportements et interactions des clients, et de les importer dans Braze pour les utiliser dans la segmentation et le ciblage des clients. 

#### Shopify - eCommerce

L’intégration entre Braze et [Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) a été élargie pour offrir un délai avant abandon d’achat, définir un identifiant de produit préféré, et plusieurs nouveaux événements Shopify, notamment `shopify_paid_order`, `shopify_partially_fulfilled_order`, `shopify_fulfilled_order`, `shopify_cancelled_order` et `shopify_created_refund`.

#### Survicate - Sondages

L’intégration entre Braze et [Survicate]({{site.baseurl}}/partners/message_orchestration/channel_extensions/surveys/survicate/) vous permet d’inclure des liens d’enquête dans vos e-mails ou d’intégrer directement des extraits de code d’enquête pour améliorer le taux de réponse. Une fois les enquêtes terminées, retournez à Survicate pour identifier et analyser les attributs et les réponses de vos répondants à l’enquête.

#### Viralsweep - Fidélisation

L’intégration entre Braze et [ViralSweep]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/viralsweep/) vous permet de lancer des loteries et des concours sur la plateforme ViralSweep (en développant vos listes d’e-mails et de SMS), puis d’envoyer des informations de participation aux loteries/concours vers Braze pour les utiliser dans des campagnes ou des Canvas. 


[support]: {{site.baseurl}}/support_contact/

<br><br>