---
nav_title: Jebbit
article_title: Jebbit
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Jebbit, einer PaaS, die es Ihnen ermöglicht, Benutzer-E-Mails und Attribute aus Ihren Jebbit-Kampagnen als Benutzerdaten in Echtzeit an Braze zu übergeben."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/) ist eine PaaS, mit der Sie ansprechende Erlebnisse für Benutzer zur Erfassung von Erstanbieterdaten erstellen können.

Mit der Integration von Braze und Jebbit können Sie Benutzer-E-Mails und Attribute aus Ihren Jebbit-Kampagnen als Benutzerdaten in Echtzeit an Braze weitergeben. Diese Daten können dann verwendet werden, um Marketinginitiativen wie personalisierte E-Mail-Kampagnen und Trigger zu steuern. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|Jebbit-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Jebbit-Konto. |
| Braze REST API Schlüssel | Ein Braze REST API-Schlüssel mit allen Berechtigungen für Benutzerdaten. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
|Braze REST Endpunkt | Ihre REST-Endpunkt-URL. Ihr Endpunkt hängt von der Braze-URL für Ihre [Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Wenn Sie die Integration mit Jebbit beantragen, teilen Sie uns mit, ob feste Fristen eingehalten werden müssen. Stellen Sie außerdem sicher, dass Sie die Attribute Ihrer Jebbit-Erfahrung(en), die Sie an Braze weitergeben möchten, zugeordnet haben.

### Schritt 1: API-Anmeldeinformationen bereitstellen

Stellen Sie Jebbit Ihre API-Zugangsdaten in einer Textdatei über eine Dropbox-Dateianfrage zur Verfügung.
Senden Sie Ihre Datei über die folgende [Dropbox-URL](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx).

### Schritt 2: Bestätigung der Testabgabe

Ein Jebbit-Ingenieur, der für Ihre Integration zuständig ist, wird eine Testübertragung von Jebbit zu Braze durchführen, damit Sie sehen können, wie die Daten in Ihrer Braze-Umgebung aussehen werden. Dies ist der letzte Schritt zur Aktivierung der Integration. Jetzt, da Ihre Jebbit-Daten eingerichtet sind, können Sie sie für Ihre Marketinginitiativen nutzen.

{% alert note %}
Die Attribut-ID, die Sie in Jebbit festgelegt haben, ist die Art und Weise, wie der Name des Attributfelds in Braze angezeigt wird.
{% endalert %}

## Anpassung

Wir unterstützen derzeit speziell die Endpunkte für [Benutzerdaten]({{site.baseurl}}/api/endpoints/user_data/), aber Anfragen für andere Endpunkte können unterstützt werden.
Auch die Namen der Attributfelder können Sie nach Belieben anpassen.

Wenn Sie zusätzliche Attribute von Jebbit in Braze wünschen, ordnen Sie das neue Attribut in Ihrem Jebbit-Konto zu. Das Attribut wird automatisch in Braze angezeigt, wenn Sie Daten für dieses Attribut sammeln.
