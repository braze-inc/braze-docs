---
nav_title: À propos des Webhooks
article_title: À propos des Webhooks
page_order: 0
channel:
  - webhooks
description: "Cet article de référence couvre les bases des webhooks."
---

# À propos des Webhooks

> Cet article de référence couvre les bases des webhooks pour vous donner les blocs de construction dont vous avez besoin pour créer vos propres crochets. Vous cherchez des étapes sur la façon de créer un webhook au Brésil? Reportez-vous à [Créer un webhook][1].

Les Webhooks sont un moyen courant pour les applications de communiquer, de partager des données en temps réel. À notre époque, nous avons rarement une application autonome qui peut tout faire. La plupart du temps, vous travaillez dans plusieurs applications ou systèmes différents qui sont spécialisés pour exécuter certaines tâches, et ces applications ont besoin d'être en mesure de communiquer entre elles. C'est là que les webhooks entrent.

Un webhook est un message automatisé d'un système à l'autre après avoir rempli certains critères. En Brésil, ce critère est généralement le déclenchement d'un événement personnalisé.

En son cœur, un webhook est une méthode événementielle permettant à deux systèmes distincts de prendre des mesures efficaces en fonction des données transmises en temps réel. Ce message contient des instructions qui indiquent au système de réception quand et comment effectuer une tâche spécifique. Grâce à cela, les webhooks peuvent vous fournir un accès plus dynamique et plus flexible aux données et aux fonctionnalités programmatiques, et vous permettre de mettre en place des trajets clients qui simplifient les processus.

## Cas d'utilisation

Les Webhooks sont un excellent moyen de connecter vos systèmes ensemble — après tout, les webhooks sont la façon dont les applications communiquent. Voici quelques scénarios généraux où les webhooks peuvent être particulièrement utiles :

- Envoi de données vers et depuis Braze
- Envoi de messages à vos clients via des canaux qui ne sont pas directement pris en charge par Braze
- Envoi sur Braze APIs

Quelques cas d'utilisation plus spécifiques incluent les suivants :

- Si un utilisateur se désabonne de l'e-mail, vous pourriez avoir un webhook mettre à jour votre base de données d'analyse ou CRM avec les mêmes informations, en garantissant une vue d'ensemble du comportement de cet utilisateur.
- Envoyez [messages transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) aux utilisateurs dans Facebook Messenger ou Line.
- Envoyez du courrier direct aux clients en réponse à leur activité dans l'application et Web en utilisant des webhooks pour communiquer avec des services tiers tels que [Lob. om]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/lob/).
- Si vous êtes une application de réservation, vous pouvez envoyer un message SMS propulsé par Twilio pour confirmer la demande de l'application d'un client.
- Si un joueur atteint un certain niveau ou accède à un certain nombre de points, utilisez les webhooks et votre configuration API existante pour envoyer une mise à niveau de personnage ou des pièces directement sur leur compte. Si vous envoyez le webhook dans le cadre d'une campagne de messagerie multi-canaux, vous pouvez envoyer un message push ou autre pour informer le joueur de la récompense en même temps.
- Si vous êtes une compagnie aérienne, vous pouvez utiliser des webhooks et votre configuration API existante pour créditer le compte d'un client avec une remise une fois qu'il a réservé un certain nombre de vols.
- Recettes sans fin « Si cela alors » ([IFTTT](https://ifttt.com/about)) — par exemple, si un client se connecte à l'application par e-mail, cette adresse peut être automatiquement configurée dans Salesforce.

## Anatomie d'un webhook

Un webhook se compose des trois parties suivantes :

!\[Exemple de webhook divisé en méthode HTTP, URL HTTP, et corps de requête\]\[2\]

| Partie du Webhook        | Libellé                                                                                                                                                                                                                                                                                        |
| ------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [Méthode HTTP](#methods) | Tout comme les API, les webhooks ont besoin de méthodes de requête. Celles-ci sont données à l'URL à laquelle le webhook accède et indiquent au endpoint ce qu'il faut faire avec les informations fournies. Il y a quatre méthodes HTTP que vous pouvez spécifier : POST, GET, PUT et DELETE. |
| URL HTTP                 | L'adresse URL du point de terminaison de votre webhook. Le point de terminaison est l'endroit où vous enverrez les informations que vous capturez dans le webhook.                                                                                                                             |
| Corps de la requête      | Cette partie du webhook contient les informations que vous communiquez à la terminaison. Le corps de la requête peut être des paires de clés JSON ou du texte brut.                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

### Méthodes HTTP {#methods}

Le tableau suivant décrit les quatre méthodes HTTP que vous pouvez spécifier dans votre webhook.

| Méthode HTTP | Libellé                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| POSTER       | Cette méthode écrit de nouvelles informations sur le serveur récepteur. Un exemple commun de la méthode POST dans l'application réelle est un [formulaire de contact](https://www.braze.com/company/contact) sur un site web. Toutes les informations que vous mettez dans le formulaire font partie d'un corps de demande et sont envoyées à un destinataire. C'est la méthode la plus courante utilisée lors de l'envoi de données. |
| OBTENIR      | Cette méthode récupère les informations existantes, plutôt que d'écrire de nouvelles informations. C'est la méthode la plus courante utilisée pour demander des données à partir d'un serveur. Par exemple, considérez le point de terminaison [segments/liste]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Si vous faites une demande GET, elle retournera une liste de vos segments.                              |
| EFFACER      | Cette méthode met à jour les informations sur la terminaison, en remplaçant toutes les informations existantes par ce qui se trouve dans le corps de la requête.                                                                                                                                                                                                                                                                      |
| SUPPRIMER    | Cette méthode supprime la ressource dans l'URL HTTP.                                                                                                                                                                                                                                                                                                                                                                                  |
{: .reset-td-br-1 .reset-td-br-2}

## Webhooks à Braze

Au Brésil, vous pouvez créer un webhook comme une campagne de webhook, une campagne API ou une étape de Canvan.

{% tabs %}
{% tab Webhook Campaign %}

1. Dans le tableau de bord de Braze, allez dans **Campagnes**.
2. Cliquez sur **Créer une campagne** et sélectionnez **Webhook**.

Reportez-vous à [Créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) pour plus d'informations.

{% endtab %}
{% tab API Campaign %}

1. Dans le tableau de bord de Braze, allez dans **Campagnes**.
2. Cliquez sur **Create Campaign** et sélectionnez **API Campaign**.
3. Cliquez sur **Ajouter des messages** et sélectionnez **Webhook**.
4. Formatez votre appel API pour inclure un objet [webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Reportez-vous à [Créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) pour plus d'informations.

{% endtab %}
{% tab Canvas Step %}

1. Dans votre Canva, créez une nouvelle étape.
2. Dans la section **Message** de votre étape, sélectionnez **Webhook**.

Reportez-vous à [Créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) pour plus d'informations.

{% endtab %}
{% endtabs %}
[2]: {% image_buster /assets/img_archive/webhook_anatomy.png %}


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
