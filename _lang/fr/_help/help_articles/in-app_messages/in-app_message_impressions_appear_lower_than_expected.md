---
nav_title: Peu d’impressions des messages in-app
article_title: Peu d’impressions des messages in-app
page_order: 2

page_type: solution
description: "Cet article d’aide couvre les actions que vous pouvez prendre si le nombre d’impressions de vos messages in-app est inférieur à celui que vous souhaitez."
channel: messages in-app
---
# Peu d’impressions des messages in-app

Si le nombre d’impressions de vos messages in-app est inférieur à celui que vous souhaitez, nous vous recommandons de vérifier :
* [Taille du segment](#segment-size)
* [Journal de modifications](#segment-changelogs)
* [Exécuter des tests](#run-tests)
* [Déclencheurs d’événements](#event-triggers)
* [Impressions du message](#message-impressions)

## Taille du segment

Il est important de veiller à ce que votre taille de segment dans la campagne reflète votre public cible. Il peut y avoir des filtres appliqués qui limitent votre public et qui expliquent les faibles impressions pour votre campagne.

## Journal de modifications du Segment

Si le nombre d’impressions est faible par rapport à vos campagnes précedentes, assurez-vous que le segment ou la campagne n’a pas été accidentellement modifié depuis le lancement. Nos Journaux de modifications des segments et des campagnes vous informeront sur les changements, qui les a faits et quand.

![Lien pour afficher le journal de modifications sur la page Details (Détails) de la campagne avec sept changements depuis que l’utilisateur a vu la campagne pour la dernière fois][10]

## Exécuter des tests

Une façon rapide d’identifier les problèmes évidents est de cloner la campagne, de cibler votre propre ID utilisateur ou e-mail, et de lancer la campagne. Après avoir effectué le déclencheur du message (début de session, événement personnalisé, etc.), vérifiez que vous avez bien reçu le message. Ensuite, naviguez jusqu’au tableau de bord et actualisez la page pour voir si l’impression a bien été enregistrée. Si ce n’est pas le cas, le problème vient probablement de votre implémentation.

## Déclencheurs d’événements

Si la campagne est déclenchée par un début de session ou un événement personnalisé, vous devez vous assurer que cet événement ou cette session est suffisamment fréquent pour déclencher le message. Vérifiez ces données sur les pages [Overview][1] (pour les données de session) ou [Custom Events][2] (Événements personnalisés) :

![Page Événements personnalisés affichant un graphique pour le nombre de fois où l’événement personnalisé Added to Favorites (Ajouté aux favoris) s’est produit sur une période d’un mois][11]

## Impressions du message

La personnalisation de l’interface utilisateur ou des mécanismes de livraison des messages in-app dans le SDK peut nécessiter que vos développeurs utilisent nos méthodes pour enregistrer manuellement les impressions de message in-app. Consultez vos développeurs pour voir si vous personnalisez vos messages in-app pour :
  * [iOS][12] 
  * [Android][13] 

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 6 mai 2021_

[1]: {{site.baseurl}}/user_guide/data_and_analytics/reporting/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[10]: {% image_buster /assets/img_archive/trouble4.png %}
[11]: {% image_buster /assets/img_archive/trouble5.png %}
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/handing_in_app_display/#logging-impressions-and-clicks
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/
