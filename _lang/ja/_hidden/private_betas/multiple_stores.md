---
nav_title: 複数店舗サポート
permalink: "/shopify_multiple_store/"
hidden: true
layout: dev_guide
---

# Shopify複数店舗サポート

> 複数のShopifyストアを1つのワークスペースに接続し、複数ストアをサポートする新しいベータ版で、すべての市場やブランドにわたる顧客の全体像を把握できる。複数のインスタンスで作業を重複させることなく、単一のワークスペースで自動化プログラムとジャーニーを構築し、起動する。 

{% alert important %}
複数のShopifyストアのサポートはベータ版として提供されており、バグが含まれている可能性がある。この機能は、開発が進むにつれて変更される可能性がある。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| 店舗ごとに[Eメール購読グループを]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group)作成する | Eメール購読グループが作成されたら、セットアップフローの "[EメールまたはSMS購読者を収集する]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers)"ステップで、特定のストアに指定する。<br><br>これは、コンプライアンス上、ユーザーがどのストアのメール購読グループに属しているかを追跡するために必要である。 |
| Shopifyの属性を使用してセグメント、キャンペーン、キャンバスを監査し、更新する | 複数のストアから収集されるカスタム属性は、ネストされたオブジェクトの形式となり、文字列値としてフォーマットされるShopify統合全体で使用されている現在の構造とは異なる。その結果、"ネストされたカスタム属性 "フィルタを使用するために複数のストアを接続した後、または "カスタム属性の変更 "トリガーイベントを更新した後、すべてのセグメント、キャンペーン、またはキャンバスを新しいフォーマットに更新する必要がある。<br><br>今日、どの属性も使用していないのであれば、これは無視して構わない。 |
| Shopifyエイリアスの監査と更新 | 複数のストアを接続すると、`shopify_customer_id` エイリアスは{% raw %}`shopify_customer_id_{{storename}}`{% endraw %} に移行される。新しいエイリアスを使用するように内部システムを更新していることを確認する。従来のエイリアス、`shopify_customer_id` は廃止される。今日エイリアスを使用しないのであれば、これを無視して構わない。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合
Brazeの複数店舗サポートでは、以下のことが可能だ：
- 店舗全体で顧客を360°把握する
- 店舗データを集計して顧客のセグメントを作成する 
- 顧客が異なる店舗を移動する際に、メッセージングやジャーニーを設定する
- さまざまな店舗でEメールとSMSの購読を管理する

### 追加店舗を設定する
1. 最初のストアをインストールしたら、**「+ Connect New Store**」オプションを選択する。<br>![][1]{: style="max-width:70%;"}<br><br>
2. 新規店舗のオンボーディング・フローに進むよう促される。詳細は[Shopifyの設定]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)ガイドを参照されたい。<br><br>以前のストアの設定は引き継ぐことができるが、オンボーディングを進めていく中で、適宜設定を更新していくことができる。<br><br>
3. EメールまたはSMS購読者の収集ステップについて：
- 各ストアのEメールとSMS購読を適切に収集するには、各ストアのセットアップに固有の購読グループを割り当てる必要がある。 
- 既存のグローバルステートを上書きする "を有効に**しない**ことをお勧めする。<br><br>
4. 必要な店舗数だけ、このインストールを繰り返す。<br><br>
5. 各ストアのインテグレーションを表示し、詳細設定を行うには、ドロップダウンメニューからストアをクリックする：<br>![][2]{: style="max-width:70%;"}

## Shopifyのデータ

### Shopifyのエイリアス

{% raw %}複数のストアを接続した後、Shopifyに流入するすべてのユーザーは、既存のエイリアス、`shopify_customer_id` に加えて、新しいエイリアス、`shopify_customer_id_{{storename}}` を持つことになる。なお、`shopify_customer_id` はレガシーエイリアスであり、この機能が一般的に利用可能になった時点で非推奨となる。今後は新しいエイリアスの使用に移行する必要がある。 {% endraw %}

### Shopifyカスタム属性

複数のストアを接続すると、以下の属性が、ストアごとの値と集約値を含むネストしたオブジェクトとして同期される：
- `shopify_tags`
- `shopify_order_count` (ヒストリカル・バックフィルのみ）
- `shopify_total_spent` (ヒストリカル・バックフィルのみ）

セグメントの作成または編集時にカスタム・イベントを使用するには、**ネストされたカスタム属性**フィルターを選択し、ネストされた属性を見つける。オブジェクト内の特定のパスやフィールドを特定するには、[Generate Schema]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#generate-schema)ツールを使う。ネストされた属性を選択すると、選択した属性の横にパスを指定するためのプラス・ボタンが付いたフィールドが表示される。ネストされたアトリビュートについての詳細は、[ネストされたカスタム・アトリビュートを]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/)参照のこと。

![3]{:style="max-width:70%;"}

パスを指定するには、フィールドに入力するか、プラスボタンをクリックしてパスを選択する。

![4]{:style="max-width:70%;"}

### Shopifyカスタムイベント

複数のストアを接続した後、Shopifyのカスタムイベントに新しいイベントプロパティ`shopify_storefront` が追加される。この統合でサポートされるすべてのカスタムイベントを見るには、[Shopifyのデータ処理を]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events)参照のこと。このイベントプロパティは、Shopifyストアドメインイベントを提供する。

### アクションベースの配信またはコンバージョントラッキング

特定の店舗でアクションを完了したユーザーに対してメッセージをトリガーする：

1. キャンペーンの**Schedule Delivery**ステップに移動する。
2. トリガーイベントとして「**カスタムイベントを実行**」を選択する。
![5]{:style="max-width:70%;"}
3. **Shopify_created_order の**ようなトリガーイベントとして Shopify イベントを選択し、**Add property filters**チェックボックスをチェックする。
![6]{:style="max-width:70%;"}
4. **Add Filter**ドロップダウンで**Basic Propertyを**選択する。
5. **shopify_storefrontを**選択し、ストアの完全なShopifyドメインを入力する。
![7]{:style="max-width:70%;"}


### Shopifyユーザーのマージと同期

ユーザーのShopify顧客ID、電子メールアドレス、または電話番号が、Braze内でエイリアス、{% raw %}`shopify_customer_id_{{storefront_domain}}` 、`shopify_email` 、または`shopify_phone` 、{% endraw %} を使用してすでに存在する場合は、既存のユーザープロファイルを更新する。これらのエイリアスがBraze内に存在しない場合は、新しいユーザープロファイルを作成する。同一ユーザーの複数のShopifyストアで、ユーザーのデータ（例えば、都市）が異なる可能性があることに注意すること。このような場合、Brazeは常に最新のアクティビティでストアからユーザープロフィールを更新する。 

{% alert warning %}
Brazeは、最新のアクティビティを持つ店舗のShopify顧客データでユーザープロファイルを更新する。つまり、Eメール、電話番号、送信先電話、都市などの属性は、最新のストアアクティビティで上書きされる可能性がある。例えば、ユーザーが2つの異なる店舗で異なる電話番号を持っている場合、Brazeは最も新しいアクティビティを持つ店舗の電話番号でユーザープロフィールを更新する。
{% endalert %}

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
[3]: {% image_buster /assets/img/shopify_nested_attributes.png %}
[4]: {% image_buster /assets/img/shopify_tags.png %}
[5]: {% image_buster /assets/img/shopify_add_trigger.png %}
[6]: {% image_buster /assets/img/shopify_select_event.png %}
[7]: {% image_buster /assets/img/shopify_enter_storefront.png %}
