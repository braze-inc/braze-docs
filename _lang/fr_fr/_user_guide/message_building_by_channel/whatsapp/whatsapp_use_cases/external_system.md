---
nav_title: WhatsApp et le système externe
article_title: Intégration de Braze et de WhatsApp à un système externe
page_order: 2
description: "Cet article de référence fournit un guide étape par étape pour l'intégration de Braze et WhatsApp avec un système d'intelligence artificielle ou de communication externe."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Intégration de Braze et WhatsApp à un système d'intelligence artificielle ou de communication externe.

> Tirez parti de la puissance des chatbots d'intelligence artificielle et de la production/instantanée d'agents en ligne sur le canal WhatsApp pour rationaliser vos opérations d'assistance à la clientèle. En automatisant les demandes de renseignements de routine et en passant de façon fluide/sansans homogène à des agents humains en cas de besoin, vous pouvez améliorer considérablement les temps de réponse et l'expérience client dans son ensemble.

## Comment cela fonctionne-t-il ?

L'intégration entre Braze et l'intelligence artificielle ou le système de communication externe fonctionne dans les deux sens : Braze est le canal de communication et le système externe est l'"intelligence" qui traite les messages et formule des réponses.

Le processus d'intégration peut être divisé en deux flux principaux :
**Flux entrant :** Le message d'un utilisateur arrive dans Braze et est ensuite transmis à votre système externe pour y être traité.
**Flux sortant :** Après avoir traité le message, votre système externe envoie une réponse à Braze, qui transmet ensuite le message à l'utilisateur final.

Pour automatiser efficacement cette communication, cette intégration utilise deux fonctionnalités clés de Braze : les [campagnes webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) et les [campagnes déclenchées par l'API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

Architecture de l'intégration entre le canal Braze WhatsApp et un système externe.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Architecture de l'intégration entre le canal Braze WhatsApp et un système externe.*</sup>

## Conditions préalables

| Conditions préalables | Description |
| - | - |
| Système externe | Un système d'intelligence artificielle ou de communication tiers capable de créer et de gérer des chatbots, des systèmes de service client automatisés utilisant des API, ou les deux. |
| Intégration de Braze et de WhatsApp | Un numéro WhatsApp géré par Braze |
| Clé API REST Braze | Une clé API REST avec des autorisations `campaigns.trigger.send`. Celle-ci peut être créée dans le tableau de bord de Braze en allant dans **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Configuration de l'intégration

### Étape 1 : Créer une campagne webhook pour les messages entrants.

Tout d'abord, créez une campagne webhook pour établir un moyen d'envoyer les messages WhatsApp reçus par Braze à votre système externe.

1. Dans Braze, créez une campagne webhook.
2. Dans le compositeur de webhook, sélectionnez **Composer un webhook**.
3. Dans le champ **Webhook URL**, entrez le point d'extrémité API (URL) du système externe qui recevra le message.
4. Sélectionnez **Raw text** pour le corps de la demande et entrez un payload avec personnalisation qui contient le `external_id` et le numéro de téléphone de l'utilisateur, le contenu du message et d'autres informations pertinentes, comme par exemple :

{% raw %}
```liquid
{
  "user_id": "{{${user_id}}}",
  "phone_number": "{{${phone_number}}}",
  "message": "{{whats_app.${inbound_message_body}}}"
}
```
{% endraw %}

{: start="5"}
5\. Dans l'étape **Planifier la livraison du** compositeur de votre campagne, sélectionnez **Basé sur l'action** pour le type de réception/distribution et **Envoyer un message WhatsApp entrant** pour le déclencheur de la campagne.

Livraison par événement avec un déclencheur d'envoi d'un message WhatsApp entrant.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. Terminez la composition de votre campagne, puis enregistrez et lancez la campagne. Désormais, à chaque fois qu'un message est reçu, Braze envoie un webhook à votre système externe.

### Étape 2 : Créez une campagne déclenchée par l'API pour les messages envoyés. {#step-2}

Ensuite, créez une campagne déclenchée par l'API afin d'établir un moyen pour votre système externe de renvoyer des messages aux utilisateurs via WhatsApp.

1. Dans Braze, créez une campagne WhatsApp. 
2. Dans le compositeur de messages, sélectionnez soit **WhatsApp Template Message**, soit **Response Message**, puis sélectionnez la mise en page du modèle ou du message de réponse. Vous pouvez sélectionner n'importe quelle présentation de message de réponse car le message entrant a ouvert la fenêtre WhatsApp de 24 heures.

!Compositeur de messages avec des options permettant de sélectionner le type de message et la présentation du message.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. Ajoutez la propriété du déclencheur API au corps du message, par exemple {% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}. Cela permet à votre système d'intelligence artificielle d'alimenter le message qui sera envoyé.

\![Compositeur de message avec un corps de message contenant les propriétés du déclencheur.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. Dans l'étape **Planifier la réception/distribution** du compositeur de votre campagne, sélectionnez le type de **réception/distribution basé sur une action**.
5\. Enregistrez la campagne, puis prenez note de l'unique `campaign_id` que Braze génère pour cette campagne. Vous aurez besoin de l'ID pour l'étape suivante.

### Étape 3 : Connecter le système externe à la campagne déclenchée par l'API

Enfin, configurez votre système externe pour qu'il appelle Braze et envoie la réponse.

1. Dans le code de votre système externe, après avoir traité le message reçu et généré la réponse, faites une demande POST au point de terminaison Braze `/messages/send`.
2. Dans le corps de la requête `/messages/send`, incluez le `campaign_id` de l' [étape 2](#step-2), le `external_id` de l'utilisateur et le contenu de la réponse du système externe.
3. Utilisez la propriété de déclencheur API de l' [étape 2](#step-2) pour insérer la réponse du système externe, et n'oubliez pas d'inclure votre clé API dans l'en-tête de la requête pour l'authentification, comme dans cet exemple cURL :

{% raw %}
```json
curl -X POST \
  -H 'Content-Type:application/json' \
  -H 'Authorization: Bearer a valid rest API key' \
  -d '{
    "campaign_id": "campaign_id",
    "recipients": [
      {
        "external_user_id": "external_id",
        "trigger_properties": {
          "external_system_msg_body": "your external system message"         
        }
      }
    ]
  }' \
  {{Braze endpoint}}/campaigns/trigger/send
```
{% endraw %}

Vous disposez désormais d'une base solide pour créer un flux de travail de chatbot d'intelligence artificielle !

### Personnaliser votre flux de travail

Vous pouvez étendre votre logique d'intégration à :
- Utilisez différents mots-clés pour déclencher des campagnes webhook distinctes.
- Créez des flux de conversation plus complexes avec des campagnes déclenchées par l'API en plusieurs étapes.
- Enregistrez les informations relatives au chat dans Braze sous forme d'attributs personnalisés afin d'enrichir le profil utilisateur et de segmenter les futures campagnes.
