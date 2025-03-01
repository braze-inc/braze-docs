---
nav_title: Glossar zu den Berichtsmetriken
article_title: Glossar zu den Berichtsmetriken
layout: report_metrics
page_order: 0
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

{% multi_lang_include metrics.md metric='AMP Clicks' %}

{% endapi %}

{% api %}

### AMP-Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='AMP Opens' %}

{% endapi %}

{% api %}

### Zielgruppe

{% apitags %}
Alle
{% endapitags %}

{% multi_lang_include metrics.md metric='Audience' %}

<span class="calculation-line">Kalkulation: (Anzahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)</span>

{% endapi %}

{% api %}

### Absprünge

{% apitags %}
E-Mail, Web-Push, iOS Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Bounces' %} Dies könnte daran liegen, dass kein gültiges Push-Token vorliegt, der oder die Nutzer:in sich abgemeldet hat, nachdem die Kampagne gestartet wurde, oder die E-Mail Adresse ungenau oder deaktiviert ist.

#### E-Mail

Ein E-Mail-Bounce für Kund:innen, die SendGrid verwenden, besteht aus Hard Bounces, Spam (`spam_report_drops`) und E-Mails, die an ungültige Adressen gesendet wurden (`invalid_emails`).

Bei E-Mails ist *Bounce %* oder *Bounce Rate* der prozentuale Anteil der Nachrichten, die von den verwendeten Serviceleistungen; Diensten erfolglos versendet oder als "zurückgeschickt" oder "nicht erhalten" bezeichnet wurden oder von den vorgesehenen Nutzer:innen nicht empfangen wurden.

#### Push

Diese Nutzer:innen sind automatisch von allen zukünftigen Push-Benachrichtigungen abgemeldet worden. 

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

{% multi_lang_include metrics.md metric='Body Click' %}

<span class="calculation-line">Kalkulation: (Körper Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Klicks auf Text

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include metrics.md metric='Body Clicks' %} Weitere Einzelheiten finden Sie in den SDK Changelogs für [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/changelog/objc_changelog#3310) und [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/changelog#1100).

<span class="calculation-line">Kalkulation: (Körper Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Klicks auf Button 1

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include metrics.md metric='Button 1 Clicks' %}

<span class="calculation-line">Kalkulation: (Button-1-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Klicks auf Button 2

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include metrics.md metric='Button 2 Clicks' %}

<span class="calculation-line">Kalkulation: (Button-2-Klicks) / (Impressionen)</span>

{% endapi %}

{% api %}

### Eingereichte Auswahlen

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include metrics.md metric='Choices Submitted' %}

{% endapi %}

{% api %}

### Effektive Klickrate

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Kalkulation: (Eindeutige Klicks) / (Eindeutige Öffnungen) (für E-Mail)</span>

{% endapi %}

{% api %}

### Bestätigte Zustellungen

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmed Deliveries' %} Als Kund:in von Braze werden die Zustellungen auf Ihr SMS-Kontingent angerechnet. 

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Vertrauen

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS-Push, Android-Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Button auf Bestätigungsseite

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Button' %}

{% endapi %}

{% api %}

### Ausblendungen der Bestätigungsseite

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include metrics.md metric='Confirmation Page Dismissals' %}

{% endapi %}

{% api %}

### Konversionen (B, C, D)

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS-Push, Android-Push, Webhook, SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversions (B, C, D)' %} Dieses definierte Event wird von Ihnen bei der Erstellung der Kampagne festgelegt. Bei E-Mail, Push und Webhooks beginnen wir mit dem Tracking von Konversionen nach dem ersten Versand. Bei Content-Cards beginnt diese Zählung, wenn sie eine Content-Card zum ersten Mal sehen.

#### In-App-Nachrichten

Bei In-App-Nachrichten wird eine Konversion gezählt, wenn der Nutzer:innen die Kampagne der In-App-Nachricht erhalten und angesehen hat und anschließend das spezifische Konversions-Event innerhalb des definierten Konversionsfensters ausführt, unabhängig davon, ob er auf die Nachricht geklickt hat oder nicht.

Konversionen werden der zuletzt empfangenen Nachricht zugeordnet. Wenn die Wiederzulassung aktiviert ist, wird die Konversion der zuletzt eingegangenen In-App-Nachricht zugeordnet, sofern sie innerhalb des definierten Konversionsfensters erfolgt. Wenn der In-App-Nachricht jedoch bereits eine Konversion zugewiesen wurde, kann die neue Konversion für diese spezielle Nachricht nicht protokolliert werden. Das bedeutet, dass jede Zustellung einer In-App-Nachricht mit nur einer Konversion verbunden ist.

{% endapi %}

{% api %}

### Konversionen gesamt

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Conversions' %}

Wenn ein:e Nutzer:in eine In-App-Nachricht-Kampagne nur einmal anschaut, wird nur eine Konversion gezählt, auch wenn sie das Konversions-Event später mehrfach durchführen. Wenn jedoch die Wiederzulassung aktiviert ist und der Nutzer die In-App-Nachricht-Kampagne mehrfach sieht, kann die *Gesamtkonversion* für jede Impression, die der Nutzer für eine neue Instanz der In-App-Nachricht-Kampagne protokolliert, einmal steigen. 

Wenn ein Nutzer:innen zum Beispiel zweimal eine In-App-Nachricht triggert und nach jeder Impression einer In-App-Nachricht konvertiert (was zu zwei Konversionen führt), erhöht sich die *Gesamtzahl der Konversionen* um zwei. Wenn es jedoch nur eine Impression einer In-App-Nachricht gab, auf die zwei Konversions-Events folgten, wird nur eine Konversion protokolliert, und die *Gesamtzahl der Konversionen* erhöht sich um eins.

{% endapi %}

{% api %}

### Konversionsrate

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS-Push, Android-Push, Webhook, SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Conversion Rate' %}

#### In-App-Nachrichten

Die Metrik der gesamten täglichen <i>Eindeutigen Impressionen</i> wird zur Berechnung der <i>Konversionsrate</i> für In-App-Nachrichten verwendet.

Impressionen für In-App-Nachrichten können nur einmal pro Tag gezählt werden. Andererseits kann die Anzahl der Nutzer:innen, die eine gewünschte Aktion (eine "Konversion") durchführen, innerhalb eines Zeitraums von 24 Stunden steigen. Während Konversionen mehrmals am Tag stattfinden können, ist dies bei Impressionen nicht möglich. Wenn also ein Nutzer:innen innerhalb eines Tages mehrmals eine Konversion abschließt, kann die <i>Konversionsrate</i> entsprechend steigen, aber die Impressionen werden nur einmal gezählt.

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

{% multi_lang_include metrics.md metric='Conversion Window' %}

{% endapi %}

{% api %}

### Zustellungen

{% apitags %}
E-Mail, Web-Push, iOS Push, Android Push, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Deliveries' %} Bei E-Mails ist *Zustellungen* die Gesamtzahl der Nachrichten (Sendungen), die erfolgreich an empfangbare Parteien gesendet und von diesen empfangen wurden.

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

### Zustellfehler

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Delivery Failures' %}

Wenden Sie sich an den <a href="/docs/braze_support/">Braze Support</a>, um die Gründe für die fehlgeschlagene Zustellung zu erfahren.

<span class="calculation-line">Kalkulation: (Sendungen) – (Sendungen an Netzbetreiber)</span>

{% endapi %}

{% api %}

### Direkte Öffnungen

{% apitags %}
iOS-Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Direct Opens' %}

<span class="calculation-line">Kalkulation: (Direkte Öffnungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

### Per E-Mail versendbar

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Emailable' %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Fehler

{% apitags %}
Webhook
{% endapitags %}

{% multi_lang_include metrics.md metric='Errors' %} Fehler sind in der Zählung der <i>Sendungen</i> enthalten, aber nicht in der Zählung der <i>eindeutigen Empfänger</i>: <i>innen</i>.

{% endapi %}

{% api %}

### Geschätzte reale Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Estimated Real Opens' %}

{% endapi %}

{% api %}

### Misserfolge

{% apitags %}
WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Failures' %} Ausfälle sind in der Anzahl der <i>Sendungen</i>, aber nicht in der Anzahl der <i>Zustellungen</i> enthalten.</td>

<span class="calculation-line">Kalkulation<i>(Misserfolgsrate</i>): (Misserfolge) / (Sendungen)</span>

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Hard Bounce' %} 

In diesem Fall markiert Braze die E-Mail Adresse als ungültig, aktualisiert aber nicht den [Abo-Status]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) des Nutzers oder der Nutzerin. Wenn eine E-Mail einen "Hard Bounce" erhält, werden wir alle zukünftigen Anfragen an diese E-Mail Adresse stoppen.

{% endapi %}

{% api %}

### Hilfe

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Help' %} Eine Nutzerantwort wird immer dann gemessen, wenn ein Nutzer:in innerhalb von vier Stunden nach Erhalt Ihrer Nachricht eine eingehende Nachricht sendet.

{% endapi %}

{% api %}

### Beeinflusste Öffnungen

{% apitags %}
iOS Push, Android Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Influenced Opens' %}

<span class="calculation-line">Kalkulation: (Beeinflusste Öffnungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

### Lifetime-Umsatz

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Revenue' %}

{% endapi %}

{% api %}

### Lifetime-Value je Benutzer

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Lifetime Value Per User' %}

{% endapi %}

{% api %}

### Durchschnittlicher Tagesumsatz

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS-Push, Android-Push, Webhook, SMS,LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Average Daily Revenue' %}

{% endapi %}

{% api %}

### Tägliche Einkäufe

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Daily Purchases' %}

{% endapi %}

{% api %}

### Täglicher Umsatz pro Nutzer:in

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS Push, Android Push, Webhook, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Daily Revenue Per User' %}

{% endapi %}

{% api %}

### Automatische Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Machine Opens' %} Diese Metrik wird ab dem 11\. November 2021 für SendGrid und ab dem 2\. Dezember 2021 für SparkPost getrackt.

{% endapi %}

{% api %}

### Öffnungen

{% apitags %}
Internet-Push, iOS-Push, Android-Push
{% endapitags %}

{% multi_lang_include metrics.md metric='Opens' %}

{% endapi %}

{% api %}

### Opt-out

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Opt-Out' %} Eine Nutzerantwort wird immer dann gemessen, wenn ein Nutzer:in innerhalb von vier Stunden nach Erhalt Ihrer Nachricht eine eingehende Nachricht sendet.

{% endapi %}

{% api %}

### Sonstige Öffnungen

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Other Opens' %} Beachten Sie, dass ein:e Nutzer:in eine E-Mail auch öffnen kann (z. B. wird die Anzahl der Öffnungen unter „Sonstige Öffnungen“ erfasst), bevor eine „ Automatische Öffnungen“-Zählung protokolliert wird. Wenn ein Nutzer:innen eine E-Mail einmal (oder öfter) nach einem maschinellen Öffnungsereignis aus einem Posteingang, der nicht zu Apple Mail gehört, öffnet, dann wird die Anzahl der Öffnungen des Nutzers:innen in die Kategorie Andere Öffnungen und nur einmal in die Kategorie Eindeutige Öffnungen eingerechnet.

{% endapi %}

{% api %}

### Ausstehender Wiederholungsversuch

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Pending Retry' %}

{% endapi %}

{% api %}

### Primäre Konversionen (A) oder primäres Konversions-Event

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS-Push, Android-Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Bei E-Mail, Push und Webhooks beginnen wir mit dem Tracking der Konversionen nach dem ersten Versand. Bei Content-Cards und In-App-Nachrichten beginnt die Zählung, wenn sie eine Content-Card oder Nachricht zum ersten Mal sehen.

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

{% multi_lang_include metrics.md metric='Reads' %}

{% endapi %}

{% api %}

### Empfangen

{% apitags %}
E-Mail, Content-Cards, In-App-Messaging, Web-Push, iOS-Push, Android-Push, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Received' %} 

- Content-Cards: Wird empfangen, wenn Nutzer:innen die Karte in der App ansehen.
- Push: Wird empfangen, wenn Nachrichten vom Braze Server an den Push-Anbieter gesendet werden.
- E-Mail: Wird empfangen, wenn Nachrichten vom Braze Server an den Anbieter von Serviceleistungen; Diensten für E-Mails gesendet werden.
- SMS/MMS: „Zugestellt“, nachdem der SMS-Anbieter eine Bestätigung vom vorgelagerten Netzbetreiber und dem Zielgerät erhalten hat.
- In-App-Nachricht: Wird zum Zeitpunkt der Anzeige auf der Grundlage der definierten Aktion triggern empfangen.
- WhatsApp: Wird zum Zeitpunkt der Anzeige auf der Grundlage der definierten Aktion triggern empfangen.

{% endapi %}

{% api %}

### Zurückweisungen

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Rejections' %} Als Kund:in von Braze werden Ablehnungen auf Ihr SMS-Kontingent angerechnet.

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Umsatz

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Revenue' %}

{% endapi %}

{% api %}

### Gesendet

{% apitags %}
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sent' %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Sendungen

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS-Push, Android-Push, Webhook, SMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends' %} Diese Metrik wird von Braze bereitgestellt. Beachten Sie, dass beim Einführen einer geplanten Kampagne diese Metrik alle gesendeten Nachrichten berücksichtigt, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden.

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
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS-Push, Android-Push, Webhook, SMS, WhatsApp, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Messages Sent' %} Diese Metrik wird von Braze bereitgestellt. Beachten Sie, dass beim Einführen einer geplanten Kampagne diese Metrik alle gesendeten Nachrichten berücksichtigt, unabhängig davon, ob sie aufgrund von Rate-Limiting bereits versendet wurden.

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
SMS
{% endapitags %}

{% multi_lang_include metrics.md metric='Sends to Carrier' %} 

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Soft Bounce' %} Wenn eine E-Mail einen Soft Bounce erhält, versuchen wir es in der Regel innerhalb von 72 Stunden erneut, aber die Anzahl der Wiederholungsversuche variiert von Empfänger zu Empfänger.

{% endapi %}

{% api %}

### Spam

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Spam' %}

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

{% multi_lang_include metrics.md metric='Survey Page Dismissals' %}

{% endapi %}

{% api %}

### Einreichung von Umfragen

{% apitags %}
In-App-Nachricht
{% endapitags %}

{% multi_lang_include metrics.md metric='Survey Submissions' %}

{% endapi %}

{% api %}

### Klicks gesamt

{% apitags %}
E-Mail, Content-Cards, SMS, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Clicks' %} Bei LINE wird dies getrackt, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde. Bei AMP-E-Mails ist dies die Gesamtzahl der Klicks in der HTML- und der Klartextversion.

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

{% multi_lang_include metrics.md metric='Total Dismissals' %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Impressionen gesamt

{% apitags %}
In-App-Nachricht, Content-Cards
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Impressions' %} Diese Zahl ist die Summe der Impressionen, die Braze von den SDKs erhält. Bei Content-Cards ist dies die Gesamtzahl der Impressionen, die für eine bestimmte Content-Card protokolliert wurden. Dieser Wert kann für denselben Nutzer:in mehrfach erhöht werden.

Bei In-App-Nachrichten sollte der Nutzer:in, wenn es mehrere Geräte gibt und die Wiederzulassung ausgeschaltet ist, die In-App-Nachricht nur einmal sehen. Selbst wenn der oder die Nutzer:in mehrere Geräte verwendet, wird er nur auf dem ersten Gerät angezeigt, auf das das Targeting ausgerichtet ist. Dies setzt voraus, dass das Profil über konsolidierte Geräte verfügt und ein:e Nutzer:in eine ID hat, bei der er geräteübergreifend angemeldet ist. Wenn die erneute Qualifizierung aktiviert ist, wird jedes Mal eine Impression protokolliert, wenn der oder die Nutzer:in die In-App-Nachricht sieht.

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Öffnungen gesamt

{% apitags %}
E-Mail, iOS Push, Android Push, Internet Push, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Opens' %} Bei LINE wird dies getrackt, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde. Bei AMP-E-Mails ist dies die Gesamtzahl der Öffnungen für die HTML- und die Klartextversion. 

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><b>E-Mail:</b> (Öffnungen) / (Zustellungen)</li>
        <li><b>Web-Push:</b> (Direkte Öffnungen) / (Zustellungen)</li>
        <li><b>iOS, Android, und Kindle Push:</b> (Eindeutige Öffnungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Umsatz gesamt

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS-Push, Android-Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Total Revenue' %} Diese Metrik ist nur in Kampagnenvergleichsberichten über den <a href='https://braze.com/docs/user_guide/data_and_analytics/reporting/report_builder/'>Berichts-Builder</a> verfügbar.

{% endapi %}

{% api %}

### Eindeutige Klicks

{% apitags %}
E-Mail, Content-Cards, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Clicks' %} Dies wird über einen Zeitraum von sieben Tagen für E-Mails getrackt. Dazu gehören auch Klicks auf die von Braze zur Verfügung gestellten Abmeldelinks. Bei LINE wird dies getrackt, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde.

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

{% multi_lang_include metrics.md metric='Unique Dismissals' %}

<span class="calculation-line">Kalkulation: (Eindeutige Entlassungen) / (Eindeutige Impressionen)</span>

{% endapi %}

{% api %}

### Eindeutige Impressionen

{% apitags %}
In-App-Nachricht, Content-Cards
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Impressions' %} Für In-App-Nachrichten können die eindeutigen Impressionen nach 24 Stunden wieder erhöht werden, wenn die Wiederzulassung aktiviert ist und ein:e Nutzer:in die Aktion triggert. Wenn die Wiedererkennbarkeit eingeschaltet ist, sind <i>Eindeutige Impressionen</i> = <i>Eindeutige Empfänger:innen</i>. <br><br>Bei Content-Cards sollte die Anzahl nicht erhöht werden, wenn ein Nutzer:innen eine Karte zum zweiten Mal ansieht. 

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Eindeutige Öffnungen

{% apitags %}
E-Mail, LINE
{% endapitags %}

{% multi_lang_include metrics.md metric='Unique Opens' %} Bei E-Mails wird dies über einen Zeitraum von 7 Tagen verfolgt. Bei LINE wird dies getrackt, nachdem eine Mindestschwelle von 20 Nachrichten pro Tag erreicht wurde.

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

{% multi_lang_include metrics.md metric='Unique Recipients' %}

Da ein Betrachter jeden Tag ein einzigartiger Empfänger sein kann, sollten Sie erwarten, dass dieser Wert höher ist als die <i>Unique Impressions</i>. Diese Nummer erhalten Sie von Braze und basiert auf der `user_id`.

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Abgemeldete Personen oder Abmeldung

{% apitags %}
E-Mail
{% endapitags %}

{% multi_lang_include metrics.md metric='Unsubscribers or Unsub' %}

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

{% multi_lang_include metrics.md metric='Unsubscribes' %}

<span class="calculation-line">Kalkulation: (Abmeldungen) / (Zustellungen)</span>

{% endapi %}

{% api %}

### Variante

{% apitags %}
Content-Cards, E-Mail, In-App-Messaging, Web-Push, iOS-Push, Android-Push, Webhook, SMS, WhatsApp
{% endapitags %}

{% multi_lang_include metrics.md metric='Variation' %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}