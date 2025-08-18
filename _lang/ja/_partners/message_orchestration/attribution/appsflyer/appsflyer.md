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
| AppsFlyerアカウント | このパートナーシップを活用するには、AppsFlyer アカウントが必要です。 |
| iOSやAndroid アプリ | この統合では、iOS アプリと Android アプリがサポートされています。ご使用のプラットフォームによっては、アプリケーションでコードスニペットが必要な場合があります。これらの要件の詳細については、統合プロセスのステップ1を参照してください。 |
| AppsFlyer SDK | 必要な Braze SDK に加えて、[AppsFlyer SDK](https://dev.appsflyer.com/hc/docs/getting-started) をインストールする必要があります。
| Eメールドメインのセットアップ完了 | Braze オンボーディング時にメールを設定するには、[IP とドメインの設定ステップ]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)を完了している必要があります。 |
| SSL証明書 | [SSL 証明書]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate) を設定する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:デバイス ID をマッピングする

{% tabs local %}
{% tab Android %}
Androidアプリをお持ちの場合、AppsFlyerに固有のBrazeデバイスIDを渡す必要がある。 

次のコード行が正しい位置に挿入されていることを確認します。これは、Braze SDK の起動と AppsFlyer SDK の初期化コードの間です。詳細については、AppsFlyer の [Android SDK 統合ガイド](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk)を参照してください。

```kotlin
val customData = HashMap<String, Any>()
Braze.getInstance(context).getDeviceIdAsync { deviceId ->
   customData["brazeCustomerId"] = deviceId
   setAdditionalData(customData)
}
```
{% endtab %}

{% tab ios %}
{% alert important %}
2023年2月以前は、AppsFlyerのアトリビューション統合は、iOSアトリビューションデータを照合するための主要な識別子としてIDFVを使用していた。Objective-C を使用している Braze のお客様は、サービスが中断されることはないため、インストール時に Braze `device_id` を取得してAppsFlyer に送信する必要はありません。
{% endalert%}

Swift SDK v5.7.0+ を使用しているお客様は、相互識別子として IDFV を引き続き使用するには、`useUUIDAsDeviceId` フィールドが `false` に設定されていることを確認する必要があります。これにより、統合が中断されることがなくなります。 

`true` に設定している場合、Brazeが iOS アトリビューションを適切に照合できるように、アプリのインストール時に AppsFlye に Braze`device_id` を渡すために、Swift用の iOS デバイス ID マッピングを実装する必要があります。

{% subtabs local %}
{% subtab Swift %}

```swift
let configuration = Braze.Configuration(
    apiKey: "<BRAZE_API_KEY>",
    endpoint: "<BRAZE_ENDPOINT>")
configuration.useUUIDAsDeviceId = false
let braze = Braze(configuration: configuration)
AppsFlyerLib.shared().customData = ["brazeDeviceId": braze.deviceId]
```
{% endsubtab %}

{% subtab Objective-C %}
```objc
BRZConfiguration *configurations = [[BRZConfiguration alloc] initWithApiKey:@"BRAZE_API_KEY" endpoint:@"BRAZE_END_POINT"];
[configurations setUseUUIDAsDeviceId:NO];
Braze *braze = [[Braze alloc] initWithConfiguration:configurations];
[[AppsFlyerLib shared] setAdditionalData:@{
    @"brazeDeviceId": braze.deviceId
}];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Unity %}
UnityでデバイスIDをマッピングするには、次を使用します。

```
Appboy.AppboyBinding.getDeviceId()
Dictionary<string, string> customData = new Dictionary<string, string>();
customData.Add("brazeCustomerId", Appboy.AppboyBinding.getDeviceId());
AppsFlyer.setAdditionalData(customData);
```
{% endtab %}
{% endtabs %}

### ステップ2:Braze データインポートキーを取得する

Brazeで、**Partner Integrations** > **Technology Partners** に移動し、**AppsFlyer** を選択します。 

ここでは、REST エンドポイントが見つかり、Brazeデータインポートキーが生成されます。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、AppsFlyerのダッシュボードでポストバックを設定する際に、次のステップで使用される。<br><br>![AppsFlyer テクノロジーページで利用可能な「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーと REST エンドポイントが表示されている。][4]{: style="max-width:70%;"}

### ステップ 3:AppsFlyerのダッシュボードでBrazeを設定する

1. AppsFlyer で、左側のバーの [**Integrated Partners**] ページに移動します。次に **Braze** を検索し、Braze のロゴを選択すると設定ウィンドウが開きます。
2. [**Integration**] タブで [**Activate Partner**] をオンにします。
3. Braze ダッシュボードで見つけたデータインポートキーと RESTエンドポイントを入力します。 
4. [**Advanced Privacy**] をオフに切り替え、設定を保存します。

これらの手順に関する追加情報は、[AppsFlyer のドキュメント][16]に掲載されています。

### ステップ4:統合を確認する

BrazeがAppsFlyerからアトリビューションデータを受信すると、BrazeのAppsFlyerテクノロジーパートナーページのステータス接続インジケータが「未接続」から「接続済み」に変わる。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、紐づけられるインストールに関するデータを受け取るまでは発生しないことに注意してください。AppsFlyerのポストバックから除外されるべきオーガニックインストールは、APIによって無視され、接続が正常に確立されたかどうかを判断する際にカウントされない。

### ステップ 5: ユーザーアトリビューションデータを確認する

#### 利用可能なデータフィールド

提案されたとおりに統合を構成したと仮定すると、Brazeはすべての非オーガニックインストールデータをセグメントフィルターにマッピングする。

| AppsFlyer データフィールド | Braze セグメントフィルター |
| -------------------- | --------------------- |
| `media_source` | 紐づけられるソース |
| `campaign` | 紐づけられるキャンペーン |
| `af_adset` | 紐づけられる広告グループ |
| `af_ad` | 紐づけられる広告 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

ユーザー群は、Braze ダッシュボードで インストールアトリビューションのフィルターを使用して、アトリビューションデータによってセグメント化できます。

![4つのフィルターがある。1つ目は「Install Attribution Source is network_val_0」である。2つ目は「Install Attribution Source is campaign_val_0」である。3つ目は「Install Attribution Source is adgroup_val_0」である。4つ目は、「表示ソースをcreative_val_0に設定する」である。表示されているフィルターの横に、これらのアトリビューションソースがユーザープロファイルにどのように追加されるかが示されている。ユーザー情報ページの「インストールアトリビューション」ボックスで、インストールソースとしてnetwork_val_0、キャンペーンとしてcampaign_val_0が表示されている。][2]

さらに、特定のユーザーのアトリビューションデータは、Braze ダッシュボードの各ユーザーのプロファイルで利用可能です。

{% alert note %}
FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできない。これらのメディアソースは、そのパートナーが帰属データを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできない。
{% endalert %}

## AppsFlyerとメールサービスプロバイダを統合してディープリンクを実現する

AppsFlyerは、メールサービスプロバイダ（ESP）としてSendGridとSparkPostの両方と統合し、ディープリンクとクリックトラッキングをサポートする。次の手順に従って、使用するメールサービスプロバイダー (ESP) と統合します。

{% alert tip %}
ディープリンク（アプリやウェブサイト内の特定のページや場所にユーザーを誘導するリンク）は、ユーザーに合わせてカスタマイズされたユーザー体験を作り出すために使用される。広く使用されている一方で、ユーザーデータの収集に使用されるもう一つの重要な機能であるクリックトラッキングでEメールによるディープリンクを使用する場合、問題が発生する可能性がある。これらの問題は、ESPがディープリンクをクリックを記録するドメインでラップし、元のリンクを壊してしまうことに起因する。そのため、ディープリンクをサポートするには、追加の設定が必要になる。AppsFlyerをSendGridまたはSparkPostと統合することで、これらの問題を回避できる。このトピックの詳細については、「[ユニバーサルリンクとアプリリンク]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links/)」を参照してください。
{% endalert %}

### ステップ1:AppsFlyerでOneLinkを設定する

1. AppsFlyerで、メールキャンペーン用のOneLinkテンプレートを選択する。テンプレートがユニバーサルリンク（iOS）またはアプリリンク（Android）をサポートしていることを確認する。 
2. OneLink でディープリンクをサポートするようにアプリを設定します。OneLinkをサポートするアプリの設定の詳細については、[AppsFlyerのドキュメントを](https://dev.appsflyer.com/hc/docs/dl_work_flow#initial-setup)参照のこと。

### ステップ2:ユニバーサルリンクとアプリリンクをサポートするようにアプリを設定する

ユニバーサルリンク（iOS）またはアプリリンク（Android）は、クリックすると指定されたアプリを開くことがデバイスのオペレーティングシステムによって許可されている。

ユニバーサルリンクとアプリリンクをサポートするには、次の手順を実行します。

{% tabs ローカル %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
Apple App Site Association (AASA)のファイルホスティングを設定し、Eメールでユニバーサルリンクを有効にする。

1. 以下のいずれかの方法でAASAファイルを入手する：
    * ユニバーサルリンクでOneLinkを設定している場合、OneLinkに関連付けられたAASAファイルがすでにあるかもしれない。AASAファイルを入手するには、以下を実行する：
        * OneLinkテンプレートのOneLinkサブドメインをコピーする。テンプレートがユニバーサルリンクをサポートしていることを確認する。
        * それを以下のURLのプレースホルダーの代わりに貼り付ける： `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * AASAファイルをダウンロードするには、OneLinkのURLをブラウザのアドレスバーに貼り付け、**Enter**キーを押す。ファイルがコンピューターにダウンロードされます。任意のテキストエディターを使用してこのファイルを開き、その内容を表示できます。
    * [アップルのユニバーサルリンクに関するガイドでは](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content)、AASAファイルの作成方法が説明されている。
2. クリックレコーディングドメインサーバーで AASA ファイルをホストします。ファイルが `click.example.com/.well-known/apple-app-site-association` というパスでホストされている必要があります。 

SendGrid 用に AASA ファイルを設定し、AASA ファイルをホストするように CDN サービスを設定する方法については、[SendGrid ドキュメント](https://docs.sendgrid.com/ui/sending-email/universal-links) を参照してください。

{% alert important %}
いったんAASAファイルがホストされると、OneLinkコンフィギュレーションを変更（修正または交換）する場合は、新しいAASAファイルを生成する必要がある。
{% endalert %}
{% endsubtab %}
{% subtab Android %}
デジタルアセットリンクファイルのホスティングを設定して、メールでアプリケーションリンクを有効にします。

1. 以下のいずれかの方法でデジタルアセットリンクファイルを入手します。
    * アプリリンクで OneLink を設定している場合は、OneLink に関連付けられているデジタルアセットリンクファイルがすでに存在している可能性があります。このファイルを入手するには、以下のようにする：
        * OneLinkテンプレートのOneLinkサブドメインをコピーする。テンプレートがApp Linksをサポートしていることを確認する。
        * OneLink URL の末尾に`/.well-known/assetlinks.json` を追加します。
        * デジタルアセットリンクファイルをダウンロードするには、OneLinkのURLをブラウザのアドレスバーに貼り付け、**Enter**キーを押す。たとえば `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json` です。ファイルがコンピューターにダウンロードされます。任意のテキストエディターを使用してこのファイルを開き、その内容を表示できます。
    * [Android のアプリリンクのガイド](https://developer.android.com/studio/write/app-link-indexing)で、デジタルアセットリンクファイルの作成方法が説明されています。
2. クリックレコーディングドメインサーバーでデジタルアセットリンクファイルをホストします。ファイルが `click.example.com/.well-known/apple-app-site-association` というパスでホストされている必要があります。

SendGrid 用にデジタルアセットリンクファイルを設定し、デジタルアセットリンクファイルをホストするように CDN サービスを設定する方法については、[SendGrid ドキュメント](https://docs.sendgrid.com/ui/sending-email/universal-links) を参照してください。

{% alert important %}
デジタルアセットリンクファイルがホストされたら、OneLink 設定を変更 (修正または置換) するには、新しいファイルを生成する必要があります。
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### ステップ 2a: AASAファイルのホスティングを設定する
Apple App Site Association (AASA)のファイルホスティングを設定し、Eメールでユニバーサルリンクを有効にする。

1. 以下のいずれかの方法でAASAファイルを入手する：
    * ユニバーサルリンクでOneLinkを設定している場合、OneLinkに関連付けられたAASAファイルがすでにあるかもしれない。AASAファイルを入手するには、以下を実行する：
        * OneLinkテンプレートのOneLinkサブドメインをコピーする。テンプレートがユニバーサルリンクをサポートしていることを確認する。
        * それを以下のURLのプレースホルダーの代わりに貼り付ける： `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * AASAファイルをダウンロードするには、OneLinkのURLをブラウザのアドレスバーに貼り付け、**Enter**キーを押す。ファイルがコンピューターにダウンロードされます。任意のテキストエディターを使用してこのファイルを開き、その内容を表示できます。
    * [アップルのユニバーサルリンクに関するガイドでは](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content)、AASAファイルの作成方法が説明されている。
2. クリックレコーディングドメインサーバーで AASA ファイルをホストします。ファイルが `click.example.com/.well-known/apple-app-site-association` というパスでホストされている必要があります。 

SparkPost 用の AASA ファイルを設定し、カスタムリンクサブパスを設定する方法については、[SparkPost のドキュメント](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve)を参照してください。

{% alert important %}
いったんAASAファイルがホストされると、OneLinkコンフィギュレーションを変更（修正または交換）する場合は、新しいAASAファイルを生成する必要がある。
{% endalert %}

#### ステップ 2b: クリック追跡ドメインをAASAファイルホストにリダイレクトする
[電子メールの設定]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)中に、DNSサーバーにCNAMEレコードを作成した。Braze でクリックトラッキングドメインを確認した後で、次の手順を実行します。 

1. サブドメインをSparkPostドメインにリダイレクトするCNAMEレコードを削除する。
2. 上記で削除したレコードの代わりに、クリック追跡ドメインをアプリのAASAファイルをホストしているCDNにリダイレクトするCNAMEレコードを作成する。
{% endsubtab %}
{% subtab Android %}
#### ステップ 2a: デジタルアセットリンクファイルのホスティングを設定する
デジタルアセットリンクファイルのホスティングを設定して、メールでアプリケーションリンクを有効にします。

1. 以下のいずれかの方法でデジタルアセットリンクファイルを入手します。
    * アプリリンクで OneLink を設定している場合は、OneLink に関連付けられているデジタルアセットリンクファイルがすでに存在している可能性があります。このファイルを入手するには、以下のようにする：
        * OneLinkテンプレートのOneLinkサブドメインをコピーする。テンプレートがApp Linksをサポートしていることを確認する。
        * OneLink URL の末尾に`/.well-known/assetlinks.json` を追加します。
        * デジタルアセットリンクファイルをダウンロードするには、OneLinkのURLをブラウザのアドレスバーに貼り付け、**Enter**キーを押す。たとえば `https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json` です。ファイルがコンピューターにダウンロードされます。任意のテキストエディターを使用してこのファイルを開き、その内容を表示できます。
    * [Android のアプリリンクのガイド](https://developer.android.com/studio/write/app-link-indexing)で、デジタルアセットリンクファイルの作成方法が説明されています。
2. クリックレコーディングドメインサーバーでデジタルアセットリンクファイルをホストします。ファイルが `click.example.com/.well-known/apple-app-site-association` というパスでホストされている必要があります。

SendGrid 用にデジタルアセットリンクファイルを設定し、カスタムリンクサブパスを設定する方法については、[SparkPost のドキュメント](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve)を参照してください。

{% alert important %}
デジタルアセットリンクファイルがホストされたら、OneLink 設定を変更 (修正または置換) するには、新しいファイルを生成する必要があります。
{% endalert %}

#### ステップ 2b: クリックトラッキングドメインをデジタルアセットリンクファイルホストにリダイレクトする
[電子メールの設定]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)中に、DNSサーバーにCNAMEレコードを作成した。Braze でクリックトラッキングドメインを確認した後で、次の手順を実行します。 

1. サブドメインをSparkPostドメインにリダイレクトするCNAMEレコードを削除する。
2. 上記で削除したレコードの代わりに、アプリのDigital Asset LinksファイルをホストしているCDNにクリック追跡ドメインをリダイレクトするCNAMEレコードを作成する。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ 3:ディープリンクをサポートするようにAppsFlyer SDKを設定する

{% tabs ローカル %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
#### ステップ3a:AASAファイルをサポートするようにSDKを設定する。
クリックレコーディングドメインで AASA ファイルをホストした後で、AASA ファイルをサポートするように AppsFlyer SDK を設定します。

1. Xcodeでプロジェクトを選択する。
2. [**Capabilities**] を選択します。
3. [**Associated Domains.**] をオンにします。
4. [**+**] をクリックし、クリックドメインを入力します。たとえば `applinks:click.example.com` です。
ユニバーサルリンクがクリックされると、アプリが開き、SDK が開始されます。アプリがクリックドメインの背後にあるOneLinkを抽出し、ディープリンクを解決できるようにするには、以下を実行する：

#### ステップ3b:ディープリンクのデータを扱う
1. SDK API [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls) にクリックレコーディングドメインを指定します。このAPIはSDKの初期化の前にコールされる必要がある。 `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
2. ディープリンクパラメーターを取得し、ディープリンクデータを処理するには、[`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API を使用します。

{% endsubtab %}
{% subtab Android %}
#### ステップ3a:デジタルアセットリンクファイルをサポートするようにSDK を設定する

前の手順でクリックレコーディングドメインでデジタルアセットリンクファイルをホストした後で、ファイルをサポートするように SDK を設定します。

Android マニフェストで、ディープリンクのリンク先にするアクティビティのアクティビティタグに、クリックドメインホストと任意の接頭辞を追加します。

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

#### ステップ3b:ディープリンクのデータを扱う
アプリリンクがクリックされると、アプリが開き、SDK が開始されます。 アプリがクリックドメインの背後にある OneLink を抽出し、ディープリンクを解決できるようにするには、SDK メソッド [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls) にクリックドメインをリストします。このプロパティはSDK初期化の前に設定する必要がある。`AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "anotherclickdomain.com");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### ステップ3a:AASAファイルをサポートするようにSDKを設定する。
クリックレコーディングドメインで AASA ファイルをホストした後で、AASA ファイルをサポートするように SDK を設定します。

1. Xcodeでプロジェクトを選択する。
2. [**Capabilities**] を選択します。
3. [**Associated Domains.**] をオンにします。
4. [**+**] をクリックし、クリックドメインを入力します。たとえば `applinks:click.example.com` です。

#### ステップ3b:ディープリンクのデータを扱う
ユニバーサルリンクがクリックされると、アプリが開き、SDK が開始されます。クリックドメインの背後にある OneLink を SDK が抽出できるようにするには、次の手順を実行します。
1. SDK プロパティ [`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls) にクリックドメインをリストします。SDK初期化の前にこのプロパティを必ず設定すること。
2. リスト <em>spgo.io</em> が、リストしたドメインの1つであることを確認します。SparkPost はこのドメインを所有しており、これはリダイレクトフローの一部です。`AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
3. ディープリンクパラメーターを取得し、ディープリンクデータを処理するには、[`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution) API を使用します。
{% endsubtab %}
{% subtab Android %}
#### ステップ3a:デジタルアセットリンクファイルをサポートするようにSDK を設定する

前の手順でクリックレコーディングドメインでデジタルアセットリンクファイルをホストした後で、ファイルをサポートするように SDK を設定します。

Android マニフェストで、ディープリンクのリンク先にするアクティビティのアクティビティタグに、クリックドメインホストと任意の接頭辞を追加します。

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

#### ステップ3b:アプリリンクのデータを処理する
アプリリンクがクリックされると、アプリが開き、SDK が開始されます。アプリがクリックドメインの背後にあるOneLinkを抽出し、ディープリンクを解決できるようにするには、以下を実行する：

1. SDK メソッド [`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls) にクリックドメインをリストします。このプロパティはSDK初期化の前に設定する必要がある。
2. リスト *spgo.io* が、リストしたドメインの1つであることを確認します。SparkPost はこのドメインを所有しており、これはリダイレクトフローの一部です。`AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "spgo.io");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

統合手順が完了したら、OneLink を使用してディープリンクを送信することで、品質保証とトラブルシューティングを実行できます。OneLinkの使い方の詳細については、[AppsFlyerのドキュメントを](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a)参照のこと。

### BrazeのAppsFlyerクリックトラッキングURL（オプション）

プッシュやメールなどの Braze キャンペーンで AppsFlyer の[OneLink アトリビューションリンク](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) を使用できます。これにより、BrazeのキャンペーンからインストールやリエンゲージメントのアトリビューションデータをAppsFlyerに送り返すことができる。その結果、マーケティング活動をより効果的に測定し、データに基づいた意思決定を行うことができるようになる。

AppsFlyerでOneLinkトラッキングURLを作成し、Brazeキャンペーンに直接挿入するだけでよい。その後、AppsFlyerは[確率的アトリビューション手法を](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling)使用して、リンクをクリックしたユーザーをアトリビュートする。Brazeキャンペーンからの帰属の精度を高めるために、AppsFlyerのトラッキングリンクにデバイス識別子を付加することを推奨する。これにより、リンクをクリックしたユーザーの属性が決定的になる。

{% tabs ローカル %}
{% tab Android %}
Android の場合、Braze ではお客様が [Google 広告 ID (GAID) 収集]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)にオプトインできます。GAID はまた、AppsFlyer SDK統合によってネイティブに収集されます。以下のリキッドロジックを利用することで、AppsFlyerのクリックトラッキングリンクにGAIDを含めることができる：
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
