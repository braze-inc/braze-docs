---
nav_title: AppsFlyer
article_title: AppsFlyer
alias: /partners/appsflyer/
description: "この参考記事では、アプリの分析と最適化を支援するモバイルマーケティング分析とアトリビューションプラットフォームであるBrazeとAppsFlyerのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner

---

# AppsFlyer

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> AppsFlyerはモバイルマーケティング分析とアトリビューションプラットフォームで、マーケティング分析、モバイルアトリビューション、ディープリンクを通じてアプリの分析と最適化を支援する。

BrazeとAppsFlyerの統合により、AppsFlyerのモバイルインストールアトリビューションデータを活用することで、より全体的なキャンペーンを最適化し、構築する方法をよりよく理解することができる。 

また、[AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/appsflyer_audiences/)統合により、AppsFlyerのオーディエンス（コホート）を直接Brazeに渡すことができ、適切なタイミングで適切なユーザーをターゲットにした強力な顧客エンゲージメントキャンペーンを作成できる。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| AppsFlyerアカウント | このパートナーシップを利用するには、AppsFlyerアカウントが必要である。 |
| iOSまたはAndroidアプリ | この統合はiOSとAndroidアプリをサポートしている。プラットフォームによっては、アプリケーションにコード・スニペットが必要になるかもしれない。これらの要件の詳細は、統合プロセスのステップ1に記載されている。 |
| AppsFlyer SDK | 必要なBraze SDKに加えて、[AppsFlyer SDKを](https://dev.appsflyer.com/hc/docs/getting-started)インストールする必要がある。
| Eメールドメインのセットアップ完了 | Brazeのオンボーディング時に、[IPとドメインのセットアップステップを]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)完了していること。 |
| SSL証明書 | [SSL証明書が]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate)設定されていなければならない。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:マップ・デバイスID

#### Android

Androidアプリをお持ちの場合、AppsFlyerに固有のBrazeデバイスIDを渡す必要がある。 

Braze SDKが起動した後、AppsFlyer SDKの初期化コードの前。詳細はAppsFlyer[Android SDKインテグレーションガイドを](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk)参照のこと。

```java
HashMap<String, Object> customData = new HashMap<String,Object>();
String deviceId =(Braze.getInstance(MyActivity.this).getDeviceId());
customData.put("brazeCustomerId", deviceId);
AppsFlyerLib.setAdditionalData(customData);
```

#### iOS

{% alert important %}
2023年2月以前は、AppsFlyerのアトリビューション統合は、iOSアトリビューションデータを照合するための主要な識別子としてIDFVを使用していた。Objective-Cを使用しているBrazeの顧客が、インストール時にBraze`device_id` を取得し、AppsFlyerに送信する必要はない。
{% endalert%}

Swift SDK v5.7.0+を使用している場合、相互識別子としてIDFVを引き続き使用したい場合は、`useUUIDAsDeviceId` フィールドが`false` に設定されていることを確認し、統合が中断されないようにする必要がある。 

`true` に設定した場合、BrazeがiOSアトリビュートと適切に一致するように、アプリインストール時にAppsFlyerにBraze`device_id` を渡すために、Swift用のiOSデバイスIDマッピングを実装する必要がある。

{% tabs ローカル %}
{% tab Objective-C %}

```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[braze deviceIdWithCompletion:^(NSString * _Nonnull brazeDeviceId) {
    NSLog(@">>[BRZ]: %@", brazeDeviceId);
    [[AppsFlyerLib shared] setAdditionalData:@{
        @"brazeDeviceId": brazeDeviceId
    }];
}];
```

{% endtab %}
{% tab スウィフト %}

##### スイフト完了ハンドラ
```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
braze.deviceId {
    brazeDeviceId in
    AppsFlyerLib.shared().customData = ["brazeDeviceId": brazeDeviceId]
}
```
##### 迅速な対応
```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
let brazeDeviceId = await braze.deviceId()
AppsFlyerLib.shared().customData = ["brazeDeviceId": brazeDeviceId]
```

{% endtab %}
{% endtabs %}

#### Unity

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```

### ステップ2:Brazeデータインポートキーを取得する

Brazeで、**Partner Integrations**>**Technology Partnersに**移動し、**AppsFlyerを**選択する。 

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**統合」の**下に**テクノロジー・パートナーが**ある。
{% endalert %}

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。鍵の生成後、新しい鍵を作成したり、既存の鍵を無効にしたりすることができる。データインポートキーとRESTエンドポイントは、AppsFlyerのダッシュボードでポストバックを設定する際に、次のステップで使用される。<br><br>![AppsFlyer Technologyページで利用可能な「Data Import for Install Attribution」ボックス。このボックスに含まれるのは、データ・インポート・キーとRESTエンドポイントである。][4]{: style="max-width:70%;"}

### ステップ3:AppsFlyerのダッシュボードでBrazeを設定する

1. AppsFlyerで、左バーの**Integrated Partners**ページに移動する。次に**Brazeを**検索し、Brazeのロゴをクリックして設定ウィンドウを開く。
2. **Integration "**タブで**"Activate Partner "**を選択する。
3. Brazeのダッシュボードで見つけたデータインポートキーとRESTエンドポイントを提供する。 
4. **Advanced Privacyを**オフに切り替え、設定を保存する。

これらの手順に関する追加情報は、\[AppsFlyer's documentation][16] に掲載されている。

### ステップ 4:統合を確認する

BrazeがAppsFlyerからアトリビューションデータを受信すると、BrazeのAppsFlyerテクノロジーパートナーページのステータス接続インジケータが「未接続」から「接続済み」に変わる。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、帰属するインストールに関するデータを受け取るまでは起こらないことに注意してほしい。AppsFlyerのポストバックから除外されるべきオーガニックインストールは、APIによって無視され、接続が正常に確立されたかどうかを判断する際にカウントされない。

### ステップ 5: ユーザー属性データを見る

#### 利用可能なデータフィールド

提案されたとおりに統合を構成したと仮定すると、Brazeはすべての非オーガニックインストールデータをセグメントフィルターにマッピングする。

| AppsFlyer データフィールド | ブレージングセグメントフィルター |
| -------------------- | --------------------- |
| `media_source` | 帰属元 |
| `campaign` | 帰属キャンペーン |
| `af_adset` | 帰属アドグループ |
| `af_ad` | 帰属広告 |
{: .reset-td-br-1 .reset-td-br-2}

ユーザーベースは、BrazeダッシュボードのInstall Attributionフィルタを使用して、アトリビューションデータによってセグメントすることができる。

![フィルターは4種類ある。1つ目は、"Install Attribution Source is network_val_0 "である。2つ目は、"Install Attribution Source is campaign_val_0 "である。3つ目は「アトリビューション・ソースのインストールはadgroup_val_0」である。4つ目は、「表示ソースをcreative_val_0に設定する」である。リストされたフィルターの横に、これらの属性ソースがどのようにユーザープロファイルに追加されるかを見ることができる。ユーザー情報ページの "Install Attribution "ボックスでは、Install Sourceはnetwork_val_0、campaignはcampaign_val_0などと表示される。][2]

さらに、特定のユーザーのアトリビューションデータは、Brazeダッシュボードの各ユーザーのプロフィールで見ることができる。

{% alert note %}
FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできない。これらのメディアソースは、そのパートナーが帰属データを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできない。
{% endalert %}

## AppsFlyerとメールサービスプロバイダを統合してディープリンクを実現する

AppsFlyerは、メールサービスプロバイダ（ESP）としてSendGridとSparkPostの両方と統合し、ディープリンクとクリックトラッキングをサポートする。以下の手順に従って、選択したESPと統合する。

{% alert tip %}
ディープリンク（アプリやウェブサイト内の特定のページや場所にユーザーを誘導するリンク）は、ユーザーに合わせてカスタマイズされたユーザー体験を作り出すために使用される。広く使用されている一方で、ユーザーデータの収集に使用されるもう一つの重要な機能であるクリックトラッキングでEメールによるディープリンクを使用する場合、問題が発生する可能性がある。これらの問題は、ESPがディープリンクをクリックを記録するドメインでラップし、元のリンクを壊してしまうことに起因する。そのため、ディープリンクをサポートするには、追加の設定が必要になる。AppsFlyerをSendGridまたはSparkPostと統合することで、これらの問題を回避できる。このトピックについては、[ユニバーサルリンクとアプリリンクで]({{site.baseurl}}/help/help_articles/email/universal_links/)詳しく説明している。
{% endalert %}

### ステップ1:AppsFlyerでOneLinkを設定する

1. AppsFlyerで、メールキャンペーン用のOneLinkテンプレートを選択する。テンプレートがユニバーサルリンク（iOS）またはアプリリンク（Android）をサポートしていることを確認する。 
2. OneLinkでディープリンクをサポートするようにアプリを設定する。OneLinkをサポートするアプリの設定の詳細については、[AppsFlyerのドキュメントを](https://dev.appsflyer.com/hc/docs/dl_work_flow#initial-setup)参照のこと。

### ステップ2:ユニバーサルリンクとApp Linksをサポートするようにアプリを設定する

ユニバーサルリンク（iOS）またはアプリリンク（Android）は、クリックすると指定されたアプリを開くことがデバイスのオペレーティングシステムによって許可されている。

ユニバーサルリンクとApp Linksをサポートするには、以下の手順を実行する。

{% tabs ローカル %}
{% tab センドグリッド %}
{% subtabs %}
{% subtab iOS %}
Apple App Site Association (AASA)のファイルホスティングを設定し、Eメールでユニバーサルリンクを有効にする。

1. 以下のいずれかの方法でAASAファイルを入手する：
    * ユニバーサルリンクでOneLinkを設定している場合、OneLinkに関連付けられたAASAファイルがすでにあるかもしれない。AASAファイルを入手するには、以下を実行する：
        * OneLinkテンプレートのOneLinkサブドメインをコピーする。テンプレートがユニバーサルリンクをサポートしていることを確認する。
        * それを以下のURLのプレースホルダーの代わりに貼り付ける： `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * AASAファイルをダウンロードするには、OneLinkのURLをブラウザのアドレスバーに貼り付け、**Enter**キーを押す。ファイルはあなたのコンピューターにダウンロードされ、テキストエディタを使ってその内容を開いて見ることができる。
    * [アップルのユニバーサルリンクに関するガイドでは](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content)、AASAファイルの作成方法が説明されている。
2. AASAファイルをクリック録音ドメインサーバーにホストする。ファイルは`click.example.com/.well-known/apple-app-site-association` というパスにホストされていなければならない。 

[SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links)用のAASAファイルを設定し、AASAファイルをホストするCDNサービスを設定する方法については、[SendGridのドキュメントを](https://docs.sendgrid.com/ui/sending-email/universal-links)参照のこと。

{% alert important %}
いったんAASAファイルがホストされると、OneLinkコンフィギュレーションを変更（修正または交換）する場合は、新しいAASAファイルを生成する必要がある。
{% endalert %}
{% endsubtab %}
{% subtab Android %}
デジタルアセットリンクファイルのホスティングを設定し、メール内のアプリリンクを有効にする。

1. 以下のいずれかの方法でデジタルアセットリンクファイルを入手する：
    * アプリリンクでOneLinkをセットアップしている場合、OneLinkに関連付けられているデジタルアセットリンクファイルがすでにあるかもしれない。このファイルを入手するには、以下のようにする：
        * OneLinkテンプレートのOneLinkサブドメインをコピーする。テンプレートがApp Linksをサポートしていることを確認する。
        * OneLinkのURLの最後に`/.well-known/assetlinks.json` 。
        * デジタルアセットリンクファイルをダウンロードするには、OneLinkのURLをブラウザのアドレスバーに貼り付け、**Enter**キーを押す。例えば、`https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json` 。ファイルはあなたのコンピューターにダウンロードされ、テキストエディタを使ってその内容を開いて見ることができる。
    * [AndroidのApp Linksガイドでは](https://developer.android.com/studio/write/app-link-indexing)、Digital Asset Linksファイルの作成方法を説明している。
2. デジタルアセットリンクファイルをクリックレコーディングドメインサーバーにホストする。ファイルは`click.example.com/.well-known/apple-app-site-association` というパスにホストされていなければならない。

[SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links)用のDigital Asset Linksファイルの設定方法と、Digital Asset LinksファイルをホストするCDNサービスの設定方法については、[SendGridのドキュメントを](https://docs.sendgrid.com/ui/sending-email/universal-links)参照のこと。

{% alert important %}
デジタルアセットリンクファイルがホスティングされると、OneLinkコンフィギュレーションを変更（修正または交換）する場合は、新しいファイルを生成する必要がある。
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab スパークポスト %}
{% subtabs %}
{% subtab iOS %}
#### ステップ 2a: AASAファイルのホスティングを設定する
Apple App Site Association (AASA)のファイルホスティングを設定し、Eメールでユニバーサルリンクを有効にする。

1. 以下のいずれかの方法でAASAファイルを入手する：
    * ユニバーサルリンクでOneLinkを設定している場合、OneLinkに関連付けられたAASAファイルがすでにあるかもしれない。AASAファイルを入手するには、以下を実行する：
        * OneLinkテンプレートのOneLinkサブドメインをコピーする。テンプレートがユニバーサルリンクをサポートしていることを確認する。
        * それを以下のURLのプレースホルダーの代わりに貼り付ける： `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * AASAファイルをダウンロードするには、OneLinkのURLをブラウザのアドレスバーに貼り付け、**Enter**キーを押す。ファイルはあなたのコンピューターにダウンロードされ、テキストエディタを使ってその内容を開いて見ることができる。
    * [アップルのユニバーサルリンクに関するガイドでは](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content)、AASAファイルの作成方法が説明されている。
2. AASAファイルをクリック録音ドメインサーバーにホストする。ファイルは`click.example.com/.well-known/apple-app-site-association` というパスにホストされていなければならない。 

[SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve)用のAASAファイルを設定し、カスタムリンクサブパスを設定する方法については、[SparkPostのドキュメントを](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve)参照のこと。

{% alert important %}
いったんAASAファイルがホストされると、OneLinkコンフィギュレーションを変更（修正または交換）する場合は、新しいAASAファイルを生成する必要がある。
{% endalert %}

#### ステップ 2b: クリック追跡ドメインをAASAファイルホストにリダイレクトする
[電子メールの設定]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)中に、DNSサーバーにCNAMEレコードを作成した。Brazeでクリックトラッキングドメインを確認した後、以下の手順を実行する。 

1. サブドメインをSparkPostドメインにリダイレクトするCNAMEレコードを削除する。
2. 上記で削除したレコードの代わりに、クリック追跡ドメインをアプリのAASAファイルをホストしているCDNにリダイレクトするCNAMEレコードを作成する。
{% endsubtab %}
{% subtab Android %}
#### ステップ 2a: デジタルアセットリンクのファイルホスティングを設定する
デジタルアセットリンクファイルのホスティングを設定し、メール内のアプリリンクを有効にする。

1. 以下のいずれかの方法でデジタルアセットリンクファイルを入手する：
    * アプリリンクでOneLinkをセットアップしている場合、OneLinkに関連付けられているデジタルアセットリンクファイルがすでにあるかもしれない。このファイルを入手するには、以下のようにする：
        * OneLinkテンプレートのOneLinkサブドメインをコピーする。テンプレートがApp Linksをサポートしていることを確認する。
        * OneLinkのURLの最後に`/.well-known/assetlinks.json` 。
        * デジタルアセットリンクファイルをダウンロードするには、OneLinkのURLをブラウザのアドレスバーに貼り付け、**Enter**キーを押す。例えば、`https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json` 。ファイルはあなたのコンピューターにダウンロードされ、テキストエディタを使ってその内容を開いて見ることができる。
    * [AndroidのApp Linksガイドでは](https://developer.android.com/studio/write/app-link-indexing)、Digital Asset Linksファイルの作成方法を説明している。
2. デジタルアセットリンクファイルをクリックレコーディングドメインサーバーにホストする。ファイルは`click.example.com/.well-known/apple-app-site-association` というパスにホストされていなければならない。

[SparkPost](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve)用のDigital Asset Linksファイルを設定し、カスタムリンクサブパスを設定する方法については、[SparkPostのドキュメントを](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve)参照のこと。

{% alert important %}
デジタルアセットリンクファイルがホスティングされると、OneLinkコンフィギュレーションを変更（修正または交換）する場合は、新しいファイルを生成する必要がある。
{% endalert %}

#### ステップ 2b: クリックトラッキングドメインをデジタルアセットリンクファイルホストにリダイレクトする
[電子メールの設定]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)中に、DNSサーバーにCNAMEレコードを作成した。Brazeでクリックトラッキングドメインを確認した後、以下の手順を実行する。 

1. サブドメインをSparkPostドメインにリダイレクトするCNAMEレコードを削除する。
2. 上記で削除したレコードの代わりに、アプリのDigital Asset LinksファイルをホストしているCDNにクリック追跡ドメインをリダイレクトするCNAMEレコードを作成する。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ3:ディープリンクをサポートするようにAppsFlyer SDKを設定する

{% tabs ローカル %}
{% tab センドグリッド %}
{% subtabs %}
{% subtab iOS %}
#### ステップ3a：AASAファイルをサポートするようにSDKを設定する。
クリック録音ドメインでAASAファイルをホストした後、AASAファイルをサポートするようにAppsFlyer SDKを設定する。

1. Xcodeでプロジェクトを選択する。
2. **能力を**選択する**。**
3. **関連ドメインを**オンにする**。**
4. **を**クリックし、クリックするドメインを入力する。例えば、`applinks:click.example.com` 。
ユニバーサルリンクがクリックされると、アプリが開かれ、SDKが起動する。アプリがクリックドメインの背後にあるOneLinkを抽出し、ディープリンクを解決できるようにするには、以下を実行する：

#### ステップ3b：ディープリンクのデータを扱う
1. SDK APIにクリック記録ドメインを提供する [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls).このAPIはSDKの初期化の前にコールされる必要がある。 `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
2. APIを使用する [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution)APIを使用して、ディープリンク・パラメータを取得し、ディープリンク・データを処理する。

{% endsubtab %}
{% subtab Android %}
#### ステップ3a：デジタルアセットリンクファイルをサポートするようにSDKを設定する。

前のステップでデジタルアセットリンクファイルをクリック録音ドメインにホストしたら、そのファイルをサポートするようにSDKを設定する。

Androidマニフェストで、ディープリンクしたいアクティビティのアクティビティタグに、クリックドメインホストと接頭辞を追加する。

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### ステップ3b：ディープリンクのデータを扱う
アプリリンクをクリックすると、アプリが開かれ、SDKが起動する。 アプリがクリックドメインの背後にあるOneLinkを抽出し、ディープリンクを解決できるようにするには、SDKメソッドでクリックドメインをリストする。 [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls).このプロパティはSDK初期化の前に設定する必要がある。`AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "anotherclickdomain.com");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab スパークポスト %}
{% subtabs %}
{% subtab iOS %}
#### ステップ3a：AASAファイルをサポートするようにSDKを設定する。
クリック録音ドメインでAASAファイルをホストした後、AASAファイルをサポートするようにSDKを設定する。

1. Xcodeでプロジェクトを選択する。
2. **能力を**選択する**。**
3. **関連ドメインを**オンにする**。**
4. **を**クリックし、クリックするドメインを入力する。例えば、`applinks:click.example.com` 。

#### ステップ3b：ディープリンクのデータを扱う
ユニバーサルリンクがクリックされると、アプリが開かれ、SDKが起動する。SDKがクリックドメインの背後にあるOneLinkを抽出できるようにするには、以下を実行する：
1. SDKプロパティにクリックドメインをリストする  [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls).SDK初期化の前にこのプロパティを必ず設定すること。
2. リスト <em>spgo.io</em>がリストされたドメインの1つであることを確認する。SparkPostはこのドメインを所有しており、リダイレクトフローの一部となっている。 `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
3. APIを使用する [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution)APIを使用して、ディープリンク・パラメータを取得し、ディープリンク・データを処理する。
{% endsubtab %}
{% subtab Android %}
#### ステップ3a：デジタルアセットリンクファイルをサポートするようにSDKを設定する。

前のステップでデジタルアセットリンクファイルをクリック録音ドメインにホストしたら、そのファイルをサポートするようにSDKを設定する。

Androidマニフェストで、ディープリンクしたいアクティビティのアクティビティタグに、クリックドメインホストと接頭辞を追加する。

```xml
<activity android:name=".DeepLinkActivity">
    <intent-filter android:autoVerify="true">
      <action android:name="android.intent.action.VIEW" />
      <category android:name="android.intent.category.DEFAULT" />
      <category android:name="android.intent.category.BROWSABLE" />
      <data
        android:scheme="https"
        android:host="click.example.com"
        android:pathPrefix="/campaign"
      />
    </intent-filter>
  </activity>
```

#### ステップ3b：アプリリンクのデータを扱う
アプリリンクをクリックすると、アプリが開かれ、SDKが起動する。アプリがクリックドメインの背後にあるOneLinkを抽出し、ディープリンクを解決できるようにするには、以下を実行する：

1. SDKメソッドのクリックドメインをリストする [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls).このプロパティはSDK初期化の前に設定する必要がある。
2. リスト *spgo.io*がリストされたドメインの1つであることを確認する。SparkPostはこのドメインを所有しており、リダイレクトフローの一部となっている。 `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "spgo.io");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

統合ステップが完了したら、OneLinkを使ってディープリンクを送信することで、品質保証とトラブルシューティングを行うことができる。OneLinkの使い方の詳細については、[AppsFlyerのドキュメントを](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a)参照のこと。

### BrazeのAppsFlyerクリックトラッキングURL（オプション）

AppsFlyerの[OneLinkアトリビューションリンクは](https://support.AppsFlyer.com/hc/en-us/articles/360001294118)、Brazeのキャンペーンでプッシュ、Eメールなどで使用できる。これにより、BrazeのキャンペーンからインストールやリエンゲージメントのアトリビューションデータをAppsFlyerに送り返すことができる。その結果、マーケティング活動をより効果的に測定し、データに基づいた意思決定を行うことができるようになる。

AppsFlyerでOneLinkトラッキングURLを作成し、Brazeキャンペーンに直接挿入するだけでよい。その後、AppsFlyerは[確率的アトリビューション手法を](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling)使用して、リンクをクリックしたユーザーをアトリビュートする。Brazeキャンペーンからの帰属の精度を高めるために、AppsFlyerのトラッキングリンクにデバイス識別子を付加することを推奨する。これにより、リンクをクリックしたユーザーの属性が決定的になる。

{% tabs ローカル %}
{% tab アンドロイド %}
Androidの場合、Brazeは[Google Advertising ID収集（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)）にオプトインすることができる。GAIDはまた、AppsFlyer SDKの統合によってネイティブに収集される。以下のリキッドロジックを利用することで、AppsFlyerのクリックトラッキングリンクにGAIDを含めることができる：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAppsFlyerの両社は、SDKインテグレーションを通じてIDFVをネイティブに自動収集する。これはデバイス識別子として使用できる。以下のリキッドロジックを利用することで、AppsFlyerのクリックトラッキングリンクにIDFVを含めることができる：

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}



[1]: {% image_buster /assets/img/braze_integration.png %}
[2]: {% image_buster /assets/img/braze_attribution.png %}
[3]: https://support.appsflyer.com/hc/en-us/articles/360001294118
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration "AppsFlyer Push API"
[31]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Braze-Formerly-Appboy-Integration
[4]: {% image_buster /assets/img/attribution/appsflyer.png %}
