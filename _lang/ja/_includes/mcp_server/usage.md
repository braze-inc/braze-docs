# Braze MCPサーバーを使用する

> ClaudeやCursorといったツールを使って、自然言語でBrazeデータとやり取りする方法を学習しよう。より一般的な情報については、[Braze MCPサーバー]{% if include.section == "user" %}を参照せよ{{site.baseurl}}/user_guide/brazeai/mcp_server/){% elsif include.section == "developer" %}。{{site.baseurl}}/developer_guide/mcp_server/){% endif %}

{% multi_lang_include mcp_server/beta_alert.md %}

## 前提条件

この機能を使う前に、[Braze MCPサーバーの設定]{% if include.section == "user" %}が必要だ。{{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}{{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}

## ベストプラクティス

ClaudeやCursorのような自然言語ツールを通じてBraze MCPサーバーを使用する際は、最良の結果を得るために以下のポイントに注意せよ：

- 大規模言語モデルは間違いを犯すことがある。だから、その回答は必ず再確認することだ。
- データ分析では、必要な時間範囲を明確にせよ。短い距離の方が、より正確な結果を得られることが多い。
- [Brazeの](https://www.braze.com/resources/articles/glossary)正確な[用語](https://www.braze.com/resources/articles/glossary)を使用せよ。そうすればLLMが正しい関数を呼び出す。
- 結果が不完全に見える場合、LLMに続行または掘り下げを促せ。
- 創造的なプロンプトを試してみろ！MCPクライアントによっては、CSVファイルやその他の有用なファイルをエクスポートできる場合がある。

## 使用例

[Braze MCPサーバーの設定]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %})が完了したら、ClaudeやCursorといったツールを使って自然言語でBrazeとやり取りできる。始めにいくつか例を挙げておこう：

### 利用可能なBrazeの機能は何ですか？

{% tabs %}
{% tab Claude %}
![「利用可能なBrazeの機能は何か？」という質問がClaudeで尋ねられ、回答されている。]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![「利用可能なBraze機能は何か」という質問がCursorで尋ねられ、回答されている。]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

### キャンバス IDの詳細を確認する

{% tabs %}
{% tab Claude %}
![「キャンバスIDの詳細を取得する」という質問がClaudeで尋ねられ、回答されている。]({% image_buster /assets/img/mcp_server/claude/get_details_about_a_canvas_id.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![「キャンバスIDの詳細を取得する」という質問がCursorで問われ、回答されている。]({% image_buster /assets/img/mcp_server/cursor/get_details_about_a_canvas_id.png %})
{% endtab %}
{% endtabs %}

### 最近のキャンバスを見せてくれ

{% tabs %}
{% tab Claude %}
![「最近のキャンバスを見せてくれ」とクローズで尋ねられ、答えている。]({% image_buster /assets/img/mcp_server/claude/show_my_recent_canvases.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![「最近のキャンバスを見せてくれ」とカーソルで尋ねられ、答えている。]({% image_buster /assets/img/mcp_server/cursor/show_me_my_recent_canvases.png %})
{% endtab %}
{% endtabs %}

{% multi_lang_include mcp_server/legal_disclaimer.md %}
