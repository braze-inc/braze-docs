---
nav_title: キックボクシング
article_title: キックボクシング
alias: /partners/kickbox/
description: "この参考記事では、メールリストの検証やアプリケーションへの検証の統合に使用されるメール検証プラットフォームであるKickboxとBrazeのパートナーシップについて概説している。"
page_type: partner
search_tag: Partner
---

# キックボクシング

> [Kickboxは](https://kickbox.com/)オールインワンのメール検証プラットフォームで、メールデータをクリーンで配信可能な状態に保つために必要な機能、統合、セキュリティが満載されている。Kickboxとの統合により、Brazeキャンペーンの配信性が向上。Kickboxのメール検証を使用することで、未配信や低品質のメールアドレスを送信前に識別することができる。

Kickboxでは、ユーザープロファイルが更新された瞬間に、ユーザーのメールアドレスの品質を検証することができる。これは、専用のキャンバスまたはキャンペーンワークフローによって達成され、プロファイルの`email` フィールドの人口によってトリガーされる。

キャンバスまたはキャンペーンはKickboxにWebhookを送信し、ユーザーのメールアドレスを共有する。Kickboxはメールアドレスを検証し、Braze REST APIエンドポイントを使用して、その品質を詳述するカスタム属性でユーザープロファイルを更新する。

## 前提条件

| 必要条件                           | 説明                                                                   |
| --------------------------------------|-------------------------------------------------------------------------------|
| キックボクシング口座                       | この統合を使用するには、アクティブなKickboxアカウントが必要である。                |
| REST APIキー   | `users.track` 権限を持つ Braze REST API キー。<br><br>これは、ダッシュボードの**「設定」**>「**APIと識別子**」>「**APIキー**」で作成できる。|
| 統合へのアクセスをリクエストする。     | KickboxのサポートチームにBrazeインテグレーションへのアクセスを許可してもらう。        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 統合

Kickboxと統合するには、[Brazeとの統合の](https://docs.kickbox.com/docs/integrating-with-braze#/)ステップに従う。

## ユースケース

### 一括検証

また、数ヶ月に一度、あるいは四半期に一度、リスト全体を検証することで、解約するメールや、時間の経過とともに劣化し、徐々に配信率が低下するリストから身を守ることもできる。

そのためには、Kickboxが説明するように、ワークフローの**エントリ**設定を変更する必要がある。**アクションベースの配信を**選択する代わりに、**スケジュールされた配信を**選択する。そして、リストを一度に確認するスケジュールされた時間を選ぶ。

### 検証済みのセグメンテーションを作成する

Kickboxのカスタム属性は一貫したスキーマを持っており、以下の例と一致している。

{% raw %}
```json
   {
  "attributes": [
    {
      "email": "example1@kickbox.com",
      "_update_existing_only": true,
      "success": true,
      "code": null,
      "message": null,
      "result": "deliverable",
      "reason": "accepted_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": null,
      "sendex": 1,
      "user": "example1",
      "domain": "kickbox.com"
    },
    {
      "email": "example2@gamil.com",
      "_update_existing_only": true,
      "success": true,
      "code": "44312",
      "message": "SMTP verification",
      "result": "undeliverable",
      "reason": "rejected_email",
      "role": false,
      "free": false,
      "disposable": false,
      "accept_all": false,
      "did_you_mean": "example2@gmail.com",
      "sendex": 0.23,
      "user": "example2",
      "domain": "gamil.com"
    }
  ]
}
```
{% endraw %}

つまり、メールアドレスが確認されたユーザーのオーディエンスセグメントを作成することで、キャンペーンやキャンバスの配信成功率を高め、メールサービスプロバイダー（ESP）からの評判を守ることができる。

そのためには、以下の手順に従ってほしい：

1. Brazeで、**オーディエンス**>**セグメンテーション**> セグメントを作成する**。**
2. **フィルターグループセクションで**、**カスタム属性**フィルターを追加し、ドロップダウンで "result "を選択する。 

ユースケースによっては、Kickboxカスタム属性 "result "がユーザープロファイルに存在する、またはその値が "deliverable "に等しいセグメンテーションを作成することが適切な場合がある。このフィルターを単独で使用してセグメンテーションを作成することもできるし、将来的にすべてのセグメントの一部にして、セグメント内のすべてのユーザーを検証することもできる。 