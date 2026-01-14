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

> [AppsFlyerは](https://www.appsflyer.com/)モバイルマーケティング分析およびアトリビューションプラットフォームで、マーケティング分析、モバイルアトリビューション、ディープリンクを通じてアプリの分析と最適化を支援する。

BrazeとAppsFlyerの統合により、AppsFlyerのモバイルインストールアトリビューションデータを活用することで、より全体的なキャンペーンを最適化し、構築する方法をよりよく理解することができる。 

また、[AppsFlyer Audiences]({{site.baseurl}}/partners/data_and_analytics/cohort_import/appsflyer_audiences/)統合により、AppsFlyerのオーディエンス（コホート）を直接Brazeに渡すことができ、適切なタイミングで適切なユーザーをターゲットにした強力な顧客エンゲージメントキャンペーンを作成できる。 

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
Androidアプリの場合、AppsFlyerに固有のBrazeデバイスIDを渡す必要がある。 

以下のコード行が、Braze SDKの起動後、AppsFlyer SDKの初期化コードの前の正しい位置に挿入されていることを確認する。詳細については、AppsFlyer の [Android SDK 統合ガイド](https://dev.appsflyer.com/hc/docs/integrate-android-sdk#initializing-the-android-sdk)を参照してください。

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
2023年2月以前のAppsFlyerアトリビューション統合では、iOSアトリビューションデータを照合するための主要識別子としてIDFV（Identifier for Vendor）を使用していた。Objective-Cを使用しているBraze顧客は、サービスを中断することがないため、インストール時にBraze`device_id` を取得し、AppsFlyerに送信する必要はない。
{% endalert%}

Swift SDK v5.7.0+を使用している場合、相互識別子としてIDFVを引き続き使用したい場合は、統合の中断を避けるため、`useUUIDAsDeviceId` フィールドが`false` に設定されていることを確認する必要がある。 

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

{% tab unity %}
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

ここで、RESTエンドポイントを見つけ、Brazeデータインポートキーを生成する。キーが生成されたら、新しいキーを作成するか、既存のキーを無効にできます。データインポートキーとRESTエンドポイントは、AppsFlyerのダッシュボードでポストバックを設定する際に、次のステップで使用される。<br><br>![AppsFlyer テクノロジーページで利用可能な「インストールアトリビューションのデータインポート」ボックス。このボックスには、データインポートキーと REST エンドポイントが表示されている。]({% image_buster /assets/img/attribution/appsflyer.png %}){: style="max-width:70%;"}

### ステップ 3:AppsFlyerのダッシュボードでBrazeを設定する

1. AppsFlyer で、左側のバーの [**Integrated Partners**] ページに移動します。次に **Braze** を検索し、Braze のロゴを選択すると設定ウィンドウが開きます。
2. [**Integration**] タブで [**Activate Partner**] をオンにします。
3. Braze ダッシュボードで見つけたデータインポートキーと RESTエンドポイントを入力します。 
4. [**Advanced Privacy**] をオフに切り替え、設定を保存します。

これらの手順に関する追加情報は、[AppsFlyer のドキュメント](https://support.appsflyer.com/hc/en-us/articles/115001603343-AppsFlyer-Appboy-Integration)に掲載されています。

### ステップ 4: 統合を確認する

BrazeがAppsFlyerからアトリビューションデータを受信すると、BrazeのAppsFlyerテクノロジーパートナーページのステータス接続インジケータが「未接続」から「接続済み」に変わる。最後に成功したリクエストのタイムスタンプも含まれる。 

これは、Brazeがインストールアトリビューションに関するデータを受け取るまで起こらない。BrazeのAPIは、AppsFlyerのポストバックから除外されるべきオーガニックインストールを無視し、接続が正常に確立されたかどうかを判断する際にカウントしない。

### ステップ 5: ユーザーアトリビューションデータを確認する

#### 利用可能なデータフィールド

統合が成功した場合、Brazeはすべての非オーガニックインストールデータをセグメンテーションフィルターにマッピングする。

| AppsFlyer データフィールド | Braze セグメントフィルター |
| -------------------- | --------------------- |
| `media_source` | 紐づけられるソース |
| `campaign` | 紐づけられるキャンペーン |
| `af_adset` | 紐づけられる広告グループ |
| `af_ad` | 紐づけられる広告 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Brazeダッシュボードでは、インストールアトリビューションフィルターを使用して、ユーザー群をアトリビューションデータでセグメンテーションすることができる。

![4つのフィルターがある。1つ目は、「インストールアトリビューションソースがnetwork_val_0". 」 2つ目は、「インストールアトリビューションソースがcampaign_val_0". 」 3つ目は、「インストールアトリビューションソースがadgroup_val_0". 」 4つ目は、「インストールアトリビューションソースがcreative_val_0". 」 リストされたフィルターの横に、これらのアトリビューションソースがどのようにユーザープロファイルに追加されるかを見ることができる。ユーザー情報ページの「インストールアトリビューション」ボックスで、インストールソースはnetwork_val_0, キャンペーンはcampaign_val_0, などと表示される。]({% image_buster /assets/img/braze_attribution.png %})

さらに、特定のユーザーのアトリビューションデータは、Braze ダッシュボードの各ユーザーのプロファイルで利用可能です。

{% alert note %}
FacebookおよびX（旧Twitter）キャンペーンのアトリビューションデータは、当社のパートナーを通じて利用できません。これらのメディアソースは、そのパートナーがアトリビューションデータを第三者と共有することを許可していないため、当社のパートナーがそのデータをBrazeに送信することはできない。
{% endalert %}

## ディープリンクのためにAppsFlyerとBrazeを統合する

ディープリンク（アプリやウェブサイト内の特定のページや場所にユーザーを誘導するリンク）は、ユーザーに合わせてカスタマイズされたユーザー体験を作り出すために使用される。 

ユーザーデータの収集に使われるもう一つの重要な機能であるクリックトラッキング#8212でメールによるディープリンクを使用する場合、広く使われている一方で問題が発生する可能性がある。これらの問題は、メールサービスプロバイダ（ESP）がディープリンクをクリック記録ドメインでラッピングし、元のリンクを壊してしまうことに起因する。そのため、ディープリンクをサポートするには、追加の設定が必要になる。

AppsFlyerはこのような問題を回避する[サービスを](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer)提供しており、メールサービスプロバイダー（ESP）とお客様のドメイン名の間にイネーブルメントを介在させることができる。 プロキシとしての役割は、ディープリンクを容易にするアソシエーションファイル（AASA/アセットリンク）の提供を可能にする。 

## ステップ1 - クリック追跡ドメインを作成する 

[Brazeのメール設定ガイダンスの]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate)初期要素に従って、メール送信ドメインとクリック追跡ドメインを作成する。サポートについては、Brazeダッシュボードからチケットを発行し、Brazeメールチームと新しいCTDのセットアップを開始することができる。

![右上の "Support "ボタンの下にある "Get Help "ボタンを示すBraze UI]({% image_buster /assets/img/attribution/appsflyer/1.png %})

既存のCTDを使用している場合でも、新しいCTDの作成は必須である。これにより、現在のライブメールキャンペーンのトラフィックに影響を与えることはない。 

{% alert important%}
AppsFlyersがSSL証明書を作成する。この段階では、メールのリンクはセキュリティで保護されていない可能性が高く、URLプレフィックスがHTTPSではなくHTTPであることを意味する。これは後のステップで解決される。	
{%endalert%}

## ステップ2 - AppsFlyerでOneLinkテンプレートを作成する
[OneLinkテンプレートを](https://support.appsflyer.com/hc/en-us/articles/207032246-Create-a-OneLink-template#procedures)作成し、「アプリがインストールされたとき」にユニバーサルリンク/アプリリンクを設定する。このテンプレートは、後でメールキャンペーン用のOneLinkリンクを作成する際に使用する。

{% alert note%} ユニバーサルリンク/アプリリンクをイネーブルメントにする既存のOneLinkテンプレートがすでに設定されている場合は、それを使用できる。
{%endalert%}

## ステップ3 - AppsFlyerでBrazeインテグレーションを設定する
いよいよAppsFlyerでBrazeインテグレーションを設定する。このステップと次のステップ（「アプリの設定」）は同時に設定できる。
AppsFlyerでBrazeインテグレーションを設定する：

### 1\.AppsFlyerのサイドメニューから、エンゲージメント > メールサービスプロバイダー（ESPインテグレーション）を選択する。
![AppsFlyerのUIには、左側のメニューにある「ESPインテグレーション」ボタンが表示されている。]({% image_buster /assets/img/attribution/appsflyer/2.png %})

 
### 2\.Brazeを選択する。
![メールサービスプロバイダー（Braze）を含むESP統合のリストを表示するAppsFlyerのUI。]({% image_buster /assets/img/attribution/appsflyer/3.png %})

 
### 3\.メールキャンペーンに使用するOneLinkテンプレートを選択し、[次へ]をクリックする。
![AppsFlyerのUIに、ユーザーがテンプレートを選択できるドロップダウンが表示されている。]({% image_buster /assets/img/attribution/appsflyer/4.png %})

 
### 4. ステップ1で作成した新しいCTDで提供されたクリックトラッキングドメインと "エンドポイント "の値を入力し、"Validate connection "をクリックする。

これにより、クリック追跡ドメインが入力したエンドポイントを指していることが検証される。

![AppsFlyerのUIは、顧客がクリック追跡ドメインと関連する詳細を追加する場所をハイライトする。]({% image_buster /assets/img/attribution/appsflyer/5.png %})

AppsFlyerは、「Brazeエンドポイント」によって、このガイドのステップ1でBrazeから提供された詳細、特に新しいCTDを要求している。 

次に、**Validate connectionを**クリックし、クリック追跡ドメインが入力したエンドポイントを指していることを検証する。
完了したら、**Nextを**クリックする。

### 5. リンクトラフィックをAppsFlyerにルーティングする：

#### a. AppsFlyerでカスタマイズされたプレハブの説明書をコピーし、ITまたはドメイン管理者に送信する。 

管理者は、AppsFlyerが提供する新しいドメインでDNS CNAMEレコードを更新することにより、メールキャンペーントラフィックをESPサーバーからAppsFlyerサーバーに迂回させる必要がある。

その結果、リンクがクリックされるたびに、クリックはAppsFlyerにリダイレクトされ、AppsFlyerからESPエンドポイントにリダイレクトされる。

![クリックデータがドメインからメールサービスプロバイダー（ESPエンドポイント）へどのように渡されるかを示す図。]({% image_buster /assets/img/attribution/appsflyer/6.png %})

#### b. 指示をコピーして送信したら、「完了」をクリックする。
Brazeインテグレーションが作成された。

{%alert important%}
Brazeの統合ステータスは保留中で、CNAMEレコードがマッピングされた後にのみ機能し始める。新しい統合が機能し、アクティブになるまでには、マッピング後24時間かかることがある。
{%endalert%}

## ステップ 4: アプリを設定する（開発者タスク）
AppsFlyerは、ユニバーサルリンクをサポートするために、Webチームまたはアプリチームが従うべき正しいアプリ構成に関する[ガイダンスを提供する](https://support.appsflyer.com/hc/en-us/articles/26967438815377-Set-up-your-ESP-integration-with-AppsFlyer#step-2-configure-your-app-developer-task)。 

## ステップ 5: BrazeでSSLクリックトラッキングが有効になっていることを確認する。

この段階で、AppsFlyerでCTDの詳細を共有し、検証した後、Onelinkの送信ドメインにSSL証明書があるかどうかを確認するため、テスト送信を実行することを推奨する。これは[メール設定](https://www.braze.com/docs/user_guide/message_building_by_channel/email/email_setup/ssl/#acquiring-an-ssl-certificate)ガイドに沿ったものである。

OneLinkを使ってディープリンクを送信することで、品質保証やトラブルシューティングを行うことができる。OneLinkの使い方の詳細については、[AppsFlyerのドキュメントを](https://support.appsflyer.com/hc/en-us/articles/360001437497-Integrating-AppsFlyer-and-Braze#step-3-sending-your-first-email::2ffdb79a)参照のこと。

CTDリンクがHTTPと識別された場合は、Brazeのメールオペレーションチームに連絡して、SSLクリックトラッキングを有効にしてもらう。これにより、すべてのHTTPリンクが自動的にHTTPSに変換される。
カスタマーサクセスマネージャーに連絡する際、またはステップ1と同様にBrazeダッシュボードで再度チケットを発行する際に、以下のメッセージ文例を使用することができる： 

```
Hi Team,
Could you please enable SSL click tracking for CTD XXX? It is currently set to HTTP instead of HTTPS. 
```

### BrazeのAppsFlyerクリックトラッキングURL（オプション）

プッシュやメールなどの Braze キャンペーンで AppsFlyer の[OneLink アトリビューションリンク](https://support.AppsFlyer.com/hc/en-us/articles/360001294118) を使用できます。これにより、インストールやリエンゲージメントのアトリビューションデータをBrazeキャンペーンからAppsFlyerに送り返すことができる。その結果、マーケティング活動をより効果的に測定し、データドリブン型の意思決定を行うことができる。

AppsFlyerでOneLinkトラッキングURLを作成し、Brazeキャンペーンに直接挿入するだけでよい。その後、AppsFlyerは[確率的アトリビューション手法を](https://support.AppsFlyer.com/hc/en-us/articles/207447053-Attribution-model-explained#probabilistic-modeling)使用して、リンクをクリックしたユーザーの属性を決定する。Brazeキャンペーンからの帰属の精度を高めるために、AppsFlyerのトラッキングリンクにデバイス識別子を付加することを推奨する。これは、リンクをクリックしたユーザーを決定論的に属性化する。

{% tabs local %}
{% tab Android %}
Androidの場合、Brazeは顧客が[Google Advertising ID収集（GAID]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/optional_gaid_collection/#optional-google-advertising-id)）にオプトインできるようにしている。AppsFlyer SDKインテグレーションはGAIDも収集する。以下のLiquidロジックを使用することで、AppsFlyerのクリック追跡リンクにGAIDを含めることができる：
{% raw %}
```
{% if most_recently_used_device.${platform} == 'android' %}
aifa={{most_recently_used_device.${google_ad_id}}}
{% endif %}
```
{% endraw %}
{% endtab %}

{% tab iOS %}
iOSの場合、BrazeとAppsFlyerの両社は、SDKインテグレーションを通じてIDFVをネイティブに自動収集する。IDFCをデバイス識別子として使うことができる。以下のLiquidロジックを使用することで、AppsFlyerのクリック追跡リンクにIDFVを含めることができる：

{% raw %}
```
{% if most_recently_used_device.${platform} == 'ios' %}
idfv={{most_recently_used_device.${id}}}
{% endif %}
```
{% endraw %}
{% endtab %}
{% endtabs %}
