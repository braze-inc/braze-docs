---
nav_title: Grouparoo
page_order: 1
description: "この記事では、BrazeとGrouparooのパートナーシップについて概説している。GrouparooはオープンソースのリバースETLツールで、データウェアハウスのデータを使ってマーケティング、セールス、サポートの各ツールに簡単にパワーを与えることができる。"
page_type: update

---

# Grouparoo

{% alert update %}
Grouparoo のサポートは、2022年4月に終了しました。
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/)は、開封ソースのリバースETLツールで、倉庫内のデータを使用してマーケティング、販売、サポートツールに簡単に電力を供給します。設定はモデル中心のUIで行われるため、技術者でないチームメンバーでも、運用をサポートするためのデータ同期の設定やスケジュールを立てることができる。

BrazeとGrouparooの統合により、倉庫に保存されているデータをBrazeに送信することで、簡単に運用することができる。自動同期スケジュールを設定すると、最新の情報により顧客とのコミュニケーションを一貫して強化できます。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Grouparooのアカウントとプロジェクト | このパートナーシップを利用するには、Grouparooアカウントとプロジェクトが必要である。<br><br>この統合は、Grouparooが提供する無料のコミュニティーエディションおよびエンタープライズソリューションで使用できます。セットアップはGrouparooコンフィギュレーション・ユーザーインターフェイスで行われる。 |
| Braze REST API キー | ユーザーとトラック権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze REST エンドポイント | [あなたのRESTエンドポイントURL](https://www.grouparoo.com/)。お客様のエンドポイントは、お客様のインスタンスのBraze URLに依存します。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ 1:GrouparooでBrazeアプリを作成する

Grouparoo で、[**Apps**] に移動し、[**Braze**] を選択して新しいBraze アプリを作成します。表示されたモーダルで、Braze APIキーとRESTエンドポイントを入力する。

![]({% image_buster /assets/img/grouparoo/add-app.png %})

### ステップ2:モデルとデータソースをセットアップする

この統合では、次のステップに進む前に、既存のモデルとデータソースをセットアップしておく必要がある。この設定がない場合は、Grouparoo ドキュメントにアクセスして、[model](https://www.grouparoo.com/docs/config/models) および[データソース](https://www.grouparoo.com/docs/config/sources) の設定方法を確認してください。

### ステップ 3:GrouparooでBrazeの目的地を作成する

#### 同期モードを選択する

Grouparooで、ナビゲーションバーからモデルを選択する。次に、**Destinations**セクションまでスクロールし、**Add new Destination**をクリックします。

次に、作成した**Braze**アプリを選択し、保存先に名前を付け、希望の同期モードを以下から選択する：
- **同期**:必要に応じてBrazeユーザーを追加、更新、削除する。このオプションでは、新しいレコード、既存レコードの変更、および削除を検索します。
- **Additive**: 必要に応じてBrazeユーザーを追加・更新するが、誰も削除しないこと。このオプションは、Brazeに追加する新規ユーザーと既存のBrazeユーザーの変更を探すが、削除は追跡しない。
- **Enrich**: Brazeにすでに存在するユーザーのみをアップデートする。ユーザを追加または削除しない。このオプションは、Brazeの既存ユーザーのみを更新する。

#### プロパティ・フィールドのマッピング

次に、Grouparooのプロパティ・フィールドをBrazeのプロパティ・フィールドにマッピングする必要がある。 

![プロパティのマッピングフィールドの例。Grouparoo の userID は external_id にマッピングされるように設定されます。email、firstName、lastName は対応する grouparoo フィールドである「email」、「first_name」、「last_name」として設定されます。]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Braze`external_id` フィールドがソーステーブルの主キーにマッピングされていることを確認する。ユースケースでの必要に応じて、残りのフィールドをマッピングします。

[**Send Record Properties**] セクション:データのマッピングに使用できるプリセットユーザープロファイルフィールドのリスト。これらのいずれかをGrouparoo プロパティから同期できます。

**Optional Braze User Profile Fields**セクション:オプションのカスタムBrazeユーザープロファイルフィールドを作成する。[**Add New Braze User Profile Field**] を選択すると、Braze にマッピングできるすべてのプロパティが表示されます。新しく作成するフィールドの名前はGrouparooプロパティと同じになるが、名前を変更することができる。

#### Grouparooグループ

マッピングに加えて、Grouparoo グループを Braze 購読グループに追加することもできます。 

![Grouparoo の送信先設定ウィンドウの「Braze 購読グループ」で、「High value with recent automotive purchase (最近の自動車購入による高価値)」Grouparoo グループが「High value with recent automotive purchase (最近の自動車購入による高価値)」Braze 購読グループに追加されます。]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
この統合に関する詳細および更新は、[Grouparooのドキュメント](https://www.grouparoo.com/docs/integrations/grouparoo-braze)にあります。
{% endalert %}

