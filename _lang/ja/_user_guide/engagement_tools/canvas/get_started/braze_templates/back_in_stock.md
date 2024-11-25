---
nav_title: バックイン・ストック
article_title: バックイン・ストック
page_order: 2
page_type: reference
description: "この記事では、Braze Canvas テンプレートを使用して、パーソナライズされたメッセージングでアイテムが在庫に戻ったときにユーザーに通知することで、購入を駆動する方法について説明します。"
tool: Canvas
---

# 再入荷

> 在庫切れのアイテムを以前に閲覧したか、関心を示したが購入可能なユーザーをターゲットとするメッセージを作成するには、在庫切れテンプレートを使用します。これにより、製品が可用性に戻った重要な時点でユーザーが彼らを関与させることで、ユーザーが欲しい製品を手に入れることができるようになります。

この記事では、ユーザーライフサイクルの変換ステップ用に設計された**Back In Stock**テンプレートのユースケースについて説明します。終了すると、アイテムが在庫に戻ったときにプッシュ(Web またはモバイル)、SMS、またはメールをユーザーに送信し、最大2 つのリマインダーを送信するキャンバスが作成されます。

## 前提条件

このテンプレートを正常に使用するには、次のものが必要です。

- アイテムに関する情報を含む[catalog]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog)
- [ユーザにメッセージを送信する項目に、在庫返却通知]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work)を設定する必要があります

## 必要に応じてテンプレートをカスタマイズする

ここでは、スラックス、ジーンズ、キュロット、その他多くのタイプのパンツを専門とする消費者向けの衣料品小売業者であるPantsLabyrinthに勤務しているとしよう。私たちは、バックイン在庫テンプレートを使用して、人気のジーンズ、クラシックストレートレッグが在庫に戻ったときに、様々なチャンネルの顧客に通知することができます。

キャンバスを作成する前に、[は、ストレート・レッグ・パンツの在庫に関する情報を含むカタログ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog)と、クラシック・ストレート・レッグ・ジーンズの[バックアップ・イン・ストック通知]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications)をセットアップしました。ユーザーがアプリでクラシックストレートレッグジーンズをお気に入りにするカスタムイベントを実行した後、通知をサブスクライブするようにしました。

バックインストックテンプレートにアクセスするには、新しいキャンバスを作成するときに、**キャンバステンプレートを使用**> **ブレーズテンプレート**を選択します。次に、**Back in Stock**の横にある**Apply Template**を選択します。これで、テンプレートを使用してニーズに合わせることができます。

### ステップ1:詳細を設定する

キャンバスの詳細を調整して、目標を反映しましょう。

1. テンプレート名の横にある**編集**を選択します。

![Canvas.]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %})の現在のタイトルと説明{: style="max-width:45%;"}

{:start="2"}
2\.キャンバス名を更新して、製品のClassic Straight Leg が在庫に戻ったときに、キャンバスがユーザーをターゲットとしていることを指定します。
3\.このキャンバスにパーソナライズされたメッセージングが含まれていることを説明する説明を更新します。
4. タグ**Back in Stock** を追加します。これはタグ**Promotional** の下にネストされているため、キャンバスのホームページでフィルタリングできます。 

!["Canvas Details&quot の設定;Canvas 名&quot のステップ;Stock の戻るClassic Straight Leg"およびCanvas の簡単な説明。][1]

### ステップ2:変換イベントの割り当て

**Primary Conversion Event - A**を**に変更し、特定の購入**を作成し、製品名に**Classic Straight Leg**を選択します。

![" Assign Conversion Events" Classic Straight Leg 製品を購入するコンバージョンイベントタイプのセクション。コンバージョン期限は7 日です。][2]

### ステップ 3:入力スケジュールを調整する

入力スケジュールを**Action-Based**のままにして、ユーザーがアクションを実行したときにキャンバスに入るようにしましょう。テンプレートはすでに**ストックイベントでバックを実行**に設定されています。

このステップでは、2 つの調整を行います。

1. 「ストレートレッグパンツ」と名付けたクラシックストレートレッグジーンズの情報を含むカタログを選択します。 

!["Entry Schedulde"アクションベースのキャンバスのステップ。][3]

{: start="2"}
2\.**Start Time (Required)**を希望の開始日時に設定します。

![" Entry Window" 2025年1 月2 日の開始時刻が12 時のセクション。][4]

### ステップ4:対象者を選択

ターゲット・オーディエンスを、クラシック・ストレート・レッグ・ジーンズを購入する可能性が高いと思われるユーザーとして定義します。

1. 私たちのアプリまたはウェブサイトでクラシックストレートレッグジーンズをお気に入りのユーザーで構成されるターゲットセグメント「Favorited - Classic Straight Leg Jeans」を選択します。
2. 「Jeans」を「0」回以上購入したユーザを含めるフィルタを選択します。

![" Target Audience" " のセグメントへのステップ; Favorited - Classic Straight Leg Jeans"][5]

{: start="3"}
3\.ユーザがキャンバスの最長継続時間後にキャンバスに再び入ることができるように、入力コントロールを調整して、ユーザが同じステップを同時にトリガしないようにします。

![" Entry Controls" ユーザがキャンバスの最大継続時間でこのキャンバスを再入力できるようにするチェックボックス付きのセクション。][6]

{: start="4"}
4. Classic Straight Leg ジーンズをお気に入りにならないカスタムイベントを実行したユーザーを削除するには、終了基準を調整します。

!["Exit Criteria"セクション。ただし、"のカスタムイベントを実行するユーザは例外です。Unfavorited"。][7]

### ステップ 5: 送信設定を選択する

デフォルトのサブスクリプション設定を維持するため、メッセージまたは通知の受信をサブスクライブまたはオプトインしたユーザーにのみ送信し、その他の設定(頻度の上限、静かな時間、シードグループ)はスキップします。

!["Settings&quot を送信します。サブスクライブまたはオプトインしているユーザーをターゲットにするステップです。][8]

### ステップ 6:キャンバスをカスタマイズする

ここでは、ユーザーに送信するチャンネルとコンテンツをカスタマイズして、Canvas を構築します。4 つのテンプレートチャネル(モバイルおよびWeb プッシュ、SMS、およびメール) すべてを使用し、[インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) フィルタを使用しているため、追加または削除する必要はありません。

{% alert tip %}
[キャンバスエントリプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/)を使用して、参照している製品に基づいてキャンバス内のメッセージをカスタマイズできます。
{% endalert %}

カスタマイズを開始するには、各メッセージステップを実行してコンテンツを更新します。

1. `!!YOURCATALOGHERE!!` をカタログ名("Straight_Leg_Pants") に置き換えます。
2. `[0]` をClassic Straight Leg ジーンズのインデックス番号に置き換えます。これは、ジーンズがカタログの`items` 配列の10 番目の項目であるため、"9" です。(配列はLiquidではゼロインデックスであるため、最初の項目は`0`であり、`1`ではありません。)
3. 以下を含む残りのすべてのメッセージステップについて、ステップ1 と2 を繰り返します。
    - 1日遅れて送信される「In-Product Msg & Email」メッセージ
    - 購入していないユーザに送信する「プッシュ+メールアラート」メッセージ
4. アクションパスステップを更新するには、**Purchase**アクショングループを選択します。次に、**特定の購入**を選択し、製品のClassic Straight Leg ジーンズを選択します。

![Mobile Push Canvas ステップで、製品が在庫に戻ったことをユーザーに通知するメッセージが表示されます。][9]

### ステップ 7:キャンバスをテストして起動する

キャンバスをテストし、期待通りに動作することを確認した後、**Launch Canvas**を選択して起動します。これで、クラシックストレートレッグジーンズをお気に入りにして、私たちのメッセージングチャンネルに加入したユーザーは、在庫が戻ったときに通知を受け取ります!

{% alert tip %}
キャンバスを起動する前と後に考慮すべき事柄については、[起動前と起動後のチェックリスト]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch)を参照してください。
{% endalert %}

[1]: {% image_buster /assets/img/canvas_templates/back_in_stock_1.png %}
[2]: {% image_buster /assets/img/canvas_templates/back_in_stock_2.png %}
[3]: {% image_buster /assets/img/canvas_templates/back_in_stock_3.png %}
[4]: {% image_buster /assets/img/canvas_templates/back_in_stock_4.png %}
[5]: {% image_buster /assets/img/canvas_templates/back_in_stock_5.png %}
[6]: {% image_buster /assets/img/canvas_templates/back_in_stock_6.png %}
[7]: {% image_buster /assets/img/canvas_templates/back_in_stock_7.png %}
[8]: {% image_buster /assets/img/canvas_templates/back_in_stock_8.png %}
[9]: {% image_buster /assets/img/canvas_templates/back_in_stock_9.png %}