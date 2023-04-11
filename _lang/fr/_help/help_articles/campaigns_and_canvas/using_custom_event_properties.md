---
nav_title: Journalisation des Propriétés de l’événement personnalisé
article_title: Journalisation des Propriétés de l’événement personnalisé
page_order: 3
page_type: solution
description: "Cet article d’aide vous guide à travers trois vérifications importantes pour vous assurer que vos événements personnalisés sont enregistrés comme vous le souhaitez."
tool: 
- Campaigns
- Canvas
---

# Journalisation des Propriétés de l’événement personnalisé

Il y a trois vérifications importantes à faire pour vous assurer que vos événements personnalisés sont enregistrés comme vous le souhaitez :

* [Déterminer quels événements sont enregistrés](#verify-events)
* [Vérifier le journal](#verify-log)
* [Vérifier les valeurs](#verify-values)

## Propriétés d’événement personnalisé

Les [Propriétés d’événement personnalisées][22] sont des métadonnées qui décrivent des événements personnalisés. Plusieurs propriétés peuvent être consignées chaque fois qu’un événement personnalisé est journalisé.

### Vérifier les événements

Vérifiez auprès de vos développeurs quelles propriétés d’événement sont suivies. Gardez à l’esprit que toutes les propriétés de l'événement sont sensibles à la casse. Pour plus d’informations sur le suivi des événements personnalisés, consultez les articles suivants pour votre plateforme :

* [Android][51]
* [iOS][23]
* [Web][52]

### Vérifier le journal

Pour confirmer que les propriétés de l’événement sont suivies avec succès, vous pouvez afficher toutes les propriétés d’événement en allant sur l’onglet **Custom Events** (Événements personnalisés) de la page **Manage Settings** (Gérer les paramètres), puis en cliquant sur **Manage Properties** (Gérer les propriétés). Cela vous indiquera les noms des propriétés associées à un événement.

### Vérifier les valeurs

Pour vérifier les valeurs de propriété spécifiques qui sont transmises pour chaque événement, vérifiez le [Journal d’événements utilisateurs][24] sur votre tableau de bord. Après avoir ajouté votre utilisateur en tant qu’utilisateur test, vous devez effectuer l’événement personnalisé dans l’application, attendre environ 10 secondes pour que les données arrivent, puis actualiser le journal des utilisateurs de l’événement pour afficher l’événement personnalisé et la valeur de la propriété d’événement qui a été transmise avec lui.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 16 novembre 2022_

[22]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties
[23]: {{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/
[24]: {{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab
[51]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/ 
[52]: {{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/
