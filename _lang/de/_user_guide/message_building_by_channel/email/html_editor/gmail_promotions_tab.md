---
nav_title: Gmail-Aktionen einrichten
article_title: Gmail-Aktionen einrichten
page_order: 8
description: "In diesem Artikel erfahren Sie, wie Sie mit Braze die Gmail-Karte für Mobilgeräteaktionen aus E-Mail-Kampagnen erstellen."
channel:
  - email

---

# Gmail Promotion einrichten

> Der [Gmail-Tab Mobilgeräteaktionen][1] erlaubt es Marketern, mittels Anmerkungen neben Betreffzeile oder Preheader-Daten weitere Informationen in Karten zu versenden. Braze verfügt über ein integriertes Tool, mit dem Sie die Karte aus Ihrer E-Mail-Kampagne erstellen können.

## Voraussetzung

Leiten Sie zunächst Ihre Domains und Subdomains an das Team von Google Promotions Tab unter <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> weiter, damit sie in die Zulassungsliste von Gmail aufgenommen werden. So können Sie Features mit reichhaltigen Bildern wie das Produktkarussell im Aktions-Tab von Gmail verwenden.

## Karten in Braze erstellen

Befolgen Sie diese Anleitung, um eine Gmail-Aktionskarte für eine E-Mail-Kampagne zu erstellen. Beachten Sie, dass das Verlassen des Bereichs **Inhalt** im Editor die Felder und Informationen auf der Registerkarte **Google Mail Werbung** zurücksetzt. Schließen Sie die Einrichtung der Aktionskarte ab und kopieren Sie den generierten HTML-Code, damit Sie ihn nicht verlieren.

1. [Erstellen Sie Ihre E-Mail-Kampagne][7], und wählen Sie den **HTML-Editor** als Bearbeitungsumgebung.
2. Gehen Sie im HTML-Editor zum Abschnitt **Inhalt** und wählen Sie die Registerkarte **Gmail Promotion**.
3. Füllen Sie die Felder unter **Basisinformationen** aus und klicken Sie dann auf **HTML-Code generieren**. Dies wird Ihnen helfen, das Skript für Ihre Gmail Promo-Tab-Karte unter dem Abschnitt **Kopieren und Einfügen des HTML-Codes in `<Head>`** zu erstellen. <br> ![Ein Beispiel dafür, wie Sie eine Karte erstellen können.][2]
4. Wählen Sie aus, ob Sie ein Rabattangebot, Aktionskarten oder beides in die Gmail-Aktionskarte einfügen möchten. <br> ![Optionen zur Einbindung von Rabattangeboten und Aktionskarten.][10]{: style="max-width:50%;"}
5. Kopieren Sie das Skript und fügen Sie es in das `<head>` Element im HTML-Code Ihrer E-Mail ein.

{% alert warning %}
Das Aktionsskript erscheint nur, wenn Ihre E-Mail im Aktions-Tab von Gmail landet. Derzeit verwendet Gmail Algorithmen, um zu entscheiden, wo Ihre E-Mail landet. Wenn ein Nutzer Ihre E-Mail jedoch als Werbeaktion markiert, wird der Algorithmus von Google Mail ignoriert, und Ihre E-Mail landet automatisch auf der Registerkarte Werbeaktionen.
{% endalert %}

### Einschließlich eines Rabattangebots

Wenn Sie ein Rabattangebot einrichten, können Sie die Gültigkeitsdaten für einen Rabatt festlegen. Wenn Sie das Rabattangebot festgelegt haben, wählen Sie ein Anfangsdatum und eine Uhrzeit aus. Sie können das Rabattangebot zu einem bestimmten Zeitpunkt enden lassen oder auswählen, dass es nie endet.

![Optionen zur Angabe von Angebotswert, Code sowie Anfangsdatum und -uhrzeit eines Rabattangebots.][11]{: style="max-width:50%;"}

### Produkt-Karussell anpassen

Aktionskarten im Produktkarussell sind hilfreich, um Ihr Angebot zu bebildern. Sie können die Variablen des Produktkarussells anpassen und bis zu zehn eindeutige Vorschaubilder einfügen.

![Ein Beispiel für ein Produktkarussell von einem Unternehmen namens Motto mit der E-Mail-Überschrift "Unsere meistverkauften Socken sind im Angebot", mit drei Bildern von Socken und ihren reduzierten Preisen.][9]{: style="max-width:40%;"}

| Anpassbare Variable | Beschreibung |
|---|---|
| Bild-URL | Die URL zu Ihrem Bild. Jedes Bild in Ihrem Produktkarussell muss eine eindeutige URL haben und das gleiche Seitenverhältnis verwenden (4:5, 1:1, 1,91:1). |
| Ziel-URL | Der Link zu Ihrer Aktion. |
| Überschrift | (optional) Eine ein- oder zweisätzige Beschreibung der Werbeaktion. Wird unter dem Vorschaubild angezeigt. |
| Währung | (optional) Die Währung des Preises. |
| Preis | Der Preis der Aktion. |
| Rabattwert | Der vom ursprünglichen Preis abgezogene Betrag. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Wir empfehlen Ihnen, Ihre Produktbilder in die Mediathek hochzuladen und dann die URLs zu kopieren und in die entsprechenden Felder einzufügen. Es werden nur statische Bildformate (PNG und JPEG) akzeptiert. Einige Bildformate (GIF) werden zwar hochgeladen, aber nicht wie erwartet angezeigt.
{% endalert %}

### Bewährte Praktiken

Orientieren Sie sich an diesen Empfehlungen von [Gmail][8]. 

{% alert tip %}
Sie können Liquid zwar in diesem Skript verwenden, aber wir empfehlen Ihnen dringend, Ihre Nachrichten so oft wie möglich zu testen, um einen Fehler zu vermeiden.
{% endalert %}

#### Bilder einbinden

Gmail hat mit aussagekräftigen Bildern zur E-Mail bessere Ergebnisse festgestellt. Gmail rät von reinem Text ab, da ansonsten die für das E-Mail Marketing so wichtige Bildsprache in der Vorschau fehlt. Verwenden Sie keine Bilder mit abgeschnittenem Text oder wiederholte Bilder in mehreren Kampagnen.

#### Angebote beschreiben

Gmail rät davon ab, Sätze oder Phrasen zu verwenden, wie z. B. "Sie können 1 Gratis kaufen oder Rabatt auf alle Shorts und Hemden", da diese möglicherweise abschneiden, nicht mehr ins Auge fallen und mit der Betreffzeile konkurrieren. Dieser Bereich sollte nur dazu verwendet werden, Ihre Kunden für Ihre Nachrichten zu interessieren. Vermeiden Sie also Formulierungen wie "Öffnen Sie diese E-Mail jetzt" oder "Klicken Sie hier für Angebote". Vermeiden Sie es, einfach nur die Betreffzeile zu wiederholen.

## Häufig gestellte Fragen

### Warum wird die Aktionskarte oder das Produktkarussell in meiner Nachricht nicht im Postfach angezeigt?

Es gibt viele Faktoren, die bestimmen, ob das Produktkarussell in Gmail unter "Aktion" angezeigt wird.

Alle Bilder in der Anmerkung müssen noch einen Qualitätsfilter passieren. Damit das Produktkarussell angezeigt werden kann, müssen alle Bilder in der Anmerkung das empfohlene Bildseitenverhältnis aufweisen und von hoher Qualität sein oder hochauflösende Nahaufnahmen des Produkts enthalten. Die Bilder sollten wenig bis gar keinen Text enthalten (vorzugsweise). Der Qualitätsfilter filtert auch unangemessene Inhalte. Ihre Bilder sollten also familien-, nutzer- und kinderfreundlich sein.

Darüber hinaus hat Google Mail eine Obergrenze für die Anzahl der Produktkarussells, die auf der Registerkarte Google Mail Promotion eines Benutzers erscheinen. Abonniert jemand z. B. viele Anbieter, die in ihren Werbemails Produktkarussells verwenden, begrenzt Gmail deren Anzahl früher oder später.

Aufgrund der Datenschutz- und Sicherheitsbestimmungen von Google müssen E-Mails mit Anmerkungen weit versendet werden, damit die Anmerkungen funktionieren. Es wird empfohlen, Kampagnen an mindestens 100 Personen zu senden, damit Google sie als Massensendungen erkennt. Die Bild-URLs dürfen nicht zwischen den Empfängern variieren.

### Wie werden die Klicks auf eine Aktionskarte oder ein Produktkarussell verfolgt?

Bei Braze und anderen ESP ist Link-Tracking bei Links im Header nicht möglich. Das bedeutet, dass Klicks auf eine Aktionskarte oder ein Produktkarussell nicht nachverfolgt werden können.

### Gibt es eine Möglichkeit zu sehen, wie viele Benutzer ein Produktkarussell erhalten haben?

Gmail bestimmt, wann und wem die Karte angezeigt wird. Es gibt also keine Garantie dafür, dass alle das Produktkarussell sehen können.

[1]: https://developers.google.com/gmail/promotab/
[2]: {% image_buster /assets/img/create-gmail-promo.png %}
[3]: {% image_buster /assets/img/copy-gmail-promo-script.png %}
[4]: {% image_buster /assets/img/promocardmap.png %}
[5]: https://developers.google.com/gmail/promotab/overview#preview_your_annotations
[6]: {% image_buster /assets/img/gmail_preview.png %}
[7]: {{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/
[8]: https://developers.google.com/gmail/promotab/best-practices
[9]: {% image_buster /assets/img_archive/product_carousel.png %}
[10]: {% image_buster /assets/img_archive/gmail_promo_discount.png %}
[11]: {% image_buster /assets/img/gmail_promo_discount_details.png %}