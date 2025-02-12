---
nav_title: "ユーザーエイリアスオブジェクト"
article_title: APIユーザーエイリアスオブジェクト
page_order: 11
page_type: reference
description: "このリファレンス記事では、ユーザーエイリアスオブジェクトのさまざまなコンポーネントについて説明します。"

---

# ユーザーエイリアスオブジェクト

> エイリアスは、代替の一意なユーザー識別子の役割を果たす。ユーザーエイリアスオブジェクトを使用することで、モバイルアプリやウェブサイトにログインする前と後の両方で、特定のユーザーを追跡するアナリティクス用の一貫した識別子を設定することができる。このオブジェクトを使用して、サードパーティベンダーが使用する識別子をBrazeユーザーに追加し、外部とのデータの照合をより簡単に行うこともできる。

ユーザーエイリアスオブジェクトは、2つの部分から構成される：識別子そのものの`alias_name` 、エイリアスのタイプを示す`alias_label` 。ユーザーは、異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに `alias_name` は1つしか持つことができません。

このオブジェクトはあらゆるエンドポイントで頻繁に使用され、他のオブジェクト中でもよく使用されます。

## オブジェクト本体

```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```

### 例

```json
{
  "user_alias": {
    "alias_name": "john_doe_123",
    "alias_label": "email_id"
  },
  "external_id": "user_456"
}
```