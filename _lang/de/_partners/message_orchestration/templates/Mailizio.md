---
nav_title: Mailizio
article_title: Mailizio
alias: /partners/mailizio
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Mailizio, einer Plattform zur Erstellung und Verwaltung von E-Mails, mit der Sie wiederverwendbare, markensichere Inhalte erstellen und nach Braze exportieren können."
page_type: partner
search_tag: Partner

---

# Mailizio

> [Mailizio](https://mailizio.com/) ist eine Plattform zur Erstellung und Verwaltung von E-Mails, mit der Sie wiederverwendbare, markensichere Inhalte mit einem intuitiven visuellen Editor erstellen können. Mit der Integration von Mailizio in Braze können Sie Ihre Content-Blöcke und E-Mail-Templates exportieren und dann automatisch In-App-Nachrichten aus denselben Assets generieren, was eine schnelle und vollständig kontrollierte Bereitstellung von Kampagnen ermöglicht.

_Diese Integration wird von Mailizio gepflegt._

## Über die Integration

Mit der Integration von Mailizio und Braze können Sie dynamische E-Mail-Templates mit dem Mailizio-Editor entwerfen, Liquid-Variablen nutzen, wie sie in Ihren Braze-Konfigurationen verwendet werden, und diese für eine optimierte Ausführung der Kampagne an Braze pushen.

## Anwendungsfälle

- Pushen Sie versandfertige E-Mail-Templates für Kampagnen und Transaktionsnachrichten direkt in Braze.
- Erstellen Sie wiederverwendbare Inhaltsmodule (Kopfzeilen, Fußzeilen, Aktionen und mehr), um die Produktion über mehrere Kampagnen und Kanäle hinweg zu optimieren.
- Generieren Sie In-App-Nachrichten aus E-Mails: Mailizio identifiziert relevante Abschnitte Ihrer E-Mail und lässt Sie den HTML-Code zur Verwendung in Ihren In-App Kampagnen exportieren.
- Personalisieren Sie in großem Umfang mit Liquid-Variablen, die mit Braze kompatibel sind, sowohl in E-Mails als auch in In-App-Nachrichten.
- Halten Sie Ihr Branding konsistent, indem Sie Ihre kreativen Assets in Mailizio verwalten und in Braze mit einem einzigen Export aktualisieren.

## Voraussetzungen

| Anforderung | Beschreibung |                          
| ----------- | ----------- |  
| Mailizio-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Mailizio-Konto. |  
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Templates-Berechtigungen**.<br><br>Sie können einen Braze REST API-Schlüssel im Braze-Dashboard unter **Einstellungen** > API-Schlüssel erstellen. |  
| Braze REST Endpunkt | [Ihre URL für den REST-Endpunkt]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Ihr Endpunkt hängt von der Braze-URL für Ihre Instanz ab. |  
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integration

Stellen Sie Ihrem Mailizio Customer-Success-Manager Ihren Braze REST API-Schlüssel und Ihre Cluster-Instanz zur Verfügung. Das Mailizio Team richtet dann die erste Integration für Sie ein.

{% alert important %}
Dies ist eine einmalige Einrichtung, und alle zukünftigen Exporte verwenden automatisch diesen API-Schlüssel.
{% endalert %}

### Schritt 1: Erstellen Sie eine E-Mail in Mailizio

Erstellen Sie in Mailizio mit dem Drag-and-Drop-Editor eine E-Mail, die Ihre Markenidentität widerspiegelt, und klicken Sie dann auf **Speichern**, um Ihre Arbeit zu sichern.

![Drag-and-Drop-Editor Bildschirmfoto]({% image_buster /assets/img/mailizio/screenshot_1.png %})

### Schritt 2: Exportieren Sie Ihr Template für E-Mails nach Braze

Wenn Sie fertig sind, klicken Sie auf **Newsletter exportieren**. Wählen Sie im Popup-Fenster **Braze-email** und bestätigen Sie den Export.

Wenn Sie Ihre Inhalte später aktualisieren, exportieren Sie sie erneut aus Mailizio, um sie in Braze zu aktualisieren.

![Bildschirmfoto Modal exportieren]({% image_buster /assets/img/mailizio/screenshot_2.png %})

{% alert important %}  
Sie können Content-Blöcke auf die gleiche Weise mit dem **Modul-Editor** von Mailizio erstellen und exportieren.  
{% endalert %}

## Nutzung

Ihre hochgeladene Mailizio-Vorlage finden Sie in Ihrem Braze-Konto im Bereich **Templates & Medien > E-Mail-Vorlagen**. Mit dieser E-Mail-Vorlage können Sie jetzt damit beginnen, ansprechende Nachrichten an Ihre Kund:in zu versenden!
