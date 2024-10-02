---
nav_title: グルーパルー
page_order: 1
description: "この記事では、BrazeとGrouparooのパートナーシップについて概説している。GrouparooはオープンソースのリバースETLツールで、データウェアハウスのデータを使ってマーケティング、セールス、サポートの各ツールに簡単にパワーを与えることができる。"
page_type: update

---

# グルーパルー

{% alert update %}
Grouparooのサポートは2022年4月をもって終了した。
{% endalert %}

> [Grouparooは][1]オープンソースのリバースETLツールで、倉庫内のデータを使ってマーケティング、セールス、サポートツールを簡単にパワーアップできる。設定はモデル中心のUIで行われるため、技術者でないチームメンバーでも、運用をサポートするためのデータ同期の設定やスケジュールを立てることができる。

BrazeとGrouparooの統合により、倉庫に保存されているデータをBrazeに送信することで、簡単に運用することができる。自動同期のスケジュールを設定すれば、常に最新の情報で顧客とのコミュニケーションを強化できる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Grouparooのアカウントとプロジェクト | このパートナーシップを利用するには、Grouparooアカウントとプロジェクトが必要である。<br><br>この統合は、Grouparooが提供する無料のコミュニティ版と企業向けソリューションで使用することができる。セットアップはGrouparooコンフィギュレーション・ユーザーインターフェイスで行われる。 |
| Braze REST API キー | ユーザーとトラック権限を持つBraze REST APIキー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][1]。エンドポイントは、インスタンスのBraze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ 1:GrouparooでBrazeアプリを作成する

Grouparooで**Appsに**移動し、**Brazeを**選択して新しいBrazeアプリを作成する。表示されたモーダルで、Braze APIキーとRESTエンドポイントを入力する。

![][2]

### ステップ2:モデルとデータソースをセットアップする

この統合では、次のステップに進む前に、既存のモデルとデータソースをセットアップしておく必要がある。この設定がない場合は、Grouparoo ドキュメントにアクセスして、[model](https://www.grouparoo.com/docs/config/models) および[データソース](https://www.grouparoo.com/docs/config/sources) の設定方法を確認してください。

### ステップ 3:GrouparooでBrazeの目的地を作成する

#### 同期モードを選択する

Grouparooで、ナビゲーションバーからモデルを選択する。次に、**Destinations**セクションまでスクロールし、**Add new Destinationを**クリックする。

次に、作成した**Braze**アプリを選択し、保存先に名前を付け、希望の同期モードを以下から選択する：
- **同期する**：必要に応じてBrazeユーザーを追加、更新、削除する。このオプションは、新規レコード、既存レコードの変更、および削除を検索する。
- **添加物**だ：必要に応じてBrazeユーザーを追加・更新するが、誰も削除しないこと。このオプションは、Brazeに追加する新規ユーザーと既存のBrazeユーザーの変更を探すが、削除は追跡しない。
- **豊かにする**：Brazeにすでに存在するユーザーのみをアップデートする。ユーザを追加または削除しない。このオプションは、Brazeの既存ユーザーのみを更新する。

#### プロパティ・フィールドのマッピング

次に、Grouparooのプロパティ・フィールドをBrazeのプロパティ・フィールドにマッピングする必要がある。 

![プロパティのマッピングフィールドの例。grouparooのuserIDはexternal_idにマップされるように設定される。email、firstName、lastNameは同等の "email"、"first_name"、"last_name "grouparooフィールドとして設定される。][3]{: style="max-width:80%;"}

Braze`external_id` フィールドがソーステーブルの主キーにマッピングされていることを確認する。残りのフィールドは、ユースケースに応じてマッピングする。

**レコードプロパティセクションを送信する**：データをマップするために利用可能なプリセット・ユーザー・プロファイル・フィールドのリスト。これらのどれでもGrouparooのプロパティから同期させることができる。

**オプションのBraze User Profile Fields**セクション：オプションのカスタムBrazeユーザープロファイルフィールドを作成する。**Add New Braze User Profile Fieldを**クリックすると、Brazeにマッピングできるすべての利用可能なプロパティが表示される。新しく作成するフィールドの名前はGrouparooプロパティと同じになるが、名前を変更することができる。

#### Grouparooグループ

マッピングだけでなく、GrouparooグループをBrazeサブスクリプショングループに追加することもできる。 

![Grouparoo宛先設定ウィンドウの "Braze Subscription Groups "で、"High value with recent automotive purchase "Grouparooグループが "High value with recent automotive purchase "Brazeサブスクリプショングループに追加される。][4]{: style="max-width:80%;"}

{% alert important %}
この統合に関する詳細と最新情報は[Grouparooのドキュメントを](https://www.grouparoo.com/docs/integrations/grouparoo-braze)参照されたい。
{% endalert %}

[1]: https://www.grouparoo.com/
[2]: {% image_buster /assets/img/grouparoo/add-app.png %}
[3]: {% image_buster /assets/img/grouparoo/mapping.png %}
[4]: {% image_buster /assets/img/grouparoo/lists.png %}