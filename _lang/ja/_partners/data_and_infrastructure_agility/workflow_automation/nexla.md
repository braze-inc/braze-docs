---
nav_title: ネクスラ
article_title: ネクスラ
description: "この参考記事では、BrazeとNexlaのパートナーシップについて概説している。Nexlaは統合データ運用プラットフォームであり、Braze Currentsのユーザーはデータレイクデータを抽出、変換し、カスタムフォーマットで他の場所にロードすることができる。"
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# ネクスラ

> [ネクスラは](https://www.nexla.com)ユニファイド・データ・オペレーションのリーダーであり、2021年ガートナー・クールベンダーに選ばれている。Nexlaプラットフォームは、誰でも簡単にスケーラブルなデータフローを作成することができ、ビジネスチームとデータチームに摩擦のないガバメントされたデータオペレーション、より良いコラボレーション、俊敏性を提供する。データを扱うチームは、あらゆるユースケースに対応したデータの統合、変換、プロビジョニング、監視を、ノー／ローコードで統一されたエクスペリエンスで行うことができる。 

BrazeとNexlaの統合により、[Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/)使用している顧客は、Nexlaを活用してデータレイクデータをカスタムフォーマットで他の場所に抽出、変換、ロードできるようになり、エコシステム全体でデータに簡単にアクセスできるようになる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| ネクスラアカウント | このパートナーシップを利用するには、\[ネクスラアカウント][2] ]が必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは、\[インスタンスのBraze URL][1] に依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

Nexlaのデータ・アズ・ア・プロダクトである[Nexsetsは](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information)、メタデータを気にすることなく、あらゆるフォーマットのデータを簡単に扱うことができる。Brazeとの間のデータフローをNexlaで設定する場合、コード不要のツールで簡単に数分で利用できる。データフローを宛先に設定した後、Nexlaはフローを監視し、任意のデータ量に拡張する。

## 統合

### ステップ1:ネクスラアカウントを作成する

まだネクスラのアカウントをお持ちでない方は、ネクスラの[ウェブサイトから](https://www.nexla.com)無料デモとトライアルを申し込むことができる。次に [www.dataops.nexla.io](https://www.dataops.nexla.io)にログオンし、新しい認証情報でサインオンする。

### ステップ2:ソースを追加する

#### Brazeをデータソースとする場合
1. Nexlaプラットフォームで、左ツールバーの「**フロー」>「新規フローの作成**」を選択する。
2. **Create New Sourceを**クリックし、Brazeコネクタを選択し、**Nextを**クリックする。 
3. **Add a New Credentialを**選択し、クレデンシャルに名前を付け、Braze APIキーとRESTエンドポイントを追加して、**Save**する。
4. 最後に、データを選択し、**Saveを**クリックする。 

Nexlaは、ソースのデータを検索し、変換またはデスティネーションに送信するための[Nexsetを](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information)生成する。

#### ブレーズが目的地なら

[Nexlaへのソースの接続については](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source)、Nexlaのドキュメントを参照のこと。

### ステップ3:トランスフォーム（オプション）

データに対してカスタム[変換を](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations)実行したい場合、またはNexlaのビルド済みコネクタを使用したい場合は、データセットの**変換**ボタンをクリックして変換ビルダーに入る。Transform Builderの使用方法は、[Nexlaのドキュメントに](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data)記載されている。

### ステップ4:宛先に送信する

デスティネーションにデータを送信するには、データセット上の「**デスティネーションに送信**」矢印をクリックし、Nexlaのデスティネーションコネクター、またはソースが異なる場合はBrazeのいずれかを選択する。認証情報を入力し、宛先オプションを設定し、**Saveを**クリックする。データは即座に、あなたが指定したフォーマットで、あなたが選んだ宛先に流れ始める。

## この統合を使う

一度フローがセットアップされれば、あとは何も必要ない。Nexlaはソースデータの変更に対応し、新しいデータへのスケーリングを行い、スキーマの変更やトリアージのためのエラーを通知する。トランスフォーム、ソース、デスティネーションを変更したい場合は、これらのオプションをクリックして変更すれば、Nexlaは即座にフローを更新する。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: https://www.nexla.com/get-demo