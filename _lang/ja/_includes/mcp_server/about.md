# Braze MCP サーバー

> クラウドやカーソルなどのAI ツールがPII 以外のBrazeデータにアクセスして、疑問に答えたり、傾向を分析したり、データを変更せずにインサイトを提供したりできる、安全で読み取り専用のBraze MCP サーバーについて説明します。

{% multi_lang_include mcp_server/beta_alert.md %}

## モデルコンテキストプロトコル(MCP)とは。

​モデルコンテキストプロトコル(MCP) は、AI エージェントが別のプラットフォームのデータに接続し、それを使用できるようにする規格です。主に2 つの部分があります。

- **クライアント:**カーソルやクロードなど、AI エージェントが実行されるアプリライセンス。
- **MCP サーバ:**Braze などの別のプラットフォームが提供するサービスで、AI が使用できるツールとアクセスできるデータを定義します。

## Braze MCP サーバーについて

[Braze MCP サーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide//user_guide/brazeai/mcp_server/setup/){%elsif include.section=="開発者;" %}({{site.baseurl}}/developer_/developer_guide/mcp_server/setup/){%endif %}など)を設定すると、エージェント、アシスタント、チャットボットなどのAI ツールをBraze に直結し、キャンバスやキャンペーン分析、カスタム属性s、SegmentsBraze MCP サーバーは次の用途に適しています。

- Brazeの文脈を必要とするAIを活用した工具の構築。
- マルチステップエージェントワークフローを作成するCRMエンジニア。
- 技術マーケターは自然言語の問い合わせを試みる。

Braze MCP サーバーは、Braze ユーザープロファイルs からデータを返さない38 個の読み取り専用エンドポイントs をサポートします。これらのエンドポイントの一部のみをBraze API キーに割り当てて、エージェントがアクセスできるデータ量をさらに制限することができます。

{% alert warning %}
**not** read-only という権限をAPI キーに割り当てないでください。エージェントは、意図しない結果を引き起こす可能性があるBrazeの書き込みや消去を試みることがあります。
{% endalert %}

## 使用例

クラウドやカーソルなどのツールを使用して、自然言語でBrazeを操作できます。他の事例やベストプラクティスについては、[Braze MCP サーバー]{% if include.section == "user" %}({{site.baseurl}}/user_guide/brazeai/mcp_server/usage/){% elsif include.section= "開発者" %}({{site.baseurl}}/developer_guide/mcp_server/usage/){% endif %}を参照してください。

{% tabs %}
{% tab クロード %}
![Claude.]({% image_buster /assets/img/mcp_server/claude/what_are_my_available_braze_functions.png %})で質問・回答されている「私のBraze機能は何ですか?」{: style="max-width:85%;"}
{% endtab %}

{% tab カーソル %}
![Cursor.]({% image_buster /assets/img/mcp_server/cursor/what_are_my_available_braze_functions.png %})で質問され回答されている「利用可能なBraze機能とは」
{% endtab %}
{% endtabs %}

## よくある質問 (FAQ) {#faq}

### どのMCPクライアントがサポートされていますか?

現在、[Claude](https://claude.ai/)と[Cursor](https://cursor.com/)のみが公式にサポートされています。Braze MCP サーバーを使用するには、次のいずれかのクライアントのアカウントが必要です。

### MCP クライアントはどのようなBraze情報にアクセスできますか?

MCP クライアント s は、PII を取得するために構築されていない読み取り専用エンドポイントにのみアクセスできます。Brazeでは操作できません。

### MCP クライアントはBrazeを操作できますか?

いいえ。MCP サーバーは、PII 以外の読み取り専用データを処理するツールのみを公開します。

### サードパーティ製のMCP サーバーをBrazeに使用できますか?

サードパーティ製のMCP サーバーをBrazeに使用することはお勧めしません。[PyPi](https://pypi.org/project/braze-mcp-server/) でホストされている正式なBraze MCP サーバーのみを使用してください。

### Braze MCP サーバーがPII または書き込みアクセスを提供しないのはなぜですか?

イノベーションを可能にしながらデータを保護するために、通常はPIIを返さない読み取り専用のエンドポイントに限定してサーバーを構築しました。これにより、価値あるユースケースをサポートしながら、危険性が低減されます。

### API キー s を再利用できますか?

いいえ。MCP クライアント用に新しいAPI キーを作成する必要があります。AI ツールが快適なものにアクセスできるようにし、権限の引き上げを避けることを忘れないでください。

### Braze MCP サーバーはローカルまたはリモートでホストされていますか?

現在、Braze MCP サーバーはローカルでホストされています。

### Cursor のみが機能をリストしているのはなぜですか?

「ask」モードか「agent」モードかを確認します。MCP サーバを使用するには、エージェントモードである必要があります。

### エージェントが不正確に見える回答を返す場合、どうすればよいですか?

Cursor などのツールを使用する場合は、使用するモデルを変更してみてください。たとえば、「自動」に設定している場合は、特定のモデルに変更して、ユースケースに最適なモデルを探してみてください。新しいチャットを開始してプロンプトを再試行することもできます。 

問題が解決しない場合は、[mcp-product@braze.com](mailto:mcp-product@braze.com) にメールしてお知らせください。できれば、動画を含め、呼び出し関数を展開して、エージェントが試行した呼び出しを確認できます。

{% multi_lang_include mcp_server/legal_disclaimer.md %}
