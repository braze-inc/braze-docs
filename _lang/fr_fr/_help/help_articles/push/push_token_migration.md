---
nav_title: Migration des jetons Push
article_title: Migration des jetons Push
page_order: 0

page_type: solution
description: "Cet article de référence explique comment migrer les jetons push pour pouvoir continuer à envoyer des messages push à vos utilisateurs après être passé à Braze."
channel: push
---

# Migration des jetons Push

> Un [jeton de notification]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#push-tokens/) est un identifiant anonyme unique qui spécifie où envoyer les notifications d'une application. Braze se connecte à des fournisseurs de services push comme Firebase Cloud Messaging Service (FCMs) pour Android et Apple Push Notification Service (APN) pour iOS, et ces fournisseurs envoient des jetons d’appareil uniques qui identifient votre application. Si vous envoyiez des notifications push avant d'intégrer Braze, soit par vous-même, soit par un autre fournisseur, la migration des jetons push vous permet de continuer à envoyer des notifications push à vos utilisateurs avec des jetons push enregistrés.

## Migration automatique via SDK

Après avoir [intégré le SDK de Braze]({{site.baseurl}}/developer_guide/sdk_integration/), les jetons de push de vos utilisateurs abonnés seront automatiquement migrés la prochaine fois qu'ils ouvriront votre application. En attendant, vous ne pourrez pas envoyer à ces utilisateurs des notifications push via Braze.

Vous pouvez également [migrer vos jetons push manuellement](#manual-migration-via-api), ce qui vous permettra de réengager vos utilisateurs plus rapidement.

### Considérations relatives aux jetons Web

En raison de la nature des jetons de push pour le web, veillez à prendre en compte les éléments suivants lors de la mise en œuvre du push pour le web :

|Considération|Détails|
|----------------------|------------|
| **Service de traitement**  | Par défaut, le SDK Web recherche un service de traitement à l'adresse `./service-worker`, sauf si une autre option est spécifiée, telle que `manageServiceWorkerExternally` ou `serviceWorkerLocation`. Si votre service de traitement n'est pas configuré correctement, vos utilisateurs risquent de voir leurs jetons push expirer. |
| **Jetons expirés**   | Si un utilisateur n'a pas démarré de session web dans les 60 jours, son jeton push expirera. Comme Braze ne peut pas migrer les jetons push expirés, vous devrez envoyer une [amorce de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages) pour les réengager. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Migration manuelle via API

La migration manuelle des jetons push est le processus d'importation de ces clés précédemment créées dans votre plateforme Braze via l'API.

Migrez par programme les jetons iOS (APNs) et Android (FCM) vers votre plateforme en utilisant le [`users/track` point de terminaison]({{site.baseurl}}/api/endpoints/user_data/post_user_track/). Vous pouvez migrer à la fois les utilisateurs identifiés (utilisateurs avec un ID externe associé) et les utilisateurs anonymes (utilisateurs sans ID externe).

Spécifiez votre `app_id` lors de la migration du jeton de notification pour associer le jeton de notification approprié à l'application appropriée. Chaque application (iOS, Android, etc.) a son propre `app_id`, qui peut être trouvé dans la section **Identification** de la page [Clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/). Assurez-vous d’utiliser les bonnes `app_id` pour chaque plateforme.

{% alert important %}
Il n’est pas possible de faire migrer les jetons push Web via l’API. En effet, les jetons push Web n’utilisent pas le même schéma que les autres plateformes. 

<br>Si vous tentez de migrer des jetons de notification push Web par programmation, une erreur semblable à celle-ci peut s’afficher :`Received '400: Invalid subscription auth' sending to 'https://fcm.googleapis.com/fcm/send`

<br>
En guise d’alternative à la migration via API, nous vous recommandons d’intégrer le SDK et de permettre à votre base de jetons de se remplir naturellement de nouveau.
{% endalert %}

{% tabs local %}
{% tab ID externe présent %}
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
}'
```
{% endtab %}

{% tab ID externe manquant %}
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
}'
```

Après l'importation, lorsque l'utilisateur anonyme lance la version de votre application activée par Braze, Braze déplacera automatiquement leur jeton de notification importé vers leur profil utilisateur Braze et nettoiera le profil temporaire.

Braze vérifiera une fois par mois s’il existe des profils anonymes avec l’indicateur `push_token_import` qui n’ont pas de jeton de notification push. Si le profil anonyme n’a plus de jeton de notification push, nous le supprimerons. Cependant, si le profil anonyme a toujours un jeton de notification push, indiquant que l’utilisateur ne s’est pas encore connecté à l’appareil avec le jeton de notification push, nous ne ferons rien.
{% endtab %}
{% endtabs %}

## Importation de jetons push Android

{% alert important %}
Les éléments suivants ne s’appliquent qu’aux applications Android. Les applications iOS ne nécessiteront pas ces étapes, car cette plateforme ne dispose que d’un seul cadre pour afficher les notifications push, et les notifications push s’afficheront immédiatement tant que Braze dispose des jetons push et des certificats nécessaires.
{% endalert %}

Si vous devez envoyer une notification push Android à vos utilisateurs avant d’avoir terminé l’intégration du SDK Braze, utilisez des paires clé-valeur pour valider les notifications push. 

Vous devez disposer d’un récepteur pour manipuler et afficher les charges utiles de push. Pour notifier le récepteur de la charge utile de push, ajoutez les paires valeur-clé nécessaires à la campagne push. Les valeurs de ces paires dépendent du partenaire push spécifique que vous utilisiez avant Braze.

{% alert note %}
Pour certains fournisseurs de notifications push, le Braze devra aplanir les paires clé-valeur pour qu’elles puissent être interprétées correctement. Pour aplanir les paires clé-valeur pour une application Android spécifique, contactez votre gestionnaire de la réussite ou gestionnaire de l’Onboarding Client.
{% endalert %}

_Dernière mise à jour le 5 décembre 2022_
