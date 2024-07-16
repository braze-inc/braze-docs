---
nav_title: Taxi for Email
article_title:メール用Taxi
alias: /partners/taxi_for_email
description:"この参考記事では、BrazeとオンラインメールマーケティングツールであるTaxi for Emailのパートナーシップについて概説している。" Brazeの顧客は、ドラッグ＆ドロップのインターフェイスとシンプルかつパワフルな構文を使用して、インテリジェントなメールテンプレートを作成することができる。
page_type: partner
search_tag:Partner

---

# メール用Taxi

> [Taxi for Emailは](http://taxiforemail.com/)、直感的なドラッグ＆ドロップのビジュアルメールエディタを提供するオンラインメールマーケティングツールである。Taxiは、コピーライターやエディターがメール作成に必要なアクセスやリソースをコードなしで利用できるようにすることで、チームでのメールキャンペーンの共同作業を容易にする。

BrazeとTaxiの統合は、Taxiのシンプルかつ強力な構文を活用して、インテリジェントなメールテンプレートを作成し、Brazeにエクスポートする。 

## 前提条件

| 必要条件 | 説明 |
| ------------| ----------- |
| メールアカウント用Taxi | このパートナーシップを利用するには、Taxi for Emailアカウントが必要である。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST APIキー。<br><br> これはダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Brazeエンドポイント | [Brazeエンドポイントは]({{site.baseurl}}/api/basics/#endpoints)、BrazeダッシュボードのURLと一致する。<br><br> 例えば、ダッシュボードのURLが`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` となる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 統合

### ステップ1:Taxiメールテンプレートを作成する

TaxiプラットフォームでTaxiテンプレートを作成する。テンプレートが作成されたら、**組織設定に**移動し、メールサービス**プロバイダー（ESPコネクター**）タブを選択する。

### ステップ2:Brazeコネクタを作成する

1. 表示されたダイアログで「**新規追加**」ボタンをクリックし、ドロップダウンから**Brazeを**選択する。 
2. **Braze**コネクタ設定を編集するには、**Brazeを**クリックする。
3. BrazeエンドポイントとBraze APIキーを入力する。

正しい権限を持つ詳細が提供されると、コネクタフィールドの色が変わる。このフィールドが変更されない場合は、あなたのフィールドがリストされた要件と一致していることを確認する。

## 使用

アップロードしたTaxiテンプレートをBrazeアカウントの**Templates & Media > Email Templates**セクションで探す。このテンプレートを使って、カスタマーにエンゲージメントメッセージを送ることができる！

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/email/creating_an_email_template/
