---
nav_title: Just Words
article_title: Just Words
description: "このリファレンス記事では、AIベースのSaaSビジネスプラットフォームであるBrazeとJust Wordsのパートナーシップについて概説します。このビジネスプラットフォームは、既存のキャンペーンのパーソナライズされたバージョンを作成し、サブジェクトライン、クリエイティブコンテンツ、HTMLメールレイアウトを時間の経過とともに最適化します。"
alias: /partners/just_words/
page_type: partner
---

# Just Words 統合ガイド

> [Just Words](https://www.justwords.ai/) は、ライフサイクルマーケティングチャネルのメッセージングを大規模にパーソナライズし、何百ものバリエーションをダイナミックな方法でテストし、パフォーマンスの低いコンテンツを自動的に更新します。

Just Words と Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/) を使用して既存の Braze キャンペーンとキャンバスをパーソナライズする場合、Just Words は Braze Currents を使用してコンテンツをダイナミックに最適化します。そのためユーザーが行う必要はありません。

## メリットは何でしょうか。

統合が完了したら、Just Works プラットフォームを活用して次の操作を実行できます。

- リアルタイムの実験結果を確認する
- コピーを動的に編集する
- パフォーマンスインサイトの表示

{% alert note %}
ご質問はありますか?[予約ページ](https://www.justwords.ai/book-demo)または共有 Slack チャネルから Just Words にお問い合わせください。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
|---|---|
| Just Words アカウント | このパートナーシップを活用するには、[Just Words](https://www.justwords.ai/)アカウントが必要です。Just Words アカウントをお持ちでない場合は、[30 分のオンボーディングコール](https://www.justwords.ai/book-demo)をスケジュールしてください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Just Words と Braze の統合

### ステップ 1: Just Words テンプレートの作成

1. Just Words コンソールに移動し、[新しいテンプレートを作成します](https://console.justwords.ai/new)。
2. 文字、数字、アンダースコアのみを使用する覚えやすいID を選択します。
3. キャンペーンの基本的な詳細を入力します。
4. AI を使用してパーソナライズされたバリエーションを生成します。

![Just Words テンプレート作成プラットフォーム。]({% image_buster /assets/img/just_words/creation_interface.png %}){: style="max-width:80%;"}

### ステップ2: Just Words API キーの作成

1. [**Org 設定**] > [**API キー**] < [**API キーを生成**] を選択します。
2. API キーを安全な場所にコピーして保存します。

![Just Words API キーフォーム。]({% image_buster /assets/img/just_words/api_key_form.png %}){: style="max-width:80%;"}

### ステップ 3: Braze コンテンツで Just Words を使用する

Connected Content を使用して、Just Words がキャンバスやキャンペーンと連携します。キャンバスを作成する場合、各メールステップは一意の単語のみのテンプレートに対応する必要があります。

#### ステップ 3.1:A/B テストのセットアップ

{% tabs %}
{% tab キャンバス %}

1. キャンバスで、[**Add Variant**] > [**Add Variant**] を希望するバリアント数になるまで選択し、各バリアントにステップを追加します (メールメッセージステップなど)。
2. 必要に応じてオーディエンスのトラフィックを分割します。たとえば、2 つのバリアントがある場合、それぞれに 50% を与えることができます。または、2 つのバリアントをそれぞれ 40%、コントロールグループを 20% 持つこともできます。キャンバスのA/Bテストの詳細については、[キャンバスの作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)を参照してください。
3. Connected Content で使用するメッセージステップのコンポーザーで、Just Words Console から取得した Connected Content スニペット (以下のようなスニペットです) を貼り付けてください。

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

![Braze A/B テストキャンバス設定。]({% image_buster /assets/img/just_words/braze_canvas.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab キャンペーン %}

1. キャンペーンの [**メッセージ作成**] ステップで、2 つのバリアントを作成します。
2. [**ターゲットオーディエンス**] ステップで、[**AB テスト**] セクションに移動し、各バリアント (およびオプションのコントロールグループ) を受信するユーザーの割合を変更します。最適化オプションを選択すると、テストをさらにカスタマイズできます。キャンペーンのA/Bテストの詳細については、[多変量およびA/Bテストの作成]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/)を参照してください。
3. メッセージ作成画面で、次のスニペットなど、Just Words Console のConnected Content スニペットを貼り付けます。

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

{% endtab %}
{% endtabs %}

#### ステップ 3.2: カスタム属性を使用したパーソナライズの追加 (オプション)

カスタム属性(`industry` など) を使用してメッセージをカスタマイズするには、次のリキッド形式を使用します。

{% raw %}
```liquid
{% connected_content https://worker.justwords.ai/api/generate/just-words?template_id=<test_id>&user_id={{${user_id}}}&attrs.industry={{ custom_attribute.industry }}
  :save jw
  :headers {
    "x-api-key": <jw_api_key>,
    "Content-Type": "application/json"
  }
%}

{{jw.copy.vars.cta}}
{% message_extras :key copy_id :value {{jw.copy.id }} %}
```
{% endraw %}

`industry` のカスタム属性は、{% raw %}```&attrs.industry={{ custom_attribute.industry }}```{% endraw %} で示されます。 

![HTML メッセージ作成画面の Braze Liquid ロジック。]({% image_buster /assets/img/just_words/just_words_personalization.png %}){: style="max-width:80%;"}

### ステップ 4: メールをプレビューする

Braze でメールをプレビューして、パーソナライズされたコンテンツが正しくレンダリングされていることを確認してください。

![Just Words メールのの Braze メッセージプレビュー]({% image_buster /assets/img/just_words/just_words_preview.png %}{: style="max-width:80%;"}

### ステップ 5: Braze Currents の設定

Braze Currents により、時間の経過に伴うパフォーマンスの追跡と最適化が可能になります。

1. Braze で、[**パートナー連携**] > [**データエクスポート**] に移動します。
2. [**Create New Test Current**] を選択し、[**Test Amazon S3 Data Export**] を選択します。

![[Create New Test Current] ドロップダウンと [Test Amazon S3 Data Export] オプション。]({% image_buster /assets/img/just_words/test_amazon_s3.png %}){: style="max-width:80%;"}

{: start="3" }
3\.オンボーディング時に Just Words によって提供された S3 アクセス ID、AWS シークレットアクセスキー、バケット名、およびフォルダを入力します。

![AWS シークレットアクセスキーの「認証情報」セクション。]({% image_buster /assets/img/just_words/aws_secret_access_key.png %}){: style="max-width:80%;"}

{: start="4" }
4\.送信数、開封数、クリック数、購読解除数、コンバージョン数など、追跡するイベントを選択します。

![選択するイベントを含む「メッセージエンゲージメントイベント」セクション。]({% image_buster /assets/img/just_words/message_engagement_events.png %}){: style="max-width:80%;"}

{: start="5" }
5\.Braze Current を開始します。

すべて完了しました。Braze Connected Content で Just Words を使用できるようになりました。