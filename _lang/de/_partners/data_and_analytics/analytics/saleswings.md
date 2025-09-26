---
nav_title: SalesWings
article_title: SalesWings
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und SalesWings, einer Lösung für den Vertrieb und das Marketing von Braze, die Sie bei der Qualifizierung von Leads und Konten unterstützt, Insights und Warnmeldungen für den Vertrieb innerhalb von CRM wie Salesforce sowie B2B-Attributionsberichte liefert."
alias: /partners/saleswings/
page_type: partner
search_tag: Partner

---

# SalesWings

> [SalesWings](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) ist eine B2B SaaS Lösung für Vertrieb und Operator, die die Lead- und Account-Qualifizierung durch ganzheitliches Lead-Scoring und -Grading unterstützt, Insights und Warnmeldungen für den Vertrieb liefert, B2B-Attribution-Berichte erstellt und eine enge Integration mit Salesforce CRM bietet.

_Diese Integration wird von SalesWings gepflegt._

## Über die Integration

SalesWings erlaubt es Marketing Teams und Marketing Operations Managern, Leads und Accounts für ihre Vertriebsteams zu qualifizieren, was für die Ausrichtung von Vertrieb und Marketing und die operative Effizienz unerlässlich ist. Darüber hinaus kann SalesWings zusammen mit Braze den Vertriebsmitarbeitern die vollständige Customer Journey eines Leads und eines Kontos sowie Daten über das Engagement der Braze-Kampagnen anzeigen, was es Ihnen erlaubt, die Lead-Qualifizierungsraten durch fundiertere Gespräche zu erhöhen. SalesWings identifiziert Bedürfnisse und Interessen zusammen mit anderen Signalen, was es zulässig macht, qualifizierte Käufer auf automatisierte Weise an Vertriebsteams in Ihrem CRM weiterzuleiten.

## Voraussetzungen
 
| Anforderung | Beschreibung |
| ----------- | ----------- |
| SalesWings Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [SalesWings-Konto](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs). |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit `users.export.ids` Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| Segment.com Konto (optional) | Wenn Sie Nutzer:innen von Segment.com sind, können Sie alle Daten zum Engagement und Profil von Leads sowie zur Identifizierung von Ereignissen an Segment.com senden, um ein Lead-Profil zu erstellen. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

{% tabs %}
{% tab Lead- und Kontoscoring %}

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
Durch die native SalesWings-Integration mit Salesforce können Sie automatisierte Berichte mit Leads, Kontakten, Konten und Opportunities auf der Grundlage von Internet-Engagement-Daten und jeglichem Engagement von Braze-Kampagnen mit einer nativen Currents-Integration erstellen. So können Sie z.B. eine Liste von Hot Leads an ein Vertriebsteam weiterleiten, in der alle Personen aufgeführt sind, die auf eine bestimmte Kampagne per E-Mail geklickt oder eine bestimmte Aktion in Ihrer App oder auf Ihrer Website ausgeführt haben.

![Beispiel für ein Dashboard, das mit dem E-Mail- und Marketing-Engagement von Braze in Salesforce verknüpft ist und die Auswirkungen der Kampagnen von Braze auf die Verkaufsergebnisse und -erfolge untersucht]({% image_buster /assets/img/saleswings/saleswings_email_campaign_attribution_dashboard.png %})

_Ein Beispiel für ein Dashboard, das mit dem E-Mail- und Marketing-Engagement von Braze in Salesforce verknüpft ist und die Auswirkungen der Kampagnen von Braze auf die Verkaufsergebnisse und -erfolge untersucht._
{% endtab %}
{% endtabs %}

## Integration

### Schritt 1: SalesWings Konto und Konfiguration

[Vereinbaren Sie einen Zeitplan für eine Demo](https://www.saleswingsapp.com/schedule-a-demo?utm_source=braze&utm_campaign=technicaldocs) mit dem freundlichen SalesWings Team, um mehr über SalesWings zu erfahren.

### Schritt 2: Installieren Sie Behavioral Tracking auf Ihrer Website oder App

Es gibt mehrere Möglichkeiten, in SalesWings Verhaltensdaten für das Lead- und Account-Scoring, die Identifizierung der Absicht des Käufers und für Insights zu sammeln:
* [Setzen Sie das SalesWings Tracking JavaScript ein](https://support.saleswingsapp.com/en/collections/3285135-1-implementing-saleswings-tracking-script) auf den Websites und Apps, auf denen Sie Leads verfolgen und identifizieren möchten.
* Nehmen Sie Braze-Ereignisse zusammen mit Event-Eigenschaften über Braze-Currents in SalesWings auf.
* Senden Sie verhaltensbezogene Lead-Aktivitätsdaten (und Lead-Profil-Daten) über die [SalesWings Integration mit Segment](https://support.saleswingsapp.com/en/articles/9258905-segment-com-integration)
* Senden Sie Daten direkt von einer Drittanbieter-Lösung an die SalesWings [API](https://support.saleswingsapp.com/en/articles/6930889-using-saleswings-open-api-to-send-events-to-saleswings) 

### Schritt 3: Verbindung zwischen SalesWings und Braze

Gehen Sie auf die [Seite**SalesWings Integrationen**](https://helium.saleswings.pro/integrations) und erweitern Sie den Abschnitt **Braze Integration**.

![Der Abschnitt Braze Integration auf der Seite SalesWings Einstellungen.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_integration_settings.png %})

Kopieren Sie den Wert der Spalte **Bezeichner** für den neu erstellten Schlüssel und fügen Sie ihn in das Feld **Braze API-Schlüssel** im Abschnitt SalesWings **Braze Integration** ein.

Fügen Sie Ihren Braze API-Endpunkt hinzu, wie im Artikel [API- und SDK-Endpunkte]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints) beschrieben, und geben Sie ihn in das Feld **Braze API-Endpunkt** ein. Kopieren Sie den Wert der Spalte **REST Endpunkt** und geben Sie ihn in das Feld **Braze API Endpunkt** im Abschnitt SalesWings **Braze Integration** ein.

Wählen Sie dann **Speichern**.

### Schritt 4: Richten Sie einen angepassten Currents-Export zu SalesWings ein (optional)

Wenn Sie [Nutzerverhalten-]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events) und [Messaging-Ereignisse]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events) für Behavioral Intelligence, Lead- und Account-Scoring, Insights oder Berichte in Ihrem CRM nutzen möchten, gehen Sie auf die [Seite **SalesWings Integrationen**](https://helium.saleswings.pro/integrations) und erweitern Sie den Abschnitt **Braze Integration**.

Wählen Sie **Generieren** unter **Generieren Sie ein API-Token, um einen angepassten Currents Export einzurichten**.

[Erstellen Sie dann einen neuen Current]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents) und wählen Sie als Current-Typ **Custom Currents Export** aus.

Geben Sie im Abschnitt **Zugangsdaten** des Formulars zur Erstellung von Currents das API-Token ein, das Sie auf der [Seite** SalesWings-Integrationen**](https://helium.saleswings.pro/integrations) für **Bearer Token** generiert haben, und `https://helium.saleswings.pro/api/braze/currents/events` für **Endpunkt**.

### Schritt 5: Konfigurieren von SalesWings Lead- und Kontoscoring für Braze, CRM Integration und mehr

Wenden Sie sich an das Team der Serviceleistungen von SalesWings, das Sie beim Onboarding über die [Website](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs) unterstützt.

## Verwendung dieser Integration 

Um die Verknüpfung von Verhaltensdaten und anderen Daten mit Leads und Accounts zu triggern, muss SalesWings einen Nutzer:innen auf Ihrer Website oder App oder durch eine Drittanbieter-Integration identifizieren. Dies kann auf die folgenden Arten geschehen:

- **Formular einreichen:** Wenn ein Nutzer ein Internet-Formular abschickt, identifiziert SalesWings automatisch alle Ihre Web-Formulartypen (wie Anmeldung, Download, Kontakt usw.) und löst die Identität eines Nutzers:innen auf, wenn er ein Formular abschickt. 
- **URL-Klicks mit einer Braze ID oder externen ID:** Ein Nutzer:innen klickt auf eine Marketing-Aktion von Braze, typischerweise auf eine E-Mail, ein Banner oder ähnliches, was zu einer Seite führt, die Sie mit SalesWings tracken.
- **Braze-Currents Ereignisse (optional):** Wenn der Export von Braze-Currents nach SalesWings konfiguriert ist, erstellt SalesWings für jeden Nutzer:innen von Braze ein identifiziertes Profil mit einer E-Mail, in der Events an den Current gesendet werden.
- **Tracking von E-Mails über Gmail- und Outlook-Plugins (optional):** Wenn Sie Ihre Vertretung mit E-Mail-Tracking-Plugins ausstatten, können diese das vollständige Website Tracking der Nutzer:innen triggern, indem sie trackbare Links versenden.
- **Segment.com Bezeichner des Ereignisses (optional):** Als Nutzer:innen von Segment.com können Sie die Identität eines Nutzers:innen auch über die Integration von Segment.com auflösen.

### Identifizierung von Nutzer:innen anhand von URL-Klicks

Sie können Nutzer:innen automatisch identifizieren, wenn sie auf eine trackbare URL klicken (z.B. E-Mail-Blasts, Banner mit URLs). Um eine URL verfolgbar zu machen, gibt es zwei Möglichkeiten, Ihre Website-URLs in Ihren E-Mails, Bannern oder SMS zu ändern, indem Sie den Parameter und die ID am Ende Ihrer Links hinzufügen.

1. Anhängen von `?braze_id=` gefolgt von {% raw %}`{{${braze_id}}}`{% endraw %} 
  - **Beispiel für einen Link:** {% raw %}`https://www.your-website.com?braze_id={{${braze_id}}}`{% endraw %}<br><br>

2. Anhängen von `?br_user_id=` gefolgt von {% raw %}`{{${user_id}}}`{% endraw %}
  - **Beispiel für einen Link:** {% raw %}`https://www.client-website.com?br_user_id={{${user_id}}}`{% endraw %}

Die Variable `braze_id` wird auf einen von Braze erzeugten Bezeichner der Nutzer:innen gesetzt und ist immer verfügbar. Die Variable `br_user_id` wird auf den Bezeichner des Nutzers in Ihrem System gesetzt und kann in bestimmten Szenarien fehlen (z.B. bei anonymen Nutzer:innen, die mit dem Braze SDK erstellt wurden). Wenn sowohl `braze_id` als auch `br_user_id` in einem Link verwendet werden, wird SalesWings nur den Parameter `braze_id` berücksichtigen.

### Verwendung von Braze-Currents Ereignissen in Ihrem CRM

Wenn Sie einen Braze-Currents mit SalesWings verbinden, erstellt SalesWings für jeden Braze-Nutzer identifizierte Lead-Profile mit einer E-Mail und erfasst unterstützte Braze-Ereignisse als Lead-Aktivität. In Ihrem CRM können alle Daten automatisch auf der Kontoebene des Leads aggregiert werden. Die aufgezeichneten Aktivitäten und Daten können mit den Verhaltensdaten, die mit dem Tracking-Skript von SalesWings oder Segment.com erfasst wurden, oder mit anderen Daten, die an die SalesWings API gesendet werden, kombiniert werden, um die Bedürfnisse und die Verkaufsbereitschaft Ihrer potenziellen Kunden für Ihre Lead- und Account-Management-Prozesse zu ermitteln.

Die folgende Tabelle zeigt die von SalesWings unterstützten Braze-Ereignistypen und ihre Darstellung im Verlauf der Lead-Aktivitäten und in der Regelmaschine von SalesWings:

| Ereignis-Kategorie | Event-Typ | Name des Ereignisses in SalesWings |
| ----------- | ----------- | ----------- |
| Canvas-Events | Entrys | `[Nurturing] Added by marketing team onto the journey $canvas_name` |
| Kundenverhalten-Events | Benutzerdefinierte Ereignisse | `[Custom Event tracked] $name` |
| Kundenverhalten-Events | Erste Sitzung | `[User Action] Today marks the user's first session` |
| Kundenverhalten-Events | Install-Attribution | `[User Action] User installed app from $source` |
| Kundenverhalten-Events | Kauf-Events | `[Purchase] Customer purchased $product_id for $price $currency` |
| Nachrichten-Events | Contend-Card-Klick | `[Content Card engagement] Clicked on $campaign_name content card` |
| Nachrichten-Events | E-Mail-Rückläufer (Bounce) | `[Alerting or negative] Email hard-bounced. This person's email appears to be no longer valid` |
| Nachrichten-Events | E-Mail-Klick | `[Email campaign engagement] Clicked in email $campaign_name on $url` |
| Nachrichten-Events | E-Mail-Zustellung | `[Nurturing] Received email $campaign_name` |
| Nachrichten-Events | E-Mail-Öffnung | `[Email campaign engagement] Opened email $campaign_name` |
| Nachrichten-Events | E-Mail-Abmeldung | `[Subscription status change] Unsubscribed from $campaign_name` |
| Nachrichten-Events | In-App-Nachricht-Klick | `[In-app campaign engagement] Clicked on message $campaign_name` |
| Nachrichten-Events | Push-Öffnung | `[Push notification engagement] Clicked on notification $campaign_name` |
| Nachrichten-Events | Eingehende SMS/MMS Empfangen | `[SMS/mobile campaign engagement] We received a message from this person to our internal number $inbound_phone_number: $message_body` |
| Nachrichten-Events | SMS/MMS-Kurzlink-Klick | `[SMS/mobile campaign engagement] Clicked on $short_url` |
| Nachrichten-Events | Eingehende WhatsApp-Nachricht empfangen | `[WhatsApp engagement] We received a message from this person to our WhatsApp number $inbound_phone_number: $message_body` |
| Nachrichten-Events | Gelesen auf WhatsApp | `[WhatsApp engagement] Lead read our message from the $campaign_name campaign` |
| Abos | Globale Abostatus-Änderung | `[Subscription status change] Global marketing subscription setting set to $subscription_status` |
| Abos | Statusänderung der Abo-Gruppe | `[Subscription status change] $subscription_status to/from $campaign_name` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sie können dann die Bedingungen für **Angepasstes Event** > **Event-Name** und **Angepasstes Event** > **Event-Eigenschaft** für SalesWings Tags und Scores anhand der SalesWings Event-Namen aus der obigen Tabelle anpassen. Die Liste der Event-Eigenschaften, die für Bedingungen zur Verfügung stehen, ist mit einigen häufig verwendeten Einträgen vorausgefüllt. Sie können jederzeit neue Eigenschaften im Abschnitt **Event-Eigenschaften** auf der [Konfigurationsseite der Rule Engine](https://helium.saleswings.pro/falcon) hinzufügen.

![Beispiel für eine Bedingung für einen Ereignisnamen.]({% image_buster /assets/img/saleswings/saleswings_braze_lead_scoring_custom_event_condition.png %})

Für die Konfiguration und weitere Fehlerbehebungen beim Onboarding Support wenden Sie sich bitte an das [SalesWings Team für Serviceleistungen](https://www.saleswingsapp.com/?utm_source=braze&utm_campaign=technicaldocs).

