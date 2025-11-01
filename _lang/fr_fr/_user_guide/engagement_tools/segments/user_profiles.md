---
nav_title: Profils utilisateurs
article_title: Profils utilisateurs
page_order: 9
page_type: reference
tool: 
  - Dashboard
description: "Cet article de référence décrit comment accéder au profil d'un utilisateur dans le tableau de bord, les cas d'utilisation des profils et ce que chaque profil contient."

---

# Profils utilisateurs

> Les profils utilisateurs sont un excellent moyen de trouver des informations sur des utilisateurs spécifiques. Toutes les données persistantes associées à un utilisateur sont stockées dans son profil utilisateur.

## Profils d'accès

Pour accéder au profil d'un utilisateur, accédez à la page **Recherche d'utilisateurs** et recherchez un utilisateur à l'aide de l'un des éléments suivants :

- ID externe
- Braze ID
- e-mail
- Numéro de téléphone
- Jeton de poussée
- Alias d'utilisateur au format "[user_alias]:[alias_name]", tel que "amplitude_id:user_123"

Si une correspondance est trouvée, vous pouvez consulter les informations que vous avez enregistrées pour cet utilisateur avec le SDK de Braze. Sinon, si votre recherche d'utilisateurs renvoie plusieurs profils utilisateurs, vous pouvez fusionner chaque profil individuellement ou effectuer une fusion en bloc. Pour une présentation complète, consultez la section [Utilisateurs en double]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

Les résultats de la recherche sont accompagnés d'une bannière indiquant "Plusieurs utilisateurs correspondent à vos critères de recherche" et de deux boutons intitulés "Précédent" et "Suivant".]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Cas d'utilisation

Les profils utilisateurs sont une excellente ressource pour la résolution des problèmes et les essais, car vous pouvez facilement accéder à des informations sur l'historique d'engagement d'un utilisateur, son appartenance à un segment, son appareil et son système d'exploitation.

Par exemple, si un utilisateur signale un problème et que vous n'êtes pas sûr de l'appareil et du système d'exploitation qu'il utilise, vous pouvez utiliser l' [onglet Aperçu](#overview-tab) pour trouver ces informations (à condition d'avoir son e-mail ou son ID utilisateur). Vous pouvez également afficher la langue de l'utilisateur, ce qui peut s'avérer utile lors de la résolution des problèmes d'une [campagne multilingue]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) qui ne s'est pas déroulée comme prévu.

Vous pouvez utiliser l'[onglet Engagement](#engagement-tab) pour vérifier si un certain utilisateur a reçu une campagne. En outre, si l'utilisateur en question a bien reçu la campagne, vous pouvez savoir quand il l'a reçue. Vous pouvez également vérifier si un utilisateur fait partie d'un certain segment et s'il a opté pour le push, l'e-mail ou les deux. Ces informations sont utiles pour la résolution des problèmes. Par exemple, vous devez vérifier cette information si un utilisateur ne reçoit pas une campagne que vous attendiez qu'il reçoive ou reçoit une campagne que vous n'attendiez pas qu'il reçoive.

## Éléments du profil utilisateur

Le profil utilisateur se compose de quatre sections principales.

- **Aperçu :** Informations de base sur l'utilisateur, données de session, attributs personnalisés, événements personnalisés, achats et appareil le plus récent sur lequel l'utilisateur s'est connecté.
- **Engagement :** Informations sur les paramètres de contact de l'utilisateur, les campagnes reçues, les segments, les statistiques de communication, l'attribution d'installation et le numéro de compartiment aléatoire.
- **L'histoire de l'envoi des messages :** Événements récents liés à l'envoi de messages pour cet utilisateur au cours des 30 derniers jours.
- **Éligibilité des drapeaux de fonctionnalité :** Validez les drapeaux de fonctionnalité auxquels un utilisateur est actuellement éligible dans les déploiements, les étapes du canvas et les expériences Canvas. 

### Onglet Aperçu {#overview-tab}

L'onglet **Aperçu** contient des informations de base sur un utilisateur et ses interactions avec votre appli ou votre site web.

| Catégorie aperçu | Contient |
| --- | --- |
| Profil | Le sexe, la tranche d'âge, les emplacements, la langue, la localisation, le fuseau horaire et l'anniversaire. |
| Aperçu des sessions | Le nombre de séances, la date de la première et de la dernière séance et les applications utilisées. |
| Attributs personnalisés | Les attributs personnalisés attribués à cet utilisateur et leur valeur associée, y compris les attributs personnalisés imbriqués. |
| Appareils récents | Le nombre d'appareils sur lesquels ils se sont connectés, les détails de chaque appareil et les ID publicitaires qui leur sont associés (le cas échéant). |
| Événements personnalisés | Les événements personnalisés que cet utilisateur a réalisés, le nombre de fois et la date du dernier événement personnalisé. |
| Achats | Le chiffre d'affaires à vie attribué à cet utilisateur, son dernier achat, le nombre total d'achats et une liste de chaque achat. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Pour plus d'informations sur ces données, voir [Collecte des données utilisateur]({{site.baseurl}}/user_guide/data/user_data_collection/).

!L'onglet Aperçu d'un profil utilisateur.]({% image_buster /assets/img_archive/user_profile2.png %})

### Onglet Engagement {#engagement-tab}

L'onglet **Engagement** contient des informations sur les interactions d'un utilisateur avec les messages que vous lui avez envoyés à l'aide de Braze.

| Catégorie d'engagement | Contient |
| --- | --- |
| Paramètres de contact | Statut du groupe d'abonnement pour l'e-mail, le SMS et le push, et les groupes d'abonnement auxquels cet utilisateur est associé pour ces trois canaux. Cette section comprend également des informations sur le journal des modifications pour les jetons de poussée. Reportez-vous aux rubriques [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) et [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) pour plus d'informations sur les modalités d'abonnement et d'opt-in. |
| Campagnes reçues | Les campagnes reçues sont marquées lorsque l'utilisateur reçoit la campagne, ou lorsque nous détectons pour la première fois des données d'interaction pour un utilisateur. Sélectionnez une campagne dans la liste pour l'afficher. |
| Segmentations | Segments dans lesquels cet utilisateur est inclus. Sélectionnez un segment dans la liste pour le visualiser. |
| Statistiques sur la communication | Date à laquelle cet utilisateur a reçu pour la dernière fois des messages de votre part dans chaque canal. |
| Attribution d'installation | Informations sur la façon dont l'utilisateur a installé votre application et sur le moment où il l'a fait. En savoir plus sur [les installations d'utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Divers | Le [numéro de compartiment]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) aléatoire de l'utilisateur. |
| Envois de canvas reçus | Messages canvas que cet utilisateur a reçus et à quel moment. Sélectionnez un message dans la liste pour l'afficher. |
| Les prédictions | Les scores de [prédiction du taux d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) et de [prédiction des événements]({{site.baseurl}}/user_guide/brazeai/predictive_events/) pour cet utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

L'onglet Engagement du profil utilisateur affiche les paramètres de contact et les statistiques de communication.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Onglet Historique des messages

L'onglet **Historique des messages** du profil utilisateur montre les événements récents liés aux messages (environ 40) pour un utilisateur individuel au cours des 30 derniers jours. Ces événements comprennent les messages que l'utilisateur a envoyés, reçus, avec lesquels il a interagi, etc. Notez que les données de cet onglet ne sont pas mises à jour après la fusion d'un utilisateur.

{% alert note %}
Si vous avez des commentaires sur ce tableau ou si vous souhaitez voir des événements spécifiques, veuillez envoyer un e-mail à [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) avec comme ligne d'objet "Messaging History Tab Feedback".
{% endalert %}

L'onglet "Historique des messages" indique les campagnes de communication et les photos qu'un utilisateur a reçues.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Visualiser et comprendre les événements

Pour chaque événement du tableau **Historique des messages**, vous pouvez voir le canal de communication, le type d'événement, l'heure à laquelle l'événement s'est produit, la campagne ou le message Canvas associé et les données de l'appareil de l'utilisateur. Pour filtrer des événements spécifiques, cliquez sur **Filtres** et sélectionnez des événements dans la liste.

##### Événements d'engagement lié aux messages

Les événements d'engagement lié aux messages suivants sont disponibles pour les e-mails, les SMS, les push, les messages in-app, les cartes de contenu et les webhooks. Pour en savoir plus sur le suivi d'événements spécifiques, consultez le [glossaire des événements liés aux messages.]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/)

| Chaîne | Événements d'engagement disponibles |
| --- | --- |
| e-mail | Rebondir<br>Cliquez sur<br>Événements de report<br>Réception/distribution<br>Marquer comme spam<br>Ouvert (voir [note sur l'événement ouvert par e-mail)](#note-on-email-open-event)<br>Envoyer<br>Échappée provisoire d'envoi<br>Se désabonner |
| SMS | Envoi du transporteur<br>Réception/distribution<br>Défaut de réception/distribution<br>Réception de courrier entrant<br>Rejet<br>Envoyer |
| Pousser | Rebondir<br>Influencé ouvert<br>Avant-plan iOS<br>Ouvrir<br>Envoyer |
| Message in-app | Cliquez sur<br>Impression |
| Cartes de contenu | Cliquez sur<br>Rejeter<br>Impression<br>Envoyer |
| Webhooks | Envoyer |
| WhatsApp | Abandonner<br>Réception/distribution<br>Échec<br>Limite de fréquence<br>Réception de courrier entrant<br>Lire<br>Envoyer |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Événements d'interruption des messages

Les événements d'abandon de message se produisent lorsqu'un message envoyé à un utilisateur a été abandonné en raison d'une logique conditionnelle dans [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) ou dans le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages), ou en raison de délais d'attente de rendu de Liquid.

Les événements d'abandon sont disponibles pour les canaux suivants :

- e-mail
- SMS
- Pousser
- Webhooks

Les événements d'abandon ne sont actuellement pas disponibles pour les messages in-app et les cartes de contenu.

##### Fréquence limite de fréquence

Un événement de limitation de fréquence se produit lorsqu'un utilisateur est qualifié pour recevoir un message, mais ne le reçoit pas en raison des paramètres de [limitation de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Vous pouvez personnaliser les paramètres de limitation de fréquence à partir de **Paramètres** > **Règles de limitation de fréquence**.

##### Destinations vierges

Certains envois de messages peuvent apparaître dans l'historique des messages avec des destinations vides (indiquées par "-"). En effet, certains canaux, tels que les cartes de contenu et les webhooks, ne recueillent pas les données relatives à l'appareil lors de l'envoi du message.

Cartes de contenu Les envois sont enregistrés lorsque la carte peut être consultée. Les cartes de contenu pouvant être consultées sur plusieurs appareils, les données relatives à l'appareil ne sont pas enregistrées pour un envoi. Au lieu de cela, ces informations sont enregistrées au moment de l'impression (lorsque la carte est effectivement consultée). Les webhooks sont envoyés à un endpoint du système (et non à un appareil) ; les données relatives à l'appareil ne sont donc pas applicables.

#### Note sur l'événement ouvert par e-mail {#note-on-email-open-event}

Le suivi de l'ouverture des e-mails est source d'erreurs, quel que soit l'outil utilisé, y compris Braze. Grâce aux diverses fonctionnalités de protection de la vie privée offertes par les différents clients de messagerie qui bloquent le chargement automatique des images ou les chargent de manière proactive sur le serveur, les événements d'ouverture d'un e-mail sont susceptibles de donner lieu à des faux positifs et à des faux négatifs.

Si les statistiques d'ouverture des e-mails peuvent être utiles dans l'ensemble, par exemple pour comparer l'efficacité de différentes lignes d'objet, vous ne devez pas supposer qu'un événement d'ouverture individuel pour un utilisateur donné est significatif.

#### Pourquoi certains champs sont-ils vides dans l'onglet Historique des messages ?

Certains champs peuvent être absents de l'onglet **Historique des messages d'** un utilisateur dans les cas suivants :

- Lorsqu'un événement ne contient pas de données sur les **messages envoyés**, cela signifie que la campagne ne comporte pas de variations de messages.
- Lorsqu'un événement manque de données pour **Campagne/Canvas** et **Message envoyé**, cela indique que ce message a été envoyé à partir d'une campagne API (pas les campagnes déclenchées par l'API) qui n'a pas spécifié les adresses `campaign_id` et `message_variation_id`. Ces champs sont facultatifs et peuvent être omis dans le corps de la demande. Lorsque ces champs sont spécifiés, ces informations sont intégrées dans les journaux de l'historique des messages.
   - Si un message particulier ne figure pas dans l'historique des messages mais apparaît dans le journal des **campagnes reçues**, il est probable que l'utilisateur ait reçu la campagne avant d'être identifié comme l'utilisateur actuel. Si un profil existant est orphelin, le journal des **campagnes reçues** est transféré, mais pas l'historique des envois. 
- Lorsque des données sont manquantes pour **Campaign/Canvas**, il se peut qu'un test manuel ait été envoyé. Les tests manuels sont enregistrés dans l'onglet **Historique des messages**, mais la campagne ou le canvas envoyé n'est pas enregistré.


