---
nav_title: Erreurs et réponses
article_title: Erreurs et réponses d’API
description: "Cet article de référence couvre les diverses erreurs et réponses du serveur qui peuvent apparaître lors de l’utilisation de l’API Braze et la façon de les résoudre." 
page_type: reference
page_order: 2.3

---
# Erreurs et réponses d’API

> Cet article de référence couvre les diverses erreurs et réponses du serveur qui peuvent apparaître lors de l’utilisation de l’API Braze et la façon de les résoudre. 

{% raw %}

## Réponses du serveur

Si votre charge utile POST a été acceptée par nos serveurs, les messages réussis seront reçus avec la réponse suivante :

```json
{
  "message" : "success"
}
```

Notez que la réussite signifie que la charge utile de l’API RESTful a été correctement créée et transmise à notre notification push ou à nos e-mails ou autres services de messagerie. Cela ne signifie pas que les messages ont effectivement été envoyés, car des facteurs supplémentaires peuvent empêcher l'envoi du message (par exemple, un appareil peut être hors ligne, le jeton push peut être rejeté par les serveurs d'Apple, vous pouvez avoir fourni un ID utilisateur inconnu).

Si votre message est réussi, mais que vous avez des erreurs non fatales, vous recevrez la réponse suivante :

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

Dans le cas d’un succès, tout message n’ayant pas été affecté par une erreur du tableau `errors` sera toujours livré. Si votre message contient une erreur fatale, vous recevrez la réponse suivante :

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Réponses pour les ID d’envoi suivis

Les analyses sont toujours disponibles pour les campagnes. De plus, les analyses sont disponibles pour une instance spécifique de campagne lorsque celle-ci est envoyée en tant que diffusion. Lorsque le suivi est disponible pour une instance spécifique de campagne, vous recevrez la réponse suivante :

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

L'ID d'envoi fourni peut être utilisé comme paramètre pour l'endpoint `/send/data_series` afin d'obtenir des analyses/analytiques spécifiques à l'envoi.

## Erreurs

L’élément du code d’état d’une réponse serveur est un numéro à 3 chiffres où le premier chiffre du code définit la classe de réponse.

- Le code d'état de **classe 2XX** (non fatal) indique que **votre demande** a été reçue, comprise et acceptée avec succès.
- La **classe 4XX** du code de statut (fatal) indique une **erreur du client**. Reportez-vous au tableau des erreurs fatales pour obtenir une liste complète des codes d’erreur et descriptions de la classe 4XX.
- La **classe 5XX** du code de statut (fatal) indique une **erreur du serveur**. Il y a plusieurs causes possibles, par exemple, le serveur auquel vous essayez d'accéder n'est pas en mesure d'exécuter la requête, le serveur fait l'objet d'une maintenance qui l'empêche d'exécuter la requête, ou le serveur connaît des niveaux élevés de trafic. Dans ce cas, nous vous recommandons de réessayer votre demande avec un délai exponentiel. En cas d'incident ou de panne, Braze n'est pas en mesure de lire à nouveau un appel d’API REST qui a échoué pendant la fenêtre d'incident. Vous devrez réessayer les appels qui ont échoué pendant la fenêtre d'incident.
  - Une **erreur 502** est un échec avant que le message n'atteigne le serveur de destination.
  - Une **erreur 503** signifie que la demande est parvenue jusqu'au serveur de destination, mais que nous ne pouvons pas la traiter en raison d'un manque de capacité, d'un problème de réseau ou d'un problème similaire.
  - Une **erreur 504** indique qu'un serveur n'a pas reçu de réponse d'un autre serveur en amont.

### Erreurs fatales

Les codes d’état suivants et les messages d’erreur associés seront renvoyés si votre demande rencontre une erreur fatale.

{% endraw %}
{% alert warning %}
Tous les codes d’erreur suivants indiquent qu’aucun message ne sera envoyé.
{% endalert %}
{% raw %}

| Code d’erreur | Description |
|---|---|
| `5XX Internal Server Error` | Réessayer votre demande avec des délais exponentiels.|
| `400 Bad Request` | Syntaxe incorrecte.|
| `400 No Recipients` | Il n'y a pas d'ID externe ou d'ID de segmentation, ni de jetons de poussée dans la demande.|
| `400 Invalid Campaign ID` | Aucune campagne API d'envoi de messages n'a été trouvée pour l'ID de campagne que vous avez fourni.|
| `400 Message Variant Unspecified` | Vous fournissez un ID de campagne mais aucun ID de variation de message.|
| `400 Invalid Message Variant` | Vous avez fourni un ID de campagne valide, mais l’ID de modification de message ne correspond pas à l’un des messages de cette campagne.|
| `400 Mismatched Message Type` | Vous avez fourni une variation de message du mauvais type de message pour au moins un de vos messages.|
| `400 Invalid Extra Push Payload` | Vous fournissez la clé `extra` pour `apple_push` ou `android_push` mais ce n’est pas un dictionnaire.|
| `400 Max Input Length Exceeded` | Causé par l'appel de plus de 75 ID externes lors de l'atteinte de l'endpoint `/users/track`.|
| `400 The max number of external_ids and aliases per request was exceeded` | Causé par l'appel de plus de 50 ID externes.|
| `400 The max number of ids per request was exceeded` | Causé par l'appel de plus de 50 ID externes.|
| `400 No message to send` | Aucune charge utile n’est spécifiée pour le message.|
| `400 Slideup Message Length Exceeded` | Le message Slideup contient plus de 140 caractères.|
| `400 Apple Push Length Exceeded` | La charge utile JSON est supérieure à 1 912 octets.|
| `400 Android Push Length Exceeded` | La charge utile JSON est supérieure à 4 000 octets.|
| `400 Bad Request` | Impossible d’analyser l’horodatage `send_at`.|
| `400 Bad Request` | Dans votre demande, `in_local_time` est vrai, mais `time` est passé dans le fuseau horaire de votre entreprise.|
| `401 Unauthorized` | Clé API non valide. Cette erreur peut également se produire si<br><br> \- Vous envoyez la demande à la mauvaise [instance]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Par exemple, si votre compte se trouve sur notre instance européenne (`https://dashboard-01.braze.eu`), la demande doit être envoyée à `https://rest.fra-01.braze.eu`.<br>\- La syntaxe de la clé API utilise des guillemets simples ou doubles. La syntaxe correcte est `Authorization: Bearer {YOUR-API-KEY}`. |
| `403 Forbidden` | Le plan tarifaire n'est pas pris en charge ou le compte est désactivé.|
| `403 Access Denied` | La clé API REST que vous utilisez ne dispose pas d'autorisations suffisantes, vérifiez les autorisations de la clé API sous la page **Paramètres.** |
| `404 Not Found` | URL non valide. |
| `429 Rate Limited` | Limite de débit dépassée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endraw %}
