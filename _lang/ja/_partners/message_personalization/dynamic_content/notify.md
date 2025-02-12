---
nav_title: Notify
article_title: Notify
description: "この参考記事では、顧客ライフサイクル全体にわたってパーソナライゼーションを提供するリアルタイムオムニチャネルパーソナライゼーションソリューションである Braze と Notify のパートナーシップについて概説しています。"
alias: /partners/notify/
page_type: partner
search_tag: Partner
---

# Notify

> [Notify](https://notifyai.io/) は、カスタマーリレーションシップマネジメントツールとシームレスに統合し、マーケティング戦略を強化し、複数のチャネルにわたってエンゲージメントを促進する AI 主導のソフトウェアソリューションです。

Braze と Notify の統合により、マーケターは様々なプラットフォームで効果的にエンゲージメントを促進できるようになります。従来のマーケティング手法に依存する代わりに、Braze API によってトリガーされたキャンペーンでは、Notify の機能を活用して、メール、SMS、プッシュ通知などを含む複数のチャネルを通じてパーソナライズされたメッセージングを配信できます。

## 前提条件

開始する前に、次のものが必要になります。

| 要件          | 説明                                                                                                                                |
|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|  Braze REST API キー  | `users.export.segment` および `campaigns.trigger.send` の権限を持つ Braze REST API キー。<br><br> これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| CNAME 設定 | Notify がメッセージングに対するユーザーのエンゲージメントを追跡し、モデルにさらに情報を提供するには、メールで使用されるトラッキングピクセル用にサブドメインを作成する必要がある。サブドメイン作成後、サブドメインのURLをNotifyと共有する。 |
| データベースのオプトイン・エクスポート | 昨年 (12ヶ月) のキャンペーンと購入のデータを Notify に送信します。​このエクスポートは、Notify予測モデルのトレーニングに使用される。<br><br> **フィールド:**<br><br> **メール: **メールのSHA256ハッシュを小文字に変換し、先頭または末尾のスペースを取り除いたもの。<br><br>**セグメント:**活動レベル（アクティブまたは非アクティブ）を定義するセグメンテーション情報。<br><br>**サブセグメント：**購買アクティビティレベルなど、その他の関連するアクティビティ情報。|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### ステップ1:キャンペーンを作成

Braze で[API トリガーキャンペーン](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/api_triggered_delivery)を作成します。そして、キャンペーン`api_identifier` を Notify と共有します。

### ステップ 2: Braze でセグメントを作成する

次に、[ステップ1](#step-1-create-your-campaign)で作成したキャンペーンでターゲットにしたいユーザーのセグメントを作成します。そして、セグメント ID を Notify と共有します。

### ステップ 3: セグメントを取得する

そして、Notify はキャンペーンに関連付けられたセグメント内のユーザーをエクスポートします。

### ステップ 4: Notify によってキャンペーンがトリガーされます。

Notify の AI は `/campaigns/trigger/send` エンドポイントを使用して、[ステップ1](#step-1-create-your-campaign)で作成した Braze キャンペーンをトリガーし、ユーザーが最も関心を持ちそうなタイミングでユーザーに送信します。