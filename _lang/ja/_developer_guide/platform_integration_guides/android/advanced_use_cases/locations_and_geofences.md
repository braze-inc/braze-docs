---
nav_title: 位置情報とジオフェンス
article_title: Android と FireOS の位置情報とジオフェンス
platform: 
  - Android
  - FireOS
page_order: 6
description: "このリファレンス記事では、Android または FireOS アプリケーションに位置情報とジオフェンスを実装する方法を説明します。"
Tool:
  - Location

---

# 位置情報とジオフェンス

> [ジオフェンスは]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences/)、一部の Braze パッケージでのみ利用できます。利用するには、[サポートチケット][support]を作成するか、Braze カスタマーサクセスマネージャーにご相談ください。

Android のジオフェンスをサポートするには、以下の条件を満たす必要があります。

1. 統合はバックグラウンドプッシュ通知に対応している必要があります。
2. Braze のジオフェンスまたは位置情報収集機能が有効になっている必要があります。

## ステップ1: build.gradle を更新する

`android-sdk-location`をアプリレベル`build.gradle`に追加します。また、Google Play Services [セットアップガイド][10]を使用して、Google Play Services の[位置情報パッケージ][3]を追加します。

```
dependencies {
  implementation "com.braze:android-sdk-location:+"
  implementation "com.google.android.gms:play-services-location:${PLAY_SERVICES_VERSION}"
}
```

## ステップ2: マニフェストを更新する

`AndroidManifest.xml`にブート、精度の高い位置情報、バックグラウンド位置情報の権限を追加します。

```xml
<uses-permission android:name="android.permission.RECEIVE_BOOT_COMPLETED" />
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
<uses-permission android:name="android.permission.ACCESS_BACKGROUND_LOCATION" />
```

{% alert important %}
バックグラウンド位置情報アクセス権限は Android 10 で追加されたもので、Android 10 以降のすべてのデバイスでは、アプリがバックグラウンドで動作している間ジオフェンスが機能するために必要です。
{% endalert %}

`AndroidManifest.xml`の`application`エレメントに Braze ブートレシーバーを追加します。

```xml
<receiver android:name="com.braze.BrazeBootReceiver">
  <intent-filter>
    <action android:name="android.intent.action.BOOT_COMPLETED" />
  </intent-filter>
</receiver>
```

## ステップ3: Braze の位置情報収集機能を有効にする

まだ Braze の位置情報収集機能を有効にしていない場合は、`com_braze_enable_location_collection`を含むように`braze.xml`ファイルを更新し、その値が`true`に設定されていることを確認します。

```xml
<bool name="com_braze_enable_location_collection">true</bool>
```

{% alert important %}
Braze Android SDK バージョン3.6.0から、Braze の位置情報収集機能はデフォルトで無効になっています。
{% endalert %}

Braze のジオフェンスは、Braze の位置情報収集機能が有効になっている場合に有効になります。デフォルトの位置情報収集機能をオプトアウトしながらも、ジオフェンスを使用したい場合は、`com_braze_enable_location_collection`の値とは別に、`braze.xml`のキー`com_braze_geofences_enabled`の値を`true`に設定することで、選択的に有効にすることができます。

```xml
<bool name="com_braze_geofences_enabled">true</bool>
```

## ステップ4: エンドユーザーから位置情報の許可を得る

Android M 以降のバージョンでは、位置情報を収集したりジオフェンスを登録したりする前に、エンドユーザーに位置情報の許可を求める必要があります。

ユーザーがアプリに位置情報の許可を付与したときに Braze に通知するために、以下の呼び出しを追加します。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).requestLocationInitialization();
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).requestLocationInitialization()
```

{% endtab %}
{% endtabs %}

これにより、SDK は Braze サーバーにジオフェンスを要求し、ジオフェンスの追跡を初期化します。

実装例については、[`RuntimePermissionUtils.java`][4]を参照してください。

{% tabs %}
{% tab JAVA %}

\`\`\`java
public class RuntimePermissionUtils {
  private static final String TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils.class);
  public static final int DROIDBOY\_PERMISSION\_LOCATION = 40;

  public static void handleOnRequestPermissionsResult(Context context, int requestCode, int[] grantResults) {
switch (requestCode) {
case DROIDBOY_PERMISSION_LOCATION:
// In Android Q, we require both FINE and BACKGROUND location permissions. Both
// are requested simultaneously.
if (areAllPermissionsGranted(grantResults)) {
Log.i(TAG, "Required location permissions granted.");
Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH_SHORT).show();
Braze.getInstance(context).requestLocationInitialization();
} else {
    Log.i(TAG, "Required location permissions NOT granted.");
      Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH\_SHORT).show();
        }
        break;
        default:
          break;
          }
          }

  private static boolean areAllPermissionsGranted(int[] grantResults) {
for (int grantResult : grantResults) {
if (grantResult != PackageManager.PERMISSION_GRANTED) {
return false;
}
    }
      return true;
        }
      }
    \`\`\`

{% endtab %}
{% tab KOTLIN %}

\`\`\`kotlin
object RuntimePermissionUtils {
  private val TAG = BrazeLogger.getBrazeLogTag(RuntimePermissionUtils::class.java!!)
  val DROIDBOY\_PERMISSION\_LOCATION = 40

  fun handleOnRequestPermissionsResult(context:Context, requestCode:Int, grantResults:IntArray) {
    when (requestCode) {
      DROIDBOY\_PERMISSION\_LOCATION ->
        // In Android Q, we require both FINE and BACKGROUND location permissions. Both
// are requested simultaneously.
        if (areAllPermissionsGranted(grantResults)) {
        Log.i(TAG, "Required location permissions granted.")
          Toast.makeText(context, "Required location permissions granted.", Toast.LENGTH\_SHORT).show()
          Braze.getInstance(context).requestLocationInitialization()
          } else {
        Log.i(TAG, "Required location permissions NOT granted.")
          Toast.makeText(context, "Required location permissions NOT granted.", Toast.LENGTH\_SHORT).show()
          }
        else -> {
      }
      }
    }

  private fun areAllPermissionsGranted(grantResults:IntArray):Boolean {
    for (grantResult in grantResults) {
      if (grantResult != PackageManager.PERMISSION\_GRANTED) {
        return false
      }
    }
    return true
  }
}
\`\`\`

{% endtab %}
{% endtabs %}

先のサンプルコードの使用は、以下の方法で行います。

{% tabs %}
{% tab JAVA %}

```java
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    boolean hasAllPermissions = PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION);
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  } else {
    if (!PermissionUtils.hasPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION},
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION);
    }
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
  if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.Q) {
    val hasAllPermissions = PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_BACKGROUND_LOCATION)
        && PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)
    if (!hasAllPermissions) {
      // Request both BACKGROUND and FINE location permissions
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.ACCESS_BACKGROUND_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  } else {
    if (!PermissionUtils.hasPermission(applicationContext, Manifest.permission.ACCESS_FINE_LOCATION)) {
      // Request only FINE location permission
      requestPermissions(arrayOf(android.Manifest.permission.ACCESS_FINE_LOCATION),
          RuntimePermissionUtils.DROIDBOY_PERMISSION_LOCATION)
    }
  }
}
```

{% endtab %}
{% endtabs %}

## ステップ5: ダッシュボードでジオフェンスを有効にする

Android では、1つのアプリに保存できるジオフェンスは100個までとなっています。Braze の位置情報製品は、利用可能であれば最大20のジオフェンススロットを使用します。アプリ内の他のジオフェンス関連機能への偶発的または不要な中断を防ぐため、位置情報ジオフェンスはダッシュボード上で個々のアプリに対して有効にする必要があります。

Braze 位置情報製品が正しく動作するには、アプリが利用可能なジオフェンススポットをすべて使用していないことを確認する必要があります。

### ロケーションページからジオフェンスを有効にする

![The geofence options on the Braze locations page.]({% image_buster /assets/img_archive/enable-geofences-locations-page.png %})

### 設定ページからジオフェンスを有効にする

![The geofence checkbox located on the Braze settings pages.]({% image_buster /assets/img_archive/enable-geofences-app-settings-page.png %}){: style="max-width:65%;" }

## ステップ6: ジオフェンスの更新を手動でリクエストする (オプション)

デフォルトでは、Braze は自動的にデバイスの位置情報を取得し、その取得した位置情報に基づいてジオフェンスを要求します。しかし、代わりに近接する Braze ジオフェンスを取得するために使用される GPS 座標を手動で指定することもできます。手動で Braze ジオフェンスをリクエストするには、自動 Braze ジオフェンスリクエストを無効にし、リクエスト用に GPS 座標を指定する必要があります。

#### パート1: 自動ジオフェンスリクエストを無効にする

自動 Braze ジオフェンスリクエストは、`com_braze_automatic_geofence_requests_enabled`を`false`に設定することで、`braze.xml`ファイルで無効にすることができます。

```xml
<bool name="com_braze_automatic_geofence_requests_enabled">false</bool>
```

これはさらに、ランタイム時に以下の方法で行うことができます。

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig.Builder brazeConfigBuilder = new BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false);
Braze.configure(getApplicationContext(), brazeConfigBuilder.build());
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfigBuilder = BrazeConfig.Builder()
    .setAutomaticGeofenceRequestsEnabled(false)
Braze.configure(applicationContext, brazeConfigBuilder.build())
```

{% endtab %}
{% endtabs %}

#### パート2: GPS 座標で Braze のジオフェンスを手動でリクエストする

Braze のジオフェンスは、[`requestGeofences()`][11]メソッドを使用して手動でリクエストします。

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(getApplicationContext()).requestGeofences(latitude, longitude);
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(applicationContext).requestGeofences(33.078947, -116.601356)
```

{% endtab %}
{% endtabs %}

{% alert important %}
ジオフェンスは、SDK により自動的に、またはこのメソッドにより手動で、セッションごとに一度だけリクエストできます。
{% endalert %}

## プッシュ同期

Braze では、バックグラウンドプッシュを使用してジオフェンスをデバイスに同期します。ほとんどの場合、この機能はアプリ側でのさらなる統合を必要としないため、コードの変更を伴いません。

しかし、アプリケーションが停止している場合にバックグラウンドプッシュを受信すると、バックグラウンドで起動し、その`Application.onCreate()`メソッドが呼び出されることに注意してください。カスタムの`Application.onCreate()`実装がある場合は、自動サーバーコールやバックグラウンドプッシュでトリガーしないアクションを延期する必要があります。

[3]: https://developers.google.com/android/reference/com/google/android/gms/location/package-summary
[4]: https://github.com/braze-inc/braze-android-sdk/blob/master/droidboy/src/main/java/com/appboy/sample/util/RuntimePermissionUtils.kt
[10]: https://developers.google.com/android/guides/setup
[11]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-geofences.html
[support]: {{site.baseurl}}/braze_support/
