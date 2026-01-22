---
nav_title: Événements d’engagement par message
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Ce glossaire répertorie les différents comportements client et événements utilisateur que Braze peut suivre et envoyer via Currents à des entrepôts de données désignés."
tool: Currents
search_rank: 6
---

Les schémas de stockage s'appliquent aux données d'événements sous forme de fichiers plats que nous envoyons aux partenaires de stockage de l'entrepôt de données (Google Cloud Storage, Amazon S3 et Microsoft Azure Blob Storage). Pour les schémas qui s'appliquent aux autres partenaires, reportez-vous à notre liste de [partenaires disponibles]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) et consultez leurs pages respectives.

Contactez votre gestionnaire de compte ou ouvrez un [ticket d'assistance]({{site.baseurl}}/braze_support/) si vous avez besoin d'accéder à des droits d'événements supplémentaires. Si vous ne trouvez pas ce dont vous avez besoin dans cet article, consultez notre [bibliothèque d'événements de comportement client]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) ou nos [exemples de données Currents](https://github.com/Appboy/currents-examples/tree/master/sample-data).

{% details Explication de la structure de l'événement d'engagement lié aux messages et des valeurs de la plateforme %}

### Structure d’événement

Cette ventilation des événements montre le type d’information généralement inclus dans un événement d’engagement de message. Avec une bonne compréhension de ses composants, vos développeurs et votre équipe BI peuvent utiliser les données d’événements Currents entrants pour créer des rapports et des graphiques axés sur les données, et tirer parti des précieux indicateurs de données fournis.

![Décomposition d'un événement d'engagement de message montrant un événement de désinscription d'un e-mail avec les propriétés énumérées regroupées par propriétés spécifiques à l'utilisateur, propriétés de suivi de campagne ou de Canvas, et propriétés spécifiques à l'événement]({% image_buster /assets/img/message_engagement_event.png %}).

Les événements d'engagement aux messages se composent de propriétés **propres à l'utilisateur**, de propriétés de **suivi de la campagne/du canevas** et de propriétés **propres à l'événement**.

### Schéma d'ID utilisateur

Notez les conventions d'appellation pour les ID d'utilisateurs.

| Schéma de Braze | Schéma actuel | Description |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | L'identifiant unique attribué automatiquement par Braze. |
| `external_id` | `"EXTERNAL_USER_ID"` | Identifiant unique du profil d'un utilisateur défini par le client. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

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
Currents abandonnera les événements dont la charge utile est excessivement importante (plus de 900 Ko).
{% endalert %}

{% alert note %}
Les objets liés aux flux de canevas ont des ID qui peuvent être utilisés pour le regroupement et traduits en noms lisibles par l'utilisateur grâce à l'[endpoint Export Canvas details (Exporter les détails du canevas]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)).
{% endalert %}

{% alert note %}
Certains champs peuvent prendre plus de temps pour afficher leur état le plus récent après la mise à jour d'une campagne ou d'un canvas. Ces champs sont les suivants :
<ul>
  <li>"nom_de_la_campagne"</li>
  <li>"nom_de_la_toile"</li>
  <li>"nom_de_l'étape_de_la_toile"</li>
  <li>"conversion_behavior"</li>
  <li>"nom_de_la_variation_de_la_toile"</li>
  <li>"nom_de_l'expérience"</li>
  <li>"nom_du_message"</li>
</ul>
Si une cohérence totale est requise, nous vous recommandons d'attendre une heure après la dernière mise à jour de ces champs avant d'envoyer vos messages à vos utilisateurs.
{% endalert %}