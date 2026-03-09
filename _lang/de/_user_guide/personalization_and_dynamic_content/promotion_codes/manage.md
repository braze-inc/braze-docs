---
nav_title: Verwendung von Codes
article_title: Verwendung von Aktionscodes
page_order: 0.2
description: "Erfahren Sie, wie Sie Aktionscodes verwenden und die Nutzung für Ihre Kampagnen und Canvases anzeigen können."
---

# Verwendung von Aktionscodes

> Erfahren Sie, wie Sie Aktionscodes verwenden und die Nutzung für Ihre Kampagnen und Canvases anzeigen können.

## Voraussetzungen

Bevor Sie Aktionscodes verwenden können, müssen Sie [eine Liste mit Aktionscodes erstellen]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/).

## Verwendung von Aktionscodes

Um einen Aktionscode in einer Nachricht zu versenden, wählen Sie **bitte „Snippet auswählen“** neben der [zuvor erstellten]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/create/#create) Aktionscodeliste.

![Eine Option zum Kopieren des Snippets zum Einfügen in Ihre Nachricht.]({% image_buster /assets/img/promocodes/promocode9.png %}){: style="max-width:70%"}

Fügen Sie die Code-Snippets in eine Ihrer Nachrichten in Braze ein und verwenden Sie anschließend [Liquid,]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) um einen der eindeutigen Aktionscodes aus Ihrer Liste einzufügen. Dieser Code wird als gesendet markiert, um sicherzustellen, dass keine andere Nachricht denselben Code sendet.

![Eine Beispielnachricht "Gönnen Sie sich diesen Frühling etwas Schönes mit unserem exklusiven Angebot", gefolgt von dem Code Snippet.]({% image_buster /assets/img/promocodes/promocode10.png %}){: style="max-width:70%"}

### Über Canvas-Schritte hinweg

Wenn ein Code-Snippet in einer Kampagne oder Canvas mit Multichannel-Nachrichten verwendet wird, erhält jede Nutzer:in einen eindeutigen Code. In einem Canvas mit mehreren Schritten, die Aktionscodes referenzieren, erhält eine Nutzer:in für jeden Schritt, den sie ausführt, einen neuen Code.

Um einen Aktionscode in einem Canvas zuzuweisen und über mehrere Schritte hinweg wiederzuverwenden:

1. Weisen Sie den Aktionscode im ersten Schritt (Benutzeraktualisierung) als angepasstes Attribut zu.
2. Verwenden Sie Liquid in späteren Schritten, um dieses angepasste Attribut zu referenzieren, anstatt einen neuen Code zu generieren.

Wenn ein Nutzer:in sich über mehrere Kanäle für einen Code qualifiziert, erhält er in jedem Kanal denselben Code. Wenn sie beispielsweise Nachrichten per E-Mail und Push erhalten, wird derselbe Code an beide gesendet. Die Berichterstattung spiegelt ebenfalls einen einzigen Code wider.

{% alert note %}
Wenn keine Aktionscodes verfügbar sind, werden Test- oder Live-Nachrichten, die auf Codes basieren, nicht versendet.
{% endalert %}

### In-App-Nachrichten-Kampagnen {#promotion-codes-iam-campaigns}

Nachdem Sie eine [In-App-Kampagne]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages) erstellt haben, können Sie ein [Snippet mit einer Liste von Aktionscodes]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/manage/#using-promotion-codes-1) in den Nachrichtentext Ihrer In-App-Nachrichten einfügen. Aktionscodes in In-App-Nachrichten werden nur abgezogen und verwendet, wenn ein Nutzer die Anzeige der In-App-Nachricht triggert.

### Testnachrichten

Test-E-Mails und E-Mail-Versendungen an Seed-Gruppen verbrauchen Aktionscodes, sofern nicht anders angegeben. Wenden Sie sich an Ihre:n Braze-Account Manager, um dieses Feature zu aktualisieren, damit Aktionscodes bei Testversand und E-Mail-Versand an Seed-Gruppen nicht verwendet werden.

### Mit zusätzlichen Nachrichten für Currents

{% multi_lang_include shopify.md section='Liquid promotion codes with Currents' %}

## Speichern von Aktionscodes in Nutzerprofilen {#save-to-profile}

Um denselben Aktionscode in späteren Nachrichten zu verwenden, muss der Code als benutzerdefiniertes Attribut im Benutzerprofil gespeichert werden. Dies kann über einen [Schritt „Benutzeraktualisierung“]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update/) erfolgen, der den Rabattcode einem benutzerdefinierten Attribut, beispielsweise „Promo-Code“, unmittelbar vor einem Schritt „Nachricht“ zuweist.

Wählen Sie zunächst für jedes Feld im Schritt „Update für Nutzer:innen“ Folgendes aus:

- **Attributname:** Aktionscode
- **Aktion:** Aktualisieren
- **Schlüssel-Wert:** Der Liquid-Code-Snippet des Aktionscodes, wie beispielsweise {% raw %}`{% promotion('spring25') %}`{% endraw %}

Fügen Sie zweitens das angepasste Attribut (in diesem Beispiel ){% raw %}`{{custom_attribute.${Promo Code}}}`{% endraw %} zu einer Nachricht hinzu. Der Rabattcode ist im Template enthalten.

## Anzeige der Verwendung von Aktionscodes

Die Anzahl der verbleibenden Codes finden Sie in der Spalte **Verbleibend** in der Liste der Aktionscodes auf der Seite **Aktionscodes**.

![Ein Beispiel für einen Aktionscode mit unbenutzten Codes.]({% image_buster /assets/img/promocodes/promocode11.png %})

Die Anzahl der Codes finden Sie auch, wenn Sie eine bereits existierende Seite mit Aktionscodes aufrufen. Sie können nicht verwendete Codes auch als CSV-Datei exportieren. 

![Ein Aktionscode namens "Black Friday Sale" mit 992 verbleibenden Codes.]({% image_buster /assets/img/promocodes/promocode12.png %}){: style="max-width:70%"}

## Mehrkanalige und einkanalige Sendungen

Bei Multichannel- und Single-Send-Kampagnen und Canvases werden alle Promotion-Codes, auf die in der Liquid einer Nachricht verwiesen wird, abgezogen, **bevor** die Nachricht versendet wird, um sicherzustellen, dass Folgendes geschieht:

- In einer Multichannel-Nachricht werden auf allen Kanälen die gleichen Aktionscodes verwendet.
- Zusätzliche Aktionscodes werden nicht verwendet, wenn eine Nachricht fehlschlägt oder abbricht.

Wenn ein Nutzer:in zwei Listen mit Aktionscodes in einer Nachricht hat, die durch ein Liquid-Tag für bedingte Logik getrennt sind, werden alle Aktionscodes weiterhin abgezogen, unabhängig davon, welchem Bedingungsablauf der Nutzer:in folgt.

Wenn ein Nutzer:in einen neuen Canvas-Schritt aufruft oder erneut in einen Canvas eintritt und der Liquid-Snippet für den Aktionscode erneut für eine Nachricht an diesen Nutzer:in angewendet wird, wird ein neuer Aktionscode verwendet.

### Beispiel

Im folgenden Beispiel werden sowohl die Listen mit`regular-deal` `vip-deal`Aktionscodes  als auch  abgezogen. Hier ist das Liquid:

{% raw %}
```
{% if user.is_vip %}
  {% promotion('vip-deal') %}
{% else %}
  {% promotion('regular-deal') %}
{% endif %} 
```
{% endraw %}

Braze empfiehlt, mehr Aktionscodes hochzuladen, als Sie voraussichtlich verwenden werden. Wenn eine Liste mit Aktionscodes abläuft oder keine Aktionscodes mehr enthält, werden die nachfolgenden Nachrichten abgebrochen.

{% alert tip %}
**Hier ist eine Analogie dafür, wie Aktionscodes in Braze verwendet werden.** <br><br>Stellen Sie sich vor, dass das Versenden Ihrer Nachricht wie das Versenden eines Briefes auf dem Postamt ist. Sie geben den Brief einem Angestellten und dieser sieht, dass Ihr Brief einen Coupon enthalten sollte. Der Angestellte zieht den ersten Coupon aus dem Stapel und legt ihn in den Umschlag. Der Sachbearbeiter schickt den Brief ab, aber aus irgendeinem Grund geht der Brief in der Post verloren (und der Coupon ist nun auch verloren). <br><br>In diesem Szenario fungiert Braze als Postbeamter und Ihr Aktionscode als Gutschein. Wir können ihn nicht wiederherstellen, nachdem er aus dem Stack der Aktionscodes entfernt wurde, unabhängig vom Ergebnis des Webhooks.
{% endalert %}
