---
nav_title: データ・グレイル
article_title: データ・グレイル
description: "この参考記事では、Brazeとプライバシー管理プラットフォームであるDataGrailのパートナーシップについて概説しており、Braze内で収集・保存された消費者データを検出してDSRを迅速に処理することができる。"
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# データ・グレイル

> プライバシー管理プラットフォームである[DataGrailは](https://www.datagrail.io/)、消費者の信頼を築き、リスクの高いビジネスを排除するのに役立つ。継続的なシステム検知と自動化されたデータ対象者要求（DSR）の履行により、DataGrailはプライバシープログラムを強化し、GDPR、CCPA、CPRAのような進化するプライバシー法や規制へのコンプライアンスをサポートする。 

BrazeとDataGrailの統合により、Braze内に収集・保存された消費者データを検出し、DSR（アクセス、削除、販売禁止要求）を迅速に処理することができる。Brazeは、自動化されたデータマッピングによって、消費者データが組織内のどこに存在するかの正確な青写真に追加される。プライバシーフレームワークを維持したり、処理活動の記録（RoPA）を作成したりするための調査やスプレッドシートはもう必要ない。 

## 前提条件

| 要件 | 説明 |
|---|---|
| DataGrailアカウント | このパートナーシップを利用するには、DataGrailアカウントが必要である。<br>統合に関する問題や質問があれば、管理者に連絡するか、support@datagrail.io 。 |
| BrazeのAPIキー | `events.list` 、`users.export.ids` 、`users.delete` 、`users.track` の権限を持つBraze REST APIキー。<br><br>これは、Brazeダッシュボードの**「設定」**>「**APIキー**」から作成できる。 |
| ブレイズインスタンス | あなたのBrazeインスタンスは、あなたのBrazeオンボーディングマネージャーから取得するか、[API概要ページで]({{site.baseurl}}/api/basics/#endpoints)見つけることができる。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

DataGrailポータルにログインし、Brazeの統合ページで**Connectを**クリックする。次に、インスタンスとBraze API Keyを入力し、**Connect Brazeを**クリックする。

統合するBrazeアカウントが追加された場合：
1. Brazeの統合ページで**Edit Connectionを**クリックする。
2. ドロップダウンから、**+Add New Connectionを**選択する。
3. **Connection Name（接続名**）の下に、この別個のアカウントを識別するための新しい名前を入力する（例：Braze Training Account）。
4. この新しいアカウント用に、別のBrazeインスタンスとAPIキーを入力する。
5. **コネクトを**クリックする。

統合に関する問題や質問があれば、DataGrail（support@datagrail.io ）までEメールで問い合わせを。
