
{% tab android %}
Braze bietet mehrere Standard In-App-Nachrichtentypen, die jeweils mit Nachrichten, Bildern, [Font Awesome-Symbolen](https://fontawesome.com/icons?d=gallery&p=2), Klick-Aktionen, Analytics, Farbschemata und mehr angepasst werden können.

Ihr grundlegendes Verhalten und ihre Eigenschaften werden durch die [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html) Schnittstelle, in einer Unterklasse namens [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html). `IInAppMessage` enthält auch eine Unterschnittstelle, [`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html)mit der Sie Ihrer App [Buttons](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) zum Schließen, zum Klicken und für Analytics hinzufügen können.

{% alert important %}
Denken Sie daran, dass In-App-Nachrichten, die Buttons enthalten, die Nachricht `clickAction` in der endgültigen Nutzlast enthalten, wenn die Klick-Aktion vor dem Hinzufügen des Button-Textes hinzugefügt wurde.
{% endalert %}

{% subtabs local %}
{% subtab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) In-App-Nachrichten werden so genannt, weil sie vom oberen oder unteren Bildschirmrand nach oben oder unten gleiten. Sie bedecken nur einen kleinen Teil des Bildschirms und bieten eine effektive und unaufdringliche Möglichkeit zur Nachrichtenübermittlung.

Das In-App-Nachricht-Objekt `slideup` erweitert [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).

![Eine In-App-Nachricht, die vom unteren Rand des Telefondisplays herabgleitet, zeigt an: "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird die gleiche In-App-Nachricht in der unteren rechten Ecke einer Internetseite angezeigt.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Modal %}
[`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Feld eingerahmt. Für kritischere Nachrichten können sie mit zwei Click-Action- und Analytics-fähigen Buttons ausgestattet werden.

Dieser Nachrichtentyp ist eine Unterklasse von [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html), einer abstrakten Klasse, die `IInAppMessageImmersive` implementiert. Damit haben Sie die Möglichkeit, Ihre lokal generierten In-App-Nachrichten um angepasste Funktionen zu erweitern.

![Eine Modal-In-App-Nachricht in der Mitte des Telefondisplays mit dem Text "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird die gleiche In-App-Nachricht in der Mitte einer Webseite angezeigt.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html)-In-App-Nachrichten sind nützlich, um den Inhalt und die Wirkung Ihrer Nutzer-Kommunikation zu maximieren. Die obere Hälfte einer In-App-Nachricht von `full` enthält ein Bild, die untere Hälfte Text und bis zu zwei Click-Action- und Analytics-fähigen Buttons.

Dieser Nachrichtentyp erweitert [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html)und bietet Ihnen die Möglichkeit, Ihre lokal generierten In-App-Nachrichten um angepasste Funktionen zu erweitern.

![Eine In-App-Nachricht im Vollbildmodus, die über den gesamten Bildschirm des Telefons angezeigt wird und lautet: "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird dieselbe In-App-Nachricht weitgehend in der Mitte einer Internetseite angezeigt.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endsubtab %}
{% subtab Custom HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)-In-App-Nachrichten sind nützlich, um vollständig angepasste Nutzerhalte zu erstellen. Benutzerdefinierte HTML-In-App-Nachrichten werden in `WebView` angezeigt und können optional andere Rich-Content-Inhalte wie Bilder und Schriftarten enthalten, sodass Sie die volle Kontrolle über das Aussehen und die Funktionalität der Nachrichten haben.

Dieser Nachrichtentyp implementiert [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html), die eine Unterklasse von [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html).

In-App-Nachrichten für Android unterstützen eine JavaScript `brazeBridge` Schnittstelle, um Methoden des Braze Android SDK aus Ihrem HTML-Code heraus aufzurufen. Weitere Informationen finden Sie auf unserer <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge/">JavaScript-Bridge-Seite</a>.

![Eine HTML-In-App-Nachricht mit einem Karussell von Inhalten und interaktiven Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Die Anzeige angepasster In-App-Nachrichten im HTML-Format in einem iFrame wird derzeit auf den Plattformen iOS und Android nicht unterstützt.
{% endalert %} 

{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Sie können auch angepasste In-App-Nachricht-Ansichten für Ihre App definieren. Eine vollständige Anleitung finden Sie unter [Anpassen von Fabriken]({{site.baseurl}}/developer_guide/in_app_messages/customization#android_setting-custom-factories).
{% endalert %}
{% endtab %}