---
nav_title: WhatsApp et système externe
article_title: Intégrer Braze et WhatsApp à un système externe
page_order: 2
description: "Cet article de référence fournit un guide étape par étape pour l'intégration de Braze et WhatsApp avec un système externe d'intelligence artificielle ou de communication."
page_type: reference
alias: /whatsapp_external_system_integration/
channel:
  - WhatsApp
---

# Effectuez l'intégration de Braze et WhatsApp avec un système externe d'intelligence artificielle ou de communication.

> Tirez parti de la puissance des chatbots basés sur l'intelligence artificielle et des transferts vers des agents en ligne sur le canal WhatsApp pour optimiser vos opérations de support client. En automatisant les demandes courantes et en transférant de façon fluide les appels vers des agents humains lorsque cela est nécessaire, vous pouvez considérablement améliorer les temps de réponse et l'expérience client globale.

## Fonctionnement

L'intégration entre Braze et l'intelligence artificielle ou le système de communication externe fonctionne dans les deux sens, Braze servant de canal de communication et le système externe d'« intelligence » traitant les messages et formulant les réponses.

Le flux de travail d'intégration peut être divisé en deux flux principaux :
**Flux entrant :** Le message d'un utilisateur arrive dans Braze, puis est transféré vers votre système externe pour être traité.
**Flux sortant :** Après avoir traité le message, votre système externe envoie une réponse à Braze, qui transmet ensuite le message à l'utilisateur final.

Afin d'automatiser efficacement cette communication, cette intégration utilise deux fonctionnalités clés de Braze : [les campagnes webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) et [les campagnes déclenchées par API]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery/).

![Architecture de l'intégration entre le canal WhatsApp de Braze et un système externe.]({% image_buster /assets/img/whatsapp/external_system_architecture.png %})
<sup>*Architecture de l'intégration entre le canal WhatsApp de Braze et un système externe.*</sup>

## Conditions préalables

| Prérequis | Description |
| - | - |
| Système externe | Un système d'intelligence artificielle ou de communication tiers capable de créer et de gérer des chatbots, des systèmes automatisés de service à la clientèle utilisant des API, ou les deux. |
| Intégration de Braze et WhatsApp | Un numéro WhatsApp géré par Braze |
| Clé API REST Braze | Une clé API REST avec`campaigns.trigger.send`les autorisations nécessaires. Vous pouvez le créer dans le tableau de bord de Braze en vous rendant dans **Paramètres** > **Clés API**. |
{: .reset-td-br-1 .reset-td-br-2 role=”presentation” }

## Configuration de l'intégration

### Étape 1 : Créer une campagne de webhook pour les messages entrants

Tout d'abord, veuillez créer une campagne webhook afin de mettre en place un moyen d'envoyer les messages WhatsApp reçus par Braze vers votre système externe.

1. Dans Braze, veuillez créer une campagne webhook.
2. Dans le compositeur de webhook, veuillez sélectionner **« Composer un webhook** ».
3. Dans le champ **URL du webhook**, veuillez saisir l'endpoint API (URL) du système externe qui recevra le message.
4. Sélectionnez **Texte brut** pour le corps de la requête et saisissez une charge utile de personnalisation contenant le nom`external_id`et le numéro de téléphone de l'utilisateur, le contenu du message et d'autres informations pertinentes, telles que :

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
5\. Dans l'étape **de planification **de **la livraison** de votre éditeur de campagne, veuillez sélectionner **Livraison par événement** comme type de livraison et **Envoyer un message WhatsApp entrant** comme déclencheur de la campagne.

![Livraison par événement, avec un déclencheur : l'envoi d'un message WhatsApp entrant.]({% image_buster /assets/img/whatsapp/inbound_message_trigger.png %})

{: start="6"}
6\. Veuillez terminer la composition de votre campagne, puis enregistrez-la et lancez-la. Une fois la campagne lancée, chaque fois qu'un message est reçu, Braze envoie un webhook à votre système externe.

### Étape 2 : Créer une campagne déclenchée par API pour les messages sortants {#step-2}

Ensuite, veuillez créer une campagne déclenchée par API afin de permettre à votre système externe d'envoyer des messages aux utilisateurs via WhatsApp.

1. Dans Braze, veuillez créer une campagne WhatsApp. 
2. Dans l'éditeur de message, veuillez sélectionner soit « **Modèle de message WhatsApp** », soit **« Message de réponse** », puis choisissez le modèle ou la mise en page du message de réponse. Vous pouvez sélectionner n'importe quelle mise en page de message de réponse, car le message entrant a ouvert la fenêtre WhatsApp de 24 heures.

![Éditeur de messages avec options permettant de sélectionner le type et la mise en page du message.]({% image_buster /assets/img/whatsapp/response_message_layout.png %})

{: start="3"}
3\. Veuillez ajouter la propriété de déclencheur API au corps du message, par exemple{% raw %}```{{api_trigger_properties.${external_system_msg+body}}}```{% endraw %}. Cela permet à votre système d'intelligence artificielle de remplir le message qui sera envoyé.

![Compositeur de message avec corps de message contenant les propriétés de déclencheur.]({% image_buster /assets/img/whatsapp/api_trigger_properties.png %})

{: start="4"}
4\. Dans l'étape **de planification **de **la livraison** de votre éditeur de campagne, veuillez sélectionner **la livraison par événement** comme type de livraison.
5\. Veuillez enregistrer la campagne, puis notez l'identifiant unique `campaign_id`généré par Braze pour cette campagne. Vous aurez besoin de l'ID pour l'étape suivante.

### Étape 3 : Veuillez connecter le système externe à la campagne déclenchée par l'API.

Enfin, veuillez configurer votre système externe pour qu'il appelle Braze et envoie la réponse.

1. Dans le code de votre système externe, après avoir traité le message reçu et généré la réponse, veuillez effectuer une requête POST vers l'endpoint`/messages/send` Braze.
2. Dans le corps`/messages/send` de la requête, veuillez inclure l'élément`campaign_id`de [l'étape 2](#step-2), l'identifiant de l'utilisateur `external_id`et le contenu de la réponse du système externe.
3. Veuillez utiliser la propriété de déclencheur API de [l'étape 2](#step-2) pour insérer la réponse du système externe, et n'oubliez pas d'inclure votre clé API dans l'en-tête de la requête pour l'authentification, comme dans cet exemple cURL :

{% raw %}
```bash
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

Vous disposez désormais d'une base solide pour créer un flux de travail pour votre chatbot à intelligence artificielle.

### Flux de travail personnalisé

Vous pouvez étendre votre logique d'intégration à :
- Veuillez utiliser différents mots-clés pour servir de déclencheurs à des campagnes webhook distinctes.
- Créez des flux de conversation plus complexes grâce à des campagnes déclenchées par API en plusieurs étapes.
- Enregistrez les informations de chat dans Braze en tant qu'attributs personnalisés afin d'enrichir le profil utilisateur et de segmenter les campagnes futures.
