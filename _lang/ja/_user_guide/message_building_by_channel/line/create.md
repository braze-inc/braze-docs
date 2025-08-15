---
nav_title: LINE メッセージの作成
article_title: LINE メッセージの作成
page_order: 1
description: "この記事では、LINE メッセージのキャンペーンまたはキャンバスを作成する方法について説明します。"
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# LINE メッセージの作成

> LINE キャンペーンは、顧客に直接配信され、プログラムでチャットできます。Liquid などのダイナミックコンテンツを使用して、ユーザー一人ひとりに合わせた体験を作り出し、控えめなブランド体験を強化する環境を作ることができます。

## 前提条件

LINE メッセージを作成する前に、次の手順を実行します。

1. LINE の概要を読みます。
2. ポリシー、制限、およびコンテンツルールを承認します。
3. [LINE への接続を設定します]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/)。

Braze から LINE メッセージを送信すると、アカウントのメッセージクレジットが消費されます。

## ステップ 1: メッセージを作成する場所を選択する

メッセージは、キャンペーンとキャンバスのどちらを使用して配信すべきでしょうか。キャンペーンは単一のシンプルなメッセージングキャンペーンに適していますが、キャンバスはマルチステップのユーザーのジャーニーに適しています。

{% tabs %}
{% tab キャンペーン %}

**ステップ:**

1. [**メッセージング**] > [**キャンペーン**] の順に進み、[**キャンペーンを作成**] を選択します。
2. [**LINE**] を選択するか、マルチチャネルをターゲットとするキャンペーンでは、[**マルチチャネルキャンペーン**] を選択します。
3. キャンペーンに、明確で意味のある名前を付けます。
4. 必要に応じて、[[チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)] と [[タグ]({{site.baseurl}}/user_guide/administrative/app_settings/tags/)] を追加します。
   * タグを使用すると、キャンペーンを検索してレポートを作成しやすくなります。
5. キャンペーンに必要な数だけバリアントを追加して名前を付けます。追加したバリアントごとに、さまざまなプラットフォーム、メッセージタイプ、レイアウトを選択できます。このトピックの詳細については、「[多変量テストと AB テスト]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/)」を参照してください。

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

## ステップ 2: LINE メッセージを作成する

必要に応じて、パーソナライゼーション (Liquid またはコネクテッドコンテンツなど) を使用してメッセージを作成します。LINE では、各メッセージに最大5 つのメッセージバブルを使用できます。これらのバブルには、テキスト、イメージ、リッチ、またはカードベースのいずれかの使用可能なメッセージレイアウトを使用できます。

![プレビューにメッセージが表示された LINE 作成画面。]({% image_buster /assets/img/line/line_composer.png %})

### ヒント

#### Liquid の使用

Liquid を使用する場合は、必ずパーソナライゼーションのデフォルト値を含めてください。これにより、不完全なユーザープロファイルを持つ受信者が空のプレースホルダーを受信しないようにできます。例えば、ユーザーは、メッセージ「様」を受信する代わりに、メッセージ「新規に配信登録をいただいたお客様へ」を受信できます。

#### 右から左へのメッセージを作成する

右から左へのメッセージの最終的な出現は、サービスプロバイダがそれらをどのようにレンダリングするかに大きく依存します。右から左へのメッセージを可能な限り正確に表示するためのベストプラクティスについては、[右から左へのメッセージを作成する]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/)を参照してください。

## ステップ 3: メッセージをプレビューしてテストする

[**テスト**] タブに切り替えて、コンテンツテストグループまたは個々のユーザーにテスト用の LINE メッセージを送信するか、ユーザーとしてメッセージを Braze で直接プレビューします。

![[テスト] タブには、テストメッセージのプレビューが表示されます。]({% image_buster /assets/img/line/test_preview.png %})

## ステップ 4: キャンペーンまたはキャンバスの残りの部分を作成する

{% tabs %}
{% tab キャンペーン %}

キャンペーンの残りの部分を作成します。ツールを最適に使用して LINE メッセージを作成する方法の詳細については、次のセクションを参照してください。

### 配信スケジュールまたはトリガーを選択する

LINE メッセージは、スケジュールされた時刻、アクション、または API トリガーに基づいて配信できます。スケジュールとトリガーのオプションの詳細については、「[キャンペーンのスケジュール設定]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/)」を参照してください。

配信コントロールを指定できます。たとえば、ユーザーを[再有効化]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns)してキャンペーンを受信できるようにしたり、[フリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping)ルールを有効にしたりできます。アクションベースの配信では、キャンペーンの継続時間と [[サイレント時間]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours)] を設定することもできます。

### ターゲットとするユーザーを選択する

セグメントまたはフィルターを選択して [[ユーザーをターゲットに設定]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/)] し、オーディエンスを絞り込みます。すでにサブスクリプショングループを選択しているため、ユーザーがブランドに対して希望しているコミュニケーションの頻度やカテゴリによって、ユーザーが絞り込まれます。 

セグメントから大きなオーディエンスを選択し、必要に応じて[フィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/)でさらにセグメントを絞り込みます。セグメントのおおよその人数について現在の状態を示すスナップショットが自動的に表示されます。正確なセグメントメンバーシップは常にメッセージが送信される直前に計算されることに注意してください。

### コンバージョンイベントを選択する

Braze では、キャンペーンを受信した後、ユーザーが指定のアクションや[コンバージョンイベント]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/)を実行する頻度を追跡できます。ユーザーが指定したアクションを実行した場合にコンバージョンがカウントされる期間は、最大 30 日間まで設定できます。

コンバージョンイベントにより、キャンペーンの成否を測定できます。以下に例を示します。

- ジオターゲティングを使用して、購入を行うユーザーの最終目標を持つ LINE メッセージをトリガーする場合は、コンバージョンイベントを `Purchase` に設定します。
- ユーザーをアプリに誘導しようとする場合は、コンバージョンイベントを `Starts Session` に設定します。

独自のユースケースに基づいて、カスタムコンバージョンイベントを設定することもできます。このキャンペーンの成功を測定する方法について独創的に考えてみましょう。

{% endtab %}
{% tab キャンバス %}

まだキャンバスの残りのセクションを完了していない場合は、完了します。キャンバスの残りの部分を作成する方法の詳細については、多変量テストとインテリジェントセレクションを使用してください。詳しくは、「[キャンバスの作成]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/)」を参照してください。

{% endtab %}
{% endtabs %}

## ステップ 5: レビューと展開

キャンペーンまたはキャンバスの最後の部分の作成が完了したら、その詳細を確認し、テストしてから送信してください。

次に、[LINE レポート]({{site.baseurl}}/line/reporting/)をチェックして、LINE キャンペーンの結果にアクセスする方法を確認します。


