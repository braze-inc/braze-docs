---
nav_title: Movable Ink
alias: "/movable_ink/"
---
# Movable Ink

> [Moveable Ink][1] gives digital marketers a way to offer creative, compelling, and unique visual experiences that are based in relevant data for their customers. The Movable Ink Platform provides valuable customization options that can easily be inserted into your campaigns. 

Expand Braze's creative capabilites by leveraging Intellegent Creative features like polling, countdown timer, and scratch off with Movable Ink. Movable Ink and Braze power a more well rounded approach to dynamic data driven messages, providing users with real-time elements about the things that matter.

## Integration

### Integration Requirements

- This integration supports iOS and Android applications.
- Your app will need Braze's SDK and Movable Ink's SDK.
- You must have an active Movable Ink account.

Intelligent Creative has many offerings that Braze users can take advantage of. Below is a list of what is supported. 

| Movable Ink Capability || Rich Push Notification | In-App Messaging / Content Cards | Details |
| ---------------------- || ---------------------- | -------------------------------- | ------- |
| Creative Optimizer | Display A/B Contents | no | ✔ | |
|| Optimize | no | ✔* | *Must Use Branch's Deeplinking solution |
| Targeting Rules | Date | ✔* | ✔ | *Supported but not recommended because push notifications are cached upon receipt and do not refresh |
|| Day of Week | ✔* | ✔ | *Supported but not recommended because push notifications are cached upon receipt and do not refresh |
|| Time of Day | ✔* | ✔ | *Supported but not recommended because push notifications are cached upon receipt and do not refresh |
| Stories/Behavior Activity | | ✔* | ✔* | *The unique user identifier used for Braze must be linked to your ESP’s identifier |
| Deep-Linking within the app | | ✔* | ✔* | *Must use Branch’s deep linking solution |
| Apps | Countdown Timer | ✔* | ✔ | *Supported but not recommended because push notifications are cached upon receipt and do not refresh |
|| Polling | no | ✔* | *After voting, will leave the app to be a mobile landing page |
|| Scratch Off | ✔* | ✔* | *On click, will leave the app for the Scratch off experience |
|| Video | ✔* | ✔* | *Animated GIFs only |

### Out-of the Box Integration 

1. Set up Content in Movable Ink Dashboard.
2. From the Movable Ink Dashboard, Finish & Export your content.
3. On the Finish page, copy the sourse URL(`img src`) from the creative tag.
4. In the Braze Platform, paste the URL in the appropriate field. Check out [Customization][] to see appropriate fields. 

## Customization

### Push Notifications

1. In the Braze Platform, paste the URL in the __Push Icon Image__ and __Expanded Notification Image__ fields.
2. In order to make sure images are not cached, prepend the URL with empty Liquid tags: {% if true %}{% endif %}

### In-App and Content Card Messages

1. In Braze’s platform, paste the URL in the __Rich Notification Media__ field.
2. __Provide a Unique URL to help Prevent Caching.__ To ensure that Movable Ink’s real-time images work and will not be affected by caching, use Liquid to append a timestamp to the URL. <br><br> To do this, use the following syntax, replacing the image URL as needed:<br>{% raw %} ```{% assign timestamp = "now" | date: "%s" %}``` <br> ```{% assign img = "https://yapji3pc.mi-msg.com/p/rp/822cdb1956883563.gif?" |  append:timestamp %} {{img}}``` {% endraw %} <br>This template will take the current time (in seconds), append it to the end of the Movable Ink image tab (as a query param), and then output the final result. You can preview it's working with the "Test" tab on the right of the Compose tab - this will evaluate the code and show a preview.
3. __Re-Evalate Segment Membership__. Enable this option located on the "Target Users" step of a campaign. This option will tell the mobile SDKs re-request the campaign each time an In App Message is triggered. It's needed because ordinarily the Liquid code is evaluated just once at send-time, and we need a unique URL every time the message is shown.

## Use Cases

## Trouble Shooting

[1]: https://movableink.com/
