# 位置情報の追跡

> この記事では、Android または FireOS アプリケーションの位置情報の追跡を構成する方法を説明します。

次の権限のうち少なくとも1つを`AndroidManifest.xml`ファイルに追加して、位置データを収集するアプリの意図を宣言します。

```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```
```xml
<uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />
```

`ACCESS_FINE_LOCATION`には、ユーザーの位置情報をレポートする際に GPS データが含まれます。`ACCESS_COARSE_LOCATION`には、利用可能な最もバッテリー効率の高い非 GPS プロバイダー (ネットワークなど) からのデータが含まれます。ほとんどの位置データの使用例では、大まかな位置で十分な可能性があります。ただし、ランタイム権限モデルでは、ユーザーから位置権限を受け取ると、精度の高い位置データの収集が暗黙的に許可されます。これらの位置情報権限の違いとその使用方法について詳しくは、Android Developers の [Location Strategies](https://stuff.mit.edu/afs/sipb/project/android/docs/guide/topics/location/strategies.html) をご覧ください。

{% alert important %}
Android M のリリースにより、Android はインストール時権限モデルからランタイム権限モデルに切り替わりました。Android M 以降を実行しているデバイスで位置追跡を有効にするには、アプリがユーザーから位置を使用する許可を明示的に受け取る必要があります (Braze はこれを行いません)。位置情報の許可が取得された後、`braze.xml`で位置情報の収集が有効になっている場合、Braze は次回のセッション開始時に位置の追跡を自動的に開始します。以前のバージョンの Android を実行しているデバイスでは、位置情報権限を`AndroidManifest.xml`で宣言する必要があるだけです。詳細については、Android の[権限に関するドキュメント](https://developer.android.com/training/permissions/index.html)を参照してください。
{% endalert %}

## 自動位置情報の追跡を無効にする

### コンパイル時オプション

コンパイル時に自動位置情報の追跡を無効にするには、`braze.xml`で`com_braze_enable_location_collection`を`false`に設定します。

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

### ランタイムオプション

ランタイム時に自動位置情報の追跡を選択的に無効にするには、[`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration)を使用します。

{% tabs %}
{% tab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endtab %}
{% tab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endtab %}
{% endtabs %}

## 位置情報を手動で記録する

自動追跡が無効になっている場合でも、以下のように`BrazeUser`の[`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html)メソッドで、単一の位置のデータ ポイントを手動でログに記録できます。 

{% tabs %}
{% tab JAVA %}

```java
Braze.getInstance(context).getCurrentUser(new IValueCallback<BrazeUser>() {
  @Override
  public void onSuccess(BrazeUser brazeUser) {
    brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE);
  }
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
Braze.getInstance(context).getCurrentUser { brazeUser ->
  brazeUser.setLastKnownLocation(LATITUDE_DOUBLE_VALUE, LONGITUDE_DOUBLE_VALUE, ALTITUDE_DOUBLE_VALUE, ACCURACY_DOUBLE_VALUE)
}
```

{% endtab %}
{% endtabs %}

