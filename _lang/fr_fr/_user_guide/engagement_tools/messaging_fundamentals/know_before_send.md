---
nav_title: "Savoir avant d'envoyer"
article_title: "Savoir avant d'envoyer"
description: "Après avoir consulté notre guide de pré-lancement, reportez-vous à cette dernière liste de vérifications ou \" gotchas \" pour les cartes de contenu, les e-mails, les messages in-app, le push et les SMS."
alias: /know_before_send/
page_order: 10.2
tool:
    - Campaigns
    - Canvas
---

# Sachez avant d'envoyer : les canaux

Lancez vos campagnes et vos toiles en toute confiance ! Reportez-vous à cette dernière liste de vérifications ou "gotchas" pour les cartes de contenu, les e-mails, les messages in-app, le push et les SMS.

{% alert note %}
Bien que nous fournissions une liste exhaustive de ressources à consulter avant l'envoi, chaque canal présente des nuances individuelles qui ne cessent de croître au fur et à mesure que nous faisons évoluer nos produits. Les contrôles énumérés ci-dessous sont des suggestions utiles, et nous vous recommandons de tester minutieusement vos campagnes et vos envois importants avant de les envoyer.
{% endalert %}

## Général

#### Ce qu'il faut vérifier
- [**Limites de débit de l'API**](https://braze.com/resources/articles/whats-rate-limiting): Passez en revue les [limites de débit de]({{site.baseurl}}/api/api_limits/) l'API Braze pour vos espaces de travail afin d'éviter les erreurs. Si vous souhaitez augmenter vos limites de débit (et que vous mettez déjà des demandes en lot), contactez votre gestionnaire de satisfaction client. Gardez à l'esprit que ce processus nécessite un délai d'exécution, alors prévoyez-le en conséquence.
- [**Limites de fréquence nécessaires**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): Pour certaines campagnes, comme les messages transactionnels, vous voudrez toujours atteindre l'utilisateur, même si vous avez déjà atteint leur limite de fréquence (par exemple, une notification de réception/distribution). Si vous souhaitez qu'une campagne particulière ne tienne pas compte des règles de limitation de fréquence, vous pouvez le faire dans le tableau de bord de Braze lors de la planification de la réception/distribution de cette campagne en basculant la limitation de fréquence.

#### Ce qu'il faut savoir
- [**Groupe de contrôle global**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): Si vous utilisez un groupe de contrôle global, un pourcentage d'utilisateurs ne recevra aucune campagne ou Canvas. (Vous pouvez créer des exceptions avec des [paramètres d'exclusion]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)). Pour voir une liste de ces utilisateurs, exportez-les via CSV ou [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [**Limites de débit pour les toiles**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): Dans un Canvas, la limite de débit s'applique à l'ensemble du Canvas, et non aux étapes individuelles. Par exemple, si vous fixez une limite de débit de 10 000 messages par minute sur un Canvas comportant plusieurs étapes, il sera toujours limité à 10 000 messages car la limite aura été atteinte à la première étape.
- **Limitation de fréquence**: 
  - Les règles de limite de fréquence seront appliquées aux messages push, aux e-mails, aux SMS et aux webhooks, mais pas aux messages in-app et aux cartes de contenu.
  - La limite de fréquence globale est planifiée en fonction du fuseau horaire de l'utilisateur et est calculée par jours calendaires, et non par périodes de 24 heures. Par exemple, si vous avez mis en place une règle de limitation de fréquence prévoyant l'envoi d'une seule campagne par jour, un utilisateur peut recevoir un message à 23 heures dans son fuseau horaire local et être éligible pour recevoir un autre message une heure plus tard.

{% alert tip %}
Pour toute assistance supplémentaire concernant la résolution des problèmes liés à Canvas et aux campagnes, veillez à contacter le service d'assistance de Braze dans les 30 jours suivant l'apparition de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

## e-mail

#### Ce qu'il faut vérifier
- **Consentement du client**: Avant d'envoyer vos premiers e-mails, il est important d'obtenir l'autorisation de vos clients. Reportez-vous à la section [Consentement et collecte d'adresses]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/) et à notre [politique d'utilisation acceptable de Braze](https://www.braze.com/company/legal/aup) pour plus d'informations.
- **Volume prévu**: 2 millions d'e-mails par jour pour une seule IP est la recommandation générale, à condition que ce volume ait été [correctement réchauffé]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming). 
  - Si vous prévoyez d'envoyer régulièrement un volume supérieur, pour éviter que les fournisseurs ne limitent la réception des e-mails, ce qui entraînerait un grand nombre d'échecs provisoires d'envois, une baisse du taux de livrabilité et une diminution de la réputation de votre adresse IP, envisagez d'utiliser plusieurs adresses IP regroupées dans un pool d'adresses IP. 
  - Si vous souhaitez envoyer des messages dans un délai plus court, nous vous recommandons d'examiner la rapidité avec laquelle les différents fournisseurs acceptent le courrier afin d'évaluer le nombre approprié d'adresses IP à partir desquelles vous pouvez envoyer des messages. 

#### Ce qu'il faut savoir
- **Envoi de facteurs de volume**: Voici quelques facteurs qui déterminent les volumes d'envoi possibles pour un IP :
  - Boîtes aux lettres : Les grands fournisseurs d'e-mails peuvent probablement traiter des millions par jour à partir d'une seule IP, alors qu'un petit fournisseur régional de boîtes aux lettres ou un fournisseur disposant d'une infrastructure plus réduite ne sera peut-être pas en mesure de traiter une telle quantité.
  - Réputation de l'expéditeur : Vous pouvez envoyer un volume plus important par jour à partir d'une seule adresse IP si l'expéditeur est en mesure d'atteindre ce volume et si sa réputation d'expéditeur est suffisamment bonne pour chaque boîte aux lettres ou domaine auquel il envoie des messages.
- **Meilleures pratiques**: Consultez les [meilleures pratiques de Braze en matière d'e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) et contactez votre Braze Account Team si vous souhaitez en savoir plus sur les services de livrabilité.

## Pousser

#### Ce qu'il faut vérifier
- [**Abonné/optled-in et push enabled**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): Pour que les utilisateurs reçoivent un message push de Braze, il faut que leurs statuts d'abonnement soient soit opt-in (iOS), soit abonnés (Android) et `Push Enabled = True`. Notez qu'Android 13 introduit un changement majeur dans la manière dont les utilisateurs gèrent les apps qui envoient des notifications push. Le [guide de mise à jour du SDK Android 13 de]({{site.baseurl}}/developer_guide/platforms/android/android_13/) Braze continuera d'être mis à jour au fur et à mesure de la publication des nouvelles versions bêta d'Android 13.

#### Ce qu'il faut savoir
- **Web push**: Si vous avez [configuré le SDK Web de]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) Braze, envisagez d'utiliser le push Web pour impliquer les utilisateurs. Le Web push fonctionne de la même manière que les notifications push des applications sur votre téléphone. Pour plus d'informations sur la composition d'un push web, consultez la rubrique [Création d'une notification push.]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message)
- **Ciblage d'une application singulière**: Passez en revue les [différences de segmentation]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app) pour cibler une appli singulière et ses utilisateurs.

## SMS

#### Ce qu'il faut vérifier
- **Attributions et débit**: Comprenez quelles attributions de SMS sont actuellement rattachées à votre compte (code court, code long, etc.) et [quel débit cela vous procure]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) afin de confirmer que vous disposez d'un débit suffisant pour envoyer dans les délais souhaités.
- **Estimez le segmentation à partir de la copie du SMS :** Testez le texte de votre SMS à l'aide du [calculateur de segment d'un SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). Gardez à l'esprit que le nombre de segments de SMS doit être pris en compte en fonction de vos capacités de débit. (Audience * segments SMS = débit nécessaire). Reportez-vous à la FAQ SMS pour [éviter les dépassements]({{site.baseurl}}/sms_faq/).
- **Lois et réglementations relatives au SMS :** [Examinez les lois, les réglementations et la prévention des abus en matière de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) afin de confirmer que vous utilisez les services SMS conformément à toutes les lois applicables. Assurez-vous de demander l'avis de votre conseiller juridique avant de l'envoyer.

#### Ce qu'il faut savoir
- **Envoi de messages SMS par défaut**: Les messages SMS sont normalement envoyés par défaut à partir du code court figurant dans le pool d'expéditeurs.
- **ID alphanumérique de l'expéditeur**: Les messages bidirectionnels ne fonctionneront plus si vous utilisez un ID d'expéditeur alphanumérique ; ils sont désormais uniquement unidirectionnels.
- **Débit actualisé aux États-Unis**: Le débit a changé aux États-Unis avec l'[enregistrement A2P 10DLC](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Notez que nous ne nous engageons pas contractuellement sur des accords de niveau de service en matière de vitesse d'envoi en raison de multiples facteurs tels que la congestion du trafic et les problèmes liés aux transporteurs qui peuvent avoir un impact sur les taux de réception/distribution réels.
- **Groupe d'abonnement**: Pour lancer une campagne SMS via Braze, il faut sélectionner un groupe d'abonnement. En outre, afin de respecter la [conformité et les directives]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) internationales en matière [de télécommunications]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), Braze n'enverra jamais de SMS aux utilisateurs qui ne se sont pas [abonnés au groupe d'abonnement sélectionné]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group).

## WhatsApp

#### Ce qu'il faut savoir

- [**Meilleures pratiques**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/): Consultez nos suggestions de bonnes pratiques pour WhatsApp.

## Bannières

#### Ce qu'il faut vérifier
- **Dimensions de la bannière :** Créez vos bannières à l'aide d'un élément de dimension fixe et testez-les dans l'éditeur.
- **Priorité :** Si vous lancez plusieurs bannières, vous pouvez définir manuellement la priorité d'affichage de chaque bannière.

#### Ce qu'il faut savoir
- **Personnalisation liquide :** La personnalisation liquide s'actualise à chaque demande d'actualisation.
- **Placement et taux de bannière :** Chaque placement de bannière peut être utilisé dans un maximum de 10 campagnes dans un espace de travail.  
- **Clics et impressions :** Les clics et les impressions pour les bannières sont suivis automatiquement avec le SDK.
- **Limites :**  Actuellement, les fonctionnalités suivantes ne sont pas prises en charge : Intégration de Canvas, campagnes déclenchées par l'API et basées sur des actions, contenu connecté, codes de promotion, licenciements contrôlés par l'utilisateur et `catalog_items` à l'aide de l'[étiquette`:rerender` ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).
- **Test :** Pour afficher la bannière de test, l'appareil que vous utilisez doit pouvoir recevoir des notifications push au premier plan.
- **HTML personnalisé :** Exploitez le [pont JS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge) pour enregistrer les clics lorsque vous utilisez du HTML personnalisé pour définir les actions de clic, comme les liens et les boutons. Les actions de clic ne sont enregistrées automatiquement que lorsque vous utilisez les composants préconstruits dans l'éditeur par glisser-déposer.
- **Demande de placement :** Jusqu'à 10 placements peuvent être renvoyés au SDK en une seule demande d'actualisation. Chaque placement comprendra la bannière la plus prioritaire à laquelle l'utilisateur peut prétendre.

## Cartes de contenu

#### Ce qu'il faut vérifier
- **Taille de la carte de contenu**: Les champs des messages de la carte de contenu sont limités à 2 Ko en taille de précompression, calculée en additionnant la longueur en octets des champs suivants : titre, message, URL de l'image, texte du lien, URL du lien et paires clé-valeur. Les messages qui dépassent cette taille ne seront pas envoyés. Notez que cela n'inclut pas la taille de l'image mais plutôt la longueur de l'URL de l'image.
- **Mise à jour de la copie après l'envoi :** Après l'envoi d'une carte, vous ne pourrez pas mettre à jour la copie de cette même carte. Reportez-vous à la section [Mise à jour des cartes d'envoi]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards) pour comprendre comment vous pouvez aborder ce scénario.

#### Ce qu'il faut savoir
- **Limite des campagnes de cartes de contenu actives**: Vous pouvez avoir jusqu'à 500 campagnes cartes de contenu actives. Ce chiffre inclut les cartes de contenu envoyées avec l'une ou l'autre des options de [création de cartes]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/).  
- [**Conditions d'établissement des rapports**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): Passez en revue les termes tels que impressions totales, impressions uniques et destinataires uniques, car les définitions peuvent parfois prêter à confusion.
- **Carte de contenu actualisée**: Par défaut, Braze actualise les demandes de cartes de contenu au fur et à mesure qu'elles se synchronisent au début de la session, lors du balayage du flux vers le bas (mobile) et à l'ouverture de la vue des cartes si la dernière actualisation remonte à plus d'une minute.
- **Mise en cache des cartes de contenu**: Les options de mise en cache de la carte de contenu se trouvent dans nos documentations [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) et [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards). 
- **Limitation de fréquence**: La limite de fréquence ne s'applique pas aux cartes de contenu.
- **Impressions**: Les impressions sont généralement enregistrées lorsqu'une carte est vue. Par exemple, si vous avez une boîte de réception pleine de cartes de contenu, une impression ne sera pas enregistrée tant que l'utilisateur n'aura pas fait défiler la page jusqu'à la carte de contenu en question. Il existe des différences entre les plateformes Web, Android et iOS.  

## Messages in-app

#### Ce qu'il faut savoir
- **Déclenchement de messages in-app**: Au début de la session, le SDK demande que tous les messages in-app éligibles soient envoyés à l'appareil avec ses déclencheurs, de sorte que s'il effectue l'événement pendant la session, il puisse recevoir le message in-app rapidement et de manière fiable.
- **Envoyés ou impressions**: Pour les messages in-app, la notion d'"envoyé" diffère des autres canaux disponibles. Pour voir un message in-app, un utilisateur doit démarrer une session, faire partie de l'audience éligible et effectuer le déclencheur. C'est pourquoi nous suivons les "impressions", qui sont plus claires.
- **Déclenchement**: Par défaut, les messages in-app sont déclenchés par les événements enregistrés par le SDK. Si vous souhaitez déclencher des messages in-app par des événements envoyés par le serveur, vous pouvez également y parvenir grâce à ces guides pour [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift) et [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
- [Canvas messages in-app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options): Ces messages apparaissent la première fois que votre utilisateur ouvre l'application (déclenché par la session de démarrage) après que le message planifié dans le composant Canvas lui a été envoyé.
- **Appels au contenu connecté**: L'utilisation du contenu connecté vous permet d'envoyer du contenu dynamique dans les messages. Lorsque vous envoyez des messages via un canal comme les messages in-app, cela peut créer davantage de connexions simultanées avec les appareils de vos utilisateurs (les messages sont envoyés un par un plutôt que par lots). Pour gérer ce problème, nous vous recommandons de [limiter le débit de]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) vos messages.
