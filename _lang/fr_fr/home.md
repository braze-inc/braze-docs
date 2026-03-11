---
nav_title: Accueil
article_title: Quoi de neuf chez Braze
description: "Les notes de mise à jour de Braze sont publiées mensuellement afin que vous puissiez rester informé des principales versions du produit, des améliorations continues, des partenariats de Braze, des modifications importantes apportées au SDK et des fonctionnalités obsolètes."
page_order: 0
search_rank: 1
page_type: reference

---

# Quoi de neuf chez Braze

{% alert tip %}
Pour obtenir de plus amples informations sur les mises à jour mentionnées sur cette page, veuillez contacter votre gestionnaire de compte ou [ouvrir un ticket d'assistance]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Veuillez consulter nos [journaux des modifications SDK]({{site.baseurl}}/developer_guide/changelogs) pour obtenir plus d'informations sur nos versions mensuelles du SDK, les améliorations et les modifications importantes.
{% endalert %}

{% details March 5, 2026 %}

## Sortie le 5 mars 2026

### Rapport &de données

#### Nouveau centre de données

{% multi_lang_include release_type.md release="General availability" %}

Braze a inauguré un nouveau [centre de données]({{site.baseurl}}/user_guide/data/data_centers/) : JP-01. Vous pouvez vous inscrire à des centres de données spécifiques à une région lors de la création de votre compte Braze.

#### Variables de contexte

{% multi_lang_include release_type.md release="General availability" %}

[Les variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) sont des données temporaires que vous pouvez créer et utiliser au cours du parcours d'un utilisateur dans un canvas spécifique. Chaque fois qu'un utilisateur entre dans le canvas - même s'il l'a déjà fait auparavant - les variables contextuelles seront redéfinies en fonction des dernières données d'entrée et de la configuration du canvas. Cette approche permet à chaque entrée canvas de conserver son propre contexte indépendant, ce qui permet aux utilisateurs d'avoir plusieurs états actifs au sein d'un même parcours tout en conservant le contexte spécifique à chaque état.

#### Sources d'ingestion de données dans le cloud

{% multi_lang_include release_type.md release="Early access" %}

[L'ingestion de données]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) dispose d'une nouvelle interface utilisateur qui sépare les sources des synchronisations, vous permettant ainsi de réutiliser une seule source pour un nombre illimité de synchronisations. Cela réduit les doublons dans la configuration et simplifie la configuration lorsque vous avez plusieurs synchronisations. Si vous disposez déjà de synchronisations, elles sont automatiquement soumises à une migration vers la nouvelle structure sources-et-synchronisations sans temps d'arrêt. Pour commencer, veuillez vous rendre dans **Cloud Data Ingestion** > **Sources** afin de consulter, modifier ou créer des sources, puis sélectionner une source dans le menu déroulant lors de la création d'une synchronisation.

#### Champs supplémentaires pour les événements Currents et Data Share

{% multi_lang_include release_type.md release="General availability" %}

[Les événements Currents et Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) incluent désormais les nouveaux champs suivants afin d'enrichir les données disponibles pour les systèmes d'analyse/analytique et les systèmes en aval :

- `agentconsole.AgentExecuted` : Ajouté`error`(chaîne de caractères) — description de toute erreur survenue.
- `agentconsole.ToolInvocation` : Ajouté`request_id`(chaîne de caractères) — ID unique pour la requête LLM globale et l'exécution complète.
- `users.messages.rcs.InboundReceive` : Ajouté`canvas_variation_name`(chaîne de caractères) — nom de la variante canvas reçue par l'utilisateur.

#### Campagne et Canvas pour Snowflake Data Share

{% multi_lang_include release_type.md release="General availability" %}

[Snowflake Data Share]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3) inclut désormais des champs supplémentaires reflétant les informations relatives aux campagnes et aux canevas dans 66 tableaux existants, notamment :

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### Validation préalable à l'importation des fichiers CSV et signalement des erreurs

{% multi_lang_include release_type.md release="General availability" %}

[Les importations CSV par les utilisateurs]({{site.baseurl}}/user_guide/data/user_data_collection/user_import) prennent désormais en charge la validation préalable à l'importation et la création de rapports d'erreurs détaillés. Avant l'importation, veuillez sélectionner **Valider le fichier avant l'importation** sur la page **Importer des utilisateurs**. Braze analysera votre fichier et générera un rapport identifiant les lignes qui échoueront complètement (erreurs) et celles qui réussiront avec certaines valeurs ignorées (avertissements). Vous pouvez télécharger le rapport, corriger votre fichier CSV et le télécharger à nouveau, ou continuer tel quel. Une fois l'importation terminée, un rapport téléchargeable répertoriant toutes les lignes ayant échoué est également disponible, avec la raison exacte de chaque problème.

#### Tableau de bord de diagnostic de l'envoi de messages

{% multi_lang_include release_type.md release="Early access" %}

Le [tableau de bord Diagnostics de messagerie]({{site.baseurl}}/user_guide/analytics/dashboard/diagnostics_dashboard) fournit une analyse détaillée des résultats d'envoi de messages, vous permettant ainsi d'identifier les tendances et de diagnostiquer les problèmes potentiels dans votre configuration de messagerie. Ce tableau de bord peut vous aider à comprendre pourquoi les messages de vos campagnes ou de vos Canvases n'ont pas été envoyés comme prévu.

### BrazeAI<sup>TM</sup>

#### Agents Braze dans la console d'agent

{% multi_lang_include release_type.md release="General availability" %}

[Les agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/) sont des assistants alimentés par l'intelligence artificielle que vous pouvez créer dans Braze. Les agents peuvent générer du contenu, prendre des décisions éclairées et enrichir vos données afin que vous puissiez offrir des expériences client plus personnalisées. Lorsque vous créez un agent, vous définissez son objectif et établissez des garde-fous quant à son comportement. Une fois en ligne/en production/instantané, l'agent peut être [déployé]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) dans Braze pour générer des copies personnalisées, prendre des décisions en temps réel ou mettre à jour les champs du catalogue.

### Orchestration

#### Autorisations utilisateur granulaires

{% multi_lang_include release_type.md release="Early access" %}

Braze introduit [des autorisations granulaires]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/), une méthode plus flexible pour la gestion de l'accès des utilisateurs. Veuillez vous référer à [la section Migration vers des autorisations granulaires]({{site.baseurl}}/granular_permissions_migration/) pour en savoir plus sur le processus de migration, y compris sur la manière dont les autorisations héritées sont effectuées.

#### Limite de débit par canal

{% multi_lang_include release_type.md release="General availability" %}

Lorsque vous définissez une limite de débit pour une campagne multicanal ou Canvas, vous avez la possibilité de choisir entre une limite commune ou une [limite par canal]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#multichannel-campaigns-and-canvases). Lorsqu'une campagne multicanal ou canvas utilise une limitation de débit basée sur les canaux, la limite de débit s'applique à chacun des canaux sélectionnés. Par exemple, vous pouvez configurer votre campagne ou votre canvas pour envoyer un maximum de 5 000 webhooks et 2 500 messages SMS par minute pour l'ensemble de la campagne ou du canvas.

#### Étape du contexte canvas

{% multi_lang_include release_type.md release="General availability" %}

[Les étapes du canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) vous permettent de créer et de mettre à jour une ou plusieurs variables pour un utilisateur lorsqu'il navigue dans un canvas. Par exemple, si vous avez un Canvas qui gère les remises saisonnières, vous pouvez utiliser une variable de contexte pour stocker un code de remise différent chaque fois qu'un utilisateur entre dans le Canvas.

### Canaux&  Points de contact

#### Traduire les paramètres régionaux dans les blocs de contenu

{% multi_lang_include release_type.md release="Early access" %}

Après avoir ajouté des paramètres régionaux à votre espace de travail, vous pouvez [effectuer le ciblage d'utilisateurs dans différentes langues,]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) le tout dans un bloc de contenu.

### Partenariats

#### Algolia - Recommandations de recherche

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia) est une plateforme de recherche et de découverte qui aide les développeurs à créer des expériences de recherche rapides, pertinentes et évolutives. Grâce à une approche API-first performante, Algolia combine des algorithmes de classement avancés et des informations basées sur l'intelligence artificielle pour offrir une recherche sur site, une navigation et une découverte de contenu en mode fluide, sans heurts et de façon homogène en termes de personnalisation.

#### Anthropic - Fournisseur de modèles d'intelligence artificielle

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic) est une entreprise spécialisée dans la sécurité et la recherche en matière d'intelligence artificielle qui crée Claude, un assistant IA de nouvelle génération conçu pour être utile, honnête et sûr pour un large éventail de tâches linguistiques.

#### Canva - Personnalisation des messages - Studio créatif

[Canva]({{site.baseurl}}/partners/canva) synchronise vos images directement dans la bibliothèque multimédia de Braze, ce qui rationalise votre flux de travail créatif et garantit la mise à jour de vos ressources visuelles sur tous vos canaux de communication.

#### DOTS.ECO \- Récompenses

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) vous permet de récompenser les utilisateurs pour leur impact environnemental réel grâce à des certificats numériques traçables. Chaque certificat peut inclure des métadonnées telles qu'une URL de certificat partageable et une URL d'image, afin que les utilisateurs puissent consulter (et revoir) leur preuve d'impact.

#### Figma - Personnalisation des messages - Studio créatif

[Figma]({{site.baseurl}}/partners/figma) est une plateforme de conception collaborative qui vous permet de créer, concevoir et prototyper des produits. Veuillez utiliser cette intégration pour transférer des images et des ressources visuelles depuis Figma directement vers la bibliothèque multimédia Braze.

#### Flybuy - Personnalisation des messages - Localisation/emplacement

[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy) de Radius Networks est la principale plateforme de localisation omnicanal qui exploite une technologie basée sur l'intelligence artificielle pour optimiser la rapidité du service dans les domaines de la collecte, de la réception/distribution, du service au volant et de la restauration sur place. Grâce à sa suite marketing intégrée, Flybuy permet également aux marques de diffuser des messages hyperciblés et adaptés au moment, contribuant ainsi à stimuler l'engagement, à augmenter le montant des achats et à soutenir des initiatives de fidélisation plus larges.

#### Google Gemini - Fournisseur de modèles d'intelligence artificielle

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini) est la gamme de modèles d'intelligence artificielle de Google qui combine des capacités de raisonnement avancées sur le texte, le code et les images afin d'aider les marques à offrir des expériences plus intelligentes et personnalisées.

#### Limbik - Personnalisation des messages - Moteurs de personnalisation

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik) est votre couche de résonance en intelligence artificielle : elle prédit comment les audiences réelles interprètent et réagissent aux messages, aux concepts et aux résultats de l'intelligence artificielle avant qu'ils n'atteignent le marché. S'appuyant sur des recherches primaires continues menées dans plus de 60 pays et dans plus de 25 langues, Limbik fournit des audiences synthétiques validées par des humains, c'est-à-dire des populations numériques qui simulent la réponse réelle d'un public à la vitesse d'une machine et avec une précision de niveau scientifique (confiance de 95 %, marge d'erreur de 1,5 % à 3 %). Limbik vous permet de vous assurer immédiatement que votre message correspond aux croyances et aux sentiments de votre audience cible.

#### Linkrunner - Orchestration des messages - Attribution

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner) est une plateforme mobile d'attribution et d'analyse qui vous aide à suivre et à analyser vos campagnes d'acquisition d'utilisateurs.

#### Mailizio - Orchestration des messages - Modèles

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio) est une plateforme de création et de gestion d'e-mails qui facilite la conception de contenus réutilisables et adaptés à l'image de marque à l'aide d'un éditeur visuel intuitif. Grâce à l'intégration de Mailizio à Braze, vous pouvez exporter vos blocs de contenu et vos modèles d'e-mails, puis générer automatiquement des messages in-app à partir de ces mêmes ressources, ce qui permet un déploiement rapide et entièrement contrôlé de vos campagnes.

#### Fidélité ouverte - Données et analyse/analytique - Fidélité

[Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty) est une plateforme cloud dédiée aux programmes de fidélisation qui vous permet de créer et de gérer des programmes de fidélisation et de récompenses pour vos clients. L'intégration Braze et Open Loyalty synchronise les données de fidélité, telles que le solde de points, les changements de niveau et les avertissements d'expiration, directement dans Braze en temps réel. Cela vous permet de déclencher l'envoi de messages personnalisés (e-mail, notification push, SMS) lorsque le statut de fidélité d'un utilisateur change.

#### OpenAI - Fournisseur de modèles d'intelligence artificielle

[OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai) développe des modèles d'intelligence artificielle avancés, tels que GPT, qui permettent la compréhension et la génération du langage naturel, permettant ainsi aux marques de créer et de développer des interactions significatives avec leurs clients.

#### Shopgate - Canaux

[Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate) est une plateforme de commerce mobile et omnicanal qui assiste les commerçants dans la création d'applications d'achat et l'amélioration de l'efficacité des magasins physiques grâce à des outils de gestion des commandes et de clienteling, c'est-à-dire un service client personnalisé en magasin basé sur les données clients.

#### Splio - Données et analyse/analytique - Importation de la cohorte

[Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio) est un outil de création d'audience qui vous permet d'augmenter le nombre de campagnes et le chiffre d'affaires sans nuire à l'expérience client, et fournit des analyses pour suivre les performances des campagnes CRM en ligne et hors ligne.

### SDK

#### Mises à jour importantes du SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SDK Flutter 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [SDK Swift 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Xamarin 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Nous avons mis à jour la liaison Android de [Braze Android SDK 37.0.0 à 41.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Nous avons mis à jour la liaison iOS de [Braze Swift SDK 13.3.0 à 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Ajout de nouvelles dépendances NuGet transitives requises par le SDK Android Braze :
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib a été mis à jour de la version 2.0.21.3 à la version 2.3.0.1. Si votre projet lie explicitement ce paquet à une version antérieure, il sera nécessaire de le mettre à jour afin d'éviter des erreurs de restauration.
    - Suppression de la fonctionnalité Fil d'actualité.
        - Cette fonctionnalité a été supprimée du SDK Android natif dans la version [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0).
        - Cette fonctionnalité a été supprimée du SDK Swift natif dans la version [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0).
    - Le casBRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData enum a été renommé en BRZInAppMessageDismissalReason.WipeData.
- [Plugin Expo 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - Cette version nécessite la version 19.0.0 du SDK Braze React native.
    - (Android) Correction d'une fuite de mémoire dans la couche de persistance des données.
    - (Android) Ajout de la prise en charge de Braze.getInitialPushPayload() pour gérer les liens profonds des notifications push lorsque l'application est lancée à partir d'un état terminé. Ceci résout un problème où les liens profonds provenant des notifications push n'étaient pas gérés sur Android lorsque l'application était lancée à froid.
- [SDK React native 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - Mise à jour des liaisons de version du SDK Swift natif de Braze Swift SDK 13.3.0 à 14.0.1.
    - Mise à jour des liaisons de version native du SDK Android de Braze Android SDK 40.0.2 à 41.0.0.

{% enddetails %}

{% details February 5, 2026 %}

## Sortie le 5 février 2026

### BrazeAI<sup>TM</sup>

#### Optimiseur de contenu

{% multi_lang_include release_type.md release="Beta" %}

[Content Optimizer]({{site.baseurl}}/user_guide/brazeai/content_optimizer) est une étape du canvas de test de contenu continu et à haute variante qui permet une optimisation automatisée de l'engagement. À l'aide d'une interface glisser-déposer similaire à celle de l'étape Message, veuillez définir les composants à tester, générer des variantes à l'aide de l'intelligence artificielle (ou les saisir manuellement) et utiliser des étiquettes Liquid pour effectuer le mappage de ces composants au contenu de votre message.

Créé sur la base d'un optimiseur multi-bras non contextuel, Content Optimizer envoie un seul message par utilisateur, déterminant quelle combinaison de variantes de composants fournir en fonction de prédictions. Au fur et à mesure que l'étape recueille des données, les variantes performantes voient naturellement leur allocation d'envoi augmenter, tandis que les variantes moins performantes voient la leur diminuer. Content Optimizer fonctionne de manière optimale avec les canevas à envoi répété qui ont un volume quotidien constant d'utilisateurs (au moins quelques milliers d'utilisateurs par jour) afin de permettre une optimisation continue.

### Rapport &de données

#### Événements recommandés pour le commerce électronique

{% multi_lang_include release_type.md release="Early access" %}

Afin de faire correspondre les événements recommandés pour le commerce électronique avec l'événement d'achat existant, nous avons ajouté l'[événement de conversion « Passer une commande »]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report), qui est similaire à « Effectuer un achat ».

### Canaux&  Points de contact

#### Traduire les paramètres régionaux dans les bannières

{% multi_lang_include release_type.md release="Early access" %}

Après avoir ajouté des paramètres régionaux à votre espace de travail, [vous pouvez cibler des utilisateurs dans différentes langues]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales) à l'aide d'une seule bannière.

#### Veuillez configurer la largeur des blocs de contenu glisser-déposer.

[Veuillez ajuster la largeur de votre bloc de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) en sélectionnant le bouton dans le menu de navigation. La largeur par défaut est de 100 % si elle n'est pas spécifiée dans les paramètres de style globaux de votre e-mail ; dans le cas contraire, les paramètres globaux seront respectés.

![Une flèche double face avec une option permettant de modifier la largeur.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Utiliser le réchauffement d’adresses IP automatisé

{% multi_lang_include release_type.md release="Early access" %}

Utilisez [le réchauffement d’adresses IP automatisé]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/#automated-ip-warming) pour augmenter progressivement votre volume d'envoi quotidien, permettant ainsi aux fournisseurs de boîtes de réception de se familiariser avec vos habitudes d'envoi et de leur accorder leur confiance. Braze envoie d'abord vos messages aux utilisateurs abonnés les plus engagés, ce qui permet au volume quotidien d'augmenter à un rythme conforme aux meilleures pratiques.

### Partenariats

#### LinkedIn – Synchronisation de l'audience Canvas

À l'aide de [Braze Audience Sync vers LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/), veuillez ajouter les données utilisateur de votre intégration Braze aux listes de clients LinkedIn afin de diffuser des publicités basées sur des déclencheurs comportementaux, la segmentation et bien plus encore. Tout critère habituellement utilisé pour déclencher un message (tel que push, e-mail, SMS et webhook) dans un Braze Canvas basé sur les données utilisateur peut désormais déclencher une publicité destinée à cet utilisateur dans vos listes de clients LinkedIn.

#### Oracle Crowdtwist - Analyse de& données

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist) est une solution cloud native de premier plan dédiée à la fidélisation de la clientèle, qui permet aux marques d'offrir des expériences client personnalisées. Leur solution propose plus de 100 parcours d'engagement prêts à l'emploi, offrant aux marketeurs un retour sur investissement rapide pour développer une vision plus complète du client.

#### Fullstory - Contenu dynamique

La plateforme de données comportementales [de Fullstory]({{site.baseurl}}/partners/fullstory/) aide les leaders technologiques à prendre des décisions plus éclairées et plus pertinentes. En intégrant des données comportementales numériques à leur pile analytique, la technologie brevetée de Fullstory exploite la puissance des données comportementales de qualité à grande échelle, transformant chaque visite numérique en informations exploitables. 

#### Loyauté ouverte - Analyse des données&analytiques

[Open Loyalty]({{site.baseurl}}/partners/openloyalty) est une plateforme cloud dédiée aux programmes de fidélisation qui vous permet de créer et de gérer des programmes de fidélisation et de récompenses pour vos clients. L'intégration Braze et Open Loyalty synchronise les données de fidélité, telles que le solde de points, les changements de niveau et les avertissements d'expiration, directement dans Braze en temps réel. Cela vous permet de déclencher l'envoi de messages personnalisés (e-mail, notification push, SMS) lorsque le statut de fidélité d'un utilisateur change.

#### DOTS.ECO \- Extensions

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco) vous permet de récompenser les utilisateurs pour leur impact environnemental réel grâce à des certificats numériques traçables. Chaque certificat peut inclure des métadonnées telles qu'une URL de certificat partageable et une URL d'image, afin que les utilisateurs puissent consulter (et revoir) leur preuve d'impact.

#### Mailizio - Orchestration des messages

[Mailizio]({{site.baseurl}}/partners/mailizio/) est une plateforme de création et de gestion d'e-mails qui facilite la conception de contenus réutilisables et adaptés à l'image de marque à l'aide d'un éditeur visuel intuitif. Grâce à l'intégration de Mailizio à Braze, vous pouvez exporter vos blocs de contenu et vos modèles d'e-mails, puis générer automatiquement des messages in-app à partir de ces mêmes ressources, ce qui permet un déploiement rapide et entièrement contrôlé de vos campagnes.

### API

#### API POST de la bibliothèque multimédia

{% multi_lang_include release_type.md release="General availability" %}

Les ressources de la bibliothèque multimédia peuvent désormais être ajoutées via l'API, ce qui permet aux clients, partenaires et agences d'automatiser davantage leurs workflows de création de messages. Veuillez utiliser l'[API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) pour télécharger directement un fichier de ressource ou copier un fichier à partir d'une URL existante. Cette fonctionnalité permet l'intégration et l'automatisation.

### Courants et partage de données

#### Événements de la console d'agent pour les destinations de stockage et le partage de données

{% multi_lang_include release_type.md release="General availability" %}

Deux nouveaux [événements](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) sont désormais disponibles pour les destinations de stockage (AWS S3, GCS et Azure Blob Storage) et Snowflake Datashare :`agentconsole.AgentExecuted`et `agentconsole.ToolInvocation`. Ces événements vous permettent d'analyser l'utilisation de la console d'agent et les détails dans vos systèmes en aval, vous aidant ainsi à comprendre et à tirer le meilleur parti de l'utilisation de vos agents. Les agents vous permettent de créer et de déployer des agents intelligents capables d'effectuer des tâches spécifiques dans Braze, notamment générer du contenu dans des canevas ou des catalogues et diriger les utilisateurs vers différents chemins en fonction de décisions intelligentes. Pour plus d'informations, veuillez consulter le [journal des modifications de Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Nouveaux événements « Réessayer » pour les canaux individuels

{% multi_lang_include release_type.md release="General availability" %}

[De](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) nouvelles [tentatives](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) sont désormais disponibles pour les canaux e-mail, LINE, notifications push, SMS, webhooks et WhatsApp. Ces événements permettent de déterminer quand la limite de fréquence entraîne le report d'un message soumis à la planification plutôt que son annulation. Lorsqu'un message est dépriorisé ou soumis à une limite de fréquence, il est désormais possible de réessayer de l'envoyer dans un délai de réessai configuré, ce qui vous permet d'obtenir des informations sur les modèles de réception/distribution des messages et les impacts de la limite de fréquence. Pour plus d'informations, veuillez consulter le [journal des modifications de Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Ajouter un nouveau'time_ms'champ à l'événement TokenStateChange

{% multi_lang_include release_type.md release="General availability" %}

Un nouveau`time_ms`champ a été ajouté à [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events)l'événement, offrant une granularité de l'ordre de la milliseconde pour suivre les changements d'état des jetons push. Cette précision accrue vous aide à comprendre le dernier statut d'un jeton push lorsque plusieurs modifications surviennent en l'espace d'une seconde, vous garantissant ainsi la fiabilité du statut d'abonnement dans les systèmes en aval. Pour plus d'informations, veuillez consulter le [journal des modifications de Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Envoyer l'utilisateur anonyme vers les destinations Tealium

{% multi_lang_include release_type.md release="General availability" %}

Les événements pour lesquels aucun ID externe n'est défini peuvent désormais être diffusés vers les destinations [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents). Lorsque vous cochez la case « Inclure les événements provenant d'utilisateurs anonymes » dans votre intégration Currents, les événements sans ID externe seront envoyés à la destination au lieu d'être supprimés. Cette fonctionnalité est essentielle pour les analyses/analytiques en aval et les cas d'utilisation impliquant des utilisateurs non identifiés et anonymes.

##### Envoyer l'utilisateur anonyme vers les destinations HTTP personnalisées

{% multi_lang_include release_type.md release="Beta" %}

Les événements pour lesquels aucun ID externe n'est défini peuvent désormais être diffusés vers des destinations CustomHTTP. Lorsque vous cochez la case « Inclure les événements provenant d'utilisateurs anonymes » dans votre intégration Currents, les événements sans ID externe seront envoyés à la destination au lieu d'être supprimés. Cette fonctionnalité est essentielle pour les analyses/analytiques en aval et les cas d'utilisation impliquant des utilisateurs non identifiés et anonymes.

#### Événement « Ouverture de l'e-mail » —"machine_open"champ

[L]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events)'[événement « Ouverture d'e-mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) » génère désormais la valeur"machine_open" du champ permettant de générer un rapport sur l'indicateur [_« Ouverture de machine_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens) ». 

### SDK

Les mises à jour SDK suivantes ont été publiées. La version 14.0.1 du SDK Swift corrige un problème lié à la gestion des liens universels. Android SDK v40.2.0 corrige une fuite de mémoire potentielle et résout un problème lié à l'ouverture de plusieurs sessions en présence d'activités transparentes. Expo SDK v3.2.0 ajoute `forwardUniversalLinks`l'option (valeur par défaut : false) pour configurer la gestion des liens universels par le SDK Swift natif.

#### Mises à jour importantes du SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Android 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - Renommé `BrazeConfig.Builder.setIsLocationCollectionEnabled()` par `setIsAutomaticLocationCollectionEnabled()`.
    - Renommé `BrazeConfig.isLocationCollectionEnabled` par `isAutomaticLocationCollectionEnabled`.
    - Renommé `BrazeConfigurationProvider.isLocationCollectionEnabled` par `isAutomaticLocationCollectionEnabled`.
- [SDK Android 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Plugin Expo 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [SDK Swift 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details January 8, 2026 %}
## Sortie le 8 janvier 2026

### Rapport &de données

#### Mises à jour des événements Currents

{% multi_lang_include release_type.md release="General availability" %}

Les modifications suivantes ont été apportées à Currents dans la version 4 :

* Modifications apportées au champ « Type d'événement`users.behaviors.pushnotification.TokenStateChange` » :
    * Ajout d'un nouveau`string`champ `push_token`: Jeton Push de l'événement
* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.Bounce` » :
    * Ajout d'un nouveau`string`champ `push_token`: Jeton Push de l'événement
* Modifications apportées au champ « Type d'événement`users.messages.pushnotification.Send` » :
    * Ajout d'un nouveau`string`champ `push_token`: Jeton Push de l'événement
* Modifications apportées au champ « Type d'événement`users.messages.rcs.Click` » :
    * Ajout d'un nouveau`string`champ `canvas_variation_name`: Nom de la variante canvas reçue par cet utilisateur
    * Le champ`user_phone_number`est désormais *facultatif*.
* Modifications apportées au champ « Type d'événement`users.messages.rcs.InboundReceive` » :
    * Le champ`user_id`est désormais *facultatif*.
* Modifications apportées au champ « Type d'événement`users.messages.rcs.Rejection` » :
    * Ajout d'un nouveau`string`champ `canvas_step_message_variation_id`: ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue

Veuillez consulter le [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) pour connaître les changements apportés à chaque version.

#### Exporter les journaux de synchronisation pour toutes les lignes

{% multi_lang_include release_type.md release="Early access" %}

Dans le [tableau de bord Cloud Data Ingestion **Sync Log**]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), veuillez sélectionner l'exportation des journaux au niveau des lignes pour une synchronisation effectuée par :

* **Lignes contenant des erreurs :** Télécharge un fichier contenant uniquement les lignes qui présentaient un statut **d'erreur**.
* **Toutes les lignes :** Télécharge un fichier contenant toutes les lignes traitées lors de l'exécution.

### Canaux&  Points de contact

#### Connecteur WhatsApp BYO (Bring Your Own)

Le [connecteur WhatsApp BYO (Bring Your Own)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/) est le fruit d'un partenariat entre Braze et Infobip, dans le cadre duquel vous accordez à Braze l'accès à votre WhatsApp Business Manager (WABA) d'Infobip. Cela vous permet de gérer et de régler les coûts liés à l'envoi de messages directement auprès d'Infobip tout en utilisant Braze pour la segmentation, la personnalisation et l'orchestration des campagnes. 

#### Bannières dans Canvas

{% multi_lang_include release_type.md release="Early access" %}

Veuillez sélectionner **Bannières** comme canal de communication dans une [étape Message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) pour Canvas. Utilisez l'éditeur par glisser-déposer pour créer des messages personnalisés intégrés, offrant des expériences non intrusives et pertinentes dans leur contexte, qui se mettent à jour automatiquement au début de chaque session utilisateur. 

#### CCI dynamique

{% multi_lang_include release_type.md release="General availability" %}

Avec [la fonction CCI dynamique]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc), veuillez utiliser liquid dans votre adresse CCI. Veuillez noter que cette fonctionnalité n'est disponible que dans **les préférences d'e-mail** et ne peut pas être configurée dans la campagne elle-même. Une seule adresse CCI par destinataire d'e-mail est autorisée.

#### Limites de débit basées sur les canaux

Au lieu d'utiliser une limite de débit commune à l'ensemble d'une campagne multicanal ou d'un canvas, veuillez sélectionner une limite de débit spécifique pour chaque canal. Dans ce cas, la limite de débit s'appliquera à chacun des canaux que vous avez sélectionnés. Par exemple, configurez votre campagne ou votre Canvas pour envoyer un maximum de 5 000 webhooks et 2 500 SMS par minute pour l'ensemble de la campagne ou du Canvas. Pour plus d'informations, veuillez consulter [la section Limite de débit et limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting).

### Partenariats

#### LILT - Localisation

[LILT]({{site.baseurl}}/partners/lilt/) est la solution d'intelligence artificielle complète pour la traduction et la création de contenu en entreprise. LILT permet aux organisations internationales de développer et d'optimiser leurs contenus, leurs produits, leurs communications et leurs opérations d'assistance grâce à des agents d'intelligence artificielle et des flux de travail entièrement automatisés.

### Mises à jour importantes du SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [SDK Android 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [SDK Swift 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Supprime le fil d'actualité.
        - Cela supprime complètement tous les éléments de l'interface utilisateur, les modèles de données et les actions associés au fil d'actualité.
- [SDK Web 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 9 décembre 2025

### Rapport &de données

#### Ajouter Google Tag Manager à une page d'accueil

Pour intégrer Google Tag Manager à vos pages de destination, veuillez ajouter un bloc de code personnalisé à votre page de destination dans l'éditeur par glisser-déposer, puis [insérer le code Tag Manager]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) dans le bloc.

### Orchestration

#### Cas d'utilisation de SMS Liquid

Le cas d'utilisation « [Répondre avec différents messages en fonction du mot-clé du SMS entrant]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) » intègre le traitement dynamique des mots-clés SMS afin de répondre à des messages entrants spécifiques avec différents messages. Par exemple, vous pouvez envoyer des réponses différentes lorsque quelqu'un envoie le message « START » ou « JOIN ».

#### Liste blanche pour le contenu connecté

Vous pouvez autoriser l'utilisation d'URL spécifiques pour [le contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call). Pour accéder à cette fonctionnalité, veuillez contacter votre gestionnaire de la satisfaction client.

### Canaux&  Points de contact

#### Codage des caractères SMS

Notre [calculateur de segment SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator) dispose désormais d'un encodage des caractères. Veuillez sélectionner **« Afficher le codage des caractères** » pour identifier les caractères codés en GSM-7 ou UCS-2. 

![Calculateur de segment SMS avec un exemple de message SMS saisi dans la zone de texte et l'encodage des caractères activé.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Messages WhatsApp avec optimisation

Étant donné que l'API MM pour WhatsApp n'offre pas une livrabilité à 100 %, il est essentiel de comprendre comment recibler les utilisateurs qui n'ont peut-être pas reçu votre message sur d'autres canaux. 

Pour recibler les utilisateurs, nous vous recommandons de créer un segment d'utilisateurs qui n'ont pas reçu un message spécifique. Pour ce faire, veuillez filtrer par code `131049`d'erreur, qui indique qu'un message type marketing n'a pas été envoyé en raison de l'application de la limite de messages types marketing par utilisateur imposée par WhatsApp. Vous pouvez y parvenir en [utilisant Braze Currents ou les extensions de segments SQL]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Partenariats

#### Autres niveaux - Contenu dynamique

[OtherLevels]({{site.baseurl}}/partners/otherlevels/) est une plateforme d'expérience qui utilise l'intelligence artificielle générative pour transformer la manière dont les marques sportives, les éditeurs et les opérateurs interagissent avec leurs clients en transformant le contenu traditionnel en vidéos personnalisées et en expériences multimédias riches à grande échelle.

### SDK

#### Mises à jour importantes du SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## 11 novembre 2025

### Flexibilité des données

#### `Live Activities Push to Start Registered for App` filtre de segmentation

Le`Live Activities Push to Start Registered for App`filtre segment vos utilisateurs selon qu'ils sont enregistrés ou non pour démarrer une activité en ligne via les notifications push iOS pour une application spécifique.

#### Extensions de segments RFM SQL

Vous pouvez créer une [extension de segment RFM (récence, fréquence, montant)]({{site.baseurl}}/rfm_segments/) afin de réaliser un ciblage précis de vos meilleurs utilisateurs en évaluant leurs habitudes d'achat.

L'analyse RFM est une technique marketing qui identifie vos meilleurs utilisateurs en leur attribuant une note comprise entre 0 et 3 pour chaque catégorie (récence, fréquence, valeur monétaire), 3 étant la meilleure note et 0 la moins bonne. La récence, la fréquence et les valeurs monétaires sont toutes basées sur les données d'une période spécifique de votre choix.

#### Attributs personnalisés — Valeurs 

Lorsque vous consultez un rapport d'utilisation, veuillez sélectionner l'[onglet]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) [**Valeurs**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) pour afficher les valeurs les plus élevées des attributs personnalisés sélectionnés, sur la base d'un échantillon d'environ 250 000 utilisateurs.

#### Synchronisation des journaux et observabilité pour l'ingestion de données dans le cloud

{% multi_lang_include release_type.md release="General availability" %}

Le [tableau de bord]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) Cloud Data Ingestion (CDI) [Sync Log]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) vous permet de surveiller toutes les données traitées par CDI, de vérifier si les données ont été synchronisées avec succès et de diagnostiquer tout problème lié à des données « incorrectes » ou manquantes.

#### Déploiement de fonctionnalités à règles multiples

Utilisez [le déploiement de drapeaux de fonctionnalités à règles multiples]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) pour définir une séquence de règles d'évaluation des utilisateurs, ce qui permet une segmentation précise et un contrôle des versions des fonctionnalités. Cette méthode est particulièrement adaptée pour déployer la même fonctionnalité auprès de audiences variées.

#### Mappage vers les champs du catalogue pour les blocs de produits glisser-déposer

Dans les paramètres de votre catalogue, vous pouvez basculer sur l'option **« Blocs de produits** » pour [effectuer le mappage de champs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) et d'informations [spécifiques]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) de votre catalogue. Cela vous permet de sélectionner les champs à utiliser comme titre du produit, URL du produit et URL de l'image.

#### Limite de fréquence pour les événements d'interruption dans Currents

Lorsque vous utilisez Currents, vous pouvez désormais référencer les événements `abort_type`d'interruption de canal. Cela indique qu'un message a été interrompu en raison d'une limite de fréquence et précise quelle règle de limite de fréquence a provoqué l'interruption. Cela vous aidera à définir vos règles de limite de fréquence. Veuillez vous référer aux [événements d'engagement liés aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) pour obtenir des détails spécifiques sur les événements Currents.

### Canaux robustes

#### Images d'arrière-plan 

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez [ajouter une image d'arrière-plan]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image) à un message in-app ou à une page de destination dans le panneau **Propriétés de la ligne**. Basculez l'option **Image d'arrière-plan**, puis fournissez l'URL d'une image ou sélectionnez une image dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). Enfin, veuillez configurer votre texte alternatif, la taille, la position et si l'image doit se répéter pour créer des motifs sur toute la ligne.

![Une image d'arrière-plan représentant une pizza avec un motif répétitif horizontal.]({% image_buster /assets/img_archive/background_row.png %})

#### Copier le lien de l’aperçu

Veuillez utiliser **le lien « Copier l'aperçu** » dans vos [bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), [vos pieds de page personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer) et [vos pages d'abonnement et de désinscription aux e-mails]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers) afin de générer un lien partageable qui montre à quoi ressemblera votre contenu pour un utilisateur aléatoire.

#### Messages WhatsApp avec réception/distribution optimisée

Utilisez les systèmes d'intelligence artificielle avancés de Meta pour diffuser vos messages marketing auprès d'un plus grand nombre d'utilisateurs susceptibles d'interagir avec eux, ce qui améliore considérablement la livrabilité et l'engagement.

[Les messages WhatsApp dont la réception/distribution est optimisée]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) sont envoyés à l'aide de [la](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) nouvelle [API Marketing Messages Lite](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) de Meta, qui offre des performances supérieures à celles de l'API Cloud traditionnelle. Ce nouveau canal d'envoi vous permet de mieux atteindre les utilisateurs qui apprécient et souhaitent recevoir vos messages.

#### Flux WhatsApp

Lorsque vous intégrez un message WhatsApp Flow dans un Braze Canvas ou une campagne, vous pouvez souhaiter capturer et utiliser des informations spécifiques que les utilisateurs soumettent via le Flow. Braze a besoin de recevoir des informations supplémentaires concernant la structure de la réponse utilisateur, en particulier la forme attendue de la réponse JSON, afin de générer le schéma d'attributs personnalisés imbriqués (NCA) requis.

Vous pouvez désormais fournir à Braze les informations relatives à la structure de réponse en [enregistrant la réponse Flow en tant qu'attribut personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) et en effectuant un envoi test.

#### Aperçu utilisateur modifiable

Vous pouvez [modifier les champs individuels d'un utilisateur aléatoire ou existant]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user) afin de tester le contenu dynamique de votre message. Veuillez sélectionner **Modifier** pour convertir l'utilisateur sélectionné en un utilisateur personnalisé que vous pouvez modifier.

![L'onglet « Prévisualiser en tant qu'utilisateur » avec un bouton « Modifier ».]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### L'intelligence artificielle et l'automatisation de l’apprentissage machine.

#### BrazeAI Decisioning Studio™ Go

Vous pouvez désormais configurer votre intégration avec [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go) en vous référant à ces articles de configuration pour :

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Nouvelles fonctionnalités pour les agents Braze

{% multi_lang_include release_type.md release="Beta" %}

Vous pouvez désormais personnaliser votre [Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) de manière personnalisée en :

- Appliquer [les directives de marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) que votre agent doit respecter dans sa réponse. 
- Veuillez vous référer à un catalogue pour réaliser une personnalisation supplémentaire de votre message.
- Structurer la sortie d'un agent en fournissant le [format de sortie]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format).
- Adjusting the [temperature]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) for the level of deviation in your agent's production.

### Modèles ChatGPT avec BrazeAI Operator<sup>TM</sup>

{% multi_lang_include release_type.md release="Beta" %}

Vous pouvez sélectionner parmi ces modèles GPT à utiliser pour différents types de requêtes avec [Operator]({{site.baseurl}}/user_guide/brazeai/operator) :

- GPT-5 nano
- GPT-5 mini (par défaut)
- GPT-5

### Nouveaux partenariats Braze

#### StackAdapt - Publicité

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) est une plateforme marketing alimentée par l'intelligence artificielle qui propose des publicités ciblées axées sur la performance. Il vous permet de synchroniser les données des profils utilisateurs de Braze vers le Data Hub de StackAdapt. En connectant les deux plateformes, vous pouvez créer une vue unifiée de vos clients et activer les données first-party afin d'améliorer les performances publicitaires.

#### Cloudinary - Contenu dynamique

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) est une plateforme d'images et de vidéos qui vous permet de gérer, modifier, optimiser et diffuser des images et des vidéos à grande échelle pour toute campagne, sur tous les canaux et tout au long du parcours client. Une fois intégrée et activée, la gestion des médias de Cloudinary optimisera et fournira une diffusion dynamique, contextuelle et personnalisée des ressources pour vos campagnes Braze et vos canevas.

#### Kameleoon - Test A/B

[Kameleoon]({{site.baseurl}}/partners/kameleoon/) est une solution d'optimisation qui regroupe des fonctionnalités d'expérimentation, de personnalisation basée sur l'intelligence artificielle et de gestion des fonctionnalités au sein d'une plateforme unifiée.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK React native 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Corrige le type Typescript pour le rappel de`subscribeToInAppMessage`et`addListener`pour `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Ces auditeurs renvoient désormais correctement un rappel avec le nouveau`InAppMessageEvent`type. Auparavant, les méthodes étaient annotées pour renvoyer un`BrazeInAppMessage`type, mais elles renvoyaient en réalité un `String`.
         - Si vous utilisez l'une ou l'autre des API d'abonnement, veuillez vous assurer que le comportement de vos messages in-app reste inchangé après la mise à jour vers cette version. Veuillez consulter notre exemple de code dans `BrazeProject.tsx`.
    - Les API `logInAppMessageClicked`, `logInAppMessageImpression`, et  `logInAppMessageButtonClicked`n'acceptent désormais qu'un`BrazeInAppMessage`  objet pour correspondre à son interface publique existante.
        - Auparavant, il acceptait à la fois un`BrazeInAppMessage`objet et un `String`.
    - `BrazeInAppMessage.toString()` renvoie désormais une chaîne de caractères lisible par l'utilisateur au lieu de la représentation JSON de la chaîne de caractères.
        - Pour obtenir la représentation sous forme de chaîne de caractères JSON d'un message in-app, veuillez utiliser `BrazeInAppMessage.inAppMessageJsonString`.
    - Sur iOS, l'application`[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` a été déplacée vers`[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - Cette nouvelle méthode est désormais une méthode de classe au lieu d'une méthode d'instance.
    - Ajoute des annotations de nullabilité aux`BrazeReactUtils`méthodes.
    - Supprime les méthodes et propriétés obsolètes suivantes de l'API :
        - `getInstallTrackingId(callback:)` en faveur de `getDeviceId`.
        - `registerAndroidPushToken(token:)` en faveur de `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` en faveur de `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` en faveur de `payload_type`.
        - `PushNotificationEvent.deeplink` en faveur de `url`.
        - `PushNotificationEvent.content_text` en faveur de `body`.
        - `PushNotificationEvent.raw_android_push_data` en faveur de `android`.
        - `PushNotificationEvent.kvp_data` en faveur de `braze_properties`.
    - Mise à jour des liaisons de version native du SDK Android [de Braze Android SDK 39.0.0 à 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK .NET MAUI (Xamarin) version 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Nous avons mis à jour la liaison iOS [de Braze Swift SDK 12.1.0 à 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Cela inclut la prise en charge de Xcode 26.
- [SDK Flutter 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Mise à jour du pont Android natif [de Braze Android SDK 39.0.0 à 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK Braze Swift 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Web 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [SDK Android 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## Sortie le 14 octobre 2025

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) remplace les tests A/B par une prise de décision basée sur l'intelligence artificielle qui effectue la personnalisation de tout et optimise tous les indicateurs : générez des revenus, pas des clics. Grâce à BrazeAI Decisioning Studio™, vous pouvez optimiser tous les indicateurs clés de performance (KPI) de votre entreprise. Veuillez consulter notre section dédiée [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) pour découvrir des exemples d'utilisation et les principales fonctionnalités.

### Flexibilité des données

#### Nouveaux événements Currents

Ces nouveaux événements ont été ajoutés au [glossaire]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) :

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

Ces nouveaux champs ont été ajoutés aux événements Currents suivants :

- `is_sms_fallback` : 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id`, `in_reply_to`, `flow_id`, `flow_response_json`, `product_id`, `catalog_id`: 
  - `users.messages.whatsapp.InboundReceive`
- `message_id`, `flow_id`, `template_name`: 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Listes de suppression

{% multi_lang_include release_type.md release="General availability" %}

[Les listes de suppression]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) sont des groupes d'utilisateurs qui ne reçoivent automatiquement aucune campagne ni aucun Canvases. Les listes de suppression sont définies par des filtres de segment, et les utilisateurs sont ajoutés ou retirés de ces listes lorsqu'ils répondent aux critères de filtrage.

#### Personnalisation sans copie

{% multi_lang_include release_type.md release="Early access" %}

Synchronisez les déclencheurs Canvas à l'aide de l'ingestion de données pour [une personnalisation sans copie]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). Cette fonctionnalité permet d'accéder aux informations spécifiques à l'utilisateur à partir de votre solution de stockage de données et les transmet à un canvas de destination. Les étapes du canvas peuvent éventuellement inclure des champs de personnalisation qui ne sont pas conservés dans les profils utilisateurs Braze.

#### Variables Canvas Context pour les étapes « Parcours d'audience » et « Étape de l'arbre décisionnel »

{% multi_lang_include release_type.md release="Early access" %}

Vous pouvez [créer des filtres de variables de contexte]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters) qui utilisent des variables de contexte précédemment déclarées dans les étapes [du parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) et [de l'arbre décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

### Libérer la créativité

#### Cartes promotionnelles pour les e-mails

Veuillez utiliser [les cartes de transaction]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab) pour fournir les informations essentielles relatives à la transaction directement en haut du corps des e-mails. Cela permet aux destinataires de comprendre rapidement les détails de l'offre et de prendre les mesures nécessaires.

#### Modèles pour bannières

Lorsque vous [créez votre bannière]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create), vous pouvez désormais commencer avec un modèle vierge, utiliser un modèle Braze ou sélectionner un modèle de bannière enregistré.

### Canaux robustes

#### Listes de suppression

{% multi_lang_include release_type.md release="General availability" %}
 
[Les listes de suppression]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/) spécifient les groupes d'utilisateurs qui ne recevront jamais de messages. Les administrateurs peuvent créer des listes de suppression avec des filtres de segmentation pour restreindre un groupe d'utilisateurs de la même manière que vous le feriez pour la segmentation.

#### Suivi des clics LINE

{% multi_lang_include release_type.md release="General availability" %}

Lorsque [le suivi des clics LINE]({{site.baseurl}}/line/click_tracking/) est activé, Braze raccourcit automatiquement vos URL, ajoute des mécanismes de suivi et enregistre les clics en temps réel. Alors que LINE fournit des données agrégées sur les clics, Braze offre des informations détaillées sur les utilisateurs, qui sont opportunes et exploitables. Ces données vous permettent de créer des stratégies de segmentation et de reciblage plus ciblées, telles que la segmentation des utilisateurs en fonction de leur comportement de clic et le déclenchement de messages en réponse à des clics spécifiques.

#### Filtrage des clics des bots SMS et RCS

{% multi_lang_include release_type.md release="General availability" %}

[Le filtrage des clics des bots SMS et RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) améliore l'analyse des campagnes et les flux de travail en excluant les clics suspects provenant de bots. Un « clic de bot » désigne les clics automatisés sur des liens raccourcis dans les SMS et les messages RCS, tels que ceux provenant de robots d'indexation, d'aperçus de liens Android et iOS ou de logiciels de sécurité CPaaS. Cette fonctionnalité facilite la création de rapports précis, la segmentation et l'orchestration afin d'interagir avec de véritables utilisateurs.

#### Transférer des numéros de téléphone WhatsApp

Veuillez transférer le numéro de téléphone d'un compte WhatsApp Business (WABA) et le groupe d'abonnement associé [d'un espace de travail à un autre]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) au sein de Braze.

#### WhatsApp Flows : messages de réponse et aperçu

Dans un canvas, vous pouvez créer une étape de message WhatsApp qui utilise un [message de réponse]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) et un message de flux. Vous pouvez également sélectionner **« Preview Flow** » (Aperçu du flux) pour prévisualiser le flux directement dans Braze afin de vérifier qu'il se comporte comme prévu.

#### Messages relatifs aux produits WhatsApp

[Les messages produits]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/) vous permettent d'envoyer des messages WhatsApp interactifs qui présentent des produits directement à partir de votre catalogue Meta.

#### Intégration de Braze et WhatsApp à un système externe

[Tirez parti de la puissance des chatbots basés sur l'intelligence artificielle et des transferts vers des agents en ligne]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) sur le canal WhatsApp pour optimiser vos opérations de support client. En automatisant les demandes courantes et en transférant de façon fluide les appels vers des agents humains lorsque cela est nécessaire, vous pouvez considérablement améliorer les temps de réponse et l'expérience client globale.

### L'intelligence artificielle et l'automatisation de l’apprentissage machine.

#### Agents Braze

{% multi_lang_include release_type.md release="Beta" %}

[Les agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/) sont des assistants alimentés par l'intelligence artificielle que vous pouvez créer dans Braze. Les agents peuvent générer du contenu, prendre des décisions éclairées et enrichir vos données afin que vous puissiez offrir des expériences client plus personnalisées.

### Nouveaux partenariats Braze

#### Jasper - Modèles

L'intégration de [Jasper]({{site.baseurl}}/partners/jasper/) à Braze vous permet de rationaliser la création de contenu et l'exécution des campagnes. Grâce à Jasper, vos équipes marketing peuvent créer en quelques minutes des contenus de haute qualité, parfaitement adaptés à votre marque. Braze facilite ensuite la réception/distribution de ces messages auprès de l’audience appropriée au moment opportun. Cette intégration favorise des flux de travail fluides, réduit les efforts manuels et renforce l'engagement.

#### Swym - Fidélisation et reciblage

[Swym]({{site.baseurl}}/partners/swym/) aide les marques de commerce électronique à identifier les intentions d'achat grâce à des fonctionnalités telles que les listes de souhaits, les options « Enregistrer pour plus tard », les listes de cadeaux et les alertes de réapprovisionnement. Grâce à des données riches et basées sur les autorisations, vous pouvez élaborer des campagnes hyper-ciblées et offrir des expériences d'achat personnalisées qui stimulent l'engagement, augmentent les conversions et renforcent la fidélité.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez consulter toutes les autres mises à jour en vérifiant les journaux des modifications SDK correspondants.

- [SDK Cordova 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Mise à jour du pont Android natif [de Braze Android SDK 37.0.0 à 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - La version minimale requise de GradlePluginKotlinVersion est désormais 2.1.0.
    - Mise à jour du pont iOS natif [de Braze Swift SDK 12.0.0 à 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Cela inclut la prise en charge de Xcode 26.
    - Supprime la prise en charge du fil d'actualité. Les API suivantes ont été supprimées :
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [SDK React native 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Mise à jour des liaisons de version native du SDK Android [de Braze Android SDK 37.0.0 à 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Supprime la prise en charge du fil d'actualité. Les API suivantes ont été supprimées :
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [SDK Web 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [SDK Flutter 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [SDK Unity 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Mise à jour du pont iOS natif [de Braze Swift SDK 12.0.0 à 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Cela inclut la prise en charge de Xcode 26.

{% enddetails %}
{% details September 16, 2025 %}

## Sortie le 16 septembre 2025

### Flexibilité des données

#### Plateforme de données Braze

La plateforme de données Braze est un ensemble complet et modulable de fonctionnalités de données et d'intégrations de partenaires qui vous permet de créer des expériences personnalisées et percutantes tout au long du cycle de vie du client. Veuillez vous renseigner sur les trois tâches liées aux données à accomplir : 

- [Unification des données]({{site.baseurl}}/user_guide/data/unification)
- [Activation des données]({{site.baseurl}}/user_guide/data/activation)
- [Distribution des données]({{site.baseurl}}/user_guide/data/distribution)

#### Propriétés de la bannière personnalisée

{% multi_lang_include release_type.md release="Early access" %}

Vous pouvez utiliser les propriétés personnalisées de votre campagne Banner pour récupérer des données clé-valeur via le SDK et modifier le comportement ou l'apparence de votre application. Pour en savoir plus, veuillez consulter [les propriétés des bannières personnalisées]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Authentification par jeton

{% multi_lang_include release_type.md release="General availability" %}

Lorsque vous utilisez le contenu connecté de Braze, vous pouvez constater que certaines API nécessitent un jeton au lieu d'un nom d'utilisateur et d'un mot de passe. Braze peut stocker des informations d'identification contenant [des valeurs d'en-tête d'authentification par jeton]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication).

#### Codes de promotion

Vous pouvez enregistrer les codes de promotion dans le profil utilisateur via l'étape Mise à jour de l'utilisateur. Pour plus d'informations, veuillez vous référer à [la section Enregistrement des codes de promotion dans les profils utilisateurs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile).

### Libérer la créativité

#### Braze Pilot

[Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot) est une application accessible au public pour Android et iOS qui vous permet d'envoyer des messages depuis votre tableau de bord de Braze vers votre téléphone. Veuillez consulter la section [« Premiers pas avec Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) » pour obtenir des instructions détaillées sur le téléchargement de l'application, l'initialisation de la connexion à votre tableau de bord de Braze et la finalisation de la configuration.

### Nouveaux partenariats Braze

#### Blings - Contenu visuel et interactif

[Blings]({{site.baseurl}}/partners/blings/) est une plateforme vidéo personnalisée de nouvelle génération qui vous permet de proposer des expériences vidéo en temps réel, interactives et basées sur les données, à grande échelle et sur tous les canaux.

#### Intégration standard de Shopify avec un outil tiers

Pour les boutiques en ligne Shopify, nous recommandons d'utiliser la méthode d'intégration standard de Braze afin de prendre en charge les SDK Braze sur votre site.

Cependant, nous comprenons que vous puissiez préférer utiliser un outil tiers, tel que Google Tag Manager. Nous avons donc élaboré un guide expliquant comment procéder. Pour commencer, veuillez consulter [Shopify : Marquage par ]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/)des tiers.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Braze Flutter 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Mise à jour du pont Android natif de Braze Android SDK`36.0.0`vers `39.0.0`.
    - Mise à jour du pont iOS natif de Braze Swift SDK`13.2.0``12.0.0`. Cela inclut la prise en charge de Xcode 26.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Met à jour les bindings du SDK Swift de Braze pour exiger les versions de la dénomination `13.0.0+` SemVer. Cela permet la compatibilité avec n'importe quelle version du SDK de Braze, de `13.0.0` jusqu'à, mais sans inclure, `14.0.0`.

{% enddetails %}
{% details August 19, 2025 %}

## Sortie le 19 août 2025

### Normalisation de la cohérence des fuseaux horaires dans Canvas Context

{% multi_lang_include release_type.md release="Early access" %}

Si vous participez à [l'accès anticipé à l'étape]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) du [canvas Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), tous les horodatages de type date/heure provenant des propriétés d'événement dans les canevas basés sur des actions seront systématiquement normalisés en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Pour en savoir plus à ce sujet, veuillez consulter la section [Normalisation de la cohérence des fuseaux horaires]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization).

### Flexibilité des données

#### Domaines personnalisés en libre-service

{% multi_lang_include release_type.md release="General access" %}

[Les domaines personnalisés en libre-service]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) vous permettent de configurer et de gérer vos propres domaines personnalisés pour les SMS, les RCS et WhatsApp, directement depuis le tableau de bord de Braze. Vous pouvez facilement ajouter, surveiller et gérer jusqu'à 10 domaines personnalisés en un seul endroit.

#### Statistiques sur l'entonnoir de segment

Veuillez sélectionner [Afficher les statistiques de l'entonnoir]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) pour afficher les statistiques de ce groupe de filtres et observer l'impact de chaque filtre ajouté sur les statistiques de votre segment. Vous verrez un nombre estimé et un pourcentage d'utilisateurs soumis au ciblage par tous les filtres jusqu'à ce stade. Une fois les statistiques affichées pour un groupe de filtres, elles se mettront à jour automatiquement chaque fois que vous modifierez les filtres. 

#### Nouveaux champs de réponse pour`/campaigns/details`l'endpoint des notifications push

La`messages`réponse aux notifications push comprend désormais deux nouveaux champs :

- `image_url` : URL d'une image pour une notification Android, une notification iOS ou une icône de notification push Web.
- `large_image_url` : URL d'image de notification push pour les actions de notification push Android Chrome et Windows.

#### Définition des champs PII

La sélection et [la définition de certains champs comme champs PII]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) n'affectent que ce que les utilisateurs peuvent voir sur le tableau de bord de Braze et n'ont aucune incidence sur la manière dont les données des utilisateurs finaux dans ces champs PII sont traitées.

Veuillez consulter votre équipe juridique afin d'aligner les paramètres de votre tableau de bord sur les réglementations et politiques de confidentialité applicables à votre entreprise, y compris celles relatives à [la conservation des données]({{site.baseurl}}/api/data_retention/).

#### Partager un lien de téléchargement du générateur de rapports

Vous pouvez [partager un lien]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) vers le [tableau de bord]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) du rapport en sélectionnant **Partager**, puis **Partager un lien** ou **Envoyer ou effectuer la planification d'un e-mail**.

### Libérer la créativité

#### Balises d'en-tête personnalisées pour les e-mails glisser-déposer

Veuillez utiliser`<head>`les tags pour ajouter du CSS et des métadonnées à votre message d'e-mail. Par exemple, vous pouvez utiliser ces tags pour ajouter une feuille de style ou une favicon. Le liquide est pris en charge dans`<head>`les tags.

### Canaux robustes

#### Meilleures pratiques en matière de flou

Nous avons ajouté une [section consacrée aux meilleures pratiques]({{site.baseurl}}) afin de vous aider à configurer de manière réfléchie votre message de désinscription flou et à créer une expérience claire, conforme et positive pour vos utilisateurs abonnés.

#### Flux WhatsApp

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) est une amélioration du canal de communication WhatsApp existant, qui vous permet de créer des expériences de communication interactives et dynamiques. 

#### Questions relatives aux produits reçues via WhatsApp

Les utilisateurs peuvent répondre à votre message concernant un produit ou un catalogue en posant [des questions sur le produit]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions). Ces messages sont reçus en tant que messages entrants, qui peuvent ensuite être triés à l'aide d'un parcours d’action.

De plus, Braze extrait l'ID du produit et l'ID du catalogue à partir de ces questions. Ainsi, si vous souhaitez automatiser les réponses ou envoyer des questions à une autre équipe (telle que le service client), vous pouvez inclure ces informations.

### L'intelligence artificielle et l'automatisation de l’apprentissage machine.

#### Nouveaux articles sur les cas d'utilisation de BrazeAI™

Nous avons ajouté de nouveaux articles sur les cas d'utilisation afin de vous aider à tirer le meilleur parti de BrazeAI™. Ces guides mettent en avant des méthodes pratiques pour intégrer l'intelligence artificielle à vos stratégies d'engagement, notamment :

- [Prédiction du taux d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_churn/use_case) : Identifiez les clients susceptibles de se désabonner et prenez des mesures à un stade précoce.
- [Événements prévisibles]({{site.baseurl}}/user_guide/brazeai/predictive_events/use_case) : Anticipez les actions clés des utilisateurs et façonnez les expériences en temps réel.
- [Recommandations]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): Proposez des contenus et des produits plus pertinents en fonction du comportement des clients.

#### Serveur MCP

{% multi_lang_include release_type.md release="Beta" %}

Le [serveur MCP de]({{site.baseurl}}/user_guide/brazeai/mcp_server/) [Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server/), une connexion sécurisée et en lecture seule, permet aux outils d'intelligence artificielle tels que Claude et Cursor d'accéder aux données Braze non personnelles afin de répondre à des questions, d'analyser des tendances et de fournir des informations sans modifier les données.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Swift 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Étend la fonctionnalité de`BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`  en tant que déclencheur pour les erreurs d'authentification « facultatives ».
        - La méthode `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)`déléguée sera désormais un déclencheur pour les erreurs d'authentification « Obligatoire » et « Facultative ».
        - Si vous souhaitez uniquement traiter les erreurs d'authentification SDK « obligatoires », veuillez ajouter une vérification garantissant que`BrazeSDKAuthError.optional`  est faux dans votre implémentation de cette méthode déléguée.
    - Modifie l'utilisation de`Braze.Configuration.sdkAuthentication`  pour qu'elle prenne effet lorsqu'elle est activée.
        - Auparavant, la valeur de cette configuration n'était pas prise en compte par le SDK et le jeton était systématiquement joint aux requêtes s'il était présent.
        - Désormais, le SDK n'associera le jeton d'authentification SDK aux requêtes réseau sortantes que lorsque cette configuration est activée.
    - Les paramètres pour toutes les propriétés de`Braze.FeatureFlag`et toutes les propriétés de`Braze.Banner`ont été définis`private`. Les propriétés de ces classes sont désormais en lecture seule.
    - Supprime la`Braze.Banner.id`propriété, qui était obsolète dans la version`11.4.0`.
        - Veuillez utiliser à la place`Braze.Banner.trackingId` pour lire l'ID de suivi de campagne d'une bannière.
- [SDK React native 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Mise à jour des liaisons de version native du SDK Android de [Braze Android SDK 36.0.0 à 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Mise à jour des liaisons de version du SDK Swift natif de [Braze Swift SDK 12.0.0 à 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - L'événement`sdkAuthenticationError` sera désormais un déclencheur pour les erreurs d'authentification « obligatoires » et « facultatives ».
- [SDK Xamarin 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Ajout de la prise en charge de .NET 9.0 pour les liaisons iOS et Android.
        - Cela supprime la prise en charge de .NET 8.0.
        - Cela nécessite [au](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0) [minimum ](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0)la [version iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Nous avons mis à jour la liaison Android de [Braze Android 32.0.0 à 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Mise à jour de la liaison iOS de [Braze Swift SDK 10.0.0 à 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Cette version contient des API pour la fonctionnalité Bannières, mais n'est actuellement pas entièrement prise en charge par ce SDK. Si vous souhaitez utiliser des bannières dans votre application .NET MAUI, veuillez contacter votre gestionnaire du service clientèle avant l’intégration des bannières dans votre application.
- [SDK Cordova 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Mise à jour de l'implémentation iOS interne de`enableSdk`la méthode pour utiliser `setEnabled`: à la place de `_requestEnableSDKOnNextAppRun`, qui a été déprécié dans le SDK Swift.
    - L'appel de cette méthode ne nécessite plus le redémarrage de l'application pour prendre effet. Le SDK sera désormais activé dès que cette méthode sera exécutée.
    - Mise à jour du pont Android [`36.0.0``37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)natif de [Braze Android SDK.](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

{% enddetails %}
{% details July 22, 2025 %}

## Sortie le 22 juillet 2025

### Exportation d'événements de sécurité avec Amazon S3

Vous pouvez [exporter]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/) automatiquement [les événements de sécurité vers Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/), un fournisseur de stockage cloud, grâce à une tâche quotidienne qui s'exécute à minuit UTC. Une fois configuré, il n'est pas nécessaire d'exporter manuellement les événements de sécurité depuis le tableau de bord.

### Flexibilité des données

#### Importation CSV

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez utiliser l'importation CSV pour enregistrer et mettre à jour les attributs utilisateur et les événements personnalisés dans Braze, tels que `first_name`,`last_destination_searched` , et `trip_booked`. Pour commencer, consultez la section [Importation de fichiers CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### Alertes relatives à l'utilisation de l'API

{% multi_lang_include release_type.md release="General availability" %}

Les alertes d'utilisation des API offrent une visibilité essentielle sur l'utilisation de vos API, vous permettant de détecter de manière proactive tout trafic inattendu. En configurant ces alertes pour suivre les volumes de requêtes API clés, vous pouvez recevoir des notifications en temps réel et résoudre les problèmes avant qu'ils n'aient un impact sur vos campagnes marketing.

#### Limites de débit de l'API Workspace

Les limites de débit de l'API de l'espace de travail vous permettent de définir le nombre maximal de requêtes API qu'un espace de travail peut envoyer à un endpoint spécifique d'ingestion de données, tel que`/users/track`ou les données SDK. Vous pouvez également appliquer des limites de débit à un groupe d'espaces de travail, ce qui signifie que la limite est partagée entre tous les espaces de travail de ce groupe.

#### Nouveaux événements Currents

Ces nouveaux événements ont été ajoutés au glossaire Currents :

- [Bannière Événements d'abandon]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Bannière Cliquez sur les événements]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Evénements d'impression de la bannière]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [Bannière Événements consultés]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Événements d'échec de webhook]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### Intervalle de temps par défaut pour l'analyse des campagnes

Par défaut, la période prise en compte par [**Campaign Analytics**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) correspond aux 90 derniers jours à compter de la date actuelle. Cela signifie que si la campagne a été lancée il y a plus de 90 jours, les analyses afficheront « 0 » pour la période donnée. Pour consulter toutes les analyses des campagnes antérieures, veuillez ajuster la période de référence du rapport.

#### Mise à jour du comportement de l'étape « Chemins d’expérience » dans Canvas

Si votre canevas comporte une [expérience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) active ou en cours et que vous mettez à jour le canevas actif (même si ce n'est pas à l'étape des chemins d'expérience), l'expérience en cours prendra fin. Pour redémarrer l'expérience, vous pouvez déconnecter le chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et en lancer un nouveau. 

Pour plus d'informations, consultez [Modification d’un canvas après son lancement]({{site.baseurl}}/post-launch_edits/).

#### Limite de débit plus rapide disponible pour`/users/export/ids`l'endpoint

Vous pouvez également augmenter la [limite de débit pour l'endpoint /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) à 40 requêtes par seconde en respectant les conditions suivantes :

- Votre espace de travail dispose d'une limite de débit par défaut (250 requêtes par minute) activée. Veuillez contacter votre gestionnaire de compte Braze pour obtenir de l'aide afin de supprimer toute limite de débit préexistante dont vous pourriez disposer.
- Votre requête inclut lefields_to_exportparamètre permettant de lister tous les champs que vous souhaitez recevoir.

#### Nouvelle traduction pour les endpoints de modèles d'e-mails

{% multi_lang_include release_type.md release="Early access" %}

Veuillez utiliser ces endpoints pour afficher et mettre à jour les traductions et les paramètres régionaux des modèles d'e-mails :

- [GET : Veuillez consulter les traductions sources.]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET : Afficher une traduction et une locale spécifiques pour l'endpoint du modèle d'e-mail]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_locale_template)
- [GET : Afficher toutes les traductions et toutes les configurations régionales pour un modèle d'e-mail]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_template)
- [PUT : Mettre à jour les traductions d'un modèle d'e-mail]({{site.baseurl}}/api/endpoints/translations/email_templates/put_update_template)

### Libérer la créativité

#### Landing pages

Vous pouvez rendre votre page d'accueil [réactive à la taille de l'appareil de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) en empilant verticalement les colonnes sur les écrans plus petits. Pour ce faire, veuillez ajouter une colonne à la ligne que vous souhaitez rendre réactive, puis basculez l'option **« Empiler verticalement sur les petits écrans** » dans la section **« Personnaliser les colonnes** ».

### Canaux robustes

#### Filtrage des bots pour les e-mails

{% multi_lang_include release_type.md release="General availability" %}

Configurez le filtrage des robots dans vos [préférences d'e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) pour exclure tous les clics suspectés d'être des machines ou des robots. Un "bot click" dans un e-mail fait référence à un clic sur des hyperliens dans un e-mail qui est généré par un programme automatisé. En filtrant ces clics de robots, vous pouvez déclencher et envoyer intentionnellement des messages à des destinataires qui sont engagés.

#### Glisser-déposer des blocs de produits

{% multi_lang_include release_type.md release="Early access" %}

L'[éditeur]({{site.baseurl}}/dnd_product_blocks/) [par glisser-déposer]({{site.baseurl}}/dnd_product_blocks/) vous permet d'ajouter et de configurer rapidement des blocs de produits à vos messages pour une présentation fluide des produits, sans avoir à créer de code Liquid personnalisé. La fonctionnalité de bloc de produit par glisser-déposer n'est actuellement disponible que pour les e-mails.

#### Texte pour les pages d'accueil et les messages in-app

Le texte en enjambement vous permet d'appliquer un style spécifique à des blocs de texte sans code personnalisé pour vos [pages de destination]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) et [vos messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks). Pour ce faire, veuillez sélectionner le texte que vous souhaitez mettre en forme, puis choisissez **l'option « Envelopper avec span » pour le style**. 

#### Cliquez ici pour accéder à WhatsApp

[Les publicités qui renvoient vers WhatsApp]({{site.baseurl}}/whatsapp_use_cases/) constituent un moyen efficace d'attirer de nouveaux clients et de fidéliser les clients existants à partir des publicités Meta sur Facebook, Instagram ou d'autres plateformes. Veuillez utiliser ces publicités pour promouvoir vos produits et services tout en informant les utilisateurs de votre présence sur WhatsApp. 

### Nouveaux partenariats Braze

#### API Shopify Visitory — Commerce électronique

Braze recueille des informations sur les visiteurs, telles que les adresses e-mail et les numéros de téléphone, par le biais de messages dans le navigateur. Ces informations sont ensuite envoyées à Shopify. Ces données aident les commerçants à reconnaître les visiteurs de leur magasin et à créer une expérience d'achat plus personnalisée.

#### Okendo — Commerce électronique

L'intégration de Braze et [Okendo]({{site.baseurl}}/partners/okendo/) fonctionne sur plusieurs produits de la plateforme Okendo, notamment les avis, la fidélisation, les recommandations, les sondages et les quiz. Okendo transmet des événements personnalisés et des attributs utilisateur à Braze, qui peuvent être utilisés pour personnaliser et déclencher des messages.

#### Lemnisk — Plateforme de données client

L'intégration de Braze et [Lemnisk]({{site.baseurl}}/partners/lemnisk/) permet aux marques et aux entreprises d'exploiter pleinement le potentiel de Braze en agissant comme une couche d'intelligence guidée par la CDP qui unifie les données utilisateur sur toutes les plateformes en temps réel et en envoyant les informations et les comportements de l'utilisateur collectés à Braze en temps réel.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Suppression des`Banner.html`propriétés et des`logBannerImpressions` méthodes`logBannerClick`. Veuillez utiliser à la place[`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner), qui gère automatiquement le suivi des impressions et des clics.
    - Suppression de la prise en charge de l'ancienne fonctionnalité Fil d'actualité. Cela inclut la suppression de la classe Feed et des méthodes associées.
    - Les champs created et categories utilisés par les anciennes cartes de fil d'actualité ont été supprimés des[`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html)sous-classes.
    - Le champ linkText a également été supprimé de la [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html)sous-classe Card et de son constructeur.
    - Définitions clarifiées et types mis à jour afin d'indiquer que certaines méthodes SDK renvoient explicitement une valeur indéfinie lorsque le SDK n'est pas initialisé, alignant ainsi les typages sur le comportement réel lors de l'exécution. Cela pourrait introduire de nouvelles erreurs TypeScript dans les projets qui s'appuyaient sur les typages précédents (incomplets).
    - Les images des messages in-app avec`cropType`  de`CENTER_CROP`  (telles que`FullScreenMessage`  par défaut) sont désormais rendues via une`<img>`étiquette  au lieu de`<span>`  afin d'améliorer l'accessibilité. Cela pourrait perturber les personnalisations CSS personnalisées pour la`.ab-center-cropped-img`classe ou ses éléments enfants.
- [SDK Cordova 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Mise à jour de l'implémentation iOS interne de`enableSdk`la méthode pour utiliser setEnabled: à la place de `_requestEnableSDKOnNextAppRun`, qui a été déprécié dans le SDK Swift.
        - L'appel de cette méthode ne nécessite plus le redémarrage de l'application pour prendre effet. Le SDK sera désormais activé dès que cette méthode sera exécutée.
    - Mise à jour du pont Android natif [de Braze Android SDK 36.0.0 à 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK Android 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SDK Swift 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
