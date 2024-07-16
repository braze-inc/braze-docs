---
nav_title: Nexla
article_title:ネクスラ
description:"この参考記事では、Braze Currentsユーザーがデータレイクデータをカスタムフォーマットで他の場所に抽出、変換、読み込むことを可能にする統合データ運用プラットフォームであるBrazeとNexlaのパートナーシップについて概説している。"
alias: /partners/nexla/
page_type: partner
search_tag:Partner

---

# ネクスラ

> [ネクスラは](https://www.nexla.com)ユニファイド・データ・オペレーションのリーダーであり、2021年ガートナー・クールベンダーに選ばれている。Nexlaプラットフォームは、誰でも簡単にスケーラブルなデータフローを作成することができ、ビジネスチームとデータチームに摩擦のないガバメントされたデータオペレーション、より良いコラボレーション、アジリティを提供する。データを扱うチームは、あらゆるユースケースに対応したデータの統合、変換、プロビジョニング、監視を、コードなし／ローコードで統一されたエクスペリエンスで行うことができる。 

BrazeとNexlaの統合により、[Currentsを]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents/)使用している顧客は、Nexlaを活用してデータレイクデータをカスタムフォーマットで他の場所に抽出、変換、読み込むことができ、エコシステム全体でデータに簡単にアクセスできるようになる。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| ネクスラアカウント | このパートナーシップを利用するには、\[ネクスラアカウント][2] ]が必要である。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント  | RESTエンドポイントのURL。エンドポイントは\[インスタンスのBraze URL][1]]に依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

Nexlaのデータ・アズ・ア・プロダクトである[Nexsetsは](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information)、メタデータを気にすることなく、あらゆるフォーマットのデータを簡単に扱うことができる。BrazeとのデータフローをNexlaで設定する場合、コード不要のツールで簡単に数分で利用できる。データフローが送信先に設定されると、Nexlaはフローを監視し、任意のデータ量に拡張する。

## 統合

### ステップ1:ネクスラアカウントを作成する

まだネクスラのアカウントをお持ちでない方は、ネクスラの[Web](https://www.nexla.com)サイトで無料デモとトライアルを申し込む。次に、[www.dataops.nexla.io](https://www.dataops.nexla.io)にログオンし、新しい認証情報でサインオンする。

### ステップ2:ソースを追加する

#### Brazeをデータソースとする場合
1. Nexlaプラットフォームで、左ツールバーの「**フロー」>「新規フローの作成**」を選択する。
2. **Create New Sourceを**クリックし、Brazeコネクタを選択し、**Nextを**クリックする。 
3. **Add a New Credentialを**選択し、認証情報に名前を付け、Braze APIキーとRESTエンドポイントを追加し、**Save**する。
4. 最後に、データを選択し、**Saveを**クリックする。 

Nexlaはデータソースを検索し、変換または送信先への送信のために[Nexsetを](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information)生成する。

#### Brazeが送信先なら

[Nexlaへのソースの接続については](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source)、Nexlaドキュメントを参照のこと。

### ステップ3:トランスフォーム（オプション）

顧客データに対してカスタム[変換を](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations)行いたい場合、またはNexlaのビルド済みコネクタを使用したい場合は、データセットの**変換**ボタンをクリックして変換ビルダーに入る。トランスフォームビルダーの使用方法は、[Nexlaのドキュメントに](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data)記載されている。

### ステップ 4:送信先

送信先にデータを送信するには、データセット上の「**送信**先」矢印をクリックし、Nexlaの送信先コネクタを選択するか、送信元が異なる場合はBrazeを選択する。認証情報を入力し、送信先オプションを設定し、**Saveを**クリックする。データは即座に、指定した送信先に指定したフォーマットで流れ始める。

## この統合を使う

一度フローが設定されれば、あとは何も必要ない。Nexlaはソースデータの変更に対応し、新しいデータへの拡張を行い、スキーマの変更やエラーをトリアージのために通知する。トランスフォーム、送信元、送信先を変更したい場合は、これらのオプションをクリックして変更すれば、Nexlaは即座にフローを更新する。

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)
[2]: https://www.nexla.com/get-demo