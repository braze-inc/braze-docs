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
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Notes de version Braze les plus récentes {#most-recent}

> Braze publie des informations sur les mises à jour du produit à une cadence mensuelle, en s’alignant sur les versions majeures du produit, bien que le produit soit mis à jour avec des améliorations diverses sur une base hebdomadaire.
> <br>
> <br>
> Pour plus d'informations sur l'une des mises à jour répertoriées dans cette section, contactez votre gestionnaire de compte ou [ouvrez un ticket de support]({{site.baseurl}}/help/support/). Vous pouvez également consulter [nos journaux de modifications SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) pour voir plus d'informations sur nos versions mensuelles de SDK, mises à jour et améliorations.

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

L'intégration de Braze et [Zeotap](https://zeotap.com/) vous permet d'étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients de Zeotap avec les profils d'utilisateurs de Braze. Avec [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), vous pouvez également connecter les données à Zeotap pour les rendre exploitables dans l'ensemble des outils de croissance.

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

## Libération le 12 novembre 2024
 
### Flexibilité des données
 
#### Limite de vitesse pour `/users/track`

La limite de vitesse pour l'[endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) a été mise à jour à 3 000 par 3 secondes.
 
### Libérer la créativité

#### Cas d'utilisation de Canvas

Nous avons rassemblé quelques cas d'utilisation illustrant les différentes façons dont vous pouvez tirer parti d'un Braze Canvas. Si vous êtes en quête d'inspiration, choisissez un cas d'utilisation ci-dessous pour commencer.

- [Panier abandonné]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [En stock]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [Fonctionnalité Adoption]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [Utilisateur déchu]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [Onboarding]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [Rétroaction après l'achat]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### Canaux robustes

#### LINE

{% multi_lang_include release_type.md release="Disponibilité générale" %}

L'intégration de LINE dans Braze est désormais disponible ! LINE est l'application de messages la plus populaire au Japon, avec plus de 95 millions d'utilisateurs actifs par mois. En plus de la messagerie, LINE offre à ses utilisateurs une plateforme « tout-en-un » pour les réseaux sociaux, les jeux, les achats et les paiements.

Pour commencer, consultez notre [documentation LINE.]({{site.baseurl}}/user_guide/message_building_by_channel/line/)
 
#### Synchronisation de l'audience LinkedIn

{% multi_lang_include release_type.md release="Beta" %}

Vous pouvez désormais utiliser LinkedIn avec Braze [Audience Sync]({{site.baseurl}}/partners/canvas_steps/), un outil qui vous aide à étendre la portée de vos campagnes à de nombreuses technologies sociales et publicitaires de premier plan. Pour participer à la version bêta, contactez votre gestionnaire de succès Braze.
 
### Améliorer le guide du développeur
 
Nous sommes en train d'apporter des améliorations majeures au [guide du développeur de Braze]({{site.baseurl}}/developer_guide/home/). Dans un premier temps, nous avons simplifié la navigation et réduit le nombre de sections imbriquées. 

|Avant|Après|
|------|-----|
|!["L'ancienne navigation pour le guide du développeur de Braze."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["La nouvelle navigation pour le guide du développeur de Braze"]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### Nouveaux partenariats Braze
 
#### MyPostcard

[MyPostcard](https://www.mypostcard.com/), une application mondiale de cartes postales de premier plan, vous permet d'exécuter des campagnes de publipostage en toute simplicité, offrant un moyen fluide et rentable d'entrer en contact avec vos clients. Pour commencer, consultez la section [Intégration de MyPostcard à Braze]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/).
 
### Mises à jour SDK
 
Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.
 
- [Expo Plugin 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - Cette version nécessite la version 13.1.0 du SDK React native de Braze.
    - Remplace l'appel à la méthode BrazeAppDelegate iOS de BrazeReactUtils.populateInitialUrl par BrazeReactUtils.populateInitialPayload.
        - Cette mise à jour résout un problème où les événements push ouverts ne se déclenchaient pas lors d'un clic sur une notification alors que l'application est dans un état terminé.
        - Pour tirer pleinement parti de cette mise à jour, remplacez tous les appels de Braze.getInitialURL par Braze.getInitialPushPayload dans votre code JavaScript. L'URL initiale est désormais accessible via la propriété url de la charge utile initiale du push.
- [Braze Segmentation Swift Plugin 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Met à jour les bindings du SDK Swift de Braze afin qu'ils requièrent les versions 11.1.1+ SemVer.
    - Cela permet d'assurer la compatibilité avec toutes les versions du SDK de Braze, de la 11.1.1 à la 12.0.0 incluse.
    - Consultez le journal des modifications de la version 11.1.1 pour plus d'informations sur les ruptures potentielles.

## Libération le 15 octobre 2024

### Flexibilité des données

#### Campagnes et canvas

Lors de la création de campagnes et de canevas, vous pouvez calculer le nombre exact d'utilisateurs atteignables dans votre audience cible au lieu de l'estimation par défaut en sélectionnant [Calculer les statistiques exactes.]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size)

#### Objets de l'API Android

Le [paramètre`android_priority` ]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) accepte les valeurs "normal" ou "élevé" pour spécifier la priorité de l'expéditeur FCM. Par défaut, les messages de notification sont envoyés avec une priorité élevée et les messages de données avec une priorité normale.

Pour plus d'informations sur l'impact des différentes valeurs sur la réception/distribution, voir [Priorité des messages Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority/).

#### SDK

Utilisez [le débogueur intégré au SDK de Braze]({{site.baseurl}}/developer_guide/platform_wide/debugging/) pour résoudre les problèmes de vos canaux alimentés par le SDK sans avoir à activer la journalisation verbeuse dans votre application.

#### Activités en direct

Nous avons mis à jour la [foire aux questions]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) sur les activités en ligne/instantanées de Swift avec quelques nouvelles questions et réponses.

#### Événements personnalisés

Les [objets de propriété d'événement]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) qui contiennent des valeurs de tableau ou d'objet peuvent désormais avoir une charge utile de propriété d'événement pouvant aller jusqu'à 100 Ko.

#### Numéros de compartiment aléatoire

Utilisez la [réinscription aléatoire de l'audience avec des numéros de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) pour les tests A/B ou le ciblage de groupes d'utilisateurs spécifiques dans vos campagnes.

#### Extensions de segments

Vous pouvez [actualiser les extensions de segments selon une planification récurrente]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh) en sélectionnant la fréquence à laquelle les extensions seront actualisées (quotidienne, hebdomadaire ou mensuelle) et l'heure spécifique à laquelle l'actualisation aura lieu.

### Canaux robustes

#### SMS

Nous avons ajouté [Ajouter des paramètres U]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) TM pour montrer comment vous pouvez utiliser des paramètres UTM dans un message SMS, afin que vous puissiez suivre les performances des campagnes dans des outils d'analyse/analytique tiers, tels que Google Analytics.

#### Landing pages

[Connectez votre propre domaine]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/connect_domain/) à votre espace de travail Braze pour personnaliser les URL de vos pages de destination avec votre marque.

#### LINE et Braze

{% multi_lang_include release_type.md release="Beta" %}

Nous avons ajouté une nouvelle documentation :

- [Types de messages LINE]({{site.baseurl}}/line/create/message_types/) couvre les types de messages LINE que vous pouvez composer, y compris les aspects et les limitations, et fait partie de la collection LINE beta.
- Le [lien avec le compte utilisateur]({{site.baseurl}}/line/line_setup/#user-account-linking) permet aux utilisateurs de relier leur compte LINE au compte utilisateur de votre application. Vous pouvez ensuite utiliser Liquid dans Braze, comme {% raw %}`{{line_id}}`{% endraw %}, pour créer une URL personnalisée pour l'utilisateur qui transmet son LINE ID à votre site Web ou à votre application, qui peut alors être associée à un utilisateur connu.

#### WhatsApp et Braze

Les [comptes WhatsApp Business (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) peuvent désormais être partagés avec plusieurs fournisseurs de solutions professionnelles.

### Nouveaux partenariats Braze

#### Future Anthem - Contenu dynamique

Le partenariat entre Braze et [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) s'appuie sur l'intelligence artificielle Amplifier pour offrir une personnalisation du contenu, des expériences en temps réel et des audiences dynamiques. L'intelligence artificielle Amplifier fonctionne dans les sports, les casinos et les loteries, vous permettant d'améliorer les profils de joueurs de Braze avec des attributs de joueurs spécifiques à l'industrie, tels qu'un jeu favori, un score d'engagement, le prochain pari attendu, et plus encore.

### Paramètres

#### Cryptage au niveau du champ d'identification

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Grâce au [chiffrement au niveau du champ d'identification]({{site.baseurl}}/user_guide/data_and_analytics/field_level_encryption/), vous pouvez chiffrer de façon fluide/sans heurts les adresses e-mail avec AWS Key Management Service (KMS) afin de minimiser les informations personnelles identifiables (PII) partagées dans Braze. Le chiffrement remplace les données sensibles par du texte chiffré, c'est-à-dire des informations cryptées et non lisibles.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Swift 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [SDK Swift 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Ajout de la prise en charge de la [vérification stricte de la concurrence dans Swift 6](https://developer.apple.com/documentation/swift/adoptingswift6)
        - Les classes et types de données publics pertinents de Braze sont désormais conformes au protocole `Sendable` et peuvent être utilisés en toute sécurité dans tous les contextes de concurrence.
        - Les API réservées aux threads principaux sont désormais marquées par l'attribut `@MainActor`.
        - Nous vous recommandons d'utiliser Xcode 16.0 ou une version ultérieure pour profiter de ces fonctionnalités tout en minimisant le nombre d'avertissements générés par le compilateur. Les versions précédentes de Xcode peuvent toujours être utilisées, mais certaines fonctionnalités peuvent générer des avertissements.
    - Lors de l'intégration manuelle de la prise en charge des notifications push, il se peut que vous deviez mettre à jour la conformité `UNUserNotificationCenterDelegate` pour utiliser l'attribut `@preconcurrency` afin d'éviter les avertissements.
        - L'application de l'attribut `@preconcurrency` sur la conformité du protocole n'est disponible que dans Xcode 16.0 ou une version ultérieure. Consultez notre exemple de code d'intégration [ici.](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual)
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - Mise à jour des liens de la version native d'Android du [SDK Android de Braze 31.1.0 à 32.1.0.](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Met à jour les liaisons de la version native d'iOS du [SDK Swift de Braze 10.3.0 vers 11.0.0.](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [SDK Swift 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [SDK Android 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Mise à jour de Kotlin de 1.8 à Kotlin 2.0.
- [SDK Web 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## Libération le 17 septembre 2024

### Flexibilité des données

#### Braze Cloud Data Ingestion pour S3

Vous pouvez utiliser [Cloud Data Ingestion (CDI) for S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) pour intégrer directement un ou plusieurs compartiments S3 de votre compte AWS à Braze. Lorsque de nouveaux fichiers sont publiés sur S3, un message est envoyé à SQS et Braze Cloud Data Ingestion prend en charge ces nouveaux fichiers.

#### Utilisateurs actifs par mois CY 24-25

Pour les clients qui ont acheté Utilisateurs actifs par mois - CY 24-25, Braze gère différentes limites de débit sur son endpoint `/users/track`. Pour plus de détails, reportez-vous à [POST : Suivre les utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### Libérer la créativité

#### Modélisation de produits de catalogue comprenant des étiquettes Liquid

{% multi_lang_include release_type.md release="Accès anticipé" %}

Utilisez l'indicateur `:rerender` dans une balise Liquid pour [afficher le contenu Liquid d'un article de catalogue]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). Par exemple, si vous rendez le contenu Liquid suivant :

{% raw %}
```liquid
Hi ${first_name}
{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

L'affichage est le suivant :

{% raw %}
```
Hi Peter,
Welcome to our store, Peter!
```
{% endraw %}

### Canaux robustes

#### Messages de réponse WhatsApp

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez utiliser les [messages de réponse]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) pour répondre aux messages WhatsApp entrants de vos utilisateurs. Ces messages sont créés in-app sur Braze pendant votre expérience sur la composition et peuvent être modifiés à tout moment. Vous pouvez utiliser Liquid pour faire correspondre la langue du message de réponse aux utilisateurs appropriés.

#### Modèles de canvas

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Créez des [modèles de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/) pour affiner votre envoi de messages en créant un cadre cohérent qui peut être facilement personnalisé pour s'adapter à vos objectifs spécifiques sur l'ensemble de vos Canvas.

#### Landing pages

{% multi_lang_include release_type.md release="Beta" %}

Les [pages d'atterrissage de Braze]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) sont des pages web autonomes qui peuvent piloter votre stratégie d'acquisition et d'engagement des utilisateurs.

#### Changements depuis la dernière consultation

Vous pouvez consulter le nombre de mises à jour de vos [Teams]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), campagnes et [segments]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) par d'autres membres de votre équipe en vous référant à l'indicateur *Changements depuis le dernier affichage* sur les pages d'aperçu respectives (comme la page d'aperçu d'une [campagne d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)). 

#### Résolution des problèmes liés aux demandes de webhook et de contenu connecté 

[Cet article]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) explique comment résoudre les codes d'erreur de webhook et de contenu connecté, notamment la nature des erreurs et les étapes pour les résoudre.

### Nouveaux partenariats Braze

#### Boîte de réception Monster - Analyse/analytique (si utilisé comme adjectif)

[Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) est une plateforme de signaux de boîte de réception qui aide les marques d'entreprise à faire atterrir chaque envoi. Il s'agit d'une suite intégrée de solutions pour la livrabilité, le rendu créatif et le contrôle des SMS, qui permet aux équipes modernes de gestion de la relation client (CRM) d'être plus efficaces et de mettre fin aux angoisses liées à l'envoi de messages.

#### SessionM - Loyauté

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) est une plateforme d'engagement et de fidélisation des clients qui offre des fonctionnalités de gestion de campagne et des solutions de gestion de la fidélisation pour aider les marketeurs à mener un ciblage de proximité afin d'augmenter l'engagement et le bénéfice.

### L'intelligence artificielle et l'automatisation de l’apprentissage machine.

#### Recommandations d'articles à la mode

Outre le modèle "AI Personalized", la fonctionnalité de [recommandations d'articles par l'intelligence artificielle]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) comprend également un modèle de recommandation pour "Trending", qui présente les articles qui ont eu l'élan le plus positif en ce qui concerne les interactions récentes avec les utilisateurs.

### Paramètres

#### Rôles

{% multi_lang_include release_type.md release="Disponibilité générale" %}

[Les rôles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) permettent une meilleure structuration en regroupant vos autorisations personnalisées individuelles avec les contrôles d'accès à l'espace de travail. Ceci est particulièrement utile si vous avez plusieurs marques ou espaces de travail régionaux dans un seul tableau de bord. Grâce aux rôles, vous pouvez ajouter les utilisateurs du tableau de bord aux bons espaces de travail et leur accorder directement les autorisations associées. 

#### Rapport sur les événements de sécurité

Nous avons ajouté une liste complète des [événements de sécurité]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) qui peuvent apparaître dans votre rapport de sécurité téléchargé.

#### Rapport sur l'utilisation des messages

{% multi_lang_include release_type.md release="Accès anticipé" %}

Le [tableau de bord de l'utilisation des messages]({{site.baseurl}}/message_usage/) fournit en libre-service des informations sur votre utilisation des crédits SMS et WhatsApp pour une vue d'ensemble de l'utilisation historique et actuelle par rapport aux attributions contractuelles. Ces informations peuvent réduire votre confusion et vous aider à faire des ajustements pour prévenir les risques de dépassement.

### SDK

#### Initialisation retardée pour le SDK Braze Swift

Configurez l'[initialisation différée]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/) pour initialiser votre SDK Braze Swift de manière asynchrone tout en veillant à ce que la gestion des notifications push soit préservée. Cela peut être utile lorsque vous devez configurer d'autres services avant d'initialiser le SDK, par exemple pour récupérer des données de configuration sur un serveur ou attendre le consentement de l'utilisateur.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segment Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [SDK Swift 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - Cette version nécessite désormais Cordova Android 13.0.0.
    - Reportez-vous à l'[annonce de la version de Cordova](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html) pour une liste complète des exigences en matière de dépendances du projet.- Mise à jour du pont Android natif de Braze [Android SDK 30.3.0 à 32.1.0.](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 9.2.0 vers 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK Swift 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - Mise à jour du pont natif Android [du SDK Android de Braze 30.3.0 vers 32.1.0.](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 9.0.0 vers 10.1.0.](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Braze Segmentation Swift Plugin 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - Met à jour les bindings du SDK Swift de Braze pour exiger les versions de la dénomination `10.2.0+` SemVer.
        - Cela permet la compatibilité avec n'importe quelle version du SDK de Braze, de `10.2.0` jusqu'à, mais sans inclure, `11.0.0`.
        - Reportez-vous au journal des modifications de [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) pour plus d'informations sur les ruptures potentielles.
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - Mise à jour du pont natif Android [du SDK Android de Braze 30.4.0 vers 32.1.0.](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - Modifie le comportement de `wipeData()` sur Android pour conserver les abonnements externes (comme `subscribeToContentCards()`) après avoir été appelé.
    - Met à jour le pont natif iOS [du SDK Swift de Braze 9.0.0 vers 10.2.0.](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [SDK Swift 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

## Libération le 20 août 2024

### Nouveaux cas d'utilisation

#### Catalogues

Vous pouvez ajouter n’importe quel type de données à un catalogue. Généralement, les données sont des métadonnées sur les offres, telles que les produits, les remises, les promotions, les événements, etc. Lisez nos [cas d'utilisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) et découvrez comment vous pouvez utiliser ces données pour cibler les utilisateurs avec des messages très pertinents.

#### Intelligence Suite

La suite Intelligence offre des fonctionnalités puissantes pour analyser l'historique des utilisateurs et les performances des campagnes et des Canvas, puis procéder à des ajustements automatiques pour augmenter l'engagement, l'audience et les conversions. Pour quelques exemples de la façon dont ces fonctionnalités peuvent bénéficier à différents secteurs, consultez nos [cas d'utilisation]({{site.baseurl}}/user_guide/brazeai/intelligence).

### Mise à jour du tableau de bord de la maison

Vous pouvez [reprendre là où vous vous étiez arrêté]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off) dans le tableau de bord de Braze en accédant facilement aux fichiers que vous avez récemment modifiés ou créés. Cette section apparaît en haut de la page d **'accueil** du tableau de bord de Braze.

### Flexibilité des données

#### Modèles de transformation des données et nouvelle destination

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Créez votre transformation de données à l'aide de notre [bibliothèque de modèles]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-2-create-a-transformation) dédiée pour vous aider à démarrer avec certaines plateformes externes, au lieu du code par défaut. Vous pouvez maintenant sélectionner **POST : Envoyez des messages immédiatement via l'API Seul** comme destination pour transformer les webhooks d'une plateforme source afin d'envoyer des messages immédiats à vos utilisateurs.

#### Fusionner des utilisateurs en masse

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Si vous rencontrez des profils utilisateurs en double, vous pouvez [fusionner ces utilisateurs en bloc]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) afin de rendre vos données plus cohérentes.

#### Exporter des attributs personnalisés

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez [exporter la liste des attributs personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data) sous forme de fichier CSV en sélectionnant **Exporter tout** dans la page **Attributs personnalisés**. Le fichier CSV sera généré et un lien de téléchargement vous sera envoyé par e-mail.

#### Liste actuelle des adresses IP autorisées

Braze enverra des données Currents à partir des IP répertoriées, qui sont automatiquement et dynamiquement ajoutées à toutes les clés API qui ont fait l'objet d'un abonnement à la [liste d'autorisation]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents).

### Canaux robustes

#### Nouvelle expérience de générateur de segmentation

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Créez un segment à l'aide de notre [expérience actualisée]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment). Les segments sont mis à jour en temps réel en fonction des modifications de données, et vous pouvez créer autant de segments que nécessaire pour remplir vos objectifs de ciblage et de communication.

#### Indicateurs par segments

Utilisez les modèles de rapport de [Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) pour décomposer les indicateurs de performance des campagnes, Canvas, variantes et étapes par segments.

#### Acquisition de numéro de téléphone

Pour utiliser le canal de messagerie WhatsApp, vous aurez besoin d'un numéro de téléphone qui répond aux exigences de WhatsApp pour son [API Cloud](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [API sur site](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers). 

Vous devez acquérir votre numéro de téléphone vous-même, car Braze ne fournira pas le numéro pour vous. Vous pouvez soit acheter un téléphone physique avec une carte SIM auprès de votre fournisseur de téléphonie professionnelle, soit utiliser l'un de nos partenaires : Twilio ou Infoblip. **Vous devez disposer de votre propre compte Twilio ou Infobip car cela ne peut pas être fait via Braze.**

### Nouveaux partenariats Braze

#### Zendesk Chat - Chat instantané

L'intégration de Braze et de [Zendesk Chat]({{site.baseurl}}/partners/zendesk_chat/) utilise les webhooks de chaque plateforme pour établir une conversation SMS bidirectionnelle. Lorsqu'un utilisateur demande de l'aide, un ticket est créé dans Zendesk. Les réponses des agents sont transmises à Braze par le biais d'une campagne SMS déclenchée par l'API, et les réponses des utilisateurs sont renvoyées à Zendesk.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 32.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SDK Swift 10.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Les changements suivants ont été apportés lors de l'abonnement aux événements Push avec [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)):
        - La fermeture de `update` sera désormais déclenchée par défaut par les événements "Push Opened" et "Push Received". Auparavant, il n'était déclenché que par les événements "Push Opened".
            - Pour continuer à vous abonner uniquement aux événements "Push Opened", indiquez `[.opened]` pour le paramètre `payloadTypes`. Vous pouvez également mettre en œuvre votre fermeture `update` pour vérifier que le `type` provenant du `Braze.Notifications.Payload` est le `.opened`.
        - Lors de la réception d'une notification push avec `content-available: true`, l'élément [`Braze.Notifications.Payload.type`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type) sera désormais `.received` au lieu de `.opened`.
    - Marque les API dépréciées suivantes comme indisponibles :
        - `Braze.Configuration.Api.Flavor`
        - `Braze.Configuration.Api.flavor`
        - `Braze.Configuration.Api.SdkMetadata`
        - `Braze.Configuration.Api.addSdkMetadata(_:)`
        - `Braze.ContentCard.ClickAction.uri(_:useWebview:)`
        - `Braze.ContentCard.ClickAction.uri`
        - `Braze.InAppMessage.ClickAction.uri(_:useWebview:)`
        - `Braze.InAppMessage.ClickAction.uri`
        - `Braze.InAppMessage.ModalImage.imageUri`
        - `Braze.InAppMessage.Full.imageUri`
        - `Braze.InAppMessage.FullImage.imageUri`
        - `Braze.InAppMessage.Themes.default`
        - `Braze.deviceId(queue:completion:)`
        - `Braze._objc_deviceId(completion:)`
        - `Braze.deviceId()`
        - `Braze.User.setCustomAttributeArray(key:array:fileID:line:)`
        - `Braze.User.addToCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User._objc_addToCustomAttributeArray(key:value:)`
        - `Braze.User._objc_removeFromCustomAttributeArray(key:value:)`
        - `gifViewProvider`
        - `GifViewProvider.default`
    - Supprime les API obsolètes :
        - `Braze.Configuration.DeviceProperty.pushDisplayOptions`
        - `Braze.InAppMessageRaw.Context.Error.extraProcessClickAction`
    - Supprime la classe dépréciée `BrazeLocation` en faveur de `BrazeLocationProvider`.
- [Xamarin SDK Version 6.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Ajout de la prise en charge de .NET 8.0 pour les liaisons iOS et Android, car .NET 7.0 a atteint la fin de sa durée de vie.
        - Cela supprime la prise en charge de .NET 7.0.
    - Mise à jour de la liaison Android de Braze [Android 30.4.0 à 32.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour de la liaison iOS du [SDK Swift de Braze 9.0.0 vers 10.0.0.](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - Lorsque vous vous abonnez à des événements de notification push, l'abonnement sera déclenché sur iOS à la fois pour les événements "Push reçu" et "Push ouvert", au lieu de l'être uniquement pour les événements "Push ouvert".
- [React Native SDK 12.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/12.0.0/CHANGELOG.md)
    - Met à jour les liaisons de la version native iOS du [SDK Swift de Braze 9.0.0 à 10.0.0.](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - Lorsque vous vous abonnez à des événements de notification push, l'abonnement sera déclenché sur iOS pour les événements `push_received` et `push_opened`, au lieu de seulement pour `push_opened`.

## Libération le 23 juillet 2024

### Mises à jour de la documentation de Braze

#### Diátaxis et documentation de Braze

Nous sommes en train de normaliser notre documentation à l'aide d'un cadre appelé [Diátaxis.](https://diataxis.fr/) Pour aider nos rédacteurs et contributeurs à créer des contenus qui s'inscrivent dans ce nouveau cadre, nous avons créé des [modèles pour chaque type de contenu.]({{site.baseurl}}/contributing/content_types)

#### Nouveau modèle de demande d'intervention pour Braze Documentation

Nous avons pris le temps d'améliorer notre modèle de demande de retrait (PR) afin qu'il soit plus facile et moins déroutant de [contribuer à Braze Docs.]({{site.baseurl}}/contributing/home/) Si vous pensez qu'il y a encore des améliorations à apporter, ouvrez un PR ou [soumettez un problème.](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=) Tout ce qui est le plus facile !
 
### Flexibilité des données

#### Exporter des événements et attributs personnalisés

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais exporter des événements personnalisés et des attributs personnalisés à l'aide des boutons [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) et [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) endpoints.

#### Nouvelles autorisations pour les utilisateurs de Currents

Il existe deux nouveaux paramètres d'autorisation pour les utilisateurs : **Visualiser les intégrations currents** et **modifier les intégrations currents**. En savoir plus sur les [autorisations des utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions). 

#### Mise à jour de la politique de conservation des données de Snowflake
 
À compter du 27 août 2024, les informations personnelles identifiables (IPI) seront supprimées de toutes les données des événements de partage sécurisé des données de Snowflake datant de plus de deux ans. Si vous utilisez Snowflake, vous pouvez choisir de conserver l'intégralité des données relatives aux événements dans votre environnement en stockant une copie dans votre compte Snowflake avant l'application de la politique de conservation. En savoir plus sur la [conservation des données par Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/).
 
### Libérer la créativité

#### Messages in-app multipages

{% multi_lang_include release_type.md release="Disponibilité générale" %}

L'ajout de pages à votre message in-app vous permet de guider les utilisateurs à travers un flux séquentiel, comme un flux d'onboarding ou un parcours de bienvenue. Pour en savoir plus, consultez la section [Créer un message in-app par glisser-déposer.]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page)

#### Raccourcissement de lien avec Liquid

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Utilisez [Liquid pour personnaliser les]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening) URL afin de raccourcir automatiquement les URL contenues dans les messages SMS et de recueillir des analyses sur le taux de clics. Pour l'essayer, voir [Link shortening.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/)

#### Exemples d'API pour les catalogues

Nous avons ajouté des exemples pour l'endpoint `/catalogs` utilisant des champs de type tableau. Pour voir les exemples, consultez les pages suivantes :

- [modifier plusieurs produits du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [Créer plusieurs produits du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [Mettre à jour les produits du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [Éditer un produit du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [Créer un produit du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [Mettre à jour un produit du catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [Créer un catalogue]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### Canaux robustes

### Plusieurs comptes WhatsApp Business

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais ajouter plusieurs comptes WhatsApp Business et groupes d'abonnement (et numéros de téléphone) à chaque espace de travail. Pour plus d'informations, consultez la section [Plusieurs comptes WhatsApp Business.]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups) 

#### Autorisations géographiques des SMS

Les autorisations géographiques pour les SMS renforcent la sécurité et protègent contre le trafic frauduleux de SMS en appliquant des contrôles sur les pays auxquels vous pouvez envoyer des messages SMS. Pour savoir comment spécifier une liste de pays autorisés afin de vous assurer que les messages SMS ne sont envoyés qu'aux régions approuvées, reportez-vous à la section [Configuration de votre liste de pays autorisés pour les SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist)

#### LINE et Braze

{% multi_lang_include release_type.md release="Beta" %}

[LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf) est l'application de messages la plus populaire au Japon, avec plus de 95 millions d'utilisateurs actifs par mois. Vous pouvez intégrer vos comptes LINE à Braze pour exploiter vos données clients zero-party et first-party afin d'envoyer des messages LINE attrayants aux bons clients en fonction de leurs préférences, de leurs comportements et de leurs interactions cross-canal. Pour commencer, voir [LINE]({{site.baseurl}}/line).

#### Shopify : Baisse des prix et retour en stock

{% multi_lang_include release_type.md release="Accès anticipé" %}

Désormais, avec Shopify, vous pouvez créer des notifications personnalisées pour les [baisses de prix]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) et les [articles en rupture de stock]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications).
 
### L'intelligence artificielle et l'automatisation de l’apprentissage machine.
 
#### Fusion basée sur des règles pour les utilisateurs en double

Auparavant, vous pouviez rechercher et fusionner les utilisateurs en double dans Braze, individuellement ou en masse. Vous pouvez désormais créer des règles pour contrôler la manière dont les doublons sont résolus, afin que l'utilisateur le plus pertinent soit conservé. Pour en savoir plus, consultez la section [Fusion basée sur des règles]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

#### Assistant Liquid avec IA

{% multi_lang_include release_type.md release="Beta" %}

L'assistant Liquid avec IA est un assistant de chat alimenté par BrazeAI<sup>TM</sup> qui aide à générer le code Liquid dont vous avez besoin pour personnaliser le contenu des messages. Vous pouvez générer du code Liquid à partir de modèles, recevoir des suggestions de balises Liquid personnalisées et optimiser les balises Liquid existantes avec l'aide de BrazeAI<sup>TM</sup>. L'assistant Liquid de l'intelligence artificielle fournit également des annotations expliquant le Liquid utilisé, ce qui vous permet d'améliorer votre compréhension du Liquid et d'apprendre à écrire le vôtre.

Pour commencer, consultez l'[assistant Liquid avec IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_liquid).
 
### SDK
 
#### Journaux du SDK Android

Nous avons remanié la [documentation sur la journalisation pour le SDK Android de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging), afin qu'elle soit plus facile à lire et à utiliser dans votre application. Nous avons également ajouté des descriptions pour chaque niveau d'enregistrement.

#### SDK iOS notifications push en avant-plan

La méthode `subscribeToUpdates` du SDK iOS de Braze peut désormais détecter si une notification push au premier plan est reçue. Pour en savoir plus, consultez l'[intégration des notifications push d'iOS.]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration)
 
#### Mise à jour de la documentation Xamarin
 
Depuis la [version 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0), le SDK Xamarin de Braze utilise le binding du SDK Swift, nous avons donc mis à jour les extraits de code et le matériel de référence. Nous avons également restructuré la section pour la rendre plus facile à lire et à comprendre. Pour le vérifier, consultez [la documentation de Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup).

#### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.
 
- [SDK Swift 9.3.1](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.1)
- [SDK Web 5.3.2](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#532)
    - Correction d'une régression introduite dans la version 5.2.0 qui pouvait entraîner un rendu incorrect des messages in-app HTML lorsqu'un script externe est chargé de manière synchrone.
- [SDK Web 5.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#540)

## Libération le 25 juin 2024

### Documentation japonaise

Nous prenons désormais en charge la langue japonaise pour la documentation de Braze !

![Le site Braze Docs affichant l'interface japonaise]({% image_buster /assets/img/braze-docs-japan.png %}){: style="max-width:70%;"}
 
### Flexibilité des données

#### Pièces jointes pour les campagnes déclenchées par l'API

{% multi_lang_include release_type.md release="Disponibilité générale" %}

L'[endpoint`/campaigns/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) prend désormais en charge les pièces jointes (tout comme l'endpoint `/messages/send` prend en charge les pièces jointes pour les e-mails). 

#### Soutien supplémentaire à l'entrepôt de données

{% multi_lang_include release_type.md release="Accès anticipé" %}

Braze [Cloud Data Ingestion (CDI)]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources) prend désormais en charge BigQuery, Databricks, Redshift et Snowflake.

#### Migration du numéro de téléphone WhatsApp

Migrez votre numéro de téléphone WhatsApp entre les comptes WhatsApp Business en utilisant la signature intégrée de Meta. En savoir plus sur la [migration des numéros de téléphone WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration).
 
### Libérer la créativité

#### Engagement par appareil

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Le nouveau rapport sur l **'engagement par appareil** fournit une ventilation des appareils utilisés par vos utilisateurs pour s'engager dans votre e-mail. Ces données permettent de suivre l'engagement des e-mails sur les mobiles, les ordinateurs de bureau, les tablettes et d'autres types d'appareils. En savoir plus sur le [rapport et le tableau de bord des performances de l'e-mail]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard).

#### Propriétés Liquid de WhatsApp et SMS dans le flux Canvas

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Nous avons ajouté la prise en charge des [propriétés WhatsApp et SMS Liquid dans le flux Canvas.]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) Désormais, lorsqu'une étape du parcours action contient un déclencheur "Envoi d'un message SMS entrant" ou "Envoi d'un message WhatsApp entrant", les étapes du canvas suivantes peuvent inclure une propriété SMS ou WhatsApp Liquid. Cela reflète le fonctionnement des propriétés d'événement dans Canvas Flow. Vous pouvez ainsi tirer parti de vos messages pour enregistrer et référencer des données first-party sur les profils utilisateurs et les envois de messages conversationnels.
 
#### Chemins personnalisés en toiles récurrentes

{% multi_lang_include release_type.md release="Accès anticipé" %}

Les parcours personnalisés dans les Canvas vous permettent de personnaliser n'importe quel point d'un parcours Canvas pour des utilisateurs individuels en fonction de la probabilité de conversion. Désormais, les chemins personnalisés sont disponibles pour les toiles récurrentes. En savoir plus sur les [variantes personnalisées]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths).

#### Résolution des problèmes des segmentations

Travailler avec des segments ? Voici quelques [étapes de résolution des problèmes et considérations]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting) à garder à l'esprit.

#### Surlignage Liquid

Nous avons amélioré le [code couleur utilisé par Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) pour mieux prendre en compte les directives en matière d'accessibilité.

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### Canaux robustes

#### Autorisations géographiques pour les SMS

{% multi_lang_include release_type.md release="Accès anticipé" %}

Les autorisations géographiques pour les SMS renforcent la sécurité et protègent contre le trafic frauduleux de SMS en appliquant des contrôles sur les pays auxquels vous pouvez envoyer des messages SMS. Les administrateurs peuvent désormais spécifier une liste de pays autorisés afin de s'assurer que les messages SMS ne sont envoyés qu'aux régions approuvées. Pour plus d'informations, reportez-vous à la section [Autorisations géographiques SMS.]({{site.baseurl}}/sms_geographic_permissions) 

![Le menu déroulant "Liste blanche des pays" avec les pays les plus courants affichés en haut.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### Meilleures pratiques pour les SMS/MMS

En savoir plus sur les [meilleures pratiques pour les SMS/MMS avec Braze]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices), y compris nos recommandations pour le contrôle de l'abonnement et le pompage du trafic. 

#### Suivi des désabonnements aux services de push

Consultez notre nouvel [article d'aide]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) pour obtenir des conseils sur le suivi des désabonnements par push.

#### Shopify `checkout.liquid` deprecation

Veuillez noter que la prise en charge de Shopify `checkout.liquid` commencera à être obsolète en août 2024 et se terminera en août 2025. En savoir plus sur la manière dont Braze va [gérer cette transition.]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout) 

### Mises à jour SDK
 
Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.
 
- [SDK Swift 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - Déclasse les API de signalisation des fonctionnalités existantes, qui seront supprimées dans une prochaine version :
        - `Braze.FeatureFlag.jsonStringProperty(key:)` a été supprimée.
        - `Braze.FeatureFlag.jsonObjectProperty(key:)` a été abandonné au profit de `Braze.FeatureFlag.jsonProperty(key:)`.
- [SDK Roku 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Braze Expo Plugin 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### Documentation tvOS

Il y a quelques mois, les articles pour les [cartes de contenu tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos) et les [messages in-app]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos) ont été dépréciés par erreur. Ces documentations ont été republiées dans la section Swift de Braze Docs.

{% alert note %}
[Les contributeurs]({{site.baseurl}}/contributing/home) à la documentation de Braze doivent noter que le site fonctionne désormais avec Ruby 3.3.0. Veuillez mettre à jour votre version de Ruby si nécessaire.
{% endalert %}

## Version du 28 mai 2024

### Mises à jour visuelles du site de documentation

Vous avez peut-être remarqué que notre site web de documentation a un nouveau look ! Nous l'avons remanié pour refléter la nouvelle identité vibrante de la marque Braze. Pour découvrir les coulisses de notre nouvelle marque, consultez le site [Unveiling Our New Brand : Une conversation avec Greg Erdelyi, directeur créatif exécutif de Braze](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi).

### Prise en charge du portugais et de l'espagnol

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Braze est désormais disponible en portugais et en espagnol. Pour modifier la langue dans laquelle le tableau de bord de Braze s'affiche, reportez-vous à la section [Paramètres de langue]({{site.baseurl}}/user_guide/administrative/access_braze/language/).

### Canaux robustes

#### Paramètres multilingues

{% multi_lang_include release_type.md release="Disponibilité générale" %}

En ajustant les [paramètres multilingues]({{site.baseurl}}/multi_language_support/), vous pouvez cibler les utilisateurs dans différentes langues et emplacements avec des messages différents dans un seul e-mail. Pour modifier et gérer la prise en charge multilingue, vous devez disposer du droit d'utilisateur "Gérer les paramètres multilingues". Pour ajouter des paramètres linguistiques à un message, vous devez disposer des autorisations nécessaires pour modifier les campagnes.

#### En-tête de liste de désabonnement en un clic au niveau du message

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Le désabonnement en un clic pour l'en-tête list-unsubscribe[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) permet aux destinataires de se désabonner facilement des e-mails. Vous pouvez ajuster ce paramètre d'en-tête pour qu'il soit appliqué au niveau d'un message dans vos e-mails. Pour plus d'informations sur ce paramètre, reportez-vous à la section [En-tête de désabonnement par e-mail dans les espaces de travail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces).

#### À propos de l'assainissement des e-mails

Consultez notre nouvel article sur l'[assainissement]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization) pour en savoir plus sur le processus qui se produit lorsque Braze détecte un type spécifique de JavaScript dans votre message e-mail. Son objectif principal est d'empêcher les acteurs malveillants d'accéder aux données de session des autres utilisateurs du tableau de bord de Braze.

#### Nombre d'inclusions pour les blocs de contenu

Après avoir ajouté un bloc de contenu dans une campagne ou un canvas actif, vous pouvez [prévisualiser ce bloc de contenu]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) à partir de la bibliothèque des blocs de contenu en plaçant le pointeur de la souris sur le bloc de contenu et en sélectionnant l'icône de <i class="fa fa-eye preview-icon"></i> **prévisualisation**.

#### Statuts des canevas

Sur le tableau de bord de Braze, vos toiles sont regroupées en fonction de leur statut. Consultez les différents [états et descriptions de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) pour en connaître la signification.

### L'intelligence artificielle et l'automatisation de l’apprentissage machine.

#### Lignes directrices de la marque pour l'assistant de rédaction de l'intelligence artificielle.

{% multi_lang_include release_type.md release="Disponibilité générale" %}

Vous pouvez désormais créer et appliquer des [directives de marque]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/) pour personnaliser le style du texte généré par l'assistant de rédaction de l'intelligence artificielle afin qu'il corresponde à la voix de votre marque. Établissez plusieurs lignes directrices pour différents scénarios afin de vous assurer que votre ton est toujours adapté au contexte.
 
### Nouveaux partenariats Braze

#### Adikteev - Analyse

L'intégration de Braze et d'[Adikteev]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/) vous permet de stimuler la rétention des utilisateurs en exploitant la technologie de prédiction du taux d'attrition d'Adikteev au sein des campagnes CRM de Braze afin de cibler en priorité les segments d'utilisateurs désabonnés.
 
#### Celebrus - Analyse
 
L'intégration de Braze et [Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus) fonctionne parfaitement avec le SDK de Braze sur les canaux du web et des applications mobiles, facilitant ainsi la génération des données d'activité des canaux dans Braze. Il s'agit notamment d'informations complètes sur le trafic des visiteurs sur l’ensemble des ressources numériques au cours de périodes déterminées.
 
#### IAM Studio - Modèles de messages
 
Grâce à l'intégration de Braze et d'[IAM Studio]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/), vous pouvez facilement insérer des modèles de messages in-app personnalisables dans vos messages in-app de Braze, offrant un remplacement d'image, une modification du texte, des paramètres de liens profonds, des attributs personnalisés et des paramètres d'événements. Grâce à IAM Studio, vous pouvez réduire le temps de production des messages et consacrer plus de temps à la planification du contenu.
 
#### Regal - Chat instantané

En intégrant Braze et [Regal]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/), vous pouvez créer une expérience plus cohérente et personnalisée sur tous les points de contact avec vos clients.

#### Treasure data - Importation de la cohorte
 
Grâce à l'intégration de Braze et [Treasure Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/), vous pouvez importer des cohortes d'utilisateurs de Treasure Data vers Braze afin d'envoyer des campagnes ciblées basées sur des données susceptibles de n'exister que dans votre entrepôt.
 
#### Zapier - Automatisation du flux de travail
 
Le partenariat entre Braze et [Zapier]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/) s'appuie sur l'API Braze et les webhooks Braze pour se connecter à des applications tierces afin d'automatiser diverses actions.

### Mises à jour SDK
 
Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Plugin Braze Segment Swift 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - Met à jour les interfaces de liaison du SDK Swift de Braze pour qu'il exige les versions 9.2.0+ SemVer.
        - Cela permet d'assurer la compatibilité avec toutes les versions du SDK de Braze, de la version 9.2.0 à la version 10.0.0.
        - Consultez le journal des modifications des versions [7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700), [8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800) et [9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900) pour plus d'informations sur les disruptions potentielles.
    - La prise en charge des notifications push nécessite désormais un appel à la méthode statique `BrazeDestination.prepareForDelayedInitialization()` le plus tôt possible dans le cycle de vie de l'application, dans la méthode `AppDelegate.application(_:didFinishLaunchingWithOptions:)` de votre application.
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 7.7.0 vers 9.0.0.](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Expo Plugin 2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [Swift SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 7.7.0 vers 9.0.0.](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif Android [du SDK Android de Braze 29.0.1 vers 30.3.0.](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [SDK Web 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDK Version 5.0.0
    - Mise à jour de l’[interface de liaison iOS du SDK Swift de Braze 8.4.0 vers 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
