---
nav_title: DataGrail
article_title: DataGrail
description: "このリファレンス記事では、Braze と DataGrail のパートナーシップについて説明します。DataGrail はプライバシー管理プラットフォームであり、Braze 内で収集され、保存されている消費者データを検出してDSR を迅速に処理できます。"
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/) は、消費者の信頼を得て、リスクの高いビジネスを排除するうえで役立つプライバシー管理プラットフォームです。DataGrail は、継続的なシステム検出と自動化されたデータ主体要求 (DSR) の履行により、プライバシープログラムを推進し、GDPR、CCPA、CPRA などの変遷するプライバシー関連の法律や規制に準拠できるように支援します。 

_この統合は DataGrail によって管理されます。_

## 統合について

BrazeとDataGrailの統合により、Braze内に収集・保存された消費者データを検出し、DSR（アクセス、削除、販売禁止要求）を迅速に処理することができる。自動化されたデータマッピングにより、消費者データが組織内のどこにあるかを正確に把握できるうえに、Braze が追加されるため、プライバシーフレームワークの維持や処理活動の記録 (RoPA) の作成にアンケートやスプレッドシートは不要になります。 

## 前提条件

| 要件 | 説明 |
|---|---|
| DataGrailアカウント | このパートナーシップを活用するには、DataGrail アカウントが必要です。<br>統合に関する問題や質問がある場合は、システム管理者にお問い合わせいただくか、または support@datagrail.io までメールでお問い合わせください。 |
| BrazeのAPIキー | `events.list`、`users.export.ids`、`users.delete`、`users.track` の権限を持つ Braze REST API キー。<br><br>これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Brazeインスタンス | Braze インスタンスは Braze オンボーディングマネージャーから入手できます。また、[API 概要ページ]({{site.baseurl}}/api/basics/#endpoints)でも確認できます。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

DataGrail ポータルにログインし、Braze の統合ページで [**接続**] を選択します。次にインスタンスと Braze API キーを入力し、[**Braze を接続**] を選択します。

統合するBrazeアカウントが追加された場合：
1. Braze の統合ページで [**接続を編集**] を選択します。
2. ドロップダウンから [**+新しい接続の追加**] を選択します。
3. **Connection Name（接続名**）の下に、この別個のアカウントを識別するための新しい名前を入力する（例：Braze Training Account）。
4. この新しいアカウント用に、別のBrazeインスタンスとAPIキーを入力する。
5. [**接続**] を選択します。

統合に関する問題やご質問がある場合は、DataGrail (support@datagrail.io) までメールでお問い合わせください。

