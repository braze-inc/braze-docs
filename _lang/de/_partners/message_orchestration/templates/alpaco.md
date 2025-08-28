---
nav_title: Alpaco
article_title: Alpaco
alias: /partners/Alpaco
description: "Die Integration von Braze und Alpaco erlaubt Ihnen den Export von Liquid-kompatiblen E-Mail-Templates und Content-Blöcken nach Braze, die Sie dann in E-Mails und In-App-Nachrichten verwenden können."
page_type: partner
search_tag: Partner
---

# Alpaco

> [Alpaco](https://alpaco.email/) ist ein Online Management-Tool, das einen Drag-and-Drop-Editor zur Erstellung wiederverwendbarer, markensicherer Inhalte für Braze bietet. Die Integration von Alpaco und Braze erlaubt es Ihnen, Content-Blöcke, E-Mail-Vorlagen und In-App-Nachricht-Vorlagen zu exportieren.

_Diese Integration wird von Alpaco gepflegt._

{% alert note %}
Alpaco unterstützt [alle Liquid-Variablen](https://shopify.github.io/liquid/) und somit auch alle Liquid-Variablen, die in Ihren Braze-Konfigurationen verwendet werden.
{% endalert %}

## Voraussetzungen

| Anforderung | Beschreibung |
| ------------| ----------- |
| Alpaco Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Alpaco-Konto. |
| Braze REST API-Schlüssel | Ein Braze REST API-Schlüssel mit vollständigen **Templates-Berechtigungen**. <br><br> Dieser kann im Braze-Dashboard unter **Einstellungen** > **API-Schlüssel** erstellt werden. |
| Cluster Instanz | Ihre [Braze-Cluster-Instanz]({{site.baseurl}}/api/basics/#endpoints) ist auf Ihr Braze-Dashboard und Ihren REST-Endpunkt abgestimmt. <br><br> Wenn Ihre Dashboard-URL zum Beispiel `https://dashboard-03.braze.com` lautet, ist Ihr Endpunkt `dashboard-03`. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Anwendungsfälle

- Exportieren Sie vollständig gestaltete **E-Mail-Vorlagen** zur Verwendung in Kampagnen und Messaging für Transaktionen.
- Erstellen und verwalten Sie **modulare Content-Blöcke** (e.g., Kopfzeilen, Fußzeilen, Aktionen), die über mehrere Kanäle hinweg wiederverwendet werden können.
- Entwerfen Sie ansprechende **In-App-Nachrichten** mit der gleichen kreativen Flexibilität wie E-Mails, so dass Sie auf einfache Weise konsistente, markengerechte Erlebnisse über alle Kanäle hinweg liefern können.
- Ermöglichen Sie die **Personalisierung** durch Einbindung von Liquid-Tags, die von Braze unterstützt werden, wie `{{first_name}}` oder `{{custom_attribute}}`.
- Sorgen Sie für **Markenkonsistenz**, indem Sie das kreative Design in Alpaco zentralisieren und Updates mit einem einzigen Export an Braze pushen.

## Integration

Stellen Sie dem Customer-Success-Team von Alpaco Ihren Braze REST API-Schlüssel und Ihre Cluster-Instanz zur Verfügung. Das Team wird dann die erste Integration für Sie einrichten.

{% alert note %}
Dies ist eine einmalige Einrichtung und alle zukünftigen Exporte werden automatisch diesen API-Schlüssel verwenden.
{% endalert %}

## Exportieren von Alpaco Nachrichten nach Braze

### Schritt 1: Erstellen Sie ein Template in Alpaco

Erstellen Sie in Alpaco ein Template, das Ihre Markenidentität zum Ausdruck bringt. Wenn Sie fertig sind, wählen Sie **Speichern**.

![Alpaco Template erstellen]({% image_buster /assets/img/alpaco/alpaco_1.png %})

### Schritt 2: Entwerfen Sie eine Nachricht unter Verwendung des Templates

Als Nächstes gehen Sie in die Alpaco-Lobby und verwenden Ihr Template, um eine E-Mail, eine In-App-Nachricht oder einen Content-Block zu erstellen. Um Ihre Nachricht vor dem Exportieren noch einmal zu überprüfen, wählen Sie **Überprüfen**.

![Alpaco E-Mail erstellen]({% image_buster /assets/img/alpaco/alpaco_2.png %})

### Schritt 3: Exportieren Sie Ihre Nachricht an Braze

Wählen Sie **Exportieren**, wählen Sie dann die Braze Integration und geben Sie an, ob Sie eine E-Mail-Vorlage oder einen Content-Block exportieren.

Wenn Sie nach dem Export Änderungen vornehmen, können Sie den Inhalt aus Alpaco erneut exportieren, um ihn in Braze zu aktualisieren.

![Alpaco Export email]({% image_buster /assets/img/alpaco/alpaco_3.png %})

## Verwendung von Alpaco-Templates und Blöcken in Braze

Je nach Art des Inhalts, den Sie exportieren, wird Ihr Template in einem der folgenden Abschnitte angezeigt:

- **Templates und Medien > E-Mail Templates**
- **Templates und Medien > Content-Blöcke**

Die Templates von Alpaco sind ideal für Unternehmen, die die Markenkonsistenz zentral verwalten möchten. Sie unterstützen auch die in Braze integrierten Tags zur einfachen Kategorisierung und Verwaltung von Inhalten.
