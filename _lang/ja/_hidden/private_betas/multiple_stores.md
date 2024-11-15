---
nav_title: 複数店舗サポート
permalink: "/shopify_multiple_store/"
hidden: true
---

# Shopify 複数店舗サポート

> 複数のShopifyストアを1つのワークスペースに接続し、複数ストアをサポートする新しいベータ版で、すべてのマーケターにわたる顧客の全体像を把握しよう。複数のインスタンス間で作業を重複させることなく、単一のワークスペースでオートメーションプログラムとジャーニーを構築および起動します。 

{% alert important %}
複数の Shopify ストアのサポートはベータ版で利用可能ですが、バグが含まれている可能性があります。この機能は、開発が続行されるにつれて変更される可能性があります。
{% endalert %}

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| ストアごとに[メール サブスクリプショングループ]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group)を作成 | メール サブスクリプショングループが作成された後、設定フローの「[メールまたはSMS サブスクライバーs]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers) を収集」ステップの間、指定したストアに指定します。<br><br>これは、ユーザーが準拠のためにどのストアのメールサブスクリプショングループに属しているかを追跡するために必要です。 |
| Shopify 属性を使用したセグメント、キャンペーン、キャンバスの監査と更新 | 複数のストアから収集されたカスタム属性s は、ネストされたオブジェクトの形式になります。これは、文字列値としてフォーマットされた、総合的なShopify積分で使用されている現行の構造とは異なります。そのため、複数のストアを接続して「階層化カスタム属性」フィルターを使用するか、「カスタム属性の変更」トリガーイベントを更新した後に、すべてのセグメント、キャンペーン、またはキャンバスを新しい形式に更新する必要があります。<br><br>現在、どの属性sも使用していない場合は、これを無視できます。 |
| Shopify エイリアスの監査と更新 | 複数のストアを接続した後、`shopify_customer_id` エイリアスは{% raw %}`shopify_customer_id_{{storename}}`{% endraw %} に移行されます。新しいエイリアスを使用するようにすべての内部システムを更新していることを確認します。従来のエイリアス `shopify_customer_id` は廃止されます。現在エイリアスを使用していない場合は、これを無視できます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合
Braze の複数ストアサポートでは、次のことが可能です。
- 店舗全体の顧客を360度見渡すことができる
- 集計ストアデータを使用して顧客のセグメントを作成する 
- 顧客が別の店舗を移動するときにメッセージングまたはジャーニーを設定する
- 複数のストア間でメールと SMS のサブスクリプションを管理する

{% alert important %}
1つのワークスペースで複数のブランドをサポートすると、ユーザーはそれらのブランド間で買い物ができるため、ユーザープロファイルが重複する可能性が高くなる。各ブランドをそれぞれのワークスペースに配置することをお勧めする。
{% endalert %}

### 店舗の増設
1. 最初のストアをインストールしたら、**「+ Connect New Store**」オプションを選択する。<br>![][1]{: style="max-width:70%;"}<br><br>
2. 新店舗のオンボーディング・フローを確認する。詳しくは、[Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/)のセットアップガイドを参照してください。<br><br>前のストアの設定は引き継ぐことができますが、オンボーディングの進行に応じて設定を更新できます。<br><br>
3. メールまたは SMS サブスクライバーの収集ステップの場合:
- 各ストアのメールおよび SMS サブスクリプションを適切に収集するには、各ストア設定に固有のサブスクリプショングループを割り当てる必要があります。 
- 「ユーザーの既存のグローバル状態を上書き」を有効に**しない**ことをお勧めします。これは、顧客が複数のストアとやり取りした場合に、グローバルに配信停止される可能性があるためです。<br><br>
4. 必要な数の店舗に対してこのインストールを繰り返します。<br><br>
5. 各ストアのインテグレーションを表示し、詳細設定を行うには、ドロップダウンメニューからストアをクリックする：<br>![][2]{: style="max-width:70%;"}

## Shopify情報

### Shopify別名

{% raw %}複数のストアに接続すると、すべての新しい Shopify ユーザーは、既存のエイリアス `shopify_customer_id` に加えて新しいエイリアス `shopify_customer_id_{{storename}}` を持つことになります。`shopify_customer_id` は従来のエイリアスであり、この機能が一般公開されると非推奨になります。今後は、新しいエイリアスの使用に移行する必要があります。 {% endraw %}

### Shopify カスタム属性s

複数のストアを接続した後、次の属性は、ストアごとの値と集計値を含む階層化オブジェクトとして同期されます。
- `shopify_tags`
- `shopify_order_count` (履歴バックフィル経由でのみ使用可能)
- `shopify_total_spent` (履歴バックフィル経由でのみ使用可能)

セグメントの作成または編集時にカスタムイベントを使用するには、[**階層化カスタム属性**] フィルターを選択し、階層化属性を見つけます。オブジェクト内の特定のパスまたはフィールドを特定するには、[[スキーマの生成]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#generate-schema)] ツールを使用します。階層化属性を選択すると、選択した属性の横にプラスボタンの付いたフィールドが表示され、パスを指定できます。階層化属性の詳細については、[階層化カスタム属性]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/) を参照してください。

![3]{:style="max-width:70%;"}

パスを指定するには、フィールドに入力するか、「+」ボタンをクリックしてパスを選択します。

![4]{:style="max-width:70%;"}

### Shopify カスタムイベントs

複数のストアを接続すると、新たな Shopifyカスタムイベントに新しいイベントプロパティ `shopify_storefront` が含まれるようになります。[Shopifyデータプロセッシング]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events)を参照して、このインテグレーションでサポートされるすべてのカスタムイベントを確認してください。このイベントプロパティは、イベントの送信元のShopifyストアドメインを提供します。

### アクションベースの配信またはコンバージョントラッキング

特定のストアでアクションを完了したユーザーにメッセージングをトリガーするには、以下を実行します。

1. キャンペーンの**Schedule Delivery** ステップに移動します。
2. トリガーとして**カスタムイベントを実行**を選択します。
![5]{:style="max-width:70%;"}
3. トリガーイベントとして Shopify イベントを選択します ([**shopify_created_order**]、[**プロパティフィルターの追加**] チェックボックスなど)。
![6]{:style="max-width:70%;"}
4. **Add Filter**ドロップダウンで**Basic Property**を選択します。
5. **Shopify_storefront**を選択し、ストアのフルShopify領域を入力します。
![7]{:style="max-width:70%;"}


### Shopify ユーザーのマージと同期

エイリアス、{% raw %}`shopify_customer_id_{{storefront_domain}}`、`shopify_email`、または`shopify_phone`、{% endraw %} を使用して、ユーザーのShopify 顧客 ID、メールアドレス、または電話番号がすでにBraze内に存在する場合は、既存のユーザープロファイルを更新します。これらの別名がBraze内に存在しない場合は、新しいユーザープロファイルを作成します。ユーザーのデータ(都市など)は、同じユーザーの複数のShopifyストア間で異なることがあります。このような場合、Braze は、最新のアクティビティを持つストアからユーザープロファイルを必ず更新します。 

{% alert warning %}
Braze は、最新のアクティビティを持つストアからShopify 顧客データを持つユーザープロファイルを更新します。つまり、メール、電話番号、送信元の電話番号、都市などの属性は、最新のストアアクティビティで上書きできます。たとえば、ユーザーが2つの別のストアに別の電話番号を持っている場合、Brazeは、最新のアクティビティを持つストアの電話番号でユーザープロファイルを更新します。
{% endalert %}

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
[3]: {% image_buster /assets/img/shopify_nested_attributes.png %}
[4]: {% image_buster /assets/img/shopify_tags.png %}
[5]: {% image_buster /assets/img/shopify_add_trigger.png %}
[6]: {% image_buster /assets/img/shopify_select_event.png %}
[7]: {% image_buster /assets/img/shopify_enter_storefront.png %}
