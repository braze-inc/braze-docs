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

複数のブランドが存在するBrazeワークスペースのユーザーにWhatsAppメッセージを送信する場合、複数のWhatsApp Businessアカウントを持つことが有効である。各ビジネスアカウントはWhatsApp内で個別に運営され、独自の電話番号、メッセージテンプレート、品質評価を持っているからだ。

同じMeta Business Manager内にネストされたビジネスアカウントは、ユーザーアクセス権限管理とカタログも共有する（Brazeではまだサポートされていない）。

### WhatsApp Businessアカウントを追加する

1ワークスペースにつきWhatsApp Businessアカウントを10個まで追加できる。アカウントを追加する：

1. **テクノロジーパートナー**>**WhatsAppの**順に選択し、**WhatsAppビジネスアカウントを追加する**。![WhatsAppメッセージングインテグレーションセクションでは、ビジネスアカウントの追加、購読グループと番号の追加ができる。][1]<br>
2. サインアップのワークフローに従う。ステップバイステップの詳しい説明は、[WhatsApp埋め込みサインアップを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/embedded_signup/)参照のこと。

{% alert important %}
他のWhatsAppアカウントに登録されていないなど、WhatsApp電話番号に必要な条件を全て満たしていること。
{% endalert %}

## 複数の契約グループと電話番号

メッセージテンプレートはWhatsApp Businessアカウント内の全ての電話番号で共有される。WhatsAppサブスクリプショングループの詳細は[サブスクリプショングループを]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/)ご覧下さい。

WhatsAppの各電話番号は、ユーザーには個別のWhatsAppチャットとして表示される。WhatsApp Businessアカウント内の電話番号はそれぞれ独立しているため、以下のように同じ値を設定することも、異なる値を設定することもできる： 
- 表示名 
- ステータス 
- 品質評価 
- メッセージ送信制限 

### 購読グループと電話番号を追加する

WhatsApp Businessアカウント1つにつき、最大20のサブスクリプショングループ(および送信電話番号)を追加できる。購読グループと電話番号を追加するには

1. **テクノロジーパートナー** > **WhatsApp** に移動し、**サブスクリプショングループと番号を追加** を選択します。![WhatsApp メッセージング統合セクションには、ビジネスアカウントを追加するか、サブスクリプショングループと番号を追加するオプションがあります。][1]<br>
2. サインアップのワークフローに従う。<br><br> **WhatsApp Businessアカウントを選択**"ステップで既存のWhatsApp Businessアカウントを選択し、新しい電話番号を追加する。この電話番号は、他のWhatsAppアカウントに登録されていないなど、WhatsApp電話番号の全ての条件を満たしている必要がある。

### 購読グループと電話番号を削除する 

1. **Audience**>**Subscriptionsに**移動し、購読グループをアーカイブする。
2. メタビジネスマネージャーに行き、電話番号を削除する。

[1]: {% image_buster /assets/img/whatsapp/multiple_wabas.png %} 
