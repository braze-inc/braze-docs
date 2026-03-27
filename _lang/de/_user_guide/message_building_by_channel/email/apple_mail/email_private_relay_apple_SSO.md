---
nav_title: E-Mails an Apple Private Relay senden
article_title: E-Mails an Apple Private Relay senden
alias: /email_relay/
page_order: 0
description: "Dieser Artikel beschreibt den Vorgang des Versendens von E-Mails an Apple Private Relay."
channel:
  - email
toc_headers: h2
---

# E-Mails an Apple Private Relay senden

> Das Single Sign-on (SSO)-Feature von Apple erlaubt es Nutzer:innen, ihre E-Mail-Adressen (`example@icloud.com`) zu teilen oder ihre E-Mail-Adressen auszublenden, indem anstelle der persönlichen E-Mail-Adresse eine maskierte Adresse (`tq1234snin@privaterelay.appleid.com`) an Marken weitergegeben wird. Apple leitet dann die an die Relay-Adressen gesendeten Nachrichten an die tatsächliche E-Mail-Adresse der Nutzer:innen weiter. 

Um E-Mails an das private E-Mail-Relay von Apple zu senden, registrieren Sie Ihre Versanddomains bei Apple. Wenn Sie Ihre Domains nicht bei Apple konfigurieren, führen E-Mails an Relay-Adressen zu Bounces.

Wenn Nutzer:innen beschließen, die E-Mail-Weiterleitung an die Relay-E-Mail Ihrer App zu deaktivieren, erhält Braze wie gewohnt die Bounce-Informationen. Diese Nutzer:innen können Apps, die „Mit Apple anmelden" verwenden, über die Einstellungsseite ihrer Apple-ID verwalten (siehe [Dokumentation von Apple](https://support.apple.com/en-us/HT210426)).

{% tabs %}
{% tab SendGrid %}

## SendGrid konfigurieren 

Wenn Sie SendGrid als E-Mail-Anbieter verwenden, können Sie E-Mails an Apple senden, ohne DNS-Änderungen vornehmen zu müssen. 

1. Melden Sie sich beim [Apple Developer Portal](https://developer.apple.com/) an.
2. Gehen Sie auf die Seite **Certificates, Identifiers & Profiles**.
3. Wählen Sie **Services** > **Sign in with Apple for Email Communication**.
4. Fügen Sie im Abschnitt **Email Sources** die Domains und Subdomains hinzu.
- Die Adresse sollte wie folgt formatiert werden: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>` (ein Beispiel ist: `bounces+1234567@braze.online.docs.com`). 

Wenn Ihre gewünschte „Von"-Adresse eine `abmail`-Adresse ist, fügen Sie diese in Ihre Subdomain ein. Verwenden Sie zum Beispiel `abmail.docs.braze.com` anstelle von `docs.braze.com`.

{% endtab %}
{% tab SparkPost %}

## SparkPost konfigurieren 

Um Apple Private Relay für SparkPost einzurichten, gehen Sie wie folgt vor: 

1. Melden Sie sich mit Apple an.
2. Folgen Sie der [Dokumentation von Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service), um die E-Mail-Domains zu registrieren.
3. Apple überprüft automatisch die Domains, zeigt an, welche davon verifiziert sind, und bietet die Möglichkeit, die Domains erneut zu überprüfen oder zu löschen.

### Wenn die Versanddomain auch die Bounce-Domain ist

Wenn eine Versanddomain auch als Bounce-Domain verwendet wird, können Sie keine Einträge speichern und müssen diese zusätzlichen Schritte ausführen:

1. Wenn die Domain bereits auf SparkPost verifiziert wurde, **müssen** Sie MX- und TXT-Einträge erstellen: 

| Instanz | MX-Eintrag                   | TXT-Eintrag                                    |
|----------|-----------------------------|-----------------------------------------------|
| US       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
Um SPF-Fehler zu vermeiden, müssen Sie die MX- und TXT-Einträge erstellen und sie im DNS propagieren lassen, **bevor** Sie den CNAME-Eintrag löschen.
{% endalert %}

{:start="2"}
2. Löschen Sie den CNAME-Eintrag.
3. Ersetzen Sie ihn durch die MX- und TXT-Einträge für ein korrektes Routing.
4. Erstellen Sie Ihren A-Eintrag, der auf Ihr CDN oder Filehosting verweist.

{% endtab %}
{% tab Amazon SES %}

## Amazon SES konfigurieren

### Eine angepasste MAIL FROM-Domain konfigurieren

Um Apple Private Relay für Amazon Simple Email Service (SES) einzurichten, müssen Sie zunächst eine angepasste MAIL FROM-Domain in SES konfigurieren. Weitere Informationen finden Sie in der [Dokumentation von AWS](https://docs.aws.amazon.com/ses/latest/dg/mail-from.html).

### Domains bei Apple registrieren

1. Melden Sie sich mit Apple an.
2. Folgen Sie der [Dokumentation von Apple](https://developer.apple.com/help/account/configure-app-capabilities/configure-private-email-relay-service), um die E-Mail-Domains zu registrieren.
3. Apple überprüft automatisch die Domains, zeigt an, welche davon verifiziert sind, und bietet die Möglichkeit, die Domains erneut zu überprüfen oder zu löschen.

{% endtab %}
{% endtabs %}

Wenn Sie weitere Fragen haben, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).