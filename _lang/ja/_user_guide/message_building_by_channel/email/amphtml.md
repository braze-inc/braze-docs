---
nav_title: AMP for Email
article_title: AMP for Email
alias: /amphtml/
page_order: 11
description: "このリファレンス記事では、AMP for Email の概要と一般的な使用例について説明します。"
channel:
  - email

---

# メール向け AMP

> [メール向け AMP](https://amp.dev/about/email) を使用すると、メールにインタラクティブな要素を追加して顧客とのコミュニケーションを向上させ、ユーザーの受信トレイに直接完全なエクスペリエンスを提供できます。AMP は、アンケート、フィードバックアンケート、投票キャンペーン、レビュー、サブスクリプション センターなど、魅力的なメールサービスを構築するために使用できるさまざまなコンポーネントを使用することで、これを可能にします。このようなツールは、エンゲージメントとリテンションを高める機会を提供することができます。

## 要件

Brazeは、ユーザーがGoogleに登録したり、必要なセキュリティ要件を満たしたりすることについて責任を負いません。

|応募資格 |説明 |
| --------------| ----------- |
|AMP for email がオンになっている |AMP はどなたでもご利用いただけます。この機能を有効にすることに関心がある場合は、アカウントマネージャーにお問い合わせください。|
|Gmail アカウントの有効化 | [「Gmail アカウントの有効化](#enabling-gmail-account)」を参照してください。|
|Google 送信者認証 |Gmail では、AMP メールの [送信者を](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) DKIM、SPF、DMARC で認証します。これらはアカウントに設定する必要があります。<br><br>- [DKIM(Domain Keys Identified Mail) (ドメインキー識別メール](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM)) <br>- [送信者ポリシーフレームワーク](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>- [ドメインベースのメッセージ認証、レポート、および準拠](https://en.wikipedia.org/wiki/DMARC)(DMARC)
|AMP メール要素 |説得力のあるAMPメールには、さまざまなコンポーネントの戦略的な使用が含まれています。以下の「 [コンポーネント](#components) 」セクションの「要点」タブを参照してください。|
{: .reset-td-br-1 .reset-td-br-2}

### サポートされているクライアント

AMPメールをユーザーに送信する前に、クライアントに登録する必要があります。登録プロセスでは、テスト用の AMP HTML メールを送信して承認を受けます。承認時間はクライアントごとに異なります。詳細については、登録リンクをたどってください。

|クライアント |登録リンク |
| ------ | -------- |
|Gmailの | [グーグル](https://developers.google.com/gmail/ampemail/register) |
|フェアメール | [フェアメール](https://email.faircode.eu/) |
|ヤフー | [ヤフー](https://senders.yahooinc.com/amp/) |
|Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

サポートされているプラットフォームの完全なリストについては、 [AMP のドキュメント](https://amp.dev/support/faq/email-support)を参照してください。 

### Gmailアカウントの有効化

Gmailの設定に移動し、[**全般**]で[**動的メールを有効にする**]を選択します。

![[動的メールを有効にする] チェックボックスをオンにした Gmail の設定例。[1]

## API の使用状況

また、AMP for email を API で使用することもできます。Braze [Messagingエンドポイント]({{site.baseurl}}/api/endpoints/messaging/) のいずれかを使用して電子メールを送信する場合は、以下に示すようにオブジェクト仕様として追加 `amp_body` します。

### メールオブジェクトの指定

```json
{
  "app_id": (required, string) see app identifier above,
  "subject": (optional, string),
  "from": (required, valid email address in the format "Display Name <email@address.com>"),
  "reply_to": (optional, valid email address in the format "email@address.com" - defaults to your workspace's default reply to if not set),
  "plaintext_body": (optional, valid plaintext, defaults to autogenerating plaintext from "body" when this is not set),
  "amp_body": (optional, updates the text-amp-html MIME type) the email body in AMP HTML. The MIME (Multipurpose Internet Mail Extensions) type to be referenced is "text/x-amp-html",
  "body": (required unless email_template_id is given, valid HTML),
  "preheader": (optional*, string) Recommended length 50-100 characters,
  "email_template_id": (optional, string) If provided, we will use the subject/body/should_inline_css values from the given email template UNLESS they are specified here, in which case we will override the provided template,
  "message_variation_id": (optional, string) used when providing a campaign_id to specify which message variation this message should be tracked under,
  "extras": (optional, valid key-value hash), extra hash - for SendGrid customers, this will be passed to SendGrid as Unique Arguments,
  "headers": (optional, valid key-value hash), hash of custom extensions headers. Currently, only supported for SendGrid customers,
  "should_inline_css": (optional, boolean), whether to inline CSS on the body. If not provided, falls back to the default CSS inlining value for the workspace,
  "attachments": (optional, array), array of JSON objects like [{"file_name","url"}] that define the files you need attached. Your file name's extension will be detected automatically from the URL, which should return the appropriate `Content-Type` as a response header,
}
```

## AMP メールの作成

まず、 [コンポーネント](#components)を使用して AMP メールを作成します。次に、 [Braze API](#api-usage) を使用してメッセージを送信し、AMP HTMLに必ず含め `amp_body` ます。

AMP HTML に加えて、通常の HTML `body` バージョンが必要であり、AMP メールのバージョンを提案し `plaintext_body` ます。すべてのAMPメールはマルチパートで送信されるため、BrazeはHTML、プレーンテキスト、AMP HTMLをサポートするメールを送信します。これは、メールが AMP for email をまだサポートしていないプロバイダ経由で送信された場合に、ユーザーとそのデバイスに基づいてメールが自動的に適切なバージョンにデフォルト設定されるため便利です。

{% alert note %}
AMP メールを作成するときは、AMP コードを HTML エディターに追加しないように、AMP エディターを使用していることを確認してください。
{% endalert %}

次の追加リソースを参照してください。

- [AMP チュートリアル](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- 最終製品がどのように見えるかを確認するための[サンプルコード](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73)。 
- [AMP メール コンポーネント ライブラリ](https://amp.dev/documentation/components/?format=email/)

### コンポーネント

{% tabs %}
  {% tab Essentials %}

AMP HTML メールの作成方法は次のとおりです。AMP'ed!これらの各要素は、AMP メールの本文に必要です。

|コンポーネント |説明 |例え |
|---------|--------------|---------|
|識別 <br><br> `⚡4email` または `amp4email`|メールを AMP HTML メールとして識別します。| `<!doctype html>`<br> `<html ⚡4email>`<br> `<head>` |
|AMP ランタイムの読み込み <br><br> `<script>` |AMP が JavaScript を使用してメール内で楽しめるようにします。| `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
|CSS ボイラープレート |AMP が読み込まれるまでコンテンツを非表示にします。<br> AMP メールをサポートするメールプロバイダーは、精査された AMP スクリプトのみをクライアントで実行できるようにするセキュリティチェックを実施します。| `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

  {% endtab %}
  {% tab Dynamic %}

これらのコンポーネントを使用して、Eメールに動的なレイアウトと動作を作成します。

|コンポーネント |説明 |必要なスクリプト |
|---------|--------------|---------|
| [アコーディオン](https://amp.dev/documentation/components/amp-accordion?format=email)<br><br> `amp-accordion`|ユーザーはコンテンツの概要を表示し、任意のセクションにジャンプできます。| `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [フォーム](https://amp.dev/documentation/components/amp-form?format=email)<br><br> `amp-form`|AMP ドキュメントで入力フィールドを送信するためのフォームを作成します。| `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
ユーザーの認証を必要とするコンポーネントでは [、Google アクセス トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) または [プロキシ アサーション トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  AMP のコンポーネントを気に入って、オーディエンスにメールを配信しましょう。

|コンポーネント |説明 |必要なスクリプト |
|---------|--------------|---------|
| [アニメーション画像](https://amp.dev/documentation/components/amp-anim?format=email)<br><br> `amp-anim`|ランタイムで管理されるアニメーション画像(通常はGIF)を表示します。| `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [回転木馬](https://amp.dev/documentation/components/amp-carousel?format=email)<br><br> `amp-carousel`|複数の類似したコンテンツを横軸に沿って表示します。| `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [画像](https://amp.dev/documentation/components/amp-img?format=email) |ランタイム管理で HTML `img` タグを置き換えるもの。<br>  [画像用のライトボックス](https://amp.dev/documentation/components/amp-image-lightbox?format=email)を作成することもできます。| `<amp-img alt="A view of the sea"`<br> `src="images/sea.jpg"`<br> `width="900"`<br>  `height="675"`<br>  `layout="responsive">` <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
ユーザーの認証を必要とするコンポーネントでは [、Google アクセス トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) または [プロキシ アサーション トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}

  {% endtab %}
  {% tab Other %}

|コンポーネント |説明 |
|---------|--------------|
| [データバインディングと式](https://amp.dev/documentation/components/amp-anim?format=email)<br><br> `amp-bind`|カスタム ステートフルなインタラクティビティを、データ バインディングと JavaScript に似た式を使用して AMP ページに追加します。|
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
ユーザーの認証を必要とするコンポーネントでは [、Google アクセス トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens) または [プロキシ アサーション トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}

{% endtab %}
{% endtabs %}

AMP コンポーネントの完全なリストについては、 [AMP のドキュメント](https://amp.dev/documentation/components/?format=email)をご覧ください。  

### ユースケース

{% tabs local %}
{% tab Interactive Surveys %}

この `<amp-form>` コンポーネントを使用すると、メールの受信トレイを離れることなく完了できるインタラクティブな調査を作成できます。これは、 を使用して `<amp-form>` アンケート回答を送信し、バックエンドにこの集計データを提供してもらうことで実現できます。 

たとえば、次のようなものがあります。
\*会議アンケートメール
\*フィード内のアイテムを動的に更新する
\*記事のブックマークメール

このコンポーネントを使用して、ユーザーはフィールド値を送信またはクリアできます。また、メールの設定方法によっては、アンケートの送信が成功したかどうかなどの追加のプロンプトをユーザーに表示したり、アンケートの結果を示すユーザーからの回答(投票キャンペーンなど)を表示したりできます。

{% endtab %}
{% tab Collapsable Content %}

コンポーネントを使用してコンテンツセクションを展開します `<amp-accordion>` 。このコンポーネントを使用すると、折りたたみ可能なコンテンツセクションと展開可能なコンテンツセクションを表示して、閲覧者がコンテンツの概要を一目で確認したり、任意のセクションにジャンプしたりできます。 

長い教育記事やパーソナライズされたレコメンデーションを送信する傾向がある場合、これにより、視聴者はコンテンツの概要を一目見て、セクションや特定の製品のレコメンデーションにジャンプして詳細を確認できます。これは、セクションに数文入るだけでもスクロールが必要なモバイルユーザーにとって特に役立ちます。
{% endtab %}
{% tab Image Heavy Emails %}

小売ブランドなど、プロの写真をたくさん使ってメールを送る傾向がある場合は、ユーザーが自分にアピールする画像でエンゲージできるコンポーネントを使用できます `<amp-image-lightbox>` 。ユーザーが画像をクリックすると、このコンポーネントによってメッセージの中央に画像が表示され、ライトボックス効果が作成されます。 

さらに、この `<amp-image-lightbox>` コンポーネントを使用すると、ユーザーは詳細な画像の説明を表示できます。複数の画像に同じコンポーネントを使用できます。たとえば、メールに複数の画像が含まれている場合、ユーザーがいずれかの画像をクリックすると、その画像がライトボックスに表示されます。

{% endtab %}
{% tab Font Driven Emails %}

主にテキストコピーに依存する電子メールの場合、コンポーネント `<amp-fit-text>` を使用すると、指定した領域内のテキストのサイズとフィットを管理できます。

たとえば、次のようになります。

- 領域に収まるようにテキストを拡大縮小する
- 最大フォントサイズを設定できる最大フォントサイズを使用して、領域に合わせてテキストを拡大縮小します
- コンテンツが領域からはみ出した場合のテキストの切り捨て

{% endtab %}
{% endtabs %}

### amp-mustache を使う

Liquid と同様に、AMP はより高度なユースケース向けのスクリプト言語をサポートしています。このコンポーネントは と呼ばれます [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email)。Mustacheマークアップ言語を含める場合は、Liquidのタグで [`raw`](https://shopify.github.io/liquid/tags/raw/) 囲む必要があります。Liquid と Mustache は構文のスタイルを共有していることに注意してください。 

コンテンツをタグで `raw` 囲むことで、Braze処理エンジンはタグ間の `raw` コンテンツを無視し、チームが必要とするMustache変数を送信します。

## メトリクスと分析

|メトリック |詳細 |
|---|---|
|合計開封数 |AMP E メールの HTML バージョンとプレーンテキストバージョンの合計開封数。|
|合計クリック数 |AMP メールの HTML バージョンとプレーンテキストバージョンの合計クリック数。|
|AMP が開く |AMP HTML メールと AMP HTML バージョンのメールの開封の合計数。|
|AMP クリック数 |AMP HTML メールの合計クリック数、メールの HTML、プレーンテキスト、AMP HTML バージョンの累積数。|
{: .reset-td-br-1 .reset-td-br-2}  

## テストとトラブルシューティング

合計クリック数とユニーククリック数には、AMP メッセージ(HTML とプレーンテキストのみ)から発生したクリックは考慮されません。AMP 固有のクリックは、 *amp\_click* 指標に関連付けられます。

AMP メールを送信する前に、 [Gmail のガイドライン](https://developers.google.com/gmail/ampemail/testing-dynamic-email)に沿ってテストすることをおすすめします。

AMP メールを Gmail アカウントに配信するには、メールが次の条件を満たしている必要があります。
\- AMP for email のセキュリティ要件を満たす必要があります。
\- AMP MIME パートには、有効な AMP ドキュメントが含まれている必要があります。
\- メールには、HTML MIME 部分の前に AMP MIME 部分を含める必要があります。
\- AMP MIME パートは 100 KB 未満にする必要があります。

これらの条件のいずれもエラーの原因でない場合は、[サポート][サポート]に連絡してください。

### よくある質問

{% details Should I segment with AMP emails? %}
セグメンテーションを行わないことで、すべての異なるタイプのユーザーに送信することをお勧めします。これは、AMP メッセージをマルチパートで送信し、元のメールに異なるバージョンが含まれているためです。ユーザーに AMP バージョンが表示されない場合は、デフォルトで HTML に戻ります。
{% enddetails %}

{% details Do you have any additional tips for building an AMP email? %}
エンジニアリングチームに相談して、AMP 要素を構築します。これらの要素を設定したら、デザインリソースと要素を追加して、さらに磨きをかけることをお勧めします。
{% enddetails %}

[1]: {% image_buster /assets/img/dynamic-content.png %}
[support]: {{site.baseurl}}/support_contact/
