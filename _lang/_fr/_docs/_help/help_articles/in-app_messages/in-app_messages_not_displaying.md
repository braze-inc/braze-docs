---
nav_title: Les messages dans l'application ne sont pas affichés
article_title: Les messages dans l'application ne sont pas affichés
page_order: 1
page_type: Solution
description: "Cet article d'aide vous guide à travers le dépannage de problèmes avec des messages intégrés qui ne s'affichent pas ou ne s'affichent pas correctement."
channel: messages intégrés à l'application
---

# Les messages de l'application ne s'affichent pas

Si vous trouvez que vos messages dans l'application ne s'affichent pas ou ne s'affichent pas correctement, il y a un certain nombre d'approches que vous pouvez essayer de cocher :

* [Déclencheurs d'événement](#event-triggers)
* [Impressions des messages](#message-impressions)
* [Tests](#run-tests)
* [Expiration de la session](#session-timeout)
* [Intervalle de messagerie](#minimum-interval)

## Déclencheurs d'événement

Si la campagne est déclenchée par un début de session ou un événement personnalisé, vous voulez vous assurer que cet événement ou cette session se produit assez fréquemment pour déclencher le message. Vérifiez ces données sur les pages [Aperçu][1] (pour les données de session) ou [Événements personnalisés][2]:

!\[Statistiques personnalisées des compteurs d'événements\]\[14\]

## Impressions des messages

La personnalisation de l'interface utilisateur de message dans l'application ou des mécanismes de livraison dans le SDK peut nécessiter que vos développeurs utilisent nos méthodes pour connecter manuellement les impressions de messages dans l'application. Vérifiez avec vos développeurs si vous utilisez la personnalisation des messages dans l'application.

## Exécuter des tests

Il est important de déterminer si l'événement déclencheur ne se produit pas, ou si le message lui-même ne peut pas s'afficher. Pour tester, déclencher le message en utilisant une action différente (comme un démarrage de session ou un autre événement personnalisé) et vérifier s'il s'affiche. Cela aidera à isoler si c'est potentiellement un problème de données.

Vous pouvez également essayer d'utiliser un autre type de modèle de message ou de taille d'image dans l'application. Il y a [spécifications pour les messages dans l'application][15] qui doivent être suivies. Parfois, si une image est trop grande, cela empêchera l'affichage du message dans l'application.

## Expiration de la session

Découvrez si vous avez personnalisé le délai d'attente de votre session. Par défaut, Braze récupère les messages dans l'application au début d'une session du serveur.

Si vous avez prolongé le délai d'attente de la session, cela prolongera la période de temps à partir de laquelle nous pourrons actualiser les messages potentiels dans l'application pour lesquels vous êtes éligible. De plus, si votre campagne est configurée pour déclencher le démarrage d'une session, vous devrez vous assurer que le temps nécessaire est écoulé pour qu'une nouvelle session soit enregistrée. Par exemple, le délai d'attente de la session peut avoir été personnalisé pour être de 30 secondes. Si vous ouvrez et fermez l'application en moins de 30 secondes, vous ne serez pas autorisé à recevoir un autre message déclenché au démarrage de la session. Vous pouvez en savoir plus à ce sujet pour:

* [iOS][16]
* [Android][17]
* [Web][18]

## Intervalle minimum

Il y a un intervalle minimum auquel nous autoriserons le déclenchement consécutif des messages dans l'application, vous pouvez donc essayer de les déclencher trop rapidement. Consultez notre documentation pour plus d'informations à ce sujet:
* [iOS][19]
* [Android][20]
* [Web][21]

Bien que les intervalles soient personnalisables, nous les avons toujours en place pour éviter de surenvoyer vos utilisateurs.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 15 juillet 2021_
[14]: {% image_buster /assets/img_archive/trouble5.png %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[15]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/
[16]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#customizing-session-timeout
[17]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#customizing-session-timeout
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_sessions/#customizing-session-timeout
[19]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[20]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers
[21]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#in-app-message-delivery
