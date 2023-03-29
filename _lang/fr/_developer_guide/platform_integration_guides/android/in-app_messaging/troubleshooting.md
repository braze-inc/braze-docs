---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes des messages in-app pour Android et FireOS
page_order: 40
platform: 
  - Android
  - FireOS
description: "Cet article de référence couvre les sujets potentiels de résolution des problèmes des messages in-app pour Android ou FireOS."
channel:
  - messages In-App

---

# Résolution des problèmes

## Impressions

#### L’impression ou les analytiques de clics ne sont pas enregistrées

Si vous avez défini un délégué de message in-app pour gérer manuellement l’affichage des messages ou les actions de clic, vous devrez enregistrer manuellement les clics et les impressions sur le message in-app.

#### Les impressions sont inférieures à la valeur attendue

Les déclencheurs mettent du temps à se synchroniser avec le périphérique au démarrage de la session, il peut donc y avoir une condition de concurrence si les utilisateurs enregistrent un événement ou achètent juste après avoir démarré une session. Une possible solution pourrait être de changer la campagne pour qu’elle se déclenche au démarrage de la session, puis de segmenter l’événement ou l’achat prévu. Notez que cela enverrait le message in-app à l’application au prochain démarrage de la session après que l’événement se soit produit.

## Le message in-app attendu ne s’est pas affiché

La plupart des problèmes de messages in-app peuvent être divisés en deux catégories principales : livraison et affichage. Pour résoudre les problèmes d’un message in-app qui n’a pas été affiché sur votre périphérique, vous devez d’abord vous assurer que le [message in-app a été envoyé au périphérique][troubleshooting_iams_11], puis [résoudre le problème d’affichage du message][troubleshooting_iams_12].

## Livraison de messages in-app {#troubleshooting-in-app-message-delivery}

Le SDK fait la requête de messages in-app aux serveurs de Braze au démarrage de session. Pour vérifier si les messages in-app sont livrés sur votre périphérique, vous devez vous assurer que les messages in-app sont tous deux demandés par le SDK et retournés par les serveurs de Braze.

### Vérifier si les messages sont demandés et retournés

1. Ajoutez-vous comme un [utilisateur test][troubleshooting_iams_1] sur le tableau de bord.
2. Configurez une campagne de messages in-app ciblée pour votre utilisateur.
3. Assurez-vous qu’une nouvelle session se produit dans votre application.
4. Utilisez les [journaux d’événements utilisateurs][troubleshooting_iams_3] pour vérifier que votre périphérique demande des messages in-app lors du démarrage de la session. Recherchez la requête SDK associée à l’événement de démarrage de session de votre utilisateur test.
  - Si votre application était censée requérir des messages in-app déclenchés, vous devriez voir `trigger` dans le champ **Réponses demandées** sous **Données de réponse**.
  - Si votre application était censée requérir des messages in-app originaux, vous devriez voir `in_app` dans le champ **Réponses demandées** sous **Données de réponse**.
5. Utilisez les [journaux d’événements utilisateurs][troubleshooting_iams_3] pour vérifier si les messages in-app corrects sont retournés dans les données de réponse.<br>![][troubleshooting_iams_5]

#### Résoudre les problèmes de messages non demandés

Si vos messages in-app ne sont pas demandés, il est possible que votre application ne suive pas correctement les sessions, car les messages in-app sont actualisés au démarrage de la session. Assurez-vous également que votre application démarre réellement une session en fonction de la sémantique du délai d’expiration de session de votre application :

![La requête SDK trouvée dans les journaux des utilisateurs d’événements affiche un événement de démarrage de session réussi.][troubleshooting_iams_10]

### Résoudre les problèmes de messages non renvoyés

Si les messages in-app ne sont pas renvoyés, vous risquez probablement d’avoir un problème de ciblage de campagne :

- Votre segment ne contient pas votre utilisateur.
  - Vérifiez l’onglet de l’[**Engagement**][troubleshooting_iams_6] de votre utilisateur pour voir si le bon segment apparaît dans **Segments**.
- Votre utilisateur a déjà reçu le message in-app, mais n’était pas rééligible pour le recevoir à nouveau.
  - Vérifiez les [paramètres de rééligibilité de la campagne][troubleshooting_iams_7] à l’étape **Livraison** du **Gestionnaire de campagne** et assurez-vous que les paramètres de rééligibilité correspondent à la configuration de test.
- Votre utilisateur a atteint la limite de fréquence pour la campagne.
  - Vérifiez les [paramètres de limite de fréquence][troubleshooting_iams_8] de la campagne et assurez-vous qu’ils correspondent à la configuration de votre test.
- Si un groupe de contrôle a été créé pour la campagne, votre utilisateur peut être tombé dans le groupe de contrôle.
  - Vous pouvez vérifier si cela s’est produit en créant un segment avec un filtre de variante de campagne reçu, où la variante de campagne est définie sur **Contrôle** et vérifier si votre utilisateur a chuté dans ce segment.
  - Lors de la création de campagnes à des fins de test d’intégration, veillez à désactiver l’ajout d’un groupe de contrôle.

## Affichage manuel de messages in-app {#troubleshooting-in-app-message-display}

Si votre application demande et reçoit avec succès des messages in-app mais qu’ils ne s’affichent pas, une logique du côté de l’appareil peut empêcher l’affichage :

- Les messages in-app déclenchés sont limités à la fréquence en fonction de l’[intervalle de temps minimum entre les déclencheurs][troubleshooting_iams_9], qui est de 30 secondes par défaut.
- Si vous avez défini un délégué pour personnaliser la gestion des messages in-app, vérifiez votre délégué pour vous assurer qu’il n’affecte pas l’affichage du message in-app.
- Les échecs de téléchargement d’images empêcheront l’affichage des messages in-app contenant des images. Les téléchargements d’images échoueront toujours si le `BrazeInAppMessageManager` n’est pas enregistré correctement. Vérifiez les journaux de votre périphérique pour vous assurer que les téléchargements d’images n’échouent pas.
- Si l’orientation de l’appareil ne correspond pas à l’orientation spécifiée par le message in-app, il ne s’affichera pas. Assurez-vous que votre périphérique est dans la bonne orientation.

[troubleshooting_iams_1]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users
[troubleshooting_iams_2]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[troubleshooting_iams_3]: {{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[troubleshooting_iams_4]: #session-tracking
[troubleshooting_iams_5]:  {% image_buster /assets/img_archive/event_user_log_iams.png %}
[troubleshooting_iams_6]: {{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab
[troubleshooting_iams_7]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/
[troubleshooting_iams_8]: {{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping
[troubleshooting_iams_9]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[troubleshooting_iams_10]: {% image_buster /assets/img_archive/event_user_log_session_start.png %}
[troubleshooting_iams_11]: #troubleshooting-in-app-message-delivery
[troubleshooting_iams_12]: #troubleshooting-in-app-message-display
