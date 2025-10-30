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

> Ein Secure Socket Layer (SSL) verschlüsselt eine URL mit HTTPS anstelle des weniger sicheren HTTP. HTTPS in einer URL zeigt an, dass ein gültiges und vertrauenswürdiges SSL- oder TLS-Zertifikat vorhanden ist und dass die Website sicher ist und keine Quelle für gefährliche Malware darstellt.

## Warum ist SSL wichtig?

Obwohl die meisten Domains kein SSL benötigen, empfiehlt Braze die Verwendung von SSL aus diesen wichtigen Gründen.

Die Sicherung Ihrer Website und Links mit SSL ist eine gängige Praxis, selbst für Unternehmen, die nicht direkt mit sensiblen Kundendaten arbeiten. Die Benutzer sind vertrauensvoller gegenüber Links, die mit SSL gesichert sind, und die zusätzliche Authentifizierungsebene trägt zum Schutz Ihrer Daten bei.

### Erforderlich für das Tracking von Klicks und Öffnungen

Wenn wir bei Braze E-Mails versenden, wandeln wir Ihre Links zunächst mit Ihrer eigenen Link-Tracking-Subdomain um, um die Klicks und Öffnungen der Benutzer zu verfolgen. Diese Links beginnen standardmäßig mit HTTP. Das bedeutet, dass Nutzer:innen mit einem Browser oder einer Erweiterung, die den unsicheren Datenverkehr einschränken, möglicherweise Schwierigkeiten haben, die Umleitung zu passieren, bevor sie auf der Ziel-URL landen, selbst wenn die URL sicher ist. Dies kann zu fehlerhaften Bildern und ungenauem Tracking von Klicks und Öffnungen in Ihren E-Mails führen. Aus diesem Grund empfiehlt es sich, eine SSL-Schicht auf die Subdomain für die Linkverfolgung anzuwenden, um sichere Weiterleitungen in Ihren E-Mails zu bestätigen. 

### Browser-Anforderung

SSL-Protokolle werden heute immer häufiger verwendet, da große Browser wie Google Chrome damit beginnen, den Datenverkehr über unsichere URLs zu beschränken, um ihre Benutzer zu schützen. Unternehmen mit SSL auf ihrer Website bestätigen diesen wichtigen Browsern, dass ihre Inhalte vertrauenswürdig sind, wodurch Probleme bei der Anzeige von Inhalten wie fehlerhafte Links und Bilder in ihren E-Mails minimiert werden.

### HSTS-Domänen Anforderung 

Unabhängig davon, mit welchen Browsern Ihre Benutzer auf Ihre E-Mails zugreifen, müssen Sie SSL einrichten, wenn Sie eine HTTP Strict Transport Security (HSTS)-Domäne haben, und ein CDN konfigurieren, um die erforderlichen Sicherheitszertifikate zu senden. Wenn Sie SSL nicht einrichten, werden sowohl Bild- als auch Weblinks unterbrochen.

## Erwerben eines SSL-Zertifikats

Sie können ein SSL-Zertifikat über einen Drittanbieter erwerben, in der Regel ein Content Delivery Network (CDN). Ein CDN kann das SSL-Zertifikat hosten und es dem Browser jedes Mal zur Verfügung stellen, wenn auf einen Ihrer Links geklickt wird. Dies geschieht, indem der Datenverkehr durch das CDN umgeleitet wird, um die erforderlichen Zertifikate anzuwenden, bevor er an unsere E-Mail-Partner SendGrid oder SparkPost weitergeleitet wird.

Um mit der SSL-Einrichtung zu beginnen, wenden Sie sich an Ihren Customer-Success-Manager von Braze, um eine vollständige E-Mail-Einrichtung von Braze vorzunehmen.

Nachdem Braze diese Einrichtung eingeleitet hat, folgen Sie diesen Schritten:
1. Braze stellt Ihnen DNS-Einträge zur Verfügung, die Sie zu Ihrer Domainregistrierung hinzufügen können.
2. Braze prüft, ob die Datensätze korrekt zu Ihrer Registrierung hinzugefügt wurden.
3. Danach wählen Sie ein CDN aus und beziehen SSL-Zertifikate von einem Drittanbieter. 
4. An diesem Punkt richten Sie Ihr CDN ein. Beachten Sie, dass Braze nicht in der Lage ist, bei der Fehlerbehebung der CDN-Konfiguration zu helfen. Wenden Sie sich an Ihren CDN-Anbieter, wenn Sie weitere Hilfe benötigen.
5. Wenden Sie sich an Ihren Customer Success Manager, um SSL zu aktivieren.

### Was ist ein CDN, und warum brauche ich es?

Ein Content Delivery Network (CDN) ist eine Plattform von Servern, die für schnelle Ladezeiten von hochwertigen Inhalten über verschiedene Medien sorgen und gleichzeitig Sicherheitszertifikate verwalten. 

{% alert important %}
Die CDN-Konfiguration erfolgt immer nach der Validierung Ihrer DNS-Einträge durch Braze. Wenn Sie diesen Schritt noch nicht eingeleitet haben, wenden Sie sich an Ihren Customer-Success-Manager, um weitere Informationen über die ersten Schritte zu erhalten.
{% endalert %}

Bei Braze wandeln unsere Partner für die Nachverfolgung von Klicks und Öffnungen die Links mithilfe einer gebrandeten Subdomain um, und das CDN wendet das SSL-Zertifikat auf diese neu umgewandelten Links an. Oft müssen unsere Versandpartner dem Browser Ihres E-Mail-Empfängers gültige und vertrauenswürdige Zertifikate vorlegen, damit Links und Bilder korrekt angezeigt werden können. Da Braze solche Zertifikate nicht anfordert oder verwaltet, muss dies auf Ihrer Seite über ein CDN eingerichtet werden. 

{% alert note %}
Wenn Sie die aufgelisteten CDNs bei der Einrichtung von SSL für die Verfolgung von Klicks und Öffnungen nicht verwenden können oder möchten, können Sie eine benutzerdefinierte SSL-Konfiguration einrichten. Beachten Sie, dass alternative CDNs oder angepasste Proxys zu einer komplexeren und differenzierteren Einrichtung führen können. Lesen Sie die Artikel von [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) und [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/) zu diesem Thema.
{% endalert %}

#### Zusätzliche Ressourcen

{% alert important %}
Für weitere Hilfe bei der Fehlerbehebung Ihrer CDN-Konfiguration müssen Sie sich an Ihren CDN-Anbieter wenden.
{% endalert %}

Die folgende Tabelle enthält Schritt-für-Schritt-Anleitungen von ESP Partnern zur Konfiguration bestimmter CDNs. Auch wenn Ihr spezielles CDN nicht aufgeführt ist, müssen Sie sicherstellen, dass Ihr CDN die Möglichkeit hat, SSL-Zertifikate anzuwenden.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud-Plattform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Für Amazon SES, siehe [Option 2: Konfiguration einer HTTPS-Domain](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) und Angabe der AWS Tracking Domain nach Ihrer Region auf der Grundlage Ihres Braze-Clusters:

- **Braze US-Cluster:** `r.us-east-1.awstrack.me`
- **Braze EU-Cluster:** `r.eu-central-1.awstrack.me`

{% alert important %}
Wenn Sie die Click-Tracking Domain Ihres CDN konfigurieren, stellen Sie sicher, dass Sie den `X-Forwarded-Host` Header aktivieren. Dies dient dazu, potenzielle Sicherheitsprobleme, wie z.B. Host-Header-Angriffe, zu verhindern. Informieren Sie sich in der Dokumentation des CDN oder bei Ihrem Team über die Vorgehensweise, da diese je nach CDN unterschiedlich ist.
{% endalert %}

#### Fehlersuche

Während CDN-Konfiguration, Zertifikate und Proxy-Probleme mit Ihrem CDN geklärt werden sollten, finden Sie hier einige allgemeine Tipps zur Fehlerbehebung, um häufige Probleme bei der Einrichtung des SSL-Click-Tracking zu identifizieren.

##### Probleme mit der Domainregistrierung

Mit dem Befehl dig können Sie feststellen, ob Sie Ihr Link Tracking auf das CDN richten. Dies können Sie in Ihrem Terminal tun, indem Sie `dig CNAME link_tracking_subdomain` ausführen. Nachdem der Befehl ausgeführt wurde, sollte unter `ANSWER SECTION` aufgelistet werden, worauf Ihr CNAME verweist. Wenn er auf den von Ihnen gewählten Anbieter von E-Mail-Diensten (SendGrid oder SparkPost) und nicht auf Ihr CDN zeigt, versuchen Sie, Ihre Domain-Registrierung so umzukonfigurieren, dass sie auf Ihr CDN zeigt.

##### CDN-Probleme

Wenn Ihre Live-E-Mail-Links während der Einrichtung nicht mehr funktionieren, bedeutet dies in der Regel, dass Sie Ihr DNS auf Ihr CDN gerichtet haben, ohne dass es richtig konfiguriert wurde. Dies kann als "falscher Link"-Fehler erscheinen. Wenden Sie sich an Ihren CDN-Anbieter und lesen Sie dessen Dokumentation, um die Fehlerbehebung bei Ihrer CDN-Konfiguration zu unterstützen.

##### Status der SSL-Aktivierung

Wenn Sie Ihre SSL-Einrichtung abgeschlossen haben und Ihre Links immer noch als HTTP und nicht als HTTPS angezeigt werden, wenden Sie sich an Ihren Braze Customer Success Manager, um sicherzustellen, dass SSL von Braze aktiviert wurde. SSL kann von Braze erst dann aktiviert werden, wenn alle Aspekte Ihrer SSL-Einrichtung abgeschlossen sind.

