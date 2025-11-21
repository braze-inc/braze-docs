---
nav_title: 複数のビジネスアカウント
article_title: 複数のWhatsAppビジネスアカウントと電話番号
page_order: 2
description: "この参考記事ではWhatsApp Businessアカウントと電話番号を追加する手順を説明する。"
page_type: reference
channel:
  - WhatsApp
---

# 複数のWhatsApp Businessアカウントと電話番号

> 各ワークスペースに複数のWhatsApp Businessアカウントとサブスクリプショングループ（および電話番号）を追加できる。<br><br>各サブスクリプショングループは1つの固有の電話番号に接続されるため、同じ電話番号を複数のサブスクリプショングループに接続したり、複数の電話番号を1つのサブスクリプショングループに接続したりすることはできない。

## 複数のWhatsAppビジネスアカウント 

複数のブランドを持つ Braze ワークスペースのユーザーに WhatsApp メッセージを送信する場合、複数の WhatsApp Business アカウントを使用すると便利です。各ビジネスアカウントはWhatsApp内で個別に運営され、独自の電話番号、メッセージテンプレート、品質評価を持っているからだ。

同じ Meta Business Manager 内にネストされているビジネスアカウントは、ユーザーアクセス権限管理とカタログも共有します (Brazeではまだサポートされていません)。

]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %})ワークスペースとWhatsApp Businessアカウントの相互接続を示す、Braze と WhatsApp のエコシステム図: 1 つの購読グループを 1 つの電話番号に、複数の WhatsApp Business アカウントを 1 つのワークスペースに、1 つのワークスペースを複数の Meta Business ポートフォリオに接続できる。 

### WhatsApp Businessアカウントを追加する

1 つのワークスペースにつき WhatsApp Business アカウントを 10 個まで追加できます。ビジネスアカウントは異なる Meta Business Manager にネストできます。アカウントを追加する：

1. [**テクノロジーパートナー**] > [**WhatsApp**] に移動して [**WhatsApp ビジネスアカウントを追加**] を選択します。 

![WhatsApp Messaging Integrationセクションでビジネスアカウントの追加、サブスクリプショングループと電話番号の追加ができる。]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\.サインアップのワークフローを実行します。ステップごとの詳しいガイドは、[WhatsApp 埋め込みサインアップ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)を参照してください。

{% alert important %}
他のWhatsAppアカウントに登録されていないなど、WhatsApp電話番号に必要な条件を全て満たしていること。
{% endalert %}

## 複数の購読グループと電話番号

メッセージテンプレートは同じ WhatsApp Business アカウント内のすべての電話番号で共有されます。WhatsAppサブスクリプショングループの詳細は[サブスクリプショングループを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)ご覧下さい。

WhatsAppの各電話番号は、ユーザーには個別のWhatsAppチャットとして表示される。WhatsApp Businessアカウント内の電話番号はそれぞれ独立しているため、以下のように同じ値を設定することも、異なる値を設定することもできる： 
- 表示名 
- ステータス 
- 品質評価 
- メッセージング制限 

### 購読グループと電話番号の追加

WhatsApp Business アカウントごとに最大 20 の購読グループ (および送信電話番号) を追加できます。購読グループと電話番号を追加するには:

1. [**テクノロジーパートナー**] > [**WhatsApp**] に移動して [**購読グループと番号を追加**] を選択します。

![WhatsApp Messaging Integrationセクションでビジネスアカウントの追加、サブスクリプショングループと電話番号の追加ができる。]({% image_buster /assets/img/whatsapp/multiple_wabas.png %})

{: start="2"}
2\.サインアップのワークフローを実行します。<br><br> **WhatsApp Businessアカウントを選択**"ステップで既存のWhatsApp Businessアカウントを選択し、新しい電話番号を追加する。この電話番号は、他のWhatsAppアカウントに登録されていないなど、WhatsApp電話番号の全ての条件を満たしている必要がある。

### 購読グループと電話番号の削除 

1. [**オーディエンス**] > [**購読**] に移動し、購読グループをアーカイブします。
2. Meta Business Manager に移動して電話番号を削除します。
