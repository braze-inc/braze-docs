---
nav_title: グルパルー
page_order: 1
description: "この記事では、データウェアハウスのデータを使用してマーケティング、セールス、サポートツールに簡単に電力を供給できるオープンソースのリバースETL ツールであるBraze とGrouparoo のパートナーシップについて説明します。"
page_type: update

---

# グルパルー

{% alert update %}
Grouparooのサポートは、2022年4月に廃止されました。
{% endalert %}

> [Grouparoo][1]はオープンソースのリバースETLツールで、倉庫内のデータを使用してマーケティング、販売、サポートツールを簡単に動かすことができます。設定は、モデル中心のUI で行われるため、非テクニカルチームメンバーは、オペレーションをサポートするデータ同期を設定およびスケジュールできます。

Braze とGrouparoo の統合により、Braze に送信することで、倉庫に保存されているデータを簡単に操作できるようになります。自動同期スケジュールを設定すると、最新の情報を使用して顧客とのコミュニケーションを一貫して強化できます。

## 前提条件

| 要件| 説明|
| ----------- | ----------- |
| Grouparooアカウントとプロジェクト| このパートナーシップを活用するには、Grouparooアカウントとプロジェクトが必要です。<br><br>この統合は、Grouparooが提供する無料のコミュニティエディションおよびエンタープライズソリューションで使用できます。設定は、Grouparoo 設定ユーザインタフェースで行われます。|
| Raze REST API キー| ユーザーとトラッキング権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys**.| からBraze ダッシュボードで作成できます。
| Raze REST エンドポイント| [Your REST エンドポイントURL][1]。エンドポイントは、インスタンスのBraze URL によって異なります。|
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1:Grouparoo でのブレーズアプリの作成

Grouparoo で、**Apps** に移動し、**Braze** を選択して新しいBraze アプリを作成します。表示されるモーダルで、Braze API キーとREST エンドポイントを指定します。

![][2]

### ステップ2:モデルとデータソースの設定

この統合では、次のステップに進む前に、既存のモデルとデータソースが設定されている必要があります。この設定がない場合は、Grouparoo のドキュメントを参照して、[model](https://www.grouparoo.com/docs/config/models) および[データソース](https://www.grouparoo.com/docs/config/sources) の設定方法を確認してください。

### ステップ3:Grouparoo でのブレーズ送信先の作成

#### 同期モードの選択

Grouparooで、ナビゲーションバーからモデルを選択します。次に、**Destinations**セクションまでスクロールし、**Add new Destination**をクリックします。

次に、作成した**Braze** アプリを選択し、宛先に名前を付け、次の中から目的の同期モードを選択します。
- **同期**:必要に応じて、ブレーズユーザーを追加、更新、および削除します。このオプションは、新しいレコード、既存のレコードへの変更、および削除を検索します。
- **加算**:必要に応じてブレーズユーザーを追加および更新しますが、誰も削除しないでください。このオプションは、ブレーズに追加する新規ユーザーと既存のブレーズユーザーの変更を検索しますが、削除の追跡は行いません。
- **Enrich**:Braze にすでに存在するユーザーのみを更新します。ユーザーを追加または削除しないでください。このオプションは、Braze の既存ユーザーのみを更新します。

#### プロパティフィールドのマッピング

次に、GrouparooプロパティフィールドをBrazeプロパティフィールドにマップする必要があります。 

![プロパティマッピングフィールドの例。Grouparoo userID は、external\_id にマップするように設定されています。email、firstName、lastName は、同等の"email"、"first\_name"、および"last\_name"grouparoo fields.][{: style="max-width:80%;"}

Braze `external_id` フィールドがソーステーブルのプライマリキーにマッピングされていることを確認します。ユースケースに応じて、残りのフィールドを必要に応じてマップします。

**レコードプロパティの送信**セクション:データのマッピングに使用できるプリセットユーザープロファイルフィールドのリスト。これらのいずれかをGrouparoo プロパティから同期できます。

**オプションのブレーズユーザープロファイルフィールド**セクション:オプションのカスタムブレーズユーザープロファイルフィールドを作成します。**Add New Braze User Profile Field**をクリックすると、Brazeにマッピングできるすべてのプロパティが表示されます。作成する新しいフィールドの名前は、Grouparoo プロパティと同じですが、名前を変更することができます。

#### Grouparooグループ

マッピングに加えて、GrouparooグループをBrazeサブスクリプショングループに追加することもできます。 

! [" Braze Subscription Groups" Grouparoo 宛先設定ウィンドウで、" 最近の自動車購入&quot で高い値; Grouparoo グループが&quot に追加されます; 最近の自動車購入&quot で高い値; Braze サブスクリプショングループ] [4]{: style="max-width:80%;"}

{% alert important %}
この統合に関する詳細および更新は、[Grouparooのドキュメント](https://www.grouparoo.com/docs/integrations/grouparoo-braze)にあります。
{% endalert %}

[1]: https://www.grouparoo.com/
[2]: {% image_buster /assets/img/grouparoo/add-app.png %}
[3]: {% image_buster /assets/img/grouparoo/mapping.png %}
[4]: {% image_buster /assets/img/grouparoo/lists.png %}