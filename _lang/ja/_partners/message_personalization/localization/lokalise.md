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

BrazeとLokaliseの統合は、Connected Contentを活用し、ユーザーの言語設定に基づいてBrazeキャンペーンに翻訳コンテンツを簡単に挿入できる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Lokalise アカウント | このパートナーシップを利用するには、Lokaliseアカウントが必要である。 |
| Lokalise 翻訳プロジェクト | この統合を設定する前に、Lokalise翻訳プロジェクトを作成する必要がある。 |
{: .reset-td-br-1 .reset-td-br-2}

### 新しいLokaliseプロジェクトを作成する

新しい翻訳プロジェクトを作成するには、Lokaliseにログインし、**新規プロジェクトを**選択する。次に、プロジェクトに名前を付け、**ベース言語**（翻訳元の言語）を選択し、1つ以上の**ターゲット言語を**追加し、**ソフトウェアローカリゼーションプロジェクトタイプを**選択する。準備ができたら、**Proceedを**クリックする。

## 統合

Lokaliseでは、Brazeで定義したConnected Content変数ごとに翻訳キーを作成する。翻訳の準備ができたら、言語ごとに1つのJSONファイルを生成し、コネクテッド・コンテンツを提供するURLに公開することができる。

### ステップ1:ユーザー言語を設定する

まだの場合は、Brazeダッシュボードを開き、**Users > User importに**進む。ここで、ユーザーをインポートすることができる。インポート用のCSVファイルを準備する際には、ユーザーの言語を記載した言語カラムを必ず含めること。この言語フィールドは、後で翻訳を表示するときに使われる。 

{% alert important %}
使用する言語コードは、BrazeとLokaliseの両方で一致していなければならない。
{% endalert %}
### ステップ2:Lokaliseで翻訳を準備する

次に、Lokaliseで翻訳を準備するには、Braze Connected Content変数で使用しているのと同じ名前の翻訳キーを手動で作成する必要がある。 

例えば、単純な翻訳キー、`description` を作ってみよう：
1. Lokaliseプロジェクトを開き、**Add Keyを**クリックし、**Key**フィールドに "description "を入力する。
2. **Base Language Value**フィールドに「Demo description」と入力する。
3. **Platformsの**ドロップダウンに "Web "を追加する。 
4. 準備ができたら、**Saveを**クリックする。

![][1]{: style="max-width:60%"}

プロジェクトエディターに翻訳キーが表示されるはずだ：

![][2]{: style="max-width:90%"}

#### 既知の問題

- キーは**ウェブ・プラットフォームに**割り当てられなければならない。
- ピリオド（`.` ）や`_on` 文字列を含むキーの使用は避けること。例えば、`this.is.the.key` の代わりに`this_is_the_key` を使い、`join_us_on_instagram` の代わりに`join_us_instagram` を使う。

### ステップ3:LokaliseでBrazeアプリを設定する

Lokaliseプロジェクトを開き、**Appsを**クリックする。ここで、Brazeアプリを検索してインストールする。以下の画面が表示される：

![Lokalise上のBraze設定には、プロジェクトIDと翻訳ファイルのURLが記載されている。][3]

**翻訳ファイルURLでは**、Lokaliseは、プロジェクト内のキーのすべての翻訳を含むJSONファイルを公開する。プロジェクトにあるターゲット言語の数だけ、翻訳ファイルのURLが得られる。そのため、翻訳ファイルのURLは2つに分かれている：

1. URLパスの最初の部分はすべての言語に共通である。
2. URL末尾のJSONファイル名は、言語コードに基づいている。

翻訳ファイルのURLは、Brazeキャンペーンを設定する際に必要となるURLである。**Refreshを**クリックすれば、JSONファイルの内容を更新できる。URLは変わらないので、BrazeのConnected Contentコールを変更する必要はない。

### テストURL

このURLをテストするには、このURLをコピーし、{% raw %}`{{${language}}}`{% endraw %} を言語コード（たとえば、`en` ）に置き換えて、ブラウザでこのURLを開く。キーと翻訳を含むJSONファイルが表示される：

![][4]

### ステップ4:Brazeキャンペーンで翻訳を使用する

#### コネクテッド・コンテンツを挿入する

準備ができたら、Brazeに戻り、既存のキャンペーンを開くか、新しいキャンペーンを作成する。この例では、サンプルコンテンツで新しいメールキャンペーンを作成する。**メール本文の編集を**クリックする。

翻訳を挿入するには、HTMLにConnected Contentリクエストを追加する必要がある。これは、以下のマークアップを挿入することで可能になる：

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

`https://exports.live.lokalise.cloud/...` URLを、前のステップで取得した翻訳ファイルのURLに置き換える。

{% raw %}

- `{{${language}}}` とは、「この位置にユーザー言語を挿入する」という意味である。あるいは、言語コードをハードコードすることもできる。例えば、`en.json` 。
  - 各ユーザに適切な翻訳JSONファイルが取得されるようにするには、`{{${language}}}` profile属性か、ユーザの言語を保持する別の同様のカスタム属性を翻訳ファイルのURLの最後に配置する必要がある。(例えば、`/{{${language}}}.json`) これらの属性に保持される値は、翻訳されたJSONファイルのそれぞれの接頭辞と一致しなければならない。これにより、各ユーザーに対して正しい翻訳ファイルが返されるようになる。
- `:save translations` はJSONコンテンツをtranslations変数の下に保存する。

#### 翻訳を表示する

ここでtranslations変数を使い、必要な翻訳をキーで表示する。

例えば、`description` キーを表示するには、`{{ translations.description }}` とする。

{% endraw %}
![][6]

最後に、メールテンプレートを保存し、プレビューする。翻訳が表示されるはずだ。

## よくある質問

**誤ってLokaliseからキーを削除した場合はどうなるのか？**<br>
Brazeの対応する文字列はもう翻訳を持たない。

**`en` のロケールをLokaliseの`en-US` で上書きした場合、Brazeはそれを`en-US` と読み取るのだろうか？**<br>
いいえ、ロケールのISOコードはBrazeとLokaliseで一致していなければならない。

**Lokaliseコンテンツに接続する際、`:rerender` フラグを使用できるか？**<br>
ああ、もちろんだ。このフラグの追加方法については、Brazeのドキュメントを参照されたい。

**Lokaliseで翻訳ファイルを更新した後、Brazeで翻訳されたコンテンツの変更を確認できないのはなぜか？**<br>
Brazeは翻訳されたコンテンツをキャッシュするので、更新に数分かかることがある。キャンペーンをテストしていて、翻訳の結果をすぐに確認する必要がある場合は、この参考記事で説明されているように、`:cache_max_age` パラメータを使うことができる。

[1]: {% image_buster /assets/img/lokalise/1_add_key.png %}
[2]: {% image_buster /assets/img/lokalise/2_translation_key_added.png %}
[3]: {% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %}
[4]: {% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %}
[5]: {% image_buster /assets/img/lokalise/5_edit_email.png %}
[6]: {% image_buster /assets/img/lokalise/6_integration_usage_sample.png %}