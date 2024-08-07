---
nav_title: "ユーザーエイリアスオブジェクト"
article_title: APIユーザーエイリアスオブジェクト
page_order: 11
page_type: reference
description: "このリファレンスでは、ユーザー・エイリアス・オブジェクトのさまざまなコンポーネントについて説明します。"

---

# ユーザーエイリアスオブジェクト

> エイリアスは、代替の一意なユーザー識別子の役割を果たす。ユーザーエイリアスオブジェクトを使用することで、モバイルアプリやウェブサイトにログインする前と後の両方で、特定のユーザーを追跡する分析用の一貫した識別子を設定することができます。このオブジェクトを使用して、サードパーティベンダーが使用する識別子をBrazeユーザーに追加し、外部とのデータの照合をより簡単に行うこともできます。

ユーザーエイリアスオブジェクトは2つの部分から構成される。識別子そのものを表す`alias_name` 、エイリアスのタイプを示す`alias_label` 。ユーザーは異なるラベルを持つ複数のエイリアスを持つことができますが、`alias_label` ごとに1つの`alias_name` のみです。

このオブジェクトはすべてのエンドポイントで頻繁に使用され、他のオブジェクトの中でもしばしば使用されます。

## オブジェクト本体
```json
{
  "user_alias" : {
    "alias_name" : (required, string),
    "alias_label" : (required, string)
  }
}
```
