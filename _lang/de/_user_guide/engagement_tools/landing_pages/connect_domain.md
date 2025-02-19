---
nav_title: Verbinden Ihrer Domain
article_title: Verbinden Ihrer Domain
description: "Dieser Artikel beschreibt, wie Sie Ihre eigene benutzerdefinierte Domain mit Braze-Landingpages verbinden können."
page_order: 1
alias: /landing_pages/connect_domain/
---

# Verbinden Ihrer Domain

> Verbinden Sie Ihre eigene Domain mit Ihrem Braze-Arbeitsbereich, um die URLs Ihrer Landing Pages an Ihre Marke anzupassen.

Um eine Domain oder Subdomain mit Ihrem Braze-Konto zu verbinden, lassen Sie einen Administrator die folgenden Schritte ausführen.

1. Gehen Sie zu **Einstellungen** > **Landing Page-Einstellungen**.
2. Geben Sie die Domain oder Subdomain ein, die Sie verbinden möchten, und wählen Sie **Senden**. Zum Beispiel: `forms.example.com`.
3. Kopieren Sie die **TXT-** und **CNAME-Einträge** und fügen Sie sie in die DNS-Einstellungen Ihres Domain-Providers ein.
4. Kehren Sie zum Braze-Dashboard zurück, um die Verbindung zu überprüfen.

![Seite „Startseiteneinstellungen“ mit einem TXT- und zwei CNAME-Einträgen, die mit ihren jeweiligen Namen und Werten aufgeführt sind.][1]

{% alert note %}
Je nach Ihrem Domainanbieter kann die Verbindung bis zu 48 Stunden dauern. Wenn der Prozess abgeschlossen ist, verwenden wir Ihre benutzerdefinierte Domain für Ihre Landing Pages im Braze Dashboard.
{% endalert %}

## Verwendung Ihrer Domain in Braze

Nachdem die Überprüfung Ihrer Domain abgeschlossen ist, wird sie standardmäßig in Braze verwendet. Wenn Sie beispielsweise die Subdomain `forms.example.com` verbinden, werden Ihre Startseiten-URLs aktualisiert und sehen dann wie `forms.example.com/holiday-sale` aus.

{% alert note %}
Die Löschung von benutzerdefinierten Domänen ist in Kürze möglich. Wenden Sie sich an Ihre:n Customer-Success-Manager:in, wenn Sie Ihre Subdomain entfernen müssen.
{% endalert %}

## Ressourcen von Domainanbietern

Nachfolgend finden Sie Ressourcen für die Erstellung und Verwaltung von DNS-Einträgen bei häufig verwendeten Domain-Providern. Wenn Sie einen anderen Anbieter verwenden, schlagen Sie in der Dokumentation dieses Anbieters nach oder wenden Sie sich an dessen Support-Team.

| Domain-Anbieter | Ressourcen |
| --- | --- |
| Bluehost | [DNS-Einträge erklärt](https://my.bluehost.com/hosting/help/508)<br> [DNS-Verwaltung Hinzufügen Bearbeiten oder Löschen von DNS-Einträgen](https://my.bluehost.com/hosting/help/559) |
| Dreamhost | [Wie kann ich benutzerdefinierte DNS-Einträge hinzufügen?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| GoDaddy | [CNAME-Eintrag hinzufügen](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| Cloudflare | [DNS-Einträge verwalten](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Squarespace | [Hinzufügen benutzerdefinierter DNS-Einstellungen](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Fehlersuche 

### Meine Domainverbindung ist fehlgeschlagen

Vergewissern Sie sich, dass Ihre Domain korrekt eingegeben wurde und dass sie mit der Domain übereinstimmt, die Sie Braze über Ihr Domain-Provider-Konto übermittelt haben. Wenn sie korrekt ist und übereinstimmt, überprüfen Sie die von Braze bereitgestellten TXT- und CNAME-Einträge. Sie sollten mit den Einträgen übereinstimmen, die Sie in Ihrem Domain-Anbieter-Konto eingegeben haben.

## Häufig gestellte Fragen

### Kann ich mehrere Subdomains mit meinem Arbeitsbereich verbinden oder eine Subdomain mit mehreren Arbeitsbereichen verbinden?

Nein, Sie können derzeit nur eine Subdomain mit einem Arbeitsbereich verbinden.

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}
