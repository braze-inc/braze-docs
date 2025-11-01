---
nav_title: "POST : Mise à jour de la production en ligne/instantanée"
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

> Utilisez cet endpoint pour mettre à jour et terminer les [activités en direct]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift) affichées par votre application iOS. Cet endpoint nécessite une configuration supplémentaire.

Après avoir enregistré une activité en direct, vous pouvez passer une charge utile JSON pour mettre à jour votre service de notification push Apple (APNs). Consultez la documentation d'Apple sur [la mise à jour de votre activité en direct avec des charges utiles de notification push](https://developer.apple.com/documentation/activitykit/updating-and-ending-your-live-activity-with-activitykit-push-notifications) pour plus d'informations.

Si `content-available` n'est pas défini, la priorité par défaut du service de notification push d'Apple (APN) est de 10. Si l'option `content-available` est activée, cette priorité est de 5. Pour plus de détails, reportez-vous à l'[objet Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object). 

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#2300226e-f26a-4154-9bcc-5883f1f294cd {% endapiref %}

## Conditions préalables

Pour utiliser cet endpoint, vous devrez effectuer les opérations suivantes :

- Générez une clé API avec l’autorisation `messages.live_activity.update`.
- Enregistrez une activité en direct [à distance]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=remote&sdktab=swift) ou [localement]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?tab=local&sdktab=swift) à l'aide du SDK Braze Swift.

{% multi_lang_include api/payload_size_alert.md %}

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
| `app_id` | Requis | Chaîne de caractères | Identifiant [API]({{site.baseurl}}/api/identifier_types/#the-app-identifier) récupéré depuis la page [Clés API]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/).  |
| `activity_id` | Requis | Chaîne de caractères | Lorsque vous enregistrez votre Activité en direct en utilisant [`launchActivity`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/liveactivities-swift.class), vous utilisez le paramètre `pushTokenTag` pour nommer le jeton push de l'Activité avec une chaîne personnalisée.<br><br>Définissez l’`activity_id` vers cette chaîne de caractères personnalisée pour définir l’activité en direct que vous souhaitez mettre à jour. |
| `content_state` | Requis | Objet | Vous définissez les paramètres `ContentState` lorsque vous créez votre activité en direct. Transmettez les valeurs mises à jour pour votre `ContentState` en utilisant cet objet.<br><br>Le format de cette requête doit correspondre à la forme que vous avez initialement définie. |
| `end_activity` | Facultatif | Valeur booléenne | Si `true`, cette requête met fin à l’activité en direct. |
| `dismissal_date` | Facultatif | DateTime <br>chaîne ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Ce paramètre définit le moment de suppression de l’activité en direct de l’interface utilisateur. Si cette heure est dans le passé et `end_activity` est `true`, l'Activité en direct sera supprimée immédiatement.<br><br> Si `end_activity` est `false` ou omis, ce paramètre met uniquement à jour l'Activité en direct.|
| `stale_date` | Facultatif | DateTime <br>chaîne ([ISO-8601](https://en.wikipedia.org/wiki/ISO_8601)) | Ce paramètre indique au système quand le contenu de l’activité en direct devient obsolète dans l’interface utilisateur. |
| `notification` | Facultatif | Objet | Inclure un [`apple_push`]({{site.baseurl}}/api/objects_filters/messaging/apple_object/) objet pour définir une notification push. Le comportement de cette notification push dépend du fait que l'utilisateur est actif ou qu'il utilise un appareil proxy. {::nomarkdown}<ul><li>Si une <code>notification</code> est incluse et que l'utilisateur est actif sur son iPhone au moment de la mise à jour, l'interface utilisateur de l'activité en direct mise à jour coulissera vers le bas et s'affichera comme une notification push.</li><li>Si une <code>notification</code> est incluse et que l'utilisateur n'est pas actif sur son iPhone, son écran s'allume pour afficher l'interface utilisateur de l'activité en direct mise à jour sur son écran de verrouillage.</li><li>L'<code>alerte de notification</code> ne s'affichera pas comme une notification push standard. En outre, si un utilisateur dispose d'un appareil proxy, comme une Apple Watch, l'<code>alerte</code> s'y affichera.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

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

La classe du code de statut `4XX` indique une erreur client. Reportez-vous à l'article [erreurs et réponses de l'API]({{site.baseurl}}/api/errors/) pour plus d'informations sur les erreurs que vous pouvez rencontrer.

Le code de statut `400` pourrait renvoyer le corps de réponse suivant. 

```json
{
    "error": "\nProblem:\n  message body does not match declared format\nResolution:\n  when specifying application/json as content-type, you must pass valid application/json in the request's 'body' "
}
```

{% endapi %}
