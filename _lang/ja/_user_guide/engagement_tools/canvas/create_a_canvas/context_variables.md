---
nav_title: コンテキスト変数
article_title: コンテキスト変数
page_type: reference
description: "この参考記事では、Braze キャンバスにおけるコンテキスト変数について、その種類、使用方法、およびベストプラクティスを説明します。"
---

# コンテキスト変数

> コンテキスト変数とは、特定のキャンバス内をユーザーが移動する過程で作成・使用できる一時的なデータです。遅延をパーソナライズしたり、ユーザーをダイナミックにセグメント化したり、メッセージングを充実させたりすることが、ユーザープロファイル情報を恒久的に変更することなく実現できます。コンテキスト変数はキャンバスセッション内でのみ存在し、異なるキャンバス間やセッション外では永続化されません。

## コンテキスト変数の仕組み

コンテキスト変数は2つの方法で設定できます。

- **キャンバスエントリ時：**ユーザーがキャンバスに入ると、イベントまたは API トリガーのデータが自動的にコンテキスト変数に入力されます。
- **コンテキストステップ内：**[コンテキストステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context)を追加することで、キャンバス内でコンテキスト変数を手動で定義または更新できます。

各コンテキスト変数には以下が含まれます。

- 名前（`flight_time` や `subscription_renewal_date` など）
- データタイプ（数値、文字列、時刻、配列など）
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) または**パーソナライゼーションを追加**ツールを使用して割り当てる値

定義したコンテキスト変数は、キャンバス全体で {% raw %}`{{context.${example_variable_name}}}`{% endraw %} という形式で参照できます。

例えば、{% raw %}`{{context.${flight_time}}}`{% endraw %} はユーザーのスケジュールされたフライト時刻を返すことができます。

ユーザーがキャンバスにエントリするたびに（以前にエントリしたことがある場合でも）、コンテキスト変数は最新のエントリデータとキャンバス設定に基づいて再定義されます。このステートフルなアプローチにより、各キャンバスエントリは独自の独立したコンテキストを維持できます。これにより、ユーザーは同一のジャーニー内で複数のアクティブな状態を保持しつつ、各状態固有のコンテキストを維持できます。

例えば、顧客が2つのフライトを予約している場合、2つの別々のジャーニー状態が同時に進行します。それぞれに、出発時刻や目的地といったフライト固有のコンテキスト変数が存在します。これにより、午後2時のニューヨーク行きのフライトについてはパーソナライズされたリマインダーを送信しつつ、明日の午前8時のロサンゼルス行きフライトについては別の更新情報を送信できます。こうして各メッセージが特定の予約に関連した内容となります。

## 考慮事項

[コンテキストステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)ごとに最大10個のコンテキスト変数を定義できます。各変数名は最大100文字までで、英字、数字、またはアンダースコアのみを使用する必要があります。

コンテキスト変数の定義は最大10,240文字まで可能です。API によってトリガーされたキャンバスにコンテキスト変数を渡した場合、それらの変数はコンテキストステップで作成された変数と同じ名前空間を共有します。例えば、[`/canvas/trigger/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)のコンテキストオブジェクトに変数 `purchased_item` を送信した場合、それを {% raw %}`{{context.${purchased_item}}}`{% endraw %} として参照できます。その変数をコンテキストステップで再定義すると、新しい値がそのユーザーのジャーニーにおける API 値を上書きします。

コンテキストステップごとに最大50KBを保存でき、これは最大10個の変数に分散して保存されます。ステップ内の全変数の合計サイズが50KBを超える場合、制限値を超えた変数は評価も保存も行われません。例えば、コンテキストステップに3つの変数がある場合：

- 変数1：30KB
- 変数2：19KB
- 変数3：2KB

変数3は評価も保存もされません。前の変数の合計が50KBを超えているためです。

## データタイプ

ステップで作成または更新されるコンテキスト変数には、次のデータタイプを割り当てることができます。

{% alert note %}
コンテキスト変数は、[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format)と同様のデータタイプの形式が期待されます。<br><br>配列型を使用する場合、Braze はその値を JSON として解析しようとします。これにより、オブジェクトの配列が正常に作成されます。配列内のオブジェクトが有効な JSON でない場合、結果は単純な文字列の配列となります。<br><br>ネストされたオブジェクトやオブジェクトの配列には、[`as_json_string` Liquid フィルター](#converting-connected-content-strings-to-json)を使用してください。コンテキストステップで同じオブジェクトを作成する場合、`as_json_string` を使用してオブジェクトをレンダリングする必要があります。例えば、{%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| データタイプ | 変数名の例 | 値の例 |
|---|---|---|
|ブール値| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|数値| credit_score |{% raw %}<code>740</code>{% endraw %}|
|文字列| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|配列| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|配列（オブジェクトの）| pet_details |{% raw %}<code>[<br>&emsp;{ "id": 1, "type": "dog", "breed": "beagle", "name": "Gus" }<br>&emsp;,<br>&emsp;{ "id": 2, "type": "cat", "breed": "calico", "name": "Gerald" }<br>]</code>{% endraw %}|
|時間（UTC）| last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|オブジェクト（フラット化）| user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

デフォルトでは、時刻データタイプは UTC です。文字列データタイプで時刻値を保存する場合、その時刻を PST のような別のタイムゾーンとして定義できます。

例えば、ユーザーの誕生日の前日にメッセージを送信する場合、前日に送信するという Liquid ロジックが関連しているため、コンテキスト変数を時間データタイプとして保存します。ただし、クリスマスの日（12月25日）にホリデーメッセージを送る場合、時間をダイナミックな変数として参照する必要はないため、文字列データタイプを使用するのが望ましいです。

オブジェクトデータタイプの場合、ドット記法を使用してデータ内のパスを指定できます。例えば、コンテキストステップで以下の構造を持つコンテキスト変数 `order_summary` を定義した場合：

```json
{
  "shipping": {
    "carrier": "overnight"
  }
}
```

[オーディエンスパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/)や[条件分岐]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/)フィルターでは、ドット記法を使用してコンテキスト変数名としてパスを入力します（例：`order_summary.shipping.carrier`）。フィルターが評価されると、Braze はそのパスを値 `overnight` に解決します。

Liquid 内（[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)ステップなど）では、代わりに {% raw %}`{{context.${order_summary}.shipping.carrier}}`{% endraw %} を使用してください。

## コンテキスト変数の使用

キャンバス内の Liquid を使用する場所ならどこでも、コンテキスト変数を使用できます。例えば[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step)ステップや[ユーザー更新]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/user_update)ステップで**パーソナライゼーションを追加**を選択するだけです。アプリ内メッセージやメッセージステップ内のバナーでは、コンテキスト変数を選択してメッセージの有効期限を決定できます。

例えば、次のフライトの前に VIP ラウンジへのアクセスについて乗客に通知したいとします。このメッセージは、ファーストクラスのチケットを購入した乗客にのみ送信する必要があります。コンテキスト変数は、この情報を追跡する柔軟な方法です。

ユーザーは、飛行機のチケットを購入するときにキャンバスに入ります。ラウンジアクセスの適格性を判断するために、コンテキストステップで `lounge_access_granted` というコンテキスト変数を作成し、その後のユーザージャーニーのステップでそのコンテキスト変数を参照します。

![コンテキスト変数は、乗客が VIP ラウンジの利用資格があるかどうかをトラッキングするために設定されます。]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

このコンテキストステップでは、{% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} を使用して、購入したフライトのタイプが `first_class` かどうかを判断します。

次に、{% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} が `true` であるユーザーをターゲットにするメッセージステップを作成します。このメッセージは、パーソナライズされたラウンジ情報を含むプッシュ通知となります。このコンテキスト変数に基づいて、適格な乗客はフライト前に関連するメッセージを受け取ります。

- ファーストクラスの乗客は次のメッセージを受け取ります：「Enjoy exclusive VIP lounge access!」
- ビジネスクラスとエコノミークラスの乗客は次のメッセージを受け取ります：「Upgrade your flight for exclusive VIP lounge access.」

![購入した航空券の種類に応じて、異なるメッセージを送信するメッセージステップ。]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
コンテキストステップの情報を使用して、[パーソナライズされた遅延オプション]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays)を追加できます。つまり、ユーザーを遅延させる変数を選択できます。
{% endalert %}

### アクションパスと終了条件について

これらのトリガーアクションでは、コンテキスト変数またはカスタム属性のいずれかを使用してプロパティフィルターの比較を活用できます：**カスタムイベントを実行**および**購入**。これらのアクショントリガーは、基本プロパティとネストされたプロパティの両方に対するプロパティフィルターもサポートしています。

- 基本プロパティとの比較では、利用可能な比較はカスタムイベントで定義されたプロパティの型に一致します。例えば、文字列プロパティは完全一致や正規表現一致を持ちます。ブール値プロパティは true か false になります。
- ネストされたプロパティとの比較では、型は事前定義されていないため、ブール値、数値、文字列、時刻、年の日数といった複数のデータタイプにわたる比較を選択できます。これは階層化カスタム属性の比較と同様です。比較時に、ネストされたプロパティの実際のデータタイプと一致しないデータタイプを選択した場合、ユーザーはアクションパスや終了条件に一致しません。

#### アクションパスの例

{% alert important %}
カスタム属性の比較では、アクションが実行された時点でのカスタム属性値を使用します。これは、比較時にこのカスタム属性が設定されていない場合、またはカスタム属性の値が定義されたプロパティ比較と一致しない場合、ユーザーがアクションパスのグループに一致しないことを意味します。ユーザーがアクションパスステップに入った時点で条件に合致していた場合でも、この現象は発生します。
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

以下のアクションパスは、カスタムイベント `Account_Created` を実行したユーザーを、基本プロパティ `source` をコンテキスト変数 `app_source_variable` と照合してソートするように設定されています。

![カスタムイベントを実行する際にコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

以下のアクションパスは、特定の製品名 `shoes` に対する基本プロパティ `brand` をコンテキスト変数 `promoted_shoe_brand` に一致させるように設定されています。

![購入時にコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### 終了条件の例

{% tabs %}
{% tab Perform custom event %}

終了条件は、キャンバス内のユーザージャーニーのいずれかの時点で、以下の条件を満たした場合にユーザーがキャンバスから退出することを示しています。

- カスタムイベント**カート放棄**を実行し、かつ
- 基本プロパティ**カート内のアイテム**がコンテキスト変数 `cart_item_threshold` の文字列値と一致する。

![コンテキスト変数に基づいてカスタムイベントを実行した場合にユーザーを退出させる終了条件の設定。]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

終了条件は、キャンバス内のユーザージャーニーのいずれかの時点で、以下の条件を満たした場合にユーザーがキャンバスから退出することを示しています。

- 「book」という商品名で特定の購入を行い、かつ
- その購入のネストされたプロパティ「loyalty_program」がユーザーのカスタム属性「VIP」と等しい。

![購入した場合にユーザーを退出させる終了条件の設定。]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### 有効期限の設定

キャンバスの[メッセージ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/)ステップ内の[バナー]({{site.baseurl}}/user_guide/message_building_by_channel/banners/)や[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/)では、有効期限として**ステップが利用可能になってからの期間**を選択し、**期間をパーソナライズ**をオンにすることで、コンテキスト変数から利用可能時間枠を制御できます。例えば、コンテキストステップのプロモーションや予約期間に合わせることができます。

**期間をパーソナライズ**は、その期間ベースの有効期限オプションに適用されます。代わりに**特定の日時**を選択した場合は、日時コントロールを使用して有効期限を設定してください。

### アクションパスの遅延

[アクションパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/)ステップの**評価時間枠**で、**遅延をパーソナライズ**をオンにすると、コンテキスト変数からユーザーがステップに留まる時間を設定できます。ティアやリージョンなどの詳細に基づいて、待機期間をユーザーごとに変える必要がある場合に使用してください。

### コンテキスト変数フィルター

[オーディエンスパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths)と[条件分岐]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)ステップでは、事前に宣言されたコンテキスト変数を使用するフィルターを作成できます。

{% alert note %}
コンテキスト変数フィルターは、オーディエンスパスと条件分岐ステップでのみ利用可能です。
{% endalert %}

コンテキスト変数はキャンバスのスコープ内で宣言され、アクセス可能となります。つまり、セグメント内では参照できません。コンテキスト変数フィルターは、オーディエンスパスと条件分岐ステップで同様の機能を持ちます。オーディエンスパスステップは複数のグループを表し、条件分岐ステップは二値の決定を表します。

![条件分岐ステップの例。コンテキスト変数でフィルターを作成するオプション付き。]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

キャンバスのコンテキスト変数が事前定義された型を持つのと同様に、コンテキスト変数と静的値の比較では[データタイプが一致]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types)していなければなりません。コンテキスト変数フィルターは、ブール値、数値、文字列、時刻、および年の日数といった複数のデータタイプ間で比較を可能にします。これは、[階層化カスタム属性]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/)に対する比較と同様です。

{% alert note %}
コンテキスト変数と比較には同じデータタイプを使用してください。例えば、コンテキスト変数が時間データタイプの場合、時間比較（「前」や「後」など）を使用します。データタイプの不一致（時間コンテキスト変数との文字列比較など）を使用すると、予期しない動作を引き起こす可能性があります。
{% endalert %}

{% multi_lang_include alerts/important_alerts.md alert='time filter types' %}

以下は、コンテキスト変数 `product_name` を正規表現 `/braze/` と比較するコンテキスト変数フィルターの例です。

![コンテキスト変数「product_name」に正規表現「/braze/」に一致するフィルター設定。]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### コンテキスト変数やカスタム属性との比較

**コンテキスト変数またはカスタム属性との比較**トグルを選択することで、事前に定義されたコンテキスト変数やユーザーのカスタム属性と比較するコンテキスト変数フィルターを構築できます。これは、API トリガーの `context` などユーザーごとにダイナミックな比較を行う場合や、コンテキスト変数にまたがって定義された複雑な比較ロジックを簡略化するのに有用です。

{% tabs %}
{% tab Example 1 %}

例えば、ダイナミックな非アクティブ期間の後にユーザーへパーソナライズされたリマインダーを送信したい場合を考えてみましょう。具体的には、過去3日間アプリにログインしていないユーザー全員にメッセージが届くようにします。

コンテキスト変数 `re_engagement_date` があり、{% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} として定義されています。`3 days` は変数量であり、ユーザーのカスタム属性としても保存できます。`re_engagement_date` が `last_login_date`（ユーザープロファイルのカスタム属性として保存）の後にある場合、そのユーザーにはメッセージが送信されます。

![カスタム属性をパーソナライゼーションタイプとするフィルター設定。コンテキスト変数「re_engagement_date」の後にカスタム属性「last_login_date」を追加した例。]({% image_buster /assets/img/context_variable_filter2.png %})

{% endtab %}
{% tab Example 2 %}

以下のフィルターは、コンテキスト変数 `reminder_date` がコンテキスト変数 `appointment_deadline` より前にあるかどうかを比較します。これにより、オーディエンスパスステップ内のユーザーをグループ分けし、予約期限前に追加のリマインダーを受け取るべきかどうかを判断できます。

![コンテキスト変数をパーソナライゼーションタイプとして、コンテキスト変数「reminder_date」とコンテキスト変数「appointment_deadline」を用いたフィルター設定。]({% image_buster /assets/img/context_variable_filter3.png %})

{% endtab %}
{% endtabs %}

## タイムゾーンの一貫性に関する標準化

キャンバスでは、タイムスタンプ型を使用するイベントプロパティの大半は既に UTC で管理されていますが、例外も存在します。Canvas Context の追加により、アクションベースのキャンバスにおけるすべてのデフォルトのタイムスタンプイベントプロパティは、一貫して UTC で表示されるようになります。この変更は、キャンバスのステップやメッセージを編集する際の操作性をより予測可能で一貫性のあるものにするための、より広範な取り組みの一環です。この変更は、特定のキャンバスがコンテキストステップを使用しているかどうかに関わらず、すべてのアクションベースのキャンバスに影響を与えることに注意してください。

{% alert important %}
いかなる状況においても、タイムスタンプを希望のタイムゾーンで表現するには、[Liquid time_zone フィルター]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)を使用することを強く推奨します。この[よくある質問はコンテキストステップの記事]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#faq-example)で例として参照できます。
{% endalert %}

## 関連記事

- [コンテキストステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/)
- [Liquid によるパーソナライゼーションとダイナミックなコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)