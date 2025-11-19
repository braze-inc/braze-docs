---
nav_title: Eine MMS-Kampagne erstellen
article_title: Eine MMS-Kampagne erstellen
page_order: 2
description: "Dieser Referenzartikel behandelt die Schritte zum Erstellen, Senden und Anzeigen einer MMS-Nachricht."
page_type: reference
alias: /create_mms_message/
tool:
  - Campaigns
channel:
  - MMS
search_rank: 1  
---

# Eine MMS-Kampagne erstellen

> Dieser Artikel enthält Informationen speziell zur MMS-Komposition, die Teil des SMS-Editors ist. Ausführlichere Informationen über den SMS/MMS-Editor finden Sie im [SMS-Editor]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).

## Grundlagen des MMS-Versands

### Wählen Sie Ihre Abonnementgruppe

Sie müssen eine Abonnementgruppe mit MMS-fähigen Telefonnummern angeben, die Sie ansprechen möchten (das können kurze oder lange Codes sein).

### Nachrichtentext eingeben

Fügen Sie PNG-, JPEG-, GIF- und VCF-Bildtypen aus der Medienbibliothek ein oder geben Sie eine URL an. Es wird nur ein Bild unterstützt.

### MMS-Versand verstehen

MMS werden zu einem anderen Tarif abgerechnet als reine Text-SMS, und nicht alle Anbieter können MMS akzeptieren. In diesen Fällen wandelt Twilio die MMS automatisch in einen Bildlink um, auf den der Benutzer klicken kann.

### Verwenden Sie Kontaktkarten

Kontaktkarten (manchmal auch als vCard oder Virtual Contact Files (vcf) bezeichnet) sind ein standardisiertes Dateiformat zum Versenden von Geschäfts- und Kontaktinformationen, die sich leicht in Adress- oder Kontaktbücher importieren lassen. Diese Karten können [programmgesteuert](https://www.twilio.com/blog/send-vcard-twilio-sms) erstellt und in die Braze-Mediathek hochgeladen oder über unseren integrierten [Kontaktkartengenerator]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) erstellt werden.

## Erstellen einer MMS Nachricht

Um eine MMS-Nachricht zu erstellen, muss Ihre Abo-Gruppe für den MMS-Versand konfiguriert sein. Sie erkennen dies daran, dass beim Auswählen einer Abo-Gruppe der MMS-Tag angezeigt wird. Wenn Sie eine MMS-aktivierte Abo-Gruppe auswählen, haben Sie die Möglichkeit, ein Bild hochzuladen, eine Bild-URL zu referenzieren oder eine Kontaktkarte einzufügen.

![Der Tab "Verfassen" zum Schreiben Ihrer Nachricht.]({% image_buster /assets/img/sms/mms_composer.png %}){: style="max-width:80%;"}

### Bild-Spezifikationen

| **Bild-Spezifikationen** | **Empfohlene Eigenschaften** |
|--------------------------|----------------------------|
| Größe                     | Bis zu 600 KB        |
| Dateitypen               | PNG, JPEG, GIF             |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Vorschau einer MMS-Nachricht

Braze bietet im Panel **Vorschau** des Nachrichten-Editors eine Vorschau des von Ihnen hochgeladenen Bildes an. 

{% alert note %}
Die Reihenfolge der SMS/MMS-Assets ist nicht anpassbar. Die Bestellung ist abhängig von dem Telefon, das diese Nachricht empfängt.
{% endalert %}

![Ein Beispiel für eine Nachricht "Bereit für das Fitnessstudio... zu Hause?". Die Vorschau zeigt die Nachricht und das Bild, die als Text gesendet werden.]({% image_buster /assets/img/sms/mms_preview.png %})
