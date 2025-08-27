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

# Journalisation des propriétés d'événement personnalisé

Il y a trois vérifications importantes à faire pour vous assurer que vos événements personnalisés sont enregistrés comme vous le souhaitez :

* [Déterminer les événements qui sont enregistrés](#verify-events)
* [Vérifier le journal](#verify-log)
* [Vérifier les valeurs](#verify-values)

## Propriétés d’événement personnalisé

Les [propriétés d'événement personnalisé]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) sont des métadonnées qui décrivent les événements personnalisés. Plusieurs propriétés peuvent être consignées chaque fois qu’un événement personnalisé est journalisé.

### Vérifier les événements

Vérifiez auprès de vos développeurs quelles propriétés d’événement sont suivies. Gardez à l’esprit que toutes les propriétés de l'événement sont sensibles à la casse. Pour plus d'informations sur le suivi des événements personnalisés, consultez ces articles en fonction de votre plateforme :

* [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/)
* [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/)
* [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/tracking_custom_events/)

### Vérifier le journal

Pour confirmer que les propriétés de l'événement sont bien suivies, vous pouvez afficher toutes les propriétés de l'événement à partir de la page **Événements personnalisés**.

1. Naviguer vers **Paramètres des données** > **Événements personnalisés**.
2. Emplacement/localisation de votre événement personnalisé dans la liste.
3. Pour votre événement, cliquez sur **Gestion des propriétés**. Cela vous indiquera les noms des propriétés associées à un événement.

### Vérifier les valeurs

Après avoir ajouté votre utilisateur en tant qu'utilisateur test, suivez les étapes suivantes pour vérifier vos valeurs : 

1. Exécutez l'événement personnalisé dans l'application.
2. Attendez environ 10 secondes pour que les données se déversent.
3. Actualisez le [journal des événements utilisateurs]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) pour afficher l'événement personnalisé et la valeur de la propriété d'événement qui lui a été transmise.

Vous avez toujours besoin d’aide ? Ouvrez un [ticket de support]({{site.baseurl}}/braze_support/).

_Dernière mise à jour le 10 avril 2023_

