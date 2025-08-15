---
nav_title: mai
page_order: 8
noindex: true
page_type: update
description: "Cet article contient les notes de version de mai 2019."
---

# Mai 2019

## Cartes de contenu

Les cartes de contenu sont des contenus persistants qui apparaissent dans l’application et les expériences Web des clients.

Avec les cartes de contenu, vous pouvez envoyer un flux dynamique et hautement ciblé de contenu riche à vos clients, dans les applications qu’ils aiment, sans interrompre leur expérience. Vous pouvez également associer des cartes de contenu avec d’autres canaux, comme des notifications par e-mail ou push, pour créer des stratégies marketing cohésives.

![Cartes de contenu Feed]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

De plus, les cartes de contenu prennent en charge des fonctionnalités plus personnalisées, notamment les badges de carte, les fermetures de carte de contenu, la livraison basée sur API, des délais personnalisés d’expiration de carte et les indicateurs des performances.

Vous pouvez utiliser ces fonctionnalités pour créer des centres de notification, des flux d’accueil et des flux de promotion.

Vous devrez mettre à jour vers une version de SDK Braze prise en charge :
- iOS : 3.8.0 ou version ultérieure
- Android : 2.6.0 ou ultérieure
- Web : 2.2.0 ou ultérieure

[Pour en savoir plus sur les cartes de contenu, cliquez ici !]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about/)

{% alert update %}
Les cartes de contenu pour Currents et notre documentation API pour les cartes de contenu seront lancées plus tard cette semaine. Restez à l’écoute !
{% endalert %}

## Ajout de la plateforme Roku

Braze a ajouté un nouveau canal à ses capacités ! En proposant de nouveaux canaux, nous pouvons permettre à nos clients d’enrichir leurs données grâce à une meilleure compréhension du comportement de visualisation des utilisateurs ou des opportunités de leur offrir des expériences intéressantes sur tous les canaux pertinents.

Vous pouvez désormais [récupérer les données des appareils Roku]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) à des fins d'enrichissement des données et de suivi des événements personnalisés.

## Préférences de notification pour les mises à jour de Canvas ou de campagne

Cette [nouvelle notification]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences) vous alertera par e-mail lorsqu'une campagne ou un canvas est activé, mis à jour, réactivé ou désactivé. Activez cette fonction dans les **préférences de notification de** votre compte Braze.

## Documentation du partenaire Jampp

Jampp est une plateforme de performance marketing utilisée pour acquérir et recibler les clients mobiles. Jampp combine des données comportementales avec une technologie prédictive et programmatique pour générer des revenus pour les annonceurs en montrant des publicités personnelles et pertinentes qui inspirent les consommateurs à acheter pour la première fois, ou plus souvent.

Les clients de Braze peuvent [s'intégrer à Jampp]({{site.baseurl}}/partners/jampp/) en personnalisant le canal webhook Braze pour le flux d'événements dans Jampp. Ils ont donc désormais la capacité d’ajouter des ensembles de données plus riches à leurs initiatives de reciblage dans leurs écosystèmes de publicité mobile.

## Sélecteur de plateforme pour les messages in-app

Notre sélecteur de plateforme facilite la sélection de vos messages in-app et des plateformes pour lesquelles ils sont conçus, et met l’accent sur cette étape dans le processus de création de campagnes.

![Plateforme Picker]({% image_buster /assets/img/iam_platforms.gif %})

## Champ Dispatch ID Currents pour l’e-mail

{% alert update %}
Le comportement par rapport au `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les étapes de Canvas (à l’exception des étapes d’entrée, qui peuvent être programmées) en tant qu’événements déclenchés, et ce même lorsqu’elles sont « programmées ». En savoir plus sur le [comportement de`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans Canvas et les campagnes.

_Mise à jour notée en août 2019._
{% endalert %}

Pour continuer à améliorer les capacités de Currents, nous ajoutons `dispatch_id` en tant que champ aux événements e-mail Currents sur tous les types de connecteurs.

Le `dispatch_id` est l’ID unique généré pour chaque transmission (« dispatch ») envoyée depuis la plateforme Braze.

Alors que tous les clients qui reçoivent un message planifié reçoivent les mêmes `dispatch_id`, les clients qui reçoivent des messages basés sur des actions ou des API auront un `dispatch_id` unique par message. Le champ `dispatch_id` vous permet d’identifier l’instance d’une campagne récurrente qui est responsable de la conversion, ce qui vous fournit des informations supplémentaires et des informations sur les types de campagnes qui peuvent booster vos objectifs commerciaux.

## Fonction de tri de campagne « Only Show Mine » (Afficher uniquement les miennes)

Quand un utilisateur coche la case `Only Show Mine` sur la grille de campagne, les résultats affichés montreront uniquement les campagnes créées par l’utilisateur actuellement connecté. De plus, l’utilisateur peut utiliser la barre de recherche en saisissant `created_by_me:true`.

Et la barre latérale de la grille de campagne est maintenant redimensionnable !

## Supprimer les utilisateurs par alias

Vous pouvez désormais utiliser l'endpoint `users/delete` pour [supprimer des utilisateurs par alias]({{site.baseurl}}/api/endpoints/user_data/#user-delete-request)!

## Calcul unique pour les clics et les ouvertures d’e-mails

Les clics uniques et les ouvertures uniques pour l’e-mail sont désormais capturés et affichés sur un délai de 7 jours par utilisateur et s’incrémentent de 1 dans cette fenêtre de 7 jours, pour chaque `dispatch_id`.

Utiliser `dispatch_id` permet des messages récurrents pour refléter le nombre réel d’ouvertures uniques ou de clics uniques de chaque message. Il sera facile pour les clients de faire correspondre ces données, maintenant que `dispatch_id` est disponible dans Currents.

Tous les utilisateurs sur Mailjet verront un pic dans ces chiffres, étant donné que la période d’unicité précédente était de plus de 30 jours. Vous auriez dû être averti de cette modification il y a trois (3) semaines.  Les clients de SendGrid ne devraient pas voir de différence.

Vous pouvez rechercher ces termes actualisés dans notre [glossaire des indicateurs de rapport]({{site.baseurl}}/user_guide/data/report_metrics/).

{% alert update %}
Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les étapes de Canvas (à l'exception des étapes d'entrée, qui peuvent être planifiées) comme des événements déclenchés, même lorsqu'elles sont " planifiées ". [En savoir plus sur le [comportement de`dispatch_id` ]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans Canvas et les campagnes.

_Mise à jour notée en août 2019._
{% endalert %}


## Canal le plus engagé

{% alert update %}
À partir de la [version du produit de novembre 2019]({{site.baseurl}}/help/release_notes/2019/november/#intelligence-suite), le " canal le plus engagé " a été renommé [" canal intelligent ".]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/)
{% endalert %}

Le filtre Most Engaged Channel (Canal avec le plus d’interactions) sélectionne la partie de votre audience pour qui le canal de communication sélectionné est le « meilleur » canal. Dans ce cas, « le meilleur » signifie celui qui a la plus forte probabilité d’engagement, compte tenu de l’historique de l’utilisateur. Vous pouvez sélectionner l’e-mail, les notifications push Web ou notifications push sur mobile (qui inclut tout système d’exploitation ou appareil mobile disponible) comme canal.

Découvrez ce nouveau filtre dans notre [bibliothèque de filtres de segmentation]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).

