---
nav_title: メール用 AMP
article_title: メール用AMP
alias: /amphtml/
page_order: 11
description: "この記事では、メール用 AMP と一般的なユースケースの概要について説明します。"
channel:
  - email

---

# メール用 AMP

> メール用[AMP](https://amp.dev/about/email)を使用すると、メールにインタラクティブな要素を追加し、顧客とのコミュニケーションを向上させ、ユーザーの受信トレイに直接完全な体験を提供できます。AMP は、アンケート、フィードバック質問票、投票キャンペーン、レビュー、購読センターなど、エキサイティングなメールオファリングの作成に役立つさまざまなコンポーネントを使用することで、これを可能にします。このようなツールは、エンゲージメント向上とリテンションの機会を提供することができます。

## 要件

Brazeは、Googleで登録するユーザーや必要なセキュリティ要件を満たすことに対して責任を負いません。メール用 AMPは、SparkPost および SendGrid にのみ使用できます。

| 必要条件   | 説明 |
| --------------| ----------- |
| メール用 AMP がオンになっている | AMP はすべてのユーザーが利用できます。 |
| Gmail アカウントの有効化 | [Gmailアカウントの有効化](#enabling-gmail-account)を参照してください。 |
| Google送信者認証 | Gmail は DKIM、SPF、および DMARC を使用して AMP メールの[送信者を認証](https://developers.google.com/gmail/ampemail/security-requirements#sender_authentication)します。お客様のアカウントにこれらが設定されている必要があります。<br><br>- [ドメインキー識別メール](https://en.wikipedia.org/wiki/DomainKeys_Identified_Mail) (DKIM) <br>- [送信者ポリシーフレームワーク](https://en.wikipedia.org/wiki/Sender_Policy_Framework) (SPF)<br>- [ドメインベースのメッセージ認証、レポート、および準拠](https://en.wikipedia.org/wiki/DMARC) (DMARC)
| AMP メール要素 | 説得力のある AMP メールでは、さまざまなコンポーネントが戦略的に使用されます。以下の[コンポーネント](#components)セクションの必須タブを参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### サポートされている電子メールクライアント

AMP メールをユーザーに送信する前に、メールクライアントに登録する必要があります。登録プロセスには、承認を得るためにテストAMP HTMLメールを送信することが含まれます。承認の所要時間はクライアントごとに異なります。詳細については、登録リンクを参照してください。

| クライアント | 登録リンク |
| ------ | -------- |
| Gmail | [Google](https://developers.google.com/gmail/ampemail/register) |
| FairEmail | [FairEmail](https://email.faircode.eu/) |
| ヤフー | [ヤフー](https://senders.yahooinc.com/amp/) |
| Mail.ru | [Mail.ru](https://postmaster.mail.ru/amp/) |

サポートされている電子メールクライアントの完全なリストについては、[AMPドキュメント](https://amp.dev/support/faq/email-support)を参照してください。

### Gmailアカウントを有効にする

Gmailの設定に移動し、**ダイナミックなメールを有効にする**を**全般**の下で選択します。

![「ダイナミックなメールを有効にする」チェックボックスが選択されているGmail設定の例です。]({% image_buster /assets/img/dynamic-content.png %})

## API使用

また、APIを使用してメールにAMPを使用することもできます。Brazeの[メッセージングエンドポイント]({{site.baseurl}}/api/endpoints/messaging/)を使用してメールを送信する場合は、以下に示すように`amp_body`をオブジェクト仕様として追加します。

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

まず、[コンポーネント](#components)を使用して AMP メールを作成します。次に、[Braze API](#api-usage) を使用してメッセージを送信します。AMP HTML の `amp_body` を必ず含めてください。

AMP HTML に加えて、通常の HTML `body` バージョンが必要です。AMP メールの `plaintext_body` バージョンをお勧めします。すべてのAMPメールはマルチパートで送信されます。つまり、BrazeはHTML、プレーンテキスト、およびAMP HTMLをサポートするメールを送信します。これは、メール用 AMP をまだサポートしていないプロバイダー経由でメールが送信された場合に役立ちます。なぜなら、メールはユーザーとそのデバイスに基づいて適切なバージョンに自動的にデフォルト設定されるからです。

{% alert note %}
AMPメールを作成する際には、AMPコードをHTMLエディタに追加しないように、AMPエディタにいることを確認してください。
{% endalert %}

これらの追加リソースを参照してください:

- [AMP チュートリアル](https://amp.dev/documentation/guides-and-tutorials/start/create_email?format=email)
- [サンプルコード](https://gist.github.com/CrystalOnScript/988c3f0a2eb406da27e9d9bf13a8bf73)が最終製品の見た目を確認するためのものです。 
- [AMP メールコンポーネントライブラリ](https://amp.dev/documentation/components/?format=email/)

### コンポーネント

AMP 要素を作成する際には、エンジニアリングチームに連絡し、さらに洗練させるためのデザインリソースと要素を含めることをお勧めします。

{% tabs %}
  {% tab Essentials %}

これらの要素はすべて、AMPメールの本文に必要です。

| コンポーネント | 説明 | 例 |
|---------|--------------|---------|
| 識別 <br><br> `⚡4email` または `amp4email`| メールを AMP HTML メールとして識別します。 | `<!doctype html>`<br> `<html ⚡4email>`<br> `<head>` |
| 読み込む AMP ランタイム <br><br> `<script>` | JavaScriptを使用してAMPをメール内で実行できるようにする。 | `<script async src="https://cdn.ampproject.org/v0.js"></script>`|
| CSSボイラープレート | AMPが読み込まれるまでコンテンツを非表示にします。<br> AMP メールをサポートするメールプロバイダーは、クライアントで審査済みの AMP スクリプトのみが実行されるように、セキュリティチェックを実施します。 | `<style amp4email-boilerplate>body{visibility:hidden}</style>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

  {% endtab %}
  {% tab Dynamic %}

これらのコンポーネントを使用して、メールにダイナミックなレイアウトと動作を作成します。

| コンポーネント | 説明 | 必須スクリプト |
|---------|--------------|---------|
| [アコーディオン](https://amp.dev/documentation/components/amp-accordion?format=email)<br><br> `amp-accordion`| ユーザーがコンテンツの概要を表示し、任意のセクションにジャンプできるようにします。 | `<script async custom-element="amp-accordion" src="https://cdn.ampproject.org/v0/amp-accordion-0.1.js"></script>` |
| [フォーム](https://amp.dev/documentation/components/amp-form?format=email)<br><br> `amp-form`| AMPドキュメントで入力フィールドを送信するフォームを作成します。 | `<script async custom-element="amp-form" src="https://cdn.ampproject.org/v0/amp-form-0.1.js"></script>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
ユーザーの認証を必要とするコンポーネントは、[Google アクセス トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens)または[プロキシアサーショントークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}
  {% endtab %}
  {% tab Creative %}

  お客様のメールをオーディエンスに届けるのに役立つ AMP のクリエイティブなコンポーネントの使用をお勧めします。

| コンポーネント | 説明 | 必須スクリプト |
|---------|--------------|---------|
| [アニメーション画像](https://amp.dev/documentation/components/amp-anim?format=email)<br><br> `amp-anim`| ランタイムで管理されるアニメーション画像（通常はGIF）を表示します。 | `<script async custom-element="amp-anim" src="https://cdn.ampproject.org/v0/amp-anim-0.1.js"></script>` |
| [カルーセル](https://amp.dev/documentation/components/amp-carousel?format=email)<br><br> `amp-carousel`| 水平方向に沿って複数の類似したコンテンツを表示します。 | `<script async custom-element="amp-carousel" src="https://cdn.ampproject.org/v0/amp-carousel-0.1.js"></script>` |
| [画像](https://amp.dev/documentation/components/amp-img?format=email) | HTML `img` タグのランタイム管理された置き換え。<br>  また、画像の[ライトボックスを作成することもできます](https://amp.dev/documentation/components/amp-image-lightbox?format=email)。 | `<amp-img alt="A view of the sea"`<br> `src="images/sea.jpg"`<br> `width="900"`<br>  `height="675"`<br>  `layout="responsive">` <br> `</amp-img>` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
ユーザーの認証を必要とするコンポーネントは、[Google アクセス トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens)または[プロキシアサーショントークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}

  {% endtab %}
  {% tab Other %}

| コンポーネント | 説明 |
|---------|--------------|
| [データバインディングと式](https://amp.dev/documentation/components/amp-anim?format=email)<br><br> `amp-bind`| データバインディングと JavaScript 風の式を介して、AMP ページにカスタムのステートフルなインタラクティビティを追加します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
ユーザーの認証を必要とするコンポーネントは、[Google アクセス トークン](https://developers.google.com/gmail/ampemail/authenticating-requests#access_tokens)または[プロキシアサーショントークン](https://developers.google.com/gmail/ampemail/authenticating-requests#proxy_assertion_tokens)を使用する必要があります。
{% endalert %}

{% endtab %}
{% endtabs %}

AMP コンポーネントの完全なリストについては、[AMP のドキュメント](https://amp.dev/documentation/components/?format=email)を確認してください。  

### ユースケース

{% tabs local %}
{% tab Interactive Surveys %}

`<amp-form>` コンポーネントを使用すると、メール受信トレイを離れずに行えるインタラクティブなアンケートを作成できます。これは、`<amp-form>` を使用して調査の回答を送信し、その後バックエンドがこの集計データを提供することによって行うことができます。 

例としては次のようなものがあります。
* 会議のアンケートメール
* フィード内のアイテムを動的に更新する
* 記事ブックマークメール

このコンポーネントを使用すると、ユーザーはフィールド値を送信したりクリアしたりできます。また、メールの設定によっては、アンケートの送信が成功したかどうかなど、ユーザーに追加のプロンプトを表示したり、アンケート結果を示すユーザーからのレスポンスをレンダリングしたりすることもできる（投票キャンペーンなど）。

{% endtab %}
{% tab Collapsable Content %}

`<amp-accordion>` コンポーネントを使用してコンテンツのセクションを展開表示します。このコンポーネントを使用すると、折りたたみと展開が可能なコンテンツセクションを表示でき、オーディエンスはコンテンツの概要を一目で確認し、任意のセクションにジャンプできるようになります。 

長い教育記事やパーソナライズされたおすすめを送る傾向がある場合、これにより視聴者はコンテンツの概要を一目で確認し、任意のセクションや特定の製品のおすすめにジャンプして詳細を得ることができます。これは、セクションに数行を入力するだけでもスクロールが必要なモバイルユーザーにとって特に便利です。
{% endtab %}
{% tab Image Heavy Emails %}

小売（店）ブランドのようにプロフェッショナルな写真を多用したメールを送信する傾向がある場合は、`<amp-image-lightbox>` 、ユーザーが魅力的な画像にエンゲージメントできるコンポーネントを利用できる。ユーザーが画像をクリックすると、このコンポーネントはメッセージの中央に画像を表示し、ライトボックス効果を作成します。 

さらに、`<amp-image-lightbox>` コンポーネントを使用すると、ユーザーは画像の詳細な説明を表示できます。同じコンポーネントを複数の画像に使用することができます。例えば、メールに複数の画像が含まれている場合、ユーザーがどちらかの画像をクリックすると、画像がライトボックスに表示されます。

{% endtab %}
{% tab Font Driven Emails %}

主にテキストコピーに依存するメールの場合、`<amp-fit-text>` コンポーネントを使用すると、指定した領域内のテキストのサイズとフィットを管理できます。

例としては次のようなものがあります:

- テキストをエリアに合わせて拡大縮小する
- テキストをエリアに合わせてスケーリングし、最大フォントサイズを使用して最大フォントサイズを設定できます。
- コンテンツが領域を超えたときにテキストを切り捨てる

{% endtab %}
{% endtabs %}

### amp-mustache の使用

Liquidと同様に、AMPはより高度なユースケースのためのスクリプト言語をサポートしています。このコンポーネントは [`amp-mustache`](https://amp.dev/documentation/components/amp-mustache/?format=email) と呼ばれます。Mustache マークアップ言語を含める場合、これを Liquid の [`raw`](https://shopify.github.io/liquid/tags/raw/) タグで囲む必要があります。LiquidとMustacheは構文スタイルを共有していることに注意してください。 

コンテンツを`raw`タグで囲むと、Braze処理エンジンは`raw`タグ間のコンテンツを無視し、チームが必要とするMustache変数を送信します。

## メトリクスと分析

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>詳細</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split">開封数の合計</td>
            <td class="no-split">AMP メールの場合、これはHTML およびプレーンテキストバージョンの合計オープン数です。</td>
        </tr>
        <tr>
            <td class="no-split">クリック数の合計</td>
            <td class="no-split">AMP メールの場合、これはHTML およびプレーンテキストバージョンのクリックの合計です。</td>
        </tr>
        <tr>
            <td class="no-split">AMPが開く</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Opens' %}</td>
        </tr>
        <tr>
            <td class="no-split">AMP クリック数</td>
            <td class="no-split">{% multi_lang_include analytics/metrics.md metric='AMP Clicks' %}</td>
        </tr>
    </tbody>
</table>

## テストとトラブルシューティング

総クリック数とユニーククリック数には、AMPメッセージから発生するクリックは含まれません（HTMLおよびプレーンテキストのみ）。AMP特有のクリックはアトリビューションに属性される。 *amp_click*メトリックに起因する。

送信する前に、AMPメールをこれらの[Gmailガイドライン](https://developers.google.com/gmail/ampemail/testing-dynamic-email)に従ってテストすることをお勧めします。

AMP メールを任意の Gmail アカウントに配信するには、メールが次の条件を満たしている必要があります。

- メールのセキュリティ要件のための AMP を満たしていること。
- AMP MIMEパートには有効なAMPドキュメントが含まれている必要があります。
- メールの HTML MIME 部分の前に AMP MIME 部分が含まれていること。
- AMP MIME パートは 100 KB 未満である必要があります。

いずれの条件でもエラーが発生しない場合は、[サポートに]({{site.baseurl}}/support_contact/)連絡すること。

### よくある質問

#### AMP メールをセグメント化する必要がありますか?

私たちは、すべての異なるタイプのユーザーに送信するためにセグメント化しないことを提唱しています。これは、元のメールに含まれる異なるバージョンを持つマルチパートでAMPメッセージを送信するためです。ユーザーがAMPバージョンを表示できない場合、デフォルトでHTMLに戻ります。


