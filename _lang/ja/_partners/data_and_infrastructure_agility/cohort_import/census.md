---
nav_title: Census
article_title: Census のコホートインポート
description: "このリファレンス記事は、クラウドウェアハウスのデータを使用してターゲットユーザーセグメントを動的に作成できるデータ統合プラットフォームであるCensusのコホートインポート機能を概説しています。"
page_type: partner
search_tag: Partner

---

# Census のコホートインポート

> この記事では、ユーザーコホートを[Census][1]からBrazeにインポートする方法について説明します。詳細については、[Census のメイン記事]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/census/)を参照してください。

## コホートインポート統合

### ステップ1:Brazeサービス接続を作成する

Census プラットフォームで Census を統合するには、[**Connections**] タブに移動し、[**New Destination**] を選択して新しい Braze サービス接続を作成します。

表示されるプロンプトで、この接続に名前を付け、BrazeエンドポイントURL、Braze REST APIキー、およびデータインポートキーを提供します。データインポートキーはコホートを同期するために必要であり、**パートナー統合** > **テクノロジーパートナー** > **Census**に移動することでBrazeで見つけることができます。

![][8]{: style="max-width:60%;"}

### ステップ2:国勢調査の同期を作成する

顧客を Braze に同期するには、同期を作成する必要があります。ここで、データを同期する場所と、2つのプラットフォーム間でどのようにフィールドをマッピングするかを定義する。

1. [**Syncs**] タブに移動し、[**New Sync**] を選択します。<br><br> 
2. コンポーザーで、データウェアハウスからソースデータモデルを選択します。<br><br>
3. モデルが同期される場所を設定します。**Braze**を送信先として選択し、**ユーザー & コホート**を同期するオブジェクトとして選択します。<br>![[Select a Destination] プロンプトで接続として「Braze」が選択されており、さまざまなオプションが一覧表示されている。][10]{: style="max-width:80%;"}<br><br>
4. **ソース列**を選択して、コホートに追加するユーザーを識別し、**外部ユーザーID**を**識別子タイプ**として選択します。<br><br>
5. [**Cohort Name**] ドロップダウンでコホートを選択するか、コホートを作成するか、またはソース列を選択してコホート名を取り込みます。<br><br>
6. **ソースデータからレコードが削除されたとき**のドロップダウンを使用して、ソースデータセットから削除されたときにユーザーに何が起こるかを選択します。例えば、**何もしない**や**コホートから一致するレコードを削除する**などです。<br><br>
7. 最後に、Census データフィールドを対応する Braze フィールドにマッピングします。<br>![Census でのマッピング][11]{: style="max-width:80%;"}<br><br>
8. 詳細を確認して同期を作成します。 

これで同期を実行できます！

同期中にマッピングするフィールドは、最初にユーザーオブジェクトに同期され、既にBrazeに存在するものが更新されます。その後、更新されたユーザーは指定されたコホートに追加されます。

同期後、Brazeセグメントを作成し、Censusコホートフィルターを追加して、将来のBrazeキャンペーンやCanvasでそのユーザーをターゲットにすることができます。 

{% alert note %}
Census と Braze の統合を使用する場合、Census は Braze との同期のたびに差分 (変更データ) のみを送信します。
{% endalert %}

## ユーザーマッチング

識別されたユーザーは、`external_id` または`alias` のどちらかによって照合できます。匿名ユーザーは、`device_id` によって照合できます。元々匿名ユーザーとして作成された識別されたユーザーは、`device_id` では識別できず、`external_id` または`alias` で識別しなければなりません。

[1]: https://www.getcensus.com/
[8]: {% image_buster /assets/img/census/add_service.png %}
[10]: {% image_buster /assets/img/census/census_2.png %}
[11]: {% image_buster /assets/img/census/census_3.png %}