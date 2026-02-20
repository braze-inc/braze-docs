---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "このレファレンス記事では、Brazeと、ブランドが懸賞、コンテスト、インスタント・ウィン、ウェイトリスト、紹介プロモーションなどのデジタルマーケティングプロモーションを構築、実行、管理できるソフトウェアサービス「ViralSweep」との提携について概説する。"
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com)は、懸賞、コンテスト、インスタントウィン、ウェイトリスト、紹介プロモーションなどのデジタルマーケティングプロモーションを、ブランドが構築、実行、管理できるようにするソフトウエアサービスです。 

_この統合は ViralSweep によって管理されます。_

## 統合について

Braze と ViralSweep の統合により、ViralSweep プラットフォームで懸賞とコンテストを開催し (メールと SMS のリストが増加します)、キャンペーンまたはキャンバスで使用できるように懸賞とコンテストへの参加情報を Braze に送信できます。 

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| ViralSweep アカウント | このパートナーシップを活用するためには、ビジネスプランを利用している ViralSweep アカウントが必要です。 |
| Braze REST API キー | すべてのユーザーデータおよびメール権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
|Braze RESTエンドポイント | REST エンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1 :ViralSweep内のBrazeへの接続

ViralSweepで、**Integrations > Email& SMS > Add Serviceに**移動し、**Brazeを**選択する。 

![]({% image_buster /assets/img/viralsweep/connect.gif %})

### ステップ2 :Braze 認証情報を追加する

統合設定ウィンドウで、Braze REST API キーと REST エンドポイントを指定します。指定するエンドポイントに`https://` が含まれていないことを確認します(`dashboard-03.braze.com` など)。 

![ユーザーに Braze API キーと Braze ダッシュボード URL の入力を求める ViralSweep サービス統合ページ。]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

[**Connect**] をクリックします。

### ステップ3 :Braze 認証情報を追加する
接続が完了しました。プロモーションがBrazeに接続され、ViralSweepによって収集されたすべてのエントリーが自動的にBrazeに送信されます。

## よくある質問

### ViralSweep から Braze にはどのフィールドが渡されますか?
- 名
- 姓
- メールアドレス
- 住所
- Address 2
- 市区町村
- 状態
- Zip
- 国
- 生年月日
- 電話
- プロモーションID
- Referral link
- 追跡キャンペーンの名前

### ViralSweep ではサブスクライバーが更新されますか?
そうです。プロモーションを実行し、ViralSweep が誰かをBraze に渡した場合、将来別のプロモーションを実行し、同じ人物が入力すると、その人物の情報は自動的にBraze で更新d になります(新しい情報が提供されている場合)。主に、紹介 URL は、入力するプロモーションごとに最新の URL で更新され、プロモーション ID フィールドにはこれまでに入力したすべてのプロモーションの ID が含まれます。

## トラブルシューティング

Brazeに接続していて、アカウントに追加されていない場合は、次のような理由が考えられます。

- **メールがすでに Braze に存在している**<br>
プロモーションに入力されたメールの住所は、すでにあなたのBrazeアカウントに登録されている可能性があるため、再度追加されることはありません。その連絡先に新しい情報が提供された場合にのみ更新 d となります。<br><br>
- **メールがすでに ViralSweep に入力されている**<br>
プロモーションに入力されたメールの住所はすでに入力されているため、再度Brazeに渡されることはありません。プロモーションにすでに参加した後にBrazeインテグレーションを設定すると、このアプリが表示されます。


