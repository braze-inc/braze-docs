---
nav_title: Airbridge
article_title: Airbridge
alias: /partners/airbridge/
description: "Dieser referenzierte Artikel beschreibt die Partnerschaft zwischen Braze und Airbridge, die personenbasierte Attribution und inkrementelle Messungen anbietet, um die tatsächliche Effektivität des Marketings über Geräte, Identitäten und Plattformen hinweg zu messen."
page_type: partner
search_tag: Partner

---

# Airbridge

> [Airbridge](https://www.airbridge.io/) ist eine einheitliche Plattform für die Messung mobiler Daten, die Ihnen hilft, wahre Wachstumsquellen durch mobile Attribution, inkrementelle Messung und Marketing-Mix-Modellierung zu entdecken.

_Diese Integration wird von Airbridge gepflegt._

## Über die Integration

Mit der Integration von Braze und Airbridge können Sie alle nicht-organischen Daten zur Install-Attribution von Airbridge an Braze weitergeben, um personalisierte Kampagnen zu erstellen.

## Voraussetzungen

| Anforderung | Beschreibung |
|---|---|
| Airbridge-Konto | Um diese Partnerschaft nutzen zu können, benötigen Sie ein Airbridge-Konto. |
| iOS oder Android App | Diese Integration unterstützt iOS- und Android-Apps. Je nach Plattform können Code Snippets in Ihrer Anwendung erforderlich sein. |
| Airbridge SDK | Zusätzlich zum erforderlichen Braze SDK müssen Sie das Airbridge [Android](https://help.airbridge.io/en/developers/android-sdk) oder [iOS](https://help.airbridge.io/en/developers/ios-sdk) SDK installieren. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integration

### Schritt 1: ID des Geräts abbilden

Die Server-zu-Server Integration kann durch Einfügen der folgenden Code-Snippets in Ihre Apps aktiviert werden.

#### Android

Wenn Sie eine Android App haben, müssen Sie eine eindeutige Braze ID für das Gerät an Airbridge weitergeben.

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

Wenn Sie eine iOS App haben, können Sie sich dafür entscheiden, IDFV zu sammeln, indem Sie das Feld useUUIDAsDeviceId auf false setzen. Wenn diese Option nicht gesetzt ist, wird die iOS Attribution wahrscheinlich nicht genau von Airbridge auf Braze abgebildet. Weitere Informationen finden Sie unter Sammeln von IDFV.

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

#### Flutter

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

#### Unity

{% tabs %}
{% tab C# %}

```c#
string BrazeID = AppboyBinding.GetInstallTrackingId();
AirbridgeUnity.SetDeviceAlias("braze_device_id", BrazeID);
AirbridgeUnity.StartTracking()
```

{% endtab %}
{% endtabs %}

### Schritt 2: Holen Sie sich den Datenimport-Schlüssel für Braze

Navigieren Sie in Braze zu **Partnerintegrationen** > **Technologiepartner** und wählen Sie **Airbridge** aus.

Hier finden Sie den REST-Endpunkt und generieren Ihren Datenimport-Schlüssel für Braze. Nachdem der Schlüssel generiert wurde, können Sie einen neuen Schlüssel erstellen oder einen bestehenden Schlüssel ungültig machen. Der Datenimport-Schlüssel und der REST-Endpunkt werden im nächsten Schritt verwendet, wenn Sie ein Postback im Dashboard von Airbridge einrichten.

![][1]

### Schritt 3: Konfigurieren Sie Braze im Dashboard von Airbridge

1. Navigieren Sie in Airbridge in der linken Seitenleiste zu **Integrationen > Drittanbieter-Integrationen** und wählen Sie **Braze** aus.
2. Geben Sie den Datenimport-Schlüssel und den REST-Endpunkt an, den Sie im Braze-Dashboard gefunden haben.
3. Wählen Sie den Ereignistyp (Ereignis installieren oder Ereignis installieren & öffnen) und speichern Sie.

{% alert note %}
Die Attribution-Daten für Kampagnen, die zu Deeplink-Öffnungen geführt haben, werden auf der Ebene der Geräte aktualisiert. Wenn beispielsweise zwei Nutzer:innen ein Gerät verwenden und ein Nutzer:in ein Deeplink-Öffnungs-Ereignis ausführt, werden die Attributionsdaten dieses Ereignisses auch in die Daten des anderen Nutzers:in übernommen.
{% endalert %}

Ausführlichere Anweisungen finden Sie unter [Airbridge](https://help.airbridge.io/en/guides/braze).

### Schritt 4: Bestätigen Sie die Integration

Sobald Braze Attribution-Daten von Airbridge erhält, ändert sich der Verbindungsstatus auf der Technologie-Partnerseite von Airbridge in Braze von "Nicht verbunden" zu "Verbunden". Ein Zeitstempel der letzten erfolgreichen Anfrage wird ebenfalls mitgeschickt.

Beachten Sie, dass dies erst dann geschieht, wenn wir Daten über eine attributierte Installation erhalten. Organische Installationen, die vom Airbridge-Postback ausgeschlossen werden sollten, werden von unserer API ignoriert und bei der Ermittlung, ob eine erfolgreiche Verbindung hergestellt wurde, nicht mitgezählt.

## Verfügbare Datenfelder

Airbridge kann vier Arten von Attributionsdaten an Braze senden, die in dem folgenden Chart aufgeführt sind. Diese Daten können im Airbridge Dashboard eingesehen werden und werden für die Install-Attribution und Filterung von Nutzer:innen verwendet.

Vorausgesetzt, Sie konfigurieren Ihre Integration wie vorgeschlagen, wird Braze die Daten der Installation den Filtern der Segmente zuordnen.

| Airbridge Datenfeld | Braze Segmente Filter | Beschreibung |
| -------------------- | ---------------------| ---- |
| `Channel` | Install-Attribution-Quelle | Der Kanal, dem die Installationen oder Öffnungen des Deeplinks zugeschrieben werden |
| `Campaign` | Install-Attribution-Kampagne | Die Kampagne, der die Installationen oder Deeplink-Öffnungen zugerechnet werden |
| `Ad Group` | Install-Attribution-Anzeigengruppe | Die Anzeigengruppe, der die Installationen oder Deeplink-Öffnungen zugeschrieben werden |
| `Ad Creative` | Install-Attribution-Anzeige | Das Werbemittel, auf das die Öffnungen der Installationen oder Deeplinks zurückzuführen sind |

Ihre Nutzer:innen können im Braze-Dashboard mit Hilfe der Install-Attribution-Filter nach Attributionsdaten segmentiert werden.

![][2]

## Meta Business Attribution Daten

Attributionsdaten für Meta Business Kampagnen sind nicht über unsere Partner verfügbar. Diese Medienquelle erlaubt ihren Partnern nicht, Attribution-Daten an Dritte weiterzugeben, und daher können unsere Partner diese Daten nicht an Braze senden.

## Airbridge Click Tracking URLs in Braze (optional)

Wenn Sie Tracking-Links für Klicks in Ihren Braze-Kampagnen verwenden, können Sie leicht erkennen, welche Kampagnen zu App-Installationen und erneuter Interaktion führen. So können Sie Ihre Marketing-Bemühungen effektiver messen und datengestützte Entscheidungen darüber treffen, wo Sie mehr Ressourcen für einen maximalen ROI investieren sollten.

Um mit Airbridge Click Tracking Links zu beginnen, besuchen Sie [Airbridge](https://help.airbridge.io/en/guides/creating-a-new-tracking-link). Nachdem die Einrichtung abgeschlossen ist, können Sie die Airbridge Click Tracking Links direkt in Ihre Kampagnen bei Braze einfügen. Airbridge verwendet dann seine [probabilistischen Attributionsmethoden](https://help.airbridge.io/en/guides/identity-matching), um den Nutzer:innen, die auf den Link geklickt haben, zu attributieren. Wir empfehlen, Ihre Airbridge Tracking-Links mit einem Bezeichner für das Gerät zu versehen, um die Genauigkeit der Attributionen Ihrer Kampagnen von Braze zu verbessern. Dadurch wird der Nutzer:in, der auf den Link geklickt hat, deterministisch attributiert.

{% tabs %}
{% tab Android %}
Für Android erlaubt Braze den Kund:in, sich für die [Sammlung der Google Advertising ID (GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)) zu entscheiden. Die GAID wird auch nativ über die Airbridge SDK-Integration erfasst. Sie können die GAID in Ihre Airbridge Click Tracking Links einfügen, indem Sie die folgende Liquid-Logik verwenden:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
Für iOS erfassen sowohl Braze als auch Airbridge den IDFV automatisch und nativ über unsere SDK-Integrationen. Dies kann als Bezeichner für das Gerät verwendet werden. Sie können den Identifier for Vendors (IDFV) in Ihre Airbridge Click Tracking-Links integrieren, indem Sie die folgende Liquid-Logik verwenden:

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
Wenn Sie derzeit keine Geräte-Identifikatoren - wie IDFV oder GAID - in Ihren Click-through-Links verwenden oder dies in Zukunft nicht vorhaben, ist Airbridge dennoch in der Lage, diese Klicks durch seine probabilistische Modellierung zu attributieren.
{% endalert %}


[1]: {% image_buster /assets/img/airbridge/airbridge_integration_step_1.png %}
[2]: {% image_buster /assets/img/airbridge/airbridge_integration_step_2.png %}
