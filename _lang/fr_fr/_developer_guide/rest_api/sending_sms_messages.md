---
nav_title: Envoyer des messages SMS
article_title: "Envoi de messages SMS à l'aide de l'API REST"
page_order: 2
page_type: reference
description: "Cet article de référence explique comment envoyer des messages SMS à l'aide de l'API REST Braze et d'une campagne API."
channel:
  - SMS
---

# Envoi de messages SMS à l'aide de l'API REST

> Veuillez utiliser l'API REST Braze pour envoyer des messages SMS transactionnels depuis votre backend en temps réel. Cette approche vous permet de créer un service qui envoie des SMS de manière programmatique tout en suivant les analyses de réception/distribution parallèlement à vos autres campagnes et canevas dans le tableau de bord de Braze.

Cela peut s'avérer particulièrement utile pour l'envoi de messages transactionnels à haut volume dont le contenu est défini dans vos systèmes backend. Par exemple, vous pouvez informer les consommateurs lorsqu'ils reçoivent un message d'un autre utilisateur, en les invitant à visiter votre site Web et à consulter leur boîte de réception.

Grâce à cette approche, vous pouvez :

- Déclenchez l'envoi de SMS depuis votre backend en temps réel.
- Suivez les analyses parallèlement à toutes vos campagnes marketing et Canvases.
- Élargissez le champ d'application avec des fonctionnalités Braze supplémentaires, telles que les retards de message, le reciblage de suivi et les tests A/B.
- Vous pouvez également opter pour [la distribution déclenchée par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) afin de définir vos modèles de message dans le tableau de bord de Braze tout en continuant à déclencher les envois depuis votre backend.

Pour envoyer un SMS via l'API REST, il est nécessaire de configurer une campagne API dans le tableau de bord de Braze, puis d'utiliser [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)l'endpoint pour envoyer le message.

## Conditions préalables

Pour suivre ce guide, vous aurez besoin de :

| Condition | Description |
| --- | --- |
| Clé d'API REST Braze | Une clé avec l'autorisation`messages.send`. Pour en créer une, veuillez vous rendre dans **Paramètres** > **API et identifiants** > **clés API**. |
| Groupe d'abonnement SMS | Un groupe d'abonnement SMS configuré dans votre espace de travail Braze. |
| Service backend | Un service backend ou un environnement de script capable d'effectuer des requêtes HTTP POST vers l'API REST Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 1 : Créer une campagne API

1. Dans le tableau de bord de Braze, veuillez vous rendre dans **Envoi de messages** > **Campagnes**.
2. Veuillez sélectionner **Créer une campagne**, puis **Campagnes API**.
3. Veuillez saisir un nom et une description pour votre campagne, par exemple « Notification par SMS ».
4. Veuillez ajouter des étiquettes pertinentes pour l'identification et le suivi.
5. Veuillez sélectionner **« Ajouter un canal de communication** », puis choisissez **« SMS** ».
6. Veuillez noter l'**ID** **de la campagne** et **l'ID de la variante du message** affichés sur la page de la campagne. Vous aurez besoin de ces deux valeurs pour créer votre requête API.

## Étape 2 : Envoyer un message SMS à l'aide de l'API

Veuillez créer une requête POST vers [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)l'endpoint. Veuillez inclure l'ID de la campagne, l'ID utilisateur externe du destinataire et le contenu du SMS dans la charge utile de la requête.

{% alert important %}
Chaque destinataire mentionné dans`external_user_ids`  doit déjà exister dans Braze. Les envois via API uniquement ne créent pas de nouveaux profils utilisateurs. Si vous avez besoin de créer des utilisateurs dans le cadre d'un envoi, veuillez utiliser[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)d'abord, ou bien optez pour une [campagne déclenchée par déclencheur d'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

### Exemple de demande

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Veuillez remplacer`YOUR_REST_ENDPOINT`par l'[URL]({{site.baseurl}}/api/basics/#endpoints) [de l'endpoint REST]({{site.baseurl}}/api/basics/#endpoints) de votre espace de travail.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "sms": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_SMS_SUBSCRIPTION_GROUP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "body": "Hi {{${first_name}}}, you have a new message in your inbox. Check it out at https://yourwebsite.com/messages. Text STOP to opt out."
    }
  }
}
```
{% endraw %}

Veuillez remplacer les valeurs de marque substitutive par vos ID réels. Ce`body`champ prend en charge [la personnalisation Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), ce qui vous permet d'adapter le contenu du message à chaque destinataire. Pour obtenir la liste complète des paramètres pris en charge par l'objet d'envoi de messages SMS, veuillez consulter [l'objet SMS]({{site.baseurl}}/api/objects_filters/messaging/sms_object/).

Une fois la requête construite, veuillez envoyer la requête POST depuis votre service backend vers l'API REST Braze.

## Étape 3 : Veuillez vérifier votre intégration.

Une fois la configuration terminée, veuillez vérifier votre intégration :

1. Veuillez envoyer une requête API comme indiqué à [l'étape 2](#step-2-send-an-sms-message-using-the-api), en utilisant votre propre ID utilisateur comme destinataire.
2. Veuillez vérifier que le message SMS a bien été reçu sur votre téléphone.
3. Dans le tableau de bord de Braze, veuillez vous rendre sur la page des résultats de la campagne et vérifier que l'envoi a bien été enregistré.
4. Veuillez surveiller attentivement les résultats à mesure que vous développez votre campagne.

## Considérations

- Veuillez vous assurer que vos campagnes SMS sont conformes aux réglementations applicables et aux exigences des opérateurs. Veuillez inclure les instructions de désabonnement (par exemple, « Envoyez STOP pour vous désabonner ») dans chaque message. Pour plus d'informations, veuillez consulter [les lois et réglementations relatives aux SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) ainsi que [les mots-clés d'abonnement et de désinscription]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/).
- Utilisez [les fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) de Braze pour adapter le contenu des SMS à chaque consommateur, notamment grâce à du contenu dynamique et des données spécifiques à l'utilisateur.
- L'API REST Braze propose [des points de terminaison d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/) supplémentaires pour la planification de messages, le déclenchement de campagnes et bien plus encore.
