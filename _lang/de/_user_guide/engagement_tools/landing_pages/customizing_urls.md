---
nav_title: Passen Sie die URL an
article_title: Anpassen von Landing Page URLs
description: "Erfahren Sie, wie Sie die URLs Ihrer Landing Page an die Marke Ihres Unternehmens anpassen können, indem Sie Ihre Domain mit Ihrem Braze Workspace verbinden."
page_order: 1
---

# Anpassen von Landing Page URLs

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

![Seite „Startseiteneinstellungen“ mit einem TXT- und zwei CNAME-Einträgen, die mit ihren jeweiligen Namen und Werten aufgeführt sind.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

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

{% multi_lang_include dns_records.md %}

## Fehlersuche 

### Meine Domainverbindung ist fehlgeschlagen

Vergewissern Sie sich, dass Ihre Domain korrekt eingegeben wurde und dass sie mit der Domain übereinstimmt, die Sie Braze über Ihr Domain-Provider-Konto übermittelt haben. Wenn sie korrekt ist und übereinstimmt, überprüfen Sie die von Braze bereitgestellten TXT- und CNAME-Einträge. Sie sollten mit den Einträgen übereinstimmen, die Sie in Ihrem Domain-Anbieter-Konto eingegeben haben.

## Häufig gestellte Fragen

### Kann ich mehrere Subdomains mit meinem Arbeitsbereich verbinden oder eine Subdomain mit mehreren Arbeitsbereichen verbinden?

Nein, Sie können derzeit nur eine Subdomain mit einem Arbeitsbereich verbinden.

### Kann ich dieselbe Subdomain verwenden, die ich derzeit für meine Haupt-Website oder meine sendende Domain verwende?

Nein, Sie können keine Subdomains verwenden, die bereits in Gebrauch sind. Diese Subdomains sind zwar gültig, können aber nicht für Landing Pages verwendet werden, wenn sie bereits anderen Zwecken zugewiesen sind oder DNS-Einträge haben, die mit den erforderlichen CNAME-Einträgen in Konflikt stehen.

### Warum bleibt meine angepasste Domain trotz gültiger DNS-Einträge auf "Verbinden" stehen?

Wenn Ihre angepasste Domain alle DNS-Einträge als "Verbunden" anzeigt, der Domain-Status jedoch länger als vier Stunden auf "Verbunden" bleibt, verwendet Ihr Unternehmen möglicherweise CAA-Einträge (Certificate Authority Authorization) oder Cloudflare-Zonen-Holds, die Braze daran hindern, Ihre Seite zu sichern.

#### CAA Aufzeichnungen

CAA-Einträge schränken ein, welche Zertifizierungsstellen SSL-Zertifikate für Ihre Domain ausstellen können. Wenn Ihre CAA-Einträge LetsEncrypt nicht enthalten, kann Braze (über Cloudflare) das erforderliche SSL-Zertifikat nicht ausstellen.

Bitten Sie Ihr IT-Team, Ihrer Subdomain einen CAA-Eintrag mit den folgenden Werten hinzuzufügen, um dieses Problem zu lösen:
- **Datensatztyp:** CAA
- **Wert:** `0 issue "letsencrypt.org"`

Weitere Informationen finden Sie in der [CAA-Dokumentation von LetsEncrypt](https://letsencrypt.org/docs/caa/).

#### Cloudflare-Zone hält

Wenn Ihr Unternehmen Cloudflare verwendet, verhindert möglicherweise ein Sicherheitsfeature für Zonen, dass Braze Ihre angepasste Domain erstellt.

Um dieses Problem zu lösen, bitten Sie Ihr IT Team, die Sperrung der Zone vorübergehend aufzuheben. Weitere Informationen finden Sie in [der Dokumentation von Cloudflare zur Zonenhaltung](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Neustart des Validierungsprozesses

Nachdem Sie eines der beiden Probleme gelöst haben, löschen Sie Ihre angepasste Domain im Braze-Dashboard und erstellen Sie sie neu, um den Validierungsprozess neu zu starten.

