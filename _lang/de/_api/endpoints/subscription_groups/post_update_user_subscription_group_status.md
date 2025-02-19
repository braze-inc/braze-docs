---
nav_title: "POST: Status der Abonnementgruppe eines Benutzers aktualisieren"
article_title: "POST: Status der Abonnementgruppe eines Benutzers aktualisieren"
search_tag: Endpoint
page_order: 4
layout: api_page
page_type: reference
description: "Dieser Artikel beschreibt die Details des Braze Endpunkts Update user's subscription group status."
---
{% api %}
# Status der Abonnementgruppe des Benutzers aktualisieren
{% apimethod post core_endpoint|https://www.braze.com/docs/core_endpoints %}
/subscription/status/set
{% endapimethod %}

> Verwenden Sie diesen Endpunkt, um den Abonnementstatus von bis zu 50 Benutzern auf dem Braze-Dashboard im Stapel zu aktualisieren. 

Sie können auf die `subscription_group_id` einer Abonnementgruppe zugreifen, indem Sie zur Seite **Abonnementgruppe** navigieren.

Wenn Sie Beispiele sehen oder diesen Endpunkt für **E-Mail-Abonnementgruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#8895e87e-6324-47a3-a833-adf29a258bb9 {% endapiref %}

Wenn Sie Beispiele sehen oder diesen Endpunkt für **SMS-Abonnementgruppen** testen möchten:

{% apiref postman %}https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#72558b32-7dbe-4cba-bd22-a7ce513076dd {% endapiref %}

## Voraussetzungen

Um diesen Endpunkt zu verwenden, benötigen Sie einen [API-Schlüssel]({{site.baseurl}}/api/basics#rest-api-key/) mit der Berechtigung `subscription.status.set`.

## Preisgrenze

{% multi_lang_include rate_limits.md endpoint='subscription status set' %}

## Körper der Anfrage

{% tabs %}
{% tab SMS %}
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
   // SMS subscription group - one of external_id or phone is required
 }
```
\* SMS-Abonnementgruppen: Nur `external_id` oder `phone` werden akzeptiert.

{% endtab %}
{% tab E-Mail %}
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
\* E-Mail-Abonnementgruppen: Entweder `email` oder `external_id` ist erforderlich.
{% endtab %}
{% endtabs %}

Diese Eigenschaft sollte nicht für die Aktualisierung der Profilinformationen eines Benutzers verwendet werden. Verwenden Sie stattdessen die Eigenschaft [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

{% alert tip %}
Bei der Erstellung neuer Benutzer über den Endpunkt [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) können Sie Abonnementgruppen innerhalb des Objekts für die Benutzerattribute festlegen. So können Sie in einem einzigen API-Aufruf einen Benutzer erstellen und den Status der Abonnementgruppe festlegen.
{% endalert %}

## Parameter anfordern

| Parameter | Erforderlich | Daten Typ | Beschreibung |
|---|---|---|---|
| [`subscription_group_id`]({{site.baseurl}}/api/identifier_types/?tab=subscription%20group%20ids) | Erforderlich | String | Die `id` Ihrer Abonnementgruppe. |
| `subscription_state` | Erforderlich | String | Verfügbare Werte sind `unsubscribed` (nicht in der Abonnementgruppe) oder `subscribed` (in der Abonnementgruppe). |
| `external_id` | Erforderlich* | Array von Zeichenketten | Die `external_id` des Nutzers oder der Nutzer, kann bis zu 50 `id`s umfassen. |
| `email` | Erforderlich* | String oder Array von Strings | Die E-Mail-Adresse des Benutzers, kann als Array von Strings übergeben werden. Sie müssen mindestens eine E-Mail-Adresse angeben (maximal 50). <br><br>Wenn mehrere Benutzer (`external_id`) im selben Arbeitsbereich dieselbe E-Mail-Adresse haben, werden alle Benutzer, die dieselbe E-Mail-Adresse haben, mit den Änderungen der Abonnementgruppe aktualisiert. |
| `phone` | Erforderlich* | Zeichenkette im [E.164](https://en.wikipedia.org/wiki/E.164) Format | Die Telefonnummer des Benutzers, kann als Array von Strings übergeben werden. Muss mindestens eine Telefonnummer enthalten (maximal 50). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4 role="presentation" }

## Beispiel Anfragen

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

### SMS

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

Der Statuscode `201` könnte den folgenden Antwortkörper zurückgeben.

```json
{
    "message": "success"
}
```

{% alert important %}
Der Endpunkt akzeptiert nur den Wert `email` oder `phone`, nicht beide. Wenn Sie beides angeben, erhalten Sie diese Antwort: `{"message":"Either an email address or a phone number should be provided, but not both."}`
{% endalert %}

{% endapi %}

