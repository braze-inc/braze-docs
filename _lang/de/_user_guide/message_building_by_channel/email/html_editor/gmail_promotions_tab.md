---
nav_title: Gmail-Aktionen einrichten
article_title: Gmail-Aktionen einrichten
page_order: 8
description: "In diesem Referenzartikel erfahren Sie, wie Sie mit Braze die Gmail-Karte für Mobilgeräteaktionen aus Ihrer E-Mail-Kampagne erstellen."
channel:
  - email
toc_headers: h2
---

# Gmail Promotion einrichten

> Der [Gmail-Tab für Mobilgeräteaktionen](https://developers.google.com/gmail/promotab/) erlaubt es Marketern, mittels Annotationen in einer „Karte" über Betreffzeile oder Preheader hinaus weitere Informationen zu versenden. Braze verfügt über ein integriertes Tool, mit dem Sie die Karte aus Ihrer E-Mail-Kampagne erstellen können.

## Voraussetzung

Leiten Sie zunächst Ihre Domains und Subdomains an das Outreach-Team von Googles Promotions Tab unter <a href="mailto:p-promo-outreach@google.com">p-promo-outreach@google.com</a> weiter, damit sie in die Zulassungsliste von Gmail aufgenommen werden. So können Sie Features mit reichhaltigen Bildern wie das Produktkarussell im Aktions-Tab von Gmail verwenden.

## Karten in Braze erstellen

Befolgen Sie diese Anleitung, um eine Gmail-Aktionskarte für eine E-Mail-Kampagne zu erstellen. Beachten Sie, dass das Verlassen des Bereichs **Inhalt** im Editor die Felder und Informationen auf dem Tab **Gmail Promotion** zurücksetzt. Schließen Sie die Einrichtung Ihrer Aktionskarte ab und kopieren Sie den generierten HTML-Code, damit Sie ihn nicht verlieren.

### 1. Schritt: E-Mail-Kampagne erstellen

[Erstellen Sie zunächst Ihre E-Mail-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) und wählen Sie den **HTML-Code-Editor** als Bearbeitungsumgebung aus.

### 2. Schritt: Details zur Gmail-Aktionskarte hinzufügen

Gehen Sie als Nächstes in den Bereich **Inhalt** des HTML-Editors und wählen Sie den Tab **Gmail Promotion** aus. Füllen Sie die Felder unter **Grundlegende Informationen** aus und wählen Sie dann **HTML-Code generieren**. Dies erstellt das Skript für Ihre Gmail-Promo-Tab-Karte unter dem Abschnitt **Kopieren und Einfügen des HTML-Codes in `<Head>`**.

![Ein Beispiel dafür, wie Sie eine Karte erstellen können.]({% image_buster /assets/img/create-gmail-promo.png %})

### 3. Schritt: Gmail-Aktionskarte anpassen

Wählen Sie, ob Sie ein Rabattangebot, eine Deal Card, eine Aktionskarte oder alle Optionen für Ihre Gmail-Aktionskarte einfügen möchten.

{% tabs %}
{% tab Discount offer %}

Wenn Sie ein Rabattangebot einrichten, können Sie die Gültigkeitsdaten für einen Rabatt festlegen.

1. Wählen Sie den Schalter **Rabattangebot** aus.
2. Geben Sie bei **Angebot** eine kurze Zusammenfassung für den Rabatt ein. Ein Beispiel ist „20 % Rabatt".
3. Fügen Sie bei **Code** den Aktionscode ein, den Nutzer:innen an der Kasse eingeben müssen.
4. Wählen Sie dann das Startdatum und die Uhrzeit für das Rabattangebot aus.
5. Legen Sie fest, ob das Rabattangebot zu einem bestimmten Zeitpunkt oder nie enden soll.

![Optionen zur Angabe von Angebotswert, Code sowie Anfangsdatum und -uhrzeit eines Rabattangebots.]({% image_buster /assets/img/gmail_promo_discount_details.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Deal Cards %}

Verwenden Sie Deal Cards, um wichtige Angebotsinformationen direkt am Anfang von E-Mails bereitzustellen. Dies erlaubt es Empfänger:innen, die Details des Angebots schnell zu verstehen und zu handeln. Sie können zum Beispiel Deal Cards verwenden, um zeitlich begrenzte Aktionen zu bewerben und den Nutzer:innen die Suche nach Details in E-Mails zu ersparen.

1. Wählen Sie den Schalter **Deal Card** aus.
2. Geben Sie bei **Angebot** eine kurze Zusammenfassung für den Rabatt ein. Ein Beispiel ist „20 % Rabatt auf alle Schuhe".
3. (optional) Fügen Sie bei **Code** den Aktionscode hinzu, den Nutzer:innen beim Checkout eingeben müssen.
4. Geben Sie mindestens eine der folgenden URLs ein.
-  **URL der Angebotsseite:** Die URL für die Landing-Page des spezifischen Angebots. Dadurch wird ein Button „Jetzt einkaufen" (oder ähnlich) erstellt. Wir empfehlen, diese URL für Ihre Deal Card anzugeben.
- **Händler-Homepage-URL:** Die URL für Ihre Hauptseite. Verwenden Sie dieses Feld nur, wenn die URL einer bestimmten Angebotsseite nicht verfügbar ist.
5. (optional) Fügen Sie ein Startdatum für das Angebot hinzu.
6. Legen Sie fest, ob das Angebot zu einem bestimmten Zeitpunkt oder nie enden soll.

![Optionen zur Angabe des Angebotswertes, des Codes sowie des Startdatums und der Startzeit für eine Deal Card.]({% image_buster /assets/img/gmail_promo_deal_cards.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Promotion cards %}

Aktionskarten im Produktkarussell sind hilfreich, um Ihr Angebot zu bebildern. Sie können die Variablen des Produktkarussells anpassen und bis zu zehn eindeutige Vorschaubilder einfügen.

1. Wählen Sie den Schalter **Aktionskarten** aus.
2. Wählen Sie **Aktionskarte hinzufügen**. Jedes Bild in Ihrem Produktkarussell muss eine eindeutige URL haben und das gleiche Seitenverhältnis verwenden (4:5, 1:1, 1,91:1).
3. Fügen Sie eine Bild-URL ein.
4. Fügen Sie unter **Ziel-URL** den Link für Ihre Aktion hinzu.

{% alert tip %}
Wir empfehlen Ihnen, Ihre Produktbilder in die Bibliothek hochzuladen und dann die URLs zu kopieren und in die entsprechenden Felder einzufügen. Es werden nur statische Bildformate (PNG und JPEG) akzeptiert. Einige Bildformate (GIF) werden zwar hochgeladen, aber nicht wie erwartet angezeigt.
{% endalert %}

{: start="5"}
5. Passen Sie Ihre Aktionskarte an, indem Sie eine Überschrift, eine Währung, einen Preis und einen Rabattwert hinzufügen.

| Anpassbare Eigenschaft | Beschreibung |
|---|---|
| Überschrift | (optional) Eine ein- oder zweisätzige Beschreibung der Aktion. Wird unter dem Vorschaubild angezeigt. |
| Währung | (optional) Die Währung des Preises. |
| Preis | Der Preis der Aktion. |
| Rabattwert | Der vom ursprünglichen Preis abgezogene Betrag. | 
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Ein Beispiel für ein Produktkarussell eines Unternehmens namens Motto mit der E-Mail-Überschrift „Unsere meistverkauften Socken sind im Angebot", mit drei Bildern von Socken und ihren ermäßigten Preisen.]({% image_buster /assets/img_archive/product_carousel.png %}){: style="max-width:40%;"}

{% endtab %}
{% endtabs %}

### 4. Schritt: HTML-Code generieren und einfügen

Nachdem Sie Ihre Gmail-Aktionskarte erstellt haben, wählen Sie **HTML-Code generieren**. Kopieren Sie das Skript und fügen Sie es in das `<head>`-Element im HTML-Code Ihrer E-Mail ein.

{% alert tip %}
Kopieren Sie für den Drag-and-Drop-Editor den generierten HTML-Code und fügen Sie ihn in den Abschnitt [Angepasste Head-Tags]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#custom-head-tags) unter **Sendeeinstellungen** ein.
{% endalert %}

{% alert warning %}
Das Aktionsskript erscheint nur, wenn Ihre E-Mail im Aktions-Tab von Gmail landet. Derzeit verwendet Gmail Algorithmen, um zu entscheiden, wo Ihre E-Mail landet. Wenn Nutzer:innen Ihre E-Mail jedoch als Werbung markieren, wird der Algorithmus von Gmail ignoriert, und Ihre E-Mail landet künftig automatisch im Aktions-Tab.
{% endalert %}

## Gmail-Karten messen

Gmail liefert keine Analytics für diese Karten, und E-Mail-Anbieter (ESPs) wie Braze können kein eigenes Link-Tracking für Links im Header-Bereich einfügen (einschließlich Aktionskarten und Produktkarussells). Sie können jedoch während der Einrichtung UTM-Parameter oder eindeutige Codes an die URLs anhängen. Mit diesen Parametern können Sie das Engagement über Ihr eigenes Website-Analytics oder Konversions-Tracking verfolgen, da das Tracking Teil der URL selbst ist und nicht vom ESP eingefügt wird. Klick-Tracking auf ESP-Ebene ist für diese Links nicht verfügbar.

### Bilder einbinden

Gmail hat mit aussagekräftigen Bildern zur E-Mail-Nachricht bessere Ergebnisse erzielt. Gmail rät von reinem Textdesign ab, da dieser Bereich dafür konzipiert wurde, die für das E-Mail-Marketing so wichtige Bildsprache in die Vorschau zu bringen. Verwenden Sie keine Bilder mit abgeschnittenem Text und wiederholen Sie keine Bilder in mehreren Kampagnen.

### Angebote beschreiben

Gmail rät davon ab, Sätze oder Phrasen zu verwenden wie „Kaufen Sie 1 und erhalten Sie 1 gratis oder Rabatt auf alle Shorts und Hemden", da diese möglicherweise abgeschnitten werden, nicht mehr ins Auge fallen und mit der Betreffzeile konkurrieren. Dieser Bereich sollte nur dazu verwendet werden, Ihre Kund:innen für Ihr Messaging zu begeistern. Vermeiden Sie also Formulierungen wie „Öffnen Sie diese E-Mail jetzt" oder „Klicken Sie hier für Angebote". Vermeiden Sie es außerdem, einfach nur die Betreffzeile zu wiederholen.

## Best Practices

Halten Sie sich im Allgemeinen an diese [von Gmail empfohlenen Best Practices](https://developers.google.com/gmail/promotab/best-practices).

{% alert tip %}
Sie können Liquid zwar in diesem Skript verwenden, aber wir empfehlen Ihnen dringend, Ihre Nachrichten so oft wie möglich zu testen, um Fehler zu vermeiden.
{% endalert %}

### Vorschau Ihrer Annotation

Verwenden Sie das [Vorschau-Tool](https://developers.google.com/workspace/gmail/promotab/preview), um Ihre Annotation in der Vorschau anzuzeigen. Beachten Sie, dass das Senden einer Test-E-Mail an sich selbst bei Annotationen nicht funktioniert, da Ihre Annotation nur gerendert wird, wenn die E-Mail an eine signifikante Anzahl von Empfänger:innen gesendet wird. Stellen Sie sicher, dass Sie die finale E-Mail (mit ihren Bild-URLs) an mindestens 100 Gmail-Empfänger:innen senden.

Verwenden Sie Google Workspace nicht zum Senden von E-Mails mit Annotationen. Verwenden Sie nur zugelassene E-Mail-Domains, um Annotationen an eine große Gruppe von Empfänger:innen zu senden.

### Bildrichtlinien einhalten

Stellen Sie sicher, dass Ihre Bilder diesen Richtlinien entsprechen:
- Verwenden Sie hochwertige und hochauflösende Bilder.
- Alle annotierten Bilder verwenden das gleiche Seitenverhältnis. Unterstützte Seitenverhältnisse sind: 4:5, 1:1, 1,91:1.
- Verwenden Sie korrekte Bildgrößen. Das Minimum beträgt 256×256, das Maximum 4096×4096 Pixel.

Gmail empfiehlt, Folgendes zu vermeiden:
- Übermäßig viel Text in Ihren Bildern
- Bilder, die nur aus Icons bestehen
- Bilder mit runden Masken
- Personalisierte Bild-URLs

### Mit DMARC registrieren

Damit Ihre Annotationen korrekt gerendert werden, bestätigen Sie, dass die eingereichten Domains bei DMARC registriert sind und alle Richtlinien aktiviert sind.


## Häufig gestellte Fragen

### Warum wird die Aktionskarte oder das Produktkarussell in meiner Nachricht nicht im Posteingang angezeigt?

Es gibt viele Faktoren, die bestimmen, ob das Produktkarussell im Aktions-Tab von Gmail angezeigt wird.

Alle Bilder in der Annotation müssen einen Qualitätsfilter passieren. Damit das Produktkarussell dargestellt werden kann, müssen alle Bilder in der Annotation das empfohlene Seitenverhältnis aufweisen und qualitativ hochwertige, hochauflösende Nahaufnahmen von Produkten sein. Die Bilder sollten wenig bis gar keinen Text enthalten. Der Qualitätsfilter filtert auch unangemessene Inhalte, sodass die Bilder familien-, nutzer:innen- und kinderfreundlich sein müssen.

Darüber hinaus gibt es in Gmail eine Obergrenze für die Anzahl der Produktkarussells, die im Aktions-Tab von Nutzer:innen erscheinen. Wenn beispielsweise Nutzer:innen viele Marken abonniert haben, die Produktkarussells in ihren Aktions-E-Mails verwenden, setzt Gmail irgendwann eine Obergrenze für die Anzahl der angezeigten Produktkarussells.

Aufgrund der Datenschutz- und Sicherheitsbestimmungen von Google müssen E-Mails mit Annotationen breit versendet werden, damit die Annotationen funktionieren. Es wird empfohlen, eine Kampagne zu starten und an mindestens 100 Empfänger:innen zu senden, damit das System von Google sie als „Massensendung" erkennt. Die Bild-URLs dürfen nicht zwischen den Empfänger:innen variieren.

### Wie werden Klicks auf eine Aktionskarte oder ein Produktkarussell verfolgt?

Braze und andere ESPs können kein Link-Tracking für Links im Header-Bereich einfügen. Das bedeutet, dass Klicks auf eine Aktionskarte oder ein Produktkarussell nicht nachverfolgt werden können.

### Gibt es eine Möglichkeit zu sehen, wie viele Nutzer:innen ein Produktkarussell erhalten haben?

Gmail bestimmt, wann und wem die Karte angezeigt wird. Es gibt also keine Garantie dafür, dass alle Empfänger:innen das Produktkarussell sehen.

### Warum sehe ich keine Annotationen in meinem Aktions-Tab in Gmail?

Annotationen werden für Google Workspace nicht unterstützt. Für die Vorschau von Annotationen können Sie mit Gmail eine persönliche E-Mail-Adresse erstellen.

Beachten Sie, dass Annotationen weder im Tab **Primär** noch in einem anderen Tab in der mobilen App von Gmail angezeigt werden. Annotationen werden nicht angezeigt, nachdem Nutzer:innen eine E-Mail geöffnet haben oder wenn Sie den Annotationstyp `DiscountOffer` verwenden und Zeit und Datum bereits abgelaufen sind.