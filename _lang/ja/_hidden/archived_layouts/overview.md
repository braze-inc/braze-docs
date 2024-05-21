---
nav_title: 概要
page_order: 0
noindex: true
---

# layout:例の概要

> 概要レイアウトは、ユーザーがボタンをクリックしてページの特定の部分、またはまったく別のページに移動できるようにする特定のナビゲーションオプションをページの上部に作成するのに適しています。

セレクターレイアウトの典型的な例としては、[[SDK変更ログページやアプリ内メッセージクリエイティブ詳細ページがあります](https://www.braze.com/docs/user_guide/message_building_by_channel/in-app_messages/creative_details/)](https://www.braze.com/docs/developer_guide/platform_integration_guides/sdk_changelogs/)。

## 必要なコンポーネント

1. YAMLのオープンとクロージングの表記法。つまり、内容の前に---、そして内容の後に---。
2. 特定のパラメーターの内容を引用します。(ヘッダーパラメーター、テキストパラメーター、ハイフンまたはその他の特殊文字を含むコンテンツ)
3. 用語集タグ表記 (これらはフィルタータグです)

## 必須パラメーター

|パラメーター | コンテンツタイプ | 詳細 |
|---|---|---|
| `page_order` | 数値 | セクション内のページの順序を指定します。この順序は左側のナビゲーションに反映されます。|
| `nav-title` | 英数字 | 左側のナビゲーションに表示されるタイトル。|
| `layout` | 英数字-スペースなし | [ドキュメントのレイアウトセクションからレイアウトを選択してください](https://github.com/Appboy/braze-docs/tree/develop/_layouts)。|
| `guide_top_header` |英数字 | ページにタイトルを付けます。|
| `guide_top_text` |英数字 | ページを説明してください。ボタンとそのタイトルのすぐ上に表示されます。内容については引用が必要です。|
| `guide_featured_title` | 英数字 | カードにタイトルを付けてください。これはボタンのすぐ上に表示されます。
| `guide_featured_list` | その他のYAML、英数字 | [下記のガイドリスト形式を参照してください](#guide-listing-format)。|

### ガイドリスト形式

|パラメーター | コンテンツタイプ | 詳細 |
|---|---|---|
| `name` | 英数字 | ボックスに名前を付けます。|
| `link` | URL またはパス | ボックスの配置先へのリンク。完全な URL または (内部リンクの場合) `/docs...` | を含める必要があります
| `image` | パス | 画像の場所へのリンク。|

フォーマットの例:

```yaml
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/icon_modal.png
```

## 例:

\`\`yaml
---
nav_title: クリエイティブ詳細
page_order: 4
layout: 特集
ガイドトップヘッダー:「クリエイティブディテール」
ガイドトップテキスト:「アプリ内メッセージでクリエイティブになりましょう！ただし、最初にいくつかのガイドラインを知っておく必要があります。結局のところ、ルールを破るにはルールを知っておく必要があります！個々のメッセージタイプのクリエイティブスペックまたは下記のグローバルクリエイティブ詳細を確認してください。」

guide\_featured_ title:「メッセージタイプのクリエイティブスペック」
ガイド\_特集\_リスト:
-name: モーダル
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/icon_modal.png
-name: スライドアップ
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/icon_slideup.png
-name: フルスクリーン
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/icon_full_screen.png
---

# クリエイティブ詳細 {#general}

Brazeのアプリ内メッセージには、グローバルなクリエイティブ仕様と個別のクリエイティブ仕様の両方があります。よりカスタマイズ可能なアプリ内メッセージタイプの詳細については、[カスタマイズ] ({{site.baseurl}}) をご覧ください/user_guide/message_building_by_channel/in-app_messages/customize/) page.

{% alert important %}
  これらの詳細は、最新のアプリ内メッセージ生成（第3世代）にのみ適用されます。最新世代のアプリ内メッセージを使用していない場合は、[以前のアプリ内メッセージ生成] ({{site.baseurl}}) を確認してください/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}

