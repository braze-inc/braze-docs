---
nav_title: Übersicht
article_title: Übersicht der In-App Nachrichten für iOS
platform: iOS
page_order: 0
description: "Dieser Referenzartikel behandelt die verschiedenen Arten von iOS-In-App-Nachrichten, das erwartete Verhalten und mehrere Anwendungsfälle."
channel:
  - in-app messages
search_rank: 4
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# In-App-Nachrichten

Mit [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) können Sie Inhalte an Ihre Nutzer übermitteln, ohne sie mit einer Push-Benachrichtigung zu unterbrechen. Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größtmöglichen Nutzen aus Ihrer App zu ziehen. Mit einer Vielzahl von Layouts und Anpassungswerkzeugen, aus denen Sie wählen können, binden In-App-Nachrichten Ihre Nutzer mehr als je zuvor.

In unseren [Fallstudien](https://www.braze.com/customers) finden Sie Beispiele für In-App-Nachrichten.

## Arten von In-App-Nachrichten

Braze bietet derzeit die folgenden standardmäßigen In-App-Nachrichtenarten: 

- `Slideup`
- `Modal`
- `Full`
- `HTML Full`

Jede Art von In-App-Nachricht ist in Bezug auf Inhalt, Bilder, Symbole, Klickaktionen, Analytics, Anzeige und Zustellung in hohem Maße anpassbar.

Alle In-App-Nachrichten sind Unterklassen von `ABKInAppMessage`, die das grundlegende Verhalten und die Merkmale für alle In-App-Nachrichten definiert. Es gibt folgende Klassenstrukturen von In-App-Nachrichten:

![Eine Grafik, die zeigt, dass die Klasse ABKInAppMessage die Stammklasse von ABKInAppMessageSlideup, ABKInAppMessageImmersive und ABKInAppMessageHTML ist. ABKInAppMessage enthält anpassbare Eigenschaften wie Nachricht, Extras, Dauer, Klickaktion, URI, Ausblendungsaktion, Symbolausrichtung und Textausrichtung. Das ABKInAppMessageSlideup enthält anpassbare Eigenschaften wie Chevron und Slide-up-Anker. ABKInAppMessageImmersive enthält anpassbare Eigenschaften wie Kopfzeile, Schließen-Schaltfläche, Rahmen und In-App-Nachrichten-Schaltflächen. Mit ABKInAppMessageHTML können Klicks auf Buttons In-App-Nachrichten im HTML-Format manuell protokolliert werden.]({% image_buster /assets/img_archive/ABKInAppMessage-models.png %})

{% alert important %}
In-App-Nachrichten werden standardmäßig nach Abschluss der standardmäßigen SDK-Integration aktiviert, einschließlich der GIF-Unterstützung.
<br><br>
Beachten Sie, dass die Integration von `SDWebImage` erforderlich ist, wenn Sie unsere Braze UI für die Anzeige von Bildern in iOS In-App-Nachrichten oder Content Cards verwenden möchten.
{% endalert %}

### Erwartete Verhaltensweisen nach Nachrichtentypen

So sieht es aus, wenn Ihre Nutzer eine unserer Standardarten von In-App-Nachrichten öffnen.

{% tabs %}
{% tab Slideup %}

[`Slideup`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html) In-App-Nachrichten werden so genannt, weil sie vom oberen oder unteren Bildschirmrand nach oben oder unten gleiten. Sie bedecken nur einen kleinen Teil des Bildschirms und bieten eine effektive und unaufdringliche Möglichkeit zur Nachrichtenübermittlung.

![In-App-Nachricht, die vom unteren Rand eines Smartphone-Displays eingeblendet wird, mit dem Text "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird die gleiche In-App-Nachricht in der unteren Ecke einer Webseite angezeigt.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}


{% endtab %}
{% tab Modal %}

[`Modal`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html) In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Feld eingerahmt. Sie können mit bis zu zwei Schaltflächen für Klick-Aktionen und Analysen ausgestattet werden und sind damit für kritische Mitteilungen geeignet.

![Modale In-App-Nachricht in der Mitte eines Smartphone-Displays mit dem Text "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird die gleiche In-App-Nachricht in der Mitte einer Webseite angezeigt.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Vollbild %}

In-App-Nachrichten des Typs [`Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html) sind nützlich, um den Inhalt und die Wirkung Ihrer Nutzerkommunikation zu maximieren. Die obere Hälfte einer In-App-Nachricht des Typs `full` enthält ein Bild. Die untere Hälfte enthält Text und bis zu zwei durch Klickaktionen und Analytics aktivierte Buttons.

![In-App-Nachricht im Vollbildmodus, die über das gesamte Display eines Smartphones angezeigt wird, mit dem Text "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird dieselbe In-App-Nachricht weitgehend in der Mitte einer Webseite angezeigt.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Benutzerdefiniertes HTML %}

[`HTML Full`](https://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html) In-App-Nachrichten sind nützlich, um vollständig angepasste Nutzerinhalte zu erstellen. Benutzerdefinierter Inhalt einer In-App-Nachricht des Typs "Full" im HTML-Format wird in `WKWebView` angezeigt und kann optional anderen Rich Content wie Bilder und Schriftarten enthalten. So haben Sie die volle Kontrolle über das Aussehen und die Funktionalität der Nachrichten. <br><br>iOS In-App-Nachrichten unterstützen eine JavaScript `brazeBridge` Schnittstelle, um Methoden des Braze Web SDK aus Ihrem HTML-Code heraus aufzurufen. Weitere Details finden Sie in unseren [Best Practices]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

Das folgende Beispiel zeigt eine paginierte HTML Full In-App Nachricht:

![In-App-Nachricht im HTML-Format mit einem Inhaltskarussell und interaktiven Buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Der Inhalt einer In-App-Nachricht des Typs "Full" wird in einer `WKWebView` angezeigt und kann optional anderen Rich Content wie Bilder und Schriftarten enthalten. So haben Sie die volle Kontrolle über das Aussehen und die Funktionalität der Nachrichten. Beachten Sie, dass die Anzeige von angepassten In-App-Nachrichten im HTML-Format in einem iFrame unter iOS und Android derzeit nicht unterstützt wird.

{% alert note %}
Ab iOS SDK Version 3.19.0 sind die folgenden JavaScript-Methoden in In-App-Nachrichten im HTML-Format No-Ops: `alert`, `confirm`, `prompt`.
{% endalert %}

{% endtab %}
{% endtabs %}

