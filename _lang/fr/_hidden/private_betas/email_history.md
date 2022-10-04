---
nav_title: FAQ sur l’onglet Historique des e-mails
permalink: "/email_history/"
hidden: true
---

# FAQ sur l’onglet Historique des e-mails

## Qu’est-ce que l’onglet Historique des e-mails ?

L’onglet **Historique des e-mails** du profil utilisateur vous permet de voir les événements e-mail récents (environ 40) pour d’un seul utilisateur au cours des 30 derniers jours.

{% alert important %}
L’onglet **Historique des e-mails** est une fonction expérimentale déployée uniquement pour sélectionner des clients.
{% endalert %}

## Quels événements sont inclus dans le tableau ?

Le tableau affiche les événements d’e-mail suivants :

- [Rebond]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-bounce-event)
- [Clic]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-clicks-events)
- [Livraison]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-delivery-events)
- [Marqué comme spam]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-spam-events)
- [Ouvrir]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-open-events)
- [Envoyer]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-send-events)
- [Rebond léger]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-soft-bounce-event)
- [Se désabonner]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events#email-unsubscribe-events)

## L’événement ouvert est-il fiable ?

Le suivi de l'ouverture d’e-mails est sujet à des erreurs, quel que soit l'outil utilisé, y compris Braze. Grâce à une variété de fonctions de protection de la vie privée offertes par différents clients de messagerie qui bloquent le chargement automatique des images ou les chargent de manière proactive sur le serveur, les événements d'ouverture des e-mails sont susceptibles d'entraîner à la fois des faux positifs et des faux négatifs. 

Si les statistiques d'ouverture des e-mails peuvent être utiles dans leur ensemble, par exemple pour comparer l'efficacité de différentes lignes d'objet, vous ne devez pas supposer qu'un événement d'ouverture individuel pour un utilisateur individuel est significatif.

## Est-ce que je peux voir d’autres événements dans ce tableau ?

Si vous avez des commentaires sur ce tableau, ou si vous souhaitez consulter des événements spécifiques, n’hésitez pas à nous en faire part. Envoyez un e-mail avec vos commentaires à [smb-product@braze.com](mailto:smb-product@braze.com?subject=Email%20History%20Tab%20Feedback) ayant pour ligne d’objet "Email History Tab Feedback".
