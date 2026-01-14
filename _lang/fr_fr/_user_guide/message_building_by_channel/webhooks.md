---
nav_title: Webhooks
article_title: Webhooks
page_order: 4
layout: dev_guide
alias: /about_webhooks/
guide_top_header: "Webhooks"
guide_top_text: "Les webhooks sont un moyen courant pour les applications de communiquer, de partager des données en temps réel. De nos jours, il est rare qu'une seule application autonome puisse tout faire. La plupart du temps, vous travaillez avec plusieurs applications ou systèmes différents, spécialisés dans l'exécution de certaines tâches, et ces applications doivent toutes pouvoir communiquer entre elles. C'est là qu'interviennent les webhooks. <br><br> Un webhook est un message automatisé envoyé par un système à un autre après qu'un certain critère a été rempli. Dans Braze, ce critère est généralement le déclenchement d'un événement personnalisé. <br><br>À la base, un webhook est une méthode basée sur les événements permettant à deux systèmes distincts de prendre des mesures efficaces sur la base de données transmises en temps réel. Ce message contient des instructions qui indiquent au système récepteur quand et comment effectuer une tâche spécifique. De ce fait, les webhooks peuvent vous offrir un accès plus dynamique et plus flexible aux données et aux fonctionnalités programmatiques, et vous donner les moyens de mettre en place des parcours clients qui rationalisent les processus. <br><br>**La disponibilité des webhooks dépend de votre paquetage Braze. Contactez votre gestionnaire de compte ou votre responsable satisfaction client pour commencer.**."
description: "Cette page d'atterrissage abrite les webhooks. Vous y trouverez des articles sur la création de webhooks, la création de modèles de webhooks et les webhooks Braze à Braze."
channel:
  - webhooks
search_rank: 3
guide_featured_title: "Articles de section"
guide_featured_list:
- name: "Création d'un webhook"
  link: /docs/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
  image: /assets/img/braze_icons/refresh-ccw-01.svg
- name: "Création d'un modèle de webhook"
  link: /docs/user_guide/message_building_by_channel/webhooks/webhook_template/
  image: /assets/img/braze_icons/table.svg
- name: Webhooks Braze à Braze
  link: /docs/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/
  image: /assets/img/braze_icons/switch-horizontal-01.svg
- name: Rapports
  link: /docs/user_guide/message_building_by_channel/webhooks/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: Résolution des problèmes liés aux demandes de webhook 
  link: /docs/help/help_articles/api/webhook_connected_content_errors/
  image: /assets/img/braze_icons/check-square-broken.svg
---

## ![cours d'apprentissage de Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"} Cas d'utilisation

Les webhooks sont un excellent moyen de connecter vos systèmes entre eux - après tout, les webhooks sont le moyen de communication des applications. Voici quelques scénarios généraux dans lesquels les webhooks peuvent être particulièrement utiles :

- Envoi de données vers et depuis Braze
- Envoi de messages à vos clients via des canaux qui ne sont pas directement pris en charge par Braze
- Publication dans les API de Braze

Voici quelques cas d'utilisation plus spécifiques :

- Si un utilisateur se désabonne d'un e-mail, vous pourriez demander à un webhook de mettre à jour votre base de données analytique ou CRM avec ces mêmes informations, garantissant ainsi une vue holistique du comportement de cet utilisateur.
- Envoyez des [messages transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) aux utilisateurs dans Facebook Messenger ou Line.
- Envoyez un publipostage aux clients en réponse à leur activité in-app et web en utilisant des webhooks pour communiquer avec des services tiers comme... [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Si un joueur atteint un certain niveau ou accumule un certain nombre de points, utilisez des webhooks et votre configuration API existante pour envoyer une amélioration de personnage ou des pièces directement sur son compte. Si vous envoyez le webhook dans le cadre d'une campagne de communication multicanale, vous pouvez envoyer un message push ou autre pour informer le joueur de la récompense en même temps.
- Si vous êtes une compagnie aérienne, vous pouvez utiliser les webhooks et votre configuration API existante pour créditer le compte d'un client d'une réduction après qu'il ait réservé un certain nombre de vols.
- Des recettes "If This Then That"[(IFTTT](https://ifttt.com/about)) à l'infini - par exemple, si un client se connecte à l'appli par e-mail, alors cette adresse peut être automatiquement configurée dans Salesforce.

## Anatomie d'un webhook

Un webhook se compose des éléments suivants.

| Partie de webhook | Description |
| --- | --- |
| [Méthode HTTP](#methods) | Comme les API, les webhooks ont besoin de méthodes de requête. Elles sont transmises à l'URL que le webhook atteint et indiquent à l'endpoint ce qu'il doit faire avec les informations fournies. Vous pouvez spécifier quatre méthodes HTTP : POST, GET, PUT et DELETE. |
| URL HTTP | L'adresse URL de votre endpoint webhook. L'endpoint est l'endroit où vous enverrez les informations que vous capturez dans le webhook. |
| Corps de la demande | Cette partie du webhook contient les informations que vous communiquez à l'endpoint. Le corps de la demande peut être constitué de paires clé-valeur JSON ou de texte brut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Exemple de webhook avec une méthode HTTP, une URL HTTP et un corps de requête.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### Méthodes HTTP {#methods}

Le tableau suivant décrit les quatre méthodes HTTP différentes que vous pouvez spécifier dans votre webhook.

| Méthode HTTP | Description |
| ----------- | ----------- |
| POST | Cette méthode permet d'écrire de nouvelles informations sur le serveur de réception. Un exemple courant de la méthode POST dans une application réelle est un [formulaire de contact](https://www.braze.com/company/contact) sur un site web. Les informations que vous saisissez dans le formulaire sont intégrées dans le corps de la requête et envoyées à un destinataire. C'est la méthode la plus couramment utilisée pour l'envoi de données.
| GET | Cette méthode permet de récupérer des informations existantes, plutôt que d'en écrire de nouvelles. Par définition, une requête GET ne comporte pas de corps de requête. C'est la méthode la plus couramment utilisée pour demander des données à un serveur. Prenons l'exemple de l'[endpoint`/segments/list` ]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Si vous effectuez une requête GET, vous obtiendrez une liste de vos segmentations.
| PUT | Cette méthode met à jour les informations sur l'endpoint, en remplaçant toute information existante par ce qui se trouve dans le corps de la requête. 
| SUPPRIMER | Cette méthode supprime la ressource dans l'URL HTTP. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Les webhooks à Braze

Dans Braze, vous pouvez créer un webhook en tant que campagne webhook, campagne API ou composant Canvas.

{% tabs %}
{% tab Webhook Campaign %}

1. Dans le tableau de bord de Braze, allez dans **Campagnes**.
2. Cliquez sur **Créer une campagne** et sélectionnez **Webhook**.

Pour plus d'informations, reportez-vous à la section [Création d'un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% tab API Campaign %}

1. Dans le tableau de bord de Braze, allez dans **Campagnes**.
2. Cliquez sur **Créer une campagne** et sélectionnez **Campagne API**.
3. Cliquez sur **Ajouter des messages** et sélectionnez **Webhook**.
4. Formulez votre appel à l'API pour inclure un [objet webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Pour plus d'informations, reportez-vous à la section [Création d'un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% tab Canvas Component %}

1. Dans votre canvas, créez un nouveau composant.
2. Dans la section **Message** de votre composant, sélectionnez **Webhook**.

Pour plus d'informations, reportez-vous à la section [Création d'un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).

{% endtab %}
{% endtabs %}

## Gestion des erreurs et limitation du débit des webhooks

Lorsque Braze reçoit une réponse d'erreur d'un appel de webhook, nous ajustons automatiquement le comportement d'envoi de ce webhook sur la base de ces en-têtes de réponse :

- `Retry-After`
- `X-Rate-Limit-Limit`
- `X-Rate-Limit-Remaining`
- `X-Rate-Limit-Reset`

Ces en-têtes nous aident à interpréter les limites de débit et à adapter la vitesse d'envoi en conséquence pour éviter d'autres erreurs. Nous mettons également en œuvre une stratégie de délais exponentiels pour les tentatives, ce qui permet de réduire le risque de saturation de vos serveurs en espaçant les tentatives dans le temps.

Si nous constatons que la majorité des demandes de webhook adressées à un hôte spécifique échouent, nous reportons temporairement toutes les tentatives d'envoi vers cet hôte. Ensuite, nous reprenons l'envoi après une période de refroidissement définie, ce qui permet à votre système de se rétablir.


