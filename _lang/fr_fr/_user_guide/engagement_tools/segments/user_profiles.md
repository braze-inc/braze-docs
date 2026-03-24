---
nav_title: Profils utilisateur
article_title: Profils utilisateur
page_order: 9
page_type: reference
tool: 
  - Dashboard
description: "Cet article de référence décrit comment accéder à un profil utilisateur dans le tableau de bord, les cas d'utilisation des profils et ce que chacun d'eux contient."

---

# Profils utilisateur

> Les profils utilisateur constituent un excellent moyen de trouver des informations sur des utilisateurs spécifiques. Toutes les données persistantes associées à un utilisateur sont stockées dans son profil utilisateur.

## Accéder aux profils

Pour accéder au profil d'un utilisateur, rendez-vous sur la page **Recherche d'utilisateurs** et recherchez un utilisateur à l'aide de l'un des éléments suivants :

- ID utilisateur externe
- ID Braze
- E-mail
- Numéro de téléphone
- Jeton de notification push
- Alias d'utilisateur au format "[user_alias]:[alias_name]", tel que "amplitude_id:user_123"

Si une correspondance est trouvée, vous pouvez consulter les informations que vous avez enregistrées pour cet utilisateur avec le SDK Braze. Si votre recherche renvoie plusieurs profils utilisateur, vous pouvez fusionner chaque profil individuellement ou effectuer une fusion en bloc. Pour une présentation complète, consultez [Utilisateurs en double]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/).

{% alert important %}
Lorsqu'un numéro de téléphone est utilisé dans la recherche, il est converti au format [`E.164`](https://en.wikipedia.org/wiki/e.164). Les utilisateurs dont les numéros de téléphone ne peuvent pas être convertis au format `E.164` (par exemple, parce que le numéro de téléphone comporte un code pays ou un indicatif régional non valide) ne peuvent pas faire l'objet d'une recherche par numéro de téléphone.
{% endalert %}

![Résultats de la recherche avec une bannière indiquant "Plusieurs utilisateurs correspondent à vos critères de recherche" et deux boutons intitulés Précédent et Suivant.]({% image_buster /assets/img_archive/User_Search_Nonunique.png %}){: style="max-width:60%;"}

## Cas d'utilisation

Les profils utilisateur sont une excellente ressource pour la résolution des problèmes et les tests, car vous pouvez facilement accéder à des informations sur l'historique d'engagement d'un utilisateur, son appartenance à un segment, son appareil et son système d'exploitation.

Par exemple, si un utilisateur signale un problème et que vous ne savez pas quel appareil ni quel système d'exploitation il utilise, vous pouvez utiliser l'[onglet Aperçu](#overview-tab) pour trouver ces informations (à condition de disposer de son e-mail ou de son ID utilisateur). Vous pouvez également consulter la langue de l'utilisateur, ce qui peut s'avérer utile lors de la résolution des problèmes d'une [campagne multilingue]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages) qui ne s'est pas déroulée comme prévu.

Vous pouvez utiliser l'[onglet Engagement](#engagement-tab) pour vérifier si un utilisateur donné a bien reçu une campagne. Si c'est le cas, vous pouvez voir quand il l'a reçue. Vous pouvez également vérifier si un utilisateur fait partie d'un certain segment et s'il est abonné aux notifications push, aux e-mails, ou aux deux. Ces informations sont utiles pour la résolution des problèmes. Par exemple, vous devriez vérifier ces informations si un utilisateur n'a pas reçu une campagne qu'il devait recevoir, ou s'il reçoit une campagne qui ne lui était pas destinée.

## Éléments d'un profil utilisateur

Un profil utilisateur comporte quatre sections principales.

- **Aperçu :** Informations de base sur l'utilisateur, données de session, attributs personnalisés, événements personnalisés, achats et appareil le plus récent sur lequel l'utilisateur s'est connecté.
- **Engagement :** Informations sur les paramètres de contact de l'utilisateur, les campagnes reçues, les segments, les statistiques de communication, l'attribution d'installation et le numéro de compartiment aléatoire.
- **Historique d'envoi de messages :** Événements récents liés aux messages pour cet utilisateur au cours des 30 derniers jours.
- **Éligibilité aux indicateurs de fonctionnalité :** Vérifiez les indicateurs de fonctionnalité auxquels un utilisateur est actuellement éligible dans les déploiements, les étapes du canvas et les expériences.

### Onglet Aperçu {#overview-tab}

L'onglet **Aperçu** contient des informations de base sur un utilisateur et ses interactions avec votre application ou votre site web.

| Catégorie d'aperçu | Contient |
| --- | --- |
| Profil | Genre, groupe d'âge, emplacement, langue, localisation, fuseau horaire et date d'anniversaire. |
| Aperçu des sessions | Nombre de sessions, date de la première et de la dernière session, et applications utilisées. |
| Attributs personnalisés | Attributs personnalisés associés à cet utilisateur et leur valeur correspondante, y compris les attributs personnalisés imbriqués. |
| Appareils récents | Nombre d'appareils sur lesquels l'utilisateur s'est connecté, détails de chaque appareil et identifiants publicitaires associés (le cas échéant). |
| Événements personnalisés | Événements personnalisés effectués par cet utilisateur, nombre d'occurrences et date de la dernière occurrence de chaque événement. |
| Achats | Chiffre d'affaires à vie attribué à cet utilisateur, dernier achat, nombre total d'achats et liste de chacun de ces achats. |
{: .reset-td-br-1 .reset-td-br_2 role="presentation" }

Pour plus d'informations sur ces données, consultez [Collecte de données du SDK]({{site.baseurl}}/user_guide/data/unification/user_data/sdk_data_collection/).

![L'onglet Aperçu d'un profil utilisateur.]({% image_buster /assets/img_archive/user_profile2.png %})

### Onglet Engagement {#engagement-tab}

L'onglet **Engagement** contient des informations sur les interactions d'un utilisateur avec les messages que vous lui avez envoyés via Braze.

| Catégorie d'engagement | Contient |
| --- | --- |
| Paramètres de contact | Statut d'abonnement pour les e-mails, les SMS et les notifications push, ainsi que les groupes d'abonnement auxquels cet utilisateur est associé pour ces trois canaux. Cette section comprend également les informations du journal des modifications pour les jetons de notification push. Consultez les rubriques [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), [SMS]({{site.baseurl}}/sms_rcs_subscription_groups/) et [push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) pour plus d'informations sur la configuration des abonnements et des opt-ins. |
| Campagnes reçues | Les campagnes reçues sont marquées lorsque l'utilisateur reçoit la campagne, ou lorsque nous détectons pour la première fois des données d'interaction pour un utilisateur. Sélectionnez une campagne dans la liste pour l'afficher. |
| Segments | Segments dans lesquels cet utilisateur est inclus. Sélectionnez un segment dans la liste pour l'afficher. |
| Statistiques de communication | Date à laquelle cet utilisateur a reçu pour la dernière fois des messages de votre part pour chaque canal. |
| Attribution d'installation | Informations sur comment et quand un utilisateur a installé votre application. En savoir plus sur [les installations par les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Divers | Le [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) de l'utilisateur. |
| Messages Canvas reçus | Messages Canvas reçus par cet utilisateur et date de réception. Sélectionnez un message dans la liste pour l'afficher. |
| Prédictions | Les scores de [prédiction d'attrition]({{site.baseurl}}/user_guide/brazeai/predictive_churn/) et de [prédiction d'événements]({{site.baseurl}}/user_guide/brazeai/predictive_events/) pour cet utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![L'onglet Engagement d'un profil utilisateur affichant ses paramètres de contact et ses statistiques de communication.]({% image_buster /assets/img_archive/profiles_engagement_tab.png %})

### Onglet Historique d'envoi de messages

L'onglet **Historique des messages** du profil utilisateur affiche les événements récents liés aux messages (environ 40) pour un utilisateur individuel au cours des 30 derniers jours. Ces événements comprennent les messages que l'utilisateur a reçus, avec lesquels il a interagi, etc.

{% alert note %}
Les données de cet onglet ne sont pas mises à jour après la fusion d'un utilisateur. De plus, les événements associés à des messages envoyés via l'API (par exemple, l'[endpoint /messages/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/#creating-new-users-with-api-sends)) n'apparaîtront pas dans cet onglet si aucun ID de campagne n'est spécifié dans ces envois.
{% endalert %}

![L'onglet Historique des messages indiquant les campagnes et les Canvas qu'un utilisateur a reçus.]({% image_buster /assets/img_archive/profiles_messaging_history_tab.png %})

#### Afficher et comprendre les événements

Pour chaque événement du tableau **Historique des messages**, vous pouvez voir le canal de communication, le type d'événement, l'horodatage de l'événement, la campagne ou le message Canvas associé et les données de l'appareil de l'utilisateur. Pour filtrer des événements spécifiques, cliquez sur **Filtres** et sélectionnez des événements dans la liste.

##### Événements d'engagement lié aux messages

Les événements d'engagement lié aux messages suivants sont disponibles pour l'e-mail, les SMS, les notifications push, les messages in-app, les cartes de contenu et les webhooks. Pour en savoir plus sur le suivi d'événements spécifiques, consultez le [glossaire des événements d'engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/).

| Canal | Événements d'engagement disponibles |
| --- | --- |
| E-mail | Rebond<br>Clic<br>Événements de report<br>Réception<br>Marqué comme courrier indésirable<br>Ouverture (voir la [note sur l'événement d'ouverture d'e-mail](#note-on-email-open-event))<br>Envoi<br>Échec provisoire d'envoi<br>Désabonnement |
| SMS | Envoi par l'opérateur<br>Réception<br>Échec de réception<br>Entrant reçu<br>Rejet<br>Envoi |
| Notification push | Rebond<br>Ouverture influencée<br>Premier plan iOS<br>Ouverture<br>Envoi |
| Message in-app | Clic<br>Impression |
| Cartes de contenu | Clic<br>Rejet<br>Impression<br>Envoi |
| Webhooks | Envoi |
| WhatsApp | Abandon<br>Réception<br>Échec<br>Limite de fréquence atteinte<br>Entrant reçu<br>Lu<br>Envoi |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

##### Événements d'abandon de message

Les événements d'abandon de message se produisent lorsqu'un message envoyé à un utilisateur a été abandonné en raison d'une logique conditionnelle dans [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) ou dans le [contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages), ou en raison de délais d'attente de rendu Liquid.

Les événements d'abandon sont disponibles pour les canaux suivants :

- E-mail
- SMS
- Notification push
- Webhooks

Les événements d'abandon ne sont actuellement pas disponibles pour les messages in-app et les cartes de contenu.

##### Événements de limite de fréquence

Un événement de limite de fréquence se produit lorsqu'un utilisateur est qualifié pour recevoir un message, mais ne le reçoit pas en raison des paramètres de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Vous pouvez personnaliser les paramètres de limite de fréquence depuis **Paramètres** > **Règles de limite de fréquence**.

##### Destinations vides

Certains envois de messages peuvent apparaître dans l'historique des messages avec des destinations vides (indiquées par « — »). En effet, certains canaux, tels que les cartes de contenu et les webhooks, ne recueillent pas de données relatives à l'appareil lors de l'envoi du message.

Les envois de cartes de contenu sont enregistrés lorsque la carte est disponible pour consultation. Les cartes de contenu pouvant être consultées sur plusieurs appareils, les données relatives à l'appareil ne sont pas enregistrées lors de l'envoi. Ces informations sont plutôt enregistrées au moment de l'impression (lorsque la carte est effectivement consultée). Les webhooks sont envoyés à un endpoint système (et non à un appareil) ; les données relatives à l'appareil ne sont donc pas applicables.

#### Note sur l'événement d'ouverture d'e-mail {#note-on-email-open-event}

Le suivi de l'ouverture des e-mails est source d'erreurs, quel que soit l'outil utilisé, y compris Braze. Les différentes fonctionnalités de protection de la vie privée proposées par les clients de messagerie, qui bloquent le chargement automatique des images ou les chargent de manière proactive sur le serveur, rendent les événements d'ouverture des e-mails susceptibles de générer à la fois des faux positifs et des faux négatifs.

Si les statistiques d'ouverture des e-mails peuvent être utiles de manière agrégée, par exemple pour comparer l'efficacité de différentes lignes d'objet, vous ne devez pas considérer qu'un événement d'ouverture individuel pour un utilisateur donné est significatif.

#### Pourquoi certains champs sont-ils vides dans l'onglet Historique des messages ?

Certains champs peuvent être absents de l'onglet **Historique des messages** d'un utilisateur dans les cas suivants :

- Lorsqu'un événement ne contient pas de données pour **Message envoyé**, cela signifie que la campagne ne comporte pas de variations de messages.
- Lorsqu'un événement ne contient pas de données pour **Campagne/Canvas** et **Message envoyé**, cela indique que ce message a été envoyé à partir d'une campagne API (et non une campagne déclenchée par l'API) qui n'a pas spécifié les champs `campaign_id` et `message_variation_id`. Ces champs sont facultatifs et peuvent être omis dans le corps de la requête. Lorsqu'ils sont renseignés, ces informations apparaissent dans les journaux de l'historique des messages.
   - Si un message particulier ne figure pas dans l'historique des messages mais apparaît dans le journal des **Campagnes reçues**, il est probable que l'utilisateur ait reçu la campagne avant d'être identifié comme l'utilisateur actuel. Si un profil existant est orphelin, le journal des **Campagnes reçues** est transféré, mais pas l'historique des messages.
- Lorsque des données sont manquantes pour **Campagne/Canvas**, il se peut qu'un test manuel ait été envoyé. Les tests manuels sont enregistrés dans l'onglet **Historique des messages**, mais la campagne ou le canvas envoyé n'est pas enregistré.

## Articles connexes

- [Cycle de vie du profil utilisateur]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle/)
- [POST : Exporter le profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)
- [POST : Supprimer des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_delete/)