---
nav_title: Accueil
article_title: Quoi de neuf dans Braze ?
description: "Les notes de mise à jour de Braze sont publiées mensuellement afin que vous puissiez vous tenir au courant des versions majeures du produit, des améliorations continues du produit, des partenariats de Braze, des changements de SDK et de l'élimination des fonctionnalités."
page_order: 0
search_rank: 1
page_type: reference

---

# Quoi de neuf dans Braze ?

{% alert tip %}
Pour plus d'informations sur l'une des mises à jour énumérées sur cette page, contactez votre gestionnaire de compte ou [ouvrez un ticket d'assistance.]({{site.baseurl}}/user_guide/administrative/access_braze/support/) Vous pouvez également consulter notre [journal des modifications du]({{site.baseurl}}/developer_guide/changelogs) SDK pour plus d'informations sur les versions mensuelles du SDK, les améliorations et les ruptures.
{% endalert %}

{% details January 8, 2026 %}
## Publication le 8 janvier 2026

### Données & Rapports

#### Événements recommandés pour le commerce électronique

{% multi_lang_include release_type.md release="Early access" %}

Pour faire correspondre les événements recommandés pour le commerce électronique avec l'événement d'achat existant, nous avons ajouté l'[événement de conversion "Passe une commande"]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report), qui est similaire à l'événement "Effectue un achat".

#### Mises à jour des événements en cours

{% multi_lang_include release_type.md release="General availability" %}

Les changements suivants ont été apportés à Currents dans la version 4 :

* Le champ change pour le type d'événement `users.behaviors.pushnotification.TokenStateChange`:
    * Ajout d'un nouveau champ `string` `push_token` : Jeton de l'événement
* Le champ change pour le type d'événement `users.messages.pushnotification.Bounce`:
    * Ajout d'un nouveau champ `string` `push_token` : Jeton de l'événement
* Le champ change pour le type d'événement `users.messages.pushnotification.Send`:
    * Ajout d'un nouveau champ `string` `push_token` : Jeton de l'événement
* Le champ change pour le type d'événement `users.messages.rcs.Click`:
    * Ajout d'un nouveau champ `string` `canvas_variation_name` : Nom de la variation de canvas reçue par cet utilisateur
    * Le champ `user_phone_number` est désormais *facultatif*.
* Le champ change pour le type d'événement `users.messages.rcs.InboundReceive`:
    * Le champ `user_id` est désormais *facultatif*.
* Le champ change pour le type d'événement `users.messages.rcs.Rejection`:
    * Ajout d'un nouveau champ `string` `canvas_step_message_variation_id` : ID API de la variation de message de l'étape de Canvas que l’utilisateur a reçue

Reportez-vous au [journal des modifications de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) pour connaître les modifications apportées à chaque version.

#### Exporter les journaux de synchronisation par toutes les lignes

{% multi_lang_include release_type.md release="Early access" %}

Dans le [tableau de bord Cloud Data Ingestion **Sync Log**]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), vous pouvez choisir d'exporter les journaux de niveau ligne pour une exécution de synchronisation par :

* Lignes avec des erreurs Télécharge un fichier contenant uniquement les lignes ayant un statut d'**erreur.** 
* Toutes les lignes Télécharge un fichier contenant toutes les lignes traitées au cours de l'exécution.

### Canaux & Points de contact

#### Apportez votre propre connecteur WhatsApp (BYO)

Le [connecteur WhatsApp Bring Your Own (BYO)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/) propose un partenariat entre Braze et Infobip, dans le cadre duquel vous donnez à Braze l'accès à votre gestionnaire WhatsApp d'Infobip (WABA). Cela vous permet de gérer et de payer les coûts d'envoi de messages directement avec Infobip tout en utilisant Braze pour la segmentation, la personnalisation et l'orchestration des campagnes. 

#### Bannières en canvas

{% multi_lang_include release_type.md release="Early access" %}

Vous pouvez sélectionner les **bannières** comme canal de communication dans une [étape du]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) canvas. Vous pouvez utiliser l'éditeur par glisser-déposer pour créer des messages en ligne personnalisés, offrant des expériences non intrusives et contextuellement pertinentes qui se mettent à jour automatiquement au début de chaque session utilisateur. 

#### CCI dynamique

{% multi_lang_include release_type.md release="General availability" %}

Avec la [CCI dynamique]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc), vous pouvez utiliser du liquide dans votre adresse de CCI. Notez que cette fonctionnalité n'est disponible que dans les **préférences d'e-mail** et ne peut pas être définie dans la campagne elle-même. Une seule adresse CCI est autorisée par destinataire de l'e-mail.

#### Limites de débit basées sur le canal

Au lieu d'une limite de débit qui s'applique à l'ensemble d'une campagne multicanal ou d'un Canvas, vous pouvez sélectionner une limite de débit spécifique par canal. Dans ce cas, la limite de débit s'appliquera à chacun des canaux que vous avez sélectionnés. Par exemple, vous pouvez paramétrer votre campagne ou Canvas pour qu'elle envoie un maximum de 5 000 webhooks et 2 500 messages SMS par minute sur l'ensemble de la campagne ou du Canvas. Pour plus de détails, voir [Limitation du débit et limitation de fréquence.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting)

### Partenariats

#### LILT - Localisation

[LILT]({{site.baseurl}}/partners/lilt/) est la solution complète d'intelligence artificielle pour la traduction et la création de contenu en entreprise. LILT permet aux organisations mondiales de mettre à l'échelle et d'optimiser leurs opérations de contenu, de produit, de communication et de support, avec des agents d'intelligence artificielle et des flux de travail entièrement automatisés.

### Mises à jour de rupture du SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011):
- [SDK Android 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [SDK Swift 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Supprime le fil d'actualité.
        - Cette opération supprime entièrement tous les éléments de l'interface utilisateur, les modèles de données et les actions associés au fil d'actualité.
- [SDK Web 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 9 décembre 2025

### Données & Rapports

#### Ajout du Google Tag Manager à une page de destination

Pour ajouter Google Tag Manager à vos pages de destination, ajoutez un bloc de code personnalisé à votre page de destination dans l'éditeur par glisser-déposer, puis [insérez le code Tag Manager]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) dans le bloc.

### Orchestration

#### Cas d'utilisation de SMS Liquid

Le cas d'utilisation [Répondre avec des messages différents en fonction du mot-clé du SMS entrant]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) intègre le traitement dynamique des mots-clés du SMS pour répondre à des messages entrants spécifiques avec un texte de message différent. Par exemple, vous pouvez envoyer des réponses différentes lorsque quelqu'un envoie un message "START" ou "JOIN".

#### Allowlisting pour le contenu connecté

Vous pouvez autoriser l'utilisation d'URL spécifiques pour le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call). Pour accéder à cette fonctionnalité, contactez votre gestionnaire de satisfaction client.

### Canaux & Points de contact

#### Codage des caractères du SMS

Notre [calculateur de segmentation des SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator) dispose désormais de l'encodage des caractères ! Sélectionnez **Afficher le codage des caractères** pour identifier les caractères qui sont codés en GSM-7 ou UCS-2. 

![Calculatrice de segment SMS avec un exemple de message SMS saisi dans la zone de texte et l'encodage des caractères activé.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Envois de messages WhatsApp avec optimisation

L'API MM pour WhatsApp n'offrant pas une livrabilité à 100 %, il est important de comprendre comment recibler les utilisateurs qui n'ont peut-être pas reçu votre message sur d'autres canaux. 

Pour recibler les utilisateurs, nous vous recommandons de créer un segment d'utilisateurs qui n'ont pas reçu un message spécifique. Pour ce faire, filtrez par le code d'erreur `131049`, qui indique qu'un message de modèle marketing n'a pas été envoyé en raison de l'application de la limite de modèles marketing par utilisateur de WhatsApp. Pour ce faire, vous pouvez [utiliser les Braze Currents ou les extensions de segments SQL]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Partenariats

#### OtherLevels - Contenu dynamique

[OtherLevels]({{site.baseurl}}/partners/otherlevels/) est une plateforme d'expérience qui utilise l'intelligence artificielle générative pour transformer la façon dont les marques de sport, les éditeurs et les opérateurs se connectent avec leurs clients en transformant le contenu traditionnel en expériences vidéo et rich media personnalisées à l'échelle de la marque.

### SDK

#### Mises à jour de rupture du SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## Novembre 11, 2025 :

### Flexibilité des données

#### `Live Activities Push to Start Registered for App` filtre de segmentation

Le filtre `Live Activities Push to Start Registered for App` segmente vos utilisateurs selon qu'ils sont ou non enregistrés pour démarrer une activité en direct via les notifications push iOS pour une app spécifique.

#### RFM SQL Extension de segments

Vous pouvez créer une [extension segmentation RFM (récence, fréquence, monétaire)]({{site.baseurl}}/rfm_segments/) pour cibler vos meilleurs utilisateurs en mesurant leurs habitudes d'achat.

L'analyse RFM est une technique marketing qui permet d'identifier vos meilleurs utilisateurs en les notant sur une échelle de 0 à 3 pour chaque catégorie (récurrence, fréquence, monétaire), 3 étant le meilleur score et 0 le plus mauvais. La récence, la fréquence et les valeurs monétaires sont toutes basées sur les données d'une période spécifique de votre choix.

#### Attributs personnalisés - Valeurs 

Lorsque vous consultez un rapport d'utilisation, sélectionnez l'[onglet**Valeurs**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) pour afficher les valeurs maximales des attributs personnalisés sélectionnés sur la base d'un échantillon d'environ 250 000 utilisateurs.

#### Synchronisation des journaux et observabilité pour l'ingestion de données dans le Cloud

{% multi_lang_include release_type.md release="General availability" %}

Le [tableau de bord]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) Cloud Data Ingestion (CDI) [Sync Log]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) vous permet de surveiller toutes les données traitées par CDI, de vérifier si les données ont été synchronisées avec succès et de diagnostiquer tout problème lié à des données "incorrectes" ou manquantes.

#### Déploiement de drapeaux à fonctionnalités multiples

Utilisez les [déploiements d'indicateurs de fonctionnalité à règles multiples]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) pour définir une séquence de règles d'évaluation des utilisateurs, ce qui permet une segmentation précise et des déploiements de fonctionnalité contrôlés. Cette méthode est idéale pour déployer la même fonctionnalité auprès de diverses audiences.

#### Mappage des champs du catalogue pour les blocs de produits glissés-déposés

Dans les paramètres de votre catalogue, vous pouvez basculer les **blocs de produits** [vers des champs]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) et des informations [spécifiques]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) de votre catalogue. Cela vous permet de sélectionner les champs à utiliser pour le titre du produit, l'URL du produit et l'URL de l'image.

#### Limitation de fréquence des avortements dans les courants

Lorsque vous utilisez Currents, vous pouvez désormais faire référence à `abort_type` dans les événements d'interruption de canal. Il indique qu'un message a été interrompu en raison d'une limitation de fréquence et précise la règle de limitation de fréquence à l'origine de l'interruption. Cela vous aidera à définir vos règles de limitation de fréquence. Reportez-vous aux [événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) pour plus de détails sur les événements Currents.

### Canaux robustes

#### Images de lignes d'arrière-plan 

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez [ajouter une image de ligne d'arrière-plan]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image) à un message in-app ou à une page de destination dans le panneau des **propriétés de la ligne**. Basculez sur **Image d'arrière-plan**, puis indiquez l'URL de l'image ou sélectionnez une image dans la [bibliothèque multimédia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). Enfin, configurez le texte alt, la taille, la position et la répétition éventuelle de l'image pour créer des motifs sur toute la ligne.

![Image d'arrière-plan d'une pizza avec un motif de répétition horizontal.]({% image_buster /assets/img_archive/background_row.png %})

#### Copier le lien de l’aperçu

Utilisez le **lien Copy preview** dans vos [bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), vos [pieds de page personnalisés pour les e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer) et vos [pages d'abonnement et de désabonnement]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers) pour générer un lien partageable qui montre à quoi ressemblera votre contenu pour un utilisateur aléatoire.

#### Messages WhatsApp avec réception/distribution optimisée

Utilisez les systèmes d'intelligence artificielle avancés de Meta pour diffuser vos messages marketing à un plus grand nombre d'utilisateurs qui sont les plus susceptibles de s'engager avec eux, en stimulant considérablement la livrabilité et l'engagement des messages.

Les [messages WhatsApp à réception/distribution optimisée]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) sont envoyés à l'aide de la nouvelle [API Marketing Messages Lite](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) de Meta, qui offre des performances supérieures à celles de l'API Cloud traditionnelle. Ce nouveau pipeline d'envoi vous permet de mieux atteindre les utilisateurs qui valorisent vos messages et souhaitent les recevoir.

#### Flux WhatsApp

Lorsque vous intégrez un message WhatsApp Flow dans un canvas ou une campagne de Braze, vous pouvez vouloir capturer et utiliser des informations spécifiques que les utilisateurs soumettent par le biais du Flow. Braze a besoin de recevoir des informations supplémentaires concernant la structure de la réponse de l'utilisateur, en particulier la forme attendue de la réponse JSON, pour générer le schéma d'attribut personnalisé imbriqué (NCA) requis.

Vous pouvez maintenant fournir à Braze les informations relatives à la structure de la réponse en [enregistrant la réponse au flux en tant qu'attribut personnalisé]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) et en effectuant un envoi test.

#### Aperçu modifiable de l'utilisateur

Vous pouvez [modifier des champs individuels d'un utilisateur aléatoire ou existant]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user) pour vous aider à tester le contenu dynamique de votre message. Sélectionnez **Modifier** pour convertir l'utilisateur sélectionné en un utilisateur personnalisé que vous pouvez modifier.

![L'onglet "Prévisualisation en tant qu'utilisateur" avec un bouton "Modifier".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### L'intelligence artificielle et l'automatisation de l’apprentissage machine.

#### BrazeAI Decisioning Studio™ Go

Vous pouvez maintenant configurer votre intégration avec [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go) en vous référant à ces articles de configuration pour :

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Nouvelles fonctionnalités pour les agents de Braze

{% multi_lang_include release_type.md release="Beta" %}

Vous pouvez désormais personnaliser votre [agent Braze]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) en :

- Appliquer les [lignes directrices de la marque]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) pour que votre agent y adhère dans sa réponse. 
- Faire référence à un catalogue pour personnaliser davantage votre message.
- Structurer les résultats d'un agent en fournissant le [format de sortie.]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format)
- Adjusting the [temperature]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) for the level of deviation for your agent's output.

### Modèles ChatGPT avec <sup>BrazeAITM</sup> Opérateur

{% multi_lang_include release_type.md release="Beta" %}

Vous pouvez sélectionner l'un de ces modèles GPT à utiliser pour différents types de demandes avec [Operator]({{site.baseurl}}/user_guide/brazeai/operator):

- GPT-5 Nano
- GPT-5 mini (par défaut)
- GPT-5

### Nouveaux partenariats Braze

#### StackAdapt - Publicité

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) est une plateforme de marketing alimentée par l'intelligence artificielle qui propose des publicités ciblées axées sur la performance. Il vous permet de synchroniser les données des profils utilisateurs de Braze dans le Data Hub de StackAdapt. En connectant les deux plateformes, vous pouvez créer une vue unifiée de vos clients et activer les données first-party pour améliorer les performances publicitaires.

#### Cloudinary - Contenu dynamique

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) est une plateforme d'images et de vidéos qui vous donne les moyens de gérer, modifier, optimiser et diffuser massivement des images et des vidéos dans le cadre de n'importe quelle campagne sur l'ensemble des canaux et des parcours clients. Une fois intégrée et activée, la gestion des médias de Cloudinary alimentera et fournira une réception/distribution dynamique, contextuelle et personnalisée des ressources pour vos campagnes et toiles Braze.

#### Kameleoon - Test A/B

[Kameleoon]({{site.baseurl}}/partners/kameleoon/) est une solution d'optimisation avec des fonctionnalités d'expérimentation, de personnalisation par l'intelligence artificielle et de gestion des fonctionnalités dans une seule plateforme unifiée.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Corrige le type Typescript pour le rappel de `subscribeToInAppMessage` et `addListener` pour `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Ces récepteurs renvoient désormais correctement un rappel avec le nouveau type `InAppMessageEvent`. Auparavant, les méthodes étaient annotées pour renvoyer un type `BrazeInAppMessage`, mais elles renvoyaient en fait un type `String`.
         - Si vous utilisez l'une ou l'autre API d'abonnement, assurez-vous que le comportement de vos messages in-app reste inchangé après la mise à jour vers cette version. Consultez notre exemple de code à l'adresse `BrazeProject.tsx`.
    - Les API `logInAppMessageClicked`, `logInAppMessageImpression` et `logInAppMessageButtonClicked` n'acceptent plus qu'un objet `BrazeInAppMessage` pour correspondre à son interface publique existante.
        - Auparavant, il acceptait à la fois un objet `BrazeInAppMessage` et un objet `String`.
    - `BrazeInAppMessage.toString()` renvoie désormais une chaîne de caractères lisible par l'homme au lieu de la représentation sous forme de chaîne JSON.
        - Pour obtenir la chaîne caractères JSON d'un message in-app, utilisez `BrazeInAppMessage.inAppMessageJsonString`.
    - Sur iOS, `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` a été déplacé vers `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - Cette nouvelle méthode est une méthode de classe au lieu d'une méthode d'instance.
    - Ajoute des annotations de nullité aux méthodes `BrazeReactUtils`.
    - Supprime de l'API les méthodes et propriétés dépréciées suivantes :
        - `getInstallTrackingId(callback:)` en faveur de `getDeviceId`.
        - `registerAndroidPushToken(token:)` en faveur de `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` en faveur de `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` en faveur de `payload_type`.
        - `PushNotificationEvent.deeplink` en faveur de `url`.
        - `PushNotificationEvent.content_text` en faveur de `body`.
        - `PushNotificationEvent.raw_android_push_data` en faveur de `android`.
        - `PushNotificationEvent.kvp_data` en faveur de `braze_properties`.
    - Mise à jour des liens de la version native du SDK [Android de Braze 39.0.0 à 40.0.2.](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [.NET MAUI (Xamarin) SDK Version 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Mise à jour de la liaison iOS du [SDK Swift de Braze 12.1.0 vers 13.3.0.](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) Cela inclut la prise en charge de Xcode 26.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Mise à jour du pont natif Android du SDK Android de Braze 39.0.0 vers 40.0.0.
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [SDK Web 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [SDK Android 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## Libération le 14 octobre 2025

### BrazeAI Decisioning Studio™

[BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) remplace les tests A/B par une prise de décision basée sur l'intelligence artificielle qui personnalise tout, et maximise n'importe quel indicateur : faites grimper les dollars, pas les clics. Avec BrazeAI Decisioning Studio™, vous pouvez optimiser n'importe quel indicateur clé de performance de l'entreprise. Consultez notre section dédiée [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) pour découvrir des exemples de cas d'utilisation et les principales fonctionnalités.

### Flexibilité des données

#### Nouveaux événements Currents

Ces nouveaux événements ont été ajoutés au [glossaire de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events):

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
- ``in_reply_to``message_id` 
  - `users.messages.whatsapp.InboundReceive`
- ``flow_id``message_id` 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Listes de suppression

{% multi_lang_include release_type.md release="General availability" %}

Les [listes de suppression]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) sont des groupes d'utilisateurs qui ne reçoivent automatiquement aucune campagne ou Canvas. Les listes de suppression sont définies par des critères de segmentation, et les utilisateurs entrent et sortent des listes de suppression lorsqu'ils répondent aux critères de segmentation.

#### Personnalisation sans copie

{% multi_lang_include release_type.md release="Early access" %}

Synchronisez les déclencheurs de Canvas à l'aide de l'ingestion de données dans le cloud pour une [personnalisation sans copie.]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/) Cette fonctionnalité permet d'accéder à des informations spécifiques à l'utilisateur à partir de votre solution de stockage de données et de les transmettre à un Canvas de destination. Les étapes du canvas peuvent éventuellement inclure des champs de personnalisation qui ne sont pas conservés dans les profils utilisateurs de Braze.

#### Canvas Variables de contexte pour les parcours d'audience et les étapes de l'arbre décisionnel

{% multi_lang_include release_type.md release="Early access" %}

Vous pouvez [créer des filtres de variables]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters) contextuelles qui utilisent des variables contextuelles préalablement déclarées dans les [parcours d'audience]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) et les étapes de l'arbre [décisionnel]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

### Libérer la créativité

#### Cartes d'offres pour les e-mails

Utilisez les [cartes d'offres]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab) pour fournir des informations clés sur les offres directement en haut du corps des e-mails. Cela permet aux destinataires de comprendre rapidement les détails de l'offre et de passer à l'action.

#### Modèles de bannières

Lorsque vous [composez votre bannière]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create), vous pouvez désormais commencer par un modèle vierge, utiliser un modèle de Braze ou sélectionner un modèle de bannière enregistré.

### Canaux robustes

#### Listes de suppression

{% multi_lang_include release_type.md release="General availability" %}
 
[Les listes de suppression]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/) spécifient les groupes d'utilisateurs qui ne recevront jamais de messages. Les administrateurs peuvent créer des listes de suppression avec des filtres de segmentation pour restreindre un groupe d'utilisateurs de la même manière que vous le feriez pour la segmentation.

#### LINE suivi des clics

{% multi_lang_include release_type.md release="General availability" %}

Lorsque le [suivi des clics LINE]({{site.baseurl}}/line/click_tracking/) est activé, Braze raccourcit automatiquement vos URL, ajoute des mécanismes de suivi et enregistre les clics en temps réel. Alors que LINE offre des données agrégées sur les clics, Braze fournit des informations granulaires sur les utilisateurs qui sont opportunes et exploitables. Ces données vous permettent de créer des stratégies de segmentation et de reciblage plus ciblées, par exemple en segmentant les utilisateurs en fonction de leur comportement au clic et en déclenchant des messages en réponse à des clics spécifiques.

#### Filtrage des clics des robots SMS et RCS

{% multi_lang_include release_type.md release="General availability" %}

Le [filtrage des clics de robots par SMS et RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) améliore l'analyse/analytique des campagnes et les flux de travail en excluant les clics de robots présumés. Un "bot click" désigne les clics automatisés sur des liens raccourcis dans les SMS et les messages RCS, tels que ceux provenant de robots d'exploration du web, d'aperçus de liens Android et iOS, ou de logiciels de sécurité CPaaS. Cette fonctionnalité facilite l'établissement de rapports précis, la segmentation et l'orchestration pour engager les utilisateurs réels.

#### Transférer des numéros de téléphone WhatsApp

Transférez un numéro de téléphone de WhatsApp Business Account (WABA) et son groupe d'abonnement associé [d'un espace de travail à un autre]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) dans Braze.

#### Messages d'envoi de messages et aperçu de WhatsApp Flows

Dans un canvas, vous pouvez créer une étape du message WhatsApp qui utilise un [message de réponse]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) et un message de flux. Vous pouvez également sélectionner **Prévisualiser** le flux pour prévisualiser le flux directement dans Braze et confirmer qu'il se comporte comme prévu.

#### Envois de produits par WhatsApp

Les messages produits vous permettent d'envoyer des messages WhatsApp interactifs qui présentent des produits directement à partir de votre catalogue Meta.

#### Intégration de Braze et de WhatsApp à un système externe

[Tirez parti de la puissance des chatbots d'intelligence artificielle et de la production/instantanée d'agents en ligne]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) sur le canal WhatsApp pour rationaliser vos opérations d'assistance à la clientèle. En automatisant les demandes de renseignements de routine et en passant de façon fluide/sansans homogène à des agents humains en cas de besoin, vous pouvez améliorer considérablement les temps de réponse et l'expérience client dans son ensemble.

### L'intelligence artificielle et l'automatisation de l’apprentissage machine.

#### Agents Braze

{% multi_lang_include release_type.md release="Beta" %}

Les [agents Braze]({{site.baseurl}}/user_guide/brazeai/agents/) sont des assistants dotés d'une intelligence artificielle que vous pouvez créer à l'intérieur de Braze. Les agents peuvent générer du contenu, prendre des décisions intelligentes et enrichir vos données afin que vous puissiez proposer des expériences client plus personnalisées.

### Nouveaux partenariats Braze

#### Jasper - Modèles

L'intégration de [Jasper]({{site.baseurl}}/partners/jasper/) avec Braze vous permet de rationaliser la création de contenu et l'exécution des campagnes. Avec Jasper, vos marketeurs peuvent générer en quelques minutes des textes de haute qualité et conformes à la marque. Braze facilite ensuite la réception/distribution de ces messages à la bonne audience au moment optimal. Cette intégration favorise des flux de travail fluides, réduit les efforts manuels et permet d'obtenir de meilleurs résultats en matière d'engagement.

#### Swym - Fidélisation et reciblage

[Swym]({{site.baseurl}}/partners/swym/) aide les marques d'e-commerce à capturer l'intention d'achat avec des listes de souhaits, enregistrer pour plus tard, registre de cadeaux, et des alertes de rupture de stock. Grâce à des données riches et basées sur les autorisations, vous pouvez élaborer des campagnes hyperciblées et proposer des expériences d'achat personnalisées qui stimulent l'engagement, augmentent les conversions et renforcent la fidélisation.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les mises à jour de rupture sont listées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux des modifications du SDK correspondant.

- [Cordova SDK 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Mise à jour du pont natif Android [du SDK Android de Braze 37.0.0 vers 39.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - La version minimale requise de GradlePluginKotlinVersion est maintenant 2.1.0.
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 12.0.0 vers 13.2.0.](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) Cela inclut la prise en charge de Xcode 26.
    - Suppression de la prise en charge du fil d'actualité. Les API suivantes ont été supprimées :
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Mise à jour des liens de la version native du SDK [Android de 37.0.0 à 39.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Suppression de la prise en charge du fil d'actualité. Les API suivantes ont été supprimées :
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
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 12.0.0 vers 13.2.0.](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed) Cela inclut la prise en charge de Xcode 26.

{% enddetails %}
{% details September 16, 2025 %}

## Libération le 16 septembre 2025

### Flexibilité des données

#### Plateforme de données Braze

La plateforme de données Braze est un ensemble complet et composable de capacités de données et d'intégrations de partenaires qui vous permet de créer des expériences personnalisées et percutantes tout au long du cycle de vie du client. Découvrez les trois tâches à accomplir en matière de données : 

- [Unification des données]({{site.baseurl}}/user_guide/data/unification)  :
- Activation des données
- [Distribution des données]({{site.baseurl}}/user_guide/data/distribution)  :

#### Propriétés personnalisées de la bannière

{% multi_lang_include release_type.md release="Early access" %}

Vous pouvez utiliser les propriétés personnalisées de votre campagne Banner pour récupérer des données clé-valeur via le SDK et modifier le comportement ou l'apparence de votre application. Pour en savoir plus, consultez les [propriétés des bannières personnalisées]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Authentification par jeton

{% multi_lang_include release_type.md release="General availability" %}

Lorsque vous utilisez le contenu connecté de Braze, vous pouvez constater que certaines API nécessitent un jeton au lieu d'un nom d'utilisateur et d'un mot de passe. Braze peut stocker des informations d'identification qui contiennent des [valeurs d'en-tête d'authentification par jeton]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication).

#### Codes de promotion

Vous pouvez enregistrer des codes de promotion dans le profil d'un utilisateur par le biais d'une étape de mise à jour de l'utilisateur. Pour plus d'informations, reportez-vous à la section [Enregistrer les codes de promotion dans les profils utilisateurs]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile).

### Libérer la créativité

#### Braze Pilot

[Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot) est une application disponible publiquement pour Android et iOS qui vous permet de lancer des messages depuis votre tableau de bord de Braze vers votre téléphone. Consultez la rubrique [Démarrer avec Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) pour découvrir comment télécharger l'application, initialiser la connexion à votre tableau de bord de Braze et terminer la configuration.

### Nouveaux partenariats Braze

#### Blings - Contenu visuel et interactif

[Blings]({{site.baseurl}}/partners/blings/) est une plateforme vidéo personnalisée de nouvelle génération qui vous permet de proposer des expériences vidéo en temps réel, interactives et axées sur les données sur l'ensemble des canaux, à grande échelle.

#### Intégration standard de Shopify avec un outil tiers.

Pour les boutiques en ligne Shopify, nous vous recommandons d'utiliser la méthode d'intégration standard de Braze pour prendre en charge les SDK de Braze sur votre site.

Cependant, nous comprenons que vous puissiez préférer utiliser un outil tiers, comme Google Tag Manager, c'est pourquoi nous avons élaboré un guide sur la façon dont vous pouvez le faire. Pour commencer, consultez [Shopify : Étiquettes de tiers]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Mise à jour du pont natif Android du SDK Android de Braze `36.0.0` vers `39.0.0`.
    - Met à jour le pont iOS natif de Braze Swift SDK `12.0.0` à `13.2.0`. Cela inclut la prise en charge de Xcode 26.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Met à jour les bindings du SDK Swift de Braze pour exiger les versions de la dénomination `13.0.0+` SemVer. Cela permet la compatibilité avec n'importe quelle version du SDK de Braze, de `13.0.0` jusqu'à, mais sans inclure, `14.0.0`.

{% enddetails %}
{% details August 19, 2025 %}

## Libération le 19 août 2025

### Normalisation de la cohérence des fuseaux horaires pour Canvas Context

{% multi_lang_include release_type.md release="Early access" %}

Si vous participez à l' [accès anticipé à l'étape du canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), tous les horodatages de type datetime provenant des propriétés des événements déclencheurs dans les canvas basés sur l'action seront toujours normalisés en [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Pour en savoir plus, consultez la rubrique [Normalisation de la cohérence des fuseaux horaires]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization).

### Flexibilité des données

#### Domaines personnalisés en libre-service

{% multi_lang_include release_type.md release="General access" %}

Les [domaines personnalisés en libre-service]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) vous permettent de configurer et de gérer vos propres domaines personnalisés pour SMS, RCS et WhatsApp, directement depuis votre tableau de bord Braze. Vous pouvez facilement ajouter, surveiller et gérer jusqu'à 10 domaines personnalisés en un seul endroit.

#### Statistiques sur les entonnoirs de segmentation

Sélectionnez [Afficher les statistiques de l'entonnoir]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) pour afficher les statistiques de ce groupe de filtres et voir l'impact de chaque filtre ajouté sur les statistiques de votre segmentation. Vous obtiendrez une estimation du nombre et du pourcentage d'utilisateurs ciblés par tous les filtres jusqu'à ce point. Une fois que les statistiques sont affichées pour un groupe de filtres, elles sont mises à jour automatiquement chaque fois que vous modifiez les filtres. 

#### Nouveaux champs de réponse pour l'endpoint `/campaigns/details` pour les notifications push

La réponse `messages` pour les notifications push comprend désormais deux nouveaux champs :

- `image_url` : Une URL d'image pour une image de notification Android, une image de notification iOS ou une image d'icône de push web.
- `large_image_url` : Une URL d'image de notification web pour les actions de push web Android Chrome et Windows.

#### Définition des champs d'informations nominatives

La sélection et la [définition de certains champs en tant que champs PII]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) affectent uniquement ce que les utilisateurs peuvent voir sur le tableau de bord de Braze et n'ont pas d'impact sur la façon dont les données de l'utilisateur final dans ces champs PII sont traitées.

Consultez votre équipe juridique pour aligner les paramètres de votre tableau de bord sur les réglementations et politiques de confidentialité applicables à votre entreprise, y compris celles relatives à la [conservation des données]({{site.baseurl}}/api/data_retention/).

#### Partager le lien de téléchargement d'un générateur de rapports

Vous pouvez [partager un lien]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) vers le [tableau de bord du]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) rapport en sélectionnant **Partager**, puis **Partager un lien** ou **Envoyer ou planifier un e-mail.**

### Libérer la créativité

#### Tags personnalisés pour les e-mails à glisser-déposer

Utilisez les étiquettes `<head>` pour ajouter des CSS et des métadonnées dans votre message e-mail. Par exemple, vous pouvez utiliser ces étiquettes pour ajouter une feuille de style ou un favicon. Liquid est pris en charge dans les étiquettes `<head>`.

### Canaux robustes

#### Meilleures pratiques floues

Nous avons ajouté une [section sur les meilleures pratiques]({{site.baseurl}}) pour vous aider à configurer de manière réfléchie votre message d'abonnement flou et à créer une expérience claire, conforme et positive pour vos abonnés.

#### Flux WhatsApp

{% multi_lang_include release_type.md release="Early access" %}

[WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) est une amélioration du canal WhatsApp existant, qui vous permet de créer des expériences d'envoi de messages interactives et dynamiques. 

#### WhatsApp : questions entrantes sur les produits

Les utilisateurs peuvent répondre au message de votre produit ou de votre catalogue en posant des [questions sur le produit]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions). Ceux-ci arrivent sous forme de messages entrants, qui peuvent ensuite être triés à l'aide d'un parcours d'action.

En outre, Braze extrait l'ID du produit et l'ID du catalogue de ces questions, de sorte que si vous souhaitez automatiser les réponses ou envoyer les questions à une autre équipe (comme le support client), vous pouvez inclure ces détails.

### L'intelligence artificielle et l'automatisation de l’apprentissage machine.

#### Nouveaux articles sur les cas d'utilisation de BrazeAI™

Nous avons ajouté de nouveaux articles sur les cas d'utilisation pour vous aider à tirer le meilleur parti de BrazeAI™. Ces guides mettent en lumière des moyens pratiques d'appliquer l'intelligence artificielle à vos stratégies d'engagement, notamment :

- Prédiction du taux d’attrition Identifiez les clients qui risquent de se désabonner et intervenez rapidement.
- Événements prévisionnels Anticipez les actions clés de l'utilisateur et façonnez l'expérience en temps réel.
- [Recommandations]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): Proposez des contenus et des produits plus pertinents en fonction du comportement des clients.

#### Serveur MCP

{% multi_lang_include release_type.md release="Beta" %}

Le [serveur MCP de Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server/), une connexion sécurisée et en lecture seule, permet aux outils d'intelligence artificielle comme Claude et Cursor d'accéder aux données Braze non PII pour répondre aux questions, analyser les tendances et fournir des informations sans modifier les données.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Swift 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Étend la fonctionnalité de `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` pour qu'elle soit déclenchée en cas d'erreur d'authentification "facultative".
        - La méthode de délégation `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` sera désormais déclenchée pour les erreurs d'authentification "Required" et "Optional".
        - Si vous souhaitez traiter uniquement les erreurs d'authentification "Required" du SDK, ajoutez un contrôle garantissant que `BrazeSDKAuthError.optional` est faux dans votre implémentation de cette méthode de délégué.
    - Corrige l'utilisation de `Braze.Configuration.sdkAuthentication` pour qu'elle prenne effet lorsqu'elle est activée.
        - Auparavant, la valeur de cette configuration n'était pas consommée par le SDK et le jeton était toujours attaché aux demandes s'il était présent.
        - Désormais, le SDK ne joindra le jeton d'authentification du SDK aux demandes réseau sortantes que si cette configuration est activée.
    - Les définisseurs de toutes les propriétés de `Braze.FeatureFlag` et de toutes les propriétés de `Braze.Banner` sont devenus `private`. Les propriétés de ces classes sont désormais en lecture seule.
    - Supprime la propriété `Braze.Banner.id`, qui était obsolète dans la version `11.4.0`.
        - Utilisez plutôt `Braze.Banner.trackingId` pour lire l'ID de suivi de campagne d'une bannière.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Met à jour les liaisons de la version native du SDK [Android de Braze 36.0.0 à 37.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Met à jour les liaisons de la version native du SDK [Swift de Braze de 12.0.0 à 13.0.0.](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
        - L'événement `sdkAuthenticationError` se déclenche désormais pour les erreurs d'authentification "obligatoire" et "facultative".
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Ajout de la prise en charge de .NET 9.0 pour les liaisons iOS et Android.
        - Cela supprime la prise en charge de .NET 8.0.
        - Cela nécessite une [version minimale d'iOS 12.2.](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0)
    - Mise à jour de la liaison Android de Braze [Android 32.0.0 à 37.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour de la liaison iOS du [SDK Swift de Braze 10.0.0 vers 12.1.0.](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Cette version contient des API pour la fonctionnalité Bannières, mais elle n'est pas encore entièrement prise en charge par ce SDK. Si vous souhaitez utiliser les bannières dans votre application .NET MAUI, contactez votre responsable du support client avant de procéder à l'intégration dans votre application.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Mise à jour de l'implémentation interne iOS de la méthode `enableSdk` pour utiliser `setEnabled`: au lieu de `_requestEnableSDKOnNextAppRun`, qui a été dépréciée dans le SDK Swift.
    - L'appel à cette méthode ne nécessite plus le redémarrage de l'application pour qu'elle prenne effet. Le SDK sera activé dès que cette méthode sera exécutée.
    - Mise à jour du pont natif Android du [SDK Android de Braze `36.0.0` vers `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

{% enddetails %}
{% details July 22, 2025 %}

## Libération le 22 juillet 2025

### Exportation d'événements de sécurité avec Amazon S3

Vous pouvez exporter automatiquement les événements de sécurité vers Amazon S3, un fournisseur de stockage en nuage, à l'aide d'une tâche quotidienne qui s'exécute à minuit UTC. Une fois configuré, vous n'avez plus besoin d'exporter manuellement les événements de sécurité à partir du tableau de bord.

### Flexibilité des données

#### Importation CSV

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez utiliser l'importation CSV pour enregistrer et mettre à jour les attributs des utilisateurs et les événements personnalisés dans Braze, comme `first_name`, `last_destination_searched`, et `trip_booked`. Pour commencer, consultez la section [Importation de fichiers CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### Alertes d'utilisation de l'API

{% multi_lang_include release_type.md release="General availability" %}

Les alertes d'utilisation de l'API offrent une visibilité essentielle sur l'utilisation de votre API, ce qui vous permet de détecter de manière proactive un trafic inattendu. En configurant ces alertes pour suivre les volumes de requêtes API clés, vous pouvez recevoir des notifications en temps réel et résoudre les problèmes avant qu'ils n'aient un impact sur vos campagnes marketing.

#### Limites de débit de l'API de l'espace de travail

Avec les limites de débit de l'API de l'espace de travail, vous pouvez définir un nombre maximum de demandes d'API qu'un espace de travail peut effectuer à un endpoint d'ingestion spécifique, tel que `/users/track` ou les données SDK. Vous pouvez également appliquer des limites de débit à un groupe d'espaces de travail, ce qui signifie que la limite est partagée par tous les espaces de travail de ce groupe.

#### Nouveaux événements Currents

Ces nouveaux événements ont été ajoutés au glossaire de Currents :

- [Bannière Événements d'abandon]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Bannière Cliquez sur les événements]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Evénements d'impression de la bannière]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [Bannière Evénements visualisés]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Événements d'échec de webhook]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### Période par défaut pour l'analyse/analytique de la campagne (si utilisée comme adjectif)

Par défaut, l'intervalle de temps pour [**Analyse/analyse de campagne (si elle est utilisée comme anjective)**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) affiche les 90 derniers jours à partir de l'heure actuelle. Cela signifie que si la campagne a été lancée il y a plus de 90 jours, l'analyse/analytique affichera "0" pour la période donnée. Pour afficher toutes les analyses/analytiques des campagnes plus anciennes, ajustez l'intervalle de temps des rapports.

#### Mise à jour du comportement à l'étape des chemins d'expérience Canvas

Si votre Canvas comporte une expérience active ou en cours et que vous mettez à jour le Canvas actif (même si ce n'est pas à l'étape des chemins chemins d'expérience), l'expérience en cours prendra fin. Pour redémarrer l'expérience, vous pouvez déconnecter le chemin d'expérience existant et en lancer un nouveau, ou dupliquer le Canvas et en lancer un nouveau. 

Pour plus d'informations, consultez [Modification d’un canvas après son lancement]({{site.baseurl}}/post-launch_edits/).

#### Limite de débit plus rapide disponible pour l'endpoint `/users/export/ids` 

Vous pouvez également augmenter la [limite de débit pour l'endpoint /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) à 40 requêtes par seconde en remplissant les conditions suivantes :

- La limite de débit par défaut (250 requêtes par minute) est activée dans votre espace de travail. Contactez votre gestionnaire de compte Braze pour obtenir de l'aide afin de supprimer toute limite de débit préexistante.
- Votre demande comprend le paramètre fields_to_export pour énumérer tous les champs que vous souhaitez recevoir.

#### Nouvelle traduction pour les endpoints des modèles d'e-mail

{% multi_lang_include release_type.md release="Early access" %}

Utilisez ces endpoints pour afficher et mettre à jour les traductions et les locales des modèles d'e-mail :

- [GET : Voir les traductions sources]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET : Afficher une traduction et une locale spécifiques pour l'endpoint du modèle d'e-mail
- [GET : Afficher toutes les traductions et locales d'un modèle d'e-mail
- [PUT : Mise à jour des traductions d'un modèle d'e-mail

### Libérer la créativité

#### Landing pages

Vous pouvez rendre votre page d'atterrissage [réactive à la taille de l'appareil de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) en empilant verticalement les colonnes sur les écrans plus petits. Pour ce faire, ajoutez une colonne dans la rangée que vous souhaitez rendre réactive, puis basculez sur **Empiler verticalement sur les petits écrans** dans la section **Personnaliser les colonnes.** 

### Canaux robustes

#### Filtrage des bots pour les e-mails

{% multi_lang_include release_type.md release="General availability" %}

Configurez le filtrage des robots dans vos [préférences d'e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) pour exclure tous les clics suspectés d'être des machines ou des robots. Un "bot click" dans un e-mail fait référence à un clic sur des hyperliens dans un e-mail qui est généré par un programme automatisé. En filtrant ces clics de robots, vous pouvez déclencher et envoyer intentionnellement des messages à des destinataires qui sont engagés.

#### Glisser-déposer des blocs de produits

{% multi_lang_include release_type.md release="Early access" %}

L'éditeur par glisser-déposer vous permet d'ajouter et de configurer rapidement des blocs de produits à vos messages pour une mise en valeur transparente des produits, sans qu'il soit nécessaire de créer un code Liquid personnalisé. La fonctionnalité de glisser-déposer des blocs de produits n'est actuellement disponible que pour les e-mails.

#### Span text pour les pages d'atterrissage et les messages in-app.

Span text vous permet d'appliquer un style personnalisé à des blocs de texte sans code personnalisé pour vos [pages d'atterrissage]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) et vos [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks). Pour ce faire, mettez en surbrillance le texte que vous souhaitez styliser, puis sélectionnez l'option **Enrouler avec l'empan pour le style**. 

#### Cliquez sur l'annonce pour WhatsApp

[Les publicités qui cliquent sur WhatsApp]({{site.baseurl}}/whatsapp_use_cases/) sont un moyen efficace d'apporter des clients nouveaux et existants à partir des publicités Meta sur Facebook, Instagram ou d'autres plateformes. Utilisez ces annonces pour promouvoir vos produits et services tout en sensibilisant les utilisateurs à votre présence sur WhatsApp. 

### Nouveaux partenariats Braze

#### Shopify Visitory API - eCommerce

Braze recueille des informations sur les visiteurs, telles que les adresses e-mail et les numéros de téléphone, par le biais de messages dans le navigateur. Ces informations sont ensuite envoyées à Shopify. Ces données aident les commerçants à reconnaître les visiteurs de leur magasin et à créer une expérience d'achat plus personnalisée.

#### Okendo - eCommerce

L'intégration entre Braze et [Okendo]({{site.baseurl}}/partners/okendo/) fonctionne sur plusieurs produits de la plateforme d'Okendo, notamment les avis, la fidélité, les recommandations, les enquêtes et les quiz. Okendo envoie des événements personnalisés et des attributs clients à Braze, qui peuvent être utilisés pour personnaliser et déclencher des messages.

#### Lemnisk - Plate-forme de données client

L'intégration de Braze et [Lemnisk]({{site.baseurl}}/partners/lemnisk/) permet aux marques et aux entreprises de libérer tout le potentiel de Braze en agissant comme une couche d'intelligence pilotée par la CDP qui unifie les données des utilisateurs à travers les plateformes en temps réel, et en envoyant les informations et les comportements de l'utilisateur collectés à Braze en temps réel.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [SDK Web 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Suppression de la propriété `Banner.html`, des méthodes `logBannerClick` et `logBannerImpressions`. Utilisez plutôt [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) qui gère automatiquement le suivi des impressions et des clics.
    - Suppression de la prise en charge de l'ancienne fonctionnalité de fil d'actualité. Cela inclut la suppression de la classe Feed et de ses méthodes associées.
    - Les champs created et categories qui étaient utilisés par les anciennes cartes de fil d'actualité ont été supprimés des [`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) des sous-classes.
    - Le champ linkText a également été supprimé de la sous-classe [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) Card et de son constructeur.
    - Clarification des définitions et mise à jour des types pour indiquer que certaines méthodes du SDK renvoient explicitement des données non définies lorsque le SDK n'est pas initialisé, ce qui permet d'aligner les typages sur le comportement réel en cours d'exécution. Cela pourrait introduire de nouvelles erreurs TypeScript dans les projets qui s'appuient sur les typages précédents (incomplets).
    - Les images des messages in-app avec `cropType` de `CENTER_CROP` (comme `FullScreenMessage` par défaut) sont maintenant rendues via une étiquette `<img>` au lieu de `<span>` pour une meilleure accessibilité. Cela risque d'interrompre les personnalisations CSS existantes pour la classe `.ab-center-cropped-img` ou ses enfants.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Mise à jour de l'implémentation interne iOS de la méthode `enableSdk` pour utiliser setEnabled : au lieu de `_requestEnableSDKOnNextAppRun`, qui a été dépréciée dans le SDK Swift.
        - L'appel à cette méthode ne nécessite plus le redémarrage de l'application pour qu'elle prenne effet. Le SDK sera activé dès que cette méthode sera exécutée.
    - Mise à jour du pont natif Android [du SDK Android de Braze 36.0.0 vers 37.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [SDK Android 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SDK Swift 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
{% details June 24, 2025 %}

## Publication le 24 juin 2025

### BrazeAI Decisioning Studio™

BrazeAI [Decisioning Studio](https://www.braze.com/product/brazeai-decisioning-studio/) ™ remplace les tests A/B par une prise de décision basée sur l'intelligence artificielle qui personnalise tout, et maximise n'importe quel indicateur : stimulez les dollars, pas les clics - avec BrazeAI Decisioning Studio™, vous pouvez optimiser n'importe quel indicateur clé de performance. Consultez notre section dédiée [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) pour découvrir des exemples de cas d'utilisation et les principales fonctionnalités.

### Nouveaux tutoriels SDK

Chaque didacticiel du SDK de Braze propose des instructions étape par étape ainsi que des exemples de code complets. Choisissez un tutoriel ci-dessous pour commencer :

- [Affichage de bannières]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Personnalisation du style des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [Affichage conditionnel des messages in-app]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [Report des messages in-app déclenchés]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### Flexibilité des données

#### Approvisionnement SAML juste-à-temps

{% multi_lang_include release_type.md release="General availability" %}

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

{% multi_lang_include release_type.md release="General availability" %}

Utilisez les [tests d'accessibilité]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) dans Inbox Vision pour mettre en évidence les problèmes d'accessibilité que peut présenter votre e-mail. 

Les tests d'accessibilité analysent le contenu de vos e-mails en fonction de certaines exigences des [Directives pour l'accessibilité des contenus web](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA. Cela peut fournir des informations sur les éléments qui ne respectent pas les normes d'accessibilité.

#### Suivi des clics pour WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez activer le [suivi des clics]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking) dans les messages de réponse et les messages modèles pour voir les données relatives aux clics dans vos rapports de performance WhatsApp et être en mesure de segmenter les utilisateurs en fonction de qui a cliqué sur quoi.

#### Vidéos pour WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez [intégrer des vidéos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features) dans le corps du texte pour les envois WhatsApp sortants. Ces fichiers doivent être hébergés par URL ou dans la [bibliothèque multimédia de Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library).

### Nouveaux partenariats Braze

#### Stripe - eCommerce

L'intégration Braze et [Stripe]({{site.baseurl}}/partners/stripe) vous permet de déclencher des messages dans Braze en fonction des événements Stripe, tels que le démarrage d'un essai, l'activation d'un abonnement, l'annulation d'un abonnement, et plus encore.

### Mises à jour SDK

Les mises à jour SDK suivantes ont été publiées. Les dernières mises à jour sont répertoriées ci-dessous ; vous pouvez trouver toutes les autres mises à jour en consultant les journaux de modifications SDK correspondants.

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - Mise à jour du pont natif Android [du SDK Android de Braze 35.0.0 vers 36.0.0.](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Mise à jour du pont natif iOS [du SDK Swift de Braze 11.6.1 vers 12.0.0.](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Segmentation de Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Mise à jour du SDK Android de Braze [de 35.0.0 à 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

{% enddetails %}
{% details May 27, 2025 %}

## Publication le 27 mai 2025

### Flexibilité des données

#### Copier des toiles dans différents espaces de travail

{% multi_lang_include release_type.md release="General availability" %}

Vous pouvez désormais copier des toiles dans différents espaces de travail. Cela vous permet de démarrer la composition de votre message en commençant par une copie d'un canvas dans un espace de travail différent. Pour plus d'informations sur ce qui est copié, reportez-vous à la section [Copier des campagnes et des toiles dans les espaces de travail]({{site.baseurl}}/copying_to_workspaces/).

#### Règles d'envoi de messages pour le flux de travail d'approbation 

{% multi_lang_include release_type.md release="General availability" %}

Utilisez des [règles d'envoi de messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules) dans votre flux de travail d'approbation pour limiter le nombre d'utilisateurs atteignables avant qu'une approbation supplémentaire ne soit requise. De cette façon, vous pouvez revoir vos campagnes et vos canevas avant de cibler un public plus large.

#### Diagrammes de relations entre entités pour Snowflake et Braze

En début d'année, nous avons créé des tables de relations d'entités pour les données partagées entre Snowflake et Braze. Ce mois-ci, nous avons ajouté de [nouveaux diagrammes interactifs]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/) dans lesquels vous pouvez effectuer des panoramiques, des saisies et des zooms sur les détails de chaque tableau, vous donnant ainsi une meilleure idée de la façon dont vos données interagissent avec Braze.

### Libérer la créativité

#### Événements recommandés

{% multi_lang_include release_type.md release="Early access" %}

Les [événements recommandés]({{site.baseurl}}/user_guide/data/custom_data/recommended_events) mappent les cas d'utilisation les plus courants du commerce électronique. En utilisant les événements personnalisés, vous pouvez débloquer des modèles de canvas pré-créés, des tableaux de bord de reporting qui mappent le cycle de vie du client, et plus encore.

### Canaux robustes

#### Canal des bannières

{% multi_lang_include release_type.md release="General availability" %}

Avec les [bannières]({{site.baseurl}}/user_guide/message_building_by_channel/banners), vous pouvez créer des envois de messages personnalisés pour vos utilisateurs, tout en étendant la portée de vos autres canaux, tels que l'e-mail ou les notifications push. Vous pouvez intégrer des bannières directement dans votre application ou votre site web, ce qui vous permet d'engager le dialogue avec les utilisateurs à travers une expérience qui semble naturelle.

#### Canal Rich Communication Services (RCS)

{% multi_lang_include release_type.md release="General availability" %}

Les [services de communication riches (RCS)]({{site.baseurl}}/about_rcs/) améliorent les SMS traditionnels en permettant aux marques d'envoyer des messages non seulement informatifs, mais aussi beaucoup plus attrayants. Désormais pris en charge sur Android et iOS, RCS apporte des fonctionnalités telles que des médias de haute qualité, des boutons interactifs et des profils d'expéditeur de marque directement dans les applications d'envoi de messages préinstallées des utilisateurs, éliminant ainsi le besoin de télécharger une application distincte.

#### Page des paramètres de poussée

{% multi_lang_include release_type.md release="General availability" %}

Utilisez la [page**Paramètres de push**]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings) pour configurer les paramètres clés de vos notifications push, notamment la durée en vie (TTL) de push et la priorité FCM par défaut pour les campagnes Android. Ces paramètres permettent d'optimiser la réception/distribution de vos notifications push et leur efficacité, garantissant ainsi une meilleure expérience à vos utilisateurs.

#### Codes de promotion pour les campagnes de messages in-app.

{% multi_lang_include release_type.md release="Early access" %}

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

{% multi_lang_include accessibility/feedback.md %}

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

{% enddetails %}
