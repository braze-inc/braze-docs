---
nav_title: Notes de version
article_title: Notes de version
page_order: 4
layout: en vedette
guide_top_header: "Notes de version"
guide_top_text: "C'est là que vous pouvez trouver toutes les mises à jour de la plateforme de Braze, avec les <a href='/docs/help/release_notes/#most-recent'>mises à jour les plus récentes de la plateforme</a>, listées ci-dessous. Vous pouvez également\nconsulter nos journaux de modifications <a href='/docs/developer_guide/platform_integration_guides/sdk_changelogs/'>SDK</a>."
page_type: atterrissage
description: "Cette page d'accueil accueille les notes de version de Braze. C'est ici que vous pouvez trouver toutes les mises à jour de la plateforme Braze et des SDKs, ainsi qu'une liste des fonctionnalités obsolètes."
guide_featured_title: "Notes de version"
guide_featured_list:
  - 
    name: 2022
    link: /fr/docs/help/release_notes/2022/
    fa_icon: fas fa-calendar-alt
  - 
    name: 2021
    link: /fr/docs/help/release_notes/2021/
    fa_icon: fas fa-calendar-alt
  - 
    name: 2020
    link: /fr/docs/help/release_notes/2020/
    fa_icon: fas fa-calendar-alt
  - 
    name: 2019
    link: /fr/docs/help/release_notes/2019/
    fa_icon: fas fa-calendar-alt
  - 
    name: 2018
    link: /fr/docs/help/release_notes/2018/
    fa_icon: fas fa-calendar-alt
  - 
    name: 2017
    link: /fr/docs/help/release_notes/2017/
    fa_icon: fas fa-calendar-alt
  - 
    name: 2016
    link: /fr/docs/help/release_notes/2016/
    fa_icon: fas fa-calendar-alt
  - 
    name: Dépréciations
    link: /fr/docs/help/release_notes/deprecations/
    fa_icon: fa-calendar-times loin
  - 
    name: Historique des modifications du SDK
    link: /fr/docs/developer_guide/platform_integration_guides/sdk_changelogs/
    fa_icon: fas fa-file-code
---

# Notes de version les plus récentes de Braze {#most-recent}

> Braze publie des informations sur les mises à jour des produits sur une cadence mensuelle, en s'alignant sur les principales versions du produit, bien que le produit soit mis à jour avec des améliorations diverses semaine à semaine. <br> <br> Pour plus d'informations sur l'une des mises à jour listées dans cette section, contactez votre responsable de compte ou [ouvrez un ticket de support][support]. Vous pouvez également consulter [nos Changelogs SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) pour voir plus d'informations sur nos versions, mises à jour et améliorations mensuelles du SDK.

# Février 2022

## Étape des chemins d'expérience de Canvas
La nouvelle Étape des chemins d'expérience de Canvas permet de suivre les performances des chemins en testant plusieurs chemins de Canvas les uns contre les autres et un groupe de contrôle à n'importe quel moment du parcours de l'utilisateur. Maintenant, vous pouvez tirer parti des analyses rassemblées ici pour déterminer quel chemin est le plus efficace. En savoir plus sur la façon de créer une [étape des chemins d'expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).

## Gestion des numéros de téléphone non valides
Vous avez rencontré un scénario où un utilisateur a entré un numéro de téléphone invalide. Voici votre solution! Braze marque ces numéros de téléphone non valides et ne tentera pas d'envoyer d'autres communications à ces numéros. En savoir plus sur la façon dont Braze [gère les numéros de téléphone non valides]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers/).

### Nouveaux points de terminaison SMS
Vous pouvez maintenant gérer des numéros de téléphone non valides en utilisant le nouveau [Braze SMS Endpoints]({{site.baseurl}}/api/endpoints/sms/)! Fonctionnalités de cette mise à jour :
- [GET: Interrogation ou liste de numéros de téléphone non valides]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) renvoie une liste de numéros de téléphone qui sont considérés comme « invalides » par Brésil.
- [POST: Supprimer les numéros de téléphone non valides]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) vous permet de supprimer les numéros de téléphone « invalides » de la liste invalide de Brase.

## Limites de taux
Les limites de taux de l'API ont été incluses pour tous les [articles Braze Endpoint]({{site.baseurl}}/api/basics/#nav_top_endpoints). Vous pouvez maintenant facilement voir les limites de taux par type de requête. Pour plus d'informations sur les limites de taux, consultez notre article sur [les limites de taux API]({{site.baseurl}}/api/api_limits/).

## Nouveau point de terminaison REST
Braze a ajouté un [nouveau point d'extrémité REST EU-02]({{site.baseurl}}/api/basics/#api-definitions).

## À propos de l'e-mail
Les messages électroniques sont un excellent moyen de se connecter avec vos clients. Pour une brève introduction sur la façon dont vous pouvez personnaliser et tirer parti des messages électroniques, consultez notre nouvel article sur [À propos de l'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/).

## À propos des messages dans l'application
Les messages intégrés fournissent un contenu enrichi à vos utilisateurs actifs dans votre application. Vous pouvez facilement vous engager auprès de vos clients actifs en créant des messages dans l'application pour des messages de vœux personnalisés ou l'adoption de fonctionnalités. Pour en savoir plus sur les avantages et les types de messages, consultez notre nouvel article sur [À propos des messages dans l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/).

## Janvier 2022

Bienvenue dans une nouvelle année !

### Mettre à jour pour exporter les utilisateurs par segment de terminaison

À partir de décembre 2021, les modifications suivantes prennent effet pour les [utilisateurs d'exporter par segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/):

1. Le champ `fields_to_export` dans cette requête API sera requis. L'option par défaut pour tous les champs sera supprimée.
2. Les champs pour `custom_events`, `achats`, `campagnes_received`, et `canvases_received` ne contiendra que les données des 90 derniers jours.

### Nouvelles propriétés pour les événements d'engagement de messages courants

De nouvelles propriétés ont été ajoutées pour la sélection des [événements d'engagement de message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/). Cette mise à jour s'applique aux événements d'engagement de messages courants suivants et à tous les partenaires qui les utilisent :

- Ajouter `LINK_ID`, `LINK_ALIAS` à :
  - Clique sur l'email (toutes les destinations)
- Ajouter `USER_AGENT` à :
  - Courriel ouvert
  - Email Click
  - Email Marquer comme spam
- Ajouter `MACHINE_OPEN` à :
  - Courriel ouvert

### Nouveau tag de personnalisation Liquid

Nous supportons maintenant le ciblage des utilisateurs qui ont activé la poussée au premier plan sur leur appareil avec les balises Liquid suivantes :

{% raw %}
- `{{most_recently_used_device.${foreground_push_enabled}}}`
- `{{targted_device.${foreground_push_enabled}}}`
{% endraw %}

Pour plus d'informations, reportez-vous à [balises de personnalisation supportées]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/).

### À propos des webhooks

Les Webhooks sont des outils puissants et flexibles, mais ils peuvent être un peu déroutants. Si vous vous demandez quels sont les webhooks et comment vous pouvez les utiliser au Brésil, consultez notre nouvel article sur [À propos des webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/).

### Personnaliser Amazon

Amazon Personalize est comme avoir votre propre système de recommandation automatique Amazon pour toute la journée. Basé sur plus de 20 ans d'expérience dans les recommandations, La personnalisation d'Amazon vous permet d'améliorer l'engagement de vos clients en faisant fonctionner en temps réel des recommandations de produits et de contenu personnalisés et des promotions marketing ciblées.

Si vous souhaitez en savoir plus, visitez notre nouvel article [Amazon Personalize]({{site.baseurl}}/partners/message_personalization/dynamic_content/amazon_personalize/amazon_personalize/) pour comprendre les cas d'utilisation que Amazon Personnalise les offres, les données avec lesquelles il fonctionne, comment configurer le service et comment l'intégrer avec Braze.

### Nouveaux partenariats Braze

#### Yotpo – commerce électronique

L'intégration de [Yotpo]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/yotpo/) et de Braze vous permet de tirer et d'afficher dynamiquement les notes des étoiles, les meilleurs commentaires, et le contenu visuel généré par les utilisateurs sur les produits dans les e-mails et les autres canaux de communication au Brésil. Vous pouvez également inclure des données de fidélisation au niveau du client dans les courriels et d'autres méthodes de communication pour créer une interaction plus personnalisée, boostant les ventes et fidélisation.

#### Zeotap – Plateforme de données client

Avec l'intégration de [Zeotap]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/zeotap/) et de Braze, vous pouvez étendre l'échelle et la portée de vos campagnes en synchronisant les segments de clients de Zeotap pour associer les données utilisateur à Braze. Vous pouvez ensuite agir sur ces données, en fournissant des expériences ciblées personnalisées à vos utilisateurs.

## Décembre 2021

### Métrique de rapport de taux cliquer-pour-ouvrir
Braze a ajouté une nouvelle métrique de courriel, cliquez pour ouvrir le taux, disponible dans le [Rédacteur de rapports]({{site.baseurl}}/user_guide/data_and_analytics/your_reports/report_builder/). Cette métrique représente le pourcentage d'emails ouverts qui ont été cliqués.

### Métrique de rapport d'ouverture de la machine

Une nouvelle métrique de courriel, [Machine Ouvre]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/analytics_glossary/#machine-opens), est disponible sur les pages Analytiques Canvas et Campagne pour les courriels. Cette métrique identifie les courriels qui ne sont pas humains (c'est-à-dire ouverts par les serveurs d'Apple), affichés sous la forme d'un sous-ensemble d'ouvertures totales.

### variable aléatoire_bucket_number Liquid
Une variable `random_bucket_number` a été ajoutée à la liste des [variables Liquid supportées]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#supported-personalization-tags) pour la personnalisation du message.

### Instructions de notification de push enrichi iOS 15
De nouvelles [directives de notification push iOS]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/rich_notifications/) ont été ajoutées à la documentation riche d'iOS, y compris des informations sur les états de notification et une répartition des variables de troncature de texte.

### IPs à la liste blanche dans l'UE pour les webhooks et le contenu connecté
Des adresses IP supplémentaires pour la liste blanche dans l'UE pour les webhooks et le contenu connecté ont été ajoutées à notre article [webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) et [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/). Ces nouvelles adresses IP incluent `18.157.135.97`, `3.123.166.46`, `3.64.27. 6`, `3.65.88.25`, `3.68.144.188`et `3.70.107.88`.

### Exporter le point de terminaison des achats
Un nouveau [GET: liste des identifiants de produits]({{site.baseurl}}/api/endpoints/export/purchases/get_list_product_id/) de terminaison a été ajouté au Brésil. Ce point de terminaison renvoie les listes paginées des identifiants de produit.

### Nouveaux partenariats Braze

#### Adobe - Plateforme de données client
L'intégration de Braze et [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/#adobe) permet aux marques de se connecter et de cartographier leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel. Les marques peuvent alors agir sur ces données, en fournissant des expériences personnalisées et ciblées à ces utilisateurs.

#### BlueConic - Plateforme de données client
Avec [Blueconic]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/blueconic/#blueconic), les utilisateurs de Braze peuvent unifier les données en permanent, les profils individuels et ensuite les synchroniser entre les points de contact des clients et les systèmes à l'appui d'un large éventail d'initiatives axées sur la croissance. y compris l'orchestration du cycle de vie des clients, la modélisation et l'analyse, les produits et expériences numériques, la monétisation basée sur le public et bien plus encore.

#### Valable - Contenu dynamique
L'intégration de Braze et de [Worthy]({{site.baseurl}}/partners/message_personalization/dynamic_content/worthy/#worthy) vous permet de créer facilement des personnalisés, riche expérience dans l'application en utilisant le glisser-déposer de l'éditeur de contenu dynamique de Worthy et en les livrant à travers Brésil.

#### Judo - Contenu dynamique
L'intégration [Judo]({{site.baseurl}}/partners/message_personalization/dynamic_content/judo/#judo) et Braze vous permet d'écraser les composants de votre campagne et de les remplacer par des expériences de Judo. Les données provenant de Braze peuvent être utilisées pour soutenir le contenu personnalisé dans une expérience de Judo. Les événements utilisateur et les données de l'expérience peuvent donner des commentaires sur Braze pour l'attribution et le ciblage.

#### Ligne - Messagerie
L'intégration [Line]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/line/#line) et Braze vous permet d'exploiter les webhooks de Braze, la segmentation avancée, des fonctionnalités de personnalisation et de déclenchement pour envoyer des messages à vos utilisateurs via l'API [Messagerie en ligne](https://developers.line.biz/en/docs/messaging-api/overview/).

#### Revenus - Paiements
L'intégration [RevenueCat]({{site.baseurl}}/partners/data_and_infrastructure_agility/payments/revenuecat/#revenuecat) et Braze vous permet de synchroniser automatiquement les événements d'achat et d'abonnement de vos clients sur des plates-formes. Cela vous permet de construire des campagnes qui réagissent à la phase de cycle de vie de l'abonnement de vos clients, comme s'engager avec les clients qui se sont retirés pendant leur essai gratuit ou envoyer des rappels aux clients avec des problèmes de facturation.

#### Punchh - Loyauté
[Punchh]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/punchh/#punchh) a établi un partenariat avec Braze pour synchroniser les données sur les deux plates-formes à des fins de don et de fidélité. Les données publiées à Braze seront disponibles pour la segmentation et pourront à nouveau synchroniser les données utilisateur avec Punchh via la configuration des modèles de webhook au Brésil.

## Novembre 2021

### Tableau de bord d'utilisation des points de données

Utilisez le tableau de bord **Utilisation totale de points de données** pour suivre le rythme d'utilisation de vos points de données par rapport à votre allocation de contrat. Ce tableau de bord fournit des informations sur votre contrat, le cycle de facturation en cours, les données de facturation de la société et les données de groupe d'applications. Pour plus d'informations, reportez-vous à [Abonnements et Utilisation]({{site.baseurl}}/user_guide/onboarding_with_braze/subscription_and_usage/#total-data-points-dashboard).

### Passer à la régénération d'extension de segment

À partir du 1er février 2022, le paramètre de régénération des extensions quotidiennes sera automatiquement désactivé pour les [extensions de segment non utilisées]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/). Braze définit les extensions inutilisées comme celles qui répondent aux critères suivants :

- Non utilisé dans aucune campagne active, Canvases ou segments actifs
- Non utilisé dans aucune campagne inactive (brouillon, arrêté, archivé), Canvases ou segments
- N'a pas été modifié depuis plus de 7 jours

Braze informera le contact de la société et le créateur de l'extension lorsque ce paramètre est désactivé. L'option de régénérer les extensions quotidiennement peut être activée à tout moment.

### Guides de mise en œuvre avancée Android

#### Cartes de contenu

Ce guide de mise en œuvre [optionnel et avancé]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/) couvre les considérations de code de la carte de contenu, trois cas d'utilisation personnalisée construits par notre équipe, des extraits de code accompagnateurs et des conseils sur l'enregistrement des impressions, les clics et les licenciements.

#### Messagerie intégrée

Ce guide de mise en œuvre [optionnel et avancé]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/implementation_guide/) couvre les considérations de code de message dans l'application, trois cas d'utilisation personnalisés construits par notre équipe, et des extraits de code qui l'accompagnent.

#### Notifications push

Ce guide d'implémentation [optionnel et avancé]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/implementation_guide/) couvre les moyens de tirer parti d'une sous-classe personnalisée `FirebaseMessagingService` pour tirer le meilleur parti de vos messages push. Included is a custom use case built by our team, accompanying code snippets, and guidance on logging analytics.

### Nouveaux partenariats Braze

#### Adobe - Plateforme de données client

Construit sur la plateforme Adobe Experience, La plateforme de données client en temps réel d'Adobe (CDP en temps réel) aide les entreprises à rassembler des données connues et anonymes provenant de multiples sources d'entreprise afin de créer des profils clients qui peuvent être utilisés pour fournir des expériences clients personnalisées sur tous les canaux et appareils en temps réel.

L'intégration CDP de Braze et [Adobe]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/adobe/) permet aux marques de se connecter et de mapper leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel. Les marques peuvent alors agir sur ces données, en fournissant des expériences personnalisées ciblées à ces utilisateurs.

#### Shopify - eCommerce

[Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify/) est une entreprise commerciale leader dans le monde qui fournit des outils de confiance pour démarrer, croître, commercialiser et gérer une entreprise de détail de toute taille. Ensemble, l'intégration de Braze et Shopify permet aux marques de connecter leur magasin Shopify de façon transparente avec Braze pour passer certains webhooks Shopify au Brésil. Profitez des stratégies transversales de Braze et de Canvas pour recibler vos utilisateurs avec des messages de caisse abandonnés et inciter les clients à achever leur achat, ou utilisateurs de retarget en fonction de leurs achats précédents.

## Octobre 2021

### iOS 15

#### Protection de la vie privée d'Apple Mail

La protection de la vie privée (MPP) d’Apple est une mise à jour de la vie privée qui sera disponible pour les utilisateurs de l’application Apple Mail sur iOS 15, iPadOS 15, macOS Monterey, et watchOS 8, sorti à la mi-septembre. Pour les utilisateurs qui optent pour le MPP, les e-mails seront maintenant préchargés en utilisant des serveurs proxy, mettre en cache les images et empêcher la possibilité de tirer parti des pixels de suivi pour les métriques comme [le suivi d'ouverture]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings/#email-open-tracking-pixel/). Pour en savoir plus sur les MPP et les problèmes concernant les paramètres de délivrabilité des courriels et les problèmes liés aux campagnes préexistantes et aux toiles qui se déclenchent sur la base de ces métriques, visitez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/mpp/).

#### Fonctionnalités push

iOS 15 a introduit de nouvelles fonctionnalités de notification pour aider les utilisateurs à rester concentrés et éviter des interruptions fréquentes tout au long de la journée. Nous sommes heureux de proposer un support pour ces nouvelles fonctionnalités, y compris les [niveaux d'interruption et les Scores de pertinence]({{site.baseurl}}/user_guide/message_building_by_channel/push/ios/notification_options/).

### Cartes de contact

Les Cartes de contact sont un format de fichier normalisé pour envoyer des informations commerciales et de contact qui peuvent être facilement importées dans des carnets d'adresses ou des carnets de contacts. Vous pouvez maintenant télécharger et créer des cartes de contact pour vos messages SMS et MMS. Pour en savoir plus sur la façon de construire des cartes de contact dans notre générateur de carte de contact intégré, visitez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/).

### Personnalisation des cartes de contenu

Vous pouvez créer votre propre interface de cartes de contenu en étendant `ABKContentCardsTableViewController` pour personnaliser tous les éléments de l'interface utilisateur et le comportement des cartes de contenu. Pour en savoir plus sur la façon de personnaliser le flux des Cartes de Contenu, visitez notre [documentation]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/content_cards/customization/#customizing-the-content-cards-feed/).

### Limites de débit de l'API

[Les limites de taux]({{site.baseurl}}/api/basics/#api-limits/) s'appliqueront à tous les clients embarqués après le 16 septembre 2021.

### Mises à jour vers les guides de développeurs Android et FireOS

Les guides de développeurs Android et FireOS ont fusionné en un seul endroit. Des articles dédiés à FireOS seront disponibles dans cette [nouvelle section Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/fireos/integration/).

### Mises à jour de l'entonnoir et des rapports de fidélisation

Les [Rapports d'entonnoir]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_funnel_reports/) et [Rapports de fidélisation]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/retention_reports/) sont maintenant disponibles pour les campagnes de SMS.

## Septembre 2021

### Synchronisation Google Audience

L'intégration de Braze [Synchronisation de l'audience vers Google]({{site.baseurl}}/partners/canvas_steps/google_audience_sync/) permet aux marques d'étendre la portée de leurs trajets clients inter-canaux à Google Search, Google Shopping, Gmail, YouTube et Google Display. En utilisant les données de vos clients de première partie, vous pouvez livrer des publicités en toute sécurité en fonction des déclencheurs de comportement, de la segmentation et plus encore. Tous les critères que vous utilisez généralement pour déclencher un message (par exemple, push, email, SMS, etc.). dans le cadre d'un Braze Canvas peut être utilisé pour déclencher une publicité pour cet utilisateur via Google Customer Match.

### Guide d'intégration des meilleures pratiques pour iOS SDK

Ce guide SDK facultatif d'intégration [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/initial_sdk_setup/ios_sdk_integration/) vous emmène étape par étape dans la mise en place des meilleures pratiques lors de l'intégration du SDK iOS et de ses composants principaux dans votre application. Ce guide vous aidera à construire un `Gestionnaire de Brase. wift` fichier d'aide qui découplera toutes les dépendances du Braze iOS SDK du reste de votre code de production. ce qui a entraîné une `importation AppboyUI` dans toute votre application. Cette approche limite les problèmes liés aux importations excessives de SDK, facilitant le suivi, le débogage et le changement de code.

### Achats prédictifs

Les achats prédictifs offrent aux marketeurs un outil puissant pour identifier et envoyer des messages en fonction de leur probabilité de faire un achat. Lorsque vous créez une prévision d'achat, Braze forme un modèle d'apprentissage automatique à l'aide de [arbres de décision boostés par gradient](https://en.wikipedia.org/wiki/Gradient_boosting) pour apprendre de l'activité d'achat précédente et prédire l'activité d'achat future. Visitez notre documentation [Achats prédicitvés]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/) pour en savoir plus.

### Editeur Glisser & Déposer

Avec Braze Email, vous pouvez créer des messages électroniques personnalisés et personnalisés dans les campagnes ou Canvas en utilisant notre nouvelle expérience d'édition par glisser & Déposer. Les utilisateurs peuvent maintenant faire glisser des blocs d'éditeur dans leurs e-mails, permettant une personnalisation plus intuitive. Pour savoir comment commencer avec l'éditeur Drag & Drop, visitez notre [documentation]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/).

### Import des alias de l'utilisateur

Pour cibler les utilisateurs qui n'ont pas d' `external_id`, vous pouvez importer une liste d'utilisateurs avec des alias d'utilisateur. Un alias sert d'identifiant d'utilisateur unique alternatif. Cela peut être utile si vous essayez de commercialiser des utilisateurs anonymes qui n'ont pas créé de compte avec votre application. Visitez notre [documentation]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import/#import-with-user-alias) pour en savoir plus.

### Guide de mise à jour iOS 15

Ce [guide]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/ios_15/) décrit les changements introduits dans iOS 15 (WWDC21) et les étapes nécessaires à la mise à jour de votre intégration dans Braze iOS SDK.

### Guide de mise à jour d'Android 12

Ce [guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_12/) décrit les changements pertinents introduits dans Android 12 (2021) et les étapes de mise à jour requises pour votre intégration à Braze Android SDK.

### A2P 10DLC

A2P 10DLC fait référence à un système aux États-Unis qui permet aux entreprises d'envoyer des messages de type Application-to-Person (A2P) via un numéro de téléphone standard à 10 chiffres long code (10DLC). Les codes à 10 chiffres ont traditionnellement été conçus pour le trafic de personne à personne (P2P), ce qui a pour effet de contraindre les entreprises à un débit limité et à un filtrage accru. Ce service aide à soulager ces problèmes, améliorant la délivrance globale des messages, permettant aux marques d'envoyer des messages à l'échelle, y compris les liens et les appels à l'action, et aider à protéger davantage les consommateurs des messages indésirables.

Tous les clients qui possèdent et/ou utilisent actuellement des codes longs américains pour envoyer aux clients américains doivent enregistrer leurs codes longs pour 10DLC. Pour en savoir plus sur les spécificités de 10DLC et pourquoi il est nécessaire, visitez notre [article 10DLC dédié]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/10dlc/).

### Réinitialisation de l'authentification à deux facteurs

Les utilisateurs rencontrant des problèmes de connexion via l'authentification à deux facteurs peuvent contacter les administrateurs de leur entreprise pour réinitialiser leur authentification à deux facteurs. Visitez notre [documentation]({{site.baseurl}}/user_guide/administrative/company_settings/security_settings/#user-authetication-reset) pour en savoir plus.

### Nouveaux partenariats Braze

#### Hightouch - Automatisation du flux de travail

L'intégration de Braze et de [Hightouch]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/hightouch/) vous permet de construire de meilleures campagnes sur Braze avec des données clients actualisées à partir de votre entrepôt de données. Vous souhaitez fournir des interactions pertinentes et opportunes à vos clients, et le faire repose fortement sur les données dans votre compte Braze pour être précis et frais. En synchronisant automatiquement les données clients de votre entrepôt de données dans Braze, vous n'avez plus besoin de vous soucier de la cohérence des données, et vous pouvez vous concentrer sur la construction d'expériences de classe mondiale.

#### Transcend - Confidentialité des données & Conformité

Le partenariat Braze et [Transcend]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_privacy/transcend/) aide les utilisateurs à automatiser les demandes de confidentialité en orchestrant les données sur des dizaines de systèmes de données. En fin de compte, cela aide les équipes à se conformer à la réglementation comme le RGPD et l’ACCP et place les personnes sur le siège du conducteur en ce qui concerne leurs données.

#### Tinyindices - Importation de cohortes

[Tinyclues]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/tinyclues/) est une fonctionnalité de création d'audience qui offre la capacité d'augmenter le nombre de campagnes et de revenus sans nuire à l'expérience du client. et analytiques pour suivre les performances des campagnes CRM en ligne et hors ligne. Ensemble, l’intégration de Braze et Tinyclues offre aux utilisateurs une voie vers une meilleure planification et une meilleure stratégie de CRM permettant aux utilisateurs d'envoyer plus de campagnes de ciblage, de trouver de nouvelles opportunités de produits et d'augmenter leurs revenus à l'aide d'une interface utilisateur incroyablement conviviale.

#### optilyz - Mail direct

[optilyz]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/optilyz/) est une plate-forme d'automatisation de messagerie directe qui vous permet d'exécuter des campagnes de messagerie directe plus axées sur le client, durables et rentables. optilyz est utilisé par des centaines d'entreprises à travers l'Europe et vous permet d'intégrer des lettres, des cartes postales et les auto-mailers dans vos campagnes de marketing inter-canaux et automatiser et mieux personnaliser vos campagnes. Utilisez l'intégration optilyz et Braze webhook pour envoyer du courrier direct à vos clients.


<br><br>

[support]: {{site.baseurl}}/support_contact/
