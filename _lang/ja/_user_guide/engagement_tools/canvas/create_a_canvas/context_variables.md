---
nav_title: コンテキスト変数
article_title: コンテキスト変数
page_type: reference
description: "このリファレンス記事では、Braze Canvasesのコンテキスト変数について、その種類、使い方、ベストプラクティスなどを解説している。"
---

# コンテキスト変数

> コンテキスト変数とは、ユーザーが特定のキャンバス内を移動する際に、一時的に作成し使用できるデータのことである。これにより、ユーザーのプロファイル情報を永続的に変更することなく、遅延のパーソナライゼーション、ダイナミックなユーザーのセグメンテーション、メッセージングの充実が可能になる。コンテキスト変数はキャンバス・セッション内にのみ存在し、異なるキャンバス間やセッション外では持続しない。

## コンテキスト変数の仕組み

コンテキスト変数は2つの方法で設定できる：

- **キャンバスエントリで:**ユーザがキャンバスに入ると、イベントまたはAPI トリガのデータが自動的にコンテキスト変数に入力されます。
- **コンテキストステップで:**コンテキスト・[ステップを]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)追加することで、キャンバス内部でコンテキスト変数を手動で定義または更新することができる。

各コンテキスト変数には以下が含まれます。

- 名前 (`flight_time` や`subscription_renewal_date` など)
- データ型（数値、文字列、時刻、配列など）。
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)または**Add Personalization**ツールを使用して割り当てる値。

定義したコンテキスト変数は、キャンバス全体で {% raw %}`{{context.${example_variable_name}}}`{% endraw %} という形式で参照できます。

例えば、{% raw %}`{{context.${flight_time}}}`{% endraw %} 、ユーザーのスケジュールされたフライト時間を返すことができる。

ユーザーがキャンバスにエントリするたびに (以前にキャンバスにエントリしたことがある場合でも)、コンテキスト変数は、最新のエントリデータとキャンバス設定に基づいて再定義されます。このステートフルなアプローチにより、各キャンバスエントリーは独立系のコンテキストを維持することができ、ユーザーは各ステートに固有のコンテキストを保持しながら、同じ旅の中で複数のアクティブステートを持つことができる。

例えば、顧客に2つのフライトの予定がある場合、2つの別々のカスタマージャーニーの状態が同時に実行される。これにより、ニューヨーク行きの午後2時のフライトに関するパーソナライズされたリマインダーを送る一方で、ロサンゼルス行きの明日の午前8時のフライトに関する異なる更新を送ることができ、各メッセージが特定の予約に関連したものに保たれる。

## 考慮事項

[コンテキスト・ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)ごとに、最大10個のコンテキスト変数を定義できる。各変数名は100文字までで、文字、数字、アンダースコアのみを使用しなければならない。

コンテキスト変数の定義は10,240文字まで可能である。APIトリガーのキャンバスにコンテキスト変数を渡すと、コンテキストステップで作成された変数と同じ名前空間を共有する。例えば、[`/canvas/trigger/send` エンドポイントコンテキストオブジェクトで]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)変数`purchased_item` を送信した場合、{% raw %}`{{context.${purchased_item}}}`{% endraw %} として参照することができる。コンテキストのステップでその変数を再定義すると、新しい値はそのユーザーの旅のAPI値を上書きする。

コンテクスト・ステップごとに最大50KBまで保存でき、最大10変数に分散できる。ステップ内の全変数の合計サイズが50KBを超える場合、制限を超える変数は評価も保存もされない。例えば、コンテキスト・ステップに3つの変数があるとする：

- 変数1：30 KB
- 変数2：19 KB
- 変数3：2 KB

変数3は、前の変数の合計が50KBを超えるため、評価も保存もされない。

## データ型

ステップで作成または更新されるコンテキスト変数には、次のデータ型を割り当てることができます。

{% alert note %}
コンテキスト変数のデータ型は、[カスタムイベントと]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format)同じである。<br><br>array型を使用する場合、Brazeは値をJSONとしてパースしようとするため、オブジェクトの配列を正常に作成することができる。配列内のオブジェクトが有効なJSONでない場合、結果は単純な文字列の配列になる。<br><br>ネストしたオブジェクトやオブジェクトの配列には、[`as_json_string` Liquidフィルターを](#converting-connected-content-strings-to-json)使う。コンテキストのステップで同じオブジェクトを作成する場合は、`as_json_string` を使ってオブジェクトをレンダリングする必要がある。 {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| データタイプ | 変数名の例 | 値の例 |
|---|---|---|
|ブール値| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|数値| credit_score |{% raw %}<code>740</code>{% endraw %}|
|string| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|配列| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|オブジェクトの配列| pet_details |{% raw %}<code>[_mem_lt_br>_mem_amp_emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }_mem_lt_br>_mem_amp_emsp;,_mem_lt_br>_mem_amp_emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }_mem_lt_br>]</code>{% endraw %}|
|時間（UTC） | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|オブジェクト (フラット化) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

デフォルトでは、時刻のデータ型はUTCである。文字列データ型を使って時間値を格納する場合、PSTのような異なるタイムゾーンとして時間を定義することができる。 

例えば、ユーザーの誕生日の前日にメッセージを送信する場合、前日送信に関連するLiquidロジックがあるため、コンテキスト変数をtimeデータ型として保存する。しかし、クリスマス（12月25日）にホリデー・メッセージを送るのであれば、ダイナミックな変数として時刻を参照する必要はないだろうから、文字列データ型を使うのが望ましいだろう。

## コンテキスト変数を使う

**パーソナライゼーションを追加]**を選択すると、[メッセージや]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) [ユーザー更新]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update)ステップなど、キャンバスでリキッドを使用する任意の場所でコンテキスト変数を使用できる。

たとえば、次のフライトの前に、VIP ラウンジへのアクセスについて乗客に通知したいとします。このメッセージは、ファーストクラスのチケットを購入した乗客にのみ送信する必要があります。コンテキスト変数は、この情報を追跡する柔軟な方法です。

ユーザーは、飛行機のチケットを購入するときにキャンバスに入ります。ラウンジアクセスの適格性を判断するために、コンテキストステップで`lounge_access_granted`というコンテキスト変数を作成し、その後のユーザージャーニーのステップでそのコンテキスト変数を参照します。

![乗客がVIPラウンジを利用する資格があるかどうかを追跡するために設定されたコンテキスト変数。]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

このコンテキストステップでは、{% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} を使用して、購入したフライトのタイプが`first_class` かどうかを判断します。

次に、{% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} が`true` であるユーザーをターゲットにするメッセージステップを作成します。このメッセージは、パーソナライズされたラウンジ情報を含むプッシュ通知になる。このコンテキスト変数に基づいて、適格な乗客は、フライト前に関連するメッセージを受け取ります。

- ファーストクラスの乗客は次のメッセージを受け取ります:「Enjoy exclusive VIP lounge access!」
- ビジネスクラスとエコノミークラスの乗客は次のメッセージを受け取ります:「Upgrade your flight for exclusive VIP lounge access.」

![購入した航空券の種類によって送信するメッセージが異なるメッセージステップ。]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
コンテキストステップの情報を使用して、[パーソナライズされた遅延オプション]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) を追加できます。つまり、ユーザーを遅延させる変数を選択できます。
{% endalert %}

### アクションパスと終了基準について

これらのトリガーアクションでは、コンテキスト変数またはカスタム属性でプロパティフィルターを比較することができる：[**カスタムイベントを実行**] または [**購入**] のいずれかを選択できます。これらのアクショントリガーは、基本プロパティとネストされたプロパティの両方のプロパティフィルターにも対応している。 

- 基本プロパティと比較する場合、利用可能な比較はカスタムイベントによって定義されたプロパティのタイプと一致する。例えば、文字列プロパティは、正規表現と完全に一致する。ブール型プロパティは真か偽になる。 
- 階層化されたプロパティを比較する場合、型はあらかじめ定義されていないため、階層化されたカスタム属性の比較と同様に、真偽値、数値、文字列、時刻、曜日について、複数のデータ型にまたがる比較を選択することができる。比較時にネストされたプロパティの実際のデータ型と一致しないデータ型を選択した場合、ユーザーはアクションパスまたは終了基準に一致しない。

#### アクションパスの例

{% alert important %}
カスタム属性の比較では、アクションが実行された時点でのカスタム属性値を使用する。つまり、比較時にユーザーがこのカスタム属性を入力していない場合、またはカスタム属性値が定義されたプロパティ比較と一致しない場合、ユーザーはアクションパス・グループと一致しない。これは、ユーザーがアクションパスのステップに入ったときにマッチしていたとしても同様である。
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

以下のアクションパスは、基本プロパティ`source` を持つカスタムイベント`Account_Created` を実行したユーザーを、コンテキスト変数`app_source_variable` にソートするように設定されている。

![カスタムイベントを実行するときにコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

以下のアクションパスは、特定の製品名`shoes` の基本プロパティ`brand` をコンテキスト変数`promoted_shoe_brand` にマッチさせるように設定されている。

![購入時にコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### 終了基準の例

{% tabs %}
{% tab Perform custom event %}

終了基準とは、ユーザーがキャンバス内を移動するどの時点でも、以下の場合にキャンバスから退出するというものである：

- 彼らはカスタムイベント**Abandon Cartを**実行する。
- **Cartの**基本プロパティ**Itemは**、コンテキスト変数`cart_item_threshold` の文字列値と一致する。

![コンテキスト変数に基づき、ユーザーがカスタムイベントを実行した場合に終了するように設定された終了基準。]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

終了基準とは、ユーザーがキャンバス内を移動するどの時点でも、以下の場合にキャンバスから退出するというものである：

- 彼らは「本」という商品名のために特定の購入をする。
- その購入のネストされたプロパティ"loyalty_program" は、ユーザーのカスタム属性「VIP」と等しい。

![ユーザーが購入した場合に終了するように設定された終了基準。]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### コンテキスト変数フィルター

[オーディエンスパスと]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) [条件分岐]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)ステップで、以前に宣言したコンテキスト変数を使用するフィルターを作成できる。

{% alert note %}
コンテキスト変数フィルターは、オーディエンスパスと条件分岐ステップでのみ使用できる。
{% endalert %}

つまり、セグメンテーションの中で参照することはできない。オーディエンスパスのステップは複数のグループを表し、条件分岐のステップは二値決定を表す。

![条件分岐ステップの例。コンテキスト変数でフィルターを作成するオプションがある。]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

キャンバスのコンテキスト変数があらかじめ定義された型を持っているのと同様に、コンテキスト変数とスタティック値の比較も、[データ型が一致して]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types)いなければならない。コンテキスト変数フィルターは、階層[化されたカスタム属性の]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/)比較と同様に、ブーリアン、数値、文字列、時刻、曜日について、複数のデータ型にまたがる比較を可能にする。

{% alert note %}
コンテキスト変数と比較には同じデータ型を使う。例えば、コンテキスト変数が時間データ型の場合、時間比較（"before "や "after "など）を使う。不一致のデータ型（時間コンテキスト変数との文字列比較など）を使用すると、予期せぬ動作を引き起こす可能性がある。
{% endalert %}

以下は、コンテキスト変数`product_name` を正規表現`/braze/` と比較するコンテキスト変数フィルターの例である。

![コンテキスト変数"product_name" 、正規表現"/braze/"にマッチするフィルターを設定する。]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### コンテキスト変数やカスタム属性との比較

**コンテキスト変数またはカスタム属性と比較する**トグルを選択することにより、以前に定義されたコンテキスト変数またはユーザーカスタム属性と比較するコンテキスト変数フィルターを構築することができる。これは、APIトリガー（`context` ）のようにユーザーごとにダイナミックな比較を実行する場合や、コンテキスト変数にまたがって定義された複雑な比較ロジックを凝縮する場合に便利である。

{% tabs %}
{% tab Example 1 %}

例えば、過去3日間アプリにログインしていないユーザーを含むダイナミックな非アクティブ期間の後に、パーソナライズされたリマインダーをユーザーに送信したいとしよう。

コンテキスト変数`re_engagement_date` は、{% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} と定義されている。なお、`3 days` 、ユーザーのカスタム属性として保存されることもある。つまり、`re_engagement_date` （ユーザープロファイルのカスタム属性として保存されている）が`last_login_date` （ユーザープロファイルのカスタム属性として保存されている）の後であれば、メッセージが送られる。

![カスタム属性をパーソナライゼーション・タイプとするフィルター・セットアップ（コンテキスト変数"re_engagement_date" 、カスタム属性"last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %}の後)

{% endtab %}
{% tab Example 2 %}

次のフィルターは、コンテキスト変数`reminder_date` がコンテキスト変数`appointment_deadline` より前にあることを比較する。これは、オーディエンスパスのステップでユーザーをグループ化し、予約締め切り前に追加リマインダーを受け取るべきかどうかを判断するのに役立つ。

![コンテキスト変数のパーソナライゼーションタイプとしてコンテキスト変数を使ったフィルターセットアップ"reminder_date" on the context variable"appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## タイムゾーンの一貫性の標準化

タイムスタンプ・タイプを使用するほとんどのイベント・プロパティは、キャンバスではすでにUTCになっているが、いくつかの例外がある。キャンバス・コンテキストの追加により、アクションベースのキャンバスにおけるすべてのデフォルト・タイムスタンプ・イベント・プロパティは、一貫してUTCになる。この変更は、キャンバスのステップやメッセージを編集する際に、より予測しやすく一貫性のあるエクスペリエンスを保証するための幅広い取り組みの一環である。この変更は、特定のキャンバスがコンテキスト・ステップを使用しているかどうかにかかわらず、すべてのアクションベースのキャンバスに影響する。

{% alert important %}
どのような状況においても、タイムスタンプを希望のタイムゾーンで表現するために、[Liquidtime_zone フィルターを]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)使用することを強く推奨する。この[よくある質問は、コンテキスト・ステップの記事に]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example)例があるので参考にしてほしい。
{% endalert %}

## 関連記事

- [コンテキストステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Liquidによるパーソナライゼーションとダイナミックなコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)
