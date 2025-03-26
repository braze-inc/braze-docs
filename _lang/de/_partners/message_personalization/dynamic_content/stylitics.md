---
nav_title: Stylitics
article_title: Stylitics
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Stylitics, einer Cloud-basierten SaaS-Plattform, die es Ihnen ermöglicht, Ihre bestehenden E-Mail-Kampagnen mit ansprechenden und relevanten gebündelten Inhalten zu erweitern und so ein personalisiertes Kundenerlebnis zu schaffen."
alias: /partners/stylitics/
page_type: partner
search_tag: Partner

---

# Stylitics

> [Stylitics](https://stylitics.com/) ist eine Cloud-basierte SaaS-Plattform für Einzelhändler, um visuelle Inhalte in großem Umfang zu automatisieren und zu verbreiten. Stylitics-Bundles inspirieren durch die Kontextualisierung von Produkten, stärken das Kaufvertrauen und erhöhen das Engagement, was letztendlich zu einem höheren durchschnittlichen Bestellwert und höheren Konversionsraten führt.

Die Integration von Braze und Stylitics ermöglicht es Ihnen, Ihre bestehenden E-Mail-Kampagnen mit ansprechenden und relevanten gebündelten Inhalten zu erweitern und so ein personalisiertes Kundenerlebnis zu schaffen.

![][0]{: style="max-width:60%;"}

## Voraussetzungen

| Anforderung | Beschreibung |
| ----------- | ----------- |
| Stylitics Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein [Stylitics-Konto](https://stylitics.com/). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Anwendungsfälle

Im Folgenden finden Sie einige Beispiele für gängige E-Mail-Programme:
- E-Mails zu abgebrochenen Warenkörben 
- Abgebrochene Such-E-Mails 
- Versandbestätigungs-E-Mails
- E-Mails nach dem Kauf 

## Integration

Stylitics stellt für diese Integration Datenpakete zur Verfügung. Ihr E-Mail-Dienstleister kann die E-Mail-Vorlage so erstellen oder aktualisieren, dass sie Stylitics-Bundles enthält. Stylitics kann das Layout oder Design der E-Mails nicht ändern. 

1. Integrieren Sie das Bündel in die E-Mail. ESP bestimmt die Position und die Anpassung.
2. ESP aktualisiert den Trigger-E-Mail-Code, um Stylitics-Inhalte einzubeziehen.
3. ESP wird die Updates testen, eine Vorschau anzeigen und die ausgelöste Serie starten. 

Stylitics stellt nur die Daten der Pakete für die Artikel zur Verfügung. Sie und Ihr ESP verfügen über Benutzerdaten und können Stylitics-Bündeldaten einfügen, um sie an die Benutzer zu senden.

## Datenaustausch

Mit den folgenden drei Methoden können Sie Stylitics-Bundles in Ihre Trigger-E-Mails einbinden.

### 1\. API-Ansatz (empfohlen)

Sie oder Ihr ESP können pro Artikel einen API-Aufruf tätigen, um die Daten des Pakets in Ihre E-Mail zu übertragen. Stylitics empfiehlt Ihnen, seine API für API-Aufrufe zu verwenden, da sie sofort einsatzbereit ist.

{% alert note %}
Wenn Sie einen mit Stylitics durchgeführten A/B-Test durchführen, müssen die Parameter `styliticsCID` und `styliticsoverride` an die PDP-URLs der Stylitics-Artikel angehängt werden, auf die der Benutzer in der E-Mail klickt.
<br><br>
Zum Beispiel, {% raw %}`&styliticsoverride=001?styliticsCID=email[clientname]`{% endraw %}
{% endalert %}

### 2\. Flat File Ansatz
Sie oder Ihr ESP können auf die Bundle-Daten eines Artikels in einer flachen Datei verweisen, um die Bundle-Daten in Ihre E-Mail einzufügen. Stylitics kann Bündeldaten in das CSV-, TXT- oder XML-Format umwandeln und Ihnen diese täglich zusenden. Sie können auch dabei helfen, das Dateiformat an die Anforderungen Ihres ESP anzupassen. Beachten Sie, dass die Erstellung dieser Datei 2-3 Wochen dauert.

#### Anforderungen:
- **Standort**: Stylitics kann die Datei auf dem Stylitics SFTP ablegen, so dass Sie sie täglich abholen können, oder Sie können Stylitics Ihre SFTP-Zugangsdaten schicken, um die Datei abzulegen. 
- **Zeit**: Stylitics wird die Datei täglich am Morgen abliefern. Lassen Sie sie wissen, ob Sie die Datei bis zu einem bestimmten Zeitpunkt benötigen. 
- **Datei-Schlüssel**: Sie und Stylitics müssen sich darauf einigen, auf welche Artikeldatenfolge die Datei verschlüsselt werden soll, damit Ihr ESP die Daten referenzieren kann. SKU, `item_group_id`, oder `item_number` werden häufig verwendet. 

### 3\. Ansatz zur Extraktion von Website-Daten
Anbieter können das Frontend Ihrer Website nach Stylitics-Inhalten durchsuchen und gebündelte Daten in E-Mails einfügen. Es ist keine zusätzliche Arbeit von Stylitics erforderlich. 

## Bewährte Verfahren für E-Mail-Vorlagen 

Sie und Ihr ESP erstellen eine HTML-E-Mail-Vorlage, in die Sie Stylitics-Daten und -Bundles einfügen. Hier finden Sie einige bewährte Verfahren und Empfehlungen. 
- Anzeige von 2-4 Bundles in der E-Mail für den teuersten Artikel oder den ersten Vollpreisartikel, den der Benutzer gekauft oder mit dem er interagiert hat 
- Rufen Sie mehrere `item_numbers` auf und zeigen Sie die ersten Bündelreaktionen 
- Haben Sie eine Ausweichoption, wenn keine Bundles für den Artikel verfügbar sind. 
	- Den Bereich ausblenden, in dem die Stylitics-Bundles liegen 
	- Bundles für den nächsten Artikel anzeigen, den der Benutzer angesehen hat 
- Zeigen Sie Bilder von Produktpaketen und eine Liste von Produkttiteln und Miniaturbildern an, um sicherzustellen, dass der Benutzer einen eindeutigen Click-Through hat.

{% alert note %}
Das Stylitics Widget JavaScript kann nicht in E-Mails eingefügt werden, da E-Mails kein JavaScript unterstützen.
{% endalert %}

## Analytics

Stylitics stellt die Paketdaten für diese Art von E-Mail-Programm zur Verfügung. Daher bitten wir um eine offene Datenfreigabe zwischen Ihnen, Ihrem ESP und Stylitics. Wenn möglich, hoffen wir, von Ihnen die folgenden Metriken zu erhalten, um den Auftrieb zu verstehen und das Programm zu verbessern:
- Gesendete Emails 
- Geöffnete Emails 
- Ansichten und Engagements 
- Durchklickrate 
- Zu den Taschen hinzufügen 
- Käufe

## Nächste Schritte 

Wenden Sie sich an Ihren Stylitics-Kundenbetreuer, um die nächsten Schritte und Zeitpläne für das E-Mail-Programm zu koordinieren. Einige nächste Schritte sind: 
- Entscheiden Sie, welche E-Mails Sie verwenden möchten
- Setzen Sie Stylitics mit Ihrem ESP in Verbindung, um den Datenaustausch zu besprechen und zu entscheiden, ob Sie eine API-Option oder eine Flat-File-Option wünschen. 
- Erstellen Sie Mockups mit Ihrem ESP 
- Auf Analysen abstimmen 
- Auf den Zeitplan der Markteinführung abstimmen 

[0]: {% image_buster /assets/img/stylitics.png %}