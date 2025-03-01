---
nav_title: Nift
article_title: Nift
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Nift, einer zweiseitigen Plattform, die Unternehmen hilft, Kunden zu gewinnen, zu binden und zu halten."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) hilft Unternehmen, Kunden zu gewinnen, zu binden und zu halten. Die zweiseitige Plattform hilft Partnern, sich bei ihren Kunden mit Nift-Geschenkkarten zu bedanken. Wenn Sie sich bei Ihren Kunden bedanken, erhöhen Sie deren Lebenszeitwert und generieren zusätzlichen Umsatz.

Die Integration von Braze und Nift ermöglicht es Ihnen, zu wichtigen Zeitpunkten im Kundenlebenszyklus automatisch "Dankeschöns" mit Nift-Geschenken auszulösen und festzustellen, welche Kunden ihr Geschenk verwendet haben. Nift-Geschenkkarten können für Produkte und Dienstleistungen von Marken verwendet werden, die sich auf die Matchmaking-Technologie von Nift verlassen, um kostengünstig und in großem Umfang neue Kunden zu gewinnen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Nift-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein Nift-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen für Benutzerdaten. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für Ihre [Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Verbinden mit Braze in Nift

Besuchen Sie Ihr [Nift-Dashboard][2], navigieren Sie zu **Konten** > **Integrationen** > **Braze** und klicken Sie auf **Verbinden**.

### Schritt 2: Anmeldedaten für Braze hinzufügen

Auf der Seite **Verknüpfen Sie Ihr Braze-Konto** geben Sie Ihren Braze-REST-API-Schlüssel an und wählen Ihren Braze-Endpunkt aus, der von der Braze-URL für Ihre [Instanz]({{site.baseurl}}/api/basics/#endpoints) abhängt.

Sie können den Namen des Kunden-ID-Parameters im Empfehlungslink, den Sie an Ihre Kunden senden, ändern. Nift verwendet dies, um Ihre Kunden als in Braze verarbeitet zu kennzeichnen, wenn sie ein Geschenk von einer unserer Marken ausgewählt haben.

Klicken Sie auf **Konto verknüpfen**.

!["Nift-Service-Integrationsseite, die den Benutzer zur Eingabe des Braze-API-Schlüssels und der Braze-Dashboard-URL auffordert.][5]

## Verwendung der Integration

Um die Integration zu nutzen, verteilen Sie den Empfehlungslink in Ihren Nachrichten. Wenn Ihr Kunde den Empfehlungslink verwendet und ein Geschenk von einer unserer Marken auswählt, markiert Nift dies in Braze als bearbeitet.

Nach der Integration mit Braze wird Nift automatisch Ereignisse mit den folgenden Daten in den bestehenden Braze-Kundendatensatz einfügen:

- Name der Veranstaltung: `nift_processed`
- Zeit: Der Zeitpunkt, zu dem der Kunde das Geschenk ausgewählt/eingesetzt hat


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.gonift.com/users/sign_in
[5]: {% image_buster /assets/img/nift/link_your_braze_account.png %}
[6]: {% image_buster /assets/img/nift/braze_account_linked.png %}