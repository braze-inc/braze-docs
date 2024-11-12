---
nav_title: 調整する
article_title: 調整する
alias: /partners/adjust/
description: "この参考記事では、Brazeとモバイルアトリビューション・アナリティクス企業のAdjustとの提携について概説している。Adjustは、オーガニックインストール以外のアトリビューションデータをインポートし、ライフサイクルキャンペーン内でよりインテリジェントにセグメントすることを可能にする。"
page_type: partner
search_tag: Partner

---

# 調整する

> [Adjust](https://www.adjust.com/) は、モバイルアトリビューションおよび分析を扱う企業です。広告ソースのアトリビューションと高度な分析を組み合わせ、総合的なビジネスインテリジェンスを提供しています。

BrazeとAdjustの統合により、オーガニックインストール以外のアトリビューションデータをインポートし、ライフサイクルキャンペーン内でよりインテリジェントにセグメント化できる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Adjust アカウント | このパートナーシップを活用するには、Adjust アカウントが必要です。 |
| iOSまたはAndroidアプリ | この統合はiOSとAndroidアプリをサポートしている。プラットフォームによっては、アプリケーションにコード・スニペットが必要になるかもしれない。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| SDKを調整する | 必要な Braze SDK に加えて、[Adjust SDK](https://docs.adjust.com/en/getting-started/#integrate-the-adjust-sdk) をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:デバイスIDをマップする

#### Android

Androidアプリをお持ちの場合は、Adjustに固有のBrazeデバイスIDを渡す必要がある。この ID は、Adjust SDK の`addSessionPartnerParameter()`メソッドで設定できます。`Adjust.onCreate.` で SDK を初期化する前に、次のコードスニペットを含める必要があります。

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

[iOS14アップグレードガイドに]({{site.baseurl}}/android_12/)記載されているように、BrazeでIDFAを収集している場合、BrazeはオプトインしたユーザーのIDFA値を引き続き保存する。このようにしないと、ユーザーをマッピングするためのフォールバック識別子として IDFV が使用されます。

{% endtab %}
{% tab Swift %}

iOSアプリを使用している場合は、`useUUIDAsDeviceId` フィールドを`false` に設定することで、IDFV を収集することを選択できます。設定されていない場合、iOSのアトリビューションはAdjustからBrazeに正確にマッピングされない可能性が高い。詳細については、「[IDFV の収集]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/swift_idfv/)」を参照してください。

{% endtab %}
{% endtabs %}

{% alert note %}
AdjustからBrazeにインストール後のイベントを送信する予定がある場合は、次のことが必要になる：<br><br>1) Adjust SDK 内でセッションおよびイベントパラメーターとして `external_id` を必ず追加します。収益イベント転送では、イベントのパラメーターとして `product_id` も設定する必要があります。イベント転送のためのパートナーパラメーターの定義の詳細については、[Adjust のドキュメント](https://github.com/adjust/sdks)を参照してください。<br><br>2) Adjust に入力する新しい API キーを生成します。これを行うには、Braze ダッシュボードの Adjust パートナーページにある \[**API キーを生成**] ボタンを選択します。
{% endalert %}

### ステップ2:Brazeデータインポートキーを取得する

Brazeで \[**統合**] > \[**テクノロジーパートナー**] に移動し、\[**Adjust**] を選択します。 

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、\[**テクノロジーパートナー**] は \[**統合**] にあります。
{% endalert %}

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、Adjustのダッシュボードでポストバックを設定する際に次のステップで使用される。<br><br>![Adjust テクノロジーページにある「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーと REST エンドポイントが表示されている。][1]{: style="max-width:90%;"}

### ステップ3:Adjust で Braze を設定する

1. Adjust のダッシュボードで \[**App Settings**]、\[**Partner Setup**]、\[**Add Partners**] の順に移動します。
2. \[**Braze (formerly Appboy)**] を選択し、データインポートキーと Braze REST エンドポイントを入力します。
3. \[**Save & Close**] をクリックします。

### ステップ4:統合を確認する

Braze が Adjust からアトリビューションデータを受信すると、Braze の Adjust テクノロジーパートナーページのステータス接続インジケーターが \[接続されていません] から \[接続済み] に変わります。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、紐づけられるインストールに関するデータを受け取るまでは発生しないことに注意してください。Adjust のポストバックから除外する必要があるオーガニックインストールは、Braze の API では無視され、接続の確立が成功したかどうかを判断する際に考慮されません。

## 利用可能なデータフィールド

提案されたとおりに統合を設定すると、次の表に示すように、Braze により Adjust のデータがセグメントフィルターにマッピングされます。

| データフィールドを調整する | Braze セグメントフィルター |
| --- | --- |
| `{network_name}` | 紐づけられるソース |
| `{campaign_name}` | 紐づけられるキャンペーン |
| `{adgroup_name}` | 紐づけられる広告グループ |
| `{creative_name}` | 紐づけられる広告 |
{: .reset-td-br-1 .reset-td-br-2}

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできない。これらのメディアソースは、そのパートナーが帰属データを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできない。

## BrazeでクリックトラッキングURLを調整する（オプション）

Brazeのキャンペーンでクリック追跡リンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できる。その結果、マーケティング活動をより効果的に測定できるようになり、ROI を最大化するためにどこにリソースを投資すべきかについて、データに基づいた意思決定ができるようになります。

クリックトラッキング・リンクの調整を始めるには、[ドキュメントを](https://help.adjust.com/tracking/attribution/tracker-urls)参照すること。BrazeのキャンペーンにAdjustクリックトラッキングリンクを直接挿入することができる。Adjustは、[確率的アトリビューション手法を使って](https://www.adjust.com/blog/attribution-compatible-with-ios14/)、リンクをクリックしたユーザーをアトリビュートする。Brazeキャンペーンからのアトリビューションの精度を高めるために、Adjustトラッキングリンクにデバイス識別子を付加することをお勧めする。これにより、リンクをクリックしたユーザーの属性が決定的になる。

{% tabs ローカル %}
{% tab Android %}
Android の場合、Braze ではお客様が [Google 広告 ID (GAID) 収集]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection)にオプトインできます。GAID はまた、Adjust SDK 統合によってネイティブに収集されます。以下のリキッドロジックを利用することで、GAIDをAdjustクリックトラッキングリンクに含めることができる：
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
**この推奨事項の適用は完全に任意です。**<br>
現在、クリックトラッキングのリンクにIDFVやGAIDなどのデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Adjustは確率的モデリングによってこれらのクリックを識別することができる。
{% endalert %}

[1]: {% image_buster /assets/img/attribution/adjust.png %}
[2]: {% image_buster /assets/img/attribution/adjust2.png %}
