---
nav_title: ジュストゥーノ
article_title: ジュストゥーノ
description: "Justuno と Braze を統合する方法を学習することで、両方のプラットフォームにわたって顧客データを活用し、すべてのオーディエンスに対してよりパーソナライズされた経験を作成できます。"

alias: /partners/justuno
page_type: partner
search_tag: Partner
---

# ジュストゥーノ

> [Justuno](https://www.justuno.com/) を使用すると、すべてのユーザーに対して、動的セグメントを使用して完全に最適化されたビジターエクスペリエンスを作成できます。これにより、サイトの速度に影響を与えたり、開発作業を増加させたりすることなく、最先端のターゲット設定が可能になります。作成されたプロファイルの数、訪問者の収益率、セッションごとのページなどのカスタム分析を表示して、コンバージョン率を分析し、業界でマーケティング優位性を維持します。Justunoでは、訪問者1人当たりの収益を増やし、有意義な顧客エンゲージメントを確立し、ビジネスを成長させることができます。接続されたプラットフォームで、オーディエンス・ジャーニー全体をエンドツーエンドで最適化します。

## ユースケース

Braze では、どのマーケターも、任意のソースから任意の量のデータを収集し、処理することができます。そのため、1 つのプラットフォームからのチャネルをまたいで、リアルタイムで顧客と創造的に関わることができます。

「Justuno」と「Braze」を統合することで、両方の世界の中で最高のものが得られます。Brazeに保存されている顧客データと、Justunoに保存されている訪問者および顧客データを組み合わせて、すべてのオーディエンスに対してよりパーソナライズされた体験を作成できます。これにより、マーケティングキャンペーンと顧客エンゲージメントの効果が向上します。

## 前提条件

| Braze Rest API キー| `users.track` および`custom_attributes.get` 権限を持つBraze REST API キー。<br><br>これは、**Settings** > **API Keys**.| からBraze ダッシュボードで作成できます。
| Raze REST エンドポイント| REST エンドポイントURL。エンドポイントは、インスタンスの[ブレーズURL に依存します]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints).|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Justunoとブレーズの統合

### ステップ1:ブレーズでカスタム属性を作成する

Justuno から Braze にユーザー属性を同期するには、Braze でそれらの属性を作成する必要があります(まだ作成していない場合)。**Data Settings**> **Custom Attributes**に移動し、カスタム属性を作成することで、これを行うことができます。完全なウォークスルーについては、[ブレーズ]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/)のカスタム属性の管理を参照してください。

### ステップ2: Braze アプリを Justuno に追加する

#### ステップ 2.1:アカウントに追加する

Braze アプリを Justuno アカウントに追加するには、** Account Settings** > **Apps** に移動し、Braze アプリを検索して選択します。

!["Connect Apps" ページ(検索結果のリストに表示されるBraze アプリを含むJustuno)。]({% image_buster /assets/img/justuno/search-for-braze.png %})

API キーとベースURL [以前に作成した](#prerequisites)を入力し、**Connect**を選択します。

![Braze API キーとベースURL を尋ねるBraze Authentication ポップアップウィンドウ。]({% image_buster /assets/img/justuno/authenticate-braze.png %}){: style="max-width:75%;"}

#### ステップ 2.2:ワークフローに追加する

Braze アプリを[Justuno ワークフロー](https://hub.justuno.com/knowledge/workflows-overview) に追加するには、**アプリ** アクションをワークフローにドラッグアンドドロップし、**Select App** > **Braze** を選択します。

!["Select App"オプションは"Sync to App" action.]({% image_buster /assets/img/justuno/select-app.png %})にあります。{: style="max-width:45%;"}

### ステップ 3:Braze サブスクリプショングループを接続する

Justuno から特定の Braze メールまたは SMS サブスクリプショングループにプロファイルデータを送信するには、Justuno ワークフローの Braze アプリに ID を追加する必要があります。

| IDタイプ                          | 必要か？ | 説明                                                                                                   |
|----------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| ブレーズSMSサブスクリプショングループID  | はい       | このID は、ユーザプロファイルからSMS 同意を収集するために使用されます。Justuno にID が入力されていない場合、Justuno がそのプロファイルをBraze にプッシュすると、プロファイルは同意されません。 |
| Braze EメールサブスクリプショングループID | いいえ        | このID がJustuno に入力されていない場合、Justuno はプロファイルデータを関連付けられたサブスクリプショングループを持たないユーザとしてBraze に送信します。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### ステップ 3.1:ブレーズでID を見つける

Braze ダッシュボードでこれらのID を見つけるには:

1. [**オーディエンス**] > [**購読**] に移動します。
2. サブスクリプショングループごとに、ID 列にあるID を書き留めます。

#### ステップ 3.2:Braze アプリにID を追加する

Justuno ワークフローで、Braze アプリを開き、各サブスクリプショングループのID を入力します。

![E メールおよび SMS サブスクリプショングループ ID を追加するオプションを指定して、Justuno ワークフローで開かれた Braze アプリ。]({% image_buster /assets/img/justuno/enter-subscription-groups.png %}){: style="max-width:55%;"}

### ステップ4:属性の設定

以下の属性は、Justuno からBraze に自動的に同期されます。

- メール  
- 電話  
- 名  
- 姓  
- 言語  
- 性別  
- 国

追加の属性を同期するには:

1. ワークフロー内のブレーズアプリで、**Sync Another Property** を選択します。
    ![Braze アプリがJustuno ワークフローで開き、"Sync Another Property" option.]({% image_buster /assets/img/justuno/sync-another-property.png %}) を表示します。{: style="max-width:55%;"}
2. 同期するブレーズ属性を選択します。
3. JustunoのプロパティとBrazeの同等物(ソーシャルハンドル、誕生日、ショッピングの好み、アンケートの回答など)を一致させます。これらのプロパティは、0 パーティデータまたは1 番目のパーティデータと見なされます。詳細については、[Justuno を参照してください。訪問者データ収集](https://www.justuno.com/guides/zero-first-party-data/)。
4. ワークフロービルダーで、**Save**、**Preview**、または**Publish** ワークフローを選択します。
    !["Publish"メニューが開き、保存、プレビュー、またはバージョン履歴を表示します。]({% image_buster /assets/img/justuno/publish-workflow.png %}){: style="max-width:45%;"}

## 知っておくべきこと

- アプリ設定でサブスクリプショングループID を手動で入力する必要があります。  
- 次のブレーズデータタイプは、**not supported** です。オブジェクト、オブジェクト配列。  
- JustunoのSMS同意フィールドが使用されていない場合、暗黙的なSMS同意が提供されます。  
- Justunoデザインに同意フィールドが含まれている場合、明示的なSMS同意が尊重されます。
