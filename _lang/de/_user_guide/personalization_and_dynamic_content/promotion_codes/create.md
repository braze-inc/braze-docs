---
nav_title: Codes erstellen
article_title: Aktionscodes erstellen
page_order: 0.1
description: "Lernen Sie, wie Sie Aktionscodes in Ihren Kampagnen und Canvase erstellen können."
---

# Aktionscodes erstellen

> Lernen Sie, wie Sie Aktionscodes in Ihren Kampagnen und Canvase erstellen können.

## Erstellen einer Liste von Aktionscodes {#create}

### Schritt 1: Eine neue Liste erstellen

Gehen Sie im Dashboard zu **Dateneinstellungen** > **Aktionscodes** und wählen Sie dann **Aktionscode-Liste erstellen**.

![Button zum Erstellen eines Aktionscodes.]({% image_buster /assets/img/promocodes/promocode1.png %})

### Schritt 2: Geben Sie die Details ein

1. Benennen Sie Ihre Aktionscode-Liste und fügen Sie eine optionale Beschreibung hinzu.
2. Als nächstes erstellen Sie ein Snippet für den Code der Aktion. 

Hier finden Sie einige Details, die Sie bei der Erstellung eines Code Snippets beachten sollten:

- Sie können ein Code Snippet nach dem Speichern nicht mehr bearbeiten.
- Bei Snippets wird zwischen Groß- und Kleinschreibung unterschieden. Zum Beispiel erkennt das System "Birthday_promo" und "birthday_promo" als zwei verschiedene Snippets.
- Verwenden Sie den Snippet-Namen in Liquid, um diese Reihe von Aktionscodes zu referenzieren.
- Stellen Sie sicher, dass das Code Snippet nicht bereits in einer anderen Liste verwendet wird.

![Eine Liste von Aktionscodes mit dem Namen "SpringSale2025" und dem Code Snippet "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Schritt 3: Wählen Sie die Optionen für den Aktionscode

Jede Liste mit Aktionscodes hat ein entsprechendes Ablaufdatum und eine entsprechende Uhrzeit, die bei der Erstellung festgelegt werden. Die maximale Verfallsdauer beträgt sechs Monate ab dem Tag, an dem Sie Ihre Liste erstellen oder bearbeiten.

Innerhalb dieser Zeit können Sie das Ablaufdatum wiederholt ändern und aktualisieren. Dieses Ablaufdatum gilt für alle Codes, die zu dieser Liste hinzugefügt werden. Nach Ablauf werden die Codes aus dem Braze-System gelöscht, und alle Nachrichten, die das Code Snippet dieser Liste aufrufen, werden nicht gesendet.

![Die Ablaufeinstellungen der Liste besagen, dass alle verbleibenden Codes am 30\. April 2025 um 12 Uhr ablaufen werden.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Sie haben auch die Möglichkeit, optionale und angepasste Schwellenwertwarnungen einzurichten. Wenn Sie diese Benachrichtigungen einrichten, erhalten die angegebenen Empfänger:in eine E-Mail, wenn die Liste der verfügbaren Aktionscodes in dieser Liste zur Neige geht oder wenn Ihre Liste mit Aktionscodes bald abläuft. Der Empfänger:in wird einmal pro Tag benachrichtigt.

![Ein Beispiel für einen Schwellenwertalarm, der "marketing@abc.com" benachrichtigt, wenn die Liste der Aktionscodes in 5 Tagen abläuft.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Schritt 4: Aktionscodes hochladen

Braze verwaltet weder die Erstellung noch die Einlösung von Codes, d.h. Sie müssen Ihre Aktionscodes in einer CSV-Datei generieren und diese in Braze hochladen. 

Stellen Sie sicher, dass Ihre CSV-Datei diesen Richtlinien entspricht:

- Enthält eine Spalte für Aktionscodes.
- Hat einen Aktionscode pro Zeile.

Sie können unsere integrierte Integration mit [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) oder [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) verwenden, um Aktionscodes zu erstellen und zu exportieren.

{% alert important %}
Die maximale Dateigröße beträgt 100 MB und die maximale Listengröße beträgt 20 MM unbenutzte Codes. Wenn Sie feststellen, dass eine falsche Datei hochgeladen wurde, laden Sie eine neue Datei hoch, um die vorherige Datei zu ersetzen.
{% endalert %}

1. Nachdem der Upload abgeschlossen ist, wählen Sie **Liste speichern**, um alle Details und Codes zu speichern, die Sie gerade eingegeben haben.

![CSV-Datei mit dem Namen "springsale", die erfolgreich hochgeladen wurde.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Nachdem Sie Speichern ausgewählt haben, erscheint eine neue Zeile im **Verlauf des Imports**.
3\. Um die Tabelle zu aktualisieren und zu sehen, ob Ihr Import abgeschlossen ist, wählen Sie <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** oben in der Tabelle.

![Aktionscodes, die gerade hochgeladen werden.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Bei größeren Dateien dauert der Import mehrere Minuten. Während Sie warten, können Sie die Seite verlassen und an etwas anderem arbeiten, während der Importvorgang läuft. Wenn der Import abgeschlossen ist, ändert sich der Status in der Tabelle auf **Vollständig**.
{% endalert %}

## Aktualisieren einer Liste von Aktionscodes

Um eine Liste zu aktualisieren, wählen Sie eine Ihrer bestehenden Listen aus. Sie können den Namen, die Beschreibung, den Ablauf der Liste und die Schwellenwerte für Alarme ändern. Sie können der Liste auch weitere Codes hinzufügen, indem Sie neue Dateien hochladen und **Liste aktualisieren** auswählen. Alle Codes in der Liste haben das gleiche Verfallsdatum, unabhängig vom Datum der Einfuhr.

{% alert important %}
Aktionscodes können nicht gelöscht werden.
{% endalert %}

### Ändern einer falschen Liste von Aktionscodes 

Wenn Sie eine CSV-Datei mit den falschen Aktionscodes hochgeladen und **Liste speichern** ausgewählt haben, können Sie das Problem mit einer der beiden Methoden beheben:

- Verwerfen Sie die gesamte Liste: Verwenden Sie die aktuelle Liste der Aktionscodes nicht mehr in Kampagnen, Canvase oder Templates. Laden Sie dann die CSV-Datei mit den richtigen Codes hoch und verwenden Sie sie in Ihren Nachrichten.
- Verwenden Sie die falschen Codes: Erstellen Sie eine Kampagne, die Aktionscodes aus der Liste der falschen Aktionscodes an einen Platzhalter sendet, bis alle falschen Codes verwendet wurden. Laden Sie dann die richtigen Aktionscodes in dieselbe Liste hoch.
