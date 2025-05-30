---
nav_title: Präferenzen für Benachrichtigungen
article_title: Präferenzen für Benachrichtigungen
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt Ihre verfügbaren Optionen zur Überwachung von Nachrichten und Aktivitäten in Ihrem Unternehmenskonto."

---

# Präferenzen für Benachrichtigungen

> Wenn Sie die Nachrichten und Aktivitäten in Ihrem Unternehmenskonto überwachen möchten, können Sie bestimmte Benachrichtigungen einrichten und auswählen, wohin diese gehen sollen.

Auf der Seite **Benachrichtigungseinstellungen** können Sie festlegen, wer (wenn überhaupt) Benachrichtigungen über Ihr Unternehmen erhält. Sie können festlegen, wer Benachrichtigungen über die Zustellung von Kampagnen oder technische Fehler erhalten soll. Sie können auch Empfänger für den wöchentlichen Analysebericht angeben. Für die meisten Benachrichtigungen unterstützt Braze E-Mail- und Webhook-Kanäle.

![Seite "Benachrichtigungseinstellungen" im Braze Dashboard][61]

Um auf diese Seite zuzugreifen, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Benachrichtigungseinstellungen**.

## Verfügbare Benachrichtigungen

In der folgenden Tabelle sind die verfügbaren Benachrichtigungen aufgeführt:

| Benachrichtigung | Beschreibung | Verfügbare Benachrichtigungskanäle |
|--------------|-------------|-----------------|
| AWS-Zugangsdaten fehlerhaft | Benachrichtigt die Empfänger:innen, wenn Braze bei der Verwendung Ihrer Amazon Web Services-Zugangsdaten für einen Datenexport einen Fehler erhält. Dazu gehören auch Benachrichtigungen über Zugangsdaten-Fehler für Google Cloud Serviceleistungen; Dienste und Azure (Microsoft Cloud Serviceleistungen; Dienste). | E-Mail, Webhook |
| Kampagne automatisch angehalten | Benachrichtigt die Empfänger:innen, wenn Braze eine Kampagne angehalten hat. | E-Mail |
| Ablauf der Kampagnen-Interaktion | Benachrichtigt die Empfänger über alle Kampagnen, deren Interaktionsdaten ablaufen, sowie über alle Informationen zu Segmenten, Kampagnen oder Canvases, die in einem Retargeting-Filter darauf verweisen und in den letzten 30 Tagen zum Senden einer Nachricht verwendet wurden. | E-Mail |
| Kampagne/Canvas aktualisiert | Benachrichtigt Empfänger:in, wenn eine aktive Kampagne oder ein Canvas aktualisiert oder deaktiviert wird, sowie wenn eine inaktive Kampagne oder ein Canvas reaktiviert wird oder Entwürfe gestartet werden. | E-Mail |
| Kampagne/Canvas Volumengrenze erreicht | Benachrichtigt Empfänger:in, wenn eine Kampagne oder ein Canvas seine Volumengrenze erreicht. | E-Mail | 
| Ablauf der Canvas-Interaktion | Benachrichtigt Empfänger über alle Canvas, deren Interaktionsdaten ablaufen, sowie über alle Informationen zu Segmenten, Kampagnen oder Canvases, die in einem Retargeting-Filter darauf verweisen und in den letzten 30 Tagen zum Senden einer Nachricht verwendet wurden. | E-Mail |
| News Feed Karte Veröffentlicht/Live | Benachrichtigt die Empfänger, wenn News Feed-Karten geplant oder veröffentlicht werden. | E-Mail, Webhook |
| Fehler bei Push-Zugangsdaten | Benachrichtigt Empfänger, wenn die Push-Anmeldeinformationen einer App ungültig sind und wenn die Push-Anmeldeinformationen einer App bald ablaufen. | E-Mail, Webhook |
| Geplante Kampagne gesendet/nicht gesendet | Benachrichtigt Empfänger:innen, wenn geplante Kampagnen mit dem Versand beginnen oder wenn geplante Kampagnen versuchen, etwas zu versenden, aber keine berechtigten Nutzer:innen zum Versenden vorhanden sind. | E-Mail, Webhook |
| Limit von geplanter Kampagne erreicht | Benachrichtigt die Empfänger:innen, wenn das Limit für eine wiederkehrende geplante Kampagne erreicht wurde. | E-Mail, Webhook |
| Versand von geplanter Kampagne beendet | Benachrichtigt die Empfänger:innen, wenn der Versand einer geplanten Kampagne beendet ist. | E-Mail, Webhook |
| Analytics-Wochenbericht | Sendet jeden Montag eine Zusammenfassung der Arbeitsbereichsaktivitäten der vergangenen Woche an die Empfänger. Empfänger:innen erhalten für jeden Workspace, dem sie angehören, eine Zusammenfassung. | E-Mail |
| Tägliches Canvas/Kampagneneingang Volumenlimits | Sendet jedes Mal eine Benachrichtigung, wenn ein Sendelimit erreicht wird. | E-Mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Wöchentliche analytische Berichte

Braze sendet optional jeden Montag um 5 Uhr EST einen wöchentlichen Bericht per E-Mail an die von Ihnen benannten Personen in Ihrem Unternehmen. Sie können die benutzerdefinierten Ereignisse, die in den Wochenbericht aufgenommen werden sollen, unter **Dateneinstellungen** > **Benutzerdefinierte Ereignisse** auswählen.

Sie können bis zu fünf Events auswählen, die in Ihren Wochenbericht aufgenommen werden sollen:

![Events auswählen, die in den Analysebericht aufgenommen werden sollen][22]

## Integration von Slacks eingehendem Webhook

Slack verfügt über eine [eingehende Webhook-App][67], mit der Nachrichten aus externen Quellen in Slack gepostet werden können. Um loszulegen, öffnen Sie die App für eingehende Webhooks.

1. Wählen Sie den Slack-Kanal aus, an den die Benachrichtigungen gehen sollen, und klicken Sie auf **Eingehende Webhooks-Integration hinzufügen**.<br><br>
    ![Integration eingehender Webhooks in Slack hinzufügen][63]<br><br>
  Slack generiert eine URL, die Sie in Braze für die Benachrichtigungen eingeben müssen, die Sie erhalten möchten.<br><br>
2. Kopieren Sie die **Webhook-URL**.<br><br>
    ![Webhook-URL kopieren][64]<br><br>
3. Navigieren Sie zur Registerkarte **Benachrichtigungseinstellungen** in den **Unternehmenseinstellungen**.<br><br>
4. Wählen Sie die Benachrichtigung aus, die Sie für Slack aktivieren möchten. Wenn Sie mehrere Benachrichtigungen haben, die Sie an diesen Slack-Kanal senden möchten, können Sie den Webhook mithilfe von **Masseneintrag** zu mehreren Benachrichtigungen hinzufügen.<br><br>
    ![Wählen Sie die zu aktivierenden Slack-Benachrichtigungen aus][65]{: style="max-width:60%;"}<br><br>
5. Geben Sie die URL ein, die Slack für Sie generiert hat.

Das war's! Sie sollten ab sofort Benachrichtigungen über Ihr Unternehmen in diesem Slack-Kanal erhalten. Sie können auch den Hilfeartikel von Slack zu diesem Thema lesen: [Senden von Nachrichten über eingehende Webhooks][62].

[22]: {% image_buster /assets/img_archive/company_analytics_report_new.png %}
[63]: {% image_buster /assets/img_archive/slack_f.png %}
[64]: {% image_buster /assets/img_archive/copy_url.png %}
[65]: {% image_buster /assets/img_archive/click_edit_f.png %}
[67]: https://my.slack.com/services/new/incoming-webhook/
[61]: {% image_buster /assets/img_archive/notification_preferences.png %}
[62]: https://api.slack.com/incoming-webhooks
