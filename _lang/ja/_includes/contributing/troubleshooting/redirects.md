グローバル・リダイレクト・ファイル(`assets/js/broken_redirect_list.js`)で[設定したリダイレクトが]({{site.baseurl}}/contributing/content_management/redirecting_urls/)機能していない場合は、URL文字列に大文字が含まれていないか再確認すること。もし見つかったら、（`_docs` ディレクトリの対応するファイル名に大文字が含まれていても）小文字に変換する。

{% tabs local %}
{% tab before %}
```javascript
validurls['/docs/hidden/WIP_Partnerships/WIP_Guidelines'] = '/docs/feedback/';
```
{% endtab %}

{% tab after %}
```javascript
validurls['/docs/hidden/wip_partnerships/wip_guidelines'] = '/docs/feedback/';
```
{% endtab %}
{% endtabs %}
