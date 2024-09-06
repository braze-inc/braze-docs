---
nav_title: 複数店舗サポート
permalink: "/shopify_multiple_store/"
hidden: true
layout: dev_guide
---

# Shopify多店舗化支援

> 複数のShopifyストアを単一のワークスペースに接続し、複数のストアをサポートする新しいベータを使用して、すべてのマーケットまたはブランドの顧客を全体的に把握できます。複数のインスタンスにまたがる取り組みを重複することなく、単一のワークスペースでオートメーション番組およびジャーニーを構築し、起動します。 

{% alert important %}
複数のShopifyストアの対応は、バグを含む可能性があるベータ版で利用できます。この機能は、開発が続行されるにつれて変更される可能性があります。
{% endalert %}

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| ストアごとに[メール サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group)を作成 | メール サブスクリプショングループが作成された後、設定フローの「[メールまたはSMS サブスクライバーs]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers) を収集」ステップの間、指定したストアに指定します。<br><br>これは、ユーザーが準拠のためにどのストアのメールサブスクリプショングループに属しているかを追跡するために必要です。 |
| Shopify 属性 s を使用したs、キャンペーン s、およびキャンバスのオーディットと更新 Segment | 複数のストアから収集されたカスタム属性s は、ネストされたオブジェクトの形式になります。これは、文字列値としてフォーマットされた、総合的なShopify積分で使用されている現行の構造とは異なります。そのため、複数のストアを接続して「ネストされたカスタム属性」フィルターを使用するか、「カスタム属性の変更」トリガーを更新した後に、すべてのSegments、キャンペーンs、またはキャンバスを新しい形式に更新する必要があります。<br><br>現在、どの属性sも使用していない場合は、これを無視できます。 |
| オーディットと更新 Shopifyの別名 | 複数のストアを接続した後、`shopify_customer_id` エイリアスは{% raw %}`shopify_customer_id_{{storename}}`{% endraw %} に移行されます。新しい別名を使用するように内部を更新していることを確認します。従来のエイリアス`shopify_customer_id` は廃止されます。現在エイリアスを使用していない場合は、これを無視できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合
Braze のマルチストアサポートでは、次のことが可能です。
- 店舗全体の顧客を360°表示
- 集約ストアデータを使用して、顧客s のSegments を作成する 
- 顧客が別の店舗を移動するときにメッセージングまたはジャーニーを設定する
- メールやSMSサブスクリプションを複数の店舗で管理する

### 店舗の増設
1. 最初のストアをインストールしたら、**\+ Connect New Store** オプションを選択します。<br>![][1]{: style="max-width:70%;"}<br><br>
2. この新しいストアのオンボーディングフローを実行するように求められます。詳しくは、[Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)のセットアップガイドを参照してください。<br><br>前のストアの設定s は引き継ぐことができますが、オンボーディングの進行に応じて設定s を更新できます。<br><br>
3. 収集メールまたはSMS サブスクライバー s ステップの場合:
- ストアごとに適切なメールとSMSサブスクリプションをアプリ収集するには、ストア設定ごとに一意のサブスクリプショングループsを割り当てる必要があります。 
- ここでは、**do not** enable "Override existing global state for ユーザー s" を有効にすることをお勧めします。これは、複数のストアとやり取りする場合に顧客s をグローバルに配信停止できるためです。<br><br>
4. 必要な数の店舗に対してこのインストールを繰り返します。<br><br>
5. 各ストアのインテグレーションを表示し、詳細設定を設定するには、ドロップダウンメニューでストアを選択します。<br>![][2]{: style="max-width:70%;"}

## Shopify情報

### Shopify別名

{% raw %}複数のストアを接続すると、すべての受信Shopify ユーザーs には、既存のエイリアス`shopify_customer_id` に加えて、新しいエイリアス`shopify_customer_id_{{storename}}` が追加されます。`shopify_customer_id` はレガシーエイリアスであり、この機能が一般的に使用可能な場合は廃止されることに注意してください。前に進む新しいエイリアスを使用するように移行する必要があります。 {% endraw %}

### Shopify カスタム属性s

複数のストアを接続した後、次の属性s は、ストアごとの値と集計値を含むネストされたオブジェクトとして同期されます。
- `shopify_tags`
- `shopify_order_count` (ヒストリカル・バックフィルでのみ使用可能)
- `shopify_total_spent` (ヒストリカル・バックフィルでのみ使用可能)

カスタムイベント s を使用してSegmentを作成または編集するには、**ネストされたカスタム属性** フィルターを選択し、ネストされた属性を見つけます。オブジェクト内のパスまたはフィールドを特定するには、[Generate Schema]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#generate-schema)ツールを使用します。ネストされた属性s を選択すると、プラスボタンの付いたフィールドが選択した属性s の横に耳をアプリし、パスを指定します。ネストされた属性s の詳細については、[ネストされたカスタム属性s]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/) を参照してください。

![3]{:style="max-width:70%;"}

パスを指定するには、フィールドに入力するか、「+」ボタンをクリックしてパスを選択します。

![4]{:style="max-width:70%;"}

### Shopify カスタムイベントs

複数のストアを接続すると、受信Shopify カスタムイベントs に新しいイベントプロパティ`shopify_storefront` が含まれるようになります。[Shopifyデータプロセッシング]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events)を参照して、このインテグレーションでサポートされるすべてのカスタムイベントを確認してください。このイベントプロパティは、イベントの送信元のShopifyストアドメインを提供します。

### アクションベースの配信またはコンバージョン "トラッキング

指定したストアでアクションs を完了するユーザーにトリガー メッセージングするには:

1. キャンペーンの**Schedule Delivery** ステップに移動します。
2. トリガーとして**カスタムイベントを実行**を選択します。
![5]{:style="max-width:70%;"}
3. **Shopify_created_order**、**プロパティ フィルターを追加s** チェックボックスなど、トリガーの行動としてShopifyを選択します。
![6]{:style="max-width:70%;"}
4. **Add Filter**ドロップダウンで**Basic Property**を選択します。
5. **Shopify_storefront**を選択し、ストアのフルShopify領域を入力します。
![7]{:style="max-width:70%;"}


### Shopify ユーザーのマージと同期

エイリアス、{% raw %}`shopify_customer_id_{{storefront_domain}}`、`shopify_email`、または`shopify_phone`、`shopify_phone`、{% endraw %} を使用して、ユーザーのShopify 顧客 ID、メールアドレス、または電話番号がすでにBraze内に存在する場合は、既存のユーザープロファイルを更新します。これらの別名がBraze内に存在しない場合は、新しいユーザープロファイルを作成します。ユーザーのデータ(都市など)は、同じユーザーの複数のShopifyストア間で異なることがあります。このような場合、Braze は、最新のアクティビティを持つストアからユーザープロファイルを必ず更新します。 

{% alert warning %}
Braze は、最新のアクティビティを持つストアからShopify 顧客データを持つユーザープロファイルを更新します。つまり、メール、電話番号、送信側の電話機、市区町村など、任意の属性sは、最新のストアアクティビティで上書きできます。たとえば、ユーザーが2つの別のストアに別の電話番号を持っている場合、Brazeは、最新のアクティビティを持つストアの電話番号でユーザープロファイルを更新します。
{% endalert %}

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
[3]: {% image_buster /assets/img/shopify_nested_attributes.png %}
[4]: {% image_buster /assets/img/shopify_tags.png %}
[5]: {% image_buster /assets/img/shopify_add_trigger.png %}
[6]: {% image_buster /assets/img/shopify_select_event.png %}
[7]: {% image_buster /assets/img/shopify_enter_storefront.png %}
