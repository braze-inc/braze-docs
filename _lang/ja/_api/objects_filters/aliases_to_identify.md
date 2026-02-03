---
nav_title: "オブジェクトを識別するためのエイリアス"
article_title: オブジェクトを識別するためのAPIエイリアス
page_order: 11
page_type: reference
description: "この記事では、オブジェクトの仕様を識別するためのエイリアスについて説明する。"

---

# オブジェクトを識別するためのエイリアス

属性 s オブジェクトにフィールドs が含まれるAPI リクエストは、指定されたユーザープロファイルに指定された値で、その名前の属性を作成または更新します。

Brazeユーザープロファイルフィールド名（以下にリストされているもの、または[Brazeユーザープロファイルフィールド]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)のセクションにリストされているもの）を使用して、ダッシュボードのユーザープロファイル上のそれらの特別な値を更新するか、独自のカスタム属性データをユーザーに追加します。

## オブジェクト本体

```json
{
  "aliases_to_identify" : (required, array of aliases to identify object)
  [
    {
      "external_id" : (required, string) see External user ID,
      // external_ids for users that do not exist return a non-fatal error.
      // See server responses for details.
      "user_alias" : {
        "alias_name" : (required, string) see User aliases,
        "alias_label" : (required, string) see User aliases
      }
    }
  ]
}
```

- [外部ユーザ ID]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)
- [ユーザーのエイリアス]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/#user-aliases)