---
nav_title: Mai
page_order: 8
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de mise à jour pour mai 2019."
---

# Mai 2019

## Cartes de contenu

Les Cartes de Contenu sont des contenus persistants qui apparaissent dans les applications et les expériences Web des clients.

Avec les Cartes de Contenu, vous pouvez envoyer un très ciblé, flux dynamique de contenu riche pour vos clients directement dans les applications qu'ils aiment, sans interrompre leur expérience. Ou, vous pouvez associer les Cartes de Contenu à d'autres canaux, comme les notifications par e-mail ou push, pour permettre des stratégies de marketing cohérentes.

![Flux de cartes de contenu]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

De plus, les Cartes de Contenu prennent en charge des fonctionnalités plus personnalisées, y compris le épinglage de cartes, le rejet de cartes, la livraison basée sur API, les délais d'expiration de cartes personnalisées, les analyses de cartes.

Utilisez-le pour créer des centres de notification, des flux de la page d'accueil et des flux de promotion.

Vous devrez mettre à jour vers une version de Braze SDK supportée :
- __iOS__: 3.8.0 ou supérieur
- __Android__: 2.6.0 ou supérieur
- __Web__: 2.2.0 ou supérieur

[En savoir plus sur les Cartes de Contenu ici !]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/overview/)

{% alert update %}
Les Cartes de Contenu pour les Courants, ainsi que notre documentation API pour les Cartes de Contenu, seront lancées plus tard dans la semaine. Restez à l'écoute!
{% endalert %}

## Ajout de la plateforme Roku

Braze a ajouté un nouveau canal à nos capacités! En se développant dans de nouveaux canaux, nous pouvons permettre à nos clients d'enrichir leurs données en comprenant les comportements de visualisation ou en fournissant à leurs consommateurs des expériences significatives sur tous les canaux pertinents.

Vous pouvez maintenant récupérer des données depuis les appareils Roku pour l'enrichissement de données et le suivi d'événements personnalisés.

[Consultez la documentation ici!]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/initial_sdk_setup/)

## Préférences de notification pour les mises à jour de Canvas & de la campagne

Cette nouvelle notification vous avertira par courriel lorsqu'une campagne/Canvas est activée, mise à jour, réactivée ou désactivée. Activez ceci dans les Préférences de Notification dans votre compte Braze. [En savoir plus sur cette préférence ici.]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences/#notification-preferences)

## Documentation des partenaires technologiques de Jampp

Jampp est une plateforme de marketing performante pour l'acquisition et le reciblage de clients mobiles. Il combine des données comportementales avec des technologies prédictives et programmatiques pour générer des revenus pour les annonceurs en montrant leur caractère personnel, des publicités pertinentes qui incitent les consommateurs à acheter pour la première fois, ou plus souvent.

[Les clients Braze peuvent s'intégrer à Jampp]({{site.baseurl}}/partners/advertising_technologies/retargeting/jampp/) en configurant le canal de webhook Braze pour diffuser des événements dans Jampp. En conséquence, les clients ont la possibilité d'ajouter des ensembles de données plus riches à leurs initiatives de redistribution avec Jampp dans l'écosystème de publicité mobile.

## Sélecteur de plateforme pour les messages dans l'application

Nous avons facilité la sélection de la destination de vos messages dans l'application et des plateformes pour lesquelles ils sont construits avec notre sélecteur de plateforme, qui souligne cette étape dans le processus de création de campagne.

!\[Plateforme Picker\]\[plat_p\]

## Champ Devises d'envoi pour l'e-mail

{% alert update %}
Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Mise à jour notée en août 2019._
{% endalert %}

Dans le but de continuer à améliorer nos capacités de courants, nous ajoutons `dispatch_id` en tant que champ aux événements Courriel courants pour tous les types de connecteurs.

Le `dispatch_id` est l'ID unique généré pour chaque transmission – ou expédition – envoyée depuis la plateforme Braze.

Alors que tous les clients qui reçoivent un message planifié reçoivent le même `dispatch_id`, les clients qui reçoivent des messages basés sur l'action ou sur l'API recevront un `dispatch_id unique` par message. Le champ `dispatch_id` vous permet d'identifier quelle instance d'une campagne récurrente est responsable de la conversion, ainsi vous disposez de plus d'informations et de plus amples informations sur les types de campagnes qui vous aident à pousser l'aiguille sur vos objectifs commerciaux.

## Afficher uniquement les mines - fonction de tri des campagnes

Lorsqu'un utilisateur coche la case `Afficher uniquement la mine` sur la grille de campagne, les résultats filtreront vers les campagnes uniquement créées par l'utilisateur connecté. De plus, l'utilisateur peut utiliser la barre de recherche en entrant `created_by_me:true`.

Aussi, la barre latérale de la grille de campagne est maintenant redimensionnable!

## Supprimer les utilisateurs par alias

Vous pouvez maintenant utiliser le point de terminaison `utilisateurs/supprimer` pour [supprimer des utilisateurs par alias]({{site.baseurl}}/api/endpoints/user_data/#user-delete-request)!

## Calcul unique pour les clics de courriel et ouvre

Les clics uniques et les ouvertures uniques pour les e-mails sont maintenant capturés et affichés sur une période de 7 jours par utilisateur et incrémentez un nombre de 1 dans cette fenêtre de 7 jours, par `dispatch_id`.

L'utilisation de `dispatch_id` permet aux messages récurrents de refléter le véritable nombre de clics ouverts ou uniques de chaque message. Il sera facile pour les clients de faire correspondre ces données, maintenant que le `dispatch_id` est disponible dans les courants.

Tous les utilisateurs utilisant Mailjet verront également une pointe dans ces chiffres, puisque la période d'unicité précédente était de plus de 30 jours. Vous auriez dû être informé de ce changement il y a trois (3) semaines.  Les clients de Sendgrid ne devraient pas voir de différence.

Vous pouvez rechercher ces termes mis à jour dans notre [Glossaire de métriques de rapport]({{site.baseurl }}/user_guide/data_and_analytics/report_metrics/).

{% alert update %}
Le comportement de `dispatch_id` diffère entre Canvas et les campagnes car Braze traite les pas de Canvas (à l'exception des pas d'entrée, qui peuvent être programmés) en tant qu'événements déclenchés, même lorsqu'ils sont "programmés". [En savoir plus sur le comportement de `dispatch_id` dans Canvas et les campagnes ici]({{site.baseurl}}/help/help_articles/data/dispatch_id/).

_Mise à jour notée en août 2019._
{% endalert %}


## Chaîne la plus engagée

{% alert update %}
Depuis la publication du produit [Novembre 2019]({{site.baseurl}}/help/release_notes/2019/november/#intelligence-suite), « Chaîne la plus engagée » a été renommée en [« Chaîne intelligente »]({{site.baseurl}}/user_guide/intelligence/intelligent_channel/).
{% endalert %}

Le filtre La Chaîne La Plus Engagée sélectionne la portion de votre auditoire pour laquelle le canal de messagerie sélectionné est leur « meilleur ». Dans ce cas, le « meilleur » signifie « a la plus grande probabilité d’engagement, compte tenu de l’histoire de l’utilisateur ». Vous pouvez sélectionner Email, Web Push, ou Mobile Push (qui comprend tout système d'exploitation ou appareil mobile disponible) comme chaîne.

Consultez ce nouveau filtre dans [notre bibliothèque de filtres de segmentation]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).
[plat_p]: {% image_buster /assets/img/iam_platforms.gif %}
