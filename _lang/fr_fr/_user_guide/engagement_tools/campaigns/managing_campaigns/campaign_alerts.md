---
nav_title: Alertes de campagne
article_title: Alertes de campagne
page_order: 6

page_type: reference
description: "Cet article de référence donne un aperçu des alertes de campagne, de leurs avantages et de la manière de les implémenter pour vous aider à garder l'esprit tranquille."
tool: Campaigns
channel:
- email
- webhooks

---

# Alertes de campagne

> Nous voulons vous alerter lorsque quelque chose ne semble pas correspondre à ce que vous attendiez et vous donner la tranquillité d'esprit de savoir que le navire navigue sans encombre. Les alertes de seuil de campagne vous permettent d'avoir l'esprit tranquille : soyez le premier à savoir si une campagne importante envoie plus ou moins de messages que prévu.

Les alertes de campagne sont disponibles pour les campagnes suivantes :

- Campagnes planifiées récurrentes
- Campagnes basées sur l'action
- Campagnes déclenchées par l'API

## Implémenter des campagnes d'alerte

Accédez à la page d'analyse/analytique de votre campagne pour commencer à implémenter votre alerte. Lorsque vous sélectionnez **Configurer une alerte**, vous pouvez spécifier les seuils d'alerte supérieurs et inférieurs ainsi que les destinataires et les canaux d'alerte.

!Boîte de dialogue de suivi de campagne avec deux boutons : Annuler et Enregistrer.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Pour une campagne récurrente planifiée, vous pouvez définir des seuils supérieurs et inférieurs pour les messages envoyés à chaque fois que la campagne est envoyée. Pour une campagne déclenchée, vous pouvez définir des seuils supérieurs et inférieurs pour le nombre de messages envoyés par heure et par jour.

Vous pouvez configurer une alerte par e-mail, une alerte par webhook ou les deux. Les alertes webhook peuvent être très utiles, car elles vous permettent d'envoyer une alerte à un canal Slack. Pour plus d'informations sur l'intégration des alertes de campagne avec Slack, consultez notre [documentation]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration).

{% alert note %}
Lorsque vous définissez des alertes pour des campagnes futures, vous pouvez recevoir des mises à jour avant le début de la campagne et après sa fin. En effet, les alertes de la campagne continueront à être envoyées jusqu'à ce que la campagne soit arrêtée manuellement.
{% endalert %}

## Charge utile du webhook d'alerte de campagne

Vous trouverez ci-dessous un exemple de charge utile pour le corps d'un webhook d'alerte de campagne. Cet exemple utilise une alerte configurée pour être envoyée lorsque le nombre d'envois de messages est inférieur à 500 pour une campagne donnée.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

