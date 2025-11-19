---
nav_title: Kanal Performance Dashboard
article_title: Kanal Performance Dashboard
page_order: 2
page_type: reference
description: "Dieser referenzierte Artikel befasst sich mit dem Channel Performance Dashboard, mit dem Sie die Performance-Metriken für ganze Kanäle sowohl für Kampagnen als auch für Canvase anzeigen können."
tool: 
  - Reports

---

# Dashboard für die Performance des Kanals

> Das Dashboard für die Kanal-Performance zeigt die aggregierten Metriken für einen gesamten Kanal, sowohl für Kampagnen als auch für Canvase. Diese Dashboards sind derzeit für E-Mail und SMS verfügbar.

Das Dashboard für die E-Mail Performance zeigt das Engagement des E-Mail Kanals in den letzten dreißig Tagen an.]({% image_buster /assets/img_archive/email_performance_dashboard_1.png %})

Sie können die folgenden Dashboards einsehen:
- [E-Mail Performance Dashboard](#email-performance-dashboard)
- [E-Mail Insights Dashboard](#email-insights-dashboard)
- [SMS Performance Dashboard](#sms-performance-dashboard)

## E-Mail Performance Dashboard

Sehen Sie sich Ihr E-Mail Performance Dashboard an, indem Sie zu **Analytics** > **E-Mail Performance** gehen und den Datumsbereich für den Zeitraum auswählen, für den Sie Daten anzeigen möchten. Ihr Datumsbereich kann bis zu einem Jahr in die Vergangenheit reichen.

### Wie die Metriken berechnet werden

![Eine beispielhafte E-Mail Kampagne mit 335.630 Sendungen, mit einem Durchschnitt von 11.187,667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Die Berechnungen für die verschiedenen Metriken im Dashboard für die E-Mail-Performance entsprechen denen auf der Ebene der einzelnen Nachrichten (z.B. Analytics für Kampagnen). Auf diesem Dashboard werden die Metriken über alle Kampagnen und Canvase für den von Ihnen ausgewählten Datumsbereich aggregiert. Um mehr über diese Definitionen zu erfahren, referenzieren Sie auf [E-Mail Metriken]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-metrics).

Jede Kachel zeigt zuerst die Metrik für die Rate an, gefolgt von der Zählung (mit Ausnahme von *Sends*, wo die Zählung gefolgt von der durchschnittlichen Anzahl pro Tag angezeigt wird). Die Kachel Eindeutige Klicks enthält beispielsweise die *Eindeutige Klickrate* aus dem von Ihnen ausgewählten Zeitraum und die Gesamtzahl der eindeutigen Klicks aus diesem Zeitraum. Jede Kachel zeigt auch den [Vergleich zur letzten Periode](#comparing-time-periods).

| Metrisch | Typ | Berechnung |
| --- | --- | ---- |
| Sendungen | Anzahl | Gesamtzahl der Sendungen für jeden Tag im Datumsbereich |
| Zustellrate | Rate | (Gesamtzahl der Zustellungen an jedem Tag des Datumsbereichs) / (Gesamtzahl der Sendungen an jedem Tag des Datumsbereichs) |
| Absprungrate | Rate | (Gesamtzahl der Bounces an jedem Tag im Datumsbereich) / (Gesamtzahl der Sendungen an jedem Tag im Datumsbereich) |
| Abmeldungsrate | Rate | (Gesamtzahl der eindeutigen Abmeldungen für jeden Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich)<br><br>Dies verwendet eindeutige Abmeldungen, die auch in Campaign Analytics, Übersicht und Berichts-Builder verwendet werden. Diese Abmeldungen werden über alle Quellen hinweg protokolliert (z. B. SDK, REST API, CSV-Importe, E-Mails und Abmeldungen von Listen). Die Abmelderaten in Campaign und Canvas Analytics sind Abmeldungen, die auf einen Klick auf eine zugestellte E-Mail zurückzuführen sind.  |
| Eindeutige Öffnungsrate | Rate | (Gesamtzahl der eindeutigen Öffnungen an jedem Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich) |
| Andere Öffnungsrate | Rate | (Gesamtzahl der sonstigen Öffnungen an jedem Tag im Datumsbereich) / (Gesamtzahl der Zustellungen im Datumsbereich)<br><br>Andere Öffnungen umfassen E-Mails, die nicht als maschinell geöffnet identifiziert wurden, z.B. wenn ein Nutzer:innen eine E-Mail öffnet. Diese Metrik ist nicht eindeutig und ist eine Untermetrik der gesamten Öffnungen.  |
| Eindeutige Klickrate | Rate | (Gesamtzahl der eindeutigen Klicks an jedem Tag im Datumsbereich) / (Gesamtzahl der Zustellungen für einen Datumsbereich) |
| Eindeutige Klick-zu-Öffnung-Rate | Rate | (Gesamtzahl der eindeutigen Klicks an jedem Tag im Datumsbereich) / (Gesamtzahl der eindeutigen Öffnungen an jedem Tag im Datumsbereich) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## E-Mail Insights Dashboard 

Das E-Mail Insights Dashboard verfolgt, wo und wann Ihre Kunden mit Ihren E-Mails interagieren. Diese Berichte können umfangreiche und detaillierte Daten darüber liefern, wie Sie Ihre E-Mails optimieren können, um ein größeres Engagement zu erreichen. Das E-Mail Insights Dashboard enthält die Daten der letzten sechs Monate. Um auf das Dashboard zuzugreifen, gehen Sie zu **Analytics** > **E-Mail Performance** > E-Mail Insights.

### Engagement nach Gerät

Der Bericht **Engagement nach Gerät** bietet eine Aufschlüsselung, mit welchen Geräten Ihre Nutzer:innen auf Ihre E-Mails zugreifen. Diese Daten verfolgen das Engagement bei E-Mails über Mobil-, Desktop-, Tablet- und andere Geräte. Diese Daten basieren auf dem User Agent String, der von den Geräten Ihrer Nutzer:innen übermittelt wird.

{% alert note %}
Wenn Sie CloudFront als CDN verwenden, stellen Sie sicher, dass der Nutzer:innen-Agent an den ESP weitergeleitet wird. Andernfalls wird jeder Nutzer:in "Amazon Cloudfront" sein.
{% endalert %}

Die Kategorie "Andere" umfasst jeden Nutzer:in String, der nicht als Desktop, Handy oder Tablet identifiziert werden kann. Zum Beispiel Fernsehen, Auto, Videospielkonsole, OTT (Over-the-Top oder Streaming) und ähnliches. Dies kann auch null oder leere Werte umfassen.

Um besser zu verstehen, was sich in dieser Kategorie "Andere" befindet, können Sie die Nutzer:innen mit einer der beiden folgenden Optionen extrahieren:

1. [Currents]({{site.baseurl}}/user_guide/data/braze_currents) sendet Ihnen den genauen Nutzer:innen String, der von den Geräten Ihrer Nutzer:innen abgerufen wurde.
2. Nutzen Sie unseren [Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder) zur Verwendung von SQL oder unseren [KI Query Builder]({{site.baseurl}}/user_guide/analytics/query_builder#generating-sql-with-the-ai-query-builder) zur Anzeige der Nutzer:innen.

![Engagement nach Gerät Bericht, der die Anzahl der Klicks für Handy, Desktop, Tablet und andere Geräte anzeigt. Die meisten Klicks erfolgen auf mobilen Geräten.]({% image_buster /assets/img/engagement_by_device_type.png %}){: style="max-width:70%;"}

Für die Öffnung von E-Mails trennt Braze Google Image Proxy, Apple Image Proxy und Yahoo Mail Proxy. Diese Dienste zwischenspeichern und laden alle eingebetteten Bilder in einer E-Mail, bevor sie dem Empfänger:in zugestellt wird. Infolgedessen wird eine E-Mail von den Servern des Postfachanbieters und nicht vom Server des Empfängers aus getriggert, was zu überhöhten Öffnungen von E-Mails führen kann. Diese Dienste dienen dazu, den Datenschutz, die Sicherheit, die Performance und die Effizienz beim Laden von Bildern zu verbessern. Dies kann auch echte Öffnungen von Empfängern enthalten, da diese Serviceleistungen; Dienste den Nutzer:innen maskieren und wir die Daten anhand des Nutzer:innen kategorisieren.

![Engagement nach Gerät Bericht, der die Anzahl der Klicks für Mobile, Desktop, Tablet, Apple Privacy Proxy, Google Image Proxy, Yahoo Mail Proxy und Andere anzeigt. Die meisten Öffnungen finden auf mobilen Geräten statt.]({% image_buster /assets/img/engagement_by_device_type_proxy.png %}){: style="max-width:70%;"}

### Engagement nach Mailbox-Anbieter

Der Bericht **Engagement nach Postfachanbieter** zeigt die wichtigsten Postfachanbieter an, die zu Ihren Klicks oder Öffnungen beitragen. Sie können auf bestimmte Premier Mailbox-Anbieter klicken, um bestimmte empfangende Domains aufzuschlüsseln. Wenn zum Beispiel Microsoft in diesem Bericht als eine Ihrer wichtigsten Metriken für den Mailbox-Anbieter aufgeführt ist, können Sie weitere Details für die empfangenden Domains einsehen, wie z.B. "outlook.com", "hotmail.com", "live.com" und mehr.

![Ein Beispiel für ein Engagement nach Mailbox-Anbieter mit Google, Apple iCloud, Yahoo, Microsoft und Mail.Ru Group und der entsprechenden Anzahl von Klicks.]({% image_buster /assets/img_archive/mailbox_provider_time_engagement.png %}){: style="max-width:70%;"}

### Engagement-Zeitpunkt

Der Bericht **"Zeitpunkt des Engagements** " zeigt Daten darüber an, wann Nutzer:innen auf Ihre E-Mails zugreifen. Dies kann Ihnen helfen, Fragen zu beantworten, z. B. an welchem Wochentag oder zu welcher Uhrzeit das Engagement Ihrer Kund:in am höchsten ist. Mit diesen Insights können Sie mit dem besten Tag oder der besten Uhrzeit für den Versand Ihrer Nachrichten experimentieren, um ein höheres Engagement zu erzielen. Beachten Sie, dass sich diese Zeiten nach der Zeitzone Ihres Unternehmens richten.

Der Engagement-Bericht für **den Wochentag** schlüsselt die Öffnungen oder Klicks nach Wochentag auf. 

![Ein Beispiel für einen Engagement-Bericht für den Tag der Woche mit den meisten Klicks am Montag und Mittwoch.]({% image_buster /assets/img_archive/time_engagement.png %})

Der Bericht über das Engagement **zur Tageszeit** schlüsselt die Öffnungen oder Klicks nach jeder Stunde in einem 24-Stunden-Zeitfenster auf.

![Ein Beispiel für einen Engagement-Bericht zur Tageszeit mit den Öffnungen oder Klicks von 12 Uhr bis 23 Uhr.]({% image_buster /assets/img_archive/time_engagement_day.png %})

Weitere Informationen zu Analytics für Ihre E-Mails finden Sie unter [E-Mail-Berichterstattung]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/).

## SMS Performance Dashboard

Um Ihr SMS Performance Dashboard zu nutzen, gehen Sie zu **Analytics** > **SMS Performance** und wählen Sie den Datumsbereich für den Zeitraum aus, für den Sie Daten anzeigen möchten. Ihr Datumsbereich kann bis zu einem Jahr in die Vergangenheit reichen.

### Wie die Metriken berechnet werden

![Eine beispielhafte SMS Kampagne mit 335.630 Sendungen, mit einem Durchschnitt von 11.187.667 pro Tag.]({% image_buster /assets/img_archive/email_performance_dashboard_2.png %}){: style="max-width:40%;float:right;margin-left:15px;border:none;"}

Die Berechnungen für die verschiedenen Metriken im SMS Performance Dashboard sind die gleichen wie auf der Ebene der einzelnen Nachrichten (z.B. Analytics für Kampagnen). Auf diesem Dashboard werden die Metriken über alle Kampagnen und Canvase für den von Ihnen ausgewählten Datumsbereich aggregiert. Um mehr über diese Definitionen zu erfahren, referenzieren Sie auf [SMS Metriken]({{site.baseurl}}/sms_mms_rcs_reporting/).

Jede Kachel zeigt zuerst die Metrik für die Rate an, gefolgt von der Zählung (mit Ausnahme von _Sends_, wo die Zählung gefolgt von der durchschnittlichen Anzahl pro Tag angezeigt wird). Jede Kachel zeigt auch den [Vergleich zur letzten Periode](#comparison-to-last-period-change-in-totals-or-rates).

| Metrisch | Typ | Berechnung |
| --- | --- | ---- |
| Sendungen | Anzahl | Gesamtzahl der Sendungen für jeden Tag im Datumsbereich |
| Rate der bestätigten Zustellungen | Rate | (Gesamtzahl der Zustellungen an jedem Tag des Datumsbereichs) / (Gesamtzahl der Sendungen an jedem Tag des Datumsbereichs) |
| Rate der Zustellungsausfälle | Rate | (Gesamtzahl der Ausfälle für jeden Tag im Datumsbereich) / (Gesamtzahl der Sendungen für jeden Tag im Datumsbereich) |
| Ablehnungsquote | Rate | (Gesamtzahl der Ablehnungen an jedem Tag des Datumsbereichs) / (Gesamtzahl der Sendungen an jedem Tag des Datumsbereichs) |
| Klickrate | Rate | (Gesamtzahl der Klicks an jedem Tag im Datumsbereich) / (Gesamtzahl der Zustellungen an jedem Tag im Datumsbereich) |
| Opt-ins insgesamt | Rate | Gesamtzahl der eingehenden Nachrichten Opt-Ins für jeden Tag im Datumsbereich |
| Opt-outs insgesamt | Rate | Gesamtzahl der Opt-outs für eingehende Nachrichten für jeden Tag im Datumsbereich |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Dashboard Filter

Sie können die Daten auf Ihrem Dashboard mit Hilfe der folgenden Filteroptionen filtern:

- **Tag:** Wählen Sie einen Tag. Wenn Sie diese Option anwenden, zeigt Ihr Dashboard Metriken nur für den ausgewählten Tag an.
- **Canvas:** Wählen Sie bis zu 10 Canvase. Wenn Sie diese Option anwenden, zeigt Ihr Dashboard nur die Metriken für die ausgewählten Canvase an. Wenn Sie zuerst einen Tag-Filter auswählen, werden in Ihren Optionen für Canvas-Filter nur Canvase angezeigt, die den ausgewählten Tag aufweisen.
- **Kampagne:** Wählen Sie bis zu 10 Kampagnen. Wenn Sie diese Option anwenden, zeigt Ihr Dashboard nur die Metriken für die ausgewählten Kampagnen an. Wenn Sie zuerst einen Tag-Filter auswählen, werden in Ihren Optionen für Kampagnenfilter nur Kampagnen angezeigt, die den von Ihnen ausgewählten Tag aufweisen.

![Filteroptionen auf dem Channel Performance Dashboard, wo Sie einen Tag und eine Liste von Canvase auswählen können, nach denen Sie filtern möchten.]({% image_buster /assets/img_archive/dashboard_filters.png %})

## Vergleich der Zeiträume

Das Dashboard für die Performance des Kanals vergleicht automatisch den Zeitraum, den Sie im Datumsbereich ausgewählt haben, mit dem vorherigen Zeitraum, der die gleiche Anzahl von Tagen umfasst. Wenn Sie zum Beispiel "Letzte 7 Tage" als Datumsbereich im Dashboard wählen, werden beim Vergleich mit dem letzten Zeitraum die Metriken der letzten sieben Tage mit denen der sieben Tage davor verglichen. Wenn Sie einen angepassten Datumsbereich auswählen - sagen wir 10\. Mai bis 15\. Mai, also Daten aus sechs Tagen - vergleicht das Dashboard die Metriken aus diesen Tagen mit den Metriken vom 4\. bis 9\. Mai.

Der Vergleich ist die prozentuale Veränderung zwischen der letzten und der aktuellen Periode, die berechnet wird, indem die Differenz zwischen den beiden Perioden durch die Metrik der letzten Periode geteilt wird.

### Anzeigen von Änderungen der Gesamtzahlen und -raten

Sie können zwischen der Option **Änderung der Gesamtzahlen anzeigen - die**die Gesamtzahlen (z. B. die Anzahl der zugestellten E-Mails) zwischen den beiden Zeiträumen vergleicht - und der Option **Änderung der Raten anzeigen - die**die Raten (z. B. die Zustellungsrate) vergleicht - wechseln.

![Radio-Buttons zum Umschalten zwischen der Anzeige von Änderungen in den Summen oder Änderungen in den Raten für das Channel Performance Dashboard.]({% image_buster /assets/img_archive/email_performance_dashboard_3.png %}){: style="max-width:60%"}

## Häufig gestellte Fragen

### Warum werden auf meinem Dashboard leere Werte angezeigt?

Es gibt ein paar Szenarien, die zu leeren Werten für eine Metrik führen können:

- Braze aufgezeichnete Nullen für diese bestimmte Metrik in dem von Ihnen ausgewählten Datumsbereich.
- Sie haben im ausgewählten Datumsbereich keine Nachrichten gesendet.
- Es gab zwar Metriken wie Öffnungen, Klicks oder Abmeldungen für einen ausgewählten Datumsbereich, aber keine Zustellungen oder Versendungen. In diesem Fall berechnet Braze keine Metriken für den Preis.

Um mehr Metriken zu sehen, versuchen Sie, den Datumsbereich zu erweitern.

### Warum zeigt mein E-Mail Dashboard mehr andere Öffnungen als eindeutige Öffnungen an?

Für die Metrik _Eindeutige Öffnungen_ dedupliziert Braze alle wiederholten Öffnungen, die von einem bestimmten Nutzer:innen registriert werden (unabhängig davon, ob es sich um _maschinelle Öffnungen_ oder _andere Öffnungen_ handelt), so dass nur eine _eindeutige Öffnung_ gezählt wird, wenn ein Nutzer:innen mehrfach öffnet. Bei _anderen Öffnungen_ führt Braze keine Deduplizierung durch.

<!---Temporarily hidden until functionality is added

## Empty values in your data

#### If a metric displays "0%" or "0"

This means Braze recorded zero for that particular metric during the time frame you've selected.

#### If a metric displays "N/A"

This means that while Braze recorded positive counts for a particular metric for the time frame you've selected, the denominator for the rate calculation (either sends or deliveries in most cases) was zero. This can occur when emails are sent out on one day and opens and clicks are recorded the following days if your selected time frame does not include the date the messages were sent.

#### If a metric displays "--"

This means Braze hasn't recorded any data for that metric during the time you selected. If you haven't set up or sent any emails yet, learn more about how to do so in our dedicated [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email) section.

--->

