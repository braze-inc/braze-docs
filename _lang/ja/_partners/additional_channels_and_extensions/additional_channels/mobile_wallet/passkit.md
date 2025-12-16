---
nav_title: PassKit
article_title: PassKit
alias: /partners/passkit/
description: "このリファレンス記事では、Brazeと Passkit のパートナーシップについて説明します。このパートナーシップにより、Apple ウォレットと Google Pay のパスをカスタマーエクスペリエンスに統合してモバイルリーチを拡大できます。"
page_type: partner
search_tag: Partner

---

# PassKit

> PassKit は Apple ウォレットと Google Pay のパスをカスタマーエクスペリエンスに統合するモバイルリーチの拡大を支援しています。デジタルクーポン、ロイヤルティカード、会員カード、チケットなどの作成、管理、配布、パフォーマンス分析を簡単に行うことができ、顧客は他のアプリを使用する必要がなくなります。

_この統合は Passkit によって管理されます。_

## 統合について

Braze と PassKit の統合により、Apple ウォレットと Google Pay のカスタムパスを即時に配信して、オンラインキャンペーンのエンゲージメントを高め、このエンゲージメントを測定できます。その後、利用状況を分析し、リアルタイムに調整することで、顧客のモバイルウォレットに位置情報に基づくメッセージやパーソナライズされたダイナミックな最新情報を送信し、ストア内のトラフィックを増加させることができます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| PassKitアカウント | PassKitアカウントとPassKitアカウントマネージャーが必要である。 |
| `userDefinedID` | PassKitとBrazeの間でユーザーへのカスタムイベントやカスタム属性を適切に更新するには、Brazeの外部IDを`userDefinedID` に設定する必要がある。この`userDefinedID` は、PassKit のエンドポイントに API コールを行う際に使用される。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | REST エンドポイントのURL。エンドポイントはインスタンスの [Braze URL]({{site.baseurl}}/api/basics/#endpoints) に応じて異なります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

顧客のモバイルウォレットエクスペリエンスをさらに充実させるために、PassKit ダッシュボードから、Braze [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint)を通じて Braze にデータを渡す選択ができます。 

PassKit から共有するデータの例を以下に示します。
- **Pass created**: 顧客がパスリンクをクリックして、パスが最初に表示される時点。
- **Pass installs**: 顧客がパスを追加し、自分のウォレットアプリに保存する時点。
- **Pass updates**: パスが更新される時点。
- **Pass delete**: 顧客がウォレットアプリからパスを削除する時点。

データがBrazeに渡されると、オーディエンスを構築し、Liquidでコンテンツをパーソナライズし、これらのアクションが実行された後にキャンペーンやCanvasesをトリガーすることができる。

## Passkit を Braze に接続する

PassKit からデータを渡すには、Braze external ID を PassKit の`externalId` として設定していることを確認します。

1. PassKit パスプロジェクトまたはプログラムの [**Settings**] の [**Integrations**] で、[**Braze**] タブの [**Connect**] をクリックします。<br>![PassKitプラットフォームのBraze統合タイル。]({% image_buster /assets/img/passkit/passkit5.png %}){: style="max-width:80%"}<br><br>
2. Braze API キーとエンドポイント URL を入力し、コネクターの名前を入力します。<br><br>
3. **Enable Integration（統合を有効にする**）をトグルし、Brazeでメッセージをトリガーまたはパーソナライズしたいイベントを選択する。<br>![API キー、エンドポイント URL、統合名、有効化設定、メンバーシップ設定、およびパス設定を受け入れるために展開されている PassKit Braze 統合タイル。]({% image_buster /assets/img/passkit/passkit4.png %}){: style="max-width:70%"}

## SmartPass リンクを使用してパスを作成する

Braze では、SmartPass リンクを設定して、顧客が Android またはiOS にパスをインストールするための一意のURL を生成するようにできます。そのためには、Brazeコンテンツブロックから呼び出せる暗号化されたSmartPassデータペイロードを定義する必要がある。この[コンテンツブロック]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks)は、今後のパスやクーポンに再利用できます。以下は統合の際に使用される：

- **PassKit URL**:PassKit URL は、PassKit プログラムの一意のURL です。<br>各プログラムには固有のURLがあり、PassKitプログラムまたはプロジェクトの「**Distribution」**タブで見つけることができる。(例えば、https://pub1.pskt.io/c/ww0jir ）<br><br>
- **PassKit シークレット**:URLとともに、このプログラムのPassKit Keyを手元に用意しておく必要がある。<br>これは PassKit URL と同じページで確認できます。<br><br>
- **プログラム (またはプロジェクト) ID**:スマートパスのURLを作成するには、PassKitプログラムIDが必要である。<br>プロジェクトやプログラムの**"Settings "**タブにある。

暗号化されたスマートパス・リンクの作成に関する詳細は、こちらの [PassKit の記事](https://help.passkit.com/en/articles/3742778-hashed-smartpass-links)を参照してください。

### ステップ 1: パスデータペイロードを定義する {#passkit-integrations}

まず、クーポンまたはメンバーのペイロードを定義する必要があります。 

ペイロードにはさまざまな構成要素を含めることができますが、ここでは2つの重要な構成要素を示します。

| 構成要素 | 必須 | タイプ | 説明 |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | 必須 | String | Brazeの外部IDとして設定され、PassKitからBrazeへのコールバックが機能するために重要であり、Brazeユーザーは1つのキャンペーンで複数のオファーのクーポンを持つことができる。一意であることは必須ではありません。 |
| `members.member.externalId` | オプション | String | Braze external ID として設定します。external ID を使用してメンバーシップパスを更新できます。このフィールドを設定することで、メンバーシッププログラム内でユーザーが一意になります。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

使用可能なすべてのフィールドとそのタイプ、役立つ説明については、[PassKit GitHub のドキュメント](https://github.com/PassKit/smart-pass-link-from-csv-generator)を参照してください。

#### ペイロードの例
{% raw %}
```liquid
{
  "members.member.externalId": "{{${user_id}}}",
  "members.member.points": "100",
  "members.tier.name": "current_customer",
  "person.displayName": "{{${first_name}}} {{${last_name}}}",
  "person.externalId": "{{${user_id}}}",
  "universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"
}
```
{% endraw %}

### ステップ2:未定義のペイロード変数を作成し、エンコードする

Braze ダッシュボード内の [**テンプレート**] > [**コンテンツブロック**] に移動して、新しいコンテンツブロックを作成し、名前を付けます。

[**コンテンツブロックを作成**] を選択して開始します。

次に、**コンテンツブロックの Liquid タグ**を定義します。このコンテンツブロックを保存したら、メッセージを作成するときにこの Liquid タグを参照できます。この例では、リキッドタグを{% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %} として割り当てている。 

このコンテンツブロック内部では、ペイロードを直接含めず、{% raw %}`{{passData}}`{% endraw %} 変数で参照する。コンテンツ・ブロックに追加しなければならない最初のコード・スニペットは、{% raw %}`{{passData}}`{% endraw %} 変数の Base64 エンコードをキャプチャする。
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### ステップ3:SHA1 HMACハッシュを使用して暗号化署名を作成する。

次に、プロジェクトのURLとペイロードの[SHA1 HMAC](https://en.wikipedia.org/wiki/HMAC)ハッシュを使って暗号化署名を作成する。 

コンテンツ・ブロックに追加しなければならない2つ目のコード・スニペットは、ハッシュに使用するURLをキャプチャするものだ。
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

次に、このハッシュと `Project Secret` を使用して署名を生成する必要があります。これは、3つ目のコード・スニペットを含めることで可能になる：
{% raw %}
```liquid
{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}
```
{% endraw %}

最後に、5番目のコード・スニペットを使って、完全なURLに署名を追加する：
{% raw %}
```liquid
{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}{% endcapture %}
```
{% endraw %}

### ステップ4:URLを印刷する

最後に、最終的な URL を呼び出すことを確認します。これにより、メッセージ内に SmartPass URL が出力されます。
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

この時点で、あなたは次のようなコンテンツブロックを作ったことになる：

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

この例では、これらのインストールのソースを Braze とこのキャンペーンまで追跡するために、UTM パラメーターが追加されています。

{% alert tip %}
ページを離れる前に、コンテンツブロックを必ず保存してください。
{% endalert %}

### ステップ 5: すべてをまとめる

このコンテンツブロックが作成されたら、今後再利用できます。 

コンテンツ・ブロックの例では、2つの変数が未定義のままになっていることにお気づきだろうか。<br> 
{% raw %}`{{passData}}`{% endraw %} - [ステップ1](#passkit-integrations)で定義した JSON パスデータのペイロード<br>
{% raw %}`{{projectUrl}}`{% endraw %} - Passkit プロジェクトの配布タブにあるプロジェクトまたはプログラムの URL。

これは意図的な決定であり、コンテンツブロックの再利用性がサポートされます。これらの変数は参照されるだけで、コンテンツ・ブロック内で作成されるわけではないので、コンテンツ・ブロックを作り直すことなく、これらの変数を変更することができる。 

たとえば、紹介オファーを変更して、ロイヤルティプログラムに初回ポイントを追加したり、セカンダリメンバーカードやクーポンを作成したりすることがあります。これらのシナリオでは必要な Passkit `projectURLs` またはパスペイロードが異なる可能性があります。これらは Braze でキャンペーンごとに定義します。  

#### メッセージ本文を作成する

この2つの変数をメッセージ本文に取り込んでから、コンテンツブロックを呼び出すことができます。
[ステップ1](#passkit-integrations)のミニファイ化された JSON ペイロードをキャプチャします。

**プロジェクト URL を割り当てる**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**JSON をキャプチャする**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**先ほど作成したコンテンツブロックを参照する**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

メッセージ本文は次のようなものだ：
![キャプチャされた JSON およびコンテンツブロック参照を含むコンテンツブロックメッセージ作成画面。]({% image_buster /assets/img/passkit/passkit1.png %}){: style="max-width:70%"}

サンプルの出力URLは以下の通りだ：
![ランダムに生成された文字と数字からなる長い文字列を含む出力 URL。]({% image_buster /assets/img/passkit/passkit2.png %}){: style="max-width:70%"}

出力URLは長くなる。その理由は、パスデータがすべて含まれており、データの完全性とURL変更による改ざんを確実にするために、クラス最高のセキュリティが組み込まれているからだ。SMS を使用してこのURL を配布する場合は、[bit.ly](https://dev.bitly.com/v4/#operation/createFullBitlink) のようなリンク短縮プロセスで実行することができます。これは、bit.ly エンドポイントへのコネクテッドコンテンツ呼び出しを使用して行うことができます。

## PassKit Webhook を使用してパスを更新する

Brazeでは、WebhookキャンペーンやCanvas内のWebhookを設定して、ユーザーの行動に基づいて既存のパスを更新することができる。有用な PassKit エンドポイントについては、次のリンクを参照してください。 
- [メンバープロジェクト](https://docs.passkit.io/protocols/member/)
- [クーポンプロジェクト](https://docs.passkit.io/protocols/coupon/)
- [フライトプロジェクト](https://docs.passkit.io/protocols/boarding/)

### ペイロードパラメーター

始める前に、PassKitへのウェブフックの作成と更新に含めることができる一般的なJSONペイロードパラメータを以下に示す。

| データ | タイプ | 説明 |
| ---- | ---- | ----------- |
| `externalId` | String | 一意の顧客識別子 (メンバーシップ番号など) を使用する既存のシステムとの互換性を得るために、パスレコードに一意の ID を追加できるようにします。このエンドポイントを使用して、パス ID ではなく `userDefinedId` と `campaignName` でパスデータを取得できます。この値はキャンペーン内で一意でなければならず、設定後は変更できない。<br><br>Braze 統合では、Braze external ID {% raw %}`{{${user_id}}}`{% endraw %} を使用することをお勧めします。 |
| `campaignId` (クーポン) <br><br> `programId` (メンバーシップ) | String | PassKitで作成したキャンペーンまたはプログラムテンプレートのID。これを確認するには、PassKit パスプロジェクトの [**Settings**] タブに移動します。 |
| `expiryDate` | ISO8601 日時 | パスの有効期限。この有効期限を過ぎると、パスは自動的に無効になります (`isVoided` を参照)。この値はテンプレートとキャンペーン終了日の値を上書きする。 |
| `status` | String | `REDEEMED` や`UNREDEEMED` など、クーポンの現在のステータス。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### ステップ1:BrazeのWebhookテンプレートを作成する

今後のキャンペーンやCanvasesで使用するPassKit Webhookテンプレートを作成するには、Brazeダッシュボードの**Templates& Media**セクションに移動する。単発のPassKitウェブフックキャンペーンを作成する場合、または既存のテンプレートを使用する場合は、新しいキャンペーンを作成する際にBrazeで**ウェブフックを**選択する。

PassKitウェブフック・テンプレートを選択すると、以下のように表示される：
- **Webhook URL**: `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **リクエスト本文**:Raw Text

#### リクエストヘッダと方法

PassKit の認証には、Base64 でエンコードされた PassKit API キーを含む `HTTP Header` が必要です。以下はすでにキーと値のペアとしてテンプレートに含まれているが、**Settings**タブでは、`<PASSKIT_LONG_LIVED_TOKEN>` をあなたのPassKitトークンに置き換える必要がある。トークンを取得するには、PassKit プロジェクト/プログラムに移動し、**[Settings] > [Integrations] > [Long Lived Token]** に移動します。

{% raw %}
- **HTTPメソッド**：PUT:
- **リクエストヘッダー**:
  - **Authorization**:ベアラー `<PASSKIT_LONG_LIVED_TOKEN>`
  - **Content-Type**: application/json
{% endraw %}

#### Request body

Webhookをセットアップするには、リクエストボディに新しいイベントの詳細を記入し、ユースケースに必要なペイロードパラメータを含める：

```json
{% raw %}{
  "externalId": "{{${user_id}}}",
  "campaignId": " 2xa1lRy8dBz4eEElBfmIz8",
  "expiryDate": "2020-05-10T00:00:00Z"
}{% endraw %}
```

### ステップ2:リクエストをプレビューする

入力したテキストがBrazeタグに該当する場合、自動的にハイライト表示される。 

**Preview**パネルでリクエストをプレビューするか、**Test**タブに移動して、ランダムなユーザー、既存のユーザーを選択するか、ウェブフックをテストするために自分でカスタマイズする。

{% alert important %}
ページを離れる前にテンプレートを保存することを忘れないこと！<br>更新されたWebhookテンプレートは、新しい[Webhookキャンペーンを]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)作成するときに、**保存されたWebhookテンプレート**リストで見つけることができる。
{% endalert %}

## コネクテッドコンテンツからパスの詳細を取得する

パスの作成と更新に加え、ユーザーのパスメタデータを Braze [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/)から取得し、パーソナライズされたパスの詳細をメッセージングキャンペーンに組み込むこともできます。

**PassKit コネクテッドコンテンツ呼び出し**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**Liquid の応答の例**

{% tabs local %}
{% tab passes redemptionDetails %}

```json
{
    "redemptionDate": null,
    "redemptionCode": "",
    "lat": 0,
    "lon": 0,
    "alt": 0,
    "redemptionSource": "",
    "redemptionReference": "",
    "transactionReference": "",
    "transactionAmount": 0
}
```

{% endtab %}
{% tab passes status %}
```
UNREDEEMED 
```
{% endtab %}
{% endtabs %}


