---
nav_title: パスキット
article_title: パスキット
alias: /partners/passkit/
description: "この参考記事では、ブレイズとパスキットのパートナーシップについて概説している。この提携により、アップルウォレットとグーグルペイを顧客体験に統合することで、モバイル・リーチを拡大することができる。"
page_type: partner
search_tag: Partner

---

# パスキット

> PassKitは、Apple WalletやGoogle Payのパスを顧客体験に統合することで、モバイル・リーチを拡大することを可能にする。デジタルクーポン、ポイントカード、会員カード、チケットなどの作成、管理、配布、パフォーマンス分析が簡単にできる。

BrazeとPassKitの統合により、Apple WalletとGoogle Payのカスタムパスを即座に配信することで、オンラインキャンペーンのエンゲージメントを高め、測定することができる。その後、利用状況を分析し、顧客のモバイル・ウォレットに位置情報ベースのメッセージやパーソナライズされた動的な更新をトリガーすることで、店舗でのトラフィックを増やすためのリアルタイム調整を行うことができる。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| PassKitアカウント | PassKitアカウントとPassKitアカウントマネージャーが必要である。 |
| `userDefinedID` | PassKitとBrazeの間でユーザーへのカスタムイベントやカスタム属性を適切に更新するには、Brazeの外部IDを`userDefinedID` 。この`userDefinedID` 、PassKitエンドポイントにAPIコールを行う際に使用される。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは、\[インスタンスのBraze URL][6] に依存する。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

顧客のモバイルウォレット体験をさらに豊かにするために、PassKitダッシュボードから、Brazeの\[`/users/track` エンドポイント][7]]を通じてBrazeにデータを渡すことができる。 

PassKitから共有されるデータの例には以下が含まれる：
- **パスの作成**：顧客がパスのリンクをクリックし、最初にパスが表示されたとき。
- **パスのインストール**：顧客がウォレットアプリにパスを追加し、保存**する**。
- **パスの更新**：パスが更新されたとき。
- **パスの削除**：顧客がウォレットアプリからパスを削除した場合。

データがBrazeに渡されると、オーディエンスを構築し、Liquidでコンテンツをパーソナライズし、これらのアクションが実行された後にキャンペーンやCanvasesをトリガーすることができる。

## パスキットとブレイズを接続する

PassKitからデータを渡すには、Brazeの外部IDをPassKitの`externalId` 。

1. **設定**内のPassKit passプロジェクトまたはプログラムの**Integrationsで**、**Braze**タブの**Connectを**クリックする。<br>![PassKitプラットフォームのBraze統合タイル。][5]{: style="max-width:80%"}<br><br>
2. Braze APIキー、エンドポイントURLを入力し、コネクタの名前を入力する。<br><br>
3. **Enable Integration（統合を有効にする**）をトグルし、Brazeでメッセージをトリガーまたはパーソナライズしたいイベントを選択する。<br>![PassKit Braze統合タイルが拡張され、APIキー、エンドポイントURL、統合名、有効化設定、会員設定、パス設定を受け付ける。][4]{: style="max-width:70%"}

## スマートパスリンクを使ってパスを作成する

Braze内では、スマートパスリンクを設定し、顧客がAndroidまたはiOSのいずれかにパスをインストールするための固有のURLを生成することができる。そのためには、Brazeコンテンツブロックから呼び出せる暗号化されたSmartPassデータペイロードを定義する必要がある。この\[コンテンツ・ブロック][9] ]は、将来のパスやクーポンに再利用できる。以下は、統合の際に使用される：

- **PassKitのURL**：PassKitのURLは、PassKitプログラムに固有のURLである。<br>各プログラムには固有のURLがあり、PassKitプログラムまたはプロジェクトの「**Distribution」**タブで見つけることができる。(例えば、https://pub1.pskt.io/c/ww0jir ）<br><br>
- **PassKitの秘密**だ：URLと一緒に、このプログラムのPassKit Keyも手元に用意しておく必要がある。<br>これはPassKitのURLと同じページに記載されている。<br><br>
- **プログラム（またはプロジェクト）ID**：スマートパスのURLを作成するには、PassKitプログラムIDが必要となる。<br>プロジェクトやプログラムの**"Settings "**タブにある。

暗号化されたスマートパス・リンクの作成に関する詳細は、こちらの\[PassKitの記事][8] 。

### ステップ1:パスデータのペイロードを定義する {#passkit-integrations}

まず、クーポンやメンバーのペイロードを定義しなければならない。 

ペイロードに含めることができるコンポーネントは多岐にわたるが、ここでは2つの重要なコンポーネントを紹介する：

| コンポーネント | 必須 | タイプ | 説明 |
| --------- | -------- | ---- | ----------- |
|`person.externalId` | 必須 | String | Brazeの外部IDとして設定され、PassKitからBrazeへのコールバックが機能するために重要であり、Brazeユーザーは1つのキャンペーンで複数のオファーのクーポンを持つことができる。ユニークなものとして施行されていない。 |
| `members.member.externalId` | オプション | String | Brazeの外部IDとして設定し、外部IDを使用して会員パスを更新することができる。このフィールドを設定することで、会員プログラム内でユーザーが一意であることが強制される。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

利用可能なフィールドの完全なリストとそのタイプ、役に立つ説明については、\[PassKit GitHub documentation][10] を見てほしい。

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

Brazeダッシュボードの**Templates**>**Content Blocksに**移動して、新しいコンテンツブロックを作成し、名前を付ける。

{% alert note %}
[旧式のナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**エンゲージメント**」＞「**テンプレート＆メディア**」＞「**コンテンツ・ブロック・ライブラリ**」と進む。
{% endalert %}

**コンテンツ・ブロックの作成**」を選択して開始する。

次に、**コンテンツブロックのリキッドタグを**定義しなければならない。このコンテンツブロックを保存した後、このリキッドタグはメッセージを作成するときに参照できる。この例では、リキッドタグを{% raw %}`{{content_blocks.${passKit_SmartPass_url}}}`{% endraw %} として割り当てている。 

このコンテンツ・ブロック内では、ペイロードを直接含めず、{% raw %}`{{passData}}`{% endraw %} 変数で参照する。コンテンツ・ブロックに追加しなければならない最初のコード・スニペットは、{% raw %}`{{passData}}`{% endraw %} 変数の Base64 エンコードをキャプチャする。
{% raw %}
```liquid
{% capture base64JsonPayload %}{{passDatapassData|base64_encode}}{% endcapture %}
```
{% endraw %}

### ステップ3:SHA1 HMACハッシュを使用して暗号化署名を作成する。

次に、プロジェクトのURLとペイロードの\[SHA1 HMAC][16] ハッシュ]を使って暗号化署名を作成する。 

コンテンツ・ブロックに追加しなければならない2つ目のコード・スニペットは、ハッシュに使用するURLをキャプチャするものだ。
{% raw %}
```liquid
{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}
```
{% endraw %}

次に、このハッシュと`Project Secret` を使って署名を生成する必要がある。これは、3つ目のコード・スニペットを含めることで可能になる：
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

最後に、最終的なURLを呼び出し、メッセージ内にスマートパスのURLが表示されるようにする。
{% raw %}
```liquid
{{longURL}}
```
{% endraw %}

この時点で、あなたは次のようなコンテンツ・ブロックを作成したことになる：

{% raw %}
```liquid
{% capture base64JsonPayload %}{{passData|base64_encode}}{% endcapture %}

{% capture url %}{{projectUrl}}?data={{base64JsonPayload}}{% endcapture %}

{% capture sig %}{{url | hmac_sha1: "Project_Secret"}}{% endcapture %}

{% capture longURL %}{{projectUrl}}?data={{base64JsonPayload}}&sig={{sig}}&utm_source=braze&utm_campaign={{campaign.${name}}}{% endcapture %}{% capture longURL %}{{longURL | url_encode}}{% endcapture %}

{{longURL}}
```
{% endraw %}

この例では、インストール元をBrazeとこのキャンペーンまで追跡するためにUTMパラメータが追加されている。

{% alert tip %}
ページを離れる前に、コンテンツ・ブロックを保存することを忘れないこと。
{% endalert %}

### ステップ 5: すべてをまとめる

このコンテンツ・ブロックは、一度作成されれば、今後も再利用することができる。 

コンテンツ・ブロックの例では、2つの変数が未定義のままになっていることにお気づきだろうか。<br> 
{% raw %}`{{passData}}`{% endraw %} [- ステップ](#passkit-integrations)1で定義したJSONパス・データのペイロード<br>
{% raw %}`{{projectUrl}}`{% endraw %} - Passkitプロジェクトのディストリビューション・タブにある、プロジェクトまたはプログラムのURL。

この決定は意図的なものであり、コンテンツ・ブロックの再利用性をサポートするものである。これらの変数は参照されるだけで、コンテンツ・ブロック内で作成されるわけではないので、コンテンツ・ブロックを作り直すことなく、これらの変数を変更することができる。 

例えば、ロイヤリティ・プログラムの初期ポイントを増やすために、紹介オファーを変更したいかもしれないし、二次的なメンバー・カードやクーポンを作りたいかもしれない。これらのシナリオでは、異なるPasskit`projectURLs` 、または異なるパスペイロードが必要となり、Brazeでキャンペーンごとに定義することになる。  

#### メッセージ本文を作成する

この2つの変数をメッセージ・ボディに取り込み、コンテンツ・ブロックを呼び出す。
[ステップ](#passkit-integrations)1で最小化したJSONペイロードをキャプチャする：

**プロジェクトのURLを割り当てる**
{% raw %}
```liquid
{% assign projectUrl = "https://pub1.pskt.io/c/ww0jir" %}
```
{% endraw %}

**JSONをキャプチャする**
{% raw %}
```liquid
{% capture passData %}{"members.member.externalId": "{{${user_id}}}","members.member.points": "100","members.tier.name": "current_customer","person.displayName": "{{${first_name}}} {{${last_name}}}","person.externalId": "{{${user_id}}}","universal.expiryDate": "{{ "now" | date: "%s" | plus: 31622400 | date: "%FT%TZ" }}"}{% endcapture %}
```
{% endraw %}

**先ほど作成したコンテンツ・ブロックを参照する**
{% raw %}
```liquid
{{content_block.${passkit_SmartPass_url}}}
```
{% endraw %}

メッセージ本文は次のようなものだ：
![キャプチャされたJSONとコンテンツ・ブロック・リファレンスが表示されたコンテンツ・ブロック・メッセージ・コンポーザーの画像。][1]{: style="max-width:70%"}

サンプルの出力URLは以下の通りだ：
![ランダムに生成された文字と数字の長い文字列を含む出力URL。][2]{: style="max-width:70%"}

出力URLは長くなる。その理由は、パスデータがすべて含まれており、データの完全性とURL変更による改ざんを確実にするために、クラス最高のセキュリティが組み込まれているからだ。SMSを使ってこのURLを配布する場合は、\[bit.ly][3].これは、bit.ly エンドポイントへのコネクテッド・コンテンツ・コールを通じて行うことができる。

## PassKitウェブフックを使用してパスを更新する

Brazeでは、WebhookキャンペーンやCanvas内のWebhookを設定して、ユーザーの行動に基づいて既存のパスを更新することができる。便利なPassKitエンドポイントについては、以下のリンクをチェックしてほしい。 
- \[メンバープロジェクト][12]
- \[クーポン企画][13]
- \[フライト・プロジェクト][14]

### ペイロードパラメーター

始める前に、PassKitへのウェブフックの作成と更新に含めることができる一般的なJSONペイロードパラメータを以下に示す。

| データ | タイプ | 説明 |
| ---- | ---- | ----------- |
| `externalId` | String | 一意の顧客識別子（会員番号など）を使用する既存のシステムとの互換性を提供するために、パスレコードに一意のIDを追加できるようにする。このエンドポイントを使えば、パスIDの代わりに`userDefinedId` 、`campaignName` 。この値はキャンペーン内で一意でなければならず、設定後は変更できない。<br><br>Brazeとの統合には、Brazeの外部IDを使用することをお勧めする： {% raw %}`{{${user_id}}}`{% endraw %} |
| `campaignId` (クーポン） <br><br> `programId` (会員制） | String | PassKitで作成したキャンペーンまたはプログラムテンプレートのID。これを見つけるには、PassKitパス・プロジェクトの**Settings**タブに向かう。 |
| `expiryDate` | IO8601 datetime | パスの有効期限。有効期限を過ぎると、パスは自動的に無効となる（`isVoided` を参照）。この値はテンプレートとキャンペーン終了日の値を上書きする。 |
| `status` | String | `REDEEMED` や`UNREDEEMED` など、クーポンの現在のステータス。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

### ステップ1:BrazeのWebhookテンプレートを作成する

今後のキャンペーンやCanvasで使用するPassKitウェブフックテンプレートを作成するには、Brazeダッシュボードの「**テンプレート＆メディア」**セクションに移動する。単発のPassKitウェブフックキャンペーンを作成する場合、または既存のテンプレートを使用する場合は、新しいキャンペーンを作成する際にBrazeで**ウェブフックを**選択する。

PassKitウェブフック・テンプレートを選択すると、以下のように表示される：
- **ウェブフックのURL**： `https://api-pub1.passkit.io/coupon/singleUse/coupon`
- **リクエスト・ボディ**Raw Text

#### リクエストヘッダと方法

PassKitの認証には、Base64でエンコードされたPassKit APIキーを含む`HTTP Header` 。以下はすでにキーと値のペアとしてテンプレートに含まれているが、**Settings**タブでは、`<PASSKIT_LONG_LIVED_TOKEN>` をあなたのPassKitトークンに置き換える必要がある。トークンを取得するには、PassKitプロジェクト/プログラムに移動し、**「設定」>「統合」>「Long Lived Token**」の順に移動する。

{% raw %}
- **HTTPメソッド**：プット
- **ヘッダーをリクエストする**：
  - **認可する**：ベアラー `<PASSKIT_LONG_LIVED_TOKEN>`
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

## コネクテッド・コンテンツでパスの詳細を取得する

パスの作成と更新に加え、Brazeの\[Connected Content][15] ] を介してユーザーのパスメタデータを取得し、メッセージングキャンペーンにパーソナライズされたパスの詳細を組み込むこともできる。

**PassKitコネクテッド・コンテンツ・コール**

{% raw %}
```liquid
{% connected_content  https://api-pub1.passkit.io/coupon/singleUse/coupon/externalId/{{${user_id}}} :headers {"Authorization": "Bearer <PASSKIT_LONG_LIVED_TOKEN>","Content-Type": "application/json"} :save passes %}

{{passes.status}} 
```
{% endraw %}

**液体の回答例**

{% tabs ローカル %}
{% tab {{passes.redemptionDetails}} %}

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
{% tab {{passes.status}} %}
```
UNREDEEMED 
```
{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/passkit/passkit1.png %}
[2]: {% image_buster /assets/img/passkit/passkit2.png %}
[3]: https://dev.bitly.com/v4/#operation/createFullBitlink
[4]: {% image_buster /assets/img/passkit/passkit4.png %}
[5]: {% image_buster /assets/img/passkit/passkit5.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints
[7]: {{site.baseurl}}/api/endpoints/user_data/#user-track-endpoint
[8]: https://help.passkit.com/en/articles/3742778-hashed-smartpass-links
[9]: {{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#content-blocks
[10]: https://github.com/PassKit/smart-pass-link-from-csv-generator
[12]: https://docs.passkit.io/protocols/member/
[13]: https://docs.passkit.io/protocols/coupon/
[14]: https://docs.passkit.io/protocols/boarding/
[15]: {{site.baseurl}}/user_guide/パーソナライゼーションとダイナミックスcontent/connected_content/making_an_api_call/
[16]: https://en.wikipedia.org/wiki/HMAC
