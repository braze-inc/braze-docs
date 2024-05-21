---
nav_title: 複数店舗サポート
permalink: "/shopify_multiple_store/"
hidden: true
layout: dev_guide
---

# Shopify複数店舗サポート

> 複数のShopifyストアを1つのワークスペースに接続し、複数のストアをサポートする新しいベータ版で、すべての市場またはブランドにわたる顧客の全体的なビューを持つことができます。複数のインスタンスで作業を重複させることなく、単一のワークスペースで自動化プログラムとジャーニーを構築して起動します。 

{% alert important %}
複数のShopifyストアのサポートはベータ版として提供されており、バグが含まれている可能性があります。この機能は開発が進むにつれて変更される可能性がある。
{% endalert %}

## 前提条件

| 要件
| ----------- | ----------- |
| 各店舗に[メール購読グループを]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group)作成する｜メール購読グループを作成した後、設定フローの「[メールまたはSMS購読者を収集]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers)する」ステップで特定の店舗に指定します。<br><br>これは、コンプライアンス上、ユーザーがどのストアのメール購読グループに属しているかを追跡するために必要です。|
| Shopifyの属性を使用したセグメント、キャンペーン、キャンバスの監査と更新｜複数のストアから収集されたカスタム属性は、ネストされたオブジェクトの形式になります。その結果、"入れ子のカスタム属性 "フィルタを使用するために複数のストアを接続した後、または "カスタム属性の変更 "トリガーイベントを更新した後、すべてのセグメント、キャンペーン、またはキャンバスを新しいフォーマットに更新する必要があります。<br><br>今日、どの属性も使っていないのであれば、これは無視して構わない。|
| Shopifyエイリアスの監査と更新｜`shopify_customer_id` エイリアスは、複数のストアを接続した後、{% raw %}`shopify_customer_id_{{storename}}`{% endraw %} に移行されます。新しいエイリアスを使用するように内部システムを更新していることを確認してください。従来のエイリアス、`shopify_customer_id` は廃止される。今日エイリアスを使用しないのであれば、これは無視して構わない。|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合
Brazeの複数店舗サポートでは、以下のことが可能です：
\- 店舗を横断して顧客を360度見渡せる
\- 店舗データを集計して顧客セグメントを作成
\- 顧客が異なる店舗を移動する際のメッセージングやジャーニーの設定
\- さまざまな店舗でEメールやSMSの購読を管理

### 追加店舗の設定
1. 最初のストアをインストールしたら、**「+ Connect New Store**」オプションを選択します。<br>![][1]{: style="max-width:70%;"}<br><br>
2. この新しいストアのオンボーディングフローに進むよう促されます。詳細は[Shopifyの]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)設定ガイドをご覧ください。<br><br>前のストアの設定は引き継ぐことができますが、オンボーディングを進めるにつれて、適宜設定を更新することができることに注意してください。<br><br>
3. EメールまたはSMS購読者を収集するステップ：
- 各ストアのEメールとSMS購読を適切に収集するには、各ストアのセットアップに固有の購読グループを割り当てる必要があります。 
- 既存のグローバル状態を上書きする」を有効に**しない**ことをお勧めします。複数の店舗とやり取りをした場合、グローバルに配信停止になる可能性があります。<br><br>
4. 必要な店舗数だけこのインストールを繰り返す。<br><br>
5. 各ストアのインテグレーションを表示し、詳細設定を行うには、ドロップダウンメニューからストアをクリックしてください：<br>![][2]{: style="max-width:70%;"}

## Shopifyデータ

### Shopifyのエイリアス

{% raw %}複数のストアを接続した後、Shopifyにログインするすべてのユーザーは、既存のエイリアス、`shopify_customer_id` に加えて、新しいエイリアス、`shopify_customer_id_{{storename}}` を持つことになります。なお、`shopify_customer_id` はレガシーエイリアスであり、この機能が一般的に利用できるようになった時点で非推奨となる。今後は新しいエイリアスの使用に移行してください。 {% endraw %}

### Shopifyカスタム属性

複数のストアを接続すると、以下の属性がストアごとの値と集計値を含むネストしたオブジェクトとして同期されます：
`shopify_tags`
-`shopify_order_count` （ヒストリカル・バックフィルからのみ利用可能）
-`shopify_total_spent` （ヒストリカル・バックフィルからのみ利用可能）

セグメントの作成または編集時にカスタム・イベントを使用するには、**ネストされたカスタム属性**フィルタを選択し、ネストされた属性を見つけます。オブジェクト内の特定のパスやフィールドを特定するには、[Generate Schema]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#generate-schema)ツールを使用します。ネストされた属性を選択すると、選択した属性の横にパスを指定するためのプラス・ボタンが付いたフィールドが表示されます。ネストされた属性の詳細については、[ネストされたカスタム属性を]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/)参照してください。

![3]{:style="max-width:70%;"}

パスを指定するには、フィールドに入力するか、プラスボタンをクリックしてパスを選択します。

![4]{:style="max-width:70%;"}

### Shopifyカスタムイベント

複数のストアを接続すると、Shopifyのカスタムイベントに新しいイベントプロパティ`shopify_storefront` が追加されます。この統合でサポートされているすべてのカスタムイベントを見るには、[Shopifyのデータ処理を]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events)参照してください。このイベントプロパティは、Shopifyストアドメインイベントを提供します。

### アクションベースの配信またはコンバージョントラッキング

特定のストアでアクションを完了したユーザーにメッセージをトリガーする：

1. キャンペーンの**スケジュール配信**ステップに移動します。
2. トリガー・イベントとして**カスタム・イベントの実行を**選択する。
![5]{:style="max-width:70%;"}
3. **Shopify\_created\_order の**ようなトリガーイベントとして Shopify イベントを選択し、**Add property filters**チェックボックスをチェックします。
![6]{:style="max-width:70%;"}
4. **Add Filter**ドロップダウンで**Basic Property**を選択する。
5. **shopify\_storefrontを**選択し、ストアの完全なShopifyドメインを入力します。
![7]{:style="max-width:70%;"}


### Shopifyユーザーのマージと同期

ユーザーのShopify顧客ID、電子メールアドレス、または電話番号が、Braze内でエイリアス、{% raw %}`shopify_customer_id_{{storefront_domain}}` 、`shopify_email` 、または`shopify_phone` 、{% endraw %} を使用して既に存在する場合は、既存のユーザープロファイルを更新します。これらのエイリアスがBraze内に存在しない場合は、新しいユーザープロファイルを作成します。ユーザーのデータ(例えば、都市)は、同じユーザーの複数のShopifyストアで異なる可能性があることに注意してください。このような場合、Brazeは常に最新のアクティビティでストアからユーザープロフィールを更新します。 

{% alert warning %}
Brazeは、最新のアクティビティを持つ店舗のShopify顧客データでユーザープロファイルを更新します。つまり、Eメール、電話番号、送信先電話、都市などの属性は、最新のストアアクティビティで上書きされる可能性がある。例えば、ユーザーが2つの異なる店舗で異なる電話番号を持っている場合、Brazeは最も新しいアクティビティがあった店舗の電話番号でユーザープロフィールを更新します。
{% endalert %}

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
[3]: {% image_buster /assets/img/shopify_nested_attributes.png %}
[4]: {% image_buster /assets/img/shopify_tags.png %}
[5]: {% image_buster /assets/img/shopify_add_trigger.png %}
[6]: {% image_buster /assets/img/shopify_select_event.png %}
[7]: {% image_buster /assets/img/shopify_enter_storefront.png %}
