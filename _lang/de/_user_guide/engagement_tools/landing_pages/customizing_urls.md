---
nav_title: Anpassen der URL
article_title: Anpassen der URLs von Zielseiten
description: "Erfahren Sie, wie Sie die URLs Ihrer Landing Page an die Marke Ihres Unternehmens anpassen können, indem Sie Ihre Domain mit Ihrem Braze Workspace verbinden."
page_order: 1
---

# Anpassen der URLs von Zielseiten

> Erfahren Sie, wie Sie die URLs Ihrer Landing Page an die Marke Ihres Unternehmens anpassen können, indem Sie Ihre Domain mit Ihrem Braze Workspace verbinden.

## Funktionsweise

Wenn Sie [Ihre Domain mit Braze verbinden](#connecting-your-domain-to-braze), wird sie als Standard Domain für alle Landing Pages verwendet. Wenn Sie beispielsweise die Subdomain `forms.example.com` einbinden, würden Ihre Landing Page URLs nun `forms.example.com/holiday-sale` lauten.

Die Anzahl der angepassten Domains, die Sie mit Ihrem Braze-Konto verbinden können, hängt von Ihrer [Tarifstufe]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers) ab. Um Ihr Limit zu erhöhen, wenden Sie sich an Ihren Braze-Konto Manager:in.

## Ihre Domain mit Braze verbinden

Um eine Domain mit Ihrem Braze-Konto zu verbinden, lassen Sie einen Administrator die folgenden Schritte ausführen.

1. Gehen Sie zu **Einstellungen** > **Landing Page-Einstellungen**.
2. Geben Sie die Domain ein, die Sie verbinden möchten, und wählen Sie **Senden**. Zum Beispiel: `forms.example.com`.
3. Kopieren Sie die **TXT-** und **CNAME-Einträge** und fügen Sie sie in die DNS-Einstellungen Ihres Domain-Providers ein.
4. Kehren Sie zum Braze-Dashboard zurück, um die Verbindung zu überprüfen.

![Landing Page-Einstellungsseite mit einem TXT- und zwei CNAME-Einträgen, die mit ihren jeweiligen Namen und Werten aufgeführt sind.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Je nach Ihrem Domainanbieter kann die Verbindung bis zu 48 Stunden dauern. Wenn der Prozess abgeschlossen ist, verwenden wir Ihre benutzerdefinierte Domain für Ihre Landing Pages im Braze Dashboard.
{% endalert %}

## Entfernen Ihrer Domain

Wenn Sie ein Braze-Administrator sind, können Sie eine zuvor konfigurierte Domain entfernen, indem Sie die folgenden Schritte ausführen:

1. Gehen Sie zu **Einstellungen** > **Landing Page-Einstellungen**.
2. Wählen Sie **Angepasste Domain entfernen**
3. Bestätigen Sie die Entfernung der Domain.
4. Entfernen Sie die aufgeführten DNS-Einträge aus Ihren Domain-Einstellungen.

{% alert important %}
Wenn Sie eine angepasste Domain entfernen, wird diese URL nicht mehr gültig sein. Alle Landing Pages, die diese Domain verwendet haben, werden automatisch auf die von Braze eingestellte Standard Domain zurückgesetzt.
{% endalert %}


## DNS-Ressourcen

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

### Kann ich dieselbe Subdomain verwenden, die ich derzeit für meine Haupt-Website oder meine sendende Domain verwende?

Nein, Sie können keine Subdomains verwenden, die bereits in Gebrauch sind. Diese Subdomains sind zwar gültig, können aber nicht für Landing Pages verwendet werden, wenn sie bereits anderen Zwecken zugewiesen sind oder DNS-Einträge haben, die mit den erforderlichen CNAME-Einträgen in Konflikt stehen.

