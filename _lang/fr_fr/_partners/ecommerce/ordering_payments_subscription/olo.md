---
nav_title: Olo
article_title: Olo
description: "Cet article présente le partenariat entre Braze et Olo, une plateforme SaaS ouverte de premier plan pour les restaurants qui permet de renforcer l’accueil à chaque point de contact."
alias: /partners/olo/
page_type: partner
search_tag: Partner
---

# Olo

> [Olo](https://www.olo.com/) est une plateforme SaaS ouverte de premier plan pour les restaurants qui permet de renforcer l’accueil à chaque point de contact.

En intégrant Olo et Braze, vous pouvez :

- Mettre à jour des profils utilisateurs dans Braze pour qu'ils soient cohérents avec les profils utilisateurs d'Olo
- Envoyer des messages pertinents depuis Braze en fonction d’événements Olo.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Olo | Un compte Olo avec accès aux webhooks est nécessaire pour profiter de ce partenariat. Configurez les abonnements aux webhooks via l'[outil webhooks en libre-service](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dans le tableau de bord d'Olo. |
| Transformation des données de Braze | Une [URL de transformation des données]({{site.baseurl}}/data_transformation/) est nécessaire pour recevoir des données d'Olo. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Un webhook est un moyen pour Olo d'envoyer des informations événementielles à Braze sur les utilisateurs et leurs actions, y compris des événements tels que la commande passée, l'abonnement d'un invité, la commande récupérée et plus encore. Le webhook Olo transmet l'événement à Braze généralement dans les secondes qui suivent l'exécution de l'action.

## Clause de non-responsabilité

Dans Olo, vous êtes limité à un webhook par environnement pour chaque marque approuvée, tous envoyés à la même **URL de destination**. Des marques différentes peuvent avoir des URL différents, mais les événements d'une même marque doivent partager une même URL. En Braze, cela signifie que vous ne pouvez réaliser qu'une seule transformation à utiliser avec Olo.

Pour gérer plusieurs événements Olo au sein de cette transformation unique, recherchez l'en-tête `X-Olo-Event-Type` dans chaque webhook. Cet en-tête vous permet de traiter de manière conditionnelle différents événements Olo.

## Intégration

### Étape 1 : Configurez la transformation des données de Braze pour qu'elle accepte l'événement test de Olo. {#step-1}

{% multi_lang_include create_transformation.md location="default" %}

### Étape 2 : Configurer les webhooks d'Olo

Utilisez l'[outil webhooks en libre-service](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dans le tableau de bord d'Olo pour configurer des webhooks à envoyer à votre transformation de données.

1. Choisissez les événements à envoyer à Braze
2. Configurez l'**URL de destination**. Il s'agit de l'URL de transformation des données créée à l'[étape 1](#step-1).

{% alert note %}
`OAuth` et le secret partagé de l'en-tête `X-Olo-Signature` ne sont pas nécessaires à la transformation.
{% endalert %}

{:start="3"}
3\. Vérifiez que le webhook est configuré correctement en envoyant un [événement test](https://developer.olo.com/docs/load/webhooks#operation/test) à votre transformation de données. Seuls les utilisateurs du tableau de bord d'Olo disposant de l'autorisation [Outils de développement](https://olosupport.zendesk.com/hc/en-us/articles/115001427843-Dashboard-Permissions) peuvent envoyer des événements de test.

Olo a besoin d'une réponse positive du webhook de l'événement de test avant de pouvoir terminer le processus de configuration du webhook d'Olo.

### Étape 3 : Écrire un code de transformation pour accepter les événements Olo que vous avez choisis.

Dans cette étape, vous transformerez la charge utile du webhook qui sera envoyée depuis la plateforme source en une valeur de retour d'un objet JavaScript.

1. Envoyez une requête à votre URL de transformation des données avec un exemple de charge utile d'un événement Olo que vous avez l'intention de prendre en charge. Consultez le [format du corps de la requête](#request-body-format) pour obtenir de l'aide sur le formatage de votre requête.
2. Actualisez votre transformation de données et assurez-vous que vous pouvez voir l'exemple de charge utile d'événement dans les **détails du webhook.**
3. Mettez à jour votre code de transformation des données pour prendre en charge les événements Olo que vous avez choisis.
4. Cliquez sur **Valider** pour obtenir un aperçu de la sortie de votre code et vérifier s'il s'agit d'une requête `/users/track` acceptable.
5. Enregistrez et activez votre transformation de données.

#### Format du corps de la requête

Cette valeur de retour doit respecter le format du corps de la requête `/users/track` de Braze :

- Le code de transformation est accepté dans le langage de programmation JavaScript. Tout flux de contrôle JavaScript standard, tel que la logique if/else, est pris en charge.
- Le code de transformation accède au corps de la requête de webhook via la variable payload. Cette variable est un objet rempli en analysant le JSON du corps de la requête.
- Toutes les fonctionnalités prises en charge dans notre endpoint `/users/track` sont prises en charge, y compris :
    - Objets d'attributs utilisateur, objets d'événements et objets d'achat
    - Attributs et propriétés d'événements personnalisés imbriqués
    - Mise à jour des groupes d'abonnement
    - L'adresse e-mail comme identifiant

## Exemples de transformations de données pour les webhooks Olo

Cette section contient des exemples de modèles qui peuvent être utilisés comme point de départ. N'hésitez pas à repartir de zéro ou à supprimer des éléments spécifiques si vous le souhaitez.

Dans chaque modèle, le code définit une variable, `brazecall`, pour créer une requête `/users/track`.

Une fois que la requête `/users/track `est affectée à `brazecall`, vous devez renvoyer explicitement `brazecall` pour créer une sortie.

### Transformation d'un événement unique

Si vous ne souhaitez prendre en charge qu'un seul événement Olo, vous n'aurez pas besoin d'utiliser l'en-tête `X-Olo-Event-Type` pour créer conditionnellement la charge utile de la requête `/users/track`. Par exemple, l'enregistrement d'un événement d'achat ou d'un événement personnalisé dans le profil utilisateur lorsqu'un webhook Olo Order Placed est envoyé à Braze.

### Enregistrement de chaque produit en tant qu'achat

```javascript
// iterate through the items included within the order

const purchases = payload.items.map((item) => {
 return {
   external_id: payload.customer.customerId.toString(),
   product_id: item.productId.toString(),
   currency: 'USD',
   price: item.sellingPrice,
   time: new Date().toISOString(),
   quantity: item.quantity,
   properties: {
     customValues: item.customValues
   }
 };
});

// log a purchase per item in the order

let brazecall = {
 "purchases": purchases
};

return brazecall;
```

### Enregistrement d'un événement personnalisé

```javascript
// log an event “Order Placed” to the profile that includes all items in the order as event properties.

let brazecall = { 
"events": [
   {
     "external_id": payload.customer.customerId.toString(),
     "_update_existing_only": false,
     "name": "Order Placed",
     "time": new Date().toISOString(),
     "properties": {
       "Delivery Method": payload.deliveryMethod,
       "Items": payload.items,
       "Total": payload.totals.total,
       "Location": payload.location.name
     }
   }
 ]
};

return brazecall;
```

## Transformation multi-événements

Olo envoie le type d'événement dans l'en-tête `X-Olo-Event-Type` de chaque webhook. Pour prendre en charge plusieurs événements webhook Olo au sein d'une même transformation, utilisez une logique conditionnelle pour transformer la charge utile webhook en fonction de la valeur de ce type d'en-tête.  

Dans l'exemple de transformation ci-dessous, le script JavaScript crée une charge utile particulière pour les événements `UserSignedUp` et `OrderPlaced`. En outre, une condition `else` gère une charge utile pour tous les événements Olo envoyés à Braze sans l'en-tête X-Olo-Event-Type de `UserSignedUp` et `OrderPlaced`.

```javascript
// captures the value within the X-Olo-Event-Type header for use in the conditional logic

let event_type = headers["X-Olo-Event-Type"];

// defines a variable 'brazecall' that will hold the request payload for the /users/track request

let brazecall;

// if the X-Olo-Event-Type header is 'UserSignedUp', define a variable for the different subscription statuses that could be included within the Olo event payload

if (event_type == "UserSignedUp") {
	let emailSubscribe;
	let emailSubscriptionGroup;
	let smsSubscriptionGroup;


// determine if the user has opted into marketing emails


	if (payload.allowEmail) {
		emailSubscribe = "opted_in";
		emailSubscriptionGroup = "subscribed";
	} else {
		emailSubscribe = "unsubscribed";
		emailSubscriptionGroup = "unsubscribed";
	}


	// determine if the user has opted into SMS


	if (payload.allowMarketingSms) {
		smsSubscriptionGroup = "subscribed";
	} else {
		smsSubscriptionGroup = "unsubscribed";
	}

	// build the /users/track request and pass in the appropriate subscription statuses


	brazecall = {
		"attributes": [{
			"external_id": payload.id.toString(),
			"_update_existing_only": false,
			"email": payload.emailAddress,
			"first_name": payload.firstName,
			"last_name": payload.lastName,
			"email_subscribe": emailSubscribe,
			"phone": payload.contactNumber,
			"subscription_groups": [{
					"subscription_group_id": "57e5307f-9084-490d-9d6d-8244dc919a48",
					"subscription_state": emailSubscriptionGroup
				},
				{
					"subscription_group_id": "6440ba26-86ea-47db-a935-6647941dc78b",
					"subscription_state": smsSubscriptionGroup
				}
			]
		}]
	}; // if the X-Olo-Event-Type header is 'OrderPlaced', build the /users/track request to log an event to the user profile
} else if (event_type == "OrderPlaced") {
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": false,
			"name": "Order Placed",
			"time": new Date().toISOString(),
			"properties": {
				"Delivery Method": payload.deliveryMethod,
				"Items": payload.items,
				"Total": payload.totals.total,
				"Location": payload.location.name
			}
		}]
	};
} else { // if the X-Olo-Event-Type header is anything else, build the /users/track request to log an event to the user profile
	brazecall = {
		"events": [{
			"external_id": payload.customer.customerId.toString(),
			"_update_existing_only": true,
			"name": "Another Event",
			"time": new Date().toISOString()
		}]

	};
}

// return `brazecall` to create an output.

return brazecall;
```

### Étape 4 : Publier votre webhook Olo

Après avoir activé votre transformation de données dans Braze, utilisez l'[outil webhooks en libre-service](https://olosupport.zendesk.com/hc/en-us/articles/360061153692-Self-Service-Webhooks) dans le tableau de bord de Braze pour publier votre webhook. Lorsque le webhook est publié, la transformation de données commence à recevoir des messages d'événements de webhooks d'Olo.

## Ce qu'il faut savoir

### Tentatives

Olo retentera les appels de webhook aboutissant à un code d'état de réponse HTTP de `429 - Too Many Requests` ou de l'ordre de `5xx` (par exemple, en raison d'un délai d'attente de la passerelle ou d'une erreur du serveur), jusqu'à 50 fois sur une période de 24 heures avant d'abandonner la requête.

### Au moins une fois la distribution

Si un appel webhook aboutit à un code d'état de réponse HTTP de `429 - Too Many Requests` ou de l'ordre de `5xx` (par exemple, en raison d'un dépassement de délai de la passerelle ou d'une erreur du serveur), Olo réessayera le message jusqu'à 50 fois sur une période de 24 heures avant d'abandonner.

Les webhooks peuvent donc être reçus plusieurs fois par un abonné. Il appartient à l'utilisateur abonné d'ignorer les doublons en vérifiant l'en-tête `X-Olo-Message-Id`.


