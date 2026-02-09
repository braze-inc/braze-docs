---
nav_title: E-Mail-Analyse-Glossar
article_title: E-Mail-Analyse-Glossar
layout: email_report_metrics
page_order: 0
excerpt_separator: ""
page_type: glossary
description: "Dieses Glossar enthält die Begriffe, die Sie im Analysebereich Ihrer E-Mail-Kampagne oder Ihres Canvas nach dem Start finden werden. Dieses Glossar enthält keine Currents-Metriken."
channel: 
  - email
---

<style>
  .calculation-line {
    color: #76848C;
    font-size: 14px;
  }
</style>

{% api %}

### Variante

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Variation' %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Per E-Mail versendbar

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Emailable' %}

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Zielgruppe %

{% apitags %}
Prozentsatz
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Audience' %}

<span class="calculation-line">Kalkulation: (Anzahl der Empfänger:innen in der Variante) / (Eindeutige Empfänger:innen)</span>

{% endapi %}

{% api %}

### Eindeutige Empfänger:innen

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Recipients' %} Diese Nummer wird von Braze empfangen.

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Sendungen

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Sends' %}  Diese Metrik wird von Braze bereitgestellt.

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Nachrichten gesendet

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Messages Sent' %}  Diese Metrik wird von Braze bereitgestellt.

<span class="calculation-line">Kalkulation: Anzahl</span>

{% endapi %}

{% api %}

### Zustellungen

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries' %} Bei E-Mails ist *Deliveries* die Gesamtzahl der Nachrichten (Sends), die erfolgreich an empfangbare Parteien gesendet und von diesen empfangen wurden.

<span class="calculation-line">Kalkulation: (Sendet) - (Prellt) </span>

{% endapi %}

{% api %}

### Zustellungen %

{% apitags %}
Prozentsatz
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Deliveries %' %}

<span class="calculation-line">Kalkulation: (Sendungen - Bounces) / (Sendungen) </span>

{% endapi %}

{% api %}

### Absprünge

{% apitags %}
Anzahl, Prozentsatz
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Bounces' %} 

Bei E-Mails ist *Bounce %* oder *Bounce Rate* der prozentuale Anteil der Nachrichten, die von den verwendeten Serviceleistungen; Diensten erfolglos versendet oder als "zurückgeschickt" oder "nicht erhalten" bezeichnet wurden oder von den vorgesehenen Nutzer:innen nicht empfangen wurden.

Ein E-Mail-Bounce für Kund:innen, die SendGrid verwenden, besteht aus Rückläufern (Hard Bounced), Spam (`spam_report_drops`) und E-Mails, die an ungültige Adressen gesendet wurden (`invalid_emails`).

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><b><i>Prellungen</i>:</b> Anzahl</li>
        <li><b><i>Bounce %</i> oder <i>Bounce Rate %</i>:</b> (Bounces) / (Sendungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Hard Bounce

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Hard Bounce' %} 

<span class="calculation-line">Kalkulation: Zählen</span>

{% endapi %}

{% api %}

### Soft Bounce

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Soft Bounce' %} Wenn eine E-Mail einen Soft Bounce erhält, versuchen wir es normalerweise innerhalb von 72 Stunden erneut, aber die Anzahl der Wiederholungsversuche variiert von Empfänger zu Empfänger. 

Soft Bounces werden zwar nicht in den Analytics Ihrer Kampagne getrackt, aber Sie können die Soft Bounces im [Nachrichten-Aktivitätsprotokoll]({{site.baseurl}}/user_guide/administrative/app_settings/message_activity_log_tab/) überwachen oder diese Nutzer:innen mit dem [Filter für Soft Bounced-Segmente]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced) von Ihrem Versand ausschließen. Im Nachrichten-Aktivitätsprotokoll können Sie auch den Grund für die Soft Bounces sehen und mögliche Diskrepanzen zwischen den "Sendungen" und "Zustellungen" Ihrer Kampagnen nachvollziehen.

<span class="calculation-line">Kalkulation: Zählen</span>

{% endapi %}

{% api %}
  
### Spam

{% apitags %}
Anzahl, Prozentsatz
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Spam' %}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><b><i>Spam</i>:</b> Anzahl</li>
        <li><b><i>Spam %</i> oder <i>Spam-Rate %</i>:</b> (Als Spam markiert) / (Sendet)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Eindeutige Öffnungen

{% apitags %}
Anzahl, Prozentsatz
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Opens' %} Bei E-Mails wird dies über einen Zeitraum von 7 Tagen getrackt.

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><b><i>Eindeutige Öffnungen</i>:</b> Anzahl</li>
        <li><b><i>Eindeutige Öffnungen %</i> oder <i>Eindeutige Öffnungsrate</i>:</b> (Eindeutige Öffnungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Eindeutige Klicks

{% apitags %}
Anzahl, Prozentsatz
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unique Clicks' %} Dies wird über einen Zeitraum von sieben Tagen für E-Mails getrackt und durch <a href='/docs/help/help_articles/data/dispatch_id/'>dispatch_id</a>. Dazu gehören auch Klicks auf die von Braze zur Verfügung gestellten Abmeldelinks.

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><b><i>Eindeutige Klicks</i>:</b> Anzahl</li>
        <li><b><i>Einzigartige Klicks %</i> oder <i>Klickrate</i>:</b> (Einzigartige Klicks) / (Auslieferungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}
  
### Abgemeldete Personen oder Abmeldung

{% apitags %}
Anzahl, Prozentsatz
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Unsubscribers or Unsub' %}

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><b><i>Abgemeldete Personen</i> oder <i>Abmeldung</i>:</b> Anzahl</li>
        <li><b><i>Abgemeldete Personen %</i> oder <i>Abmelderate</i>:</b> (Abmeldungen) / (Zustellungen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Umsatz

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Revenue' %}

<span class="calculation-line">Kalkulation: Zählen</span>

{% endapi %}

{% api %}

### Primäre Konversionen (A) oder primäres Konversions-Event

{% apitags %}
Anzahl, Prozentsatz
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Primary Conversions (A) or Primary Conversion Event' %} Bei E-Mail, Push und Webhooks beginnen wir mit dem Tracking von Konversionen nach dem ersten Versand.

{::nomarkdown}
<span class="calculation-line">
    Kalkulation:
    <ul>
        <li><b><i>Primäre Konversionen (A)</i> oder <i>primäres Konversions-Event</i>:</b> Anzahl</li>
        <li><b><i>Primäre Konversionen (A) %</i> oder <i>Primäre Konversions-Event-Rate</i>:</b> (Primäre Konversionen) / (Eindeutige Empfänger:innen)</li>
    </ul>
</span>
{:/}

{% endapi %}

{% api %}

### Vertrauen

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Confidence' %}

{% endapi %}

{% api %}

### Automatische Öffnungen
  
{% multi_lang_include analytics/metrics.md metric='Machine Opens' %} Diese Metrik wird ab dem 11\. November 2021 für SendGrid und ab dem 2\. Dezember 2021 für SparkPost getrackt.

<span class="calculation-line">Kalkulation: Zählen</span>

{% endapi %}

{% api %}

### Sonstige Öffnungen

{% apitags %}
Anzahl
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Other Opens' %} Beachten Sie, dass ein Nutzer:innen eine E-Mail auch öffnen kann (so wie die Öffnung zu den <i>anderen Öffnungen</i> zählt), bevor die Anzahl der <i>Maschinenöffnungen</i> protokolliert wird. Wenn ein Benutzer eine E-Mail einmal (oder öfter) nach einem maschinellen Öffnungsereignis aus einem Nicht-Apple Mail-Posteingang öffnet, wird die Anzahl der Öffnungen des Benutzers in die Kategorie <i>Andere Öffnungen</i> und nur einmal in die Kategorie <i>Einmalige Öffnungen</i> eingerechnet.

<span class="calculation-line">Kalkulation: Zählen</span>

{% endapi %}

{% api %}

### Effektive Klickrate

{% apitags %}
Prozentsatz
{% endapitags %}

{% multi_lang_include analytics/metrics.md metric='Click-to-Open Rate' %}

<span class="calculation-line">Kalkulation: (Eindeutige Klicks) / (Eindeutige Öffnungen) (für E-Mail)</span>

{% endapi %}