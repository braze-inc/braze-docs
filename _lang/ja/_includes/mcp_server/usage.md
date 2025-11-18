# Braze MCPサーバーを使用する

> ClaudeやCursorのようなツールを使って、自然言語を通してBrazeデータと対話する方法を学ぶ。より一般的な情報については、[Braze MCP server]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/){% endif %}.

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件

この機能を使用する前に、[Braze MCPサーバーの設定]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}.

## ベストプラクティス

ClaudeやCursorのような自然言語ツールを使ってBraze MCPサーバーを使用する場合、最良の結果を得るために以下のヒントに留意すること：

- LLMは間違いを犯す可能性があるので、必ず答えを再確認すること。
- データ分析では、必要な時間範囲を明確にする。より短い距離の方が、より正確な結果が得られることが多い。
- [Brazeの用語を](https://www.braze.com/resources/articles/glossary)正確に使い、LLMが正しい関数を呼び出せるようにする。
- 結果が不完全と思われる場合は、LLMに続行または深堀りするよう促す。
- クリエイティブなプロンプトを試してみよう！MCPクライアントによっては、CSVファイルやその他の便利なファイルをエクスポートできる場合もある。

## 使用例

[BrazeのMCPサーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}, ClaudeやCursorのようなツールを使って、自然言語を通してBrazeと対話することができる。以下はその例である：

### 私が利用できるBrazeの機能は？

{% tabs %}
{% tab クロード %}
![]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab カーソル %}
![]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### キャンバスIDの詳細を取得する

{% tabs %}
{% tab クロード %}
![]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab カーソル %}
![キャンバスIDの詳細を取得」がカーソルで質問され、回答される]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### 最近のキャンバスを見せてくれ

{% tabs %}
{% tab クロード %}
![最近のキャンバスを見せてください」クロードで問われ、答える]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab カーソル %}
![最近のキャンバスを表示する」カーソルでの質問と回答]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
