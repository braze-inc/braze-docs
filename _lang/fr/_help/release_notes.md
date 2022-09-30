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

## Août 2022

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

## Juillet 2022

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

## Juin 2022

### Approbation de campagne

L’approbation de campagne ajoute un processus d’examen à votre flux de travail avant de lancer une campagne. Vous pouvez maintenant vous assurer que chaque confirmation est approuvée afin de lancer la campagne. Pour en savoir plus sur le processus d’approbation, consultez [Approbation des campagnes]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_approval/).

### Étape de message Canvas

Les Étapes de message vous permettent d’ajouter un message indépendant où vous voulez dans votre flux Canvas. Pour en savoir plus, lisez notre article sur les [étapes de message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/).

### Assistant de rédaction IA

L’[Assistant de rédaction IA]({{site.baseurl}}/user_guide/intelligence/ai_copywriting#ai-copywriting-assistant) de Braze transmet un bref nom ou une brève description du produit à l’outil de génération de copies GPT3 de OpenAI pour générer une copie marketing qui semble générée par un humain et que vous pouvez utiliser dans vos communications. Cette fonctionnalité est disponible pour la plupart des compositeurs de messages dans le tableau de bord de Braze.

### Guide des tests unitaires de notification push iOS

Un [Guide des tests unitaires pour les notifications push sur iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/push_notifications/unit_tests#unit-tests) a été ajouté au Guide du développeur. Ce guide décrit des tests unitaires qui vérifieront si le délégué de votre application est configuré correctement. 

### Questionnaire de confidentialité de Google

À compter d’avril 2022, les développeurs Android doivent remplir le [formulaire de sécurité des données][4] de Google Play pour révéler leurs pratiques de confidentialité et de sécurité. [Ce guide]({{site.baseurl}}/developer_guide/platform_integration_guides/android/google_play_privacy#google-play-privacy-questionnaire) fournit des instructions sur la façon de remplir ce nouveau formulaire avec des informations sur la manière dont Braze gère les données de votre application. 

### RelayState SAML SSO

Les instructions initiales de configuration de l’authentification unique (SSO) ont été mises à jour pour recommander l’utilisation d’une clé API `RelayState`. Pour plus d’informations, consultez les articles [Configuration SAML SSO]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/) et [Onelogin]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/onelogin/), [Okta]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/okta/) et [Azure Active Directory]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/azure_ad/) correspondants. 

### Mises à jour de l’intégration Talon.One

Les étapes d’intégration, les endpoints et les exemples ont été mis à jour dans notre article sur notre partenariat avec [Talon.One]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/talonone#talonone). Si vous utilisez notre partenariat avec Talon.One, nous vous recommandons de mettre à jour votre intégration en conséquence.

### Lancement du SDK Web Braze v4

L’équipe SDK Braze a publié la v4 du SDK Web. Pour obtenir une liste des changements, des mises à jour et des ajouts, consultez le [journal de modifications](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md) de notre SDK Web. Un [Guide de mise à niveau](https://github.com/braze-inc/braze-web-sdk/blob/master/UPGRADE_GUIDE.md) a été créé pour passer de la V3 à la V4.

### Fin de prise en charge de Grouparoo

La prise en charge de Grouparo a été arrêtée en avril 2022.

## Mai 2022

### Filtrer par attribution de campagne / Canvas
Vous pouvez maintenant filtrer les utilisateurs qui ont répondu à une campagne ou Canvas Step, ou par catégorie de mot-clé ou tag spécifique via SMS. Pour plus d’informations, voir [Reciblage SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/).

### Tableau de bord des performances e-mail
Le [tableau de bord des performances d’e-mail]({{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/) vous permet d’afficher les mesures de performance globales pour l’ensemble de votre canal e-mail, à partir des campagnes et des Canvas pour la période que vous avez sélectionnée.

Pour plus d’informations sur les tableaux de bord analytiques disponibles dans Braze, consultez la section [Your Analytics Dashboards]({{site.baseurl}}/user_guide/data_and_analytics/your_analytics_dashboards/understanding_your_app_usage_data/) (Vos tableaux de bord analytiques).

### Paramètres de style global

Voici les nouveaux [paramètres de style global]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings/) pour l’éditeur Drag & Drop ! Vous pouvez désormais personnaliser facilement l’apparence de vos campagnes et de vos Canvas d’e-mail en ajoutant un thème par défaut, en définissant le style de texte de base, et bien plus encore.

### Webhooks Braze à Braze
Avec un webhook Braze à Braze, vous pouvez utiliser des webhooks pour communiquer avec l’API de Braze REST, et faire tout ce que notre API vous permet de faire. En gros, c’est un webhook pour communiquer entre Braze et Braze. Pour plus d’informations, consultez notre article sur les [Webhooks Braze à Braze]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/).

### Obsolescences

#### SDK Windows
Le [SDK Windows de Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/windows_universal/initial_sdk_setup/) est obsolète depuis le 24 mars 2022, et aucune nouvelle application Windows ne peut être créée dans le tableau de bord de Braze. 

#### Intégration des push Baidu
L’[intégration des push Baidu]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/integration/baidu_integration/) est obsolète depuis le 24 mars 2022 et aucune nouvelle application Baidu ne peut être créée dans le tableau de bord de Braze. 

### Nouveaux partenariats Braze

#### Tealium pour Currents

L’intégration entre Braze et [Tealium]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/tealium/tealium_for_currents/) permet de contrôler facilement le flux d’informations entre les deux systèmes. Avec Currents, vous pouvez également connecter des données à Tealium pour les rendre utilisables sur tout votre stack d’outils de croissance.

## Avril 2022

### Messages in-app pour Roku

Braze prend désormais en charge l’envoi des messages in-app à vos utilisateurs sur leurs appareils Roku ! Notez que cela nécessite une configuration SDK supplémentaire et n’est pas disponible « out-of-the-box ». Pour plus d’informations sur l’intégration des messages in-app pour Roku, reportez-vous à [messages in-app Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/).

### Mode de filtrage complet pour les prédictions du taux d’attrition et d’achat

Si vous voulez créer immédiatement une nouvelle prédiction, seul un sous-ensemble de filtres de segmentation Braze est pris en charge par défaut. Vous pouvez maintenant activer le Mode de filtrage complet pour activer tous les filtres de segmentation, mais ce mode vous limite à une seule fenêtre lors de la création de la prédiction. Consultez les articles suivants pour en savoir plus :

- [Création d’une prédiction du taux d’attrition]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn/creating_a_churn_prediction/#full-filter-mode)
- [Création d’une prévision d’achat]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases/creating_a_purchase_prediction/#full-filter-mode)

### Option de reciblage pour les réponses avec mot-clé

Quand vous visualisez des analyses pour une campagne SMS, vous pouvez désormais créer facilement un segment pour recibler les utilisateurs qui ont répondu avec une catégorie spécifique de mots-clés. Pour plus d’informations, consultez [Réponses contenant des mots-clés]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/#keyword-responses) dans les rapports SMS.

### Meilleures pratiques de collecte de données

Vous êtes-vous déjà demandé quand et comment collecter des données utilisateur si vous traitez à la fois avec des utilisateurs connus et des utilisateurs inconnus ? Nous savons que le cycle de vie d’un profil utilisateur à Braze peut être un peu déroutant, donc nous avons rassemblé les [meilleures pratiques de collecte de données]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/) pour clarifier les différentes méthodes et les meilleures pratiques de collecte de données pour les utilisateurs nouveaux ou existants.

### Obsolescence de l’API Transifex

Depuis le 7 avril 2022, Transifex a arrêté le support pour les versions 2 et 2.5 de son API pour se concentrer sur la version 3. Après cette date, les versions v2 et v2.5 ne seront plus opérationnelles, et les requêtes associées échoueront. Si vous utilisez l’API Transifex, mettez à jour vos appels de Contenu connecté en conséquence. Reportez-vous à [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/) pour plus d’informations.

### Nouveaux partenariats Braze

#### Toovio - Plateforme de données client

Le partenariat entre Braze et [Toovio]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/toovio/) fournit des déclenchements de messages en temps quasi réel, des outils pour stimuler les performances et un accès aux outils avancés de mesure de campagne de Toovio.

#### Snowplow - Analyses

L’intégration entre Braze et [Snowplow]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/snowplow/) permet aux utilisateurs de transférer des événements de Snowplow vers Braze via le marquage côté serveur de Google Tag Manager. La balise Snowplow Braze vous permet d’envoyer des événements à Braze tout en bénéficiant d’une flexibilité et d’un contrôle accrus :

- Visibilité totale sur toutes les modifications de données
- Capacité à évoluer et à se développer au fil du temps
- Toutes les données restent dans votre cloud privé jusqu’à ce que vous choisissiez de les envoyer
- Configuration simplifiée grâce à de vastes bibliothèques de balises et à l’interface utilisateur familière de Google Tag Manager

Tirez parti des données comportementales enrichies de Snowplow pour effectuer des interactions client efficaces dans Braze et livrer des messages personnalisés en temps réel.

#### Clarisights - Analyses

L’intégration entre Braze et [Clarisights]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/clarisights/) vous permet d’importer des données issues des campagnes et Canvas de Braze pour tirer parti d’une interface de reporting unifiée pour votre performance et votre marketing de rétention client/système de gestion de la relation client (CRM).

#### Wyng - Contenu dynamique

L’intégration entre Braze et [Wyng]({{site.baseurl}}/partners/message_personalization/dynamic_content/wyng/) vous permet de tirer parti des expériences de Wyng pour personnaliser vos campagnes et Canvas Braze. Wyng comprend également un portail de préférences des clients afin que les utilisateurs puissent contrôler les données et les préférences qu’ils partagent avec une marque.

#### Grouparoo - Automatisation des workflows

L’intégration entre Braze et [Grouparoo]({{site.baseurl}}/help/release_notes/deprecations/grouparoo) facilite l’opérationnalisation des données stockées dans un entrepôt en les envoyant à Braze. En configurant des calendriers de synchronisation automatique, vous pouvez constamment améliorer vos communications client grâce à des informations actualisées.

#### Lexer - Plateforme de données client

L’intégration entre Braze et [Lexer]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/lexer/) vous permet de synchroniser des données entre les deux plateformes. Utilisez vos données Lexer pour créer des segments Braze, ou importez vos propres données dans Lexer pour en extraire de précieuses informations.

#### Knak - Orchestration des e-mails

L’intégration entre Braze et [Knak]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/knak/) permet de créer des e-mails totalement réactifs en quelques minutes ou en heures au lieu de quelques jours ou semaines, et de les exporter en tant que modèles Braze prêts à l’emploi. Knak est conçu pour les marketeurs qui souhaitent mettre à niveau leur création d’e-mails pour les campagnes gérées dans Braze, sans avoir besoin d’agences extérieures ou de codage manuel.

## Mars 2022

### Parcours d’action Canvas

Les [parcours d’action]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) vous permettent de trier vos utilisateurs en fonction de leurs actions. Les parcours d’action vous permettent d’effectuer les tâches suivantes :
- Personnaliser les parcours utilisateur en fonction d’une action spécifique. 
- Conserver des utilisateurs pendant une certaine durée pour prioriser leur parcours suivant en fonction de leurs actions au cours de cette période d’évaluation. 

L’accès aux parcours d’action sera déployé progressivement sur toutes les instances de Braze. Contactez votre gestionnaire de compte Braze pour en savoir plus.

### Page de référence des endpoints API

Vous recherchez une page de référence rapide de tous les endpoints Braze disponibles ? Visitez notre [Index des endpoints d’API]({{site.baseurl}}/api/endpoints/).

### Obsolescence des v2 et v2.5 de l’API Transifex
À compter du 7 avril 2022, [Transifex]({{site.baseurl}}/partners/message_personalization/localization/transifex/#transifex) arrêtera le support pour les versions 2 et 2.5 de son API pour se concentrer sur la version 3. Après cette date, les versions v2 et v2.5 ne seront plus opérationnelles, et les requêtes associées échoueront. Les utilisateurs qui ont intégré le partenaire Transifex sont invités à mettre à jour leur version d’API avant cette date.

### Types de données disponibles pour les attributs personnalisés 
Bientôt disponible ! La prise en charge des types de données Objet et Tableau d’objets pour les attributs personnalisés arrive au printemps 2022.

## Février 2022

### Étape des chemins d’expérience Canvas
La nouvelle Étape des chemins d’expérience Canvas vous permet de tester plusieurs chemins Canvas les uns par rapport aux autres et par rapport à un groupe de contrôle, à tout moment dans le parcours de l’utilisateur. Maintenant, vous pouvez tirer parti des analyses rassemblées ici pour déterminer encore plus précisément le parcours le plus efficace. En savoir plus sur la façon de créer une [Étape des chemins d’expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).

### Gestion des numéros de téléphone non valides
Vous avez rencontré un scénario où un utilisateur a entré un numéro de téléphone non valide. Voici votre solution ! Braze marque ces numéros de téléphone comme non valides et ne tentera pas d’envoyer d’autres communications à ces numéros. En savoir plus sur la façon dont Braze [gère les numéros de téléphone non valides]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#handling-invalid-phone-numbers/).

### Nouveaux endpoints pour SMS
Vous pouvez maintenant gérer les numéros de téléphone non valides en utilisant le nouvel [Endpoint SMS de Braze]({{site.baseurl}}/api/endpoints/sms/) ! Cette mise à jour comprend :
- [GET: L’endpoint de requête ou liste de numéros de téléphone non valides]({{site.baseurl}}/api/endpoints/sms/get_query_invalid_numbers/) renvoie une liste de numéros de téléphone considérés comme « non valides » par Braze.
- [POST: L’endpoint de suppression des numéros de téléphone invalides]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/) vous permet de supprimer ces numéros de téléphone « non valides » figurant sur la liste de numéros non valides de Braze.

### Limites de débit
Les limites de taux API ont été précisées dans tous les [articles sur les endpoints de Braze]({{site.baseurl}}/api/basics/#nav_top_endpoints). Vous pouvez maintenant afficher facilement les limites de débit par type de demande. Pour plus d’informations sur les limites de débit, consultez notre article sur les [Limites de débit de notre API]({{site.baseurl}}/api/api_limits/).

### Nouvel endpoint REST
Braze a ajouté un [nouvel endpoint EU-02 REST]({{site.baseurl}}/api/basics/#api-definitions).

### À propos de l’e-mail
Les e-mails sont un excellent moyen de communiquer avec vos clients. Pour une introduction rapide sur la façon de personnaliser et d’utiliser les e-mails, consultez notre nouvel article [À propos de l’e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/about/). 

### À propos des messages in-app
Les messages in-app diffusent du contenu riche à vos utilisateurs qui sont actifs dans votre application. Vous pouvez facilement interagir avec vos clients actifs en créant des messages in-app pour des salutations personnalisées ou une adoption de fonctionnalité. Pour en savoir plus sur les avantages et les types de messages, consultez notre nouvel article [À propos des messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about/).


[support]: {{site.baseurl}}/support_contact/
