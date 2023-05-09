---
nav_title: À savoir avant l’envoi
article_title: À savoir avant l’envoi
description: "Après avoir consulté notre Guide de prélancement, consultez la liste finale des vérifications (les « pièges ») pour les cartes de contenu, les e-mails, les messages In-App, les notifications push et les SMS."
alias: /know_before_send/

---

# Être sûr avant d’envoyer : canaux

Lancez vos campagnes et Canvas en toute confiance ! Après avoir consulté notre [Guide de prélancement](https://labplaybooks.braze.com/canvas-playbooks#/subpage/b2rj8), consultez la liste finale des vérifications (les « pièges ») pour les cartes de contenu, les e-mails, les messages In-App, les notifications push et les SMS.

{% alert note %}
Même si nous fournissons une vaste liste de ressources pour aider les clients avant l’envoi, chaque canal possède des nuances individuelles qui continuent à croître tandis que nos produits évoluent. Les vérifications énumérées ci-dessous sont des suggestions utiles, et nous vous recommandons de tester minutieusement vos campagnes et vos gros envois avant de les envoyer. 
{% endalert %}

## Généralités

#### Choses à vérifier
- [**Limites de débit de l’API**](https://braze.com/resources/articles/whats-rate-limiting) : Vérifiez les [limites de taux]({{site.baseurl}}/api/api_limits/) de l’API Braze pour vos groupes d’apps pour éviter les erreurs. Si vous cherchez à augmenter vos limites de taux (et que vous faites déjà des requêtes en lots), contactez votre gestionnaire du succès des clients. Gardez à l’esprit que ce processus peut prendre un certain temps, alors prévoyez en conséquence.
- [**Écrasements nécessaires des limites de fréquence**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) : Il vaut mieux que certaines campagnes (de messages transactionnels par exemple) arrivent systématiquement chez l’utilisateur même si vous avez déjà sa limite de fréquence (par exemple, notification de livraison d’un produit). Si vous souhaitez qu’une campagne particulière ignore les règles de limite de fréquence, vous pouvez configurer cela dans le tableau de bord de Braze lors de la planification de la livraison de cette campagne en cliquant sur le bouton Frequency Cap.

#### Choses à savoir
- [**Groupes de contrôle mondiaux**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group) : Si vous utilisez un groupe de contrôle global, un pourcentage d’utilisateurs ne recevra aucune campagne ou Canvas. (vous pouvez créer des exceptions avec les [paramètres d’exclusion]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)). Si vous souhaitez voir une liste de ces utilisateurs, exportez-les via CSV ou [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [**Limites de débit Canvas**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting) : Dans un Canvas, la limite de taux s’applique à l’ensemble du Canvas et non pas aux étapes individuelles. Par exemple, si vous configurez une limite de 10 000 messages par minute sur un Canvas avec plusieurs étapes, il sera toujours limité à 10 000 messages, car la limite aura été atteinte à la première étape.
- **Limite de fréquence** : 
  - Les règles de limite de fréquence seront appliquées aux notifications push, aux e-mails, aux SMS et aux webhooks, mais pas aux messages in-app et cartes de contenu.
  - La limite de fréquence globale est planifiée en fonction du fuseau horaire de l’utilisateur et est calculée par jours calendaires et non pas par périodes de 24 heures. Par exemple, si vous configurez une règle de limite de fréquence pour qu’elle n’envoie pas plus d’une campagne par jour, un utilisateur peut recevoir un message à 23 h dans son fuseau horaire local et être éligible à recevoir un autre message une heure plus tard.

## E-mail

#### Choses à vérifier
- **Consentement du client** : Avant d’envoyer vos e-mails initiaux, il est important d’obtenir d’abord l’autorisation de vos clients. Consultez[Consentement et collecte d’adresses]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/consent_and_address_collection/) et la [Politique d’utilisation acceptable de Braze]({{site.baseurl}}/company/legal/aup) pour plus d’informations.
- **Volume anticipé** : 2 millions d’e-mails par jour pour une seule IP sont la recommandation générale, tant que ce volume a été [correctement réchauffé]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming). 
  - Si vous prévoyez d’envoyer régulièrement un volume plus élevé que cela, pour éviter que les fournisseurs limitent la réception de vos e-mails, ce qui générerait beaucoup de soft bounces, un taux de livraison réduit et une baisse de la réputation IP, envisagez d’utiliser plusieurs adresses IP groupées dans un pool IP. 
  - Si vous souhaitez envoyer uniquement dans un laps de temps plus court, nous vous recommandons de déterminer à quelle vitesse différents fournisseurs acceptent les e-mails pour établir le nombre approprié d’adresses IP émettrices. 

#### Choses à savoir
- **Facteurs de volume des envois** : Certains facteurs qui déterminent les volumes d’envoi d’une IP sont les suivants :
  - Boîtes de réception : Les grands fournisseurs mondiaux d’e-mails peuvent accepter des millions de personnes par jour à partir d’une seule IP, alors qu’un fournisseur de messagerie national avec une infrastructure plus modeste ne sera peut-être pas en mesure de gérer un tel volume.
  - Réputation de l’expéditeur : Vous pouvez envoyer un volume plus important par jour à partir d’une seule IP si l’émetteur est capable de gérer un tel volume et si sa réputation d’expéditeur est suffisamment forte dans chaque boîte de réception ou domaine qu’il envoie.
- **Meilleures pratiques** : Passez en revue les [meilleures pratiques pour l’e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) de Braze et contactez l’équipe de votre compte Braze si vous souhaitez en savoir plus sur nos services de délivrabilité.

## Notification push

#### Choses à vérifier
- [**Activé/abonné et push activé**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) : Pour que les utilisateurs reçoivent un message push de Braze, ils doivent avoir un statut d’abonnement « opted-in » (iOS), ou abonné (Android) et `Push Enabled = True`. Notez qu’Android 13 introduit une modification majeure dans la façon dont les utilisateurs gèrent les applications qui envoient des notifications push. Le [Guide de mise à niveau du SDK pour Android 13]({{site.baseurl}}/developer_guide/platform_integration_guides/android/android_13/) de Braze continuera d’être mis à jour quand de nouvelles versions bêta Android 13 sont publiées.

#### Choses à savoir
- **Web push** : Si vous avez le [SDK Configuration Web]({{site.baseurl}}/user_guide/message_building_by_channel/push/web) de Braze, envisagez le push Web pour engager vos utilisateurs. Les notifications push pour Web fonctionnent de la même façon que les notifications push de l’application sur votre téléphone. Pour plus d’informations sur la composition d’une notification push pour Web, consultez [Création d’une notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).
- **Cibler une seule application** : Passez en revue les [différences de segmentation]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app) pour cibler une application unique et ses utilisateurs.

## SMS

#### Choses à vérifier
- **Allocations et débit** : Comprendre les allocations SMS actuellement attachées à votre compte (code court, code long, etc.) [le débit qui vous fournit]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/short_and_long_codes/) pour vous assurer que vous avez assez de débit pour pouvoir envoyer aux moments où vous le souhaitez.
- **Estimation du segment à partir de la copie SMS** : Testez votre copie SMS dans la [Calculatrice de segments SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). Gardez à l’esprit que le nombre de segments SMS doit être pris en compte avec vos capacités de débit. (Public * Segments SMS = Débit nécessaire). Reportez-vous à la FAQ sur les SMS pour [éviter les excédents]({{site.baseurl}}/user_guide/message_building_by_channel/sms/faqs/#how-can-i-avoid-overages).
- **Lois et réglementations sur les SMS** : [Passez en revue les lois, réglementations et prévention des abus des SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/) pour vous assurer que vous utilisez les services SMS conformément à toutes les lois applicables. Demandez conseil à votre conseiller juridique avant d’envoyer.

#### Choses à savoir
- **Message SMS par défaut** : Les SMS sont normalement envoyés par défaut à partir du code court du pool de l’expéditeur.
- **ID d’expéditeur alphanumérique** : La messagerie bidirectionnelle ne fonctionnera plus si vous utilisez un ID d’expéditeur alphanumérique ; ces messages sont désormais unidirectionnels uniquement.
- **Mise à jour du débit aux États-Unis** : Le débit a changé aux États-Unis avec l’[homologation de A2P 10DLC](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) américaine. Veuillez noter que nous ne nous engageons pas contractuellement à respecter les SLA de vitesse d’envoi en raison de plusieurs facteurs tels que la congestion du trafic et les problèmes d’opérateur qui peuvent avoir un impact sur les taux réels de délivrabilité.
- **Groupe d’abonnement :** Pour lancer une campagne SMS via Braze, un groupe d’abonnement doit être sélectionné. De même, pour adhérer aux [normes et directives de conformité relatives aux télécommunications]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_laws_and_regulations/), Braze n’enverra jamais de SMS aux utilisateurs qui ne sont pas [inscrits au groupe d’abonnement sélectionné]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group).

## Cartes de contenu

#### Choses à vérifier
- **Taille des Cartes de contenu** : Les champs de message de carte de contenu sont limités à 2 Ko en taille précompression. Cette taille est calculée en additionnant la longueur en octets des champs suivants : titre, message, URL de l’image, texte de lien, URL de lien et paires valeur-clé. Les messages qui dépassent cette taille ne seront pas envoyés. Notez que cela n’inclut pas la taille de l’image, mais plutôt la longueur de l’URL de l’image.
- **Mise à jour de la copie après envoi** : Une fois qu’une carte est envoyée, vous ne pourrez pas modifier sa copie (c.-à-d. son texte). Au lieu de cela, vous devrez retirer la carte originale et envoyer une nouvelle carte actualisée.

#### Choses à savoir
- **Limite des campagnes de cartes de contenu actives** : Vous pouvez avoir jusqu’à 500 campagnes de cartes de contenu actives. Ce nombre comprend les cartes de contenu envoyées avec l’une ou l’autre option de [création de carte]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/).  
- [**Termes utilisés dans le reporting**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/) : Passez en revue les définitions des impressions totales, impressions uniques et destinataires uniques, car ces termes peuvent parfois prêter à confusion.
- **Actualisation des cartes de contenu** : Par défaut, Braze actualise les demandes de carte de contenu lorsqu’elles se synchronisent au démarrage de la session, quand l’utilisateur fait défiler le flux (mobile), et lorsque la vue des cartes est affichée si la dernière actualisation était il y a plus d’une minute.
- **Mise en cache des cartes de contenu** : Les options de mise en cache des cartes de contenu sont disponibles dans notre documentation [Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) et [Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards). 
- **Limite de fréquence** : Le plafonnement de fréquence ne s’applique pas aux cartes de contenu.
- **Impressions** : Les impressions sont généralement enregistrées une fois qu’une carte est vue. Par exemple, si vous avez une boîte de réception pleine de cartes de contenu, une impression ne sera pas enregistrée tant que l’utilisateur ne sera pas allé sur la carte de contenu spécifique. Il y a certaines nuances entre les plateformes Web, Android et iOS.  

## Messages in-app

#### Choses à savoir
- **Déclenchement personnalisé de messages in-app** : Au début de la session, le SDK demande que tous les messages in-app éligibles soient envoyés à l’appareil avec ses déclencheurs, donc si l’utilisateur effectue l’événement pendant la session, il peut recevoir le message in-app rapidement et de façon fiable. Les messages in-app ne peuvent pas être déclenchés par des événements personnalisés dans Canvas.
- **Envoyé vs Impressions** : Pour les messages in-app, le concept « envoyé » diffère des autres canaux disponibles. Pour afficher un message dans l’application, un utilisateur doit démarrer une session, être dans le public éligible et exécuter le déclencheur. Pour cette raison, nous suivons les « impressions », car c’est plus clair ainsi.
- **Déclenchement** : Par défaut, les messages in-app sont déclenchés par des événements enregistrés par le SDK. Si vous souhaitez déclencher des messages in-app par des événements envoyés par le serveur, vous pouvez également le faire en suivant ces guides pour [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#custom-in-app-message-triggering) et [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization).
- [**Messages in-app Canvas**]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options) : Ces messages s’afficheront la première fois que votre utilisateur ouvre l’application (déclenché par le démarrage de la session), une fois que le message planifié dans le composant Canvas lui a été envoyé.
