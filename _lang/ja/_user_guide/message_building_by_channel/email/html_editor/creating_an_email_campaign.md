---
nav_title: メールを作成する
article_title: ユーザ定義HTMLを使用したメールの作成
page_order: 1
description: "この参考記事では、Brazeプラットフォームを使ってEメールを作成する方法を説明する。メッセージを作成し、コンテンツをプレビューし、キャンペーンやキャンバスのスケジュールを立てる方法についてのベストプラクティスが含まれている。"
tool:
  - Campaigns
channel:
  - email
search_rank: 1  
---

# カスタムHTMLでメールを作成する

> メールメッセージは、ユーザーにコンテンツを配信するのに適している。また、アプリをアンインストールしたユーザーを再エンゲージさせるための優れたツールでもあります。カスタマイズと調整を行ったメールメッセージを送信すると、ユーザー体験が向上し、ユーザーがアプリから最大限の価値を引き出すうえで役立ちます。 

Eメールキャンペーンの事例をご覧になりたい方は、[ケーススタディを](https://www.braze.com/customers)ご覧ください。 

{% alert tip %}
初めてメールキャンペーンを作成する場合は、Brazeラーニングコースをチェックすることを強くお勧めする：<br><br>
- [メールのオプトインと許諾](https://learning.braze.com/messaging-channels-email)
- [プロジェクト:基本的なEメールマーケティングプログラムを構築する](https://learning.braze.com/project-build-a-basic-email-marketing-program)
{% endalert %}

## ステップ 1: メッセージを作成する場所を選択する

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

1. [**メッセージング**] > [**キャンペーン**] の順に進み、[**キャンペーンを作成**] を選択します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**エンゲージメント**] の下に [**キャンペーン**] が表示されます。
{% endalert %}

{:start=“2"}
2\.[**メール**] を選択するか、複数のチャネルを対象とするキャンペーンの場合は、［**マルチチャネル**] を選択します。
3\.キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じて[チームや]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) [タグを]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)追加する。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、[[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、[**バリアントを追加**] ドロップダウンから [**バリアントをコピー**] を選択できます。
{% endalert %}
{% endtab %}
{% tab キャンバス %}

1. キャンバス作成ツールを使用して [[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. [[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルター処理します。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。遅延後のメッセージの送信時に、オーディエンスのオプションがチェックされます。
5. [[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせる他のメッセージングチャネルを選択します。
{% endtab %}
{% endtabs %}

## ステップ 2: 編集経験を選択してください {#step-2-choose-your-template-and-compose-your-email}

Brazeでは、メールキャンペーンを作成する際に、[ドラッグ＆ドロップエディターと]({{site.baseurl}}/dnd/)標準のHTMLエディターの2種類の編集機能を提供している。好みの編集体験に適したタイルを選ぶ。 

![ドラッグ＆ドロップエディターとHTMLエディターのどちらを使うか、メール編集の経験を選ぶ。][3]{: style="max-width:75%" }

次に、既存の[メールテンプレート][10]の選択、ファイルから[テンプレートをアップロード][18] (HTML エディターのみ)、または空白のテンプレートの使用ができます。 

{% alert tip %}
1つのメールキャンペーンにつき1つの編集経験を選択することをお勧めする。例えば、1つのメールキャンペーンで、エディターを切り替えるのではなく、**HTMLクラシック** **エディターかブロックエディターの**どちらかを選択する。
{% endalert %}

## ステップ 3:メールを作成します。

テンプレートを選択すると、メールの概要が表示されます、そこから全画面エディターに直接移動して、メールの下書き、送信情報の変更、配信可能性や法令遵守に関する警告の表示ができます。 

{% alert tip %}
ほとんどの受信トレイはJavaScriptをサポートしていないため、正確なプレビューでメールに動きを加えるには、JavaScriptを必要とする要素の代わりにGIFを使用する。
{% endalert %}

![メールを作成するための [メールのバリアント] パネル。][14]{: style="max-width:75%" }

{% alert important %}
Brazeは、属性として参照されているHTMLイベントハンドラを自動的に削除する。これによりHTMLが変更されるので、完了後にメールを再チェックすることをお勧めする。[HTML ハンドラー](https://www.w3schools.com/tags/ref_eventattributes.asp)の詳細を参照してください。
{% endalert %}

{% alert tip %}
魅力的な文章を作成するためのサポートが必要な場合は、[AI コピーライティングアシスタント]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/)を使用してみてください。商品名や説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用する。

![メール作成画面の [本文] タブにある [AI コピーライターを起動] ボタン。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_email.png %}){: style="max-width:80%"}
{% endalert %}

### ステップ 3a: 送信情報の追加

メールメッセージのデザインと作成が終わったら、**送信設定**セクションで送信情報を追加しよう。

1. [**送信情報**] で、[**差出人の表示名 + アドレス**] としてメールアドレスを選択します。[**差出人の表示名 + アドレスをカスタマイズ**] を選択してカスタマイズすることもできます。
2. [**返信先アドレス**] としてメールアドレスを選択します。[**返信先アドレスをカスタマイズ**] を選択してカスタマイズすることもできます。
3. 次に、[**BCCアドレス**] としてメールアドレス選択し、このアドレスからあなたのメールアドレスが表示できるようにします。
4. メールに件名を追加します。必要に応じて、プリヘッダーおよびその後の空白を追加することもできます。

右側のパネルに、追加した送信情報が入力されたプレビューが表示されます。この情報は、[**設定**] > [**メール設定**] > [**送信設定**] で更新することもできます。

#### 上級

[**送信設定**] > [**詳細設定**] では、インライン CSS をオンにしたり、メールヘッダーやメールの追加情報をパーソナライズできます。これにより、他のメールサービスプロバイダーに追加データを送信できます。

##### 電子メールのヘッダー

メールヘッダーを追加するには、**「新しいヘッダーを追加**」を選択する。電子メールのヘッダーには、送信される電子メールに関する情報が含まれている。これらの[キーと値のペアは]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/key_value_pairs/)通常、送信者、受信者、認証プロトコル、電子メールのルーティング情報についての情報を持っている。Brazeは、メールが受信プロバイダーに正しく配信されるために、RFCで要求される必要なヘッダー情報を自動的に追加する。

Braze には、高度なユースケースで必要に応じてメールヘッダーを追加できる柔軟性があります。Brazeプラットフォームが送信時に上書きする予約フィールドがいくつかある。 

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
    <td>DKIM 署名</td>
    <td>返信先</td>
  </tr>
  <tr>
    <td>CC</td>
    <td>より</td>
    <td>件名</td>
  </tr>
  <tr>
    <td>コンテンツ転送エンコーディング</td>
    <td>MIME バージョン</td>
    <td>へ</td>
  </tr>
  <tr>
    <td>コンテンツタイプ</td>
    <td>受信済み</td>
    <td>X-SG-EID</td>
  </tr>
  <tr>
    <td>DKIM 署名</td>
    <td>受け取った</td>
    <td>x-sg-id</td>
  </tr>
</tbody>
</table>

##### メールエクストラの追加

メールエクストラでは、他のメールサービスプロバイダーに追加データを送り返すことができます。これは高度なユースケースにのみ適用されるものであるため、社内でこれがすでに設定されている場合にのみメールエクストラを使用してください。

メール・エクストラを追加するには、「**送信情報**」から**「新しいエクストラを追加**」を選択する。

{% alert warning %}
追加されるキーと値のペアの合計は1kBを超えてはならない。それ以外の場合、メッセージは中止されます。
{% endalert %}

Eメールの余分な値は、CurrentsやSnowflakeには公開されない。追加のメタデータやダイナミックな値を Currents や Snowflake に送信する場合は、代わりに [`message_extras`]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/advanced_filters/message_extras/)を使用してください。

### ステップ 3b： メッセージをプレビューしてテストする

完璧なEメールを作成し終えたら、送信する前にテストする必要がある。概要画面の下部から ［**プレビュー後にテスト**] を選択します。 

ここで、顧客の受信トレイでメールがどのように表示されるかをプレビューできます。**プレビューをユーザー**として選択すると、ランダムユーザーとしてメールをプレビューしたり、特定のユーザーを選択したり、カスタムユーザーを作成したりできます。これにより、コネクテッドコンテンツとパーソナライゼーションの呼び出しがコールが正常に機能していることをテストできます。

また、デスクトップ、モバイル、プレーンテキストのビューを切り替えて、異なるコンテクストでメッセージがどのように表示されるかを知ることもできる。

{% alert tip %}
ユーザーがダークモードのときにメールがどのように表示されるかを確認するには、**プレビューとテスト」**セクションにある**「ダークモードプレビュー」**トグルを選択する（ドラッグ＆ドロップエディターのみ）。
{% endalert %}

最終チェックの準備ができたら、**テスト送信を**選択し、自分自身またはコンテンツテスターのグループにテストメッセージを送信して、さまざまなデバイスやメールクライアントでメールが正しく表示されることを確認しよう。

![メール作成時の [テスト送信] オプションとプレビューの例。][15]

メールに問題がある場合や変更を加えたい場合には、[**メールを編集**] を選択してエディターに戻ります。

{% alert tip %}
プレビューテキストをサポートする電子メールクライアントは、常に利用可能なすべてのプレビューテキストのスペースを埋めるのに十分な文字を引き込む。しかし、これではプレビュー・テキストが不完全であったり、最適化されていなかったりする。
<br><br>これを避けるために、メールクライアントが他の不要なテキストや文字を外側のコンテンツに入れないように、目的のプレビューテキストの後に空白を作成できます。そのためには、表示するプレビューテキストの後に、一連のゼロ幅非接合子 (`&zwnj;`) とノーブレークスペース (`&nbsp;`) を追加します。<br><br>プレヘッダー・セクションのプレビュー・テキストの末尾に追加すると、HTMLエディター用の以下のコードが、あなたが探している空白を追加してくれる：<br><br>

```html
<div style="display: none; max-height: 0px; overflow: hidden;">&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;</div>
```
ドラッグ・アンド・ドロップ・エディターの場合は、**送信設定**セクションのプレヘッダーに、`<div>` の書式を使わずにゼロ幅のノンジョイナー（`&zwnj;` ）だけを直接追加する。

{% endalert %}

### ステップ 3c： 電子メールのエラーをチェックする

送信する前に、エディターがあなたのメッセージの問題点を指摘する。以下に、当社のエディターでエラーが発生する主な原因のリストを示します。

- [**差出人の表示名**] と [**ヘッダー**] がともに指定されていない
- 無効な**From**アドレスと**Reply-To**アドレス
- **ヘッダー**キーが重複している
- Liquid の構文の問題
- 400kbを超えるメール本文（本文は[102kb以下][16]]にすることを強く推奨する
- **本文**または**件名が**空白の電子メール
- 配信停止リンクのないメール
- 送信元のメールが許可リストに登録されていない（配信可能性を確保するため、送信は高度に制限される）

## ステップ 4:キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}
次に、キャンペーンの残りの部分を作成します。Eメールキャンペーンを構築するための最適なツールの使用方法については、次のセクションを参照してください。

#### 配信スケジュールまたはトリガーを選択する

メールは、スケジュールされた時刻、アクション、または API トリガーに基づいて配信できます。詳細については、[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を参照してください。

{% alert note %}
APIトリガーキャンペーンの場合、トリガーアクションが**Interact With Campaignに**設定されている場合、インタラクションとして**Receive**オプションを選択すると、Brazeが選択したキャンペーンを送信済みとマークした時点で、たとえそのメッセージがバウンスしたり、配信に失敗したりしても、新しいキャンペーンがトリガーされる。
{% endalert %}

また、キャンペーンの期間を設定し、[クワイエットアワーを]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)指定し、[頻度の上限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを設定することもできる。

#### ターゲットとするユーザーを選択する

次に、セグメントまたはフィルターを選択して[ユーザーをターゲットに設定]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)し、オーディエンスを絞り込む必要があります。そのセグメントのうちメールでリーチ可能なユーザー数など、そのセグメントの母集団の現在のスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

また、特定の[サブスクリプションステータス]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/)を持つユーザー (メールに登録してオプトインしたユーザーなど) にのみキャンペーンを送信することもできます。

オプションで、セグメント内の指定されたユーザー数に配信を制限したり、キャンペーンが再来したときに同じメッセージを2回受け取ることをユーザーに許可することもできる。

##### Eメールとプッシュによるマルチチャネルキャンペーン

メールチャネルとプッシュ通知チャネルの両方をターゲットにしたマルチチャネルキャンペーンの場合、明示的にオプトインしているユーザーのみがメッセージを受け取るようにキャンペーンを制限することができます (配信登録済みユーザーまたは配信停止済みユーザーを除く)。例えば、次のようにオプトインステータスが異なる 3 人のユーザーがいるとします。

- **ユーザー A** はメールを購読しており、プッシュ通知が有効です。このユーザーはメールを受信しませんが、プッシュ通知は受信します。
- **ユーザー B** はメールにオプトインしていますが、プッシュ通知を有効にしていません。このユーザーはメールを受信しますが、プッシュ通知は受信しません。
- **ユーザー C** はメールにオプトインしており、プッシュ通知が有効です。このユーザーはメールとプッシュ通知の両方を受け取ります。

そのためには、[**オーディエンスの概要**] で、このキャンペーンの送信先に [オプトイン済みのユーザーのみ] を選択します。このオプションは、オプトインしたユーザーだけにメールが届くようにチェックし、Brazeはデフォルトでプッシュが有効になっているユーザーにのみプッシュを送信する。

{% alert important %}
この構成では、**Target Users**ステップに、オーディエンスを単一のチャネルに限定するフィルタ（例えば、`Push Enabled = True` や`Email Subscription = Opted-In` ）を含めない。
{% endalert %}

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を実行する頻度を追跡できます。コンバージョンイベントとして、次のアクションをいずれでも選択できます。

- アプリを開く
- 購入する（これは一般的な購入でも、特定の商品でも構わない）
- 特定のカスタムイベントを実行する
- メールを開く

ユーザーが指定されたアクションを取った場合、コンバージョンがカウントされる最大30日間のウィンドウを許可することができる。Brazeはキャンペーンの開封とクリックを自動的に追跡するが、[インテリジェントセレクションを]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)活用するために、ユーザーがメールアドレスを開封またはクリックしたときにコンバージョンイベントを設定したい場合がある。
{% endtab %}

{% tab キャンバス %}
キャンバスコンポーネントがまだ完成していない場合は、残りのセクションを完成させます。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの「[キャンバスを構築する」]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照のこと。
{% endtab %}
{% endtabs %}

## ステップ 5: レビューと展開

最後のセクションでは、あなたがデザインしたキャンペーンの概要が表示される。関連するすべての詳細を確認し、「**キャンペーンを開始**」を選択する。すべてのデータが揃うまで待ちます。 

メールキャンペーンの結果にアクセスする方法については、[メール]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/)レポートをご覧ください。

[3]: {% image_buster /assets/img_archive/choose_email_creation.png %}
[5]: {% image_buster /assets/img_archive/targetsegment_email_new.png %}
[6]: {% image_buster /assets/img_archive/confirm_email.png %}
[10]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/#creating-an-email-template
[13]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/
[14]: {% image_buster /assets/img/email.png %}
[15]: {% image_buster /assets/img_archive/newEmailTest.png %}
[16]: {{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/guidelines_and_tips/#email-size
[18]: {{site.baseurl}}/user_guide/message_building_by_channel/email/templates/html_email_template/
[19]: {% image_buster /assets/img_archive/new_campaign_email.png %}
[20]: {{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/
[21]: {{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/
[22]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/
