# Braze MCPサーバー

> BrazeのMCPサーバーについて学ぶ。このサーバーは、ClaudeやCursorのようなAIツールが、データを変更することなく、質問に答えたり、傾向を分析したり、インサイトを提供したりするために、非PIIのBrazeデータにアクセスできるようにする安全な読み取り専用接続である。

{% multi_lang_include mcp_server/beta_alert.md %}

## モデル・コンテキスト・プロトコル（MCP）とは何か？

​モデル・コンテキスト・プロトコル（MCP）は、AIエージェントが他のプラットフォームのデータに接続し、作業できるようにする標準である。大きく分けて2つの部分がある：

- **MCPクライアントだ：**CursorやClaudeなど、AIエージェントが動作するアプリケーション。
- **MCPサーバーだ：**Brazeのような別のプラットフォームが提供するサービスで、AIが使用できるツールやアクセスできるデータを定義する。

## Braze MCPサーバーについて

Braze MCPサーバーの設定]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %}) の後、エージェント、アシスタント、チャットボットなどのAIツールをBrazeに直接接続し、キャンバス＆キャンペーン分析、カスタム属性、セグメンテーションなどの集計データを読み取ることができる。BrazeのMCPサーバーは素晴らしい：

- Brazeのコンテキストを必要とするAI搭載ツールを構築する。
- マルチステップエージェントワークフローを作成するCRMエンジニア。
- テクニカルマーケターが自然言語によるクエリを試している。

Braze MCPサーバーは、ユーザープロファイルからデータを返さない38の読み取り専用エンドポイントをサポートしている。これらのエンドポイントの一部のみをAPIキーに割り当てることで、エージェントがアクセスできるデータをさらに制限することができる。

{% alert warning %}
APIキーに読み取り専用**以外の**権限を割り当てないこと。エージェントはBrazeにデータを書き込んだり削除しようとするかもしれないが、それは意図しない結果を引き起こす可能性がある。
{% endalert %}

## 使用例

ClaudeやCursorのようなツールを使って自然言語でBrazeと対話することができる。その他の例やベストプラクティスについては、[Braze MCPサーバーの使用]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}) を参照のこと。

{% tabs %}
{% tab Claude %}
![私が利用できるBrazeの機能は何ですか？]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![私の利用可能なBrazeの機能は何ですか」と尋ねられ、Cursorで答える。]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## よくある質問 (FAQ) {#faq}

### どのMCPクライアントがサポートされているか？

現在、[Claudeと](https://claude.ai/) [Cursorのみが](https://cursor.com/)公式にサポートされている。Braze MCPサーバーを使用するには、これらのクライアントのいずれかのアカウントが必要である。

### MCPクライアントがアクセスできるBrazeデータは？

MCPクライアントは、PIIを取得するために構築されていない読み取り専用のエンドポイントにのみアクセスできる。Brazeでデータを操作することはできない。

### MCPクライアントはBrazeデータを操作できるか？

MCPサーバーが公開するのは、PII以外の読み取り専用データを扱うツールだけだ。

### サードパーティのMCPサーバーをBrazeに使用できるか？

Brazeデータ用にサードパーティのMCPサーバーを使用することは推奨されない。[PyPiで](https://pypi.org/project/braze-mcp-server/)ホストされている公式Braze MCPサーバーのみを使用する。

### なぜBraze MCPサーバーはPIIや書き込みアクセスを提供しないのか？

データを保護しつつイネーブルメントを可能にするため、我々は読み取り専用で通常PIIを返さないエンドポイントに限定してサーバーを構築した。これにより、貴重なユースケースをサポートしながらリスクを軽減することができる。

### APIキーを再利用できるか？

いいえ。MCPクライアント用に新しいAPIキーを作成する必要がある。AIツールへのアクセスは、自分が納得できるものだけに限定し、権限の昇格は避けることを忘れないでほしい。

### Braze MCPサーバーはローカルでホストされているのか、それともリモートでホストされているのか？

Currents, Braze MCPサーバーはローカルでホストされている。

### なぜカーソルは機能だけをリストアップしているのか？

質問モードかエージェントモードかを確認する。MCPサーバーを使用するには、エージェントモードにする必要がある。

### エージェントが不正確と思われる回答を返した場合、どうすればよいか？

カーソルのようなツールで作業する場合、使用するモデルを変えてみるのもいいだろう。例えば、自動に設定されている場合は、特定のモデルに変更してみて、ユースケースに最適なパフォーマンスを発揮するモデルを実験してみよう。新しいチャットを開始して、プロンプトを再試行することもできる。 

問題が解決しない場合は、[mcp-product@braze.com](mailto:mcp-product@braze.com)までメールでお知らせいただきたい。可能であれば、動画を掲載し、通話機能を拡張して、エージェントがどのような通話を試みたかを確認できるようにしてほしい。

{% multi_lang_include mcp_server/legal_disclaimer.md %}
