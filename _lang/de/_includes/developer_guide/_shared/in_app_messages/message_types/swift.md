{% tab schnell %}
Jede Art von In-App-Nachricht ist in Bezug auf Inhalt, Bilder, Symbole, Klickaktionen, Analytics, Anzeige und Zustellung in hohem Maße anpassbar. Sie sind aufgezählte Typen von `Braze.InAppMessage`, die das grundlegende Verhalten und die Eigenschaften aller In-App-Nachrichten definieren. Eine vollständige Liste der Eigenschaften von In-App-Nachrichten und deren Verwendung finden Sie in der [Klasse`InAppMessage` ](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage).

Dies sind die verfügbaren In-App-Nachrichtentypen in Braze und wie sie für Endnutzer:in aussehen werden.

{% subtabs %}
{% subtab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) In-App-Nachrichten heißen so, weil sie vom oberen oder unteren Bildschirmrand aus "nach oben" oder "nach unten" rutschen. Sie bedecken nur einen kleinen Teil des Bildschirms und bieten eine effektive und unaufdringliche Möglichkeit zur Nachrichtenübermittlung.

![Eine Slideup-In-App-Nachricht am unteren und oberen Rand eines Handy-Displays.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endsubtab %}
{% subtab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Feld eingerahmt. Für kritische Nachrichten können sie mit bis zu zwei Analytics-fähigen Buttons ausgestattet werden.

![Eine Modal-In-App-Nachricht in der Mitte des Handydisplays. ]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Modal Image %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Feld eingerahmt. Diese Nachrichten ähneln dem Typ `Modal`, jedoch ohne Kopfzeile oder Nachrichtentext. Für kritische Nachrichten können sie mit bis zu zwei Analytics-fähigen Buttons ausgestattet werden.

![Eine Modal-Bild-In-App-Nachricht in der Mitte des Handydisplays ]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Fullscreen %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct)-In-App-Nachrichten sind nützlich, um den Inhalt und die Wirkung Ihrer Nutzer-Kommunikation zu maximieren. Die obere Hälfte einer In-App-Nachricht des Typs `Full` enthält ein Bild. Die untere Hälfte enthält Text und bis zu zwei Analytics-fähige Buttons.

![Eine Fullscreen-In-App-Nachricht, die auf dem gesamten Handydisplay angezeigt wird.]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Full Screen Image %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct)-In-App-Nachrichten sind ähnlich wie `Full` In-App-Nachrichten, jedoch ohne Kopfzeile oder Nachrichtentext. Dieser Nachrichtentyp ist nützlich, um den Inhalt und die Wirkung Ihrer Nutzer-Kommunikation zu maximieren. Eine `Full Image`-In-App-Nachricht enthält ein Bild, das sich über den gesamten Bildschirm erstreckt, mit der Option, bis zu zwei Analytics-aktivierte Buttons anzuzeigen.

![Eine Fullscreen-Bild-In-App-Nachricht, die auf dem gesamten Handydisplay angezeigt wird.]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Custom HTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct)-In-App-Nachrichten sind nützlich, um vollständig angepasste Nutzerhalte zu erstellen. Der gesamte Inhalt von benutzerdefinierten HTML-Full-In-App-Nachrichten wird in `WKWebView`angezeigt und kann optional anderen Rich Content wie Bilder und Schriftarten enthalten. So haben Sie die volle Kontrolle über das Aussehen und die Funktionalität der Nachrichten. <br><br>iOS In-App-Nachrichten unterstützen eine JavaScript `brazeBridge` Schnittstelle, um Methoden des Braze Web SDK aus Ihrem HTML-Code heraus aufzurufen. Weitere Details finden Sie in unseren [Best Practices]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/).

Das folgende Beispiel zeigt eine paginierte HTML Full In-App Nachricht:

![HTML-In-App-Nachricht mit einem Inhaltskarussell und interaktiven Buttons.]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

Beachten Sie, dass die Anzeige von angepassten In-App-Nachrichten im HTML-Format in einem iFrame unter iOS und Android derzeit nicht unterstützt wird.

{% endsubtab %}
{% subtab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) In-App-Nachrichten enthalten keine UI-Komponente und werden in erster Linie zu Analytics-Zwecken verwendet. Dieser Typ wird verwendet, um den Empfang einer In-App-Nachricht zu überprüfen, die an eine Kontrollgruppe gesendet wurde.

Weitere Einzelheiten über die Intelligente Auswahl und Kontrollgruppen finden Sie unter [Intelligente Auswahl]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/).

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
