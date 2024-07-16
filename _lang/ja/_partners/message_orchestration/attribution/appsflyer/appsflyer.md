---
nav_title: AppsFlyer
article_title:アプリフライヤー
alias: /partners/appsflyer/
description:「この参考記事では、アプリの分析と最適化に役立つモバイルマーケティング分析およびアトリビューションプラットフォームであるBrazeとAppsFlyerのパートナーシップについて概説しています。「
page_type: partner
search_tag:Partner

---

# アプリフライヤー

{% multi_lang_include video.html id="gQ9y2DA2LuQ" align="right" %}

> AppsFlyerは、マーケティング分析、モバイルアトリビューション、ディープリンクを通じてアプリの分析と最適化を支援するモバイルマーケティング分析およびアトリビューションプラットフォームです。

BrazeとAppsFlyerの統合により、AppsFlyerのモバイルインストールアトリビューションデータを活用して、より包括的なキャンペーンを最適化および構築する方法をより深く理解できるようになります。 

AppsFlyerオーディエンスの統合により、AppsFlyerオーディエンス（コホート）をBrazeに直接渡すこともできます。これにより、[適切なユーザーを適切なタイミングでターゲットとする強力なカスタマーエンゲージメント]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/appsflyer_audiences/)キャンペーンを作成できます。 

## 前提条件

| 必要条件 | 説明 |
|---|---|
| アプリフライヤーアカウント | このパートナーシップを利用するには、AppsFlyerアカウントが必要です。 |
| iOS またはAndroid アプリ | このインテグレーションは iOS アプリと Android アプリをサポートします。プラットフォームによっては、アプリケーションにコードスニペットが必要な場合があります。これらの要件の詳細は、統合プロセスのステップ1に記載されています。 |
| AppsFlyer SDK | 必要な Braze SDK に加えて、[AppsFlyer](https://dev.appsflyer.com/hc/docs/getting-started) SDK をインストールする必要があります。
| メールドメインの設定が完了しました | Braze [オンボーディング中にメール設定 IP とドメインの設定ステップ]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)を完了している必要があります。 |
| SSL 証明書 | [SSL 証明書を設定する必要があります]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#acquiring-an-ssl-certificate)。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:デバイス ID をマッピング

#### Android

Androidアプリをお持ちの場合は、固有のBrazeデバイスIDをAppsFlyerに渡す必要があります。 

Braze SDKの起動後、AppsFlyer SDK Kの初期化コードの前に、次のコード行が正しい場所に挿入されていることを確認してください。詳細については、[AppsFlyerAndroid SDKインテグレーションガイドをご覧ください](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk)。

```java
HashMap<String, Object> customData = new HashMap<String,Object>();
String deviceId =(Braze.getInstance(MyActivity.this).getDeviceId());
customData.put("brazeCustomerId", deviceId);
AppsFlyerLib.setAdditionalData(customData);
```

#### iOS

{% alert important %}
2023年2月以前は、AppsFlyerアトリビューション統合では、iOSのアトリアトリビューションデータを照合するためのプライマリ識別子としてIDFVを使用していました。Objective-Cを使用しているBrazeのお客様は、サービスが中断されないため、`device_id`インストール時にBrazeを取り出してAppsFlyerに送信する必要はありません。
{% endalert%}

Swift SDK v5.7.0以降を使用している場合、引き続きIDFVを相互識別子として使用する場合は、`useUUIDAsDeviceId``false`統合が中断されないようにフィールドがに設定されていることを確認する必要があります。 

に設定した場合`true`、BrazeがiOSのアトリビューションと適切に一致するようにするには、アプリ`device_id`インストール時にBrazeをAppsFlyerに渡すために、SwiftのiOSデバイスIDマッピングを実装する必要があります。

{% tabs local %}
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
{% tab Swift %}

##### スウィフトコンプリートハンドラー
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
##### スウィフト・ウェイト
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

### ステップ2:Braze データインポートキーを取得

**Brazeで、「**パートナー統合」>「テクノロジーパートナー****」に移動し、AppsFlyerを選択します**。** 

{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、「**インテグレーション**」**の下にテクノロジーパートナーが表示されます**。
{% endalert %}

ここで REST エンドポイントを見つけ、Braze データインポートキーを生成します。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にすることができます。データインポートキーとRESTエンドポイントは、AppsFlyerダッシュボードでポストバック設定する際のステップで使用されます。<br><br>![AppsFlyerテクノロジーページにある「インストールアトリビューションのデータインポート」ボックスがあります。このボックスには、データインポートキーと REST エンドポイントが含まれています。][4]{: style="max-width:70%;"}

### ステップ3:AppsFlyerダッシュボードでBraze を設定します

1. AppsFlyerで、左側のバーにある「**連携パートナー**」ページに移動します。次に、**Brazeを検索し**、Brazeのロゴをクリックして設定ウィンドウ開封。
2. \[**統合**] タブで \[**パートナーをアクティブ化**] を切り替える。
3. Braze のダッシュボードで見つけたデータインポートキーと REST エンドポイント。 
4. **アドバンスドプライバシーをオフに切り替えて**、設定を保存します。

これらの手順に関する追加情報は、\[AppsFlyer] のドキュメントに記載されています。][16]

### ステップ 4:統合を確認する

BrazeがAppsFlyerからアトリビューションデータを受信すると、BrazeのAppsFlyerテクノロジーパートナーページのステータス接続インジケーターが「未接続」から「接続済み」に変わります。最後に成功したリクエストのタイムスタンプも含まれます。 

なお、アトリビューションされたインストールに関するデータを受け取るまでは発生しません。AppsFlyerポストバックから除外すべきオーガニックインストールは、APIでは無視され、正常に接続が確立されたかどうかを判断する際にはカウントされません。

### ステップ 5: ユーザーアトリビューションデータを表示する

#### 使用可能なデータフィールド

提案どおりに統合を設定した場合、Brazeはすべての非オーガニックインストールデータをSegment フィルターにマッピングします。

| AppsFlyer データフィールド | Braze Segment フィルター |
| -------------------- | --------------------- |
| `media_source` | 属性付きソース |
| `campaign` | アトリビューションキャンペーン |
| `af_adset` | アトリビューション広告グループ |
| `af_ad` | アトリビューション広告 |
{: .reset-td-br-1 .reset-td-br-2}

インストールアトリビューションフィルターを使用して、Brazeダッシュボードでユーザー群をアトリビューションデータでセグメント化できます。

![4 つのフィルターを使用できます。1つ目は「インストールアトリビューションソースはnetwork_val_0です」です。2つ目は「インストールアトリビューションソースはcampaign_val_0です」です。3つ目は「インストールアトリビューションソースはadgroup_val_0です」です。4つ目は「インストールアトリビューションソースはcreative_val_0です」です。リストされているフィルターの横に、これらのアトリビューションソースがユーザープロファイルどのように追加されるかがわかります。ユーザー情報ページの「インストールアトリビューション」ボックスでは、インストールソースはnetwork_val_0、キャンペーンはcampaign_val_0などと表示されます。][2]

さらに、特定のユーザーアトリビューションデータは、Braze管理画面の各ユーザーのプロファイルで確認できます。

{% alert note %}
FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、パートナーを通じて入手することはできません。これらのメディアソースは、パートナーがアトリビューションデータを第三者と共有することを許可していないため、パートナーがそのデータを Braze に送信することはできません。
{% endalert %}

## AppsFlyerをメールサービスプロバイダーと統合してディープリンクを行う

AppsFlyerはメールサービスプロバイダー（ESP）としてSendGridとSparkPostの両方と統合されており、ディープリンクとクリックトラッキング, 追跡をサポートしています。以下の手順に従って、お使いのメールサービスプロバイダー (ESP) と統合してください。

{% alert tip %}
ディープリンク（アプリやWeb サイト内の特定のページや場所にユーザーを誘導するリンク）は、カスタマイズされたユーザーエクスペリエンスを実現するために使用されます。広く使用されていますが、電子メールで送信されるディープリンクとクリックトラッキングを使用すると問題が発生する可能性があります。クリックトラッキング, 追跡は、ユーザーデータ収集に使用されるもう1つの重要な機能です。これらの問題は、ESP がクリック記録ドメインでディープリンクをラップし、元のリンクを壊してしまうことが原因です。そのため、ディープリンクをサポートするには追加の設定が必要です。AppsFlyerをSendGridまたはSparkPostと統合することで、このような問題を回避できます。このトピックの詳細については、[ユニバーサルリンクとアプリリンクをご覧ください]({{site.baseurl}}/help/help_articles/email/universal_links/)。
{% endalert %}

### ステップ1:AppsFlyerでワンリンクをセットアップ

1. AppsFlyerで、メールキャンペーン用のOneLinkテンプレートを選択します。テンプレートがユニバーサルリンク (iOS) またはアプリリンク (Android) をサポートしていることを確認してください。 
2. OneLink とのディープリンクをサポートするようにアプリを設定します。OneLinkをサポートするようにアプリを設定する方法の詳細については、[AppsFlyerのドキュメントを参照してください](https://dev.appsflyer.com/hc/docs/dl_work_flow#initial-setup)。

### ステップ2:ユニバーサルリンクとアプリリンクをサポートするようにアプリを設定する

ユニバーサルリンク（iOS）またはアプリリンク（Android）は、デバイスのオペレーティングシステムにより、クリック時に特定のアプリ開封ことができます。

ユニバーサルリンクとアプリリンクをサポートするには、次の手順を実行します。

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
Apple App Site Association（AASA）のファイルホスティングを設定して、Eメールでユニバーサルリンクを有効にしてください。

1. 次のいずれかの方法で AASA ファイルを取得します。
    * ユニバーサルリンクを使用してOneLinkを設定した場合、OneLinkに関連付けられたAASAファイルがすでにある可能性があります。AASA ファイルを取得するには、以下を実行します。
        * OneLink テンプレートの OneLink サブドメインをコピーします。テンプレートがユニバーサルリンクをサポートしていることを確認してください。
        * プレースホルダーの代わりに次の URL に貼り付けます。 `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * **AASA ファイルをダウンロードするには、OneLink の URL をブラウザーのアドレスバーに貼り付け、Enter キーを押します。**その後、ファイルがコンピューターダウンロードされ、任意のテキストエディターを使用してその内容開封表示できます。
    * [Appleのユニバーサルリンクガイドでは](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content)、AASAファイルの作成方法が説明されています。
2. クリック記録ドメインサーバーで AASA ファイルをホストします。ファイルはパス:でホストされている必要があります`click.example.com/.well-known/apple-app-site-association`。 

[SendGrid 用に AASA ファイルを設定する方法と、その AASA ファイルをホストする CDN サービスを設定する方法については、SendGrid のドキュメントを参照してください](https://docs.sendgrid.com/ui/sending-email/universal-links)。

{% alert important %}
AASA ファイルがホストされたら、OneLink の設定を変更 (変更または置換) した場合は、新しい AASA ファイルを生成する必要があります。
{% endalert %}
{% endsubtab %}
{% subtab Android %}
デジタルアセットリンクファイルホスティングを設定して、メール内のアプリリンクを有効にします。

1. 以下のいずれかの方法でデジタル資産リンクファイルを取得します。
    * アプリリンクで OneLink を設定した場合、すでに OneLink に関連付けられたデジタルアセットリンクファイルがある可能性があります。ファイルを入手するには、以下を実行します。
        * OneLink テンプレートの OneLink サブドメインをコピーします。テンプレートがアプリリンクをサポートしていることを確認してください。
        * OneLink URL `/.well-known/assetlinks.json` の末尾に追加します。
        * **デジタルアセットリンクファイルをダウンロードするには、OneLink URL をブラウザのアドレスバーに貼り付け、Enter キーを押します。**たとえば、`https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`。その後、ファイルがコンピューターダウンロードされ、任意のテキストエディターを使用してその内容開封表示できます。
    * [Android のアプリリンクガイドでは](https://developer.android.com/studio/write/app-link-indexing)、デジタルアセットリンクファイルの作成方法が説明されています。
2. クリック記録ドメインサーバーでデジタルアセットリンクファイルをホストします。ファイルはパス:でホストされている必要があります`click.example.com/.well-known/apple-app-site-association`。

[SendGrid のデジタルアセットリンクファイルを設定する方法と、デジタルアセットリンクファイルをホストする CDN サービスを設定する方法については、SendGrid のドキュメントを参照してください](https://docs.sendgrid.com/ui/sending-email/universal-links)。

{% alert important %}
デジタルアセットリンクファイルがホストされたら、OneLinkの設定を変更（変更または置換）した場合は、新しいファイルを生成する必要があります。
{% endalert %}
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### ステップ 2a: AASA ファイルホスティングの設定
Apple App Site Association（AASA）のファイルホスティングを設定して、Eメールでユニバーサルリンクを有効にしてください。

1. 次のいずれかの方法で AASA ファイルを取得します。
    * ユニバーサルリンクを使用してOneLinkを設定した場合、OneLinkに関連付けられたAASAファイルがすでにある可能性があります。AASA ファイルを取得するには、以下を実行します。
        * OneLink テンプレートの OneLink サブドメインをコピーします。テンプレートがユニバーサルリンクをサポートしていることを確認してください。
        * プレースホルダーの代わりに次の URL に貼り付けます。 `<OneLinkSubdomain>.onelink.me/.well-known/apple-app-site-association`
        * **AASA ファイルをダウンロードするには、OneLink の URL をブラウザーのアドレスバーに貼り付け、Enter キーを押します。**その後、ファイルがコンピューターダウンロードされ、任意のテキストエディターを使用してその内容開封表示できます。
    * [Appleのユニバーサルリンクガイドでは](https://developer.apple.com/documentation/xcode/allowing_apps_and_websites_to_link_to_your_content)、AASAファイルの作成方法が説明されています。
2. クリック記録ドメインサーバーで AASA ファイルをホストします。ファイルはパス:でホストされている必要があります`click.example.com/.well-known/apple-app-site-association`。 

[SparkPost 用の AASA ファイルを設定する方法とカスタムリンクサブパスを設定する方法については、SparkPost のドキュメントを参照してください](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve)。

{% alert important %}
AASA ファイルがホストされたら、OneLink の設定を変更 (変更または置換) した場合は、新しい AASA ファイルを生成する必要があります。
{% endalert %}

#### ステップ 2b: クリックトラッキング, 追跡ドメインを AASA ファイルホストにリダイレクトする
[メールの設定中に]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)、DNS サーバーに CNAME レコードを作成しました。Braze でクリックトラッキング, 追跡ドメインを確認したら、次の手順を実行します。 

1. サブドメインを SparkPost ドメインにリダイレクトする CNAME レコードを削除します。
2. 上記で削除したレコードの代わりに、クリックトラッキング, 追跡ドメインをアプリの AASA ファイルをホストしている CDN にリダイレクトする CNAME レコードを作成します。
{% endsubtab %}
{% subtab Android %}
#### ステップ 2a: デジタルアセットリンクのファイルホスティングを設定する
デジタルアセットリンクファイルホスティングを設定して、メール内のアプリリンクを有効にします。

1. 以下のいずれかの方法でデジタル資産リンクファイルを取得します。
    * アプリリンクで OneLink を設定した場合、すでに OneLink に関連付けられたデジタルアセットリンクファイルがある可能性があります。ファイルを入手するには、以下を実行します。
        * OneLink テンプレートの OneLink サブドメインをコピーします。テンプレートがアプリリンクをサポートしていることを確認してください。
        * OneLink URL `/.well-known/assetlinks.json` の末尾に追加します。
        * **デジタルアセットリンクファイルをダウンロードするには、OneLink URL をブラウザのアドレスバーに貼り付け、Enter キーを押します。**たとえば、`https://<OneLinkSubdomain>.onelink.me/.well-known/assetlinks.json`。その後、ファイルがコンピューターダウンロードされ、任意のテキストエディターを使用してその内容開封表示できます。
    * [Android のアプリリンクガイドでは](https://developer.android.com/studio/write/app-link-indexing)、デジタルアセットリンクファイルの作成方法が説明されています。
2. クリック記録ドメインサーバーでデジタルアセットリンクファイルをホストします。ファイルはパス:でホストされている必要があります`click.example.com/.well-known/apple-app-site-association`。

[SparkPostのデジタル・アセット・リンク・ファイルを構成し、カスタム・リンク・サブパスを設定する方法については、SparkPostのドキュメントを参照してください](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve)。

{% alert important %}
デジタルアセットリンクファイルがホストされたら、OneLinkの設定を変更（変更または置換）した場合は、新しいファイルを生成する必要があります。
{% endalert %}

#### ステップ 2b: クリックトラッキング, 追跡ドメインをデジタルアセットリンクファイルホストにリダイレクト
[メールの設定中に]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/setting_up_ips_and_domains/)、DNS サーバーに CNAME レコードを作成しました。Braze でクリックトラッキング, 追跡ドメインを確認したら、次の手順を実行します。 

1. サブドメインを SparkPost ドメインにリダイレクトする CNAME レコードを削除します。
2. 上記で削除したレコードの代わりに、クリックトラッキング, 追跡ドメインをアプリデジタルアセットリンクファイルをホストしている CDN にリダイレクトする CNAME レコードを作成します。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

### ステップ3:ディープリンクをサポートするようにAppsFlyer SDKを設定してください

{% tabs local %}
{% tab SendGrid %}
{% subtabs %}
{% subtab iOS %}
#### ステップ 3a:AASA ファイルをサポートするようにSDKを設定する
クリック記録ドメインでAASAファイルをホストしたら、AppsFlyer SDKがAASAファイルをサポートするように設定します。

1. Xcode で、プロジェクトを選択します。
2. 「**機能」を選択します。**
3. 「**関連ドメイン」をオンにする。**
4. 「**+**」をクリックし、クリックドメインを入力します。たとえば、`applinks:click.example.com`。
ユニバーサルリンクをクリックすると、アプリが開き、SDKが開始されます。アプリクリックドメインの背後にあるOneLinkを抽出してディープリンクを解決できるようにするには、以下を実行します。

#### ステップ 3b:ディープリンクデータを処理する
1. SDK API にクリック記録ドメインを指定します[`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls)。この API は、SDK を初期化する前に呼び出す必要があります。 `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
2. [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution)API を使用してディープリンクのパラメータを取得し、ディープリンクのデータを処理します。

{% endsubtab %}
{% subtab Android %}
#### ステップ 3a:デジタルアセットリンクファイルをサポートするようにSDKを設定

前のステップでクリック記録ドメインでデジタルアセットリンクファイルをホストしたら、そのファイルをサポートするようにSDKを設定します。

Androidマニフェストで、ディープリンクしたいアクティビティのアクティビティタグに、クリックドメインホストと任意のプレフィックスを追加します。

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

#### ステップ 3b:ディープリンクデータを処理する
アプリリンクをクリックすると、アプリが開き、SDKが開始されます。 アプリクリックドメインの背後にあるOneLinkを抽出してディープリンクを解決できるようにするには、SDKメソッドにクリックドメインを一覧表示します。[`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls)このプロパティは、SDK を初期化する前に設定する必要があります。 `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "anotherclickdomain.com");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% tab SparkPost %}
{% subtabs %}
{% subtab iOS %}
#### ステップ 3a:AASA ファイルをサポートするようにSDKを設定する
クリック記録ドメインで AASA ファイルをホストしたら、その AASA ファイルをサポートするように SDK を設定します。

1. Xcode で、プロジェクトを選択します。
2. 「**機能」を選択します。**
3. 「**関連ドメイン」をオンにする。**
4. 「**+**」をクリックし、クリックドメインを入力します。たとえば、`applinks:click.example.com`。

#### ステップ 3b:ディープリンクデータを処理する
ユニバーサルリンクをクリックすると、アプリが開き、SDKが開始されます。SDKがクリックドメインの背後にあるOneLinkを抽出できるようにするには、以下を実行します。
1. SDK プロパティにクリックドメインを一覧表示します[`resolveDeepLinkURLs`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlib#resolvedeeplinkurls)。SDK を初期化する前に、このプロパティを必ず設定してください。
2. List <em>spgo.ioがリストされているドメインの1つであることを確認してください</em>。SparkPostはこのドメインを所有しており、リダイレクトフローの一部です。 `AppsFlyerLib.shared().resolveDeepLinkURLs = ["click.example.com","spgo.io"]`
3. [`onAppOpenAttribution`](https://dev.appsflyer.com/hc/docs/ios-sdk-reference-appsflyerlibdelegate#onappopenattribution)API を使用してディープリンクのパラメータを取得し、ディープリンクのデータを処理します。
{% endsubtab %}
{% subtab Android %}
#### ステップ 3a:デジタルアセットリンクファイルをサポートするようにSDKを設定

前のステップでクリック記録ドメインでデジタルアセットリンクファイルをホストしたら、そのファイルをサポートするようにSDKを設定します。

Androidマニフェストで、ディープリンクしたいアクティビティのアクティビティタグに、クリックドメインホストと任意のプレフィックスを追加します。

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

#### ステップ 3b:アプリリンクデータを処理する
アプリリンクをクリックすると、アプリが開き、SDKが開始されます。アプリクリックドメインの背後にあるOneLinkを抽出してディープリンクを解決できるようにするには、以下を実行します。

1. SDK メソッドのクリックドメインを一覧表示します[`setResolveDeepLinkURLs`](https://support.appsflyer.com/hc/en-us/articles/4408735106193#resolve-wrapped-deep-link-urls)。このプロパティは、SDK を初期化する前に設定する必要があります。
2. List *spgo.ioがリストされているドメインの1つであることを確認してください*。SparkPostはこのドメインを所有しており、リダイレクトフローの一部です。 `AppsFlyerLib.getInstance().setResolveDeepLinkURLs("clickdomain.com", "myclickdomain.com", "spgo.io");`
{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

統合手順を完了したら、OneLinkを使用してディープリンクを送信することで、QAとトラブルシューティングを実行できます。OneLinkの使用方法の詳細については、[AppsFlyerのドキュメントを参照してください](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a)。

### BrazeのAppsFlyerクリックトラッキング, 追跡 URL（オプション）

[AppsFlyerのOneLinkアトリビューションリンクは](https://support.AppsFlyer.com/hc/en-us/articles/360001294118)、プッシュやメールなどのBrazeキャンペーンで使用できます。これにより、BrazeキャンペーンのインストールまたはエンゲージメントアトリビューションデータをAppsFlyerに送り返すことができます。その結果、マーケティング活動をより効果的に測定し、データドリブン型のの意思決定を行うことができます。

AppsFlyerでOneLinkトラッキング, 追跡 URLを作成し、Brazeキャンペーンに直接挿入するだけです。その後、[AppsFlyerは確率的アトリビューション手法を使用して](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling)、リンクをクリックしたユーザー属性します。Brazeキャンペーンのアトリビューションの精度を向上させるために、AppsFlyerのトラッキング, 追跡リンクにデバイス識別子を追加することをおすすめします。これにより、リンクをクリックしたユーザー確定的に属性します。

{% tabs local %}
{% tab Android %}
Android の場合、Braze ではユーザーが [Google 広告 ID コレクション（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)）へのオプトインを許可しています。また、GAIDはAppsFlyer SDKインテグレーションを通じてネイティブに収集されます。以下のLiquidロジックを利用して、AppsFlyerのクリックトラッキング, 追跡リンクにGAIDを含めることができます。
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAppsFlyerの両方がSDKインテグレーションを通じてIDFVをネイティブに自動的に収集します。これはデバイス識別子として使用できます。以下のLiquidロジックを利用して、IDFVをAppsFlyerのクリックトラッキング, 追跡リンクに含めることができます。

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
[16]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration 「アプリフライヤープッシュAPI」
[31]: https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Braze-Formerly-Appboy-Integration
[4]: {% image_buster /assets/img/attribution/appsflyer.png %}
