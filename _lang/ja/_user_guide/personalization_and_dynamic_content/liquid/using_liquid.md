---
nav_title: 液体を使用する
article_title: リキッドユースケースと概要
page_order: 0
description: "この参考記事では、Liquidの一般的なユースケースの概要と、Liquidタグをメッセージングに組み込む方法について説明します。"
search_rank: 2
---

# [![Braze Learning course]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/path/dynamic-personalization-with-liquid){: style="float:right;width:120px;border:0;" class="noimgborder"}液体を使用する

{% raw %}

> メッセージングに個人情報を動的に挿入するために使用できるさまざまなユーザー属性があります。

メッセージに次のテキストを含めると`{{${first_name}}}`、メッセージが送信されるときに、（ユーザーのプロファイルから取得された）ユーザーの名が置き換えられます。カスタム属性の値を使用する場合は、変数に名前空間「custom\_attribute」を追加する必要があります。たとえば、「zip code」という名前のカスタム属性を使用するには、`{{custom_attribute.${zip code}}}`メッセージに含めます。

使用可能な値に応じて、次の値をメッセージに置き換えることができます。

- [基本ユーザー情報][1] (例:`first_name`、`last_name`、`email_address`)
- [カスタム属性][2]
- [カスタムイベントプロパティ][11]
- [最近使用したデバイス情報][39]
- [ターゲットデバイス情報][40]

Braze [Connected Content経由でウェブサーバーから直接コンテンツを取得することもできます][9]。
{% endraw %}

{% alert important %}
Brazeは現在、**Shopifyのリキッド5までのリキッドをサポートしています**。
{% endalert %}

## 液体を使用する

{% raw %}

[使用可能なLiquidタグがわかったら][1]、Liquidを使用するとメッセージのパーソナライゼーションを驚くほど高めることができます。Liquidタグはメッセージ内のプレースホルダーとして機能し、ユーザーのアカウントから同意した情報を引き出し、パーソナライズや適切なメッセージングプラクティスを可能にします。

次のブロックでは、ユーザーのファーストネームを呼び出すためのLiquidタグと、ユーザーがファーストネームを登録しない場合のデフォルトタグを二重に使用していることがわかります。

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Janet Doe という名前のユーザーには、メッセージは次のいずれかとして表示されます。

```
Hi Janet, thanks for using the App!
```

または

```
Hi Valued User, thanks for using the App!
```

### リキッド構文

Liquidは特定の構造または構文に従っているため、動的パーソナライゼーションを作成する際に留意する必要があります。覚えておくべき基本的なルールは次のとおりです。

1. **Braze ではストレートクォートを使う:**カーリークォート (**'') とストレートクォート ('****'**) には違いがあります。リキッド・イン・ブレイズではストレートクォート (**''**) を使用してください。特定のテキストエディターからコピーして貼り付けるときにカーリークォートが表示されることがあり、Liquidで問題が発生する可能性があります。Braze ダッシュボードに見積もりを直接入力する場合は問題ありません。
2. **ブラケットはペアになっています。**すべての括弧は **{}** を開いたり閉じたりする必要があります。必ず中括弧を使用してください！
3. **ステートメントがペアになっている場合:**いずれの場合も`if`、`endif``if`ステートメントが終了したことを示すにはが必要です。

### タグを挿入する

任意のメッセージに2つの開いた中括弧を入力することでタグを挿入できます。これにより、`{{`入力中に更新され続けるオートコンプリート機能が起動します。入力時に表示されるオプションから変数を選択することもできます。

カスタムタグを使用している場合は、タグをコピーして任意のメッセージに貼り付けることができます。

{% endraw %}

{% alert note %}

メールメッセージでLiquidを使用する場合は、次の点を確認してください。

1. 従来のエディターではなく、HTML エディターを使用して挿入します。クラシックエディターはLiquidをプレーンテキストとして解析することがあります。
2. `<body>`Liquidコードはタグ内にのみ配置してください。このタグの外に配置すると、配信時にレンダリングに一貫性がなくなる可能性があります。

{% endalert %}

{% raw %}


### 事前にフォーマットされた変数

テンプレート化されたテキストフィールドの右上にある「パーソナライゼーション属性の挿入」モーダルを使用して、事前にフォーマットされた変数をデフォルトで挿入できます。

![Liquid in Braze をサポートするテキストフィールドにパーソナライゼーション属性を挿入するためのプラスボタン] [44]{: style="max-width:70%;"}

モーダルは、カーソルが置かれた位置に、指定されたデフォルト値でLiquidを挿入します。挿入ポイントはプレビューボックスでも指定できます。プレビューボックスには変更前と変更後のテキストが表示されます。テキストのブロックが強調表示されている場合、強調表示されたテキストが置き換えられます。

![パーソナライゼーションを挿入] をクリックした後に表示されるパーソナライゼーションモーダルを追加。モーダルにはパーソナライゼーションタイプ、属性、オプションのデフォルト値のフィールドがあり、Liquid構文のプレビューが表示されます。] [45]

{% endraw %}

### 変数を割り当てる

{% raw %}
Liquidの一部の操作では、操作したい値を変数として保存する必要があります。これは、Liquidステートメントに複数の属性、イベントプロパティ、またはフィルターが含まれている場合によく見られます。

たとえば、2 つのカスタムデータ整数を加算するとします。以下を単純に使用することはできません。

```liquid
{{custom_attribute.${one}}} | plus: {{custom_attribute.${two}}}
```

このLiquidは、1行で複数の属性を参照できないため機能しません。数学関数を実行する前に、これらの値の少なくとも1つに変数を割り当てる必要があります。2 つのカスタム属性を追加するには、2 行の Liquid が必要です。1 行はカスタム属性を変数に割り当てる行で、もう 1 行は追加を実行するためのものです。

#### 例:

たとえば、ギフトカードの残高とリワード残高を足して、ユーザーの現在の残高を計算してみましょう。

まず、`assign`タグを使用して、`current_rewards_balance`のカスタム属性を「balance」という用語に置き換えます。これで、という名前の変数が作成され`balance`、これを操作できるようになりました。

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
```

次に、`plus`フィルターを使用して、各ユーザーのギフトカード残高とリワード残高（`{{balance}}`で示されます）を組み合わせます。

```liquid
{% assign balance = {{custom_attribute.${current_rewards_balance}}} %}
You have ${{custom_attribute.${giftcard_balance} | plus: {{balance}}}} to spend!
```
{% endraw %}

{% alert tip %}
すべてのメッセージに同じ変数を割り当てていることに気づきましたか？`assign`タグを何度も書き出す代わりに、そのタグをコンテンツブロックとして保存し、代わりにメッセージの上部に配置できます。

1. [コンテンツブロックを作成します]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/#create-a-content-block)。
2. コンテンツブロックに名前を付けます (スペースや特殊文字は使用しないでください)。
3. ページの下部にある [**編集**] をクリックします。
4. `assign`タグを入力します。

コンテンツブロックがメッセージの上部にある限り、変数がオブジェクトとしてメッセージに挿入されるたびに、選択したカスタム属性が参照されます。
{% endalert %}

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/
[9]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/
[11]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[39]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#most-recently-used-device-information
[40]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/#targeted-device-information
[44]: {% image_buster /assets/img_archive/insert_liquid_var_arrow.png %}
[45]: {% image_buster /assets/img_archive/insert_var_shot.png %}
