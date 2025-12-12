---
nav_title: "POST: Update der Nutzer:innen Abo-Gruppenstatus"
article_title: "POST: Update des Abo-Gruppenstatus eines Nutzers"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Endpunkts Update Nutzer:innen Abo-Gruppenstatus Braze."
---
{% api %}
# Update des Abo-Gruppenstatus des Nutzers:in
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/abo/status/set
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um das Update des Abo-Status von bis zu 50 Nutzer:innen auf dem Braze-Dashboard im Stapelverfahren durchzuführen. 

Sie können auf die `subscription_group_id` einer Abo-Gruppe zugreifen, indem Sie zur Seite **Abo-Gruppe** navigieren.

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **SMS und RCS Abo-Gruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.status.set`.

## Rate-Limit

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Anfragetext

{% tabs %}
{% tab SMS and RCS %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "phone": (required*, array of strings in E.164 format) The phone number of the user (must include at least one phone number and at most 50 phone numbers),
   // SMS and RCS subscription group - one of external_id or phone is required
 }
```
\* SMS und RCS Abo-Gruppen: Nur `external_id` oder `phone` werden akzeptiert.

{% endtab %}
{% tab Email %}
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
   "subscription_group_id": (required, string) the id of your subscription group,
   "subscription_state": (required, string) available values are "unsubscribed" (not in subscription group) or "subscribed" (in subscription group),
   "external_id": (required*, array of strings) the external ID of the user or users, may include up to 50 IDs,
   "email": (required*, array of strings) the email address of the user (must include at least one email and at most 50 emails),
   // Email subscription group - one of external_id or email is required
   // Note that sending an email address that is linked to multiple profiles will update all relevant profiles
 }
```
\* Abo-Gruppen per E-Mail: Entweder `email` oder `external_id` ist erforderlich.
{% endtab %}
{% endtabs %}

Diese Eigenschaft sollte nicht zum Update der Profil-Informationen eines Nutzers:innen verwendet werden. Verwenden Sie stattdessen die Eigenschaft [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

{% alert tip %}
Wenn Sie neue Nutzer:innen über den Endpunkt [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) erstellen, können Sie Abo-Gruppen innerhalb des Objekts für die Nutzer-Attribute festlegen. So können Sie in einem einzigen API-Aufruf einen Nutzer erstellen und den Status der Abo-Gruppe festlegen.
{% endalert %}

## Parameter der Anfrage

| Parameter | Erforderlich | Datentyp | Beschreibung |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Erforderlich | String | Die `id` Ihrer Abo-Gruppe. |
| `subscription_state` | Erforderlich | String | Verfügbare Werte sind `unsubscribed` (nicht in Abo-Gruppe) oder `subscribed` (in Abo-Gruppe). |
| `external_id` | Erforderlich* | String-Array | Die `external_id` des Nutzers oder der Nutzer:innen kann bis zu 50 `id`s umfassen. |
| `email` | Erforderlich* | String oder String-Array | Die E-Mail Adresse des Nutzers:innen, kann als String-Array übergeben werden. Sie müssen mindestens eine E-Mail Adresse angeben (maximal 50). <br><br>Wenn mehrere Nutzer:innen (`external_id`) im selben Workspace dieselbe E-Mail Adresse haben, werden alle Nutzer:innen mit den Änderungen der Abo-Gruppe aktualisiert. |
| `phone` | Erforderlich* | String in [E.164](https://en.wikipedia.org/wiki/E.164) Format | Die Telefonnummer des Nutzers:innen, kann als String-Array übergeben werden. Muss mindestens eine Telefonnummer enthalten (bis zu 50). <br><br>Wenn mehrere Nutzer:innen (`external_id`) im selben Workspace dieselbe Telefonnummer haben, werden alle Nutzer:innen mit denselben Änderungen der Abo-Gruppe aktualisiert. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel-Anfragen

### E-Mail

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "email": ["example1@email.com", "example2@email.com"]
}
'
```

### SMS und RCS

```
curl --location --request POST 'https://rest.iad-01.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "subscription_group_identifier",
  "subscription_state": "unsubscribed",
  "external_id": "external_identifier",
  "phone": ["+12223334444", "+11112223333"]
}
'
```

## Beispiel für eine erfolgreiche Antwort

Der Status Code `201` könnte den folgenden Antwortkörper zurückgeben.

```json
{
    "message": "success"
}
```

{% alert important %}
Der Endpunkt akzeptiert nur den Wert `email` oder `phone`, nicht beide. Wenn Sie beides angeben, erhalten Sie diese Antwort: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}

