---
nav_title: Lokalise
article_title: Lokalise
description: "この参考記事では、Brazeとアジャイルチーム向け翻訳管理サービスLokaliseのパートナーシップについて概説している。"
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> [Lokaliseは](https://lokalise.com)アジャイルチームのための翻訳管理サービスである。

_この統合は Lokalise によって管理されます。_

## 統合について

Brazeとロカリスの統合では、Connected Contentを使用して、ユーザーの設定sに基づいて翻訳されたコンテンツをBraze キャンペーンsに簡単に挿入できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Lokalise アカウント | このパートナーシップを活用するには、Lokalise アカウントが必要です。 |
| Lokalise 翻訳プロジェクト | この統合を設定する前に、Lokalise翻訳プロジェクトを作成する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### 新しい Lokalise プロジェクトを作成する

新しい翻訳プロジェクトを作成するには、Lokalise にログインして [**New Project**] を選択します。次に、プロジェクトに名前を付け、**ベース言語**（翻訳元の言語）を選択し、1つ以上の**ターゲット言語を**追加し、**ソフトウェアローカリゼーションプロジェクトタイプを**選択する。準備ができたら、[**Proceed**] をクリックします。

## 統合

Lokalise で、Braze で定義したコネクテッドコンテンツ変数ごとに翻訳キーを作成します。翻訳の準備ができたら、言語ごとに1つのJSONファイルを生成し、コネクテッド・コンテンツを提供するURLに公開することができる。

### ステップ1:ユーザー言語を設定する

まだ設定していない場合は、Braze ダッシュボードを開いて **[ユーザー] > [ユーザーインポート]** に移動します。ここで、ユーザーをインポートすることができる。インポート用のCSVファイルを準備する際には、ユーザーの言語を記載した言語カラムを必ず含めること。この言語フィールドは、後で翻訳を表示するときに使われる。 

{% alert important %}
使用する言語コードは、Braze と Lokalise の両方で一致している必要があります。
{% endalert %}
### ステップ2:Lokalise で翻訳を準備する

次に、Lokaliseで翻訳を準備するには、Braze Connected Content変数で使用しているのと同じ名前の翻訳キーを手動で作成する必要がある。 

例えば、単純な翻訳キー、`description` を作ってみよう：
1. Lokaliseプロジェクトを開いて [**Add Key**] をクリックし、[**Key**] フィールドに「description」と入力します。
2. **Base Language Value**フィールドに「Demo description」と入力する。
3. [**Platforms**] のドロップダウンに「Web」を追加します。 
4. 準備ができたら、[**Save**] をクリックします。

![]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

プロジェクトエディターに翻訳キーが表示されるはずだ：

![]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

#### 既知の問題

- キーが **Web** プラットフォームに割り当てられている必要があります。
- ピリオド（`.` ）や`_on` 文字列を含むキーの使用は避けること。たとえば、`this.is.the.key` の代わりに `this_is_the_key` を使用し、`join_us_on_instagram` の代わりに `join_us_instagram` を使用します。

### ステップ3:Lokalise で Braze アプリを設定する

Lokalise プロジェクトを開いて [**Apps**] をクリックします。ここで、Brazeアプリを検索してインストールする。以下の画面が表示される：

![Lokalise上のBraze設定には、プロジェクトIDと翻訳ファイルのURLが記載されている。]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

**翻訳ファイルURLでは**、Lokaliseは、プロジェクト内のキーのすべての翻訳を含むJSONファイルを公開する。プロジェクトにあるターゲット言語の数だけ、翻訳ファイルのURLが得られる。そのため、翻訳ファイルのURLは2つに分かれている：

1. URLパスの最初の部分はすべての言語に共通である。
2. URL末尾のJSONファイル名は、言語コードに基づいている。

翻訳ファイルのURLは、Brazeキャンペーンを設定する際に必要となるURLである。JSON ファイルのコンテンツを更新するには [**Refresh**] をクリックします。URL は変更されず、Braze でコネクテッドコンテンツ呼び出しを変更する必要がないことに注意してください。

### テストURL

このURLをテストするには、このURLをコピーし、{% raw %}`{{${language}}}`{% endraw %} を言語コード（たとえば、`en` ）に置き換えて、ブラウザでこのURLを開く。キーと翻訳を含むJSONファイルが表示される：

![]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

### ステップ 4: Braze キャンペーンで翻訳を使用する

#### コネクテッドコンテンツ呼び出しを挿入する

準備ができたら、Brazeに戻り、既存のキャンペーンを開くか、新しいキャンペーンを作成する。この例では、サンプルコンテンツで新しいメールキャンペーンを作成する。[**メール本文を編集**] をクリックします。

翻訳を挿入するには、ドキュメントの最上部または翻訳が必要な最初の位置の直前に、HTML 形式のコネクテッドコンテンツリクエストを追加する必要があります。これは、以下のマークアップを挿入することで可能になる：

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

`https://exports.live.lokalise.cloud/...` URLを、前のステップで取得した翻訳ファイルのURLに置き換える。

{% raw %}

- `{{${language}}}` は、「この位置にユーザー言語を挿入する」という意味です。あるいは、言語コードをハードコードすることもできる。例えば、`en.json` 。
  - 各ユーザに適切な翻訳JSONファイルが取得されるようにするには、`{{${language}}}` profile属性か、ユーザの言語を保持する別の同様のカスタム属性を翻訳ファイルのURLの最後に配置する必要がある。(例えば、`/{{${language}}}.json`) これらの属性に保持される値は、翻訳されたJSONファイルのそれぞれの接頭辞と一致しなければならない。これにより、各ユーザーに対して正しい翻訳ファイルが返されるようになる。
- `:save translations` により JSON コンテンツが translations 変数に保存されます。

#### 翻訳を表示する

ここでtranslations変数を使い、必要な翻訳をキーで表示する。

たとえば、`description` キーを表示するには `{{ translations.description }}` を使用します。

{% endraw %}
![]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

最後に、メールテンプレートを保存し、プレビューする。翻訳が表示されるはずです。

## よくある質問

### 誤って Lokalise からキーを削除した場合はどうなりますか?

Brazeの対応する文字列はもう翻訳を持たない。

### `en` ロケールを持っているが、Lokalise で`en-US` で上書きした場合、Braze`en-US` として読み込まれますか?

いいえ、ロケールの ISO コードは Braze と Lokalise で一致している必要があります。

### Lokalise コンテンツを接続するときに、`:rerender` フラグを使用できますか?

使用できます。このフラグの追加方法については、Brazeのドキュメントを参照されたい。

### ローカリスで翻訳ファイルを更新した後、なぜBrazeで翻訳内容に変更が見られないのでしょうか?

Braze では翻訳コンテンツがキャッシュされ、その更新には数分かかることがあります。キャンペーンをテストしていて、翻訳の結果をすぐに確認する必要がある場合は、このリファレンス記事で説明されているように、`:cache_max_age` パラメーターを使用できます。


