---
nav_title: Envoyer les messages
article_title: "Envoi de messages à l'aide de l'API REST"
page_order: 1
page_type: reference
description: "Cet article de référence présente les deux méthodes permettant d'envoyer des messages de manière programmatique à l'aide de l'API REST Braze."
---

# Envoi de messages à l'aide de l'API REST

> Vous pouvez envoyer des messages depuis votre backend en temps réel à l'aide de deux endpoints Braze différents. Chacune a une forme de requête différente : l'une nécessite le contenu complet du message dans la requête ; l'autre nécessite un ID de campagne et envoie le contenu défini dans le tableau de bord.

Cette approche est compatible avec tous les canaux de communication pris en charge par l'API (WhatsApp, e-mail, SMS, notifications push, cartes de contenu, webhooks, etc.).

## Deux méthodes pour envoyer

| | [`/messages/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) | [`/campaigns/trigger/send`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) |
| --- | --- | --- |
| **ID de campagne** | Facultatif. Veuillez l'omettre pour envoyer sans suivi de campagne dans le tableau de bord, ou fournissez un ID de campagne API ainsi que`message_variation_id`  dans chaque message pour effectuer le suivi dans le tableau de bord. | Obligatoire. |
| **Contenu du message** | Il est nécessaire d'inclure un`messages`objet dans la requête (par exemple, `messages.whats_app`, `messages.email`). | Non accepté. Le contenu du message est défini dans la campagne sur le tableau de bord de Braze. |
| **Cas d’utilisation** | Veuillez envoyer un message dont le contenu est entièrement spécifié dans la requête API. | Déclenchez une campagne pré-créée (contenu dans le tableau de bord) à des destinataires spécifiques via l'API. |

Pour obtenir tous les détails relatifs aux requêtes et aux réponses, veuillez consulter les références [Envoyer des messages immédiatement (API uniquement)]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) et [Envoyer des campagnes à l'aide d']({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)un endpoint [de réception/distribution déclenché par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/).

---

## Option 1 : Veuillez envoyer le contenu du message dans la requête (`/messages/send`)

Veuillez utiliser cet endpoint lorsque vous souhaitez spécifier le contenu complet du message dans la requête API. Vous **devez** inclure un`messages`objet (par exemple,`messages.whats_app` `messages.email`, ou `messages.sms`). Vous pouvez omettre`campaign_id`l'envoi sans suivi de campagne ou inclure un ID de campagne API et`message_variation_id`dans chaque message afin de suivre les envois dans le tableau de bord (consultez la [référence de l'endpoint]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/) pour plus de détails).

**Obligatoire :** Clé API avec `messages.send`l'autorisation requise.

{% alert important %}
Chaque destinataire `external_user_ids`doit déjà être enregistré dans Braze. Pour créer des utilisateurs dans le cadre d'un envoi, veuillez utiliser[`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)l'option 1 ou [l'option 2](#option-2-trigger-a-campaign-with-content-in-the-dashboard-campaignstriggersend) (campagne déclenchée par l'API) à la place.
{% endalert %}

### Exemple : Modèle de message WhatsApp

```
POST YOUR_REST_ENDPOINT/messages/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "whats_app": {
      "app_id": "YOUR_APP_ID",
      "subscription_group_id": "YOUR_WHATSAPP_SUBSCRIPTION_GROUP_ID",
      "message_type": "template_message",
      "message": {
        "template_name": "new_message_received",
        "template_language_code": "en_US"
      }
    }
  }
}
```

Pour obtenir la spécification complète de l'objet WhatsApp, veuillez consulter [Objet WhatsApp]({{site.baseurl}}/api/objects_filters/messaging/whats_app_object/).

{% alert note %}
L'endpoint`/messages/send` ne prend en charge que les modèles WhatsApp avec des en-têtes TEXTE ou IMAGE. Pour les types d'en-tête DOCUMENT, VIDÉO ou autres types de médias, veuillez utiliser l'[endpoint de campagne déclenché par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) ou le tableau de bord de Braze.
{% endalert %}

### Exemple : E-mail

```json
{
  "external_user_ids": ["user123"],
  "messages": {
    "email": {
      "app_id": "YOUR_APP_ID",
      "subject": "Your order has shipped",
      "from": "no-reply@example.com",
      "body": "<p>Your order #12345 is on its way.</p>"
    }
  }
}
```

Pour les autres canaux, veuillez consulter [la section Objets d'envoi de messages]({{site.baseurl}}/api/objects_filters/#messaging-objects).

---

## Option 2 : Déclenchez une campagne avec du contenu dans le tableau de bord.`/campaigns/trigger/send`

Veuillez utiliser cet endpoint lorsque le contenu du message est créé dans le tableau de bord de Braze (campagne déclenchée par API). Vous envoyez un champ **obligatoire**`campaign_id`et les destinataires ; vous **n'**envoyez **pas** `messages`d'objet.

**Obligatoire :** Clé API avec `campaigns.trigger.send`l'autorisation requise.

### Étape 1 : Créer une campagne déclenchée par API

1. Dans le tableau de bord de Braze, veuillez vous rendre dans **Envoi de messages** > **Campagnes**.
2. Veuillez sélectionner **Créer une campagne**, puis **Campagne déclenchée par API** (et non « Campagne API »).
3. Veuillez ajouter votre canal de communication (WhatsApp, e-mail, SMS, etc.) et créer le contenu du message dans le tableau de bord.
4. Veuillez noter l'**identifiant** **de la campagne** (et **l'identifiant d'envoi** si vous utilisez plusieurs variantes de message). Vous les utiliserez dans la requête API.

Pour plus d'informations sur la création de campagnes déclenchées par API, veuillez consulter [la section Réception/distribution déclenchée par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

### Étape 2 : Veuillez déclencher la campagne via l'API.

Veuillez envoyer une requête POST à`/campaigns/trigger/send`  avec`campaign_id`  et`recipients`  (ou `broadcast`/`audience`). Veuillez ne pas inclure `messages`d'objet — le contenu provient de la campagne.

```
POST YOUR_REST_ENDPOINT/campaigns/trigger/send
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
```

```json
{
  "campaign_id": "YOUR_CAMPAIGN_ID",
  "recipients": [
    {
      "external_user_id": "user123"
    }
  ]
}
```

Pour obtenir le corps complet de la requête (y compris `trigger_properties`, `send_to_existing_only`, `attributes`, etc.), veuillez consulter la référence [relative à l'envoi de campagnes à l'aide de]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body) l'endpoint [de réception/distribution déclenché par l'API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body).

---

## Veuillez vérifier votre intégration.

1. Veuillez envoyer une demande en utilisant l'une des options ci-dessus, en indiquant votre propre ID utilisateur comme destinataire.
2. Veuillez confirmer que le message a bien été transmis.
3. Si vous utilisez l'option 2, veuillez vérifier la campagne dans le tableau de bord de Braze afin de confirmer que l'envoi a bien été enregistré.

## Considérations

- Veuillez utiliser [les fonctionnalités de personnalisation]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/) de Braze pour adapter le contenu lorsque cela est possible.
- Veuillez vous assurer que l'envoi de messages est conforme aux réglementations applicables et qu'il inclut les options de désabonnement et les avis de confidentialité requis.
- Pour plus de points de terminaison (planification, déclencheurs Canvas, etc.), veuillez consulter [la section Points de terminaison d'envoi de messages]({{site.baseurl}}/api/endpoints/messaging/).
