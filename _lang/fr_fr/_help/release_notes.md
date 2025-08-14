---
nav_title: Notes de version
article_title: Notes de version
page_order: 4
layout: dev_guide
guide_top_header: "Notes de version"
guide_top_text: "C’est là que vous trouverez toutes les mises à jour de la plateforme Braze, avec <a href='/docs/help/release_notes/#most-recent'>les dernières mises à jour de la plateforme</a> suivantes."
page_type: landing
search_rank: 1
description: "Cette page de destination est le foyer des notes de version de Braze. C’est là que vous trouverez toutes les mises à jour de notre plateforme et de nos SDK Braze ainsi que la liste des fonctionnalités retirées."

guide_featured_title: "Notes de version"
guide_featured_list:
  - name: 2025
    link: /docs/help/release_notes/2025/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2024
    link: /docs/help/release_notes/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
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
    link: /docs/developer_guide/changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Notes de version Braze les plus récentes {#most-recent}

> Braze publie des informations sur les mises à jour du produit à une cadence mensuelle, en s’alignant sur les versions majeures du produit, bien que le produit soit mis à jour avec des améliorations diverses sur une base hebdomadaire.<br><br>Pour plus d'informations sur l'une des mises à jour répertoriées dans cette section, contactez votre gestionnaire de compte ou [ouvrez un ticket de support]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Vous pouvez également consulter [nos journaux de modifications SDK]({{site.baseurl}}/developer_guide/changelogs) pour voir plus d'informations sur nos versions mensuelles de SDK, mises à jour et améliorations.

## Publication le 24 juin 2025

### OfferFit par Braze

[OfferFit](https://www.offerfit.ai/) remplace les tests A/B par une prise de décision basée sur l'intelligence artificielle qui personnalise tout et maximise n'importe quel indicateur : générez des dollars, pas des clics - avec OfferFit, vous pouvez optimiser n'importe quel indicateur clé de performance de votre entreprise. Consultez notre section dédiée [OfferFit by Braze]({{site.baseurl}}/user_guide/offerfit) pour des exemples de cas d'utilisation et les principales fonctionnalités.

### Nouveaux tutoriels SDK

Chaque didacticiel du SDK de Braze propose des instructions étape par étape ainsi que des exemples de code complets. Choisissez un tutoriel ci-dessous pour commencer :

- [Affichage de bannières]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Personnalisation du style des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [Affichage conditionnel des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [Report des messages in-app déclenchés]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### Flexibilité des données

#### Approvisionnement SAML juste-à-temps

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Utilisez le [provisionnement SAML en flux tendu]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit) pour permettre aux nouveaux utilisateurs du tableau de bord de créer un compte Braze lors de leur première connexion. Cela élimine le besoin pour les administrateurs de créer manuellement un compte pour un nouvel utilisateur de tableau de bord, de choisir leurs autorisations, de les affecter à un espace de travail et d'attendre qu'ils activent leur compte.

#### Filtres par sélection

Vous pouvez désormais ajouter jusqu'à 10 filtres par [sélection]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections).

#### Stockage du catalogue

La taille de stockage pour la version gratuite des [catalogues]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#catalog-storage) est de 100 Mo maximum. Vous pouvez avoir un nombre illimité d'articles tant qu'ils ne dépassent pas 100 Mo.

#### Nombre de lignes synchronisées avec l'ingestion de données dans le nuage.

Par défaut, pour Cloud Data Ingestion, chaque exécution peut synchroniser jusqu'à 500 millions de données. Toute synchronisation comportant plus de 500 millions de nouvelles lignes sera interrompue.

Reportez-vous aux [limitations du produit Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations) pour plus de données.

### Canaux robustes

#### Tests d'accessibilité dans Inbox Vision

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Utilisez les [tests d'accessibilité]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) dans Inbox Vision pour mettre en évidence les problèmes d'accessibilité que peut présenter votre e-mail. 

Les tests d'accessibilité analysent le contenu de vos e-mails en fonction de certaines exigences des [Directives pour l'accessibilité des contenus web](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA. Cela peut fournir des informations sur les éléments qui ne respectent pas les normes d'accessibilité.

#### Suivi des clics pour WhatsApp

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez activer le [suivi des clics]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking) dans les messages de réponse et les messages modèles pour voir les données relatives aux clics dans vos rapports de performance WhatsApp et être en mesure de segmenter les utilisateurs en fonction de qui a cliqué sur quoi.

#### Vidéos pour WhatsApp

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez [intégrer des vidéos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features) dans le corps du texte pour les envois WhatsApp sortants. Ces fichiers doivent être hébergés par URL ou dans la [bibliothèque multimédia de Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library).

### Nouveaux partenariats Braze

#### Stripe - eCommerce

L'intergation Braze et [Stripe]({{site.baseurl}}/partners/stripe) vous permet de déclencher des messages dans Braze sur la base d'événements Stripe tels que le démarrage d'un essai, l'activation d'un abonnement, l'annulation d'un abonnement, et plus encore.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - Mise à jour du pont natif Android [du SDK Android de Braze 35.0.0 vers 36.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 11.6.1 vers 12.0.0.](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Segmentation de Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Mise à jour du SDK Android de Braze [de 35.0.0 à 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

## Publication le 27 mai 2025

### Flexibilité des données

#### Copier des toiles dans différents espaces de travail

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais copier des toiles dans différents espaces de travail. Cela vous permet de démarrer la composition de votre message en commençant par une copie d'un canvas dans un espace de travail différent. Pour plus d'informations sur ce qui est copié, reportez-vous à la section [Copier des campagnes et des toiles dans les espaces de travail]({{site.baseurl}}/copying_to_workspaces/).

#### Règles d'envoi de messages pour le flux de travail d'approbation 

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Utilisez des [règles d'envoi de messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules) dans votre flux de travail d'approbation pour limiter le nombre d'utilisateurs atteignables avant qu'une approbation supplémentaire ne soit requise. De cette façon, vous pouvez revoir vos campagnes et vos canevas avant de cibler un public plus large.

#### Diagrammes de relations entre entités pour Snowflake et Braze

En début d'année, nous avons créé des tables de relations d'entités pour les données partagées entre Snowflake et Braze. Ce mois-ci, nous avons ajouté de [nouveaux diagrammes interactifs]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/) dans lesquels vous pouvez effectuer des panoramiques, des saisies et des zooms sur les détails de chaque tableau, vous donnant ainsi une meilleure idée de la façon dont vos données interagissent avec Braze.

### Libérer la créativité

#### Événements recommandés

{% multi_lang_include release_type.md release="Accès anticipé" %}

Les [événements recommandés]({{site.baseurl}}/user_guide/data/custom_data/recommended_events) mappent les cas d'utilisation les plus courants du commerce électronique. En utilisant les événements personnalisés, vous pouvez débloquer des modèles de canvas pré-créés, des tableaux de bord de reporting qui mappent le cycle de vie du client, et plus encore.

### Canaux robustes

#### Canal des bannières

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Avec les [bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners), vous pouvez créer des envois de messages personnalisés pour vos utilisateurs, tout en étendant la portée de vos autres canaux, tels que l'e-mail ou les notifications push. Vous pouvez intégrer des bannières directement dans votre application ou votre site web, ce qui vous permet d'engager le dialogue avec les utilisateurs à travers une expérience qui semble naturelle.

#### Canal Rich Communication Services (RCS)

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Les [services de communication riches (RCS)]({{site.baseurl}}/about_rcs/) améliorent les SMS traditionnels en permettant aux marques d'envoyer des messages non seulement informatifs, mais aussi beaucoup plus attrayants. Désormais pris en charge sur Android et iOS, RCS apporte des fonctionnalités telles que des médias de haute qualité, des boutons interactifs et des profils d'expéditeur de marque directement dans les applications d'envoi de messages préinstallées des utilisateurs, éliminant ainsi le besoin de télécharger une application distincte.

#### Page des paramètres de poussée

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Utilisez la [page**Paramètres de push**]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings) pour configurer les paramètres clés de vos notifications push, notamment la durée en vie (TTL) de push et la priorité FCM par défaut pour les campagnes Android. Ces paramètres permettent d'optimiser la réception/distribution de vos notifications push et leur efficacité, garantissant ainsi une meilleure expérience à vos utilisateurs.

#### Codes de promotion pour les campagnes de messages in-app.

{% multi_lang_include release_type.md release="Accès anticipé" %}

Vous pouvez utiliser des [codes promotionnels]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) dans les campagnes de messages in-app en insérant un [extrait de liste de codes promotionnels]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) dans le corps du message de votre campagne de messages in-app.

#### Gestion des erreurs de webhook et limite de débit

La nouvelle section [À propos des webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#webhook-error-handling-and-rate-limiting) décrit comment Braze gère les erreurs des webhooks et la limite de débit.

#### Localités des messages in-app

Après avoir [ajouté des locales]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/using_locales) à votre espace de travail, vous pouvez cibler des utilisateurs dans différentes langues au sein d'un seul message in-app.

#### Amazon SES en tant que fournisseur d'envoi d'e-mails (ESP)

Vous pouvez désormais utiliser Amazon SES en tant qu'ESP, de la même manière que vous utiliseriez SendGrid et SparkPost. Reportez-vous à [SSL chez Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) et aux [liens universels et liens d'application]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) pour connaître les nuances dans la mise en place de SSL et le suivi des clics sur la base d'un lien à l'autre.

### Nouveaux partenariats Braze

#### Eagle Eye - Loyauté

L'intégration bidirectionnelle de Braze et d'[Eagle Eye]({{site.baseurl}}/partners/eagle_eye/) vous permet d'activer les données de fidélisation et de promotion directement dans Braze, ce qui permet aux marketeurs de personnaliser l'engagement client à l'aide de données en temps réel telles que les soldes de points, les promotions et les activités de récompense.

#### Eppo - Test A/B

L'intégration de Braze et d'[Eppo]({{site.baseurl}}/partners/eppo/) vous permet de mettre en place des tests A/B dans Braze et d'analyser les résultats dans Eppo pour découvrir des informations et lier la performance des messages à des indicateurs commerciaux à long terme tels que le chiffre d'affaires ou la fidélisation.

#### Mentionnez-moi - Recommandations

Ensemble, [Mention Me](https://www.mention-me.com/) et Braze peuvent être votre porte d'entrée pour attirer des clients haut de gamme et favoriser une fidélité inébranlable à votre marque. En intégrant de façon fluide/sans heurts les données first-party des recommandations dans Braze, vous pouvez proposer des expériences omnicanales hautement personnalisées et ciblées sur les fans de votre marque. Pour commencer, consultez le site [Technology Partners : Mentionnez-moi]({{site.baseurl}}/partners/mention_me).

#### Shopify - eCommerce

[Connectez plusieurs domaines de boutiques Shopify]({{site.baseurl}}/shopify_connecting_multiple_stores/) à un espace de travail unique pour avoir une vue globale de vos clients sur tous les marchés. Créez et lancez des programmes d'automatisation et des parcours dans un espace de travail unique sans dupliquer les efforts dans les magasins régionaux.

### Autre

#### Mise à jour pour créer des messages accessibles dans Braze

Nous avons mis à jour notre article [Créer des messages accessibles dans Braze]({{site.baseurl}}/help/accessibility/) avec des conseils plus clairs et plus prescriptifs sur la création de messages accessibles. Cet article comprend désormais des bonnes pratiques élargies pour la structure du contenu, le texte alt, les boutons et le contraste des couleurs, ainsi qu'une nouvelle section sur la gestion de l'ARIA pour les messages HTML personnalisés. 

Cette mise à jour fait partie de notre effort plus large pour soutenir des expériences d'envoi de messages plus accessibles dans Braze. Nous savons que l'accessibilité est un domaine en constante évolution et nous continuerons à partager ce que nous apprenons.

{% multi_lang_include l'accessibilité/feedback.md %}

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 36.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Cette version annule l'augmentation de la version minimale du SDK Android de Braze de l'API 21 à l'API 25 introduite dans la version 34.0.0. Cela permet au SDK d'être à nouveau compilé dans des applications prenant en charge l'API 21. Notez que si nous réintroduisons la possibilité de compiler, nous ne réintroduisons pas la prise en charge formelle de < API 25, et nous ne pouvons pas garantir que le SDK fonctionnera comme prévu sur les appareils fonctionnant avec ces versions.
    - Si votre application prend en charge ces versions, vous devez le faire :
        - Validez que votre intégration du SDK fonctionne comme prévu sur les appareils physiques (et pas seulement sur les émulateurs) pour ces versions de l'API.
        - Si vous ne pouvez pas valider le comportement attendu, vous devez soit appeler [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html), soit ne pas initialiser le SDK sur ces versions. Sinon, vous risquez de provoquer des effets secondaires involontaires ou une dégradation des performances sur les appareils de vos utilisateurs finaux.
    - Correction d'un problème où les messages in-app provoquaient une lecture sur le fil principal.
    `BrazeInAppMessageManager.displayInAppMessage` est désormais une fonction de suspension Kotlin.
        - Si vous n'appelez pas directement cette fonction, vous n'avez pas besoin de la modifier.
    - AndroidX Compose BOM mis à jour à 2025.04.01 pour gérer les mises à jour dans les API Jetpack Compose.
- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Mise à jour du pont natif Android du SDK Android de Braze 35.0.0 vers 36.0.0.
    - Met à jour les liaisons de la version native d'iOS du SDK Swift de Braze 11.9.0 vers 12.0.0.
    - Mise à jour de l'unité de représentation de PushNotificationEvent.timestamp en millisecondes sur iOS.
        - Auparavant, cette valeur était représentée en secondes sur iOS. Cela correspondra désormais à l'implémentation existante d'Android.
- [SDK Web 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - Cette version annule l'augmentation de la version minimale du SDK Android de Braze de l'API 21 à l'API 25 introduite dans la version 34.0.0. Cela permet au SDK d'être à nouveau compilé dans des applications prenant en charge l'API 21. Cependant, nous ne réintroduisons pas de support formel pour < API 25. Plus d'informations [ici](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600).
    - Mise à jour du pont natif Android du SDK Android de Braze 35.0.0 vers 36.0.0.
    - Met à jour le pont natif iOS du SDK Swift de Braze 11.9.0 vers 12.0.0.

## Publication le 29 avril 2025

### Résolution des problèmes d'accès à Braze

La [résolution des problèmes]({{site.baseurl}}/user_guide/administrative/access_braze/troubleshooting/) d'accès à Braze vous aide à résoudre les problèmes que vous pouvez rencontrer lorsque vous essayez d'accéder à Braze, comme le verrouillage de votre compte ou l'utilisation d'un tableau de bord de Braze qui ne fonctionne pas comme prévu.

### Flexibilité des données

#### Foire aux questions sur les courants

Vous trouverez les réponses à certaines questions fréquemment posées sur Currents sur la nouvelle page [Foire aux questions.]({{site.baseurl}}/user_guide/data/braze_currents/faq/) 

#### Utilisateurs anonymes

Consultez les sections suivantes de la rubrique [Utilisateurs anonymes]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) pour en savoir plus sur le fonctionnement des utilisateurs anonymes et sur les raisons pour lesquelles vous pourriez vouloir leur attribuer des alias d'utilisateur :
- [Fonctionnement]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#how-it-works) 
- [L'attribution d'aliasing de l'utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#assigning-user-aliases)

#### Projets de campagne

[Enregistrer des brouillons]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#campaign-drafts) peut vous aider à apporter des modifications à grande échelle à des campagnes actives. En créant un brouillon, vous pouvez piloter les changements prévus avant votre prochain lancement.

#### Identifier et fusionner les utilisateurs

Lors de l'[identification]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) ou de la [fusion d'utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/), vous pouvez désormais utiliser le paramètre `least_recently_updated` dans le tableau `prioritization` pour donner la priorité à l'utilisateur le moins récemment mis à jour.

#### Fusion d'utilisateurs planifiée

La [fusion planifiée]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#scheduled-merging) vous permet d'automatiser la fusion des profils utilisateurs sur une base quotidienne à l'aide de règles préconfigurées. Braze informera les administrateurs de votre espace de travail 24 heures avant la fusion planifiée, afin de leur rappeler et de leur donner le temps de revoir la configuration.

#### Objet destinataire

Vous pouvez désormais inclure `braze_id` dans l'[objet destinataire]({{site.baseurl}}/api/objects_filters/recipient_object/), ce qui vous permet de demander ou d'écrire des informations dans nos endpoints.

#### Nouveaux centres de données

Braze a ouvert deux nouveaux [centres de données]({{site.baseurl}}/user_guide/data/data_centers/): US-10 et ID-01. Vous pouvez vous inscrire à des centres de données spécifiques à une région lors de la création de votre compte Braze. 

### Libérer la créativité

#### Modèles de pages d'atterrissage

Utilisez les [modèles de page d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#using-landing-page-templates) pour créer des modèles pour vos prochaines campagnes. Ces modèles sont accessibles et gérés à la fois dans l'éditeur de page de destination et dans la section **Modèles** du tableau de bord.

#### Champ du formulaire de la page d'atterrissage

Lorsque vous personnalisez votre page de destination, vous pouvez choisir si un champ de formulaire est [obligatoire ou facultatif]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page). Les champs obligatoires doivent être remplis avant que le formulaire puisse être soumis. Les champs facultatifs peuvent être laissés vides ou non sélectionnés par l'utilisateur.

#### Modèles de canevas préconstruits

Braze Canvas propose plusieurs [modèles préconstruits]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) spécialement conçus pour les marketeurs de l'e-commerce, ce qui facilite la mise en œuvre de stratégies essentielles. Cette page propose quelques modèles clés que vous pouvez utiliser pour améliorer vos parcours clients.

### Canaux robustes

#### Vidéos WhatsApp

{% multi_lang_include release_type.md release="Accès anticipé" %}

Les [fichiers vidéo WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages) peuvent désormais être hébergés via une URL ou dans la bibliothèque multimédia de Braze.

#### Liste des messages WhatsApp

Les [messages de liste]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages#list-messages/) apparaissent sous la forme d'un corps de message avec une liste d'options cliquables. Chaque liste peut comporter plusieurs sections et chaque liste peut comporter jusqu'à 10 lignes.

#### Copier le lien de l’aperçu

Utilisez le **lien Copier l'aperçu** dans vos [messages e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#step-3-add-your-sending-information) HTML et glisser-déposer, vos [modèles d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/#step-5-preview-and-test-your-message) et vos [blocs de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) pour générer un lien partageable qui montre à quoi ressemblera votre contenu pour un utilisateur aléatoire.

#### Schéma d'enregistrement des poussées

Nous avons remanié notre documentation sur les notifications push dans le guide de l'utilisateur et ajouté un nouveau diagramme pour aider à visualiser [ce à quoi ressemble l'enregistrement push à plus grande échelle]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#what-does-this-look-like-on-a-broader-scale).

### Nouveaux partenariats Braze

#### Mise à jour des catégories de partenaires

Nous avons mis à jour la [section Partenaires technologiques]({{site.baseurl}}/partners/home/) avec de nouvelles catégories et sous-catégories afin d'améliorer votre expérience de navigation.

#### Shopify (nouvelle version) - eCommerce

Une nouvelle version de l'intégration Shopify sera publiée par phases à partir d'avril, en fonction du type de magasin Shopify et de l'ID externe utilisé pour configurer l'intégration initiale.

**L'ancienne version de l'intégration sera obsolète le 28 août 2025. Vous devez mettre à jour la version la plus récente de l'intégration avant le 28 août 2025.**

Nouveaux clients de Braze : À partir d'avril 2025, Braze déploiera progressivement le nouveau connecteur Shopify pour les nouveaux onboardings et la mise à niveau des clients existants. Pour en savoir plus sur la nouvelle intégration standard, consultez l'[intégration standard de Shopify]({{site.baseurl}}/shopify_standard_integration/).

#### Just Words - Contenu dynamique

[Just Words]({{site.baseurl}}/partners/just_words/) hyperpersonnalise les messages à grande échelle sur les canaux de marketing du cycle de vie, vous permettant de tester dynamiquement des centaines de variations et d'actualiser automatiquement les contenus peu performants.

#### Tapcart - eCommerce

[Tapcart]({{site.baseurl}}/partners/ecommerce/tapcart/) est une plateforme de commerce mobile de premier plan pour les marques alimentées par Shopify, permettant aux marchands de créer des applications mobiles personnalisées qui offrent des expériences d'achat personnalisées et attrayantes que leurs clients adorent.

### SDK

#### Gestion des versions du SDK de Braze

Vous pouvez désormais en savoir plus sur la [gestion des versions]({{site.baseurl}}/developer_guide/sdk_integration/version_management/) du SDK de Braze, afin que votre application puisse rester à jour avec les dernières fonctionnalités et améliorations de qualité.

#### Audit de la documentation du SDK

Nous vérifions actuellement l'ensemble du [contenu de notre SDK pour les développeurs]({{site.baseurl}}/developer_guide/) afin de nous assurer que tous nos échantillons de code sont utiles et exacts. Jusqu'à présent, nous avons apporté diverses mises à jour à nos documentations Android et Swift, et d'autres sont à venir.

### Contribution aux documents de Braze

#### Support hors ligne pour les contributeurs de Braze

Si vous contribuez à Braze Docs, vous pouvez désormais générer votre site local de documentation de manière totalement déconnectée. Pour commencer, consultez la rubrique [Contribuer à la documentation de Braze]({{site.baseurl}}/contributing/home/).

#### Résolution des problèmes de votre fourchette de documentation Braze

Pour les contributeurs de Braze Documentation qui ont des difficultés à cibler notre dépôt à partir de leur fork, nous avons créé des [étapes de résolution des problèmes]({{site.baseurl}}/contributing/troubleshooting/#missing-base-repository) pour vous aider à vous remettre sur les rails.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [Braze Unity SDK 8.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
    - Mise à jour du pont natif iOS du [SDK Swift de Braze 10.3.0 vers 11.9.0.](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif Android du [SDK Android de Braze 32.1.0 vers 35.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - La version minimale requise du SDK Android est 25. Pour plus de détails [, cliquez ici.](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Segmentation de Braze Kotlin 3.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)
    - Mise à jour du SDK Android [de Braze de la version 32.1.0 à la version 35.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - La version minimale requise du SDK Android est 25. Pour plus de détails [, cliquez ici.](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200)
    - Les XCFrameworks statiques distribués incluent désormais leurs ressources directement au lieu de s'appuyer sur des bundles de ressources externes.
        - Lors de l'intégration manuelle des XCFrameworks statiques, vous devez sélectionner l'option *Embed & Sign (Intégrer et signer)* pour chaque XCFramework dans la section *Frameworks, Libraries, and Embedded Content (Cadres, bibliothèques et contenu intégré)* des *General settings (Paramètres généraux)* de votre cible.
        - Aucune modification n'est nécessaire pour les intégrations du gestionnaire de paquets swift ou de CocoaPods.
- [Braze Segmentation Swift 6.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Met à jour les bindings du SDK Swift de Braze pour qu'il nécessite les versions de la dénomination `12.0.0`+ SemVer.
        - Cela permet la compatibilité avec n'importe quelle version du SDK de Braze, de `12.0.0` jusqu'à, mais sans inclure, `13.0.0`.
        - Reportez-vous au journal des modifications de [`12.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200) pour plus d'informations sur les ruptures potentielles.

## Publication le 1er avril 2025

### Mises à jour de la navigation sur Braze

La navigation mise à jour dans Braze est conçue pour vous aider à accéder efficacement aux fonctionnalités et au contenu sur tous les appareils. Notez que l'option permettant de passer d'une version de navigation à l'autre n'est plus disponible. Pour en savoir plus, consultez notre article consacré à [la navigation dans la Braze]({{site.baseurl}}/user_guide/administrative/access_braze/navigation).

### Guide du développeur démêler

Auparavant, de nombreuses tâches au niveau de la plateforme étaient réparties sur plusieurs pages, l'intégration du SDK Swift étant par exemple répartie sur six pages. En outre, les fonctionnalités partagées étaient documentées individuellement pour chaque plateforme, ce qui signifie qu'une recherche sur un sujet tel que "Configuration des notifications push" aboutissait à 10 pages différentes.

**Avant :**

![La documentation Swift précédente se trouve dans la section Guides d'intégration de la plate-forme.]({% image_buster /assets/img/before_swift.png %})

Désormais, les tâches au niveau de la plateforme ont été fusionnées en une seule page et les fonctionnalités partagées du SDK existent désormais sur la même page (avec l'aide de notre nouvelle fonctionnalité de navigation vers le SDK). Par exemple, il n'y a plus qu'une seule page pour l'intégration du SDK Braze, où vous pouvez passer d'une plateforme à l'autre en sélectionnant un onglet en haut de la page. Lorsque vous le faites, même la table des matières de la page est mise à jour pour refléter l'onglet sélectionné.

**Après :**

![La documentation Swift mise à jour se trouve dans l'onglet Swift de l'article Intégration du SDK.]({% image_buster /assets/img/after_swift.png %})

![La documentation Android mise à jour se trouve dans l'onglet Android de l'article Intégration du SDK.]({% image_buster /assets/img/after_android.png %})

### Contribution aux documents de Braze

Si vous ne le saviez pas, notre documentation est entièrement open-source ! Pour en savoir plus, consultez notre [Guide de la contribution]({{site.baseurl}}/contributing/home). Ce mois-ci, nous avons documenté certaines fonctionnalités du site, comme le [développement automatique des sections]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand) et le [rendu du contenu généré par l'API]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server).

### Flexibilité des données

#### Mise à jour des propriétés de l'entrée Canvas

Les propriétés d'entrée dans le canvas font désormais partie des [variables de contexte du canvas.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) Chaque variable de contexte comprend un nom, un type de données et une valeur qui peut inclure Liquid. Pour plus d'informations, reportez-vous au [composant Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

#### Mise à jour des filtres de segmentation pour les filtres de numéros de téléphone

Les filtres de segmentation ont été mis à jour pour refléter les changements apportés à deux filtres de numéros de téléphone :

- [Numéro de téléphone non formaté]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (anciennement **numéro de téléphone**) : Segmente vos utilisateurs en fonction de leur numéro de téléphone non formaté.
- [Numéro de téléphone]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (anciennement **numéro de téléphone de l'expéditeur**) : Segmente vos utilisateurs en fonction du champ de numéro de téléphone formaté E.164.

#### Supprimer les données personnalisées

Au fur et à mesure que vous créez des campagnes et des segments ciblés, vous constaterez peut-être que vous n'avez plus besoin d'un événement personnalisé ou d'un attribut personnalisé. Vous pouvez maintenant [supprimer ces données personnalisées]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data) et retirer leurs références de votre app.

#### Importation d'utilisateurs avec des adresses e-mail et des numéros de téléphone

Vous pouvez désormais utiliser une adresse e-mail ou un numéro de téléphone pour [importer des utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#importing-with-email-addresses-and-phone-numbers) et omettre un ID externe ou un alias utilisateur.

#### Résolution des problèmes d'identifiant à l'initiative du fournisseur de services

L'identifiant initié par le fournisseur de services dispose désormais d'une [section de résolution des problèmes]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting) pour vous aider à résoudre les problèmes liés à SAML et à l'authentification unique.

#### Résolution des problèmes liés à l'importation d'utilisateurs

La [section "Résolution des problèmes liés à l'importation d'utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting) " comporte des entrées nouvelles et mises à jour, notamment sur la manière de résoudre les problèmes liés aux lignes manquantes dans vos fichiers CSV importés.

#### Questions fréquemment posées sur les extensions de segments

Consultez notre [foire aux questions]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions) sur les extensions de segments, notamment sur la façon dont vous pouvez créer une extension de segments qui utilise plusieurs événements personnalisés.

#### Délais personnalisés et prolongés

{% multi_lang_include release_type.md release="Accès anticipé" %}

Vous pouvez définir un [délai personnalisé]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays) pour vos utilisateurs et l'utiliser avec une étape Contexte pour sélectionner la variable contextuelle à retarder.

Vous pouvez également prolonger les délais jusqu'à deux ans. Par exemple, si vous intégrez de nouveaux utilisateurs à votre application, vous pouvez ajouter un délai prolongé de deux mois avant d'envoyer une étape Message pour inciter les utilisateurs qui n'ont pas encore démarré une session à le faire.

#### Attributs par défaut du profil utilisateur pour Snowflake

{% multi_lang_include release_type.md release="Beta" %}

Il y a maintenant trois [attributs de profil utilisateur par défaut]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes/) dans Snowflake. Chaque vue est conçue pour un cas d'utilisation spécifique, avec ses propres considérations en matière de performances. Par exemple, vous pouvez recevoir un snapchat périodique des attributs par défaut d'un profil utilisateur.

### Canaux robustes

#### Principes de base de l'envoi de messages

[Fondamentaux de l'envoi de messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals) est une nouvelle section des outils d'engagement qui abrite les concepts et termes partagés pour les campagnes et les toiles, tels que l'archivage et la localisation des messages.

#### Domaines personnalisés WhatsApp

Vous pouvez désormais attribuer des [domaines personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/) à un ou plusieurs groupes d'abonnement WhatsApp.

#### Messages in-app déclenchés pour Canvas

Vous pouvez désormais sélectionner un [déclencheur pour vos messages in-app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) au démarrage de la session, ou en fonction d'événements personnalisés et d'achats. Une fois les délais écoulés et les options d'audience cochées, les messages in-app sont mis en ligne/en production/instantané lorsque l'utilisateur atteint l'étape Message. Si un utilisateur démarre une session et effectue l'événement déclencheur pour le message in-app, l'utilisateur verra le message in-app. 

#### Limiter le volume d'entrée pour les canvas

Vous pouvez limiter le nombre de personnes susceptibles d'entrer dans ce Canvas en fonction d'une cadence choisie (quotidienne, pendant toute la durée du Canvas ou à chaque fois que le Canvas est planifié). Par exemple, vous pouvez [paramétrer les contrôles d'entrée de]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience) manière à ce que la toile ne puisse être envoyée qu'à 5 000 utilisateurs par jour.

#### Nouveau cas d'utilisation : Système d'e-mail de rappel de réservation

Découvrez comment vous pouvez utiliser les fonctionnalités de Braze pour [créer un service d'envoi de messages e-mail de rappel de réservation]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case). Le service permettra aux utilisateurs de prendre des rendez-vous et leur enverra des messages pour leur rappeler leurs rendez-vous à venir. Bien que ce cas d'utilisation utilise des messages e-mail, vous pouvez envoyer des messages dans n'importe quel canal, ou dans plusieurs, sur la base d'une seule mise à jour d'un profil utilisateur.

#### Suivi des clics pour des liens spécifiques

Vous pouvez [désactiver le suivi des clics]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) pour des liens spécifiques en ajoutant du code HTML à votre message e-mail dans l'éditeur HTML ou aux composants dans l'éditeur par glisser-déposer.

#### Gestion dynamique de la passerelle du service de notification push d'Apple

La [gestion dynamique des passerelles APN]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management) améliore la fiabilité et l'efficacité des notifications push d'iOS en détectant automatiquement l'environnement APN adéquat. Auparavant, vous deviez sélectionner manuellement des environnements APN (développement ou production) pour vos notifications push, ce qui entraînait parfois des configurations de passerelle incorrectes, des échecs de réception/distribution et des erreurs BadDeviceToken.

#### Support de Flutter pour les bannières

{% multi_lang_include release_type.md release="Accès anticipé" %}

Les bannières sont désormais compatibles avec Flutter. En outre, toute la documentation de Banner a été revue pour en faciliter l'utilisation. Consultez les articles suivants pour commencer :

- [À propos des bannières]({{site.baseurl}}/developer_guide/banners/)
- [Création de campagnes de bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
- [Intégrer des bannières dans votre application]({{site.baseurl}}/developer_guide/banners/creating_placements/)

#### Suivi des clics sur WhatsApp

{% multi_lang_include release_type.md release="Accès anticipé" %}

Le [suivi des clics]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/) vous permet de savoir quand quelqu'un clique sur un lien dans votre message WhatsApp, ce qui vous donne une vision claire du contenu qui suscite l'engagement. Braze raccourcit vos URL, ajoute un suivi en coulisses et enregistre les clics au fur et à mesure qu'ils se produisent.

#### Questions fréquemment posées pour push

Consultez notre nouvel article [Push FAQ]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq) qui aborde certaines des questions les plus fréquemment posées lors de l'implémentation des campagnes push.

#### Résolution des problèmes de poussée

La [résolution des problèmes]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting) liés aux notifications push propose un certain nombre d'étapes pour vous aider à relever les défis liés à la réception/distribution des notifications push. Par exemple, si vous rencontrez des problèmes de réception/distribution avec les notifications push, nous avons compilé les étapes à suivre pour résoudre le problème.

### Nouveaux partenariats Braze

#### Movable Ink Da Vinci - Contenu dynamique

L'intégration de Braze et Movable Ink [Da Vinci]({{site.baseurl}}/partners/movable_ink_da_vinci) permet aux marques de diffuser des messages hautement personnalisés en s'appuyant sur le moteur de décision de contenu piloté par l'intelligence artificielle de Da Vinci. Da Vinci sélectionne le contenu le plus pertinent pour chaque utilisateur et déploie les messages de façon fluide/sans heurts/de façon homogène, etc.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [Flutter SDK 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Mise à jour du pont natif Android du [SDK Android 33.0.0 vers 35.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - La version minimale requise du SDK Android est 25. Pour plus de détails [, cliquez ici.](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information)
- [Swift SDK v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Web v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## Publication le 4 mars 2025

### Reports

Braze a mis à jour notre définition de ce qu'est un échec provisoire d'envoi et envoie un nouvel événement appelé [reports à]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance) partir du 25 février 2025 à 10h EST.

Pour les clients de Sendgrid, nous avons apporté une modification afin de séparer les événements d'ajournement de nos événements d'échec provisoire envoi. Nous considérons les événements différés comme un échec provisoire d'envoi. Cela concerne tous les clients de Sendgrid qui utilisent Currents, Query Builder, SQL Extension, Snowflake Data Sharing ou notre produit Transactional Email.

#### Comportement antérieur

Avant le 25 février 2025, un événement différé pour une adresse e-mail sur une campagne ou un Canvas enregistre un événement d'échec provisoire d'envoi à chaque fois. Par conséquent, les reports sont inclus dans les données relatives aux échecs provisoires d'envoi. Un utilisateur ou une campagne peut ainsi signaler plus d'événements d'échec provisoire d'envoi que prévu. 

#### Nouveau comportement

À partir du 25 février 2025, un événement différé n'enregistrera plus à chaque fois un événement d'échec provisoire d'envoi. Au lieu de cela, nous enregistrerons un événement d'échec provisoire d'envoi une fois par envoi pour l'adresse e-mail, quel que soit le nombre de fois que l'e-mail est retenté ou différé.

#### Ce que cela signifie

Vous constaterez une baisse sensible du volume des événements provisoires d'envoi à partir du 25 février 2025, ce qui entraînera les changements potentiels suivants :

- Diminution des échecs provisoires d'envoi pour tous les rapports créés à l'aide du générateur de requêtes.
- Réduction de la taille des segments à l'aide des extensions SQL si vous ciblez des utilisateurs ayant subi X échecs provisoires d'envoi au cours d'une période donnée.
- Baisse du nombre d'échecs provisoires d'envois réalisés à l'aide de Currents et de l'une de nos fonctionnalités à l'aide de Snowflake.
- Baisse du nombre d'échecs provisoires d'envois pour le produit "Transactional Email".

Pour les clients de Sparkpost, il n'y a pas d'impact sur vos données d'événements d'échec provisoire, à la place vous commencerez à recevoir un nouvel événement e-mail, deferral, dans Currents et Snowflake.

### Guide du développeur démêler

Les contenus identiques partagés entre plusieurs SDK commencent à être fusionnés grâce à la nouvelle fonctionnalité d'onglet SDK du site de documentation. Ce mois-ci, l'[intégration SDK]({{site.baseurl}}/developer_guide/sdk_integration/), l'[initialisation SDK]({{site.baseurl}}/developer_guide/sdk_initialization/) et les [cartes de contenu]({{site.baseurl}}/developer_guide/content_cards/) ont été combinées. Restez à l'écoute pour d'autres mises à jour dans les mois à venir.

### Flexibilité des données
 
#### ID de Braze pour les profils utilisateurs

Le profil utilisateur comprend désormais un [ID Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles). Vous pouvez l'utiliser lors de la recherche de profils utilisateurs.

#### Reports

Braze a mis à jour sa définition de ce qu'est un échec provisoire (soft bounce) et envoie un nouvel événement appelé [report]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance), c'est-à-dire lorsqu'un e-mail n'a pas été livré immédiatement, mais que Braze relance l'e-mail jusqu'à 72 heures après cet échec provisoire de la réception/distribution afin de maximiser les chances de réussite avant que les tentatives pour cette campagne spécifique ne soient interrompues.

#### Relations entre entités Snowflake
 
Nous avons mappé les [schémas bruts des tables](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt) pour les relations entre entités de Snowflake et Braze dans une nouvelle [page de documentation conviviale](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships). Il comprend une ventilation des tables `USER_MESSAGES` appartenant à chaque canal, ainsi que des descriptions des clés primaires, étrangères et natives de chaque table.

#### Gestion des identités pour les ID externes

L'utilisation d'une adresse e-mail ou d'une adresse e-mail hachée comme ID externe Braze peut simplifier la gestion des identités dans l'ensemble de vos sources de données. Cependant, il est important de prendre en compte les [risques potentiels]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) pour la confidentialité des utilisateurs et la sécurité des données.
 
### Libérer la créativité

#### Didacticiels sur les liquides

Ajout de trois [didacticiels Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/#tutorials) sur l'utilisation des opérateurs dans les scénarios suivants.

<table border="1">
  <tr>
    <td>Choix d'un message avec un attribut personnalisé de type entier.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/integer.png %}" alt="L&apos;étape de composition dans Braze affichant un message avec un attribut personnalisé de type entier." /></td>
  </tr>
  <tr>
    <td>Choix d'un message avec un attribut personnalisé de type chaîne de caractères.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/string.png %}" alt="L&apos;étape de composition dans Braze affichant un message avec une chaîne de caractères en attribut personnalisé." /></td>
  </tr>
  <tr>
    <td>Abandon d'un message en fonction de l'emplacement/localisation.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/location.png %}" alt="L&apos;étape de composition dans Braze montre l&apos;interruption d&apos;un message en fonction de l&apos;emplacement/localisation." /></td>
  </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Étapes du contexte pour Canvas
 
{% multi_lang_include release_type.md release="Accès anticipé" %}
 
Utilisez les [étapes Contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) pour créer ou mettre à jour un ensemble de variables qui conseillent le contexte d'un utilisateur (ou des informations sur le comportement de cet utilisateur) au fur et à mesure qu'il se déplace dans un Canvas.

#### Délai personnalisé

{% multi_lang_include release_type.md release="Accès anticipé" %}

Vous pouvez définir un [délai personnalisé]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) pour vos utilisateurs en basculant la case Délai **personnalisé** dans votre étape Délai. Vous pouvez l'utiliser avec une étape Contexte pour sélectionner une variable contextuelle à retarder.

Lorsque vous configurez une étape du canvas dans votre parcours utilisateur, vous pouvez désormais créer un délai allant jusqu'à 2 ans.

#### Annulation de la synchronisation automatique

Lors de la [rédaction d'un message e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email), vous pouvez revenir à la synchronisation automatique dans l'onglet Texte en clair en sélectionnant l'icône Régénérer à partir du HTML, qui n'apparaît que si le texte en clair n'est pas synchronisé.

![Le bouton de retour pour la synchronisation automatique dans Braze.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### Canaux robustes

#### Mises à jour en ligne/en production/instantané d'Android

Bien que les mises à jour en ligne/instantanées ne soient pas officiellement disponibles avant le mois d'août, elles ne sont pas encore disponibles.
[Android 16](https://android-developers.googleblog.com/2025/01/first-beta-android16.html), notre page [Mises à jour en direct pour Android]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=android&tab=local) vous montre comment émuler leur comportement, afin que vous puissiez afficher des notifications interactives sur l'écran de verrouillage, similaires aux [activités en direct pour le SDK Braze de Swift]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift). Contrairement aux mises à jour en ligne/en production/instantanées officielles, cette fonctionnalité peut être mise en œuvre pour les anciennes versions d'Android.

#### Copier des campagnes avec des drapeaux de fonctionnalité dans plusieurs espaces de travail

Vous pouvez désormais [copier des campagnes avec des drapeaux de fonctionnalité dans les espaces de travail.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/#copying-campaigns-with-feature-flags) Pour ce faire, assurez-vous que l'espace de travail de destination dispose d'une expérience d'indicateur de fonctionnalité configurée avec un ID correspondant à l'indicateur de fonctionnalité référencé dans la campagne d'origine.

#### Prise en charge de nouveaux types d'envoi de messages WhatsApp

Les messages WhatsApp prennent désormais en charge les [envois de vidéos, d'audio et de documents]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages). Contactez votre gestionnaire de compte Braze si vous souhaitez participer à l’accès anticipé.

#### Envois de messages de droite à gauche

La [création de messages de droite à gauche]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) couvre les meilleures pratiques pour rédiger des messages dans des langues qui se lisent de droite à gauche, afin que vos messages s'affichent avec le plus de précision possible.
 
### L'intelligence artificielle et l'automatisation de l’apprentissage machine.
 
#### Recommandations de poste

L'[utilisation des recommandations d'éléments dans les messages]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations) couvre l'objet `product_recommendation` Liquid et comprend un tutoriel pour vous aider à mettre ces connaissances en pratique.

### Nouveaux partenariats Braze
 
#### Email Love - Extensions de canaux
 
Le partenariat entre Braze et [Email Love]({{site.baseurl}}/partners/message_orchestration/) s'appuie sur la fonctionnalité Export to Braze d'Email Love et sur l'API de Braze pour télécharger vos modèles d'e-mails vers Braze de façon fluide/sans heurts/de façon façon homogène.

#### VWO - Test A/B
 
L'intégration de Braze et de [VWO]({{site.baseurl}}/partners/data_and_analytics/ab_testing/vwo/) vous permet d'exploiter les données d'expérience de VWO pour créer des segments ciblés et proposer des campagnes personnalisées.
 
### Mises à jour SDK
 
Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Fait passer la version minimale requise de React native à [0.71.0.](https://reactnative.dev/blog/2023/01/12/version-071) Pour plus d'informations, reportez-vous à la [politique de soutien aux versions du](https://github.com/reactwg/react-native-releases#releases-support-policy) groupe de travail React.
    - La version minimale requise d'iOS passe à 12.0.
    - Met à jour les liaisons de la version native d'iOS du [SDK Swift de Braze 7.5.0 à 8.1.0.](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour des liens de la version native d'Android du [SDK Android de Braze 29.0.1 vers 30.1.1.](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

## Publication le 4 février 2025

### Améliorations apportées à la documentation de Braze

#### Guide du contributeur
Nos récentes mises à jour du [Guide de contribution]({{site.baseurl}}/contributing/your_first_contribution) permettent aux utilisateurs non techniques de contribuer plus facilement à la documentation de Braze.

#### Refonte des données et de l'analyse/analytique (si utilisé comme adjectif)
Pour vous permettre de trouver plus facilement ce que vous cherchez, nous avons séparé les articles qui se trouvaient auparavant sous "Data & Analytics" en " [Data]({{site.baseurl}}/user_guide/data) and [Analytics]({{site.baseurl}}/user_guide/analytics)". 

#### Guide du développeur
Nous avons fait un grand ménage dans toute la documentation du [Guide du développeur Braze]({{site.baseurl}}/developer_guide/home), notamment en fusionnant les "comment faire" répartis sur plusieurs pages en une seule.

Vous trouverez également une nouvelle [page de référence SDK]({{site.baseurl}}/developer_guide/references) qui répertorie l'ensemble de la documentation de référence et des référentiels pour chaque SDK Braze.

##### SDK Unreal Engine Braze
Nous avons migré et réécrit tout le contenu du README du dépôt GitHub du SDK d'Unreal Engine Braze dans sa [section dédiée sur Braze Docs]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine).

### Flexibilité des données

#### Tableau de bord de l'utilisation de l'API

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Le [tableau de bord de l'utilisation de l'API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard) vous permet de surveiller le trafic de votre API REST entrant dans Braze afin de comprendre les tendances de votre utilisation de nos API REST et de résoudre les problèmes éventuels.

#### Ajout d'étiquettes aux attributs personnalisés

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez [ajouter des étiquettes à un attribut personnalisé]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#adding-tags) après sa création si vous disposez de l'autorisation "Gérer les événements et les attributs, les clients". Les étiquettes peuvent ensuite être utilisées pour filtrer la liste des attributs.

#### Sélections de catalogue et endpoints de champs de catalogue asynchrones 

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Les endpoints suivants sont désormais généralement disponibles :
* [POST : Créer des champs de catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)
* [DELETE : Supprimer un champ du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)
* [DELETE : Supprimer la sélection du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)
* [POST : Créer une sélection de catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections)

#### Utilisation d'une adresse e-mail pour déclencher des campagnes ou des canevas

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais spécifier un destinataire par adresse e-mail pour déclencher vos [campagnes]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) et [Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience).

#### Utilisation d'un numéro de téléphone pour identifier un utilisateur via l'API

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais utiliser un numéro de téléphone, en plus d'un alias et d'une adresse e-mail, pour identifier un utilisateur via l'[endpoint de l'API`/users/identify` ]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

#### Obtenir une trace SAML
Nous avons ajouté des [étapes sur la façon d'obtenir une trace SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace), ce qui vous aide à résoudre plus efficacement les problèmes liés à l'authentification unique (SSO) SAML avec le support.
 
#### Centres de données spécifiques à une région
Comme Braze se développe pour desservir de nouvelles régions, nous avons ajouté un [article sur les centres de données de Braze]({{site.baseurl}}/user_guide/data/data_centers) afin de clarifier notre approche opérationnelle.
 
### Libérer la créativité
 
#### Notifications de baisse de prix et de retour en stock

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais avertir les clients lorsqu'un article est de nouveau en stock en configurant des [notifications de retour en stock]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications) par le biais d'un Canvas et d'un catalogue.

Vous pouvez également créer des [notifications de baisse de]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications) prix pour informer les clients lorsque le prix d'un article a baissé en configurant des notifications de baisse de prix dans un catalogue et dans Canvas.

#### Aperçu de la sélection 

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Après avoir créé une sélection, vous pouvez [voir ce qu'elle donnerait]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview) pour un utilisateur aléatoire ou pour un utilisateur spécifique.

#### Modélisation de produits de catalogue comprenant des étiquettes Liquid 

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez [créer des modèles d'articles de catalogue qui incluent le liquide]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).

#### Modèles de canvas
Nous avons ajouté de nouveaux modèles Canvas pour l'[onboarding des utilisateurs avec une enquête de préférences]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey) et la [création d'une inscription par e-mail avec double abonnement.]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup)

#### Gérer les prospects avec Salesforce Sales Cloud pour le B2B
Les marketeurs B2B peuvent notamment utiliser Braze par le biais d'une intégration avec Salesforce Sales Cloud. Pour en savoir plus sur la mise en œuvre de ce [cas d'utilisation]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud), cliquez ici.
 
### Canaux robustes

#### Listes de suppression

{% multi_lang_include release_type.md release="Beta" %}
 
[Les listes de suppression]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) spécifient les groupes d'utilisateurs qui ne recevront jamais de messages. Les administrateurs peuvent créer des listes de suppression avec des filtres de segmentation pour restreindre un groupe d'utilisateurs de la même manière que vous le feriez pour la segmentation.

### Nouveaux partenariats Braze

#### Constructeur - Contenu dynamique
[Constructor]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/constructor/) est une plateforme de recherche et de découverte de produits qui utilise l'intelligence artificielle et le machine learning pour offrir des recherches, des recommandations et des expériences de navigation personnalisées pour les sites web de ecommerce et de retailing.
 
#### Trustpilot - Contenu dynamique
[Trustpilot]({{site.baseurl}}/partners/trustpilot/) est une plateforme d'évaluation en ligne qui permet à vos clients de partager leurs commentaires et vous permet de gérer les évaluations et d'y répondre.

### Mises à jour SDK
 
Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.
 
- [Braze Android SDK 34.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3400)
    - Mise à jour de la version minimale du SDK, qui passe de 21 (Lollipop) à 25 (Nougat).

## Publication le 7 janvier 2025

### Libérer la créativité

#### Modèles de messages in-app

Nous avons ajouté des [modèles]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/) pour les messages in-app à glisser-déposer.

#### B2B Salesforce Sales Cloud Gestion des prospects

[Gérer les leads avec Salesforce Sales]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud/) Cloud montre comment utiliser les webhooks de Braze pour créer et mettre à jour des leads dans Salesforce Sales Cloud via une intégration soumise par la communauté.

### Canaux robustes

#### Modèles de canvas

Nous avons ajouté des modèles Braze Canvas pour l'[inscription par e-mail avec double abonnement]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/) et l'[onboarding avec enquête sur les préférences.]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/)

#### Modifications de la politique d'abonnement de WhatsApp

Meta a récemment mis à jour sa [politique d'abonnement](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Pour plus d'informations, consultez les [mises à jour des produits WhatsApp.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/)

#### Outil de largeur pour les blocs de contenu dans l'éditeur par glisser-déposer de l'e-mail

Vous pouvez [ajuster la largeur]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) de votre bloc de contenu dans l'éditeur par glisser-déposer de l'e-mail. La largeur par défaut est de 100 %.

### Flexibilité des données

#### Filtre de segmentation provisoire d'envoi

Segmentez vos utilisateurs en fonction du nombre d'échecs provisoires d'envoi X fois en Y jours. Pour plus d'informations, reportez-vous au [glossaire des filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced).

#### Aperçu des utilisateurs anonymes

[Utilisateurs anonymes]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) donne un aperçu des utilisateurs anonymes et des alias d'utilisateurs, en soulignant leur importance et la manière dont ils peuvent être exploités dans vos messages.

#### Composition du groupe de contrôle global

Vous pouvez [consulter l'appartenance à un groupe de contrôle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group) en accédant à l'onglet **Engagement** du profil d'un utilisateur et en faisant défiler la page jusqu'à la section **Divers.** 

### Nouveaux partenariats Braze

#### Justuno - Capture de prospects

[Justuno]({{site.baseurl}}/partners/data_and_analytics/leads_capture/justuno/) vous permet de créer des expériences visiteurs entièrement optimisées pour toutes vos audiences avec des segments dynamiques, offrant le ciblage le plus avancé disponible - le tout sans impacter la vitesse du site ou augmenter le travail de développement.

#### Odicci - plateforme de données client

Intégrez Braze à [Odicci]({{site.baseurl}}/partners/odicci/), une plateforme qui donne aux entreprises les moyens d'acquérir, d'engager et de fidéliser leurs clients grâce à des expériences omnicanales axées sur la fidélisation.

#### Optimizely - Test A/B

L'intégration entre Braze et [Optimizely]({{site.baseurl}}/partners/data_and_analytics/ab_testing/optimizely/) est une intégration bidirectionnelle qui vous permet de :

- Synchronisez chaque nuit vos segments et événements personnalisés de Braze vers Optimizely Data Platform (ODP) afin d'enrichir les profils, rapports et segmentations des clients d'Optimizely.
- Envoyez les événements de Braze Currents depuis Braze vers l'outil de reporting d'Optimizely.
- Synchronisez les données et événements personnalisés de l'ODP vers Braze pour enrichir vos données clients et déclencher l'envoi de messages Braze en fonction des événements clients dans l'ODP.

## 10 décembre 2024 libération

### Emplacement/localisation des utilisateurs du SDK par adresse IP

À partir du 26 novembre 2024, Braze détectera les emplacements/localisations des utilisateurs à partir du pays géolocalisé en utilisant l'adresse IP du début de la première session SDK. Braze utilisera l'adresse IP pour définir la valeur du pays sur les profils utilisateurs créés via le SDK, et ce paramètre de pays basé sur l'IP sera disponible pendant et après la première session. Pour plus d'informations, reportez-vous à la section [Emplacement/localisation]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/).

### Cadre d'accès surélevé

L['accès élevé]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#elevated-access) ajoute une couche de sécurité supplémentaire pour les actions sensibles dans votre tableau de bord de Braze. Lorsqu'il est actif, l'utilisateur doit revérifier son compte avant d'exporter un segment ou de consulter une clé API. Pour utiliser l'accès élevé, accédez à **Paramètres** > **Paramètres d'administration** > **Paramètres de sécurité** et basculez sur cette option.

### Autorisation de consulter des informations personnelles identifiables (IPI)

Pour les administrateurs, vous pouvez [autoriser les utilisateurs à afficher les IIP]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) définies par votre entreprise dans le tableau de bord, dans des aperçus de messages qui utilisent des variables Liquid pour accéder aux propriétés de l'utilisateur. 

Pour les espaces de travail, vous pouvez autoriser les utilisateurs à afficher les IIP définies par votre entreprise dans le tableau de bord, ou afficher les profils utilisateurs mais expurger les champs que votre entreprise a identifiés comme étant des IIP.

### Flexibilité des données

#### Schémas de lac de données

Les schémas suivants ont été ajoutés aux schémas des tables brutes :
- `USERS_CANVASSTEP_PROGRESSION_SHARED` : Événements de progression d'un utilisateur dans un canvas
- `CHANGELOGS_GLOBALCONTROLGROUP_SHARED` : Identifier les numéros de compartiment aléatoires présents dans le groupe de contrôle global actuel et dans le précédent.
- `USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED` : Événements d'impression lorsqu'un utilisateur consulte un indicateur de fonctionnalité

#### Segmentation basée sur les comptes

Vous pouvez effectuer une [segmentation interentreprises (B2B) basée sur les comptes de]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/) deux manières, en fonction de la façon dont vous avez configuré votre modèle de données B2B :

- Lorsque vous utilisez des catalogues pour vos objets de gestion
- Lorsque vous utilisez des sources connectées pour vos objets de gestion

#### Filtres de segmentation

Reportez-vous à la section [Filtres de segmentation]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) pour obtenir la liste complète des filtres de segmentation et leur description.

##### Profil utilisateur créé à

Segmentez vos utilisateurs en fonction de la date de création de leur profil. Si un utilisateur a été ajouté par CSV ou API, ce filtre reflète la date à laquelle il a été ajouté. Si l'utilisateur n'est pas ajouté par CSV ou API et que sa première session est suivie par le SDK, ce filtre reflète la date de cette première session.

##### Envoi du numéro de téléphone

Segmentez vos utilisateurs en fonction du champ du numéro de téléphone e.164. Vous pouvez utiliser des expressions régulières avec ce filtre pour segmenter les numéros de téléphone avec un code pays spécifique.

### Nouveaux partenariats Braze

#### Narvar - Commerce électronique

L'intégration de Braze et [Narvar](https://corp.narvar.com/) permet aux marques d'exploiter les événements de notification de Narvar pour déclencher des messages directement depuis Braze, en tenant les clients informés grâce à des mises à jour opportunes.

#### Zeotap pour Currents - plateforme de données client

L'intégration de Braze et [Zeotap](https://zeotap.com/) vous permet d'étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients de Zeotap avec les profils d'utilisateurs de Braze. Avec [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), vous pouvez également connecter les données à Zeotap pour les rendre exploitables dans l'ensemble des outils de croissance.

#### Notify - Contenu dynamique

L'intégration de Braze et [Notify](https://notifyai.io/) permet aux marketeurs de stimuler efficacement l'engagement sur différentes plateformes. Au lieu de s'appuyer sur les méthodes de marketing traditionnelles, une campagne déclenchée par l'API de Braze peut exploiter les capacités de Notify pour diffuser des messages personnalisés par le biais de plusieurs canaux, notamment les e-mails, les SMS, les notifications push et bien plus encore.

#### Contentful - Contenu dynamique

L'intégration entre Braze et [Contentful](https://www.contentful.com/) vous permet d'utiliser dynamiquement le contenu connecté pour tirer du contenu de Contentful dans vos campagnes Braze.

#### Dépassement - Capture de prospects 

L'intégration de Braze et [Outgrow](https://outgrow.co/) vous permet de transférer automatiquement les données des utilisateurs d'Outgrow vers Braze, ce qui permet de réaliser des campagnes hautement personnalisées et ciblées.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 5.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 12.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/12.0.0)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 10.3.1 vers 11.3.0.](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif Android de Braze [Android SDK 32.1.0 à 33.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [SDK Swift 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/11.0.1/CHANGELOG.md)
