---
nav_title: Justuno
article_title: Justuno
description: "Justuno と Braze を統合して、両方のプラットフォームで顧客データを活用し、すべてのオーディエンスにパーソナライズされたエクスペリエンスを提供する方法について説明します。"

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# Justuno

> [Justuno](https://www.justuno.com/) では、ダイナミックなセグメントにより、すべてのオーディエンスに対して完全に最適化されたビジター体験を作成することができ、サイトの速度に影響を及ぼしたり、開発作業を増やすことなく、最も高度なターゲティングを利用できます。作成されたプロファイル数、再訪者の影響率、セッションあたりのページ数などのカスタム分析を表示して、コンバージョン率を分析し、業界でのマーケティングの優位性を維持できるようにします。Justuno は、訪問者当たりの売上を増やし、有意義なカスタマーエンゲージメントを確立し、ビジネスを成長させることができます。接続されたプラットフォームで、オーディエンスジャーニー全体をエンドツーエンドで最適化します。

## ユースケース

Braze では、あらゆるマーケターがあらゆるデータソースからあらゆる量のデータを収集し、対処することができるため、1 つのプラットフォームから様々なチャネルでリアルタイムでクリエイティブに顧客とのエンゲージメントを進めることができます。

Justuno と Braze を統合することで、両方の長所を生かすことができます。Braze に保存されたカスタマーデータと Justuno に保存されたビジターデータや顧客データを組み合わせることで、すべてのオーディエンスに対してよりパーソナライズされたエクスペリエンスを提供することができます。これにより、マーケティングキャンペーンやカスタマーエンゲージメントの効果を上げることができます。

## 前提条件

| Braze Rest APIキー｜`users.track` および`custom_attributes.get` の権限がある Braze REST API キー。<br><br>これは Braze のダッシュボードで [**設定**] > [**API キー**] から作成できます。
| Braze RESTエンドポイント｜利用する REST エンドポイントの URL。エンドポイントは、[インスタンスの Braze URL]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) によって異なります。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Justuno と Braze の統合

### ステップ 1: Braze でカスタム属性を作成する

Justuno から Braze にユーザー属性を同期させるには、Braze で作成されていないユーザー属性を作成する必要があります。[**データ設定**] > [**カスタム属性**] と移動し、カスタム属性を作成することで、これを行うことができます。詳細なチュートリアルについては、[Braze のカスタム属性の管理]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)を参照してください。

### ステップ2: Braze アプリを Justuno に追加する

#### ステップ 2.1: アカウントに追加する

Justuno アカウントに Braze アプリを追加するには、[**Account Settings**] > [**Apps**] と移動し、Braze アプリを検索して選択します。

![Brazeアプリが検索結果のリストに表示されたJustunoの「Connect Apps」ページ。]({% image_buster /assets/img/justuno/search-for-braze.png %})

[すでに作成済みの](#prerequisites) API キーとベース URL を入力し、[**Connect**] を選択します。

![Braze APIキーとベースURLを求めるBraze認証ポップアップウィンドウ。]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### ステップ 2.2:ワークフローに追加する

Braze アプリを [Justuno ワークフロー](https://hub.justuno.com/knowledge/workflows-overview) に追加するには、**Sync to App** アクションをワークフローにドラッグ＆ドロップし、[**Select App**] > [**Braze**] の順に選択します。

![アプリに同期 "アクションにある "アプリを選択 "オプション。]({% image_buster /assets/img/justuno/select-app.png %}){: style="max-width:45%;"}

### ステップ 3:Braze 購読グループを接続する

Justuno から特定の Braze メールまたは SMS 購読グループにプロファイルデータを送信するには、Justuno ワークフローで Braze アプリにその ID を追加する必要があります。

| ID タイプ                          | 必要か？ | 説明                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| Braze SMS 購読グループ ID  | はい       | このID は、ユーザープロファイルからの SMS の同意の収集に使用されます。Justuno に ID が入力されていない場合、Justuno がそのプロファイルを Braze にプッシュしたときにプロファイルへの同意がないことになります。 |
| Braze のメール購読グループ ID | いいえ        | Justuno にこの ID が入力されていない場合、購読グループの関連付けがないユーザーとして Justuno から Braze にプロファイルデータが送信されます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### ステップ 3.1: Braze で ID を見つける

Braze ダッシュボードで必要な ID を見つけます。

1. [**オーディエンス**] > [**購読**] に移動します。
2. ID 列にある各購読グループの ID を書き留めておきますます。

#### ステップ 3.2: Braze アプリに ID を追加する

Justuno ワークフローで Braze アプリを開き、各購読グループの ID を入力します。

![BrazeアプリはJustunoワークフローで開封され、メールとSMSサブスクリプショングループIDを追加するオプションがある。]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### ステップ 4: 属性の設定

以下の属性は、自動的に Justuno から Braze への同期が行われます。

- メール  
- 電話  
- 名  
- 姓  
- 言語  
- 性別  
- 国

同期する属性を追加する

1. ワークフロー内の Braze アプリで、[**Sync Another Property**] を選択します。
    ![BrazeアプリがJustunoワークフローで開封され、「別のプロパティを同期」オプションが表示された。]({% image_buster /assets/img/justuno/sync-another-property.png %}){: style="max-width:55%;"}
2. 同期する Braze の属性を選択します。
3. Justuno のプロパティと相当する Braze のプロパティをマッチングします (ソーシャルハンドル、誕生日、ショッピングの好み、アンケートの回答など）。これらのプロパティは、0 パーティデータまたはファーストパーティデータと見なされます。詳細については、[Justuno: Visitor data collection](https://www.justuno.com/guides/zero-first-party-data/) を参照してください。
4. ワークフロービルダーで、ワークフローの [**Save**]、[**Preview**]、[**Publish**] を選択します。
    ![Publish」メニューが開封され、保存、プレビュー、バージョン履歴の表示のオプションが表示された。]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## 知っておくべきこと

- アプリ設定で購読グループ ID を手動で入力する必要があります。  
- 次の Braze データ型には**対応していません**。オブジェクト、オブジェクト配列。  
- Justuno の SMS 同意フィールドが使用されていない場合、SMSの同意が暗黙的に提供されます。  
- Justuno のデザインに同意フィールドが含まれている場合は、明示的な SMS 同意が考慮されます。
