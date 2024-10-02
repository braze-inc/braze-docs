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

> Brazeプラットフォームを使って、キャンペーン、キャンバス、またはAPIキャンペーンとして、アプリ内メッセージまたはブラウザ内メッセージを作成できる。便利な[アプリ内メッセージ準備ガイドを使って]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)、事前にメッセージを計画し、すべての資料を準備することを強くお勧めする。

## ステップ 1:メッセージを発信する場所を選ぶ {#create-new-campaign-in-app}

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. **Messaging**>**Campaignsに**進み、<i class="fas fa-plus"></i> **Create Campaignを**クリックする。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、\[**エンゲージメント**] の下に \[**キャンペーン**] が表示されます。
{% endalert %}

{:start="2"}
2\.**アプリ内メッセージを**選択する。なお、アプリ内メッセージはマルチチャネルキャンペーンでは利用できない。
3\.キャンペーンに、明確で意味のある名前を付けます。
4\.必要に応じて、\[[チーム]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)] と \[[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)] を追加します。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、\[[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、\[**バリアントを追加**] ドロップダウンから \[**バリアントをコピー**] を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**ステップ:**

1. キャンバス作成ツールを使用して \[[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. \[[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。アプリ内メッセージを含むステップは、アクションベースにはできない。
4. このステップでは、必要に応じて聴衆をフィルタリングする。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。視聴者オプションは、遅延の後、メッセージが送信された時点でチェックされる。
5. \[[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせる他のメッセージングチャネルを選択します。

{% alert important %}
1つのステップで複数のアプリ内メッセージのバリエーションを持つことはできない。
{% endalert %}

キャンバス固有の情報は、[キャンバスのアプリ内メッセージで]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/)確認できる。

{% endtab %}
{% endtabs %}

## ステップ 2:配信プラットフォームを指定する

まず、どのプラットフォームがメッセージを受け取るかを選択することから始める。この選択を使用して、キャンペーンの配信を特定のアプリのセットに制限する。例えば、モバイルアプリのダウンロードを促すブラウザ内メッセージに**ウェブブラウザを**選択し、すでにアプリを入手した後にメッセージを受け取らないようにする。プラットフォームの選択はそれぞれのバリアントに固有なので、プラットフォームごとにメッセージのエンゲージメントをテストしてみるのもいいだろう！

| プラットフォーム | メッセージの配信 |
|---|---|
| モバイルアプリ | iOS & Android SDK|
| ウェブブラウザ | ウェブSDK|
| モバイルアプリとウェブブラウザの両方 | iOS、Android、Web SDK|
{: .reset-td-br-1 .reset-td-br-2}

## ステップ 3:メッセージの種類を指定する

送信プラットフォームを選択したら、そのプラットフォームに関連するメッセージタイプ、レイアウト、その他のオプションをブラウズする。各メッセージの期待される動作や見た目については、[クリエイティブの詳細]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)ページで、または以下の表のリンク先のメッセージタイプをクリックして詳細を確認してほしい。

どのメッセージタイプを使うかを決める際には、アプリ内メッセージキャンペーンをどの程度押し付けがましくする必要があるかを検討する必要がある。これは、メッセージがどれだけの画面領域を占め、あなたのアプリやサイトでの顧客の通常の体験をどれだけ妨げるかを示す指標である。配信したいコンテンツがリッチになればなるほど、メッセージはより押しつけがましくなる。

![スライダーが最も邪魔でなく、モーダルがそれに続き、フルスクリーンが最も邪魔である。]({% image_buster /assets/img_archive/iam_intrusive.png %}){: style="max-width:80%" }

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
    <th>タイプ</th>
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
    <td>大きくて大胆だ！最も重要なキャンペーン、重要な通知、大規模なプロモーションなど、ユーザーに確実にコンテンツを見てもらいたい場合に使用する。<br><br>モバイル・デバイスでは、デバイスの向きとメッセージの向きが一致しない場合、縦向きと横向きのメッセージは表示されないことに注意。</td>
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
    <td>良い中間地点だ。ユーザーに新機能を試してもらったり、プロモーションを利用してもらうなど、ユーザーの注意を引く明白な方法が必要な場合に使用する。</td>
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

### 高度なメッセージ・タイプ

これらのアプリ内メッセージは、あなたのニーズに合わせてカスタマイズできる。

<table class="tg">
<thead>
  <tr>
    <th>メッセージの種類</th>
    <th>タイプ</th>
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
    <td>設定する必要がある <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> 初期化オプションを <code>true</code> アプリ内メッセージを有効にする。</td>
    <td>これは、IAMのすべての利点を求めるが、追加機能が必要な場合や、外観を "on brand "に保ちたい場合に有効なオプションである。フォント、色、形、サイズ、ボタンなど、メッセージの細部まで変更できる。<br><br>使用例としては、ユーザーにアプリのフィードバックを求める場合、電子メールのキャプチャフォーム、ページ分割されたメッセージなどがある。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>メール・キャプチャ・フォーム</a></td>
    <td>通常、視聴者の電子メールをキャプチャするために使用される。</td>
    <td>該当なし</td>
    <td>設定する必要がある <span style="white-space: nowrap"><code>allowUserSuppliedJavascript</code></span> 初期化オプションを <code>true</code> アプリ内メッセージを有効にする。</td>
    <td>ユーザーにメールアドレスの送信を促す場合。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>CSSを使ったウェブモーダル</a></td>
    <td>カスタマイズ可能なCSSによるウェブ用モーダルメッセージ。</td>
    <td>
      <ul>
      <li>テキスト（オプション画像付き）</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>Web Modal with CSSはWeb SDK独自のもので、<b>Web Browsersを</b>選択しないと使えない。</td>
    <td>カスタムCSSをアップロードまたは記述して、美しく、あらゆるカスタムスタイルのメッセージングを作成したい場合。</td>
  </tr>
</tbody>
</table>

{% alert important %}
Brazeが、あなたのコードに閉じるボタンや終了ボタンが含まれていないことを検知した場合、追加するよう要求する。便宜上、あなたのコードにコピー＆ペーストできるスニペットを用意した：<br><br>`<a href= "appboy://close">X</a>`.
{% endalert %}

## ステップ 4:アプリ内でメッセージを作成する

**Compose**タブでは、メッセージの内容と動作のあらゆる面を編集できる。

![][24]{: style="max-width:85%" }

**Compose」**タブの内容は、前のステップで選択したメッセージ・オプションによって異なるが、以下のオプションのいずれかを含むことができる：

#### 言語

**Add Languagesを**クリックし、提供されたリストから希望の言語を選択する。これで[リキッドが]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic)メッセージに挿入される。コンテンツを書く前に言語を選択することをお勧めする。私たちの\[利用可能な言語の完全なリストを参照してください][18] 。

#### イメージ

メッセージの種類によって、**画像のアップロード**、**バッジの選択**、**Font Awesomeの**使用ができる。画像をアップロードするには、**画像の追加を**クリックするか、画像のURLを入力する。**画像の追加を**クリックすると**メディア・ライブラリーが**開き、以前にアップロードした画像を選択したり、新しい画像を追加したりできる。メッセージの種類やプラットフォームによって、推奨される比率や要件が異なる場合がある！

#### ヘッダーとボディ

何でも好きなことを書けばいい！完全にカスタム化されたコピー（多くの場合、カスタムHTML機能付き）を含み、[リキッドや]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)他のタイプのパーソナライゼーションを含めるオプションがある。より早くメッセージを伝え、顧客にクリックしてもらうことができれば、それに越したことはない！明確で簡潔なヘッダーとメッセージ内容を推奨する。

メッセージタイプによっては、ヘッダーを必要とせず、従ってヘッダーを要求 しないものもある。

{% alert tip %}
素晴らしいコピーの作成にお困りですか？[AIコピーライティング・アシスタントを使って]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/)みよう。商品名や説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用する。

![アプリ内メッセージコンポーザーのメッセージ欄にある「AIコピーライター」ボタンを起動する。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}
{% endalert %}

#### ボタンテキスト {#buttons}

メッセージタイプで利用可能な場合、本文の下に最大2つのボタンを表示させることができる。カスタムボタンのテキストと色を作成、編集できる。また、Eメールキャプチャフォーム内に利用規約リンクを追加することもできる。

![アプリ内メッセージのプライマリボタンとセカンダリボタン]({% image_buster /assets/img/primary-secondary-buttons.png %}){: style="float:right;margin-left:15px;height:30%;width:30%"}

ボタンを1つしか使用しない場合、追加ボタンを設置するスペースは確保されず、メッセージ下部の空いているスペースに自動的に調整される。

##### プライマリー・ボタンを選ぶ

これらのボタンを独自の色でフォーマットする場合は、ボタン2を使用することをお勧めする。言い換えれば、ユーザーにどちらかのボタンをより多くクリックしてもらいたいのであれば、それが右側にあることを確認する。右のボタンはクリックされる可能性が高く、特にメッセージの他の部分とは対照的な、あるいは目立つ色であることが多い。これは、左側のボタンがメッセージとより視覚的に調和している場合にのみ強調される。

#### オン・クリック動作 {#button-actions}

顧客がアプリ内メッセージのボタンをクリックすると、以下のアクションが利用できる。 

| アクション (Action) | 説明 |
|---|---|
| ウェブURLにリダイレクトする | ネイティブでないウェブページを開く。 |
| [アプリへのディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content) | アプリの既存画面にディープリンクする。 |
| メッセージを閉じる | 現在アクティブなメッセージを閉じる。 |
| カスタムイベントを記録する | トリガーする[カスタムイベントを]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)選択する。別のアプリ内メッセージを表示したり、追加メッセージのトリガーとして使用できる。 |
| ログ・カスタム属性 | 現在のユーザーに設定する[カスタム属性を]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)選択する。 |
| プッシュ許可をリクエストする | ネイティブのプッシュ許可を表示する。[プッシュ・プライミングの]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)詳細と、プッシュのための[ベスト・プラクティスを]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices)読む。 |
{: .reset-td-br-1 .reset-td-br-2}

注：__Request Push Permission__、__Log Custom Event__、__Log Custom Attribute__オプションは、以下のSDK最小バージョンを必要とする：

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

#### iOSデバイスのオプション

必要であれば、アプリ内メッセージをiOSデバイスのみに送信するよう制限することもできる。そのためには、**Changeを**クリックし、**Only send to iOS devicesを**選択する。

#### メッセージを閉じる

以下のオプションから選択する：
 
- **自動的に消去:**メッセージを何秒間画面に残すかを選択する。
- **ユーザーのスワイプまたはタッチを待つ：**解任またはクローズのオプションが必要である。

#### スライドアップポジション

この設定はSlideupメッセージタイプにのみ適用される。スライドアップを**アプリ画面の下から**または**アプリ画面の上から**表示するように選択します。

#### HTMLとアセット

この設定はカスタムコードメッセージタイプにのみ適用される。空いているスペースにHTMLをコピー＆ペーストし、ZIPでアセットをアップロードする。

#### 電子メールのキャプチャ入力プレースホルダ

この設定は、Eメールキャプチャフォームのメッセージタイプにのみ適用される。Eメール入力フィールドのプレースホルダーテキストとして表示されるカスタムコピーを入力する。デフォルトは "Enter your email address "となっている。

## ステップ 5: アプリ内メッセージをスタイリングする

**Style**タブでは、メッセージのビジュアル面をすべて調整できる。画像やバッジをアップロードするか、あらかじめデザインされたバッジアイコンを選ぶ。パレットから選択するか、16進数、RGB、またはHSBコードを入力して、ヘッダーと本文テキスト、ボタン、および背景の色を変更する。

**スタイル・**タブの内容は、前のステップで選択したメッセージ・オプションによって異なるが、以下のオプションのいずれかを含むことができる：

| フォーマット | インプット | 説明 |
|---|---|---|
|カラープロフィール | アプリ内のメッセージテンプレートギャラリーから申し込む。 | **Apply Templateを**クリックし、ギャラリーから選択する。そして、**Saveを**クリックする。 |
|文字揃え | 左、中央、右のいずれかだ。  | 新しいBraze SDKバージョンでのみ使用可能。 |
|ヘッダー | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できる。  |
|テキスト | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できる。 |
|ボタン | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できる。メッセージの「閉じるボタンの背景」、各ボタンの「背景」、「テキスト」、「ボーダー」の色を選択できる。 |
| ボタン・ボーダー | HEXカラーコード。 | 新しい！これにより、プライマリボタンとセカンダリボタンを別々に設定することができる。ボタンのアウトラインをコントラストカラーにすることをお勧めする。 |
|背景色 | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できる。これはメッセージ全体の背景であり、本文の後ろにはっきりと表示される。 |
|スクリーンオーバーレイ | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できる。新しいBraze SDKバージョンでのみ使用可能。これは、メッセージ全体を囲むフレームである。 |
|シェブロンまたはその他のクローズメッセージオプション | HEXカラーコード。 | 希望のHEXカラーが表示される。色の不透明度も選択できる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

送信する前に、必ずメッセージを[プレビューし、テストする]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)こと。

{% alert important %}
アプリ内メッセージの種類によっては、ZIP経由でカスタムHTML（またはCSSやJavaScript）やアセットをアップロードする以上のスタイリングオプションがないものもある。[CSS付きウェブモーダルでは]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css)、カスタムCSSをアップロードまたは記述して、美しく、あらゆるカスタムスタイルのメッセージングを作成できる。
{% endalert %}

## ステップ 6:追加設定を行う（オプション）

### キーと値のペア

キーと値のペア][19] ]を追加して、ユーザー・デバイスに追加のカスタム・フィールドを送ることができる。

## ステップ 7:キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}

アプリ内メッセージの作成に最適なツールの使い方については、以下のセクションを参照のこと。

#### トリガーを選ぶ

キャンペーンやキャンバスの開始・終了時間と同様に、メッセージのトリガーとなるアクションを選択する。

{% alert important %}
カスタム・イベントに基づいてアプリ内メッセージをトリガーする場合、そのカスタム・イベントはSDK経由で送信されなければならない。
{% endalert %}

![トリガーアクションが「セッション開始」に設定されたアクションベースのキャンペーン。]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

アプリ内メッセージ配信は、すべて以下のアクショントリガーに基づいている：

- 購入する
- アプリ／ウェブページを開く
- カスタムイベントを実行する（SDK経由で送信されたイベントでのみ機能する）
- 特定のプッシュ・メッセージを開く
- 各ユーザーの現地時間に合わせて、特定の時間に送信するキャンペーンを自動的にスケジュールする。
- メッセージは、毎日、毎週（オプションで特定の日に）、または毎月、繰り返し送信されるように設定することもできる。

開始日時は必ず選択しなければならないが、終了日時は任意である。終了日を指定すると、指定した日時以降、特定のアプリ内メッセージがデバイスに表示されなくなる。

[サーバーサイドのイベントトリガーと]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/) [ローカルでのアプリ内メッセージ配信については]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages)、開発者向けドキュメントを参照のこと。

##### オンライン・トリガーとオフライン・トリガー

アプリ内メッセージは、メッセージとトリガーをユーザーのデバイスに送信することで機能する。アプリ内メッセージがデバイスに表示された後、トリガー条件が満たされるまで表示を待つ。アプリ内メッセージがユーザーのデバイスにすでにキャッシュされていれば、Brazeに接続していないオフライン状態（例えば、機内モード）でアプリ内メッセージをトリガーすることもできる。

{% alert important %}
アプリ内メッセージが一度停止されると、メッセージが停止される前にセッションを開始し、その後にトリガーイベントを実行した場合、メッセージを見続けるユーザーが存在する可能性がある。これらのユーザーは、キャンペーンが中止された後でも、ユニーク・インプレッションとしてカウントされる。
{% endalert %}

#### 優先順位を選ぶ

最後に、アプリ内メッセージのトリガーとなるアクションを選択したら、優先順位も設定する。同じアクションで2つのメッセージがトリガーされた場合、優先順位の高いメッセージが優先順位の低いメッセージより先にユーザーのデバイスに表示されるようにスケジュールされる。 

メッセージの優先順位は以下の中から選ぶことができる：

- 優先順位が低い（他のメッセージの後に表示される）
- 中位の優先度
- 優先度が高い（他のメッセージより先に表示される）

トリガーされたメッセージの優先順位の高、中、低オプションはバケツであ り、複数のメッセージが同じ優先順位を持つ可能性がある。これらのバケツ内で優先順位を設定するには、**「正確な優先順位を設定**」をクリックし、キャンペーンをドラッグ＆ドロップして正しい優先順位で並べることができる。

![]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### ターゲットとするユーザーを選択する

次に、セグメントやフィルターを選択することで、[ユーザーを絞り込む]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)必要がある。セグメントのおおよその人数について現在の状態を示すスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

{% alert note %}
アプリ内メッセージのステップに遅延がある場合、セグメントメンバーシップは遅延後に評価される。ユーザーに資格があれば、アプリ内メッセージは次に利用可能なセッションで同期される。
{% endalert %}

##### キャンペーンの適格性と液体を再評価する

シナリオによっては、アプリ内メッセージの表示をトリガーとして、ユーザーの適格性を再評価したい場合がある。例えば、頻繁に変更されるカスタム属性をターゲットにしたキャンペーンや、直前のプロフィール変更を反映すべきメッセージなどがある。

![ターゲットユーザーステップのオーディエンスサマリーセクションで、「表示前にキャンペーンの適格性を再評価する」オプションが選択されている。]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %})

**表示前にキャンペーンの適格性を再評価する**]を選択すると、送信前にユーザーがまだこのメッセージの適格者であることを確認するために、Brazeに追加のリクエストが行われる。加えて、[リキッド]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)変数や[コネクテッドコンテンツは]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)、メッセージが表示される前に、その時点でテンプレート化される。

これにより、期限切れまたはアーカイブされたキャンペーン内のユーザーにアプリ内メッセージが送信されるのを防ぐことができる。ユーザーの適格性を再評価しない場合、キャンペーンが期限切れまたはアーカイブされた後でも、ユーザーはアプリ内メッセージを受け取ることになる。

{% alert note %}
このオプションを有効にすると、ユーザーがアプリ内メッセージをトリガーしてからメッセージが表示されるまでの間に、追加された適格性とテンプレート化リクエストのためにわずかな遅延（100ミリ秒未満）が生じる。
<br><br>
このオプションは、ユーザーがオフラインの間、または適格性評価と液 体再評価が必要でないときにトリガーされるメッセージには使用しないこと。
{% endalert %}

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間は、最大 30 日間まで設定できます。

{% endtab %}
{% tab キャンバス %}

まだやっていない場合は、キャンバス・コンポーネントの残りのセクションを完成させる。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの「[キャンバスを構築する」]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照のこと。

Canvas固有のアプリ内メッセージオプションについては、[Canvasのアプリ内]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/)メッセージを参照のこと。

{% endtab %}
{% endtabs %}

## ステップ 8:レビューと展開

キャンペーンやキャンバスの最後の構築が終わったら、その詳細を確認し、[テストし]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)、そして送信する！

次に、[アプリ内メッセージの]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)レポートをチェックして、メッセージングキャンペーンの結果にアクセスする方法を学ぼう。

## 知っておくべきこと

### アクティブなアプリ内メッセージキャンペーンの制限

ブレイズは信頼性とスピードを重視している。必要なデータだけをBrazeに送信することをお勧めするのと同様に、ブランドに価値を与えなくなったキャンペーンはすべてオフにすることをお勧めする。

アクションベースのアプリ内メッセージキャンペーンを処理すると、まだアクティブな状態であるが、メッセージを送信しなくなったり、不要になったりして、お客様や他のお客様のBrazeサービス全体のパフォーマンスが低下する。このような大量のアイドルキャンペーンを処理するために必要な余分な時間は、アプリ内メッセージがエンドユーザーの端末に表示されるまでに時間がかかることを意味し、エンドユーザーの体験に影響を与える。

{% alert important %}
メッセージの配信速度を最適化し、タイムアウトを防ぐため、ワークスペースごとに、アクティブなアクションベースのアプリ内メッセージキャンペーンは200件までという制限がある。キャンバスには適用されない。
{% endalert %}

200カウントには、終了時刻を迎えていないアクティブなアプリ内メッセージキャンペーンと、終了時刻を迎えていないキャンペーンが含まれる。終了時間を過ぎたアクティブなアプリ内メッセージキャンペーンはカウントされない。平均的なBrazeの顧客は、一度に合計26のキャンペーンをアクティブにしているため、この制限が影響を与える可能性は低い。


[2]: {% image_buster /assets/img/iam-generations.gif %}
[16]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img_archive/iam_compose.png %}
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[27]: {% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}
