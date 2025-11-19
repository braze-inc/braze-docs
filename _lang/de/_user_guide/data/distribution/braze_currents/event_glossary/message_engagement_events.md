---
nav_title: Nachrichtenengagement-Events
layout: message_engagement_events_glossary
alias: /message_events_glossary/
page_order: 5
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar listet die verschiedenen Nachrichten Engagement Events auf, die Braze mit Currents verfolgen und an ausgewählte Data Warehouses senden kann."
tool: Currents
search_rank: 6
---

Speicherschemata gelten für die Flat File-Ereignisdaten, die wir an Data Warehouse Storage Partner (Google Cloud Storage, Amazon S3 und Microsoft Azure Blob Storage) senden. Schemata, die für andere Partner gelten, finden Sie in unserer Liste der [verfügbaren Partner]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) und auf den entsprechenden Seiten.

Wenden Sie sich an Ihren Account Manager:in oder öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/), wenn Sie Zugang zu zusätzlichen Veranstaltungsberechtigungen benötigen. Wenn Sie in diesem Artikel nicht finden, was Sie brauchen, sehen Sie sich unsere [Bibliothek für Kundenverhalten-Events]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) oder unsere [Currents-Beispiele für Daten](https://github.com/Appboy/currents-examples/tree/master/sample-data) an.

{% details Explanation of message engagement event structure and platform values %}

### Event-Struktur

Diese Aufschlüsselung der Ereignisse zeigt, welche Art von Informationen im Allgemeinen in einem Ereignis zum Engagement für Nachrichten enthalten sind. Mit einem soliden Verständnis seiner Komponenten können Ihre Entwickler:in und Ihr Business-Intelligence Strategie Team die eingehenden Currents Ereignisdaten nutzen, um datengestützte Berichte und Charts zu erstellen und andere wertvolle Metriken zu nutzen.

![Aufschlüsselung eines Nachrichten-Engagement-Ereignisses, das ein E-Mail-Abmelde-Ereignis zeigt, mit den aufgelisteten Eigenschaften gruppiert nach benutzerspezifischen Eigenschaften, Kampagnen- oder Canvas-Tracking-Eigenschaften und ereignisspezifischen Eigenschaften]({% image_buster /assets/img/message_engagement_event.png %})

Nachrichten-Engagement-Ereignisse setzen sich aus **benutzerspezifischen** Eigenschaften, **Kampagnen/Canvas Tracking-Eigenschaften** und **ereignisspezifischen** Eigenschaften zusammen.

### Schema der Nutzer:innen ID

Beachten Sie die Namenskonventionen für Nutzer:innen.

| Braze Schema | Currents Schema | Beschreibung |
| ----------- | ----------- | ----------- |
| `braze_id` | `"USER_ID"` | Der eindeutige Bezeichner, der automatisch von Braze zugewiesen wird. |
| `external_id` | `"EXTERNAL_USER_ID"` | Der eindeutige Bezeichner des Profils eines Nutzers:in, der vom Kunden festgelegt wird. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Plattformwerte

Bestimmte Ereignisse geben einen `platform`-Wert zurück, der die Plattform des Nutzergeräts angibt.
<br>In der folgenden Tabelle finden Sie die möglichen Rückgabewerte:

| Nutzer:in-Gerät | Plattformwert |
| --- | --- |
| iOS | `ios` |
| Android | `android` |
| FireTV | `kindle` |
| Kindle | `kindle` |
| Internet | `web` |
| tvOS | `tvos` |
| Roku | `roku` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% enddetails %}

{% alert important %}
Currents verwirft Events mit übermäßig großen Nutzdaten von mehr als 900 KB.
{% endalert %}

{% alert note %}
Objekte, die sich auf Canvas Flow beziehen, haben IDs, die zur Gruppierung verwendet und über den [Endpunkt Canvas-Details exportieren]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/) in menschenlesbare Namen übersetzt werden können.
{% endalert %}

{% alert note %}
Bei bestimmten Feldern kann es länger dauern, bis der neueste Stand angezeigt wird, nachdem eine Kampagne oder ein Canvas aktualisiert wurde. Diese Felder sind:
<ul>
  <li>"campaign_name"</li>
  <li>"canvas_name"</li>
  <li>"canvas_step_name"</li>
  <li>"conversion_behavior"</li>
  <li>"canvas_variation_name"</li>
  <li>"experiment_split_name"</li>
  <li>"message_variation_name"</li>
</ul>
Wenn eine vollständige Konsistenz erforderlich ist, empfehlen wir, eine Stunde nach dem letzten Update dieser Felder zu warten, bevor Sie Ihre Nachrichten an Ihre Nutzer:innen versenden.
{% endalert %}

{% api %}
## Ereignisse deinstallieren {#uninstall-events}

{% apitags %}
Deinstallation
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen eine App deinstalliert. Verwenden Sie diese Daten, um zu verfolgen, wenn Nutzer:innen eine App deinstallieren. Zur Zeit ist dies ein Ereignis für das Engagement in Nachrichten, wird aber in Zukunft in ein Ereignis für das Nutzer:innen-Verhalten geändert.

{% alert important %}
Dieses Ereignis wird nicht ausgelöst, wenn der Nutzer:innen die App tatsächlich deinstalliert, da es unmöglich ist, das genau zu verfolgen. Braze sendet täglich einen stillen Push, um festzustellen, ob die App noch auf dem Gerät Ihres Nutzers:innen vorhanden ist. Wenn wir bei diesem stillen Push einen Fehler erhalten, wird davon ausgegangen, dass die App deinstalliert wurde.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Uninstall (users.behaviors.Uninstall)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Uninstall (users.behaviors.Uninstall)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Application Uninstalls (users.behaviors.Uninstall)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Application Uninstalled (users.behaviors.Uninstall)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.Uninstall

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Globale Ereignisse zur Änderung des Abo-Status {#global-subscription-state-change-events}

{% apitags %}
Abo
{% endapitags %}

Dieses Ereignis tritt ein, wenn Braze eine Anfrage zum Update des globalen Abo-Status des Nutzers erhält, auch wenn die Anfrage den aktuellen Abo-Status des Nutzers nicht ändert.

{% tabs %}
{% tab Amplitude %}
```json
// Global Subscription State Change (users.behaviors.subscription.GlobalStateChange)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Global Subscription State Change (users.behaviors.subscription.GlobalStateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Global Subscription State Changes (users.behaviors.subscription.GlobalStateChange)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "channel" : "(optional, string) Channel this event belongs to",
          "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(optional, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Global Subscription State Changed (users.behaviors.subscription.GlobalStateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(optional, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.subscription.GlobalStateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "channel" : "(optional, string) Channel this event belongs to",
  "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed', 'Unsubscribed' or 'Opted In'",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- `state_change_source` gibt einen String mit dem vollständigen Namen der Quelle zurück. Der Quell-CSV-Import gibt beispielsweise den String `CSV Import` zurück. Die verfügbaren Quellen sind unten aufgeführt:

| Quelle | Beschreibung |
| --- | --- |
| SDK | SDK-Endpunkte |
| Dashboard | Wenn der Status des Abos eines Nutzers auf der Seite **Benutzerprofil** im Dashboard aktualisiert wird |
| Abo Seite | Wenn sich ein Nutzer:innen über einen E-Mail-Link abmeldet, der nicht das Einstellungscenter ist |
| REST API | REST API Endpunkte |
| CSV-Import | CSV-Nutzerimport |
| Präferenzzentrum | Wenn ein Nutzer:innen über das Einstellungscenter aktualisiert wird |
| Eingehende Nachricht | Wenn ein Nutzer:in durch eingehende Nachrichten von Endnutzern über Kanäle wie z.B. SMS aktualisiert wird |
| Migration | Wenn ein Nutzer:innen durch interne Migrationen oder Wartungsskripte aktualisiert wird |
| Nutzer:in zusammenführen | Wenn ein Nutzer:innen durch das Zusammenführen von Nutzern aktualisiert wird |
| Canvas-Schritt „Nutzeraktualisierung“ | Wenn ein Nutzer:innen durch den Canvas-Schritt Update aktualisiert wird |
| Push-Token Registrierung | Wenn ein Nutzer:innen durch den Prozess der Token-Registrierung aktualisiert wird |
| List-Unsubscribe | Wenn sich ein Nutzer:innen über Braze mailto oder die Kopfzeile Liste-abmelden mit einem Klick abmeldet |
| Sonstiges | Einschließlich aller anderen Quellen, wie z.B. Demo- oder Provider-Synchronisierungsaufträge oder SMS- und Whatsapp-Ereignis-Callbacks |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}
## Abo Gruppe Statusänderung Ereignisse {#subscription-group-state-change-events}

{% apitags %}
Abo
{% endapitags %}

Dieses Ereignis tritt ein, wenn sich der Abo-Status eines Nutzers:innen in einer Abo-Gruppe ändert.

{% alert important %}
Abo-Gruppen sind zur Zeit nur für die Kanäle E-Mail, SMS und WhatsApp verfügbar.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Subscription Group State Change (users.behaviors.subscriptiongroup.StateChange)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Subscription Group State Change (users.behaviors.subscriptiongroup.StateChange)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(optional, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Subscription Group State Changes (users.behaviors.subscriptiongroup.StateChange)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "channel" : "(optional, string) Channel this event belongs to",
          "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
          "subscription_group_id" : "(required, string) Subscription group API ID",
          "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(optional, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Subscription Group State Changed (users.behaviors.subscriptiongroup.StateChange)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(optional, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "channel" : "(optional, string) Channel this event belongs to",
    "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
    "subscription_group_id" : "(required, string) Subscription group API ID",
    "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.behaviors.subscriptiongroup.StateChange

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "channel" : "(optional, string) Channel this event belongs to",
  "channel_identifier" : "(optional, string) [PII] The user's identifier on the channel the event is for.",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(optional, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "phone_number" : "(optional, string) [PII] Phone number of the user in e.164 format (for example +14155552671)",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "state_change_source" : "(optional, string) Source of the state change, e.g: REST API, SDK, Dashboard, etc.",
  "subscription_group_id" : "(required, string) Subscription group API ID",
  "subscription_status" : "(required, string) Subscription status: 'Subscribed' or 'Unsubscribed'",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- `state_change_source` gibt einen String mit dem vollständigen Namen der Quelle zurück. Der Quell-CSV-Import gibt beispielsweise den String `CSV Import` zurück. Die verfügbaren Quellen sind unten aufgeführt:

| Quelle | Beschreibung |
| --- | --- |
| SDK | SDK-Endpunkte |
| Dashboard | Wenn der Status des Abos eines Nutzers:innen auf der Seite Benutzerprofil im Dashboard aktualisiert wird |
| Abo Seite | Wenn sich ein Nutzer:innen über einen E-Mail-Link abmeldet, der nicht das Einstellungscenter ist |
| REST API | REST API Endpunkte |
| CSV-Import | CSV-Nutzerimport |
| Präferenzzentrum | Wenn ein Nutzer:innen über das Einstellungscenter aktualisiert wird |
| Eingehende Nachricht | Wenn ein Nutzer:in durch eingehende Nachrichten von Endnutzern über Kanäle wie SMS aktualisiert wird |
| Migration | Wenn ein Nutzer:innen durch interne Migrationen oder Wartungsskripte aktualisiert wird |
| Nutzer:in zusammenführen | Wenn ein Nutzer:innen durch den Prozess der Zusammenführung von Nutzern aktualisiert wird |
| Canvas-Schritt „Nutzeraktualisierung“ | Wenn ein Nutzer:innen durch den Canvas-Schritt zum Update aktualisiert wird |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}
## Kampagne Konversions-Events {#campaign-conversion-events}

{% apitags %}
Kampagne, Konversion
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen eine Aktion ausführt, die als Konversions-Event in einer Kampagne festgelegt wurde.

{% alert note %}
`dispatch_id` ist veraltet und wird in der nächsten Currents Version entfernt.
{% endalert %}

{% alert important %}
Beachten Sie, dass das Konversions-Ereignis im Feld `conversion_behavior` kodiert wird, das die Art des Konversions-Ereignisses, das Fenster (Zeitrahmen) und zusätzliche Informationen je nach Art des Konversions-Ereignisses enthält. Das Feld `conversion_behavior_index` gibt an, welches Konversions-Event vorliegt, z.B. 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Campaign Conversion (users.campaigns.Conversion)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Conversion (users.campaigns.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Conversions (users.campaigns.Conversion)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Campaign Converted (users.campaigns.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.campaigns.Conversion

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Kampagne Kontrollgruppe Einschreibeereignisse {#campaign-control-group-enrollment-events}

{% apitags %}
Kampagne, Eingang
{% endapitags %}

Dieses Ereignis tritt ein, wenn sich ein Nutzer:innen in eine Kontrollvariante einer multivariaten Kampagne einträgt. Dieses Ereignis wird erzeugt, da es für diesen Nutzer:innen kein Kanal-Sendeereignis geben wird.

{% alert note %}
`dispatch_id` ist veraltet und wird in der nächsten Currents Version entfernt.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Campaign Control Group Enrollment (users.campaigns.EnrollInControl)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Campaign Control Group Enrollment (users.campaigns.EnrollInControl)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Campaign Control Group Enrollments (users.campaigns.EnrollInControl)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Campaign Control Group Entered (users.campaigns.EnrollInControl)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.campaigns.EnrollInControl

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(required, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Canvas Konversions-Ereignisse {#canvas-conversion-events}

{% apitags %}
Canvas, Konversion
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen eine Aktion ausführt, die als Konversions-Event in Canvas festgelegt wurde.

{% alert important %}
Beachten Sie, dass das Konversions-Ereignis im Feld `conversion_behavior` kodiert wird, das die Art des Konversions-Ereignisses, das Fenster (Zeitrahmen) und zusätzliche Informationen je nach Art des Konversions-Ereignisses enthält. Das Feld `conversion_behavior_index` gibt an, welches Konversions-Event vorliegt, z.B. 0 = A, 1 = B, 2 = C, 3 = D.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Conversion (users.canvas.Conversion)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Conversion (users.canvas.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Conversions (users.canvas.Conversion)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Converted (users.canvas.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "device_id" : "(optional, string) ID of the device on which the event occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.Conversion

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Canvas Eingang Ereignisse {#canvas-entry-events}

{% apitags %}
Canvas, Eingang
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:in den Canvas eintritt. Dieses Ereignis teilt Ihnen mit, in welche Variante der Nutzer:in eingetreten ist.

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Entry (users.canvas.Entry)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Entry (users.canvas.Entry)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Entries (users.canvas.Entry)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Entered (users.canvas.Entry)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.Entry

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Exit Match Publikumsveranstaltungen {#exit-match-audience-events}

{% apitags %}
Exit, Canvas
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen einen Canvas verlassen hat, indem er eine Zielgruppe gefunden hat.

{% tabs %}
{% tab Amplitude %}
```json
// Exit Match Audience (users.canvas.exit.MatchedAudience)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Match Audience (users.canvas.exit.MatchedAudience)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Matched Audiences (users.canvas.exit.MatchedAudience)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Exit Matched Audience (users.canvas.exit.MatchedAudience)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.exit.MatchedAudience

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Exit Perform Event-Ereignisse {#exit-perform-event-events}

{% apitags %}
Exit, Canvas
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen ein Canvas durch die Ausführung eines Ereignisses verlassen hat.

{% tabs %}
{% tab Amplitude %}
```json
// Exit Perform Event (users.canvas.exit.PerformedEvent)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Exit Perform Event (users.canvas.exit.PerformedEvent)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Exit Performed Events (users.canvas.exit.PerformedEvent)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Exit Performed Event (users.canvas.exit.PerformedEvent)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.exit.PerformedEvent

{
  "app_group_api_id" : "(optional, string) [DEPRECATED]",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "canvas_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_id" : "(required, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_api_id" : "(optional, string) [DEPRECATED]",
  "canvas_variation_id" : "(required, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Experiment Schritt Konversions-Ereignisse {#experiment-step-conversion-events}

{% apitags %}
Canvas
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:in für einen Canvas-Experiment-Schritt konvertiert.

{% tabs %}
{% tab Amplitude %}
```json
// Experiment Step Conversion (users.canvas.experimentstep.Conversion)

{
  "event_properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Step Conversion (users.canvas.experimentstep.Conversion)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Step Conversions (users.canvas.experimentstep.Conversion)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
          "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "experiment_split_name" : "(optional, string) Name of the experiment split",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Experiment Step Converted (users.canvas.experimentstep.Conversion)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
    "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.experimentstep.Conversion

{
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "conversion_behavior" : "(optional, string) JSON-encoded string describing the conversion behavior",
  "conversion_behavior_index" : "(optional, int) Index of the conversion behavior",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_split_name" : "(optional, string) Name of the experiment split",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Experiment Split Eingang Ereignisse {#experiment-split-entry-events}

{% apitags %}
Canvas
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen einen Canvas-Experiment-Schritt-Pfad betritt.

{% tabs %}
{% tab Amplitude %}
```json
// Experiment Split Entry (users.canvas.experimentstep.SplitEntry)

{
  "event_properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Experiment Split Entry (users.canvas.experimentstep.SplitEntry)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Experiment Split Entries (users.canvas.experimentstep.SplitEntry)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
          "experiment_split_name" : "(optional, string) Name of the experiment split",
          "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
          "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Experiment Split Entered (users.canvas.experimentstep.SplitEntry)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
    "experiment_split_name" : "(optional, string) Name of the experiment split",
    "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
    "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvas.experimentstep.SplitEntry

{
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "experiment_split_id" : "(optional, string) API ID of the experiment split the user enrolled in",
  "experiment_split_name" : "(optional, string) Name of the experiment split",
  "experiment_step_id" : "(optional, string) API ID of the experiment step this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "in_control_group" : "(required, boolean) Whether the user was enrolled in the control group",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Canvas-Schritt Progression Ereignisse {#canvas-step-progression-events}

{% apitags %}
Canvas, Progression
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen einen Schritt in einem Canvas mit einem bestimmten Ergebnis durchläuft. Beachten Sie, dass dieses Ereignis nicht eintritt, wenn Schritte betreten oder verlassen werden. Gegenwärtig erzeugen nur geteilte Schritte (Zielgruppen-Pfade, Decision-Split, Aktions-Pfade, Experiment) und vorgebrachte Ergebnisse Schrittfortschrittsereignisse.

{% tabs %}
{% tab Amplitude %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Canvas Step Progressions (users.canvasstep.Progression)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
          "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
          "next_step_id" : "(optional, string) API ID of the next step in the canvas",
          "progression_type" : "(required, string) What type of step progression event this is",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Canvas Step Progression (users.canvasstep.Progression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
    "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
    "next_step_id" : "(optional, string) API ID of the next step in the canvas",
    "progression_type" : "(required, string) What type of step progression event this is"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.canvasstep.Progression

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "canvas_entry_id" : "(required, string) Unique identifier for this instance of a user in a canvas",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "exit_reason" : "(optional, string) If this is an exit, the reason a user exited the canvas during the step",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_canvas_entry" : "(optional, boolean) Whether this is entry into a first step in a canvas",
  "next_step_id" : "(optional, string) API ID of the next step in the canvas",
  "progression_type" : "(required, string) What type of step progression event this is",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Banner Abbruchereignisse {#banner-abort-events}

{% apitags %}
Banner, Abbrechen
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine ursprünglich geplante Bannernachricht aus irgendeinem Grund abgebrochen wurde.

{% tabs %}
{% tab Amplitude %}
```json
// Banner Abort (users.messages.banner.Abort)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Abort (users.messages.banner.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Aborts (users.messages.banner.Abort)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Banner Aborted (users.messages.banner.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.banner.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Banner Klick-Ereignisse {#banner-click-events}

{% apitags %}
Banner, Klicks
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen auf ein Banner klickt.

{% tabs %}
{% tab Amplitude %}
```json
// Banner Click (users.messages.banner.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Click (users.messages.banner.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Clicks (users.messages.banner.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Banner Clicked (users.messages.banner.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.banner.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Banner Impressionen Ereignisse {#banner-impression-events}

{% apitags %}
Banner, Impressionen
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:in ein Banner blickt.

{% tabs %}
{% tab Amplitude %}
```json
// Banner Impression (users.messages.banner.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_model" : "(optional, string) Model of the device",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Banner Impression (users.messages.banner.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Banner Impressions (users.messages.banner.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Banner Viewed (users.messages.banner.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.banner.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "banner_placement_id" : "(optional, string) Customer specified banner placement ID",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Content-Card Abbruch-Ereignisse {#content-card-abort-events}

{% apitags %}
Abbruch, Content-Cards
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine Content-Card Nachricht aufgrund von Liquid-Abbrüchen etc. abgebrochen wurde.

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Abort (users.messages.contentcard.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Abort (users.messages.contentcard.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Aborts (users.messages.contentcard.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Aborted (users.messages.contentcard.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Content-Card Klick-Ereignisse {#content-card-click-events}

{% apitags %}
Content-Cards, Klicks
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen auf eine Content-Card klickt.

{% alert note %}
`dispatch_id` ist veraltet und wird in der nächsten Currents Version entfernt.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Click (users.messages.contentcard.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Click (users.messages.contentcard.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Clicks (users.messages.contentcard.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Clicked (users.messages.contentcard.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Für `ad_id`, `ad_id_type` und `ad_tracking_enabled` müssen Sie die iOS Identifier for Advertisers (IDFA) und Android Google Advertising ID explizit über die nativen SDKs erfassen. Erfahren Sie mehr über diese Einrichtung für [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) und [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Wenn Sie Kafka zur Aufnahme von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) Daten verwenden, wenden Sie sich an Ihren Customer-Success-Manager, um das Senden von `ad_id` zu aktivieren.
{% endapi %}

{% api %}
## Content-Card Entlassungsereignisse {#content-card-dismiss-events}

{% apitags %}
Content-Cards, Entlassung
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen eine Content-Card ablehnt.

{% alert note %}
`dispatch_id` ist veraltet und wird in der nächsten Currents Version entfernt.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Dismiss (users.messages.contentcard.Dismiss)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Dismiss (users.messages.contentcard.Dismiss)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Dismisses (users.messages.contentcard.Dismiss)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Dismissed (users.messages.contentcard.Dismiss)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Dismiss

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Für `ad_id`, `ad_id_type` und `ad_tracking_enabled` müssen Sie die iOS Identifier for Advertisers (IDFA) und Android Google Advertising ID explizit über die nativen SDKs erfassen. Erfahren Sie mehr über diese Einrichtung für [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) und [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Wenn Sie Kafka zur Aufnahme von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) Daten verwenden, wenden Sie sich an Ihren Customer-Success-Manager, um das Senden von `ad_id` zu aktivieren.
{% endapi %}

{% api %}
## Content-Card Impression Ereignisse {#content-card-impression-events}

{% apitags %}
Content-Cards, Impressionen
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen eine Content-Card ansieht.

{% alert note %}
`dispatch_id` ist veraltet und wird in der nächsten Currents Version entfernt.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Impression (users.messages.contentcard.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Impression (users.messages.contentcard.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Impressions (users.messages.contentcard.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Viewed (users.messages.contentcard.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Für `ad_id`, `ad_id_type` und `ad_tracking_enabled` müssen Sie die iOS Identifier for Advertisers (IDFA) und Android Google Advertising ID explizit über die nativen SDKs erfassen. Erfahren Sie mehr über diese Einrichtung für [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) und [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Wenn Sie Kafka zur Aufnahme von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) Daten verwenden, wenden Sie sich an Ihren Customer-Success-Manager, um das Senden von `ad_id` zu aktivieren.
{% endapi %}

{% api %}
## Content-Card Sendeereignisse {#content-card-send-events}

{% apitags %}
Content-Cards, Sendungen
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine Content-Card an einen Nutzer:innen gesendet wird.

{% alert note %}
`dispatch_id` ist veraltet und wird in der nächsten Currents Version entfernt.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Content Card Send (users.messages.contentcard.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Content Card Send (users.messages.contentcard.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Content Card Sends (users.messages.contentcard.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(required, string) ID of the card that generated this event",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Content Card Sent (users.messages.contentcard.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(required, string) ID of the card that generated this event",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.contentcard.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_card_id" : "(required, string) ID of the card that generated this event",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- `message_extras` ermöglichen es Ihnen, Ihre Sende-Events mit dynamischen Daten aus Connected-Content, angepassten Attributen (wie Sprache oder Land) und Canvas-Eingangs-Eigenschaften zu versehen. Weitere Informationen finden Sie unter [Extras für Nachrichten]({{site.baseurl}}/message_extras_tag/).
{% endapi %}

{% api %}
## E-Mail-Ereignisse abbrechen {#email-abort-events}

{% apitags %}
Abbrechen, E-Mail
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine E-Mail Nachricht aufgrund von Liquid Abbrüchen etc. abgebrochen wurde.

{% tabs %}
{% tab Amplitude %}
```json
// Email Abort (users.messages.email.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Abort (users.messages.email.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Aborts (users.messages.email.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Aborted (users.messages.email.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## E-Mail Bounce-Ereignisse {#email-bounce-events}

{% apitags %}
E-Mail, Bounce
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Internet-Provider einen Hard Bounce zurückschickt. Ein Hard Bounce bedeutet einen dauerhaften Zustellbarkeitsfehler.

{% tabs %}
{% tab Amplitude %}
```json
// Email Bounce (users.messages.email.Bounce)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Bounce (users.messages.email.Bounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Bounces (users.messages.email.Bounce)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Bounced (users.messages.email.Bounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Bounce

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_drop" : "(optional, boolean) Indicates that this event counts as a drop event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie geplant sind. Erfahren Sie mehr über das [Verhalten der ID im Versand]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## E-Mail Klick-Ereignisse {#email-click-events}

{% apitags %}
E-Mail, Klicks
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen auf eine E-Mail klickt. Es können mehrere Ereignisse für dieselbe Kampagne erzeugt werden, wenn ein Nutzer:innen mehrfach klickt oder verschiedene Links in der E-Mail anklickt.

{% tabs %}
{% tab Amplitude %}
```json
// Email Click (users.messages.email.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_model" : "(optional, string) Model of the device",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Click (users.messages.email.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Clicks (users.messages.email.Click)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
          "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
          "link_alias" : "(optional, string) Alias associated with this link ID",
          "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Link Clicked (users.messages.email.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
    "link_alias" : "(optional, string) Alias associated with this link ID",
    "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
    "link_url" : "(optional, string) URL that the user clicked on",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "is_suspected_bot_click" : "(optional, boolean) Indicates that this is a suspected bot click. Will only populate when Bot Filtering setting is enabled",
  "link_alias" : "(optional, string) Alias associated with this link ID",
  "link_id" : "(optional, string) Unique ID for the link which was clicked, as created by Braze",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "suspected_bot_click_reason" : "(optional, array of string) Reason(s) why this is a suspected bot click. Will always populate even if Bot Filtering setting is disabled.",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(optional, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie geplant sind. Erfahren Sie mehr über das [Verhalten der ID im Versand]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## E-Mail Aufschiebung von Ereignissen {#email-deferral-events}

{% apitags %}
E-Mail, Aufschub
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Internet-Provider die E-Mail nicht sofort an eine nicht hart gebouncte E-Mail-Adresse zustellt und Braze die E-Mail bis zu 72 Stunden lang erneut versucht. Typische Gründe für Aufschübe sind reputationsbasierte Rate-Limiting des Posteingangs-Anbieters für das E-Mail-Volumen, vorübergehende Verbindungsprobleme, ein volles Postfach des Empfängers oder DNS-Fehler.

{% tabs %}
{% tab Amplitude %}
```json
// Email Deferral (users.messages.email.Deferral)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Deferral (users.messages.email.Deferral)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Deferrals (users.messages.email.Deferral)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "attempt_count" : "(optional, int) Number of attempts made to send the message",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "recipient_domain" : "(optional, string) Receipient's email domain",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Deferred (users.messages.email.Deferral)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "attempt_count" : "(optional, int) Number of attempts made to send the message",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "recipient_domain" : "(optional, string) Receipient's email domain",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Deferral

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "attempt_count" : "(optional, int) Number of attempts made to send the message",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "deferral_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this deferral event",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "recipient_domain" : "(optional, string) Receipient's email domain",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie geplant sind. Erfahren Sie mehr über das [Verhalten der ID im Versand]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## E-Mail-Zustellung Ereignisse {#email-delivery-events}

{% apitags %}
E-Mail, Zustellung
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine gesendete E-Mail erfolgreich im Posteingang des Endnutzers:in angekommen ist.

{% tabs %}
{% tab Amplitude %}
```json
// Email Delivery (users.messages.email.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Delivery (users.messages.email.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Deliveries (users.messages.email.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Delivered (users.messages.email.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie geplant sind. Erfahren Sie mehr über das [Verhalten der ID im Versand]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## E-Mail Als Spam markieren Ereignisse {#email-mark-as-spam-events}

{% apitags %}
E-Mail, Spam
{% endapitags %}

Dieses Ereignis tritt ein, wenn der Endnutzer:in auf den Button "Spam" in der E-Mail drückt. Beachten Sie, dass dies nicht bedeutet, dass die E-Mail im Spam-Ordner gelandet ist, da Braze dies nicht trackt.

{% tabs %}
{% tab Amplitude %}
```json
// Email Mark As Spam (users.messages.email.MarkAsSpam)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Mark As Spam (users.messages.email.MarkAsSpam)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Marks As Spam (users.messages.email.MarkAsSpam)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Marked as Spam (users.messages.email.MarkAsSpam)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.MarkAsSpam

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie geplant sind. Erfahren Sie mehr über das [Verhalten der ID im Versand]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## E-Mail Öffentliche Veranstaltungen {#email-open-events}

{% apitags %}
E-Mail, Öffnungen
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen eine E-Mail öffnet. Es können mehrere Ereignisse für dieselbe Kampagne erzeugt werden, wenn ein Nutzer:innen die E-Mail mehrfach öffnet.

{% alert important %}
Es ist ein bekanntes Verhalten, dass die Felder für die Öffnung von E-Mails `device_model` und `mailbox_provider` leer sind. Diese können Sie vorerst ignorieren.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Email Open (users.messages.email.Open)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_model" : "(optional, string) Model of the device",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Open (users.messages.email.Open)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Opens (users.messages.email.Open)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "device_os" : "(optional, string) Device operating system extracted from user_agent",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
          "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
          "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Opened (users.messages.email.Open)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device"
    },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "device_os" : "(optional, string) Device operating system extracted from user_agent",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
    "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
    "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Open

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_class" : "(optional, string) Device class extracted from user_agent (mobile, desktop, tablet, etc...)",
  "device_model" : "(optional, string) Model of the device",
  "device_os" : "(optional, string) Device operating system extracted from user_agent",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "is_amp" : "(optional, boolean) Indicates that this is an AMP event",
  "machine_open" : "(optional, string) Populated to 'true' if the open event is triggered without user engagement, for example by an Apple device with Mail Privacy Protection enabled. Value may change over time to provide more granularity.",
  "mailbox_provider" : "(optional, string) Mailbox provider value returned by the esp for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie geplant sind. Erfahren Sie mehr über das [Verhalten der ID im Versand]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## E-Mail Ereignisse senden {#email-send-events}

{% apitags %}
E-Mail, Sendet
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine Anfrage zum Senden von E-Mails erfolgreich zwischen Braze und SendGrid übermittelt wurde. Dies bedeutet jedoch nicht, dass die E-Mail im Posteingang des Nutzers:innen eingegangen ist.

{% tabs %}
{% tab Amplitude %}
```json
// Email Send (users.messages.email.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Send (users.messages.email.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Sends (users.messages.email.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Sent (users.messages.email.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie geplant sind. Erfahren Sie mehr über das [Verhalten der ID im Versand]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
- `message_extras` ermöglichen es Ihnen, Ihre Sende-Events mit dynamischen Daten aus Connected-Content, angepassten Attributen (z.B. Sprache, Land) und Canvas-Eingangs-Eigenschaften zu versehen. Weitere Informationen finden Sie unter [Extras für Nachrichten]({{site.baseurl}}/message_extras_tag/).
{% endapi %}

{% api %}
## E-Mail Soft Bounce-Ereignisse {#email-soft-bounce-events}

{% apitags %}
E-Mail, Bounce
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Internet-Provider einen Soft Bounce zurückschickt. Ein Soft Bounce bedeutet, dass eine E-Mail aufgrund einer vorübergehenden Störung der Zustellbarkeit nicht zugestellt werden konnte.

{% tabs %}
{% tab Amplitude %}
```json
// Email Soft Bounce (users.messages.email.SoftBounce)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Soft Bounce (users.messages.email.SoftBounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Soft Bounces (users.messages.email.SoftBounce)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
          "from_domain" : "(optional, string) Sending domain for the email",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Email Soft Bounced (users.messages.email.SoftBounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
    "from_domain" : "(optional, string) Sending domain for the email",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.SoftBounce

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "bounce_reason" : "(optional, string) [PII] The SMTP reason code and user friendly message received for this bounce event",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "esp" : "(optional, string) ESP related to the event (SparkPost, SendGrid, or Amazon SES)",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_domain" : "(optional, string) Sending domain for the email",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "sending_ip" : "(optional, string) IP address from which the email send was made",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie geplant sind. Erfahren Sie mehr über das [Verhalten der ID im Versand]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## E-Mail Abmelden von Ereignissen {#email-unsubscribe-events}

{% apitags %}
E-Mail, Abo
{% endapitags %}

Dieses Ereignis tritt ein, wenn der Endnutzer:in auf "Abmelden" in der E-Mail geklickt hat.

{% alert important %}
Das Ereignis `Unsubscribe` ist eigentlich ein spezielles Klick-Ereignis, das ausgelöst wird, wenn Ihr Nutzer:in auf den Abmeldelink in der E-Mail klickt (entweder ein normaler Abmeldelink im Textkörper oder in der Fußzeile der E-Mail oder über die [Kopfzeile list-unsubscribe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/email_settings#include-a-list-unsubscribe-header)), und nicht, wenn der Nutzer:in den Status "abgemeldet" wechselt. Wenn die Änderung des Abo-Status über die API oder über einen angepassten (nicht-Braze) Abmeldelink gesendet wird, löst dies kein Ereignis auf Currents aus.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Email Unsubscribe (users.messages.email.Unsubscribe)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "email_address" : "(required, string) [PII] Email address of the user",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Email Unsubscribe (users.messages.email.Unsubscribe)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "email_address" : "(required, string) [PII] Email address of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Email Unsubscribes (users.messages.email.Unsubscribe)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "ip_pool" : "(optional, string) IP pool from which the email send was made",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user",
    "email" : "(required, string) [PII] Email address of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Unsubscribed (users.messages.email.Unsubscribe)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "email" : "(required, string) [PII] Email address of the user"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "ip_pool" : "(optional, string) IP pool from which the email send was made",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.email.Unsubscribe

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "email_address" : "(required, string) [PII] Email address of the user",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "ip_pool" : "(optional, string) IP pool from which the email send was made",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Das Verhalten für `dispatch_id` unterscheidet sich zwischen Canvas und Kampagnen, da Braze Canvas-Schritte (mit Ausnahme von Eingangsschritten, die geplant werden können) als getriggerte Ereignisse behandelt, auch wenn sie geplant sind. Erfahren Sie mehr über das [Verhalten der ID im Versand]({{site.baseurl}}/help/help_articles/data/dispatch_id/).
{% endapi %}

{% api %}
## Feature-Flag Experiment Impressionen Ereignisse {#feature-flag-experiment-impression-events}

{% apitags %}
Feature-Flags, Impressionen
{% endapitags %}

Dieses Ereignis tritt immer dann ein, wenn ein Nutzer:innen die Opportunity hatte, mit Ihrem Feature zu interagieren, oder wenn er hätte interagieren können, wenn das Feature deaktiviert ist (im Falle einer Kontrollgruppe in einem A/B-Test).

Feature-Flag Impressionen werden nur einmal pro Sitzung protokolliert.


{% tabs %}
{% tab Amplitude %}
```json
// Feature Flag Experiment Impression (users.messages.featureflag.Impression)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Feature Flag Experiment Impression (users.messages.featureflag.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Feature Flag Experiment Impressions (users.messages.featureflag.Impression)

{
  "device_info" : {
    "device_model" : "(optional, string) Model of the device",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Feature Flag Experiment Impressed (users.messages.featureflag.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.featureflag.Impression

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "carrier" : "(optional, string) Carrier of the device",
  "country" : "(optional, string) [PII] Country of the user",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "feature_flag_id_name" : "(optional, string) The Feature Flag Rollout identifier",
  "gender" : "(optional, string) [PII] Gender of the user, one of ['M', 'F', 'O', 'N', 'P']",
  "id" : "(required, string) Globally unique ID for this event",
  "language" : "(optional, string) [PII] Language of the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "sdk_version" : "(optional, string) Version of the Braze SDK in use during the event",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## In-App-Nachricht Abbruch-Ereignisse {#in-app-message-abort-events}

{% apitags %}
In-App-Nachrichten, Abbruch
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine ursprünglich geplante In-App-Nachricht abgebrochen wurde.

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Abort (users.messages.inappmessage.Abort)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Abort (users.messages.inappmessage.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Aborts (users.messages.inappmessage.Abort)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Aborted (users.messages.inappmessage.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.inappmessage.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "browser" : "(optional, string) Device browser - extracted from user_agent - on which the open occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "carrier" : "(optional, string) Carrier of the device",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "resolution" : "(optional, string) Resolution of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "version" : "(required, string) Which version of in-app message, legacy or triggered"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## In-App-Nachricht Klick-Ereignisse {#in-app-message-click-events}

{% apitags %}
In-App-Nachrichten, Klicks
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen auf eine In-App-Nachricht klickt.

{% alert note %}
`dispatch_id` ist veraltet und wird in der nächsten Currents Version entfernt.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Click (users.messages.inappmessage.Click)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Click (users.messages.inappmessage.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Clicks (users.messages.inappmessage.Click)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(optional, string) API ID of the card",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Clicked (users.messages.inappmessage.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.inappmessage.Click

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_id" : "(optional, string) ID of the button clicked, if this click represents a click on a button",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Für `ad_id`, `ad_id_type` und `ad_tracking_enabled` müssen Sie die iOS Identifier for Advertisers (IDFA) und Android Google Advertising ID explizit über die nativen SDKs erfassen. Erfahren Sie mehr über diese Einrichtung für [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) und [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Wenn Sie Kafka zur Aufnahme von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) Daten verwenden, wenden Sie sich an Ihren Customer-Success-Manager, um das Senden von `ad_id` zu aktivieren.
{% endapi %}

{% api %}
## In-App-Nachricht Impressionen Ereignisse {#in-app-message-impression-events}

{% apitags %}
In-App-Nachrichten, Impressionen
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:in eine In-App-Nachricht sieht.

{% alert note %}
`dispatch_id` ist veraltet und wird in der nächsten Currents Version entfernt.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// In-App Message Impression (users.messages.inappmessage.Impression)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// In-App Message Impression (users.messages.inappmessage.Impression)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// In-App Message Impressions (users.messages.inappmessage.Impression)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "card_id" : "(optional, string) API ID of the card",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// In-App Message Viewed (users.messages.inappmessage.Impression)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "card_id" : "(optional, string) API ID of the card",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.inappmessage.Impression

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "card_id" : "(optional, string) API ID of the card",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Für `ad_id`, `ad_id_type` und `ad_tracking_enabled` müssen Sie die iOS Identifier for Advertisers (IDFA) und Android Google Advertising ID explizit über die nativen SDKs erfassen. Erfahren Sie mehr über diese Einrichtung für [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) und [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Wenn Sie Kafka zur Aufnahme von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) Daten verwenden, wenden Sie sich an Ihren Customer-Success-Manager, um das Senden von `ad_id` zu aktivieren.
{% endapi %}

{% api %}
## Ereignisse abbrechen {#abort-events}

{% apitags %}
LINE, Abbrechen
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine geplante LINE Nachricht nicht zugestellt werden kann, bevor sie an LINE gesendet wird.

{% tabs %}
{% tab Amplitude %}
```json
// Abort (users.messages.line.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Abort (users.messages.line.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Aborts (users.messages.line.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
          "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Aborted (users.messages.line.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.line.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
  "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Klick-Ereignisse {#click-events}

{% apitags %}
LINE, Klicks
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen in einer LINE Nachricht auf einen Link klickt, dessen Domain mit der Click Tracking Domain übereinstimmt.

{% tabs %}
{% tab Amplitude %}
```json
// Click (users.messages.line.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(required, string) Shortened url that was clicked",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "timezone" : "(optional, string) Time zone of the user",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Click (users.messages.line.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(required, string) Shortened url that was clicked",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Clicks (users.messages.line.Click)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
          "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
          "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Clicked (users.messages.line.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(required, string) Shortened url that was clicked",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.line.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
  "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
  "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "short_url" : "(required, string) Shortened url that was clicked",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## LINE Eingehende Empfangsereignisse {#line-inbound-receive-events}

{% apitags %}
LINE, Eingehend Empfangen
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine LINE-Nachricht von einem Nutzer:innen empfangen wird.

{% tabs %}
{% tab Amplitude %}
```json
// LINE Inbound Receive (users.messages.line.InboundReceive)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// LINE Inbound Receive (users.messages.line.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// LINE Inbound Receives (users.messages.line.InboundReceive)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
          "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
          "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// LINE Inbound Received (users.messages.line.InboundReceive)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.line.InboundReceive

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
  "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
  "media_id" : "(optional, string) The LINE-generated ID which can be used to retrieve inbound media from LINE",
  "message_body" : "(optional, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Ereignisse senden {#send-events}

{% apitags %}
LINE, Sendet
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine LINE Nachricht an LINE gesendet wird.

{% tabs %}
{% tab Amplitude %}
```json
// Send (users.messages.line.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "timezone" : "(optional, string) Time zone of the user"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Send (users.messages.line.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Sends (users.messages.line.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
          "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Sent (users.messages.line.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
    "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.line.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "line_channel_id" : "(required, string) The LINE Channel ID the message was sent to or received from",
  "line_channel_name" : "(required, string) The LINE Channel Name the message was sent to or received from",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "native_line_id" : "(required, string) [PII] The user's Line ID from which the message was sent to or received from",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Live-Aktivitäten Ergebnisse Ereignisse {#live-activity-outcome-events}

{% apitags %}
Live-Aktivität, Ergebnis
{% endapitags %}

Dieses Ereignis tritt ein, wenn Braze eine Antwort von einem Drittanbieter erhält (e.g. APNs) nach dem Senden der Live-Aktivität

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Live Activity Outcomes (users.messages.liveactivity.Outcome)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "activity_attributes_type" : "(optional, string) Live Activity attribute type",
          "activity_id" : "(optional, string) Live Activity identifier",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
          "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
          "push_to_start_token" : "(optional, string) Live Activity push to start token",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "update_token" : "(optional, string) Live Activity update token"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Outcome (users.messages.liveactivity.Outcome)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.liveactivity.Outcome

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "live_activity_event_outcome" : "(optional, string) Outcome of Live Activity event",
  "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Live-Aktivität Ereignisse senden {#live-activity-send-events}

{% apitags %}
Live-Aktivität, Sendungen
{% endapitags %}

Dieses Ereignis tritt ein, wenn das Backend von Braze eine Anfrage an seinen Provider bezüglich der Live-Aktivität stellt

{% tabs %}
{% tab Amplitude %}
```json
// Live Activity Send (users.messages.liveactivity.Send)

{
  "event_properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Live Activity Send (users.messages.liveactivity.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "update_token" : "(optional, string) Live Activity update token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Live Activity Sends (users.messages.liveactivity.Send)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "activity_attributes_type" : "(optional, string) Live Activity attribute type",
          "activity_id" : "(optional, string) Live Activity identifier",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
          "push_to_start_token" : "(optional, string) Live Activity push to start token",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "update_token" : "(optional, string) Live Activity update token"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Live Activity Sent (users.messages.liveactivity.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "activity_attributes_type" : "(optional, string) Live Activity attribute type",
    "activity_id" : "(optional, string) Live Activity identifier",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
    "push_to_start_token" : "(optional, string) Live Activity push to start token",
    "update_token" : "(optional, string) Live Activity update token"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.liveactivity.Send

{
  "activity_attributes_type" : "(optional, string) Live Activity attribute type",
  "activity_id" : "(optional, string) Live Activity identifier",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "live_activity_event_type" : "(optional, string) Event type of Live Activity. One of ['start', 'update', 'end']",
  "push_to_start_token" : "(optional, string) Live Activity push to start token",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "update_token" : "(optional, string) Live Activity update token",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Push-Benachrichtigung Abbruchereignisse {#push-notification-abort-events}

{% apitags %}
Abbrechen, Push
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine Push-Benachrichtigung aufgrund von Liquid-Abbrüchen usw. abgebrochen wurde.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Abort (users.messages.pushnotification.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Abort (users.messages.pushnotification.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Aborts (users.messages.pushnotification.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "platform" : "(optional, string) Platform of the device"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Aborted (users.messages.pushnotification.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(required, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(optional, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Push-Benachrichtigung Bounce-Ereignisse {#push-notification-bounce-events}

{% apitags %}
Push, Sendet, Prellen
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Fehler entweder vom Apple Push Notification Service oder von Fire Cloud Messaging empfangen wird. Dies bedeutet, dass die Push Nachricht abgelehnt wurde und daher dem Gerät des Nutzers:innen nicht zugestellt werden konnte.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Bounce (users.messages.pushnotification.Bounce)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Bounce (users.messages.pushnotification.Bounce)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Bounces (users.messages.pushnotification.Bounce)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Bounced (users.messages.pushnotification.Bounce)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.Bounce

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Wenn Sie Kafka zur Aufnahme von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) Daten verwenden, wenden Sie sich an Ihren Customer-Success-Manager oder Account Manager:in, um das Feature Flipper für das Senden von `ad_id` zu aktivieren.
{% endapi %}

{% api %}
## Push-Benachrichtigung iOS Foreground Offene Ereignisse {#push-notification-ios-foreground-open-events}

{% apitags %}
Push, iOS, Sendet
{% endapitags %}

Dieses Ereignis wird von unserem [Swift SDK](https://github.com/braze-inc/braze-swift-sdk) nicht unterstützt und ist jetzt mit unserem [Obj-C SDK](https://github.com/Appboy/appboy-ios-sdk) veraltet.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification iOS Foreground Open (users.messages.pushnotification.IosForeground)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification iOS Foreground Open (users.messages.pushnotification.IosForeground)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Ios Foreground Push Opened (users.messages.pushnotification.IosForeground)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.IosForeground

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Für `ad_id`, `ad_id_type` und `ad_tracking_enabled` müssen Sie die iOS Identifier for Advertisers (IDFA) und Android Google Advertising ID explizit über die nativen SDKs erfassen. Erfahren Sie mehr über diese Einrichtung für [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) und [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Wenn Sie Kafka zur Aufnahme von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) Daten verwenden, wenden Sie sich an Ihren Customer-Success-Manager, um das Senden von `ad_id` zu aktivieren.
{% endapi %}

{% api %}
## Push-Benachrichtigung Offene Ereignisse {#push-notification-open-events}

{% apitags %}
Push, Öffnet
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen direkt auf die Push-Benachrichtigung klickt, um die Anwendung zu öffnen. Derzeit referenzieren Push Open Events auf "Direkte Öffnungen" und nicht auf "Gesamte Öffnungen". Dazu gehören nicht die auf Kampagnenebene angezeigten Statistiken über "beeinflusste Öffnungen", da diese nicht auf der Ebene der Nutzer:innen attributiert werden.

{% alert note %}
In seltenen Fällen kann es vorkommen, dass eine Push-Öffnung vor dem entsprechenden Push-Sendeereignis in den Currents Daten erscheint, und zwar aus folgenden Gründen:
- Ihr SDK hat eine falsche Uhr.
- Hohe Latenzzeit beim Schreiben von Stapeln. Die aufgezeichnete Sendezeit kann hinter frühen Zustellungen zurückbleiben, so dass sehr schnelle Öffnungen protokolliert werden können, bevor der endgültige Sendezeitstempel des Stapels geschrieben wird. Große Sendungen werden in Stapeln versandt und erfasst.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Open (users.messages.pushnotification.Open)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_model" : "(optional, string) Model of the device",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "os_version" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Open (users.messages.pushnotification.Open)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "$device" : "(optional, string) Model of the device",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "$os" : "(optional, string) Version of the operating system of the device",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Opens (users.messages.pushnotification.Open)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "device_model" : "(optional, string) Model of the device",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Tapped (users.messages.pushnotification.Open)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : {
      "model" : "(optional, string) Model of the device",
      "type" : "(optional, string) Platform of the device"
    },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.Open

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "button_action_type" : "(optional, string) Action type of the push notification button, null if not from a button click. One of ['uri', 'deep_link', 'none', 'close']",
  "button_string" : "(optional, string) Identifier (button_string) of the push notification button clicked. null if not from a button click",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "device_model" : "(optional, string) Model of the device",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "os_version" : "(optional, string) Version of the operating system of the device",
  "platform" : "(optional, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Für `ad_id`, `ad_id_type` und `ad_tracking_enabled` müssen Sie die iOS Identifier for Advertisers (IDFA) und Android Google Advertising ID explizit über die nativen SDKs erfassen. Erfahren Sie mehr über diese Einrichtung für [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) und [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Wenn Sie Kafka zur Aufnahme von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) Daten verwenden, wenden Sie sich an Ihren Customer-Success-Manager, um das Senden von `ad_id` zu aktivieren.
{% endapi %}

{% api %}
## Push-Benachrichtigung Ereignisse senden {#push-notification-send-events}

{% apitags %}
Push, sendet
{% endapitags %}

Dieses Ereignis tritt ein, wenn Braze eine Push-Nachricht für einen Nutzer:innen verarbeitet und diese an den Apple Push Notification Service oder Fire Cloud Messaging weiterleitet. Das bedeutet nicht, dass der Push dem Gerät zugestellt wurde, sondern nur, dass eine Nachricht gesendet wurde.

{% tabs %}
{% tab Amplitude %}
```json
// Push Notification Send (users.messages.pushnotification.Send)

{
  "adid" : "(optional, string) [PII] Advertising identifier",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "idfa" : "(optional, string) [PII] Advertising identifier",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Push Notification Send (users.messages.pushnotification.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(optional, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Push Notification Sends (users.messages.pushnotification.Send)

{
  "device_info" : {
    "android_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred",
    "limit_ad_tracking" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "microsoft_advertising_id" : "(optional, string) [PII] Advertising identifier",
    "platform" : "(optional, string) Platform of the device",
    "roku_advertising_id" : "(optional, string) [PII] Advertising identifier"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "app_id" : "(optional, string) API ID of the app on which this event occurred",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Push Notification Sent (users.messages.pushnotification.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "ad_id" : "(optional, string) [PII] Advertising identifier",
    "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
    "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "app_id" : "(optional, string) API ID of the app on which this event occurred",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "platform" : "(required, string) Platform of the device",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.pushnotification.Send

{
  "ad_id" : "(optional, string) [PII] Advertising identifier",
  "ad_id_type" : "(optional, string) One of ['ios_idfa', 'google_ad_id', 'windows_ad_id', 'roku_ad_id']",
  "ad_tracking_enabled" : "(optional, boolean) Whether advertising tracking is enabled for the device",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "app_id" : "(required, string) API ID of the app on which this event occurred",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "locale_key" : "(optional, string) [PII] The key corresponding to the translations (for example 'en-us') used to compose this message (null for default).",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "platform" : "(required, string) Platform of the device",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- Für `ad_id`, `ad_id_type` und `ad_tracking_enabled` müssen Sie die iOS Identifier for Advertisers (IDFA) und Android Google Advertising ID explizit über die nativen SDKs erfassen. Erfahren Sie mehr über diese Einrichtung für [iOS]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift) und [Android]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=android#android_google-advertising-id).
- Wenn Sie Kafka zur Aufnahme von [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) Daten verwenden, wenden Sie sich an Ihren Customer-Success-Manager, um das Senden von `ad_id` zu aktivieren.
- `message_extras` ermöglichen es Ihnen, Ihre Sende-Events mit dynamischen Daten aus Connected-Content, angepassten Attributen (z.B. Sprache, Land) und Canvas-Eingangs-Eigenschaften zu versehen. Weitere Informationen finden Sie unter [Extras für Nachrichten]({{site.baseurl}}/message_extras_tag/).
{% endapi %}

{% api %}
## Ereignisse abbrechen {#abort--events}

{% apitags %}
RCS, Abbruch
{% endapitags %}

Dieses Ereignis wird erzeugt, wenn ein RCS-Sendevorgang aufgrund eines in Braze erkannten Fehlers unterbrochen und die Nachricht verworfen wird.

{% tabs %}
{% tab Amplitude %}
```json
// Abort  (users.messages.rcs.Abort)

{
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) The type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Abort  (users.messages.rcs.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) The type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Aborts (users.messages.rcs.Abort)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) The type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Aborted (users.messages.rcs.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) The type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) The type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Klick-Ereignisse {#click-events}

{% apitags %}
RCS, Klicks
{% endapitags %}

Ein Ereignis, das erzeugt wird, wenn der Nutzer:in mit einer RCS Nachricht so interagiert, dass er auf ein UI-Element tippt oder klickt.

{% tabs %}
{% tab Amplitude %}
```json
// Click (users.messages.rcs.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
    "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
    "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(optional, string) The shortened URL that a user clicks on",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "suspected_bot_click_reason" : "(optional, array of string) Reasons why this event was classified as a bot",
    "url" : "(optional, string) The full URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the click occurred",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Click (users.messages.rcs.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
    "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(optional, string) The shortened URL that a user clicks on",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "suspected_bot_click_reason" : "(optional, array of string) Reasons why this event was classified as a bot",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) The full URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the click occurred",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Clicks (users.messages.rcs.Click)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
          "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
          "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
          "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "short_url" : "(optional, string) The shortened URL that a user clicks on",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "url" : "(optional, string) The full URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the click occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Clicked (users.messages.rcs.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
    "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
    "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "short_url" : "(optional, string) The shortened URL that a user clicks on",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "suspected_bot_click_reason" : "(optional, array of string) Reasons why this event was classified as a bot",
    "user_agent" : "(optional, string) User agent on which the click occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "element_label" : "(optional, string) Optional details about the clicked element, such as the text of a suggested reply or button. \nExample: Button or chip text (will be reply message body for reply chips and buttons)",
  "element_type" : "(optional, string) Specifies if an interaction_type that is common across suggestions and buttons came from a suggestion or button. Examples: Suggestion, Button",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "interaction_type" : "(required, string) The type of interaction that generated the click. Example string values: Text URL, Reply, OpenURL",
  "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "short_url" : "(optional, string) The shortened URL that a user clicks on",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "suspected_bot_click_reason" : "(optional, array of string) Reasons why this event was classified as a bot",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "url" : "(optional, string) The full URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the click occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Ereignisse der Zustellung {#delivery-events}

{% apitags %}
RCS, Zustellung
{% endapitags %}

Dieses Ereignis wird erstellt, wenn eine RCS Nachricht erfolgreich an das mobile Gerät eines Nutzers:innen zugestellt wurde.

{% tabs %}
{% tab Amplitude %}
```json
// Delivery (users.messages.rcs.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Delivery (users.messages.rcs.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Deliveries (users.messages.rcs.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Delivered (users.messages.rcs.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eingehende Empfangsereignisse {#inbound-receive-events}

{% apitags %}
RCS, Eingehend empfangen
{% endapitags %}

Dieses Ereignis wird erstellt, wenn Braze eine RCS Nachricht empfängt, die vom Nutzer:innen stammt.

{% tabs %}
{% tab Amplitude %}
```json
// Inbound Receive (users.messages.rcs.InboundReceive)

{
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Inbound Receive (users.messages.rcs.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Inbound Receives (users.messages.rcs.InboundReceive)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Inbound Received (users.messages.rcs.InboundReceive)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(required, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_rcs_sender" : "(required, string) The inbound RCS sender that the message was sent to",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Ereignisse lesen {#read-events}

{% apitags %}
RCS, Lesen
{% endapitags %}

Dieses Ereignis wird erstellt, wenn ein Nutzer:innen eine RCS Nachricht auf seinem Gerät öffnet und damit anzeigt, dass er den Inhalt der Nachricht gesehen oder gelesen hat.

{% tabs %}
{% tab Amplitude %}
```json
// Read (users.messages.rcs.Read)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Read (users.messages.rcs.Read)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Reads (users.messages.rcs.Read)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Read (users.messages.rcs.Read)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Read

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Ablehnende Ereignisse {#rejection-events}

{% apitags %}
RCS, Ablehnung
{% endapitags %}

Ein Ereignis, das erzeugt wird, wenn eine RCS-Nachricht aufgrund eines Eingriffs des Netzbetreibers nicht an das mobile Gerät eines Nutzers:innen zugestellt werden kann.

{% tabs %}
{% tab Amplitude %}
```json
// Rejection (users.messages.rcs.Rejection)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) The error code from the provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Rejection (users.messages.rcs.Rejection)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) The error code from the provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Rejections (users.messages.rcs.Rejection)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
          "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) The error code from the provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Rejected (users.messages.rcs.Rejection)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) The error code from the provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Rejection

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
  "id" : "(required, string) Globally unique ID for this event",
  "is_sms_fallback" : "(optional, boolean) Indicates if SMS fallback was attempted for this rejected RCS message. It is linked/paired to the SMS Delivery event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) The error code from the provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Ereignisse senden {#send-events}

{% apitags %}
RCS, Sendungen
{% endapitags %}

Dieses Ereignis wird erstellt, wenn eine RCS Nachricht von Braze aus an unsere Partner für die Zustellung auf der letzten Meile gesendet wird.

{% tabs %}
{% tab Amplitude %}
```json
// Send (users.messages.rcs.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Send (users.messages.rcs.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Sends (users.messages.rcs.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
          "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Sent (users.messages.rcs.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
    "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.rcs.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_rcs_sender" : "(optional, string) The RCS sender ID or agent name used to send the message",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "to_phone_number" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS-Abbruch-Ereignisse {#sms-abort-events}

{% apitags %}
Abbrechen, SMS
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine SMS Nachricht aufgrund von Liquid Abbrüchen etc. abgebrochen wurde.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Abort (users.messages.sms.Abort)

{
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Abort (users.messages.sms.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Aborts (users.messages.sms.Abort)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Aborted (users.messages.sms.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS-Träger senden Ereignisse {#sms-carrier-send-events}

{% apitags %}
SMS, Sendet
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine SMS an den Netzbetreiber gesendet wird.

{% alert important %}
`CarrierSend` wird nur für Nutzer:innen von Legacy-Infrastrukturen unterstützt.
{% endalert %}

{% tabs %}
{% tab Amplitude %}
```json
// SMS Carrier Send (users.messages.sms.CarrierSend)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Carrier Send (users.messages.sms.CarrierSend)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Carrier Sends (users.messages.sms.CarrierSend)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Sent to Carrier (users.messages.sms.CarrierSend)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.CarrierSend

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS-Zustellung Ereignisse {#sms-delivery-events}

{% apitags %}
SMS, Zustellung
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine SMS erfolgreich an das Mobiltelefon des Nutzers:innen zugestellt wurde.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Delivery (users.messages.sms.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery (users.messages.sms.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Deliveries (users.messages.sms.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Delivered (users.messages.sms.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS-Zustellungsfehlerereignisse {#sms-delivery-failure-events}

{% apitags %}
SMS, Zustellung
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine SMS nicht zugestellt werden kann. Verwenden Sie dieses Ereignis und die bereitgestellten Fehlercodes, um Probleme mit der SMS-Zustellung zu beheben.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Delivery Failure (users.messages.sms.DeliveryFailure)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Delivery Failure (users.messages.sms.DeliveryFailure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Delivery Failures (users.messages.sms.DeliveryFailure)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) Error code from the SMS provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Delivery Failed (users.messages.sms.DeliveryFailure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.DeliveryFailure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) Error code from the SMS provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eingehende SMS Empfangene Ereignisse {#sms-inbound-received-events}

{% apitags %}
SMS, Eingehend empfangen
{% endapitags %}

Dieses Ereignis tritt ein, wenn einer Ihrer Nutzer:innen eine SMS an eine Rufnummer in einer Ihrer Abo-Gruppen von Braze sendet.

Wenn Braze eine eingehende SMS empfängt, attributieren wir diese eingehende Nachricht jedem Nutzer:in, der diese Telefonnummer hat. Daher erhalten Sie möglicherweise mehrere Ereignisse pro eingehender Nachricht, wenn mehrere Nutzer:innen in Ihrer Braze-Instanz dieselbe Telefonnummer haben. Wenn Sie eine Attribution bestimmter Nutzer:in auf der Grundlage früherer Nachrichten an diesen Nutzer benötigen, können Sie das Ereignis SMS zugestellt verwenden, um eingehende Ereignisse der Nutzer:in zuzuordnen, die zuletzt eine Nachricht von Ihrer Braze-Nummer erhalten haben.

Wenn wir feststellen, dass diese eingehende Nachricht eine Antwort auf eine ausgehende Kampagne oder eine Canvas-Komponente ist, die von Braze gesendet wurde, fügen wir dem Ereignis auch die Metadaten der Kampagne oder des Canvas bei. Braze definiert eine Antwort als eine eingehende Nachricht, die innerhalb von vier Stunden nach einer ausgehenden Nachricht eintrifft. Es gibt jedoch einen einminütigen Zwischenspeicher für die Attribution von Kampagneninformationen der letzten ausgehenden SMS.


{% tabs %}
{% tab Amplitude %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Inbound Received (users.messages.sms.InboundReceive)

{
  "anonymousId" : "(optional, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(required, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(required, string) Typed response from the user",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS Ablehnungsereignisse {#sms-rejection-events}

{% apitags %}
SMS, Ablehnung
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine SMS vom Netzbetreiber abgelehnt wird. Dies kann aus verschiedenen Gründen geschehen. Verwenden Sie dieses Ereignis und die bereitgestellten Fehlercodes, um Probleme mit der SMS-Zustellung zu beheben.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Rejection (users.messages.sms.Rejection)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Rejection (users.messages.sms.Rejection)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Rejections (users.messages.sms.Rejection)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "error" : "(optional, string) Error name",
          "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
          "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(optional, string) Error code from the SMS provider",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Rejected (users.messages.sms.Rejection)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "error" : "(optional, string) Error name",
    "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
    "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(optional, string) Error code from the SMS provider",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.Rejection

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "error" : "(optional, string) Error name",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "from_phone_number" : "(optional, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "is_sms_fallback" : "(optional, boolean) Indicates that a SMS fallback message was sent due to a rejected RCS message. The message could result in delivery, delivery failure, or rejection. It can be linked to the RCS Rejection event via a send ID and dispatch ID\nIt can be linked to the RCS Rejection event via a send ID and dispatch ID. (Event property)",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(optional, string) Error code from the SMS provider",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## SMS-Sendeereignisse {#sms-send-events}

{% apitags %}
SMS, Sendet
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen eine SMS sendet.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Send (users.messages.sms.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Send (users.messages.sms.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Sends (users.messages.sms.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Sent (users.messages.sms.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "category" : "(optional, string) Keyword category name, only populated for auto-reply messages: 'opt-in', 'opt-out', 'help', or custom value",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- `message_extras` ermöglichen es Ihnen, Ihre Sende-Events mit dynamischen Daten aus Connected-Content, angepassten Attributen (z.B. Sprache, Land) und Canvas-Eingangs-Eigenschaften zu versehen. Weitere Informationen finden Sie unter [Extras für Nachrichten]({{site.baseurl}}/message_extras_tag/).
{% endapi %}

{% api %}
## SMS Short Link Klick-Ereignisse {#sms-short-link-click-events}

{% apitags %}
SMS, Klicks
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen auf einen SMS-Kurzlink klickt.

{% tabs %}
{% tab Amplitude %}
```json
// SMS Short Link Click (users.messages.sms.ShortLinkClick)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// SMS Short Link Click (users.messages.sms.ShortLinkClick)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// SMS Short Link Clicks (users.messages.sms.ShortLinkClick)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// SMS Short Link Clicked (users.messages.sms.ShortLinkClick)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.sms.ShortLinkClick

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "is_suspected_bot_click" : "(optional, boolean) Whether this event was processed as a bot event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "short_url" : "(required, string) Shortened url that was clicked",
  "suspected_bot_click_reason" : "(optional, array of string) Why this event was classified as a bot",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Webhook Abbruch-Ereignisse {#webhook-abort-events}

{% apitags %}
Abbrechen, Webhooks
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine Webhook Nachricht aufgrund von Liquid Abbrüchen etc. abgebrochen wurde.

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Abort (users.messages.webhook.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Abort (users.messages.webhook.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Aborts (users.messages.webhook.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Aborted (users.messages.webhook.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.webhook.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Webhook-Ausfallereignisse {#webhook-failure-events}

{% apitags %}
Fehlschlag, Webhooks
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine Webhook Nachricht zugestellt wurde, aber mit einer Fehlerantwort des Endpunkts fehlgeschlagen ist.

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Failure (users.messages.webhook.Failure)

{
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Failure (users.messages.webhook.Failure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Failures (users.messages.webhook.Failure)

{
  "device_info" : { },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "content_length" : "(optional, int) Content length of the response",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
          "host" : "(optional, string) The host of the webhook URL that returned a failure response",
          "http_status_code" : "(optional, int) HTTP status code of the response",
          "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "raw_response" : "(optional, string) Truncated raw response from endpoint",
          "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
          "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
          "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Failed (users.messages.webhook.Failure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "content_length" : "(optional, int) Content length of the response",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
    "host" : "(optional, string) The host of the webhook URL that returned a failure response",
    "http_status_code" : "(optional, int) HTTP status code of the response",
    "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "raw_response" : "(optional, string) Truncated raw response from endpoint",
    "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
    "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
    "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.webhook.Failure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "content_length" : "(optional, int) Content length of the response",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "endpoint_url" : "(optional, string) The endpoint URL of the failed webhook",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "host" : "(optional, string) The host of the webhook URL that returned a failure response",
  "http_status_code" : "(optional, int) HTTP status code of the response",
  "id" : "(required, string) Globally unique ID for this event",
  "is_terminal" : "(optional, boolean) Whether this event was the terminal attempt in a send",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "raw_response" : "(optional, string) Truncated raw response from endpoint",
  "retry_count" : "(optional, int) Number of webhook sends attempted before giving up",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "url_path" : "(optional, string) The path of the webhook URL that returned a failure response",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "webhook_duration" : "(optional, int) Total duration of this request in milliseconds",
  "webhook_failure_source" : "(optional, string) To tell whether an error was created by Braze or by the endpoint itself. The source field could be External Endpoint, Treat no status code to host unreachable"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Webhook Ereignisse senden {#webhook-send-events}

{% apitags %}
Webhooks, Sendungen
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Webhook verarbeitet und an die in diesem Webhook angegebene Drittpartei gesendet wurde. Beachten Sie, dass dies keine Aussage darüber macht, ob die Anfrage empfangen wurde oder nicht.

{% tabs %}
{% tab Amplitude %}
```json
// Webhook Send (users.messages.webhook.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// Webhook Send (users.messages.webhook.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// Webhook Sends (users.messages.webhook.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : { },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// Webhook Sent (users.messages.webhook.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : { }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.webhook.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

#### Merkmale der Eigenschaft

- `message_extras` ermöglichen es Ihnen, Ihre Sende-Events mit dynamischen Daten aus Connected-Content, angepassten Attributen (wie Sprache oder Land) und Canvas-Eingangs-Eigenschaften zu versehen. Weitere Informationen finden Sie unter [Extras für Nachrichten]({{site.baseurl}}/message_extras_tag/).
{% endapi %}

{% api %}
## WhatsApp Abbruch-Ereignisse {#whatsapp-abort-events}

{% apitags %}
WhatsApp, Abbrechen
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine WhatsApp Nachricht aufgrund von Liquid Abbrüchen etc. abgebrochen wurde.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Abort (users.messages.whatsapp.Abort)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Abort (users.messages.whatsapp.Abort)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Aborts (users.messages.whatsapp.Abort)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
          "abort_type" : "(optional, string) Type of abort",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Aborted (users.messages.whatsapp.Abort)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
    "abort_type" : "(optional, string) Type of abort",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Abort

{
  "abort_log" : "(optional, string) [PII] Log message describing abort details (up to 128 chars)",
  "abort_type" : "(optional, string) Type of abort",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp Tracking Link Klick-Ereignisse {#whatsapp-tracked-link-click-events}

{% apitags %}
WhatsApp, Klicks
{% endapitags %}

Dieses Ereignis tritt ein, wenn ein Nutzer:innen in einer WhatsApp Nachricht auf einen Link oder Button klickt, dessen Domain mit der Click Tracking Domain übereinstimmt.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Tracked Link Click (users.messages.whatsapp.Click)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "timezone" : "(optional, string) Time zone of the user",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Tracked Link Click (users.messages.whatsapp.Click)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "time" : "(required, int) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "url" : "(optional, string) URL that the user clicked on",
    "user_agent" : "(optional, string) User agent on which the spam report occurred",
    "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Tracked Link Clicks (users.messages.whatsapp.Click)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "short_url" : "(required, string) Shortened url that was clicked",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "url" : "(optional, string) URL that the user clicked on",
          "user_agent" : "(optional, string) User agent on which the spam report occurred"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, int) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Tracked Link Clicked (users.messages.whatsapp.Click)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "short_url" : "(required, string) Shortened url that was clicked",
    "user_agent" : "(optional, string) User agent on which the spam report occurred"
  },
  "timestamp" : "(required, int) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Click

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "id" : "(required, string) Globally unique ID for this event",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "short_url" : "(required, string) Shortened url that was clicked",
  "time" : "(required, int) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "url" : "(required, string) URL that the user clicked on",
  "user_agent" : "(optional, string) User agent on which the spam report occurred",
  "user_id" : "(required, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(optional, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp Zustellung Ereignisse {#whatsapp-delivery-events}

{% apitags %}
WhatsApp, Zustellung
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine gesendete WhatsApp Nachricht erfolgreich auf dem Gerät des Nutzers:innen angekommen ist.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Delivery (users.messages.whatsapp.Delivery)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Delivery (users.messages.whatsapp.Delivery)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Deliveries (users.messages.whatsapp.Delivery)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Delivered (users.messages.whatsapp.Delivery)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Delivery

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp-Ausfallereignisse {#whatsapp-failure-events}

{% apitags %}
WhatsApp, Scheitern
{% endapitags %}

Dieses Ereignis tritt ein, wenn WhatsApp die Nachricht dem Nutzer:innen nicht zugestellt werden kann. Ein Hard Bounce bedeutet einen dauerhaften Zustellbarkeitsfehler.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Failure (users.messages.whatsapp.Failure)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Failure (users.messages.whatsapp.Failure)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Failures (users.messages.whatsapp.Failure)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "provider_error_code" : "(required, string) Error code from WhatsApp",
          "provider_error_title" : "(required, string) Description of error from WhatsApp",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Failed (users.messages.whatsapp.Failure)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "provider_error_code" : "(required, string) Error code from WhatsApp",
    "provider_error_title" : "(required, string) Description of error from WhatsApp",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Failure

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "provider_error_code" : "(required, string) Error code from WhatsApp",
  "provider_error_title" : "(required, string) Description of error from WhatsApp",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## Eingehende WhatsApp-Ereignisse {#whatsapp-inbound-received-events}

{% apitags %}
WhatsApp, Eingehend Empfangen
{% endapitags %}

Dieses Ereignis tritt ein, wenn einer Ihrer Nutzer:innen eine WhatsApp Nachricht an eine Rufnummer in einer Ihrer Abo-Gruppen von Braze WhatsApp sendet.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
    "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
    "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "productId" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
    "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
    "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "product_id" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "token" : "(required, string) The Mixpanel API token",
    "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
          "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
          "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
          "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
          "message_body" : "(optional, string) Typed response from the user",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "product_id" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
          "quick_reply_text" : "(optional, string) Text of button pressed by the user",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] The user's phone number from which the message was received"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Inbound Received (users.messages.whatsapp.InboundReceive)

{
  "anonymousId" : "(optional, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(required, string) [PII] The user's phone number from which the message was received"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
    "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
    "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
    "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
    "media_urls" : "(optional, array of string) Media URLs from the user",
    "message_body" : "(optional, string) Typed response from the user",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "product_id" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
    "quick_reply_text" : "(optional, string) Text of button pressed by the user",
    "subscription_group_id" : "(optional, string) Subscription group API ID"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.InboundReceive

{
  "action" : "(required, string) Action taken in response to this message. (for example Subscribed, Unsubscribed or None).",
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "catalog_id" : "(optional, string) Catalog ID of a product if a product is referenced in the inbound message. Otherwise, empty.",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the user is responding to a WhatsApp Flow.",
  "flow_response_json" : "(optional, string) [PII] The form values the user responded with. Present if the user is responding to a WhatsApp Flow.",
  "id" : "(required, string) Globally unique ID for this event",
  "in_reply_to" : "(optional, string) The message_id of the message this message was replying to",
  "inbound_phone_number" : "(required, string) The inbound number that the message was sent to",
  "media_urls" : "(optional, array of string) Media URLs from the user",
  "message_body" : "(optional, string) Typed response from the user",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "product_id" : "(optional, string) Product SKU if a product is referenced in the inbound message. Otherwise, empty.",
  "quick_reply_text" : "(optional, string) Text of button pressed by the user",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "user_id" : "(optional, string) Braze user ID of the user who performed this event",
  "user_phone_number" : "(required, string) [PII] The user's phone number from which the message was received"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp Ereignisse lesen {#whatsapp-read-events}

{% apitags %}
WhatsApp, Lesen
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine WhatsApp Nachricht von einem Nutzer:innen gelesen wird.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Reads (users.messages.whatsapp.Read)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Read (users.messages.whatsapp.Read)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Read

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp manager. Present if sending a Template Message",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}

{% api %}
## WhatsApp Ereignisse senden {#whatsapp-send-events}

{% apitags %}
WhatsApp, Sendet
{% endapitags %}

Dieses Ereignis tritt ein, wenn eine Sendeanfrage erfolgreich zwischen Braze und WhatsApp übermittelt wurde. Dies bedeutet jedoch nicht, dass die Nachricht bei dem Nutzer:innen angekommen ist.

{% tabs %}
{% tab Amplitude %}
```json
// WhatsApp Send (users.messages.whatsapp.Send)

{
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "event_properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "event_type" : "(required, string) The event type name, as it is exported to Amplitude",
  "insert_id" : "(required, string) Globally unique ID for this event",
  "library" : "Braze",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "user_id" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Mixpanel %}
```json
// WhatsApp Send (users.messages.whatsapp.Send)

{
  "event" : "(required, string) The event type name, as it is exported to Mixpanel",
  "properties" : {
    "$partner_id" : "braze",
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "distinct_id" : "(required, string) [PII] External ID of the user",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "$insert_id" : "(required, string) Globally unique ID for this event",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message",
    "time" : "(required, long) UNIX timestamp at which the event happened",
    "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
    "token" : "(required, string) The Mixpanel API token"
  }
}
```
{% endtab %}

{% tab mParticle %}
```json
// WhatsApp Sends (users.messages.whatsapp.Send)

{
  "device_info" : {
    "ios_idfv" : "(optional, string) ID of the device on which the event occurred"
  },
  "environment" : "(required, string) The mParticle environment (either 'development' or 'production')",
  "events" : [
    {
      "data" : {
        "custom_attributes" : {
          "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
          "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
          "campaign_name" : "(optional, string) Name of the campaign",
          "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
          "canvas_name" : "(optional, string) Name of the Canvas",
          "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
          "canvas_step_name" : "(optional, string) Name of the Canvas step",
          "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
          "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
          "device_id" : "(optional, string) ID of the device on which the event occurred",
          "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
          "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
          "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
          "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
          "message_id" : "(optional, string) The unique ID generated by Meta for this message",
          "message_variation_id" : "(optional, string) API ID of the message variation this user received",
          "message_variation_name" : "(optional, string) Name of the message variation",
          "send_id" : "(optional, string) Message send ID this message belongs to",
          "source_request_id" : "(required, string) Globally unique ID for this event",
          "subscription_group_id" : "(optional, string) Subscription group API ID",
          "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message"
        },
        "custom_event_type" : "(required, string) The mParticle custom event type if the event_type is 'custom_event' (always 'other')",
        "event_name" : "(required, string) The event type name, as it is exported to mParticle",
        "source_message_id" : "(required, string) Globally unique ID for this event",
        "timestamp_unixtime_ms" : "(required, long) UNIX timestamp at which the event happened"
      },
      "event_type" : "(required, string) mParticle event type (either 'uninstall' or 'custom_event')"
    }
  ],
  "schema_version" : 2,
  "user_attributes" : {
    "$mobile" : "(required, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
  },
  "user_identities" : {
    "customerid" : "(required, string) [PII] External ID of the user"
  }
}
```
{% endtab %}

{% tab Segment %}
```json
// WhatsApp Sent (users.messages.whatsapp.Send)

{
  "anonymousId" : "(required, string) Braze user ID of the user who performed this event",
  "context" : {
    "device" : { },
    "traits" : {
      "phone" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)"
    }
  },
  "event" : "(required, string) The event type name, as it is exported to Segment",
  "messageId" : "(required, string) Globally unique ID for this event",
  "properties" : {
    "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
    "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
    "campaign_name" : "(optional, string) Name of the campaign",
    "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
    "canvas_name" : "(optional, string) Name of the Canvas",
    "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
    "canvas_step_name" : "(optional, string) Name of the Canvas step",
    "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
    "canvas_variation_name" : "(optional, string) Name of the Canvas variation this user received",
    "device_id" : "(optional, string) ID of the device on which the event occurred",
    "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
    "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
    "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
    "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
    "message_id" : "(optional, string) The unique ID generated by Meta for this message",
    "message_variation_id" : "(optional, string) API ID of the message variation this user received",
    "message_variation_name" : "(optional, string) Name of the message variation",
    "send_id" : "(optional, string) Message send ID this message belongs to",
    "subscription_group_id" : "(optional, string) Subscription group API ID",
    "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message"
  },
  "timestamp" : "(required, long) UNIX timestamp at which the event happened",
  "type" : "track",
  "userId" : "(optional, string) [PII] External ID of the user"
}
```
{% endtab %}

{% tab Cloud Storage %}
```json
// users.messages.whatsapp.Send

{
  "app_group_id" : "(optional, string) API ID of the app group this user belongs to",
  "campaign_id" : "(optional, string) API ID of the campaign this event belongs to",
  "campaign_name" : "(optional, string) Name of the campaign",
  "canvas_id" : "(optional, string) API ID of the Canvas this event belongs to",
  "canvas_name" : "(optional, string) Name of the Canvas",
  "canvas_step_id" : "(optional, string) API ID of the Canvas step this event belongs to",
  "canvas_step_message_variation_id" : "(optional, string) API ID of the Canvas step message variation this user received",
  "canvas_step_name" : "(optional, string) Name of the Canvas step",
  "canvas_variation_id" : "(optional, string) API ID of the Canvas variation this event belongs to",
  "device_id" : "(optional, string) ID of the device on which the event occurred",
  "dispatch_id" : "(optional, string) ID of the dispatch this message belongs to",
  "external_user_id" : "(optional, string) [PII] External ID of the user",
  "flow_id" : "(optional, string) The unique ID of the Flow in the WhatsApp Manager. Present if the message includes a CTA to respond to a WhatsApp Flow",
  "from_phone_number" : "(required, string) Phone number used to send in e.164 format (for example +14155552671)",
  "id" : "(required, string) Globally unique ID for this event",
  "message_extras" : "(optional, string) [PII] A JSON string of the tagged key-value pairs during liquid rendering",
  "message_id" : "(optional, string) The unique ID generated by Meta for this message",
  "message_variation_id" : "(optional, string) API ID of the message variation this user received",
  "message_variation_name" : "(optional, string) Name of the message variation",
  "send_id" : "(optional, string) Message send ID this message belongs to",
  "subscription_group_id" : "(optional, string) Subscription group API ID",
  "template_name" : "(optional, string) [PII] Name of the template in the WhatsApp Manager. Present if sending a Template Message",
  "time" : "(required, long) UNIX timestamp at which the event happened",
  "timezone" : "(optional, string) Time zone of the user",
  "to_phone_number" : "(optional, string) [PII] Phone number of the user receiving the message in e.164 format (for example +14155552671)",
  "user_id" : "(required, string) Braze user ID of the user who performed this event"
}
```
{% endtab %}
{% endtabs %}

{% endapi %}