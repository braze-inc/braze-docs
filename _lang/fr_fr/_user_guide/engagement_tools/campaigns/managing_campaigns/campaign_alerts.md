---
nav_title: Alertes de campagne
article_title: Alertes de campagne
page_order: 6

page_type: reference
description: "Le présent article de référence donne un aperçu des alertes de campagne, de leurs avantages, ainsi que de la manière de les configurer pour vous fournir une tranquillité d’esprit."
tool: Campaigns
channel:
- email
- webhooks

---

# Alertes de campagne

> Nous voulons vous alerter lorsque quelque chose ne semble pas se passer comme prévu et vous tranquilliser sur le fait que tout va bien. Le seuil d’alertes de campagne fournit une tranquillité d’esprit. Soyez le premier à savoir si une campagne importante envoie plus ou moins de messages que ce à quoi vous vous attendiez.

Les alertes de campagne sont disponibles pour les campagnes suivantes :

- Campagnes planifiées récurrentes
- Campagnes basées sur des actions
- Campagnes déclenchées par API

## Configurer votre alerte de campagne

Accédez à la page d’analytique de votre campagne pour commencer à configurer votre alerte. Lorsque vous sélectionnez **Configurer l'alerte**, vous pourrez spécifier les seuils d'alerte supérieurs et inférieurs ainsi que les destinataires et les canaux d'alerte.

![Boîte de dialogue « Surveillance de la campagne » avec deux boutons : Annuler et enregistrer.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Pour une campagne récurrente planifiée, vous pouvez définir des seuils supérieurs et inférieurs pour les messages envoyés chaque fois que la campagne envoie. Pour une campagne déclenchée, vous pouvez définir des seuils supérieurs et inférieurs pour le nombre de messages envoyés par heure et par jour.

Vous pouvez configurer une alerte par e-mail, webhook ou les deux. Les alertes webhook peuvent être très utiles, car elles vous permettent d’envoyer une alerte à un canal Slack. Pour plus d'informations sur l'intégration des alertes de campagne avec Slack, consultez notre [documentation]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration).

{% alert note %}
Lorsque vous définissez des alertes de campagne pour de futures campagnes, vous pouvez recevoir des mises à jour avant le début et après la fin de la campagne. C’est pourquoi, les alertes de campagne continueront à être envoyées jusqu’à ce que la campagne ait été arrêtée manuellement.
{% endalert %}

## Charge utile du webhook de l’alerte de campagne

Voici un exemple de charge utile pour le corps d’un webhook d’alerte de campagne. Cet exemple utilise une alerte configurée pour être envoyée lorsque les messages envoyés passent sous 500 pour une campagne donnée.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

