---
nav_title: レムニスク
article_title: レムニスクとBrazeの統合
description: "この参考記事では、BrazeとAIを活用した顧客データプラットフォーム主導のマーケティングオートメーションプラットフォームであるLemniskとの提携について詳しく解説しており、Lemniskで収集したユーザーデータを様々なソースからBrazeに流し、Brazeのツールを使って様々なチャネルや送信先で活性化させることができる。"
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# レムニスク

> [レムニスクは](https://www.lemnisk.co/)、AIを活用した顧客データプラットフォーム（CDP）およびマーケティングオートメーションソリューションで、サイロ化した多様なソースから顧客データをリアルタイムに収集、統合、活性化できる。顧客データのライフサイクルの各段階を追跡する堅牢なリアルタイム分析を提供しながら、この統合データをさまざまなMarTechおよびビジネスプラットフォームにシームレスに配信する。 

_この統合はレムニスクによって維持されている。_

## 統合について

LemniskとBrazeの統合により、ブランドや企業は、リアルタイムでプラットフォーム間のユーザーデータを統合し、収集したユーザーの情報や行動をリアルタイムでBrazeに送信するCDP主導のインテリジェントレイヤーとして機能することで、Brazeの可能性を最大限に引き出すことができる。Lemniskは、より深いコンテキストでメッセージングをパーソナライズできるように、行動シグナルと個人属性をブレンドすることで、エンリッチされた顧客プロファイルを直接Brazeに提供する。

## 前提条件

| 必要条件 | 説明 |
| --- | --- |
| レムニスク口座 | このパートナーシップを利用するには、[レムニスクの](https://www.lemnisk.co/)アカウントが必要だ。 |
| レムニスクの外部API | レムニスクのカスタマーサクセスマネージャーに連絡して、アカウントの**外部APIを**イネーブルメントにする。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは、[アカウントのBraze URLに]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints#api-and-sdk-endpoints)依存する。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## レムニスクの統合

### ステップ 1: Braze外部APIを作成する {#create-a-braze-external-api}

Lemniskで、外部APIチャネルに行く。**Add New External APIを**選択する。[Track Users]({{site.baseurl}}/api/endpoints/user_data/post_user_track)エンドポイントを外部APIとして設定する。

![Lemniskで外部API作成プロセスを開始する]({% image_buster /assets/img/lemnisk/open_external_api.png %})

**基本的な詳細**」で、名前、説明、チャネル、チャネル識別子を入力する。

![Lemniskで新しい外部APIの基本設定の詳細を入力する]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

**External API details（外部APIの詳細**）]で、`users.track` エンドポイントの関連する詳細を入力する。{% raw %}`{{}}`{% endraw %} を使って複数のエンゲージメント・レベルのフィールドを定義することができ、キャンペーンごとに異なる値を設定できる。

![外部APIエンドポイントとペイロードの詳細を記入する]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

Track Usersの設定を終了するには、**Saveを**選択する。自動的に**Test API**ページにリダイレクトされる。

### ステップ 2:設定をテストする

**Test API**ページで、JSONツリービューにAPIパラメータのテスト値を入力し、**Test Configurationを**選択する。

認証情報とAPI定義が正しければ、Brazeは成功のレスポンスを返す。

![ペイロードと成功レスポンスのサンプルを使って外部API設定をテストする]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

次に、イベントがBrazeに正常に送信されていることを確認する。Brazeダッシュボードで、**オーディエンス**>**ユーザーを検索に**進み、外部API設定から識別子の1つ（ユーザーメール・アドレスなど）を入力する。すべてが正しく機能していれば、テストAPIトリガーを受け取ったプロファイルがリストアップされる。

![Brazeでユーザープロファイルとアクティビティ概要を表示する。]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### ステップ 3:Brazeでユーザーイベントをトリガーする

1. レムニスクで新しいセグメンテーションを作成する。例えば、ユーザーがリードフォームを送信すると同時に、Brazeに情報を送信するセグメンテーションを作成することができる。
2. 新しいセグメンテーションで、**External API**>**Add Engagementと**進む。
3. **エンゲージメントの作成**」で、基本的な詳細を入力し、[以前に作成した](#create-a-braze-external-api)コンフィギュレーションを選択する。
4. **Configure Parametersの**下に、エンゲージメントレベルで公開することにしたBrazeパラメーターの入力がある。以下の例では、_ユーザー名_、_製品ID_、_イベント時間が_表示されている。
    ![ユーザーデータをBrazeに送信するエンゲージメントを作成する]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. 選択したパラメータに関連するパーソナライゼーション変数を入力し、**Saveを**選択する。
6. 終わったら、エンゲージメントを有効にする。
