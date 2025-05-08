---
nav_title: 統合
article_title: Cordova Braze SDK の統合
page_order: 0
---

# Cordova Braze SDK の統合

> Cordova Braze SDK を iOS または Android アプリに統合する方法について説明します。完了したら、[SDK をさらにカスタマイズ]({{site.baseurl}}/developer_guide/platform_integration_guides/cordova/initial_setup/customizations/)できます。

## SDK の統合

### ステップ1:SDK をプロジェクトに追加する

Cordova 6 以降では、GitHub から直接 SDK を追加できます。または、[GitHub リポジトリ](https://github.com/braze-inc/braze-cordova-sdk)の ZIP をダウンロードして、SDK を手動で追加することもできます。

{% tabs local %}
{% tab ジオフェンス無効 %}
ロケーションコレクションとジオフェンスを使用する予定がない場合は、GitHub の `master` ブランチを使用してください。

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#master
```
{% endtab %}

{% tab ジオフェンス有効 %}
位置情報の収集とジオフェンスの使用を計画している場合は、GitHub の `geofence-branch` を使用します。

```bash
cordova plugin add https://github.com/braze-inc/braze-cordova-sdk#geofence-branch
```
{% endtab %}
{% endtabs %}

{% alert tip %}
ステップ 1 を繰り返すことで、いつでも `master` と `geofence-branch` を切り替えることができます。
{% endalert %}

### ステップ 2:プロジェクトを構成する

次に、プロジェクトの `config.xml` ファイル内の `platform` 要素に次の環境設定を追加します。

{% tabs %}
{% tab ios %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.ios_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}

{% tab Android %}
```xml
<preference name="com.braze.api_key" value="BRAZE_API_KEY" />
<preference name="com.braze.android_api_endpoint" value="CUSTOM_API_ENDPOINT" />
```
{% endtab %}
{% endtabs %}

次のように置き換えます。

| 値                 | 説明                                                                                                                      |
|-----------------------|----------------------------------------------------------------------------------------------------------------------------------|
| `BRAZE_API_KEY`       | あなたの[Braze REST APIキー]({{site.baseurl}}/user_guide/administrative/app_settings/api_settings_tab/#rest-api-keys)。              |
| `CUSTOM_API_ENDPOINT` | カスタムAPIエンドポイント。このエンドポイントは、Brazeダッシュボードの正しいアプリグループにBrazeインスタンスデータをルーティングするために使用されます。 |

`config.xml` ファイルの `platform` 要素は次のようになります。

{% tabs %}
{% tab ios %}
```xml
<platform name="ios">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.ios_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}

{% tab Android %}
```xml
<platform name="android">
    <preference name="com.braze.api_key" value="BRAZE_API_KEY" />
    <preference name="com.braze.android_api_endpoint" value="sdk.fra-01.braze.eu" />
</platform>
```
{% endtab %}
{% endtabs %}

## 自動セッショントラッキングの無効化 (Android のみ)

デフォルトでは、Android Cordova プラグインは自動的にセッションを追跡します。自動セッショントラッキングを無効にするには、プロジェクトの `config.xml` ファイル内の `platform` 要素に次の設定を追加します。

```xml
<platform name="android">
    <preference name="com.braze.android_disable_auto_session_tracking" value="true" />
</platform>
```

トラッキングセッションを再開するには、`BrazePlugin.startSessionTracking()` を呼び出します。次回の `Activity.onStart()` 以降に開始されたセッションのみが追跡されることに注意してください。
