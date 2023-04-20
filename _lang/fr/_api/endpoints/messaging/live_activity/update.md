---
nav_title: "POST : Mettre à jour l’activité en direct"
article_title: "POST : Mettre à jour l’activité en direct"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente en détail l’endpoint Mettre à jour l’activité en direct."

---
{% api %}
# Mettre à jour l’activité en direct
{% apimethod post %}
/messages/live_activity/update
{% endapimethod %}

{% alert important %} 
Les activités en direct sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer. 
{% endalert %}

Utilisez cet endpoint pour mettre à jour et mettre fin aux [Activités en direct]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/) affichées par votre application iOS. Cet endpoint nécessite une configuration supplémentaire.

Avant d’utiliser cet endpoint, vous devez enregistrer une activité avec le SDK Swift de Braze en utilisant la méthode [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class/launchactivity(pushtokentag:activity:fileid:line:)). Les paramètres de requêtes nécessaires seront définis au cours de cette étape. Reportez-vous à [Activités en direct]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/) pour plus d’informations sur l’inscription.

Une fois que vous avez enregistré votre activité, transmettez une charge utile JSON avec des mises à jour du service de notifications push Apple (APN) via cet endpoint. Consultez la documentation d’Apple sur la [mise à jour de votre activité en direct avec des charges utiles de notification push](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications) pour plus d’informations.

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```json
{
   "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
   "activity_id": "(required, string) When you register your Live Activity using launchActivity, you use the pushTokenTag parameter to name the Activity’s push token to a custom string. Set activity_id to this custom string to define which Live Activity you want to update.",
   "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
   "end_activity": "(optional, boolean) If true, this request ends the Live Activity.",
   "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
   "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
   "notification": "(optional, object ) Include an `apple_push` object to define a push notification that creates an alert for the user."
 }
 ```

## Paramètres de demande

| Paramètre | Requis | Type de données | Description |
|---|---|---|---|
| `app_id` | Requis | String | [Identifiant API]({{site.baseurl}}/api/identifier_types/#the-app-identifier) de l’application extrait de la **Developer Console (Console du développeur)**.  |
| `activity_id` | Requis | String | Lorsque vous enregistrez votre Activité en direct à l’aide de [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class), vous utilisez le paramètre `pushTokenTag` pour nommer le jeton de notification push de l’activité en une chaîne de caractère personnalisée.<br><br>Définissez l’`activity_id` vers cette chaîne de caractères personnalisée pour définir l’activité en direct que vous souhaitez mettre à jour. |
| `content_state` | Requis | Objet | Vous définissez les paramètres `ContentState` lorsque vous créez votre activité en direct. Transmettez les valeurs mises à jour pour votre `ContentState` en utilisant cet objet.<br><br>Le format de cette requête doit correspondre à la forme que vous avez initialement définie. |
| `end_activity` | Facultatif | Booléen | Si `true`, cette requête met fin à l’activité en direct. |
| `dismissal_date` | Facultatif | DateTime <br>(chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Ce paramètre définit le moment de suppression de l’activité en direct de l’interface utilisateur. Si ce moment est dépassé, l’activité en direct sera immédiatement supprimée. |
| `stale_date` | Facultatif | DateTime <br>(chaîne de caractères [ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Ce paramètre indique au système quand le contenu de l’activité en direct devient obsolète dans l’interface utilisateur. |
| `notification` | Facultatif | Objet | Inclure un objet [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) pour définir une notification push. Le comportement de cette notification push dépend du fait que l’utilisateur soit actif ou utilise un appareil proxy. {::nomarkdown}<ul><li>Si un <code>notification</code> est inclus et que l’utilisateur est actif sur son iPhone lorsque la mise à jour est livrée, l’interface utilisateur de l’activité en direct mise à jour glissera vers le bas et s’affichera comme une notification push.</li><li>Si un <code>notification</code> est inclus et que l’utilisateur n’est pas actif sur son iPhone, son écran s’allume pour afficher l’interface utilisateur de l’activité en direct mise à jour sur son écran de verrouillage.</li><li>Le paramètre <code>notification alert</code> ne s’affichera pas comme une notification push standard. De plus, si un utilisateur dispose d’un appareil proxy, comme une Apple Watch, le <code>alert</code> s’affichera ici.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Exemple de demande

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/update' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "live-activity-1",
    "content_state": {
        "teamOneScore": 2,
        "teamTwoScore": 4
    },
    "end_activity": false,
    "dismissal_date": "2023-02-28T00:00:00+0000",
    "stale_date": "2023-02-27T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "It's halftime! Let's look at the scores",
            "title": "Halftime"
        }
    }
}'
```

## Réponse

Deux réponses de code de statut existent pour cet endpoint : `201` et `4XX`.

### Exemple de réponse réussie

Un code de statut `201` est renvoyé si la requête a été formatée correctement et que nous l’avons reçue. Le code de statut `201` pourrait renvoyer le corps de réponse suivant.

```json
{
  "message": "success"
}
```

### Exemple de réponse échouée

La classe du code de statut `4XX` indique une erreur client. Reportez-vous à l’[article sur les erreurs et réponses API]({{site.baseurl}}/api/errors/) pour plus d’informations sur les erreurs que vous pouvez rencontrer.

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
