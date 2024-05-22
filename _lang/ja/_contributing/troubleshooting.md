---
nav_title: トラブルシューティング
article: Troubleshooting
description: "Braze Docs への投稿中に発生する可能性のある一般的な問題のトラブルシューティング手順。"
page_order: 9
noindex: true
---

# トラブルシューティング

> Braze Docs への投稿に問題がある場合は、まずこれらの一般的な問題を確認してください。発生している問題がリストにない場合は、[お知らせください](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=issue&projects=&template=report_an_issue.md&title=)。ここに追加させていただきます。

## リダイレクトが機能しない

[グローバルリダイレクトファイル (`assets/js/broken_redirect_list.js`) で設定したリダイレクトが機能しない場合は]({{site.baseurl}}/contributing/content_management/redirecting_urls/)、URL 文字列に大文字が含まれていないか再確認してください。見つかった場合は、それらを小文字に変換します (`_docs`ディレクトリ内の対応するファイル名に大文字が含まれていても)。

{% tabs local %}
{% tab before %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/contributing/home/';
```
{% endtab %}

{% tab after %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/contributing/home/';
```
{% endtab %}
{% endtabs %}

## クロスリファレンスリンクが 404 を返す

[ページ上の相互参照リンク]({{site.baseurl}}/contributing/content_management/cross_referencing/) (など`{% raw %}[Braze Developer Guide]({{site.baseurl}}/developer_guide/home){% endraw %}`) が 404 ページを返す場合は、URL で次の文字列を確認してください。

```plaintext
%7B%7Bsite.baseurl%7D%7D
```

この文字列を含む URL は以下のようになります。

```plaintext
https://www.braze.com/docs/user_guide/personalization_and_dynamic_content/connected_content/%7B%7Bsite.baseurl%7D%7D/user_guide/administrative/app_settings/message_activity_log_tab
```

URL にこの文字列が見つかった場合は、1 つ以上のクロスリファレンスリンクが [Liquid raw タグで囲まれています](https://shopify.dev/docs/api/liquid/tags/raw)。

{% tabs local %}
{% tab liquid raw tag %}
<code>
{% raw %} {% endraw %}
</code>
{% endtab %}
{% endtabs %}

これらのタグを移動して、未加工のまま表示したいLiquidコンテンツだけを囲むようにします。

{% tabs local %}
{% tab before %}
<code>
{% raw %} リキッドの <code> {{page\_title}} タグの使い方を学んでください。詳細については、「[Liquid タグ](&#123;&#123;site.baseurl}}/contributing/liquid/)」を参照してください。 {% endraw %}
</code>
{% endtab %}

{% tab after %}
<code>
リキッドの {% raw %} {{page\_title}} {% endraw %} タグの使い方を学んでください。詳細については、「[Liquid タグ](&#123;&#123;site.baseurl}}/contributing/liquid/)」を参照してください。
</code>
{% endtab %}
{% endtabs %}
