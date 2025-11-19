---
nav_title: Comportement des clients et événements utilisateurs
layout: customer_behavior_events_glossary
page_order: 4
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents comportement des clients et événements utilisateur que Braze peut suivre et envoyer via Currents à des entrepôts de données désignés."
tool: Currents
search_rank: 7
---

Contactez votre conseiller Braze ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires. Si vous ne trouvez pas ce dont vous avez besoin dans cet article, consultez notre [bibliothèque des événements d’engagement lié aux messages]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/) ou nos [exemples d’échantillons de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication du comportement des clients et de la structure des événements personnalisés et des valeurs de la plateforme %}

### Structure d’événement

Cette ventilation des comportement des clients et des événements utilisateur montre le type d’informations généralement incluses dans un comportement des clients ou événement utilisateur. Avec une bonne compréhension de ses composants, vos développeurs et votre équipe BI peuvent utiliser les données d’événements Currents entrants pour créer des rapports et des graphiques axés sur les données, et tirer parti des précieux indicateurs de données fournis.

![Ventilation d'un événement utilisateur montrant un événement d'achat avec les propriétés énumérées regroupées par propriétés spécifiques à l'utilisateur, propriétés spécifiques au comportement et propriétés spécifiques à l'appareil]({% image_buster /assets/img/customer_engagement_event.png %})

Le comportement des clients et les événements personnalisés se composent de propriétés **propres à l'utilisateur**, de propriétés **propres au comportement** et de propriétés **propres à l'appareil**.

### Valeurs de la plateforme

Certains événements renvoient une valeur `platform` qui spécifie la plate-forme de l’appareil de l’utilisateur.
<br>Le tableau suivant détaille les valeurs retournées possibles :

| Appareil de l’utilisateur | Valeur de la plateforme |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Web | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Les schémas de stockage s'appliquent aux données d'événements sous forme de fichiers plats que nous envoyons à des partenaires de stockage d'entrepôt de données (tels que Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage). Certaines combinaisons d'événements et de destinations énumérées ici ne sont pas encore disponibles. Pour savoir quels événements sont pris en charge par différents partenaires, consultez notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) et consultez leurs pages respectives.<br><br>En outre, notez que Currents abandonnera les événements dont la charge utile est excessivement importante (plus de 900 Ko).
{% endalert %}