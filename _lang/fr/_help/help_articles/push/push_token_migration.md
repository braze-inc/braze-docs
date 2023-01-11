---
nav_title: Migration des jetons Push
article_title: Migration des jetons Push
page_order: 2

page_type: solution
description: "Cet article explique comment migrer les jetons push pour pouvoir continuer à envoyer des messages push à vos utilisateurs après être passé à Braze."
channel: notification push
---

# Migration des jetons Push

Un [jeton push]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/) est une clé unique, créée et assignée par Apple ou Google pour créer une connexion entre une application et un appareil iOS, Android ou Web. La migration de jetons push est l’importation de ces clés déjà générées dans la plateforme Braze.

Les clients Braze qui envoyaient auparavant des notifications push, soit par eux-mêmes soit avec un autre fournisseur, disposent souvent d’une liste d’utilisateurs qui ont des jetons push enregistrés.

Pour continuer à envoyer des messages push à ces utilisateurs pendant le processus d’intégration du SDK Braze, vous pouvez importer ces jetons dans Braze et cibler ces utilisateurs à l’aide de l’outil de campagne Braze.

{% comment %}
Ces campagnes devront être configurées avec des paires valeur clé appropriées pour garantir que la configuration de notification push existante du client reconnaîtra et affichera la charge utile de push que nous envoyons aux appareils des utilisateurs. Nous enregistrerons le nombre de notifications push que nous envoyons, mais aucune donnée sur les taux d’ouverture ou les événements de conversion ne sera suivie, car cela nécessite l’intégration du SDK Braze.
{% endcomment %}

## Migration via API

Les jetons peuvent être chargés pour des utilisateurs identifiés ou des utilisateurs anonymes. Cela signifie que soit un `external_id` doit être présent, soit les utilisateurs anonymes doivent avoir le flag `push_token_import` défini sur `true`. 

Les `app_id` sont disponibles dans **Developer Console**, sous l’onglet **API Settings** (Paramètres API) dans la section **Identification**. Chaque application (iOS, Android, Web, etc.) a sa propre `app_id`. Assurez-vous d’utiliser les bonnes `app_id` pour chaque plateforme.

#### Migration si l’ID externe est présent
```json
"attributes" : [
  {
	"push_token_import" : false,
	"external_id": "external_id1",
	"country": "US",
	"language": "en",
	"YOUR_CUSTOM_ATTRIBUTE": "YOUR_VALUE",
	"push_tokens": [
	  {"app_id": "APP_ID_OF_OS", "token": "PUSH_TOKEN_STRING"}
	]
  }
]
```

{% alert note %}
Lors de l’importation de jetons de notification push provenant d’autres systèmes, un `external_id` n’est pas toujours disponible. Pour maintenir la communication avec ces utilisateurs pendant votre transition vers Braze, vous pouvez importer les jetons existants pour les utilisateurs anonymes sans fournir `external_id`, en spécifiant `push_token_import` comme `true`.
{% endalert %}

#### Migration si l’ID externe n’est pas présent

Ces jetons peuvent être migrés en les important avec notre [API]({{site.baseurl}}/api/endpoints/user_data/#push-token-import). Pour ce faire, utilisez l’endpoint `users/track` et publiez les informations suivantes :

```json
"attributes" : [
  {
	"push_token_import" : true,
	"push_tokens": [
	  { "app_id": "", "token": "", "device_id": "" }
	]
  }
]
```

##### Exemple

```json
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

En spécifiant `push_token_import` en tant que `true`, gardez à l’esprit :
* `external_id` et `braze_id` ne doit pas être spécifié
* L’objet d’attribut doit contenir un jeton de notification push
* Si le jeton existe déjà dans Braze, la demande est ignorée ; sinon, Braze créera un profil utilisateur temporaire et anonyme pour chaque jeton pour vous permettre de continuer à envoyer des messages à ces personnes

Après l’importation, lorsque chaque utilisateur lance la version compatible Braze de votre application, Braze déplace automatiquement leur jeton de notification push importé vers leur profil utilisateur Braze et efface le profil temporaire.

Braze vérifiera une fois par mois s’il existe des profils anonymes avec l’indicateur `push_token_import` qui n’ont pas de jeton de notification push. Si le profil anonyme n’a plus de jeton de notification push, nous le supprimerons. Cependant, si le profil anonyme a toujours un jeton push, ce qui suggère que l’utilisateur réel ne se s’est pas encore connecté sur l’appareil avec le jeton push en question, nous ne ferons rien.

### Jetons push Web
{% alert warning %}
Braze ne prend pas en charge la migration des jetons de notification push Web via l’API. En effet, les jetons de notification push Web contiennent des champs supplémentaires que les autres plateformes n’ont pas. 

<br>Si vous tentez de migrer des jetons de notification push Web par programmation, une erreur semblable à celle-ci peut s’afficher :`Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
En guise d’alternative, nous vous recommandons d’intégrer les notifications push et de permettre à votre base de jetons de se remplir naturellement de nouveau.
{% endalert %}


## Envoi de push avant l’intégration du SDK Braze (Android uniquement)

{% alert warning %}
Cette solution s’applique uniquement aux utilisateurs Android. Les utilisateurs iOS ne recevront pas de push avec cette méthode. iOS ne nécessite pas ces étapes, car il n’y a qu’un seul framework pour afficher les notifications push. Les notifications push s’effectueront immédiatement tant que Braze dispose des jetons et certificats push nécessaires.
{% endalert %}

Si vous devez envoyer une notification push à vos utilisateurs avant d’avoir terminé l’intégration du SDK Braze, vous pouvez utiliser des paires valeur-clé pour valider les notifications push. 

Vous devez disposer d’un récepteur pour manipuler et afficher les charges utiles de push. Pour notifier le récepteur de la charge utile de push, ajoutez les paires valeur-clé nécessaires à la campagne push. Les valeurs de ces paires dépendent du partenaire push spécifique que vous utilisiez avant Braze.

{% alert note %}
Pour certains fournisseurs de notifications push, le Braze devra aplanir les paires valeur-clé pour qu’elles puissent être interprétées correctement. Pour aplanir les paires valeur-clé pour une application Android spécifique, contactez votre gestionnaire de la réussite ou gestionnaire de l’Onboarding Client.
{% endalert %}

_Dernière mise à jour le 1er juin 2021_

