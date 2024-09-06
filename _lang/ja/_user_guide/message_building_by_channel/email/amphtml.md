---
nav_title: メール用AMP
article_title: メール用AMP
alias: /amphtml/
page_order: 11
description: "このリファレンス記事は、メール用AMPの概要と一般的な使用例を提供します。"
channel:
  - email

---

# メールのためのAMP

> メール用[AMP<1>}を使用すると、メールにインタラクティブな要素を追加し、顧客とのコミュニケーションを向上させ、ユーザーの受信トレイに直接完全な体験を提供できます。AMPは、アンケート、フィードバック質問票、投票キャンペーン、レビュー、サブスクリプションセンターなどのエキサイティングなメール提供を構築するのに役立つさまざまなコンポーネントを使用することで、これを可能にします。このようなツールは、エンゲージメント向上とリテンションの機会を提供することができます。

## 要件

Brazeは、Googleで登録するユーザーや必要なセキュリティ要件を満たすことに対して責任を負いません。

| 要件   | 説明 |
| --------------| ----------- |
| AMPがメールでオンになりました | AMPは誰でも利用できます。この機能を有効にしたい場合は、アカウントマネージャーに連絡してください。 |
| Gmailアカウントイネーブルメント | [Gmailアカウントの有効化](#enabling-gmail-account)を参照してください。 |
| Google送信者認証 | Gmail [は送信者を認証します](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication) AMPメールのDKIM、SPF、およびDMARCを使用します。これらはあなたのアカウントに設定する必要があります。<br><br>[ドメインキー識別メール](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>[送信者ポリシーフレームワーク](https://en.wikipedia.org/wiki/Sender_Policy_Framework)(SPF)<br>[ドメインベースのメッセージ認証、報告、および適合](https://en.wikipedia.org/wiki/DMARC)(DMARC)
| AMP メール要素 | 説得力のあるAMPメールには、さまざまなコンポーネントの戦略的な使用が含まれます。以下の[コンポーネント](#components)セクションの必須タブを参照してください。 |
{: .reset-td-br-1 .reset-td-br-2}

### サポートされているクライアント

ユーザーにAMPメールを送信する前に、クライアントに登録する必要があります。登録プロセスには、承認を得るためにテストAMP HTMLメールを送信することが含まれます。承認時間はクライアントごとに異なります。詳細については、登録リンクに従ってください。

| クライアント | 登録リンク |
| ------ | -------- |
| Gmail | [グーグル](https://developers.google.com/gmail/ampemail/register) |
| フェアメール | [フェアメール](https://email.faircode.eu/) |
| ヤフー | [ヤフー](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

サポートされているプラットフォームの完全なリストについては、[AMPドキュメント](https://amp.dev/support/faq/email-support)を参照してください。 

### Gmailアカウントを有効にする

Gmailの設定に移動し、**ダイナミックなメールを有効にする**を**全般**の下で選択します。

![「ダイナミックなメールを有効にする」チェックボックスが選択されているGmail設定の例です。][1]

## API使用

また、APIを使用してメールにAMPを使用することもできます。Brazeの[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging/)を使用してメールを送信する場合は、以下に示すように`amp_body`をオブジェクト仕様として追加します。

### メール object specification

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

## AMPメールを作成する

まず、[コンポーネント](#components)を使用してAMPメールを作成します。次に、[Braze API](#api-usage)を使用してメッセージを送信し、AMP `amp_body` HTMLを含めるようにしてください。

AMP HTML に加えて、通常の HTML `body` バージョンが必要であり、AMP メールの `plaintext_body` バージョンを提案します。すべてのAMPメールはマルチパートで送信されます。つまり、BrazeはHTML、プレーンテキスト、およびAMP HTMLをサポートするメールを送信します。これは、メールがAMP for emailをまだサポートしていないプロバイダー経由で送信された場合に役立ちます。なぜなら、メールはユーザーとそのデバイスに基づいて適切なバージョンに自動的にデフォルトするからです。

{% alert note %}
AMPメールを作成する際には、AMPコードをHTMLエディタに追加しないように、AMPエディタにいることを確認してください。
{% endalert %}

これらの追加リソースを参照してください:

- [AMPチュートリアル](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [サンプルコード](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73)が最終製品の見た目を確認するためのものです。 
- [AMP メール components ライブラリー](https://amp.dev/documentation/components/?format=email/)

### コンポーネント

{% tabs %}
  {% tab 必需品 %}

これらはAMP HTML email...AMPを作るものです！これらの要素はすべて、AMPメールの本文に必要です。

| コンポーネント | 説明 | 例 |
|---------|--------------|---------|
| 識別 <br><br> `⚡4email` または `amp4email`| AMP HTML メールとしてメールを識別します。 | `<!doctype html>`<br> `<html ⚡4email>`<br> `<head>` |
| 読み込む AMP ランタイム <br><br> `<script>` | JavaScriptを使用して、AMPがメール内で機能するようにします。 | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSSボイラープレート | AMPが読み込まれるまでコンテンツを非表示にします。<br> AMP メールをサポートするメールプロバイダーは、クライアントで審査済みの AMP スクリプトのみが実行されるようにするセキュリティチェックを実施します。 | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

  {% endtab %}
  {% tab ダイナミックな %}

これらのコンポーネントを使用して、メールにダイナミックなレイアウトと動作を作成します。

| コンポーネント | 説明 | 必須スクリプト |
|---------|--------------|---------|
| [アコーディオン](https://amp.dev/documentation/components/amp-accordion?format=email)<br><br> `amp-accordion`| ユーザーがコンテンツの概要を表示し、任意のセクションにジャンプできるようにします。 | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [フォーム](https://amp.dev/documentation/components/amp-form?format=email)<br><br> `amp-form`| AMPドキュメントで入力フィールドを送信するフォームを作成します。 | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
ユーザーを認証する必要があるコンポーネントは、[Googleアクセス トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens)または[プロキシ アサーション トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}
  {% endtab %}
  {% tab クリエイティブ %}

  AMP のコンポーネントを使用して、メールをオーディエンスに合わせてカスタマイズしましょう。

| コンポーネント | 説明 | 必須スクリプト |
|---------|--------------|---------|
| [アニメーション画像](https://amp.dev/documentation/components/amp-anim?format=email)<br><br> `amp-anim`| ランタイムで管理されるアニメーション画像（通常はGIF）を表示します。 | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [カルーセル](https://amp.dev/documentation/components/amp-carousel?format=email)<br><br> `amp-carousel`| 水平方向に沿って複数の類似したコンテンツを表示します。 | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [画像](https://amp.dev/documentation/components/amp-img?format=email) | HTML `img` タグのランタイム管理された置き換え。<br>  また、画像の[ライトボックスを作成することもできます](https://amp.dev/documentation/components/amp-image-lightbox?format=email)。 | `<amp-img alt="A view of the sea"`<br> `src="images/sea.jpg"`<br> `width="900"`<br>  `height="675"`<br>  `layout="responsive">` <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% alert note %}
ユーザーを認証する必要があるコンポーネントは、[Googleアクセス トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens)または[プロキシ アサーション トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}

  {% endtab %}
  {% tab 他の %}

| コンポーネント | 説明 |
|---------|--------------|
| [データバインディングと式](https://amp.dev/documentation/components/amp-anim?format=email)<br><br> `amp-bind`| データバインディングとJavaScriptのような式を介して、AMPページにカスタムのステートフルなインタラクティビティを追加します。 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
ユーザーを認証する必要があるコンポーネントは、[Googleアクセス トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens)または[プロキシ アサーション トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}

{% endtab %}
{% endtabs %}

AMPコンポーネントの完全なリストについては、[AMPドキュメント](https://amp.dev/documentation/components/?format=email)を確認してください。  

### ユースケース

{% tabs local %}
{% tab インタラクティブアンケート %}

`<amp-form>`コンポーネントを使用すると、メール受信トレイを離れることなく完了できるインタラクティブなアンケートを作成できます。これは、`<amp-form>`を使用して調査の回答を送信し、その後バックエンドがこの集計データを提供することによって行うことができます。 

いくつかの例が含まれます:
* カンファレンス調査メール
* フィード内のアイテムを動的に更新する
* 記事ブックマークメール

このコンポーネントを使用すると、ユーザーはフィールド値を送信またはクリアできます。また、メールの設定方法によっては、調査の送信が成功したかどうかなど、ユーザーに追加のプロンプトを表示したり、ユーザーからの回答を表示して調査の結果（投票キャンペーンなど）を表示することができます。

{% endtab %}
{% tab 折りたたみ可能なコンテンツ %}

`<amp-accordion>`コンポーネントを使用してコンテンツセクションを拡張します。このコンポーネントを使用すると、折りたたみ可能および展開可能なコンテンツセクションを表示でき、視聴者がコンテンツの概要を一目で確認し、任意のセクションにジャンプする方法を提供します。 

長い教育記事やパーソナライズされたおすすめを送る傾向がある場合、これにより視聴者はコンテンツの概要を一目で確認し、任意のセクションや特定の製品のおすすめにジャンプして詳細を得ることができます。これは、セクションに数文を入力するだけでもスクロールが必要なモバイルユーザーにとって特に役立ちます。
{% endtab %}
{% tab 画像 Heavy Emails %}

小売ブランドのように多くのプロフェッショナルな写真を含むメールを送信する傾向がある場合、ユーザーが自分に訴求する画像と対話できる`<amp-image-lightbox>`コンポーネントを使用できます。ユーザーが画像をクリックすると、このコンポーネントはメッセージの中央に画像を表示し、ライトボックス効果を作成します。 

さらに、`<amp-image-lightbox>`コンポーネントにより、ユーザーは詳細な画像の説明を表示できます。同じコンポーネントを複数の画像に使用できます。例えば、メールに複数の画像が含まれている場合、ユーザーがどちらかの画像をクリックすると、画像がライトボックスに表示されます。

{% endtab %}
{% tab フォント駆動のメール %}

テキストコピーに主に依存するメールの場合、`<amp-fit-text>`コンポーネントを使用すると、指定された領域内のテキストのサイズとフィット感を管理できます。

例としては次のようなものがあります:

- テキストをエリアに合わせて拡大縮小する
- テキストをエリアに合わせてスケーリングし、最大フォントサイズを使用して最大フォントサイズを設定できます。
- コンテンツが領域を超えたときにテキストを切り捨てる

{% endtab %}
{% endtabs %}

### アンプ-ムスタッシュを使用する

Liquidと同様に、AMPはより高度なユースケースのためのスクリプト言語をサポートしています。このコンポーネントは[`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email)と呼ばれます。Liquidの[`raw`](https://shopify.github.io/liquid/tags/raw/)タグで囲む必要があります。LiquidとMustacheは構文スタイルを共有していることに注意してください。 

コンテンツを`raw`タグで囲むと、Braze処理エンジンは`raw`タグ間のコンテンツを無視し、チームが必要とするMustache変数を送信します。

## メトリクスと分析

| メートル法 | 詳細 |
|---|---|
| 開封数の合計 | AMPメールのHTMLおよびプレーンテキストバージョンの合計オープン数。 |
| クリック数の合計 | AMPメールのHTMLおよびプレーンテキストバージョンでの総クリック数。 |
| AMPが開く | AMP HTML メールおよび AMP HTML バージョンのメールの開封総数。 |
| AMP クリック数 | AMP HTML メールのクリック数の合計、HTML、プレーンテキスト、および AMP HTML バージョンのメールの累積数。 |
{: .reset-td-br-1 .reset-td-br-2}  

## テストとトラブルシューティング

総クリック数とユニーククリック数には、AMPメッセージから発生するクリックは含まれません（HTMLおよびプレーンテキストのみ）。AMP固有のクリックは*amp_click*メトリックに帰属します。

送信する前に、AMPメールをこれらの[Gmailガイドライン](https://developers.google.com/gmail/ampemail/testing-dynamic-email)に従ってテストすることをお勧めします。

AMPメールを任意のGmailアカウントに配信するには、メールが次の条件を満たしている必要があります:
- メールのセキュリティ要件のためのAMPを満たす必要があります。
- AMP MIMEパートには有効なAMPドキュメントが含まれている必要があります。
- メールにはHTML MIMEパートの前にAMP MIMEパートを含める必要があります。
- AMP MIME パートは 100 KB 未満である必要があります。

これらの条件のいずれもエラーを引き起こしていない場合は、\[サポート]\[support]に連絡してください。

### よくある質問

{% details AMPメールでセグメント化すべきですか？ %}
私たちは、すべての異なるタイプのユーザーに送信するためにセグメント化しないことを提唱しています。これは、元のメールに含まれる異なるバージョンを持つマルチパートでAMPメッセージを送信するためです。ユーザーがAMPバージョンを表示できない場合、デフォルトでHTMLに戻ります。
{% enddetails %}

{% details AMPメールを作成するための追加のヒントはありますか？ %}
AMP要素を構築するために、開発チームに確認してください。これらの要素が設定された後、デザインリソースや要素を追加して、さらに磨きをかけることをお勧めします。
{% enddetails %}

[1]: {% image_buster /assets/img/dynamic-content.png %}
\[support]: {{site.baseurl}}/support_contact/
