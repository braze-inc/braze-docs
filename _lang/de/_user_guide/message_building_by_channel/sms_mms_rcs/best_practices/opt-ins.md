---
nav_title: "Sammeln von Opt-Ins für Nutzer:innen"
article_title: "Best Practices für das Sammeln von SMS-Opt-Ins von Nutzer:innen"
page_order: 7
description: "Dieser Referenzartikel behandelt drei bewährte Verfahren zum Sammeln von Opt-Ins für Nutzer:innen."
page_type: reference
channel:
  - SMS
  
---

# Sammeln von Opt-Ins für Nutzer:innen

> Der folgende Artikel listet einige gängige SMS-Opt-In-Methoden auf.

## Option 1: Bitten Sie die Nutzer:innen, eine SMS an Ihren Kurz- oder Langcode zu senden

Bitten Sie die Nutzer:innen, eine SMS mit „START", „UNSTOP", „YES" oder einem angepassten Opt-in-Schlüsselwort an Ihre Nummer zu senden, um sie automatisch zu Ihrer Abo-Gruppe hinzuzufügen. Auf Ihrer Website, in Ihrer mobilen App oder sogar in Ihrer Werbung können Sie die Nutzer:innen dazu auffordern, um ein Opt-in durchzuführen – bei Bedarf können Sie auch einen Anreiz dafür bieten.

## Option 2: Nutzer:innen melden sich per In-App-Nachricht an

Um Nutzer:innen die Möglichkeit zu geben, sich über eine In-App-Nachricht für SMS anzumelden, verwenden Sie das von Braze bereitgestellte [Formular zur Erfassung von Telefonnummern]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/), mit dem Sie ein gebrandetes Formular erstellen können, um Telefonnummern zu sammeln und Ihre SMS-Liste zu erweitern.

![Nachrichten-Editor für In-App-Nachrichten mit einem Template zur Erfassung von Telefonnummern.]({% image_buster /assets/img_archive/dnd_iam_phone_capture_select.png %}){: style="max-width:80%;"}

Braze empfiehlt, dass Sie auch das [SMS-Double-Opt-In-Feature]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) verwenden. Dieses Feature arbeitet automatisch mit dem In-App-Formular zur Erfassung von Telefonnummern zusammen und fordert die Nutzer:innen auf, ihre Absicht zu bestätigen, nachdem sie ihre Telefonnummer über das Formular übermittelt haben.

## Option 3: Registrierungs-Flow

Wenn sich neue Nutzer:innen auf der Website oder in der App anmelden oder registrieren, fragen Sie nach Telefonnummer und E-Mail-Adresse. Fügen Sie ein Kontrollkästchen ein, um Werbe-E-Mails und SMS zu erhalten. 

Nachdem sich die Nutzer:innen registriert haben, gehen Sie wie folgt vor:

1. Verwenden Sie den [`/subscription/status/set`-Endpunkt]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/#update-users-subscription-group-status), um die Nutzer:innen zu erstellen und ihre Attribute zu speichern.

```http
POST 'https://rest.iad-03.braze.com/subscription/status/set' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "subscription_group_id": "xyz-abcd-1234567",
  "subscription_state": "subscribed",
  "external_id": "external_identifier",
  "phone": "+12223334444",
  "use_double_opt_in_logic": true
}
'
```

{: start="2"}
2. Verwenden Sie den [`/users/track`-Endpunkt]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), um die Nutzer:innen für SMS zu abonnieren.

```
curl --location --request POST 'https://rest.iad-01.braze.com/users/track' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR_REST_API_KEY' \
--data-raw '{
  "attributes": [
    {
      "external_id": "external_identifier",
      "phone": "+12223334444",
      "subscription_groups": [
        {
          "subscription_group_id": "xyz-abcd-1234567",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}'
```

{% alert tip %}
Um Nutzer:innen beim Abonnieren über die REST API in den [SMS-Double-Opt-In]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/)-Workflow aufzunehmen, setzen Sie den Parameter `use_double_opt_in_logic` in Ihrer Anfrage auf `true`. Wenn Sie diesen Parameter weglassen, werden die Nutzer:innen abonniert, ohne eine Double-Opt-In-Bestätigung zu erhalten.

Dieser Parameter wird von den folgenden Endpunkten unterstützt:<br><br>
- [`/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/)
- [`/v2/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/)
- [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
{% endalert %}