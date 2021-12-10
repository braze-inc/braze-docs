---
nav_title: "Types d'identification de l'API"
article_title: Types d'identification de l'API
page_order: 2.2
description: "Cet article de référence couvre les différents types d'API Identifiants qui existent dans le tableau de bord de Braze, où vous pouvez les trouver et à quoi ils sont destinés."
page_type: Référence
---

# Types d'identification de l'API

> Ce guide de référence touche les différents types d'identifiants d'API qui peuvent être trouvés dans le tableau de bord de Braze, leur but, où vous pouvez les trouver, et comment ils sont généralement utilisés. Pour plus d'informations sur les clés d'API REST ou sur les clés API de groupe d'applications, reportez-vous à la [Aperçu de la clé d'API Rest]({{site.baseurl}}/api/api_key/)

Les identifiants d'API suivants peuvent être utilisés pour accéder à votre modèle, à votre canevas, à votre campagne, à votre segment, à votre envoi ou à votre carte depuis l'API externe de Braze. Tous les messages doivent suivre l'encodage [UTF-8][1].

{% tabs %}
{% tab Template Ids %}

## Identifiant API du modèle

Un [Template]({{site.baseurl}}/api/endpoints/templates/) API Identifier ou Template ID est une clé hors de la boîte par Braze pour un modèle donné dans le tableau de bord. Les identifiants de gabarits sont uniques pour chaque gabarit et peuvent être utilisés pour référencer des gabarits via l'API.

Les modèles sont parfaits si votre entreprise contracte vos conceptions HTML pour les campagnes. Une fois les modèles construits, vous avez maintenant un modèle qui n'est pas spécifique à une campagne mais peut être appliqué à une série de campagnes comme une newsletter.

### Où puis-je le trouver?
Vous pouvez trouver votre ID de modèle l'un des deux moyens :

1. Dans le tableau de bord, ouvrez **Modèles & Médias** sous **Engagement** et sélectionnez un modèle préexistant. Si le modèle que vous voulez n'existe pas encore, créez-en un et enregistrez-le. En bas de chaque page de modèle, vous serez en mesure de trouver votre identificateur d'API de modèle.<br><br>
2. Braze offre une recherche **Identifiants d'API supplémentaires** , ici vous pouvez rechercher rapidement des identifiants spécifiques. Il se trouve en bas de l'onglet **API Settings** dans la page **Console développeur**.

### À quoi cela peut-il servir ?

- Mettre à jour les modèles via l'API
- Récupérer des informations sur un modèle spécifique

<br>
{% endtab %}
{% tab Canvas IDs %}

## Identifiant de l'API Canvas

Un identifiant API [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/) ou Canvas ID est une clé sur-le-champ par Braze pour un Canvas donné dans le tableau de bord. Les Canvas IDs sont uniques à chaque Canvas et peuvent être utilisés pour référencer les Canevas à travers l'API.

Notez que si vous avez une toile qui a des variantes, il existe un ID global de Canvas ainsi que des IDs individuels de Canvas imbriqués sous le canevas principal.

### Où puis-je le trouver?
Vous pouvez trouver votre ID Canvas dans le tableau de bord. Ouvrez **Canvas** sous **Engagement** et sélectionnez un Canevas préexistant. Si le Canevas que vous voulez n'existe pas encore, créez en un et enregistrez-le. En bas d'une page de toile individuelle, cliquez sur **Analyser les variantes**. Une fenêtre apparaît avec l'identifiant de l'API Canvas situé en bas.

### À quoi cela peut-il servir ?
- Suivre les analyses sur un message spécifique
- Récupérer des statistiques agrégées de haut niveau sur les performances de Canvas
- Saisissez les détails sur une toile spécifique
- Avec les courants pour introduire des données au niveau utilisateur pour une approche "plus grande image" des toiles
- Avec la distribution déclenchée par l'API afin de collecter des statistiques pour les messages transactionnels

<br>
{% endtab %}
{% tab Campaign IDs %}

## Identificateur API de campagne

Une [Campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/) identifiant d'API ou identifiant de campagne est une clé hors de la boîte par Braze pour une campagne donnée dans le tableau de bord. Les identifiants de campagne sont uniques à chaque campagne et peuvent être utilisés pour référencer des campagnes à travers l'API.

Notez que si vous avez une campagne qui a des variantes, il y a à la fois un ID global de la campagne ainsi que des IDs de la campagne individuelle imbriqués dans la campagne principale.

### Où puis-je le trouver?
Vous pouvez trouver votre identifiant de campagne de l'un des deux moyens :

1. Dans le tableau de bord, ouvrez **Campagnes** sous **Engagement** et sélectionnez une campagne préexistante. Si la campagne que vous voulez n'existe pas encore, créez-en une et enregistrez-la. En bas de la page de chaque campagne, vous serez en mesure de trouver votre **Identificateur d'API de campagne**.<br><br>
2. Braze offre une recherche **Identifiants d'API supplémentaires** , ici vous pouvez rechercher rapidement des identifiants spécifiques. Vous pouvez le trouver en bas de l'onglet **API Settings** dans la **Console développeur**.

### À quoi cela peut-il servir ?
- Suivre les analyses sur un message spécifique
- Récupérer des statistiques agrégées de haut niveau sur les performances de la campagne
- Saisissez les détails sur une campagne spécifique
- Avec les courants pour introduire des données au niveau utilisateur pour une approche "plus grande image" des campagnes
- Avec la distribution déclenchée par l'API afin de collecter des statistiques pour les messages transactionnels

<br>
{% endtab %}
{% tab Segment IDs %}

## Segment API Identifier

Un [Segment]({{site.baseurl}}/user_guide/engagement_tools/segments/) API Identifier ou Segment ID est une clé hors de la boîte par Braze pour un segment donné dans le tableau de bord. Les identifiants de segment sont uniques à chaque segment et peuvent être utilisés pour référencer des segments à travers l'API.

### Où puis-je le trouver?
Vous pouvez trouver votre ID de segment une des deux façons :

1. Dans le tableau de bord, ouvrez **Segments** sous **Engagement** et sélectionnez un segment préexistant. Si le segment que vous voulez n'existe pas encore, créez-en un et enregistrez-le. En bas de la page de chaque segment, vous serez en mesure de trouver votre identificateur d'API Segment. <br><br>
2. Braze offre une recherche **Identifiants d'API supplémentaires** , ici vous pouvez rechercher rapidement des identifiants spécifiques. Il se trouve en bas de l'onglet **API Settings** dans la page **Console développeur**.

### À quoi cela peut-il servir ?
- Obtenir des détails sur un segment spécifique
- Récupérer les analyses d'un segment spécifique
- Tirez combien de fois un événement personnalisé a été enregistré pour un segment particulier
- Spécifier et envoyer une campagne aux membres d'un segment depuis l'API

{% endtab %}
{% tab Card IDs %}

## Identificateur API de la carte

Une carte API Identifier ou Card ID est une clé hors de la boite de Braze pour une carte de flux d'actualités donnée dans le tableau de bord. Les identifiants de carte sont uniques à chaque [flux d'actualités]({{site.baseurl}}/user_guide/engagement_tools/news_feed/) carte et peuvent être utilisés pour référencer des cartes via l'API.

### Où puis-je le trouver?
Vous pouvez trouver votre carte d'identité l'une des deux façons suivantes :

1. Dans le tableau de bord, ouvrez **Flux d'actualité** sous **Engagement** et sélectionnez un fil d'actualité préexistant. Si le fil d'actualité que vous voulez n'existe pas encore, créez en un et enregistrez-le. En bas de la page de chaque fil d'actualité, vous serez en mesure de trouver votre identificateur unique de carte API. <br><br>
2. Braze offre une recherche **Identifiants d'API supplémentaires** , ici vous pouvez rechercher rapidement des identifiants spécifiques. Il se trouve en bas de l'onglet **API Settings** dans la page **Console développeur**.

### À quoi cela peut-il servir ?
- Récupérer les informations pertinentes sur une carte
- Suivre les événements liés aux cartes de contenu et à l'engagement

<br>
{% endtab %}
{% tab Send IDs %}

## Envoyer l'identifiant

Un Send Identifier ou Send ID est une clé générée par Braze ou créée par vous pour un message envoyé sous lequel les analytiques doivent être suivies. L'identifiant d'envoi vous permet de récupérer des analytiques pour une instance spécifique d'une campagne envoyée via le point de terminaison [`sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics/).

### Où puis-je le trouver?

Les campagnes de déclenchement API et API envoyées en tant que diffusion génèreront automatiquement un identifiant d'envoi si un identifiant d'envoi n'est pas fourni. Si vous voulez spécifier votre propre identifiant d'envoi, vous devrez d'abord en créer un via le point de terminaison [`envoi/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/). L'identifiant doit contenir tous les caractères ASCII et au plus 64 caractères. Vous pouvez réutiliser un identifiant d'envoi à travers plusieurs envois de la même campagne si vous voulez grouper l'analyse de ces envois ensemble.

### À quoi cela peut-il servir ?
Envoyer et suivre les performances des messages de manière programmatique, sans création de campagne pour chaque envoi.

<br>
{% endtab %}
{% endtabs %}

[1]: https://en.wikipedia.org/wiki/UTF-8
