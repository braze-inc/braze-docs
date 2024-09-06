---
nav_title: 概要
article_title: カスタムHTMLでメールを作成する
page_order: 1
description: "この参考記事では、Brazeプラットフォームを使ってEメールを作成する方法を説明する。メッセージを作成し、コンテンツをプレビューし、キャンペーンやキャンバスのスケジュールを立てる方法についてのベストプラクティスが含まれている。"
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# カスタムHTMLでメールを作成する

> メールメッセージは、ユーザーにコンテンツを配信するのに適している。また、アプリをアンインストールしたユーザーを再度エンゲージするための優れたツールでもある。カスタマイズされたEメールメッセージを送信することで、ユーザーのエクスペリエンスを向上させ、アプリの価値を最大限に引き出すことができる。 

Eメールキャンペーンの事例をご覧になりたい方は、[ケーススタディを](https://www.braze.com/customers)ご覧ください。 

{% alert tip %}
初めてメールキャンペーンを作成する場合は、以下のBraze Learningのコースをチェックすることを強くお勧めする：<br>

- [メール](https://learning.braze.com/messaging-channels-email)
- [プロジェクト:基本的なEメールマーケティングプログラムを構築する](https://learning.braze.com/project-build-a-basic-email-marketing-program)

{% endalert %}

## ステップ 1:メッセージを作成する場所を選択する

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. **Messaging**>**Campaignsに**進み、**\+ Create Campaignを**クリックする。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、\[**エンゲージメント**] の下に \[**キャンペーン**] が表示されます。
{% endalert %}

{:start=“2"}
2\.**Eメール」を**選択するか、複数のチャネルを対象とするキャンペーンの場合は「**マルチチャネルキャンペーン**」を選択する。
3\.キャンペーンに、明確で意味のある名前を付けます。
4\.必要に応じて、\[[チーム]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/)] と \[[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)] を追加します。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、\[[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、\[**バリアントを追加**] ドロップダウンから \[**バリアントをコピー**] を選択できます。
{% endalert %}
{% endtab %}
{% tab キャンバス %}

**ステップ:**

1. キャンバス作成ツールを使用して \[[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. \[[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。
4. このステップでは、必要に応じて聴衆をフィルタリングする。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。視聴者オプションは、遅延の後、メッセージが送信された時点でチェックされる。
5. \[[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせたい他のメッセージング・チャンネルを選択する。
{% endtab %}
{% endtabs %}

## ステップ 2:編集経験を選択してください {#step-2-choose-your-template-and-compose-your-email}

Brazeでは、メールキャンペーンを作成する際に、[ドラッグ＆ドロップエディターと]({{site.baseurl}}/dnd/)標準のHTMLエディターの2種類の編集機能を提供している。適切なタイルをクリックし、好みの編集エクスペリエンスを選択する。 

![ドラッグ＆ドロップエディターとHTMLエディターのどちらを使うか、メール編集の経験を選ぶ。][3]{: style="max-width:75%" }

次に、既存の\[Eメールテンプレート][10]]、\[ファイルからテンプレートをアップロード][18] （HTMLエディタのみ）]、または空白のテンプレートを使用することができる。 

{% alert tip %}
1つのメールキャンペーンにつき1つの編集経験を選択することをお勧めする。例えば、1つのメールキャンペーンで、エディターを切り替えるのではなく、HTMLクラシックエディターかブロックエディターのどちらかを選択する。
{% endalert %}

## ステップ 3:メールを作成します。

テンプレートを選択すると、メールの概要が表示され、直接フルスクリーンエディターにジャンプして、メールの下書き、送信情報の変更、配信可能性や法令遵守に関する警告を見ることができる。 

{% alert tip %}
ほとんどの受信トレイはJavaScriptをサポートしていないため、正確なプレビューでメールに動きを加えるには、JavaScriptを必要とする要素の代わりにGIFを使用する。
{% endalert %}

![メールを作成するためのEメールバリアントパネル。][14]{: style="max-width:75%" }

{% alert important %}
Brazeは、属性として参照されているHTMLイベントハンドラを自動的に削除する。これによりHTMLが変更されるので、完了後にメールを再チェックすることをお勧めする。[HTMLハンドラについて](https://www.w3schools.com/tags/ref_eventattributes.asp)もっと知る。
{% endalert %}

{% alert tip %}
素晴らしいコピーの作成にお困りですか？[AIコピーライティング・アシスタントを使って]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/)みよう。商品名や説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用する。

![メールコンポーザーの「本文」タブにある「AIコピーライター」ボタンを起動する。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

### ステップ3a：送信情報を追加する

メールメッセージのデザインと作成が終わったら、**送信設定**セクションで送信情報を追加しよう。

1. **送信情報**]で、\[**送信元表示名＋アドレス**]として電子メールを選択する。**表示名＋住所からカスタマイズを**選択してカスタマイズすることもできる。
2. **返信先アドレスとして**電子メールを選択する。**返信先アドレスのカスタマイズを**選択してカスタマイズすることもできる。
3. 次に、**BCCアドレスとして**電子メールを選択し、このアドレスにあなたの電子メールが見えるようにする。
4. メールに件名をつける。オプションで、プレヘッダーとプレヘッダーの後の空白を追加することもできる。

右側のパネルにプレビューが表示され、追加した送信情報が表示される。この情報は、**「設定」**>「**メール設定**」>「**送信設定**」で更新することもできる。

#### 上級

**送信設定**＞**詳細**設定では、インラインCSSをオンにしたり、メールヘッダやメールエキストラにパーソナライズを追加したりできる。

##### 電子メールのヘッダー

メールヘッダーを追加するには、**「新しいヘッダーを追加**」を選択する。電子メールのヘッダーには、送信される電子メールに関する情報が含まれている。これらの[キーと値のペアは]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)通常、送信者、受信者、認証プロトコル、電子メールのルーティング情報についての情報を持っている。Brazeは、メールが受信プロバイダーに正しく配信されるために、RFCで要求される必要なヘッダー情報を自動的に追加する。

Brazeでは、高度なユースケースのために、必要に応じてメールヘッダを追加できる柔軟性がある。Brazeプラットフォームが送信時に上書きする予約フィールドがいくつかある。 

以下のキーの使用は避けること：

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
    <td>BCC</td>
    <td>dkim-署名</td>
    <td>返信先</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>より</td>
    <td>件名</td>
  </tr>
  <tr>
    <td>コンテンツ転送エンコーディング</td>
    <td>MIME-Version</td>
    <td>へ</td>
  </tr>
  <tr>
    <td>コンテンツタイプ</td>
    <td>受信済み</td>
    <td>X-SG-イード</td>
  </tr>
  <tr>
    <td>DKIM署名</td>
    <td>受け取った</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### Eメールの追加

Eメールエクストラでは、他のEメールサービスプロバイダに追加データを送り返すことができる。これは高度なユースケースにのみ適用されるものなので、あなたの会社ですでに設定されている場合にのみ、Eメール・エクストラを使うべきである。

Eメール・エクストラを追加するには、「**送信情報**」で**「新しいエクストラを追加**」をクリックする。

{% alert warning %}
追加されるキーと値のペアの合計は1kBを超えてはならない。そうでなければ、メッセージは中断される。
{% endalert %}

Eメールの余分な値は、CurrentsやSnowflakeには公開されない。追加のメタデータや動的な値をCurrentsやSnowflakeに送りたい場合は、代わりに [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)を使う。

### ステップ3b：メッセージをプレビューしてテストする

完璧なEメールを作成し終えたら、送信する前にテストする必要がある。

概要画面の下から、「**プレビューとテスト**」をクリックする。ここで、あなたのメールが顧客の受信箱にどのように表示されるかをプレビューすることができる。**ユーザーとしてプレビューを**選択すると、ランダムなユーザーとしてメールをプレビューしたり、特定のユーザーを選択したり、カスタムユーザーを作成したりすることができる。これにより、コネクテッド・コンテンツとパーソナライゼーション・コールが正常に機能しているかをテストすることができる。

また、デスクトップ、モバイル、プレーンテキストのビューを切り替えて、異なるコンテクストでメッセージがどのように表示されるかを知ることもできる。

{% alert tip %}
ダークモードユーザーのメールがどのように見えるか興味がある？**プレビューとテスト」**セクションにある**「ダークモードプレビュー」**トグルを選択する（ドラッグ＆ドロップエディターのみ）。
{% endalert %}

最終チェックの準備ができたら、**テスト送信を**選択し、自分自身またはコンテンツテスターのグループにテストメッセージを送信して、さまざまなデバイスやメールクライアントでメールが正しく表示されることを確認しよう。

![テスト送信オプションと、メール作成時のプレビュー例。][15]

Eメールに問題があったり、変更を加えたい場合は、**Eメールの編集を**クリックしてエディターに戻る。

{% alert tip %}
プレビューテキストをサポートする電子メールクライアントは、常に利用可能なすべてのプレビューテキストのスペースを埋めるのに十分な文字を引き込む。しかし、これではプレビュー・テキストが不完全であったり、最適化されていなかったりする。
<br><br>これを避けるには、メールクライアントが他の邪魔なテキストや文字を封筒の内容に引きずり込まないように、希望のプレビューテキストの後に空白を作ればいい。そのためには、表示させたいプレビュー・テキストの後に、ゼロ幅のノンジョイナー（`&zwnj;` ）とノン・ブリーキング・スペース（`&nbsp;` ）のチェーンを追加する。<br><br>プレヘッダー・セクションのプレビュー・テキストの末尾に追加すると、HTMLエディター用の以下のコードが、あなたが探している空白を追加してくれる：<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
ドラッグ・アンド・ドロップ・エディターの場合は、**送信設定**セクションのプレヘッダーに、`<div>` の書式を使わずにゼロ幅のノンジョイナー（`&zwnj;` ）だけを直接追加する。

{% endalert %}

### ステップ3c：電子メールのエラーをチェックする

送信する前に、エディターがあなたのメッセージの問題点を指摘する。以下は、我々のエディターで説明されているエラーのリストである：

- **表示名と** **ヘッダーが**一緒に指定されていない
- 無効な**From**アドレスと**Reply-To**アドレス
- **ヘッダーキーの**重複
- 液体構文の問題
- 400kbを超えるメール本文（本文は\[102kb以下][16]]にすることを強く推奨する
- **本文**または**件名が**空白の電子メール
- 配信停止リンクのないメール
- 送信元のメールが許可リストに登録されていない（配信可能性を確保するため、送信は高度に制限される）

## ステップ 4:キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}
次に、キャンペーンの残りの部分を構築する！Eメールキャンペーンを構築するための最適なツールの使用方法については、次のセクションを参照してください。

#### 配信スケジュールまたはトリガーを選択する

メールは、スケジュールされた時間、アクション、またはAPIトリガーに基づいて配信することができる。詳しくは、[キャンペーンのスケジューリングを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)参照のこと。

{% alert note %}
APIトリガーキャンペーンの場合、トリガーアクションが**Interact With Campaignに**設定されている場合、インタラクションとして**Receive**オプションを選択すると、Brazeが選択したキャンペーンを送信済みとマークした時点で、たとえそのメッセージがバウンスしたり、配信に失敗したりしても、新しいキャンペーンがトリガーされる。
{% endalert %}

また、キャンペーンの期間を設定し、[クワイエットアワーを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)指定し、[頻度の上限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを設定することもできる。

#### ターゲットとするユーザーを選択する

次に、セグメントやフィルターを選択することで、[ユーザーを絞り込む]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)必要がある。そのセグメント内の何人のユーザーがEメールでリーチ可能かなど、そのセグメントの母集団が現在どのようになっているかのスナップショットが自動的に表示される。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

また、特定の[購読ステータスの]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)ユーザーにのみキャンペーンを送信することもできる。

オプションで、セグメント内の指定されたユーザー数に配信を制限したり、キャンペーンが再来したときに同じメッセージを2回受け取ることをユーザーに許可することもできる。

##### Eメールとプッシュによるマルチチャネルキャンペーン

Eメールとプッシュチャネルの両方をターゲットにしたマルチチャネルキャンペーンの場合、明示的にオプトインしているユーザーのみがメッセージを受信するようにキャンペーンを制限したい場合がある（購読または購読解除したユーザーを除く）。例えば、オプトインのステータスが異なる3人のユーザーがいるとする：

- **ユーザー A** はメールを購読しており、プッシュ通知が有効です。このユーザーはメールを受信しませんが、プッシュ通知は受信します。
- **ユーザー B** はメールにオプトインしていますが、プッシュ通知を有効にしていません。このユーザーはメールを受信しますが、プッシュ通知は受信しません。
- **ユーザー C** はメールにオプトインしており、プッシュ通知が有効です。このユーザーはメールとプッシュ通知の両方を受け取ります。

そのためには、**「オーディエンス・サマリー**」で、このキャンペーンを「オプトインしたユーザーのみ」に送信することを選択する。このオプションは、オプトインしたユーザーだけにメールが届くようにチェックし、Brazeはデフォルトでプッシュが有効になっているユーザーにのみプッシュを送信する。

{% alert important %}
この構成では、**Target Users**ステップに、オーディエンスを単一のチャネルに限定するフィルタ（例えば、`Push Enabled = True` や`Email Subscription = Opted-In` ）を含めない。
{% endalert %}

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を実行する頻度を追跡できます。変換イベントとして、以下のいずれかのアクションを指定することができる：

- アプリを開く
- 購入する（これは一般的な購入でも、特定の商品でも構わない）
- 特定のカスタムイベントを実行する
- メールを開く

ユーザーが指定されたアクションを取った場合、コンバージョンがカウントされる最大30日間のウィンドウを許可することができる。Brazeはキャンペーンの開封とクリックを自動的に追跡するが、[インテリジェントセレクションを]({{site.baseurl}}/user_guide/sage_ai/intelligence/intelligent_selection/)活用するために、ユーザーがメールアドレスを開封またはクリックしたときにコンバージョンイベントを設定したい場合がある。
{% endtab %}

{% tab キャンバス %}
まだやっていない場合は、キャンバスのコンポーネントの残りのセクションを完成させる。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの「[キャンバスを構築する」]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照のこと。
{% endtab %}
{% endtabs %}

## ステップ 5: レビューと展開

最終ページには、あなたがデザインしたキャンペーンの概要が表示される。関連するすべての詳細を確認し、**Launch Campaignを**クリックして送信できるようにする。

あとはデータが出揃うのを待つだけだ！次に、[メール レポート ing]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/) をチェックして、メール キャンペーンs の結果にアクセスする方法を確認します。

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
