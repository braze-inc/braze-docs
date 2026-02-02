---
nav_title: Google Mail Aktionen einrichten
article_title: Gmail-Aktionen einrichten
page_order: 8
description: "In diesem Artikel erfahren Sie, wie Sie mit Braze die Gmail-Karte für Mobilgeräteaktionen aus E-Mail-Kampagnen erstellen."
channel:
  - email
toc_headers: h2
---

# Gmail Promotion einrichten

> Der [Gmail-Tab Mobilgeräteaktionen](https://developers.google.com/gmail/promotab/) erlaubt es Marketern, mittels Anmerkungen neben Betreffzeile oder Preheader-Daten weitere Informationen in Karten zu versenden. Braze verfügt über ein integriertes Tool, mit dem Sie die Karte aus Ihrer E-Mail-Kampagne erstellen können.

## Voraussetzung

Leiten Sie zunächst Ihre Domains und Subdomains an das Team von Google Promotions Tab unter <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> weiter, damit sie in die Zulassungsliste von Gmail aufgenommen werden. So können Sie Features mit reichhaltigen Bildern wie das Produktkarussell im Aktions-Tab von Gmail verwenden.

## Karten in Braze erstellen

Befolgen Sie diese Anleitung, um eine Gmail-Aktionskarte für eine E-Mail-Kampagne zu erstellen. Beachten Sie, dass das Verlassen des Bereichs **Inhalt** im Editor die Felder und Informationen auf der Registerkarte **Google Mail Werbung** zurücksetzt. Schließen Sie die Einrichtung der Aktionskarte ab und kopieren Sie den generierten HTML-Code, damit Sie ihn nicht verlieren.

### Schritt 1: Erstellen Sie eine E-Mail Kampagne

[Erstellen Sie]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) zunächst [Ihre E-Mail Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) und wählen Sie den **HTML Code-Editor** als Bearbeitungsumgebung aus.

### Schritt 2: Details zur Gmail Aktion Karte hinzufügen

Gehen Sie als nächstes in den Bereich **Inhalt** des HTML-Editors und wählen Sie den Tab **Google Mail Aktion** aus. Füllen Sie die Felder unter **Grundlegende Informationen** aus und wählen Sie dann **HTML-Code generieren**. Dies wird Ihnen helfen, das Skript für Ihre Gmail Promo-Tab-Karte unter dem Abschnitt **Kopieren und Einfügen des HTML-Codes in `<Head>`** zu erstellen.

![Ein Beispiel dafür, wie Sie eine Karte erstellen können.]({% image_buster /assets/img/create-gmail-promo.png %})

### Schritt 3: Passen Sie Ihre Gmail-Aktion-Karte an

Wählen Sie, ob Sie ein Rabattangebot, eine Deal-Karte, eine Aktionskarte oder alle Optionen für Ihre Gmail Promotion-Karte einfügen möchten.

{% tabs %}
{% tab Discount offer %}

Wenn Sie ein Rabattangebot einrichten, können Sie die Gültigkeitsdaten für einen Rabatt festlegen. 

1. Wählen Sie das Kästchen **Rabattangebot** aus.
2. Geben Sie bei **Angebot** eine kurze Zusammenfassung für den Rabatt ein. Ein Beispiel ist "20% Rabatt".
3. Für **Code** fügen Sie den Aktionscode ein, den ein Nutzer:innen an der Kasse anwenden muss.
4. Wählen Sie dann das Startdatum und die Uhrzeit für das Rabattangebot aus.
5. Legen Sie fest, ob das Rabattangebot zu einem bestimmten Zeitpunkt oder nie enden soll.

![Optionen zur Angabe von Angebotswert, Code sowie Anfangsdatum und -uhrzeit eines Rabattangebots.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal Cards %}

Verwenden Sie Deal Cards, um wichtige Informationen direkt am Anfang von E-Mails bereitzustellen. Dies erlaubt es Empfängern:in, die Details des Angebots schnell zu verstehen und zu handeln. Sie können zum Beispiel Deal Cards verwenden, um zeitlich begrenzte Aktionen zu bewerben und den Nutzer:innen die Suche nach Details in E-Mails zu ersparen.

1. Wählen Sie das Umschalten der **Deal Card**.
2. Geben Sie bei **Angebot** eine kurze Zusammenfassung für den Rabatt ein. Ein Beispiel ist "20% Rabatt auf alle Schuhe".
3. (optional) Fügen Sie für **Code** den Aktionscode hinzu, den ein Nutzer:innen beim Checkout anwenden muss.
4. Geben Sie mindestens eine der folgenden URLs ein. 
-  **URL der Angebotsseite:** Die URL für die Landing Page des spezifischen Angebots. Dadurch wird ein Button "Jetzt einkaufen" (oder ein ähnlicher Button) erstellt. Wir empfehlen, diese URL für Ihre Deal Card anzugeben. 
- **Händler-Homepage-URL:** Die URL für Ihre Hauptseite. Verwenden Sie dieses Feld nur, wenn die URL einer bestimmten Angebotsseite nicht verfügbar ist.
5. (optional) Fügen Sie ein Startdatum für das Angebot hinzu.
6. Legen Sie fest, ob das Angebot zu einem bestimmten Zeitpunkt oder nie enden soll.

![Optionen zur Angabe des Angebotswertes, des Codes sowie des Startdatums und der Startzeit für eine Deal Card.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Promotion cards %}

Aktionskarten im Produktkarussell sind hilfreich, um Ihr Angebot zu bebildern. Sie können die Variablen des Produktkarussells anpassen und bis zu zehn eindeutige Vorschaubilder einfügen.

1. Wählen Sie das Umschalten der **Aktion Karten**.
2. Wählen Sie **Aktionskarte hinzufügen**. Jedes Bild in Ihrem Produktkarussell muss eine eindeutige URL haben und das gleiche Seitenverhältnis verwenden (4:5, 1:1, 1,91:1).
3. Fügen Sie eine Bild-URL ein.
4. Fügen Sie unter **Targeting URL** den Link für Ihre Aktion hinzu.

{% alert tip %}
Wir empfehlen Ihnen, Ihre Produktbilder in die Bibliothek hochzuladen und dann die URLs zu kopieren und in die entsprechenden Felder einzufügen. Es werden nur statische Bildformate (PNG und JPEG) akzeptiert. Einige Bildformate (GIF) werden zwar hochgeladen, aber nicht wie erwartet angezeigt.
{% endalert %}

{: start="5"}
5\. Passen Sie Ihre Aktionskarte an, indem Sie eine Überschrift, eine Währung, einen Preis und einen Rabattwert hinzufügen.

| Anpassbare Eigenschaft | Beschreibung |
|---|---|
| Überschrift | (optional) Eine ein- oder zweisätzige Beschreibung der Werbeaktion. Wird unter dem Vorschaubild angezeigt. |
| Währung | (optional) Die Währung des Preises. |
| Preis | Der Preis der Aktion. |
| Rabattwert | Der vom ursprünglichen Preis abgezogene Betrag. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Ein Beispiel für ein Produktkarussell eines Unternehmens namens Motto mit der E-Mail-Überschrift "Unsere meistverkauften Socken sind im Angebot", mit drei Bildern von Socken und ihren ermäßigten Preisen.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### Schritt 4: HTML Code generieren und einfügen

Nachdem Sie Ihre Gmail Aktionskarte erstellt haben, wählen Sie **HTML-Code generieren**. Kopieren Sie das Skript und fügen Sie es in das `<head>` Element im HTML-Code Ihrer E-Mail ein. 

{% alert tip %}
Kopieren Sie für den Drag-and-Drop-Editor den generierten HTML-Code und fügen Sie ihn in den Abschnitt [angepasste Head Tags]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#custom-head-tags) unter **Sendeeinstellungen** ein.
{% endalert %}

{% alert warning %}
Das Aktionsskript erscheint nur, wenn Ihre E-Mail im Aktions-Tab von Gmail landet. Derzeit verwendet Gmail Algorithmen, um zu entscheiden, wo Ihre E-Mail landet. Wenn ein Nutzer Ihre E-Mail jedoch als Werbeaktion markiert, wird der Algorithmus von Google Mail ignoriert, und Ihre E-Mail landet automatisch auf der Registerkarte Werbeaktionen.
{% endalert %}

## Bewährte Praktiken

Halten Sie sich im Allgemeinen an diese [von Google Mail empfohlenen bewährten Verfahren](https://developers.google.com/gmail/promotab/best-practices). 

{% alert tip %}
Sie können Liquid zwar in diesem Skript verwenden, aber wir empfehlen Ihnen dringend, Ihre Nachrichten so oft wie möglich zu testen, um einen Fehler zu vermeiden.
{% endalert %}

## Messen von Gmail-Karten

Gmail liefert keine Analytics für diese Karten, und E-Mail-Dienstleister (ESP) wie Braze können kein eigenes Link Tracking für Links in der Kopfzeile einfügen (einschließlich Aktionskarten und Produktkarussells). Sie können jedoch während der Einrichtung UTM-Parameter oder eindeutige Codes an die URLs anhängen. Mit diesen Parametern können Sie das Engagement mit Ihrem eigenen Website Analytics oder Konversion Tracking verfolgen, da das Tracking Teil der URL selbst ist und nicht vom ESP eingefügt wird. Klick Tracking auf ESP-Ebene ist für diese Links nicht verfügbar.

### Bilder einbinden

Gmail hat mit aussagekräftigen Bildern zur E-Mail bessere Ergebnisse festgestellt. Gmail rät von reinem Text ab, da ansonsten die für das E-Mail Marketing so wichtige Bildsprache in der Vorschau fehlt. Verwenden Sie keine Bilder mit abgeschnittenem Text oder wiederholte Bilder in mehreren Kampagnen.

### Angebote beschreiben

Gmail rät davon ab, Sätze oder Phrasen zu verwenden, wie z. B. "Sie können 1 Gratis kaufen oder Rabatt auf alle Shorts und Hemden", da diese möglicherweise abschneiden, nicht mehr ins Auge fallen und mit der Betreffzeile konkurrieren. Dieser Bereich sollte nur dazu verwendet werden, Ihre Kunden für Ihre Nachrichten zu interessieren. Vermeiden Sie also Formulierungen wie "Öffnen Sie diese E-Mail jetzt" oder "Klicken Sie hier für Angebote". Vermeiden Sie es, einfach nur die Betreffzeile zu wiederholen.

## Häufig gestellte Fragen

### Warum wird die Aktionskarte oder das Produktkarussell in meiner Nachricht nicht im Postfach angezeigt?

Es gibt viele Faktoren, die bestimmen, ob das Produktkarussell auf dem Tab Aktionen von Google Mail angezeigt wird.

Alle Bilder in der Anmerkung müssen noch einen Qualitätsfilter passieren. Damit das Produktkarussell ausgefüllt werden kann, müssen alle Bilder in der Anmerkung das empfohlene Bildseitenverhältnis aufweisen und qualitativ hochwertige, hochauflösende Nahaufnahmen von Produkten sein. Die Bilder sollten wenig bis gar keinen Text enthalten. Der Qualitätsfilter filtert auch unangemessene Inhalte. Ihre Bilder sollten also familien-, nutzer- und kinderfreundlich sein.

Außerdem gibt es in Google Mail eine Obergrenze für die Dichte der Produktkarussells, die im Tab Aktionen eines Nutzers:innen erscheinen. Instanz, wenn ein Nutzer:in viele Marken abonniert, die Produkt-Karussells in ihren Aktionen per E-Mail verwenden, setzt Gmail schließlich eine Obergrenze für die Anzahl der angezeigten Produkt-Karussells.

Aufgrund der Datenschutz- und Sicherheitsbestimmungen von Google müssen E-Mails mit Anmerkungen weit versendet werden, damit die Anmerkungen funktionieren. Es wird empfohlen, eine Kampagne einzuführen und an mindestens 100 Empfänger:in zu senden, damit das System von Google sie als "Massenversand" erkennt. Die Bild-URLs dürfen nicht zwischen den Empfängern variieren.

### Wie werden die Klicks auf eine Aktionskarte oder ein Produktkarussell verfolgt?

Bei Braze und anderen ESP ist Link-Tracking bei Links im Header nicht möglich. Das bedeutet, dass Klicks auf eine Aktionskarte oder ein Produktkarussell nicht nachverfolgt werden können.

### Gibt es eine Möglichkeit zu sehen, wie viele Benutzer ein Produktkarussell erhalten haben?

Gmail bestimmt, wann und wem die Karte angezeigt wird. Es gibt also keine Garantie dafür, dass alle das Produktkarussell sehen können.

### Warum sehe ich keine Anmerkungen in meinem Tab für Aktionen in Google Mail?

Anmerkungen werden für Google Workspace nicht unterstützt. Um eine Vorschau der Anmerkungen zu erhalten, können Sie eine persönliche E-Mail Adresse mit Gmail erstellen.

Beachten Sie, dass Anmerkungen weder im Tab **Primär** noch in einem anderen Tab in der mobilen App von Google Mail angezeigt werden. Anmerkungen werden nicht angezeigt, nachdem ein Nutzer:innen eine E-Mail geöffnet hat oder wenn Sie den Annotationstyp `DiscountOffer` verwenden und die Zeit und das Datum bereits abgelaufen sind.
