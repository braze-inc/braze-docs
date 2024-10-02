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

Braze とViralSweep のインテグレーションでは、ViralSweep プラットフォームで懸賞やコンテストを開催し(メールとSMS リストを拡大)、懸賞やコンテストエントリをBraze に送信してキャンペーンやキャンバスで使用できます。 

## 前提条件

| 要件 | 説明 |
| ----------- | ----------- |
| ViralSweepアカウント | 事業計画を活用したViralSweep勘定は、この提携の前倒しタグeをとることが求められる。 |
| Braze REST API キー | すべてのユーザーデータおよびメール権限を持つBraze REST API キー。<br><br> これは、**Settings** > **API Keys** のBraze ダッシュボードで作成できます。 |
|Braze REST エンドポイント | REST エンドポイントのURL。エンドポイントは、[インスタンス]({{site.baseurl}}/api/basics/#endpoints)のBraze URLによって異なります。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### ステップ1 :ViralSweep内のBrazeへの接続

ViralSweep で、**Integrations > Email & SMS > Add Service** に移動し、**Braze** を選択します。 

![][1]

### ステップ2 :Braze認証情報の追加

統合設定ウィンドウで、Braze REST API キーとREST エンドポイントを指定します。指定するエンドポイントに`https://` が含まれていないことを確認します(`dashboard-03.braze.com` など)。 

![ViralSweep サービスインテグレーションページで、ユーザーにBraze API キーとBraze ダッシュボードのURL を入力します。][2]{: style="max-width:40%;"}

**Connect**をクリックします。

### ステップ3 :Braze認証情報の追加
あなたはつながっています!プロモーションがBrazeに接続され、ViralSweepによって収集されたすべてのエントリーが自動的にBrazeに送信されます。

## よくある質問

### ヴィラルスイープがBrazeに渡したフィールドは?
- 名
- 姓
- メールアドレス
- 住所
- アドレス2
- 市区町村
- 状態
- ジップ
- 国
- 生年月日
- 電話
- プロモーションID
- 照会リンク
- 追跡キャンペーンの名前

### ViralSweepは更新 サブスクライバーしますか?
そうです。プロモーションを実行し、ViralSweep が誰かをBraze に渡した場合、将来別のプロモーションを実行し、同じ人物が入力すると、その人物の情報は自動的にBraze で更新d になります(新しい情報が提供されている場合)。主に紹介URLは、入力したプロモーションごとに最新のURLが付いた更新dとなり、プロモーションID フィールドには入力したすべてのプロモーションのIDが含まれます。

## トラブルシューティング

Brazeに接続していて、アカウントに追加されていない場合は、次のような理由が考えられます。

- **メールはBrazeにすでに存在します**<br>
プロモーションに入力されたメールの住所は、すでにあなたのBrazeアカウントに登録されている可能性があるため、再度追加されることはありません。その連絡先に新しい情報が提供された場合にのみ更新 d となります。<br><br>
- **ViralSweepに入力済みのメール**<br>
プロモーションに入力されたメールの住所はすでに入力されているため、再度Brazeに渡されることはありません。プロモーションにすでに参加した後にBrazeインテグレーションを設定すると、このアプリが表示されます。

[1]: {% image_buster /assets/img/viralsweep/connect.gif %}
[2]: {% image_buster /assets/img/viralsweep/connect2.png %}
