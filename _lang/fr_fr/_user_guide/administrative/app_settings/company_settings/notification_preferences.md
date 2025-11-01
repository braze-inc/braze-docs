---
nav_title: Préférences de notification
article_title: Préférences de notification
page_order: 1
page_type: reference
description: "Cet article de référence présente les options dont vous disposez pour surveiller les messages et l'activité de votre compte d'entreprise."

---

# Préférences de notification

> Si vous souhaitez surveiller l'envoi de messages et l'activité de votre compte d'entreprise, vous pouvez choisir de configurer des notifications spécifiques et de sélectionner leur destination.

La page **Préférences de notification** vous permet de déterminer qui (si quelqu'un) reçoit des notifications concernant votre entreprise. Vous pouvez configurer les personnes qui doivent recevoir des notifications concernant la réception/distribution des campagnes ou les erreurs techniques. Vous pouvez également spécifier des destinataires pour le rapport d'analyse/analytique hebdomadaire. Pour la plupart des notifications, Braze prend en charge les canaux e-mail et webhook.

!page des préférences de notification dans le tableau de bord de Braze]({% image_buster /assets/img_archive/notification_preferences.png %})

Pour accéder à cette page, allez dans **Réglages** > **Réglages administratifs** > **Préférences de notification.**

## Notifications disponibles

Le tableau suivant décrit les notifications disponibles et les canaux utilisés pour les transmettre.

| Notification | Description | Canaux de notification disponibles |
|--------------|-------------|-----------------|
| Erreurs d'identification AWS | Notifie les destinataires lorsque Braze reçoit une erreur lors d'une tentative d'utilisation de vos identifiants Amazon Web Services pour une exportation de données. Il s'agit notamment des notifications d'erreurs d'identification pour Google Cloud Services et Azure (Microsoft Cloud Services). | E-mail, webhook |
| Arrêt automatique de la campagne | Informe les destinataires de l'arrêt d'une campagne par Braze. | e-mail |
| Expiration de l'interaction de la campagne | Notifie aux destinataires toute campagne dont les données d'interaction arrivent à expiration, ainsi que toute information sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | e-mail |
| Campagne/Canvas mis à jour | Notifie les destinataires lorsqu'une campagne ou un Canvas actif est mis à jour ou désactivé, ainsi que lorsqu'une campagne ou un Canvas inactif est réactivé ou que des brouillons sont lancés. | e-mail |
| Limite de volume de la campagne/du canvas atteinte | Notifie les destinataires lorsqu'une campagne ou un canvas atteint sa limite de volume. | e-mail | 
| Expiration de l'interaction Canvas | Notifie aux destinataires tout Canvas dont les données d'interaction avec le Canvas doivent expirer, ainsi que toute information sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | e-mail |
| Erreurs d'authentification par poussée | Notifie les destinataires lorsque les informations d'identification push d'une application ne sont pas valides et lorsque les informations d'identification push d'une application expirent bientôt. | E-mail, webhook |
| Campagne planifiée envoyée/non envoyée | Notifie les destinataires lorsque les campagnes planifiées commencent à être envoyées ou lorsque les campagnes planifiées tentent d'être envoyées mais n'ont pas d'utilisateurs éligibles à qui envoyer. | E-mail, webhook |
| Limite de la campagne planifiée atteinte | Notifie les destinataires lorsque la limite d'une campagne planifiée récurrente a été atteinte. | E-mail, webhook |
| Campagne planifiée Envoi terminé | Notifie les destinataires lorsque l'envoi d'une campagne planifiée est terminé. | E-mail, webhook |
| Rapport d'analyse/analytique hebdomadaire (si utilisé asjectivement) | Envoie chaque lundi aux destinataires un résumé de l'activité de l'espace de travail de la semaine écoulée. Les destinataires reçoivent un résumé pour chaque espace de travail auquel ils appartiennent. | e-mail |
| Limites quotidiennes du volume d'entrées dans les canvas/campagnes | Envoie des notifications chaque fois qu'une limite d'envoi est atteinte. | e-mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Rapports d'analyse/analytique hebdomadaires (si utilisés asjectivement)

En option, Braze envoie un rapport hebdomadaire par e-mail aux personnes que vous avez désignées au sein de votre entreprise, tous les lundis à 5 heures du matin (heure de l'Est). Vous pouvez sélectionner les événements personnalisés à inclure dans le rapport hebdomadaire à partir de **Paramètres des données** > Événements personnalisés.

Vous pouvez sélectionner jusqu'à cinq événements à inclure dans votre rapport hebdomadaire :

Sélection des événements à inclure dans le rapport d'analyse/analytique (si utilisé dans le rapport d'analyse)]({% image_buster /assets/img_archive/company_analytics_report_new.png %})

## Intégration des webhooks entrants de Slack

Slack dispose d'une [application webhook entrante](https://my.slack.com/services/new/incoming-webhook/) qui permet d'envoyer des messages depuis des sources externes dans Slack. Pour commencer, ouvrez l'application webhook entrant.

1. Sélectionnez le canal Slack sur lequel vous souhaitez que les notifications soient envoyées, puis cliquez sur **Ajouter l'intégration des webhooks entrants**.<br><br>
    !Ajouter l'intégration des webhooks entrants dans Slack]({% image_buster /assets/img_archive/slack_f.png %})<br><br>
  Slack générera une URL que vous devrez entrer dans Braze pour les notifications que vous souhaitez recevoir.<br><br>
2. Copiez l'**URL du webhook**.<br><br>
    Copier l'URL du webhook]({% image_buster /assets/img_archive/copy_url.png %})<br><br>
3. Accédez à l'onglet **Préférences de notification** dans les **Paramètres de l'entreprise**.<br><br>
4. Sélectionnez la notification que vous souhaitez activer pour Slack. Ou, si vous avez plusieurs notifications que vous souhaitez envoyer à ce canal Slack, utilisez **Bulk Add** pour ajouter le webhook à plusieurs notifications.<br><br>
    \![Sélectionnez les notifications Slack à activer]({% image_buster /assets/img_archive/click_edit_f.png %}){: style="max-width:60%;"}<br><br>
5. Saisissez l'URL que Slack a généré pour vous.

C'est tout ! Vous devriez commencer à recevoir des notifications concernant votre entreprise sur ce canal Slack. Vous pouvez également consulter l'article d'aide de Slack sur ce sujet : [Envoi de messages à l'aide de webhooks entrants](https://api.slack.com/incoming-webhooks).

