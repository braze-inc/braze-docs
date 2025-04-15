---
nav_title: 購入イベント
article_title: 購入イベント
page_order: 8
page_type: reference
description: "このリファレンス記事では、購入イベントとプロパティ、その使用方法、セグメンテーション、関連する分析を表示する場所などについて説明します。"
search_rank: 3
---

# 購入イベント

> 購入イベントとプロパティ、その使用方法、セグメンテーション、関連する分析を確認できる場所などについて学びましょう。

購入イベントとは、ユーザーが行う購入アクションです。これらのイベントは、アプリ内購入を記録したり、各ユーザープロファイルの生涯価値 (LTV) を設定したりするために使用されます。これらの購入イベントは、チームで設定する必要があります。購入イベントをログに記録すると、数量やタイプなどのプロパティを追加できるため、それらのプロパティに基づいてユーザーのターゲットをさらに絞り込むことができます。

## 購入イベントのログ記録

[購入オブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/)を [`/users/track` エンドポイント]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)に渡すことで、購入をログ記録できます。

以下に、購入をログ記録するために使用されるさまざまなプラットフォームでの方法を示します。これらのページには、購入イベントにプロパティと数量を追加する方法に関するドキュメントもあります。これらのプロパティに基づいて、さらにユーザーのターゲットを絞り込むことができます。

- [Android と FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/)
- [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/)
- [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/logging_purchases/)
- [React Native]({{site.baseurl}}/developer_guide/platform_integration_guides/react_native/analytics/#logging-purchases)
- [Unity]({{site.baseurl}}/developer_guide/platform_integration_guides/unity/Analytics/logging_purchases/)
- [Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/analytics/#logging-purchases)
- [Roku]({{site.baseurl}}/developer_guide/platform_integration_guides/roku/analytics/logging_purchases/)

## 購入データの表示

購入イベントを設定してログ記録を開始したら、この購入データを [[概要] タブ]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#overview-tab)のユーザープロファイルに表示できます。

## 購入データの使用

Braze で購入データを使用する方法には、いくつかがあります。

- **[セグメンテーション](#purchase-event-segmentation):** 購入データを使用して、購入行動に基づいてユーザーのセグメントを作成します。
- **[パーソナライゼーション](#personalization):** 購入データを使用して、ユーザーへのメッセージをパーソナライズします。
- **[トリガーメッセージ](#trigger-messages):** 購入イベントに基づいて、トリガーするメッセージを設定します。
- **[分析](#analytics):** 購入データを分析して、ユーザーの行動やマーケティングキャンペーンの効果に関するインサイトを得ます。

### セグメンテーション {#purchase-event-segmentation}

ログ記録された購入イベントに基づいて、任意の数またはタイプのフォローアップキャンペーンをトリガーできます。例えば、過去 30 日間に購入を行ったユーザーのセグメントや、特定金額を超えて支出したユーザーのセグメントを作成できます。

ユーザーのターゲットを絞り込むときに、次のセグメンテーションフィルターを使用できます。

- 最初に行った購入
- アプリでの最初の購入
- 最後に購入した製品
- 支出金額
- 購入した製品
- 購入数の合計
- X 日間に支出した金額
- Y 日間に購入した製品 X
- Y 日間の X の購入プロパティ
- 過去 Y 日間の X 回の購入

各フィルターの詳細については、[セグメンテーションフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters)の用語集を参照し、「購入行動」でフィルター処理してください。

![ちょうど 3 回購入したユーザーのフィルター適用][1]{: style="max-width:80%;"}

{% alert tip %}
特定の購入の発生回数に基づいてセグメンテーションを行う場合は、その購入を個別に[増分カスタム属性]({{site.baseurl}}/developer_guide/platform_wide/analytics_overview/#custom-attribute-storage)として記録する必要があります。
{% endalert %}

### パーソナライゼーション

ユーザーから収集する他のタイプのデータと同様に、購入データを使用し、Liquid を通じてメッセージングのパーソナライゼーションができます。例えば、先ほど購入した商品に似た商品を勧める、パーソナライズされたメールをユーザーに送信できます。

例えば、ユーザーが最後に購入した商品の名前を格納する購入イベントプロパティ `last_purchased_product` があるとします。このプロパティを使用すると、メールメッセージを次のようにパーソナライズできます。

{% raw %}

```liquid
{% if ${last_purchased_product} == "Running Shoes" %}
  We hope you're enjoying your new running shoes! Based on your recent purchase, you might also like these running shorts and water bottles.
{% elsif ${last_purchased_product} == "Yoga Mat" %}
  We hope you're enjoying your new yoga mat! Based on your recent purchase, you might also like these yoga blocks and straps.
{% else %}
  Thank you for your recent purchase! We hope you're enjoying your new item.
{% endif %}
```

{% endraw %}

この例のメッセージは、`last_purchased_product` プロパティに基づいてパーソナライズされています。ユーザーが最後に購入した製品が「ランニングシューズ」だった場合、ランニングパンツとウォーターボトルを勧めるメッセージが届きます。最後の商品が「ヨガマット」だった場合は、ヨガブロックとストラップを勧めるメッセージが届きます。`last_purchased_product` がそれ以外の場合、一般的なお礼メッセージが届きます。

### トリガーメッセージ

一般的なユースケースは、ユーザーが購入したときにメールなどのメッセージを自動送信することです。例えば、お礼のメッセージや、今後の購入に向けた割引コードを送信できます。

そのためには、アクションベースのキャンペーンまたはキャンバスを作成し、トリガーアクションを [**購入**] に設定します。購入した製品や購入金額など、トリガーに追加条件を指定することもできます。

トリガーメッセージを Liquid でパーソナライズすることもできます。

{% raw %}

```liquid
Thank you for your purchase of ${purchase_product_name}! As a token of our appreciation, here's a discount code for your next purchase: SAVE10
```

{% endraw %}

この例の `${purchase_product_name}` はカスタム属性であり、Braze の設定で、購入製品の名前を保存している実際の属性名に置き換えます。

### 分析

Braze はセグメンテーション用に購入指標を追跡するだけでなく、経時的な各製品の購入数とそれによる収益も記録します。これは、最も人気のある製品を確認したり、プロモーションキャンペーンが収益に与える影響を測定したりするときに役立ちます。

このデータは [[収益レポート]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data)] ページで確認できます。

### 収益計算の理解

<style>
    .no-split {
        word-break: keep-all;
    }
</style>

<table>
    <thead>
        <tr>
            <th>指標</th>
            <th>定義</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-revenue">生涯収益</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='Lifetime Revenue' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#lifetime-value-per-user">ユーザーあたりの生涯価値</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ユーザー一人当たりの生涯価値' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#average-daily-revenue">平均日割り売上</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='平均日収' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics#daily-purchases">日割り購入数</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='1日の購入額' %}</td>
        </tr>
        <tr>
            <td class="no-split"><a href="/docs/user_guide/data_and_analytics/report_metrics/#daily-revenue-per-user">ユーザーあたりの日割り収益</a></td>
            <td class="no-split">{% multi_lang_include metrics.md metric='ユーザー1人あたりの日次収益' %}</td>
        </tr>
    </tbody>
</table>

#### 生涯収益の計算

Braze は購入イベントを使用してユーザーの生涯収益 (生涯価値または LTV とも呼ばれる) を計算します。これは、顧客との将来の関係全体にわたって見込まれる純利益の予測です。これにより、顧客の獲得およびリテンション戦略について、情報に基づく意思決定に役立ちます。

$$\text{Average purchase value} = \frac{\text{Total spend in dollars}}{\text{Total number of purchase events}}$$  

Braze には、ユーザーの LTV を把握するために参照できる主な場所が 2 か所あります。

- 各アプリやサイトの*生涯収益*や*ユーザーあたりの生涯価値*などの全体的な指標については、[収益レポート]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/exporting_revenue_data/#revenue-data)を参照してください。
- 特定ユーザーの生涯収益を把握するには、その[ユーザープロファイル]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab)を参照してください。

##### 返金が生涯収益に与える影響

購入イベントを使用して購入データを追跡する場合、負の `price` プロパティをもつ Braze 購入イベントをログ記録して、返金を追跡する必要があります。この手法により、生涯収益の正確な合計が維持されます。

ただし、返金は追加の購入イベントとしてカウントされることに注意してください。次の例を考えてみます。Sam は 12 ドルの初回購入を行いましたが、購入品の一部を返品して 5 ドルの返金を受けました。Sam のプロファイルには次のように記録されます。

- 価格 12ドルで 1 回の購入
- 価格 -5で 1 回の購入
- 生涯収益 7 ドル

サムのプロファイルには購入イベントが 2 つありますが、実際の購入は 1 回のみです。これは、ユーザーの購入回数を含めて作成されたセグメントやユースケースがある場合、考慮すべき重要な点です。返金が継続的に行われると、ユーザープロファイルの購入数が膨れ上がります。

## 購入イベントプロパティ {#purchase-properties}

購入イベントプロパティを使用すると、購入に関するプロパティを設定して、トリガー条件のさらなる絞り込み、メッセージングのパーソナライゼーションの強化、および未加工データをエクスポートすることによる高度な分析の生成ができます。プロパティ値のタイプ (文字列、数値、ブール値、日付) はプラットフォームによって異なり、多くの場合、キーと値のペアとして割り当てられます。

例えば、ある e コマースアプリケーションで、購入後のユーザーにメッセージを送信する場合、`brand_name` という購入イベントプロパティを追加することで、オーディエンスのターゲット選択をさらに改善し、キャンペーンのパーソナライゼーションを向上できます。

**購入イベントプロパティに基づくトリガーの例:**

![ブランド名が HeadphoneMart に等しいヘッドフォンを購入したユーザーにキャンペーンを送信するアクションベースの配信設定][2]{: style="max-width:80%;margin-left:15px;"}

詳細については、「[購入プロパティオブジェクト]({{site.baseurl}}/api/objects_filters/purchase_object/#purchase-properties-object)」を参照してください。

### イベントプロパティのセグメンテーション

イベントプロパティのセグメンテーションにより、取得したカスタムイベントのみでなく、それらのイベントに関連するプロパティにも基づいて、ターゲットのユーザーを選択できます。この機能により、購入イベントとカスタムイベントをセグメント化するときのフィルターオプションが追加されます。

![][6]{: style="max-width:80%;margin-left:15px;"}

これらのセグメンテーションフィルターには次のようなものがあります。
- 最後のY 日間に、V X 倍のプロパティ Y でカスタムイベントを実行しました。
- 過去 Y 日間に、プロパティ Y とその値 V を持つ購入を X 回行った。
- 1、3、7、14、21、30 日以内に、セグメントに加えられる条件を満たした。

[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)とは異なり、使用されるセグメントはリアルタイムで更新され、サポートされるセグメントの数に制限はなく、最大 30 日間の履歴を確認でき、データポイントが使用されます。データポイントが追加で消費されるため、カスタムイベントのイベントプロパティを有効にするように、Braze カスタマーサクセスマネージャーに依頼してください。

承認されると、[**プロパティの管理**] をクリックして、ダッシュボードの [**データ設定**] > [**カスタムイベント**] でプロパティを追加できます。その後、これらのイベントプロパティをキャンペーンビルダーまたはキャンバスビルダーのターゲットステップで使用できます。

### キャンバスエントリのプロパティとイベントプロパティ

{% alert important %}
2023 年 2 月 28 日以降、元のエディターを使用したキャンバスの作成や複製はできなくなりました。このセクションは、元のキャンバスワークフローで `canvas_entry_properties` や `event_properties` を使用するとき場合の参考として用意されています。
{% endalert %}

キャンバスのユーザージャーニーで `canvas_entry_properties` と `event_properties` を活用できます。詳細と例については、「[キャンバスエントリのプロパティとイベントプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/)」を参照してください。

{% alert important %}
`event_properties` は先頭のメッセージステップで使用できません。代わりに、`canvas_entry_properties` を使用するか、`event_properties` を含むメッセージステップの**前**に、対応するイベントを含むアクションパスを追加する必要があります。
{% endalert %}

{% tabs local %}
{% tab キャンバスエントリのプロパティ %}

[キャンバスエントリのプロパティ]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/)は、アクションベースまたは API でトリガーされるキャンバスにマップするプロパティです。`canvas_entry_properties` オブジェクトのサイズ上限は 50 KB であることに注意してください。

{% alert important %}
特にアプリ内メッセージチャネルでは、以前の早期アクセスの一環として元のエディターで永続的なエントリプロパティを有効にしている場合、キャンバスフローと元のキャンバスエディターでのみ `canvas_entry_properties` を参照できます。
{% endalert %}

キャンバスフローメッセージングでは、いずれのメッセージステップでも `canvas_entry_properties` を Liquid で使用できます。これらのプロパティを参照するときには、``{% raw %} canvas_entry_properties${property_name} {% endraw %}`` の Liquid を使用してください。このように使用するには、イベントがカスタムイベントまたは購入イベントでなければならないことに注意してください。 

{% raw %}
例えば、`\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}` というリクエストを考えてみます。`{{canvas_entry_properties.${product_name}}}` という Liquid でメッセージに「靴」という単語を追加できます。
{% endraw %}

元のエディターで作成されたキャンバスの場合、`canvas_entry_properties` はキャンバスの最初のフルステップでのみ参照できます。

{% endtab %}

{% tab イベントプロパティ %}
イベントプロパティとは、カスタムイベントと購入に設定したプロパティを指します。これらの `event_properties` は、アクションベースの配信やキャンバスを含むキャンペーンで使用できます。

キャンバスフローでは、アクションパスステップに続く任意のメッセージステップで、カスタムイベントと購入イベントのプロパティを Liquid で使用できます。キャンバスフローでこれらの `event_properties` を参照する場合は、必ず {% raw %} ``{{event_properties.${property_name}}}``{% endraw %} を使用してください。メッセージコンポーネントでこのように使用するには、これらのイベントがカスタムイベントまたは購入イベントである必要があります。

元のキャンバスエディターでは、スケジュールされたフルステップで `event_properties` を使用できません。ただし、アクションベースのキャンバスの最初のフルステップでは、フルステップがスケジュールされている場合でも `event_properties` を使用できます。

アクションパスに続く最初のメッセージステップでは、そのアクションパスで参照されるイベントに関連する `event_properties` を使用できます。これらの `event_properties` は、ユーザーが実際にアクションを実行した場合 (その他のユーザーグループに移動していない) にのみ使用できます。このアクションパスとメッセージステップの間に、他のステップ (別のアクションパスやメッセージステップではない) があってもかまいません。

{% endtab %}
{% endtabs %}

### 注文レベルでの購入記録
商品レベルではなく、注文レベルで購入を記録したい場合、注文名または注文カテゴリを `product_id` として使用できます。詳細については、[購入オブジェクトの仕様]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions)を参照してください。 

## 禁止リストへの購入イベントの追加

たまに、購入イベントについて、データポイントの消費量が多いもの、マーケティング戦略に不要になったもの、または誤って記録されたものが見つかることがあります。開発チームがアプリや Web サイトのバックエンドからこのデータを削除する作業をしている間、このデータが Braze に送信されないようにするために、カスタムデータオブジェクトを禁止リストに入れておくことができます。

Braze ダッシュボードでは、[**データ設定**] > [**製品**] から禁止リストを管理できます。詳細については、「[カスタムデータの管理]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data/)」を参照してください。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**製品**] は [**設定の管理**] の下にあります。
{% endalert %}

[1]: {% image_buster /assets/img/purchase_filter_example.gif %}
[2]: {% image_buster /assets/img/purchase2.png %}
[5]: {% image_buster /assets/img/purchase5.png %}
[6]: {% image_buster /assets/img/nested_object3.png %}
