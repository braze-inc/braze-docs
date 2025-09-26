### Slideup In-App Nachrichten

[`Slideup`]{% if include.platform == "iOS" %}[in_app_message_1]{% elsif include.platform == "Android" %}[in_app_message_2]{% endif %} In-App-Nachrichten werden so genannt, weil sie vom oberen oder unteren Bildschirmrand nach oben oder nach unten rutschen.  Sie bedecken nur einen kleinen Teil des Bildschirms und bieten eine effektive und unaufdringliche Möglichkeit zur Nachrichtenübermittlung.

![Slideup Beispiel]({% image_buster /assets/img_archive/In-App_Slideup.png %})

### Modale In-App-Nachrichten

[`Modal`]{% if include.platform == "iOS" %}[in_app_message_3]{% elsif include.platform == "Android" %}[in_app_message_4]{% endif %} In-App-Nachrichten erscheinen in der Mitte des Bildschirms und werden von einem durchsichtigen Panel eingerahmt. Sie können mit bis zu zwei Schaltflächen mit Klickfunktion und Analysefunktion ausgestattet werden und sind für kritische Nachrichten nützlich.

![Modal Beispiel]({% image_buster /assets/img_archive/In-App_Modal.png %})

### Vollständige In-App-Nachrichten

[`Full`]{% if include.platform == "iOS" %}[in_app_message_5]{% elsif include.platform == "Android" %}[in_app_message_6]{% endif %} In-App-Nachrichten sind nützlich, um den Inhalt und die Wirkung Ihrer Benutzerkommunikation zu maximieren.  Die obere Hälfte einer `full` In-App-Nachricht enthält ein Bild und die untere Hälfte zeigt Text sowie bis zu zwei Buttons für Klick-Aktionen und Analytics an.

![Vollständiges Beispiel]({% image_buster /assets/img_archive/In-App_Full.png %})

### Vollständige HTML In-App Nachrichten

[`HTML Full`]{% if include.platform == "iOS" %}[in_app_message_7]{% elsif include.platform == "Android" %}[in_app_message_8]{% endif %} In-App-Nachrichten sind nützlich, um vollständig angepasste Benutzerinhalte zu erstellen. Benutzerdefiniertes HTML Der gesamte Inhalt der In-App-Nachrichten wird auf {% if include.platform == "iOS" %}`WKWebView`{% elsif include.platform == "Android" %}`WebView`{% endif %} angezeigt und kann optional weitere Inhalte wie Bilder und Schriftarten enthalten, so dass Sie das Aussehen und die Funktionalität der Nachrichten vollständig steuern können.

 {% if include.platform == "iOS" %}
Das folgende Beispiel zeigt eine paginierte HTML Full In-App Nachricht:

![HTML5 Beispiel]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

 {% elsif include.platform == "Android" %}Das folgende Beispiel zeigt eine Umfrage in Form einer vollständigen In-App-Nachricht im HTML-Format, die von SoundCloud erstellt wurde.

![HTML5 Beispiel]({% image_buster /assets/img_archive/HTML5.gif %})
{% endif %}

Der gesamte Inhalt der In-App-Nachrichten wird in einer WKWebView angezeigt und kann optional andere Rich Content-Inhalte wie Bilder und Schriftarten enthalten. So haben Sie die volle Kontrolle über das Aussehen und die Funktionalität der Nachrichten. **Bitte beachten Sie, dass wir derzeit die Anzeige von angepassten HTML-In-App-Nachrichten in einem iFrame auf den Plattformen iOS und Android nicht unterstützen.**

## Zustellung von In-App-Nachrichten

### In-App-Nachrichten (ausgelöst)

Die folgende Dokumentation bezieht sich auf das Produkt Braze `In-App Messaging`, auch bekannt als "getriggerte In-App-Nachrichten", die wie unten in der Dropdown-Liste "Kampagne erstellen" hervorgehoben sind:

![In-App Messaging Composer]({% image_buster /assets/img_archive/trigger-iam-composer.png %})

Sie können auch auf die Dokumentation für unser veraltetes [`Original In-App Messaging`]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/create/#original-in-app-messages) Produkt referenzieren.

#### Auslöser-Typen

Mit unserem Produkt für In-App-Nachrichten können Sie die Anzeige von In-App-Nachrichten als Folge verschiedener Ereignistypen auslösen: `Any Purchase`, `Specific Purchase`, `Session Start`, `Custom Event`, `Push Click`.  Außerdem können `Specific Purchase`- und `Custom Event`\- Trigger robuste Eigenschaftsfilter enthalten.

{% alert note %}
Ausgelöste In-App-Nachrichten funktionieren nur bei angepassten Events, die über das Braze SDK protokolliert werden. In-App-Nachrichten können nicht über die API oder durch API-Event (wie Kauf-Events) getriggert werden. Wenn Sie mit Android arbeiten, sehen Sie sich an, wie man [angepasste Events unter Android protokolliert]({{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/#tracking-custom-events). Wenn Sie mit iOS arbeiten, sehen Sie sich an, wie man [angepasste Events unter iOS protokolliert]({{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_custom_events/#tracking-custom-events).
{% endalert %}

#### Semantik der Zustellung

Alle In-App-Nachrichten, für die ein Nutzer berechtigt ist, werden zu Beginn der Sitzung an das Gerät des Nutzers gesendet. Weitere Informationen über die Semantik des Sitzungsstarts im SDK finden Sie in unserer [session lifecycle documentation]{% if include.platform == "iOS" %}[in_app_message_15a]{% elsif include.platform == "Android" %}[in_app_message_15b]{% endif %}. Bei der Zustellung holt das SDK die Assets vorab, so dass sie zum Zeitpunkt des Triggerns sofort verfügbar sind und die Anzeige-Latenzzeit minimiert wird.

Wenn ein Trigger-Event mit mehr als einer in Frage kommenden In-App-Nachricht verbunden ist, wird nur die In-App-Nachricht mit der höchsten Priorität zugestellt.

Bei In-App-Nachrichten, die sofort nach der Zustellung angezeigt werden (z. B. Sitzungsstart, Push-Klick), kann es zu einer gewissen Latenz kommen, da die Assets nicht vorab geholt werden.

#### Mindestzeitintervall zwischen Auslösern

Standardmäßig begrenzen wir die Anzahl der In-App-Nachrichten auf einmal alle 30 Sekunden, um eine hohe Benutzerqualität zu gewährleisten.

{% if include.platform == "iOS" %}Sie können diesen Wert über den Parameter `ABKMinimumTriggerTimeIntervalKey` innerhalb des `appboyOptions` überschreiben, der an `startWithApiKey:inApplication:withLaunchOptions:withAppboyOptions:` übergeben wird. Stellen Sie `ABKMinimumTriggerTimeIntervalKey` auf den ganzzahligen Wert ein, den Sie als Mindestzeit in Sekunden zwischen In-App-Nachrichten angeben möchten:

```objc
// Sets the minimum trigger time interval to 5 seconds
[Appboy startWithApiKey:@"YOUR-API_KEY"
          inApplication:application
      withLaunchOptions:options
      withAppboyOptions:@{ ABKMinimumTriggerTimeIntervalKey : @(5) }];
```

{% elsif include.platform == "Android" %}
Um diesen Wert außer Kraft zu setzen, setzen Sie `com_appboy_trigger_action_minimum_time_interval_seconds` in Ihrem `braze.xml`.

```xml
  <integer name="com_appboy_trigger_action_minimum_time_interval_seconds">5</integer>
```
{% endif %}

[in_app_message_1]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_slideup.html
[in_app_message_2]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-slideup/index.html
[in_app_message_3]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_modal.html
[in_app_message_4]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-modal/index.html
[in_app_message_5]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_full.html
[in_app_message_6]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-full/index.html
[in_app_message_7]: http://appboy.github.io/appboy-ios-sdk/docs/interface_a_b_k_in_app_message_h_t_m_l_full.html
[in_app_message_8]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.models.inappmessage/-in-app-message-html-full/index.html
[in_app_message_15a]: {{ site.baseurl }}/developer_guide/platform_integration_guides/ios/analytics/tracking_sessions/#session-lifecycle
[in_app_message_15b]: {{ site.baseurl }}/developer_guide/platform_integration_guides/android/analytics/tracking_sessions/#session-lifecycle

