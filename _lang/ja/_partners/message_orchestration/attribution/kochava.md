---
nav_title: Kochava
article_title: Kochava
alias: /partners/kochava/
description: "このリファレンス記事では、Braze と Kochava のパートナーシップについて説明します。Kochava は、アトリビューションおよび分析インサイトを提供して、成長のためのデータの活用を支援するモバイルアトリビューションプラットフォームです。"
page_type: partner
search_tag: Partner

---

# Kochava

> [Kochavaは](https://www.kochava.com/)モバイルのアトリビューションと分析を提供し、データを成長のために活用する手助けをする。Kochava Audience Platform では、アプリキャンペーンの計画、ターゲット、アクティベーション、測定、最適化を実施できます。

_この統合は Kochava によって管理されます。_

## 統合について

BrazeとKochavaの統合により、アトリビューションデータをBrazeに送信することで、インストール、アプリ内アクティビティなどを促進するキャンペーンをよりよく理解し、キャンペーンの全体的な理解を深めることができます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Kochavaアカウント | このパートナーシップを活用するには、Kochava アカウントが必要です。 |
| iOSやAndroid アプリ | この統合では、iOS アプリと Android アプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| Kochava SDK | 必須のBraze SDKに加えて、[Kochava SDK](https://support.kochava.com/sdk-integration/)をインストールする必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:ユーザーIDをマップする

#### Android

[Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3)SDKは、セッション開始時にGUID（Globally Unique Identifier）をBraze IDとして生成する。この識別子をKochava`IdentityLink` メソッドに渡すことで、Brazeはデータを正しいユーザープロファイルに照合することができる。以下の方法でBraze IDを取得する：

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
2023年2月以前は、Kochavaのアトリビューション統合は、iOSのアトリビューションデータを照合するための主要識別子としてIDFV（Identifier for Vendor）を使用していた。Objective-Cを使用しているBraze顧客は、サービスの中断がないため、インストール時にBraze`device_id` を取得し、Kochavaに送信する必要はない。
{% endalert%}

Swift SDK v5.7.0+ を使用しているお客様は、相互識別子として IDFV を引き続き使用するには、`useUUIDAsDeviceId` フィールドが `false` に設定されていることを確認する必要があります。これにより、統合が中断されることがなくなります。`true` に設定している場合、Brazeが iOS アトリビューションを適切に照合できるように、アプリのインストール時にKochava に Braze `device_id` を渡すために、Swift用の iOS デバイス ID マッピングを実装する必要があります。

Braze には、同じ値を生成する2つのAPI があります。1つは完了ハンドラを使用し、もう1つは新しいSwift 同時実行サポートを使用します。次のコードスニペットをKochavaの[iOS SDK](https://support.kochava.com/sdk-integration/ios-sdk-integration/)の指示に従って修正する必要があることに注意してください。その他のヘルプについては、Kochavaサポートに問い合わせること。

##### 完了ハンドラ
```
AppDelegate.braze?.deviceId(completion: { deviceId in
  // Use `deviceId`
})
```
##### SWIFTコンカレンシー
```
let deviceId = await AppDelegate.braze?.deviceId()
```

### ステップ2:Braze データインポートキーを取得する

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**Kochava** を選択します。 

ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、Kochavaのダッシュボードでポストバックを設定する次のステップで使用されます。<br><br>![この画像は、Kochavaテクノロジーページにある「インストールアトリビューションのためのデータインポート」ボックスを示しています。このボックスには、データインポートキーと REST エンドポイントが表示されている。]({% image_buster /assets/img/attribution/kochava.png %}){: style="max-width:90%;"}

### ステップ3:Kochavaからのポストバックを設定する

Kochava ダッシュボードに[ポストバックを追加します](https://support.kochava.com/campaign-management/create-a-kochava-certified-postback)。Braze のダッシュボードで見つけたデータインポートキーと REST エンドポイントの入力を求められます。

### ステップ 4: 統合を確認する

Braze が Kochava からアトリビューションデータを受信すると、Braze の Kochava テクノロジーパートナーページのステータス接続インジケーターが [接続されていません] から [接続済み] に変わります。最後の成功したリクエストのタイムスタンプも含まれます。 

これは、紐づけられるインストールに関するデータを受け取るまでは発生しないことに注意してください。オーガニックインストールはKochavaポストバックから除外する必要があり、当社のAPIによって無視され、接続が成功したかどうかを判断する際にはカウントされません。

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーはそのデータをBrazeに送信することができません。

## BrazeでのKochavaクリックトラッキングURL（オプション）

Brazeキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールと再エンゲージメントを促進しているかを簡単に確認できます。その結果、マーケティング活動をより効果的に測定できるようになり、ROI を最大化するためにどこにリソースを投資すべきかについて、データに基づいた意思決定ができるようになります。

Kochavaのクリックトラッキングリンクを開始するには、[ドキュメント](https://support.kochava.com/reference-information/attribution-overview/)をご覧ください。BrazeキャンペーンにKochavaクリックトラッキングリンクを直接挿入できます。Kochavaはその後、[確率的アトリビューション方法論](https://www.kochava.com/getting-prepared-for-ios-14/)を使用して、リンクをクリックしたユーザーを属性します。Brazeキャンペーンからのアトリビューションの精度を向上させるために、Kochavaトラッキングリンクにデバイス識別子を追加することをお勧めします。これにより、リンクをクリックしたユーザーを決定論的に属性付けします。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeを使用すると、顧客は[Google広告IDコレクション（GAID）]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)にオプトインできます。GAID はまた、Kochava SDK統合によってネイティブに収集されます。次のLiquidロジックを利用して、KochavaクリックトラッキングリンクにGAIDを含めることができます:
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとKochavaの両方が、SDK統合を通じてネイティブにIDFVを自動的に収集します。これはデバイスの識別子として使用できます。次のLiquidロジックを利用して、KochavaクリックトラッキングリンクにIDFVを含めることができます:

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
現在、クリックトラッキングリンクにIDFVやGAIDなどのデバイス識別子を使用していない場合、または将来的に使用する予定がない場合でも、Kochavaは確率モデルを通じてこれらのクリックを属性付けすることができます。
{% endalert %}


