---
nav_title: Kampagnen-Benachrichtigungen
article_title: Kampagnen-Benachrichtigungen
page_order: 6

page_type: reference
description: "Dieser Referenzartikel gibt Ihnen einen Überblick über Kampagnenwarnungen, ihre Vorteile und wie Sie sie einrichten können, damit Sie sich keine Sorgen machen müssen."
tool: Campaigns
channel:
- email
- webhooks

---

# Kampagnen-Benachrichtigungen

> Wir möchten Sie darauf aufmerksam machen, wenn etwas nicht ganz so ist, wie Sie es erwarten, und Ihnen die Gewissheit geben, dass das Schiff reibungslos fährt. Kampagnenschwellenwarnungen geben Ihnen Sicherheit - Sie erfahren als Erster, wenn eine wichtige Kampagne mehr oder weniger Nachrichten sendet als Sie erwarten.

Kampagnenwarnungen sind für die folgenden Kampagnen verfügbar:

- Wiederkehrende geplante Kampagnen
- Aktionsbasierte Kampagnen
- Per API getriggerte Kampagnen

## Einrichten Ihres Kampagnenalarms

Navigieren Sie zur Analytics-Seite Ihrer Kampagne, um mit der Einrichtung Ihrer Benachrichtigung zu beginnen. Wenn Sie **Alarm einrichten** wählen, können Sie obere und untere Alarmschwellen sowie die Alarmempfänger und -kanäle festlegen.

\![Dialogfenster Kampagnenüberwachung mit zwei Buttons: Abbrechen und Speichern.]({% image_buster /assets/img_archive/campaign_alerts.png %})

Für eine geplante wiederkehrende Kampagne können Sie obere und untere Schwellenwerte für die Nachrichten festlegen, die bei jedem Versand der Kampagne gesendet werden. Für eine ausgelöste Kampagne können Sie obere und untere Schwellenwerte für die Anzahl der stündlich und täglich versendeten Nachrichten festlegen.

Sie können eine E-Mail-Benachrichtigung, eine Webhook-Benachrichtigung oder beides einrichten. Webhook-Benachrichtigungen können sehr nützlich sein, da Sie damit eine Benachrichtigung an einen Slack-Kanal senden können. Weitere Informationen zur Integration von Kampagnen-Benachrichtigungen in Slack finden Sie in unserer [Dokumentation]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/company-wide_settings_management/#slack-incoming-webhook-integration).

{% alert note %}
Wenn Sie Kampagnenwarnungen für zukünftige Kampagnen einstellen, können Sie Aktualisierungen vor Beginn und nach Ende der Kampagne erhalten. Dies liegt daran, dass Kampagnenwarnungen so lange gesendet werden, bis die Kampagne manuell gestoppt wird.
{% endalert %}

## Webhook-Nutzdaten für Kampagnenalarm

Nachfolgend finden Sie Beispielnutzdaten für den Body eines Webhooks für Kampagnen-Benachrichtigungen. Dieses Beispiel verwendet einen Alarm, der so konfiguriert ist, dass er gesendet wird, wenn die Anzahl der gesendeten Nachrichten für eine bestimmte Kampagne unter 500 fällt.

```
{"text":"Your campaign 'Sample campaign' had fewer than 500 messages sent this run. It had 4 messages sent this run. See https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"data":{"url":"https://dashboard-01.braze.com/engagement/campaigns/5b44b00ffbe76a7024f242e6/51804f26dd365acfa700026a?page=-2",
"app_group_name":"Sample workspace",
"campaign_name":"Sample campaign",
"campaign_api_id":"fe787bc5-d13f-4123-b22f-3bd48f9fc407","upper_threshold":0,"lower_threshold":500,"value":4}}
```

