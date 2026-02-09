---
nav_title: Préférences de notification
article_title: Préférences de notification
page_order: 1
page_type: reference
description: "Cet article de référence couvre les options disponibles pour surveiller l’envoi de messages et l’activité dans votre compte d’entreprise."

---

# Préférences de notification

> Si vous souhaitez surveiller l’envoi de messages et l’activité dans votre compte d’entreprise, vous pouvez choisir de configurer des notifications spécifiques et de sélectionner où elles se trouvent.

La page **Préférences de notification** vous permet de déterminer qui (si quelqu'un) reçoit des notifications concernant votre entreprise. Vous pouvez configurer les personnes qui doivent recevoir des notifications concernant la réception/distribution des campagnes ou les erreurs techniques. Vous pouvez également spécifier les destinataires du rapport d’analyse hebdomadaire. Pour la plupart des notifications, Braze prend en charge les canaux d’e-mail et de connexion Webhook.

![Page Notification Preferences (Préférences de notification) dans le tableau de bord de Braze]({% image_buster /assets/img_archive/notification_preferences.png %})

Pour accéder à cette page, allez dans **Réglages** > **Réglages administratifs** > **Préférences de notification.**

{% alert tip %}
Vous pouvez également vous intégrer à Slack pour recevoir des notifications. Pour connaître la marche à suivre, reportez-vous à la section [Envoi de messages à l'aide de webhooks entrants](https://api.slack.com/incoming-webhooks).
{% endalert %}

## Notifications disponibles

Le tableau suivant décrit les notifications disponibles et les canaux utilisés pour les transmettre.

| Notification | Description | Canaux de notification disponibles |
|--------------|-------------|-----------------|
| Erreurs d’identification AWS | Informe le destinataire lorsque Braze reçoit une erreur lors de la tentative d'utilisation de vos identifiants Amazon Web Services pour une exportation de données. Il s'agit notamment des notifications d'erreurs d'identification pour Google Cloud Services et Azure (Microsoft Cloud Services). | E-mail, Webhook |
| Campagne arrêtée automatiquement | Avertit les destinataires lorsque Braze a arrêté une campagne. | E-mail |
| Expiration de l’interaction avec la campagne | Informe les destinataires d’une campagne dont l’expiration des données d’interaction de campagne est prévue, ainsi que de toute information pertinente sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | E-mail |
| Campagne/Canvas mis(e) à jour | Notifie les destinataires lorsqu'une campagne ou un Canvas actif est mis à jour ou désactivé, ainsi que lorsqu'une campagne ou un Canvas inactif est réactivé ou que des brouillons sont lancés. | E-mail |
| Limite de volume de la campagne/du canvas atteinte | Notifie les destinataires lorsqu'une campagne ou un canvas atteint sa limite de volume. | E-mail | 
| Expiration de l’interaction avec le canvas | Informe les destinataires d’un Canvas dont l’expiration des données d’interaction de Canvas est prévue, ainsi que de toute information pertinente sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | E-mail |
| Erreurs d’identification de notification push | Avertit les destinataires lorsque les notifications push d’identification de l’application sont invalides et lorsqu’elles sont bientôt expirées. | E-mail, Webhook |
| Campagne planifiée envoyée/non envoyée | Notifie les destinataires lorsque les campagnes planifiées commencent à être envoyées ou lorsque les campagnes planifiées tentent d'être envoyées mais n'ont pas d'utilisateurs éligibles à qui envoyer. | E-mail, Webhook |
| Limite de campagne planifiée atteinte | Informe les destinataires lorsque la limite d’une campagne planifiée récurrente a été atteinte. | E-mail, Webhook |
| Envoi terminé d’une campagne planifiée | Informe les destinataires lorsque l’envoi d’une campagne planifiée est terminé. | E-mail, Webhook |
| Rapport hebdomadaire d’analyse | Envoie chaque lundi aux destinataires un résumé de l'activité de l'espace de travail de la semaine écoulée. Les destinataires reçoivent un résumé pour chaque espace de travail auquel ils appartiennent. | E-mail |
| Limites quotidiennes du volume d'entrées dans les canvas/campagnes | Envoie des notifications chaque fois qu'une limite d'envoi est atteinte. | E-mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Rapports hebdomadaires d’analyse

Braze propose l’option d’envoi d’un rapport hebdomadaire par e-mail aux personnes que vous désignez dans votre entreprise tous les lundis à 5 h EST. Vous pouvez sélectionner les événements personnalisés à inclure dans le rapport hebdomadaire à partir de **Paramètres des données** > **Événements personnalisés**.

Vous pouvez sélectionner jusqu’à cinq événements à inclure dans votre rapport hebdomadaire :

![Sélection des événements à inclure dans le rapport d’analyse]({% image_buster /assets/img_archive/company_analytics_report_new.png %})
