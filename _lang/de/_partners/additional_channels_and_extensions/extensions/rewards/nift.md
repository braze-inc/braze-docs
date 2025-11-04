---
nav_title: Nift
article_title: Nift
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Nift, einer zweiseitigen Plattform, die Unternehmen dabei hilft, Kunden:in zu gewinnen, zu engagieren und zu binden."
alias: /partners/nift/
page_type: partner
search_tag: Partner

---

# Nift

> [Nift](https://gonift.com/) hilft Unternehmen, Kunden zu gewinnen, zu engagieren und zu binden. Die wechselseitige Plattform hilft Partnern, sich bei ihren Kunden mit Nift-Geschenkkarten zu bedanken. Sich bei seinen Kunden zu bedanken steigert den Lifetime-Value und generiert zusätzlichen Umsatz.

_Diese Integration wird von Nift gepflegt._

## Über die Integration

Die Integration von Braze und Nift ermöglicht es Ihnen, zu wichtigen Zeitpunkten im Kundenlebenszyklus automatisch "Dankeschöns" mit Nift-Geschenken auszulösen und zu erkennen, welche Kunden ihr Geschenk verwendet haben. Mit Nift-Geschenkkarten können Sie auf Produkte und Dienste von Marken zugreifen, die sich auf die Matchmaking-Technologie von Nift verlassen, um kostengünstig und in großem Umfang neue Kund:innen zu gewinnen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Nift-Konto | Um diese Partnerschaft zu nutzen, benötigen Sie ein Nift-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit allen Nutzerdaten-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Mit Braze in Nift verbinden

Besuchen Sie Ihr [Nift-Dashboard](https://www.gonift.com/users/sign_in), navigieren Sie zu **Konten** > **Integrationen** > **Braze**, und klicken Sie auf **Verbinden**.

### Schritt 2: Zugangsdaten für Braze hinzufügen

Auf der Seite **Verknüpfen Sie Ihr Braze-Konto** geben Sie Ihren REST-API-Schlüssel für Braze an und wählen Ihren Braze-Endpunkt aus, der von der Braze-URL für Ihre [Instanz]({{site.baseurl}}/api/basics/#endpoints) abhängt.

Sie können den Parameternamen der Kund:in für den Empfehlungslink ändern, der an Ihre Kunden gesendet wird. Nift verwendet dies, um Ihre Kund:in als in Braze bearbeitet zu kennzeichnen, wenn sie ein Geschenk von einer unserer Marken ausgewählt haben.

Klicken Sie auf **Konto verknüpfen**.

!["Seite zur Integration von Diensten in Nift, die den Nutzer:innen zur Eingabe des Braze API-Schlüssels und der URL des Braze-Dashboards auffordert.]({% image_buster /assets/img/nift/link_your_braze_account.png %})

## Verwendung der Integration

Um die Integration zu nutzen, verteilen Sie den Empfehlungslink in Ihren Nachrichten. Wenn Ihr Kunde den Empfehlungslink verwendet und ein Geschenk von einer unserer Marken auswählt, wird Nift ihn als in Braze bearbeitet markieren.

Nach der Integration mit Braze wird Nift automatisch Push-Events mit den folgenden Daten an den bestehenden Kund:in-Datensatz von Braze senden:

- Name der Veranstaltung: `nift_processed`
- Zeit: Der Zeitpunkt, zu dem die Kund:in das Geschenk ausgewählt/eingesetzt hat



