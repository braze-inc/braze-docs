---
nav_title: SalesWings
article_title: SalesWings
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und SalesWings, einer Analyseplattform, die Ihnen hilft, Scoring und Grading, Vertriebseinblicke und -warnungen, Marketingausrichtung und B2B-Attributionsberichte zu verfolgen."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings][1] ist ein B2B SaaS-Add-on für Lead-Profiling, das für Marketing- und Vertriebsteams entwickelt wurde. Es hilft bei der Lead- und Account-Qualifizierung durch Lead-Scoring und -Einstufung, Vertriebseinblicke und -warnungen, Marketing-Ausrichtung und B2B-Attributionsberichte sowie eine enge Salesforce CRM-Integration.

SalesWings ermöglicht es Marketing-Teams und Marketing-Managern, Leads und Accounts für ihre Vertriebsteams zu qualifizieren, was für die Abstimmung und Effizienz von Vertrieb und Marketing unerlässlich ist. Darüber hinaus kann SalesWings zusammen mit Braze den Vertriebsmitarbeitern die Customer Journey eines Leads und die Daten zum Engagement in der Braze-Marketingkampagne anzeigen, so dass Sie die Lead-Qualifizierungsrate durch fundiertere Gespräche erhöhen können.

## Voraussetzungen
 
| Anforderung | Beschreibung |
| ----------- | ----------- |
| SalesWings Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [SalesWings-Konto][1]. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit `users.export.ids` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][2]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Segment.com Konto (optional) | Wenn Sie Segment.com nutzen, können Sie alle Lead-Engagement- und Profildaten senden und Ereignisse über Segment.com für die Lead-Profilerstellung identifizieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

{% tabs %}
{% tab Lead Scoring %}

SalesWings bietet Braze-Kunden [eine flexible Möglichkeit zur Qualifizierung von Leads, Kontakten und Kunden mit hochmodernen Lead-Scoring-](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs) und Lead-Grading-Funktionen. Alle Ihre Lead-Qualifizierungsdaten werden nativ an Salesforce CRM und andere Systeme weitergeleitet, in denen Sie Leads, Kontakte, Konten und Opportunities verwalten und Berichte darüber erstellen möchten.

![Beispiel für ein einfaches Lead-Scoring-Modell mit Click-not-Code in SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Beispiel für ein einfaches Lead-Scoring-Modell in SalesWings, bei dem der Klick nicht kodiert wird_
{% endtab %}
{% tab Ausrichtung von Vertrieb und Marketing %}
SalesWings ermöglicht es Marketingteams, marketingqualifizierte Leads zu verfolgen, zu qualifizieren und an Ihre Vertriebsteams zu übergeben. Alle SalesWings-Daten werden nativ in Salesforce übertragen und können zur Feinabstimmung bestehender Prozesse oder zur Erstellung neuer Prozesse über Listen, Berichte, Abläufe und mehr genutzt werden.

![Beispiel dafür, wie SalesWings Lead Scoring eine Liste von Leads oder Kontakten nativ in Salesforce priorisiert]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Beispiel dafür, wie das SalesWings Lead Scoring eine Liste von Leads oder Kontakten nativ in Salesforce priorisiert_

![Beispiel dafür, wie SalesWings Lead Scoring eine Liste von Accounts nativ in Salesforce priorisiert]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Beispiel dafür, wie das SalesWings Lead Scoring eine Liste von Accounts nativ in Salesforce priorisiert_
{% endtab %}
{% tab Lead- und Account-Einstufung %}
Mit SalesWings können Braze-Kunden Leads und Kunden auf der Grundlage von Profildaten (in der Regel CRM-Daten) qualifizieren. Dies wird auch als "Lead Grading", "Fit Scoring" oder "Firmographic Scoring" bezeichnet. Braze-Kunden können Attributdaten direkt an SalesWings senden, und SalesWings kann alle Salesforce CRM-Standard- oder benutzerdefinierten Objektdaten und Datensätze für eine ganzheitliche Profilbewertung lesen.
{% endtab %}
{% tab Vertriebseinblicke für Vertriebsmitarbeiter %}
Mit SalesWings können Sie Ihren Vertriebsmitarbeitern Einblicke in den Vertrieb ihrer Leads, Kontakte und Konten geben (Alternative zu Marketo Sales Insights). Im Wesentlichen können Sie Ihrem Vertriebsteam alle Braze- und Web-Engagement-Daten zur Verfügung stellen. Die Erkenntnisse sind nativ in Salesforce CRM eingebettet und können an andere CRMs oder Systeme oder über eine Braze-E-Mail als "Vertriebswarnung" weitergeleitet werden.

![Beispiel für die Sales Insights-Ansicht für Vertriebsmitarbeiter in Salesforce (auch für andere CRM-Systeme verfügbar)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Beispiel einer Sales Insights-Ansicht für Vertriebsmitarbeiter in Salesforce (auch für andere CRM-Systeme verfügbar)_
{% endtab %}
{% tab Verkaufswarnungen %}
SalesWings bietet native E-Mail- und Slack-Benachrichtigungen, und Sie können Berichtsabonnements in Salesforce einrichten, auf die Ihr Vertriebsteam zugreifen kann, um tägliche, wöchentliche und monatliche E-Mail-Berichte zu erhalten. Außerdem können Sie über eine Zapier-Integration zusätzliche Workflows auf der Grundlage von SalesWings-Lead-Qualifikationsdaten erstellen.

![Beispiel einer Verkaufsmeldung über den Slack-Kanal]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Beispiel einer Verkaufsmeldung über einen Slack-Kanal_
{% endtab %}
{% tab Berichterstattung in Salesforce CRM %}
Durch die SalesWings-Integration mit Salesforce können Sie automatisierte Berichte mit Leads, Kontakten, Konten und Opportunities erstellen, die auf Daten zum Web-Engagement und dem Engagement von Braze-Kampagnen basieren. So können Sie z.B. eine Liste heißer Leads an ein Vertriebsteam weiterleiten, in der alle Personen aufgeführt sind, die auf eine bestimmte E-Mail-Kampagne geklickt oder eine bestimmte Aktion in Ihrer App oder auf Ihrer Website durchgeführt haben.

![Ein Beispiel für ein Dashboard, das mit dem E-Mail- und Marketing-Engagement von Braze in Salesforce verknüpft ist und die Auswirkungen von Braze-Kampagnen auf die Verkaufsergebnisse und -erfolge zeigt]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Ein Beispiel für ein Dashboard, das mit dem E-Mail- und Marketing-Engagement von Braze in Salesforce verknüpft ist und die Auswirkungen von Braze-Kampagnen auf die Vertriebsergebnisse und -erfolge zeigt._
{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: SalesWings Konto und Konfiguration

[Vereinbaren Sie eine Demo][4] mit dem freundlichen SalesWings-Team, um mehr über SalesWings zu erfahren.

### Schritt 2: Installieren von Verhaltenstracking auf Ihrer Website oder App

Derzeit haben Sie zwei Möglichkeiten, in SalesWings Verhaltensdaten für das Lead Scoring und die Vertriebseinblicke zu sammeln:
* [Implementieren Sie das SalesWings-Tracking-JavaScript][5] auf den Websites und Anwendungen, auf denen Sie Leads verfolgen und identifizieren möchten.
* Senden Sie verhaltensbezogene Lead-Aktivitätsdaten (und Lead-Profildaten) über die SalesWings-Integration mit Segment.com

### Schritt 3: Verbindung zwischen SalesWings und Braze

Gehen Sie zur [Seite**SalesWings-Einstellungen**][6] und erweitern Sie den Abschnitt **Braze-Integration**.

![Der Abschnitt Braze Integration auf der Seite SalesWings Einstellungen.][7]

Kopieren Sie den Wert der Spalte **Bezeichner** für den neu erstellten Schlüssel und fügen Sie ihn in das Feld **Braze API-Schlüssel** im Abschnitt SalesWings **Braze Integration** ein.

Fügen Sie Ihren Braze-API-Endpunkt hinzu, wie im Artikel [API- und SDK-Endpunkte][8] beschrieben, und geben Sie ihn in das Feld **Braze-API-Endpunkt** ein. Kopieren Sie den Wert der Spalte **REST Endpoint** und geben Sie ihn in das Feld **Braze API endpoint** im Abschnitt SalesWings **Braze Integration** ein.

Klicken Sie dann in den SalesWings-Einstellungen auf **Änderungen speichern**.

### Schritt 4: Konfigurieren der SalesWings-Lead-Bewertung für Braze, CRM-Integration und mehr

Wenden Sie sich an das SalesWings-Serviceteam, um über die [Website][1] vollständige Unterstützung beim Onboarding zu erhalten.

## Mit dieser Integration 

Um ein Lead Scoring und die Erstellung von Sales Insights auszulösen, muss SalesWings einen Benutzer auf Ihrer Website oder App identifizieren. Dies kann auf die folgenden Arten geschehen:

- **Formular einreichen:** Wenn ein Benutzer ein Webformular abschickt, identifiziert SalesWings automatisch alle Ihre Web-Formulartypen (z. B. Anmeldung, Download, Kontakt usw.) und löst die Identität eines Benutzers auf, wenn dieser ein Formular abschickt. 
- **URL-Klicks mit einer Braze-ID oder einer externen ID:** Ein Benutzer klickt auf eine Marketingaktion von Braze, in der Regel auf eine E-Mail, ein Banner oder ähnliches, was zu einer Seite führt, die Sie mit SalesWings verfolgen.
- **Verfolgung von Verkaufs-E-Mails über Gmail- und Outlook-Plugins (optional):** Wenn Sie Ihren Vertriebsmitarbeitern E-Mail-Tracking-Plugins an die Hand geben, können diese durch das Versenden von Tracking-Links eine vollständige Nachverfolgung der Nutzer auf der Website auslösen.
- **Segment.com Ereignis identifizieren (optional):** Wenn Sie ein Segment.com Benutzer sind, können Sie die Identität eines Benutzers auch mit der Segment.com Integration auflösen.

### Identifizierung von Benutzern anhand von URL-Klicks

Sie können Benutzer automatisch identifizieren, wenn sie auf eine verfolgbare URL klicken (z.B. E-Mail-Blasts, Banner mit URLs). Um eine URL nachverfolgbar zu machen, gibt es zwei Möglichkeiten, Ihre Website-URLs in Ihren E-Mails, Bannern oder SMS zu ändern, indem Sie den Parameter und die ID am Ende Ihrer Links hinzufügen.

1. Anhängen von `?braze_id=` gefolgt von {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Beispiel für einen Link:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Anhängen von `?br_user_id=` gefolgt von {% raw %}`{{${user_id}}}`{% endraw %}
  - **Beispiel für einen Link:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

Die Variable `braze_id` wird auf einen von Braze erzeugten Bezeichner des Benutzers gesetzt und ist immer verfügbar. Die Variable `br_user_id` wird auf die Benutzerkennung in Ihrem System gesetzt und kann in bestimmten Szenarien fehlen (z.B. bei anonymen Benutzern, die mit dem Braze SDK erstellt wurden). Wenn sowohl `braze_id` als auch `br_user_id` in einem Link verwendet werden, wird SalesWings nur den Parameter `braze_id` berücksichtigen.

Für die Konfiguration und weitere Fehlerbehebung wenden Sie sich bitte an das [SalesWings-Serviceteam][1], das Sie bei der Einführung unterstützt.

[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
