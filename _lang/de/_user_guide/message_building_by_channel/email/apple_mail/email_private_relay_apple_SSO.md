---
nav_title: Senden von E-Mails an Apple Private Relay
article_title: Senden von E-Mails an Apple Private Relay
alias: /email_relay/
page_order: 0
description: "Dieser Artikel beschreibt den Vorgang des Versendens von E-Mails an Apple Private Relay."
channel:
  - email
  
---

# Senden von E-Mails an Apple Private Relay

> Das Single Sign-on (SSO) Feature von Apple erlaubt es seinen Nutzer:innen, ihre E-Mail-Adressen (`example@icloud.com`) freizugeben oder ihre E-Mail-Adressen auszublenden, indem sie anstelle ihrer persönlichen E-Mail-Adresse das, was den Marken zur Verfügung gestellt wird, maskieren (`tq1234snin@privaterelay.appleid.com`). Apple leitet dann die an die Relay-Adressen gesendeten Nachrichten an die tatsächliche E-Mail Adresse des Nutzers:innen weiter. 

Um E-Mails an das private E-Mail-Relay von Apple zu senden, registrieren Sie Ihre Versanddomänen bei Apple. Wenn Sie Ihre Domains nicht mit Apple konfigurieren, werden E-Mails, die an Relay-Adressen gesendet werden, als Bounce zurückgewiesen.

Wenn ein Benutzer beschließt, die E-Mail-Weiterleitung an die Relay-E-Mail Ihrer App zu deaktivieren, erhält Braze wie gewohnt die Informationen über zurückgewiesene E-Mails. Diese Benutzer können Apps, die die Anmeldung bei Apple verwenden, über die Einstellungsseite ihrer Apple ID verwalten (siehe [die Dokumentation von Apple](https://support.apple.com/en-us/HT210426)).

## Senden von E-Mails für SendGrid

Wenn Sie SendGrid als E-Mail-Anbieter verwenden, können Sie E-Mails an Apple senden, ohne DNS-Änderungen vornehmen zu müssen. 

1. Loggen Sie sich in das [Apple Entwickler:in Portal](https://developer.apple.com/) ein.
2. Gehen Sie auf die Seite **Zertifikate, Bezeichner & Profile**.
3. Wählen Sie **Dienste** > **Mit Apple für E-Mail-Kommunikation anmelden**.
4. Fügen Sie im Abschnitt **E-Mail-Quellen** die Domains und Subdomains hinzu.
- Die Adresse sollte wie folgt formatiert werden: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (ein Beispiel ist: `bounces+1234567@braze.online.docs.com`). 

Wenn Ihre gewünschte „Von“-Adresse eine `abmail`-Adresse ist, fügen Sie diese in Ihre Subdomain ein. Verwenden Sie zum Beispiel `abmail.docs.braze.com` anstelle von `docs.braze.com`.

## Versenden von E-Mails für SparkPost

Um Apple Private Relay für SparkPost einzurichten, gehen Sie wie folgt vor: 

1. Melden Sie sich mit Apple an.
2. Folgen Sie der [Dokumentation von Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service), um die E-Mail Domains zu registrieren.
3. Apple überprüft automatisch die Domains, zeigt an, welche davon überprüft sind, und bietet die Möglichkeit, die Domains erneut zu überprüfen oder zu löschen.

### Überlegungen

Wenn eine sendende Domain auch als Bounce-Domain verwendet wird, können Sie keine Einträge speichern und müssen diese zusätzlichen Schritte ausführen:

1. Wenn die Domain bereits auf SparkPost überprüft wurde, **müssen** Sie MX- und TXT-Einträge erstellen: 

| Instanz | MX-Eintrag                   | TXT-Eintrag                                    |
|----------|-----------------------------|-----------------------------------------------|
| USA       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
Um SPF-Fehler zu vermeiden, müssen Sie die MX- und TXT-Einträge erstellen und sie im DNS propagieren lassen **, bevor Sie** den CNAME-Eintrag löschen.
{% endalert %}

{:start="2"}
2\. Löschen Sie den CNAME-Eintrag.
3\. Ersetzen Sie ihn durch die MX- und TXT-Einträge für ein korrektes Routing.
4\. Erstellen Sie Ihren A-Eintrag, der auf Ihr CDN oder Filehosting verweist.

Wenn Sie weitere Fragen haben, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).
