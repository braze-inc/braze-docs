---
nav_title: Integration
article_title: Integration von In-App-Nachrichten für das Web
platform: Web
channel: in-app messages
page_order: 0
page_type: reference
description: "Dieser Artikel enthält Ressourcen zu In-App-Nachrichtentypen sowie zum Verhalten von Nachrichten für Ihre Web-Anwendung."
search_rank: 2
---

# Integration von In-App-Nachrichten

> Dieser Artikel beschreibt, wie Sie eine In-App-Nachricht für die Web-Anwendung einrichten.

Mit [In-App-Nachrichten]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) können Sie Ihren Nutzern Inhalte zukommen lassen, ohne sie mit einer Push-Benachrichtigung zu unterbrechen. Angepasste und maßgeschneiderte In-App-Nachrichten verbessern das Nutzererlebnis und helfen Ihrer Zielgruppe, den größten Nutzen aus Ihrer App zu ziehen. Mit den verschiedenen Layouts und Anpassungswerkzeugen, die Ihnen zur Verfügung stehen, binden In-App-Nachrichten Ihre Nutzer mehr als je zuvor.

In unseren [Fallstudien](https://www.braze.com/customers) finden Sie Beispiele für In-App-Nachrichten.

## Arten von In-App-Nachrichten

Braze bietet derzeit die folgenden standardmäßigen In-App-Nachrichtenarten: 

- `Slideup`
- `Modal`
- `Full`
- `HTML`

Jede Art von In-App-Nachricht ist in Bezug auf Inhalt, Bilder, Symbole, Klickaktionen, Analytics, Anzeige und Zustellung anpassbar.

Alle In-App-Nachrichten übernehmen ihren Prototyp aus [`InAppMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.inappmessage.html), wo das grundlegende Verhalten und die Merkmale für alle In-App-Nachrichten definiert ist. Die prototypischen Unterklassen sind [`SlideUpMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html), [`ModalMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html), [`FullScreenMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html), und [`HtmlMessage`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html).

## Erwartete Verhaltensweisen nach Nachrichtentyp

So sieht es aus, wenn Ihre Nutzer eine unserer standardmäßigen In-App-Nachrichten öffnen.

{% tabs %}
{% tab Slideup %}

[`SlideUp`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.slideupmessage.html) In-App-Nachrichten werden so genannt, weil sie traditionell auf mobilen Plattformen vom oberen oder unteren Bildschirmrand nach oben oder unten gleiten. Im Braze Web SDK werden diese Nachrichten eher im Stil einer Growl- oder Toast-Benachrichtigung angezeigt, um dem vorherrschenden Paradigma des Internets gerecht zu werden. Sie bedecken nur einen kleinen Teil des Bildschirms und bieten eine effektive und unaufdringliche Möglichkeit zur Nachrichtenübermittlung.

![In-App-Nachricht, die vom unteren Rand eines Smartphone-Displays eingeblendet wird, mit dem Text "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird die gleiche In-App-Nachricht in der unteren Ecke einer Webseite angezeigt.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Modal %}

[`Modal`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.modalmessage.html) In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Feld eingerahmt. Sie können mit bis zu zwei Schaltflächen für Klick-Aktionen und Analysen ausgestattet werden und sind damit für kritische Mitteilungen geeignet.

![Modale In-App-Nachricht in der Mitte eines Smartphone-Displays mit dem Text "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird die gleiche In-App-Nachricht in der Mitte einer Webseite angezeigt.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Vollbild %}

In-App-Nachrichten des Typs [`Full`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.fullscreenmessage.html) sind nützlich, um den Inhalt und die Wirkung Ihrer Nutzerkommunikation zu maximieren. Bei schmalen Browserfenstern (z. B. auf Mobilgeräten) nehmen In-App-Nachrichten des Typs `full` das gesamte Browserfenster ein. In größeren Browserfenstern erscheinen die In-App-Nachrichten von `full` ähnlich wie die In-App-Nachrichten von `modal`. Die obere Hälfte einer In-App-Nachricht des Typs `full` enthält ein Bild. Die untere Hälfte kann bis zu acht Zeilen Text sowie und bis zu zwei durch Klickaktionen und Analytics-aktivierte Buttons enthalten.

![In-App-Nachricht im Vollbildmodus, die über das gesamte Display eines Smartphones angezeigt wird, mit dem Text "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird dieselbe In-App-Nachricht weitgehend in der Mitte einer Webseite angezeigt.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% endtab %}
{% tab Benutzerdefiniertes HTML %}

[`HTML`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.htmlmessage.html) In-App-Nachrichten sind nützlich, um vollständig angepasste Nutzerinhalte zu erstellen. Angepasster HTML-Code wird in einem iFrame angezeigt und kann Rich Content wie Bilder, Schriftarten, Videos und interaktive Elemente enthalten, die eine vollständige Kontrolle über das Aussehen und die Funktionalität der Nachrichten ermöglichen. Diese unterstützen eine JavaScript `brazeBridge` Schnittstelle, um Methoden des Braze Web SDK von Ihrem HTML-Code aus aufzurufen. Weitere Einzelheiten finden Sie in unseren [Best Practices]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

{% alert important %}

Um In-App-Nachrichten im HTML-Format über das Web SDK zu aktivieren, **müssen** Sie Braze die Initialisierungsoption `allowUserSuppliedJavascript` zur Verfügung stellen, zum Beispiel `braze.initialize('YOUR-API_KEY', {allowUserSuppliedJavascript: true})`. Dies geschieht aus Sicherheitsgründen. In-App-Nachrichten im HTML-Format können JavaScript ausführen. Daher ist ein Website-Administrator erforderlich, um sie zu aktivieren.

{% endalert %}

Das folgende Beispiel zeigt eine paginierte HTML-In-App-Nachricht:

![In-App-Nachricht im HTML-Format mit einem Inhaltskarussell und interaktiven Buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

{% endtab %}
{% endtabs %}

## Integration

Die Anzeige von In-App-Nachrichten erfolgt standardmäßig automatisch als Teil unserer empfohlenen [Integrationsanweisungen]({{ site.baseurl }}/developer_guide/platform_integration_guides/web/initial_sdk_setup/). Weitere Anpassungen können mithilfe der Schritte in diesem Leitfaden vorgenommen werden.

