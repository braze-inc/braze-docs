---
nav_title: À propos des webhooks
article_title: À propos des webhooks
page_order: 0
channel:
  - webhooks
description: "Cet article de référence couvre les bases des webhooks, y compris les cas d’utilisation courants, l’anatomie des webhooks et la manière de les utiliser dans Braze."

---

# [![Cours d'apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}À propos des webhooks

> Cet article de référence explique les bases des webhooks pour vous fournir les blocs de construction nécessaires pour créer les vôtres. Vous cherchez les étapes nécessaires pour créer un webhook dans Braze ? Reportez-vous à la section [Création d'un webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)

Les webhooks sont un moyen de communication fréquent pour les applications, pour partager des données en temps réel. À ce jour, nous avons rarement une application isolée qui peut tout faire. La plupart du temps, vous travaillez avec de nombreuses applications ou systèmes spécialisés pour effectuer certaines tâches. Ces applications doivent pouvoir communiquer entre elles. C’est là où les webhooks entrent en jeu.

Un webhook est un message automatisé d’un système à un autre lorsque certains critères sont remplis. Dans Braze, ce critère est généralement le déclenchement d’un événement personnalisé.

À sa base, un webhook est une méthode basée sur l’événement pour que deux systèmes effectuent une action sur la base de données transmises en temps réel. Ce message contient des instructions disant au système destinataire quand et comment effectuer une tâche donnée. Pour cette raison, les webhooks peuvent fournir un accès plus dynamique et flexible aux données et à des fonctionnalités de programmation, et vous permettent également de définir des parcours utilisateurs simplifiant les processus.

## Cas d’utilisation

Les webhooks sont un moyen idéal pour connecter vos systèmes entre eux. Après tout, les webhooks sont le mode de communication des applications. Voici quelques scénarios généralistes dans lesquels les webhooks peuvent s’avérer particulièrement utiles :

- Envoyer des données à et depuis Braze
- Envoyer des messages à vos clients à l’aide de canaux qui ne sont pas directement pris en charge par Braze
- Publier vers les API de Braze

D’autres cas d’utilisation spécifiques comprennent les suivants :

- Si un utilisateur se désabonne de vos e-mails, vous pourriez avoir un webhook qui met à jour votre base de données d’analyse ou votre CRM avec la même information, ce qui crée une vision holistique du comportement de votre utilisateur.
- Envoyez des [messages transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) aux utilisateurs dans Facebook Messenger ou Line.
- Envoyez un publipostage aux clients en réponse à leur activité in-app et Web en utilisant des webhooks pour communiquer avec des services tiers comme [Lob.com]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/direct_mail/lob/).
- Si un joueur atteint un niveau donné ou accumule un nombre de points données, utilisez vos webhooks et votre configuration API pour envoyer une mise à jour du personnage ou de la monnaie directement dans leur compte. Si vous envoyez un webhook en tant qu’une campagne de communication multicanale, vous pouvez envoyer une notification push ou un autre message pour signaler la récompense à votre joueur en même temps.
- Si vous êtes une compagnie aérienne, vous pouvez utiliser les webhooks et votre configuration API existante pour créditer le compte d'un client d'une réduction après qu'il ait réservé un certain nombre de vols.
- Les recettes sans fin « If This Then That » ([IFTTT](https://ifttt.com/about)), par exemple, si un client s’enregistre dans une application par e-mail, alors cette adresse sera configurée automatiquement dans Salesforce.

## Anatomie d’un webhook

Un webhook se compose des éléments suivants.

| Morceau d’un webhook | Description |
| --- | --- |
| [Méthode HTTP](#methods) | Comme pour les API, les webhooks ont besoin de méthodes. Elles sont transmises à l’URL touchée par le webhook et disent à l’endpoint quoi faire avec l’information donnée. Vous pouvez spécifier quatre méthodes HTTP : POST, GET, PUT et DELETE. |
| URL HTTP | L’adresse URL de votre endpoint webhook. L’endpoint est l’endroit où vous enverrez les informations que vous capturez dans le webhook. |
| Corps de la demande | Cette partie du webhook contient les informations que vous transmettez à l’endpoint. Le corps de la requête peut être des paires clé-valeur JSON ou du texte brut. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Exemple de webhook avec une méthode HTTP, une URL HTTP et un corps de requête.]({% image_buster /assets/img_archive/webhook_anatomy.png %})

### Méthodes HTTP {#methods}

Le tableau suivant décrit les quatre méthodes HTTP différentes que vous pouvez spécifier dans votre webhook.

| Méthode HTTP | Description |
| ----------- | ----------- |
| POST | Cette méthode écrit la nouvelle information sur le serveur destinataire. Un exemple courant de la méthode POST dans une application réelle est un [formulaire de contact](https://www.braze.com/company/contact) sur un site web. Les informations que vous intégrez dans le formulaire deviennent une partie du corps de la requête et sont envoyées à un récepteur. Il s’agit de la méthode la plus employée pour l’envoi de données.
| GET | Cette méthode récupère les informations existantes au contraire d’écrire de nouvelles informations. Par définition, une requête GET ne comporte pas de corps de requête. C’est la méthode la plus utilisée lorsque vous demandez des données à un serveur. Prenons l'exemple de l'[endpoint `/segments/list`]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Si vous réalisiez une requête GET, elle renverrait une liste de vos segments.
| PUT | Cette méthode met à jour les informations sur l’endpoint en remplaçant les informations existantes avec le contenu du corps de la requête. 
| DELETE | Cette méthode supprime la ressource dans l’URL HTTP. 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Les webhooks dans Braze

Dans Braze, vous pouvez créer un webhook en tant que campagne webhook, campagne API ou composant Canvas.

{% tabs %}
{% tab Campagne webhook %}

1. Dans le tableau de bord de Braze, sélectionnez **Campagnes**.
2. Cliquez sur **Créer une campagne** et sélectionnez **Webhook**.

Pour plus d'informations, reportez-vous à la section [Création d'un webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 

{% endtab %}
{% tab Campagne API %}

1. Dans le tableau de bord de Braze, sélectionnez **Campagnes**.
2. Cliquez sur **Créer une campagne** et sélectionnez **Campagne API**.
3. Cliquez sur **Ajouter des messages** et sélectionnez **Webhook.**
4. Formulez votre appel à l'API de manière à inclure un [objet webhook.]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/)

Pour plus d'informations, reportez-vous à la section [Création d'un webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 

{% endtab %}
{% tab Composant de canvas %}

1. Créez un nouveau composant dans votre Canvas.
2. Dans la section **Message** de votre composant, sélectionnez **Webhook.**

Pour plus d'informations, reportez-vous à la section [Création d'un webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) 

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


