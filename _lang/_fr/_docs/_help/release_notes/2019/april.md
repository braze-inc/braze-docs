---
nav_title: Avril
page_order: 9
noindex: vrai
page_type: Mettre à jour
description: "Cet article contient des notes de publication pour avril 2019."
---

# Avril 2019

## Nouveaux événements & champs en cours

En plus de quelques corrections à la section, un nouvel [événement d'abonnement]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#subscription-events) a été ajouté à la page Événements d'engagement de messages. Vous pouvez maintenant exporter les données du changement d'état du groupe d'abonnement de Braze vers le segment []({{ site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment_for_currents/#integration-details) et [mParticule]({{ site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/mParticle/mparticle_for_currents/), ainsi que cela et Installer les événements d'attribution dans [Mixpanel]({{ site.baseurl}}/partners/insights/behavioral_analytics/mixpanel_for_currents).

De plus, la propriété `canvas_step_id` a été ajoutée à [Événements de conversion]({{ site.baseurl}}/user_guide/data_and_analytics/braze_currents/message_engagement_events/#conversion-events) disponibles.

{% alert important %}
Pour profiter de ces mises à jour, vous devrez modifier les paramètres de votre connecteur courant et activer les événements que vous souhaitez utiliser. Contactez votre responsable de compte si vous avez des questions.
{% endalert %}

## Archivage des groupes d'abonnement

Vous pouvez maintenant [archiver les Groupes d'abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/#archiving-groups)! Les Groupes d'Abonnement Archivés ne peuvent pas être modifiés et n'apparaîtront plus dans les Filtres de Segment.  Si vous essayez d'archiver un groupe qui est utilisé comme filtre de segment dans n'importe quel courriel, campagne ou canvas, vous recevrez un message d'erreur qui vous empêchera d'archiver le Groupe jusqu'à ce que vous supprimiez toutes les utilisations de celui-ci.
