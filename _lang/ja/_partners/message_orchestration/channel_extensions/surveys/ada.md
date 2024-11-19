---
nav_title: Ada
article_title: Ada
description: "この参考記事では、顧客とのやり取りを自動化し、パーソナライズするAIを搭載したプラットフォームであるBrazeとAdaのパートナーシップについて概説している。この統合により、自動化された Ada の会話から収集されたデータを使用してユーザープロファイルを拡張できます。"
alias: /partners/ada/
page_type: partner
search_tag: Partner

---

# Ada

> [Ada](https://ada.cx)は、対話型 AI を使ってカスタマーエクスペリエンスを自動化およびパーソナライズするブランドインタラクションプラットフォームです。Adaを使用して、ユーザーデータに基づいてメッセージングを調整し、キャンペーンをセグメント化し、会話を測定・分析して新たな機会を発見し、顧客とのチャットから得た洞察を使用してユーザープロファイルを充実させる。  

Braze と Ada の統合により、自動化された Ada の会話から収集されたデータを使用してユーザープロファイルを拡張できます。Ada でのチャット中に収集した情報に基づいてカスタムユーザー属性を設定し、Ada での会話中に指定された時点で Braze にカスタムイベントを記録できます。Ada のチャットボットを Braze に接続すると、顧客が尋ねたブランドに関する質問に基づいて、あるいは顧客との会話を積極的に開始し、顧客の関心や好みを深く理解するための質問をすることで、顧客をより詳しく把握できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Ada アカウント | このパートナーシップを利用するには、BrazeとAnswer Utilitiesのアプリケーションを有効にした[Ada](https://ada.cx)アカウントが必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL][1]。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

BrazeとAdaの統合の一般的な使用例には次のようなものがある：
- 消費者が Ada ボットとの間で行ったさまざまなインタラクションを Braze でカスタムイベントとして追跡する。これにより、Ada でプロアクティブなキャンペーンに参加した顧客、サポートエージェントに引き継がれた顧客、特定の質問をした顧客、特定のアクションを完了した顧客を把握できます。
- 消費者に各自の関心、好み、デモグラフィックなどを尋ねる。カスタム属性を使用して、この新しい情報で Braze のプロファイルを自動的に更新します。

## 統合

Braze と Ada を統合するには、まず Ada ダッシュボードで Braze アプリケーションを設定し、Ada チームと協力して Ada 埋め込みスクリプトにユーザー ID メタ変数を設定する必要があります。次に、Brazeに情報を送り返したい場所（イベントかアトリビュート）に、Brazeブロックをアンサーエディタにドラッグする。

### ステップ1:AdaでBrazeアプリをセットアップする

Ada ダッシュボードで **[Settings] > [Integrations] > [Handoff Integrations]** の順に進みます。

Brazeの横にある「**Connect**」をクリックし、以下の情報を入力する：
- **RESTエンドポイント**：Braze RESTエンドポイントのURLを入力する。 
- **APIキー**：Braze REST APIキーを入力する。 
- **App ID**: Ada チャット機能に関連付けるアプリ ID を入力します。

### ステップ2:BrazeからAdaに識別子を渡す

正しいユーザーを確実に更新するためには、Ada チームに連絡する必要があります。Ada チームは、Braze から識別子を受け取るために Ada 埋め込みスクリプトに必要な修正を行う作業を支援します。この統合は external ID を受け取るように設計されていますが、ユーザーエイリアスなど他の識別子が受け渡されることがあります。 

### ステップ3:Braze ブロックを該当する Answer にドロップします。

Braze ブロックを使用するには、ブロックをブロックドロワーから適切な Answer にドラッグし、アクションを選択します。Braze ブロックでは次の2つのアクションを実行できます。
* イベントの追跡
* 属性を更新する

{% tabs ローカル %}
{% tab イベントの追跡 %}

#### [Answer Utilities] ブロック

1. ブロックドロワーから [Answer Utilities] ブロックを Braze ブロックの真上にドラッグします。 
2. **Format Date**アクションを選択し、**Date**フィールドに`today` 。
3. [**Output Format**] フィールドに「`iso`」と入力します。[**Save Response As Variable**] で `iso_time` という名前の**形式付き日付**の変数を作成します。

![前述のテキストで説明されているようにフィールドが入力されている Answer Utilities ブロック。]({% image_buster /assets/img/ada/ada-braze-2.png %})

#### Braze ブロック

**4\.**Brazeブロックの**External ID**フィールドに、前のステップでAdaが設定した`external_id` メタ変数を入力する。<br>
**5\.****Event Name**フィールドに、追跡したいBrazeのイベント名を入力する。<br>
**6\.**[**Time of Event**] フィールドに、[Answer Utilities] ブロックで作成した変数 `iso_time` を入力します。<br>
**7\.**Brazeへのイベント投稿中に問題が発生した場合に表示されるフォールバックアンサーを選択する。

![前述のテキストで説明されているようにフィールドが入力されている Braze ブロック。]({% image_buster /assets/img/ada/ada-braze-3.png %})

{% endtab %}
{% tab 属性の更新 %}

#### Braze ブロック

1. Brazeブロックの**External ID**フィールドに、前のステップでAdaが設定した** メタ変数を入力する。 
2. **Attribute Name（属性名**）フィールドに、追跡したいBraze属性の名前を入力する。 
3. **属性値**フィールドに、設定したい値を入力する。テキスト、変数、またはテキストと変数の組み合わせである。 
4. Brazeへの属性の投稿中に問題が発生した場合に表示されるフォールバックアンサーを選択する。

![前述のテキストで説明されているようにフィールドが入力されている Braze ブロック。]({% image_buster /assets/img/ada/ada-braze-4.png %})

{% endtab %}
{% endtabs %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/ada/ada-braze-1.png %}
[3]: {% image_buster /assets/img/ada/ada-braze-2.png %}
[4]: {% image_buster /assets/img/ada/ada-braze-3.png %}
[5]: {% image_buster /assets/img/ada/ada-braze-4.png %}