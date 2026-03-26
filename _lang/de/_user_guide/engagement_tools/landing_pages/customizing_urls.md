---
nav_title: URL anpassen
article_title: Anpassen von Landing-Page-URLs
description: "Erfahren Sie, wie Sie die URLs Ihrer Landing-Page an die Marke Ihres Unternehmens anpassen können, indem Sie Ihre Domain mit Ihrem Braze Workspace verbinden."
page_order: 1
---

# Anpassen von Landing-Page-URLs

> Erfahren Sie, wie Sie die URLs Ihrer Landing-Page an die Marke Ihres Unternehmens anpassen können, indem Sie Ihre Domain mit Ihrem Braze Workspace verbinden.

## Funktionsweise

Wenn Sie [Ihre Domain mit Braze verbinden](#connect-your-domain-to-braze), wird sie als Standard-Domain für alle Landing-Pages verwendet. Wenn Sie beispielsweise die Subdomain `forms.example.com` verbinden, lauten Ihre Landing-Page-URLs nun `forms.example.com/holiday-sale`.

Die Anzahl der angepassten Domains, die Sie mit Ihrem Braze-Konto verbinden können, hängt von Ihrer [Tarifstufe]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/#plan-tiers) ab. Um Ihr Limit zu erhöhen, wenden Sie sich an Ihren Braze Account Manager.

## Ihre Domain mit Braze verbinden {#connect-your-domain-to-braze}

Um eine Domain mit Ihrem Braze-Konto zu verbinden, lassen Sie eine:n Administrator:in die folgenden Schritte ausführen.

1. Gehen Sie zu **Einstellungen** > **Landing-Page-Einstellungen**.
2. Geben Sie die Domain ein, die Sie verbinden möchten, und wählen Sie **Senden**. Zum Beispiel: `forms.example.com`.
3. Kopieren Sie die **TXT-** und **CNAME-Einträge** und fügen Sie sie in die DNS-Einstellungen Ihres Domain-Anbieters ein.
4. Kehren Sie zum Braze-Dashboard zurück, um die Verbindung zu überprüfen.

![Seite „Landing-Page-Einstellungen" mit einem TXT- und zwei CNAME-Einträgen, die mit ihren jeweiligen Namen und Werten aufgeführt sind.]({% image_buster /assets/img/landing_pages/connect_subdomain.png %})

{% alert note %}
Je nach Domain-Anbieter kann die Verbindung bis zu 48 Stunden dauern. Sobald der Vorgang abgeschlossen ist, verwenden wir Ihre angepasste Domain für Ihre Landing-Pages im Braze-Dashboard.
{% endalert %}

## Ihre Domain entfernen

Wenn Sie Braze-Administrator:in sind, können Sie eine zuvor konfigurierte Domain entfernen, indem Sie die folgenden Schritte ausführen:

1. Gehen Sie zu **Einstellungen** > **Landing-Page-Einstellungen**.
2. Wählen Sie **Angepasste Domain entfernen**.
3. Bestätigen Sie die Entfernung der Domain.
4. Entfernen Sie die aufgeführten DNS-Einträge aus Ihren Domain-Einstellungen.

{% alert important %}
Wenn Sie eine angepasste Domain entfernen, ist diese URL nicht mehr gültig. Alle Landing-Pages, die diese Domain verwendet haben, werden automatisch auf die von Braze festgelegte Standard-Domain zurückgesetzt.
{% endalert %}

## Ihre Domain migrieren

So migrieren Sie eine angepasste Domain in einen anderen Workspace:

1. Entfernen Sie die angepasste Domain.
2. Erstellen Sie eine neue angepasste Domain im gewünschten Workspace.
3. Konfigurieren Sie die angepasste Domain mit den neuen DNS-Einträgen neu. Beachten Sie, dass Ihre Subdomain während dieses Vorgangs nicht verfügbar ist.

## DNS-Ressourcen

{% multi_lang_include dns_records.md %}

## Fehlerbehebung

### Meine Domain-Verbindung ist fehlgeschlagen

Vergewissern Sie sich, dass Ihre Domain korrekt eingegeben wurde und mit der übereinstimmt, die Sie über Ihr Domain-Anbieter-Konto an Braze übermittelt haben. Wenn sie korrekt ist und übereinstimmt, überprüfen Sie die von Braze bereitgestellten TXT- und CNAME-Einträge. Diese sollten mit den Einträgen übereinstimmen, die Sie in Ihrem Domain-Anbieter-Konto eingegeben haben.

## Häufig gestellte Fragen

### Kann ich mehrere Subdomains mit meinem Workspace verbinden oder eine Subdomain mit mehreren Workspaces verbinden?

Nein, derzeit können Sie nur eine Subdomain mit einem Workspace verbinden.

### Kann ich dieselbe Subdomain verwenden, die ich derzeit für meine Haupt-Website oder meine Versand-Domain nutze?

Nein, Sie können keine Subdomains verwenden, die bereits in Gebrauch sind. Diese Subdomains sind zwar gültig, können aber nicht für Landing-Pages verwendet werden, wenn sie bereits anderen Zwecken zugewiesen sind oder DNS-Einträge haben, die mit den erforderlichen CNAME-Einträgen in Konflikt stehen.

### Warum bleibt meine angepasste Domain trotz gültiger DNS-Einträge auf „Verbinden" stehen?

Wenn Ihre angepasste Domain alle DNS-Einträge als „Verbunden" anzeigt, der Domain-Status jedoch länger als vier Stunden auf „Verbinden" bleibt, verwendet Ihr Unternehmen möglicherweise CAA-Einträge (Certificate Authority Authorization) oder Cloudflare-Zone-Holds, die Braze daran hindern, Ihre Seite abzusichern.

#### CAA-Einträge

CAA-Einträge schränken ein, welche Zertifizierungsstellen SSL-Zertifikate für Ihre Domain ausstellen können. Wenn Ihre CAA-Einträge LetsEncrypt nicht enthalten, kann Braze (über Cloudflare) das erforderliche SSL-Zertifikat nicht ausstellen.

Um dieses Problem zu lösen, bitten Sie Ihr IT-Team, Ihrer Subdomain einen CAA-Eintrag mit den folgenden Werten hinzuzufügen:
- **Eintragstyp:** CAA
- **Wert:** `0 issue "letsencrypt.org"`

Weitere Informationen finden Sie in der [CAA-Dokumentation von LetsEncrypt](https://letsencrypt.org/docs/caa/).

#### Cloudflare-Zone-Holds

Wenn Ihr Unternehmen Cloudflare verwendet, verhindert möglicherweise ein Zone-Hold-Sicherheitsfeature, dass Braze Ihre angepasste Domain erstellt.

Um dieses Problem zu lösen, bitten Sie Ihr IT-Team, den Zone-Hold vorübergehend aufzuheben. Weitere Informationen finden Sie in der [Cloudflare-Dokumentation zu Zone-Holds](https://developers.cloudflare.com/fundamentals/account/account-security/zone-holds/#release-zone-holds).

#### Neustart des Validierungsprozesses

Nachdem Sie eines der beiden Probleme gelöst haben, löschen Sie Ihre angepasste Domain im Braze-Dashboard und erstellen Sie sie neu, um den Validierungsprozess neu zu starten.