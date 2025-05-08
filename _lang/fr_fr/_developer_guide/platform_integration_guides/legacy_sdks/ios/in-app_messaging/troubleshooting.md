---
nav_title: Résolution des problèmes
article_title: Résolution des problèmes de messagerie in-app pour iOS
platform: iOS
page_order: 7
description: "Cet article de référence couvre les sujets de résolution des problèmes potentiels des messages in-app iOS."
channel:
  - in-app messages

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Résolution des problèmes des messages in-app

## Impressions

#### L’impression ou les analyses de clics ne sont pas enregistrées

Si vous avez défini un délégué de message in-app pour gérer manuellement l’affichage des messages ou les actions de clic, vous devrez enregistrer manuellement les clics et les impressions sur le message in-app.

#### Les impressions sont inférieures à la valeur attendue

Les déclencheurs mettent du temps à se synchroniser avec l’appareil au démarrage de la session, il peut donc y avoir une condition de concurrence si les utilisateurs enregistrent un événement ou achètent juste après avoir démarré une session. Une possible solution pourrait être de changer la campagne pour qu’elle se déclenche au démarrage de la session, puis de segmenter l’événement ou l’achat prévu. Notez que cela enverrait le message in-app à l’application au prochain démarrage de la session après que l’événement se soit produit.

## Le message in-app attendu ne s’est pas affiché

La plupart des problèmes de messages in-app peuvent être divisés en deux catégories principales : livraison et affichage. Pour savoir pourquoi un message in-app attendu ne s'est pas affiché sur votre appareil, vous devez d'abord vous assurer que le [message in-app a bien été envoyé à l'appareil](#troubleshooting-in-app-message-delivery), puis [résoudre le problème de l'affichage du message](#troubleshooting-in-app-message-display).

### Livraison de messages in-app {#troubleshooting-in-app-message-delivery}

Le SDK demande des messages in-app aux serveurs Braze au démarrage de la session. Pour vérifier si les messages in-app sont livrés sur votre appareil, vous devez vous assurer que les messages in-app sont à la fois demandés par le SDK et renvoyés par les serveurs de Braze.

#### Vérifier si les messages sont demandés et retournés

1. Ajoutez vous en tant qu'utilisateur test]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) sur le tableau de bord.
2. Configurez une campagne de messages in-app ciblée pour votre utilisateur.
3. Assurez-vous qu’une nouvelle session se produit dans votre application.
4. Utilisez le journal des événements utilisateurs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) pour vérifier que votre appareil demande des messages in-app au démarrage de la session. Recherchez la requête SDK associée à l’événement de démarrage de session de votre utilisateur test.
  - Si votre application était censée demander des messages intégrés déclenchés, vous devriez voir `trigger` dans le champ **Réponses demandées** sous **Données de réponse**.
  - Si votre application était censée demander des messages intégrés originaux, vous devriez voir `in_app` dans le champ **Réponses demandées** sous **Données de réponse**.
5. Utilisez les journaux des événements utilisateurs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) pour vérifier si les messages in-app corrects sont renvoyés dans les données de réponse.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

#### Résoudre les problèmes de messages non demandés

Si vos messages in-app ne sont pas demandés, il est possible que votre application ne suive pas correctement les sessions, car les messages in-app sont actualisés au démarrage de la session. Assurez-vous également que votre application démarre réellement une session en fonction de la sémantique du délai d’expiration de session de votre application :

![La demande de SDK trouvée dans le journal des événements utilisateurs affichant un événement de démarrage de session réussi.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

### Résoudre les problèmes de messages non renvoyés

Si les messages in-app ne sont pas renvoyés, vous risquez probablement d’avoir un problème de ciblage de campagne :

- Votre segment ne contient pas votre utilisateur.
  - Vérifiez dans l'onglet [\*\*Engagement**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) ] de votre utilisateur si le segment correct apparaît sous **Segments**.
- Votre utilisateur a déjà reçu le message in-app, mais n’était pas rééligible pour le recevoir à nouveau.
  - Vérifiez les [paramètres de rééligibilité de la campagne]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) sous l'étape **Réception/distribution** du **Composeur de campagne** et assurez-vous que les paramètres de rééligibilité correspondent à votre configuration de test.
- Votre utilisateur a atteint la limite de fréquence pour la campagne.
  - Vérifiez les paramètres de la campagne [limite de fréquence]]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) et assurez-vous qu'ils correspondent à votre configuration de test.
- Si un groupe de contrôle a été créé pour la campagne, votre utilisateur peut être tombé dans le groupe de contrôle.
  - Vous pouvez vérifier si cela s'est produit en créant un segment avec un filtre de variante de campagne reçue, où la variante de campagne est définie sur **Contrôle**, et vérifier si votre utilisateur est tombé dans ce segment.
  - Lors de la création de campagnes à des fins de test d’intégration, veillez à désactiver l’ajout d’un groupe de contrôle.

### Affichage manuel de messages in-app {#troubleshooting-in-app-message-display}

Si votre application demande et reçoit avec succès des messages in-app, mais qu’ils ne s’affichent pas, une logique côté appareil peut empêcher l’affichage :

- Les messages in-app déclenchés sont limités en débit en fonction de l'[intervalle de temps minimum entre les déclenchements]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), qui est de 30 secondes par défaut.
- Si vous avez défini un délégué pour personnaliser la gestion des messages in-app, vérifiez votre délégué pour vous assurer qu’il n’affecte pas l’affichage des messages in-app.
- Les échecs de téléchargement d’images empêcheront l’affichage des messages in-app contenant des images. Les téléchargements d’images échoueront toujours si l’infrastructure `SDWebImage` n’est pas intégrée correctement. Vérifiez les journaux de votre appareil pour vous assurer que les téléchargements d’images n’échouent pas.
- Si l’orientation de l’appareil n’a pas correspondu à l’orientation spécifiée par le message in-app, le message in-app ne s’affichera pas. Assurez-vous que votre appareil est dans la bonne orientation.


