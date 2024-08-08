---
nav_title: "オブジェクトを識別するためのエイリアス"
article_title: オブジェクトを識別するための API エイリアス
page_order: 11
page_type: reference
description: "この記事では、オブジェクト仕様を識別するためのエイリアスについて説明します。"

---

# オブジェクトを識別するためのエイリアス

属性オブジェクトに任意のフィールドを含む API リクエストは、指定されたユーザープロファイルの指定された値でその名前の属性を作成または更新します。 

Brazeユーザープロファイルフィールド名（[以下またはBrazeユーザープロファイルフィールドのセクションに記載されているもの]({{site.baseurl}}/api/objects_filters/user_attributes_object/#braze-user-profile-fields)）を使用して、ダッシュボードのユーザープロファイルの特別な値を更新するか、独自のカスタム属性データをユーザーに追加します。

## オブジェクトボディ

```json
{
  "aliases_to_identify" : (required, array of aliases to identify object)
  [
    {
      "external_id" : (required, string) see External user ID,
      // external_ids for users that do not exist will return a non-fatal error.
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
