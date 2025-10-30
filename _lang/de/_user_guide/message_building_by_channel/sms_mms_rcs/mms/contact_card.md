---
nav_title: Kontaktkarten
article_title: Kontakt Karten
page_order: 3
description: "In diesem Referenzartikel erfahren Sie, wie Sie eine Kontaktkarte erstellen, die Sie in Ihre MMS- und SMS-Nachrichten einfügen können."
page_type: reference
alias: /mms_contact_cards/
channel:
  - MMS
  
---

# Kontaktkarten 

> Kontaktkarten (manchmal auch als vCard oder Virtual Contact Files (VCF) bezeichnet) sind ein standardisiertes Dateiformat zum Versenden von Geschäfts- und Kontaktinformationen, die leicht in Adress- oder Kontaktbücher importiert werden können. 

Kontaktkarten können [programmgesteuert](https://www.twilio.com/blog/send-vcard-twilio-sms) erstellt und in die [Braze-Mediathek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) hochgeladen oder über unseren integrierten Kontaktkartengenerator erstellt werden. Diese Karten können mit allgemeinen Eigenschaften wie dem Namen Ihres Unternehmens, Ihrer Telefonnummer, Ihrer Adresse, Ihrer E-Mail und einem kleinen Foto versehen werden. Um mit der Erstellung von Kontaktkarten zu beginnen, vergewissern Sie sich zunächst, dass Sie in Braze für die Verwendung von MMS eingerichtet sind.

## Kontaktkarten-Generator

### Schritt 1: Name zuweisen

Kontaktkarten können mit dem SMS- und MMS-Composer erstellt werden. Wählen Sie die Registerkarte **Kontaktkarten-Generator**, um loszulegen.

Als Nächstes werden Sie aufgefordert, Ihren Firmennamen oder Spitznamen einzugeben. Dies ist der Name, den Ihre Benutzer sehen werden, wenn sie die Karte speichern. Ein Limit von 20 Zeichen wird durchgesetzt, um sicherzustellen, dass die Nutzer:innen in ihren Kontakten und in ihrer Messaging-App Ihren gesamten Firmennamen oder Alias sehen können. 

\![Der Tab des Kontaktkartengenerators.]({% image_buster /assets/img/sms/contact_card1.png %}){: style="max-width:60%" }

### Schritt 2: Rufnummer zuweisen

Wählen Sie die Abonnementgruppe und die gewünschte Rufnummer aus den verfügbaren Dropdown-Optionen. Diese Nummer wird in Ihrer Kontaktkarte aufgeführt und ist nach dem Speichern auf dem Telefon des Empfängers als SMS verfügbar.

Beachten Sie, dass alphanumerische Codes nicht mit Zwei-Wege-Messaging kompatibel sind und für Kontaktkarten nicht unterstützt werden.

### Schritt 3: Optionale Felder

\![Optionale Felder für den Kontaktkartengenerator.]({% image_buster /assets/img/sms/contact_card2.png %}){: style="float:right;max-width:35%;margin-left:15px;"}

#### Kontaktkarte Kontaktfoto hochladen

Sie können optional ein Miniatur-Kontaktfoto für Ihre Kontaktkarte hochladen. Wir empfehlen ein 240 x 240 px großes JPEG- oder PNG-Bild. Alle hochauflösenden Bilder, die Sie hochladen, werden auf 240 x 240 px verkleinert, um die Zustellbarkeit Ihrer Nachricht zu gewährleisten, da MMS-Nachrichten über 5 MB möglicherweise fehlschlagen.

#### Mehr Informationen hinzufügen

In anderen Feldern können Sie Ihren Namen, Ihre Zwischenüberschrift, Ihre Adresse und andere Kontaktinformationen einfügen, die Sie Ihren Nutzer:innen zur Verfügung stellen möchten. 

### Schritt 4: Speichern Ihrer Kontaktkarte

Sobald Sie alle erforderlichen Felder eingegeben haben, klicken Sie auf **Kontaktkarte generieren**, und sie wird automatisch an Ihre Kampagne oder Ihr Canvas angehängt. Von hier aus können Sie eine Nachricht hinzufügen, Ihre Kontaktkarte testen und Ihre Kampagne oder Ihr Canvas starten.

Die Kontaktkarte wird auch in der [Mediathek]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/#media-library) gespeichert, damit Sie sie in zukünftigen Kampagnen und Canvases problemlos wiederverwenden können.

## Hinzufügen einer bestehenden Kontaktkarte

Um eine bestehende Kontaktkarte hinzuzufügen, erstellen Sie eine Kampagne oder ein Canvas und wählen Sie die gewünschte Abonnementgruppe. Als Nächstes erscheint im Fenster des Nachrichten-Editors die Option **Medien hinzufügen**. Hier können Sie eine vorhandene Kontaktkartendatei hochladen oder in der Mediathek nach einer suchen.
