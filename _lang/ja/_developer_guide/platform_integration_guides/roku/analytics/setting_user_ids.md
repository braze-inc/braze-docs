---
nav_title: ユーザー ID の設定
article_title: Roku のユーザー ID の設定
platform: Roku
page_order: 0
page_type: reference
description: "このリファレンス記事では、Roku のユーザー ID を識別および設定する方法と、ベストプラクティスおよび重要な考慮事項について説明します。"
 
---

# ユーザー ID の設定

> このリファレンス記事では、Roku のユーザー ID を識別および設定する方法と、ベストプラクティスおよび重要な考慮事項について説明します。

{% multi_lang_include archive/setting_user_ids/setting_user_ids.md %}

ユーザー ID を設定するため、ユーザが識別された直後 (一般的にはログイン後) に以下の呼び出しを行う必要があります。

```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```

## 推奨されるユーザー ID の命名規則

{% multi_lang_include archive/setting_user_ids/naming_convention.md %}

## ユーザー ID 統合のベストプラクティスとメモ

{% multi_lang_include archive/setting_user_ids/best_practices.md %}

