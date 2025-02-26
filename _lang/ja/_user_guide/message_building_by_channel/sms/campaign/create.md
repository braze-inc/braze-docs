---
nav_title: SMSメッセージを作成する
article_title: SMSメッセージを作成する
page_order: 5
description: "この参考記事では、SMSメッセージの構築と作成に関わるステップをカバーしている。"
page_type: reference
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# SMSメッセージを作成する

> SMS キャンペーンは、顧客に直接リーチしてプログラムを使って会話を行うのに適しています。Liquid などのダイナミックコンテンツを使用して、ユーザー一人ひとりに合わせた体験を作り出し、控えめなブランド体験を強化する環境を作ることができます。 

## ステップ 1: メッセージを作成する場所を選択する

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. [**メッセージング**] > [**キャンペーン**] の順に進み、[**キャンペーンを作成**] を選択します。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合は、[**エンゲージメント**] の下に [**キャンペーン**] が表示されます。
{% endalert %}

{: start="2"}
2\.**SMS**を選択するか、複数のチャネルをターゲットとするキャンペーンの場合は**Multichannel**を選択します。
3\.キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じて[チームや]({{site.baseurl}}/user_guide/administrative/manage_your_braze_users/teams/) [タグを]({{site.baseurl}}/user_guide/administrative/app_settings/manage_app_group/tags/)追加する。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。例えば、[[レポートビルダー]({{site.baseurl}}/user_guide/data_and_analytics/reporting/report_builder/)] を使用する場合、特定のタグでフィルターできます。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。
6. [[サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/)] を選択して、メッセージを送信するユーザーが適切であることを確認します。サブスクリプショングループを選択すると、Braze によって自動的にセグメンテーションフィルターが追加され、配信登録済みのユーザーのみがキャンペーンを受信できるようになります。そのサブスクリプショングループに属する長いコードと短いコードのみを使用して、対象ユーザーに SMS が送信されます。

{% alert tip %}
キャンペーン内のすべてのメッセージが類似しているか、同じ内容になる場合は、メッセージを作成してからバリアントを追加します。その後、[**バリアントを追加**] ドロップダウンから [**バリアントをコピー**] を選択できます。
{% endalert %}

{% endtab %}
{% tab キャンバス %}

**ステップ:**

1. キャンバス作成ツールを使用して [[キャンバスを作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)] します。
2. キャンバスを設定したら、キャンバスビルダーにステップを追加します。ステップに、明確で意味のある名前を付けます。
3. [[ステップスケジュール]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay)] を選択し、必要に応じて遅延を指定します。
4. 必要に応じて、このステップのオーディエンスをフィルターします。セグメントを指定し、フィルターを追加して、このステップの受信者をさらに絞り込むことができます。後から、メッセージの送信時に、オーディエンスオプションがチェックされます。
5. [[昇進動作]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/)] を選択します。
6. メッセージと組み合わせる他のメッセージングチャネルを選択します。

{% endtab %}
{% endtabs %}

## ステップ 2: SMSを作成する

必要に応じて言語やパーソナライズ（リキッド、コネクテッド・コンテンツ、絵文字）を使ってメッセージを書きます。超過料金を請求される可能性を減らすため、メッセージのコピー数制限を必ず守ってください。

{% alert important %}
先に進む前に、[SMSメッセージのセグメントとコピーの上限に関する]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/)ガイドラインを読みましょう。SMSメッセージ・セグメントとは、電話キャリアがテキスト・メッセージを測定するために使用する文字バッチのことです。メッセージはメッセージセグメントごとに課金されるため、メッセージの分割方法のニュアンスを理解しておきましょう。
{% endalert %}

![次のメッセージを含む Braze の SMS コンポーザー: 「first_name さん、いつも応援していただきありがとうございます。このSMSを見せれば、特別割引が適用されます。メッセージの受信を中止するには STOP と返信してください。」]({% image_buster /assets/img/sms_campaign_compose.png %})

{% alert tip %}
{% raw %}
Liquidを使用する場合は、受信者のユーザープロファイルが不完全な場合、名前やまとまった文章の代わりに空白のプレースホルダー`Hi, !` を受信しないように、選択したパーソナライズのデフォルト値を必ず含めてください。
{% endraw %}
{% endalert %}

魅力的な文章を作成するためのサポートが必要な場合は、[AI コピーライティングアシスタント]({{site.baseurl}}/user_guide/intelligence/ai_copywriting/)を使用してみてください。商品名や説明を入力すると、AIが人間のようなマーケティングコピーを生成し、メッセージングに使用します。

![SMS コンポーザーのメッセージフィールドにある [AI コピーライター] ボタンをクリックします。]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

### 連絡先カード

必要に応じて、連絡先カードをSMSメッセージに追加して、顧客がビジネスや連絡先情報を簡単に連絡先に追加できるようにすることができます。これらのカードには、会社名、電話番号、住所、Eメール、小さな写真など、一般的なプロパティを割り当てることができます。詳しくは、[お問い合わせカード]({{site.baseurl}}/user_guide/message_building_by_channel/sms/mms/contact_card/)をご覧ください。

## ステップ 3:メッセージをプレビューしてテストする

Brazeでは、送信前にメッセージをプレビューしてテストすることを常に推奨しています。**テスト**タブに切り替えて、[コンテンツテストグループ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups)または個々のユーザーにテストSMSを送信するか、Brazeで直接ユーザーとしてメッセージをプレビューしましょう。

![コンポーザーのテストタブからの SMS コピーのプレビュー。プロファイルセクションの [名] フィールドは「James」に設定されています。プレビュー・セクションでは、SMSに "Hi James, we appreciate your support!"]({% image_buster /assets/img/sms_campaign_test.png %}) と表示されるようになりました。

{% alert tip %}
SMSがいくつのセグメントに分けられるかテストしたい場合は、[SMSセグメント計算機を使って]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator)コピーの長さをテストしてみましょう。
{% endalert %}

## ステップ 4: キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}

次に、キャンペーンの残りの部分を作成します。SMSメッセージの作成に最適なツールの使い方については、以下のセクションを参照してください。

#### 配信スケジュールまたはトリガーを選択する

SMS メッセージは、スケジュールされた時刻、アクション、または API トリガーに基づいて配信することができます。詳細については、[キャンペーンのスケジューリング]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)を参照してください。

アクションベースの配信では、キャンペーンの継続時間と [[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)] を設定することもできます。

このステップでは、配信コントロールを指定できます。例えば、ユーザーを[再有効化]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)してキャンペーンを受信できるようにしたり、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを有効にしたりできます。

#### ターゲットとするユーザーを選択する

次に、セグメントまたはフィルターを選択して[ユーザーをターゲットに設定]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)し、オーディエンスを絞り込む必要があります。すでにサブスクリプショングループを選択しているため、ユーザーがブランドに対して希望しているコミュニケーションの頻度やカテゴリによって、ユーザーが絞り込まれます。このステップでは、セグメントからより多くのオーディエンスを選択し、必要であればフィルターを使ってさらにセグメントを絞り込みます。セグメントのおおよその人数について現在の状態を示すスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

{% alert tip %}
SMSリターゲティングに興味がある？詳しくはSMS[リターゲティングの記事を]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/)ご覧いただきたい。
{% endalert %}

#### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間は、最大 30 日間まで設定できます。

コンバージョンイベントにより、キャンペーンの成否を測定できます。以下に例を示します。

- ジオターゲティングを使用して、ユーザーが購入するという最終目標を持つSMSメッセージをトリガーする場合、コンバージョンイベントを`Purchase` 。
- ユーザーをアプリに誘導しようとしている場合は、コンバージョンイベントを`Starts Session` に設定する。

独自のユースケースに基づいて、カスタムコンバージョンイベントを設定することもできます。このキャンペーンの真の成功を測定する方法について独創的に考えてみましょう。

{% endtab %}

{% tab キャンバス %}

キャンバスコンポーネントが完成していない場合は、残りのセクションを完成させます。キャンバスの残りの部分の構築方法、多変量テストとインテリジェントセレクションの実装方法などの詳細については、キャンバスドキュメントの「[キャンバスを構築する」]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas)ステップを参照のこと。

{% endtab %}
{% endtabs %}

## ステップ 5: レビューと展開

キャンペーンやキャンバスの最後の構築が終わったら、その詳細を確認しテストしてから送信してください。

次に、[SMS レポート]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/)をチェックして、SMS キャンペーンの結果にアクセスする方法を確認します。
