---
nav_title: "AngebotFit"
article_title: AngebotFit
alias: /partners/offerfit/
description: "OfferFit ersetzt das manuelle A/B-Testing durch KI-Tests. Lifecycle-Vermarkter nutzen die KI-Tests von OfferFit, um die beste 1:1-Entscheidung für jeden Kunden zu treffen, alle Variablen gleichzeitig zu testen und Marktveränderungen zu erkennen und sich an sie anzupassen."
page_type: partner
search_tag: OfferFit

---


# AngebotFit

> [OfferFit](https://www.offerfit.ai/) ersetzt das manuelle A/B-Testing durch KI-Tests. Lifecycle-Vermarkter nutzen die KI-Tests von OfferFit, um die beste 1:1-Entscheidung für jeden Kunden zu treffen, alle Variablen gleichzeitig zu testen und Marktveränderungen zu erkennen und sich an sie anzupassen.

Die Integration von OfferFit und Braze ermöglicht es Ihnen, auf der Grundlage Ihrer Kundendaten automatisch die richtige Botschaft, den richtigen Kanal und das richtige Timing für jeden Kunden zu finden. Sie können Ihre Kampagnen für bereits identifizierte Kunden mit Geschäftszielen wie Cross-Selling, Upselling, Wiederkauf, Bindung, Erneuerung, Weiterempfehlung und Rückgewinnung optimieren.

## Voraussetzungen

| Anforderung | Beschreibung |
|-------------|-------------|
| OfferFit Lizenz | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie eine aktive OfferFit-Lizenz. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit den folgenden Berechtigungen: {::nomarkdown}<ul><li><code>users.export.ids</code></li><li><code>users.export.segment</code></li><li><code>messages.send</code></li><li><code>campaigns.trigger.send</code></li> <li><code>campaigns.list</code></li><li><code>campaigns.data_series</code></li><li><code>campaigns.details</code></li><li><code>canvas.trigger.send</code></li><li><code>canvas.list</code></li><li><code>canvas.data_series</code></li><li><code>canvas.details</code></li><li><code>segments.list</code></li><li><code>segments.data_series</code></li><li><code>segments.details</code></li><li><code>templates.create</code></li><li><code>templates.update</code></li><li><code>templates.info</code></li><li><code>templates.list</code></li></ul>{:/} Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST API Endpunkt | [Ihre REST-API-Endpunkt-URL][1]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, können Sie einen API-Schlüssel unter **Entwicklerkonsole** > **API-Einstellungen** erstellen.
{% endalert %}

### Braze REST API Endpunkte

Ihre OfferFit-Lizenz und Ihr Anwendungsfall bestimmen die REST-API-Endpunkte von Braze, die Sie verwenden. Im Folgenden finden Sie verschiedene API-Endpunkte, die Sie verwenden können.

| Braze REST API Endpunkt | OfferFit Verwendung |
|--------------|----------------|
| [POST /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)                          | Rufen Sie die Liste der Kunden ab, an die sich eine Kampagne oder ein Canvas richten soll. Da OfferFit keine PII-Daten akzeptiert, wird das Attribut `fields_to_export` nur verwendet, um die mit dem Plattformbenutzer vereinbarten Datenattribute abzurufen. |
| [POST /users/export/segment]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)                         | Rufen Sie alle Benutzer ab, die zu einem bestimmten Segment gehören. Da OfferFit keine PII-Daten akzeptiert, wird das Attribut `fields_to_export` verwendet, um nur die Nicht-PII-Felder abzurufen, die mit dem Plattformbenutzer vereinbart wurden. |
| [POST /benutzer/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)                                            | OfferFit kann diesen Endpunkt verwenden, um Benutzerprofile mit benutzerdefinierten Datenattributen zu aktualisieren, die zur Personalisierung von Nachrichten verwendet werden können.                                                                                                                                            |
| [POST /nachrichten/senden]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)                         | Lösen Sie eine API-Kampagne in Braze aus. |
| [POST /campaigns/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/)     | Lösen Sie einen Versand für eine Kampagne aus, die für die API-gesteuerte Zustellung konfiguriert ist. |
| [GET /Kampagnen/Liste]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaigns/)                                     | Rufen Sie die Liste aller in Braze konfigurierten Kampagnen und der zugehörigen Metadaten ab. |
| [GET /campaigns/data_series]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_analytics/)                     | Rufen Sie die Analysedaten einer bestimmten Braze-Kampagne ab. |
| [GET /Kampagnen/Details]({{site.baseurl}}/api/endpoints/export/campaigns/get_campaign_details/)                           | Rufen Sie die Details einer bestimmten Braze-Kampagne ab. |
| [POST /canvas/trigger/send]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)         | Lösen Sie einen Sendevorgang für ein Canvas aus, das für die API-gesteuerte Zustellung konfiguriert ist. |
| [GET /Leinwand/Liste]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/)                                            | Rufen Sie die Liste aller in Braze konfigurierten Leinwände und die zugehörigen Metadaten ab. |
| [GET /canvas/data_series]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics/)                             | Rufen Sie die Analysedaten eines bestimmten Canvas ab. |
| [GET /Leinwand/Details]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_details/)                                   | Rufen Sie die Details zu einem bestimmten Canvas ab. |
| [GET /Segmente/Liste]({{site.baseurl}}/api/endpoints/export/segments/get_segment/)                                        | Rufen Sie die Liste aller in Braze konfigurierten Segmente und der zugehörigen Metadaten ab. |
| [GET /segments/data_series]({{site.baseurl}}/api/endpoints/export/segments/get_segment_analytics/)                        | Rufen Sie die Größe des Lotsegments ab. |
| [GET /Segmente/Details]({{site.baseurl}}/api/endpoints/export/segments/get_segment_details/)                              | Rufen Sie die Details zu einem bestimmten Braze-Segment ab. |
| [POST /templates/email/create]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)      | Erstellen Sie eine neue Braze HTML-E-Mail-Vorlage. |
| [POST /templates/email/update]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/)      | Aktualisieren Sie eine vorhandene Braze HTML-E-Mail-Vorlage. |
| [GET /templates/email/info]({{site.baseurl}}/api/endpoints/templates/email_templates/get_see_email_template_information/) | Rufen Sie die Details einer bestimmten HTML-E-Mail-Vorlage von Braze ab. |
| [GET /templates/email/list]({{site.baseurl}}/api/endpoints/templates/email_templates/get_list_email_templates/)           | Rufen Sie die Liste aller in Braze konfigurierten HTML-E-Mail-Vorlagen sowie deren `subject line` und `HTML content` ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Nachdem Sie [OfferFit integriert haben](#integration), können Sie den Experimentierprozess automatisieren, indem Sie Folgendes tun:

1. Wählen Sie eine **Erfolgskennzahl** aus, die Sie maximieren möchten, z. B. Umsatz, Konversionen, ARPU oder eine andere
KPI, die Sie anhand Ihrer Kundendaten messen können. Dies ist die Metrik, die OfferFit mit seiner KI zu maximieren versucht.
2. Wählen Sie die **Dimensionen** aus, die Sie testen möchten (z. B. Angebot, Betreffzeile, Motiv, Kanal, Uhrzeit, Tag, Häufigkeit usw.).
3. Wählen Sie die verfügbaren **Optionen** für jede Dimension. Sie könnten zum Beispiel E-Mail, SMS und Push für die Dimension Kanal auswählen und dann täglich, zweimal pro Woche und wöchentlich für die Dimension Häufigkeit.

![of_use_case_example][2]


Nachdem der Experimentierprozess automatisiert wurde, beginnt OfferFit damit, täglich Empfehlungen für jeden Kunden auszusprechen mit dem Ziel, die gewählte Erfolgsmetrik zu maximieren. 

Die OfferFit-KI lernt aus jeder Kundeninteraktion und wendet diese Erkenntnisse auf die Empfehlungen des nächsten Tages an.


| Anwendungsfall | Ziel | Vorherige Annäherung | OfferFit-Ansatz |
|----------|------|----------------|-------------------|
| **Cross-Sell oder Upsell** | Maximieren Sie den durchschnittlichen Umsatz pro Nutzer (ARPU) aus Internet-Abonnements. | Führen Sie jährliche Kampagnen durch, in denen Sie jedem Kunden den nächsthöheren Tarif anbieten. | Ermitteln Sie empirisch die beste Nachricht, den besten Versandzeitpunkt, den besten Rabatt und den besten Plan für jeden Kunden. Erfahren Sie, welche Kunden für Leapfrog-Angebote empfänglich sind und welche Kunden Rabatte oder andere Anreize für ein Upgrade benötigen. |
| **Erneuerung & Beibehaltung** | Sichern Sie sich Vertragsverlängerungen und maximieren Sie sowohl die Vertragsdauer als auch den Kapitalwert (NPV). | Führen Sie manuelle A/B-Tests durch und bieten Sie erhebliche Preisnachlässe an, um Verlängerungen zu sichern. | Nutzen Sie automatisierte Experimente, um das beste Verlängerungsangebot für jeden Kunden zu finden und Kunden zu identifizieren, die weniger preisempfindlich sind und weniger starke Rabatte für eine Verlängerung benötigen. |
| **Wiederholter Kauf** | Maximieren Sie die Kauf- und Rückkaufsraten. | Alle Kunden erhalten die gleiche Reise, nachdem sie ein Website-Konto erstellt haben (z. B. die gleiche E-Mail-Sequenz mit der gleichen Kadenz). | Automatisieren Sie das Experimentieren, um den besten Menüpunkt für jeden Kunden zu finden, sowie die effektivste Betreffzeile, den Sendezeitpunkt und die Häufigkeit der Kommunikation. |
| **Winback** | Erhöhen Sie die Reaktivierung, indem Sie frühere Abonnenten dazu ermutigen, sich erneut anzumelden. | Ausgefeilte A/B-Tests und Segmentierung. | Nutzen Sie automatisierte Experimente, um Tausende von Variablen auf einmal zu testen und so die beste Werbung, Botschaft, den besten Kanal und die beste Kadenz für jeden Einzelnen zu finden. |
| **Empfehlung** | Maximieren Sie die Anzahl der neuen Konten, die durch Empfehlungen bestehender Kunden für Geschäftskreditkarten eröffnet werden. | Feste E-Mail-Sequenz für alle Kunden, mit umfangreichen A/B-Tests, um die besten Sendezeiten, Kadenz usw. für die Kundenpopulation zu ermitteln. | Automatisieren Sie das Experimentieren, um die ideale E-Mail, das Motiv, den Versandzeitpunkt und die Kreditkarte für bestimmte Kunden zu ermitteln. |
| **Lead Nurturing & Konvertierung** | Erhöhen Sie Ihren Umsatz und zahlen Sie den richtigen Betrag für jeden Kunden. | Da sich die Datenschutzrichtlinien bei Facebook und anderen Plattformen ändern, sind frühere Ansätze für personalisierte bezahlte Anzeigen nicht mehr wirksam. | Nutzen Sie robuste First-Party-Daten, um automatisch mit Kundensegmenten, Gebotsmethodik, Gebotsstufen und kreativen Elementen zu experimentieren. |
| **Loyalität & Engagement** | Maximieren Sie die Käufe von Neukunden im Kundenbindungsprogramm. | Kunden erhielten eine festgelegte Abfolge von E-Mails als Reaktion auf ihre Aktionen. Zum Beispiel erhalten alle neuen Teilnehmer des Treueprogramms die gleiche Reise. | Experimentieren Sie automatisch mit verschiedenen E-Mail-Angeboten, kreativen Elementen, Sendezeitpunkt und -häufigkeit, um die Kauf- und Wiederkaufrate für jeden Kunden zu maximieren. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## Integration

### Schritt 1: Definieren Sie Ihre Zielgruppe in Braze

Definieren Sie Ihr Zielpublikum, indem Sie mindestens ein Segment in Braze erstellen. Dieses Segment wird verwendet, um Ihre Kampagne oder Ihr Canvas an die richtigen Nutzer zu senden.

### Schritt 2: Konfigurieren Sie eine API-ausgelöste Braze-Kampagne oder Canvas und erstellen Sie Kampagnen-Assets (z.B. HTML-Vorlagen, Bilder) {#step-2}

1. Erstellen Sie eine Kampagne oder ein Canvas in Braze. OfferFit wird diese Kampagne oder dieses Canvas verwenden, um 1:1 personalisierte Aktivierungsereignisse an die richtigen Nutzer aus Ihrer definierten Zielgruppe zu senden. 
2. Nehmen Sie keine [Braze-Kontrollgruppe]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign#including-a-control-group) in Ihre Kampagne oder Ihr Canvas auf. Dadurch kann die OfferFit-Kontrollgruppe die einzige aktive Gruppe sein.
3. Abhängig von Ihren Dimensionen können Sie Liquid-Tags in Ihren kreativen Inhalten konfigurieren, um Ihre Kampagne oder Ihr Canvas dynamisch mit OfferFit-Empfehlungen zu bestücken. OfferFit übergibt kundenspezifische Inhalte über die Braze API an die Liquid-Tags in Ihren Vorlagen.

### Schritt 3: Aktualisieren Sie Ihre OfferFit Anwendungsfallkonfiguration, um Braze-Aktivierungsereignisse zu orchestrieren

Sie können die native Aktivierungsintegration von OfferFit mit Braze nutzen, um 1:1 personalisierte Empfehlungen für Ihre Zielgruppe zu orchestrieren und zu planen.

## Anpassung

Zusätzlich zur Orchestrierung von Aktivierungsereignissen in Braze bietet OfferFit Datenintegrationsfunktionen, die es Ihnen ermöglichen, über die verfügbaren API-Endpunkte Kundenprofile (Nicht-PII) und Engagement-Daten aus Braze abzurufen.

## Mit dieser Integration

Nachdem OfferFit konfiguriert wurde, sendet die automatisierte Experimentierplattform automatisch 1:1 personalisierte Aktivierungsereignisse für jeden Nutzer in Ihrer Zielgruppe an Braze. Diese Aktivierungsereignisse werden durch die Braze-Kampagnen oder Canvases ausgelöst, die Sie in [Schritt 2](#step-2) konfiguriert haben.

Zusätzlich zu den in Braze verfügbaren Analysedaten bietet OfferFit eine umfassende Berichtsebene, die es Marketingfachleuten ermöglicht, die von OfferFit durch seine selbstlernenden KI-Fähigkeiten gewonnenen Kundeneinblicke zu erkunden.




[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/offerfit/of_use_case_example.png %}

