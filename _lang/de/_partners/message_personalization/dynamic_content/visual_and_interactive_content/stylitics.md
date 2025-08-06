---
nav_title: Stylitics
article_title: Stylitics
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Stylitics, einer cloudbasierten SaaS-Plattform, die es Ihnen erlaubt, Ihre bestehenden E-Mail Kampagnen mit ansprechenden und relevanten gebündelten Inhalten zu erweitern und so ein personalisiertes Kundenerlebnis zu schaffen."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> [Stylitics](https://stylitics.com/) ist eine cloudbasierte SaaS-Plattform für Einzelhändler, die visuelle Inhalte in großem Umfang automatisieren und verbreiten. Stylitics bündelt die Inspiration durch kontextuelle Produkte, stärkt das Kaufvertrauen und erhöht das Engagement, was letztendlich zu einem höheren durchschnittlichen Bestellwert und höheren Konversionsraten führt.

_Diese Integration wird von Stylitics gepflegt._

## Über die Integration

Die Integration von Braze und Stylitics erlaubt es Ihnen, Ihre bestehenden E-Mail Kampagnen mit ansprechenden und relevanten gebündelten Inhalten zu erweitern und so ein personalisiertes Kundenerlebnis zu schaffen.

![]({% image_buster /assets/img/stylitics.png %}){: style="max-width:60%;"}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Stylitics Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Stylitics-Konto](https://stylitics.com/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Im Folgenden finden Sie einige Beispiele für häufig getriggerte E-Mail-Programme:
- E-Mails über abgebrochene Einkäufe 
- Abgebrochene E-Mails durchsuchen 
- E-Mails zur Versandbestätigung
- E-Mails nach dem Kauf 

## Integration

Stylitics stellt für diese Integration Daten zur Verfügung. Ihr Anbieter von E-Mail-Diensten kann das Template für E-Mails erstellen oder aktualisieren, um Stylitics-Bundles einzubinden. Stylitics kann das Layout oder Design der E-Mails nicht verändern. 

1. Integrieren Sie das Bundle in die E-Mail. ESP bestimmt die Position und passt sie an.
2. ESP aktualisiert den triggernden Code für E-Mails, um Stylitics-Inhalte einzubeziehen.
3. ESP wird die durch Updates ausgelösten Serien testen, eine Vorschau anzeigen und starten. 

Stylitics stellt nur die Daten für die Artikel zur Verfügung. Sie und Ihr ESP verfügen über Nutzerdaten und können Stylitics-Bündeldaten einfügen, um sie an die Nutzer:innen zu senden.

## Datenaustausch

Die folgenden drei Ansätze erlauben es Ihnen, Stylitics-Bundles in Ihre getriggerten E-Mails einzubinden.

### 1\. API-Ansatz (empfohlen)

Sie oder Ihr ESP können pro Artikel einen API-Aufruf tätigen, um die Daten des Pakets in Ihre E-Mail einzupflegen. Stylitics empfiehlt Ihnen, seine API für API-Aufrufe zu verwenden, da sie sofort einsatzbereit ist.

{% alert note %}
Wenn Sie einen mit Stylitics durchgeführten A/B-Test durchführen, müssen die Parameter `styliticsCID` und `styliticsoverride` an die PDP-URLs der Stylitics-Artikel angehängt werden, auf die der Nutzer:innen in der E-Mail klickt.
<br><br>
Zum Beispiel, {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2\. Flat File Ansatz
Sie oder Ihr ESP können die Bundle-Daten eines Artikels in einer Flat File referenzieren, um Bundle-Daten in Ihre E-Mail einzufügen. Stylitics kann die Daten der Bündel in das CSV-, TXT- oder XML-Format umwandeln und Ihnen täglich zusenden. Sie können auch dabei helfen, das Dateiformat an die Anforderungen Ihres ESP anzupassen. Beachten Sie, dass die Erstellung dieser Datei 2-3 Wochen dauert.

#### Anforderungen:
- **Standort**: Stylitics kann die Datei auf dem Stylitics SFTP-Server ablegen, damit Sie sie täglich abholen können, oder Sie können Stylitics Ihre SFTP-Zugangsdaten schicken, um die Datei abzulegen. 
- **Zeit**: Stylitics wird die Datei täglich am Morgen abliefern. Lassen Sie sie wissen, ob Sie die Datei bis zu einem bestimmten Zeitpunkt benötigen. 
- **Datei-Schlüssel**: Sie und Stylitics müssen sich darauf einigen, auf welchen String der Artikel-Daten die Datei verschlüsselt werden soll, damit Ihr ESP die Daten referenzieren kann. SKU, `item_group_id`, oder `item_number` werden häufig verwendet. 

### 3\. Ansatz zur Extraktion von Daten auf der Website
Anbieter können das Frontend Ihrer Website nach Stylitics-Inhalten durchsuchen und gebündelte Daten in E-Mails einfügen. Es ist keine zusätzliche Arbeit von Stylitics erforderlich. 

## Best Practices für E-Mail Templates 

Sie und Ihr ESP erstellen ein HTML Template für E-Mails, um Stylitics Daten und Bundles einzufügen. Hier finden Sie einige bewährte Verfahren und Empfehlungen. 
- Anzeige von 2-4 Paketen in der E-Mail für den teuersten Artikel oder den ersten Vollpreisartikel, den die Nutzer:innen gekauft oder mit dem sie interagiert haben 
- Rufen Sie mehrere `item_numbers` auf und zeigen Sie die ersten Bündelreaktionen 
- Verfügen Sie über eine Fallback-Option, wenn für den Artikel keine Bundles verfügbar sind. 
	- Den Bereich ausblenden, in dem sich die Stylitics-Bundles befinden 
	- Bundles für den nächsten Artikel anzeigen, den der Nutzer:in angesehen hat 
- Zeigen Sie Bundle-Bilder und eine Liste von Produkttiteln und Miniaturbildern an, um sicherzustellen, dass der Nutzer:innen einen klaren Click-through hat.

{% alert note %}
Das Stylitics Widget JavaScript kann nicht in E-Mails eingefügt werden, da E-Mails kein JavaScript unterstützen.
{% endalert %}

## Analytics

Stylitics stellt die Daten für diese Art von E-Mail-Programmen zur Verfügung. Daher bitten wir um eine Öffnung der Daten zwischen Ihnen, Ihrem ESP und Stylitics. Wenn möglich, hoffen wir, die folgenden Metriken von Ihnen zu erhalten, um den Auftrieb zu verstehen und das Programm zu verbessern:
- Versendete E-Mails 
- Geöffnete E-Mails 
- Ansichten und Engagement 
- Click-through-Rate 
- Zu den Taschen hinzufügen 
- Käufe

## Nächste Schritte 

Wenden Sie sich an Ihren Account Manager:in von Stylitics, um die nächsten Schritte und den Zeitplan für das E-Mail-Programm zu koordinieren. Einige nächste Schritte sind: 
- Entscheiden Sie, welche E-Mails Sie verwenden möchten
- Setzen Sie sich mit Stylitics und Ihrem ESP in Verbindung, um den Datenaustausch zu besprechen und über die Option API oder Flat File zu entscheiden. 
- Erstellen Sie Mockups mit Ihrem ESP 
- Auf Analytics ausrichten 
- Auf den Zeitplan der Markteinführung abstimmen 


