---
nav_title: Profils utilisateur
article_title: Profils utilisateur
page_order: 9
page_type: reference
tool: 
  - Dashboard
description: "Cet article de référence décrit comment accéder à un profil utilisateur dans le tableau de bord, des cas d’utilisation de profils et ce que chacun d’eux contient."

---

# Profils utilisateur

> Les profils d’utilisateurs sont un excellent moyen de trouver des informations sur des utilisateurs spécifiques. Toutes les données persistantes associées à un utilisateur sont stockées dans leur profil utilisateur.

## Accéder aux profils

Pour accéder au profil d'un utilisateur, accédez à la page **Recherche d'utilisateurs** et recherchez un utilisateur à l'aide de l'un des éléments suivants :

- ID utilisateur externe
- ID Braze
- E-mail
- Numéro de téléphone
- Jeton de notification push
- Alias d'utilisateur au format « [alias_utilisateur]:[nom_alias] », par exemple « amplitude_id:utilisateur_123 »

Si une correspondance est trouvée, vous pouvez consulter les informations que vous avez enregistrées pour cet utilisateur avec le SDK de Braze. Sinon, si votre recherche d'utilisateurs renvoie plusieurs profils utilisateurs, vous pouvez fusionner chaque profil individuellement ou effectuer une fusion en bloc. Pour accéder à une présentation complète, voir [Utilisateurs en double]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

![Les résultats de la recherche sont accompagnés d'une bannière indiquant "Plusieurs utilisateurs correspondent à vos critères de recherche" et de deux boutons intitulés Précédent et Suivant.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Cas d’utilisation

Les profils utilisateur sont une excellente option pour résoudre des problèmes ou effectuer des tests, car elle permet d’accéder facilement à des informations sur l’historique d’engagement d’un utilisateur, son appartenance à un segment, son appareil et son système d’exploitation.

Par exemple, si un utilisateur signale un problème et que vous n'êtes pas sûr de l'appareil et du système d'exploitation qu'il utilise, vous pouvez utiliser l' [onglet Aperçu](#overview-tab) pour trouver ces informations (à condition d'avoir son e-mail ou son ID utilisateur). Vous pouvez également afficher la langue de l'utilisateur, ce qui peut s'avérer utile lors de la résolution des problèmes d'une [campagne multilingue]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) qui ne s'est pas déroulée comme prévu.

Vous pouvez utiliser l'[onglet Engagement](#engagement-tab) pour vérifier si un certain utilisateur a reçu une campagne. De plus, si cet utilisateur a effectivement reçu la campagne, vous pouvez voir quand il l’a reçue. Vous pouvez également vérifier si un utilisateur fait partie d'un certain segment et s'il a opté pour le push, l'e-mail ou les deux. Ces informations sont utiles pour la résolution des problèmes. Par exemple, vous devez vérifier ces informations si un utilisateur n’a pas reçu une campagne qu’il devait recevoir ou s’il reçoit une campagne qui ne lui était pas destinée.

## Éléments d’un profil utilisateur

Un profil utilisateur a quatre sections principales.

- **Aperçu :** Informations globales au sujet de l’utilisateur, des données de session, des attributs personnalisés, des événements personnalisés, des achats et l’appareil le plus récent sur lequel s’est connecté l’utilisateur.
- **Engagement :** Informations concernant les paramètres de contact de l’utilisateur, ses campagnes reçues, segments, statistiques de communication, attribution d’installation et numéro de compartiment aléatoire.
- **Historique d’envoi de messages :** Événements liés aux communications récentes pour cet utilisateur sur les 30 derniers jours.
- **Éligibilité des drapeaux de fonctionnalité :** Validez les drapeaux de fonctionnalité auxquels un utilisateur est actuellement éligible dans les déploiements, les étapes du canvas et les expériences Canvas. 

### Onglet Overview {#overview-tab}

L'onglet **Aperçu** contient des informations de base sur un utilisateur et ses interactions avec votre appli ou votre site web.

| Catégorie d’aperçu | Contient |
| --- | --- |
| Profil | Genre, groupe d’âge, emplacement, langue, localisation, fuseau horaire et anniversaire. |
| Aperçu des sessions | Combien ont-ils eu de sessions, quand ont eu lieu les premières et les dernières et sur quelles applications. |
| Attributs personnalisés | Quels attributs personnalisés sont associés à cet utilisateur, leur valeur correspondante, y compris pour les attributs personnalisés imbriqués. |
| Appareils récents | Sur combien d’appareils ils se sont connectés, les détails de chaque appareil ainsi que leurs ID d’annonce associés (s’il y en a). |
| Événements personnalisés | Quels événements personnalisés ont été effectués par l’utilisateur, combien de fois, et quand ils ont effectué chaque événement pour la dernière fois. |
| Achats | Le revenu à vie attribué à cet utilisateur, son dernier achat, le nombre total d’achats ainsi qu’une liste de chacun de ces achats. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus d'informations sur ces données, voir [Collecte des données utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/).

![L'onglet Aperçu d'un profil utilisateur.]({% image_buster /assets/img_archive/user_profile2.png %})

### Onglet Engagement {#engagement-tab}

L'onglet **Engagement** contient des informations sur les interactions d'un utilisateur avec les messages que vous lui avez envoyés à l'aide de Braze.

| Catégorie d’engagement | Contient |
| --- | --- |
| Paramètres de contact | Statut d’abonnement pour les e-mails, les SMS et les notifications push, ainsi que les groupes d’abonnement auxquels cet utilisateur est associé pour ces trois canaux. Cette section comprend également les informations du journal des modifications pour les jetons de notification push. Reportez-vous aux rubriques [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) et [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) pour plus d'informations sur les modalités d'abonnement et d'opt-in. |
| Campagnes reçues | Les campagnes reçues sont marquées lorsque l'utilisateur reçoit la campagne, ou lorsque nous détectons pour la première fois des données d'interaction pour un utilisateur. Sélectionnez une campagne dans la liste pour l’afficher. |
| Segments | Segments dans lesquels est inclus cet utilisateur. Sélectionnez un segment dans la liste pour l’afficher. |
| Statistiques de communication | Quand cet utilisateur a reçu des messages de votre part depuis chaque canal pour la dernière fois. |
| Attribution d’installation | Informations concernant comment et quand un utilisateur a installé votre application. Apprenez-en plus sur [les installations par les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Divers | Le [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) de l'utilisateur. |
| Messages Canvas reçus | Messages Canvas reçus par l’utilisateur et quand il les a reçus. Sélectionnez un message dans la liste pour l’afficher. |
| Prédictions | Les scores de [prédiction du taux d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) et de [prédiction des événements]({{site.baseurl}}/user_guide/brazeai/predictive_events/) pour cet utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![L'onglet Engagement d'un profil utilisateur affiche les paramètres de contact et les statistiques de communication.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Onglet d’historique d’envoi de messages

L'onglet **Historique des messages** du profil utilisateur montre les événements récents liés aux messages (environ 40) pour un utilisateur individuel au cours des 30 derniers jours. Ces événements comprennent les messages que l’utilisateur a envoyés, reçus, avec lesquels il a interagi, etc. Notez que les données de cet onglet ne sont pas mises à jour après la fusion d'un utilisateur.

{% alert note %}
Si vous avez des commentaires sur ce tableau ou si vous souhaitez voir des événements spécifiques, veuillez envoyer un e-mail à [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) avec comme ligne d'objet "Messaging History Tab Feedback".
{% endalert %}

![L'onglet de l'historique des messages indique les campagnes et les photos qu'un utilisateur a reçues.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Afficher et comprendre les événements

Pour chaque événement du tableau **Historique des messages**, vous pouvez voir le canal de communication, le type d'événement, l'heure à laquelle l'événement s'est produit, la campagne ou le message Canvas associé et les données de l'appareil de l'utilisateur. Pour filtrer des événements spécifiques, cliquez sur **Filtres** et sélectionnez des événements dans la liste.

##### Événements d’engagement par message

Les événements d’engagement par message suivants sont disponibles pour l’e-mail, les SMS, le push, les messages in-app, les cartes de contenu et les webhooks. Pour en savoir plus sur le suivi d'événements spécifiques, consultez le [glossaire des événements d’engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

| Canal | Événements d’engagement disponibles |
| --- | --- |
| E-mail | Rebond<br>Clic<br>Réception<br>Marqué comme courrier indésirable<br>Ouvert (voir la [note sur l'événement d’ouverture d’e-mail](#note-on-email-open-event))<br>Envoyer<br>Échec provisoire de livraison<br>Se désabonner |
| SMS | Envoi par le transporteur<br>Réception<br>Échec de réception<br>Entrant reçu<br>Rejet<br>Envoyer |
| Notification push | Rebond<br>Ouverture influencée<br>Premier plan iOS<br>Ouvrir<br>Envoyer |
| Message in-app | Clic<br>Impression |
| Cartes de contenu | Clic<br>Rejeter<br>Impression<br>Envoyer |
| Webhooks | Envoyer |
| WhatsApp | Abandonner<br>Réception<br>Échec<br>Fréquence limitée<br>Entrant reçu<br>Lue<br>Envoyer |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Événements d’interruption de message

Les événements d'abandon de message se produisent lorsqu'un message envoyé à un utilisateur a été abandonné en raison d'une logique conditionnelle dans [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) ou dans le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages), ou en raison de délais d'attente de rendu de Liquid.

Les événements d’interruption sont disponibles pour les canaux suivants :

- E-mail
- SMS
- Notification push
- Webhooks

Les événements d’interruption ne sont pas disponibles actuellement pour les messages in-app et les cartes de contenu.

##### Événements de limite de fréquence

Un événement de limitation de fréquence se produit lorsqu'un utilisateur est qualifié pour recevoir un message, mais ne le reçoit pas en raison des paramètres de [limitation de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Vous pouvez personnaliser les paramètres de limitation de fréquence à partir de **Paramètres** > **Règles de limitation de fréquence**.

##### Destinations vides

Certains envois de messages peuvent apparaître dans l'historique des messages avec des destinations vides (indiquées par "-"). En effet, certains canaux, tels que les cartes de contenu et les webhooks, ne recueillent pas les données relatives à l'appareil lors de l'envoi du message.

Les envois de cartes de contenu sont enregistrés lorsque la carte peut être consultée. Les cartes de contenu pouvant être consultées sur plusieurs appareils, les données relatives à l'appareil ne sont pas enregistrées pour un envoi. Au lieu de cela, ces informations sont enregistrées au moment de l'impression (lorsque la carte est effectivement consultée). Les webhooks sont envoyés à un endpoint du système (et non à un appareil) ; les données relatives à l'appareil ne sont donc pas applicables.

#### Note sur l’événement e-mail ouvert{#note-on-email-open-event}

Le suivi de l'ouverture des e-mails est source d'erreurs, quel que soit l'outil utilisé, y compris Braze. Grâce à une variété de fonctions de protection de la vie privée offertes par différents clients de messagerie qui bloquent le chargement automatique des images ou les chargent de manière proactive sur le serveur, les événements d’ouverture des e-mails sont susceptibles d’entraîner à la fois des faux positifs et des faux négatifs.

Si les statistiques d'ouverture des e-mails peuvent être utiles dans l'ensemble, par exemple pour comparer l'efficacité de différentes lignes d'objet, vous ne devez pas supposer qu'un événement d'ouverture individuel pour un utilisateur donné est significatif.


