---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des messages in-app pour le Web
platform: Web
page_order: 5
channel: messages in-app
description: "Cette page comprend les étapes de résolution des problèmes à suivre pour les problèmes courants avec la livraison ou l’affichage de messages in-app."

---

# Résolution des problèmes

## Les impressions sont inférieures à la valeur attendue

Les déclencheurs prennent du temps pour se synchroniser à l’appareil au démarrage de la session. Il peut donc se produire une sorte de course si les utilisateurs enregistrent un événement ou un achat juste après qu’ils aient démarré la session. Une possible solution pourrait être de changer la campagne pour qu’elle se déclenche au démarrage de la session, puis de segmenter l’événement ou l’achat prévu. Notez que le message in-app serait livré au démarrage de session suivant l’arrivée de l’événement.

## Le message in-app attendu ne s’est pas affiché

La plupart des problèmes de messages in-app peuvent être divisés en deux catégories principales : la livraison et l’affichage. Pour résoudre les problèmes d’un message in-app prévu qui ne s’est pas affiché sur votre appareil, vous devez d’abord vous assurer que le [message in-app a été livré à l’appareil][troubleshooting_iams_11], puis [résoudre les problèmes d’affichage du message][troubleshooting_iams_12].

## Livraison de messages in-app {#troubleshooting-in-app-message-delivery}

Le SDK demande des messages in-app aux serveurs de Braze au démarrage de la session. Pour vérifier si des messages in-app sont livrés sur votre appareil, vous devez vous assurer qu’ils sont à la fois demandés par le SDK et retournés par les serveurs de Braze.

### Vérifier si les messages sont demandés et retournés

1. Ajoutez-vous en tant qu’[utilisateur test][troubleshooting_iams_1] sur le tableau de bord.
2. Configurez une campagne de messages in-app ciblant votre utilisateur.
3. Assurez-vous qu’une nouvelle session se produit dans votre application.
4. Utilisez les [journaux d'événements utilisateurs][troubleshooting_iams_3] pour vérifier que votre appareil demande des messages in-app lors du démarrage de la session. Trouvez la demande SDK associée à l’événement de démarrage de session de votre utilisateur test.
  - Si votre application était supposée demander des messages in-app déclenchés, vous devriez voir `trigger` dans le champ **Requested Responses (Réponses demandées)** sous **Response Data (Données de réponse)**.
  - Si votre application était supposée demander des messages in-app originaux, vous devriez voir `in_app` dans le champ **Requested Responses (Réponses demandées)** sous **Response Data (Données de réponse)**.
5. Utilisez les [journaux d’événements utilisateurs][troubleshooting_iams_3] pour vérifier si les messages in-app corrects sont retournés dans les données de réponse.<br>
![][troubleshooting_iams_5]

### Résoudre des problèmes de messages qui ne sont pas demandés

Si vos messages in-app ne sont pas demandés, votre application peut ne pas suivre correctement les sessions, car les messages in-app sont actualisés lors du démarrage de la session. Assurez-vous également que votre application démarre bien une session selon les sémantiques de libération sur temporisation de session de votre application :

![La demande SDK trouvée dans les journaux d'événements utilisateurs affichant un événement de démarrage de session réussi.][troubleshooting_iams_10]

### Résoudre des problèmes de messages qui ne sont pas retournés

Si vos messages in-app ne sont pas retournés, vous avez probablement un problème de ciblage de campagne :

- Votre segment ne contient pas votre utilisateur.
  - Vérifiez l’onglet [**Engagement (Engagement)**][troubleshooting_iams_6] de votre utilisateur pour voir si le segment correct apparaît dans **Segments (Segments)**.
- Votre utilisateur a déjà reçu le message in-app et n’était pas éligible pour le recevoir à nouveau.
  - Vérifiez les [paramètres de nouvelle éligibilité de la campagne][troubleshooting_iams_7] à l’étape **Delivery (Livraison)** du **Campaign Composer (Composeur de campagne)** et assurez-vous que les paramètres de nouvelle éligibilité correspondent à la configuration de votre test.
- Votre utilisateur a atteint la limite de fréquence pour la campagne.
  - Vérifier les [paramètres de la limite de fréquence][troubleshooting_iams_8] de la campagne et assurez-vous qu’ils correspondent à la configuration de votre test.
- Si un groupe de contrôle a été créé sur la campagne, votre utilisateur peut être passé dans le groupe de contrôle.
  - Vous pouvez vérifier si cela s’est produit en créant un segment avec un filtre de campaign variant reçu, où la variante est définie sur **Contrôle** et vérifier si votre utilisateur est passé dans ce segment.
  - Lorsque vous créez des campagnes à des fins de test d’intégration, assurez-vous de ne pas ajouter un groupe de contrôle.

## Affichage du message dans l’application {#troubleshooting-in-app-message-display}

Si votre application demande et reçoit avec succès des messages in-app mais qu’ils ne s’affichent pas, une logique du côté de l’appareil peut empêcher l’affichage :

- Les messages in-app déclenchés ont des limites de débit en fonction de l’[intervalle de temps minimum entre les déclencheurs][troubleshooting_iams_9], qui est par défaut de 30 secondes.
- Si vous avez une gestion personnalisée des messages dans l’application via `braze.subscribeToInAppMessage` ou `appboy.subscribeToNewInAppMessages`, vérifiez cet abonnement pour s’assurer qu’il n’affecte pas l’affichage des messages dans l’application.

[troubleshooting_iams_1]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[troubleshooting_iams_2]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[troubleshooting_iams_3]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[troubleshooting_iams_4]: #session-tracking
[troubleshooting_iams_5]:  {% image_buster /assets/img_archive/event_user_log_iams.png %}
[troubleshooting_iams_6]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[troubleshooting_iams_7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/
[troubleshooting_iams_8]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping
[troubleshooting_iams_9]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[troubleshooting_iams_10]: {% image_buster /assets/img_archive/event_user_log_session_start.png %}
[troubleshooting_iams_11]: #troubleshooting-in-app-message-delivery
[troubleshooting_iams_12]: #troubleshooting-in-app-message-display
