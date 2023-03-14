---
nav_title: Messages In-App non affichés
article_title: Messages In-App non affichés
page_order: 1

page_type: solution
description: "Cet article d’aide décrit comment résoudre les problèmes d’affichage ou de rendu des messages in-app."
channel: messages In-App
---

# Messages in-app non affichés

Si vous constatez que vos messages in-app ne s’affichent pas correctement, il y a différentes choses à vérifier :

* [Déclencheurs d’événements](#event-triggers)
* [Impressions du message](#message-impressions)
* [Tests](#run-tests)
* [Délai de session](#session-timeout)
* [Intervalle de messagerie](#minimum-interval)

## Déclencheurs d’événements

Si la campagne est déclenchée par un début de session ou un événement personnalisé, vous devez vous assurer que cet événement ou cette session est suffisamment fréquent pour déclencher le message. Vérifiez ces données sur les pages [Overview][1] (pour les données de session) ou [Custom Events][2] (Événements personnalisés) :

![Page Événements personnalisés affichant un graphique pour le nombre de fois que l’événement personnalisé Added to Favorites (Ajouté aux favoris) s’est produit sur une période d’un mois][14]

## Impressions du message

La personnalisation de l’interface utilisateur ou des mécanismes de livraison des messages in-app dans le SDK peut nécessiter que vos développeurs utilisent nos méthodes pour enregistrer manuellement les impressions de message in-app. Consultez vos développeurs pour voir si vous personnalisez vos messages in-app.

## Exécuter des tests

Il est important de déterminer si l’événement déclencheur ne se produit pas, ou si le message lui-même ne peut pas s’afficher. Pour tester, déclenchez le message en utilisant une action différente (comme un début de session ou un événement personnalisé différent) et vérifiez s’il s’affiche. Cela permettra de déterminer s’il s’agit potentiellement d’un problème de données.

Sinon, essayez d’utiliser un type différent de modèle de message in-app ou de taille d’image. Il y a des [spécifications à suivre pour les messages in-app][15]. Parfois, si une image est trop grande, cela empêchera le message In-App de s’afficher.

## Délai de session

Découvrez si vous avez personnalisé le délai de votre session. Par défaut, Braze récupère les messages in-app sur le serveur au début d’une session.

Si vous avez prolongé l’expiration de session, cela prolonge la période pendant laquelle nous pouvons actualiser les messages in-app potentiels auxquels vous êtes éligible. De plus, si votre campagne est définie pour se déclencher quand une session démarre, vous devez vous assurer suffisamment de temps pour permettre l’enregistrement de la nouvelle session. Par exemple, l’expiration de la session peut avoir été définie sur 30 secondes. Si vous ouvrez et fermez l’application en moins de 30 secondes, vous ne serez pas éligible pour recevoir un autre message in-app déclenché au démarrage de la session. 

Pour en savoir plus sur la personnalisation des délais de session pour les plateformes suivantes :
* [iOS][16]
* [Android][17]
* [Web][18]

## Intervalle minimum

Nous avons un intervalle minimum autorisé pour le déclenchement de messages in-app consécutifs, alors vous essayez peut-être de les déclencher trop rapidement. En savoir plus sur l’intervalle minimum pour les plateformes suivantes : 
* [iOS][19]
* [Android][20]
* [Web][21]

Les intervalles soit personnalisables, et nous les gardons pour éviter de submerger les utilisateurs avec trop de messages.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 15 juillet 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[14]: {% image_buster /assets/img_archive/trouble5.png %}
[15]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#customizing-session-timeout
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#customizing-session-timeout
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#customizing-session-timeout
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#in-app-message-delivery
