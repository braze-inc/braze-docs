---
nav_title: "SMS Objekt"
article_title: SMS Messaging Objekt
page_order: 10
page_type: reference
channel: SMS
description: "Dieser referenzierte Artikel erklärt die verschiedenen Komponenten des Braze SMS-Objekts."

---
# SMS-Objekt

> Mit dem Objekt `sms` können Sie über unsere [Messaging-Endpunkte]({{site.baseurl}}/api/endpoints/messaging) SMS-Nachrichten ändern oder erstellen.

```json
{
    "subscription_group_id": (required, string) the ID of your subscription group,
    "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
    "body": (required, string),
    "app_id": (required, string) see App Identifier,
    "media_items" :(optional, array) use this field to pass an image URL in an MMS to send an image with your message,
    "link_shortening_enabled": (optional, boolean) use this field to turn on link shortening and campaign-level click tracking,
    "user_click_tracking_enabled": (optional, boolean) if link_shortening_enabled is true, use this field to turn on link shortening, and campaign-level and user-level click tracking.     
}
```

- [Bezeichner der App]({{site.baseurl}}/api/identifier_types/)
  - Jede gültige `app_id` von einer App, die in Ihrem Workspace konfiguriert ist, funktioniert für alle Nutzer:innen in Ihrem Workspace, unabhängig davon, ob der Nutzer die spezifische App in seinem Profil hat oder nicht.