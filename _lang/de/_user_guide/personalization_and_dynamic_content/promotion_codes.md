---
nav_title: Aktionscodes
article_title: Aktionscodes
page_order: 5
alias: "/promotion_codes/"
description: "In diesem Referenzartikel erfahren Sie, wie Sie Aktionscode-Listen erstellen und sie zu Ihren Kampagnen und Canvases hinzufügen."

---

# Aktionscodes

> Promotion-Codes - auch Promo-Codes genannt - sind eine großartige Möglichkeit, Nutzer zu binden, indem sie zu Interaktionen anregen, wobei der Schwerpunkt auf Käufen liegt.

Mit der Braze Liquid-Funktionalität bieten wir Ihnen eine Möglichkeit, die Verwendung von Promotion-Codes zu einem Kinderspiel zu machen, indem Nachrichten automatisch und intuitiv aus der von Ihnen bereitgestellten Promotion-Liste gezogen werden können. Das Feature für Aktionscodes bietet Abläufe von bis zu sechs Monaten und Unterstützung für bis zu 20MM individuelle Codes pro Liste.

{% alert important %}
Aktionscodes können nicht in In-App-Nachrichten versendet werden.
{% endalert %}

## Erstellen einer Liste von Aktionscodes

### Schritt 1: Zum Abschnitt „Aktionscode“ navigieren

![][1]{: style="float:right;max-width:30%;margin-left:15px;"}

Gehen Sie auf dem Dashboard zu **Dateneinstellungen** > **Promotion Codes** und wählen Sie dann **Promotion Code Liste erstellen**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Promotion Codes** unter **Integrationen**.
{% endalert %}

### Schritt 2: Aktionscodes benennen und erstellen

Benennen Sie Ihre Aktionscode-Liste und fügen Sie eine optionale Beschreibung hinzu.

![][2]{: style="max-width:90%"}

Als nächstes erstellen Sie ein Snippet für den Code der Aktion. Auf dieses Code-Snippet werden Sie in Liquid verweisen, um diesen spezifischen Satz von Aktionscodes anzuzeigen. Stellen Sie sicher, dass es sich um einen Code-Snippet handelt, der nicht bereits in einer anderen Liste verwendet wird.

{% alert important %}
Bei Snippets wird zwischen Groß- und Kleinschreibung unterschieden. Zum Beispiel werden "Birthday_promo" und "birthday_promo" als zwei verschiedene Snippets erkannt.
{% endalert %}

![][3]{: style="max-width:90%"}

{% alert warning %}
Sie können den Code Snippet nach dem Speichern nicht mehr ändern!
{% endalert %}

### Schritt 3: Optionen für Aktionscodes

Jede Liste mit Aktionscodes hat ein entsprechendes Ablaufdatum und eine entsprechende Uhrzeit, die bei der Erstellung festgelegt werden. Die maximale Gültigkeitsdauer beträgt sechs Monate in der Zukunft ab dem Tag, an dem Sie Ihre Liste erstellen oder bearbeiten. Innerhalb dieser Zeit können Sie das Ablaufdatum wiederholt ändern und aktualisieren. Dieses Ablaufdatum gilt für alle Codes, die zu dieser Liste hinzugefügt werden. Nach Ablauf der Frist werden die Codes aus dem Braze-System gelöscht und alle Nachrichten, die den Codeausschnitt dieser Liste aufrufen, werden nicht gesendet.

![][4]{: style="max-width:90%"}

Sie haben auch die Möglichkeit, optionale und angepasste Schwellenwertwarnungen einzurichten. Wenn Sie diese Benachrichtigungen einrichten, wird der angegebene Empfänger per E-Mail benachrichtigt, wenn die Liste der verfügbaren Aktionscodes in dieser Liste zur Neige geht oder wenn Ihre Aktionscode-Liste bald abläuft. Der Empfänger wird einmal pro Tag benachrichtigt.

![][5]

### Schritt 4: Aktionscode hochladen

Braze verwaltet weder die Erstellung noch die Einlösung von Codes, d.h. Sie müssen Ihre Promotion-Codes in einer CSV-Datei generieren und diese in Braze hochladen. Stellen Sie sicher, dass die CSV-Datei diesen Richtlinien entspricht:

- Enthält eine Spalte für Aktionscodes.
- Hat einen Aktionscode pro Zeile.

Sie können unsere integrierte Integration mit [Voucherify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/voucherify/) oder [Talon.One]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/talonone/) verwenden, um Aktionscodes zu erstellen und zu exportieren.

{% alert note %}
Die maximale Dateigröße beträgt 100 MB und die maximale Listengröße beträgt 20 MM unbenutzte Codes. Wenn Sie feststellen, dass eine falsche Datei hochgeladen wurde, laden Sie eine neue Datei hoch, und die vorherige wird ersetzt.
{% endalert %}

![][6]

Nachdem der Upload abgeschlossen ist, wählen Sie **Liste speichern**, um alle Details und Codes zu speichern, die Sie gerade eingegeben haben.

![][7]

Nachdem Sie „Speichern“ ausgewählt haben, erscheint eine neue Zeile im **Verlauf des Imports**. Um die Tabelle zu aktualisieren und zu sehen, ob Ihr Import abgeschlossen ist, wählen Sie <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** oben in der Tabelle.

![][8]

{% alert note %}
Der Import größerer Dateien kann einige Minuten dauern. Während Sie warten, können Sie die Seite verlassen und an etwas anderem arbeiten, während der Importvorgang läuft. Wenn der Import abgeschlossen ist, ändert sich der Status in der Tabelle auf **Vollständig**.
{% endalert %}

#### Aktualisieren einer Liste von Aktionscodes

Um eine Liste zu aktualisieren, wählen Sie eine Ihrer bestehenden Listen aus. Sie können den Namen, die Beschreibung, den Ablauf der Liste und die Schwellenwerte für Alarme ändern. Sie können der Liste auch weitere Codes hinzufügen, indem Sie neue Dateien hochladen und **Liste aktualisieren** auswählen.

Alle Codes in der Liste haben das gleiche Ablaufdatum, unabhängig vom Datum des Imports.

### Schritt 5: Aktionscodes verwenden

Um Promotion-Codes in Nachrichten zu versenden, wählen Sie **Snippet kopieren**, um das Code-Snippet zu kopieren, das Sie beim Erstellen Ihrer Promotion-Code-Liste festgelegt haben.

![][9]{: style="max-width:70%"}

Von dort aus können Sie diesen Code in eine Nachricht auf dem Dashboard einfügen.

![][10]{: style="max-width:70%"}

Mit [Liquid][11] können Sie einen der eindeutigen Aktionscodes aus der hochgeladenen CSV-Datei in eine Nachricht einfügen. Dieser Code wird im Braze-Backend als gesendet markiert, um sicherzustellen, dass keine andere Nachricht denselben Code sendet. 

Wenn ein Code-Snippet in einer Multichannel-Kampagne oder einem Canvas-Schritt verwendet wird, erhält jeder Benutzer immer einen eindeutigen Code. Für verschiedene Schritte in einem Canvas erhält jeder Benutzer mehrere Aktionscodes.

Wenn ein bestimmter Benutzer berechtigt ist, einen Code über mehr als einen Kanal zu erhalten, erhält dieser Benutzer denselben Code über jeden Kanal. Wenn ein Nutzer:innen zum Beispiel zwei Nachrichten über zwei Kanäle erhält, bekommt er nur einen Code. Dasselbe gilt für die Berichterstattung: Es wird ein Code gesendet, und der Benutzer erhält diesen Code über die beiden Kanäle. Bei einem Canvas-Schritt mit mehreren Kanälen würde der Nutzer:innen zum Beispiel nur einen Code verwenden.

{% alert important %}
Wenn beim Versenden von Test- oder Live-Nachrichten aus einer Kampagne, die Aktionscodes einbezieht, keine Aktionscodes mehr verfügbar sind, wird die Nachricht nicht versendet.
{% endalert %}

#### Versenden von Testnachrichten mit Aktionscodes

Bei Test- und Startgruppen-E-Mails werden Aktionscodes verwendet, sofern nicht anders gewünscht. Wenden Sie sich an Ihre:n Braze-Account Manager, um dieses Feature zu aktualisieren, damit Aktionscodes bei Testversand und E-Mail-Versand an Seed-Gruppen nicht verwendet werden.

## Feststellen, wie viele Codes verwendet wurden

Die Anzahl der verbleibenden Codes finden Sie in der Spalte **Verbleibend** in der Liste der Aktionscodes auf der Seite **Aktionscodes**.

![][12]{: style="max-width:90%"}

Die Anzahl der Codes finden Sie auch, wenn Sie eine bereits existierende Seite mit Aktionscodes aufrufen. 

![][13]{: style="max-width:50%"}

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

Wenn die Nachricht einen Aktionscode aus einer leeren oder abgelaufenen Liste enthalten sollte, wird die Nachricht storniert.

Wenn die Nachricht eine Liquid-Logik enthält, die bedingt einen Aktionscode einfügt, wird die Nachricht nur dann storniert, wenn sie einen Aktionscode hätte enthalten sollen. Wenn die Nachricht keinen Aktionscode enthalten sollte, wird die Nachricht normal gesendet.

### Wie speichere ich einen Aktionscode im Profil eines Nutzers, damit er in nachfolgenden Nachrichten verwendet werden kann?

Um denselben Aktionscode in späteren Nachrichten zu verwenden, muss der Code als benutzerdefiniertes Attribut im Benutzerprofil gespeichert werden. Dies ist möglich, indem Sie einen [Braze-to-Braze-Webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/braze_to_braze_webhooks/) an dieselbe Kampagne oder denselben Canvas Message-Schritt anhängen.

[1]:{% image_buster /assets/img/promocodes/promocode1.png %}
[2]:{% image_buster /assets/img/promocodes/promocode2.png %}
[3]:{% image_buster /assets/img/promocodes/promocode3.png %}
[4]:{% image_buster /assets/img/promocodes/promocode4.png %}
[5]:{% image_buster /assets/img/promocodes/promocode5.png %}
[6]:{% image_buster /assets/img/promocodes/promocode6.png %}
[7]:{% image_buster /assets/img/promocodes/promocode7.png %}
[8]:{% image_buster /assets/img/promocodes/promocode8.png %}
[9]:{% image_buster /assets/img/promocodes/promocode9.png %}
[10]:{% image_buster /assets/img/promocodes/promocode10.png %}
[11]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[12]: {% image_buster /assets/img/promocodes/promocode11.png %}
[13]: {% image_buster /assets/img/promocodes/promocode12.png %}
