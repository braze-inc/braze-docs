---
nav_title: Logging des propriétés personnalisées de l'événement
article_title: Logging des propriétés personnalisées de l'événement
page_order: 3
page_type: Solution
description: "Cet article d'aide vous guide à travers trois vérifications importantes pour vous assurer que vos événements personnalisés sont enregistrés comme vous le souhaitez."
tool:
  - Campagnes
  - Toile
---

# Logging des propriétés d'événement personnalisées

Il y a trois contrôles importants à effectuer pour vous assurer que vos événements personnalisés sont enregistrés comme vous vous y attendez:

* [Établir quels événements sont enregistrés](#which-events)
* [Vérifier le journal](#verify-log)
* [Vérifier les valeurs](#verify-values)

## Propriétés personnalisées de l'événement

[Les propriétés d'événements personnalisés][22] sont des métadonnées qui décrivent les événements personnalisés. Plusieurs propriétés peuvent être enregistrées chaque fois qu'un événement personnalisé est enregistré.

## Vérifier les propriétés de l'événement personnalisé

### Vérifier les événements

Vérifiez avec vos développeurs quelles sont les propriétés d'événement à suivre. Gardez à l'esprit que toutes les propriétés de l'événement sont sensibles à la casse.

Pour plus d'informations, voir :

* [Android][51]
* [iOS][23]
* [Web][52]


### Vérifier le journal

Pour confirmer que les propriétés de l'événement sont suivies avec succès, vous pouvez afficher toutes les propriétés de l'événement en allant à la page **Gérer les paramètres** en cliquant sur l'onglet **Événements personnalisés** puis en cliquant sur **Gérer les Propriétés**. Cela vous montrera le nom de toutes les propriétés associées à un événement.

### Vérifier les valeurs

Pour vérifier les valeurs de propriétés spécifiques qui sont passées pour chaque événement, vérifiez les [Logs de l'utilisateur événement][24] sur votre tableau de bord. Après avoir ajouté votre utilisateur en tant qu'utilisateur de test, vous devriez effectuer l'événement personnalisé dans l'application, attendez environ 10 secondes pour que les données soient vides, puis actualisez le journal des utilisateurs d'événements pour afficher l'événement personnalisé et la valeur de la propriété de l'événement qui a été passé avec lui.

Vous avez encore besoin d'aide ? Ouvrez un ticket de support []({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 21 juin 2021_

[22]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/
[24]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
