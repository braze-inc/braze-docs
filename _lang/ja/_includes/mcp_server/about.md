# Braze MCPサーバー

> Braze MCPサーバーについて学習しよう。これは安全な読み取り専用接続であり、ClaudeやCursorのようなAIツールが非PIIのBrazeデータにアクセスして質問に答え、傾向を分析し、データを変更せずにインサイトを提供することを可能にする。

{% multi_lang_include mcp_server/beta_alert.md %}

## モデルコンテキストプロトコル（MCP）とは何か？

​モデルコンテキストプロトコル（MCP）とは、AIエージェントが別のプラットフォームのデータに接続し、そのデータと連動できるようにする規格である。それは主に二つの部分から成っている：

- **MCPクライアント：**AIエージェントが動作するアプリケーション、例えばCursorやClaudeなど。
- **MCPサーバー：**別のプラットフォーム（例えばBrazeなど）が提供するサービスであり、AIが使用できるツールとアクセス可能なデータを定義するものだ。

## Braze MCPサーバーについて

[Braze MCPサーバーの設定]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/setup/){% elsif include.section == "developer" %}({{site.baseurl}}/developer_guide/mcp_server/setup/){% endif %})後、エージェントやアシスタント、チャットボットなどのAIツールをBrazeに直接接続できる。これにより、キャンバスやキャンペーン分析、カスタム属性、セグメントなどの集計データをAIツールが読み取れるようになる。Braze MCPサーバーは以下に最適だ：

- Brazeのコンテキストを必要とするAI搭載ツールを構築する。
- CRMエンジニアが複数のステップからなるエージェントワークフローを開発している。
- 技術系マーケターが自然言語クエリの実験を行っている。

Braze MCPサーバーは、Brazeユーザープロファイルからデータを返さない読み取り専用エンドポイントを38個サポートしている。これらのエンドポイントの一部のみをBraze API キーに割り当てることで、エージェントがアクセスできるデータをさらに制限できる。

{% alert warning %}
API キーに読み取り専用**以外の**権限を割り当ててはならない。エージェントはBraze内でデータの書き込みや削除を試みる可能性がある。これにより意図しない結果が生じる恐れがある。
{% endalert %}

## 使用例

Brazeとは、ClaudeやCursorのようなツールを使って自然言語でやり取りできる。その他の例やベストプラクティスについては、[Braze MCPサーバーの使用方法]{% if include.section == "user" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}{{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section == "developer" %}を参照せよ。

{% tabs %}
{% tab Claude %}
![「利用可能なBrazeの機能は何か？」という質問がClaudeで尋ねられ、回答されている。]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %}){: style="max-width:85%;"}
{% endtab %}

{% tab Cursor %}
![「利用可能なBraze機能は何か」という質問がCursorで尋ねられ、回答されている。]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})
{% endtab %}
{% endtabs %}

## よくある質問 (FAQ) {#faq}

### どのMCPクライアントがサポートされているのか？

正式にサポートされている[のはクロード](https://claude.ai/)と[カーソル](https://cursor.com/)だけだ。これらのクライアントのいずれかのアカウントを持っている必要がある。そうしなければ、Braze MCPサーバーを利用できない。

### MCPクライアントは、Brazeのどのデータにアクセスできるのか？

MCPクライアントは、個人識別情報（PII）を取得する目的で構築されていない読み取り専用エンドポイントにのみアクセスできる。彼らはBrazeでデータを操作できない。

### MCPクライアントはBrazeデータを操作できるか？

いいえ。MCPサーバーが公開しているのは、非個人識別情報（非PII）の読み取り専用データを扱うツールのみである。

### BrazeでサードパーティのMCPサーバーを使えるか？

BrazeデータにサードパーティのMCPサーバーを使用することは推奨されない。[PyPi](https://pypi.org/project/braze-mcp-server/)でホストされている公式のBraze MCPサーバーのみを使用すること。

### なぜBraze MCPサーバーは個人識別情報（PII）や書き込みアクセスを提供しないのか？

データを保護しつつイノベーションをイネーブルメントするため、サーバーは読み取り専用かつ通常は個人識別情報（PII）を返さないエンドポイントに限定されている。これはリスクを減らしつつ、価値あるユースケースを支える。

### API キーは再利用できるか？

いいや。MCPクライアント用に新しいAPI キーを作成する必要がある。AIツールには、自分が許容できる範囲のデータのみをアクセスさせるように注意し、権限の昇格は避けること。

### Braze MCPサーバーはローカルでホストされているのか、それともリモートでホストされているのか？

Braze MCPサーバーはローカルでホストされている。

### カーソルが関数だけをリストしているのはなぜだ？

自分が質問モードかエージェントモードか確認しろ。MCPサーバーを使用するには、エージェントモードである必要がある。

### エージェントが間違っていると思われる答えを返してきたら、どうすればいいか？

カーソルのようなツールを使う時、使っているモデルを変えてみるといいかもしれない。例えば、自動設定にしているなら、特定のモデルに変更してみて、そのモデルのパフォーマンスが自分のユースケースに最適か試してみることだ。新しいチャットを始めて、プロンプトを再試行してみるのも手だ。 

問題が解決しない場合は、[mcp-product@](mailto:mcp-product@braze.com) までメールで[braze.com](mailto:mcp-product@braze.com)連絡してくれ。可能であれば、動画を含め、通話機能を拡張して、エージェントが試みた通話を確認できるようにしてほしい。

{% multi_lang_include mcp_server/legal_disclaimer.md %}
