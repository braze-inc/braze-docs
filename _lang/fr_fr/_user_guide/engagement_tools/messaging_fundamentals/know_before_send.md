---
nav_title: À savoir avant l’envoi
article_title: À savoir avant l’envoi
description: "Après avoir consulté notre Guide de prélancement, consultez la liste finale des vérifications (les « pièges ») pour les cartes de contenu, les e-mails, les messages in-app, les notifications push et les SMS."
alias: /know_before_send/
page_order: 10
tool:
    - Campaigns
    - Canvas
---

# Être sûr avant d’envoyer : canaux

Lancez vos campagnes et Canvas en toute confiance ! Reportez-vous à cette liste finale de vérifications ou de « pièges » pour les cartes de contenu, les e-mails, les messages intégrés, les notifications push et les SMS.

{% alert note %}
Bien que nous fournissions une liste exhaustive de ressources à consulter avant l'envoi, chaque canal a des nuances individuelles qui continuent de croître à mesure que nous faisons évoluer nos produits. Les vérifications énumérées ci-dessous sont des suggestions utiles, et nous vous recommandons de tester minutieusement vos campagnes et vos gros envois avant de les envoyer.
{% endalert %}

## Généralités

#### Choses à vérifier
- [**Limites de taux d'API**](https://braze.com/resources/articles/whats-rate-limiting): Examinez les [limites de taux]({{site.baseurl}}/api/api_limits/) de l'API Braze pour vos espaces de travail afin d'éviter les erreurs. Si vous cherchez à augmenter vos limites de taux (et que vous faites déjà des requêtes en lots), contactez votre gestionnaire du succès des clients. Gardez à l’esprit que ce processus peut prendre un certain temps, alors prévoyez en conséquence.
- [**Remplacements nécessaires de la limitation de fréquence**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): Il vaut mieux que certaines campagnes (de messages transactionnels par exemple) arrivent systématiquement chez l’utilisateur même si vous avez déjà sa limite de fréquence (par exemple, notification de livraison d’un produit). Si vous souhaitez qu’une campagne particulière ignore les règles de limite de fréquence, vous pouvez configurer cela dans le tableau de bord de Braze lors de la planification de la livraison de cette campagne en cliquant sur le bouton Frequency Cap.

#### Choses à savoir
- [**Groupes de contrôle globaux**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): Si vous utilisez un groupe de contrôle global, un pourcentage d'utilisateurs ne recevra aucune campagne ni aucun Canvas. (Vous pouvez créer des exceptions avec [paramètres d'exclusion]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)). Pour voir une liste de ces utilisateurs, exportez-les via CSV ou [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [**Limites de taux de Canvas**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): Dans un Canvas, la limite de taux s’applique à l’ensemble du Canvas et non pas aux étapes individuelles. Par exemple, si vous configurez une limite de 10 000 messages par minute sur un Canvas avec plusieurs étapes, il sera toujours limité à 10 000 messages, car la limite aura été atteinte à la première étape.
- **Plafonnement de la fréquence**: 
  - Les règles de limite de fréquence seront appliquées aux notifications push, aux e-mails, aux SMS et aux webhooks, mais pas aux messages in-app et cartes de contenu.
  - La limite de fréquence globale est planifiée en fonction du fuseau horaire de l’utilisateur et est calculée par jours calendaires et non pas par périodes de 24 heures. Par exemple, si vous configurez une règle de limite de fréquence pour qu’elle n’envoie pas plus d’une campagne par jour, un utilisateur peut recevoir un message à 23 h dans son fuseau horaire local et être éligible à recevoir un autre message une heure plus tard.

{% alert tip %}
Pour toute assistance supplémentaire avec Canvas et le dépannage des campagnes, assurez-vous de contacter le support Braze dans les 30 jours suivant la survenue de votre problème, car nous ne disposons que des 30 derniers jours de journaux de diagnostic.
{% endalert %}

## E-mail

#### Choses à vérifier
- **Consentement du client**: Avant d’envoyer vos e-mails initiaux, il est important d’obtenir d’abord l’autorisation de vos clients. Reportez-vous à [Consentement et collecte d'adresses]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/) et à notre [Politique d'utilisation acceptable de Braze](https://www.braze.com/company/legal/aup) pour plus d'informations.
- **Volume anticipé**: 2 millions d'e-mails par jour pour une seule IP est la recommandation générale tant que ce volume a été [correctement réchauffé]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming). 
  - Si vous prévoyez d’envoyer régulièrement un volume plus élevé que cela, pour éviter que les fournisseurs limitent la réception de vos e-mails, ce qui générerait beaucoup de soft bounces, un taux de livraison réduit et une baisse de la réputation IP, envisagez d’utiliser plusieurs adresses IP groupées dans un pool IP. 
  - Si vous souhaitez envoyer uniquement dans un laps de temps plus court, nous vous recommandons de déterminer à quelle vitesse différents fournisseurs acceptent les e-mails pour établir le nombre approprié d’adresses IP émettrices. 

#### Choses à savoir
- **Envoi des facteurs de volume**: Certains facteurs qui déterminent les volumes d’envoi d’une IP sont les suivants :
  - Boîtes de réception : Les grands fournisseurs mondiaux d’e-mails peuvent accepter des millions de personnes par jour à partir d’une seule IP, alors qu’un fournisseur de messagerie national avec une infrastructure plus modeste ne sera peut-être pas en mesure de gérer un tel volume.
  - Réputation de l’expéditeur : Vous pouvez envoyer un volume plus important par jour à partir d’une seule IP si l’émetteur est capable de gérer un tel volume et si sa réputation d’expéditeur est suffisamment forte dans chaque boîte de réception ou domaine qu’il envoie.
- **Meilleures pratiques**: Passez en revue les [meilleures pratiques de messagerie]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) de Braze et contactez votre équipe de compte Braze si vous souhaitez en savoir plus sur les services de délivrabilité.

## Notification push

#### Choses à vérifier
- [**Inscrit/abonné et notifications push activées**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): Pour que les utilisateurs reçoivent un message push de Braze, ils doivent avoir leur statut d'abonnement soit opté (iOS) soit abonné (Android) et `Push Enabled = True`. Notez qu’Android 13 introduit une modification majeure dans la façon dont les utilisateurs gèrent les applications qui envoient des notifications push. Le guide de mise à niveau du SDK [Android 13]({{site.baseurl}}/developer_guide/platforms/android/android_13/) de Braze continuera d'être mis à jour à mesure que de nouvelles versions bêta d'Android 13 seront publiées.

#### Choses à savoir
- **Notification push Web**: Si vous avez configuré le [SDK Web de Braze]({{site.baseurl}}/user_guide/message_building_by_channel/push/web), envisagez d'utiliser les notifications push Web pour engager les utilisateurs. Les notifications push pour Web fonctionnent de la même façon que les notifications push de l’application sur votre téléphone. Pour plus d'informations sur la composition d'une notification web, consultez [Créer une notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).
- **Ciblage d'une application unique**: Examinez les [différences de segmentation]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app) pour cibler une application unique et ses utilisateurs.

## SMS

#### Choses à vérifier
- **Attributions et débit**: Comprenez quelles sont les allocations de SMS actuellement attachées à votre compte (code court, code long et similaire) et [quelle quantité de débit cela vous fournit]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) pour confirmer que vous avez suffisamment de débit pour envoyer dans le délai souhaité.
- **Estimer le segment à partir de la copie SMS**: Testez votre copie SMS dans le [calculateur de segment SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). Gardez à l’esprit que le nombre de segments SMS doit être pris en compte avec vos capacités de débit. (Audience * segments SMS = Débit nécessaire). Consultez la FAQ SMS sur [éviter les dépassements]({{site.baseurl}}/sms_faq/).
- **Lois et règlements sur les SMS**: [Examiner les lois, réglementations et la prévention des abus en matière de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) pour confirmer que vous utilisez les services SMS en conformité avec toutes les lois applicables. Demandez conseil à votre conseiller juridique avant d’envoyer.

#### Choses à savoir
- **Message SMS par défaut**: Les SMS sont normalement envoyés par défaut à partir du code court du pool de l’expéditeur.
- **Identifiant d'expéditeur alphanumérique**: La messagerie bidirectionnelle ne fonctionnera plus si vous utilisez un ID d’expéditeur alphanumérique ; ces messages sont désormais unidirectionnels uniquement.
- **Mise à jour du débit aux États-Unis** Le débit a changé aux États-Unis avec l'enregistrement [A2P 10DLC](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Veuillez noter que nous ne nous engageons pas contractuellement à respecter les SLA de vitesse d’envoi en raison de plusieurs facteurs tels que la congestion du trafic et les problèmes d’opérateur qui peuvent avoir un impact sur les taux réels de livrabilité.
- **Groupe d'abonnement**: Pour lancer une campagne SMS via Braze, un groupe d’abonnement doit être sélectionné. De plus, pour se conformer aux [normes et directives internationales en matière de télécommunications]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), Braze n'enverra jamais de SMS aux utilisateurs qui ne se sont pas [abonnés au groupe d'abonnement sélectionné]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group).

## WhatsApp

#### Choses à savoir

- [**Meilleures pratiques**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/): Consultez nos meilleures pratiques suggérées pour WhatsApp.

## Bannières

#### Choses à vérifier
- **Dimensions de la bannière :** Créez vos bannières à l'aide d'un élément de dimension fixe et testez-les dans l'éditeur.
- **Priorité :** Si vous lancez plusieurs bannières, vous pouvez définir manuellement la priorité d'affichage de chaque bannière.

#### Choses à savoir
- **Personnalisation liquide :** La personnalisation liquide s'actualise à chaque début de session.
- **Placement et taux de bannière :** Chaque placement de bannière peut être utilisé dans un maximum de 10 campagnes dans un espace de travail.  
- **Clics et impressions :** Les clics et les impressions pour les bannières sont suivis automatiquement avec le SDK.
- **Limites :**  Actuellement, les fonctionnalités suivantes ne sont pas prises en charge : Intégration de Canvas, campagnes déclenchées par l'API et basées sur des actions, Currents, contenu connecté, codes de promotion, licenciements contrôlés par l'utilisateur et `catalog_items` à l'aide de l'[étiquette`:rerender` ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).
- **Test :** Pour afficher la bannière de test, l'appareil que vous utilisez doit pouvoir recevoir des notifications push au premier plan.
- **HTML personnalisé :** Exploitez le [pont JS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge) pour enregistrer les clics lorsque vous utilisez du HTML personnalisé pour définir les actions de clic, comme les liens et les boutons. Les actions de clic ne sont enregistrées automatiquement que lorsque vous utilisez les composants préconstruits dans l'éditeur par glisser-déposer.
- **Demande de placement :** Jusqu'à 10 placements peuvent être renvoyés au SDK par session. Chaque placement comprendra la bannière la plus prioritaire à laquelle l'utilisateur peut prétendre.

## Cartes de contenu

#### Choses à vérifier
- **Carte de contenu taille**: Les champs de message de la carte de contenu sont limités à 2 Ko en taille avant compression, calculée en ajoutant la longueur en octets des champs suivants : titre, message, URL de l'image, texte du lien, URL des liens et paires clé-valeur. Les messages qui dépassent cette taille ne seront pas envoyés. Notez que cela n’inclut pas la taille de l’image, mais plutôt la longueur de l’URL de l’image.
- **Mettre à jour la copie après l'envoi** Après l'envoi d'une carte, vous ne pourrez plus mettre à jour le texte de cette même carte. Reportez-vous à [Mettre à jour les cartes envoyées]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards) pour comprendre comment vous pouvez aborder ce scénario.

#### Choses à savoir
- **Limiter les campagnes de cartes de contenu actif**: Vous pouvez avoir jusqu’à 500 campagnes de cartes de contenu actives. Ce décompte inclut les cartes de contenu envoyées avec l'une ou l'autre des options de [création de carte]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/).  
- [**Termes de rapport**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): Passez en revue les définitions des impressions totales, impressions uniques et destinataires uniques, car ces termes peuvent parfois prêter à confusion.
- **Actualisation de la carte de contenu**: Par défaut, Braze actualise les demandes de cartes de contenu lorsqu'elles se synchronisent au démarrage de la session, lors du balayage vers le bas du flux (mobile) et lorsque la vue des cartes est ouverte si la dernière actualisation remonte à plus d'une minute.
- **Mettre en cache les cartes de contenu**: Les options de mise en cache des cartes de contenu se trouvent dans nos documents [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) et [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards). 
- **Plafonnement de la fréquence**: Le plafonnement de fréquence ne s’applique pas aux cartes de contenu.
- **Impressions**: Les impressions sont généralement enregistrées lorsqu'une carte est vue. Par exemple, si vous avez une boîte de réception pleine de cartes de contenu, une impression ne sera pas enregistrée tant que l’utilisateur ne sera pas allé sur la carte de contenu spécifique. Il y a certaines nuances entre les plateformes Web, Android et iOS.  

## in-app Messages

#### Choses à savoir
- **Déclenchement de message intégré à l'application**: Au début de la session, le SDK demande que tous les messages in-app éligibles soient envoyés à l’appareil avec ses déclencheurs, donc si l’utilisateur effectue l’événement pendant la session, il peut recevoir le message in-app rapidement et de façon fiable.
- **Envoyé contre impressions**: Pour les messages in-app, le concept « envoyé » diffère des autres canaux disponibles. Pour afficher un message dans l’application, un utilisateur doit démarrer une session, être dans l'audience éligible et exécuter le déclencheur. Pour cette raison, nous suivons les « impressions », car c’est plus clair ainsi.
- **Déclenchement**: Par défaut, les messages in-app sont déclenchés par des événements enregistrés par le SDK. Si vous souhaitez déclencher des messages intégrés à l'application par des événements envoyés par le serveur, vous pouvez également y parvenir grâce à ces guides pour [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift) et [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
- [Canvas messages in-app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options): Ces messages s’afficheront la première fois que votre utilisateur ouvre l’application (déclenché par le démarrage de la session), une fois que le message planifié dans le composant Canvas lui a été envoyé.
- **Appels au contenu connecté**: L'utilisation du contenu connecté vous permet d'envoyer du contenu dynamique dans les messages. Lorsque vous envoyez des messages via un canal comme les messages in-app, cela peut créer davantage de connexions simultanées avec les appareils de vos utilisateurs (les messages sont envoyés un par un plutôt que par lots). Pour gérer ce problème, nous vous recommandons de [limiter le débit de]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) vos messages.
