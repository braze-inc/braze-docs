---
nav_title: À propos des webhooks
article_title: À propos des webhooks
page_order: 0
channel:
  - Webhooks
description: "Cet article de référence explique les bases des webhooks."

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/understanding-webhooks){: style="float:right;width:120px;border:0;" class="noimgborder"}À propos des webhooks

> Cet article de référence explique les bases des webhooks pour vous fournir les blocs de construction nécessaires pour créer les vôtres. Vous cherchez les étapes nécessaires pour créer un webhook dans Braze ? Reportez-vous à la section [Création d’un webhook][1].

Les webhooks sont un moyen de communication fréquent pour les applications, pour partager des données en temps réel. À ce jour, nous avons rarement une application isolée qui peut tout faire. La plupart du temps, vous travaillez avec de nombreuses applications ou systèmes spécialisés pour effectuer certaines tâches. Ces applications doivent pouvoir communiquer entre elles. C’est là où les webhooks entrent en jeu.

Un webhook est un message automatisé d’un système à un autre lorsque certains critères sont remplis. Dans Braze, ce critère est généralement le déclenchement d’un événement personnalisé.

À sa base, un webhook est une méthode basée sur l’événement pour que deux systèmes effectuent une action sur la base de données transmises en temps réel. Ce message contient des instructions disant au système destinataire quand et comment effectuer une tâche donnée. Pour cette raison, les webhooks peuvent fournir un accès plus dynamique et flexible aux données et à des fonctionnalités de programmation, et vous permettent également de définir des parcours utilisateurs simplifiant les processus.

## Cas d’utilisation

Les webhooks sont un moyen idéal pour connecter vos systèmes entre eux. Après tout, les webhooks sont le mode de communication des applications. Voici quelques scénarios généralistes dans lesquels les webhooks peuvent s’avérer particulièrement utiles :

- Envoyer des données à et depuis Braze
- Envoyer des messages à vos clients à l’aide de canaux qui ne sont pas directement pris en charge par Braze
- Publier vers les API de Braze

D’autres cas d’utilisation spécifiques comprennent les suivants :

- Si un utilisateur se désabonne de vos e-mails, vous pourriez avoir un webhook qui met à jour votre base de données d’analytiques ou votre CRM avec la même information, ce qui crée une vision holistique du comportement de votre utilisateur.
- Envoyez des [messages transactionnels]({{site.baseurl}}/api/api_campaigns/transactional_api_campaign/) aux utilisateurs à l’aide de Facebook Messenger ou Line.
- Envoyer des publipostages aux utilisateurs en réaction à leur activité in-app et Web en utilisant des webhooks pour communiquer avec des services tiers comme [Lob.com]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/lob/).
- Si un joueur atteint un niveau donné ou accumule un nombre de points données, utilisez vos webhooks et votre paramétrage API pour envoyer une mise à jour du personnage ou de la monnaie directement dans leur compte. Si vous envoyez un webhook en tant qu’une campagne de communication multicanale, vous pouvez envoyer une notification push ou un autre message pour signaler la récompense à votre joueur en même temps.
- Si vous êtes une compagnie aérienne, vous pouvez utiliser vos webhooks et vos paramètres API existants pour créditer le compte d’un client avec une promotion une fois qu’ils ont réservé un nombre donné de vols.
- Les recettes sans fin « If This Then That » ([IFTTT](https://ifttt.com/about)), par exemple, si un client s’enregistre dans une application par e-mail, alors cette adresse sera configurée automatiquement dans Salesforce.

## Anatomie d’un webhook

Un webhook comprend les trois parties suivantes :

![Exemple de webhook décomposé en méthode HTTP, URL HTTP et corps de la requête. Reportez-vous au tableau suivant pour plus de détails.][2]

| Morceau d’un webhook | Description |
| --- | --- |
| [Méthode HTTP](#methods) | Comme pour les API, les webhooks ont besoin de méthodes. Elles sont transmises à l’URL touchée par le webhook et disent à l’endpoint quoi faire avec l’information donnée. Vous pouvez spécifier quatre méthodes HTTP : POST, GET, PUT et DELETE. |
| URL HTTP | L’adresse URL de votre endpoint webhook. L’endpoint est l’endroit où vous enverrez les informations que vous capturez dans le webhook. |
| Corps de la demande | Cette partie du webhook contient les informations que vous transmettez à l’endpoint. Le corps de la requête peut être des paires clé-valeur JSON ou du texte brut. |
{: .reset-td-br-1 .reset-td-br-2}

### Méthodes HTTP {#methods}

Le tableau suivant décrit les quatre méthodes HTTP différentes que vous pouvez spécifier dans votre webhook.

| Méthode HTTP | Description |
| ----------- | ----------- |
| POST | Cette méthode écrit la nouvelle information sur le serveur destinataire. Un exemple fréquent de la méthode POST dans une application dans le monde réel, est le [formulaire de contact](https://www.braze.com/company/contact) d’un site Internet. Les informations que vous intégrez dans le formulaire deviennent une partie du corps de la requête et sont envoyées à un récepteur. Il s’agit de la méthode la plus employée pour l’envoi de données.
| GET | Cette méthode récupère les informations existantes au contraire d’écrire de nouvelles informations. C’est la méthode la plus utilisée lorsque vous demandez des données à un serveur. Par exemple, examinez l’endpoint [segments/list]({{site.baseurl}}/api/endpoints/export/segments/get_segment/). Si vous réalisiez une requête GET, elle renverrait une liste de vos segments.
| PUT | Cette méthode met à jour les informations sur l’endpoint en remplaçant les informations existantes avec le contenu du corps de la requête. 
| DELETE | Cette méthode supprime la ressource dans l’URL HTTP. 
{: .reset-td-br-1 .reset-td-br-2}

## Les webhooks dans Braze

Dans Braze, vous pouvez créer un webhook en tant que campagne webhook, campagne API ou composant Canvas.

{% tabs %}
{% tab Webhook Campaign %}

1. Dans le tableau de bord de Braze, rendez-vous dans **Campaigns**.
2. Cliquez sur **Créer une campagne** et sélectionnez **Webhook**.

Reportez-vous à [Création d’un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) pour plus d’informations.

{% endtab %}
{% tab API Campaign %}

1. Dans le tableau de bord de Braze, rendez-vous dans **Campaigns**.
2. Cliquez sur **Créer une campagne** et sélectionnez **Campagne API**.
3. Cliquez sur **Ajouter des messages** et sélectionnez **Webhook**.
4. Formatez votre appel API et ajoutez un [objet webhook]({{site.baseurl}}/api/objects_filters/messaging/webhook_object/).

Reportez-vous à [Création d’un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) pour plus d’informations.

{% endtab %}
{% tab Canvas Component %}

1. Créez un nouveau composant dans votre Canvas.
2. Dans la section **Message** de votre composant, sélectionnez **Webhook**.

Reportez-vous à [Création d’un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) pour plus d’informations.

{% endtab %}
{% endtabs %}


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/
[2]: {% image_buster /assets/img_archive/webhook_anatomy.png %}
