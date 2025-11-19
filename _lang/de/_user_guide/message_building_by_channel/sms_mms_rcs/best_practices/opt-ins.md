---
nav_title: "Sammeln von Opt-Ins für Nutzer:innen"
article_title: "Best Practices für das Sammeln von Opt-Ins für Nutzer:innen"
page_order: 7
description: "Dieser Referenzartikel behandelt drei bewährte Verfahren zum Sammeln von Benutzer-Opt-Ins."
page_type: reference
channel:
  - SMS
  
---

# Sammeln von Opt-Ins für Nutzer:innen

> Der folgende Artikel listet einige gängige SMS-Opt-In-Methoden auf.

## Option 1: Bitten Sie die Nutzer:innen, Ihren Kurz- oder Langcode zu senden

Bitten Sie die Nutzer:innen, eine SMS mit „START“, „UNSTOP“, „YES“ oder einem angepassten Opt-in-Schlüsselwort an Ihre Nummer zu senden, um sie automatisch zu Ihrer Abonnementgruppe hinzuzufügen. Auf Ihrer Website, in Ihrer mobilen App oder sogar in Ihrer Werbung können Sie die Nutzer:innen auffordern, dies zu tun, um sich anzumelden, und Sie können einen Anreiz bieten, wenn es hilfreich ist.

## Option 2: Nutzer:innen melden sich per In-App-Nachricht an

Um Nutzern die Möglichkeit zu geben, sich in einer In-App-Nachricht für SMS zu entscheiden, verwenden Sie das von Braze bereitgestellte [Formular zur Erfassung von Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/), mit dem Sie Telefonnummern sammeln und Ihre SMS-Liste erweitern können.

![In-App-Nachricht-Editor mit einem Template für die Erfassung von Telefonnummern.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze empfiehlt, dass Sie auch die [SMS-Double-Opt-In-Funktion]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) verwenden. Diese Funktion arbeitet automatisch mit dem In-App-Formular zur Erfassung von Telefonnummern zusammen und fordert die Nutzer:innen auf, ihre Absicht zu bestätigen, nachdem sie ihre Telefonnummer über das Formular übermittelt haben.

## Option 3: Registrierungs-Flow

Wenn sich ein neuer Benutzer auf der Website oder in der App anmeldet oder registriert, fragen Sie ihn nach seiner Telefonnummer und E-Mail. Fügen Sie ein Kontrollkästchen ein, um Werbe-E-Mails und SMS zu erhalten. 

Nachdem sich der oder die Nutzer:in angemeldet hat, gehen Sie wie folgt vor:

1. Verwenden Sie den [Endpunkt`/subscription/status/set` ]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status), um den oder die Nutzer:in zu erstellen und seine oder ihre Attribute zu speichern.

```json
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444"
}
'
```

{: start="2"}
2\. Verwenden Sie den [Endpunkt`/users/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), um die SMS-Anmeldung des Nutzers oder der Nutzerin zu bestätigen.

```json
POST `https://rest.aid-03.braze.com/users/track` \
--header `Content-Type: application/json` \
--header `Authorization: Bearer YOUR-REST-API-KEY` \
--data-raw `{
"attributes" : [
Unknown macro: { "external_id" }
]
}
```

