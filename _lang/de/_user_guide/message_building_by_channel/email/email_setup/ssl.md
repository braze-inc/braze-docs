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

> Ein Secure Socket Layer (SSL) verschlüsselt eine URL mit HTTPS anstelle von HTTP. HTTPS zeigt an, dass ein gültiges und vertrauenswürdiges SSL- oder TLS-Zertifikat existiert und dass der Besuch der Website sicher ist.

## Warum ist SSL wichtig?

Für die meisten Domains ist SSL nicht erforderlich, aber Braze empfiehlt aus diesen Gründen dringend die Verwendung von SSL.

Die Sicherung Ihrer Website und Links mit SSL ist eine gängige Praxis, selbst für Unternehmen, die nicht direkt mit sensiblen Kundendaten arbeiten. Die Benutzer sind vertrauensvoller gegenüber Links, die mit SSL gesichert sind, und die zusätzliche Authentifizierungsebene trägt zum Schutz Ihrer Daten bei.

### Erforderlich für das Tracking von Klicks und Öffnungen

Braze transformiert Ihre Links unter Verwendung Ihrer gebrandeten Link Tracking Subdomain, um Klicks und Öffnungen zu tracken. Standardmäßig beginnen diese Links mit HTTP. Nutzer:innen mit Browsern oder Erweiterungen, die unsicheren Datenverkehr einschränken, haben möglicherweise Schwierigkeiten, die Umleitung vor der Ziel-URL zu passieren, selbst wenn die URL sicher ist. Dies kann zu fehlerhaften Bildern und ungenauem Tracking führen. Wenden Sie SSL auf die Subdomain des Link Tracking an, um sichere Weiterleitungen zu bestätigen.

### Browser-Anforderung

Wichtige Browser wie Google Chrome beschränken den Datenverkehr über unsichere URLs, um Nutzer:innen zu schützen. Die Verwendung von SSL bestätigt, dass die Inhalte vertrauenswürdig sind und minimiert Probleme wie defekte Links und Bilder in E-Mails.

### HSTS-Domänen Anforderung 

Wenn Sie eine HTTP Strict Transport Security (HSTS) Domain haben, richten Sie SSL ein und konfigurieren Sie ein CDN, um die erforderlichen Sicherheitszertifikate zu senden. Ohne SSL werden Bilder und Internet-Links unterbrochen.

## Erwerben eines SSL-Zertifikats

Erwerben Sie ein SSL-Zertifikat über einen Drittanbieter, in der Regel ein Content Delivery Network (CDN). Ein CDN hostet das Zertifikat und stellt es dem Browser zur Verfügung, wenn ein Nutzer:innen auf einen Link klickt, indem der Datenverkehr durch das CDN umgeleitet wird, um Zertifikate anzuwenden, bevor er an SendGrid oder SparkPost gesendet wird.

Um mit der SSL-Einrichtung zu beginnen, wenden Sie sich an Ihren Customer-Success-Manager:in von Braze, um eine vollständige E-Mail-Einrichtung von Braze zu veranlassen.

Nachdem Braze die Einrichtung gestartet hat, folgen Sie diesen Schritten:
1. Braze stellt Ihnen DNS-Einträge zur Verfügung, die Sie zu Ihrer Domainregistrierung hinzufügen können.
2. Braze prüft, ob die Datensätze korrekt zu Ihrer Registrierung hinzugefügt wurden.
3. Danach wählen Sie ein CDN aus und beziehen SSL-Zertifikate von einem Drittanbieter. 
4. An diesem Punkt richten Sie Ihr CDN ein. Beachten Sie, dass Braze nicht in der Lage ist, bei der Fehlerbehebung der CDN-Konfiguration zu helfen. Wenden Sie sich an Ihren CDN-Anbieter, wenn Sie weitere Hilfe benötigen.
5. Wenden Sie sich an Ihren Customer-Success-Manager:in, um SSL einzuschalten.

### Was ist ein CDN, und warum brauche ich es?

Ein Content Delivery Network (CDN) ist eine Plattform von Servern, die für schnelle Ladezeiten von Inhalten über mehrere Medien sorgt und gleichzeitig Sicherheitszertifikate verwaltet. 

{% alert important %}
Die CDN-Konfiguration erfolgt immer nach der Validierung Ihrer DNS-Einträge durch Braze. Wenn Sie diesen Schritt noch nicht eingeleitet haben, wenden Sie sich an Ihren Customer-Success-Manager:in, um weitere Informationen über die ersten Schritte zu erhalten.
{% endalert %}

Für das Tracking von Klicks und Öffnungen transformieren die Partner der Zustellung die Links unter Verwendung einer gebrandeten Subdomain und das CDN wendet das SSL-Zertifikat auf diese transformierten Links an. Partner müssen dem Browser des Empfängers häufig gültige Zertifikate vorlegen, damit Links und Bilder korrekt angezeigt werden. Da Braze keine Zertifikate anfordert oder verwaltet, müssen Sie dies über ein CDN einrichten. 

{% alert note %}
Wenn Sie die aufgelisteten CDNs für das SSL Tracking von Klicks und Öffnungen nicht verwenden können oder wollen, können Sie eine angepasste SSL-Konfiguration einrichten. Alternative CDNs oder angepasste Proxies können zu einer komplexeren Einrichtung führen. Lesen Sie die Dokumentation von [SendGrid](https://sendgrid.com/docs/ui/account-and-settings/custom-ssl-configurations/) und [SparkPost](https://www.sparkpost.com/docs/tech-resources/using-proxy-https-tracking-domain/).
{% endalert %}

#### Zusätzliche Ressourcen

{% alert important %}
Wenden Sie sich zur Fehlerbehebung bei Ihrer CDN-Konfiguration an Ihren CDN-Anbieter.
{% endalert %}

Die folgende Tabelle enthält Schritt-für-Schritt-Anleitungen von ESP Partnern zur Konfiguration bestimmter CDNs. Auch wenn Ihr spezielles CDN nicht aufgeführt ist, müssen Sie sicherstellen, dass Ihr CDN die Möglichkeit hat, SSL-Zertifikate anzuwenden.

| SendGrid | SparkPost |
| -------- | --------- |
| [AWS Cloudfront](https://support.sendgrid.com/hc/en-us/articles/4412701748891-How-to-configure-SSL-for-click-tracking-using-CloudFront)<br>[CloudFlare](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-cloudflare)<br>[Fastly](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-fastly)<br>[KeyCDN](https://sendgrid.com/docs/ui/sending-email/content-delivery-networks/#using-keycdn) | [AWS Cloudfront](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-aws-cloudfront)<br>[CloudFlare](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-cloudflare)<br>[Fastly](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-fastly)<br>[Google Cloud-Plattform](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-google-cloud-platform)<br>[Microsoft Azure](https://support.sparkpost.com/docs/tech-resources/enabling-https-engagement-tracking-on-sparkpost/#step-by-step-guide-with-microsoft-azure) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Für Amazon SES, siehe [Option 2: Konfigurieren einer HTTPS-Domain](https://docs.aws.amazon.com/ses/latest/dg/configure-custom-open-click-domains.html) und Festlegen der AWS Tracking Domain nach Region auf der Grundlage Ihres Braze-Clusters:

- **Braze US-Cluster:** `r.us-east-1.awstrack.me`
- **Braze EU-Cluster:** `r.eu-central-1.awstrack.me`

{% alert important %}
Wenn Sie die Click-Tracking Domain Ihres CDN konfigurieren, aktivieren Sie den `X-Forwarded-Host` Header, um potenzielle Sicherheitsprobleme wie Host-Header-Angriffe zu verhindern. Weitere Informationen finden Sie in der CDN Dokumentation oder bei Ihrem Team.
{% endalert %}

#### Fehlersuche

Während Sie sich um CDN-Konfiguration, Zertifikate und Proxy-Probleme mit Ihrem CDN kümmern sollten, nutzen Sie diese Tipps, um häufige Probleme beim SSL Click Tracking zu erkennen.

##### Probleme mit der Domainregistrierung

Führen Sie einen dig-Befehl aus, um zu bestätigen, dass Sie das Link Tracking auf das CDN richten. Führen Sie in Ihrem Terminal `dig CNAME link_tracking_subdomain` aus. Unter `ANSWER SECTION` wird aufgeführt, wohin Ihr CNAME verweist. Wenn er auf den Anbieter des E-Mail-Dienstes (SendGrid oder SparkPost) und nicht auf Ihr CDN verweist, konfigurieren Sie Ihre Domain-Registrierung so um, dass sie auf Ihr CDN zeigt.

##### CDN-Probleme

Wenn Live-E-Mail-Links während der Einrichtung nicht funktionieren, haben Sie wahrscheinlich DNS auf Ihr CDN gerichtet, bevor Sie es richtig konfiguriert haben. Dies kann als "falscher Link"-Fehler erscheinen. Wenden Sie sich an Ihren CDN-Anbieter und lesen Sie dessen Dokumentation zur Fehlerbehebung bei der Konfiguration.

##### Status der SSL-Aktivierung

Wenn Sie die SSL-Einrichtung abgeschlossen haben und die Links immer noch als HTTP erscheinen, wenden Sie sich an Ihren Customer-Success-Manager:in, um zu bestätigen, dass Braze SSL aktiviert hat. Braze aktiviert SSL erst, nachdem alle Einrichtungsschritte abgeschlossen sind.

