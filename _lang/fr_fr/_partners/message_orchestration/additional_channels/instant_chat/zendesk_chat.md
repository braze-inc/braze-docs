---
nav_title: Zendesk
article_title: Zendesk Chat
description: "Découvrez comment intégrer Zendesk Chat à Braze et mettre en place une conversation SMS bidirectionnelle."
alias: /partners/zendesk_chat/
page_type: partner
search_tag: Partner

---

# Zendesk Chat

> [Zendesk Chat](https://www.zendesk.com/service/messaging/) utilise les webhooks de chaque plateforme pour établir une conversation SMS bidirectionnelle. Lorsqu'un utilisateur demande de l'aide, un ticket est créé dans Zendesk. Les réponses des agents sont transmises à Braze par le biais d'une campagne SMS déclenchée par l'API, et les réponses des utilisateurs sont renvoyées à Zendesk.

## Conditions préalables


| Prérequis | Description |
|---|---|
| Un compte Zendesk | Un compte Zendesk est nécessaire pour bénéficier de ce partenariat.|
| Un jeton d'autorisation de base Zendesk | Un jeton d'autorisation de base Zendesk sera utilisé pour effectuer une demande de webhook sortant de Braze à Zendesk.|
| Une clé API REST de Braze  | Une clé API Braze REST avec des autorisations `campaigns.trigger.send`. Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**.|

## Cas d’utilisation

Améliorez l'efficacité du support client en combinant les fonctionnalités SMS de Braze avec les réponses des agents en ligne/instantanés de Zendesk pour répondre rapidement aux demandes des utilisateurs avec un support humain.

## Intégration de Zendesk Chat

### Étape 1 : Créer un webhook dans Zendesk

1. Dans la console de développement Zendesk, accédez à webhooks : {% raw %}`https://{{url}}.zendesk.com/admin/apps-integrations/webhooks/webhooks`{% endraw %}
2. Sous **Créer un webhook**, sélectionnez **Déclencheur ou automatisation**.
3. Pour l'**URL de** l'endpoint, ajoutez l'endpoint **/campaign/trigger/send**.
4. Sous **Authentification**, sélectionnez **Bearer token** et ajoutez la clé API REST de Braze avec les autorisations `campaigns.trigger.send`.

![Un exemple de webhook Zendesk.][1]{: style="max-width:70%;"}

### Étape 2 : Créer une campagne de SMS sortants

Ensuite, vous allez créer une campagne SMS qui écoutera les webhooks de Zendesk et enverra une réponse SMS personnalisée à vos clients.

#### Étape 2.1 : Composez votre message

Lorsque Zendesk envoie le contenu d'un message via l'API, il se présente dans le format suivant :

```
**----------------------------------------------\n\n{Replier Name}, {Replier Date}\n\n{Message}**
```

Nous devons donc extraire de cette chaîne de caractères les détails que nous voulons afficher dans le message, faute de quoi l'utilisateur verra tous les détails.

![Un exemple de SMS sans formatage.][2]{: style="max-width:40%;"}

Dans la zone de texte **Message**, ajoutez le code Liquid suivant et tout langage d'opt-out ou autre contenu statique :

{% raw %}
```liquid
{% assign body = {{api_trigger_properties.${msg_body}}} %}
{% assign msg = body | split: "
" %}
New message from Zendesk: 
{{msg[2]}}
 
Feel free to respond directly to this number!
```
{% endraw %}

![Un exemple de SMS avec mise en forme.][3]{: style="max-width:70%;"}

#### Étape 2.2 : Planifier la distribution

Pour le type de distribution, sélectionnez **Distribution déclenchée par API**, puis copiez l'ID de la campagne qui sera utilisé dans les étapes suivantes.

![Distribution déclenchée par l'API][4]{: style="max-width:70%;"}

Enfin, sous **Contrôle de la distribution**, activez la rééligibilité.

![Rééligibilité activée sous "Contrôles de la distribution".][5]

### Étape 3 : Créez un déclencheur dans Zendesk pour transmettre les réponses des agents à Braze.

Allez dans **Objets et règles** > **Règles de gestion** > **Déclencheurs**.

1. Créez une nouvelle **catégorie** (par exemple, **Déclencher un message**).
2. Créez un nouveau **déclencheur** (par exemple, **Répondre par SMS Braze**).
3. Sous **Conditions**, sélectionnez :
- **Ticket>Comment** est **présent et le demandeur peut voir le commentaire de** sorte que le message est déclenché chaque fois qu'un nouveau commentaire public est inclus dans la mise à jour d'un ticket.
- **Ticket>Update** *n'est pas un* **service Web (API) de** sorte que lorsqu'un utilisateur envoie un message depuis Braze, celui-ci n'est pas renvoyé sur son téléphone portable. Seuls les messages provenant de Zendesk seront transférés.

![Répondez par SMS Braze.][6]{: style="max-width:70%;"}

Sous **Actions**, sélectionnez **Notifier par webhook** et choisissez l'endpoint que vous avez créé à l'étape 1. Ensuite, indiquez le corps de l'appel à l'API. Saisissez l'adresse `campaign_id` de l'[étape 2.2](#step-22-schedule-the-delivery) dans le corps de la requête.

![Répondre par SMS Braze JSON body.][7]{: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_CAMPAIGN_ID}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
			"trigger_properties": {
    "msg_body": "{{ticket.latest_public_comment_html}}"
		},
		"attributes": {
        "zendesk_ticket" : "{{ticket.id}}",
	"zendesk_ticket_open" : "true"
    }
        }
    ]
}
```
{% endraw %}


### Étape 4 : Créez un déclencheur dans Zendesk pour mettre à jour un utilisateur lorsqu'un ticket est fermé.

Si vous souhaitez informer l'utilisateur que le ticket a été fermé, créez une nouvelle campagne dans Braze avec le corps de réponse modélisé.

![Mettre à jour un utilisateur lorsque le ticket est fermé.][8]{: style="max-width:70%;"}

Sélectionnez **Distribution déclenchée par l'API** et copiez l'ID de la campagne.

Ensuite, configurez un déclencheur pour avertir Braze de la clôture du ticket :
- Catégorie : **Déclencher un message**
- Sous Conditions, sélectionnez **Ticket>Ticket Status** et modifiez-le en **Solved (Résolu**).

![Résolu ticket set up in Zendesk.][9]{: style="max-width:70%;"}

Sous **Actions**, sélectionnez **Notifier par webhook** et choisissez le deuxième endpoint que vous venez de créer. À partir de là, nous devons spécifier le corps de l'appel à l'API :

![Ticket résolu Corps JSON.][10]{: style="max-width:70%;"}

{% raw %}
```liquid
{
    "campaign_id": "{{YOUR_API_KEY}}",
    "recipients": [
        {
            "external_user_id": "{{ticket.requester.custom_fields.braze_external_id}}",
"trigger_properties": {
    "msg_body": "Your ticket has been closed"
		},
,
			"attributes": {
	"zendesk_ticket_open" : "false"
    }
        }
    ]
}
```
{% endraw %}

### Étape 5 : Ajouter un champ d'utilisateur personnalisé dans Zendesk

Dans l'Admin Center, sélectionnez **Personnes** dans la barre latérale, puis **Configuration** > **Champs d'utilisateur.** Ajoutez le champ utilisateur personnalisé `braze_external_id`.

### Étape 6 : Mise en place d'une redirection des SMS entrants

Ensuite, vous allez créer deux nouvelles campagnes webhook à Braze afin de pouvoir transférer les SMS entrants des clients vers la boîte de réception de Zendesk.

| Campagne arrêtée           | Objectif                                                                              |
|--------------------|--------------------------------------------------------------------------------------|
| Campagne webhook 1 | Crée un nouveau ticket dans Zendesk.                                                     |
| Campagne webhook 2 | Transmet toutes les réponses SMS conversationnelles envoyées en amont par le client à Zendesk. |
{: .reset-td-br-1 .reset-td-br-2 }

#### Étape 6.1 : Créez une catégorie de mots-clés SMS

Dans le tableau de bord de Braze, allez dans **Audience**, choisissez votre **groupe d'abonnement SMS**, puis sélectionnez **Ajouter un mot-clé personnalisé**. Remplissez les champs suivants pour créer une catégorie de mots-clés SMS exclusive pour Zendesk.

| Champ            | Descriptif                                                                                                               |
|------------------|---------------------------------------------------------------------------------------------------------------------------|
| Catégorie de mots-clés | Le nom de votre catégorie de mots-clés, par exemple `ZendeskSMS1`.                                                                 |
| Mots clés         | Vos mots-clés personnalisés, tels que `SUPPORT`.                                                                                  |
| Message de réponse    | Le message qui sera envoyé lorsqu'un mot-clé est détecté, par exemple "Un représentant du service clientèle vous contactera sous peu". |
{: .reset-td-br-1 .reset-td-br-2 }

![Un exemple de catégorie de mots-clés SMS dans Braze.][11]{: style="max-width:70%;"}

#### Étape 6.2 : Créez votre première campagne webhook

Dans le tableau de bord de Braze, créez votre première campagne webhook. Ce message signalera à Zendesk que l'assistance est demandée.

Dans le compositeur de webhook, remplissez les champs suivants :
- URL du webhook : {% raw %}https://{{url}}.zendesk.com/api/v2/tickets{% endraw %}
- Méthode HTTP : POST
- En-têtes de requête :
- Content-Type : application/json
- Autorisation :  De base {{Token}}
- Corps de la demande : 

{% raw %}
```liquid
{
  "ticket": {
    "subject": "Action Needed",
    "comment": {
      "body": "{{sms.${inbound_message_body}}}"
    },
"requester":{
"name": "{{${first_name}}} {{${last_name}}}",
"user_fields": {
"braze_external_id": "{{${user_id}}}"
}
},
    "priority": "normal",
    "type": "problem"
  }
}
```
{% endraw %}

![Un exemple de demande avec les deux en-têtes requis.][12]{: style="max-width:70%;"}


#### Étape 6.3 : Planifiez la première distribution

Pour **Schedule Delivery**, sélectionnez **Action-Based Delivery**, puis choisissez **Send an SMS Inbound Message** pour votre type de déclencheur. Ajoutez également le groupe d'abonnement SMS et la catégorie de mots-clés que vous avez définis précédemment.

![La page "Planifier la distribution" pour la première campagne webhook.][13]

Sous **Contrôle de la distribution**, activez la rééligibilité.

![Rééligibilité sélectionnée sous "Contrôles de la distribution" pour la première campagne webhook.][14]

#### Étape 6.4 : Créez votre deuxième campagne webhook

Configurez une campagne webhook pour transmettre les messages SMS restants de l'utilisateur à Zendesk :

Comme Zendesk envoie l'ID du ticket sous forme de chaîne, créez un bloc de contenu pour convertir la chaîne en un entier afin de pouvoir l'utiliser dans le webhook de Zendesk.

{% raw %}
```liquid
{% assign var = {{custom_attribute.${zendesk_ticket}}} | to_i %}{{var}}
```
{% endraw %}

Dans le compositeur de webhook :
- URL du webhook : {% raw %}https://{{url}}.zendesk.com/api/v2/tickets/{{content_blocks.${to_int}}}.json{% endraw %}
- Demande : PUT
- KVP :
    - Content-Type:application/JSON
    - Autorisation : De base {{Token}}

Corps de l'échantillon : 

{% raw %}
```liquid
{
  "ticket": {
    "comment": {
      "body": "Inbound message from {{${first_name}}} {{${last_name}}}: {{sms.${inbound_message_body}}}"
    }
}
}
```
{% endraw %}

#### Étape 6.5 : Terminer la configuration de la deuxième campagne webhook
- Mettez en place un déclencheur basé sur une action pour les utilisateurs qui envoient un message entrant dans la catégorie "Autre".
- Établir des critères de rééligibilité.
- Ajoutez les audiences applicables (dans ce cas, l'attribut personnalisé **zendesk_ticket_open** est **true**).

[1]: {% image_buster /assets/img/zendesk/instant_chat/chat1.png %}
[2]: {% image_buster /assets/img/zendesk/instant_chat/chat2.png %}
[3]: {% image_buster /assets/img/zendesk/instant_chat/chat3.png %}
[4]: {% image_buster /assets/img/zendesk/instant_chat/chat4.png %}
[5]: {% image_buster /assets/img/zendesk/instant_chat/chat5.png %}
[6]: {% image_buster /assets/img/zendesk/instant_chat/chat6.png %}
[7]: {% image_buster /assets/img/zendesk/instant_chat/chat7.png %}
[8]: {% image_buster /assets/img/zendesk/instant_chat/chat8.png %}
[9]: {% image_buster /assets/img/zendesk/instant_chat/chat9.png %}
[10]: {% image_buster /assets/img/zendesk/instant_chat/chat10.png %}
[11]: {% image_buster /assets/img/zendesk/instant_chat/chat11.png %}
[12]: {% image_buster /assets/img/zendesk/instant_chat/chat12.png %}
[13]: {% image_buster /assets/img/zendesk/instant_chat/chat13.png %}
[14]: {% image_buster /assets/img/zendesk/instant_chat/chat14.png %}
