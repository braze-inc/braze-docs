---
nav_title: Alertes de campagne
article_title: Alertes de campagne
page_order: 3
page_type: Référence
description: "Cet article de référence donne un aperçu des alertes de campagne, leurs avantages, ainsi que la façon de les mettre en place pour vous procurer la tranquillité d'esprit."
tool: Campagnes
channel:
  - Email
  - webhooks
---

# Alertes de campagne

> Cet article de référence donne un aperçu des alertes de campagne, leurs avantages, ainsi que la façon de les mettre en place pour vous procurer la tranquillité d'esprit.

## Aperçu

Nous voulons vous avertir lorsque quelque chose ne semble pas tout à fait attendu et vous donner la tranquillité d’esprit que le navire navigue en douceur. Les alertes sur les seuils de campagne procurent une tranquillité d'esprit — soyez les premiers à savoir si une campagne importante envoie plus ou moins de messages que vous ne vous y attendez.

Des alertes de campagne sont disponibles pour les campagnes suivantes :

- Campagnes planifiées récurrentes
- Campagnes basées sur l'action
- Campagnes déclenchées par l'API

## Paramétrage de l'alerte de votre campagne

Accédez à la page Analytics de votre campagne pour commencer à configurer votre alerte. Lorsque vous appuyez sur "Configurer l'alerte", vous serez en mesure de spécifier des seuils d'alerte supérieurs et inférieurs ainsi que les destinataires et les canaux.

Pour une campagne récurrente planifiée, vous pouvez définir des seuils supérieurs et inférieurs pour les messages envoyés chaque fois que la campagne envoie. Pour une campagne déclenchée, vous pouvez définir des seuils supérieurs et inférieurs pour le nombre de messages envoyés par heure et par jour.

Vous pouvez configurer une alerte par courriel, une alerte par webhook ou les deux. Les alertes Webhook peuvent être très utiles, car elles vous permettent d'envoyer une alerte à un canal Slack. Pour plus d'informations sur l'intégration des alertes de campagne avec Slack, consultez notre [documentation][1].

!\[Mise en place de l'alerte de campagne\]\[2\]

## Charge utile sur le webhook d'alerte de campagne

Ce qui suit est un exemple de charge utile pour le corps d'un webhook d'alerte de campagne. Cet exemple utilise une alerte qui est configurée pour envoyer quand les messages envoyés tombent en dessous de 500 pour l'envoi d'une campagne donnée.

```
{"text":"Votre campagne "Exemple de campagne" avait moins de 500 messages envoyés cette exécution. Il avait 4 messages envoyés cette exécution. Voir https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample App Group",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```
[2]: {% image_buster /assets/img_archive/campaign_alerts.png %}


[1]: {{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration
