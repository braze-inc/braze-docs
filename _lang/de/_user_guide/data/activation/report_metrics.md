---
nav_title: Glossar der Metriken für Berichte
article_title: Glossar zu den Berichtsmetriken
layout: report_metrics
page_order: 0.5
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar definiert Begriffe, die Sie in Ihren Berichten in Ihrem Braze-Konto finden."
tool: Reports
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### AMP-Klicks

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### AMP-Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### Zielgruppe

{% apitags %}
Alle
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Berechnung: (Anzahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)</span>

{% endapi %}

{% api %}

### Absprünge

{% apitags %}
E-Mail, Web-Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Dies könnte daran liegen, dass kein gültiges Push-Token vorhanden ist, die Nutzer:innen sich nach dem Start der Kampagne abgemeldet haben oder die E-Mail-Adresse fehlerhaft oder deaktiviert ist.

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|E-Mail|Ein E-Mail-Bounce für Kund:innen, die SendGrid verwenden, besteht aus Hard Bounces, Spam (`spam_report_drops`) und E-Mails, die an ungültige Adressen gesendet wurden (`invalid_emails`).<br><br>Bei E-Mails ist *Bounce %* oder *Absprungrate* der prozentuale Anteil der Nachrichten, die von den verwendeten Diensten erfolglos versendet oder als „zurückgeschickt" oder „nicht erhalten" bezeichnet wurden oder von den vorgesehenen E-Mail-Nutzer:innen nicht empfangen wurden.|
|Push|Diese Nutzer:innen wurden automatisch von allen zukünftigen Push-Benachrichtigungen abgemeldet.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Bounces</i>: Anzahl</li>
        <li><i>Bounce %</i> oder <i>Absprungrate %</i>: (Bounces) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Text-Klick

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Click' %}

<span class="calculation-line">Berechnung: (Text-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Klicks auf Text

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} Weitere Einzelheiten finden Sie in den Changelogs des SDK für [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) und [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Berechnung: (Text-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Klicks auf Button 1

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} Das Reporting für _Button-1-Klicks_ funktioniert nur, wenn Sie in der In-App-Nachricht den **Bezeichner für Reporting** mit „0" angeben.

<span class="calculation-line">Berechnung: (Button-1-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Klicks auf Button 2

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} Das Reporting für _Button-2-Klicks_ funktioniert nur, wenn Sie in der In-App-Nachricht den **Bezeichner für Reporting** mit „1" angeben.

<span class="calculation-line">Berechnung: (Button-2-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Kampagnen-Analytics

{% apitags %}
Feature-Flags
{% endapitags %}

Die Performance der Nachricht über verschiedene Kanäle. Die angezeigten Metriken hängen vom ausgewählten Messaging-Kanal ab und davon, ob das [Feature-Flag-Experiment]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/experiments/#campaign-analytics) ein multivariater Test ist.

{% endapi %}

{% api %}

### Eingereichte Auswahlen

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### Effektive Klickrate

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Berechnung: (Eindeutige Klicks) / (Eindeutige Öffnungen) (für E-Mail)</span>

{% endapi %}

{% api %}

### RCS Bestätigte Zustellungen oder SMS Bestätigte Zustellungen

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Als Kund:in von Braze werden die Zustellungen auf Ihr SMS-Kontingent angerechnet. 

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Bestätigte Zustellungen</i>: Anzahl</li>
        <li><i>Bestätigte Zustellungsrate</i>: (Bestätigte Zustellungen) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Konfidenz

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Button auf Bestätigungsseite

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### Ausblendungen der Bestätigungsseite

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### Konversionen (B, C, D)

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Dieses definierte Event wird von Ihnen bei der Erstellung der Kampagne festgelegt. 

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|E-Mail, Push, Webhooks|Konversionen werden nach dem ersten Versand getrackt.|
|Content-Cards|Konversionen werden gezählt, wenn die Nutzer:innen eine Content-Card zum ersten Mal ansehen.|
|In-App-Nachrichten|Eine Konversion wird gezählt, wenn die Nutzer:innen die In-App-Nachricht-Kampagne erhalten und angesehen haben und anschließend das spezifische Konversions-Event innerhalb des definierten Konversionsfensters ausführen – unabhängig davon, ob auf die Nachricht geklickt wurde oder nicht.<br><br>Konversionen werden der zuletzt empfangenen Nachricht zugeordnet. Wenn die Wiederzulassung aktiviert ist, wird die Konversion der zuletzt eingegangenen In-App-Nachricht zugeordnet, sofern sie innerhalb des definierten Konversionsfensters erfolgt. Wenn der In-App-Nachricht jedoch bereits eine Konversion zugewiesen wurde, kann die neue Konversion für diese spezielle Nachricht nicht protokolliert werden. Das bedeutet, dass jede Zustellung einer In-App-Nachricht mit nur einer Konversion verbunden ist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Konversionen gesamt

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Wenn ein:e Nutzer:in eine In-App-Nachricht-Kampagne nur einmal anschaut, wird nur eine Konversion gezählt, auch wenn das Konversions-Event später mehrfach durchgeführt wird. Wenn jedoch die Wiederzulassung aktiviert ist und die Nutzer:innen die In-App-Nachricht-Kampagne mehrfach sehen, kann die *Gesamtkonversion* für jede Impression, die für eine neue Instanz der In-App-Nachricht-Kampagne protokolliert wird, einmal steigen. 

Wenn ein:e Nutzer:in zum Beispiel zweimal eine In-App-Nachricht triggert und nach jeder Impression konvertiert (was zu zwei Konversionen führt), erhöht sich die *Gesamtzahl der Konversionen* um zwei. Wenn es jedoch nur eine Impression einer In-App-Nachricht gab, auf die zwei Konversions-Events folgten, wird nur eine Konversion protokolliert, und die *Gesamtzahl der Konversionen* erhöht sich um eins.

{% endapi %}

{% api %}

### Nachricht schließen

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Close Message' %}

{% endapi %}

{% api %}

### Konversionsrate

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Rate' %}

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|In-App-Nachrichten|Die Metrik der gesamten täglichen <i>eindeutigen Impressionen</i> wird zur Berechnung der <i>Konversionsrate</i> für In-App-Nachrichten verwendet.<br><br>Impressionen für In-App-Nachrichten können nur einmal pro Tag gezählt werden. Andererseits kann die Anzahl der Male, die Nutzer:innen eine gewünschte Aktion (eine „Konversion") durchführen, innerhalb eines Zeitraums von 24 Stunden steigen. Während Konversionen mehrmals am Tag stattfinden können, ist dies bei Impressionen nicht möglich. Wenn also Nutzer:innen innerhalb eines Tages mehrmals eine Konversion abschließen, kann die <i>Konversionsrate</i> entsprechend steigen, aber die Impressionen werden nur einmal gezählt.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b>In-App-Nachrichten</b>: (Primäre Konversionen) / (Eindeutige Impressionen)</li>
        <li><b>Andere Kanäle</b>: (Primäre Konversionen) / (Eindeutige Empfänger:innen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Konversionsfenster

{% apitags %}
Alle
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### Zustellungen

{% apitags %}
E-Mail, Web-Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %}

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|E-Mail|Bezieht sich auf die Gesamtzahl der Nachrichten (Sends), die erfolgreich an E-Mail-Adressen gesendet und von diesen empfangen wurden.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Zustellungen</i>: Anzahl</li>
        <li><i>Zustellungen %</i>: (Sendungen – Bounces) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### RCS-Zustellungsfehler oder SMS-Zustellungsfehler

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Kontaktieren Sie den <a href="/docs/braze_support/">Braze Support</a>, um die Gründe für die fehlgeschlagene Zustellung zu erfahren.

<span class="calculation-line">Berechnung: (Sendungen) – (Sendungen an Netzbetreiber)</span>

{% endapi %}

{% api %}

### Zustellfehler

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Kontaktieren Sie den <a href="/docs/braze_support/">Braze Support</a>, um die Gründe für die fehlgeschlagene Zustellung zu erfahren.

<span class="calculation-line">Berechnung: (Sendungen) – (Sendungen an Netzbetreiber)</span>

{% endapi %}

{% api %}

### Zustellfehlerrate

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Kontaktieren Sie den <a href="/docs/braze_support/">Braze Support</a>, um die Gründe für die fehlgeschlagene Zustellung zu erfahren.

<span class="calculation-line">Berechnung: (Zustellungsfehler) / (Sendungen)</span>

{% endapi %}

{% api %}

### Direkte Öffnungen

{% apitags %}
iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Berechnung: (Direkte Öffnungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

### Per E-Mail erreichbar

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Fehler

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Fehler sind in der Anzahl der <i>Sendungen</i> enthalten, aber nicht in der Anzahl der <i>eindeutigen Empfänger:innen</i>.

{% endapi %}

{% api %}

### Geschätzte reale Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### Misserfolge

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failures' %} Misserfolge werden in der Anzahl der <i>Sendungen</i>, aber nicht in der Anzahl der <i>Zustellungen</i> berücksichtigt.</td>

<span class="calculation-line">Berechnung (<i>Misserfolgsrate</i>): (Misserfolge) / (Sendungen)</span>

{% endapi %}

{% api %}

### Feature-Flag-Experiment-Performance

{% apitags %}
Feature-Flags
{% endapitags %}

Performance-Metriken für die Nachricht in einem Feature-Flag-Experiment. Die angezeigten Metriken variieren je nach Messaging-Kanal und je nachdem, ob es sich bei dem Experiment um einen multivariaten Test handelt oder nicht.

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

In diesem Fall markiert Braze die E-Mail-Adresse als ungültig, aktualisiert aber nicht den [Abo-Status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) der Nutzer:innen. Wenn eine E-Mail einen Hard Bounce erhält, werden alle zukünftigen Anfragen an diese E-Mail-Adresse gestoppt.

{% endapi %}

{% api %}

### Hilfe

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} Eine Antwort der Nutzer:innen wird immer dann gemessen, wenn diese innerhalb von vier Stunden nach Erhalt Ihrer Nachricht eine eingehende Nachricht senden.

{% endapi %}

{% api %}

### Beeinflusste Öffnungen

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Berechnung: (Beeinflusste Öffnungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

### Lifetime-Umsatz

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Lifetime-Value je Nutzer:in

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Durchschnittlicher Tagesumsatz

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Tägliche Käufe

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Täglicher Umsatz pro Nutzer:in

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### Automatische Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Diese Metrik wird ab dem 11\. November 2021 für SendGrid und ab dem 2\. Dezember 2021 für SparkPost getrackt. Bei Amazon SES werden die Analytics als _Öffnungen_ angezeigt. Bot-Filter für Klicks werden jedoch unterstützt.

{% endapi %}

{% api %}

### Öffnungen

{% apitags %}
Web-Push, iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Opt-out

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} Eine Antwort der Nutzer:innen wird immer dann gemessen, wenn diese innerhalb von vier Stunden nach Erhalt Ihrer Nachricht eine eingehende Nachricht senden.

{% endapi %}

{% api %}

### Sonstige Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Beachten Sie, dass Nutzer:innen eine E-Mail auch öffnen können (sodass die Öffnung zu den sonstigen Öffnungen zählt), bevor die Anzahl der automatischen Öffnungen protokolliert wird. Wenn Nutzer:innen eine E-Mail einmal (oder öfter) nach einem automatischen Öffnungsereignis aus einem Posteingang, der nicht zu Apple Mail gehört, öffnen, dann wird die Anzahl der Öffnungen in die Kategorie „Sonstige Öffnungen" und nur einmal in die Kategorie „Eindeutige Öffnungen" eingerechnet.

{% endapi %}

{% api %}

### Ausstehender Wiederholungsversuch

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### Primäre Konversionen (A) oder primäres Konversions-Event

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|Kanal|Zusätzliche Informationen|
|-------------|----------------------|
|E-Mail, Push, Webhooks|Nach dem ersten Senden.|
|Content-Cards, In-App-Nachrichten|Wenn die Nutzer:innen die Content-Card oder Nachricht zum ersten Mal sehen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Primäre Konversionen (A) oder primäres Konversions-Event</i>: Anzahl</li>
        <li><i>Primäre Konversionen (A) %</i> oder <i>Primäre Konversions-Event-Rate</i>: (Primäre Konversionen) / (Eindeutige Empfänger:innen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Gelesen

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### Leserate

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Read Rate' %}

<span class="calculation-line">Berechnung: (Gelesen mit Lesebestätigungen) / (Sendungen)</span>

{% endapi %}

{% api %}

### Erhalten

{% apitags %}
E-Mail, Content-Cards, In-App-Nachricht, Web-Push, iOS Push, Android Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|Kanal|Zusätzliche Informationen|
|-------|-------|
|Content-Cards|Wird empfangen, wenn Nutzer:innen die Karte in der App ansehen.|
|Push|Wird empfangen, wenn Nachrichten vom Braze-Server an den Push-Anbieter gesendet werden.|
|E-Mail|Wird empfangen, wenn Nachrichten vom Braze-Server an den E-Mail-Anbieter gesendet werden.|
|SMS/MMS|„Zugestellt", nachdem der SMS-Anbieter eine Bestätigung vom vorgelagerten Netzbetreiber und dem Zielgerät erhalten hat.|
|In-App-Nachricht|Wird zum Zeitpunkt der Anzeige auf Grundlage der definierten Trigger-Aktion empfangen.|
|WhatsApp|Wird zum Zeitpunkt der Anzeige auf Grundlage der definierten Trigger-Aktion empfangen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### RCS-Ablehnungen oder SMS-Ablehnungen

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Rejections' %} Als Kund:in von Braze werden Ablehnungen auf Ihr SMS-Kontingent angerechnet.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Ablehnungen</i>: Anzahl</li>
        <li><i>Ablehnungsrate</i>: (Ablehnungen) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Umsatz

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### Gesendet

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sent' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Sendungen

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Diese Metrik wird von Braze bereitgestellt. Beachten Sie, dass beim Starten einer geplanten Kampagne diese Metrik alle gesendeten Nachrichten berücksichtigt, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden.

{% alert tip %}
Bei Content-Cards wird diese Metrik unterschiedlich berechnet, je nachdem, was Sie für die [Kartenerstellung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) ausgewählt haben:

- **Beim Start oder beim Einstieg in den Schritt:** Die Anzahl der erstellten und sichtbaren Karten. Dabei wird nicht berücksichtigt, ob die Nutzer:innen die Karte angesehen haben.
- **Bei der ersten Impression:** Die Anzahl der Karten, die den Nutzer:innen angezeigt werden.
{% endalert %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Nachrichten gesendet

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Diese Metrik wird von Braze bereitgestellt. Beachten Sie, dass beim Starten einer geplanten Kampagne diese Metrik alle gesendeten Nachrichten berücksichtigt, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden.

{% alert tip %}
Bei Content-Cards wird diese Metrik unterschiedlich berechnet, je nachdem, was Sie für die [Kartenerstellung]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) ausgewählt haben:

- **Beim Start oder beim Einstieg in den Schritt:** Die Anzahl der erstellten und sichtbaren Karten. Dabei wird nicht berücksichtigt, ob die Nutzer:innen die Karte angesehen haben.
- **Bei der ersten Impression:** Die Anzahl der Karten, die den Nutzer:innen angezeigt werden.
{% endalert %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Sendungen an Netzbetreiber

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Sendungen an Netzbetreiber</i>: Anzahl</li>
        <li><i>Sendungen an Netzbetreiber Rate</i>: (Sendungen an Netzbetreiber) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Beachten Sie, dass sich _Soft Bounces_ von _Deferrals_ unterscheiden. Wenn während dieses Zeitraums keine E-Mail erfolgreich zugestellt wurde, sendet Braze ein Soft-Bounce-Ereignis pro versuchtem Kampagnenversand. Vor dem 25\. Februar 2025 wurden diese Wiederholungsversuche als mehrere Soft Bounces für einen Kampagnenversand gezählt.

Soft Bounces werden zwar nicht in den Analytics Ihrer Kampagne getrackt, aber Sie können die Soft Bounces im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) überwachen. Sie können diese Nutzer:innen auch von der Versendung ausschließen oder sich die Anzahl der Soft Bounces der letzten 30 Tage mit dem [Segmentfilter „Soft Bounced"]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced) ansehen. Im Nachrichten-Aktivitätsprotokoll können Sie auch den Grund für die Soft Bounces sehen und mögliche Diskrepanzen zwischen den „Sendungen" und „Zustellungen" Ihrer E-Mail-Kampagnen nachvollziehen.

{% endapi %}

{% api %}

### Spam

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
Spam-Beschwerden werden direkt von den E-Mail-Anbietern bearbeitet und dann über eine Feedbackschleife an Braze weitergeleitet. Die meisten Feedbackschleifen melden nur einen Teil der tatsächlichen Beschwerden, sodass die _Spam_-Metrik oft nur einen Bruchteil der tatsächlichen Gesamtzahl darstellt. Nur E-Mail-Anbieter können das tatsächliche Volumen von Spam-Beschwerden einsehen, was bedeutet, dass _Spam_ als indikative und nicht als erschöpfende Metrik betrachtet werden sollte.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Spam</i>: Anzahl</li>
        <li><i>Spam %</i> oder <i>Spam-Rate %</i>: (Als Spam markiert) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Ausblendungen der Umfrageseite

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Umfrage-Einreichungen

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### Klicks gesamt

{% apitags %}
E-Mail, Content-Cards, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Clicks' %}

|Kanal|Zusätzliche Informationen|
|-------|-------|
|LINE|Tracking erfolgt, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde. AMP-E-Mails enthalten Klicks, die sowohl in der HTML- als auch in der Klartextversion aufgezeichnet werden. Diese Zahl kann durch Anti-Spam-Tools künstlich erhöht werden.|
|Banner|Die Gesamtzahl (und der Prozentsatz) der Nutzer:innen, die innerhalb der zugestellten Nachricht geklickt haben, unabhängig davon, ob dieselben Nutzer:innen mehrfach geklickt haben.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b>E-Mail:</b> (Klicks insgesamt) / (Zustellungen)</li>
        <li><b>Content-Cards:</b> (Klicks insgesamt) / (Impressionen insgesamt)</li>
        <li><b>SMS:</b> (Klick-Öffnungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Ausblendungen gesamt

{% apitags %}
Content-Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Wenn Nutzer:innen zwei verschiedene Karten aus derselben Kampagne erhalten und beide ausblenden, erhöht sich die Anzahl um zwei. Die Wiederzulassung erlaubt es Ihnen, die _Gesamtzahl der Ausblendungen_ jedes Mal zu erhöhen, wenn Nutzer:innen eine Karte erhalten; jede Karte ist eine andere Nachricht.

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Ausblendungen gesamt:</i> Anzahl</li>
        <li><i>Ausblendungsrate gesamt:</i> Ausblendungen gesamt / Impressionen insgesamt</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Impressionen gesamt

{% apitags %}
In-App-Nachricht, Content-Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Diese Zahl ist die Summe der Impressions-Events, die Braze von den SDKs erhält.

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|Content-Cards|Die Gesamtzahl der protokollierten Impressionen für eine bestimmte Content-Card. Dieser Wert kann für dieselben Nutzer:innen mehrfach erhöht werden.|
|In-App-Nachrichten|Wenn es mehrere Geräte gibt und die Wiederzulassung deaktiviert ist, sollten die Nutzer:innen die In-App-Nachricht nur einmal sehen. Selbst wenn mehrere Geräte verwendet werden, wird die Nachricht nur auf dem ersten Gerät angezeigt, auf das das Targeting ausgerichtet ist. Dies setzt voraus, dass das Profil über konsolidierte Geräte verfügt und Nutzer:innen eine Nutzer-ID haben, mit der sie geräteübergreifend angemeldet sind. Wenn die Wiederzulassung aktiviert ist, wird jedes Mal, wenn die Nutzer:innen die In-App-Nachricht sehen, eine Impression protokolliert.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Öffnungen gesamt

{% apitags %}
E-Mail, iOS Push, Android Push, Web-Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|LINE|Tracking erfolgt, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde.|
|AMP-E-Mails|Die Gesamtöffnungen für die HTML- und die Klartextversion.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><b>E-Mail <i>Öffnungen insgesamt</i>:</b> Anzahl</li>
        <li><b>E-Mail <i>Öffnungsrate insgesamt</i>:</b> (Öffnungen) / (Zustellungen)</li>
        <li><b>Web-Push <i>Öffnungen insgesamt</i>:</b> Anzahl <i>Direkte Öffnungen</i></li>
        <li><b>Web-Push <i>Öffnungsrate insgesamt</i>:</b> (Öffnungen insgesamt) / (Zustellungen)</li>
        <li><b>iOS, Android und Kindle Push <i>Öffnungen insgesamt</i>:</b> (Direkte Öffnungen) + (Beeinflusste Öffnungen)</li>
        <li><b>iOS, Android und Kindle Push <i>Öffnungsrate insgesamt</i>:</b> (Öffnungen insgesamt) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Umsatz gesamt

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Diese Metrik ist nur in Kampagnenvergleichsberichten über den <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Berichts-Builder</a> verfügbar.

{% endapi %}

{% api %}

### Eindeutige Klicks

{% apitags %}
E-Mail, Content-Cards, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Dazu gehören auch Klicks auf die von Braze bereitgestellten Abmeldelinks.

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|E-Mail|Tracking über einen Zeitraum von sieben Tagen.|
|LINE|Tracking erfolgt, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Eindeutige Klicks</i>: Anzahl</li>
        <li><b>Content-Cards</b> <i>Eindeutige Klicks %</i> oder <i>Eindeutige Klickrate</i>: (Eindeutige Klicks) / (Eindeutige Impressionen)</li>
        <li><b>E-Mail</b> <i>Eindeutige Klicks %</i> oder <i>Eindeutige Klickrate</i>: (Eindeutige Klicks) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Eindeutige Ausblendungen

{% apitags %}
Content-Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Berechnung: (Eindeutige Ausblendungen) / (Eindeutige Impressionen)</span>

{% endapi %}

{% api %}

### Eindeutige Impressionen

{% apitags %}
In-App-Nachricht, Content-Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|In-App-Nachrichten|Eindeutige Impressionen können nach 24 Stunden erneut hochgezählt werden, wenn die Wiederzulassung aktiviert ist und Nutzer:innen die Trigger-Aktion ausführen. Wenn die Wiederzulassung eingeschaltet ist, gilt: <i>Eindeutige Impressionen</i> = <i>Eindeutige Empfänger:innen</i>.|
|Content-Cards|Die Anzahl sollte sich nicht erhöhen, wenn Nutzer:innen eine Karte zum zweiten Mal ansehen.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Eindeutige Öffnungen

{% apitags %}
E-Mail, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %}

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|E-Mail|Tracking über einen Zeitraum von 7 Tagen.|
|LINE|Tracking erfolgt, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Eindeutige Öffnungen</i>: Anzahl</li>
        <li><i>Eindeutige Öffnungen %</i> oder <i>Eindeutige Öffnungsrate</i>: (Eindeutige Öffnungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Eindeutige Empfänger:innen

{% apitags %}
Alle
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %}

Da Betrachter:innen jeden Tag als eindeutige Empfänger:innen gezählt werden können, sollten Sie erwarten, dass dieser Wert höher ist als die <i>eindeutigen Impressionen</i>. Bei Content-Cards kann jede Content-Card nur einmal empfangen werden. Wenn Sie also dieselbe Content-Card ein zweites Mal ansehen, egal an welchem Tag, wird dieser Wert nicht erhöht.<br><br>Diese Zahl wird von Braze bereitgestellt und basiert auf der `user_id`. Eindeutige Empfänger:innen werden auf der Ebene der Kampagne oder des Canvas-Schrittes gezählt, nicht auf der Ebene des <a href='https://braze.com/docs/api/identifier_types/#send-identifier'>Sende-Bezeichners</a>.

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}

{% api %}

### Abgemeldete Personen oder Abmeldung

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Berechnung:
    <ul>
        <li><i>Abgemeldete Personen</i> oder <i>Abmeldung</i>: Anzahl</li>
        <li><i>Abgemeldete Personen %</i> oder <i>Abmelderate</i>: (Abmeldungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Abmeldungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Berechnung: (Abmeldungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

### Variante

{% apitags %}
Content-Cards, E-Mail, In-App-Nachricht, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Berechnung: Anzahl</span>

{% endapi %}