---
nav_title: Integration
article_title: Übersicht der In-App Nachrichten für iOS
platform: Swift
page_order: 0
description: "Dieser Artikel behandelt die verschiedenen Arten von In-App-Nachrichten für iOS, das erwartete Verhalten und verschiedene Anwendungsfälle für das Swift SDK."
channel:
  - in-app messages

---

# Integration von In-App-Nachrichten

> Mit [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) können Sie Inhalte an Ihre Nutzer übermitteln, ohne sie mit einer Push-Benachrichtigung zu unterbrechen. Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größtmöglichen Nutzen aus Ihrer App zu ziehen. Mit einer Vielzahl von Layouts und Anpassungswerkzeugen, aus denen Sie wählen können, binden In-App-Nachrichten Ihre Nutzer mehr als je zuvor.

In unseren [Fallstudien](https://www.braze.com/customers) finden Sie Beispiele für In-App-Nachrichten.

## Arten von In-App-Nachrichten

Braze bietet derzeit die folgenden standardmäßigen In-App-Nachrichtenarten: 

- Slideup
- Modal
- Modal-Bild
- Vollständig
- Volles Bild
- Angepasstes HTML
- Kontrollgruppe

Jede Art von In-App-Nachricht ist in Bezug auf Inhalt, Bilder, Symbole, Klickaktionen, Analytics, Anzeige und Zustellung in hohem Maße anpassbar.

Eine vollständige Liste der Eigenschaften von In-App-Nachrichten und deren Verwendung finden Sie in der [Dokumentation zur Klasse`InAppMessage`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

Alle In-App-Nachrichten sind enum-Typen von `Braze.InAppMessage`, die das grundlegende Verhalten und die Merkmale für alle In-App-Nachrichten definiert. Jede Art von In-App-Nachricht und die entsprechenden Details sind in den folgenden Tabs aufgeführt.

### Erwartete Verhaltensweisen nach Nachrichtentypen

So sieht es aus, wenn Ihre Nutzer eine unserer Standardarten von In-App-Nachrichten öffnen.

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) In-App-Nachrichten werden so genannt, weil sie vom oberen oder unteren Bildschirmrand nach oben oder unten gleiten. Sie bedecken nur einen kleinen Teil des Bildschirms und bieten eine effektive und unaufdringliche Möglichkeit zur Nachrichtenübermittlung.

![Eine Slideup-In-App-Nachricht am unteren und oberen Rand eines Handy-Displays.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Feld eingerahmt. Für kritische Nachrichten können sie mit bis zu zwei Analytics-fähigen Buttons ausgestattet werden.

![Eine Modal-In-App-Nachricht in der Mitte des Handydisplays. ]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Modal-Bild %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Feld eingerahmt. Diese Nachrichten ähneln dem Typ `Modal`, jedoch ohne Kopfzeile oder Nachrichtentext. Für kritische Nachrichten können sie mit bis zu zwei Analytics-fähigen Buttons ausgestattet werden.

![Eine Modal-Bild-In-App-Nachricht in der Mitte des Handydisplays ]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Vollbild %}

In-App-Nachrichten des Typs [`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) sind nützlich, um den Inhalt und die Wirkung Ihrer Nutzerkommunikation zu maximieren. Die obere Hälfte einer In-App-Nachricht des Typs `Full` enthält ein Bild. Die untere Hälfte enthält Text und bis zu zwei Analytics-fähige Buttons.

![Eine Fullscreen-In-App-Nachricht, die auf dem gesamten Handydisplay angezeigt wird.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Vollbild Bild %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct)-In-App-Nachrichten sind ähnlich wie `Full` In-App-Nachrichten, jedoch ohne Kopfzeile oder Nachrichtentext. Dieser Nachrichtentyp ist nützlich, um den Inhalt und die Wirkung Ihrer Nutzer-Kommunikation zu maximieren. Eine `Full Image`-In-App-Nachricht enthält ein Bild, das sich über den gesamten Bildschirm erstreckt, mit der Option, bis zu zwei Analytics-aktivierte Buttons anzuzeigen.

![Eine Fullscreen-Bild-In-App-Nachricht, die auf dem gesamten Handydisplay angezeigt wird.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endtab %}
{% tab Benutzerdefiniertes HTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct)-In-App-Nachrichten sind nützlich, um vollständig angepasste Nutzerhalte zu erstellen. Der gesamte Inhalt von benutzerdefinierten HTML-Full-In-App-Nachrichten wird in `WKWebView`angezeigt und kann optional anderen Rich Content wie Bilder und Schriftarten enthalten. So haben Sie die volle Kontrolle über das Aussehen und die Funktionalität der Nachrichten. <br><br>iOS In-App-Nachrichten unterstützen eine JavaScript `brazeBridge` Schnittstelle, um Methoden des Braze Web SDK aus Ihrem HTML-Code heraus aufzurufen. Weitere Details finden Sie in unseren [Best Practices]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

Das folgende Beispiel zeigt eine paginierte HTML Full In-App Nachricht:

![HTML-In-App-Nachricht mit einem Inhaltskarussell und interaktiven Buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Beachten Sie, dass die Anzeige von angepassten In-App-Nachrichten im HTML-Format in einem iFrame unter iOS und Android derzeit nicht unterstützt wird.

{% endtab %}
{% tab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) In-App-Nachrichten enthalten keine UI-Komponente und werden in erster Linie zu Analytics-Zwecken verwendet. Dieser Typ wird verwendet, um den Empfang einer In-App-Nachricht zu überprüfen, die an eine Kontrollgruppe gesendet wurde.

Weitere Einzelheiten über die Intelligente Auswahl und Kontrollgruppen finden Sie unter [Intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% endtab %}
{% endtabs %}


{% alert important %}
Die standardmäßige SDK-Integration umfasst Schritte zur Aktivierung von In-App-Nachrichten, einschließlich GIF-Unterstützung. Weitere Einzelheiten zur GIF-Unterstützung finden Sie in dieser [Anleitung](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support).
{% endalert %}


