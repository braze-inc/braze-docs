---
nav_title: Lob
article_title: Lob 
alias: /partners/lob/
description: "Cet article de référence présente le partenariat entre Braze et Lob.com, qui vous permet d'envoyer des lettres, des cartes postales et des chèques par la poste sous forme de publipostage."
page_type: partner
search_tag: Partner

---

# Lob

> [Lob.com](https://lob.com) est un service en ligne qui vous permet d'envoyer un publipostage à vos utilisateurs.

_Cette intégration est maintenue par Lob._

## À propos de l'intégration

Grâce à cette intégration, vous pouvez :

- Envoyez des lettres, des cartes postales et des chèques par courrier à l'aide des webhooks Braze et de l'API Lob.
- Partagez les événements Lob avec Braze en tant qu'attributs et attributs personnalisés à l'aide de Braze Data Transformation et de webhooks Lob.

## Conditions préalables

|Condition| Description|
| ---| ---|
|Compte Lob | Un compte Lob est nécessaire pour bénéficier de ce partenariat. |
| Clé API de Lob | Votre clé API de Lob se trouve dans la section des paramètres, sous votre nom, dans le tableau de bord de Lob. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Envoi de courrier à l'aide des webhooks de Braze

### Étape 1 : Choisissez un endpoint Lob

En fonction de ce que vous souhaitez faire dans Lob, vous devrez utiliser l'endpoint correspondant dans la requête HTTP de votre webhook. Pour des informations détaillées sur chaque endpoint, consultez la [documentation de référence de l'API de Lob.](https://lob.com/docs#intro)

| URL de base | Endpoints disponibles |
| ------------ | ------------------- |
| `https://api.lob.com/` | `/v1/addresses<br>/v1/addresses/{id}`<br>`/v1/verify`<br>`/v1/postcards`<br>`/v1/postcards/{id}`<br>`/v1/letter`<br>`/v1/letter/{id}`<br>`/v1/checks<br>/v1/checks/{id}`<br>`/v1/bank_accounts`<br>`/v1/bank_accounts/{id}`<br>`/v1/bank_accounts/{id}/verify`<br>`/v1/areas<br>/v1/areas/{id}`<br>`/v1/routes/{zip_code}`<br>`/v1/routes`<br>`/v1/countries<br>/v1/states`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 2 : Créez votre modèle de webhook Braze à Braze

Pour créer un modèle de webhook Lob à utiliser dans de futures campagnes ou Canvases, rendez-vous dans **Modèles** > **Modèles de webhook** dans le tableau de bord de Braze. 

Si vous souhaitez créer une campagne unique de webhook à Braze ou utiliser un modèle existant, sélectionnez **Webhook** à Braze lors de la création d'une nouvelle campagne.

Dans votre nouveau modèle de webhook, remplissez les champs suivants :

- **URL de webhook** : `<LOB_API_ENDPOINT>`
- **Corps de la requête** : Texte brut

#### En-têtes de requête et méthode

Lob nécessite un en-tête HTTP pour l'autorisation et une méthode HTTP. Ce qui suit sera déjà inclus dans le modèle en tant que paire clé-valeur, mais dans l'onglet **Paramètres**, vous devez remplacer le `<LOB_API_KEY>` par votre clé API Lob. Cette clé doit comporter un " : " directement après la clé et être codée en base 64. 

- **Méthode HTTP** : POST
- **En-têtes de la requête** :
  - **Autorisation**: De base `{{'<LOB_API_KEY>:' | base64_encode}}`
  - **Content-Type**: application/json

![Code du corps de la requête et URL du webhook affichés dans l'onglet de composition du générateur webhook Braze.]({% image_buster /assets/img_archive/lob_full_request.png %})

#### Corps de la demande

Voici un exemple de corps de requête pour l'endpoint Lob postcards. Bien que ce corps de requête soit fourni dans le modèle de base Lob de Braze, si vous souhaitez utiliser d'autres endpoints, vous devez ajuster vos champs Liquid en conséquence.

{% raw %}
```json
"description": "Demo Postcard",
"to": {
    "name": "{{${first_name}}} {{${last_name}}}",
    "address_line1": "{{custom_attribute.${address_line1}}}",
    "address_city": "{{custom_attribute.${address_city}}}"
    "address_zip": "{{custom_attribute.${address_zip}}}",
    "address_country": "{{custom_attribute.${address_country}}}"
},
"front": "https://lob.com/postcardfront.pdf",
"back": "https://lob.com/postcardback.pdf"
```
{% endraw %}

### Étape 3 : Prévisualisez votre requête

À ce stade, votre campagne devrait être prête à être testée et envoyée. Consultez le tableau de bord de Lob et les journaux des messages d'erreur de la console de développement de Braze si vous rencontrez des erreurs. Par exemple, l'erreur suivante a été provoquée par un en-tête d'authentification mal formaté. 

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)
{% endalert %}

![Un journal des erreurs indiquant l'heure, le nom de l'application, le canal et le message d'erreur. Le message d'erreur comprend le message d'alerte et le code d'état.]({% image_buster /assets/img_archive/error_log.png %})

## Partager des événements à l'aide des webhooks de Lob 

[Braze Data Transformation]({{site.baseurl}}/user_guide/data/data_transformation/overview) vous permet de créer et de gérer des webhooks pour automatiser le flux de données depuis des plateformes externes vers Braze. Chaque transformation se voit attribuer un endpoint unique, que d'autres plateformes peuvent utiliser comme destination de leur webhook.

{% alert important %}
Le modèle de transformation des données de Lob envoie des événements à l'aide de votre [endpoint`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track), qui consomme des points de données dans Braze. Nous vous recommandons de fixer une limite de débit dans les paramètres de votre webhook Lob, afin d'éviter une surconsommation de données.
{% endalert %}

### Étape 1 : Créer une transformation dans Braze

1. Dans le tableau de bord de Braze, accédez à **Paramètres des données** > **Transformations de données**, puis sélectionnez **Créer une transformation.**
2. Saisissez un nom court et descriptif pour votre transformation.
3. Sous **Modifier l'expérience**, sélectionnez **Utiliser un modèle**, puis recherchez Lob et cochez la case.
4. Lorsque vous avez terminé, sélectionnez **Créer une transformation.** Vous serez redirigé vers l'éditeur de transformation, que vous utiliserez à l'étape suivante.

### Étape 2 : Remplissez le modèle Lob

Avec ce modèle, vous pouvez transformer l'un de vos événements Lob en un événement et attributs personnalisés utilisables dans Braze. Suivez les commentaires en ligne pour finir de créer le modèle.

{% alert tip %}
Pour des informations détaillées sur la structure de la charge utile du webhook de Lob, voir [Lob : Utilisation des webhooks](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks).
{% endalert %}

```json
// First, this code defines a variable, "brazecall", to build up a /users/track request
// Everything from the incoming webhook is accessible via the special variable "payload". As such, you can template in desired values in your /users/track request with JavaScript dot notation, such as payload.x.y.z

// In this example, this function removes the periods and underscores of the event_type.id sent in the Lob payload so that an event id that is formatted like: `letter.processed_for_delivery` will log an event to Braze with the name `letter processed for delivery`.

function formatString(input) {
    return input.replace(/[._]/g, ' ');
}

let braze_event = formatString(payload.event_type.id);

// In this example, a metadata value passed in the Lob Webhook called 'external_ID' is being used to match the Event to the corresponding Braze user.

let brazecall = {
  "attributes": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "Most Recent Mailer": payload.body.description
    }
  ],
  "events": [
    {
      "external_id": payload.body.metadata.external_id,
      "_update_existing_only": true,
      "name": braze_event,
      "time": new Date().toISOString(),
// Customize the properties to the Lob event you are syncing. Our example below pulls in the Tracking Events array of objects associated with certain Lob events.
      "properties": {
        "tracking_events": payload.body.tracking_events
      }
    }
  ]
};
// After the /users/track request is assigned to brazecall, you will want to explicitly return brazecall to create an output
return brazecall;
```

### Étape 3 : Créer un webhook dans Lob

1. Lorsque vous avez fini de créer votre modèle, sélectionnez **Activer**, puis copiez l' **URL du webhook** dans votre presse-papiers.
2. Dans Lob, [créez un nouveau webhook](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks#receiving-a-webhook-1), puis utilisez votre URL webhook de Braze pour recevoir le webhook.
