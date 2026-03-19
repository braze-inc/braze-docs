---
page_order: 1.5
nav_title: Lecture des journaux détaillés
article_title: Lecture des journaux détaillés
description: "Apprenez à lire et à interpréter les journaux détaillés générés par le SDK Braze, y compris les entrées clés pour les notifications push, les messages in-app, les cartes de contenu et les liens profonds."
---

# Lecture des journaux détaillés

> Cette page explique comment interpréter les informations détaillées du journal généré par le SDK Braze. Pour chaque canal de communication, vous trouverez les entrées de journal importantes à rechercher, leur signification et les problèmes courants à surveiller.

Avant de commencer, veuillez vous assurer que vous avez [activé la journalisation détaillée]({{site.baseurl}}/developer_guide/sdk_integration/verbose_logging) et que vous savez comment collecter les journaux sur votre plateforme.

## Sessions

Les sessions constituent la base de l'analyse/analytique et de la réception/distribution des messages de Braze. De nombreuses fonctionnalités d'envoi de messages, notamment les messages in-app et les cartes de contenu, nécessitent une session valide avant de pouvoir fonctionner. Si les sessions ne sont pas enregistrées correctement, veuillez d'abord examiner ce point. Pour plus d'informations sur l'activation du suivi des sessions, veuillez vous référer à [l'étape 5 : Veuillez activer le suivi des ]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_step-5-enable-user-session-tracking)sessions utilisateur.

### Entrées du journal des touches

{% tabs %}
{% tab Swift %}

**Début de la session :**

```
Started user session (id: <SESSION_ID>)
```

**Fin de la session :**

```
Ended user session (id: <SESSION_ID>, duration: <DURATION>s)
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: sessionEnd(duration: <DURATION>)
```

{% endtab %}
{% tab Android %}

**Début de la session :**

Veuillez rechercher les entrées suivantes :

```
New session created with ID: <SESSION_ID>
Session start event for new session received
Completed the openSession call
Opened session with activity: <ACTIVITY_NAME>
```

Filtrez les requêtes réseau pour votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) afin de visualiser l'événement de début de session (`ss`).

**Fin de la session :**

```
Closed session with activity: <ACTIVITY_NAME>
Closed session with session ID: <SESSION_ID>
Requesting data flush on internal session close flush timer.
```

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- Veuillez vérifier qu'un journal de démarrage de session s'affiche lorsque l'application est lancée.
- Si vous ne constatez pas le démarrage d'une session, veuillez vérifier que le SDK est correctement initialisé et que`openSession`(Android) est appelé.
- Sur Android, veuillez vérifier qu'une requête réseau est bien envoyée à l'endpoint Braze. Si vous ne voyez pas cela, veuillez vérifier votre clé API et la configuration de l'endpoint.

## Notifications push

Les journaux des notifications push vous permettent de vérifier que les jetons des appareils sont enregistrés, que les notifications sont bien envoyées et que les clics sont bien suivis.

### Enregistrement des jetons

Lorsqu'une session commence, le SDK enregistre le jeton push de l'appareil auprès de Braze.

{% tabs %}
{% tab Swift %}

```
Updated push notification authorization:
- authorization: authorized

Received remote notifications device token: <PUSH_TOKEN>
```

Filtrez les requêtes adressées à votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) et recherchez les attributs suivants`push_token`dans le corps de la requête :

```
"attributes": [
  {
    "push_token": "<PUSH_TOKEN>",
    "user_id": "<USER_ID>"
  }
]
```

Veuillez également vérifier que les informations relatives à l'appareil comprennent :

```
"device": {
  "ios_push_auth": "authorized",
  "remote_notification_enabled": 1
}
```

{% endtab %}
{% tab Android %}

Veuillez rechercher le journal d'enregistrement FCM :

```
Registering for Firebase Cloud Messaging token using sender id: <SENDER_ID>
```

Veuillez vérifier les éléments suivants :

- `com_braze_firebase_cloud_messaging_registration_enabled` est `true`.
- L'ID de l'expéditeur FCM correspond à votre projet Firebase.

Une erreur courante est `SENDER_ID_MISMATCH`, ce qui signifie que l'ID de l'expéditeur configuré ne correspond pas à votre projet Firebase.

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- Si`push_token`  est absent du corps de la requête, cela signifie que le jeton n'a pas été capturé. Veuillez vérifier la configuration des notifications push dans les paramètres de votre application.
- Si`ios_push_auth`  affiche`denied`  ou `provisional`, l'utilisateur n'a pas accordé l'autorisation push complète.
- Sur Android, si vous voyez `SENDER_ID_MISMATCH`, veuillez mettre à jour votre ID d'expéditeur FCM afin qu'il corresponde à votre projet Firebase.

### Réception/distribution express et clic

Lorsqu'une notification push est sélectionnée, le SDK enregistre les événements de traitement et de clic.

{% tabs %}
{% tab Swift %}

```
Processing push notification:
- date: <TIMESTAMP>
- silent: false
- userInfo: {
  "ab": { ... },
  "ab_uri": "<DEEP_LINK_OR_URL>",
  "aps": {
    "alert": {
      "body": "<MESSAGE_BODY>",
      "title": "<MESSAGE_TITLE>"
    }
  }
}
```

Suivi de l'événement de clic :

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: pushClick(campaignId: ...)
```

Si la notification contient un lien profond, vous verrez également :

```
Opening '<URL>':
- channel: notification
- useWebView: false
- isUniversalLink: false
```

{% endtab %}
{% tab Android %}

```
BrazeFirebaseMessagingService: Got Remote Message from FCM
```

Veuillez noter que la charge utile de la poussée et les journaux d'affichage suivent. Pour les liens profonds, veuillez rechercher les entrées Deep Link`UriAction` Delegate ou.

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- Veuillez vérifier que la charge utile de la notification push contient les éléments attendus`title`,`body` ainsi que les liens profonds (`ab_uri`).
- Veuillez confirmer qu'un`pushClick`événement est enregistré après avoir appuyé.
- Si l'événement de clic est manquant, veuillez vérifier que votre délégué d'application ou votre gestionnaire de notifications transmet correctement les événements push au SDK Braze.

## in-app Messages

Les journaux de messages in-app vous permettent de visualiser l'ensemble du cycle de vie : réception/distribution depuis le serveur, déclenchement en fonction des événements, affichage, enregistrement des impressions et suivi des clics.

### Réception/distribution des messages

Lorsqu'un utilisateur commence une session et est éligible pour recevoir un message in-app, le SDK reçoit la charge utile du message provenant du serveur.

{% tabs %}
{% tab Swift %}

Filtrez les réponses provenant de votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) contenant les données des messages in-app.

Le corps de la réponse contient la charge utile du message, notamment :

```
"templated_message": {
  "data": {
    "message": "...",
    "type": "HTML",
    "message_close": "SWIPE",
    "trigger_id": "<TRIGGER_ID>"
  },
  "type": "inapp"
}
```

{% endtab %}
{% tab Android %}

Veuillez rechercher le journal correspondant à l'événement de déclencheur :

```
Triggering action: <CAMPAIGN_BSON_ID>
```

Cela confirme que le message in-app a été associé à un événement déclencheur.

{% endtab %}
{% endtabs %}

### Affichage et impression des messages

{% tabs %}
{% tab Swift %}

```
In-app message ready for display:
- triggerId: (campaignId: <CAMPAIGN_ID>, ...)
- extras: { ... }
```

Veuillez trouver ci-dessous le journal des impressions :

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageImpression(triggerIds: [...])
```

{% endtab %}
{% tab Android %}

```
handleExistingInAppMessagesInStackWithDelegate:: Displaying in-app message
```

{% endtab %}
{% endtabs %}

### Événements liés aux clics et aux boutons

Lorsqu'un utilisateur appuie sur un bouton ou ferme le message :

{% tabs %}
{% tab Swift %}

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: inAppMessageButtonClick(triggerIds: [...], buttonId: "<BUTTON_ID>")
```

Si aucun autre message déclenché ne correspond, vous verrez également s'afficher :

```
No matching trigger for event.
```

Ce comportement est normal lorsqu'aucun message in-app supplémentaire n'est configuré pour l'événement.

{% endtab %}
{% tab Android %}

Filtrez les requêtes adressées à votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) et recherchez les événements portant le nom`sbc`(clic sur le bouton) ou`si`(impression) dans le corps de la requête.

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- Si le message in-app ne s'affiche pas, veuillez vérifier qu'un début de session a bien été enregistré au préalable.
- Filtrez les réponses provenant de votre endpoint Braze configuré afin de confirmer que le contenu du message a bien été transmis.
- Si les impressions ne sont pas enregistrées, veuillez vérifier que vous n'avez pas implémenté de délégué`inAppMessageDisplay` personnalisé qui supprime l'enregistrement.
- Si le message « Aucun déclencheur correspondant à l'événement » s'affiche, cela est normal et indique qu'aucun message in-app supplémentaire n'est configuré pour cet événement.

## Cartes de contenu

Les journaux des cartes de contenu vous permettent de vérifier que les cartes sont synchronisées avec l'appareil, affichées à l'utilisateur et que les interactions (impressions, clics, fermetures de la carte de contenu) sont suivies.

### Synchronisation des cartes

Les cartes de contenu se synchronisent au début de la session et lorsqu'il est nécessaire d'actualiser manuellement la page. Si aucune session n'est enregistrée, aucune carte de contenu n'est affichée.

{% tabs %}
{% tab Swift %}

Filtrez les réponses provenant de votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) contenant les données de la carte.

Le corps de la réponse contient les données de la carte, notamment :

```
"cards": [
  {
    "id": "<CARD_ID>",
    "tt": "<CARD_TITLE>",
    "ds": "<CARD_DESCRIPTION>",
    "tp": "short_news",
    "v": 0,
    "cl": 0,
    "p": 1
  }
]
```

Domaines clés :
- `v` (vu) :`0`  = non vu,`1`  = vu
- `cl` (cliqué) :`0`  = non cliqué,`1`  = cliqué
- `p` (épinglé) :`0`  = non épinglé,`1`  = épinglé
- `tp` (type) : `short_news`, `captioned_image`, `classic`, etc.

{% endtab %}
{% tab Android %}

```
Requesting content cards sync.
```

Suivi d'une requête POST vers votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) contenant les informations relatives à l'utilisateur et à l'appareil.

{% endtab %}
{% endtabs %}

### Impressions, clics et rejets

{% tabs %}
{% tab Swift %}

**Impression :**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardImpression(cardIds: [...])
```

**Clic :**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardClick(cardIds: [...])
```

Si la carte comporte une URL, vous verrez également :

```
Opening '<URL>':
- channel: contentCard
- useWebView: true
```

**Licenciement :**

```
Logged event:
- userId: <USER_ID>
- sessionId: <SESSION_ID>
- data: contentCardDismissed(cardIds: [...])
```

{% endtab %}
{% tab Android %}

Filtrez les requêtes adressées à votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) et recherchez les noms d'événements dans le corps de la requête :
- `cci` — Impression de la carte de contenu
- `ccc` — Carte de contenu cliquer
- `ccd` — Carte de contenu rejetée

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- **Aucune carte affichée** : Veuillez vérifier que le début de la session est bien enregistré. Les cartes de contenu nécessitent une session active pour se synchroniser.
- **Cartes manquantes pour les nouveaux utilisateurs** : Les nouveaux utilisateurs peuvent ne pas voir les cartes de contenu lors de leur première session, mais celles-ci apparaîtront lors de la session suivante. Il s'agit d'un comportement normal.
- **La carte dépasse la limite de taille** : Les cartes de contenu de plus de 2 Ko ne s'affichent pas et le message est interrompu.
- **La carte reste active après l'arrêt de la campagne** : Veuillez vérifier que la synchronisation s'est terminée après l'arrêt de la campagne. Les cartes de contenu sont supprimées de l'appareil après une synchronisation réussie. Lorsque vous interrompez une campagne, veuillez vous assurer que l'option permettant de supprimer les cartes actives des flux des utilisateurs est sélectionnée.

## Liens profonds

Les journaux de liens profonds apparaissent dans les notifications push, les messages in-app et les cartes de contenu. La structure du journal est cohérente, quel que soit le canal source.

{% tabs %}
{% tab Swift %}

Lorsque le SDK traite un lien profond :

```
Opening '<DEEP_LINK_URL>':
- channel: <SOURCE_CHANNEL>
- useWebView: false
- isUniversalLink: false
- extras: { ... }
```

Où l'un des éléments`<SOURCE_CHANNEL>` suivants est :`notification` `inAppMessage`, , ou `contentCard`.

{% endtab %}
{% tab Android %}

Pour les liens profonds, veuillez rechercher les entrées **Deep Link Delegate** ou **UriAction** dans Logcat. Pour tester la résolution des liens profonds de manière indépendante, veuillez exécuter la commande suivante :

```bash
adb shell am start -W -a android.intent.action.VIEW -d "<YOUR_DEEP_LINK>" "<YOUR_PACKAGE_NAME>"
```

Cela permet de vérifier si le lien profond fonctionne correctement en dehors du SDK Braze.

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- Veuillez vérifier que l'URL du lien profond correspond à celle que vous avez configurée dans la campagne.
- Si le lien profond fonctionne sur un canal (par exemple, push) mais pas sur un autre (par exemple, les cartes de contenu), veuillez vérifier que votre implémentation de gestion des liens profonds prend en charge tous les canaux.
- Sur iOS, les liens universels nécessitent un traitement supplémentaire. Si les liens universels ne fonctionnent pas à partir des canaux Braze, veuillez vérifier que votre application implémente le`BrazeDelegate`protocole pour la gestion des URL.
- Sur Android, veuillez vérifier que la gestion automatique des liens profonds est désactivée si vous utilisez un gestionnaire personnalisé. Dans le cas contraire, le gestionnaire par défaut pourrait entrer en conflit avec votre implémentation.

## Identification de l'utilisateur

Lorsqu'un utilisateur est identifié à l'aide d'un `external_id`, le SDK enregistre un événement utilisateur.

{% tabs %}
{% tab Android %}

```
changeUser called with: <EXTERNAL_ID>
```

Points importants à connaître :
- Veuillez appeler`changeUser`dès que l'utilisateur se connecte, le plus tôt sera le mieux.
- Si un utilisateur se déconnecte, il n'existe aucun moyen de le renvoyer`changeUser`vers un utilisateur anonyme.
- Si vous ne souhaitez pas autoriser les utilisateurs anonymes, veuillez appeler`changeUser`  au début de la session ou au démarrage de l'application.

{% endtab %}
{% tab Swift %}

Filtrez les requêtes adressées à votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com) et recherchez l'identifiant utilisateur dans le corps de la requête :

```
"user_id": "<EXTERNAL_ID>"
```

{% endtab %}
{% endtabs %}

## Demandes réseau

Les journaux détaillés comprennent tous les détails des requêtes et réponses HTTP pour la communication du SDK avec les serveurs Braze. Ces informations sont utiles pour diagnostiquer les problèmes de connectivité.

### Structure de la demande

Filtrez les requêtes adressées à votre endpoint Braze configuré (par exemple, sdk.iad-01.braze.com). La structure de la requête comprend :

{% tabs %}
{% tab Swift %}

```
[http] request POST: <YOUR_BRAZE_ENDPOINT>
- Headers:
  - Content-Type: application/json
  - X-Braze-Api-Key: <REDACTED>
  - X-Braze-Req-Attempt: 1
  - X-Braze-Req-Tokens-Remaining: <COUNT>
- Body: { ... }
```

{% endtab %}
{% tab Android %}

```
Making request(id = <REQUEST_ID>) to <YOUR_BRAZE_ENDPOINT>
```

{% endtab %}
{% endtabs %}

### Éléments à vérifier

- **Clé API** : Veuillez vérifier que cela correspond`XBraze-ApiKey` à la clé API de votre espace de travail.
- **Endpoint** : Veuillez vérifier que l'URL de la requête correspond à l'endpoint SDK que vous avez configuré.
- **Tentatives de réessai** :`XBraze-Req-Attempt`une valeur supérieure à 1 indique que le SDK réessaie une requête qui a échoué, ce qui peut signaler des problèmes de connectivité.
- **Limite de débit** :`XBraze-Req-Tokens-Remaining`affiche les jetons de requête restants. Un nombre faible peut indiquer que le SDK approche les limites de débit.
- **Demandes manquantes** : Sur Android, si vous ne constatez aucune requête vers l'endpoint Braze après le début de la session, veuillez vérifier votre clé API et la configuration de l'endpoint.

## Abréviations courantes utilisées pour les événements

Dans les charges utiles des journaux détaillés, Braze utilise des noms d'événements abrégés. Voici une référence :

| Abréviation | Événement |
|---|---|
| `ss` | Lancer la session |
| `se` | Fin de session |
| `si` | Impression des messages in-app |
| `sbc` | Clic sur le bouton de message in-app |
| `cci` | Impression de la carte de contenu |
| `ccc` | Carte de contenu cliquer |
| `ccd` | Carte de contenu rejetée |
| `lr` | Localisation enregistrée |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }