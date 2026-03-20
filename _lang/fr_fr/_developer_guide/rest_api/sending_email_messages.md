---
nav_title: Envoyer des e-mails
article_title: Envoyer des e-mails via l'API REST
page_order: 3
page_type: reference
description: "Cet article de référence explique comment envoyer des e-mails à l'aide de l'API REST de Braze et d'une campagne API."
channel:
  - email
---

# Envoyer des e-mails via l'API REST

> Utilisez l'API REST de Braze pour envoyer des e-mails transactionnels depuis votre backend en temps réel. Cette approche vous permet de créer un service qui envoie des e-mails de manière programmatique tout en suivant les analyses de distribution aux côtés de vos autres campagnes et Canvas dans le tableau de bord de Braze.

Cette méthode est particulièrement utile pour les messages transactionnels dont le contenu est défini dans vos systèmes backend. Par exemple, vous pouvez notifier vos utilisateurs lorsqu'ils reçoivent un message d'un autre utilisateur, en les invitant à visiter votre site web et à consulter leur boîte de réception.

Avec cette approche, vous pouvez :

- Déclencher des e-mails depuis votre backend en temps réel.
- Suivre les analyses aux côtés de toutes vos campagnes et Canvas marketing, y compris les ouvertures, les clics et les rebonds.
- Utiliser les données d'interaction avec les messages pour déclencher des messages ultérieurs, comme un reciblage de suivi.
- Étendre le cas d'usage avec des fonctionnalités supplémentaires de Braze, telles que les délais de message et les tests A/B.
- Optionnellement, passer à la [distribution déclenchée par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/) pour définir vos modèles d'e-mail dans le tableau de bord de Braze tout en continuant à déclencher les envois depuis votre backend.

Pour envoyer un e-mail via l'API REST, vous devez configurer une campagne API dans le tableau de bord de Braze, puis utiliser l'endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) pour envoyer le message.

## Conditions préalables

Pour suivre ce guide, vous avez besoin des éléments suivants :

| Élément requis | Description |
| --- | --- |
| Clé API REST de Braze | Une clé disposant de la permission `messages.send`. Pour en créer une, accédez à **Paramètres** > **API et identifiants** > **Clés API**. |
| ID d'application Braze | L'identifiant de votre application au sein de votre espace de travail. Pour le trouver, accédez à **Paramètres** > **API et identifiants** et consultez la section **Identifiants d'application**. Cette valeur est requise dans le champ `app_id` de l'objet e-mail. Pour plus d'informations, consultez [Identifiant d'application]({{site.baseurl}}/api/identifier_types/). |
| Contenu HTML de l'e-mail | Le corps HTML de votre e-mail, préparé à l'avance. |
| Service backend | Un service backend ou un environnement de script capable d'effectuer des requêtes HTTP POST vers l'API REST de Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Étape 1 : Créer une campagne API

1. Dans le tableau de bord de Braze, accédez à **Envoi de messages** > **Campagnes**.
2. Sélectionnez **Créer une campagne**, puis sélectionnez **Campagne API**.
3. Saisissez un nom et une description pour votre campagne, par exemple « Notification par e-mail ».
4. Ajoutez des étiquettes pertinentes pour l'identification et le suivi.
5. Sélectionnez **Ajouter un canal de communication**, puis sélectionnez **E-mail**.
6. Notez l'**ID de campagne** affiché sur la page de la campagne. Vous aurez besoin de cette valeur pour construire votre requête API. Vous pouvez également noter l'**ID de variation de message** — incluez-le dans votre requête si vous souhaitez attribuer les statistiques d'envoi à une variation de message spécifique.

## Étape 2 : Envoyer un e-mail via l'API

Construisez une requête POST vers l'endpoint [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/). Incluez l'ID de campagne, l'ID utilisateur externe du destinataire et le contenu de l'e-mail dans le PAYLOAD de la requête.

{% alert important %}
Chaque destinataire référencé dans `external_user_ids` doit déjà exister dans Braze. Les envois via API uniquement ne créent pas de nouveaux profils utilisateur. Si vous devez créer des utilisateurs dans le cadre d'un envoi, utilisez d'abord [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), ou utilisez plutôt une [campagne déclenchée par API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).
{% endalert %}

### Exemple de requête

```
POST https://YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

Remplacez `YOUR_REST_ENDPOINT` par l'[URL de l'endpoint REST]({{site.baseurl}}/api/basics/#endpoints) de votre espace de travail.

{% raw %}
```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "message_variation_id": "YOUR_MESSAGE_VARIATION_ID",
      "subject": "You have a new message!",
      "from": "Notifications <notifications@yourcompany.com>",
      "body": "<html><body><h1>You have a new message!</h1><p>Hi {{${first_name}}},</p><p>You received a new message in your inbox. Click the link below to read it:</p><a href='https://yourwebsite.com/messages'>View message</a><p>Thank you for using our service!</p></body></html>"
    }
  }
}
```
{% endraw %}

Remplacez les valeurs de substitution par vos identifiants réels. Le champ `from` doit respecter le format `"Nom d'affichage <email@adresse.com>"`. Le champ `body` accepte du HTML valide et prend en charge la [personnalisation Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), ce qui vous permet d'adapter le contenu de l'e-mail à chaque destinataire. Pour la liste complète des paramètres pris en charge par l'objet e-mail, consultez [Objet e-mail]({{site.baseurl}}/api/objects_filters/messaging/email_object/).

Une fois la requête construite, envoyez-la en POST depuis votre service backend vers l'API REST de Braze.

## Étape 3 : Vérifier votre intégration

Une fois la configuration terminée, vérifiez votre intégration :

1. Envoyez une requête API comme décrit à l'[étape 2](#step-2-send-an-email-using-the-api), en utilisant votre propre ID utilisateur comme destinataire.
2. Confirmez que l'e-mail est bien distribué dans votre boîte de réception.
3. Dans le tableau de bord de Braze, accédez à la page de résultats de la campagne et confirmez que l'envoi est enregistré.
4. Surveillez attentivement les résultats à mesure que vous montez en charge.

## Points à prendre en compte

- Assurez-vous que vos campagnes d'e-mail sont conformes aux réglementations en vigueur, telles que le RGPD et CAN-SPAM, en incluant les options de désinscription et les mentions de confidentialité nécessaires. Pour plus d'informations, consultez [Gérer les abonnements des utilisateurs]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) et [Bonnes pratiques pour les e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/).
- Utilisez les [fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) de Braze pour adapter le contenu des e-mails à chaque utilisateur, y compris le contenu dynamique et les données spécifiques à l'utilisateur.
- L'API REST de Braze propose des [endpoints de messagerie]({{site.baseurl}}/api/endpoints/messaging/) supplémentaires pour planifier des messages, déclencher des campagnes, et bien plus encore.