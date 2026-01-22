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

<span class="calculation-line">Kalkulation: (Anzahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)</span>

{% endapi %}

{% api %}

### Absprünge

{% apitags %}
E-Mail, Web-Push, iOS Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} Dies könnte daran liegen, dass es kein gültiges Push-Token gibt, der Nutzer:innen sich abgemeldet hat, nachdem die Kampagne gestartet wurde, oder die E-Mail Adresse ungenau oder deaktiviert ist.

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|E-Mail|Ein E-Mail-Bounce für Kund:innen, die SendGrid verwenden, besteht aus Hard Bounces, Spam (`spam_report_drops`) und E-Mails, die an ungültige Adressen gesendet wurden (`invalid_emails`).<br><br>Bei E-Mails ist *Bounce %* oder *Bounce Rate* der prozentuale Anteil der Nachrichten, die von den verwendeten Serviceleistungen; Diensten erfolglos versendet oder als "zurückgeschickt" oder "nicht erhalten" bezeichnet wurden oder von den vorgesehenen Nutzer:innen nicht empfangen wurden.|
|Push|Diese Nutzer:innen sind automatisch von allen zukünftigen Push-Benachrichtigungen abgemeldet worden.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><i>Bounces</i>: Anzahl</li>
        <li><i>Absprungrate %</i> oder <i>Absprungrate %</i>: (Bounces) / (Sendungen)</li>
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

<span class="calculation-line">Kalkulation: (Körper Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Klicks auf Text

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Body Clicks' %} Weitere Einzelheiten finden Sie in den Changelogs des SDK für [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) und [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Kalkulation: (Körper Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Klicks auf Button 1

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 1 Clicks' %} Reporting für _Button 1 Klicks_ funktioniert nur, wenn Sie in der In-App-Nachricht den **Bezeichner für Reporting** mit "0" angeben.

<span class="calculation-line">Kalkulation: (Button-1-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Klicks auf Button 2

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Button 2 Clicks' %} Reporting für _Button 2 Klicks_ funktioniert nur, wenn Sie in der In-App-Nachricht den **Bezeichner für Reporting** mit "1" angeben.

<span class="calculation-line">Kalkulation: (Button-2-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Kampagnen-Analysen

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

<span class="calculation-line">Kalkulation: (Eindeutige Klicks) / (Eindeutige Öffnungen) (für E-Mail)</span>

{% endapi %}

{% api %}

### RCS Bestätigte Zustellungen oder SMS Bestätigte Zustellungen

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confirmed Deliveries' %} Als Kund:in von Braze werden die Zustellungen auf Ihr SMS-Kontingent angerechnet. 

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><i>Bestätigte Zustellungen</i>: Anzahl</li>
        <li><i>Bestätigte Zustellungsrate</i>: (Bestätigte Zustellungen) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Vertrauen

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
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

{% multi_lang_include analytics/metrics.md metric='Conversions (B, C, D)' %} Dieses definierte Ereignis wird von Ihnen bei der Erstellung der Kampagne festgelegt. 

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|E-Mail, Push, Webhooks|Konversionen werden nach dem ersten Versand getrackt.|
|Content-Cards|Konversionen werden gezählt, wenn der Nutzer:innen eine Content-Card zum ersten Mal ansieht.|
|In-App-Nachrichten|Eine Konversion wird gezählt, wenn der Nutzer die In-App-Nachricht-Kampagne erhalten und angesehen hat und anschließend das spezifische Konversions-Event innerhalb des definierten Konversions-Fensters ausführt, unabhängig davon, ob er auf die Nachricht geklickt hat oder nicht.<br><br>Konversionen werden der zuletzt empfangenen Nachricht zugeordnet. Wenn die Wiederzulassung aktiviert ist, wird die Konversion der zuletzt eingegangenen In-App-Nachricht zugeordnet, sofern sie innerhalb des definierten Konversionsfensters erfolgt. Wenn der In-App-Nachricht jedoch bereits eine Konversion zugewiesen wurde, kann die neue Konversion für diese spezielle Nachricht nicht protokolliert werden. Das bedeutet, dass jede Zustellung einer In-App-Nachricht mit nur einer Konversion verbunden ist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endapi %}

{% api %}

### Konversionen gesamt

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Conversions' %}

Wenn ein:e Nutzer:in eine In-App-Nachricht-Kampagne nur einmal anschaut, wird nur eine Konversion gezählt, auch wenn sie das Konversions-Event später mehrfach durchführen. Wenn jedoch die Wiederzulassung aktiviert ist und der Nutzer die In-App-Nachricht-Kampagne mehrfach sieht, kann die *Gesamtkonversion* für jede Impression, die der Nutzer für eine neue Instanz der In-App-Nachricht-Kampagne protokolliert, einmal steigen. 

Wenn ein Nutzer:innen zum Beispiel zweimal eine In-App-Nachricht triggert und nach jeder Impression einer In-App-Nachricht konvertiert (was zu zwei Konversionen führt), erhöht sich die *Gesamtzahl der Konversionen* um zwei. Wenn es jedoch nur eine Impression einer In-App-Nachricht gab, auf die zwei Konversions-Events folgten, wird nur eine Konversion protokolliert, und die *Gesamtzahl der Konversionen* erhöht sich um eins.

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
|In-App-Nachrichten|Die Metrik der gesamten täglichen <i>Eindeutigen Impressionen</i> wird zur Berechnung der <i>Konversionsrate</i> für In-App-Nachrichten verwendet.<br><br>Impressionen für In-App-Nachrichten können nur einmal pro Tag gezählt werden. Andererseits kann die Anzahl der Nutzer:innen, die eine gewünschte Aktion (eine "Konversion") durchführen, innerhalb eines Zeitraums von 24 Stunden steigen. Während Konversionen mehrmals am Tag stattfinden können, ist dies bei Impressionen nicht möglich. Wenn also ein Nutzer:innen innerhalb eines Tages mehrmals eine Konversion abschließt, kann die <i>Konversionsrate</i> entsprechend steigen, aber die Impressionen werden nur einmal gezählt.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
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
    Kalkulation:
    <ul>
        <li><i>Zustellungen</i>: Anzahl</li>
        <li><i>Zustellungen %</i>: (Sendungen – Bounces) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### RCS-Zustellungsausfälle oder SMS-Zustellungsausfälle

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures' %}

Wenden Sie sich an den <a href="/docs/braze_support/">Braze Support</a>, um die Gründe für die fehlgeschlagene Zustellung zu erfahren.

<span class="calculation-line">Kalkulation: (Sendungen) – (Sendungen an Netzbetreiber)</span>

{% endapi %}

{% api %}

### Zustellfehler

{% apitags %}
RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Delivery Failures RCS' %}

Wenden Sie sich an den <a href="/docs/braze_support/">Braze Support</a>, um die Gründe für die fehlgeschlagene Zustellung zu erfahren.

<span class="calculation-line">Kalkulation: (Sendungen) – (Sendungen an Netzbetreiber)</span>

{% endapi %}

{% api %}

### Zustellfehlerrate

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Failed Delivery Rate' %}

Wenden Sie sich an den <a href="/docs/braze_support/">Braze Support</a>, um die Gründe für die fehlgeschlagene Zustellung zu erfahren.

<span class="calculation-line">Kalkulation: (Zustellungsausfälle) / (Sendungen)</span>

{% endapi %}

{% api %}

### Direkte Öffnungen

{% apitags %}
iOS-Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Direct Opens' %}

<span class="calculation-line">Kalkulation: (Direkte Öffnungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

### Per E-Mail versendbar

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Fehler

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Errors' %} Fehler sind in der Anzahl der <i>gesendeten Nachrichten</i> enthalten, aber nicht in der Anzahl der <i>eindeutigen Empfänger</i>: <i>innen</i>.

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

{% multi_lang_include analytics/metrics.md metric='Failures' %} Fehlschläge werden in der Anzahl der <i>Sendungen</i>, aber nicht in der Anzahl der <i>Zustellungen</i> berücksichtigt.</td>

<span class="calculation-line">Kalkulation<i>(Misserfolgsrate</i>): (Misserfolge) / (Sendungen)</span>

{% endapi %}

{% api %}

### Feature-Flag Experiment Performance

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

In diesem Fall markiert Braze die E-Mail Adresse als ungültig, aktualisiert aber nicht den [Abo-Status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) des Nutzers oder der Nutzerin. Wenn eine E-Mail einen "Hard Bounce" erhält, werden wir alle zukünftigen Anfragen an diese E-Mail Adresse stoppen.

{% endapi %}

{% api %}

### Hilfe

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Help' %} Eine Nutzer:innen-Antwort wird immer dann gemessen, wenn ein Nutzer innerhalb von vier Stunden nach Erhalt Ihrer Nachricht eine eingehende Nachricht sendet.

{% endapi %}

{% api %}

### Beeinflusste Öffnungen

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Kalkulation: (Beeinflusste Öffnungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

### Lifetime-Umsatz

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Lifetime-Value je Benutzer

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Durchschnittlicher Tagesumsatz

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Tägliche Einkäufe

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Täglicher Umsatz pro Nutzer:in

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### Automatische Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Diese Metrik wird ab dem 11\. November 2021 für SendGrid und ab dem 2\. Dezember 2021 für SparkPost getrackt. Bei Amazon SES wird Analytics als _Öffnungen_ angezeigt. Bot-Filter für Klicks werden jedoch unterstützt.

{% endapi %}

{% api %}

### Öffnungen

{% apitags %}
Internet-Push, iOS-Push, Android-Push
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Opt-out

{% apitags %}
SMS/MMS, RCS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Opt-Out' %} Eine Nutzer:innen-Antwort wird immer dann gemessen, wenn ein Nutzer innerhalb von vier Stunden nach Erhalt Ihrer Nachricht eine eingehende Nachricht sendet.

{% endapi %}

{% api %}

### Sonstige Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Beachten Sie, dass ein Nutzer:innen eine E-Mail auch öffnen kann (so wie die Öffnung zu den anderen Öffnungen zählt), bevor die Anzahl der Maschinenöffnungen protokolliert wird. Wenn ein Nutzer:innen eine E-Mail einmal (oder öfter) nach einem maschinellen Öffnungsereignis aus einem Posteingang, der nicht zu Apple Mail gehört, öffnet, dann wird die Anzahl der Öffnungen des Nutzers:innen in die Kategorie Andere Öffnungen und nur einmal in die Kategorie Eindeutige Öffnungen eingerechnet.

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
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} 

|Kanal|Zusätzliche Informationen|
|-------------|----------------------|
|E-Mail, Push, Webhooks|Nach dem ersten Senden.|
|Content-Cards, In-App-Nachrichten|Wenn der Nutzer:innen die Content-Card oder Nachricht zum ersten Mal sieht.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><i>Primäre Konversionen (A) oder Primäres Konversions-Event</i>: Anzahl</li>
        <li><i>Primäre Konversionen (A) %</i> oder <i>Primäres Konversions-Event</i>: (Primäre Konversionen) / (Eindeutige Empfänger:innen)</li>
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

<span class="calculation-line">Kalkulation: (Liest mit Lesebestätigungen) / (Sendet)</span>

{% endapi %}

{% api %}

### Empfangen

{% apitags %}
E-Mail, Content-Cards, In-App-Messaging, Web-Push, iOS-Push, Android-Push, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Received' %} 

|Kanal|Zusätzliche Informationen|
|-------|-------|
|Content-Cards|Wird empfangen, wenn Nutzer:innen die Karte in der App ansehen.|
|Push|Wird empfangen, wenn Nachrichten vom Braze Server an den Push-Anbieter gesendet werden.|
|E-Mail|Wird empfangen, wenn Nachrichten vom Braze Server an den Anbieter von Serviceleistungen; Diensten für E-Mails gesendet werden.|
|SMS/MMS|„Zugestellt“, nachdem der SMS-Anbieter eine Bestätigung vom vorgelagerten Netzbetreiber und dem Zielgerät erhalten hat.|
|In-App-Nachricht|Wird zum Zeitpunkt der Anzeige auf der Grundlage der definierten Aktion triggern empfangen.|
|WhatsApp|Wird zum Zeitpunkt der Anzeige auf der Grundlage der definierten Aktion triggern empfangen.|
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
    Kalkulation:
    <ul>
        <li><i>Ablehnungen</i>: Anzahl</li>
        <li><i>Ablehnungsquote</i>: (Ablehnungen) / (Sendungen)</li>
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

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Sendungen

{% apitags %}
Content-Cards, E-Mail, In-App Nachrichten, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, RCS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %} Diese Metrik wird von Braze bereitgestellt. Beachten Sie, dass beim Einführen einer geplanten Kampagne diese Metrik alle gesendeten Nachrichten berücksichtigt, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden.

{% alert tip %}
Bei Content-Cards wird diese Metrik unterschiedlich berechnet, je nachdem, was Sie für die [Erstellung der Karte]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) ausgewählt haben:

- **Beim Start oder beim Einstieg in die Stufe:** Die Anzahl der erstellten und sichtbaren Karten. Dabei wird nicht berücksichtigt, ob die Benutzer die Karte angesehen haben.
- **Auf den ersten Blick:** Die Anzahl der Karten, die den Benutzern angezeigt werden.
{% endalert %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Nachrichten gesendet

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Diese Metrik wird von Braze bereitgestellt. Beachten Sie, dass beim Einführen einer geplanten Kampagne diese Metrik alle gesendeten Nachrichten berücksichtigt, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden.

{% alert tip %}
Bei Content-Cards wird diese Metrik unterschiedlich berechnet, je nachdem, was Sie für die [Erstellung der Karte]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/) ausgewählt haben:

- **Beim Start oder beim Einstieg in die Stufe:** Die Anzahl der erstellten und sichtbaren Karten. Dabei wird nicht berücksichtigt, ob die Benutzer die Karte angesehen haben.
- **Auf den ersten Blick:** Die Anzahl der Karten, die den Benutzern angezeigt werden.
{% endalert %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Sendungen an Netzbetreiber

{% apitags %}
SMS/MMS
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends to Carrier' %} 

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><i>Sendet an Carrier</i>: Anzahl</li>
        <li><i>Sendet an Carrier Rate</i>: (Sendet an Carrier) / (Sendet)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Wenn eine E-Mail einen Soft Bounce erhält, versuchen wir es normalerweise innerhalb von 72 Stunden erneut, aber die Anzahl der Wiederholungsversuche variiert von Empfänger zu Empfänger.

Soft Bounces werden zwar nicht in den Analytics Ihrer Kampagne getrackt, aber Sie können die Soft Bounces im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) überwachen. Sie können diese Nutzer:innen auch von der Versendung ausschließen oder sich die Anzahl der Soft Bounces der letzten 30 Tage mit dem [Filter Soft Bounced Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced) ansehen. Im Nachrichten-Aktivitätsprotokoll können Sie auch den Grund für die Soft Bounces sehen und mögliche Diskrepanzen zwischen den "Sendungen" und "Zustellungen" Ihrer Kampagnen nachvollziehen.

{% endapi %}

{% api %}

### Spam

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{% alert note %}
Spam-Beschwerden werden direkt von den Anbietern von Serviceleistungen; Diensten bearbeitet und dann über eine Feedbackschleife an Braze weitergeleitet. Die meisten Feedback-Schleifen melden nur einen Teil der tatsächlichen Beschwerden, so dass die _Spam-Metrik_ oft nur einen Bruchteil der tatsächlichen Gesamtzahl darstellt. Nur Anbieter von E-Mail Serviceleistungen; Diensten können das tatsächliche Volumen von Spam-Beschwerden einsehen, was bedeutet, dass _Spam_ als eine indikative, nicht erschöpfende Metrik betrachtet werden sollte.
{% endalert %}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><i>Spam</i>: Anzahl</li>
        <li><i>Spam %</i> oder <i>Spam-Rate %</i>: (Als Spam markiert) / (Sendet)</li>
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

### Einreichung von Umfragen

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
|LINE|Tracking, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht worden ist. AMP E-Mails enthalten Klicks, die sowohl in der HTML- als auch in der Klartextversion aufgezeichnet werden. Diese Zahl kann durch Anti-Spam-Tools künstlich aufgebläht werden.|
|Banner|Die Gesamtzahl (und der Prozentsatz) der Nutzer:innen, die innerhalb der zugestellten Nachricht geklickt haben, unabhängig davon, ob derselbe Nutzer:innen mehrfach geklickt hat.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
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

{% multi_lang_include analytics/metrics.md metric='Total Dismissals' %} Wenn ein Nutzer:innen zwei verschiedene Karten aus der gleichen Kampagne erhält und beide ablehnt, erhöht sich die Anzahl um zwei. Die Wiederholbarkeit erlaubt es Ihnen, die _Gesamtzahl der Karten-Ausblendungen_ jedes Mal zu erhöhen, wenn ein Nutzer:innen eine Karte erhält; jede Karte ist eine andere Nachricht.

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><i>Entlassungen insgesamt:</i> Anzahl</li>
        <li><i>Gesamtentlassungsrate:</i> Entlassungen insgesamt / Impressionen insgesamt</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Impressionen gesamt

{% apitags %}
In-App-Nachricht, Content-Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Impressions' %} Diese Zahl ist die Summe der Anzahl der Impressionen, die Braze von den SDKs erhält.

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|Content-Cards|Die Gesamtzahl der protokollierten Impressionen für eine bestimmte Content-Card. Dieser Wert kann für denselben Nutzer:in mehrfach erhöht werden.|
|In-App-Nachrichten|Wenn es mehrere Geräte gibt und die Wiederzulassung deaktiviert ist, sollte der Nutzer:innen die In-App-Nachricht nur einmal sehen. Selbst wenn der oder die Nutzer:in mehrere Geräte verwendet, wird er nur auf dem ersten Gerät angezeigt, auf das das Targeting ausgerichtet ist. Dies setzt voraus, dass das Profil über konsolidierte Geräte verfügt und ein:e Nutzer:in eine ID hat, bei der er geräteübergreifend angemeldet ist. Wenn die Wiederzulassung aktiviert ist, wird jedes Mal, wenn der Nutzer:innen die In-App-Nachricht sieht, eine Impression protokolliert.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Öffnungen gesamt

{% apitags %}
E-Mail, iOS Push, Android Push, Internet Push, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Opens' %}

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|LINE|Tracking, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht worden ist.|
|AMP-E-Mails|Die Summe öffnet sich für die HTML- und die Klartextversion.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><b>E-Mail <i>Öffnungen insgesamt</i>:</b> Anzahl</li>
        <li><b>E-Mail <i>Öffnungsrate insgesamt</i>:</b> (Öffnungen) / (Zustellungen)</li>
        <li><b>Web-Push <i>Total Öffnet</i>:</b> <i>Direkt Öffnungen</i> zählen</li>
        <li><b>Web-Push <i>Öffnungsrate insgesamt</i>:</b> (Öffnungen insgesamt) / (Zustellungen)</li>
        <li><b>iOS, Android und Kindle Push <i>Total Öffnet</i>:</b> (Direkte Öffnungen) + (Beeinflusste Öffnungen)</li>
        <li><b>iOS, Android und Kindle Push <i>Total Opening Rate</i>:</b> (Öffnungen insgesamt) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Umsatz gesamt

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Total Revenue' %} Diese Metrik ist nur in Kampagnenvergleichsberichten über den <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Report Builder</a> verfügbar.

{% endapi %}

{% api %}

### Eindeutige Klicks

{% apitags %}
E-Mail, Content-Cards, LINE
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %}

Dazu gehören auch Klicks auf die von Braze zur Verfügung gestellten Abmeldelinks.

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|E-Mail|Tracking über einen Zeitraum von sieben Tagen.|
|LINE|Tracking, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht worden ist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
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

<span class="calculation-line">Kalkulation: (Eindeutige Entlassungen) / (Eindeutige Impressionen)</span>

{% endapi %}

{% api %}

### Eindeutige Impressionen

{% apitags %}
In-App-Nachricht, Content-Cards
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Impressions' %} 

|Kanal|Zusätzliche Informationen|
|-------|-----------------------|
|In-App-Nachrichten|Eindeutige Impressionen können nach 24 Stunden wieder hochgezählt werden, wenn die Wiederzulassung aktiviert ist und ein Nutzer:innen die Aktion triggert. Wenn die Wiederwählbarkeit eingeschaltet ist, sind <i>Eindeutige Impressionen</i> = <i>Eindeutige Empfänger:innen</i>.|
|Content-Cards|Die Anzahl sollte sich nicht erhöhen, wenn ein Nutzer:innen eine Karte zum zweiten Mal ansieht.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

<span class="calculation-line">Kalkulation: Anzahl</span>

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
|LINE|Tracking, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht worden ist.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
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

Da ein Betrachter jeden Tag ein einzigartiger Empfänger sein kann, sollten Sie erwarten, dass dieser Wert höher ist als die <i>Unique Impressions</i>. Bei Content-Cards kann jede Content-Card nur einmal empfangen werden. Wenn Sie also dieselbe Content-Card ein zweites Mal ansehen, egal an welchem Tag, wird dieser Wert nicht erhöht.<br><br>Diese Nummer erhalten Sie von Braze und basiert auf der `user_id`. Eindeutige Empfänger:innen werden auf der Ebene der Kampagne oder des Canvas-Schrittes gezählt, nicht auf der Ebene des <a href='https://braze.com/docs/api/identifier_types/#send-identifier'>Bezeichners der Sendung</a>.

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Abgemeldete Personen oder Abmeldung

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
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

<span class="calculation-line">Kalkulation: (Abmeldungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

### Variante

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS/MMS, WhatsApp
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}