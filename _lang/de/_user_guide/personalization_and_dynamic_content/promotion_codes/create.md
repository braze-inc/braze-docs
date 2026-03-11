---
nav_title: Codes erstellen
article_title: Aktionscodes erstellen
page_order: 0.1
description: "Erfahren Sie, wie Sie in Ihren Kampagnen und Canvases Aktionscodes erstellen können."
---

# Aktionscodes erstellen

> Erfahren Sie, wie Sie in Ihren Kampagnen und Canvases Aktionscodes erstellen können.

## Erstellen einer Liste mit Aktionscodes {#create}

### Schritt 1: Erstellen Sie eine neue Liste

Bitte navigieren Sie im Dashboard zu **„Dateneinstellungen“** > **„Aktionscodes“** und wählen Sie anschließend **„Aktionscodeliste erstellen**“.

![Button zum Erstellen eines Aktionscodes.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Schritt 2: Geben Sie die Details ein

1. Benennen Sie Ihre Aktionscode-Liste und fügen Sie eine optionale Beschreibung hinzu.
2. Als nächstes erstellen Sie ein Snippet für den Code der Aktion. 

Hier finden Sie einige Details, die Sie bei der Erstellung eines Code Snippets beachten sollten:

- Nach dem Speichern können Sie ein Snippet nicht mehr bearbeiten.
- Bei Snippets wird zwischen Groß- und Kleinschreibung unterschieden. Das System erkennt beispielsweise"Birthday_promo"  und"birthday_promo"  als zwei unterschiedliche Snippets.
- Verwenden Sie den Snippet-Namen in Liquid, um diese Reihe von Aktionscodes zu referenzieren.
- Stellen Sie sicher, dass das Code Snippet nicht bereits in einer anderen Liste verwendet wird.

![Eine Liste von Aktionscodes mit dem Namen "SpringSale2025" und dem Code Snippet "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Schritt 3: Wählen Sie die Optionen für den Aktionscode

Jede Liste mit Aktionscodes hat ein entsprechendes Ablaufdatum und eine entsprechende Uhrzeit, die bei der Erstellung festgelegt werden. Die maximale Gültigkeitsdauer beträgt sechs Monate ab dem Tag, an dem Sie Ihre Liste erstellen oder bearbeiten.

Innerhalb dieser Zeit können Sie das Ablaufdatum wiederholt ändern und aktualisieren. Dieses Ablaufdatum gilt für alle Codes, die dieser Liste hinzugefügt wurden. Nach Ablauf werden die Codes aus dem Braze-System gelöscht, und alle Nachrichten, die den Code-Snippet dieser Liste aufrufen, werden nicht versendet.

![Die Ablaufeinstellungen der Liste besagen, dass alle verbleibenden Codes am 30\. April 2025 um 12 Uhr ablaufen werden.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Sie haben auch die Möglichkeit, optionale und angepasste Schwellenwertwarnungen einzurichten. Wenn diese Benachrichtigungen eingerichtet sind, werden sie per E-Mail an den angegebenen Empfänger:in gesendet, sobald die Liste nur noch wenige verfügbare Aktionscodes enthält oder wenn Ihre Aktionscodeliste kurz vor dem Ablauf steht. Die Empfänger:innen werden einmal täglich benachrichtigt.

![Ein Beispiel für einen Schwellenwertalarm, der "marketing@abc.com" benachrichtigt, wenn die Liste der Aktionscodes in 5 Tagen abläuft.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Schritt 4: Aktionscodes hochladen

Braze verwaltet weder die Erstellung noch die Einlösung von Codes, d.h. Sie müssen Ihre Aktionscodes in einer CSV-Datei generieren und diese in Braze hochladen. 

Stellen Sie sicher, dass Ihre CSV-Datei diesen Richtlinien entspricht:

- Enthält eine Spalte für Aktionscodes.
- Hat einen Aktionscode pro Zeile.

Sie können unsere integrierte Integration mit [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) oder [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) verwenden, um Aktionscodes zu erstellen und zu exportieren.

{% alert important %}
Die maximale Dateigröße beträgt 100 MB, und die maximale Listengröße umfasst 20 Millionen unbenutzte Codes. Sollten Sie feststellen, dass die falsche Datei hochgeladen wurde, laden Sie bitte eine neue Datei hoch, um die vorherige zu ersetzen.
{% endalert %}

1. Nachdem der Upload abgeschlossen ist, wählen Sie **Liste speichern**, um alle Details und Codes zu speichern, die Sie gerade eingegeben haben.

![CSV-Datei mit dem Namen "springsale", die erfolgreich hochgeladen wurde.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Nach Auswahl von „Speichern“ erscheint eine neue Zeile im **Importverlauf**.
3\. Um die Tabelle zu aktualisieren und zu sehen, ob Ihr Import abgeschlossen ist, wählen Sie <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** oben in der Tabelle.

![Aktionscodes, die gerade hochgeladen werden.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Der Import größerer Dateien kann einige Minuten in Anspruch nehmen. Während Sie warten, können Sie die Seite verlassen und an etwas anderem arbeiten, während der Importvorgang läuft. Nach Abschluss des Imports ändert sich der Status in der Tabelle zu **„Abgeschlossen**“.
{% endalert %}

## Aktualisieren einer Liste von Aktionscodes

Um eine Liste zu aktualisieren, wählen Sie eine Ihrer bestehenden Listen aus. Sie können den Namen, die Beschreibung, den Ablauf der Liste und die Schwellenwerte für Alarme ändern. Sie können der Liste auch weitere Codes hinzufügen, indem Sie neue Dateien hochladen und **Liste aktualisieren** auswählen. Alle Codes in der Liste haben die gleiche Gültigkeitsdauer, unabhängig vom Importdatum.

{% alert important %}
Aktionscodes können nicht gelöscht werden.
{% endalert %}

### Korrektur einer fehlerhaften Liste von Aktionscodes 

Wenn Sie eine CSV-Datei mit falschen Aktionscodes hochgeladen und **„Liste speichern“** ausgewählt haben, können Sie dies auf eine der folgenden Arten beheben:

- Die gesamte Liste als veraltet kennzeichnen: Bitte verwenden Sie die aktuelle Liste mit Aktionscodes nicht mehr in Kampagnen, Canvases oder Templates. Laden Sie anschließend die CSV-Datei mit den korrekten Codes hoch und verwenden Sie diese im Messaging.
- Verwenden Sie die falschen Codes: Erstellen Sie eine Kampagne, die Aktionscodes aus der Liste der ungültigen Aktionscodes an einen Platzhalter sendet, bis alle ungültigen Codes verwendet wurden. Bitte laden Sie anschließend die korrekten Aktionscodes in dieselbe Liste hoch.
