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

Notez que la réussite signifie que la charge utile de l’API RESTful a été correctement créée et transmise à notre notification push ou à nos e-mails ou autres services de messagerie. Cela ne signifie pas que les messages ont effectivement été délivrés, car des facteurs supplémentaires pourraient empêcher la délivrance du message (par exemple, un appareil pourrait être hors ligne, le jeton push pourrait être rejeté par les serveurs d'Apple, tu pourrais avoir fourni un identifiant d'utilisateur inconnu).

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

L’ID d’envoi fourni peut être utilisé comme paramètre pour que l’envoi/l’endpoint `/send/data_series` extrait des analyses spécifiques.

## Erreurs

L’élément du code d’état d’une réponse serveur est un numéro à 3 chiffres où le premier chiffre du code définit la classe de réponse.

- La **classe 2XX** du code d'état (non fatal) indique que **ta demande** a été reçue, comprise et acceptée avec succès.
- La **classe 4XX** du code de statut (fatal) indique une **erreur du client**. Reportez-vous au tableau des erreurs fatales pour obtenir une liste complète des codes d’erreur et descriptions de la classe 4XX.
- La **classe 5XX** du code de statut (fatal) indique une **erreur du serveur**. Il y a plusieurs causes potentielles : p. ex., le serveur auquel vous essayez d’accéder est incapable d’exécuter la demande, le serveur est en cours de maintenance et est donc incapable d’exécuter la demande, ou le serveur connaît un niveau élevé de trafic. Dans ce cas, nous vous recommandons de réessayer votre demande avec un délai exponentiel. En cas d'incident ou de panne, Braze n'est pas en mesure de lire à nouveau un appel d’API REST qui a échoué pendant la fenêtre d'incident. Vous devrez réessayer les appels qui ont échoué pendant la fenêtre d'incident.

### Erreurs fatales

Les codes d’état suivants et les messages d’erreur associés seront renvoyés si votre demande rencontre une erreur fatale.

{% endraw %}
{% alert warning %}
Tous les codes d’erreur suivants indiquent qu’aucun message ne sera envoyé.
{% endalert %}
{% raw %}

| Code d'erreur | Description |
|---|---|
| `5XX Internal Server Error` | Réessaie ta demande avec un backoff exponentiel.
| `400 Bad Request` | Mauvaise syntaxe.|
| `400 No Recipients` | La requête ne contient ni ID externes ni ID de segment ni jetons de notification push.|
| `400 Invalid Campaign ID` | Aucune campagne API de messagerie n'a été trouvée pour l'identifiant de campagne que tu as fourni.|
| `400 Message Variant Unspecified` | Tu as fourni un identifiant de campagne mais pas d'identifiant de variation de message.|
| `400 Invalid Message Variant` | Tu as fourni un identifiant de campagne valide, mais l'identifiant de variation du message ne correspond à aucun des messages de cette campagne.
| `400 Mismatched Message Type` | Tu as fourni une variante du mauvais type de message pour au moins un de tes messages.
| `400 Invalid Extra Push Payload` | Vous fournissez la clé `extra` pour `apple_push` ou `android_push` mais il ne s'agit pas d'un dictionnaire.|
| `400 Max Input Length Exceeded` | Causé par l'appel de plus de 75 ID externes lors de l'utilisation de l’endpoint `/users/track`.|
| `400 The max number of external_ids and aliases per request was exceeded` | Causé par l'appel de plus de 50 identifiants externes.|
| `400 The max number of ids per request was exceeded` | Causé par l'appel de plus de 50 identifiants externes.|
| `400 No message to send` | Aucune charge utile n'est spécifiée pour le message.
`400 Slideup Message Length Exceeded` | Le message de la diapositive contient plus de 140 caractères.
| `400 Apple Push Length Exceeded` | La charge utile JSON est supérieure à 1 912 octets.|
| `400 Android Push Length Exceeded` | La charge utile JSON est supérieure à 4 000 octets.|
| `400 Bad Request` | Impossible d'analyser `send_at` datetime.|
| `400 Bad Request` | Dans ta demande, `in_local_time` est vrai mais `time` est passé dans le fuseau horaire de ton entreprise.|
| `401 Unauthorized` | Clé API invalide |
| `403 Forbidden` | Le plan tarifaire n'est pas pris en charge, ou le compte est autrement inactivé.|
| `403 Access Denied` | La clé API REST que vous utilisez n'a pas les autorisations suffisantes, vérifiez les autorisations de la clé API dans la page **Paramètres**.|
| `404 Not Found` | URL non valide. |
| `429 Rate Limited` | Dépassement de la limite de débit. |
{: .reset-td-br-1 .reset-td-br-2}

{% endraw %}
