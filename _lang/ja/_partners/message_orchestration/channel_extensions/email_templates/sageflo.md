---
nav_title: Sageflo
article_title: Sageflo Radiate
description: "この参考記事では、BrazeとSagefloのパートナーシップについて概説している。Sagefloは分散型マーケティングツールで、BrazeとのAPI統合により、マーケティングで承認されたテンプレート、画像、オーディエンスセグメントを使用して、チームが独自のメールを簡単に送信できるようにする。"
alias: /partners/sageflo/
page_type: partner
search_tag: Partner

---

# Sageflo Radiate

> [Sageflo Radiate](https://sageflo.com/radiate) は分散型マーケティングツールであり、Braze との API 統合により、ローカルチームがマーケティングで承認されたテンプレート、画像、およびオーディエンスセグメントを使用して独自のメールを簡単に送信できるようになります。

_この統合は Sageflo によって管理されます。_

## 統合について

オーディエンスのセグメンテーション、フリークエンシーガバナンス、ダイナミックなコンテンツなどの Braze の高度な機能を活用し、ブランドを保護するガードを組み込みながら、マーケターに必要な洗練されたツールをローカルのチームに提供します。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Sageflo Radiate アカウント | このパートナーシップを活用するには、Sageflo Radiate アカウントが必要です。 |
| Braze REST API キー | 完全な`templates` および`campaigns` 権限を持つ Braze REST API キー。<br><br> これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze REST エンドポイント | [RESTエンドポイントのURL][1]。API エンドポイントは、Brazeインスタンスのダッシュボード URL と一致します。<br><br> たとえば、ダッシュボード URL が`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` になります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

Radiateは、Brazeを通じてローカルオーディエンスにEメールを送信する権限を分散チームに与えることで、マーケティング活動の規模を拡大したいと考えているフランチャイズや小売業に最適である。

* 分散しているチームでも簡単にマーケティングEメールやSMSを送信できるようにする
* 地域に密着した顧客とのつながりを構築する
* 内蔵ガードレールでブランドの一貫性を保つ
* 国内マーケティングチームの負担を軽減する

## 統合

Sageflo アカウントチームが統合の設定作業を主導します。Braze API の認証情報を入力するよう求められます。Sageflo はマーケティングチームと協力して、特定のロケーションとブランチのオーディエンスセグメントを設定します。 

接続が完了すると、Sageflo は次の作業を行います。

* Radiate環境とBrazeへの接続をセットアップする。
* Brazeでロケーションベースのオーディエンス・セグメントを設定する
* キャンペーン、ロケーション、ユーザーグループの設定を定義する
* Radiateキャンペーンで使用できるBrazeの地図テンプレート
* ユーザー・トレーニングのスケジュールと実施


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints