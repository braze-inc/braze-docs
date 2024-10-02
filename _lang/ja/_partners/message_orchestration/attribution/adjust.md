---
nav_title: 調整する
article_title: 調整する
alias: /partners/adjust/
description: "この参考記事では、Brazeとモバイルアトリビューション・アナリティクス企業のAdjustとの提携について概説している。Adjustは、オーガニックインストール以外のアトリビューションデータをインポートし、ライフサイクルキャンペーン内でよりインテリジェントにセグメントすることを可能にする。"
page_type: partner
search_tag: Partner

---

# 調整する

> [Adjustは](https://www.adjust.com/)、広告ソースのアトリビューションと高度なアナリティクスを組み合わせ、ビジネスインテリジェンスの包括的なイメージを提供するモバイルアトリビューションとアナリティクスの企業である。

BrazeとAdjustの統合により、オーガニックインストール以外のアトリビューションデータをインポートし、ライフサイクルキャンペーン内でよりインテリジェントにセグメント化できる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| 口座を調整する | このパートナーシップを利用するにはアジャスト・アカウントが必要だ。 |
| iOSまたはAndroidアプリ | この統合はiOSとAndroidアプリをサポートしている。プラットフォームによっては、アプリケーションにコード・スニペットが必要になるかもしれない。これらの要件の詳細は、統合プロセスのステップ1に記載されている。 |
| SDKを調整する | 必要なBraze SDKに加えて、[Adjust SDKを](https://docs.adjust.com/en/getting-started/#integrate-the-adjust-sdk)インストールする必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:デバイスIDをマップする

#### Android

Androidアプリをお持ちの場合は、Adjustに固有のBrazeデバイスIDを渡す必要がある。このIDはAdjust SDKの`addSessionPartnerParameter()` 。でSDKを初期化する前に、以下のコード・スニペットをインクルードする必要がある。 `Adjust.onCreate.`

```
Adjust.addSessionPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the IDFV as the primary identifier to match iOS attribution data. It is not necessary for Braze customers using Objective-C to fetch the Braze `device_id` and sent to Adjust upon install as there will be no disruption of service. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift in order to pass the Braze `device_id` to Adjust upon app install in order for Braze to appropriately match iOS attributions.
--->

{% tabs ローカル %}
{% tab Objective-C %}

iOSアプリがあれば、IDFVはAdjustによって収集され、Brazeに送信される。このIDは、Brazeで一意のデバイスIDにマッピングされる。

[iOS14アップグレードガイドに]({{site.baseurl}}/android_12/)記載されているように、BrazeでIDFAを収集している場合、BrazeはオプトインしたユーザーのIDFA値を引き続き保存する。そうでない場合、IDFVはユーザーをマップするための予備識別子として使用される。

{% endtab %}
{% tab スウィフト %}

iOSアプリの場合、`useUUIDAsDeviceId` フィールドを`false` に設定することで、IDFVを収集することができる。設定されていない場合、iOSのアトリビューションはAdjustからBrazeに正確にマッピングされない可能性が高い。詳細については、「[IDFV の収集]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/)」を参照してください。

{% endtab %}
{% endtabs %}

{% alert note %}
AdjustからBrazeにインストール後のイベントを送信する予定がある場合は、次のことが必要になる：<br><br>1) Adjust SDKのセッションおよびイベントパラメータに`external_id` 。収益イベント転送のためには、`product_id` をイベントのパラメータとして設定する必要もある。イベント転送のためのパートナーパラメータの定義については、[Adjustのドキュメントを](https://github.com/adjust/sdks)参照のこと。<br><br>2) Adjustに入力する新しいAPIキーを生成する。これは、BrazeダッシュボードのAdjust partnerページにある**Generate API Key**ボタンを選択することで行うことができる。
{% endalert %}

### ステップ2:Brazeデータインポートキーを取得する

Brazeで、**Integrations**>**Technology Partnersに**移動し、**Adjustを**選択する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。鍵の生成後、新しい鍵を作成したり、既存の鍵を無効にしたりすることができる。データインポートキーとRESTエンドポイントは、Adjustのダッシュボードでポストバックを設定する際に次のステップで使用される。<br><br>![この画像は、Adjustテクノロジーページにある「Data Import for Install Attribution」ボックスを示している。このボックスには、データ・インポート・キーとRESTエンドポイントが表示される。][1]{: style="max-width:90%;"}

### ステップ3:アジャストでブレイズを設定する

1. Adjustのダッシュボードで、**App Settingsに**移動し、**Partner Setupに**移動し、**Add Partnersに**移動する。
2. **Braze（旧Appboy）を**選択し、データインポートキーとBraze RESTエンドポイントを指定する。
3. **保存して閉じる**」をクリックする。

### ステップ4:統合を確認する

BrazeがAdjustからアトリビューションデータを受信すると、BrazeのAdjustテクノロジーパートナーページのステータス接続インジケーターが "Not Connected "から "Connected "に変わる。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、帰属するインストールに関するデータを受け取るまでは起こらないことに注意してほしい。Adjustのポストバックから除外されるべきオーガニックインストールは、我々のAPIによって無視され、接続が成功したかどうかを判断する際にカウントされない。

## 利用可能なデータフィールド

提案されたとおりにインテグレーションを設定すると、BrazeはAdjustのデータを次の表のようにセグメントフィルターにマッピングする。

| データフィールドを調整する | ブレージングセグメントフィルター |
| --- | --- |
| `{network_name}` | 帰属元 |
| `{campaign_name}` | 帰属キャンペーン |
| `{adgroup_name}` | 帰属アドグループ |
| `{creative_name}` | 帰属広告 |
{: .reset-td-br-1 .reset-td-br-2}

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできない。これらのメディアソースは、そのパートナーが帰属データを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできない。

## BrazeでクリックトラッキングURLを調整する（オプション）

Brazeのキャンペーンでクリック追跡リンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できる。その結果、マーケティング活動をより効果的に測定できるようになり、ROIを最大化するためにどこにリソースを投資すべきか、データに基づいた意思決定ができるようになる。

クリックトラッキング・リンクの調整を始めるには、[ドキュメントを](https://help.adjust.com/tracking/attribution/tracker-urls)参照すること。BrazeのキャンペーンにAdjustクリックトラッキングリンクを直接挿入することができる。Adjustは、[確率的アトリビューション手法を使って](https://www.adjust.com/blog/attribution-compatible-with-ios14/)、リンクをクリックしたユーザーをアトリビュートする。Brazeキャンペーンからのアトリビューションの精度を高めるために、Adjustトラッキングリンクにデバイス識別子を付加することをお勧めする。これにより、リンクをクリックしたユーザーの属性が決定的になる。

{% tabs ローカル %}
{% tab アンドロイド %}
Androidの場合、Brazeは[Google Advertising ID収集（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection)）にオプトインすることができる。GAIDはAdjust SDKとの統合によってネイティブに収集される。以下のリキッドロジックを利用することで、GAIDをAdjustクリックトラッキングリンクに含めることができる：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAdjustはSDKインテグレーションを通じてIDFVをネイティブに自動収集する。これはデバイス識別子として使用できる。以下のリキッドロジックを利用することで、AdjustクリックトラッキングリンクにIDFVを含めることができる：

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
**この推奨は純粋にオプションである。**<br>
現在、クリックトラッキングのリンクにIDFVやGAIDなどのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Adjustは確率的モデリングによってこれらのクリックを識別することができる。
{% endalert %}

[1]: {% image_buster /assets/img/attribution/adjust.png %}
[2]: {% image_buster /assets/img/attribution/adjust2.png %}
