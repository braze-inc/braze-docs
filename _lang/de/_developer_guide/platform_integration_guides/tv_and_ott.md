---
nav_title: TV- und OTT-Integrationen
article_title: TV- und OTT-Integrationen
page_order: 15

description: "In diesem Artikel erfahren Sie mehr über die Features von Braze TV und OTT, Integrationen, verfügbare Plattformen und andere Möglichkeiten."
platform:
  - tvOS
  - Roku
  - Web
  - Android
  - FireOS
---

# TV- und OTT-Integrationen

> So wie sich die Technologie mit neuen Plattformen und Geräten weiterentwickelt, geschieht das auch mit Ihrem Messaging mit Braze. Braze bietet verschiedene Engagement-Kanäle für eine Reihe von verschiedenen TV-Betriebssystemen und "OTT"-Set-Top-Boxen.

## Plattformen und Features

Im Folgenden finden Sie eine Liste der Features und Messaging-Kanäle, die heute unterstützt werden.

<style>
#tv-feature-table td,
#tv-feature-table th {
    text-align: center !important;
    vertical-align: center;
}

</style>
<table id="tv-feature-table">
    <thead>
        <tr>
            <th>Gerätetyp</th>
            <th>DATEN UND ANALYSEN</th>
            <th>In-App-Nachrichten</th>
            <th>Content-Cards</th>
            <th>Push-Benachrichtigungen</th>
            <th>Canvas</th>
            <th>Feature-Flags</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Amazon Fire TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Kindle Fire</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Android TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fas fa-check text-success"></i></td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>LG TV (webOS)</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">--</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Samsung Tizen TV</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push">--</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Roku</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
            <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-times text-warning"></i></td>
            <td for="push">--</td>
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
        <tr>
            <td>Apple TV OS</td>
            <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
             <td for="iam"><i class="fas fa-check text-success"></i></td>
            <td for="content-cards"><i class="fas fa-check text-success"></i></td>
            <td for="push"><i class="fa-solid fa-minus"></i></td>  
            <td for="canvas"><i class="fas fa-check text-success"></i></td>
            <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
        </tr>
       <tr>
          <td>Apple Vision Pro</td>
          <td for="data-analytics"><i class="fas fa-check text-success"></i></td>
           <td for="iam"><i class="fas fa-check text-success"></i></td>
          <td for="content-cards"><i class="fas fa-check text-success"></i></td>
          <td for="push"><i class="fa-solid fa-minus"></i></td>  
          <td for="canvas"><i class="fas fa-check text-success"></i></td>
          <td for="feature-flags"><i class="fas fa-check text-success"></i></td>
      </tr>
    </tbody>
</table>

- <i class="fas fa-check text-success"></i> = Unterstützt
- <i class="fa-solid fa-minus"></i> = Teilweise Unterstützung
- <i class="fas fa-times text-warning"></i> = Nicht von Braze unterstützt
- N/A = Nicht von der OTT-Plattform unterstützt

## Integrationsleitfäden

### Amazon Fire TV {#fire-tv}

Verwenden Sie das Braze Fire OS SDK zur Integration mit Amazon Fire TV Geräten.

Zu den Features zählen:

- Datenerfassung und Analytics für kanalübergreifendes Engagement
- Push-Benachrichtigungen (bekannt als ["Heads Up Notifications")](https://developer.amazon.com/docs/fire-tv/notifications.html#headsup)
  - Die Priorität muss auf "HOCH" gestellt sein, damit diese angezeigt werden. Alle Benachrichtigungen erscheinen im Fire TV-Einstellungsmenü.
- Content-Cards
- Feature-Flags
- In-App-Nachrichten
  - Um HTML-Nachrichten auf Nicht-Touch-Geräten wie TV-Geräte anzuzeigen, setzen Sie `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` auf `false` (verfügbar ab [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))

Weitere Informationen finden Sie in der [Anleitung zur Integration von Fire OS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).

### Kindle Fire {#kindle-fire}

Verwenden Sie das Braze Fire OS SDK für die Integration mit Amazon Kindle Fire Geräten.

Zu den Features zählen:

- Datenerfassung und Analytics für kanalübergreifendes Engagement
- Push-Benachrichtigungen
- Content-Cards
- Feature-Flags
- In-App-Nachrichten

Weitere Informationen finden Sie in der [Anleitung zur Integration von Fire OS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).

### Android TV {#android-tv}

Verwenden Sie das Braze Android SDK zur Integration mit Android-TV-Geräten.

Zu den Features zählen:

- Datenerfassung und Analytics für kanalübergreifendes Engagement
- Content-Cards
- Feature-Flags
- In-App-Nachrichten 
  - Um HTML-Nachrichten auf Nicht-Touch-Geräten wie TV-Geräte anzuzeigen, setzen Sie `com.braze.configuration.BrazeConfig.Builder.setIsTouchModeRequiredForHtmlInAppMessages` auf `false` (verfügbar ab [Android SDK v23.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#2310))
- \* Push-Benachrichtigungen (manuelle Integration erforderlich)
  - Push-Benachrichtigungen werden auf Android TV nicht nativ unterstützt. Warum, erfahren Sie in den [Design-Richtlinien](https://designguidelines.withgoogle.com/android-tv/patterns/notifications.html) von Google. Sie können jedoch **eine manuelle Integration der Push-Benachrichtigung UI vornehmen, um dies zu erreichen**. Lesen Sie in unserer [Dokumentation]({{site.baseurl}}/developer_guide/platform_integration_guides/android/push_notifications/android/android_tv_push/) nach, wie Sie dies einrichten können.

Weitere Informationen finden Sie in der [Anleitung zur Android SDK-Integration]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/android_sdk_integration/).

{% alert note %}
Stellen Sie sicher, dass Sie im Dashboard eine neue Android-App für Ihre Android-OTT-Integration erstellen.
{% endalert %}

### LG webOS {#lg-webos}

Nutzen Sie das Braze Web SDK für die Integration mit [LG webOS TVs](https://webostv.developer.lge.com/discover).

Zu den Features zählen:

- Datenerfassung und Analytics für kanalübergreifendes Engagement
- Content-Cards (über [Headless UI](#custom-ui))
- Feature-Flags
- In-App-Nachrichten (über [Headless UI](#custom-ui))

Weitere Informationen finden Sie in der [Anleitung zur Integration von Internet Smart-TV]({{site.baseurl}}/developer_guide/platform_integration_guides/web/smart_tvs/).

### Samsung Tizen {#tizen}

Verwenden Sie das Braze Web SDK zur Integration mit [Samsung Tizen-TV-Geräten](https://developer.samsung.com/smarttv/develop/specifications/tv-model-groups.html).

Zu den Features zählen:

- Datenerfassung und Analytics für kanalübergreifendes Engagement
- Content-Cards (über [Headless UI](#custom-ui))
- Feature-Flags
- In-App-Nachrichten (über [Headless UI](#custom-ui))

Weitere Informationen finden Sie in der [Anleitung zur Integration von Internet Smart-TV]({{site.baseurl}}/developer_guide/platform_integration_guides/web/smart_tvs/).

### Roku {#roku}

Verwenden Sie das Braze Roku SDK zur Integration mit [Roku-Fernsehern](https://developer.roku.com/docs/developer-program/getting-started/roku-dev-prog.md).

Zu den Features zählen:

- Datenerfassung und Analytics für kanalübergreifendes Engagement
- In-App-Nachrichten (über [Headless UI](#custom-ui))
  - Webviews werden von der Roku-Plattform nicht unterstützt. In-App-Nachrichten im HTML-Format werden daher nicht unterstützt.
- Feature-Flags

Weitere Informationen finden Sie in der [Anleitung zur Integration von Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/in-app_messaging/overview/).

### Apple TV OS {#tvos}

Verwenden Sie das Braze Swift SDK für die Integration mit tvOS. Denken Sie daran, dass das Swift SDK keine standardmäßige UI oder Ansichten für tvOS enthält, sodass Sie eigene implementieren müssen.

Zu den Features zählen:

- Datenerfassung und Analytics für kanalübergreifendes Engagement
- Content-Cards (über [Headless UI](#custom-ui))
- Feature-Flags
- In-App-Nachrichten (über [Headless UI](#custom-ui))
  - Webviews werden von der tvOS-Plattform nicht unterstützt. In-App-Nachrichten im HTML-Format werden daher nicht unterstützt.
  - Sehen Sie sich unsere [Beispiel-App](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui) an, um mehr darüber zu erfahren, wie Sie eine Headless UI für angepasstes Messaging unter tvOS verwenden können.
- Stille Push-Benachrichtigungen und Update-Badges

Weitere Informationen finden Sie in der [Anleitung zur iOS Swift SDK-Integration](https://github.com/braze-inc/braze-swift-sdk).

{% alert note %}
Um zu vermeiden, dass In-App-Nachrichten für Ihre Nutzer im Fernsehen angezeigt werden, sollten Sie entweder [App Targeting](#app-targeting) einrichten oder Schlüssel-Wert-Paare verwenden, um Nachrichten herauszufiltern. Zum Beispiel, dass tvOS-Nachrichten nur dann angezeigt werden, wenn sie das spezielle Schlüssel-Wert-Paar `tv = true` enthalten.
{% endalert %}

### Apple Vision Pro {#vision-pro}

Verwenden Sie das Braze Swift SDK für die Integration mit visionOS. Die meisten Features, die unter iOS verfügbar sind, stehen auch unter visionOS zur Verfügung, darunter:

- Analytics (Sitzungen, angepasste Events, Käufe, etc.)
- In-App Messaging (Datenmodelle und UI)
- Content-Cards (Datenmodelle und UI)
- Push-Benachrichtigungen (für Nutzer:innen sichtbar mit Aktions-Buttons und stillen Benachrichtigungen)
- Feature-Flags
- Standort-Analytics

Weitere Informationen finden Sie in der [Anleitung zur iOS Swift SDK-Integration](https://github.com/braze-inc/braze-swift-sdk).

{% alert important %}
Einige iOS Features werden nur teilweise oder gar nicht unterstützt. Die vollständige Liste finden Sie unter [visionOS-Unterstützung](https://www.braze.com/docs/developer_guide/platform_integration_guides/swift/visionos).
{% endalert %}

## App-Targeting {#app-targeting}

Für das Targeting von OTT-Apps für Messaging empfehlen wir die Erstellung eines Segments speziell für Ihre OTT-App.

![Ein Segment, das mit der Android-OTT-App erstellt wurde.]({% image_buster /assets/img/android_ott.png %})

## Headless UI {#custom-ui}

{% alert important %}
Plattformen, die In-App-Nachrichten oder Content-Cards über Headless UI unterstützen , enthalten **keine** standardmäßige UI oder Ansichten. Implementieren Sie also unbedingt Ihre eigene angepasste UI.
{% endalert %}

Mit Headless UI stellt Braze ein Datenmodell (z.B. JSON) bereit, das Ihre App lesen und innerhalb eines UI verwenden kann, das Ihre App steuert. Diese Daten enthalten die im Dashboard konfigurierten Felder (Titel, Textkörper, Button-Text, Farben usw.), die Ihre App lesen und entsprechend anzeigen kann. Weitere Informationen zum angepassten Messaging-Handling finden Sie unter:

**Android SDK**
- [In-App-Nachricht anpassen](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/in-app_messaging/customization/custom_listeners/)
- [Content-Cards-Anpassung](https://www.braze.com/docs/developer_guide/platform_integration_guides/android/content_cards/implementation_guide/)

**Swift SDK**
- [In-App-Nachricht anpassen](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/brazeinappmessagepresenter/)
- [Beispiel-App für Headless UI](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)
- [Content-Cards-Anpassung](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/contentcards-swift.class/)

**Web SDK**
- [In-App-Nachricht anpassen](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/in-app_messaging/customization/key_value_pairs)
- [Content-Cards-Anpassung](https://www.braze.com/docs/developer_guide/platform_integration_guides/web/content_cards/customization/custom_ui/)

