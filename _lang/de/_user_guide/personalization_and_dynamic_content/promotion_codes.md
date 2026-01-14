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

## Über Aktionscodes

Aktionscodes - auch Promo-Codes genannt - sind eine großartige Möglichkeit, das Engagement der Nutzer:innen zu erhalten, indem sie zu Interaktionen mit einem starken Schwerpunkt auf Käufen führen. Sie können Nachrichten erstellen, die aus Ihrer Liste von Aktionscodes stammen. 

Jeder Aktionscode hat eine Gültigkeitsdauer von bis zu sechs Monaten. Sie können bis zu 20 Millionen Codes pro Liste speichern und verwalten. Durch die Verwaltung und Analyse der Performance Ihrer Aktionscodes können Sie gezielte Entscheidungen für Ihre Strategien und Nachrichten treffen.

{% alert important %}
Aktionscodes können nicht in In-App-Nachrichten in Canvas verschickt werden.
{% endalert %}

## Erstellen einer Liste von Aktionscodes {#create}

### Schritt 1: Gehen Sie zum Abschnitt Aktionscode

\![Button zum Erstellen eines Aktionscodes.]({% image_buster /assets/img/promocodes/promocode1.png %}){: style="float:right;max-width:30%;margin-left:15px;"}

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

\![Eine Liste mit Aktionscodes namens "SpringSale2025" mit dem Code Snippet "spring25".]({% image_buster /assets/img/promocodes/promocode3.png %}){: style="max-width:80%"}

### Schritt 3: Wählen Sie die Optionen für den Aktionscode

Jede Liste mit Aktionscodes hat ein entsprechendes Ablaufdatum und eine entsprechende Uhrzeit, die bei der Erstellung festgelegt werden. Die maximale Gültigkeitsdauer beträgt sechs Monate in der Zukunft ab dem Tag, an dem Sie Ihre Liste erstellen oder bearbeiten. 

Innerhalb dieser Zeit können Sie das Ablaufdatum wiederholt ändern und aktualisieren. Dieses Ablaufdatum gilt für alle Codes, die zu dieser Liste hinzugefügt werden. Nach Ablauf werden die Codes aus dem Braze-System gelöscht und alle Nachrichten, die den Code-Snippet dieser Liste aufrufen, werden nicht gesendet.

Die Ablaufeinstellungen der Liste besagen, dass alle verbleibenden Codes am 30\. April 2025 um 12 Uhr ablaufen werden.]({% image_buster /assets/img/promocodes/promocode4.png %}){: style="max-width:80%"}

Sie haben auch die Möglichkeit, optionale und angepasste Schwellenwertwarnungen einzurichten. Wenn Sie diese Benachrichtigungen einrichten, erhalten die angegebenen Empfänger:in eine E-Mail, wenn nur noch wenige Aktionscodes in dieser Liste verfügbar sind oder wenn Ihre Liste mit Aktionscodes bald abläuft. Der Empfänger wird einmal pro Tag benachrichtigt.

\![Ein Beispiel für einen Schwellenwertalarm, der "marketing@abc.com" benachrichtigt, wenn die Liste der Aktionscodes in 5 Tagen abläuft.]({% image_buster /assets/img/promocodes/promocode5.png %}){: style="max-width:80%"}

### Schritt 4: Aktionscodes hochladen

Braze verwaltet weder die Erstellung noch die Einlösung von Codes, d.h. Sie müssen Ihre Aktionscodes in einer CSV-Datei generieren und diese in Braze hochladen. 

Stellen Sie sicher, dass Ihre CSV-Datei diesen Richtlinien entspricht:

- Enthält eine Spalte für Aktionscodes.
- Hat einen Aktionscode pro Zeile.

Sie können unsere integrierte Integration mit [Voucherify]({{site.baseurl}}/partners/ecommerce/loyalty/voucherify/) oder [Talon.One]({{site.baseurl}}/partners/ecommerce/loyalty/talonone/) verwenden, um Aktionscodes zu erstellen und zu exportieren.

{% alert important %}
Die maximale Dateigröße beträgt 100 MB, und die maximale Listengröße beträgt 20MM unbenutzte Codes. Wenn Sie feststellen, dass eine falsche Datei hochgeladen wurde, laden Sie eine neue Datei hoch, und die vorherige wird ersetzt.
{% endalert %}

1. Nachdem der Upload abgeschlossen ist, wählen Sie **Liste speichern**, um alle Details und Codes zu speichern, die Sie gerade eingegeben haben.

\![CSV-Datei namens "springsale", die erfolgreich hochgeladen wurde.]({% image_buster /assets/img/promocodes/promocode7.png %})

{:start="2"}
2\. Nachdem Sie „Speichern“ ausgewählt haben, erscheint eine neue Zeile im **Verlauf des Imports**.
3\. Um die Tabelle zu aktualisieren und zu sehen, ob Ihr Import abgeschlossen ist, wählen Sie <span style="font-size: 14px;margin-bottom: .5rem;height: 16px;width: 16px;" class="fas fa-sync" ></span> **Sync** oben in der Tabelle.

\![Aktionscodes werden gerade hochgeladen.]({% image_buster /assets/img/promocodes/promocode8.png %})

{% alert note %}
Der Import größerer Dateien kann einige Minuten dauern. Während Sie warten, können Sie die Seite verlassen und an etwas anderem arbeiten, während der Importvorgang läuft. Wenn der Import abgeschlossen ist, ändert sich der Status in der Tabelle auf **Vollständig**.
{% endalert %}

## Aktualisieren einer Liste von Aktionscodes

Um eine Liste zu aktualisieren, wählen Sie eine Ihrer bestehenden Listen aus. Sie können den Namen, die Beschreibung, den Ablauf der Liste und die Schwellenwerte für Alarme ändern. Sie können der Liste auch weitere Codes hinzufügen, indem Sie neue Dateien hochladen und **Liste aktualisieren** auswählen. Alle Codes in der Liste haben das gleiche Ablaufdatum, unabhängig vom Datum des Imports.

{% alert important %}
Aktionscodes können nicht gelöscht werden.
{% endalert %}

### Ändern einer falschen Liste von Aktionscodes 

Wenn Sie eine CSV-Datei mit den falschen Aktionscodes hochgeladen und **Liste speichern** ausgewählt haben, können Sie das Problem mit einer der beiden Methoden beheben:

- Verwerfen Sie die gesamte Liste: Verwenden Sie die aktuelle Liste der Aktionscodes nicht mehr in Kampagnen, Canvase oder Templates. Laden Sie dann die CSV-Datei mit den richtigen Codes hoch und verwenden Sie sie in Ihren Nachrichten.
- Verwenden Sie die falschen Codes: Erstellen Sie eine Kampagne, die Aktionscodes aus der Liste der falschen Aktionscodes an einen Platzhalter sendet, bis alle falschen Codes verwendet wurden. Laden Sie dann die richtigen Aktionscodes in dieselbe Liste hoch.

## Aktionscodes verwenden {#update}

Um einen Aktionscode in einer Nachricht zu versenden, wählen Sie **Snippet kopieren** neben der Aktionscode-Liste [, die Sie zuvor erstellt haben](#create).

\![Eine Option zum Kopieren des Snippets zum Einfügen in Ihre Nachricht.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:50%"}

Fügen Sie die Code-Snippets in eine Ihrer Nachrichten in Braze ein, und verwenden Sie dann [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), um einen der eindeutigen Aktionscodes aus Ihrer Liste einzufügen. Dieser Code wird als gesendet markiert und stellt sicher, dass keine andere Nachricht denselben Code sendet.

\![Eine Beispielnachricht "Gönnen Sie sich diesen Frühling etwas Schönes mit unserem exklusiven Angebot", gefolgt von dem Code Snippet.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:50%"}

### Über Canvas-Schritte

Wenn ein Code-Snippet in einer Kampagne oder einem Canvas mit Multichannel-Nachrichten verwendet wird, erhält jeder Nutzer:innen einen eindeutigen Code. In einem Canvas mit mehreren Schritten, die auf Aktionscodes referenzieren, erhält ein Nutzer:innen für jeden Schritt, den er eingibt, einen neuen Code.

So weisen Sie einen Aktionscode in einem Canvas zu und verwenden ihn in verschiedenen Schritten wieder:

1. Weisen Sie den Aktionscode als angepasstes Attribut im ersten Schritt (Nutzer:innen Update) zu.
2. Verwenden Sie Liquid in späteren Schritten, um dieses angepasste Attribut zu referenzieren, anstatt einen neuen Code zu generieren.

Wenn sich ein Nutzer:innen über mehrere Kanäle für einen Code qualifiziert, erhält er in jedem Kanal denselben Code. Wenn sie zum Beispiel Nachrichten per E-Mail und Push erhalten, wird derselbe Code an beide gesendet. Die Berichterstattung erfolgt ebenfalls über einen einzigen Code.

{% alert note %}
Wenn keine Aktionscodes verfügbar sind, werden Test- oder Live-Nachrichten, die auf Codes basieren, nicht gesendet.
{% endalert %}

### In-App-Nachricht-Kampagnen {#promotion-codes-iam-campaigns}

Nachdem Sie eine [In-App-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) erstellt haben, können Sie ein [Snippet mit einer Liste von Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) in den Nachrichtentext Ihrer In-App-Nachrichten einfügen. 

Aktionscodes in In-App-Nachrichten werden nur dann abgezogen und verwendet, wenn ein Nutzer:innen die Anzeige der In-App-Nachricht triggert.

### In Test Nachrichten

Bei Test- und Startgruppen-E-Mails werden Aktionscodes verwendet, sofern nicht anders gewünscht. Wenden Sie sich an Ihre:n Braze-Account Manager, um dieses Feature zu aktualisieren, damit Aktionscodes bei Testversand und E-Mail-Versand an Seed-Gruppen nicht verwendet werden.

### Mit Nachrichten-Extras für Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Speichern von Aktionscodes in Nutzerprofilen {#save-to-profile}

Um denselben Aktionscode in späteren Nachrichten zu verwenden, muss der Code als benutzerdefiniertes Attribut im Benutzerprofil gespeichert werden. Dies kann durch ein [Nutzer:innen-Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) geschehen, das den Rabattcode einem angepassten Attribut wie "Promo Code" direkt vor einem Messaging-Schritt zuweist.

Wählen Sie zunächst für jedes Feld im Schritt Nutzer:innen aktualisieren Folgendes aus:

- **Attributname:** Promo Code
- **Aktion:** Aktualisieren
- **Schlüssel-Wert:** Das Liquid Code Snippet des Aktionscodes, wie z.B. {% raw %}`{% promotion('spring25') %}`{% endraw %}

Zweitens: Fügen Sie das angepasste Attribut (in diesem Beispiel {% raw %}`{{custom_attribute.${Promo Code}}`{% endraw %}) zu einer Nachricht hinzu. Der Rabattcode wird in einem Template erstellt.

## Anzeigen der Verwendung von Aktionscodes

Die Anzahl der verbleibenden Codes finden Sie in der Spalte **Verbleibend** in der Liste der Aktionscodes auf der Seite **Aktionscodes**.

\![Ein Beispiel für einen Aktionscode mit unbenutzten Codes.]({% image_buster /assets/img/promocodes/promocode11.png %})

Die Anzahl der Codes finden Sie auch, wenn Sie eine bereits existierende Seite mit Aktionscodes aufrufen. Sie können nicht verwendete Codes auch als CSV-Datei exportieren. 

\![Ein Aktionscode namens "Black Friday Sale" mit 992 verbleibenden Codes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:50%"}

## Mehrkanalige und einkanalige Sendungen

Bei Multichannel- und Single-Send-Kampagnen und Canvases werden alle Promotion-Codes, auf die in der Liquid einer Nachricht verwiesen wird, abgezogen, **bevor** die Nachricht versendet wird, um sicherzustellen, dass Folgendes geschieht:

- In einer Multichannel-Nachricht werden auf allen Kanälen die gleichen Aktionscodes verwendet.
- Zusätzliche Aktionscodes werden nicht verwendet, wenn eine Nachricht fehlschlägt oder abbricht.

Wenn ein:e Nutzer:in einer Nachricht, die durch ein Tag der bedingten Logik von Liquid geteilt wird, auf zwei Aktionscodes referenziert, werden trotzdem alle Aktionscodes abgezogen, unabhängig davon, welchem bedingten Flow der Nutzer:innen folgt.

Wenn ein Benutzer einen neuen Canvas-Schritt betritt oder einen Canvas erneut betritt und der Aktionscode Liquid Snippet erneut für eine Nachricht an diesen Benutzer angewendet wird, wird ein neuer Aktionscode verwendet.

### Beispiel

In dem folgenden Beispiel werden beide Aktionscode-Listen `vip-deal` und `regular-deal` abgezogen. Hier ist das Liquid:

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
**Hier ist eine Analogie dafür, wie Aktionscodes in Braze verwendet werden.** <br><br>Stellen Sie sich vor, dass das Versenden Ihrer Nachricht wie das Versenden eines Briefes auf dem Postamt ist. Sie geben den Brief einem Angestellten und dieser sieht, dass Ihr Brief einen Coupon enthalten sollte. Der Angestellte zieht den ersten Coupon aus dem Stapel und legt ihn in den Umschlag. Der Sachbearbeiter schickt den Brief ab, aber aus irgendeinem Grund geht der Brief in der Post verloren (und der Coupon ist nun auch verloren). <br><br>In diesem Szenario ist Braze der Postbeamte, und Ihr Aktionscode ist der Coupon. Wir können ihn nicht mehr abrufen, nachdem er aus dem Stack der Aktionscodes gezogen wurde, unabhängig vom Ergebnis des Webhooks.
{% endalert %}

## Häufig gestellte Fragen

### Welche Nachrichtenkanäle kann ich mit Aktionscodes verwenden?

Promotion-Codes werden derzeit für E-Mail, Mobile Push, Web Push, Content Cards, Webhook, SMS und WhatsApp unterstützt. Transaktions-E-Mail-Kampagnen und In-App-Nachrichten von Braze unterstützen derzeit keine Promotion-Codes.

### Zählen Test- und Seed-Sendungen zur Nutzung?

Standardmäßig werden bei Test- und Seed-Gruppen-E-Mail-Sendungen Aktionscodes pro Nutzer:in und Testversand verwendet. Sie können sich jedoch an Ihren Braze-Kundenbetreuer wenden, um dieses Verhalten so zu ändern, dass während der Testphase keine Aktionscodes verwendet werden.

### Was passiert, wenn mehrere Messaging-Kanäle denselben Aktionscode-Snippet verwenden?

Wenn ein bestimmter Nutzer:innen für den Erhalt eines Codes über mehrere Kanäle berechtigt ist, erhält er denselben Code über jeden Kanal. Unabhängig von den empfangenen Kanälen wird nur ein Promo Code verwendet.

### Kann ich mehrere Liquid Snippets verwenden, um dieselbe Liste von Aktionscodes in einer Nachricht zu referenzieren?

Ja Braze wendet denselben Aktionscode auf alle Instanzen dieses Snippets in der Nachricht an und stellt so sicher, dass der Nutzer:innen nur einen eindeutigen Code erhält.

### Was passiert, wenn eine Aktionscode-Liste abgelaufen oder leer ist?

Abgelaufene Codes werden nach sechs Monaten gelöscht.

Wenn die Nachricht einen Aktionscode aus einer leeren oder abgelaufenen Liste enthalten sollte, wird die Nachricht storniert. 

Wenn die Nachricht eine Liquid-Logik enthält, die bedingt einen Aktionscode einfügt, wird die Nachricht nur dann storniert, wenn sie einen Aktionscode hätte enthalten sollen. Wenn die Nachricht keinen Aktionscode enthalten sollte, wird die Nachricht normal gesendet.

### Wenn ich die falschen Aktionscodes hochgeladen habe, kann ich sie dann aktualisieren?

Ja Sie können dieses Problem lösen, indem Sie die gesamte Liste verwerfen oder einen Platzhalter verwenden, um die Liste zu löschen. Weitere Informationen finden Sie unter [Aktualisieren von Aktionscodes](#update).

### Kann ich einen Aktionscode im Profil eines Nutzers:innen für zukünftige Nachrichten speichern?

Ja Sie können Aktionscodes im Profil eines Nutzers:innen über den Schritt User Update speichern. Weitere Informationen finden Sie unter [Aktionscodes in Nutzerprofilen speichern](#save-to-profile).
