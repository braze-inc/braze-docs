---
nav_title: Lokalise
article_title:ロカライズ
description:この記事では、アジャイルチーム向けの翻訳管理サービスであるLokaliseとBrazeの提携について説明します。
alias: /partners/lokalise/
page_type: partner
search_tag:Partner

---

# ロカライズ

> [Lokalise](https://lokalise.com) はアジャイルチームのための翻訳管理サービスです。

BrazeとLokaliseの統合は、Connected Contentを活用して、ユーザーの言語設定に基づいて翻訳されたコンテンツをBrazeキャンペーンに簡単に挿入できるようにします。

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| ロカライズアカウント | このパートナーシップを利用するには、Lokaliseアカウントが必要です。 |
| ローカライズ翻訳プロジェクト | Lokaliseの翻訳プロジェクトは、この統合を設定する前に作成する必要があります。 |
{: .reset-td-br-1 .reset-td-br-2}

### 新しいLokaliseプロジェクトを作成する

新しい翻訳プロジェクトを作成するには、Lokaliseにログインして**新しいプロジェクト**を選択します。次に、プロジェクトに名前を付け、**ベース言語**（翻訳元の言語）を選択し、1つ以上の**ターゲット言語**を追加し、**ソフトウェアローカリゼーション**プロジェクトタイプを選択します。準備ができたら、**Proceed**をクリックしてください。

## 統合

Lokaliseでは、Brazeで定義した各Connected Content変数の翻訳キーを作成します。翻訳が準備できたら、言語ごとに1つのJSONファイルを生成し、接続されたコンテンツを提供するURLに公開できます。

### ステップ1:ユーザー言語の設定

まだ行っていない場合は、Brazeダッシュボードを開き、**ユーザー > ユーザーインポート**に進んでください。ここで、ユーザーをインポートできます。CSVファイルをインポートする準備をする際には、ユーザーの言語を含む言語列を含めるようにしてください。この言語フィールドは、翻訳を表示する際に後で使用されます。 

{% alert important %}
BrazeとLokaliseの両方で使用される言語コードは一致している必要があります。
{% endalert %}
### ステップ2:Lokaliseで翻訳の準備をする

次に、Lokaliseで翻訳を準備するには、Braze Connected Content変数を使用しています。 

例えば、簡単な翻訳キーを作成しましょう、`description`:
1. Lokaliseプロジェクトを開き、**キーを追加**をクリックし、**キー**フィールドに「description」と入力します。
2. 「デモの説明」と入力します **基本言語の値** フィールド。
3. 「Web」を**プラットフォーム**のドロップダウンに追加します。 
4. 準備ができたら、**保存**をクリックしてください。

![][1]{: style="max-width:60%"}

あなたの翻訳キーはプロジェクトエディタに表示されるはずです。

![][2]{: style="max-width:90%"}

#### 既知の問題

- あなたのキーは**Web**プラットフォームに割り当てられている必要があります。
- ピリオドを含むキー(`.`)や`_on`文字列を使用しないでください。例えば、`this_is_the_key`の代わりに`this.is.the.key`を使用し、`join_us_instagram`の代わりに`join_us_on_instagram`を使用します。

### ステップ3:LokaliseでBrazeアプリを構成する

Lokaliseプロジェクトを開き、**アプリ**をクリックします。ここで、Brazeアプリを検索してインストールします。次の画面が表示されます:

![LokaliseのBraze設定には、プロジェクトIDと翻訳ファイルのURLが記載されています。][3]

Lokaliseは、**Translation File URL**で、プロジェクト内のキーに対するすべての翻訳を含むJSONファイルを公開します。プロジェクトにあるターゲット言語の数だけ、翻訳ファイルのURLが取得できます。これが、結果として得られる翻訳ファイルのURLが2つの部分を持つ理由です。

1. URL パスの最初の部分はすべての言語に共通です。
2. URLの最後にあるJSONファイル名は言語コードに基づいています。

翻訳ファイルのURLは、Brazeキャンペーンを設定する際に必要なURLです。JSONファイルの内容は**更新**をクリックして更新できます。URLは同じままで、BrazeでのConnected Content呼び出しを変更する必要はありません。

### テストURL

このURLをテストするには、コピーして{% raw %}`{{${language}}}`{% endraw %}を言語コード（例えば、`en`）に置き換え、このURLをブラウザで開きます。JSONファイルにキーと翻訳が表示されます:

![][4]

### ステップ 4:Brazeキャンペーンで翻訳を使用する

#### 接続されたコンテンツの呼び出しを挿入

準備ができたら、Brazeに戻り、既存のキャンペーンを開くか、新しいキャンペーンを作成してください。この例のためにサンプルコンテンツを使用して新しいメールキャンペーンを作成します。**メール本文を編集**をクリックします。

翻訳を挿入するには、HTMLのドキュメントの先頭または翻訳が必要な最初の場所の直前に、Connected Contentリクエストを追加する必要があります。これは次のマークアップを挿入することで行うことができます:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

前のステップで取得した翻訳ファイルURLで`https://exports.live.lokalise.cloud/...` URLを置き換えます。

{% raw %}

- `{{${language}}}` は「この位置にユーザーの言語を挿入する」という意味です。あるいは、言語コードをハードコードすることもできます。例えば、`en.json`。
  - 各ユーザーに対して適切な翻訳済みJSONファイルが取得されるようにするには、翻訳ファイルのURLの末尾に`{{${language}}}`プロファイル属性またはユーザーの言語を保持する別の類似のカスタム属性を配置する必要があります。（例えば、`/{{${language}}}.json`）これらの属性に保持されている値は、各翻訳済みJSONファイルのプレフィックスと一致している必要があります。これにより、各ユーザーに対して正しい翻訳ファイルが返されることが保証されます。
- `:save translations` は JSON コンテンツを translations 変数に保存します。

#### 翻訳を表示

今、翻訳変数を使用して、キーによって目的の翻訳を表示します。

例えば、`description`キーを表示するには、`{{ translations.description }}`を使用します。

{% endraw %}
![][6]

最後に、メールテンプレートを保存してプレビューします。翻訳が表示されるのを確認してください。

## よくある質問

**誤ってLokaliseからキーを削除した場合どうなりますか？**<br>
対応する文字列は、Braze上で翻訳されなくなります。

**私が`en`ロケールを持っているが、Lokaliseで`en-US`にオーバーライドした場合、Brazeはそれを`en-US`として読み取りますか？**<br>
いいえ、ロケールISOコードはBrazeとLokaliseで一致する必要があります。

**接続時にLokaliseコンテンツの`:rerender`フラグを使用できますか?**<br>
はい、もちろん。このフラグを追加する方法については、Brazeのドキュメントを参照してください。

**ロカリゼで翻訳ファイルを更新した後、なぜBrazeの翻訳コンテンツに変更が表示されないのですか**<br>
Brazeは翻訳されたコンテンツをキャッシュし、更新に数分かかることがあります。キャンペーンをテストしていて、翻訳の結果をすぐに確認する必要がある場合は、この参考記事で説明されているように`:cache_max_age`パラメータを使用できます。

[1]: {% image_buster /assets/img/lokalise/1_add_key.png %}
[2]: {% image_buster /assets/img/lokalise/2_translation_key_added.png %}
[3]: {% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %}
[4]: {% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %}
[5]: {% image_buster /assets/img/lokalise/5_edit_email.png %}
[6]: {% image_buster /assets/img/lokalise/6_integration_usage_sample.png %}