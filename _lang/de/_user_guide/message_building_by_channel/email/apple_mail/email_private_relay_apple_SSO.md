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

1. Rufen Sie Ihre **Apple-Zertifikatsseite** auf und geben Sie die E-Mail-Adresse an, die Sie für den Versand über den E-Mail-Relay-Service von Apple verwenden möchten (Ihre gewünschte "Von"-Adresse).
- Die Adresse sollte wie folgt formatiert werden: `bounces+<YOUR_UID>@<YOUR_WHITELABELED_SUBDOMAIN_AND_DOMAIN>`(Beispiel: `bounces+1234567@braze.online.docs.com`). 

![Option zum Auflisten einzelner E-Mail-Adressen auf der Apple-Zertifikatsseite.]({% image_buster /assets/img/email-relay-whitelabel-address.png %})

{:start="2"}
2\. Nachdem die Adresse zu Ihrer Apple-Zertifikatsseite hinzugefügt wurde, werden E-Mails von dieser Domain über das Apple Private Relay System zugestellt.

{% alert important %}
Wenn Ihre gewünschte „Von“-Adresse eine `abmail`-Adresse ist, fügen Sie diese in Ihre Subdomain ein. Verwenden Sie zum Beispiel `abmail.docs.braze.com` anstelle von `docs.braze.com`.
{% endalert %}

### „Absenderadresse“-Werte

In dieser Tabelle finden Sie die Komponenten, die beim Hinzufügen von E-Mail-Adressen mit Apple Private Relay verwendet werden.

| Wert | Beschreibung |
|---|---|
| UID | Dieser Wert wird in Ihren DNS-Einträgen angegeben, die von Braze (von SendGrid) zur Verfügung gestellt werden. Verwenden Sie in Ihrer UID in der E-Mail-Adresse nicht den Buchstaben „u“. Wenn Ihre UID in SendGrid zum Beispiel als `u1234567.wl134.sendgrid.net` angezeigt wird, ist `1234567` der UID-Wert. <br><br> Wenn Sie keinen Zugriff auf Ihre DNS-Einträge haben, wenden Sie sich an Ihren Braze Customer Success Manager, um Ihre UID zu erhalten. |
| Whitelabeled Subdomain und Domain | Die ursprüngliche Domain und Subdomain, die Sie in SendGrid eingegeben haben. Sie können den **HOST-Wert** auch in Ihren DNS-Einträgen in SendGrid verwenden. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Versenden von E-Mails für SparkPost

Um Apple Private Relay für SparkPost einzurichten, gehen Sie wie folgt vor: 

1. Melden Sie sich mit Apple an.
2. Erstellen Sie anhand der [Dokumentation von Apple](https://developer.apple.com/sign-in-with-apple/get-started/) die erforderlichen Verifizierungsdateien und hosten Sie diese Dateien in einem zugänglichen Verzeichnis für die angegebenen Domains.
3. Fügen Sie in Ihren DNS-Einstellungen einen A-Eintrag hinzu, der auf die Domain verweist, auf der Ihre Verifizierungsdatei gehostet wird. Dies ist ein einmaliger Verifizierungsprozess.
4. Fügen Sie die E-Mail Domains in Apple hinzu.
5. Apple überprüft automatisch die Domains und zeigt an, welche davon überprüft wurden. Außerdem haben Sie die Möglichkeit, die Domains erneut zu überprüfen oder zu löschen.

{% alert important %}
Stellen Sie sicher, dass Sie diesen Vorgang innerhalb von 2 bis 3 Tagen nach der Erstellung der Verifizierungsdateien abschließen, da diese sonst verfallen. Apple gibt nicht bekannt, wie lange sie gültig sind.
{% endalert %}

### Überlegungen

Wenn eine sendende Domain auch als Bounce-Domain verwendet wird, können Sie keine Einträge speichern und müssen diese zusätzlichen Schritte ausführen:

1. Wenn die Domain bereits auf SparkPost überprüft wurde, **müssen** Sie MX- und TXT-Einträge erstellen: 

| Instanz | MX-Eintrag                   | TXT-Eintrag                                    |
|----------|-----------------------------|-----------------------------------------------|
| USA       | `smtp.sparkpostmail.com`    | `"v=spf1 redirect=_spf.sparkpostmail.com"`    |
| EU       | `smtp.eu.sparkpostmail.com` | `"v=spf1 redirect=_spf.eu.sparkpostmail.com"` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert important %}
Um SPF-Fehler zu vermeiden, müssen Sie die MX- und TXT-Einträge erstellen und in das DNS übertragen, **bevor** Sie den CNAME-Eintrag löschen.
{% endalert %}

{:start="2"}
2\. Löschen Sie den CNAME-Eintrag.
3\. Ersetzen Sie ihn durch die MX- und TXT-Einträge für ein korrektes Routing.
4\. Erstellen Sie Ihren A-Eintrag, der auf Ihr CDN oder Filehosting verweist.

Wenn Sie weitere Fragen haben, öffnen Sie ein [Support-Ticket]({{site.baseurl}}/braze_support/).
