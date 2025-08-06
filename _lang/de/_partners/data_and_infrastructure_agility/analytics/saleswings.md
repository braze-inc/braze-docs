---
nav_title: SalesWings
article_title: SalesWings
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und SalesWings, einer Analytics-Plattform, die Ihnen hilft, Scoring und Grading, Insights und Alerts für den Vertrieb, Marketing-Ausrichtung und B2B Attribution Reporting zu verfolgen."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings][1] ist ein B2B SaaS Lead Profiling Add-on für Marketing- und Vertriebsteams, das die Lead- und Account-Qualifizierung durch Lead Scoring und Grading, Insights und Warnungen für den Vertrieb, Insights für das Marketing und B2B Attribution Reporting sowie eine enge Integration in Salesforce CRM unterstützt.

_Diese Integration wird von SalesWings gepflegt._

## Über die Integration

SalesWings erlaubt es Marketing Teams und Marketing Operations Managern, Leads und Accounts für ihre Sales Teams zu qualifizieren, was für die Ausrichtung und Effizienz von Sales und Marketing unerlässlich ist. Darüber hinaus kann SalesWings zusammen mit Braze den Vertriebsmitarbeitern die Customer Journey eines Leads und die Daten über das Engagement in den Marketing Kampagnen von Braze anzeigen, was es Ihnen erlaubt, die Qualifizierungsraten von Leads durch fundiertere Gespräche zu erhöhen.

## Voraussetzungen
 
| Anforderung | Beschreibung |
| ----------- | ----------- |
| SalesWings Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [SalesWings-Konto][1]. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.export.ids` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt][2]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Segment.com Konto (optional) | Wenn Sie Nutzer:innen von Segment.com sind, können Sie alle Daten zum Engagement und Profil von Leads sowie zur Identifizierung von Ereignissen an Segment.com senden, um ein Lead-Profil zu erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

{% tabs %}
{% tab Lead Scoring %}

SalesWings bietet Kund:innen von Braze [eine flexible Möglichkeit, Leads, Kontakte und Konten mit hochmodernen Lead Scoring- und Lead Grading-Funktionen zu qualifizieren](https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs). Alle Ihre Daten zur Lead-Qualifizierung werden nativ an Salesforce CRM und andere Systeme gepusht, in denen Sie Leads, Kontakte, Accounts und Opportunities verwalten und darüber berichten möchten.

![Beispiel für ein einfaches Lead-Scoring-Modell mit Klick-nicht-Code in SalesWings]({% image_buster /assets/img/saleswings/example_lead_scoring_builder_braze_lead_scoring.png %})

_Beispiel für ein einfaches Lead-Scoring-Modell mit Klick-nicht-Code in SalesWings_
{% endtab %}
{% tab Ausrichtung von Marketing und Vertrieb %}
SalesWings erlaubt Marketing Teams das Tracking, die Qualifizierung und die Übergabe marketingqualifizierter Leads an Ihre Vertriebsteams. Alle SalesWings Daten werden nativ an Salesforce gepusht und können genutzt werden, um bestehende Prozesse zu optimieren oder neue Prozesse über Listen, Berichte, Abläufe und mehr zu erstellen.

![Beispiel dafür, wie SalesWings Lead Scoring eine Liste von Leads oder Kontakten nativ in Salesforce priorisiert]({% image_buster /assets/img/saleswings/prioritized_lead_or_contact_list_braze_lead_scoring.png %})

_Beispiel dafür, wie das SalesWings Lead Scoring eine Liste von Leads oder Kontakten nativ in Salesforce priorisiert_

![Beispiel dafür, wie SalesWings Lead Scoring eine Liste von Accounts nativ in Salesforce priorisiert]({% image_buster /assets/img/saleswings/prioritized_account_list_braze_lead_scoring.png %})

_Beispiel dafür, wie das SalesWings Lead Scoring eine Liste von Accounts nativ in Salesforce priorisiert_
{% endtab %}
{% tab Lead- und Account-Einstufung %}
SalesWings erlaubt es Braze-Kunden, Leads und Konten auf der Grundlage von Profildaten (typischerweise CRM-Daten) zu qualifizieren. Dies wird auch als "Lead Grading", "Fit Scoring" oder "Firmographic Scoring" bezeichnet. Braze-Kunden können Attribut-Daten direkt an SalesWings senden, und SalesWings kann alle Daten und Datensätze von Salesforce CRM-Standard- oder angepassten Objekten für eine ganzheitliche Profilbewertung lesen.
{% endtab %}
{% tab Sales Insights für Vertriebsmitarbeiter %}
Mit SalesWings können Sie Ihren Vertriebsmitarbeitern Insights über ihre Leads, Kontakte und Konten zeigen (Alternative zu Marketo Sales Insights). Im Wesentlichen können Sie alle Daten aus Braze und dem Internet-Engagement für Ihr Vertriebsteam sichtbar machen. Die Insights sind nativ in Salesforce CRM eingebettet und können per Push an andere CRMs oder Systeme oder über eine E-Mail von Braze als "Verkaufsalarm" übermittelt werden.

![Beispiel einer Insights-Ansicht für Vertriebsmitarbeiter in Salesforce (auch für andere CRM-Systeme verfügbar)]({% image_buster /assets/img/saleswings/marketo_sales_insights_alternative_for_braze.png %})

_Beispiel einer Insights-Ansicht für Vertriebsmitarbeiter in Salesforce (auch für andere CRM-Systeme verfügbar)_
{% endtab %}
{% tab Verkaufswarnungen %}
SalesWings bietet native E-Mail- und Slack-Benachrichtigungen, und Sie können Berichtsabonnements in Salesforce einrichten, auf die Ihr Vertriebsteam zugreifen kann, um tägliche, wöchentliche und monatliche E-Mail-Berichte zu erhalten. Darüber hinaus können Sie über eine Zapier Integration zusätzliche Workflows auf der Grundlage von SalesWings Daten zur Lead-Qualifizierung erstellen.

![Beispiel einer Verkaufsmeldung über den Slack-Kanal]({% image_buster /assets/img/saleswings/smart_watch_alerts.png %})

_Beispiel einer Verkaufsmeldung über einen Slack-Kanal_
{% endtab %}
{% tab Berichterstattung in Salesforce CRM %}
Durch die Integration von SalesWings in Salesforce können Sie automatisierte Berichte mit Leads, Kontakten, Konten und Opportunities auf der Grundlage von Internet-Engagement-Daten und Braze-Kampagnen-Engagement erstellen. So können Sie z. B. eine Liste mit heißen Leads an ein Vertriebsteam weiterleiten, in der alle Personen aufgeführt sind, die auf eine bestimmte E-Mail Kampagne geklickt oder eine bestimmte Aktion in Ihrer Instanz oder Website ausgeführt haben.

![Beispiel für ein Dashboard, das mit dem E-Mail- und Marketing-Engagement von Braze in Salesforce verknüpft ist und die Auswirkungen der Kampagnen von Braze auf die Verkaufsergebnisse und -erfolge untersucht]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Ein Beispiel für ein Dashboard, das mit dem E-Mail- und Marketing-Engagement von Braze in Salesforce verknüpft ist und die Auswirkungen der Kampagnen von Braze auf die Verkaufsergebnisse und -erfolge untersucht._
{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: SalesWings Konto und Konfiguration

[Vereinbaren Sie einen Zeitplan für eine Demo][4] mit dem freundlichen SalesWings Team, um mehr über SalesWings zu erfahren.

### Schritt 2: Installieren Sie Behavioral Tracking auf Ihrer Website oder App

Derzeit haben Sie zwei Möglichkeiten, in SalesWings Verhaltensdaten für Lead Scoring und Insights zu sammeln:
* [Setzen Sie das SalesWings Tracking JavaScript ein][5] auf den Websites und Apps, auf denen Sie Leads verfolgen und identifizieren möchten.
* Senden Sie verhaltensbezogene Lead-Aktivitätsdaten (und Lead-Profil-Daten) über die SalesWings Integration mit Segment.com

### Schritt 3: Verbindung zwischen SalesWings und Braze

Gehen Sie zur [Seite**SalesWings Einstellungen**][6] und erweitern Sie den Abschnitt **Braze Integration**.

![Der Abschnitt Braze Integration auf der Seite SalesWings Einstellungen.][7]

Kopieren Sie den Wert der Spalte **Bezeichner** für den neu erstellten Schlüssel und fügen Sie ihn in das Feld **Braze API-Schlüssel** im Abschnitt SalesWings **Braze Integration** ein.

Fügen Sie Ihren Braze API-Endpunkt hinzu, wie im Artikel [API- und SDK-Endpunkte][8] beschrieben, und geben Sie ihn in das Feld **Braze API-Endpunkt** ein. Kopieren Sie den Wert der Spalte **REST Endpunkt** und geben Sie ihn in das Feld **Braze API Endpunkt** im Abschnitt SalesWings **Braze Integration** ein.

Klicken Sie dann in den SalesWings-Einstellungen auf **Änderungen speichern**.

### Schritt 4: Konfigurieren von SalesWings Lead Scoring für Braze, CRM Integration und mehr

Wenden Sie sich an das Team der Serviceleistungen von SalesWings, das Sie beim Onboarding über die [Website][1] unterstützt.

## Verwendung dieser Integration 

Um das Lead Scoring und die Erstellung von Insights zu triggern, muss SalesWings einen Nutzer:innen auf Ihrer Website oder App identifizieren. Dies kann auf die folgenden Arten geschehen:

- **Formular einreichen:** Wenn ein Nutzer ein Internet-Formular abschickt, identifiziert SalesWings automatisch alle Ihre Web-Formulartypen (wie Anmeldung, Download, Kontakt usw.) und löst die Identität eines Nutzers:innen auf, wenn er ein Formular abschickt. 
- **URL-Klicks mit einer Braze ID oder externen ID:** Ein Nutzer:innen klickt auf eine Marketing-Aktion von Braze, typischerweise auf eine E-Mail, ein Banner oder ähnliches, was zu einer Seite führt, die Sie mit SalesWings tracken.
- **Tracking von E-Mails über Gmail- und Outlook-Plugins (optional):** Wenn Sie Ihre Vertretung mit E-Mail-Tracking-Plugins ausstatten, können diese das vollständige Website Tracking der Nutzer:innen triggern, indem sie trackbare Links versenden.
- **Segment.com Bezeichner des Ereignisses (optional):** Als Nutzer:innen von Segment.com können Sie die Identität eines Nutzers:innen auch über die Integration von Segment.com auflösen.

### Identifizierung von Nutzer:innen anhand von URL-Klicks

Sie können Nutzer:innen automatisch identifizieren, wenn sie auf eine trackbare URL klicken (z.B. E-Mail-Blasts, Banner mit URLs). Um eine URL verfolgbar zu machen, gibt es zwei Möglichkeiten, Ihre Website-URLs in Ihren E-Mails, Bannern oder SMS zu ändern, indem Sie den Parameter und die ID am Ende Ihrer Links hinzufügen.

1. Anhängen von `?braze_id=` gefolgt von {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Beispiel für einen Link:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Anhängen von `?br_user_id=` gefolgt von {% raw %}`{{${user_id}}}`{% endraw %}
  - **Beispiel für einen Link:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

Die Variable `braze_id` wird auf einen von Braze erzeugten Bezeichner der Nutzer:innen gesetzt und ist immer verfügbar. Die Variable `br_user_id` wird auf den Bezeichner des Nutzers in Ihrem System gesetzt und kann in bestimmten Szenarien fehlen (z.B. bei anonymen Nutzer:innen, die mit dem Braze SDK erstellt wurden). Wenn sowohl `braze_id` als auch `br_user_id` in einem Link verwendet werden, wird SalesWings nur den Parameter `braze_id` berücksichtigen.

Für die Konfiguration und weitere Fehlerbehebungen beim Onboarding Support wenden Sie sich bitte an das [SalesWings Team für Serviceleistungen][1].


[1]: https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.saleswingsapp.com/braze-lead-scoring-and-sales-insights?utm_source=braze&utm_campaign=technicaldocs
[4]: https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs
[5]: https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script
[6]: https://helium.saleswings.pro/settings
[7]: {% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %}
[8]: {{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints
