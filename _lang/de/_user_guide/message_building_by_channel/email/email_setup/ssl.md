---
nav_title: SSL bei Braze
article_title: SSL-Übersicht
page_order: 5
page_type: reference
description: "Dieser Referenzartikel behandelt SSL, wofür es verwendet wird und wie es bei Braze eingesetzt wird."
channel: email

---

# SSL bei Braze

{% multi_lang_include video.html id="zP1N_wN0SsQ" align="right" %}

> Eine SSL-Verschlüsselung verschlüsselt eine URL mit HTTPS anstelle von HTTP. HTTPS zeigt an, dass ein gültiges und vertrauenswürdiges SSL- oder TLS-Zertifikat vorhanden ist und dass die Website sicher besucht werden kann.

## Warum ist SSL wichtig?

Die meisten Domains erfordern kein SSL, jedoch empfiehlt Braze aus den folgenden Gründen dringend die Verwendung von SSL.

Die Sicherung Ihrer Website und Links mit SSL ist eine gängige Praxis, selbst für Unternehmen, die nicht direkt mit sensiblen Kundendaten arbeiten. Die Benutzer sind vertrauensvoller gegenüber Links, die mit SSL gesichert sind, und die zusätzliche Authentifizierungsebene trägt zum Schutz Ihrer Daten bei.

### Erforderlich für das Tracking von Klicks und Öffnungen

Braze führt die Transformation Ihrer Links mithilfe Ihrer markenspezifischen Link-Tracking-Subdomain durch, um Klicks und Öffnungen zu verfolgen. Standardmäßig beginnen diese Links mit HTTP. Nutzer:innen mit Browsern oder Erweiterungen, die nicht sicheren Datenverkehr einschränken, könnten Schwierigkeiten haben, die Weiterleitung vor der Ziel-URL zu passieren, selbst wenn die URL sicher ist. Dies kann zu fehlerhaften Bildern und ungenauem Tracking führen. Bitte wenden Sie SSL auf die Subdomain für das Link-Tracking an, um sichere Weiterleitungen zu gewährleisten.

### Browser-Anforderung

Gängige Browser wie Google Chrome beschränken den Datenverkehr über nicht sichere URLs, um die Nutzer:innen zu schützen. Die Verwendung von SSL trägt dazu bei, die Vertrauenswürdigkeit von Inhalten zu bestätigen und Probleme wie defekte Links und Bilder in E-Mails zu minimieren.

### HSTS-Domänen Anforderung 

Falls Sie über eine HTTP Strict Transport Security (HSTS)-Domain verfügen, richten Sie bitte SSL ein und konfigurieren Sie ein CDN, um die erforderlichen Sicherheitszertifikate zu senden. Ohne SSL funktionieren Bild- und Internet-Links nicht mehr.

## Erwerben eines SSL-Zertifikats

Erwerben Sie ein SSL-Zertifikat über einen Drittanbieter, in der Regel ein CDN. Ein CDN hostet das Zertifikat und stellt es dem Browser zur Verfügung, wenn eine Nutzer:in auf einen Link klickt, indem es den Datenverkehr über das CDN umleitet, um Zertifikate anzuwenden, bevor es an SendGrid oder SparkPost gesendet wird.

Um die SSL-Einrichtung zu starten, wenden Sie sich bitte an Ihren Braze-Customer-Success-Manager, um eine vollständige Braze-E-Mail-Einrichtung zu initiieren.

Nachdem Braze die Einrichtung initiiert hat, führen Sie bitte die folgenden Schritte aus:
1. Braze stellt Ihnen DNS-Einträge zur Verfügung, die Sie zu Ihrer Domainregistrierung hinzufügen können.
2. Braze prüft, ob die Datensätze korrekt zu Ihrer Registrierung hinzugefügt wurden.
3. Danach wählen Sie ein CDN aus und beziehen SSL-Zertifikate von einem Drittanbieter. 
4. An diesem Punkt richten Sie Ihr CDN ein. Beachten Sie, dass Braze nicht in der Lage ist, bei der Fehlerbehebung der CDN-Konfiguration zu helfen. Bitte wenden Sie sich für weitere Unterstützung an Ihren CDN-Anbieter.
5. Bitte wenden Sie sich an Ihren Customer-Success-Manager, um SSL zu aktivieren.

### Was ist ein CDN, und warum brauche ich es?

Ein Content Delivery Network (CDN) ist eine Plattform aus Servern, die schnelle Ladezeiten von Inhalten über mehrere Medien hinweg gewährleistet und gleichzeitig Sicherheitszertifikate verwaltet. 

{% alert important %}
Die CDN-Konfiguration erfolgt immer nach der Validierung Ihrer DNS-Einträge durch Braze. Sollten Sie diesen Schritt noch nicht eingeleitet haben, wenden Sie sich bitte an Ihren Customer-Success-Manager, um weitere Informationen zum Einstieg zu erhalten.
{% endalert %}

Für das Klick- und Öffnungs-Tracking wandeln die Partner Links mithilfe einer markenspezifischen Subdomain um, und das CDN wendet das SSL-Zertifikat auf diese umgewandelten Links an. Partner müssen häufig gültige Zertifikate an den Browser der Empfänger:innen übermitteln, damit Links und Bilder korrekt angezeigt werden. Da Braze keine Zertifikate anfragt oder verwaltet, müssen Sie dies über ein CDN einrichten. 

{% alert note %}
Sollten Sie die aufgeführten CDNs für SSL-Klick- und Öffnungs-Tracking nicht verwenden können oder wollen, können Sie eine angepasste SSL-Konfiguration einrichten. Alternative CDNs oder angepasste Proxys können zu einer komplexeren Konfiguration führen. Refernzieren Sie die Dokumentation von [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) und [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

#### Zusätzliche Ressourcen

{% alert important %}
Für die Fehlerbehebung Ihrer CDN-Konfiguration wenden Sie sich bitte an Ihren CDN-Anbieter.
{% endalert %}

Die folgende Tabelle enthält Schritt-für-Schritt-Anleitungen von ESP Partnern zur Konfiguration bestimmter CDNs. Auch wenn Ihr spezielles CDN nicht aufgeführt ist, müssen Sie sicherstellen, dass Ihr CDN die Möglichkeit hat, SSL-Zertifikate anzuwenden.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud-Plattform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Für Amazon SES, siehe [Option 2: Konfigurieren Sie eine HTTPS-Domain](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) und geben Sie die AWS-Tracking-Domain nach Region basierend auf Ihrem Braze-Cluster an:

- **Braze US-Cluster:** `r.us-east-1.awstrack.me`
- **Braze EU-Cluster:** `r.eu-central-1.awstrack.me`

{% alert important %}
Wenn Sie die Klick-Tracking-Domain Ihres CDN konfigurieren, aktivieren Sie bitte den`X-Forwarded-Host`Header, um potenzielle Sicherheitsprobleme wie Host-Header-Angriffe zu verhindern. Bitte referenzieren Sie die CDN-Dokumentation oder wenden Sie sich an Ihr Support-Team, um die erforderlichen Schritte zu erfahren.
{% endalert %}

#### Fehlersuche

Während Sie sich um die CDN-Konfiguration, Zertifikate und Proxy-Probleme mit Ihrem CDN kümmern sollten, können Sie diese Tipps nutzen, um häufige Probleme beim SSL-Klick-Tracking zu identifizieren.

##### Probleme mit der Domainregistrierung

Führen Sie einen Dig-Befehl aus, um sicherzustellen, dass Sie das Link-Tracking auf das CDN ausgerichtet haben. Bitte führen Sie in Ihrem Terminal . aus`dig CNAME link_tracking_subdomain`. Unter wird `ANSWER SECTION`aufgeführt, wohin Ihr CNAME verweist. Falls es auf den E-Mail-Anbieter (SendGrid oder SparkPost) und nicht auf Ihr CDN verweist, konfigurieren Sie bitte Ihre Domain neu, sodass sie auf Ihr CDN verweist.

##### CDN-Probleme

Sollten Live-E-Mail-Links während der Einrichtung nicht funktionieren, haben Sie wahrscheinlich DNS vor der ordnungsgemäßen Konfiguration auf Ihr CDN verwiesen. Dies kann als "falscher Link"-Fehler erscheinen. Bitte wenden Sie sich an Ihren CDN-Anbieter und überprüfen Sie dessen Dokumentation, um die Fehlerbehebung durchzuführen.

##### Status der SSL-Aktivierung

Wenn Sie die SSL-Einrichtung abgeschlossen haben und die Links weiterhin als HTTP angezeigt werden, wenden Sie sich bitte an Ihren Braze-Customer-Success-Manager, um zu bestätigen, dass Braze SSL aktiviert hat. Braze aktiviert SSL erst, nachdem alle Einrichtungsschritte abgeschlossen sind.

