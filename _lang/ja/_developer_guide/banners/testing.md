---
nav_title: バナーのテスト
article_title: バナーのテスト
page_order: 2
description: "すべてのメディア、コピー、パーソナライゼーション、カスタム属性が正しくレンダリングされるようにするために、キャンペーンを起動する前にバナーメッセージをテストする方法について説明します。"
channel:
  - banners
noindex: true
---

# バナーのテスト

> すべてのメディア、コピー、パーソナライゼーション、カスタム属性が正しくレンダリングされるようにするために、キャンペーンを起動する前にバナーメッセージをテストする方法について説明します。一般的な情報については、[バナーについて]({{site.baseurl}}/developer_guide/banners)を参照してください。

## 前提条件

Braze でバナーメッセージをテストする前に、[Braze でバナーキャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)を作成する必要があります。さらに、テストしたい配置がすでに[アプリや Web サイトに配置されている]({{site.baseurl}}/developer_guide/banners/placements)ことを確認します。 

テストを[コンテンツテストグループ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups)または個々のユーザーに送信するには、送信する前にテストデバイスでプッシュが有効になっており、テストユーザーの有効なプッシュトークンが登録されている必要があります。

## バナーのテスト

{% multi_lang_include banners/testing.md page="testing" %}
