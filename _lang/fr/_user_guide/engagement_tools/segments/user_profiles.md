---
nav_title: Profils utilisateur
article_title: Profils utilisateur
page_order: 5
page_type: reference
tool:
  - Tableau de bord
description: "Cet article de référence explique accéder à un profil utilisateur dans le tableau de bord, les cas d’utilisation des profils et ce que chaque profil utilisateur contient."

---

# Profils utilisateur :

> Cet article de référence explique comment utiliser la fonction Profils Utilisateur de votre tableau de bord, décrit les différents composants impliqués dans un profil utilisateur et donne quelques exemples de la manière dont cette fonctionnalité peut être utilisée pour résoudre des problèmes liés aux campagnes.

Les profils d’utilisateurs sont un excellent moyen de trouver des informations sur des utilisateurs spécifiques. Toutes les données persistantes associées à un utilisateur sont stockées dans son profil utilisateur.

## Accéder aux profils

Pour accéder à un profil utilisateur, allez sur la page **User Search** et recherchez un utilisateur en utilisant un des critères suivants :

- ID utilisateur externe
- E-mail
- Numéro de téléphone
- Jeton de notification push

Si une correspondance est trouvée, vous pouvez voir les informations que vous avez enregistrées pour cet utilisateur avec le SDK Braze.

La plupart des recherches renvoient un seul profil utilisateur. Cependant, si vous recherchez une adresse e-mail associée à plus d’un utilisateur, tous les profils utilisateur correspondant à cet e-mail seront renvoyés. Si vous entrez une adresse e-mail non unique, cliquez sur **Next (Suivant)** pour afficher les autres profils associés à cet e-mail.

![Résultats de recherche avec une bannière disant « Plusieurs utilisateurs correspondent à vos critères de recherche » et deux boutons libellés Previous (Précédent) and Next (Suivant).][1]

## Cas d’utilisation

Les Profils Utilisateur sont une excellente ressource pour la résolution des problèmes ou pour effectuer des tests, car ils permettent d’accéder facilement à des informations sur l’historique d’engagement d’un utilisateur, son appartenance à un segment, son appareil et son système d’exploitation.

Par exemple, si un utilisateur signale un problème et que vous n’êtes pas sûr de l’appareil et du système d’exploitation qu’il utilise, vous pouvez utiliser l’onglet [Overview](#overview-tab) pour trouver ces informations (tant que vous connaissez son adresse e-mail ou son ID Utilisateur). Vous pouvez également afficher la langue d’un utilisateur, ce qui pourrait être utile pour la résolution des problèmes sur une [campagne multilingue][13] qui ne se comporte pas comme prévu.

Vous pouvez utiliser l’onglet [Engagement](#engagement-tab) pour vérifier si un utilisateur a bien reçu une campagne. De plus, si cet utilisateur a effectivement reçu la campagne, vous pouvez voir quand il l’a reçue. Vous pouvez également vérifier si un utilisateur se trouve dans un certain segment, et si un utilisateur s’est abonné aux notifications push, aux communications par e-mail ou les deux. Ces informations sont utiles pour la résolution des problèmes. Par exemple, vous devez vérifier ces informations si un utilisateur n’a pas reçu une campagne qu’il devait recevoir ou s’il reçoit une campagne qui ne lui était pas destinée.

## Éléments du profil utilisateur

Un profil utilisateur a quatre sections principales

- **Overview** Des informations de base sur l’utilisateur, ses sessions, ses attributs personnalisés, ses événements personnalisés, ses achats et sur l’appareil sur lequel il s’est connecté la dernière fois.
- **Engagement :** Informations sur les paramètres de contact de l’utilisateur, les campagnes qu’il a reçues, ses segments, ses statistiques de communication, l’attribution d’installation et le numéro de compartiment aléatoire.
- **Social :** Descriptif de haut niveau des activités de l’utilisateur sur Twitter et Facebook, si connecté.
- **Historique de l’envoi de messages :** Événements d’envoi de messages récents pour cet utilisateur dans les 30 derniers jours.

### Onglet Overview {#overview-tab}

L’onglet **Overview** contient des informations de base sur l’utilisateur et ses interactions avec votre appli ou site web.

| Catégorie Overview | Contient |
| --- | --- |
| Profil | Sexe, tranche d’âge, lieu, langue, paramètres régionaux, fuseaux horaires et anniversaire. |
| Overview des sessions | Combien de sessions pour l’utilisateur, date de sa première et de sa dernière session, et sur quelles applications. |
| Attributs personnalisés | Quels attributs personnalisés sont associés à cet utilisateur, leur valeur correspondante, y compris pour les attributs personnalisés imbriqués. |
| Appareils récents | Combien d’appareils l’utilisateur a utilisés, avec les détails de chaque appareil et les ID publicitaires associés (le cas échéant). |
| Événements personnalisés | Les événements personnalisés effectués par l’utilisateur, avec le nombre d’occurrences et la date à laquelle l’événement a été effectué pour la dernière fois. |
| Achats | Total des revenus associés à l’utilisateur, son dernier achat, le nombre total de ses achats avec une liste de chaque achat. |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d’informations sur ces données, consultez l’article [Collecte des données utilisateur][12].

![][2]

### Onglet Engagement {#engagement-tab}

L’onglet **Engagement** contient des informations sur les interactions d’un utilisateur avec les messages que vous lui avez envoyés à l’aide de Braze.

| Catégorie d’engagement | Contient |
| --- | --- |
| Paramètres de contact | Statut d’abonnement pour les e-mails, les SMS et les notifications push, et les groupes d’abonnement affectés à cet utilisateur pour ces trois canaux. Cette section contient également les informations du journal de modifications des jetons des notifications push. |
| Campagnes reçues | Campagnes que cet utilisateur a reçu et quand. Sélectionnez une campagne dans la liste pour l’afficher. |
| Segments | Segments dont fait partie cet utilisateur. Sélectionnez un segment dans la liste pour l’afficher. |
| Statistiques de communication | Quand cet utilisateur a reçu en dernier des messages de votre part via chaque canal. |
| Attribution d'installation | Informations sur comment et quand un utilisateur a installé votre app. En savoir plus sur [les installations par les utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Divers | Le [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/ab_testing_with_random_buckets/) de l’utilisateur. |
| Messages Canvas reçus | Messages Canvas que cet utilisateur a reçus et quand. Sélectionnez un message dans la liste pour l’afficher. |
| Prédictions | Scores [Churn Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn) et [Purchase Prediction]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases) pour cet utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

![][3]

### Onglet Social

L’onglet **Social** contient une vue de haut niveau de l’activité de l’utilisateur sur Twitter et Facebook, si ces plateformes sont reliées.

| Catégorie Social | Contient |
| --- | --- |
| Twitter | Nom d’utilisateur Twitter, nombre de followers, nombre d’utilisateurs que l’utilisateur suit, nombre de tweets. |
| Facebook | Publications Facebook que cet utilisateur a aimées. |
{: .reset-td-br-1 .reset-td-br-2}

![][4]

### Onglet Historique de l’envoi de messages

L’onglet **Message History (Historique d’envoi de messages)** du profil utilisateur affiche les événements récents liés à la messagerie (environ 40) pour un utilisateur individuel au cours des 30 derniers jours. Ces événements comprennent les messages que l’utilisateur a envoyés, reçus, avec lesquels il a interagi, etc.

{% alert note %}
Si vous avez un feedback sur cette table, ou si vous souhaitez voir des événements particuliers, veuillez envoyer un e-mail à [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) avec la ligne d’objet « Feedback Onglet Historique de l’envoi de messages ».
{% endalert %}

![][5]

#### Consulter et comprendre les événements

Pour chaque message dans la table **Historique des messages**, vous pouvez voir le canal d’envoi de messages, le type d’événement, le timestamp de la survenue de l’événement et la campagne ou e message Canvas correspondant. Pour filtrer selon des événements particuliers, cliquez sur **Filtres** et sélectionnez des événements dans la liste.

##### Événements d’engagement par message

Les événements d’engagement par message suivants sont disponibles pour l’e-mail, les SMS, le push, les messages in-app, les cartes de contenu et les webhooks. Pour en savoir plus sur la manière dont des événements particuliers sont suivis, voir le [glossaire sur les événements d’engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events).

| Canal | Événements d’engagement disponibles |
| --- | --- |
| E-mail | Rebond<br>Clic<br>Livraison<br>Marquer comme spam<br>Ouvrir (voir la [note sur l’événement e-mail ouvert](#note-on-email-open-event))<br>Envoyer<br>Rebond léger<br>Se désabonner |
| SMS | Envoi par l’intermédiaire<br>Livraison<br>Échec de livraison<br>Réception entrante<br>Rejet<br>Envoyer |
| Notification push | Rebond<br>Ouverture influencée<br>Avant-plan iOS<br>Ouvrir<br>Envoyer |
| Message in-app | Clic<br>Impression |
| cartes de contenu | Clic<br>Ignorer<br>Impression<br>Envoyer |
| Webhooks | Envoyer |
{: .reset-td-br-1 .reset-td-br-2}

##### Événements d’annulation de message

Les événements d’annulation de message arrivent lorsqu’un message envoyé à un utilisateur a été annulé en raison d’une logique conditionnelle dans [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) ou dans le [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages), ou de dépassements de délais pour le rendu Liquid.

Les événements d’annulation sont disponibles pour les canaux suivants :

- E-mail
- SMS
- Notification push
- Webhooks

Les événements d’annulation ne sont actuellement pas disponibles pour les messages in-app et les Cartes de contenu.

##### Événements de limite de fréquence

Un événement de limite de fréquence se produit lorsqu’un utilisateur a la qualité pour recevoir un message, mais ne l’a pas reçu en raison des paramètres de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Vous pouvez personnaliser les paramètres de limite de fréquence sur la page **Global Message Settings** de votre tableau de bord.

#### Note sur l’événement e-mail ouvert{#note-on-email-open-event}

Le suivi de l'ouverture d’e-mails est sujet à des erreurs, quel que soit l'outil utilisé, y compris Braze. Grâce à une variété de fonctions de protection de la vie privée offertes par différents clients de messagerie qui bloquent le chargement automatique des images ou les chargent de manière proactive sur le serveur, les événements d'ouverture des e-mails sont susceptibles d'entraîner à la fois des faux positifs et des faux négatifs.

Si les statistiques d'ouverture des e-mails peuvent être utiles dans leur ensemble, par exemple pour comparer l'efficacité de différentes lignes d'objet, vous ne devez pas supposer qu'un événement d'ouverture individuel pour un utilisateur individuel est significatif.


[1]: {% image_buster /assets/img_archive/User_Search_Nonunique.png %}
[2]: {% image_buster /assets/img_archive/user_profile2.png %}
[3]: {% image_buster /assets/img_archive/profiles_engagement_tab.png %}
[4]: {% image_buster /assets/img_archive/profiles_social_tab.png %}
[5]: {% image_buster /assets/img_archive/profiles_messaging_history_tab.png %}

[12]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[13]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
