---
nav_title: "POST : Démarrer une ligne/en production/instantanée"
article_title: "POST : Démarrer une ligne/en production/instantanée"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Cet article présente les détails de l'endpoint Démarrer une ligne/en production/instantané."

---
{% api %}
# Démarrer une ligne/en production/instantanée
{% apimethod post %}
/messages/live_activity/start
{% endapimethod %}

> Utilisez cet endpoint pour démarrer à distance les [activités en direct]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) affichées dans votre app iOS. Cet endpoint nécessite une configuration supplémentaire.

Après avoir créé une activité en direct, vous pouvez effectuer une requête POST pour démarrer à distance votre activité pour n'importe quel segment/instantané. Pour en savoir plus sur les activités en direct d'Apple, consultez [Démarrage et mise à jour des activités en direct avec les notifications push d'ActivityKit.](https://developer.apple.com/documentation/activitykit/starting-and-updating-live-activities-with-activitykit-push-notifications)

Si `content-available` n'est pas défini, la priorité par défaut du service de notification push d'Apple (APN) est de 10. Si l'option `content-available` est activée, cette priorité est de 5. Pour plus de détails, reportez-vous à l'[objet Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object). 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez effectuer les opérations suivantes :

- Générez une clé API avec l’autorisation `messages.live_activity.start`.
- [Créez une activité en direct]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift#swift_create-an-activity) à l’aide du SDK Braze Swift.

{% multi_lang_include api/payload_size_alert.md %}

## Limite de débit

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corps de la demande

```json
{
  "app_id": "(required, string) App API identifier retrieved from the Developer Console.",
  "activity_id": "(required, string) Define a custom string as your `activity_id`. You will use this ID when you wish to send update or end events to your Live Activity.",
  "activity_attributes_type": "(required, string) The activity attributes type you define within `liveActivities.registerPushToStart` in your app",
  "activity_attributes": "(required, object) The static attribute values for the activity type (such as the sports team names, which don't change)",
  "content_state": "(required, object) You define the ContentState parameters when you create your Live Activity. Pass the updated values for your ContentState using this object. The format of this request must match the shape you initially defined.",
  "dismissal_date": "(optional, datetime in ISO-8601 format) The time to remove the Live Activity from the user’s UI. If this time is in the past, the Live Activity will be removed immediately.",
  "stale_date": "(optional, datetime in ISO-8601 format) The time the Live Activity content is marked as outdated in the user’s UI.",
  "notification": "(required, object) Include an `apple_push` object to define a push notification that creates an alert for the user, displayed on paired watchOS devices. Should include `notification.alert.title` and `notification.alert.body`",
  // One of the following:
  "external_user_ids": "(optional, array of strings) see external user identifier, maximum 50",
  "custom_audience": "(optional, connected audience object) see connected audience",
  "segment_id": "(optional, string) see segment identifier"
}
```

## Paramètres de demande

| Paramètre | Requis | Type de données| Description  |
|-----------|----------|----------|--------------|
| `app_id` | Requis | Chaîne de caractères | Identifiant [API]({{site.baseurl}}/api/identifier_types/#the-app-identifier) récupéré depuis la page [Clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/).  |
| `activity_id` | Requis | Chaîne de caractères  | Définissez une chaîne de caractères personnalisée comme votre `activity_id`. Vous utiliserez cet ID lorsque vous souhaiterez envoyer des événements de mise à jour ou de fin à votre ligne/en production/instantanée.  |
| `activity_attributes_type`  | Requis | Chaîne de caractères | Le type d'attributs d'activité que vous définissez à l'adresse `liveActivities.registerPushToStart` dans votre application.  |
| `activity_attributes` | Requis | Objet  | Les valeurs d'attributs statiques pour le type d'activité (comme les noms des équipes sportives, qui ne changent pas). |
| `content_state` | Requis | Objet  | Vous définissez les paramètres `ContentState` lorsque vous créez votre activité en direct. Transmettez les valeurs mises à jour pour votre `ContentState` en utilisant cet objet.<br><br>Le format de cette requête doit correspondre à la forme que vous avez initialement définie. |
| `dismissal_date` | Facultatif | DateTime <br>chaîne ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Ce paramètre définit le moment de suppression de l’activité en direct de l’interface utilisateur. |
| `stale_date` | Facultatif | DateTime <br>chaîne ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Ce paramètre indique au système quand le contenu de l’activité en direct devient obsolète dans l’interface utilisateur. |
| `notification` | Requis | Objet | Inclure un [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) objet pour définir une notification push. Le comportement de cette notification push dépend du fait que l'utilisateur est actif ou qu'il utilise un appareil proxy. {::nomarkdown}<ul><li>Si une <code>notification</code> est incluse et que l'utilisateur est actif sur son iPhone au moment de la mise à jour, l'interface utilisateur de l'activité en direct mise à jour coulissera vers le bas et s'affichera comme une notification push.</li><li>Si une <code>notification</code> est incluse et que l'utilisateur n'est pas actif sur son iPhone, son écran s'allume pour afficher l'interface utilisateur de l'activité en direct mise à jour sur son écran de verrouillage.</li><li>L'<code>alerte de notification</code> ne s'affichera pas comme une notification push standard. En outre, si un utilisateur dispose d'un appareil proxy, comme une Apple Watch, l'<code>alerte</code> s'y affichera.</li></ul>{:/} |
| `external_user_ids` | Facultatif si `segment_id` ou `audience` est fourni | Tableau de chaînes de caractères | Voir [ID externe]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields). Maximum 50 ID externes.  |
| `segment_id `  | Facultatif si `external_user_ids` ou `audience` est fourni | Chaîne de caractères    | Voir [identifiant de segmentation]({{site.baseurl}}/api/identifier_types/). |
| `custom_audience` | Facultatif si `external_user_ids` ou `segment_id` est fourni | Objet Audience connectée  | Voir [audience connectée]({{site.baseurl}}/api/objects_filters/connected_audience/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Exemple de demande

```json
curl --location --request POST 'https://rest.iad-01.braze.com/messages/live_activity/start' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {YOUR-REST-API-KEY}' \
--data-raw '{
    "app_id": "{YOUR-APP-API-IDENTIFIER}",
    "activity_id": "football-chiefs-bills-2024-01-21",
    "content_state": {
        "teamOneScore": 0,
        "teamTwoScore": 0
    },
    "activity_attributes_type": "FootballActivity",
    "activity_attributes": {
        "team1Name": "Chiefs",
        "team2Name": "Bills"
    },
    "dismissal_date": "2024-01-22T00:00:00+0000",
    "stale_date": "2024-01-22T16:55:49+0000",
    "notification": {
        "alert": {
            "body": "The game is starting! Tune in soon!",
            "title": "Chiefs v. Bills"
        }
    },
    // One of the following required:
    "segment_id": "{YOUR-SEGMENT-API-IDENTIFIER}", // Optional
    "custom_audience": {...}, // Optional
    "external_user_ids": ["user-id1", "user-id2"], // Optional
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

La classe du code de statut `4XX` indique une erreur client. Reportez-vous à l'article [erreurs et réponses de l'API]({{site.baseurl}}/api/errors/) pour plus d'informations sur les erreurs que vous pouvez rencontrer.

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
