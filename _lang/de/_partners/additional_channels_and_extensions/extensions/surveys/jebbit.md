---
nav_title: Jebbit
article_title: Jebbit
description: "Dieser Artikel referenziert die Partnerschaft zwischen Braze und Jebbit, einer PaaS, die es Ihnen erlaubt, E-Mails und Attribute von Nutzern aus Ihren Jebbit Kampagnen als Nutzerdaten in Realtime an Braze zu übergeben."
alias: /partners/jebbit/
page_type: partner
search_tag: Partner

---

# Jebbit

> [Jebbit](https://www.jebbit.com/) ist eine PaaS, die es Ihnen erlaubt, engagierte Erfahrungen für Nutzer:innen zu erstellen, um First-Party-Daten zu erfassen.

_Diese Integration wird von Jebbit gepflegt._

## Über die Integration

Mit der Integration von Braze und Jebbit können Sie E-Mails und Attribute von Nutzern aus Ihren Jebbit Kampagnen als Nutzerdaten in Realtime an Braze weitergeben. Diese Daten können dann für Marketing-Initiativen wie personalisierte E-Mail-Kampagnen und Trigger verwendet werden. 

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
|Jebbit Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Jebbit-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit allen Nutzerdaten-Berechtigungen. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
|Braze REST Endpunkt | Ihre URL für den REST-Endpunkt. Ihr Endpunkt hängt von der Braze-URL für [Ihre Instanz]({{site.baseurl}}/api/basics/#endpoints) ab. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

Wenn Sie eine Integration mit Jebbit anfragen, teilen Sie uns mit, ob Sie bestimmte Fristen einhalten müssen. Stellen Sie außerdem sicher, dass Sie die Attribute Ihrer Jebbit-Erfahrung(en), die Sie an Braze weitergeben möchten, abgebildet haben.

### Schritt 1: API Zugangsdaten bereitstellen

Stellen Sie Jebbit Ihre API Zugangsdaten in einer Textdatei über eine Anfrage bei Dropbox zur Verfügung.
Senden Sie Ihre Datei über die folgende [Dropbox-URL](https://www.dropbox.com/request/RqKQHkJHXw1cFBKbXpZx).

### Schritt 2: Bestätigung der Testabgabe

Ein Jebbit-Ingenieur, der für Ihre Integration zuständig ist, wird eine Testübertragung von Jebbit zu Braze durchführen, damit Sie sehen können, wie die Daten in Ihrer Braze-Umgebung aussehen werden. Dies ist der letzte Schritt zur Aktivierung der Integration. Jetzt, wo Ihre Jebbit Daten eingerichtet sind, nutzen Sie sie, um Ihre Marketing-Initiativen voranzutreiben.

{% alert note %}
Die ID des Attributs, die Sie in Jebbit festgelegt haben, ist die Art und Weise, wie der Name des Attributfelds in Braze angezeigt wird.
{% endalert %}

## Anpassung

Wir unterstützen derzeit speziell die Endpunkte für [Nutzerdaten]({{site.baseurl}}/api/endpoints/user_data/), aber Anfragen für andere Endpunkte können unterstützt werden.

Die Namen der Attribut-Felder können auch an Ihre Wünsche angepasst werden.

Wenn Sie zusätzliche Attribute von Jebbit in Braze wünschen, bilden Sie das neue Attribut in Ihrem Jebbit-Konto ab. Das Attribut wird automatisch in Braze angezeigt, wenn Sie Daten für dieses Attribut sammeln.

