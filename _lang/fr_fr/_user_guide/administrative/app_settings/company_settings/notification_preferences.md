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

![Page Notification Preferences (Préférences de notification) dans le tableau de bord de Braze][61]

Pour accéder à cette page, allez dans **Réglages** > **Réglages administratifs** > **Préférences de notification.**

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), sélectionnez le menu déroulant de votre compte et allez dans **Paramètres de l'entreprise** > **Préférences de notification.**
{% endalert %}

## Notifications disponibles

Le tableau suivant répertorie les notifications disponibles :

| Notification | Description | Canaux de notification disponibles |
|--------------|-------------|-----------------|
| Erreurs d’identification AWS | Informe le destinataire lorsque Braze reçoit une erreur lors de la tentative d'utilisation de vos identifiants Amazon Web Services pour une exportation de données. | E-mail, Webhook |
| Campagne arrêtée automatiquement | Avertit les destinataires lorsque Braze a arrêté une campagne. | E-mail |
| Expiration de l’interaction avec la campagne | Informe les destinataires d’une campagne dont l’expiration des données d’interaction de campagne est prévue, ainsi que de toute information pertinente sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | E-mail |
| Campagne/Canvas mis(e) à jour | Informe les destinataires lorsqu’une campagne/un canvas actif(ve) est mis(e) à jour ou désactivé(e), ainsi qu’une campagne/un canvas inactif(ve) est réactivé(e) ou lorsque des projets sont lancés. | E-mail |
| Expiration de l’interaction avec le canvas | Informe les destinataires d’un Canvas dont l’expiration des données d’interaction de Canvas est prévue, ainsi que de toute information pertinente sur les segments, campagnes ou Canvas qui y font référence dans un filtre de reciblage et qui ont été utilisés pour envoyer un message au cours des 30 jours précédents. | E-mail |
| Carte de fil d’actualités publiée/en direct | Informe les destinataires lorsque les cartes de fil d’actualités sont programmées ou publiées. | E-mail, Webhook |
| Erreurs d’identification de notification push | Avertit les destinataires lorsque les notifications push d’identification de l’application sont invalides et lorsqu’elles sont bientôt expirées. | E-mail, Webhook |
| Campagne planifiée envoyée/non envoyée | Informe les destinataires lorsque les campagnes planifiées commencent à être envoyées ou lorsque des tentatives d’envoi sont effectuées, mais qu’aucun utilisateur éligible n’a été trouvé. | E-mail, Webhook |
| Limite de campagne planifiée atteinte | Informe les destinataires lorsque la limite d’une campagne planifiée récurrente a été atteinte. | E-mail, Webhook |
| Envoi terminé d’une campagne planifiée | Informe les destinataires lorsque l’envoi d’une campagne planifiée est terminé. | E-mail, Webhook |
| Rapport hebdomadaire d’analyse | Envoie chaque lundi aux destinataires un résumé de l'activité de l'espace de travail de la semaine écoulée. Les destinataires reçoivent un résumé pour chaque espace de travail auquel ils appartiennent. | E-mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Rapports hebdomadaires d’analyse

Braze propose l’option d’envoi d’un rapport hebdomadaire par e-mail aux personnes que vous désignez dans votre entreprise tous les lundis à 5 h EST. Vous pouvez sélectionner les événements personnalisés à inclure dans le rapport hebdomadaire à partir de **Paramètres des données** > **Événements personnalisés**.

{% alert note %}
Si vous utilisez l'[ancienne version de la navigation]({{site.baseurl}}/navigation), cette page est située sous **Gérer les paramètres** > **Événements personnalisés**.
{% endalert %}

Vous pouvez sélectionner jusqu’à cinq événements à inclure dans votre rapport hebdomadaire :

![Sélection des événements à inclure dans le rapport d’analyse][22]

## Intégration du Webhook entrant pour Slack

Slack dispose d'une [application de webhook entrant][67] qui permet de publier des messages dans Slack à partir de sources externes. Pour commencer, ouvrez le Webhook entrant de l’application.

1. Sélectionnez le canal Slack sur lequel vous souhaitez que les notifications soient envoyées, puis cliquez sur **Ajouter l'intégration des webhooks entrants**.<br><br>
    ![Ajouter l’intégration des Webhook entrants dans Slack][63]<br><br>
  Slack génère une URL que vous devrez saisir dans Braze pour les notifications que vous souhaitez recevoir.<br><br>
2. Copiez l'**URL du webhook.**<br><br>
    ![Copier l’URL du Webhook][64]<br><br>
3. Accédez à l'onglet **Préférences de notification** dans les **Paramètres de l'entreprise**.<br><br>
4. Sélectionnez la notification que vous souhaitez activer pour Slack. Ou, si vous avez plusieurs notifications à envoyer à ce canal Slack, utilisez **Ajout groupé** pour ajouter le webhook à plusieurs notifications.<br><br>
    ![Sélectionnez les notifications Slack à activer][65]{: style="max-width:60%;"}<br><br>
5. Saisissez l’URL que Slack a générée pour vous.

Et voilà ! Vous devez commencer à recevoir des notifications concernant votre entreprise dans ce canal Slack. Vous pouvez également consulter l'article d'aide de Slack sur ce sujet : [Envoi de messages à l'aide de webhooks entrants][62].


[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.png %}
Il y a [67]: https://my.slack.com/services/new/incoming-webhook/
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
Il y a [62]: https://api.slack.com/incoming-webhooks