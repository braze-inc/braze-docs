---
nav_title: Präferenzen für Benachrichtigungen
article_title: Präferenzen für Benachrichtigungen
page_order: 1
page_type: reference
description: "Dieser Referenzartikel behandelt Ihre verfügbaren Optionen zur Überwachung von Messaging und Aktivitäten in Ihrem Unternehmenskonto."

---

# Präferenzen für Benachrichtigungen

> Wenn Sie das Messaging und die Aktivitäten in Ihrem Unternehmenskonto überwachen möchten, können Sie bestimmte Benachrichtigungen einrichten und festlegen, wohin diese gesendet werden sollen.

Auf der Seite **Benachrichtigungseinstellungen** können Sie konfigurieren, wer (wenn überhaupt) Benachrichtigungen über Ihr Unternehmen erhält. Sie können festlegen, wer Benachrichtigungen über die Zustellung von Kampagnen oder technische Fehler erhalten soll. Außerdem können Sie Empfänger:innen für den wöchentlichen Analytics-Bericht angeben. Für die meisten Benachrichtigungen unterstützt Braze E-Mail- und Webhook-Kanäle.

![Seite "Benachrichtigungseinstellungen" im Braze-Dashboard]({% image_buster /assets/img_archive/notification_preferences.png %})

Um auf diese Seite zuzugreifen, gehen Sie zu **Einstellungen** > **Admin-Einstellungen** > **Benachrichtigungseinstellungen**.

{% alert tip %}
Sie können auch eine Integration mit Slack einrichten, um Benachrichtigungen zu erhalten. Weitere Informationen finden Sie unter [Nachrichten über eingehende Webhooks senden](https://api.slack.com/incoming-webhooks).
{% endalert %}

## Verfügbare Benachrichtigungen

Die folgende Tabelle beschreibt die verfügbaren Benachrichtigungen und die Kanäle, über die sie zugestellt werden.

{% alert note %}
Wenn Sie den Standardwert **Empfänger:innen** von **Alle Dashboard-Nutzer:innen** löschen und ihn wieder hinzufügen möchten, können Sie ihn manuell in das Dropdown-Feld eingeben.
{% endalert %}

| Benachrichtigung | Beschreibung | Verfügbare Benachrichtigungskanäle |
|--------------|-------------|-----------------|
| API-Nutzungswarnungen | Wenn Sie diese Option auswählen, gelangen Sie zum **API-Nutzungs-Dashboard**, wo Sie dann zum Tab [**API-Nutzungswarnungen**]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_alerts/) navigieren und Warnungen einrichten können, um wichtige API-Anfragevolumen zu überwachen. | E-Mail, Webhook |
| AWS-Zugangsdaten-Fehler | Benachrichtigt Empfänger:innen, wenn Braze bei der Verwendung Ihrer Amazon Web Services-Zugangsdaten für einen Datenexport einen Fehler erhält. Dies umfasst auch Zugangsdaten-Fehler-Benachrichtigungen für Google Cloud Dienste und Azure (Microsoft Cloud Dienste). | E-Mail, Webhook |
| Kampagne automatisch angehalten | Benachrichtigt Empfänger:innen, wenn Braze eine Kampagne angehalten hat. | E-Mail |
| Canvas automatisch angehalten | Benachrichtigt Empfänger:innen, wenn Braze ein Canvas angehalten hat. | E-Mail |
| Ablauf der Kampagnen-Interaktionsdaten | Benachrichtigt Empfänger:innen über alle Kampagnen, deren Interaktionsdaten ablaufen, sowie über alle Informationen zu Segmenten, Kampagnen oder Canvasen, die in einem Retargeting-Filter darauf referenzieren und in den letzten 30 Tagen zum Senden einer Nachricht verwendet wurden. | E-Mail |
| Kampagne/Canvas aktualisiert | Benachrichtigt Empfänger:innen, wenn eine aktive Kampagne oder ein aktives Canvas aktualisiert oder deaktiviert wird, sowie wenn eine inaktive Kampagne oder ein inaktives Canvas reaktiviert wird oder Entwürfe gestartet werden. | E-Mail |
| Kampagne/Canvas-Volumengrenze erreicht | Benachrichtigt Empfänger:innen, wenn eine Kampagne oder ein Canvas seine Volumengrenze erreicht. | E-Mail | 
| Ablauf der Canvas-Interaktionsdaten | Benachrichtigt Empfänger:innen über alle Canvase, deren Interaktionsdaten ablaufen, sowie über alle Informationen zu Segmenten, Kampagnen oder Canvasen, die in einem Retargeting-Filter darauf referenzieren und in den letzten 30 Tagen zum Senden einer Nachricht verwendet wurden. | E-Mail |
| Kommentare in Canvasen | Benachrichtigt Empfänger:innen, wenn ein Canvas neue Kommentare enthält. | E-Mail |
| Connected-Content-Fehler | Benachrichtigt Empfänger:innen, wenn ein Connected-Content-Endpunkt Fehler aufweist. | E-Mail |
| Push-Fehler | Benachrichtigt Empfänger:innen, wenn ein Push-Endpunkt Fehler aufweist. | E-Mail, Webhook |
| Limit geplanter Kampagne erreicht | Benachrichtigt Empfänger:innen, wenn das Limit für eine wiederkehrende geplante Kampagne erreicht wurde. | E-Mail, Webhook |
| Versand geplanter Kampagne abgeschlossen | Benachrichtigt Empfänger:innen, wenn der Versand einer geplanten Kampagne abgeschlossen ist. | E-Mail, Webhook |
| Webhook-Fehler | Benachrichtigt Empfänger:innen, wenn ein Webhook-Endpunkt Fehler aufweist. | E-Mail |
| Analytics-Wochenbericht | Sendet jeden Montag eine Zusammenfassung der Workspace-Aktivitäten der vergangenen Woche an die Empfänger:innen. Empfänger:innen erhalten für jeden Workspace, dem sie angehören, eine Zusammenfassung. | E-Mail |
| Tägliche Canvas-/Kampagnen-Eingangs-Volumenlimits | Sendet jedes Mal eine Benachrichtigung, wenn ein Sendelimit erreicht wird. | E-Mail |
| Agents Console-Fehler | Benachrichtigt Empfänger:innen, wenn ein [Agents Console-Agent]({{site.baseurl}}/user_guide/brazeai/agents) sein Ausführungslimit mit der aktuellen Funktionalität erreicht hat. | E-Mail |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
[Gesperrte Nutzer:innen]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/#suspending-company-users) können weiterhin Benachrichtigungen von Braze erhalten.
{% endalert %}

## Wöchentlicher Analytics-Bericht

Braze sendet optional jeden Montag um 5 Uhr EST einen wöchentlichen Bericht per E-Mail an die von Ihnen benannten Personen in Ihrem Unternehmen. Sie können die angepassten Events, die in den Wochenbericht aufgenommen werden sollen, unter **Dateneinstellungen** > **Angepasste Events** auswählen.

Sie können bis zu fünf Events auswählen, die in Ihren Wochenbericht aufgenommen werden sollen:

![Events auswählen, die in den Analytics-Bericht aufgenommen werden sollen]({% image_buster /assets/img_archive/company_analytics_report_new.png %})