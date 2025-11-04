---
nav_title: Regal
article_title: Regal
description: "Cet article de référence décrit le partenariat entre Braze et Regal, une solution de vente par téléphone et SMS qui vous permet d'utiliser les données des deux sources pour créer des expériences personnalisées pour vos clients."
alias: /partners/regal/
page_type: partner
search_tag: Partner

---

# Regal

> [Regal.io](https://regal.io) est la solution de vente par téléphone et SMS créée pour générer plus de conversions afin que vous puissiez atteindre vos objectifs de croissance plus rapidement.

En intégrant Regal et Braze, vous pouvez créer une expérience plus cohérente et personnalisée sur tous vos points de contact avec les clients.
- Envoyez des e-mails ou des notifications push pertinents depuis Braze en fonction du contenu d’une conversation téléphonique sur Regal.
- Déclenchez un appel dans Regal lorsqu'un client de grande valeur clique sur un e-mail marketing de Braze mais n’achète pas.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Regal | Un compte Regal est requis pour profiter de ce partenariat. |
| clé API Regal | Une clé API Regal permettra d'envoyer des événements de Braze à Regal.<br><br>E-mail [support@regal.io](mailto:support@regal.io) pour obtenir cette clé. |
| Transformation des données de Braze | La transformation des données est actuellement en accès anticipé. Contactez votre gestionnaire de la satisfaction client Braze si vous êtes intéressé par l'accès anticipé. Ceci est nécessaire pour recevoir des données de Regal. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## intégration: Envoi de données de Braze à Regal

La section suivante décrit comment utiliser Braze comme source pour envoyer les profils clients et les données d'événement à Regal en utilisant les webhooks de canvas ou de campagnes de Braze.

### Étape 1 : Créer de nouveaux contacts dans Regal

Créer un canvas ou une campagne qui envoie des webhooks à Regal chaque fois qu'un nouveau contact est créé dans Braze et que vous souhaitez qu'il soit disponible pour des appels et des SMS dans Regal. 

1. Créez un canvas ou une campagne intitulée "Créer un nouveau contact pour Regal" et sélectionnez **Basé sur l'action** comme type d'entrée.

2. Définissez la logique du déclencheur comme **événement personnalisé** et sélectionnez l'événement qui est déclenché lorsqu'un contact avec un numéro de téléphone est créé. Regal recommande également d'ajouter un filtre supplémentaire sur le champ téléphone pour s'assurer qu'il est défini.

3. Dans votre nouveau modèle de webhook, remplissez les champs suivants :
   - **URL de webhook** : <https://events.regalvoice.com/events>
   - **Corps de la requête** : Texte brut

#### En-têtes de requête et méthode

Regal.io nécessite également un en-tête HTTP pour l'autorisation et une méthode HTTP. Le suivant sera déjà inclus dans le modèle en tant que paire clé-valeur dans l'onglet **Paramètres** :
{% raw %}
- **Méthode HTTP**: POST
- **En-têtes de requête**:
    - **Autorisation** : `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corps de la requête

Le seul champ requis ci-dessous est la propriété `traits.phone`. Le REST est facultatif. Cependant, si vous incluez `optIn`, vous devez inclure `optIn.channel` et `optIn.subscribed`.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "email": "<email>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": true
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": true
            }
        ],
        "custom1": "<custom1>",
        "custom2": "<custom2>"
    },
    "eventSource": "braze"
}
```

L'exemple de charge utile ci-dessus suppose que tous vos contacts ont accepté l'abonnement pour les message vocaux et les SMS. Si ce n'est pas le cas, vous pouvez supprimer la propriété `optIn` ci-dessus et configurer un canvas ou une campagne séparée pour mettre à jour un contact dans Regal lorsque `optIn` est collecté.

### Étape 2 : Mettre à jour les informations d'abonnement 

Si l'abonnement et le désabonnement peuvent se produire à différents moments de l'expérience utilisateur sur votre application, il est important de mettre à jour Regal lorsque les utilisateurs s'abonnent ou se désabonnent. Vous trouverez ci-dessous un canvas recommandé pour envoyer des informations d'abonnement à jour à Regal. Il suppose que vous l'enregistrez en tant que champ de profil Braze, mais sinon, le déclencheur peut tout aussi bien être un événement dans votre compte Braze qui représente un utilisateur s'inscrivant ou se désabonnant. (L'exemple ci-dessous concerne l'abonnement téléphonique, mais vous pouvez configurer un canvas ou une campagne similaire pour l'abonnement SMS si vous les collectez séparément).

1. Créez une canvas ou une campagne en l’intitulant "Envoyer l’inscription ou la désinscription à Regal".

2. Sélectionnez l'une des options de déclencheur suivantes et sélectionnez le champ qui représente l’état d'abonnement de l'utilisateur. Si vous déclenchez un événement vers Braze pour représenter l'abonnement ou le désabonnement, utilisez cet événement comme déclencheur à la place.
    - Champ de profil utilisateur mis à jour
    - Mettre à jour le statut du groupe d'abonnement
    - Statut de l'abonnement

3. Dans votre nouveau modèle de webhook, remplissez les champs suivants :
   - **URL de webhook** : <https://events.regalvoice.com/events>
   - **Corps de la requête** : Texte brut

#### En-têtes de requête et méthode

Regal.io nécessite également un en-tête HTTP pour l'autorisation et une méthode HTTP. Le texte suivant sera déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres** :
{% raw %}
- **Méthode HTTP**: POST
- **En-têtes de requête**:
    - **Autorisation** : `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corps de la requête

Vous êtes invité à ajouter des attributs supplémentaires de profil utilisateur dans cette charge utile également si vous souhaitez vous assurer que plus d'attributs sont à jour simultanément.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "optIn": [
            {
                "channel": "voice",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            },
            {
                "channel": "sms",
                "source": "<leadSource>",
                "subscribed": "<voice_optin_subscribed>"
            }
        ]
    },
    "eventSource": "braze"
}
```

### Étape 3 : Envoyer des événements personnalisés

Enfin, configurez un canvas ou une campagne pour chacun des événements clés que vous souhaitez envoyer à Regal - Regal recommande d'envoyer tous les événements importants pour déclencher des SMS et des appels dans Regal (comme un événement à chaque étape du processus d'inscription ou d'achat) ou qui seront utilisés comme critères de sortie pour que les contacts sortent des campagnes Regal.

Par exemple, ci-dessous se trouve un flux de travail pour envoyer un événement à Regal lorsqu'un utilisateur termine la première étape d'une application.

1. Créez un canvas ou une campagne en l’intitulant "Envoyer l'événement de l'étape 1 terminée de l'application à Regal".

2. Définissez la logique du nœud déclencheur comme **événement personnalisé** et sélectionnez le nom de l'événement que vous souhaitez envoyer à Regal, tel que "Étape 1 de l'application terminée".

3. Dans votre nouveau modèle de webhook, remplissez les champs suivants :
   - **URL de webhook** : <https://events.regalvoice.com/events>
   - **Corps de la requête** : Texte brut

#### En-têtes de requête et méthode

Regal.io nécessite également un en-tête HTTP pour l'autorisation et une méthode HTTP. Le texte suivant sera déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres** :
{% raw %}
- **Méthode HTTP**: POST
- **En-têtes de requête**:
    - **Autorisation** : `{{<REGAL_API_KEY>}}`
    - **Content-Type**: application/json
{% endraw %}

#### Corps de la requête

Vous êtes invité à ajouter des attributs supplémentaires de profil utilisateur dans cette charge utile si vous souhaitez vous assurer que plusieurs attributs sont à jour simultanément.

```json
{
    "userId": "<uniqueIdentifier>", //this is optional
    "traits": {
        "phone": "<phoneNumber>",
        "firstName": "<firstName>",
        "lastName": "<lastName>",
        "custom1": "<custom1>",
        "custom2": "<custom2>",
        "custom3": "<custom3>"
    },
    "name": "Application Step 1 Completed",
    "properties": {
      "educationalLevel": "<educationalLevel>",
      "preferredLocation": "<preferredLocation>",
      "preferredSubject": "<preferredSubject>",
      "readytoCommit": true
    },
    "eventSource": "braze"
}
```

#### Attributs de contact à jour

Bien que cela ne soit pas nécessaire, Regal recommande également d'envoyer tous les champs de données de profil utilisateur clés aux charges utiles des événements de vos flux d'événements pour s'assurer que Regal ait accès aux attributs de contact les plus récents au moment où les événements clés deviennent disponibles.

{% alert note %}
Si vous avez des questions sur les événements importants à envoyer à Regal ou sur la meilleure façon de configurer ces Canvases et campagnes, contactez support@regal.io.
{% endalert %}

## intégration: Envoi de données de Regal à Braze

Cette section décrit comment obtenir des événements de reporting Regal comme `SMS.sent` et `call.completed` dans Braze afin qu'ils puissent apparaître sur vos profils Braze et être disponibles dans l'outil de segmentation Braze, canvas, et les campagnes. Cette intégration utilise les Webhooks de Reporting Regal et la Transformation de Données de Braze pour automatiser le flux de données.

### Étape 1 : Créer une Transformation de données dans Braze

{% alert important %}
La transformation des données est actuellement en accès anticipé. Contactez votre gestionnaire de la satisfaction client Braze si vous êtes intéressé par l'accès anticipé.
{% endalert %}

Braze recommande de créer une transformation selon le webhook Regal que vous prévoyez d'envoyer à Braze. 

Pour créer une Transformation de données :
1. Accédez à la page **Transformations** dans votre tableau de bord de Braze.
2. Donnez un nom à votre transformation et cliquez sur **Créer une transformation**.
3. Dans la liste des transformations, cliquez sur <i class="fa-solid fa-ellipsis-vertical" title="Afficher les actions"></i> et sélectionnez **Copier l'URL du webhook**.

![]({% image_buster /assets/img/regal/copy_webhook_url.png %})

### Étape 2 : Activer les webhooks de rapport dans Regal

Pour configurer les webhooks de rapport :
1. Accédez à l'application Regal et ouvrez la page **Paramètres**.

2. Dans la section **Reporting Webhooks**, cliquez sur **Create Webhooks**.

3. Dans l'entrée de l'endpoint du webhook, ajoutez l'URL du webhook de transformation de données Braze pour la transformation de données associée.

![]({% image_buster /assets/img/regal/edit_webhook.png %}){: style="max-width:60%;"}

#### Mise à jour d'un endpoint
Lorsque vous modifiez un endpoint, cela peut prendre jusqu'à 5 minutes pour que le cache s'actualise et envoie des événements à votre nouvel endpoint à la place.
#### Tentatives
Actuellement, il n'y a pas de nouvelles tentatives sur ces événements. Si une réponse n'est pas reçue dans les 5 secondes, l'événement est abandonné et n'est pas retenté. Regal ajoutera des tentatives dans une future version.
#### Événements
Le [guide des webhooks de reporting](https://developer.regal.io/docs/reporting-webhooks#events) de Regal comprend la liste complète des événements de reporting qu'ils publient. Ce guide contient également les définitions des propriétés et des exemples de charges utiles.

### Étape 3 : Transformez les événements Regal en événements Braze

La fonctionnalité de [transformation des données de]({{site.baseurl}}/data_transformation) Braze vous permet de mapper les données Regal entrantes dans le format nécessaire pour les ajouter en tant qu'attributs, événements ou achats dans Braze.

1. Nommez votre transformation de donnée. Il est recommandé de configurer une transformation de données par webhook d'événement.

2. Pour tester la connexion, créez un appel sortant depuis le bureau de l’agent Regal vers votre téléphone portable et soumettez le formulaire de résumé de conversation pour créer un événement call.completed.

3. Déterminez quels identifiants vous utiliserez pour mapper vos contacts Regal à vos profils Braze. Les identifiants disponibles dans les événements Regal incluent :
   - `userId` - uniquement défini sur les événements si vous avez déjà envoyé cet identifiant pour un contact
   - `traits.phone`
   - `traits.email` - uniquement défini sur les événements si vous avez déjà envoyé cet identifiant pour un contact

#### Identifiants pris en charge par Braze
- Braze ne prend pas en charge les numéros de téléphone comme identifiant. Pour l'utiliser comme identifiant, le numéro de téléphone peut être défini comme [alias d'utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases) dans Braze.
- Lors de l'utilisation de la transformation de données Braze, l'adresse e-mail peut être utilisée comme identifiant. Si l'adresse e-mail existe en tant que profil dans Braze, le profil existant sera mis à jour. Si l'adresse e-mail n'existe pas encore dans Braze, un profil uniquement e-mail sera créé.

## Cas d'utilisation

{% tabs %}
{% tab Déclencher un e-mail %}

**Déclenchez un e-mail depuis Braze en fonction d'une disposition d'appel dans Regal**

Vous trouverez ci-dessous un exemple de charge utile pour un événement `call.completed` dans Regal. 

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com"
  },
  "name": "call.completed",
  "properties": {
    "agent_firstname": "Rebecca",
    "agent_fullname": "Rebecca Greene",
    "agent_id": "xxxx@yourbrand.com",
    "direction": "OUTBOUND",
    "regal_voice_phone": "+19545558563",
    "regal_voice_phone_internal_name": "Sales Line",
    "contact_phone": "+17625555555",
    "call_id": "WTxxxxx9",
    "type": "Outbound Call",
    "disposition": "Converted During Convo",
    "notes": null,
    "objections": null,
    "campaign_name": "Life Insurance Quote Follow Up",
    "campaign_friendly_id": "445",
    "started_at": 1657855046,
    "ended_at": 1657855053,
    "completed_at": 1657855059,
    "talk_time": 7,
    "wrapup_time": 6,
    "handle_time": 13,
    "journey_uuid": null,
    "journey_name": null,
    "journey_friendly_id": null
  },
  "originalTimestamp": "1657855059",
  "eventSource": "Regal Voice"
}
```

Vous trouverez ci-dessous un exemple de transformation de données pour mapper cela à un événement personnalisé dans Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is a default template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "name": "Call Completed",
     "time": isoString,
     "_update_existing_only": false,
     "properties": {
       "agent_firstname": payload.properties.agent_firstname,
       "agent_fullname": payload.properties.agent_fullname,
       "agent_id": payload.properties.agent_id,
       "direction": payload.properties.direction,
       "regal_voice_phone": payload.properties.regal_voice_phone,
       "regal_voice_phone_internal_name": payload.properties.regal_voice_phone_internal_name,
       "contact_phone": payload.properties.contact_phone,
       "call_id": payload.properties.call_id,
       "type": payload.properties.type,
       "disposition": payload.properties.disposition,
       "notes": payload.properties.notes,
       "objections": payload.properties.objections,
       "campaign_name": payload.properties.campaign_name,
       "campaign_friendly_id": payload.properties.campaign_friendly_id,
       "started_at": payload.properties.started_at,
       "ended_at": payload.properties.ended_at,
       "completed_at": payload.properties.completed_at,
       "talk_time": payload.properties.talk_time,
       "wrapup_time": payload.properties.wrapup_time,
       "handle_time": payload.properties.handle_time,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_name": payload.properties.journey_name,
       "journey_friendly_id": payload.properties.journey_friendly_id
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Mettre à jour les attributs du profil %}

**Mettez à jour les attributs de profil dans Braze en fonction des `contact.attribute.edited` événements de Regal**

Vous trouverez ci-dessous un exemple de charge utile pour un événement `contact.attribute.edited` dans Regal. Cet événement est déclenché chaque fois que l'un de vos agents apprend quelque chose de nouveau dans une conversation et met à jour un attribut sur le profil du contact.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.attribute.edited",
  "properties": {
    "agent_email": "xxxx@yourbrand.com",
    "contact_phone": "+17625555555",
    "changes": {
      "custom_properties": {
        "annual_income": {
          "old_value": "150,000",
          "new_value": "300,000"
        }
      }
    },
    "created_at": "1657855462"
  },
  "originalTimestamp": "1657855462",
  "eventSource": "Regal Voice"
}
```

Vous trouverez ci-dessous un exemple de transformation de données pour mapper les nouvelles valeurs de propriété personnalisée aux attributs pertinents de vos profils Braze :

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// Capture the key's updated property value within the 'changes' object and store this in an attributes variable that can be used in the /users/track request

const changes = payload.properties.changes.custom_properties;

const attributes = {};
for (const key in changes) {
 attributes[key] = changes[key].new_value;
}

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

const brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     ...attributes
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% tab Gardez vos expériences synchronisées %}

**Gardez vos expériences dans Braze et Regal synchronisées en utilisant des événements `contact.experiment.assigned`**

Vous trouverez ci-dessous un exemple de charge utile pour un événement `contact.experiment.assigned` dans Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
  },
  "name": "contact.experiment.assigned",
  "properties": {
    "experiment_name": "Post Call Offer Test",
    "experiment_id": "xxxx-xxxx-xxxx-xxxx",
    "experiment_variant": "Aggressive Offer - 50%",
    "journey_uuid": "xxxx-xxxx-xxxx-xxxx",
    "journey_friendly_id": 220,
    "journey_name": "Post Call Follow Up"
  },
  "originalTimestamp": "1657855118",
  "eventSource": "Regal Voice"
}
```

Vous trouverez ci-dessous un exemple de transformation de données pour mapper cela à un événement personnalisé dans Braze.

```
// The Braze /users/track endpoint expects timestamps in an ISO 8601 format. To use the Unix timestamp within Regal's call.completed event payload as the event timestamp in Braze, it must first be converted to ISO 8601. This can be done with the following code:
let unixTimestamp = payload.originalTimestamp;
let dateObj = new Date(unixTimestamp * 1000);
let isoString = dateObj.toISOString();

// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z
let brazecall = {
 "events": [
   {
     "external_id": payload.userId,
     "_update_existing_only": false,
     "name": "Contact Experiment Assigned",
     "time": isoString,
     "properties": {
       "experiment_name": payload.properties.experiment_name,
       "experiment_id": payload.properties.experiment_id,
       "experiment_variant": payload.properties.experiment_variant,
       "journey_uuid": payload.properties.journey_uuid,
       "journey_friendly_id": payload.properties.journey_friendly_id,
       "journey_name": payload.properties.journey_name
     }
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;

```
{% endtab %}
{% tab Se désabonner d'un contact %}

**Désabonner un contact dans Braze en fonction d'un `contact.unsubscribed` de Regal**

Vous trouverez ci-dessous un exemple de charge utile pour un événement `contact.unsubscribed` dans Regal.

```json
{
  "userId": "123",
  "traits": {
    "phone": "+17625555555",
    "email": "xxx@gmail.com",
    "ip": "78.97.213.166"
  },
  "name": "contact.unsubscribed",
  "properties": {
    "new_subscription": true,
    "channel": "voice",
    "text": null,
    "ip": "207.38.149.143",
    "source": "regalvoice.agent_desktop",
    "timestamp": "1657855229"
  },
  "originalTimestamp": "1657855230",
  "eventSource": "Regal Voice"
}
```

Vous trouverez ci-dessous un exemple de transformation de données pour désabonner le contact dans Braze.

```
// This is an example template you can use as a starting point. Feel free to delete this entirely to start from scratch or to delete specific components as you see fit.

// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JS dot notation, such as payload.x.y.z

let brazecall = {
 "attributes": [
   {
     "external_id": payload.userId,
     "_update_existing_only": true,
     "subscription_groups" : [{
       "subscription_group_id": "YOUR SUBSCRIPTION GROUP ID",
       "subscription_state": "unsubscribed"
     }]
   }
 ]
};

// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

{% endtab %}
{% endtabs %}

