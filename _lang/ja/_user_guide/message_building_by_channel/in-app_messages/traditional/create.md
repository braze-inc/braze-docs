---
nav_title: アプリ内メッセージを作成する
article_title: アプリ内メッセージを作成する
page_order: 1
description: "この参考記事では、Brazeプラットフォームを使用してキャンペーン、Canvasを使用するか、APIキャンペーンとしてアプリ内メッセージを作成する方法について説明します。"
channel:
  - in-app messages
tool:
  - Campaigns
search_rank: 4.8
---

# アプリ内メッセージを作成する

> アプリ内メッセージまたはブラウザ内メッセージは、キャンペーン、Canvasを使用するか、APIキャンペーンとしてBrazeプラットフォームを使用して作成できます。[便利なアプリ内メッセージ準備ガイドを使用して]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)、事前にメッセージの計画を立て、すべての資料を準備することを強くお勧めします。

## ステップ 1:メッセージを作成する場所を選択してください {#create-new-campaign-in-app}

メッセージをキャンペーンとキャンバスのどちらを使用して送信すべきかわからない?キャンペーンは単一のシンプルなメッセージキャンペーンに適していますが、キャンバスは複数段階のユーザージャーニーに適しています。

{% tabs %}
{% tab Campaign %}

**ステップ:**

1. [**メッセージング**] > [**キャンペーン**] に移動し、[<i class="fas fa-plus"></i>**キャンペーンを作成**] をクリックします。
{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、[**エンゲージメント**] に [**キャンペーン**] が表示されます。
{% endalert %}

{:start="2"}
2\.[**アプリ内メッセージ**] を選択します。アプリ内メッセージはマルチチャネルキャンペーンでは使用できないことに注意してください。
3\.キャンペーンには明確で意味のある名前を付けてください。
4\.[[必要に応じてチームとタグを追加します]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)。
   \* タグを使うと、キャンペーンを簡単に見つけてレポートを作成できます。たとえば、[レポートビルダーを使用する場合]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)、特定のタグでフィルタリングできます。
5\.キャンペーンに必要な数だけバリエーションを追加して名前を付けてください。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、およびレイアウトを選択できます。このトピックの詳細については、「[多変量分析と]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) A/B テスト」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似または同じ内容になる場合は、バリエーションを追加する前にメッセージを作成してください。次に、「**バリエーションを追加**」**ドロップダウンから「バリアントからコピー**」を選択できます。
{% endalert %}

{% endtab %}
{% tab Canvas %}

**ステップ:**

1. [Canvas コンポーザーを使用して Canvas を作成します]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに明確で意味のある名前を付けてください。
3. [ステップスケジュールを選択し]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)、必要に応じて遅延を指定します。アプリ内メッセージを含むステップはアクションベースにはできないことに注意してください。
4. 必要に応じて、このステップでオーディエンスをフィルタリングします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込みます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [昇進行動を選択してください]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)。
6. メッセージとペアリングしたい他のメッセージングチャネルを選択してください。

{% alert important %}
1 つのステップで複数のアプリ内メッセージバリアントを設定することはできません。
{% endalert %}

Canvas固有の情報の詳細については、[Canvasのアプリ内メッセージを参照してください]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/)。

{% endtab %}
{% endtabs %}

## ステップ 2:配信プラットフォームを指定

まず、メッセージを受信するプラットフォームを選択します。この選択を使用して、キャンペーンの配信を特定のアプリセットに制限します。たとえば、モバイルアプリのダウンロードを促すブラウザ内メッセージには **Web** ブラウザを選択し、既にアプリを入手した後にメッセージが届かないようにすることができます。プラットフォームの選択は各バリアントに固有なので、プラットフォームごとにメッセージエンゲージメントをテストしてみてください。

| プラットフォーム | メッセージ配信 |
|---|---|
| モバイルアプリ | iOS & アンドロイド SDK|
| ウェブブラウザ | ウェブ SDK|
| モバイルアプリとウェブブラウザーの両方 | iOS、アンドロイド、ウェブ SDK|
{: .reset-td-br-1 .reset-td-br-2}

## ステップ 3:メッセージタイプを指定してください

送信プラットフォームを選択したら、それに関連するメッセージタイプ、レイアウト、およびその他のオプションを参照します。これらの各メッセージの予想される動作や外観について詳しくは、[クリエイティブの詳細ページをご覧いただくか]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/)、次の表のリンクされたメッセージタイプをクリックしてください。

どのメッセージタイプを使用するかを決める際には、アプリ内メッセージキャンペーンがどの程度邪魔にならないかを考慮する必要があります。これは、メッセージが画面に占めるスペースの量と、アプリやサイトでの顧客の通常のエクスペリエンスがどの程度妨げられるかを示す指標です。配信したいコンテンツが多ければ多いほど、メッセージはより煩わしいものにする必要があります。

![Graphic showing a scale of less intrusive to more intrusive, with slider being the least intrusive, followed by modal, and fullscreen being the most intrusive]({% image_buster /assets/img_archive/iam_intrusive.png %}){: style="max-width:80%" }

### メッセージタイプ

これらのアプリ内メッセージは、モバイルアプリとウェブアプリケーションの両方で受け入れられます。

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
</style>

<table class="tg">
<thead>
  <tr>
    <th>メッセージタイプ</th>
    <th>タイプ説明</th>
    <th>使用可能なレイアウト</th>
    <th>その他のオプション</th>
    <th>推奨用途</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen'>全画面</a></td>
    <td>メッセージブロックで画面全体を覆うメッセージ。</td>
    <td>
      <ul>
      <li>画像とテキスト</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>デバイスの向きの強制 (縦向きまたは横向き)</td>
    <td>大きくて大胆！最も重要なキャンペーン、重要な通知、大規模なプロモーションなど、コンテンツをユーザーに見せたい場合に使用します。<br><br>モバイルデバイスでは、デバイスの向きがメッセージの向きと一致しない場合、縦向きと横向きのメッセージは表示されないことに注意してください。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal'>モーダル</a></td>
    <td>スクリーンオーバーレイとメッセージブロックで画面全体を覆うメッセージ。</td>
    <td>
      <ul>
      <li>テキスト (オプションの画像付き)</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>N/A</td>
    <td>良い中間点。ユーザーに新機能の試用やプロモーションの活用を促すなど、ユーザーの注意を引く明確な方法が必要な場合に使用します。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup'>スライドアップ</a></td>
    <td>画面の他の部分を遮ることなく、指定された場所にスライドして表示されるメッセージ。</td>
    <td>N/A</td>
    <td>N/A</td>
    <td>邪魔にならない—画面のスペースを最小限に抑えます。新機能、お知らせ、クッキーの使用など、ごく一部の情報についてユーザーに警告する場合に使用します。<br></td>
  </tr>
</tbody>
</table>

### 高度なメッセージタイプ

これらのアプリ内メッセージは、ニーズに合わせてカスタマイズできます。

<table class="tg">
<thead>
  <tr>
    <th>メッセージタイプ</th>
    <th>タイプ説明</th>
    <th>使用可能なレイアウト</th>
    <th>要件</th>
    <th>推奨用途</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#custom-html-messages'>カスタム HTML メッセージ</a></td>
    <td>カスタムコード (HTML、CSS、JavaScript) で定義されているとおりに動作するカスタムメッセージ。</td>
    <td>N/A</td>
    <td>アプリ内メッセージを機能させるには、<span style="white-space: nowrap"><code><code>allowUserSuppliedJavaScript初期化オプションをtrueに設定する必要があります</code></code></span>。</td>
    <td>これは、IAMの利点をすべて活用したいが、追加機能が必要な場合や、外観を「ブランドと同じ」にしたい場合に適しています。フォント、色、形、サイズ、ボタンなど、メッセージの細部をすべて変更できます。<br><br>ユースケースの例としては、アプリのフィードバックをユーザーに求めること、メールキャプチャフォーム、ページ分割されたメッセージなどがあります。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#email-capture-form'>メールキャプチャフォーム</a></td>
    <td>通常、視聴者のメールをキャプチャするために使用されます。</td>
    <td>N/A</td>
    <td>アプリ内メッセージを機能させるには、<span style="white-space: nowrap"><code><code>allowUserSuppliedJavaScript初期化オプションをtrueに設定する必要があります</code></code></span>。</td>
    <td>ユーザーにメールアドレスの送信を促すとき。</td>
  </tr>
  <tr>
    <td><a href='/docs/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css'>CSS を使用したウェブモーダル</a></td>
    <td>カスタマイズ可能な CSS を使用した Web 用のモーダルメッセージ。</td>
    <td>
      <ul>
      <li>テキスト (オプションの画像付き)</li>
      <li>画像のみ</li>
      </ul>
    </td>
    <td>CSS を使用した Web モーダルは Web SDK 独自の機能であり、<b>Web ブラウザを選択した後にのみ使用できます</b>。</td>
    <td>カスタム CSS をアップロードまたは作成して、美しく万能なカスタムスタイルのメッセージを作成したいとき。</td>
  </tr>
</tbody>
</table>

{% alert important %}
Braze がコードに [閉じる] または [却下] ボタンが含まれていないことを検出した場合、追加するようお願いします。便宜上、コピーしてコードに貼り付けることができるスニペットを用意しました。<br><br>`<a href= "appboy://close">X</a>`。
{% endalert %}

## ステップ 4: アプリ内メッセージを作成

「**作成**」タブでは、メッセージの内容と動作のあらゆる側面を編集できます。

![][24]{: style="max-width:85%" }

「**作成**」タブの内容は、前のステップで選択したメッセージオプションによって異なりますが、次のオプションのいずれかが含まれる場合があります。

#### 言語

「**言語を追加**」をクリックし、表示されたリストから目的の言語を選択します。これにより、[メッセージにLiquidが挿入されます]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#conditional-logic)。Liquidの該当箇所にテキストを入力できるように、コンテンツを書く前に言語を選択することをおすすめします。[利用可能な言語の全リスト] [18] をご覧ください。

#### 画像

メッセージタイプに応じて、**画像をアップロードしたり**、**バッジを選択したり、**Font Awesomeを使用したりできます****。画像をアップロードするには、「**画像を追加**」をクリックするか、画像の URL を入力します。「**画像を追加**」**をクリックするとメディアライブラリが開き**、以前にアップロードした画像を選択したり、新しい画像を追加したりできます。それぞれのメッセージタイプやプラットフォームには、それぞれ独自の推奨比率や要件がある場合があります。コミッショニングやゼロからの画像作成の前に、それらが何であるかを必ず確認してください。

#### ヘッダーとボディ

好きなことを書いてください！[Liquidやその他のタイプのパーソナライゼーションを含めるオプションとともに]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)、完全にカスタム化されたコピー（多くの場合カスタムHTML機能付き）を含めます。メッセージを伝え、顧客にクリックしてもらうのが早ければ早いほど、良い結果が得られます。ヘッダーとメッセージコンテンツは明確で簡潔にすることをお勧めします。

メッセージタイプの中には、ヘッダーを必要としないため、ヘッダーを必要としないものもあります。

{% alert tip %}
素晴らしいコピーを作成するのに助けが必要ですか？[AIコピーライティングアシスタントを使ってみてください]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/)。商品名または説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用できます。

![Launch AI Copywriter button, located in the Message field of the in-app message composer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_iam.png %}){: style="max-width:60%"}
{% endalert %}

#### ボタンテキスト

メッセージタイプに応じて、テキスト本文の下に最大 2 つのボタンを表示できます。カスタムボタンのテキストと色を作成および編集できます。メールキャプチャフォーム内に利用規約リンクを追加することもできます。

![Primary and secondary buttons in an in-app message]({% image_buster /assets/img/primary-secondary-buttons.png %}){: style="float:right;margin-left:15px;height:30%;width:30%"}

ボタンを 1 つだけ使用することを選択した場合、ボタンを追加するスペースがなくなるため、メッセージの下部にある空き領域が自動的に調整されます。

##### 主ボタンの選択

これらのボタンを独自の色でフォーマットする場合は、より望ましい結果を得るためにボタン 2 を使用することをお勧めします。つまり、ユーザーに 1 つのボタンを他のボタンよりも多くクリックさせたい場合は、そのボタンが右側にあることを確認してください。右のボタンは、特にメッセージの他の部分と多少対照的な色や目立つ色をしている場合に、クリックされる可能性が高くなることがよくあります。これは、左側のボタンがメッセージとより視覚的に調和している場合にのみ強調されます。

#### クリック時動作

お客様がアプリ内メッセージ内のボタンをクリックすると、次のアクションが可能になります。 

| アクション | 説明 |
|---|---|
| Web URLにリダイレクト | 非ネイティブWebページを開きます。|
| [アプリへのディープリンク | アプリの既存の画面へのディープリンク]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content)|
| メッセージを閉じる | 現在アクティブなメッセージを閉じます。|
| カスタムイベントをログに記録する | [トリガーするカスタムイベントを選択します]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)。別のアプリ内メッセージを表示したり、追加のメッセージをトリガーしたりするために使用できます。|
| ログカスタム属性 | [現在のユーザーに設定するカスタム属性を選択します]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/)。|
| プッシュ権限をリクエストする | ネイティブプッシュ権限を表示します。[プッシュプライミングの詳細と]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_primer_messages/)、[ユーザーをプッシュプライミングするためのベストプラクティスをご覧ください]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/#best-practices)。|
{: .reset-td-br-1 .reset-td-br-2}

注:「__プッシュ権限をリクエスト__」、「__カスタムイベントをログに記録する__」、および「__カスタム属性を記録__」オプションには、次の SDK 最小バージョンが必要です。

{% sdk_min_versions swift:5.4.0 android:21.0.0 web:4.0.3 %}

#### iOS デバイスオプション

必要に応じて、アプリ内メッセージを iOS デバイスにのみ送信するように制限できます。そのためには、「**変更**」をクリックし、「**iOSデバイスにのみ送信**」を選択します。

#### メッセージのクローズ

次のオプションから選択します。
 
- **自動的に消去:**メッセージを画面に表示し続ける秒数を選択します。
- **ユーザーがスワイプまたはタッチするまで待つ:**解雇またはクローズオプションが必要です。

#### スライドアップ位置

この設定は Slideup メッセージタイプにのみ適用されます。**スライドアップをアプリ画面の下部から表示するか、**アプリ画面の上部から表示するかを選択します****。

#### HTML とアセット

この設定は、カスタムコードメッセージタイプにのみ適用されます。HTML をコピーして空き領域に貼り付け、ZIP 経由でアセットをアップロードします。

#### メールキャプチャ入力プレースホルダー

この設定は、メールキャプチャフォームのメッセージタイプにのみ適用されます。メール入力フィールドのプレースホルダーテキストとして表示されるカスタムコピーを入力します。デフォルトは「メールアドレスを入力してください」です。

## ステップ 5: アプリ内メッセージのスタイルを設定する

「**スタイル**」タブでは、メッセージのあらゆる視覚的側面を調整できます。画像やバッジをアップロードするか、あらかじめデザインされたバッジアイコンを選択してください。パレットから選択するか、16 進数、RGB、または HSB コードを入力して、ヘッダーと本文のテキスト、ボタン、および背景の色を変更します。

「**スタイル**」タブの内容は、前のステップで選択したメッセージオプションによって異なりますが、次のオプションのいずれかが含まれる場合があります。

| フォーマット | 入力 | 説明 |
|---|---|---|
|カラープロファイル | アプリ内メッセージテンプレートギャラリーから適用 | [**テンプレートを適用**] をクリックしてギャラリーから選択します。次に、[**保存**] をクリックします。|
|テキストの配置 | 左、中央、または右。| 新しいBraze SDKバージョンでのみ使用できます。|
|ヘッダー | HEXカラーコード | 希望するHEXカラーが表示されます。また、色の不透明度も選択できます。|
|テキスト | HEXカラーコード | 希望するHEXカラーが表示されます。また、色の不透明度も選択できます。|
|ボタン | HEXカラーコード | 希望するHEXカラーが表示されます。また、色の不透明度も選択できます。メッセージの [閉じる] ボタンの背景と、各ボタンの背景、テキスト、境界線の色を選択できます。|
| ボタンボーダー | HEXカラーコード | 新登場!これにより、主ボタンと副ボタンを互いに区別することができます。対照的な色でボタンの輪郭を描くことをお勧めします。|
|背景色 | HEXカラーコード | 希望するHEXカラーが表示されます。また、色の不透明度も選択できます。これはメッセージ全体の背景で、テキスト本文の後ろにはっきりと表示されます。|
|スクリーンオーバーレイ | HEXカラーコード | 希望するHEXカラーが表示されます。また、色の不透明度も選択できます。新しいBraze SDKバージョンでのみ利用可能です。これはメッセージ全体を囲むフレームです。|
|シェブロンまたはその他のクローズメッセージオプション | HEXカラーコード | 希望するHEXカラーが表示されます。また、色の不透明度も選択できます。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

送信する前に、[必ずメッセージをプレビューしてテストしてください]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)。

{% alert important %}
一部のアプリ内メッセージタイプには、カスタム HTML (または CSS または JavaScript) とアセットを ZIP 経由でアップロードする以外にスタイルを設定するオプションがありません。[Web Modal with CSS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#web-modal-css) を使用すると、カスタム CSS をアップロードまたは作成して、美しく万能なカスタムスタイルのメッセージを作成できます。
{% endalert %}

## ステップ 6:その他の設定を行う (オプション)

### キーと値のペア

[キーと値のペア] [19] を追加して、追加のカスタムフィールドをユーザーデバイスに送信できます。

## ステップ 7:残りのキャンペーンやキャンバスを作成

{% tabs %}
{% tab Campaign %}

キャンペーンの残りの部分も作成してください。アプリ内メッセージの作成に当社のツールを最適に使用する方法の詳細については、以下のセクションをご覧ください。

#### トリガーを選択する

メッセージをトリガーしたいアクションと、キャンペーンまたはキャンバスの開始時間と終了時間を選択します。

{% alert important %}
カスタムイベントに基づいてアプリ内メッセージをトリガーする場合、そのカスタムイベントはSDK経由で送信する必要があることに注意してください。
{% endalert %}

![Action-based campaign with the trigger action set to "Start Session".]({% image_buster /assets/img_archive/in_app_schedule.png %}){: style="max-width:80%"}

アプリ内メッセージ配信は、すべて次のアクショントリガーに基づいています。

- 購入をする
- アプリ/ウェブページを開く
- カスタムイベントの実行 (SDK 経由で送信されたイベントでのみ機能します)
- 特定のプッシュメッセージを開く
- 各ユーザーの現地時間を基準に、特定の時間に送信するようにキャンペーンを自動的にスケジュールします。
- メッセージは、毎日、毎週 (オプションで特定の日)、または毎月繰り返すように構成することもできます。

開始日時を選択する必要があります。ただし、終了日はオプションです。終了日を設定すると、指定した日付/時刻を過ぎると、その特定のアプリ内メッセージがデバイスに表示されなくなります。

[[サーバー側のイベントトリガーとローカルアプリ内メッセージ配信については]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#local-in-app-messages)]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/)、開発者向けドキュメントを参照してください。

##### オンライントリガーとオフライントリガー

アプリ内メッセージは、メッセージとトリガーをユーザーのデバイスに送信することで機能します。アプリ内メッセージがデバイスに届いた後、トリガー条件が満たされるまで表示を待ちます。アプリ内メッセージがユーザーのデバイスに既にキャッシュされている場合は、Braze に接続せずにオフラインでアプリ内メッセージをトリガーすることもできます（機内モードなど）。

{% alert important %}
アプリ内メッセージが停止された後も、メッセージが停止される前にセッションを開始し、その後トリガーイベントを実行すると、引き続きメッセージが表示されるユーザーもいる可能性があります。これらのユーザーは、キャンペーンが中止された後でもユニークインプレッションとしてカウントされます。
{% endalert %}

#### 優先度を選択してください

最後に、アプリ内メッセージがトリガーされるアクションを選択したら、優先順位も設定する必要があります。同じアクションで2つのメッセージがトリガーされた場合、優先度の高いメッセージは、優先度の低いメッセージの前にユーザーのデバイスに表示されるようにスケジュールされます。 

次のメッセージ優先度を選択できます。

- 低優先度 (他のメッセージより後に表示)
- 中優先度
- 高優先度 (他のメッセージより前に表示)

トリガーされたメッセージの優先度の「高」、「中」、「低」のオプションはバケットなので、複数のメッセージに同じ優先度を設定できます。これらのバケット内で優先順位を設定するには、「**厳密優先度を設定**」をクリックします。そうすると、キャンペーンをドラッグアンドドロップして正しい優先順位で並べることができます。

![\]({% image_buster /assets/img_archive/bucket_prioritization.png %}){: style="max-width:70%"}

#### ターゲットにするユーザーを選択

次に、[セグメントまたはフィルターを選択してユーザーをターゲットにし]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)、オーディエンスを絞り込む必要があります。現在のおおよそのセグメント人口がどのようになっているかのスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

{% alert note %}
アプリ内メッセージステップに遅延がある場合、遅延後にセグメントメンバーシップが評価されます。ユーザーが資格を満たしている場合、アプリ内メッセージは次の利用可能なセッションで同期されます。
{% endalert %}

##### キャンペーンの適格性と Liquid を再評価する

シナリオによっては、アプリ内メッセージが表示されるので、ユーザーの適格性を再評価したい場合があります。例としては、頻繁に変更されるカスタム属性をターゲットとするキャンペーンや、直前のプロファイル変更を反映する必要があるメッセージをターゲットとするキャンペーンなどがあります。

![Audience Summary section of the Target Users step with the option to "Re-evaluate campaign eligibility before displaying" selected.]({% image_buster /assets/img_archive/re-evaluate-iam-membership.png %})

[**表示前にキャンペーンの適格性を再評価する] を選択すると、送信前にユーザーがまだこのメッセージの対象であることを確認するための追加リクエストが** Braze に送信されます。さらに、メッセージが表示される前の時点で、[[Liquid変数または接続コンテンツがテンプレート化されます]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/)]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)。

これにより、期限切れまたはアーカイブされたキャンペーン内のユーザーにアプリ内メッセージが送信されるのを防ぎます。ユーザーの適格性を再評価しない場合、メッセージはSDKにあり、ユーザーがトリガーするのを待っているため、キャンペーンの有効期限が切れたりアーカイブされたりした後でも、ユーザーはアプリ内メッセージを受け取ります。

{% alert note %}
このオプションを有効にすると、追加の資格とテンプレートリクエストにより、ユーザーがアプリ内メッセージをトリガーしてからメッセージが表示されるまでにわずかな遅延（100 ミリ秒未満）が発生します。
<br><br>
ユーザーがオフラインのときにトリガーされる可能性があるメッセージや、資格やLiquidの再評価が不要なメッセージには、このオプションを使用しないでください。
{% endalert %}

#### コンバージョンイベントを選択する

Brazeでは、キャンペーンを受け取った後、[ユーザーが特定のアクションやコンバージョンイベントを実行する頻度を追跡できます]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間を最大 30 日間設定できます。

{% endtab %}
{% tab Canvas %}

まだ行っていない場合は、Canvas コンポーネントの残りのセクションを完了してください。Canvasの残りの部分を構築する方法、多変量分析テストやインテリジェントセレクションを実装する方法などの詳細については、[Canvasドキュメントの「キャンバスの構築]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)」ステップを参照してください。

Canvas固有のアプリ内メッセージオプションについては、「[Canvasのアプリ内メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/)」を参照してください。

{% endtab %}
{% endtabs %}

## ステップ 8:確認とデプロイ

最後のキャンペーンやキャンバスの作成が終わったら、[詳細を確認してテストし]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)、送信しましょう！

次に、[アプリ内メッセージレポートを確認して]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/)、メッセージングキャンペーンの結果にアクセスする方法を確認してください。

## 知っておくべきこと

### アクティブなアプリ内メッセージキャンペーンの制限

Brazeは信頼性とスピードを重視しています。必要なデータだけを Braze に送信することをおすすめするのと同じように、ブランドに何の価値ももたらさなくなったキャンペーンはオフにすることをおすすめします。

アクションベースのアプリ内メッセージキャンペーンで、まだアクティブな状態でメッセージが送信されなくなったり、不要になったりすると、あなたや他の顧客に対するBrazeサービスの全体的なパフォーマンスが低下します。このような大量のアイドルキャンペーンの処理に余分な時間がかかるため、アプリ内メッセージがエンドユーザーのデバイスに表示されるまでに時間がかかり、エンドユーザーのエクスペリエンスに影響します。

{% alert important %}
メッセージ配信の速度を最適化し、タイムアウトを防ぐために、ワークスペースごとにアクティブなアクションベースのアプリ内メッセージキャンペーンは200に制限されています。これはキャンバスには適用されません。
{% endalert %}

200件には、まだ終了時間に達していないアクティブなアプリ内メッセージキャンペーンと、終了時間がないキャンペーンが含まれます。終了時間を過ぎたアクティブなアプリ内メッセージキャンペーンはカウントされません。平均的な Braze の顧客は、一度に合計 26 件のキャンペーンを実施しているため、この制限による影響はほとんどありません。


[2]: {% image_buster /assets/img/iam-generations.gif %}
[16]: {{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/
[18]: {{site.baseurl}}/developer_guide/platform_integration_guides/android/advanced_use_cases/localization/#languages-supported
[19]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/
[24]: {% image_buster /assets/img_archive/iam_compose.png %}
[25]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/
[26]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[27]: {% image_buster /assets/img_archive/re-evaluate-iam-membership.png %}
