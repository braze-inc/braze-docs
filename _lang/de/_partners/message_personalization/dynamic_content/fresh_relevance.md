---
nav_title: Frische Relevanz
article_title: Frische Relevanz
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Fresh Relevance, einer vielseitigen Personalisierungsplattform, mit der Sie relevante Produkte in Ihre Braze-Kampagnen und Canvases einbinden können."
alias: /partners/fresh_relevance/
page_type: partner
search_tag: Partner

---

# Frische Relevanz

> [Fresh Relevance][1] ist eine vielseitige Personalisierungslösung, die es handelsorientierten Unternehmen ermöglicht, mühelos maßgeschneiderte kanalübergreifende Erlebnisse zu schaffen. Die Plattform spart Ihnen Zeit, lässt sich in Ihr technisches System integrieren und ermöglicht es Ihnen, über Ihre Website, App, E-Mails, SMS und Anzeigen personalisierte Kundenerlebnisse zu liefern, die die Konversion steigern, ohne dass Sie auf Ihr IT-Team angewiesen sind.

Die Integration von Braze und Fresh Relevance ermöglicht es Ihnen:
* Versenden Sie erweiterte, ausgelöste E-Mail-Kampagnen, wie z.B. Preissenkungen, wieder vorrätig, mehrstufiges Stöbern oder Nachrichten über abgebrochene Einkäufe.
* Fügen Sie personalisierte Inhalte in ausgelöste E-Mails ein, wie z.B. Produktempfehlungen, die auf dem vom Kunden durchsuchten Produkt oder auf Artikeln innerhalb derselben Kategorie basieren.
* Personalisieren Sie Massen-E-Mail-Kampagnen mit KI-gesteuerten Empfehlungen, Countdown-Zeiten, Echtzeit-Wettervorhersagen, Social Media Feeds und mehr.
* Erweitern Sie Ihre E-Mail-Datenbank mit neuen Kontakten, die Sie über Pop-ups zur Datenerfassung sammeln.
* Identifizieren Sie Website-Besucher, die über einen Braze E-Mail-Link kommen.

## Voraussetzungen

| Anforderung | Beschreibung |
|-------------| ----------- |
| Frische Relevanz Konto  | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Fresh Relevance-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit ausreichenden Berechtigungen für die unten aufgeführten Endpunkte. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | [Ihre REST-Endpunkt-URL][3]. Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |
| ID der Lötkampagne | Die Standard-Braze-Kampagne, die Sie zum Versenden von E-Mails verwenden möchten. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Um die Integration in Fresh Relevance einzurichten, müssen Sie einen Braze-Kanal in **Messaging-Kanälen** erstellen und den Kanal je nach Bedarf in entsprechenden Fresh Relevance-Auslösern oder -Inhalten verwenden. 

Für eine schrittweise Anleitung melden Sie sich bei Fresh Relevance an und folgen Sie der [Dokumentation][2].

Das Fresh Relevance-System kommuniziert mit Braze über den angegebenen API-Schlüssel. Bei einer vollständigen Integration werden die folgenden Braze-API-Endpunkte verwendet:

* [`/users/alias/new`][4]
* [`/users/track`][5]
* [`/campaigns/triggers/send`][6]
* [`/users/export/ids`][7]
* [`/subscription/status/get`][8]
* [`/v2/subscription/status/set`][9]

[1]: https://www.freshrelevance.com/
[2]: https://admin.freshrelevance.com/help/esp_instructions/?esp_class_name=EspBraze
[3]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[4]: {{site.baseurl}}/api/endpoints/user_data/post_user_alias/
[5]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/
[6]: {{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/
[7]: {{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/
[8]: {{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/
[9]: {{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status_v2/