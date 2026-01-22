## 現在地を記録する

継続的なトラッキングが無効になっている場合でも、ユーザーの現在位置を [`setLastKnownLocation()`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/set-last-known-location.html)メソッドを使う。

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

## 位置情報の追跡を続ける

{% alert important %}
[Android Marshmallowからは](https://developer.android.com/training/permissions/index.html)、位置情報の追跡を明示的にオプトインするようユーザーに促す必要がある。そうすれば、Brazeは次のセッションの最初に彼らの位置情報の追跡を開始することができる。これは、`AndroidManifest.xml` で位置情報の権限のみを宣言する必要があった以前のバージョンのAndroidとは異なる。
{% endalert %}

ユーザーの位置情報を継続的に追跡するには、`AndroidManifest.xml` ファイルに以下の権限の少なくとも1つを追加して、アプリが位置情報データを収集する意図を宣言する必要がある。

|権限|説明|
|---|---|
| `ACCESS_COARSE_LOCATION` | 最もバッテリー効率の良い、非GPSプロバイダー（ホームネットワークなど）を使用する。通常、ほとんどの位置情報のニーズにはこれで十分である。実行時権限モデルの下では、位置情報の権限を与えることは、暗黙のうちに、細かい位置情報のデータ収集を許可することになる。 |
| `ACCESS_FINE_LOCATION`   | より正確な位置情報のためのGPSデータを含む。実行時権限モデルの下では、ロケーション権限の付与は、細かいロケーショ ンアクセスもカバーする。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

`AndroidManifest.xml` は次のようになります。

```xml
<manifest ... >
    <uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
    <uses-permission android:name="android.permission.ACCESS_FINE_LOCATION" />

    <application ... >
        ...
    </application>
</manifest>
```

## 連続トラッキングを無効にする

連続トラッキングは、コンパイル時または実行時に無効にすることができる。

{% tabs local %}
{% tab compile time %}

コンパイル時に位置情報の連続追跡を無効にするには、`braze.xml` で`com_braze_enable_location_collection` を`false` に設定する：

```xml
<bool name="com_braze_enable_location_collection">false</bool>
```

{% endtab %}
{% tab runtime %}

実行時に位置情報の連続追跡を選択的に無効にするには、次のようにする。 [`BrazeConfig`]({{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/runtime_configuration/#runtime-configuration):

{% subtabs %}
{% subtab JAVA %}

```java
BrazeConfig brazeConfig = new BrazeConfig.Builder()
  .setIsLocationCollectionEnabled(false)
  .build();
Braze.configure(this, brazeConfig);
```
 
{% endsubtab %}
{% subtab KOTLIN %}

```kotlin
val brazeConfig = BrazeConfig.Builder()
    .setIsLocationCollectionEnabled(false)
    .build()
Braze.configure(this, brazeConfig)
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}
