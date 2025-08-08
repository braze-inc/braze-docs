---
nav_title: "OfferFit"
article_title: OfferFit
alias: /partners/offerfit/
description: "OfferFit ersetzt manuelle A/B-Tests durch KI-Tests. Marketer im Lebenszyklus nutzen die KI-Tests von OfferFit, um die beste 1:1-Entscheidung für jede Kund:in zu treffen, alle Variablen gleichzeitig zu testen und Marktveränderungen zu erkennen und sich an sie anzupassen."
page_type: partner
search_tag: OfferFit

---


# OfferFit

> [OfferFit](https://www.offerfit.ai/) ersetzt manuelle A/B-Tests durch KI-Tests. Marketer im Lebenszyklus nutzen die KI-Tests von OfferFit, um die beste 1:1-Entscheidung für jede Kund:in zu treffen, alle Variablen gleichzeitig zu testen und Marktveränderungen zu erkennen und sich an sie anzupassen.

_Diese Integration wird von OfferFit gepflegt._

## Über die Integration

Die Integration von OfferFit und Braze ermöglicht es Ihnen, auf der Grundlage Ihrer Kundendaten automatisch die richtige Nachricht, den richtigen Kanal und das richtige Timing für jeden Kunden zu finden. Sie können Ihre Kampagnen auf bereits identifizierte Kund:in mit Geschäftszielen wie Cross-Sell, Upsell, Wiederkauf, Bindung, Erneuerung, Empfehlung und Winback optimieren.

## Voraussetzungen

| Anforderung | Beschreibung                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OfferFit Lizenz | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie eine aktive OfferFit-Lizenz.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen: {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>users.track</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.email.create</code></li><li><code>templates.email.update</code></li><li><code>templates.email.info</code></li><li><code>templates.email.list</code></li></ul>{:/} Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST API Endpunkt | [Ihre REST API Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Braze REST API Endpunkte

Ihre OfferFit-Lizenz und Ihr Anwendungsfall bestimmen die Endpunkte der Braze REST API, die Sie verwenden. Im Folgenden finden Sie verschiedene API Endpunkte, die Sie verwenden können.

| Braze REST API Endpunkt | OfferFit Verwendung |
|--------------|----------------|
| [POST /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | Rufen Sie die Liste der Kund:in ab, die von einer Kampagne oder einem Canvas angesprochen werden sollen. Da OfferFit keine PII-Daten akzeptiert, wird das Attribut `fields_to_export` nur dazu verwendet, die mit den Nutzer:innen der Plattform vereinbarten Datenattribute abzurufen. |
| [POST /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | Rufen Sie alle Nutzer:innen ab, die zu einem bestimmten Segment gehören. Da OfferFit keine PII-Daten akzeptiert, wird das Attribut `fields_to_export` nur dazu verwendet, die mit dem Nutzer:innen der Plattform vereinbarten Nicht-PII-Felder abzurufen. |
| [POST /benutzer:innen/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | Mit diesem Endpunkt kann OfferFit Nutzerprofile mit angepassten Datenattributen aktualisieren, die zur Personalisierung von Nachrichten verwendet werden können.                                                                                                                                            |
| [POST /nachrichten/senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | Triggern Sie eine API-Kampagne in Braze. |
| [POST /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | Triggern Sie einen Versand für eine Kampagne, die für eine API-gesteuerte Zustellung konfiguriert ist. |
| [GET /kampagnen/liste]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Rufen Sie die Liste aller in Braze konfigurierten Kampagnen und der zugehörigen Metadaten ab. |
| [GET /campaigns/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | Rufen Sie die Analytics-Daten einer bestimmten Kampagne von Braze ab. |
| [GET /kampagnen/details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | Rufen Sie die Details einer bestimmten Kampagne von Braze ab. |
| [POST /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | Triggern Sie einen Versand für ein Canvas, das für eine API-gesteuerte Zustellung konfiguriert ist. |
| [GET /canvas/list]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Rufen Sie die Liste aller in Braze konfigurierten Canvase und der zugehörigen Metadaten ab. |
| [GET /canvas/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | Rufen Sie die Analytics-Daten eines bestimmten Canvas ab. |
| [GET /canvas/details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | Rufen Sie die Details zu einem bestimmten Canvas ab. |
| [GET /segments/list]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Rufen Sie die Liste aller in Braze konfigurierten Segmente und der zugehörigen Metadaten ab. |
| [GET /segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Rufen Sie die Größe des Braze Segments ab. |
| [GET /segmente/details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | Rufen Sie die Details eines bestimmten Braze Segments ab. |
| [POST /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | Erstellen Sie ein neues Braze HTML Template für E-Mails. |
| [POST /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | Aktualisieren Sie ein bestehendes Braze HTML E-Mail Template. |
| [GET /templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Rufen Sie die Details einer bestimmten Braze HTML-E-Mail-Vorlage ab. |
| [GET /templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Rufen Sie die Liste aller in Braze konfigurierten HTML-E-Mail-Templates sowie deren `subject line` und `HTML content` ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Nachdem Sie [OfferFit integriert haben](#integration), können Sie den Experimentierprozess wie folgt automatisieren:

1. Wählen Sie eine **Metrik** aus, die Sie maximieren möchten, z.B. Umsatz, Konversionen, ARPU oder eine andere Metrik.
KPI, die Sie anhand Ihrer Kundendaten messen können. Dies ist die Metrik, die OfferFit mit seiner KI zu maximieren versuchen wird.
2. Wählen Sie die **Dimensionen** aus, die Sie testen möchten (z. B. Angebot, Betreffzeile, Motiv, Kanal, Uhrzeit, Tag, Häufigkeit usw.).
3. Wählen Sie die verfügbaren **Optionen** für jede Dimension aus. Sie könnten zum Beispiel E-Mail, SMS und Push für die Dimension Kanal auswählen und dann täglich, zweimal pro Woche und wöchentlich für die Dimension Häufigkeit auswählen.

![of_use_case_example][2]


Nachdem der Experimentierprozess automatisiert wurde, beginnt OfferFit damit, täglich Empfehlungen für jede Kund:in auszusprechen, mit dem Ziel, die gewählte Erfolgsmetrik zu maximieren. 

Die OfferFit KI lernt aus jeder Kundeninteraktion und wendet diese Insights auf die Empfehlungen des nächsten Tages an.


| Anwendungsfall | Ziel | Vorherige Annäherung | OfferFit-Ansatz |
|----------|------|----------------|-------------------|
| **Cross-Sell oder Upsell** | Maximieren Sie den durchschnittlichen Umsatz pro Nutzer:innen (ARPU) aus Internet-Abos. | Führen Sie jährliche Kampagnen durch, in denen Sie jeder Kund:in den nächsthöheren Tarif anbieten. | Finden Sie empirisch heraus, welche Nachricht, welcher Versandzeitpunkt, welcher Rabatt und welcher Plan für jeden Kunden am besten geeignet sind. Erfahren Sie, welche Kund:innen für Leapfrog-Angebote empfänglich sind und welche Kunden Rabatte oder andere Anreize für ein Upgrade benötigen. |
| **Erneuerung & Bindung** | Sichern Sie sich Vertragsverlängerungen und maximieren Sie sowohl die Vertragsdauer als auch den Kapitalwert (NPV). | Führen Sie manuelle A/B-Tests durch und bieten Sie erhebliche Preisnachlässe an, um Verlängerungen zu sichern. | Nutzen Sie automatisierte Experimente, um das beste Verlängerungsangebot für jeden Kunden zu finden und Kunden zu identifizieren, die weniger preisempfindlich sind und weniger starke Rabatte für eine Verlängerung benötigen. |
| **Wiederholter Kauf** | Maximieren Sie die Kauf- und Rückkaufsraten. | Alle Kund:innen erhalten nach der Erstellung eines Website-Kontos die gleiche Reise (z.B. die gleiche E-Mail-Sequenz mit der gleichen Kadenz). | Automatisieren Sie das Experimentieren, um den besten Artikel für jede Kund:in zu finden, sowie die effektivste Betreffzeile, den Sendezeitpunkt und die Häufigkeit der Kommunikation. |
| **Winback** | Erhöhen Sie die Reaktivierung, indem Sie frühere Abonnent:innen zu einem erneuten Abonnement ermutigen. | Ausgefeilte A/B-Tests und Segmentierung. | Nutzen Sie die Automatisierung von Experimenten, um Tausende von Variablen auf einmal zu testen und die beste Kreativität, Nachricht, Kanal und Kadenz für jeden Einzelnen zu entdecken. |
| **Empfehlung** | Maximieren Sie die Zahl der durch Empfehlungen bestehender Kund:innen eröffneten Konten. | Feste E-Mail-Sequenz für alle Kund:innen, mit umfangreichen A/B-Tests, um die besten Sendezeiten, Kadenz usw. für die Kundenpopulation zu ermitteln. | Automatisieren Sie das Experimentieren, um die ideale E-Mail, das Kreativmaterial, den Versandzeitpunkt und die Kreditkarte für bestimmte Kund:innen zu ermitteln. |
| **Lead Nurturing & Konversion** | Erhöhen Sie Ihren Umsatz und zahlen Sie für jede Kund:in den richtigen Betrag. | Da sich die Richtlinien zum Datenschutz bei Facebook und anderen Plattformen ändern, sind frühere Ansätze für personalisierte bezahlte Anzeigen nicht mehr wirksam. | Nutzen Sie robuste First-Party-Daten, um automatisch mit Kundensegmenten, Gebotsmethodik, Gebotsstufen und kreativen Elementen zu experimentieren. |
| **Loyalität & Engagement** | Maximieren Sie die Käufe neuer Kunden im Kundenbindungs-Programm. | Kunden:in erhalten eine feste Abfolge von E-Mails als Antwort auf ihre Aktionen. Zum Beispiel erhalten alle neuen Teilnehmer des Kundenbindungs-Programms die gleiche Reise. | Experimentieren Sie automatisch mit verschiedenen E-Mail-Angeboten, kreativen Elementen, Sendezeitpunkt und -häufigkeit, um die Kauf- und Wiederkaufrate für jede Kund:in zu maximieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Integration

### Schritt 1: Definieren Sie die Zielgruppe in Braze

Definieren Sie Ihre Zielgruppe, indem Sie mindestens ein Segment in Braze erstellen. Dieses Segment wird verwendet, um Ihre Kampagne oder Ihr Canvas an die richtigen Nutzer:innen zu senden.

### Schritt 2: Konfigurieren Sie eine API-getriggerte Braze-Kampagne oder ein Braze-Canvas und erstellen Sie Kampagnen-Assets (z.B. HTML-Templates, Bilder) {#step-2}

1. Erstellen Sie eine Kampagne oder ein Canvas in Braze. OfferFit nutzt diese Kampagne oder das Canvas, um 1:1 personalisierte Aktivierungsereignisse an die richtigen Nutzer:innen aus Ihrer definierten Zielgruppe zu senden. 
2. Nehmen Sie keine [Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) von Braze in Ihre Kampagne oder Ihr Canvas auf. Dadurch ist es zulässig, dass die Kontrollgruppe von OfferFit die einzige aktive Gruppe ist.
3. Abhängig von Ihren Dimensionen können Sie Liquid-Tags in Ihren kreativen Inhalten konfigurieren, um Ihre Kampagne oder Ihr Canvas dynamisch mit OfferFit-Empfehlungen aufzufüllen. OfferFit wird über die Braze API kundenspezifische Inhalte an die Liquid-Tags in Ihren Templates weitergeben.

### Schritt 3: Aktualisieren Sie Ihre OfferFit-Anwendungsfallkonfiguration, um Braze-Aktivierungsereignisse zu orchestrieren

Sie können die Integration der nativen Aktivierung von OfferFit mit Braze nutzen, um 1:1 personalisierte Empfehlungen für Ihre Zielgruppe zu orchestrieren und zu planen.

## Anpassung

Zusätzlich zur Orchestrierung von Aktivierungs-Events in Braze bietet OfferFit Datenintegrationsfunktionen, mit denen Sie über die verfügbaren API-Endpunkte Kundenprofile (ohne PII) und Engagement-Daten aus Braze abrufen können.

## Verwendung dieser Integration

Nachdem OfferFit konfiguriert wurde, sendet die automatisierte Experimentierplattform automatisch 1:1 personalisierte Aktivierungsereignisse für jeden Nutzer:innen Ihrer Zielgruppe an Braze. Diese Aktivierungsereignisse werden durch die Braze Kampagnen oder Canvase ausgelöst, die Sie in [Schritt 2](#step-2) konfiguriert haben.

Zusätzlich zu den in Braze verfügbaren Analytics-Daten bietet OfferFit eine umfassende Berichtsebene, die es Marketern erlaubt, die von OfferFit durch seine selbstlernenden KI-Fähigkeiten entdeckten Insights der Kunden zu untersuchen.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}

