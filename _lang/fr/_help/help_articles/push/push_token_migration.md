---
nav_title: Migration des jetons Push
article_title: Migration des jetons Push
page_order: 2

page_type: solution
description: "Cet article explique comment migrer les jetons push pour pouvoir continuer à envoyer des messages push à vos utilisateurs après être passé à Braze."
channel: push
---

# Migration des jetons Push

Un [jeton push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/) est un identifiant anonyme unique qui indique où envoyer les notifications d’une application. La migration des jetons push fait référence au processus d’importation des clés précédemment créées dans votre plateforme Braze via l’API.

Si vous êtes un client qui envoyait auparavant des notifications push, que ce soit par vous-même ou par l’intermédiaire d’un autre fournisseur, la migration des jetons push vous permet de continuer à envoyer des notifications push à vos utilisateurs avec des jetons push enregistrés pendant le processus d’implémentation du SDK. Une fois les SDK Braze mis en place, ils gèrent automatiquement les jetons de notification push sans avoir besoin de les faire migrer via l’API.

## Migration via API

Programmez la migration des jetons push iOS et Android vers votre plateforme en utilisant l’endpoint [`users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Vous pouvez migrer à la fois les utilisateurs identifiés (utilisateurs avec un `external_id` associé) et les utilisateurs anonymes (utilisateurs sans `external_id`).

Vous devez indiquer le `app_id` de votre application pendant la migration du jeton push pour associer le jeton push approprié à l’application appropriée. Chaque application (iOS, Android, etc.) possède son propre `app_id`, que vous trouverez dans la **Developer Console**, sous l’onglet **API Settings (Paramètres API)** dans la section **Identification**. Assurez-vous d’utiliser les bonnes `app_id` pour chaque plateforme.

{% alert important %}
Il n’est pas possible de faire migrer les jetons push Web via l’API. En effet, les jetons push Web n’utilisent pas le même schéma que les autres plateformes. 

<br>Si vous tentez de faire migrer des jetons push Web par programmation, une erreur semblable à celle-ci peut s’afficher : `« 400 : Invalid subscription auth (Autorisation d’abonnement non valide) » reçue et envoyée à https://fcm.googleapis.com/fcm/send`

<br>
En guise d’alternative à la migration via API, nous vous recommandons d’intégrer le SDK et de permettre à votre base de jetons de se remplir naturellement de nouveau.
{% endalert %}


### Migration si l’ID externe est présent
Pour les utilisateurs identifiés, définissez l’indicateur `push_token_import` sur `false` (ou omettez le paramètre) et spécifiez les valeurs `external_id`, `app_id` et `token` dans l’objet `attributes` utilisateur. 

Par exemple :

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
"attributes" : [
  {
	"push_token_import" : false,
	"external_id": "example_external_id",
	"country": "US",
	"language": "en",
	"YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
	"push_tokens": [
	  {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
	]
  }
]
```

### Migration si l’ID externe n’est pas présent
Lors de l’importation de jetons de notification push provenant d’autres systèmes, un `external_id` n’est pas toujours disponible. Dans ce cas, définissez votre indicateur `push_token_import` sur `true` et spécifiez les valeurs `app_id` et `token`. Braze créera un profil utilisateur temporaire et anonyme pour chaque jeton pour vous permettre de continuer à envoyer des messages à ces personnes. Si le jeton existe déjà dans Braze, la demande sera ignorée.

Par exemple :

```json
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-API-KEY-HERE' \
--data-raw '{
"attributes": [ 
  {
	"push_token_import" : true,
	"email": "braze.test1@testbraze.com",
	"country": "US",
	"language": "en",
	"YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
	"push_tokens": [
	  {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}
	]
  },
    
  {
	"push_token_import" : true,
	"email": "braze.test2@testbraze.com",
	"country": "US",
	"language": "en",
	"YOUR_CUSTOM_ATTRIBUTE_1": "YOUR_VALUE",
	"YOUR_CUSTOM_ATTRIBUTE_2": "YOUR_VALUE",
	"push_tokens": [
	  {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING", "device_id": "DEVICE_ID"}  
	]
  }
]
```

Après l’importation, lorsque l’utilisateur anonyme lance la version de votre application compatible avec Braze, Braze déplace automatiquement leur jeton de notification push importé vers leur profil utilisateur Braze et efface le profil temporaire.

Braze vérifiera une fois par mois s’il existe des profils anonymes avec l’indicateur `push_token_import` qui n’ont pas de jeton de notification push. Si le profil anonyme n’a plus de jeton de notification push, nous le supprimerons. Cependant, si le profil anonyme a toujours un jeton de notification push, indiquant que l’utilisateur ne s’est pas encore connecté à l’appareil avec le jeton de notification push, nous ne ferons rien.

## Importation de jetons push Android

{% alert important %}
Les éléments suivants ne s’appliquent qu’aux applications Android. Les applications iOS ne nécessiteront pas ces étapes, car cette plateforme ne dispose que d’un seul cadre pour afficher les notifications push, et les notifications push s’afficheront immédiatement tant que Braze dispose des jetons push et des certificats nécessaires.
{% endalert %}

Si vous devez envoyer une notification push Android à vos utilisateurs avant d’avoir terminé l’intégration du SDK Braze, utilisez des paires clé-valeur pour valider les notifications push. 

Vous devez disposer d’un récepteur pour manipuler et afficher les charges utiles de push. Pour notifier le récepteur de la charge utile de push, ajoutez les paires valeur-clé nécessaires à la campagne push. Les valeurs de ces paires dépendent du partenaire push spécifique que vous utilisiez avant Braze.

{% alert note %}
Pour certains fournisseurs de notifications push, le Braze devra aplanir les paires clé-valeur pour qu’elles puissent être interprétées correctement. Pour aplanir les paires clé-valeur pour une application Android spécifique, contactez votre gestionnaire de la réussite ou gestionnaire de l’Onboarding Client.
{% endalert %}

_Dernière mise à jour le 5 décembre 2022_