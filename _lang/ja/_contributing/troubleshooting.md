---
nav_title: トラブルシューティング
article: Troubleshooting
description: "Braze Docsへの投稿中に発生する可能性のある一般的な問題に対するトラブルシューティングのステップ。"
page_order: 9
noindex: true
---

# トラブルシューティング

> Braze Docsへの投稿に問題がある場合は、まずこれらの一般的な問題を確認してほしい。もしあなたが経験している問題が掲載されていない場合は、ここに追加することができるので[お知らせ](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=)いただきたい。

## リダイレクトが機能していない

グローバル・リダイレクト・ファイル(`assets/js/broken_redirect_list.js`)で設定した[リダイレクトが]({{site.baseurl}}/contributing/content_management/redirecting_urls/)機能していない場合は、URL文字列に大文字が含まれていないか再確認すること。もし見つかったら、（`_docs` ディレクトリの対応するファイル名に大文字が含まれていても）小文字に変換する。

{% tabs ローカル %}
{% tab 前に %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/contributing/home/';
```
{% endtab %}

{% tab 後に %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/contributing/home/';
```
{% endtab %}
{% endtabs %}

## 相互参照リンクは404を返す

あなたのページの[相互参照リンク]({{site.baseurl}}/contributing/content_management/cross_referencing/)（例えば`{% raw %}[Braze Developer Guide]({{site.baseurl}}/developer_guide/home){% endraw %}` ）が404ページを返す場合、URLに以下の文字列がないかチェックする。

```plaintext
%7B%7Bsite.baseurl%7D%7D
```

この文字列を含むURLは以下のようになる：

```plaintext
https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/%7B%7Bsite.baseurl%7D%7D/user_guide/administrative/app_settings/message_activity_log_tab
```

URLにこの文字列がある場合、相互参照リンクの1つ以上が[Liquid rawタグで](https://shopify.dev/docs/api/liquid/tags/raw)囲まれている。

{% tabs ローカル %}
{% tab Liquid rawタグで %}
<code>
&#123;% raw %} &#123;% endraw %}
</code>
{% endtab %}
{% endtabs %}

これらのタグを動かして、rawとして表示したいLiquidコンテンツだけを囲むようにする。

{% tabs ローカル %}
{% tab 前に %}
<code>
&#123;% raw %} Learn how to use Liquid's <code>&#123;&#123; page_title }} tag. For more information, see <mem_106f3a07-ce6d-47a8-961d-e39c7fd48182 href="#">Liquid tags</mem_106f3a07-ce6d-47a8-961d-e39c7fd48182>. &#123;% endraw %}
</code>
{% endtab %}

{% tab 後に %}
<code>
Learn how to use Liquid's &#123;% raw %} &#123;&#123; page_title }} &#123;% endraw %} tag. For more information, see <mem_c86a2785-7ad6-44d1-aa36-16905eff927d href="#">Liquid tags</mem_c86a2785-7ad6-44d1-aa36-16905eff927d>.
</code>
{% endtab %}
{% endtabs %}
