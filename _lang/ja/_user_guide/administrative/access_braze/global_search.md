---
nav_title: Braze ダッシュボードの検索
article_title: Braze ダッシュボードの検索
page_order: 0.5
page_type: reference
description: "Braze のグローバル検索について学習しましょう。"
---

# Braze ダッシュボードの検索

検索バーを使用して、Braze ダッシュボード内で作業やその他の情報を検索できます。検索バーは Braze ダッシュボードの最上部にあります。検索バーをクリックするか、Windows の場合は <kbd>Ctrl</kbd>+<kbd>K</kbd> キー、Mac の場合は <kbd>⌘</kbd>+<kbd>K</kbd> を押すと、検索バーに直接ジャンプします。

![キーワード"promo"の検索結果。プロモーションコードを含む、用語プロモを含むキャンペーンとアイテムを表示します。]({% image_buster /assets/img/navigation/global_search_new.png %})

## 検索できる項目

次の項目とアクションを検索できます。

- キャンペーン名
- キャンバス名
- コンテンツブロック
- セグメント名
- メールテンプレート名
- [Braze 内のページ](#find-pages-that-have-been-renamed)

{% alert tip %}
完全に一致するテキストを検索するには、検索語を引用符 ("") で囲みます。例えば、“すべてのユーザー“ を検索すると、“すべてのユーザー“ と完全に一致する語句を名前に含むすべての項目が返されます。
{% endalert %}

## 主な機能

### キーボードショートカット

キーボードショートカットを使用して、簡単に検索結果間を移動できます。

<style>
  div.small_table + table {
    max-width: 60%;
  }
table th:nth-child(1),
table th:nth-child(2),
table td:nth-child(1),
table td:nth-child(2), {
    width:20%;
}
table td {
    word-break: break-word;
}
</style>

<div class="small_table"></div>

| アクション (Action)                      | キーボードショートカット                                                             |
| --------------------------- | ----------------------------------------------------------------------------- |
| 検索メニューを開く        | {::nomarkdown}<ul> <li> Mac: <kbd>⌘</kbd> + <kbd>K</kbd></li> <li>Windows:<kbd>Ctrl</kbd> + <kbd>K</kbd></li> </ul> {:/}  |
| 検索結果間の移動 | <kbd>⬆</kbd> / <kbd>⬇</kbd>  |
| 検索結果を選択      | <kbd>Enter</kbd>    |
| 検索メニューを閉じる       | <kbd>Esc</kbd>  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### コンテンツタイプとステータスタグ

各検索結果には、結果のコンテンツタイプ (ページ、キャンペーン、キャンバス、セグメント、メールテンプレート) とステータス (アクティブ、アーカイブ済み、停止など) を示すタグが付いています。

### 最近開いたコンテンツへのアクセス

検索メニューから、最近アクセスしたコンテンツに再度アクセスできます。検索インターフェイスに、Braze プラットフォーム全体にわたって操作したアイテムを含め、最近開いた結果が検索バーの下に表示されます。これにより、以前に表示したページ、キャンペーン、キャンバス、セグメント、またはメールテンプレートに戻ることができるため、少ないクリック回数で、中断したところから再開できます。

![検索が展開され、最近開封されたページとユーザーのBrazeの内容が表示されます。]({% image_buster /assets/img/navigation/search_recently_opened.png %})

### 名前が変更されたページの検索

検索では、[更新されたナビゲーション]({{site.baseurl}}/user_guide/administrative/access_braze/navigation/)で名前が変更されたページの同義語が認識されます。例えば、「Currents」を検索すると、そのページの名前が変更されたため、「データのエクスポート」が表示されます。

![&quot の検索結果;Data Export"ユーザーが"Currents.&quot を検索した場所;]({% image_buster /assets/img/navigation/global_search_synonym.png %})

<!---

### Quick create campaigns

Search for channels to see quick create options among your top 10 results. For example, searching for "email" shows "Create Email Campaign" or "Create Transactional Email Campaign".

![][X]

--->

### 有効および下書き内容のフィルター

**Show active and 下書き only**を選択すると、検索結果にアクティブコンテンツと下書きコンテンツを含めることができます。デフォルトでは、切り替えが有効になっており、アーカイブ済みの内容を含むすべてのコンテンツが表示されます。

!["有効と下書きのみを表示"を切り替えます。]({% image_buster /assets/img/navigation/show_active_draft_new.png %})

### 絵文字の検索

Braze で作業に名前を付けるときに絵文字を使用している場合、絵文字を検索できます。絵文字を検索クエリとして使用できます。😎



