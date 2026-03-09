---
nav_title: コンテキスト変数
article_title: コンテキスト変数
page_type: reference
description: "この参考記事では、Braze Canvasesにおけるコンテキスト変数について、その種類、使用方法、およびベストプラクティスを説明する。"
---

# コンテキスト変数

> コンテキスト変数とは、特定のキャンバス内をユーザーが移動する過程で作成・使用できる一時的なデータである。それらは、遅延をパーソナライズしたり、ユーザーをダイナミックにセグメント化したり、メッセージングを充実させたりすることを可能にする。しかも、ユーザープロファイル情報を恒久的に変更することなく実現できる。コンテキスト変数はキャンバスセッション内でのみ存在し、異なるキャンバス間やセッション外では永続化されない。

## コンテキスト変数の仕組み

コンテキスト変数は二つの方法で設定できる：

- **キャンバスエントリで:**ユーザがキャンバスに入ると、イベントまたはAPI トリガのデータが自動的にコンテキスト変数に入力されます。
- **コンテキストステップで:**[コンテキストステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)を追加することで、キャンバス内でコンテキスト変数を手動で定義または更新できる。

各コンテキスト変数には以下が含まれます。

- 名前 (`flight_time` や`subscription_renewal_date` など)
- データ型（数値、文字列、時刻、配列など）
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)または**Add Personalization**ツールを使用して割り当てる値。

定義したコンテキスト変数は、キャンバス全体で {% raw %}`{{context.${example_variable_name}}}`{% endraw %} という形式で参照できます。

例えば、ユーザーのスケジュールされた{% raw %}`{{context.${flight_time}}}`{% endraw %}フライト時刻を返すことができる。

ユーザーがキャンバスにエントリするたびに (以前にキャンバスにエントリしたことがある場合でも)、コンテキスト変数は、最新のエントリデータとキャンバス設定に基づいて再定義されます。このステートフルなアプローチにより、各キャンバスエントリは独自の独立系コンテキストを維持できる。これにより、ユーザーは同一のジャーニー内で複数のアクティブな状態を保持しつつ、各状態固有のコンテキストを維持できる。

例えば、顧客が2つのフライトを予約している場合、2つの別々の旅程状態が同時に進行する。それぞれに、出発時刻や送信先といったフライト固有のコンテキスト変数が存在する。これにより、午後2時のニューヨーク行きのフライトについてはパーソナライズされたリマインダーを送信しつつ、明日の午前8時のロサンゼルス行きフライトについては別の更新情報を送信できる。こうして各メッセージが特定の予約に関連した内容となるのだ。

## 考慮事項

[コンテキストステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)ごとに最大10個のコンテキスト変数を定義できる。各変数名は最大100文字までで、英字、数字、またはアンダースコアのみを使用しなければならない。

コンテキスト変数の定義は最大10,240文字まで可能だ。APIによってトリガーされたキャンバスにコンテキスト変数を渡した場合、それらの変数はContextステップで作成された変数と同じ名前空間を共有する。例えば、[`/canvas/trigger/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)コンテキストオブジェクト`purchased_item`に変数 を送信した場合、それを として参照できる{% raw %}`{{context.${purchased_item}}}`{% endraw %}。その変数をコンテキストステップで再定義すると、新しい値がそのユーザーのジャーニーにおけるAPI値を上書きする。

コンテキストステップごとに最大50KBを保存できる。これは最大10個の変数に分散して保存される。ステップ内の全変数の合計サイズが50KBを超える場合、制限値を超えた変数は評価も保存も行われない。例えば、コンテキストステップに3つの変数がある場合：

- 変数１：30キロバイト
- 変数２：19キロバイト
- 変数３：2 KB

変数3は評価も保存もされない。前の変数の合計が50KBを超えているからだ。

## データ型

ステップで作成または更新されるコンテキスト変数には、次のデータ型を割り当てることができます。

{% alert note %}
コンテキスト変数は、カスタムイベントと同様のデータ型の形式を期待する。<br><br>配列型を使用する場合、Brazeはその値をJSONとして解析しようとする。これにより、オブジェクトの配列が正常に作成される。配列内のオブジェクトが有効なJSONでない場合、結果は単純な文字列の配列となる。<br><br>ネストされたオブジェクトやオブジェクトの配列には、[Liquid`as_json_string`フィルター](#converting-connected-content-strings-to-json)を使う。コンテキストステップで同じオブジェクトを作成する場合、そのオブジェクトをレンダリングする必要がある`as_json_string`。例えば、 {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| データタイプ | 変数名の例 | 値の例 |
|---|---|---|
|ブール値| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|数値| credit_score |{% raw %}<code>740</code>{% endraw %}|
|string| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|配列| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|配列（オブジェクトの）| pet_details |{% raw %}<code>[_mem_lt_br>_mem_amp_emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }_mem_lt_br>_mem_amp_emsp;,_mem_lt_br>_mem_amp_emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }_mem_lt_br>]</code>{% endraw %}|
|時間（UTC） | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|オブジェクト (フラット化) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

デフォルトでは、時刻データ型はUTCである。文字列データ型で時刻値を保存する場合、その時刻をPSTのような別のタイムゾーンとして定義できる。 

例えば、ユーザーの誕生日の前日にメッセージを送信する場合、その前日に送信するというLiquidロジックが関連しているため、コンテキスト変数を時間データ型として保存する。ただし、クリスマスの日（12月25日）に休日のメッセージを送る場合、時間をダイナミックな変数として参照する必要はない。したがって、文字列データ型を使用するのが望ましい。

## コンテキスト変数の使用

キャンバス内のLiquidを使用する場所ならどこでも、コンテキスト変数を使用できる。例えば[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step)ステップや[ユーザー更新]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update)ステップで「**パーソナライゼーションを追加**」を選択するだけでよい。

たとえば、次のフライトの前に、VIP ラウンジへのアクセスについて乗客に通知したいとします。このメッセージは、ファーストクラスのチケットを購入した乗客にのみ送信する必要があります。コンテキスト変数は、この情報を追跡する柔軟な方法です。

ユーザーは、飛行機のチケットを購入するときにキャンバスに入ります。ラウンジアクセスの適格性を判断するために、コンテキストステップで`lounge_access_granted`というコンテキスト変数を作成し、その後のユーザージャーニーのステップでそのコンテキスト変数を参照します。

![コンテキスト変数は、乗客がVIPラウンジの利用資格があるかどうかをトラッキングするために設定される。]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

このコンテキストステップでは、{% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} を使用して、購入したフライトのタイプが`first_class` かどうかを判断します。

次に、{% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} が`true` であるユーザーをターゲットにするメッセージステップを作成します。このメッセージは、パーソナライズされたラウンジ情報を含むプッシュ通知となる。このコンテキスト変数に基づいて、適格な乗客は、フライト前に関連するメッセージを受け取ります。

- ファーストクラスの乗客は次のメッセージを受け取ります:「Enjoy exclusive VIP lounge access!」
- ビジネスクラスとエコノミークラスの乗客は次のメッセージを受け取ります:「Upgrade your flight for exclusive VIP lounge access.」

![購入した航空券の種類に応じて、異なるメッセージを送信するメッセージステップ。]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
コンテキストステップの情報を使用して、[パーソナライズされた遅延オプション]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) を追加できます。つまり、ユーザーを遅延させる変数を選択できます。
{% endalert %}

### アクションパスと終了条件について

これらのトリガーアクションでは、コンテキスト変数またはカスタム属性のいずれかを使用してプロパティフィルターの比較を活用できる。[**カスタムイベントを実行**] または [**購入**] のいずれかを選択できます。これらのアクショントリガーは、基本プロパティとネストされたプロパティの両方に対するプロパティフィルターもサポートしている。 

- 基本プロパティとの比較では、利用可能な比較はカスタムイベントで定義されたプロパティの型に一致する。例えば、文字列プロパティは完全に一致する正規表現の一致を持つ。ブール値のプロパティは真か偽になる。 
- ネストされたプロパティとの比較では、型は事前定義されていない。そのため、ブール値、数値、文字列、時刻、年の日数といった複数のデータ型にわたる比較を選択できる。これは階層化カスタム属性の比較と同様である。比較時に、ネストされたプロパティの実際のデータ型と一致しないデータ型を選択した場合、ユーザーはアクションパスや終了条件に一致しない。

#### アクションパスの例

{% alert important %}
カスタム属性の比較では、アクションが実行された時点でのカスタム属性値を使用する。これは、比較時にこのカスタム属性が設定されていない場合、またはカスタム属性の値が定義されたプロパティ比較と一致しない場合、ユーザーがアクションパスのグループに一致しないことを意味する。ユーザーがアクションパスステップに入った時点で条件に合致していた場合でも、この現象は発生する。
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

以下のアクションパスは、カスタムイベントを実行したユーザーを、基本`Account_Created`プロパティをコンテキスト`source`変数に設定してソートするように`app_source_variable`設定されている。

![カスタムイベントを実行する際にコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

以下のアクションパスは、特定の製品名に対する基本`brand`プロパティ`shoes`をコンテキスト変数に一致させる`promoted_shoe_brand`ように設定されている。

![購入時にコンテキスト変数を参照するアクションパスの例だ。]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### 終了基準の例

{% tabs %}
{% tab Perform custom event %}

キャンバス内のユーザー行動において、以下のいずれかの条件を満たした場合、ユーザーはキャンバスから退出する。

- 彼らはカスタムイベント**「カート放棄」**を実行し、
- **カート内の**基本プロパティ「**Item」**は、コンテキスト変数の文字列値`cart_item_threshold`と一致する。

![コンテキスト変数に基づいてカスタムイベントを実行した場合にユーザーを退出させる退出条件を設定する。]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

キャンバス内のユーザー行動において、以下のいずれかの条件を満たした場合、ユーザーはキャンバスから退出する。

- 彼らは「本」という商品名で特定の購入を行う。
- その購入のネストされたプロパティは、ユーザーのカスタム"loyalty_program"属性「VIP」と等しい。

![購入した場合にユーザーを退出させる退出条件を設定する。]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### コンテキスト変数フィルター

[オーディエンスパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths)と[条件分岐]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)ステップでは、事前に宣言されたコンテキスト変数を使用するフィルターを作成できる。

{% alert note %}
コンテキスト変数フィルターは、オーディエンスパスと条件分岐ステップでのみ利用可能である。
{% endalert %}

コンテキスト変数はキャンバスのスコープ内で宣言され、アクセス可能となる。つまり、セグメント内では参照できない。コンテキスト変数フィルターは、オーディエンスパスと条件分岐ステップで同様の機能を持つ。オーディエンスパスステップは複数のグループを表し、条件分岐ステップは二値の決定を表す。

![条件分岐ステップの例。コンテキスト変数でフィルターを作成するオプション付き。]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

キャンバスのコンテキスト変数が事前定義された型を持つのと同様に、コンテキスト変数と静的値の比較では[データ型が一致]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types)していなければならない。コンテキスト変数フィルターは、ブール値、数値、文字列、時刻、および年の日数といった複数のデータ型間で比較を可能にする。これは、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/)に対する比較と同様である。

{% alert note %}
コンテキスト変数と比較には同じデータ型を使え。例えば、コンテキスト変数が時間データ型の場合、時間比較（例えば「前」や「後」など）を使う。データ型の不一致（例えば、時間コンテキスト変数との文字列比較など）を使用すると、予期しない動作を引き起こす可能性がある。
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

コンテキスト変数フィルターの一例を示す。コンテキスト`/braze/`変数`product_name`と正規表現を比較する。

![コンテキスト変数に正規表現「"product_name"/Braze/」に一致するフィルター設定だ。]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### コンテキスト変数やカスタム属性との比較

**コンテキスト変数またはカスタム属性との比較**トグルを選択することで、事前に定義されたコンテキスト変数やユーザーのカスタム属性と比較するコンテキスト変数フィルターを構築できる。これは、APIトリガーなどユーザーごとにダイナミックに比較を行う場合や、コンテキスト変数に`context`またがって定義された複雑な比較ロジックを簡略化するのに有用である。

{% tabs %}
{% tab Example 1 %}

例えば、ユーザーがダイナミックな期間アプリを利用していない場合に、パーソナライズされたリマインダーを送信したい場合を考えてみよう。具体的には、過去3日間アプリにログインしていないユーザー全員にメッセージが届くようにするのだ。

コンテキスト変数がある`re_engagement_date`。{% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %}それはとして定義されている。注意せよ、`3 days`は変数量であり、ユーザーのカスタム属性としても保存される。もし（ユーザープロファイルのカスタム属性として保存されている）`last_login_date`が`re_engagement_date`（）の後ろにある場合、そのユーザーにはメッセージが送信される。

![カスタム属性をパーソナライゼーションタイプとするフィルター設定。コンテキスト変数として、カスタム"re_engagement_date"属性の後に    "last_login_date".]({%image_buster/assets/img/context_variable_filter2.png%}) を追加する。

{% endtab %}
{% tab Example 2 %}

以下のフィルターは、コンテキスト変数  がコンテキスト`reminder_date`変数  より前にあるかどうか`appointment_deadline`を比較する。これにより、オーディエンスパスステップ内のユーザーをグループ分けし、予約期限前に追加のリマインダーを受け取るべきかどうかを判断できる。

![フィルター設定でコンテキスト変数に対するパーソナライゼーションタイプとしてコンテキスト"reminder_date"変数を用いたフィルター  コンテキスト変数/assets/img/context_variable_filter3.pngimage_buster"appointment_deadline".]({%    %})

{% endtab %}
{% endtabs %}

## タイムゾーンの一貫性に関する標準化

キャンバスでは、タイムスタンプ型を使用するイベントプロパティの大半は既にUTCで管理されているが、例外も存在する。Canvas Contextの追加により、アクションベースのキャンバスにおけるすべてのデフォルトのタイムスタンプイベントプロパティは、一貫してUTCで表示されるようになる。この変更は、キャンバスのステップやメッセージを編集する際の操作性をより予測可能で一貫性のあるものにするための、より広範な取り組みの一環である。この変更は、特定のキャンバスがコンテキストステップを使用しているかどうかに関わらず、すべてのアクションベースのキャンバスに影響を与えることに注意せよ。

{% alert important %}
いかなる状況においても、タイムスタンプを希望のタイムゾーンで表現するには、[Liquidtime_zoneフィルター]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)を使用することを強く推奨する。この[よくある質問は、コンテキストステップの記事で]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example)例として参照できる。
{% endalert %}

## 関連記事

- [コンテキストステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Liquidによるパーソナライゼーションとダイナミックなコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
