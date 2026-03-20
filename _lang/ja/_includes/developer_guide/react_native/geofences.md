{% alert important %}
React Native SDKでは、ジオフェンスは**iOSとAndroid**の両方でサポートされている。この`requestLocationInitialization`方法はAndroid専用であり、iOSでは必要とされない。その`requestGeofences`方法は両方のプラットフォームで利用できる。デフォルトでは、SDKは位置情報が利用可能な場合にジオフェンスを自動的に要求し監視する。この自動設定を利用するか、手動で要求するために\``requestGeofences`geofenceRequest()`を呼び出すことができる。
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %} Androidでは、ジオフェンス同期のために[サイレントプッシュ通知を設定]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=android)する必要がある。

## ジオフェンスの設定 {#setting-up-geofences}

### ステップ 1: Brazeで有効にする

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### ステップ 2:完全なネイティブAndroid設定

React Native SDKはネイティブのBraze Android SDKを使用するため、プロジェクトのネイティブAndroidジオフェンス設定を完了させる必要がある。これらのステップに相当するiOS版のステップは、ネイティブSWIFT SDKのジオフェンスガイド（[ステップ2.2から3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)）で説明されている。ステップ2.1（BrazeLocationモジュールの追加）はReact Nativeでは不要だ。なぜならBrazeLocationはBraze React Native SDKに既に暗黙的に含まれているからだ。

1. **更新`build.gradle`：**Google Play Servicesの位置情報機能を追加する`android-sdk-location`。[Androidのジオフェンスを]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)参照せよ。
2. **マニフェストを更新する：**位置情報の権限を追加し、Brazeのブートレシーバーを追加する。[Androidのジオフェンスを]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)参照せよ。
3. **Brazeの位置情報収集のイネーブルメント：**ファイルを`braze.xml`更新しろ。[Androidのジオフェンスを]({{site.baseurl}}/developer_guide/geofences/?sdktab=android)参照せよ。

### ステップ 3:完全なネイティブiOS設定

React Native SDKはネイティブのBraze iOS SDKを使用するため、プロジェクトのネイティブiOSジオフェンス設定を完了するには、ネイティブSWIFT SDKの手順に従い、ステップ2.2から開始する。具体的には`Info.plist`、位置情報使用説明を更新する（ステップ2.2）、Braze設定でジオフェンスをイネーブルメントする（`automaticGeofenceRequests = true`ステップ3）、オプションでバックグラウンドレポートをイネーブルメントする（ステップ3.1）こと。ステップ2.1（BrazeLocationモジュールの追加）は不要だ。BrazeLocationはBraze React Native SDKに既に暗黙的に含まれている。[iOSのジオフェンスを]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)参照せよ[。ステップ2.2から3.1まで]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module)。

### ステップ 4: JavaScriptからジオフェンスをリクエストする

**Android の場合:**ユーザーが位置情報の許可を与えた後、Brazeの位置情報機能を初期化し、Brazeサーバーからジオフェンスをリクエストするために\`BrazeLocation`requestLocationInitialization()`.initialize()`を呼び出す。この方法はiOSではサポートされておらず、iOSでは必要とされない。

**iOSの場合：**対応する設定`automaticGeofenceRequests`は、ネイティブのSWIFTまたはObjective CのBraze設定でイネーブルメントする（ステップ3を参照）。このイネーブルメントが有効になると、SDKは位置情報が利用可能な場合に自動的にジオフェンスを要求し監視する。\`geofence.request()\`に相当するJavaScript呼び出しは`requestLocationInitialization`不要だ。

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### ステップ 5: ジオフェンスを手動でリクエストする（任意）

iOSとAndroidの両方で、特定のGPS座標に対してジオフェンスの更新を手動でリクエスト`requestGeofences`できる。デフォルトでは、Brazeは自動的にデバイスの位置情報を取得し、ジオフェンスをリクエストする。代わりに手動で座標を指定するには：

1. 自動的なジオフェンスリクエストを無効にする。Androidでは、設定ファイルで を`com_braze_automatic_geofence_requests_enabled``braze.xml``false`に設定する。iOSでは、Braze`false`の設定で を`automaticGeofenceRequests`に設定する。
2. 指定した緯度と経度で`requestGeofences`呼び出す：

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
ジオフェンスは、SDK により自動的に、またはこのメソッドにより手動で、セッションごとに一度だけリクエストできます。
{% endalert %}
