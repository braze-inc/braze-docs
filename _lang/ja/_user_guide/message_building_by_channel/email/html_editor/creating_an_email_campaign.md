---
nav_title: 概要
article_title: カスタム HTML を使用したメールの作成
page_order: 1
description: "この参考記事では、Braze プラットフォームを使用してメールを作成する方法について説明します。メッセージを作成する方法、コンテンツをプレビューする方法、キャンペーンやキャンバスをスケジュールする方法に関するベストプラクティスも含まれています。"
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# カスタム HTML を使用したメールの作成

> メールメッセージは、ユーザーの思いどおりにコンテンツを配信するのに最適です。また、アプリをアンインストールしたユーザーを再び呼び込むための優れたツールでもあります。カスタマイズおよびカスタマイズされたメールメッセージを送信すると、ユーザーエクスペリエンスが向上し、ユーザーがアプリから最大限の価値を引き出すことができます。 

メールキャンペーンの例については、[ケーススタディをご覧ください](https://www.braze.com/customers)。 

{% alert tip %}
メールキャンペーンを初めて作成する場合は、次の Braze Learning コースを確認することを強くお勧めします。<br>

- [メール](https://learning.braze.com/messaging-channels-email)
- [プロジェクト:基本的なメールマーケティングプログラムの構築](https://learning.braze.com/project-build-a-basic-email-marketing-program)

{% endalert %}

## ステップ 1:メッセージを作成する場所を選択してください

メッセージをキャンペーンとキャンバスのどちらを使用して送信すべきかわからない?キャンペーンは単一のシンプルなメッセージキャンペーンに適していますが、キャンバスは複数段階のユーザージャーニーに適しています。

{% tabs %}
{% tab Campaign %}

**ステップ:**

1. [**メッセージング**] > [**キャンペーン**] に移動し、[**\+ キャンペーンを作成**] をクリックします。
{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、[**エンゲージメント**] に [**キャンペーン**] が表示されます。
{% endalert %}

{:start=“2"}
2\.[**メール**] を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は [**マルチチャネルキャンペーン**] を選択します。
3\.キャンペーンには明確で意味のある名前を付けてください。
4\.[[必要に応じてチームとタグを追加します]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)。
   \* タグを使うと、キャンペーンを簡単に見つけてレポートを作成できます。たとえば、[レポートビルダーを使用する場合]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)、特定のタグでフィルタリングできます。
5\.キャンペーンに必要な数だけバリエーションを追加して名前を付けてください。このトピックの詳細については、「[多変量分析と]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) A/B テスト」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似または同じ内容になる場合は、バリエーションを追加する前にメッセージを作成してください。次に、「**バリエーションを追加**」**ドロップダウンから「バリアントからコピー**」を選択できます。
{% endalert %}
{% endtab %}
{% tab Canvas %}

**ステップ:**

1. [Canvas コンポーザーを使用して Canvas を作成します]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに明確で意味のある名前を付けてください。
3. [ステップスケジュールを選択し]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)、必要に応じて遅延を指定します。
4. 必要に応じて、このステップでオーディエンスをフィルタリングします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込みます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [昇進行動を選択してください]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)。
6. メッセージとペアリングしたい他のメッセージングチャネルを選択します。
{% endtab %}
{% endtabs %}

## ステップ 2:編集経験を選択してください {#step-2-choose-your-template-and-compose-your-email}

Braze では、メールキャンペーンを作成する際、[ドラッグアンドドロップエディターと標準の HTML エディターの]({{site.baseurl}}/dnd/) 2 種類の編集機能を提供しています。適切なタイルをクリックして、希望する編集方法を選択してください。 

![メール編集環境に合わせてドラッグアンドドロップエディタと HTML エディタのどちらかを選択] [3]{: style="max-width:75%" }

次に、既存の [メールテンプレート] [10]、[テンプレートのアップロード] [18] をファイルから選択するか (HTML エディターのみ)、空白のテンプレートを使用できます。 

{% alert tip %}
メールキャンペーンごとに 1 つの編集エクスペリエンスを選択することをおすすめします。たとえば、エディターを切り替えるのではなく、1 つのメールキャンペーンで HTML クラシックエディターまたはブロックエディターのいずれかを選択します。
{% endalert %}

## ステップ 3:メールを作成

テンプレートを選択すると、メールの概要が表示され、フルスクリーンエディターにすばやくジャンプしてメールの下書きを作成したり、送信情報を変更したり、配信可能性や法令遵守に関する警告を確認したりできます。 

{% alert tip %}
ほとんどの受信トレイはJavaScriptをサポートしていないため、正確なプレビューでメールにモーションを追加するには、JavaScriptを必要とする要素の代わりにGIFを使用してください。
{% endalert %}

![メール作成用のメールバリアントパネル] [14]{: style="max-width:75%" }

{% alert important %}
Braze は属性として参照される HTML イベントハンドラーを自動的に削除します。これにより HTML が変更されるので、完了後にメールを再確認することをおすすめします。[HTML ハンドラーの詳細をご覧ください](https://www.w3schools.com/tags/ref_eventattributes.asp)。
{% endalert %}

{% alert tip %}
素晴らしいコピーを作成するのに助けが必要ですか？[AIコピーライティングアシスタントを使ってみてください]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/)。商品名または説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用できます。

![Launch AI Copywriter button, located in the Body tab of the email composer.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

### ステップ 3a:メールヘッダーとエクストラの追加

メールヘッダーを追加するには、[**送信情報の編集**] をクリックし、[**新しいヘッダーの追加**] を選択します。

メールヘッダーには、送信されるメールに関する情報が含まれます。[これらのキーと値のペアには]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)、通常、送信者、受信者、認証プロトコル、および電子メールルーティング情報に関する情報が含まれています。Braze は、メールが受信ボックスプロバイダーに適切に配信されるために、RFC で要求される必要なヘッダー情報を自動的に追加します。

「**プリヘッダーの後に空白を追加」チェックボックスを選択して、メールプリヘッダー内のメール本文のテキストまたは** HTML を非表示にすることもできます。 

Braze では、高度なユースケースで必要に応じてメールヘッダーを柔軟に追加できます。Braze プラットフォームが送信中に上書きする予約フィールドがいくつかあります。 

次のキーは使用しないでください。

<style>
#reserved-fields td {
    word-break: break-word;
    width: 33%;
}
</style>

<table id="reserved-fields">
<thead>
  <tr>
    <th>予約フィールド</th>
    <th></th>
    <th></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>BCC:</td>
    <td>ディムシグネチャー</td>
    <td>返信先:</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>差出人:</td>
    <td>件名</td>
  </tr>
  <tr>
    <td>コンテンツ転送エンコーディング</td>
    <td>マイムバージョン</td>
    <td>に</td>
  </tr>
  <tr>
    <td>コンテンツタイプ</td>
    <td>を受信しました</td>
    <td>X-SG-イード</td>
  </tr>
  <tr>
    <td>DKIM シグネチャ</td>
    <td>受け取った</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

#### メールエクストラの追加

メールエクストラを使用すると、追加のデータを他のメールサービスプロバイダーに送り返すことができます。これは高度なユースケースにのみ適用されるため、メールエクストラは会社ですでに設定されている場合にのみ使用してください。

メールエクストラを追加するには、「**送信情報**」に移動し、「**エクストラを追加**」をクリックします。

{% alert warning %}
追加するキーと値のペアの合計は 1 kB を超えないようにしてください。そうしないと、メッセージは中止されます。
{% endalert %}

メールの追加値はCurrentsまたはSnowflakeに公開されません。追加のメタデータまたは動的値をCurrentsまたはSnowflakeに送信する場合は、代わりに使用してください。[`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)

### ステップ 3b:メッセージをプレビューしてテストする

完璧なメールを作成したら、送信する前にテストする必要があります。

概要画面の下部から、「**プレビューとテスト**」をクリックします。ここでは、メールが顧客の受信トレイにどのように表示されるかをプレビューできます。「**ユーザーとしてプレビュー**」を選択すると、電子メールをランダムなユーザーとしてプレビューしたり、特定のユーザーを選択したり、カスタムユーザーを作成したりできます。これにより、コネクテッドコンテンツとパーソナライゼーションコールが正常に機能していることをテストできます。

デスクトップ、モバイル、プレーンテキストの表示を切り替えて、さまざまなコンテキストでメッセージがどのように表示されるかを把握することもできます。

{% alert tip %}
ダークモードのユーザーにとってメールがどのように見えるか知りたいですか？****プレビューとテストセクションにあるダークモードプレビュートグルを選択します**** (ドラッグアンドドロップエディターのみ)。
{% endalert %}

最終チェックの準備が整ったら、「**テスト送信**」を選択し、自分またはコンテンツテスターのグループにテストメッセージを送信して、メールがさまざまなデバイスやメールクライアントで正しく表示されることを確認します。

![メール作成時のテスト送信オプションとサンプルメールプレビュー] [15]

メールに問題がある場合、または変更を加えたい場合は、「**メールを編集**」をクリックしてエディターに戻ります。

{% alert tip %}
プレビューテキストをサポートする電子メールクライアントでは、使用可能なすべてのプレビューテキストスペースを埋めるのに十分な文字数が常に取り込まれます。ただし、これにより、プレビューテキストが不完全だったり、最適化されなかったりする場合があります。
<br><br>これを回避するには、目的のプレビューテキストの後に空白を作成して、メールクライアントが他の邪魔なテキストや文字をエンベロープの内容に取り込まないようにします。そのためには、表示したいプレビューテキストの後に、幅がゼロの非結合記号 (`&zwnj;`) と改行なしのスペース (`&nbsp;`) を連続して追加します。<br><br>プリヘッダーセクションのプレビューテキストの最後に追加すると、次の HTML エディター用のコードを実行すると、探している空白が追加されます。<br><br>

\`\`\`html
<div style="display: none; max-height: 0px; overflow: hidden;"> ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ ‌ </div>
```
ドラッグアンドドロップエディタでは、`を付けずに幅がゼロの非ジョイナー (``) のみを追加します<div>`**送信設定**セクションのプリヘッダーで直接フォーマットします。

{% endalert %}

### ステップ 3c:メールエラーをチェック

エディターは、メッセージで問題が見つかった場合は、送信前に指摘します。エディターで発生しているエラーのリストは次のとおりです。

-**表示名から**と**ヘッダー**は一緒に指定されていません
-**差出人**および**返信先**のアドレスが無効です
-**ヘッダー**キーが重複しています
-リキッドシンタックス問題
-400kbを超えるメール本文（本文は [102kb未満] [16] にすることを強く推奨します）
-**本文**または**件名**が空白のメール
-購読解除リンクのないメール
-送信元のメールがホワイトリストに登録されていない（配信可能性を確保するため、送信は大幅に制限されます）

## ステップ 4:残りのキャンペーンやキャンバスを作成

{% tabs %}
{% tab Campaign %}
次に、残りのキャンペーンを作成しましょう！当社のツールを最大限に活用してメールキャンペーンを構築する方法の詳細については、以下のセクションをご覧ください。

#### 配送スケジュールまたはトリガーを選択

メールは、スケジュールされた時間、アクション、または API トリガーに基づいて配信できます。詳細については、[キャンペーンのスケジュール設定] ({{site.baseurl}}) を参照してください。/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

{% alert note %}
APIトリガーキャンペーンの場合、トリガーアクションが**キャンペーンと対話**に設定されている場合、インタラクションとして**受信**オプションを選択すると、メッセージがバウンスしたり配信されなかったりした場合でも、Brazeが選択したキャンペーンを送信済みとマークするとすぐに新しいキャンペーンがトリガーされます。
{% endalert %}

キャンペーンの期間を設定することもできます。[クワイエットアワー] ({{site.baseurl}}) を指定することもできます/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours), and set [frequency capping]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) rules.

#### ターゲットにするユーザーを選択

次に、[ユーザーをターゲットにする] ({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/) by choosing segments or filters to narrow down your audience. You'll automatically be given a snapshot of what that segment population looks like right now, including how many users within that segment are reachable via email. Keep in mind that exact segment membership is always calculated just before the message is sent.

特定の [購読状況] ({{site.baseurl}}) を持つユーザーにのみキャンペーンを送信することもできます/user_guide/message_building_by_channel/email/managing_user_subscriptions/), such as those who are subscribed and opted in to email.

オプションで、セグメント内の特定の数のユーザーに配信を制限したり、キャンペーンが繰り返されるたびにユーザーが同じメッセージを 2 回受信できるようにしたりすることもできます。

##### メールとプッシュ通知によるマルチチャネルキャンペーン

メールチャネルとプッシュチャネルの両方をターゲットとするマルチチャネルキャンペーンでは、明示的にオプトインしたユーザー（登録ユーザーまたは登録解除ユーザーを除く）のみがメッセージを受信するようにキャンペーンを制限したい場合があります。たとえば、オプトインステータスの異なる 3 人のユーザーがいるとします。

-**ユーザーA**は電子メールを購読しており、プッシュが有効になっています。このユーザーはメールを受信しませんが、プッシュは受信します。
-**ユーザーB**はメール送信にオプトインしていますが、プッシュが有効になっていません。このユーザーはメールを受信しますが、プッシュは受信しません。
-**ユーザーC**はメール配信にオプトインしており、プッシュが有効になっています。このユーザーはメールとプッシュの両方を受け取ります。

そのためには、**オーディエンスの概要**で、このキャンペーンを「オプトインしたユーザーのみ」に送信することを選択します。このオプションは、オプトインしたユーザーのみがメールを受信することを確認し、Brazeはデフォルトでプッシュが有効になっているユーザーにのみプッシュを送信します。

{% alert important %}
この構成では、**ターゲットユーザー**ステップに、オーディエンスを単一のチャンネルに制限するフィルター（たとえば、「プッシュ有効 = True」や「E メール購読 = オプトイン」など）を含めないでください。
{% endalert %}

#### コンバージョンイベントを選択する

Brazeでは、ユーザーが特定のアクション（[コンバージョンイベント]）（{{site.baseurl}}）を実行する頻度を追跡できます/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/), after receiving a campaign. You can specify any of the following actions as a conversion event:

-アプリを開く
-購入を行う（一般的な購入品でも、特定の商品でも構いません）
-特定のカスタムイベントを実行します
-メールを開く

ユーザーが指定したアクションを実行した場合、コンバージョンがカウントされる期間は最大 30 日間です。Braze ではキャンペーンの開封とクリックが自動的にトラッキングされますが、[インテリジェントセレクション] ({{site.baseurl}}) を利用するために、ユーザーがメールアドレスを開いたりクリックしたりしたときにコンバージョンイベントが発生するように設定することもできます。/user_guide/sage_ai/intelligence/intelligent_selection/).
{% endtab %}

{% tab Canvas %}
まだ行っていない場合は、Canvas コンポーネントの残りのセクションを完了してください。キャンバスの残りの部分を構築する方法、多変量分析テストやインテリジェントセレクションを実装する方法などの詳細については、[キャンバスの作成] ({{site.baseurl}}) を参照してください。/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) step of our Canvas documentation.
{% endtab %}
{% endtabs %}

## ステップ 5:確認とデプロイ

最後のページには、デザインしたばかりのキャンペーンの概要が表示されます。関連する詳細をすべて確認し、**キャンペーンを開始**をクリックして送信を有効にします。

あとは、すべてのデータが取り込まれるのを待ってください！次に、[メールレポート] ({{site.baseurl}}) をチェックしてください/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) to learn how you can access the results of your email campaigns.

[3]: {% image_buster /assets/img_archive/choose_email_creation.png %}
[5]: {% image_buster /assets/img_archive/targetsegment_email_new.png %}
[6]: {% image_buster /assets/img_archive/confirm_email.png %}
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[13]: {{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_selection/
[14]: {% image_buster /assets/img/email.png %}
[15]: {% image_buster /assets/img_archive/newEmailTest.png %}
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size
[18]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/
[19]: {% image_buster /assets/img_archive/new_campaign_email.png %}
[20]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
[21]: {{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_timing/
[22]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/
