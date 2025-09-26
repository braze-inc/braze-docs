---
nav_title: Adjust
article_title: Adjust
alias: /partners/adjust/
description: "この参考記事では、Brazeとモバイルアトリビューション・アナリティクス企業のAdjustとの提携について概説している。Adjustは、オーガニックインストール以外のアトリビューションデータをインポートし、ライフサイクルキャンペーン内でよりインテリジェントにセグメントすることを可能にする。"
page_type: partner
search_tag: Partner

---

# Adjust

> [Adjust](https://www.adjust.com/) は、モバイルアトリビューションおよび分析を扱う企業です。広告ソースのアトリビューションと高度な分析を組み合わせ、総合的なビジネスインテリジェンスを提供しています。

_この統合は Adjust によって管理されます。_

## 統合について

BrazeとAdjustの統合により、オーガニックインストール以外のアトリビューションデータをインポートし、ライフサイクルキャンペーン内でよりインテリジェントにセグメント化できる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Adjust アカウント | このパートナーシップを活用するには、Adjust アカウントが必要です。 |
| iOSやAndroid アプリ | この統合では、iOS アプリと Android アプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| SDKを調整する | 必要な Braze SDK に加えて、[Adjust SDK](https://dev.adjust.com/en/sdk) をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:デバイスIDをマップする

#### Android

Androidアプリをお持ちの場合は、一意のBrazeデバイスIDをAdjustに渡す必要があります。この ID は、Adjust SDK の`addGlobalPartnerParameter()`メソッドで設定できます。`Adjust.initSdk.` で SDK を初期化する前に、次のコードスニペットを含める必要があります。

```
Adjust.addGlobalPartnerParameter("braze_device_id", Braze.getInstance(getApplicationContext()).getDeviceId()););
```

#### iOS

<!--
{% alert important %}
Prior to February 2023, our Adjust attribution integration used the IDFV as the primary identifier to match iOS attribution data. Braze customers don't need to use Objective-C to fetch the Braze `device_id` and send it to Adjust upon installation as there will be no service disruption. 
{% endalert%}

For those using the Swift SDK v5.7.0+, if you wish to continue using IDFV as the mutual identifier, you must ensure that the `useUUIDAsDeviceId` field is set to `false` so there is no disruption of the integration. 

If set to `true`, you must implement the iOS device ID mapping for Swift to pass the Braze `device_id` to Adjust upon app installation in order for Braze to match iOS attributions appropriately.
--->

{% tabs ローカル %}
{% tab Objective-C %}

iOSアプリがあれば、IDFVはAdjustによって収集され、Brazeに送信される。このIDは、Brazeで一意のデバイスIDにマッピングされる。

[iOS アップグレードガイド]({{site.baseurl}}/developer_guide/platforms/swift/ios_18/)で説明されているように、IDFA を Braze で収集している場合も、Braze はオプトインしたユーザーの IDFA 値を保存します。このようにしないと、ユーザーをマッピングするためのフォールバック識別子として IDFV が使用されます。

{% endtab %}
{% tab Swift %}

iOSアプリを使用している場合は、`useUUIDAsDeviceId` フィールドを`false` に設定することで、IDFV を収集することを選択できます。設定されていない場合、iOSのアトリビューションはAdjustからBrazeに正確にマッピングされない可能性が高い。詳細については、「[IDFV の収集]({{site.baseurl}}/developer_guide/analytics/managing_data_collection/?sdktab=swift)」を参照してください。

{% endtab %}
{% endtabs %}

{% alert note %}
AdjustからBrazeにインストール後のイベントを送信する予定がある場合は、次のことが必要になる：<br><br>1) Adjust SDK 内でセッションおよびイベントパラメーターとして `external_id` を必ず追加します。収益イベント転送では、イベントのパラメーターとして `product_id` も設定する必要があります。イベント転送のためのパートナーパラメーターの定義の詳細については、[Adjust のドキュメント](https://github.com/adjust/sdks)を参照してください。<br><br>2) Adjust に入力する新しい API キーを生成します。これを行うには、Braze ダッシュボードの Adjust パートナーページにある [**API キーを生成**] ボタンを選択します。
{% endalert %}

### ステップ2:Braze データインポートキーを取得する

Brazeで [**統合**] > [**テクノロジーパートナー**] に移動し、[**Adjust**] を選択します。 

ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、Adjustのダッシュボードでポストバックを設定する際に次のステップで使用される。<br><br>![Adjust テクノロジーページにある「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーと REST エンドポイントが表示されます。]({% image_buster /assets/img/attribution/adjust.png %}){: style="max-width:90%;"}

### ステップ3:Adjust で Braze を設定する

1. Adjust のダッシュボードで [**App Settings**]、[**Partner Setup**]、[**Add Partners**] の順に移動します。
2. [**Braze (formerly Appboy)**] を選択し、データインポートキーと Braze REST エンドポイントを入力します。
3. [**Save & Close**] をクリックします。

### ステップ4:統合を確認する

Braze が Adjust からアトリビューションデータを受信すると、Braze の Adjust テクノロジーパートナーページのステータス接続インジケーターが [接続されていません] から [接続済み] に変わります。最後の成功したリクエストのタイムスタンプも含まれます。 

これは、紐づけられるインストールに関するデータを受け取るまでは発生しないことに注意してください。Adjust のポストバックから除外する必要があるオーガニックインストールは、Braze の API では無視され、接続の確立が成功したかどうかを判断する際に考慮されません。

## 利用可能なデータフィールド

提案されたとおりに統合を設定すると、次の表に示すように、Braze により Adjust のデータがセグメントフィルターにマッピングされます。

| データフィールドを調整する | Braze セグメントフィルター |
| --- | --- |
| `{network_name}` | 紐づけられるソース |
| `{campaign_name}` | 紐づけられるキャンペーン |
| `{adgroup_name}` | 紐づけられる広告グループ |
| `{creative_name}` | 紐づけられる広告 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーはそのデータをBrazeに送信することができません。

## BrazeでクリックトラッキングURLを調整する（オプション）

Brazeキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールと再エンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定できるようになり、ROI を最大化するためにどこにリソースを投資すべきかについて、データに基づいた意思決定ができるようになります。

クリックトラッキング・リンクの調整を始めるには、[ドキュメントを](https://help.adjust.com/tracking/attribution/tracker-urls)参照すること。BrazeのキャンペーンにAdjustクリックトラッキングリンクを直接挿入することができる。Adjustは、[確率的アトリビューション手法を使って](https://www.adjust.com/blog/attribution-compatible-with-ios14/)、リンクをクリックしたユーザーをアトリビュートする。Brazeキャンペーンからのアトリビューションの精度を高めるために、Adjustトラッキングリンクにデバイス識別子を付加することをお勧めする。これにより、リンクをクリックしたユーザーを決定論的に属性付けします。

{% tabs ローカル %}
{% tab Android %}
Androidの場合、Brazeを使用すると、顧客は[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/sdk_integration#google-advertising-id)にオプトインできます。GAID はまた、Adjust SDK 統合によってネイティブに収集されます。以下のリキッドロジックを利用することで、GAIDをAdjustクリックトラッキングリンクに含めることができる：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAdjustはSDKインテグレーションを通じてIDFVをネイティブに自動収集する。これはデバイスの識別子として使用できます。以下のリキッドロジックを利用することで、AdjustクリックトラッキングリンクにIDFVを含めることができる：

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
**この推奨事項は完全に任意です**<br>
現在、IDFV やGAID などのデバイス識別子をクリックトラッキングリンクで使用していない場合、または今後使用する予定がない場合でも、Adjust は確率モデリングを介してこれらのクリックを属性化できます。
{% endalert %}


