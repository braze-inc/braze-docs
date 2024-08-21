---
nav_title: サゲフロ
article_title: Sageflo Radiate
description: "この参考記事では、BrazeとSagefloのパートナーシップについて概説している。Sagefloは分散型マーケティングツールで、BrazeとのAPI統合により、マーケティングで承認されたテンプレート、画像、オーディエンスセグメントを使用して、チームが独自のメールを簡単に送信できるようにする。"
alias: /partners/sageflo/
page_type: partner
search_tag: Partner

---

# Sageflo Radiate

> [Sageflo Radiateは](https://sageflo.com/radiate)分散型マーケティングツールで、BrazeとのAPI統合により、マーケティングが承認したテンプレート、画像、視聴者セグメントを使用して、ローカルチームが簡単に独自の電子メールを送信できるようになる。

オーディエンスのセグメンテーション、フリークエンシーガバナンス、ダイナミックコンテンツなど、Brazeの洗練された機能を活用しながら、ローカルチームがより賢くマーケティングを行うために必要なツールを提供する。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| サゲフロ・ラジエイトのアカウント | このパートナーシップを利用するには、Sageflo Radiateアカウントが必要である。 |
| Braze REST API キー | 完全な`templates` および`campaigns` 権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze RESTエンドポイント | [RESTエンドポイントのURL][1]。APIエンドポイントは、BrazeインスタンスのダッシュボードURLと一致する。<br><br> 例えば、ダッシュボードのURLが`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` となる。 |
{: .reset-td-br-1 .reset-td-br-2}

## ユースケース

Radiateは、Brazeを通じてローカルオーディエンスにEメールを送信する権限を分散チームに与えることで、マーケティング活動の規模を拡大したいと考えているフランチャイズや小売業に最適である。

* 分散しているチームでも簡単にマーケティングEメールやSMSを送信できるようにする
* 地域社会を重視した顧客とのつながりを築く
* 内蔵ガードレールでブランドの一貫性を保つ
* 国内マーケティングチームの負担を軽減する

## 統合

Sagefloのアカウント・チームが統合の設定を担当する。BrazeのAPI認証情報を提供してもらい、Sagefloが御社のマーケティングチームと協力して、特定の場所や支店の視聴者セグメントを設定する。 

一旦接続されると、セージフロはそうする：

* Radiate環境とBrazeへの接続をセットアップする。
* Brazeでロケーションベースのオーディエンス・セグメントを設定する
* キャンペーン、ロケーション、ユーザーグループの設定を定義する
* Radiateキャンペーンで使用できるBrazeの地図テンプレート
* ユーザー・トレーニングのスケジュールと実施

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints