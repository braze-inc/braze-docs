---
nav_title: アプリ内メッセージを作成する
article_title: アプリ内メッセージを作成する
page_order: 1
description: "この参考記事では、Brazeプラットフォームを使って、キャンペーンやキャンバスを使ったアプリ内メッセージの作成方法について解説する。"
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
---

# アプリ内メッセージを作成する

> キャンペーン、キャンバス、または API キャンペーンを使用して、Braze プラットフォームを使ってアプリ内メッセージまたはブラウザ内メッセージを作成できます。便利な[アプリ内メッセージ準備ガイドを使って]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)、事前にメッセージを計画し、すべての資料を準備することを強くお勧めする。

## ステップ 1:メッセージを発信する場所を選ぶ {#create-new-campaign-in-app}

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

1. [**メッセージング**] > [**キャンペーン**] の順に進み、[**キャンペーンを作成**] を選択します。
2. [**アプリ内メッセージ**] を選択します。なお、アプリ内メッセージはマルチチャネルキャンペーンでは利用できない。
3. キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じて、[[チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)] と [[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)] を追加します。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、[[レポートビルダー]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、[**バリアントを追加**] ドロップダウンから [**バリアントをコピー**] を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

1. キャンバス作成ツールを使用して [[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. [[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。アプリ内メッセージを含むステップをアクションベースにすることはできません。
4. 必要に応じて、このステップのオーディエンスをフィルター処理します。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。遅延後のメッセージの送信時に、オーディエンスのオプションがチェックされます。
5. [[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせる他のメッセージングチャネルを選択します。

{% alert important %}
1 つのステップに複数のアプリ内メッセージバリアントを含めることはできません。
{% endalert %}

キャンバス固有の詳細情報は、[キャンバスのアプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)にあります。

{% endtab %}
{% endtabs %}

## ステップ 2:配信プラットフォームを指定する

まず、メッセージを受信するプラットフォームを選択します。この選択肢を使用して、特定のアプリセットへのキャンペーンの配信を制限します。例えば、モバイルアプリのダウンロードを促すブラウザ内メッセージに**ウェブブラウザを**選択し、すでにアプリを入手した後にメッセージを受け取らないようにする。プラットフォームの選択は各バリアントに固有であるため、プラットフォームごとにメッセージエンゲージメントのテストを試すことができます。

| プラットフォーム                        | メッセージの配信        |
|---------------------------------|-------------------------|
| モバイルアプリ                     | iOS & Android SDK      |
| ウェブブラウザ                    | ウェブSDK                 |
| モバイルアプリとウェブブラウザの両方 | iOS、Android、Web SDK |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ステップ 3:メッセージの種類を指定する

送信プラットフォームを選択したら、そのプラットフォームに関連するメッセージタイプ、レイアウト、その他のオプションを参照します。各メッセージの期待される動作や見た目については、[クリエイティブの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)ページで、または以下の表のリンク先のメッセージタイプをクリックして詳細を確認してほしい。

使用するメッセージタイプを決める際には、アプリ内メッセージキャンペーンでどの程度強く売り込む必要があるかを検討する必要があります。これは、メッセージがどれだけの画面領域を占め、お客様のアプリやサイトにおける顧客の通常の体験がどの程度妨げられるかを示す指標です。配信したいコンテンツがリッチになればなるほど、メッセージはより押しつけがましくなる。

![侵入性のスケールを示すグラフィック。スライダーが最も侵入性が低く、次にモーダル、そして全画面表示では最も侵入性が高くなります]({% image_buster /assets/img_archive/iam_intrusive.png %}){: style="max-width:80%" }

### メッセージの種類

これらのアプリ内メッセージは、モバイルアプリとウェブアプリケーションの両方で受け入れられる。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>メッセージの種類</th>
    <th>タイプの説明</th>
    <th>利用可能なレイアウト</th>
    <th>その他のオプション</th>
    <th>推奨用途</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>フルスクリーン</a></td>
    <td>メッセージブロックで画面全体を覆うメッセージ。</td>
    <td>
      <ul>
      <li>画像とテキスト</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>強制的なデバイスの向き（縦または横）</td>
    <td>大きくて大胆。最も重要なキャンペーン、重要な通知、大規模なプロモーションなど、ユーザーに確実にコンテンツを見てもらいたい場合に使用します。<br><br>モバイル・デバイスでは、デバイスの向きとメッセージの向きが一致しない場合、縦向きと横向きのメッセージは表示されないことに注意。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>モーダル</a></td>
    <td>スクリーンオーバーレイとメッセージブロックで画面全体を覆うメッセージ。</td>
    <td>
      <ul>
      <li>テキスト（オプション画像付き）</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>該当なし</td>
    <td>程よい中間のオプションです。ユーザーに新機能を試してもらったり、プロモーションを利用してもらうなど、ユーザーの注意を引く明白な方法が必要な場合に使用する。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>スライドアップ</a></td>
    <td>画面の他の部分を遮ることなく、指定された場所にスライドして表示されるメッセージ。</td>
    <td>該当なし</td>
    <td>該当なし</td>
    <td>邪魔にならない-画面の占有面積を最小限に抑える。新機能、お知らせ、クッキーの使用など、小さな情報の断片をユーザーに警告する場合に使用する。<br></td>
  </tr>
</tbody>
</table>

### 高度なメッセージタイプ

これらのアプリ内メッセージは、あなたのニーズに合わせてカスタマイズできる。

<table class="tg">
<thead>
  <tr>
    <th>メッセージの種類</th>
    <th>タイプの説明</th>
    <th>利用可能なレイアウト</th>
    <th>要件</th>
    <th>推奨用途</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>カスタムHTMLメッセージ</a></td>
    <td>カスタムコード（HTML、CSS、JavaScript）で定義された通りに実行されるカスタムメッセージ。</td>
    <td>該当なし</td>
    <td><span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> 初期化オプションを設定して <code>true</code> アプリ内メッセージを有効にする。</td>
    <td>これは、IAM のすべての利点が必要であり、さらに追加の機能が必要な場合や、ブランドに沿った外観を維持したい場合に適したオプションです。フォント、色、形、サイズ、ボタンなど、メッセージの細部まで変更できる。<br><br>使用例としては、ユーザーにアプリのフィードバックを求める場合、電子メールのキャプチャフォーム、ページ分割されたメッセージなどがある。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>メールキャプチャフォーム</a></td>
    <td>通常、視聴者の電子メールをキャプチャするために使用される。</td>
    <td>該当なし</td>
    <td><span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> 初期化オプションを設定して <code>true</code> アプリ内メッセージを有効にする。</td>
    <td>ユーザーにメールアドレスの送信を促す場合。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>CSS を使った Web モーダル</a></td>
    <td>カスタマイズ可能なCSSによるウェブ用モーダルメッセージ。</td>
    <td>
      <ul>
      <li>テキスト（オプション画像付き）</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>CSS を使った Web モーダルは Web SDK 独自のもので、[<b>Web ブラウザー</b>] を選択した後でのみ使用できます。</td>
    <td>カスタムCSSをアップロードまたは記述して、美しく、あらゆるカスタムスタイルのメッセージングを作成したい場合。</td>
  </tr>
</tbody>
</table>

{% alert important %}
Brazeが、あなたのコードに閉じるボタンや終了ボタンが含まれていないことを検知した場合、追加するよう要求する。便宜上、あなたのコードにコピー＆ペーストできるスニペットを用意した：<br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## ステップ 4:アプリ内でメッセージを作成する

**Compose**タブでは、メッセージの内容と動作のあらゆる面を編集できる。

![新しい顧客を歓迎し、ユーザープロファイルを設定するように促す、サンプルブランドのアプリ内メッセージ。][24]{: style="max-width:85%" }

**Compose」**タブの内容は、前のステップで選択したメッセージ・オプションによって異なるが、以下のオプションのいずれかを含むことができる：

### 言語

**Add Languages**を選択し、表示されたリストから目的の言語を選択します。これで、[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic) がメッセージに挿入されます。コンテンツを記述する前に言語を選択することをお勧めします。これにより、Liquid 内の適切な場所にテキストを入力することができます。私たちの[利用可能な言語の完全なリストを参照してください][18] 。

### 画像

メッセージタイプに応じて、[**画像をアップロード**]、[**バッジを選ぶ**]、または [**Font Awesome**] を使用できます。画像をアップロードするには、[**画像の追加**] をクリックするか、画像の URL を入力します。[**画像を追加**] をクリックすると、**メディアライブラリ**が開き、以前にアップロードした画像を選択したり、新しい画像を追加したりできます。メッセージの種類やプラットフォームによって、推奨される比率や要件が異なる場合がある！

### ヘッダーとボディ

何でも好きなことを書けばいい！完全にカスタム化されたコピー（多くの場合、カスタムHTML機能付き）を含み、[リキッドや]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)他のタイプのパーソナライゼーションを含めるオプションがある。より早くメッセージを伝え、顧客にクリックしてもらうことができれば、それに越したことはない！明確で簡潔なヘッダーとメッセージ内容を推奨する。

メッセージタイプによっては、ヘッダーを必要とせず、従ってヘッダーを要求 しないものもある。

#### ヒント 

##### AI コピーの生成

魅力的な文章を作成するためのサポートが必要な場合は、[AI コピーライティングアシスタント]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/)を使用してみてください。商品名や説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用する。

![アプリ内メッセージ作成画面のメッセージフィールドにある [AI コピーライター] ボタンをクリックします。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}

##### 右から左へのメッセージを作成する

アラビア語やヘブライ語などの右から左へのメッセージ作成にお困りですか？ベストプラクティスについては、[右から左へのメッセージを作成するを]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)参照のこと。

### ボタンテキスト {#buttons}

メッセージタイプで利用可能な場合、テキストの本文の下に最大 2 つのボタンを表示できます。カスタムボタンのテキストと色を作成、編集できる。また、メールキャプチャフォーム内にサービス使用条件のリンクを追加することもできます。

![アプリ内メッセージのプライマリボタンとセカンダリボタン]({% image_buster /assets/img/primary-secondary-buttons.png %}){: style="float:right;margin-left:15px;height:30%;width:30%"}

ボタンを1つしか使用しない場合、追加ボタンを設置するスペースは確保されず、メッセージ下部の空いているスペースに自動的に調整される。

#### プライマリボタンの選択

これらのボタンを独自の色でフォーマットする場合は、ボタン2を使用することをお勧めする。言い換えれば、ユーザーにどちらかのボタンをより多くクリックしてもらいたいのであれば、それが右側にあることを確認する。一般に、右側のボタンはクリックされる可能性が高くなります。特に、メッセージの残りの部分とは若干対照的な色や、目立つ色を使うとその可能性が高まります。この効果は、左側のボタンの外観がメッセージにより溶け込んでいる場合にはさらに強くなります。

### クリック時動作 {#button-actions}

顧客がアプリ内メッセージのボタンをクリックしたときに、次のアクションを使用できます。 

| アクション (Action) | 説明 |
|---|---|
| ウェブURLにリダイレクトする | ネイティブでないウェブページを開く。 |
| [アプリにディープリンクする]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | アプリの既存画面にディープリンクする。 |
| メッセージを閉じる | 現在アクティブなメッセージを閉じる。 |
| カスタムイベントを記録する | トリガーする[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)を選択します。別のアプリ内メッセージを表示したり、追加メッセージをトリガーしたりするために使用できます。 |
| カスタム属性を記録する | 現在のユーザーに設定する[カスタム属性を]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)選択する。 |
| プッシュ許可をリクエストする | ネイティブのプッシュ許可を表示する。詳細については、[プッシュプライミング]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/)と、ユーザーのプッシュプライミングのための[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices)を参照してください。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

注：__Request Push Permission__、__Log Custom Event__、__Log Custom Attribute__オプションは、以下のSDK最小バージョンを必要とする：

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

### iOSデバイスのオプション

必要であれば、アプリ内メッセージをiOSデバイスのみに送信するよう制限することもできる。そのためには、[**変更**] をクリックし、[**iOS デバイスにのみ送信**] を選択します。

### メッセージを閉じる

以下のオプションから選択する：
 
- **自動的に消去:**メッセージを何秒間画面に残すかを選択する。
- **ユーザーのスワイプまたはタッチを待機: **却下または閉じるオプションが必要です。

### スライドアップポジション

この設定はSlideupメッセージタイプにのみ適用される。スライドアップを**アプリ画面の下部から**表示するか、**アプリ画面の上部から**表示するかを選択します。

### HTMLとアセット

この設定はカスタムコードメッセージタイプにのみ適用される。使用可能な領域にHTML をコピーして貼り付け、ZIP ファイルを使用してアセットをアップロードします。

### 電子メールのキャプチャ入力プレースホルダ

この設定は、Eメールキャプチャフォームのメッセージタイプにのみ適用される。Eメール入力フィールドのプレースホルダーテキストとして表示されるカスタムコピーを入力する。デフォルトは「メールアドレスを入力してください」となっています。

## ステップ 5: アプリ内メッセージをスタイリングする

**Style**タブでは、メッセージのビジュアル面をすべて調整できる。画像やバッジをアップロードするか、あらかじめデザインされたバッジアイコンを選ぶ。パレットから選択するか、16進数、RGB、または HSB コードを入力して、ヘッダーと本文テキスト、ボタン、およびバックグラウンドの色を変更します。

**スタイル・**タブの内容は、前のステップで選択したメッセージ・オプションによって異なるが、以下のオプションのいずれかを含むことができる：

| フォーマット | インプット | 説明 |
|---|---|---|
|[カラープロフィール]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/color_profiles_and_css) | アプリ内のメッセージテンプレートギャラリーから申し込む。 | **Apply Templateを**選択し、ギャラリーから選択する。次に、**Save**を選択します。 |
|文字揃え | 左、中央、または右。  | 新しいBraze SDKバージョンでのみ使用可能。 |
|ヘッダー | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できます。  |
|テキスト | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できます。 |
|ボタン | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できます。メッセージの「閉じるボタンのバックグラウンド」と、各ボタンの「背景」、「テキスト」、「境界線」の色を選択できます。 |
| ボタン・ボーダー | HEXカラーコード。 | 新機能です。これにより、プライマリボタンとセカンダリボタンを別々に設定できます。ボタンのアウトラインをコントラストカラーにすることをお勧めする。 |
|背景色 | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できます。これはメッセージ全体の背景であり、本文の後ろにはっきりと表示される。 |
|スクリーンオーバーレイ | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できます。新しいBraze SDKバージョンでのみ使用可能。これは、メッセージ全体を囲むフレームである。 |
|シェブロンまたはその他のメッセージを閉じるオプション | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

送信する前に、必ずメッセージを[プレビューし、テストする]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)こと。

{% alert important %}
一部のアプリ内メッセージタイプには、カスタムHTML (またはCSS またはJavaScript) およびZIP ファイルを使用したアセットのアップロードを超えるスタイル設定のオプションがありません。[CSS付きウェブモーダルでは]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css)、カスタムCSSをアップロードまたは記述して、美しく、あらゆるカスタムスタイルのメッセージングを作成できる。
{% endalert %}

## ステップ 6:追加の設定を行う (オプション)

### キーと値のペア

[キーと値のペア][19] を追加して、ユーザーのデバイスに追加のカスタムフィールドを送ることができます。

## ステップ 7:キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}

キャンペーンの残りの部分を作成します。アプリ内メッセージを作成するためのツールの最適な使用方法については、以下のセクションを参照してください。

#### トリガーを選ぶ

キャンペーンやキャンバスの開始・終了時間と同様に、メッセージのトリガーとなるアクションを選択する。

{% alert important %}
カスタムイベントに基づいてアプリ内メッセージをトリガーする場合は、そのカスタムイベントをSDK を使用して送信する必要があることに注意してください。
{% endalert %}

![トリガーアクションが「セッション開始」に設定されたアクションベースのキャンペーン。]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

アプリ内メッセージ配信は、すべて以下のアクショントリガーに基づいている：

- 購入する
- アプリ／ウェブページを開く
- カスタムイベントの実行(SDK を使用して送信されたイベントでのみ機能)
- 特定のプッシュ・メッセージを開く
- 各ユーザーの現地時間に合わせて、特定の時間に送信するキャンペーンを自動的にスケジュールする。
- メッセージは、毎日、毎週 (オプションで特定の曜日)、または毎月定期的に再発するように設定することもできます。

開始日時は選択する必要がありますが、終了日はオプションです。終了日は、指定した日時の後に特定のアプリ内メッセージがデバイスに表示されるのを停止します。

[サーバーサイドのイベントトリガーと]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=web) [ローカルでのアプリ内メッセージ配信については]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages)、開発者向けドキュメントを参照のこと。

##### オンライン・トリガーとオフライン・トリガー

アプリ内メッセージは、メッセージとトリガーをユーザーのデバイスに送信することで機能する。アプリ内メッセージがデバイスに表示された後、トリガー条件が満たされるまで表示を待機します。アプリ内メッセージがユーザーのデバイスにすでにキャッシュされていれば、Brazeに接続していないオフライン状態（例えば、機内モード）でアプリ内メッセージをトリガーすることもできる。

{% alert important %}
アプリ内メッセージが一度停止されると、メッセージが停止される前にセッションを開始し、その後にトリガーイベントを実行した場合、メッセージを見続けるユーザーが存在する可能性がある。これらのユーザーは、キャンペーンが停止された後でも、ユニークインプレッションとしてカウントされます。
{% endalert %}

#### 優先順位を選ぶ

最後に、アプリ内メッセージのトリガーとなるアクションを選択したら、優先順位も設定する必要があります。同じアクションで2つのメッセージがトリガーされた場合、優先順位の高いメッセージが優先順位の低いメッセージより先にユーザーのデバイスに表示されるようにスケジュールされる。 

メッセージの優先順位は以下の中から選ぶことができる：

- 優先順位が低い（他のメッセージの後に表示される）
- 中位の優先度
- 優先度が高い（他のメッセージより先に表示される）

トリガーされたメッセージの優先順位の高、中、低オプションはバケットなので、複数のメッセージが同じ優先順位を持つ可能性があります。これらのバケツ内で優先順位を設定するには、**「正確な優先順位を設定**」をクリックし、キャンペーンをドラッグ＆ドロップして正しい優先順位で並べることができる。

![アプリ内メッセージキャンペーンとキャンバスの優先順位の設定例。]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### ターゲットとするユーザーを選択する

次に、セグメントまたはフィルターを選択し、オーディエンスを絞り込んで、[ターゲットのユーザーを設定]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)する必要があります。セグメントのおおよその人数について現在の状態を示すスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

{% alert note %}
アプリ内メッセージのステップに遅延がある場合、セグメントメンバーシップは遅延後に評価される。ユーザーが適格である場合、アプリ内メッセージは次の利用可能なセッションで同期されます。
{% endalert %}

##### キャンペーンの適格性とLiquidを再評価する

シナリオによっては、アプリ内メッセージの表示をトリガーとして、ユーザーの適格性を再評価したい場合がある。例えば、頻繁に変更されるカスタム属性をターゲットにしたキャンペーンや、直前のプロフィール変更を反映すべきメッセージなどがある。

![ターゲットユーザーステップのオーディエンスサマリーセクションで、「表示前にキャンペーンの適格性を再評価する」オプションが選択されている。]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %})

**表示前にキャンペーンの適格性を再評価する**]を選択すると、送信前にユーザーがまだこのメッセージの適格者であることを確認するために、Brazeに追加のリクエストが行われる。加えて、[リキッド]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)変数や[コネクテッドコンテンツは]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)、メッセージが表示される前に、その時点でテンプレート化される。

これにより、期限切れまたはアーカイブされたキャンペーン内のユーザーにアプリ内メッセージが送信されるのを防ぐことができる。ユーザーの適格性を再評価しない場合、キャンペーンが期限切れになった後、あるいはメッセージが SDK にありユーザーがこれをトリガーするのを待機しているためにアーカイブされた後でも、ユーザーはアプリ内メッセージを受信します。

{% alert note %}
このオプションを有効にすると、ユーザーがアプリ内メッセージをトリガーしてからメッセージが表示されるまでの間に、追加された適格性とテンプレート化リクエストのためにわずかな遅延（100ミリ秒未満）が生じる。
<br><br>
このオプションは、ユーザーがオフラインの間、または適格性評価と液 体再評価が必要でないときにトリガーされるメッセージには使用しないこと。
{% endalert %}

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間は、最大 30 日間まで設定できます。

{% endtab %}
{% tab キャンバス %}

キャンバスコンポーネントが完成していない場合は、残りのセクションを完成させます。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの「[キャンバスを構築する」]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照のこと。

キャンバス固有のアプリ内メッセージングオプションの詳細については、[キャンバスのアプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas/)を参照してください。

{% endtab %}
{% endtabs %}

## ステップ 8:レビューと展開

キャンペーンやキャンバスの最後の構築が終わったら、その詳細を確認し、[テストし]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)、そして送信する！

次に、[アプリ内メッセージのレポート]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)をチェックして、メッセージングキャンペーンの結果にアクセスする方法を確認してください。

## 知っておくべきこと

### アクティブなアプリ内メッセージキャンペーンの制限

Braze は信頼性とスピードを重視しています。必要なデータだけをBrazeに送信することをお勧めするのと同様に、ブランドに価値を与えなくなったキャンペーンはすべてオフにすることをお勧めする。

アクションベースのアプリ内メッセージキャンペーンを処理すると、まだアクティブな状態であるが、メッセージを送信しなくなったり、不要になったりして、お客様や他のお客様のBrazeサービス全体のパフォーマンスが低下する。このような大量のアイドルキャンペーンを処理するために必要な余分な時間は、アプリ内メッセージがエンドユーザーの端末に表示されるまでに時間がかかることを意味し、エンドユーザーの体験に影響を与える。

{% alert important %}
メッセージ配信の速度を最適化し、タイムアウトを防ぐために、ワークスペースごとに最大200 のアクティブなアクションベースのアプリ内メッセージキャンペーンを設定できます。これはキャンバスには適用されません。
{% endalert %}

200 カウントには、まだ終了時刻に達していないアクティブなアプリ内メッセージキャンペーンと終了時刻がないものが含まれます。終了時刻を過ぎたアクティブなアプリ内メッセージキャンペーンはカウントされません。平均的なBrazeの顧客は、一度に合計26のキャンペーンをアクティブにしているため、この制限が影響を与える可能性は低い。


[2]: {% image_buster /assets/img/iam-generations.gif %}
[16]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img_archive/iam_compose.png %}
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[27]: {% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}
