---
nav_title: Faible Impressions de Message In-App
article_title: Faible Impressions de Message In-App
page_order: 2
page_type: Solution
description: "Cet article d'aide couvre les actions que vous pouvez entreprendre si vos impressions de messages intégrés sont inférieures à ce que vous voulez qu'ils soient."
channel: messages intégrés à l'application
---

# Impressions de messages faibles dans l'application

Si vos impressions sont inférieures à ce que vous voulez, nous vous recommandons :

* [Vérifier le segment](#segment-size)
* [Vérifier l'historique des modifications](#segment-changelogs)
* [Exécuter des tests](#run-tests)
* [Vérifier les déclencheurs d'événements](#event-triggers)
* [Vérifier les impressions des messages](#message-impressions)

## Taille du segment

Il est important de s'assurer que la taille de votre segment dans la campagne reflète le public que vous avez prévu. Il peut y avoir des filtres qui limitent votre audience et font que votre campagne a moins d'impressions.

## Segment changelogs

Si le nombre d'impressions est faible par rapport à l'endroit où il se trouve, assurez-vous que personne n'a modifié involontairement le segment ou la campagne depuis le lancement. Nos notes de changement de segment et de campagne vous donneront un aperçu des changements qui ont été apportés, qui ont apporté le changement et quand il s'est produit.

!\[Changelog\]\[10\]

## Exécuter des tests

Un moyen rapide d’identifier les problèmes évidents est de cloner la campagne, de cibler votre propre ID utilisateur ou votre courriel, et de lancer la campagne. Une fois que vous avez effectué le déclenchement du message (démarrage de la session, événement personnalisé, etc.), vérifiez que vous avez bien reçu le message. Ensuite, accédez au tableau de bord et rafraîchissez la page pour voir si votre impression est correctement enregistrée. Si ce n'est pas le cas, le problème est probablement dans votre mise en œuvre.


## Déclencheurs d'événement

Si la campagne est déclenchée par un début de session ou un événement personnalisé, vous voulez vous assurer que cet événement ou cette session se produit assez fréquemment pour déclencher le message. Vérifiez ces données sur les pages [Aperçu][1] (pour les données de session) ou [Événements personnalisés][2]:

!\[Statistiques personnalisées des compteurs d'événements\]\[11\]

## Impressions des messages

La personnalisation de l'interface utilisateur de message dans l'application ou des mécanismes de livraison dans le SDK peut nécessiter que vos développeurs utilisent nos méthodes pour connecter manuellement les impressions de messages dans l'application. Vérifiez avec vos développeurs si vous utilisez la personnalisation des messages dans l'application.

Vous pouvez en savoir plus à ce sujet:
  * [iOS][12] Documentation des messages intégrés à l'application
  * [Android][13] Documentation des messages dans l'application

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 6 mai 2021_
[10]: {% image_buster /assets/img_archive/trouble4.png %} [11]: {% image_buster /assets/img_archive/trouble5.png %}

[1]: {{site.baseurl}}/user_guide/data_and_analytics/your_reports/understanding_your_app_usage_data/#understanding-your-app-usage-data
[2]: {{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting
[12]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/in-app_messaging/customization/#logging-impressions-and-clicks
[13]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/#setting-custom-listeners
