---
nav_title: 再入荷
article_title: 再入荷
page_order: 2
page_type: reference
description: "この記事では、Braze Canvas テンプレートを使用して、パーソナライズされたメッセージングでアイテムが在庫に戻ったときにユーザーに通知することで、購入を駆動する方法について説明します。"
tool: Canvas
---

# 再入荷

> 在庫切れだったが現在購入可能になったアイテムを以前に閲覧したかまたは関心を示したユーザーをターゲットとするメッセージを作成するには、再入荷テンプレートを使用します。これにより、ユーザーが希望する製品が入手可能になった重要なタイミングでユーザーにエンゲージすることで、ユーザーが製品を入手できるようになります。

この記事では、ユーザーライフサイクルの変換ステップ用に設計された**Back In Stock**テンプレートのユースケースについて説明します。完了すると、アイテムが再入荷された時点にプッシュ (Web またはモバイル)、SMS、メールをユーザーに送信し、さらに2件までのリマインダーを送信するキャンバスが完成します。

## 前提条件

このテンプレートを正常に使用するには、次のものが必要です。

- アイテムに関する情報を含む[catalog]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog)
- ユーザーにメッセージを送信する対象のアイテムに[再入荷通知]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#how-back-in-stock-notifications-work)を設定する必要がある

## 必要に応じてテンプレートをカスタマイズする

ここでは、スラックス、ジーンズ、キュロット、その他多くのタイプのパンツを専門とする消費者向けの衣料品小売業者であるPantsLabyrinthに勤務しているとしよう。再入荷テンプレートを使用して、人気の高いジーンズ、Classic Straight Leg が再入荷された時点で、さまざまなチャネルで顧客に通知することができます。

キャンバスを作成する前に、ストレートレッグパンツの在庫に関する情報が含まれている[カタログを設定し]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog)、Classic Straight Leg ジーンズの[再入荷通知を設定]({{site.baseurl}}/user_guide/data/activation/catalogs/catalog_triggers/back_in_stock_notifications/#setting-up-back-in-stock-notifications)します。アプリで Classic Straight Leg ジーンズをお気に入りに登録するというカスタムイベントをユーザーが実行した後で、ユーザーが通知をサブスクリプション登録できるようにしました。

再入荷テンプレートにアクセスするには、新しいキャンバスを作成するときに [**キャンバステンプレートを使用**] > [**Braze テンプレート**] を選択します。次に、**Back in Stock**の横にある**Apply Template**を選択します。これで、テンプレートを使用して、ニーズに合わせてテンプレートを調整できます。

### ステップ1:詳細を設定する

キャンバスの詳細を調整して、目標を反映しましょう。

1. テンプレート名の横にある**編集**を選択します。

<<<<<<< HEAD
![キャンバスの現在のタイトルと説明。]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}
=======
\![キャンバスの現在のタイトルと説明。]({% image_buster /assets/img/canvas_templates/back_in_stock_old_name_description.png %}){: style="max-width:45%;"}
>>>>>>> main

{:start="2"}
2\.キャンバス名を更新し、製品 (Classic Straight Leg) の再入荷時にユーザーをターゲットとするキャンバスであることを示すようにします。
3\.このキャンバスにパーソナライズされたメッセージングが含まれていることを説明する説明を更新します。
4. タグ**Back in Stock** を追加します。これはタグ**Promotional** の下にネストされているため、キャンバスのホームページでフィルタリングできます。 

<<<<<<< HEAD
!["Canvas Details&quot の設定;Canvas の名前が&quot のステップ;Back in Stock - Classic Straight Leg"およびCanvas の簡単な説明。]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})
=======
\!["Canvas Details&quot の設定;Canvas の名前が&quot のステップ;Back in Stock - Classic Straight Leg"およびCanvas の簡単な説明。]({% image_buster /assets/img/canvas_templates/back_in_stock_1.png %})
>>>>>>> main

### ステップ 2: 変換イベントの割り当て

[**1次コンバージョンイベント - A**] を [**特定の購入**] に変更し、製品名として [**Classic Straight Leg**] を選択します。

<<<<<<< HEAD
!["コンバージョンイベント s" を割り当てます。コンバージョン期限が7 日間のクラシックストレートレッグ製品を購入するコンバージョンイベントの種類のセクションです。]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})
=======
\!["コンバージョンイベント s" を割り当てます。コンバージョン期限が7 日間のクラシックストレートレッグ製品を購入するコンバージョンイベントの種類のセクションです。]({% image_buster /assets/img/canvas_templates/back_in_stock_2.png %})
>>>>>>> main

### ステップ 3: エントリスケジュールを調整する

入力スケジュールを**Action-Based**のままにして、ユーザーがアクションを実行したときにキャンバスに入るようにしましょう。テンプレートはすでに**ストックイベントでバックを実行**に設定されています。

このステップでは、2 つの調整を行います。

1. Classic Straight Leg ジーンズの情報が含まれているカタログ (名前は「Straight Leg Pants」) を選択します。 

<<<<<<< HEAD
!["Entry Schedule"アクションベースのキャンバスのステップ。]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})
=======
\!["Entry Schedule"アクションベースのキャンバスのステップ。]({% image_buster /assets/img/canvas_templates/back_in_stock_3.png %})
>>>>>>> main

{: start="2"}
2\.**Start Time (Required)**を希望の開始日時に設定します。

<<<<<<< HEAD
![" Entry Window" 2025年1 月2 日の午前12 時の開始時刻を持つセクション。]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})
=======
\![" Entry Window" 2025年1 月2 日の午前12 時の開始時刻を持つセクション。]({% image_buster /assets/img/canvas_templates/back_in_stock_4.png %})
>>>>>>> main

### ステップ 4: ターゲットオーディエンスを選択する

ターゲットオーディエンスを、 Classic Straight Leg ジーンズを購入する可能性が高いと思われるユーザーとして定義します。

1. 「Favorited - Classic Straight Leg Jeans」というターゲッセグメントを選択します。このセグメントは、アプリまたは Web サイトで Classic Straight Legジ ーンズをお気に入りに登録したユーザーで構成されています。
2. 「Jeans」を「0」回以上購入したユーザを含めるフィルタを選択します。

<<<<<<< HEAD
!["Target Audience" &quotのSegmentでステップ;Favorited - Classic Straight Leg Jeans".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})
=======
\!["Target Audience" &quotのSegmentでステップ;Favorited - Classic Straight Leg Jeans".]({% image_buster /assets/img/canvas_templates/back_in_stock_5.png %})
>>>>>>> main

{: start="3"}
3\.ユーザーが同じステップを同時にトリガーすることを防ぐため、キャンバスの最長期間の経過後にユーザーがキャンバスに再エントリできるように、エントリコントロールを調整します。

<<<<<<< HEAD
!["Entry Controls"ユーザーがキャンバスの最長継続時間でこのキャンバスに再入力できるようにするためのチェックボックス付きのセクション。]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})
=======
\!["Entry Controls"ユーザーがキャンバスの最長継続時間でこのキャンバスに再入力できるようにするためのチェックボックス付きのセクション。]({% image_buster /assets/img/canvas_templates/back_in_stock_6.png %})
>>>>>>> main

{: start="4"}
4. Classic Straight Leg ジーンズをお気に入りにならないカスタムイベントを実行したユーザーを削除するには、終了基準を調整します。

<<<<<<< HEAD
!["Exit Criteria" section。ただし、"のカスタムイベントを実行するユーザー s は除きます。Unfavorited"]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})
=======
\!["Exit Criteria" section。ただし、"のカスタムイベントを実行するユーザー s は除きます。Unfavorited"]({% image_buster /assets/img/canvas_templates/back_in_stock_7.png %})
>>>>>>> main

### ステップ 5: 送信設定を選択する

デフォルトのサブスクリプション設定を維持します。これにより、サブスクリプション登録したユーザーおよびメッセージまたは通知の受信を選択したユーザーのみに送信されるようになります。その他の設定 (フリークエンシーキャップ、サイレント時間、シードグループ) は省略します。

<<<<<<< HEAD
!["Settings&quot を送信;登録または選択されているユーザーを対象としたステップ。]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})
=======
\!["Settings&quot を送信;登録または選択されているユーザーを対象としたステップ。]({% image_buster /assets/img/canvas_templates/back_in_stock_8.png %})
>>>>>>> main

### ステップ6: キャンバスをカスタマイズする

ここでは、ユーザーに送信するチャンネルとコンテンツをカスタマイズして、Canvas を構築します。4 つのテンプレートチャネル(モバイルおよびWeb プッシュ、SMS、およびメール) すべてを使用し、[インテリジェントチャネル]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_channel/) フィルタを使用しているため、追加または削除する必要はありません。

{% alert tip %}
[キャンバスエントリプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/)を使用して、参照している製品に基づいてキャンバス内のメッセージをカスタマイズできます。
{% endalert %}

カスタマイズを開始するには、各メッセージステップを実行してコンテンツを更新します。

1. `!!YOURCATALOGHERE!!` をカタログの名前に置き換えます (“Straight_Leg_Pants”).
2. `[0]` をClassic Straight Leg ジーンズのインデックス番号に置き換えます。これは、ジーンズがカタログの`items` 配列の10 番目の項目であるため、"9" です。(配列はLiquidではゼロインデックスであるため、最初の項目は`0`であり、`1`ではありません。)
3. 次を含む残りのすべてのメッセージステップについて、手順1と2を繰り返します。
    - 1日遅れて送信される「In-Product Msg & Email」メッセージ
    - 購入していないユーザに送信する「プッシュ+メールアラート」メッセージ
4. アクションパスステップを更新するには、[**購入**] アクショングループを選択します。［**特定の購入**] を選択し、製品として「Classic Straight Leg jeans」を選択します。

<<<<<<< HEAD
![Mobile Push Canvas ステップに、商品が再入荷したことをユーザーに通知するメッセージが表示されます。]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})
=======
\![Mobile Push Canvas ステップに、商品が再入荷したことをユーザーに通知するメッセージが表示されます。]({% image_buster /assets/img/canvas_templates/back_in_stock_9.png %})
>>>>>>> main

### ステップ 7:キャンバスをテストして起動する

キャンバスをテストし、期待通りに動作することを確認したら、[**キャンバスを起動**] を選択してキャンバスを起動します。これで、Classic Straight Leg ジーンズをお気に入りに登録し、メッセージングチャネルをサブスクリプション登録したユーザーに対し、このジーンズが再入荷された時点で通知が送信されます。

{% alert tip %}
キャンバスの起動前後に考慮すべき点については、[起動前と起動後のチェックリスト]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/pre_post_launch_checklist/#things-to-consider-before-launch)をご確認ください。
{% endalert %}

