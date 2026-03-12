
{% tab android %}
Braze bietet mehrere standardmäßige In-App-Nachrichtentypen, die jeweils mit Nachrichten, Bildern, [Font Awesome](https://fontawesome.com/icons?d=gallery&p=2)-Symbolen, Klickaktionen, Analytics, Farbschemata und mehr angepasst werden können.

Ihr grundlegendes Verhalten und ihre Eigenschaften werden durch die[`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html)Schnittstelle in einer Unterklasse namens definiert[`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html). `IInAppMessage`Enthält auch eine Unterschnittstelle,[`IInAppMessageImmersive`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-immersive/index.html) mit der Sie [Buttons](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-message-button/index.html) zum Schließen, für Klicks und für Analytics zu Ihrer App hinzufügen können.

{% alert important %}
Bitte beachten Sie, dass In-App-Nachrichten, die Buttons enthalten, die`clickAction`Nachricht in die endgültige Nutzlast aufnehmen, wenn der Klick vor dem Hinzufügen des Button-Textes hinzugefügt wird.
{% endalert %}

{% subtabs local %}
{% subtab Slideup %}
[`slideup`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html) In-App-Nachrichten werden so genannt, weil sie vom oberen oder unteren Bildschirmrand nach oben oder unten gleiten. Sie bedecken nur einen kleinen Teil des Bildschirms und bieten eine effektive und unaufdringliche Möglichkeit zur Nachrichtenübermittlung.

Das In-App-Nachricht-Objekt `slideup` erweitert [`InAppMessageBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-base/index.html).

![Eine In-App-Nachricht, die vom unteren Rand des Telefondisplays herabgleitet, zeigt an: "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird dieselbe In-App-Nachricht angezeigt, die auch in der unteren rechten Ecke einer Webseite zu sehen ist.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Modal %}
[`modal`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html) In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Feld eingerahmt. Für kritischere Nachrichten können sie mit zwei Click-Action- und Analytics-fähigen Buttons ausgestattet werden.

Dieser Nachrichtentyp ist eine Unterklasse von [`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html), einer abstrakten Klasse, die implementiert `IInAppMessageImmersive`und Ihnen die Möglichkeit bietet, Ihre lokal generierten In-App-Nachrichten mit benutzerdefinierten Funktionen anzupassen.

![Eine Modal-In-App-Nachricht in der Mitte des Telefondisplays mit dem Text "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird dieselbe In-App-Nachricht in der Mitte einer Webseite angezeigt.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

{% endsubtab %}
{% subtab Full Screen %}
[`full`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html)-In-App-Nachrichten sind nützlich, um den Inhalt und die Wirkung Ihrer Nutzer-Kommunikation zu maximieren. Die obere Hälfte einer In-App-Nachricht von `full` enthält ein Bild, die untere Hälfte Text und bis zu zwei Click-Action- und Analytics-fähigen Buttons.

Dieser Nachrichtentyp erweitert die Möglichkeiten[`InAppMessageImmersiveBase`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-immersive-base/index.html), sodass Sie Ihren lokal generierten In-App-Nachrichten benutzerdefinierte Funktionen hinzufügen können.

![Eine In-App-Nachricht im Vollbildmodus, die über den gesamten Bildschirm des Telefons angezeigt wird und lautet: "Menschen sind kompliziert. Custom Engagement sollte nicht sein." Im Hintergrund wird dieselbe In-App-Nachricht angezeigt, die groß in der Mitte einer Webseite dargestellt ist.]({% image_buster /assets/img_archive/In-App_Full.png %})

{% endsubtab %}
{% subtab Custom HTML %}
[`HTML`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html/index.html)-In-App-Nachrichten sind nützlich, um vollständig angepasste Nutzerhalte zu erstellen. Benutzerdefinierte HTML-In-App-Nachrichten werden in `WebView` angezeigt und können optional andere Rich-Content-Inhalte wie Bilder und Schriftarten enthalten, sodass Sie die volle Kontrolle über das Aussehen und die Funktionalität der Nachrichten haben.

Dieser Nachrichtentyp implementiert [`IInAppMessageHtml`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message-html/index.html), eine Unterklasse von [`IInAppMessage`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-i-in-app-message/index.html).

{% alert note %}
Unter Android werden Links, die mit`target="_blank"`  in benutzerdefinierten HTML-In-App-Nachrichten konfiguriert sind, im Standard-Webbrowser des Geräts geöffnet.
{% endalert %}

Android-In-App-Nachrichten unterstützen eine `brazeBridge`JavaScript-Schnittstelle, um Methoden des Braze Android SDK aus Ihrem HTML heraus aufzurufen. Weitere Informationen finden Sie auf unserer <a href="{{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages#javascript-bridge/">JavaScript-Bridge</a>-Seite.

![Eine HTML-In-App-Nachricht mit einer Karussellansicht von Inhalten und interaktiven Buttons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

{% alert important %}
Die Anzeige angepasster In-App-Nachrichten im HTML-Format in einem iFrame wird derzeit auf den Plattformen iOS und Android nicht unterstützt.
{% endalert %} 

{% endsubtab %}
{% endsubtabs %}

{% alert tip %}
Sie können auch benutzerdefinierte In-App-Nachrichtenansichten für Ihre App festlegen. Eine vollständige Anleitung finden Sie unter [„Benutzerdefinierte Fabriken anpassen]({{site.baseurl}}/developer_guide/in_app_messages/customization#android_setting-custom-factories)“.
{% endalert %}
{% endtab %}