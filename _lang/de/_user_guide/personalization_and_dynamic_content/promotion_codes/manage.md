---
nav_title: Codes verwenden
article_title: Aktionscodes verwenden
page_order: 0.2
description: "Erfahren Sie, wie Sie Aktionscodes verwenden und die Verwendung für Ihre Kampagnen und Canvase einsehen können."
---

# Aktionscodes verwenden

> Erfahren Sie, wie Sie Aktionscodes verwenden und die Verwendung für Ihre Kampagnen und Canvase einsehen können.

## Voraussetzungen

Bevor Sie Aktionscodes verwenden können, müssen Sie [eine Liste mit Aktionscodes erstellen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/).

## Aktionscodes verwenden

Um einen Aktionscode in einer Nachricht zu versenden, wählen Sie **Snippet kopieren** neben der Aktionscode-Liste [, die Sie zuvor erstellt haben]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#create).

![Eine Option zum Kopieren des Snippets zum Einfügen in Ihre Nachricht.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Fügen Sie die Code-Snippets in eine Ihrer Nachrichten in Braze ein, und verwenden Sie dann [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/), um einen der eindeutigen Aktionscodes aus Ihrer Liste einzufügen. Dieser Code wird als gesendet markiert, um sicherzustellen, dass keine andere Nachricht denselben Code sendet.

![Eine Beispielnachricht "Gönnen Sie sich diesen Frühling etwas Schönes mit unserem exklusiven Angebot", gefolgt von dem Code Snippet.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Über Canvas-Schritte

Wenn ein Code-Snippet in einer Kampagne oder einem Canvas mit Multichannel-Nachrichten verwendet wird, erhält jeder Nutzer:innen einen eindeutigen Code. In einem Canvas mit mehreren Schritten, die Aktionscodes referenzieren, erhält ein Nutzer:innen für jeden Schritt, den er eingibt, einen neuen Code.

So weisen Sie einen Aktionscode in einem Canvas zu und verwenden ihn in verschiedenen Schritten wieder:

1. Weisen Sie den Aktionscode als angepasstes Attribut im ersten Schritt (Nutzer:innen Update) zu.
2. Verwenden Sie Liquid in späteren Schritten, um dieses angepasste Attribut zu referenzieren, anstatt einen neuen Code zu erzeugen.

Wenn sich ein Nutzer:innen über mehrere Kanäle für einen Code qualifiziert, erhält er in jedem Kanal denselben Code. Wenn sie zum Beispiel Nachrichten per E-Mail und Push erhalten, wird derselbe Code an beide gesendet. Die Berichterstattung erfolgt ebenfalls über einen einzigen Code.

{% alert note %}
Wenn keine Aktionscodes verfügbar sind, werden Test- oder Live-Nachrichten, die auf Codes basieren, nicht gesendet.
{% endalert %}

### In-App-Nachricht-Kampagnen {#promotion-codes-iam-campaigns}

Nachdem Sie eine [In-App-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) erstellt haben, können Sie ein [Snippet mit einer Liste von Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes-1) in den Nachrichtentext Ihrer In-App-Nachrichten einfügen. Aktionscodes in In-App-Nachrichten werden nur dann abgezogen und verwendet, wenn ein Nutzer:innen die Anzeige der In-App-Nachricht triggert.

### Nachrichten testen

Bei Testversand und E-Mail-Versand an Seed-Gruppen werden Aktionscodes verwendet, sofern nicht anders angefragt. Wenden Sie sich an Ihre:n Braze-Account Manager, um dieses Feature zu aktualisieren, damit Aktionscodes bei Testversand und E-Mail-Versand an Seed-Gruppen nicht verwendet werden.

### Mit Nachrichten-Extras für Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Speichern von Aktionscodes in Nutzerprofilen {#save-to-profile}

Um denselben Aktionscode in späteren Nachrichten zu verwenden, muss der Code als benutzerdefiniertes Attribut im Benutzerprofil gespeichert werden. Dies kann durch ein [Nutzer:innen-Update]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) geschehen, das den Rabattcode einem angepassten Attribut wie "Promo Code" direkt vor einem Messaging-Schritt zuweist.

Wählen Sie zunächst im Schritt Nutzer:innen aktualisieren für jedes Feld Folgendes aus:

- **Attributname:** Promo Code
- **Aktion:** Aktualisieren
- **Schlüssel-Wert:** Das Liquid Code Snippet des Aktionscodes, wie z.B. {% raw %}`{% promotion('spring25') %}`{% endraw %}

Zweitens: Fügen Sie das angepasste Attribut (in diesem Beispiel {% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %}) zu einer Nachricht hinzu. Der Rabattcode ist in einem Template enthalten.

## Anzeigen der Verwendung von Aktionscodes

Die Anzahl der verbleibenden Codes finden Sie in der Spalte **Verbleibend** in der Liste der Aktionscodes auf der Seite **Aktionscodes**.

![Ein Beispiel für einen Aktionscode mit unbenutzten Codes.]({% image_buster /assets/img/promocodes/promocode11.png %})

Die Anzahl der Codes finden Sie auch, wenn Sie eine bereits existierende Seite mit Aktionscodes aufrufen. Sie können nicht verwendete Codes auch als CSV-Datei exportieren. 

![Ein Aktionscode namens "Black Friday Sale" mit 992 verbleibenden Codes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Mehrkanalige und einkanalige Sendungen

Bei Multichannel- und Single-Send-Kampagnen und Canvases werden alle Promotion-Codes, auf die in der Liquid einer Nachricht verwiesen wird, abgezogen, **bevor** die Nachricht versendet wird, um sicherzustellen, dass Folgendes geschieht:

- In einer Multichannel-Nachricht werden auf allen Kanälen die gleichen Aktionscodes verwendet.
- Zusätzliche Aktionscodes werden nicht verwendet, wenn eine Nachricht fehlschlägt oder abbricht.

Wenn ein Nutzer:in einer Nachricht, die durch ein Tag der bedingten Logik von Liquid geteilt wird, auf zwei Aktionscodes referenziert, werden trotzdem alle Aktionscodes abgezogen, unabhängig davon, welchem bedingten Fluss der Nutzer folgt.

Wenn ein Nutzer:innen einen neuen Canvas-Schritt betritt oder ein Canvas erneut betritt und der Aktionscode Liquid Snippet erneut für eine Nachricht an diesen Nutzer:innen angewendet wird, wird ein neuer Aktionscode verwendet.

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
