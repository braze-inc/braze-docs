---
nav_title: "Bot-Klick-Filterung"
article_title: "SMS und RCS Bot Klick-Filterung"
description: "Dieser referenzierte Artikel behandelt die Filterung von SMS- und RCS-Bot-Klicks."
alias: /sms_rcs_bot_click_filtering/
page_type: reference
page_order: 11
channel:
  - SMS
  - RCS
---

# SMS- und RCS-Bot-Klick-Filterung

> Das Filtern von SMS- und RCS-Bot-Klicks verbessert die Analytics von Kampagnen und Workflows, indem es verdächtige Bot-Klicks ausschließt. Ein "Bot-Klick" bezieht sich auf automatisierte Klicks auf verkürzte Links in SMS- und RCS-Nachrichten, z. B. von Web-Crawlern, Android- und iOS-Linkvorschauen oder CPaaS-Sicherheitssoftware. Dieses Feature erleichtert die genaue Berichterstattung, Segmentierung und Orchestrierung, um echte Nutzer:innen zu engagieren. <br><br> Informationen zum Filtern von Klicks in E-Mail Kampagnen finden Sie unter [Bot-Filterung für E-Mails]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/bot_filtering/).

## Funktionsweise

Braze verfügt über ein proprietäres Erkennungssystem, das mehrere Eingaben verwendet, um mutmaßliche Bot-Klicks zu identifizieren, die auch als nicht-menschliche Interaktionen (NHI) bezeichnet werden. Bot-Klicks können die Klickraten in die Höhe treiben und die Engagement-Raten verzerren. Durch das Filtern dieser Daten erleichtert Braze die Erfassung von zuverlässigen Daten für die Entscheidungsfindung.

Unser System analysiert Nutzer:innen, die mit Webcrawlern, Android- und iOS-Linkvorschauen oder CPaaS-Sicherheitssoftware verbunden sind. Ein paar Beispiele für gefilterte Nutzer:innen sind `GoogleBot`, `python-requests/2.32.3` und `Barracuda Sentinel (EE)`.

## Betroffene Metriken und Arbeitsabläufe

Die folgenden Metriken und Arbeitsabläufe von Braze sind von Bot-Klicks betroffen:

- **_Klicks insgesamt_:** Kampagnen-Analysen und Canvas-Analysen schließen Bot-Klicks aus und zeigen nur menschliche Interaktionen an.
- **Filter für die Segmentierung:** Segmente, die sich auf SMS-Link-Interaktionen beziehen, schließen Bot-Klicks für ein genaueres Retargeting in Kampagnen und Canvase aus.
- **Orchestrierung:** Bot-Klicks werden aus aktionsbasierten Triggern und Canvas-Aktions-Pfaden gefiltert, die auf SMS-Link-Interaktionen referenzieren, so dass die Trigger das menschliche Verhalten widerspiegeln dürfen.
- **Braze Intelligence:**
    - **Intelligente Auswahl:** Schließt Bot-Klicks bei der Optimierung der Auswahl von Varianten aus.
    - **Intelligenter Kanal:** Schließt Bot-Klicks aus, wenn SMS oder RCS für eine genaue Auswahl des Kanals ausgewählt ist.
    - **Schritte des Experiments:** Schließt Klicks von Bots aus, um zuverlässige Ergebnisse zu erhalten.
    - **Currents Datenexporte:** Enthält die Felder `is_suspected_bot_click` und `suspected_bot_click_reason` zur Analyse der Klicks von Menschen und Bots. Diese Felder sind in [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/), [Snowflake Data Sharing]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/) und [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/) verfügbar.

Abmeldungen aufgrund von mutmaßlichen Bot-Klicks sind davon nicht betroffen. Braze bearbeitet alle Anfragen zur Abmeldung wie gewohnt. Um diese Abmeldungen zu blockieren, [senden Sie uns ein Produkt-Feedback]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Currents Felder in SMS Klick-Ereignissen

Braze enthält die folgenden Currents-Felder für SMS-Klick-Ereignisse:

| Feld | Datentyp | Beschreibung |
| --- | --- | --- |
| `is_suspected_bot_click` | Boolesch | Zeigt an, ob der Klick ein mutmaßlicher Bot-Klick ist. Gibt `null` für alle Nutzer:innen zurück, bis die Filterung von Bot-Klicks für Ihr Unternehmen Enablement ist. Wenn es aktiviert ist, wird es für alle neuen Klicks mit `true` oder `false` gefüllt. |
| `suspected_bot_click_reason` | String, Array | Zeigt den Grund für einen mutmaßlichen Bot-Klick an (z. B. `user_agent`). Wird auch dann angezeigt, wenn der Filter deaktiviert ist, und bietet Insights zu potenziellen Bot-Aktivitäten. Dieses Feld ist global verfügbar und wird für alle Nutzer:innen mit einem Grund ausgefüllt, auch wenn die Filterung von Bot-Klicks noch nicht aktiviert ist. So erhalten Sie Insights über potenzielle Bot-Aktivitäten, bevor Sie die Filterung von Bot-Klicks aktivieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Query Builder Template

Für die Analyse Ihrer Daten können Sie das vorgefertigte mobile Template **SMS-Klick-Ereignisse durch Bots** im [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder/query_templates/) verwenden.

## Häufig gestellte Fragen

### Wie wirkt sich das Filtern von Bot-Klicks auf die Performance von Kampagnen aus?

Das Filtern wirkt sich nicht auf zuvor gesendete Kampagnen aus. Wenn es aktiviert ist, reduziert es die Klickraten von diesem Moment an, indem es Bot-Klicks ausschließt.

### Verhindert der Filter für Bot-Klicks, dass Bots auf Abmeldelinks klicken?

Nein. Alle Anfragen zur Abmeldung werden wie üblich bearbeitet.

### Sind Link-Vorschauen in die Filter für Bot-Klicks einbezogen?

Ja Link-Vorschauen (z.B. Android- und iOS-Link-Vorschauen) werden als Bot-Klicks gekennzeichnet und herausgefiltert.

### Wie aktiviere ich das Filtern von Bot-Klicks?

Sie müssen sich mit Ihrem Braze-Konto Team in Verbindung setzen, um das Filtern von Bot-Klicks während des frühen Zugangs zu aktivieren. Sobald der Bot-Klick-Filter allgemein verfügbar ist, wird das Feature standardmäßig für alle Nutzer:innen von SMS und RCS aktiviert sein.

Stellen Sie außerdem sicher, dass Sie das vorgebrachte Tracking von Klicks für die [Linkverkürzung]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) aktiviert haben. Dies erlaubt es Ihnen, die Bot Click Analytics zu erhalten, da wir diese Daten auf der Ebene des einzelnen Nutzers:innen tracken. 

{% alert note %}
Für weitere Hilfe [wenden Sie sich bitte an den Support]({{site.baseurl}}/braze_support/).
{% endalert %}