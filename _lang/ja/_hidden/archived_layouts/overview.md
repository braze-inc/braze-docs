---
nav_title: 概要
page_order: 0
noindex: true
---

# レイアウト例：概要

> オーバービュー・レイアウトは、ページの上部に特定のナビゲーション・オプションを設け、ユーザーがボタンをクリックしてページの特定の部分や、まったく別のページに移動できるようにするのに適している。

セレクタ・レイアウトの典型的な例としては、[SDK Changelogs](https://www.braze.com/docs/developer_guide/platform_integration_guides/sdk_changelogs/)ページや[アプリ内メッセージCreative Detailsページが](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/)ある。

## 必要なコンポーネント

1. YAMLのオープン表記とクローズ表記。つまり、コンテンツの前に---、コンテンツの後に---ということだ。
2. 特定のパラメータの内容を引用符で囲む。(ヘッダー・パラメーター、テキスト・パラメーター、ハイフンやその他の特殊文字を含むコンテンツ)。
3. 用語集タグの表記（これらはフィルタータグである）

## 必須パラメータ

|パラメーター | コンテンツ・タイプ | 詳細 |
|---|---|---|
|`page_order`| 数値 | セクション内でページを順番に並べる。この順番は左側のナビゲーションに反映される。 |
| `nav-title`| 英数字 | 左側のナビゲーションに表示されるタイトル。 |
|`layout`| 英数字 - スペースなし | ドキュメントの[レイアウトセクションから](https://github.com/Appboy/braze-docs/tree/develop/_layouts)レイアウトを選択する。 | 
|`guide_top_header`|英数字 | ページにタイトルをつける。|
|`guide_top_text`|英数字 | これはボタンとそのタイトルの真上に表示される。内容によっては引用が必要である。 |
|`guide_featured_title`| 英数字 | カードにタイトルをつける。これはボタンの真上に配置される。
|`guide_featured_list`| より多くのYAML、英数字 | 下記の[ガイド掲載フォーマットを](#guide-listing-format)参照のこと。 |

### ガイド掲載フォーマット

|パラメーター | コンテンツ・タイプ | 詳細 |
|---|---|---|
|`name`| 英数字 | 箱に名前をつける。 |
| `link`| URLまたはパス | 箱が置かれる場所へのリンク。完全なURL、または（内部リンクの場合は）完全なURLを含むこと。 `/docs...`  |
|`image`| パス | 画像の場所へのリンク。 |

フォーマットの例：

```yaml
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

## 例

```yaml
---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know those rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Creative Details {#general}

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.

{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}
```
