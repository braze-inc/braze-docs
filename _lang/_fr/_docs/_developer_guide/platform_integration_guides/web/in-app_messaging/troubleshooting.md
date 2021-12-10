---
nav_title: Dépannage
article_title: Dépannage des messages dans l'application pour le Web
platform: Web
page_order: 5
channel: messages intégrés à l'application
description: "Cette page comprend des étapes de dépannage à suivre pour les problèmes courants avec la livraison ou l'affichage de la messagerie dans l'application."
---

# Dépannage

## Le message attendu dans l'application n'a pas été affiché

La plupart des problèmes de messages intégrés peuvent être répartis en deux catégories principales : la livraison et l'affichage. Pour résoudre des problèmes, pourquoi un message attendu dans l'application ne s'affichait pas sur votre appareil, vous devriez d'abord [vous assurer que le message intégré a été transmis à l'appareil][troubleshooting_iams_11], puis [afficher le message de dépannage][troubleshooting_iams_12].

### Les impressions sont inférieures à celles attendues

Les déclencheurs prennent le temps de synchroniser l'appareil au démarrage de la session, pour qu'il puisse y avoir une condition de course si les utilisateurs enregistrent un événement ou achètent immédiatement après le début d'une session. Une solution de contournement pourrait être de modifier la campagne pour déclencher le démarrage de la session, puis de segmenter l'évènement ou l'achat prévu. Notez que cela enverrait le message dans l'application au début de la prochaine session après que l'événement se soit produit.

## Envoi de messages dans l'application {#troubleshooting-in-app-message-delivery}

Le SDK demande des messages dans l'application depuis les serveurs de Braze au démarrage de la session. Pour vérifier si des messages sont envoyés sur votre appareil, vous devrez vous assurer que les messages dans l'application sont à la fois demandés par le SDK et retournés par les serveurs de Brase.

### Vérifier si les messages sont demandés et retournés

1. S'ajouter en tant qu'\[utilisateur de test\]\[troubleshooting_iams_1\] sur le tableau de bord.
2. Configurez une campagne de message dans l'application ciblée sur votre utilisateur.
3. Assurez-vous qu'une [nouvelle session][troubleshooting_iams_4] se produit dans votre application.
4. \[Utiliser les journaux des utilisateurs\]\[troubleshooting_iams_3\] pour vérifier que votre appareil demande des messages dans l'application au démarrage de la session. Trouvez la requête SDK associée à l'événement de démarrage de votre utilisateur de test.
  - Si votre application était censée demander des messages In-App déclenchés, vous devriez voir `trigger` dans le champ Réponses demandées sous Données de réponse.
  - Si votre application était censée demander des messages originaux dans l'application, vous devriez voir  `in_app` dans le champ des réponses demandées sous Données de réponse.
5. Utilisez \[Event User Logs\]\[troubleshooting_iams_3\] pour vérifier si les bons messages dans l'application sont retournés dans les données de réponse.

!\[Message In-App\]\[troubleshooting_iams_5\]

### Dépannage des messages non demandés

Si vos messages dans l'application ne sont pas demandés, votre application pourrait ne pas être [des sessions de suivi correctement][troubleshooting_iams_4], car les messages dans l'application sont actualisés au démarrage de la session. Assurez-vous également que votre application démarre réellement une session en fonction du délai de sémantique de session de votre application :

!\[Début de session\]\[troubleshooting_iams_10\]

### Dépannage des messages non retournés

Si vos messages dans l'application ne sont pas retournés, vous rencontrez probablement un problème de ciblage de la campagne :

- Votre segment ne contient pas votre utilisateur.
  - Vérifiez \[onglet Engagement\]\[troubleshooting_iams_6\] de votre utilisateur pour voir si le segment correct apparaît sous Segments.
- Votre utilisateur a déjà reçu le message dans l'application et n'était pas de nouveau éligible pour le recevoir.
  - Vérifiez les \[paramètres de rééligibilité de la campagne\]\[troubleshooting_iams_7\] sous l'étape **Livraison** du **Compositeur de campagne** et assurez-vous que les paramètres de rééligibilité s'alignent sur votre configuration de test.
- Votre utilisateur a atteint la limite de fréquence pour la campagne.
  - Vérifiez la campagne \[paramètres de la limite de fréquence\]\[troubleshooting_iams_8\] et assurez-vous qu'elle s'aligne avec votre installation de test.
- S'il y avait un groupe de contrôle sur la campagne, votre utilisateur est peut-être tombé dans le groupe de contrôle.
  - Vous pouvez vérifier si cela s'est produit en créant un segment avec un filtre "Variante de campagne reçue", où la variante de la campagne est définie sur « Contrôle », et vérifier si votre utilisateur est tombé dans ce segment.
  - Lors de la création de campagnes à des fins de tests d'intégration, assurez-vous de ne pas ajouter un groupe de contrôle.

## Affichage du message dans l'application {#troubleshooting-in-app-message-display}

Si votre application demande et reçoit avec succès des messages dans l'application mais qu'ils ne sont pas affichés, il se peut que la logique du périphérique empêche l'affichage :

- Les messages déclenchés dans l'application sont limités à un débit basé sur l'intervalle de temps minimum [entre les déclencheurs][troubleshooting_iams_9], qui est par défaut de 30 secondes.
- Si vous avez une gestion personnalisée des messages dans l'application via `appboy.subscribeToInAppMessage` ou `appboy. ubscribeToNewInAppMessages`, vérifiez que l'abonnement n'affecte pas l'affichage des messages dans l'application.
[troubleshooting_iams_1]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users [troubleshooting_iams_2]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab [troubleshooting_iams_3]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab [troubleshooting_iams_5]: {% image_buster /assets/img_archive/event_user_log_iams. ng %} [troubleshooting_iams_6]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab [troubleshooting_iams_7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/ [troubleshooting_iams_8]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#fréquency-capping [troubleshooting_iams_10]: {% image_buster /assets/img_archive/event_user_log_session_start. ng %}

[troubleshooting_iams_4]: #session-tracking
[troubleshooting_iams_4]: #session-tracking
[troubleshooting_iams_9]: #minimum-time-interval-between-triggers
[troubleshooting_iams_11]: #troubleshooting-in-app-message-delivery
[troubleshooting_iams_12]: #troubleshooting-in-app-message-display

