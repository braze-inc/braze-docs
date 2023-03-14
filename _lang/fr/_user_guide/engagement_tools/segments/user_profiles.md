---
nav_title: Profils utilisateur
article_title: Profils utilisateur
page_order: 5
page_type: reference
tool: 
  - Tableau de bord
description: "Cet article de référence décrit comment accéder à un profil utilisateur dans le tableau de bord, des cas d’utilisation de profils et ce que chacun d’eux contient."

---

# Profils utilisateur

> Cet article de référence décrit comment accéder aux profils utilisateur dans le tableau de bord, les différents composants impliqués dans un profil utilisateur et présente quelques exemples de la manière dont les profils utilisateur peuvent être utilisés pour résoudre des problèmes liés aux campagnes.

Les profils d’utilisateurs sont un excellent moyen de trouver des informations sur des utilisateurs spécifiques. Toutes les données persistantes associées à un utilisateur sont stockées dans leur profil utilisateur.

## Accéder aux profils

Pour accéder au profil utilisateur, rendez-vous sur la page **Profil utilisateur** et recherchez un utilisateur selon les données suivantes :

- ID utilisateur externe
- E-mail
- Numéro de téléphone
- Jeton de notification push

Si une correspondance est trouvée, vous pouvez afficher les informations que vous avez enregistrées pour cet utilisateur avec le SDK Braze.

La plupart des recherches renvoient un profil utilisateur. Cependant, si vous cherchez un e-mail qui appartient à plusieurs utilisateurs, tous les profils utilisateur qui correspondent à cet e-mail seront renvoyés. Si vous saisissez une adresse e-mail non unique, cliquez sur **Next (Suivant)** pour afficher les autres profils associés à cette adresse e-mail.

![Résultats de recherche avec une bannière disant « Plusieurs utilisateurs correspondent à vos critères de recherche » et deux boutons libellés Previous (Précédent) et Next (Suivant).][1]

## Cas d’utilisation

Les profils utilisateur sont une excellente option pour résoudre des problèmes ou effectuer des tests, car elle permet d’accéder facilement à des informations sur l’historique d’engagement d’un utilisateur, son appartenance à un segment, son appareil et son système d’exploitation.

Par exemple, si un utilisateur signale un problème et que vous n’êtes pas sûr de l’appareil et du système d’exploitation qu’il utilise, vous pouvez utiliser l’onglet [Aperçu](#overview-tab) pour trouver ces informations (tant que vous connaissez leur adresse e-mail ou leur ID utilisateur). Vous pouvez également afficher la langue d’un utilisateur, ce qui pourrait être utile pour la résolution des problèmes sur une [campagne multilingue][13] qui ne se comporte pas comme prévu.

Vous pouvez utiliser l’onglet [Engagement](#engagement-tab) pour vérifier si un utilisateur a bien reçu une campagne. De plus, si cet utilisateur a effectivement reçu la campagne, vous pouvez voir quand il l’a reçue. Vous pouvez également vérifier si un utilisateur se trouve dans un certain segment, et si un utilisateur s’est abonné aux notifications push, aux communications par e-mail ou les deux. Ces informations sont utiles pour la résolution des problèmes. Par exemple, vous devez vérifier ces informations si un utilisateur n’a pas reçu une campagne qu’il devait recevoir ou s’il reçoit une campagne qui ne lui était pas destinée.

## Éléments d’un profil utilisateur

Un profil utilisateur a quatre sections principales.

- **Overview :** Informations globales au sujet de l’utilisateur, des données de session, des attributs personnalisés, des événements personnalisés, des achats et l’appareil le plus récent sur lequel s’est connecté l’utilisateur.
- **Engagement :** Informations concernant les paramètres de contact de l’utilisateur, ses campagnes reçues, segments, statistiques de communication, attribution d’installation et numéro de compartiment aléatoire.
- **Social :** Affichage de haut niveau de l’activité de l’utilisateur sur Twitter et Facebook s’il est connecté.
- **Historique d’envoi de messages :** Événements liés aux communications récentes pour cet utilisateur sur les 30 derniers jours.

### Onglet Overview {#overview-tab}

L’onglet **Overview** comprend les informations de base d’un utilisateur et ses interactions avec votre application ou votre site Internet.

| Catégorie d’aperçu | Contient |
| --- | --- |
| Profil | Genre, groupe d’âge, emplacement, langue, localisation, fuseau horaire et anniversaire. |
| Aperçu des sessions | Combien ont-ils eu de sessions, quand ont eu lieu les premières et les dernières et sur quelles applications. |
| Attributs personnalisés | Quels attributs personnalisés sont associés à cet utilisateur, leur valeur correspondante, y compris pour les attributs personnalisés imbriqués. |
| Appareils récents | Sur combien d’appareils ils se sont connectés, les détails de chaque appareil ainsi que leurs ID d’annonce associés (s’il y en a). |
| Événements personnalisés | Quels événements personnalisés ont été effectués par l’utilisateur, combien de fois, et quand ils ont effectué chaque événement pour la dernière fois. |
| Achats | Le revenu à vie attribué à cet utilisateur, son dernier achat, le nombre total d’achats ainsi qu’une liste de chacun de ces achats. |
{: .reset-td-br-1 .reset-td-br-2}

Pour plus d’informations sur ces données, consultez l’article [Collecte des données utilisateur][12].

![][2]

### Onglet Engagement {#engagement-tab}

L’onglet **Engagement** contient des informations sur les interactions d’un utilisateur avec les messages que vous lui envoyez en utilisant Braze.

| Catégorie d’engagement | Contient |
| --- | --- |
| Paramètres de contact | Statut d’abonnement pour les e-mails, les SMS et les notifications push, ainsi que les groupes d’abonnement auxquels cet utilisateur est associé pour ces trois canaux. Cette section comprend également les informations du journal de modifications pour les jetons de notification push. Reportez-vous à l’[e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/), au [SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/), et la [notification push]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/) pour obtenir des informations sur la façon dont les abonnements et les abonnements sont définis. |
| Campagnes reçues | Campagnes reçues par cet utilisateur et quand il les a reçues. Sélectionnez une campagne dans la liste pour l’afficher. |
| Segments | Segments dans lesquels est inclus cet utilisateur. Sélectionnez un segment dans la liste pour l’afficher. |
| Statistiques de communication | Quand cet utilisateur a reçu des messages de votre part depuis chaque canal pour la dernière fois. |
| Attribution d’installation | Informations concernant comment et quand un utilisateur a installé votre application. Apprenez-en plus pour [comprendre les installations utilisateurs]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/install_attribution/). |
| Divers | Le [numéro de compartiment aléatoire]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/ab_testing_with_random_buckets/) de l’utilisateur. |
| Messages Canvas reçus | Messages Canvas reçus par l’utilisateur et quand il les a reçus. Sélectionnez un message dans la liste pour l’afficher. |
| Prédictions | Score de [prédiction d’attrition]({{site.baseurl}}/user_guide/predictive_suite/predictive_churn) et de [prédiction d’achat]({{site.baseurl}}/user_guide/predictive_suite/predictive_purchases) pour cet utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

![][3]

### Onglet social

L’onglet **Social** contient un affichage de haut niveau de l’activité de l’utilisateur sur Twitter et Facebook si ces plateformes sont connectées.

| Catégorie sociale | Contient |
| --- | --- |
| Twitter | Nom de l’utilisateur sur Twitter, nombre de followers, nombre d’utilisateurs qu’ils suivent et nombre de tweets. |
| Facebook | Les publications Facebook likées par cet utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

![][4]

### Onglet d’historique d’envoi de messages

L’onglet **Message History (Historique d’envoi de messages)** du profil utilisateur affiche les événements récents liés à la messagerie (environ 40) pour un utilisateur individuel au cours des 30 derniers jours. Ces événements comprennent les messages que l’utilisateur a envoyés, reçus, avec lesquels il a interagi, etc.

{% alert note %}
Si vous avez des commentaires sur ce tableau ou désirez voir des événements particuliers, veuillez envoyer un e-mail à [user-targeting@braze.com](mailto:user-targeting@braze.com?subject=Messaging%20History%20Tab%20Feedback) avec comme ligne d’objet « Commentaire sur l’onglet d’historique d’envoi de messages ».
{% endalert %}

![][5]

#### Afficher et comprendre les événements

Pour chaque événement dans le tableau **Historique d’envoi de messages**, vous pouvez voir le canal de communication, le type d’événement, l’horodatage de la subvenue de l’événement et le message de la campagne ou du Canvas associé. Pour filtrer selon des événements donnés, cliquez sur **Filters (Filtres)** et sélectionnez des événements dans la liste.

##### Événements d’engagement par message

Les événements d’engagement par message suivants sont disponibles pour l’e-mail, les SMS, le push, les messages in-app, les cartes de contenu et les webhooks. Pour en savoir plus sur la manière dont des événements donnés sont suivis, consultez la section [Glossaire des événements d’engagement de message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events).

| Canal | Événements d’engagement disponibles |
| --- | --- |
| E-mail | Rebond<br>Clic<br>Livraison<br>Marqué comme courrier indésirable<br>Ouvert (consultez la [remarque sur l’événement d’ouverture d’e-mail](#note-on-email-open-event))<br>Envoyer<br>Rebond léger<br>Se désabonner |
| SMS | Envoi par le transporteur<br>Livraison<br>Échec de livraison<br>Entrant reçu<br>Rejet<br>Envoyer |
| Notification push | Rebond<br>Ouverture influencée<br>Premier plan iOS<br>Ouvrir<br>Envoyer |
| Message in-app | Clic<br>Impression |
| Cartes de contenu | Clic<br>Rejeté<br>Impression<br>Envoyer |
| Webhooks | Envoyer |
{: .reset-td-br-1 .reset-td-br-2}

##### Événements d’interruption de message

Des événements d’interruption de message se produisent lorsqu’un message envoyé à un utilisateur a été abandonné en raison de la logique conditionnelle dans [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/) ou le [Contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content#aborting-messages) ou en raison de temporisations de l’affichage Liquid.

Les événements d’interruption sont disponibles pour les canaux suivants :

- E-mail
- SMS
- Notification push
- Webhooks

Les événements d’interruption ne sont pas disponibles actuellement pour les messages in-app et les cartes de contenu.

##### Événements de limite de fréquence

Un événement de limite de fréquence se produit lorsqu’un utilisateur est qualifié pour recevoir un message, mais ne l’a finalement pas reçu en raison des paramètres de [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Vous pouvez personnaliser les paramètres de limite de fréquence sur la page **Global Message Settings (Paramètres généraux des messages)** de votre tableau de bord.

#### Note sur l’événement e-mail ouvert{#note-on-email-open-event}

Le suivi de l’ouverture d’e-mails est sujet à des erreurs, quel que soit l’outil utilisé, y compris Braze. Grâce à une variété de fonctions de protection de la vie privée offertes par différents clients de messagerie qui bloquent le chargement automatique des images ou les chargent de manière proactive sur le serveur, les événements d’ouverture des e-mails sont susceptibles d’entraîner à la fois des faux positifs et des faux négatifs.

Si les statistiques d’ouverture des e-mails peuvent être utiles dans leur ensemble, par exemple pour comparer l’efficacité de différentes lignes d’objet, vous ne devez pas supposer qu’un événement d’ouverture individuel pour un utilisateur individuel est significatif.


[1]: {% image_buster /assets/img_archive/User_Search_Nonunique.png %}
[2]: {% image_buster /assets/img_archive/user_profile2.png %}
[3]: {% image_buster /assets/img_archive/profiles_engagement_tab.png %}
[4]: {% image_buster /assets/img_archive/profiles_social_tab.png %}
[5]: {% image_buster /assets/img_archive/profiles_messaging_history_tab.png %}

[12]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/
[13]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/campaigns_in_multiple_languages/#campaigns-in-multiple-languages
