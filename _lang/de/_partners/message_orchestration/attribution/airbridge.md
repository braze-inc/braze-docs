---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Dieser Referenzartikel beschreibt die Partnerschaft zwischen Braze und Airbridge, die personenbezogene Attribution und inkrementelle Messungen anbietet, um die wahre Marketingeffektivität über Geräte, Identitäten und Plattformen hinweg zu messen."
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/) ist eine einheitliche Plattform für mobile Messungen, die Ihnen hilft, die wahren Wachstumsquellen durch mobile Attribution, inkrementelle Messungen und Marketing-Mix-Modellierung zu entdecken.

Mit der Integration von Braze und Airbridge können Sie alle nicht-organischen Installationsdaten von Airbridge an Braze weitergeben, um personalisierte Marketingkampagnen zu erstellen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Airbridge-Konto | Um die Vorteile dieser Partnerschaft zu nutzen, benötigen Sie ein Airbridge-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform sind in Ihrer Anwendung möglicherweise Codeschnipsel erforderlich. |
| Airbridge SDK | Zusätzlich zum erforderlichen Braze SDK müssen Sie das Airbridge [Android](https://help.airbridge.io/en/developers/android-sdk) oder [iOS](https://help.airbridge.io/en/developers/ios-sdk) SDK installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: Geräte-ID zuordnen

Die Server-zu-Server-Integration kann aktiviert werden, indem Sie die folgenden Codeschnipsel in Ihre Anwendungen einfügen.

#### Android

Wenn Sie eine Android-App haben, müssen Sie eine eindeutige Braze-Geräte-ID an Airbridge übergeben.

{% tabs %}
{% tab Android %}
{% subtabs %}
{% subtab Java %}

```java
// MainApplciation.java
@Override
public void onCreate() {
    super.onCreate();
    // Initialize Airbridge SDK
    AirbridgeConfig config = new AirbridgeConfig.Builder("APP_NAME", "APP_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build();
    Airbridge.init(this, config);
    
    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).getDeviceId());
    // Explicitly start tracking
    Airbridge.startTracking();
}
```

{% endsubtab %}
{% subtab Kotlin %}

```kotlin
// MainApplication.kt
override fun onCreate() {
    super.onCreate()
    // Initialize Airbridge SDK
    val config = AirbridgeConfig.Builder("YOUR_APP_NAME", "YOUR_APP_SDK_TOKEN")
        // Make Airbridge SDK explicitly start tracking
        .setAutoStartTrackingEnabled(false)
        .build()
    Airbridge.init(this, config)

    // Set device alias into Airbridge SDK
    Airbridge.getCurrentUser().setAlias("braze_device_id", Braze.getInstance(this).deviceId)
    // Explicitly start tracking
    Airbridge.startTracking()
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### iOS

Wenn Sie eine iOS-App haben, können Sie sich dafür entscheiden, IDFV zu sammeln, indem Sie das Feld useUUIDAsDeviceId auf false setzen. Wenn diese Option nicht gesetzt ist, wird die iOS-Attribution wahrscheinlich nicht genau von Airbridge auf Braze übertragen. Weitere Informationen finden Sie unter Sammeln von IDFV.

{% tabs %}
{% tab iOS %}
{% subtabs %}
{% subtab Swift %}

```swift
// AppDelegate.swift
func application(
  _ application: UIApplication,
  didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?
) {
    AirBridge.setAutoStartTrackingEnabled(false)
    AirBridge.getInstance("YOUR_APP_TOKEN", appName:"YOUR_APP_NAME", withLaunchOptions:launchOptions)

    AirBridge.state()?.addUserAlias(withKey:"braze_device_id", value:Appboy.sharedInstance()?.getDeviceId())
    AirBridge.startTracking()
}
```

{% endsubtab %}
{% subtab Objective-C %}

```objc
// AppDelegate.m
-           (BOOL)application:(UIApplication *)application
didFinishLaunchingWithOptions:(NSDictionary *)launchOptions
{
  AirBridge.autoStartTrackingEnabled = NO;
  [AirBridge getInstance:@"YOUR_APP_TOKEN" appName:@"YOUR_APP_NAME" withLaunchOptions:launchOptions];

    [AirBridge.state addUserAliasWithKey:@"braze_device_id" value:Appboy.sharedInstance.getDeviceId];
    [AirBridge startTracking];
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

#### React Native

{% tabs %}
{% tab TypeScript %}

```typescript
Braze.getInstallTrackingId(function (error, brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
    Airbirdge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Cordova

{% tabs %}
{% tab TypeScript %}

```typescript
AppboyPlugin.getDeviceId(function (brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Flattern

{% tabs %}
{% tab TypeScript %}

```typescript
BrazePlugin.getInstallTrackingId().then((brazeID) {
    Airbridge.state.setDeviceAlias("braze_device_id", brazeID)
  Airbridge.state.startTracking()
})
```

{% endtab %}
{% endtabs %}

#### Einigkeit

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### Schritt 2: Holen Sie sich den Braze-Datenimportschlüssel

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Airbridge**.

{% alert note %}
Wenn Sie die [ältere Navigation]({{site.baseurl}}/navigation) verwenden, finden Sie **Technologiepartner** unter **Integrationen**.
{% endalert %}

Hier finden Sie den REST-Endpunkt und generieren Ihren Braze-Datenimportschlüssel. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimportschlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Airbridge einrichten.

![][1]

### Schritt 3: Konfigurieren Sie Braze im Dashboard von Airbridge

1. Navigieren Sie in Airbridge zu **Integrationen > Drittanbieter-Integrationen** in der linken Seitenleiste und wählen Sie **Braze**.
2. Geben Sie den Datenimportschlüssel und den REST-Endpunkt an, den Sie im Dashboard von Braze gefunden haben.
3. Wählen Sie den Ereignistyp aus (Ereignis installieren oder Ereignis installieren & vertiefen öffnen) und speichern Sie.

{% alert note %}
Die Attributionsdaten für Kampagnen, die zu offenen Deeplink-Ereignissen geführt haben, werden auf Geräteebene aktualisiert. Wenn zum Beispiel zwei Benutzer ein einziges Gerät verwenden und ein Benutzer ein Deeplink-Öffnungsereignis durchführt, werden die Attributionsdaten dieses Ereignisses auch in den Daten des anderen Benutzers berücksichtigt.
{% endalert %}

Ausführlichere Anweisungen finden Sie unter [Airbridge](https://help.airbridge.io/en/guides/braze).

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attributionsdaten von Airbridge erhält, ändert sich der Verbindungsstatus auf der Airbridge-Technologiepartnerseite in Braze von "Nicht verbunden" zu "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt.

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine zugeordnete Installation erhalten. Organische Installationen, die vom Airbridge-Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht berücksichtigt.

## Verfügbare Datenfelder

Airbridge kann vier Arten von Attributionsdaten an Braze senden, die in der folgenden Datenfeldtabelle aufgeführt sind. Diese Daten können im Airbridge-Dashboard angezeigt werden und werden für die Zuordnung von Benutzerinstallationen und die Filterung verwendet.

Vorausgesetzt, Sie konfigurieren Ihre Integration wie vorgeschlagen, wird Braze die Installationsdaten den Segmentfiltern zuordnen.

| Airbridge-Datenfeld | Hartlöt-Segmentfilter | Beschreibung |
| -------------------- | ---------------------| ---- |
| `Channel` | Install-Attribution-Quelle | Der Kanal, auf den die Installationen oder Deeplink-Öffnungen zurückzuführen sind |
| `Campaign` | Install-Attribution-Kampagne | Die Kampagne, auf die die Installationen oder Deeplink-Öffnungen zurückgeführt werden |
| `Ad Group` | Install-Attribution-Anzeigengruppe | Die Anzeigengruppe, der die Installationen oder Deeplink-Öffnungen zugeschrieben werden |
| `Ad Creative` | Install-Attribution-Anzeige | Das Anzeigenmotiv, das die Installationen oder Deeplink-Öffnungen verursacht, wird zugeschrieben |

Ihre Nutzerbasis kann im Braze Dashboard mit Hilfe der Filter für die Installationsattribution nach Attributionsdaten segmentiert werden.

![][2]

## Meta Business Zuordnungsdaten

Attributionsdaten für Meta Business-Kampagnen sind nicht über unsere Partner verfügbar. Diese Medienquelle erlaubt ihren Partnern nicht, Attributionsdaten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Airbridge Klick-Tracking-URLs in Braze (optional)

Durch die Verwendung von Klick-Tracking-Links in Ihren Braze-Kampagnen können Sie leicht erkennen, welche Kampagnen zu App-Installationen und Wiedereinstieg führen. So können Sie Ihre Marketingbemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen investieren sollten, um einen maximalen ROI zu erzielen.

Um mit Airbridge zu arbeiten, klicken Sie auf die Tracking-Links und besuchen Sie [Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link). Nachdem die Einrichtung abgeschlossen ist, können Sie die Airbridge-Klick-Tracking-Links direkt in Ihre Braze-Kampagnen einfügen. Airbridge verwendet dann seine [probabilistischen Zuordnungsmethoden](https://help.airbridge.io/en/guides/identity-matching), um den Benutzer, der auf den Link geklickt hat, zuzuordnen. Wir empfehlen Ihnen, Ihre Airbridge-Tracking-Links mit einer Gerätekennung zu versehen, um die Genauigkeit der Zuordnungen Ihrer Braze-Kampagnen zu verbessern. Dadurch wird der Benutzer, der auf den Link geklickt hat, deterministisch zugeordnet.

{% tabs %}
{% tab Android %}
Für Android ermöglicht Braze seinen Kunden, sich für die [Erfassung der Google Werbe-ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die Airbridge SDK-Integration erfasst. Sie können die GAID in Ihre Airbridge-Klickverfolgungslinks aufnehmen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Airbridge die IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Gerätekennung verwendet werden. Sie können die IDFV in Ihre Airbridge-Klickverfolgungslinks integrieren, indem Sie die folgende Liquid-Logik verwenden:

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}

{% alert note %}
**Diese Empfehlung ist rein optional**<br>
Wenn Sie derzeit keine Gerätekennungen - wie IDFV oder GAID - in Ihren Click-Tracking-Links verwenden oder dies in Zukunft nicht vorhaben, kann Airbridge diese Klicks dennoch durch seine probabilistische Modellierung zuordnen.
{% endalert %}

[1]: {% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %}
[2]: {% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %}
