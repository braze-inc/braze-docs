---
nav_title: ViralSweep
article_title:ViralSweep
alias: /partners/viralsweep/
description:"この参考記事では、ブランドが懸賞、コンテスト、インスタントウィン、ウェイティングリスト、紹介プロモーションなどのデジタルマーケティングプロモーションを構築、実行、管理できるソフトウェアサービスであるViralSweepとBrazeのパートナーシップについて概説している。"
page_type: partner
search_tag:Partner

---

# ViralSweep

> [ViralSweepは](https://viralsweep.com)、ブランドが懸賞、コンテスト、インスタントウィン、ウェイティングリスト、紹介プロモーションなどのデジタルマーケティングプロモーションを構築、実行、管理できるソフトウェアサービスである。 

BrazeとViralSweepの統合により、ViralSweepプラットフォーム上で懸賞やコンテストを開催し（メールやSMSのリストを増やす）、懸賞やコンテストのエントリ情報をBrazeに送信してキャンペーンやCanvasesで使用することができる。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| ViralSweepアカウント | このパートナーシップを利用するには、ビジネスプランを利用したViralSweepアカウントが必要である。 |
| Braze REST API キー | すべてのユーザーデータとメール権限を持つBraze REST APIキー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
|Braze RESTエンドポイント | RESTエンドポイントのURL。エンドポイントは[インスタンスの]({{site.baseurl}}/api/basics/#endpoints)Braze URLに依存する。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ 1 ：ViralSweep内でBrazeに接続する

ViralSweepで、**Integrations > Email & SMS > Add Serviceに**移動し、**Brazeを**選択する。 

![][1]

### ステップ 2 ：認証情報を追加する

インテグレーション設定ウィンドウで、REST APIキーとRESTエンドポイントを入力する。提供するエンドポイントに`https://` 、例えば`dashboard-03.braze.com` が含まれていないことを確認する。 

![ViralSweep サービス統合ページで、ユーザーに API キーとダッシュボード URL の入力を求める。][2]{: style="max-width:40%;"}

**コネクトを**クリックする。

### ステップ 3 ：認証情報を追加する
つながっている！プロモーションはBrazeに接続され、ViralSweepが収集したエントリーはすべて自動的にBrazeに送信される。

## よくある質問

### ViralSweepはどのフィールドをBrazeに渡すのか？
- 名
- 姓
- メールアドレス
- 住所
- 住所 2
- 市区町村
- 状態
- ジップ
- 国
- 生年月日
- 電話
- プロモーションID
- 紹介リンク
- トラッキング, 追跡キャンペーン名

### ViralSweepはサブスクライバーを更新するのか？
そうです。プロモーションを実施し、ViralSweepが誰かをBrazeに渡した後、将来別のプロモーションを実施し、同じ人が応募した場合、その人の情報は自動的にBrazeで更新される（新しい情報が提供された場合）。主に、紹介URLは、彼らがエントリーした各プロモーションの最新のURLで更新され、プロモーションIDフィールドには、彼らがエントリーしたすべてのプロモーションのIDが含まれる。

## トラブルシューティング

Brazeに接続してもデータがアカウントに追加されない場合は、それが原因かもしれない：

- **メールはすでにBrazeに存在する**<br>
プロモーションに入力されたメールアドレスは、すでにBrazeアカウントに登録されている可能性があるため、再度追加されることはなく、その連絡先に新しい情報が提供された場合にのみ更新される。<br><br>
- **ViralSweep に入力済みのメール**<br>
プロモーションに入力されたEメールアドレスは、すでに以前に入力されているため、再度Brazeに渡されることはない。この現象は、すでにプロモーションに参加した後にBrazeとの統合を設定した場合に起こる可能性がある。

[1]: {% image_buster /assets/img/viralsweep/connect.gif %}
[2]: {% image_buster /assets/img/viralsweep/connect2.png %}
