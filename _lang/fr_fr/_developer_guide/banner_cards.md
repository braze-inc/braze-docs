---
page_order: 2.2
nav_title: Cartes bannières
article_title: Cartes bannières
description: "Cette page d'atterrissage contient tout ce qui concerne les Banner Cards, y compris des articles sur la façon de créer des Banner Cards et des cas d'utilisation."
channel:
- Banners
---

# Cartes bannières

> Avec les Banner Cards, vous pouvez créer des envois de messages personnalisés pour vos utilisateurs tout en étendant la portée de vos autres canaux, tels que l'e-mail ou les notifications push. À l'instar des [cartes de contenu]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/about), vous pouvez intégrer des cartes directement dans votre application ou votre site web, ce qui vous permet d'engager le dialogue avec les utilisateurs par le biais d'une expérience sur l'application qui semble naturelle.

{% alert important %}
Les cartes bannières sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer à cet accès anticipé.
{% endalert %}

## Cas d’utilisation

Parce que les Banner Cards n'expirent jamais et sont automatiquement personnalisées à chaque fois qu'un utilisateur démarre une nouvelle session, elles sont idéales pour :

- Mise en avant des fonctionnalités
- Informer les utilisateurs des événements à venir
- Partager des mises à jour sur les programmes de fidélisation

## À propos de Banner Cards

### Expiration de la carte

Par défaut, les Banner Cards n'expirent pas - cependant, vous pouvez choisir une date de fin si nécessaire.

### ID de placement {#placement-ids}

Les placements de cartes bannières sont uniques à chaque espace de travail et peuvent être utilisés pour 10 campagnes au sein d'un même espace de travail. En outre, les placements au sein de chaque espace de travail doivent se voir attribuer un ID unique. Vous créerez des placements et leur attribuerez des ID lorsque vous [créerez une campagne de cartes bannières]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/) ou que vous [intégrerez des cartes bannières dans votre application]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/).

{% alert important %}
Evitez de modifier les ID de placement après avoir lancé une campagne Banner Card.
{% endalert %}

### Priorité de la carte {#card-priority}

Lorsque plusieurs campagnes font référence au même ID de placement, les cartes sont affichées par ordre de priorité. Par défaut, les cartes bannières nouvellement créées sont réglées sur une priorité moyenne, mais vous pouvez [régler manuellement la priorité]({{site.baseurl}}/developer_guide/banner_cards/creating_banner_cards/#set-card-priority) sur élevée, moyenne ou faible. Si plusieurs cartes ont le même niveau de priorité, la carte la plus récente sera affichée en premier.

### Indicateurs

Il s'agit des indicateurs les plus importants de la carte Bannière. Pour une liste complète des indicateurs, des définitions et des calculs, consultez le [glossaire des indicateurs du rapport.]({{site.baseurl}}/user_guide/data/report_metrics/)

| Indicateurs | Définition |
| --- | --- |
| [Impressions totales]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-impressions) | Nombre de fois où le message a été chargé et apparaît sur l'écran d'un utilisateur, indépendamment de toute interaction préalable (par exemple, si un message est montré deux fois à un utilisateur, il sera compté deux fois). |
| [Impressions uniques]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-impressions) | Nombre total d'utilisateurs ayant reçu et consulté un message donné au cours d'une journée. Chaque utilisateur n'est compté qu'une seule fois. |
| [Nombre total de clics]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#total-clicks) | Le nombre total (et le pourcentage) d'utilisateurs qui ont cliqué dans le message diffusé, indépendamment du fait que le même utilisateur clique plusieurs fois. |
| [Clics uniques]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#unique-clicks) | Le nombre distinct de destinataires qui ont cliqué au moins une fois dans un message est mesuré par [`dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/). Chaque utilisateur n'est compté qu'une seule fois. |
| [Conversions primaires]({{site.baseurl}}/user_guide/data_and_analytics/report_metrics#primary-conversions-a-or-primary-conversion-event) | Le nombre de fois où un événement défini se produit après l’interaction ou la consultation d’un message reçu d’une campagne Braze. Cet événement défini est déterminé par vous lorsque vous créez la campagne. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étapes suivantes

Maintenant que vous connaissez les cartes bannières, vous êtes prêt pour les étapes suivantes :

- [Créer des campagnes de cartes bannières]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns/)
- [Intégrer des cartes bannières dans votre application]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards/)
