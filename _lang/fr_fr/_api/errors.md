---
nav_title: Erreurs et réponses
article_title: Erreurs et réponses d'API
description: "Cet article de référence couvre les diverses erreurs et réponses du serveur qui peuvent apparaître lors de l'utilisation de l'API Braze et la façon de les résoudre."
page_type: reference
page_order: 2.3

---
# Erreurs et réponses d'API

> Cet article de référence couvre les diverses erreurs et réponses du serveur qui peuvent apparaître lors de l'utilisation de l'API Braze et la façon de les résoudre.

## Réponses du serveur

Si votre PAYLOAD POST a été acceptée par nos serveurs, les messages réussis sont accompagnés de la réponse suivante :

```json
{
  "message" : "success"
}
```

Notez que le succès signifie uniquement que la PAYLOAD de l'API RESTful a été correctement formée et transmise à notre service de notification push, à notre service d'envoi d'e-mails ou à d'autres services d'envoi de messages. Cela ne signifie pas que les messages ont été effectivement remis, car d'autres facteurs peuvent empêcher la remise du message (par exemple, un appareil peut être hors ligne, le jeton de notification push peut être rejeté par les serveurs Apple ou vous avez peut-être fourni un ID utilisateur inconnu).

Pour les endpoints tels que [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify), qui n'envoient pas de messages, un message de réussite signifie uniquement que Braze a bien reçu la demande de traitement. Si aucune correspondance n'est trouvée pour l'alias après traitement, la requête est interrompue.

Si votre message est accepté mais contient des erreurs non fatales, vous recevrez la réponse suivante :

```json
{
  "message" : "success", "errors" : [<minor error message>]
}
```

En cas de réussite, tous les messages qui n'ont pas été affectés par une erreur dans le tableau `errors` sont tout de même livrés. Si votre message contient une erreur fatale, vous recevrez la réponse suivante :

```json
{
  "message" : <fatal error message>, "errors" : [<minor error message>]
}
```

## Réponses pour les ID d'envoi suivis

Les analyses sont toujours disponibles pour les campagnes. De plus, les analyses sont disponibles pour une instance spécifique d'envoi de campagne lorsque celle-ci est envoyée en tant que diffusion. Lorsque le suivi est disponible pour une instance d'envoi de campagne spécifique, vous recevez la réponse suivante :

```json
{
  "message": "success", "send_id" : "example_send_id"
}
```

L'ID d'envoi fourni peut être utilisé comme paramètre pour l'endpoint `/send/data_series` afin d'obtenir des analyses spécifiques à l'envoi.

## Erreurs

L'élément du code d'état d'une réponse serveur est un numéro à 3 chiffres dont le premier chiffre définit la classe de réponse.

- Le code d'état de **classe 2XX** (non fatal) indique que **votre demande** a été reçue, comprise et acceptée avec succès.
- La **classe 4XX** du code d'état (fatal) indique une **erreur du client**. Reportez-vous au tableau des erreurs fatales pour obtenir une liste complète des codes d'erreur et descriptions de la classe 4XX.
- La **classe 5XX** du code d'état (fatal) indique une **erreur du serveur**. Il y a plusieurs causes possibles : par exemple, le serveur auquel vous essayez d'accéder n'est pas en mesure d'exécuter la requête, le serveur fait l'objet d'une maintenance qui l'empêche d'exécuter la requête, ou le serveur connaît des niveaux élevés de trafic. Dans ce cas, nous vous recommandons de réessayer votre demande avec des délais exponentiels. En cas d'incident ou de panne, Braze n'est pas en mesure de rejouer un appel d'API REST qui a échoué pendant la fenêtre d'incident. Il est nécessaire de réessayer tout appel qui a échoué pendant la période de l'incident.
  - Une **erreur 502** est un échec avant que la requête n'atteigne le serveur de destination.
  - Une **erreur 503** signifie que la demande est parvenue jusqu'au serveur de destination, mais que nous ne pouvons pas la traiter en raison d'un manque de capacité, d'un problème de réseau ou d'un problème similaire.
  - Une **erreur 504** indique qu'un serveur n'a pas reçu de réponse d'un autre serveur en amont.

### Erreurs fatales

Les codes d'état suivants et les messages d'erreur associés sont renvoyés si votre demande rencontre une erreur fatale.

{% alert warning %}
Tous les codes d'erreur suivants indiquent qu'aucun message n'a été envoyé.
{% endalert %}

| Code d'erreur | Description |
|---|---|
| `5XX Internal Server Error` | Réessayez votre demande avec des délais exponentiels.|
| `400 Bad Request` | Syntaxe incorrecte.|
| `400 No Recipients` | Il n'y a pas d'ID externe ou d'ID de segment, ni de jetons de notification push dans la demande.|
| `400 Invalid Campaign ID` | Aucune campagne API d'envoi de messages n'a été trouvée pour l'ID de campagne que vous avez fourni.|
| `400 Message Variant Unspecified` | Vous fournissez un ID de campagne mais aucun ID de variante de message.|
| `400 Invalid Message Variant` | Vous avez fourni un ID de campagne valide, mais l'ID de variante de message ne correspond à aucun des messages de cette campagne.|
| `400 Mismatched Message Type` | Vous avez fourni une variante de message du mauvais type pour au moins un de vos messages.|
| `400 Invalid Extra Push Payload` | Vous fournissez la clé `extra` pour `apple_push` ou `android_push` mais ce n'est pas un dictionnaire.|
| `400 Max Input Length Exceeded` | Pour `/users/track`, cette erreur est causée par le dépassement du nombre maximum d'objets autorisés dans une seule requête. La limite dépend du modèle de limite de débit : pour la plupart des clients, chaque requête prend en charge jusqu'à 75 objets au total, répartis entre `attributes`, `events` et `purchases`. Pour les clients soumis aux anciennes limites de débit, chaque tableau prend en charge jusqu'à 75 objets indépendamment. Pour en savoir plus, consultez [POST : Créer et mettre à jour des utilisateurs]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).|
| `400 The max number of external_ids and aliases per request was exceeded` | Causé par l'appel de plus de 50 ID externes.|
| `400 The max number of ids per request was exceeded` | Causé par l'appel de plus de 50 ID externes.|
| `400 No message to send` | Aucune PAYLOAD n'est spécifiée pour le message.|
| `400 Slideup Message Length Exceeded` | Le message contextuel contient plus de 140 caractères.|
| `400 Apple Push Length Exceeded` | La PAYLOAD JSON est supérieure à 1 912 octets.|
| `400 Android Push Length Exceeded` | La PAYLOAD JSON est supérieure à 4 000 octets.|
| `400 Bad Request` | Impossible d'analyser l'horodatage `send_at`.|
| `400 Bad Request` | Dans votre demande, `in_local_time` est vrai, mais `time` est déjà passé dans le fuseau horaire de votre société.|
| `401 Unauthorized` | Clé API non valide. Les causes courantes incluent :<br><br>- **En-tête Authorization manquant ou mal formé.** La valeur de l'en-tête doit être `Bearer` suivi d'un espace puis de votre clé API : `Authorization: Bearer YOUR-API-KEY`. Les erreurs courantes incluent l'omission de `Bearer`, l'omission de la clé après `Bearer`, ou l'encadrement de la valeur par des guillemets.<br>- **Mauvais endpoint REST.** Vous envoyez la demande à la mauvaise [instance]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints/). Par exemple, si votre compte se trouve sur notre instance européenne (`https://dashboard-01.braze.eu`), la demande doit être envoyée à `https://rest.fra-01.braze.eu`.<br>- **Autorisations insuffisantes.** Chaque clé API est associée à un espace de travail et à un ensemble d'autorisations spécifiques. Vérifiez les autorisations de la clé sous **Paramètres** > **Clés API** dans le tableau de bord.<br>- **Mauvaise clé API.** Les clés API sont spécifiques à un espace de travail. Une clé d'un espace de travail ne peut pas être utilisée pour authentifier des demandes destinées à un autre espace de travail. |
| `403 Forbidden` | Le plan tarifaire ne prend pas en charge cette fonctionnalité ou le compte est désactivé.|
| `403 Access Denied` | La clé API REST que vous utilisez ne dispose pas d'autorisations suffisantes. Les causes courantes incluent : {::nomarkdown}<ul><li><strong>La clé API est antérieure à la fonctionnalité.</strong> Si la clé API a été créée avant le lancement d'une fonctionnalité (comme les Groupes d'abonnement ou les Catalogues), la clé n'hérite pas automatiquement de ces autorisations. Créez une nouvelle clé API avec les autorisations requises sous <strong>Paramètres</strong> &gt; <strong>Clés API</strong>.</li><li><strong>Autorisation spécifique à l'endpoint manquante.</strong> Chaque endpoint d'API nécessite un périmètre d'autorisation spécifique (par exemple, <code>users.track</code> ou <code>email.status</code>). Vérifiez que les autorisations de la clé correspondent à l'endpoint que vous appelez.</li><li><strong>Barre oblique finale ou faute de frappe dans l'URL.</strong> Par exemple, <code>/users/track/</code> (avec une barre oblique finale) au lieu de <code>/users/track</code> peut produire des erreurs inattendues.</li></ul>{:/}|
| `404 Not Found` | URL non valide. |
| `415 Unsupported Media Type` | L'en-tête de requête `Content-Type` est manquant ou incorrect. Dans la page **Paramètres**, ajoutez `Content-Type` avec la valeur `application/json`. |
| `429 Rate Limited` | Limite de débit dépassée. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }