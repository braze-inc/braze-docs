---
nav_title: Aktionscodes
article_title: Aktionscodes
page_order: 5
toc_headers: h2
alias: "/promotion_codes/"
description: "In diesem Referenzartikel erfahren Sie, wie Sie Aktionscode-Listen erstellen und sie zu Ihren Kampagnen und Canvases hinzufügen."
---

# Aktionscodes

> Auf dieser Seite erfahren Sie, wie Sie Listen mit Aktionscodes erstellen und diese zu Ihren Kampagnen und Canvase hinzufügen können.

## Funktionsweise

Promotion-Codes - auch Promo-Codes genannt - sind eine großartige Möglichkeit, Nutzer zu binden, indem sie zu Interaktionen anregen, wobei der Schwerpunkt auf Käufen liegt. Sie können Nachrichten erstellen, die aus Ihrer Liste von Aktionscodes stammen. 

Jeder Aktionscode hat eine Gültigkeitsdauer von bis zu sechs Monaten. Sie können bis zu 20 Millionen Codes pro Liste speichern und verwalten. Durch die Verwaltung und Analyse der Performance Ihrer Aktionscodes können Sie gezielte Entscheidungen für Ihre Strategien und Nachrichten treffen.

{% alert important %}
Aktionscodes können nicht in In-App-Nachrichten versendet werden.
{% endalert %}

## Erstellen einer Liste von Aktionscodes

### Schritt 1: Gehen Sie zum Abschnitt Aktionscode

![Button zum Erstellen eines Aktionscodes.][1]{: style="float:right;max-width:30%;margin-left:15px;"}

1. Gehen Sie auf dem Dashboard zu **Dateneinstellungen** > **Aktionscodes**.
2. Wählen Sie **Aktionscode-Liste erstellen**.

### Schritt 2: Nennen Sie den Aktionscode

1. Benennen Sie Ihre Aktionscode-Liste und fügen Sie eine optionale Beschreibung hinzu.
2. Als nächstes erstellen Sie ein Snippet für den Code der Aktion. 

Hier finden Sie einige Details, die Sie bei der Erstellung eines Code Snippets beachten sollten:

- Einmal gespeichert, können Code Snippets nicht mehr bearbeitet werden.
- Bei Snippets wird zwischen Groß- und Kleinschreibung unterschieden. Zum Beispiel werden "Birthday_promo" und "birthday_promo" als zwei verschiedene Snippets erkannt.
- Verwenden Sie den Snippet-Namen in Liquid, um diese Reihe von Aktionscodes zu referenzieren.
- Stellen Sie sicher, dass das Code Snippet nicht bereits in einer anderen Liste verwendet wird.

![Eine Liste von Aktionscodes mit dem Namen "SpringSale2025" und dem Code Snippet "spring25".][3]{: style="max-width:80%"}

### Schritt 3: Wählen Sie die Optionen für den Aktionscode

Jede Liste mit Aktionscodes hat ein entsprechendes Ablaufdatum und eine entsprechende Uhrzeit, die bei der Erstellung festgelegt werden. Die maximale Gültigkeitsdauer beträgt sechs Monate in der Zukunft ab dem Tag, an dem Sie Ihre Liste erstellen oder bearbeiten. 

Innerhalb dieser Zeit können Sie das Ablaufdatum wiederholt ändern und aktualisieren. Dieses Ablaufdatum gilt für alle Codes, die zu dieser Liste hinzugefügt werden. Nach Ablauf der Frist werden die Codes aus dem Braze-System gelöscht und alle Nachrichten, die den Codeausschnitt dieser Liste aufrufen, werden nicht gesendet.

![Die Ablaufeinstellungen der Liste besagen, dass alle verbleibenden Codes am 30\. April 2025 um 12 Uhr ablaufen werden.][4]{: style="max-width:80%"}

Sie haben auch die Möglichkeit, optionale und angepasste Schwellenwertwarnungen einzurichten. Wenn Sie diese Benachrichtigungen einrichten, wird der angegebene Empfänger per E-Mail benachrichtigt, wenn die Liste der verfügbaren Aktionscodes in dieser Liste zur Neige geht oder wenn Ihre Aktionscode-Liste bald abläuft. Der Empfänger wird einmal pro Tag benachrichtigt.

![Ein Beispiel für einen Schwellenwertalarm, der "marketing@abc.com" benachrichtigt, wenn die Liste der Aktionscodes in 5 Tagen abläuft.][5]{: style="max-width:80%"}

### Schritt 4: Aktionscodes hochladen

Braze verwaltet weder die Erstellung noch die Einlösung von Codes, d.h. Sie müssen Ihre Aktionscodes in einer CSV-Datei generieren und diese in Braze hochladen. 

Stellen Sie sicher, dass Ihre CSV-Datei diesen Richtlinien entspricht:

- Enthält eine Spalte für Aktionscodes.
- Hat einen Aktionscode pro Zeile.

Sie können unsere integrierte Integration mit [Voucherify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/) oder [Talon.One]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/talonone/) verwenden, um Aktionscodes zu erstellen und zu exportieren.

{% alert important %}
Die maximale Dateigröße beträgt 100 MB und die maximale Listengröße beträgt 20 MM unbenutzte Codes. Wenn Sie feststellen, dass eine falsche Datei hochgeladen wurde, laden Sie eine neue Datei hoch, und die vorherige wird ersetzt.
{% endalert %}

1. Nachdem der Upload abgeschlossen ist, wählen Sie **Liste speichern**, um alle Details und Codes zu speichern, die Sie gerade eingegeben haben.

![CSV-Datei mit dem Namen "springsale", die erfolgreich hochgeladen wurde.][7]

{:start="2"}
2\. Nachdem Sie „Speichern“ ausgewählt haben, erscheint eine neue Zeile im **Verlauf des Imports**.
3\. Um die Tabelle zu aktualisieren und zu sehen, ob Ihr Import abgeschlossen ist, wählen Sie <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** oben in der Tabelle.

![Aktionscodes, die gerade hochgeladen werden.][8]

{% alert note %}
Der Import größerer Dateien kann einige Minuten dauern. Während Sie warten, können Sie die Seite verlassen und an etwas anderem arbeiten, während der Importvorgang läuft. Wenn der Import abgeschlossen ist, ändert sich der Status in der Tabelle auf **Vollständig**.
{% endalert %}

#### Aktualisieren einer Liste von Aktionscodes

Um eine Liste zu aktualisieren, wählen Sie eine Ihrer bestehenden Listen aus. Sie können den Namen, die Beschreibung, den Ablauf der Liste und die Schwellenwerte für Alarme ändern. Sie können der Liste auch weitere Codes hinzufügen, indem Sie neue Dateien hochladen und **Liste aktualisieren** auswählen.

Alle Codes in der Liste haben das gleiche Ablaufdatum, unabhängig vom Datum des Imports.

### Schritt 5: Aktionscodes verwenden

So versenden Sie Aktionscodes in Nachrichten:

1. Wählen Sie **Snippet kopieren**, um den Code-Snippet zu kopieren, den Sie bei der Erstellung Ihrer Liste mit Aktionscodes festgelegt haben.

![Eine Option zum Kopieren des Snippets zum Einfügen in Ihre Nachricht.][9]{: style="max-width:70%"}

{:start="2"}
2\. Von dort aus können Sie diesen Code in eine Nachricht auf dem Dashboard einfügen.

![Eine Beispielnachricht "Gönnen Sie sich diesen Frühling etwas Schönes mit unserem exklusiven Angebot", gefolgt von dem Code Snippet.][10]{: style="max-width:70%"}

Mit [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) können Sie einen der eindeutigen Aktionscodes aus der hochgeladenen CSV-Datei in eine Nachricht einfügen. Dieser Code wird im Braze-Backend als gesendet markiert, um sicherzustellen, dass keine andere Nachricht denselben Code sendet.

#### Senden von Aktionscodes an Nutzer:innen

Wenn ein Code-Snippet in einer Multichannel-Kampagne oder einem Canvas-Schritt verwendet wird, erhält jeder Benutzer immer einen eindeutigen Code. Für verschiedene Schritte in einem Canvas erhält jeder Benutzer mehrere Aktionscodes.

Wenn ein Nutzer:innen über mehr als einen Kanal einen Code erhalten kann, erhält er über jeden Kanal denselben Code. Wenn ein Nutzer:innen zum Beispiel zwei Nachrichten über zwei Kanäle erhält, bekommt er nur einen Code. Dasselbe gilt für die Berichterstattung: Es wird ein Code gesendet, und der Benutzer erhält diesen Code über die beiden Kanäle. Bei einem Canvas-Schritt mit mehreren Kanälen würde der Nutzer:innen zum Beispiel nur einen Code verwenden.

{% alert important %}
Wenn beim Versenden von Test- oder Live-Nachrichten aus einer Kampagne, die Aktionscodes einbezieht, keine Aktionscodes mehr verfügbar sind, wird die Nachricht nicht versendet.
{% endalert %}

#### Versenden von Testnachrichten mit Aktionscodes

Bei Test- und Startgruppen-E-Mails werden Aktionscodes verwendet, sofern nicht anders gewünscht. Wenden Sie sich an Ihre:n Braze-Account Manager, um dieses Feature zu aktualisieren, damit Aktionscodes bei Testversand und E-Mail-Versand an Seed-Gruppen nicht verwendet werden.

## Feststellen, wie viele Codes verwendet wurden

Die Anzahl der verbleibenden Codes finden Sie in der Spalte **Verbleibend** in der Liste der Aktionscodes auf der Seite **Aktionscodes**.

![Ein Beispiel für einen Aktionscode mit unbenutzten Codes.][12]

Die Anzahl der Codes finden Sie auch, wenn Sie eine bereits existierende Seite mit Aktionscodes aufrufen. Sie können nicht verwendete Codes auch als CSV-Datei exportieren. 

![Ein Aktionscode namens "Black Friday Sale" mit 992 verbleibenden Codes.][13]{: style="max-width:70%"}

## Mehrkanalige und einkanalige Sendungen

Bei Multichannel- und Single-Send-Kampagnen und Canvases werden alle Promotion-Codes, auf die in der Liquid einer Nachricht verwiesen wird, abgezogen, **bevor** die Nachricht versendet wird, um sicherzustellen, dass Folgendes geschieht:

- In einer Multichannel-Nachricht werden auf allen Kanälen die gleichen Aktionscodes verwendet.
- Zusätzliche Aktionscodes werden nicht verwendet, wenn eine Nachricht fehlschlägt oder abbricht.

Wenn ein:e Nutzer:in einer Nachricht, die durch ein Tag der bedingten Logik von Liquid geteilt wird, auf zwei Aktionscodes referenziert, werden trotzdem alle Aktionscodes abgezogen, unabhängig davon, welchem bedingten Flow der Nutzer:innen folgt.

Wenn ein Benutzer einen neuen Canvas-Schritt betritt oder einen Canvas erneut betritt und der Aktionscode Liquid Snippet erneut für eine Nachricht an diesen Benutzer angewendet wird, wird ein neuer Aktionscode verwendet.

### Anwendungsfall

Für das folgende Beispiel werden beide Aktionscode-Listen `vip-deal` und `regular-deal` abgezogen. Hier ist das Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze empfiehlt, mehr Aktionscodes hochzuladen, als Sie voraussichtlich verwenden werden. Wenn eine Aktionscode-Liste abläuft oder keine Aktionscodes mehr vorhanden sind, werden die nachfolgenden Nachrichten abgebrochen.

{% alert tip %}
**Hier ist eine Analogie dafür, wie Aktionscodes in Braze verwendet werden.** <br><br>Stellen Sie sich vor, dass das Versenden Ihrer Nachricht wie das Versenden eines Briefes auf dem Postamt ist. Sie geben den Brief einem Angestellten und dieser sieht, dass Ihr Brief einen Coupon enthalten sollte. Der Angestellte zieht den ersten Coupon aus dem Stapel und legt ihn in den Umschlag. Der Sachbearbeiter schickt den Brief ab, aber aus irgendeinem Grund geht der Brief in der Post verloren (und der Coupon ist nun auch verloren). <br><br>In diesem Szenario ist Braze der Postbeamte und Ihr Aktionscode ist der Coupon. Wir können ihn nicht mehr zurückholen, nachdem er aus dem Stapel der Aktionscodes gezogen wurde, unabhängig vom Ergebnis des Webhooks.
{% endalert %}

## Häufig gestellte Fragen

### Welche Nachrichtenkanäle kann ich mit Aktionscodes verwenden?

Promotion-Codes werden derzeit für E-Mail, Mobile Push, Web Push, Content Cards, Webhook, SMS und WhatsApp unterstützt. Transaktions-E-Mail-Kampagnen und In-App-Nachrichten von Braze unterstützen derzeit keine Promotion-Codes.

### Werden Test- und Seed-Sendungen meine Promotion-Codes aufbrauchen?

Standardmäßig werden bei Test- und Seed-Gruppen-E-Mail-Sendungen Aktionscodes pro Nutzer:in und Testversand verwendet. Sie können sich jedoch an Ihren Braze-Kundenbetreuer wenden, um dieses Verhalten so zu ändern, dass während der Testphase keine Aktionscodes verwendet werden.

### Wie funktionieren Aktionscodes in einer Multichannel-Kampagne oder einem Canvas-Schritt?

Aktionscodes werden abgezogen, bevor die Nachricht versendet wird. Wenn die Messaging-Kanäle in der Kampagne oder Canvas senden, kann dies dazu führen, dass der Promotion-Code aus Gründen wie Ruhezeiten, Tarifbeschränkungen, Frequenzbegrenzung, Ausstiegskriterien und mehr verwendet wird. Wenn jedoch einer der Messaging-Kanäle gesendet wird, wird ein Aktionscode verwendet.

### Was passiert, wenn ich in meiner Nachricht mehrere Liquid-Snippets habe, die auf dieselbe Promotion-Code-Liste verweisen?

Für alle Instanzen des Liquid-Snippets in Ihrer Nachricht wird derselbe Promotion-Code als Vorlage verwendet.

### Was passiert, wenn eine Aktionscode-Liste abgelaufen oder leer ist?

Abgelaufene Codes werden nach sechs Monaten gelöscht.

Wenn die Nachricht einen Aktionscode aus einer leeren oder abgelaufenen Liste enthalten sollte, wird die Nachricht storniert. 

Wenn die Nachricht eine Liquid-Logik enthält, die bedingt einen Aktionscode einfügt, wird die Nachricht nur dann storniert, wenn sie einen Aktionscode hätte enthalten sollen. Wenn die Nachricht keinen Aktionscode enthalten sollte, wird die Nachricht normal gesendet.

### Wie speichere ich einen Aktionscode im Profil eines Nutzers, damit er in nachfolgenden Nachrichten verwendet werden kann?

Um denselben Aktionscode in späteren Nachrichten zu verwenden, muss der Code als benutzerdefiniertes Attribut im Benutzerprofil gespeichert werden. Dies ist möglich, indem Sie einen [Braze-to-Braze-Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/) an dieselbe Kampagne oder denselben Canvas Message-Schritt anhängen.

[1]:{% image_buster /assets/img/promocodes/promocode1.png %}
[3]:{% image_buster /assets/img/promocodes/promocode3.png %}
[4]:{% image_buster /assets/img/promocodes/promocode4.png %}
[5]:{% image_buster /assets/img/promocodes/promocode5.png %}
[7]:{% image_buster /assets/img/promocodes/promocode7.png %}
[8]:{% image_buster /assets/img/promocodes/promocode8.png %}
[9]:{% image_buster /assets/img/promocodes/promocode9.png %}
[10]:{% image_buster /assets/img/promocodes/promocode10.png %}
[12]: {% image_buster /assets/img/promocodes/promocode11.png %}
[13]: {% image_buster /assets/img/promocodes/promocode12.png %}
