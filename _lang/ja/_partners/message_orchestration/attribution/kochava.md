---
nav_title: Kochava
article_title:Kochava
alias: /partners/kochava/
description:"この参考記事では、BrazeとモバイルアトリビューションプラットフォームKochavaの提携について概説している。"Brazeは、アトリビューションと分析インサイトを提供し、成長に向けてデータを活用できるよう支援する。
page_type: partner
search_tag:Partner

---

# Kochava

> Kochavaはモバイルのアトリビューションと分析を提供し、データを成長のために活用する手助けをする。Kochava Audience Platformは、アプリキャンペーンの計画、ターゲット設定、有効化、測定、最適化を可能にする。

BrazeとKochavaの統合は、アトリビューションデータをBrazeに送信し、どのキャンペーンがインストールやアプリ内アクティビティなどを促進しているかをよりよく理解することで、キャンペーンをより総合的に理解するのに役立つ。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Kochavaアカウント | このパートナーシップを利用するにはKochavaアカウントが必要だ。 |
| iOSまたはAndroidアプリ | この統合はiOSとAndroidアプリをサポートしている。プラットフォームによっては、アプリケーションにコード・スニペットが必要な場合がある。これらの要件の詳細は、統合プロセスのステップ1に記載されている。 |
| Kochava SDK | 必要なBraze SDKに加えて、[Kochava SDKを](https://support.kochava.com/sdk-integration/)インストールする必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:ユーザーIDをマップする

#### Android

[Android](https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3)SDKはセッション開始時にBraze IDとしてGUIDを生成する。これは、Kochava`IdentityLink` メソッドに渡すことを推奨する識別子で、これによりBrazeは正しいユーザープロファイルにデータを照合することができる。Braze IDは以下の方法で取得できる：

```java
Apppboy.getInstance(context).getDeviceId();
```

#### iOS

{% alert important %}
2023年2月以前は、Kochavaのアトリビューション統合は、iOSのアトリビューションデータを照合するための主要識別子としてIDFVを使用していた。Objective-Cを使用しているBraze顧客は、サービスの中断がないため、インストール時にBraze`device_id` を取得し、Kochavaに送信する必要はない。
{% endalert%}

Swift SDK v5.7.0+を使用している場合、相互識別子としてIDFVを引き続き使用したい場合は、`useUUIDAsDeviceId` フィールドが`false` に設定されていることを確認する必要があるため、統合が中断されることはない。`true` に設定した場合、BrazeがiOSアトリビューションと適切に一致するように、アプリインストール時にKochavaにBraze`device_id` を渡すために、Swift用のiOSデバイスIDマッピングを実装する必要がある。

Brazeには、同じ値を生成する2つのAPIがあり、1つは完了ハンドラで、もう1つはSwiftの新しい同時実行サポートを使用している。Kochavaの[iOS SDKの](https://support.kochava.com/sdk-integration/ios-sdk-integration/)指示に合わせるために、以下のコード・スニペットを修正する必要があることに注意。その他のサポートについては、Kochavaサポートに問い合わせること。

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

### ステップ2:Brazeデータインポートキーを取得する。

Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**Kochavaを**選択する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合**」の下に**テクノロジーパートナーが**ある。
{% endalert %}

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。鍵の生成後、新しい鍵を作成したり、既存の鍵を無効にしたりすることができる。データ・インポート・キーとRESTエンドポイントは、Kochavaのダッシュボードでポストバックを設定する際、次のステップで使用される。<br><br>![この画像写真は、Kochavaテクノロジーページにある「インストールアトリビューション用データインポート」ボックスを示している。このボックスには、データ・インポート・キーとRESTエンドポイントが表示される。][4]{: style="max-width:90%;"}

### ステップ3:Kochavaからのポストバック設定

Kochavaダッシュボードに[ポストバックを][18]追加する。Brazeのダッシュボードで見つけたデータインポートキーとRESTエンドポイントの入力を求められる。

### ステップ 4:統合を確認する

BrazeがKochavaからアトリビューションデータを受信すると、BrazeのKochavaテクノロジーパートナーページのステータス接続インジケーターが「未接続」から「接続済み」に変わる。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、インストールアトリビューションに関するデータを受け取るまでは起こらないことに注意してほしい。Kochavaのポストバックから除外されるべきオーガニック・インストールは、APIによって無視され、接続が成功したかどうかを判断する際にカウントされない。

## FacebookとX（旧Twitter）のアトリビューションデータ

FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて入手することはできない。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、当社のパートナーはそのデータをBrazeに送信することができない。

## BrazeのKochavaクリックトラッキングURL（オプション）

Brazeキャンペーンでクリックトラッキングリンクを使用すると、どのキャンペーンがアプリのインストールやリエンゲージメントを促進しているかを簡単に確認できる。その結果、マーケティング活動をより効果的に測定できるようになり、ROIを最大化するためにどこにリソースを投資すべきか、データドリブン型の意思決定ができるようになる。

Kochavaのクリック・トラッキング・リンクを使い始めるには、[ドキュメントを](https://support.kochava.com/reference-information/attribution-overview/)参照のこと。Kochavaクリック追跡リンクをBrazeキャンペーンに直接挿入することができる。Kochavaは、[確率的アトリビューション手法を使って](https://www.kochava.com/getting-prepared-for-ios-14/)、リンクをクリックしたユーザーの属性を決定する。Brazeキャンペーンからのアトリビューションの精度を高めるために、Kochavaトラッキングリンクにデバイス識別子を付加することをお勧めする。これにより、リンクをクリックしたユーザーの属性が決定的になる。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeは顧客が[Google Advertising ID収集（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)）にオプトインできるようにしている。GAIDはKochava SDKとの統合によってネイティブに収集される。以下のLiquidロジックを利用することで、Kochavaのクリック追跡リンクにGAIDを含めることができる：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとKochavaの両方が、SDKの統合を通じてネイティブにIDFVを自動的に収集する。これはデバイス識別子として使用できる。以下のLiquidロジックを利用することで、Kochavaのクリック追跡リンクにIDFVを含めることができる：

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
現在、クリック追跡リンクにIDFVやGAIDのようなデバイス識別子を使用していない場合、または今後使用する予定がない場合でも、Kochavaは確率的モデリングにより、これらのクリックをアトリビューションすることができる。
{% endalert %}


[18]: https://support.kochava.com/campaign-management/create-a-kochava-certified-postback "Kochavaポストバック"
[29]: https://support.kochava.com/sdk-integration/sdk-kochavatracker-android/class-tracker?scrollto=marker_3
[30]: https://support.kochava.com/sdk-integration/windows-and-xbox-one-sdk-integration?scrollto=marker_8
[4]: {% image_buster /assets/img/attribution/kochava.png %}
