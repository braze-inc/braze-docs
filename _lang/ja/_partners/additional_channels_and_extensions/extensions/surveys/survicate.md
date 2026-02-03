---
nav_title: Survicate
article_title: Survicate
description: "この参考記事では、BrazeとカスタマーフィードバックプラットフォームであるSurvicateのパートナーシップについて概説している。Survicateは、複数のチャネルやカスタマージャーニー全体を通して、顧客のインサイトを収集、分析、活用することを支援するプラットフォームである。"
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

> [Survicateは](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)、複数のチャネルとカスタマージャーニーを通じて顧客のインサイトを収集、分析、活用するカスタマー・フィードバック・プラットフォームである。[クイックデモを見る](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter)

_この統合は Survicate によって管理されます。_

## 統合について

SurvicateとBrazeのネイティブインテグレーションを使用して、メール、アプリ内、モバイル、またはWebアンケートの回答をBrazeの顧客プロファイルと同期する。アンケートの回答は、カスタム属性またはイベントとして Braze ユーザープロファイルと自動的に同期されます。リアルタイムのフィードバックインサイトにより、顧客データとともにフィードバックを簡単に追跡・分析し、ターゲットフォローアップや超パーソナライズされたセグメントを作成することができる。 

## ユースケース

BrazeとSurvicateは、様々なフィードバックのユースケースをカバーするために連携し、アクション可能なユーザーインサイトの収集とカスタマーエクスペリエンスの向上を支援する：

- 受信トレイから回答できる埋め込み型アンケートで、アンケートのレスポンシブ率を向上させる。 
- アプリ内メッセージでカスタマージャーニーの重要な段階でインサイトを収集する。 
- Brazeでよりスマートなセグメンテーションを作成するために、Survicateに保存されたフィードバックを使用する。 
- 顧客のフィードバックに基づいてフォローアップキャンペーンをオートメーション化する。 
- 顧客インサイトを活用して、パーソナライズされたワークフローをトリガーする。 
- 自動翻訳されたアンケートで、より多くのオーディエンスにアプローチする。
- 誰かがアンケートに回答すると、Brazeコンタクトプロファイルにイベントを送信する。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Survicate アカウント | この統合を有効にするにはSurvicateアカウントが必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定**」>「**APIと識別子**」から作成できる。 |
| Braze RESTエンドポイント | [あなたのRESTエンドポイントURL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合の主な特徴

Survicate と Braze の統合により、リアルタイムのデータ同期が提供されるため、Survicate アンケートの最新情報を Braze ですぐに利用できます。アンケートの回答に基づいて、このデータを使ってタイムリーでパーソナライズされたアクションを取ることができます。

- **アンケートの回答をカスタムユーザー属性として Braze に送信する**：アンケートの回答データでユーザープロファイルを充実させます。
- **Braze のカスタムイベントをトリガーする**：アンケートの回答に基づいたイベントを利用して、特定のグループをターゲットにしたり、フォローアップキャンペーンを開始する。
- **詳細なセグメントを構築する**：Survicate アンケートのデータを使って Braze セグメントを作成し、アウトリーチをさらにパーソナライズします。

## 統合

### Survicateでアンケートを作成する

#### アンケートをメールに埋め込んだり、共有可能なリンクアンケートを作成する。 

1.  Survicate で**\+ 新規アンケートの作成を**クリックし、作成方法（テンプレート、AI アンケート作成、または独自の質問の追加）を選択し、メールまたは共有リンクのアンケートタイプを選択する：
![アンケート作成でBrazeが選択されている。]({% image_buster /assets/img/survicate/survicate_1.gif %})

{: start="2"}
2\.アンケートの設定タブで、回答者を識別するツールとして**Braze**を選択する：
![アンケートのConfigureタブでBrazeが選択されている。]({% image_buster /assets/img/survicate/survicate_2.png %})

{: start="3"}
3\.アンケートを設定したら、共有タブでメールアンケートの送信方法を決める。**アンケートをリンクとして**送信するか、**最初の質問をメールに埋め込んで**、回答者がメールからすぐにアンケートに回答できるようにする。

{% details Survey link option %}

1. アンケートリンクをコピーするボタンからアンケートへのリンクを取得する：

![アンケートリンクをコピーするボタンからアンケートへのリンクを取得する。]({% image_buster /assets/img/survicate/survicate_3.png %})

{: start="2"}
2\.BrazeメールのCTAボタンやハイパーリンクの後ろにアンケートリンクを隠す。

![BrazeメールのCTAボタンやハイパーリンクの後ろにアンケートリンクを隠す。]({% image_buster /assets/img/survicate/survicate_4.png %})

{% enddetails %}

{% details Email embed option %}

最初の質問をメール本文に直接表示し、メールからアンケートを開始する。その後、回答者は残りのアンケートに回答するためのランディングページにリダイレクトされる。

1. **メールコードを取得**」をクリックし、**HTMLコードをコピーする**：

![メールコードを取得する]({% image_buster /assets/img/survicate/survicate_5.gif %})

{: start="2"}
2\.アンケートに使用するBrazeキャンペーンに移動し、**メール本文の編集を**クリックし、テンプレートにHTMLブロックを追加する：

![HTMLブロックコードを取得する]({% image_buster /assets/img/survicate/survicate_6.png %})

{: start="3"}
3\.コードをSurvicateアンケートからコピーしたものに置き換える。すると、アンケートの最初の質問がテンプレートに表示される：

![Survicateアンケートからコピーしたコードに置き換える。]({% image_buster /assets/img/survicate/survicate_7.png %})

{: start="4"}
4. メールをスケジュールされ、ターゲットグループを選択すれば、キャンペーンは送信準備完了。

{% enddetails %}

### Brazeアプリ内メッセージ調査

1. **新しいアンケートを作成するを**クリックし、作成方法（テンプレート、AIアンケート作成、または独自の質問の追加）を選択し、プラットフォーム内アンケートとアプリ内メッセージのアンケートタイプを選択する：

![新しいアンケートを作成する」をクリックし、作成方法を選択する。]({% image_buster /assets/img/survicate/survicate_8.gif %})

{: start="2"}
2\.Brazeアカウントに移動し、**メッセージング > キャンペーン > キャンペーンの作成 > アプリ内**メッセージの順に選択して、Brazeアプリ内メッセージ調査を開始する**：**
![Brazeアプリ内メッセージアンケートを開始する。]({% image_buster /assets/img/survicate/survicate_9.gif %})

### 従来のエディタでBrazeアプリ内Messengerアンケートを開始する。

1. 従来のエディターを使用している場合は、メッセージタイプで**カスタムコードを**選択する：

![カスタムコードを選択する]({% image_buster /assets/img/survicate/survicate_10.gif %})

{: start="2"}
2\.次に、アンケートの開始タブにあるコードを HTML フィールドに貼り付ける：

![アンケートの開始タブにあるコードを HTML フィールドに貼り付ける。]({% image_buster /assets/img/survicate/survicate_11.gif %})

{% alert note %}
Brazeはデフォルトで、アプリのバックグラウンドがブロックされている間、アプリ内メッセージをiframeで表示する。Survicateのアンケートが表示されている間、アプリとのインタラクションを許可するには、次のことが必要である：<br><br>

- サービケート・ブレイズのスニペットに`opts.useBrazeIframeClipper = true` を追加する。
- Brazeを初期化し、`initBrazeBridge` 関数を使用するファイルに、`@survicate/braze-bridge-npm` [パッケージを](https://www.npmjs.com/package/@survicate/braze-bridge-npm)インストールする。

サンプル・スニペットとReactの実装は[Survicateの開発者サイトに](https://developers.survicate.com/javascript/installation/#braze)ある。
{% endalert %}

{: start="3"}
3\.Brazeキャンペーンで、TargetとAssignステップを設定する。完了したら、キャンペーンを開始できる。レビューのステップでは、キャンペーンがどのように見えるかを見ることができる。アンケートは、上記のようにSurvicateパネルで指定された場所にWebサイトに表示される。

### Brazeとの統合をイネーブルメントにする

1. Brazeとのイネーブルメントを有効にするには、「**Integrations**」から「Braze」を検索して選択する。

![ブレイズを選択する]({% image_buster /assets/img/survicate/survicate_12.gif %})

{: start="2"}
2\.**Connectを**クリックして認証を設定する。

3. BrazeアカウントのワークスペースAPIキーとBrazeインスタンスURLを入力する：

![BrazeアカウントのワークスペースAPIキーとBrazeインスタンスURLを入力する。]({% image_buster /assets/img/survicate/survicate_13.png %})

{% alert important %}
SurvicateをBrazeに接続するには、Braze APIキーに`users.track` の権限が必要である。
{% endalert %}

### アンケートをBrazeに接続する

Brazeインテグレーションが接続されたので、各アンケートに個別の設定を行うことができる。アンケートにアクセスし、**Connect**タブを選択し、利用可能な統合のリストから**Brazeを**選択する。

![アンケートにアクセスし、Connectタブを選択し、Brazeを選択する。]({% image_buster /assets/img/survicate/survicate_14.png %})

### レスポンシブをカスタム属性としてBrazeに送信する。

アンケートの回答をカスタム属性としてBrazeに流入するように設定し、収集データでユーザープロファイルを充実させる。

1. Braze Integrationの設定タブで、**更新フィールド**セクションを細かく設定する。

![更新フィールドセクションを選択する。]({% image_buster /assets/img/survicate/survicate_15.png %})

{: start="2"}
2\.フィールドを更新したい質問を選択する。Brazeユーザープロファイルがデータで溢れるのを避けるため、選択した質問のみにレスポンスを送信することができる。

![フィールドを更新したい質問を選択する。]({% image_buster /assets/img/survicate/survicate_16.png %})

{% alert note %}
このBraze統合では、ランキングとマトリックスの質問はサポートされていない。
{% endalert %}

{: start="3"}
3\.更新したいカスタム属性の名前を**ユーザー**フィールドの下に追加する：

![更新したいカスタム属性の名前をユーザーフィールドの下に追加する。]({% image_buster /assets/img/survicate/survicate_17.png %})

デフォルトでは、Survicateはアンケートの回答内容を属性値として送信する。これらの値を変更するには、**Edit mappingを**クリックして、ラベルを短くしたり、データ構造に合わせて変更することができる：

![属性値としてのアンケート回答]({% image_buster /assets/img/survicate/survicate_18.png %})

![これらの値を変更するには、マッピングの編集をクリックする。]({% image_buster /assets/img/survicate/survicate_19.png %})

{% alert note %}
NPSの場合、SurvicateはNPS®の質問の回答グループに基づいてマッピングされた値を送信する。ただし、数値を受信したい場合は、「Send Answers as 0-10」を切り替えることができる。
{% endalert %}

![Survicateはレスポンスグループに基づいてマッピングされた値を送信する。]({% image_buster /assets/img/survicate/survicate_20.png %})

{: start="4"}
4. **新規追加]**をクリックし、同じステップを適用することで、さらに多くの質問を統合に接続する。

![より多くの質問を統合につなげる]({% image_buster /assets/img/survicate/survicate_21.png %})

### Brazeコンタクトのプロファイルにイベントを送信する

これまでの設定とは別に、Survicateは、回答者がアンケートの質問に回答するたびに、Brazeで`survicate-question-answered` というカスタムイベントを送信することができる。
Survicateパネルの[カスタム属性としてレスポンスを送信]で、すべての質問に対してイベントを送信するか、[フィールドの更新]タブで選択した質問に対してイベントを送信するか、またはまったく送信しないかを選択することができる：

![すべての質問に対してイベントを送信するかどうかを選択できる。]({% image_buster /assets/img/survicate/survicate_22.png %})

イベントの送信を選択した場合、Survicateアンケートに何回回答したか、最後に回答したのはいつかをユーザープロファイルで確認できる：

![レスポンシブ ]({% image_buster /assets/img/survicate/survicate_23.png %})

イベントには、質問に対する回答と、アンケート、質問、回答者に関する情報を含むイベントプロパティが含まれる。このイベントを使用してセグメンテーションを作成することができる。例えば、特定の日付以降や特定の回数以降にアンケートに回答したユーザーのセグメンテーションを作成する：

![このイベントには、答えを持つイベントプロパティが含まれている。]({% image_buster /assets/img/survicate/survicate_24.png %})

このデータは、Brazeでキャンペーンを作成する際にも使用できる。

![このデータは、Brazeでキャンペーンを作成する際にも使用できる。]({% image_buster /assets/img/survicate/survicate_25.png %})

### 統合をテストする

アンケートの準備と統合設定が完了したら、作成した属性、タグ、新規コンタクト設定の横にある統合テストボタンをクリックすることで、Survicateを離れることなくアンケートをテストすることができる。SurvicateはBrazeアカウントにテストコンタクト(`braze-test@survicate.com`)を作成する。コンタクトのプロファイルには、設定に従って更新されたフィールドが含まれる。

![統合テストボタンをクリックする]({% image_buster /assets/img/survicate/survicate_26.png %})

Brazeでは、Survicateダミーコンタクトにマッピングされたフィールドのサンプルデータを見ることができる：

![Survicateダミーコンタクトのマッピングされたフィールドのサンプルデータ]({% image_buster /assets/img/survicate/survicate_27.png %})

### アンケート結果を分析する

Brazeのアンケートで回答を集めたら、回答者が共有したフィードバックやインサイトを調べてみよう。Survicateを使えば、結果、統計、傾向を簡単に確認し、さらなるアクションにつなげることができる。

### Survicateでのフィードバック

アンケートの収集が開始されると、アンケートの分析タブにすぐに回答が表示される。

![分析タブのレスポンシブ]({% image_buster /assets/img/survicate/survicate_28.png %})

分析]タブでは、統計およびオーバータイムデータを含む全体的な結果が表示されるほか、各アンケートの詳細を調べるための個別のレスポンシブも表示される。

### Brazeへのフィードバック

アンケートの回答でユーザーフィールドを更新したり、回答をカスタムイベントとして送信したりすると、リアルタイムで同期されたアンケートデータを確認できる。Brazeで、アンケートに回答した特定の連絡先にアクセスする。コンタクトのメインビューには、レスポンシブデータとイベントの両方が表示される。

![調査データはリアルタイムで同期される]({% image_buster /assets/img/survicate/survicate_29.png %}) 