---
nav_title: Préférences de notification
article_title: Préférences de notification
page_order: 1
page_type: reference
description: "Cet article de référence couvre les options disponibles pour surveiller l'envoi de messages et l'activité dans votre compte d'entreprise."

---

# Préférences de notification

> Si vous souhaitez surveiller l'envoi de messages et l'activité dans votre compte d'entreprise, vous pouvez configurer des notifications spécifiques et choisir où elles sont envoyées.

La page **Préférences de notification** vous permet de déterminer qui (le cas échéant) reçoit des notifications concernant votre entreprise. Vous pouvez définir les personnes qui doivent être informées de la distribution des campagnes ou des erreurs techniques. Vous pouvez également spécifier les destinataires du rapport d'analyse hebdomadaire. Pour la plupart des notifications, Braze prend en charge les canaux e-mail et webhook.

![Page Préférences de notification dans le tableau de bord de Braze]({% image_buster /assets/img_archive/notification_preferences.png %})

Pour accéder à cette page, allez dans **Paramètres** > **Paramètres administratifs** > **Préférences de notification**.

{% alert tip %}
Vous pouvez également intégrer Slack pour recevoir des notifications. Pour connaître la marche à suivre, consultez [Envoi de messages à l'aide de webhooks entrants](https://api.slack.com/incoming-webhooks).
{% endalert %}

## Notifications disponibles

Le tableau suivant décrit les notifications disponibles et les canaux utilisés pour les transmettre.

{% alert note %}
Si vous supprimez la valeur par défaut **Destinataires** de **Tous les utilisateurs du tableau de bord** et souhaitez la rétablir, vous pouvez la saisir manuellement dans le champ déroulant.
{% endalert %}

| Notification | Description | Canaux de notification disponibles |
|--------------|-------------|-----------------|
| Alertes d'utilisation de l'API | Sélectionner cette option vous redirige vers le **tableau de bord d'utilisation de l'API**, où vous pouvez ensuite accéder à l'onglet [**Alertes d'utilisation de l'API**]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_alerts/) et configurer des alertes pour suivre les volumes de requêtes API clés. | E-mail, Webhook |
| Erreurs d'identification AWS | Informe les destinataires lorsque Braze reçoit une erreur en tentant d'utiliser vos identifiants Amazon Web Services pour une exportation de données. Cela inclut les notifications d'erreurs d'identification pour Google Cloud Services et Azure (Microsoft Cloud Services). | E-mail, Webhook |
| Campagne arrêtée automatiquement | Avertit les destinataires lorsque Braze a arrêté une campagne. | E-mail |
| Canvas arrêté automatiquement | Avertit les destinataires lorsque Braze a arrêté un Canvas. | E-mail |
| Expiration de l'interaction avec la campagne | Informe les destinataires lorsqu'une campagne est sur le point d'atteindre l'expiration de ses données d'interaction, ainsi que de toute information pertinente sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | E-mail |
| Campagne/Canvas mis(e) à jour | Notifie les destinataires lorsqu'une campagne ou un Canvas actif est mis à jour ou désactivé, ainsi que lorsqu'une campagne ou un Canvas inactif est réactivé ou que des brouillons sont lancés. | E-mail |
| Limite de volume de la campagne/du Canvas atteinte | Notifie les destinataires lorsqu'une campagne ou un Canvas atteint sa limite de volume. | E-mail | 
| Expiration de l'interaction avec le Canvas | Informe les destinataires lorsqu'un Canvas est sur le point d'atteindre l'expiration de ses données d'interaction, ainsi que de toute information pertinente sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | E-mail |
| Commentaires dans les Canvas | Avertit les destinataires lorsqu'un Canvas contient de nouveaux commentaires. | E-mail |
| Erreurs de contenu connecté | Avertit les destinataires lorsqu'un endpoint de contenu connecté rencontre des erreurs. | E-mail |
| Erreurs de notification push | Avertit les destinataires lorsqu'un endpoint de notification push rencontre des erreurs. | E-mail, Webhook |
| Limite de campagne planifiée atteinte | Informe les destinataires lorsque la limite d'une campagne planifiée récurrente a été atteinte. | E-mail, Webhook |
| Envoi terminé d'une campagne planifiée | Informe les destinataires lorsque l'envoi d'une campagne planifiée est terminé. | E-mail, Webhook |
| Erreurs de webhook | Avertit les destinataires lorsqu'un endpoint de webhook rencontre des erreurs. | E-mail |
| Rapport hebdomadaire d'analyse | Envoie chaque lundi aux destinataires un résumé de l'activité de l'espace de travail de la semaine écoulée. Les destinataires reçoivent un résumé pour chaque espace de travail auquel ils appartiennent. | E-mail |
| Limites quotidiennes du volume d'entrées dans les Canvas/campagnes | Envoie des notifications chaque fois qu'une limite d'envoi est atteinte. | E-mail |
| Erreur de la console d'agents | Avertit les destinataires lorsqu'un [agent de la console d'agents]({{site.baseurl}}/user_guide/brazeai/agents) a atteint sa limite d'exécution avec la fonctionnalité actuelle. | E-mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
Les [utilisateurs suspendus]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/#suspending-company-users) peuvent continuer à recevoir des notifications de Braze.
{% endalert %}

## Rapports hebdomadaires d'analyse

Braze propose l'envoi facultatif d'un rapport hebdomadaire par e-mail aux personnes que vous désignez dans votre entreprise, tous les lundis à 5 h EST. Vous pouvez sélectionner les événements personnalisés à inclure dans le rapport hebdomadaire depuis **Paramètres des données** > **Événements personnalisés**.

Vous pouvez sélectionner jusqu'à cinq événements à inclure dans votre rapport hebdomadaire :

![Sélection des événements à inclure dans le rapport d'analyse]({% image_buster /assets/img_archive/company_analytics_report_new.png %})