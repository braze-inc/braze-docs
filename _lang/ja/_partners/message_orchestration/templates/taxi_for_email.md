---
nav_title: Taxi for Email
article_title: Taxi for Email
alias: /partners/taxi_for_email
description: "このリファレンス記事では、Braze と Taxi for Email のパートナーシップについて説明します。Taxi for Email は、Braze のお客様がドラッグアンドドロップインターフェイスとシンプルで強力な構文を使用してインテリジェントなメールテンプレートを作成できるオンラインメールマーケティングツールです。"
page_type: partner
search_tag: Partner

---

# Taxi for Email

> [メール用タクシー](http://taxiforemail.com/)は、直感的なドラッグアンドドロップビジュアルメールエディタを提供するオンラインメール マーケティングツールです。Taxi は、チームがメールキャンペーンで容易にコラボレーションできるようにし、コピーライターや編集者が、メールを作成するために必要なリソースとアクセスを、すべてコードなしで利用できるようにします。

_この統合は、Taxi for Email によって管理されます。_

## 統合について

Brazeとタクシーの統合では、タクシーのシンプルでパワフルなシンタックスを使用して、Brazeにインテリジェントなメール テンプレートを作成およびエクスポートします。 

## 前提条件

| 必要条件 | 説明 |
| ------------| ----------- |
| Taxi for Email アカウント | このパートナーシップを活用するには、Taxi for Email アカウントが必要です。 |
| Braze REST API キー | 完全な**テンプレート**権限を持つBraze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| Braze エンドポイント | [あなたのBraze エンドポイント]({{site.baseurl}}/api/basics/#endpoints)はあなたのBraze ダッシュボード URLに合わせます。<br><br> たとえば、ダッシュボード URL が`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` になります。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## 統合

### ステップ1:タクシーメール テンプレートの作成

Taxi プラットフォームで Taxi テンプレートを作成します。テンプレートが作成されたら、[**Organization Settings**] に移動して [**ESP Connectors**] タブを選択します。

### ステップ2:Brazeコネクターの作成

1. 表示されるダイアログで、**新規**ボタンを選択し、ドロップダウンから**Braze**を選択します。 
2. [**Braze**] を選択して、Braze コネクターの設定を編集します。
3. Braze エンドポイントとBraze API キーを入力します。

正しい権限を含む詳細が指定された後に、コネクターフィールドの色が変わります。このフィールドが変わらない場合は、フィールドがリストされている条件に合っていることを確認します。

## 使用

アップロード Taxi テンプレートをBraze アカウントの** テンプレート s & Media > E メールテンプレートs** セクションで見つけます。これで、このメールテンプレートを使用して、顧客に魅力的なメールメッセージを送信できます。


