---
nav_title: 記事全文
article_title: 記事全文
description: "この参考記事では、BrazeとFullstoryのパートナーシップについて概説している。"
alias: /partners/fullstory/
page_type: partner
search_tag: Partner
---

# 記事全文

フルストーリーの行動データプラットフォームは、テクノロジー・リーダーがより良い情報に基づいた意思決定を行えるよう支援する。デジタル行動データを分析スタックに注入することで、Fullstoryの特許取得済みテクノロジーは、質の高い行動データのパワーを大規模に引き出し、すべてのデジタル訪問をアクション可能なインサイトに変換する。 

*この統合はFullstoryによって維持されている。*

## この統合について
Braze内のFullstoryインサイトを活用して、ユーザーのWebサイトやアプリ体験の一瞬一瞬の画像を構築し、文脈に応じた状況に即したメッセージングを配信できる。FullstoryのセッションサマリーAPIは、ユーザーの閲覧行動に関する詳細なメタデータを取得し、キャンバスのような複数ステップのメッセージングジャーニーで使用する際に特に威力を発揮する。 

Fullstoryのセッションサマリーデータのリアルタイムの価値は、コネクテッドコンテンツを通じて最大限に活用される。コネクテッドコンテンツをキャンバスコンテキストステップで使用することで、ユーザーのキャンバスジャーニーを通してFullstoryのデータを保存し、その後のキャンバスステップで使用することができる。これにより、カスタムイベントやアトリビューションを通じてBrazeユーザープロファイルにこのデータを書き込む必要もなくなる。 

以下の例では、キャンバスコンテキストデータをエージェントAIキャンバスステップで活用し、ユーザーに放棄カートまたはカートを取り戻すよう促す最適なメッセージを生成している。しかし、データを活用してメッセージを直接パーソナライゼーションしたり、オーディエンスパスを介してユーザーのジャーニーを決定したり、後続のメッセージングステップで使用するコピーやアセットを決定したりすることができる。

## ユースケース

![BrazeとFullstoryの統合ユースケースを示す図]({% image_buster /assets/img/fullstory/1.png %})

## 前提条件

始める前に、以下のものが必要だ：

|必要条件     | 説明 |                        
|-----------------------|-----------------|
| Fullstory セッション API 認証トークン   | 以下のステップ1を参照のこと。  | 
| Braze コネクテッドコンテンツ認証トークンがイネーブルメントになっている。 | アーリーアクセスについては、下記を参照のこと。 |
| ブレイズキャンバスのコンテキストステップ |アーリーアクセスについては、下記を参照のこと。 |
| イネーブルメントAIエージェントステップ | アーリーアクセスについては、下記を参照のこと。|
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}

## フルストーリーの統合

### ステップ 1: セッションサマリーAPIイネーブルメントのためにFullstoryを設定する

#### A:セッションサマリーAPIエンドポイントの[認証トークンを](https://developer.fullstory.com/server/authentication/)取得する

FullstoryのAPIキーを作成するには、Fullstoryプラットフォームに移動し、**設定**>**APIキーに**移動する。**Standard**権限レベルを選択し、一度だけ表示されるキー値をすぐにコピーする。

#### B:セッション要約の作成 プロファイルID

[Fullstoryのガイダンスに従い](https://developer.fullstory.com/anywhere/activation/ai-session-summary-api/#step-1-creating-and-managing-summary-profiles)、専用エンドポイントを使用してセッションサマリープロファイルを作成する。ここで、セッションサマリーのレスポンスがBrazeに提供するデータの種類を定義する。
このリクエストに対するレスポンスで、Fullstoryはセッション「プロファイルID」を提供する。このプロファイルIDは、次のユースケースで使用されるコネクテッドコンテンツリクエストボディの重要な構成要素である。


### ステップ 2:コネクテッド・コンテンツ・トークン認証を作成する
1. Brazeで、**設定 > ワークスペース設定 > コネクテッドコンテンツ > 認証情報の追加 > トークン認証に**移動する。 

2. 認証名を「fullstory」とする。

3. ヘッダーキー「Authorization」を追加する。前のステップで入力したヘッダー値Fullstoryを入力する。 

4. 許可されたドメイン」の下に「api.fullstory.com」を入力する。

![認証情報の編集フィールドを示す Braze のスクリーンショット。]({% image_buster /assets/img/fullstory/2.png %})

## ユースケース:FullstoryセッションサマリーデータとBrazeキャンバスコンテキストステップおよびAIエージェントを活用し、ダイナミックなメッセージジャーニーを作成する。

Fullstoryの[Activation Streamsを](https://help.fullstory.com/hc/en-us/articles/360045134554-Streams)使えば、ユーザーとの重要なインタラクションの直後にBraze Canvasesをトリガーすることができる。この統合の威力は、システムがFullstoryからBrazeに自動的に渡す独自の`client_session_id` （{% raw %}`{{canvas_entry_properties.${client_session_id}}}`{% endraw %} ）にある。このIDがキーとなり、Brazeはユーザーが経験したセッションサマリーを完全に取得することができる。 

キャンバスコンテキストステップとコネクテッドコンテンツを活用することで、このIDを使用してFullstoryにAPIリクエストを行い、セッションデータを取得し、後で使用するために変数として保存することができる。 

![Braze キャンバスコンテキストステップのスクリーンショット。コンテキスト変数`summary_result` が作成され、Fullstoryへのコネクテッドコンテンツコールで入力され、セッションサマリーが取得されている。]({% image_buster /assets/img/fullstory/3.png %})

先に作成した認証トークンを使って、セッションサマリデータを引き出すために以下のリクエスト構造を使う。 

{% raw %}
```bash
{% connected_content https://api.fullstory.com/v2/sessions/{{canvas_entry_properties.${client_session_id} | url_encode}}/summary?config_profile=[YOUR-FULLSTORY-PROFILE-ID] :auth_credentials fullstory :save summary_result %}
{{summary_result | as_json_string }}
```
{% endraw %}

{% alert Note %}
 レスポンシブは、Liquid タグ{% raw %}`{{context.${summary_result}.response}}`{% endraw %} として保存される。このContextタグは、その後のキャンバスのステップで使用する。
{% endalert %}

この段階でキャンバスは、ユーザーセッションのメッセージペイロード全体を含む、コネクテッドコンテンツ呼び出しのレスポンスにアクセスできる。

{% details Example Payload from Session Summary API %}

{% raw %}
```bash
{
    "response": {
        "primary_goal": "User attempted to update payment method.",
        "issues_encountered": [
            "Received 'invalid card number' error twice.",
            "Clicked 'Submit' button multiple times with apparent frustration (based on event patterns)."
        ],
        "final_action": "Navigated away from payment page to dashboard.",
        "reason_for_termination_suggestion": "Could not update payment method successfully.",
        "help_pages_visited": [
            "/help/payment-errors"
        ]
    },
    "response_schema": {
        "type": "OBJECT",
        "properties": {
            "primary_goal": {
                "type": "STRING",
                "description": "A summary of the user's main objective during the session."
            },
            "issues_encountered": {
                "type": "ARRAY",
                "description": "A list of problems or errors the user faced.",
                "items": {
                    "type": "STRING",
                    "description": "A description of a single issue."
                }
            },
            "final_action": {
                "type": "STRING",
                "description": "The last significant action the user took before the session ended."
            },
            "reason_for_termination_suggestion": {
                "type": "STRING",
                "description": "A suggested reason for why the user ended their session."
            },
            "help_pages_visited": {
                "type": "ARRAY",
                "description": "A list of URLs for help or documentation pages the user visited.",
                "items": {
                    "type": "STRING",
                    "description": "The URL of a help page."
                }
            }
        },
        "required": [
            "primary_goal",
            "issues_encountered",
            "final_action",
            "reason_for_termination_suggestion",
            "help_pages_visited"
        ]
    }
}
```
{% endraw %}
{% enddetails %}

ユーザーキャンバスジャーニーの後半でコンテキストLiquidタグを使用して、上記のオブジェクトで利用可能なデータのいずれかを活用することができる。以下のステップは、[AIエージェントキャンバスステップで](https://www.braze.com/docs/user_guide/engagement_tools/canvas/canvas_components/agent_step)このデータを使用する方法を示している。

{% alert Note %}
予期しない動作を避けるために、オーディエンス・パス・ステップをコンテキスト・ステップの後に含める。このステップでは、コネクテッド・コンテンツの呼び出しが失敗したか、そうでなければ情報が返されなかったことを示すコンテキスト・タグが空の場合、ユーザーをコンテキストから外すことができる。

![Brazeオーディエンスステップのスクリーンショット]({% image_buster /assets/img/fullstory/3.png %})

{% endalert %}

## Fullstoryのペイロードを分析し、ユースケースに適したコピーを作成できるAIエージェントを作成する。

[Brazeのエージェントガイダンスでは]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents)、BrazeユーザーがどのようにAIエージェントを作成できるかを概説している。FullstoryによってトリガーされたキャンバスにAIエージェントのステップを挿入し、上記で説明したキャンバスのコンテキストステップを含めることで、ユーザーはAIエージェントにFullstoryのセッションサマリーデータをフィードすることができ、様々な目的に使用することができる。 

この例では、このデータを使用して、AIエージェントがコンテンツカードで使用する適切なメッセージコピーを生成し、ユーザーに放棄されたバスケットに戻るよう促すことができる。

![プロンプトが表示されたBraze Agent Context creatorのスクリーンショット]({% image_buster /assets/img/fullstory/4.png %})

このステップで作成されたContext Liquidタグには、先に作成されたAIエージェントステップで使用されたContext Liquidタグと同じ名前を使用する。 

ユースケースによって必要なプロンプトは異なるが、効果的なエージェントプロンプトを作成するためのベストプラクティスについては、*エージェントの作成における* [指示の書き方を]({{site.baseurl}}/docs/user_guide/brazeai/agents/creating_agents/#writing-instructions)参照のこと。 


キャンバスで、AIエージェントのステップを選択し、ドロップダウンメニューから作成された "セッションコンテキスト "エージェントを選択する。出力を変数として保存する。このケースは "メッセージ "で、ユースタグ{% raw %}`{{context.${message}.message}}`{% endraw %} を使ってメッセージコピーに入れることができる。

![Braze Agent Context Canvasステップのスクリーンショット（プロンプトが表示されている]({% image_buster /assets/img/fullstory/5.png %})

AIエージェントが作成したコピーを活用するメッセージステップを作成する。このステップではLiquidタグを使用する。 

{% alert Note %}

FullstoryのセッションサマリーAPIは、識別可能なユーザーデータを返す可能性がある。PII (パーソナライズされた識別子)を扱いながらコンプライアンスを確保するために、このユースケースを活用する前に、FullstoryのデータキャプチャルールからPIIが除外されていることを確認すること。

{% endalert %}