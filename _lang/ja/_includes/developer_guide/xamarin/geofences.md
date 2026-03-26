{% multi_lang_include developer_guide/prerequisites/xamarin.md %} さらに、[サイレントプッシュ通知の設定]({{site.baseurl}}/developer_guide/push_notifications/silent)も必要だ。

## 前提条件

ジオフェンスの使用を開始するために必要な最小限のSDKバージョンは以下の通りだ：

{% sdk_min_versions xamarin:9.0.0 %}

## ジオフェンスの設定 {#setting-up-geofences}

### ステップ 1: Brazeで有効にする

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

---

次に、Android または iOS のいずれかに対応する以下のプラットフォーム固有の手順に従う：

{% tabs %}
{% tab Android %}

### ステップ 2:依存関係を追加する

プロジェクトに次のNuGetパッケージ参照を追加する：

- `BrazePlatform.BrazeAndroidLocationBinding`

### ステップ 3:AndroidManifest.xml を更新する

以下の権限をあなたのに追加`AndroidManifest.xml`する：

```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
Android 10 以降の端末では、アプリがバックグラウンドで動作している間、ジオフェンスが機能するためにはバックグラウンド位置情報アクセス権限が必要だ。
{% endalert %}

### ステップ 4: Brazeの位置情報収集を設定する

Brazeの設定で位置情報の収集のイネーブルメントが有効になっていることを確認せよ。自動位置情報の収集なしでジオフェンスのイネーブルメントをしたい場合、設定ファイルに以下`Braze.xml`を記述する：

```xml
<bool name="com_braze_enable_location_collection">true</bool>
<bool name="com_braze_geofences_enabled">true</bool>
```

### ステップ 5: 実行時に位置情報の権限を求める

ジオフェンスを登録する前に、ユーザーから位置情報の権限を求めなければならない。C#のコードでは、次のパターンを使うんだ：

```csharp
using AndroidX.Core.App;
using AndroidX.Core.Content;

private void RequestLocationPermission()
{
  // ...existing code for checking and requesting permissions...
}

public override void OnRequestPermissionsResult(int requestCode, string[] permissions, Permission[] grantResults)
{
  // ...existing code for handling permission result...
}
```

権限が許可された後、Brazeの位置情報収集を初期化する：

```csharp
Braze.GetInstance(this).RequestLocationInitialization();
```

### ステップ 6: ジオフェンスの更新を手動でリクエストする (オプション)

特定の場所に対してジオフェンスを手動でリクエストするには：

```csharp
Braze.GetInstance(this).RequestGeofences(latitude, longitude);
```

{% alert important %}
ジオフェンスは、SDK により自動的に、またはこのメソッドにより手動で、セッションごとに一度だけリクエストできます。
{% endalert %}
{% endtab %}
{% tab iOS %}

### ステップ 2:依存関係を追加する

プロジェクトに次のNuGetパッケージ参照を追加する：

- `Braze.iOS.BrazeLocation`

### ステップ 3:位置情報の使用を設定する Info.plist

位置情報サービスに関する使用説明文字`Info.plist`列を追加する。

```xml
<key>NSLocationAlwaysAndWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
<key>NSLocationWhenInUseUsageDescription</key>
<string>This app uses your location to enable geofences and location-based messaging.</string>
```

{% alert important %}
Appleは廃止した`NSLocationAlwaysUsageDescription`。iOS 14以降では上記のキーを使用する。
{% endalert %}

### ステップ 4: Brazeの設定でジオフェンスをイネーブルメントする

アプリの起動コード（e.g., `App.xaml.cs`）で、ジオフェンスを有効にしてBrazeを設定する：

```csharp
using BrazeKit;
using BrazeLocation;

var configuration = new BRZConfiguration("<BRAZE_API_KEY>", "<BRAZE_ENDPOINT>");
configuration.Location.BrazeLocationProvider = new BrazeLocationProvider();
configuration.Location.AutomaticLocationCollection = true;
configuration.Location.GeofencesEnabled = true;
configuration.Location.AutomaticGeofenceRequests = true;
// ...other configuration...
var braze = new Braze(configuration);
```

### ステップ 5: バックグラウンド位置情報の更新をイネーブルメントする（任意）

バックグラウンドでジオフェンスを監視するには、次の設定をあなたのに追加して**位置情報の更新**バックグラウンド`Info.plist`モードのイネーブルメントを有効にせよ：

```xml
<key>UIBackgroundModes</key>
<array>
  <string>location</string>
</array>
```

次に、Brazeの設定で以下を設定する：

```csharp
configuration.Location.AllowBackgroundGeofenceUpdates = true;
configuration.Location.DistanceFilter = 8000; // meters
```

{% alert important %}
バッテリーの消耗を防ぐため、アプリの必要に応じた値に`DistanceFilter`設定せよ。
{% endalert %}

### ステップ 6: 位置情報の許可を要求する

ユーザーから、または`When In Use`の`Always`許可を求める：

```csharp
using CoreLocation;

var locationManager = new CLLocationManager();
locationManager.RequestWhenInUseAuthorization();
// or
locationManager.RequestAlwaysAuthorization();
```

{% alert important %}
許可`Always`がない場合、iOSはアプリが使用されていない間、位置情報サービスの実行を制限する。これはオペレーティングシステムによって強制されるものであり、Braze SDKでは回避できない。
{% endalert %}
{% endtab %}
{% endtabs %}
