---
nav_title: コンテキスト 
article_title: コンテキスト 
alias: /context/
page_order: 1.5
page_type: reference
toc_headers: "h2"
description: "このリファレンス記事では、キャンバスでコンテキストステップを作成して使用する方法について説明します。"
tool: Canvas

---

# コンテキスト

> コンテキストステップを使用すると、ユーザーがキャンバス内を移動するときに、ユーザーの変数を1つ以上作成、更新できます。例えば季節割引を管理するキャンバスでは、コンテキスト変数を使用して、ユーザーがキャンバスにエントリするたびに異なる割引コードを保存できます。

{% alert important %}
コンテキストステップは現在早期アクセス段階です。この初期のアクセスに参加したい場合は、Braze アカウントマネージャーに連絡してください。<br><br>キャンバスコンテキストステップへの初期アクセスを選択すると、すべてのキャンバスでタイムスタンプが処理される方法が変更されることに注意してください。詳細については、[タイムゾーン整合性標準化](#time-zone-consistency-standardization)を参照してください。
{% endalert %}

## 仕組み

![キャンバスの最初のステップとしてのコンテキストステップ。]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

コンテキストステップを使用すると、特定のキャンバスを経由したユーザーの移動中に一時データを作成して使用できます。このデータは、そのCanvas ジャーニー内にのみ存在し、異なるCanvase 間やセッション外では保持されません。

このフレームワーク内で、各コンテキストステップは、複数のコンテキスト変数(ユーザーのプロファイル情報を永続的に変更することなく、遅延のパーソナライズ、ユーザーの動的セグメント化、メッセージングの拡張を可能にする一時的なデータ)を定義できます。

たとえば、フライト予約を管理している場合、各ユーザーのスケジュールされたフライト時間のコンテキスト変数を作成できます。その後、各ユーザーのフライト時間に応じて遅延を設定し、同じキャンバスから個別のリマインダーを送信できます。

コンテキスト変数は、次の2 つの方法で設定できます。

- **キャンバスエントリで:**ユーザがキャンバスに入ると、イベントまたはAPI トリガのデータが自動的にコンテキスト変数に入力されます。
- **コンテキストステップで:**コンテキストステップを追加することで、キャンバス内でコンテキスト変数を手動で定義または更新できます。

各コンテキスト変数には以下が含まれます。

- 名前 (`flight_time` や`subscription_renewal_date` など)
- [データ型](#context-variable-types) (数値、文字列、時刻、配列など)
- [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/)または**Add Personalization**ツールを使用して割り当てる値。

定義したコンテキスト変数は、キャンバス全体で {% raw %}`{{context.${example_variable_name}}}`{% endraw %} という形式で参照できます。

たとえば、{% raw %}`{{context.${flight_time}}}`{% endraw %} は、ユーザーのスケジュールされたの飛行時間を返します。

ユーザーがキャンバスにエントリするたびに (以前にキャンバスにエントリしたことがある場合でも)、コンテキスト変数は、最新のエントリデータとキャンバス設定に基づいて再定義されます。このステートフルなアプリ侵入により、各キャンバスエントリは独自の独立系コンテキストを維持でき、ユーザーs は各ステートに固有のコンテキストを保持したまま、同じジャーニー内で複数のアクティブなステートを持つことができます。

たとえば、ある顧客に2 つの次のフライトがある場合、2 つの別々のジャーニーステートが同時に実行され、それぞれに、出発時刻や送信先などの独自のフライト固有のコンテキスト変数が含まれます。これにより、ニューヨーク行きの午後2時の飛行に関するパーソナライズされたのリマインダーを送る一方で、明日のロス・アンヘレス行きの午前8時の飛行に関する別々の更新を送ることができ、各々のメッセージは、具体的な予約に関連したものであり続けることができます。

## 考慮事項

- コンテキストステップごとに最大10 個のコンテキスト変数を使用できます。
- 各コンテキスト変数名は最大100 文字です。
- コンテキスト変数名は有効な識別子s (文字、数字、アンダースコアのみ) である必要があります。
- コンテキスト変数の定義は最大10,240 文字です。 
- API-トリガー ed Canvas に渡されるコンテキスト変数は、キャンバスのコンテキストステップで作成されるコンテキスト変数と同じ名前空間を共有します。これは、[`/canvas/trigger/send`エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/)コンテキストオブジェクトで変数`purchased_item`を送信する場合、{% raw %}`{context.${purchased_item}}`{% endraw %}として参照でき、キャンバスのコンテキストステップでその変数を再宣言すると、以前に送信されたものが上書きされることを意味します。
- コンテキストステップごとに最大50KB を保存でき、ステップごとに最大10 個の変数を分散できます。1 つのステップで最大50KB の可変長は、ユーザーに対して評価または保存されません。これらのサイズは順番に計算されます。たとえば、コンテキストステップに3 つの変数があるとします。
  - 変数1:500 KB
  - 変数2:500 KB
  - 変数3:500 KB
  - これは、他のすべてのコンテキスト変数の合計が50KB を超えるため、変数3 が評価または保存されないことを意味します。

## コンテキストステップの作成

### ステップ1:ステップを追加する

キャンバスにステップを追加し、サイドバーからコンポーネントをドラッグアンドドロップするか、<i class="fas fa-plus-circle"></i> plus ボタンを選択し、**Context** を選択します。

### ステップ2: 変数の定義

{% alert note %}
コンテキストステップごとに最大10 個のコンテキスト変数を定義できます。
{% endalert %}

コンテキスト変数を定義するには

1. コンテキスト変数に**name** を指定します。
2. [データ型](#context-variable-types)を選択します。
3. Liquid 式を手動で記述するか、**Add Personalization** を使用して既存の属性からLiquid スニペットを作成します。
4. コンテキスト変数の値を確認するには、**プレビュー**を選択します。
5. (オプション) 変数を追加するには、[**コンテキスト変数を追加**] を選択し、手順1～4を繰り返します。
6. [**完了**] を選択します。

これで、[**パーソナライズを追加する**] を選択して、メッセージステップやユーザー更新ステップなど Liquid を使用する任意の場所で、コンテキスト変数を使用できます。フルウォークスルーについては、[コンテキスト変数の使用](#using-context-variables)を参照してください。

## コンテキスト変数のデータ型 {#context-variable-types}

ステップで作成または更新されるコンテキスト変数には、次のデータ型を割り当てることができます。

{% alert note %}
コンテキスト変数は、[カスタムイベント s]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format) と同じ形式でデータタイプに期待されます。<br><br>ネストされたオブジェクトおよびオブジェクトの配列には、[`as_json_string` リキッドフィルター](#converting-connected-content-strings-to-json) を使用します。コンテキストステップで同じオブジェクトを作成する場合は、以下のように`as_json_string` を使用してオブジェクトをレンダリングする必要があります {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| データタイプ | 変数名の例 | 値の例 |
|---|---|---|
|ブール値| loyalty_program |正しい| 
|数値| credit_score |4\.|
|string| product_name |{% raw %} |
|配列| favorite_products|{% raw %}|
|時刻(UTC) | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|オブジェクト (フラット化) | user_profile|{% raw %}<br> "first_name": "{{user.first_name}}",<br> "last_name": "{{user.last_name}}",<br> メール<br> "loyalty_points":<br> "preferred_categories": {{user.preferred_categories}}<br></code> |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

デフォルトでは、時刻データタイプはUTCです。文字列データ型を使用して時刻値を格納する場合は、PSTのように別のタイムゾーンとして時刻を定義できます。 

たとえば、誕生日の前日にユーザーにメッセージを送信する場合、前日の送信に関連付けられている流動ロジックがあるため、コンテキスト変数を時間データタイプとして保存します。ただし、クリスマスデー(12月25日)にホリデーメッセージを送信する場合は、時刻をダイナミックな変数として参照する必要はありません。そのため、文字列データ型を使用することをお勧めします。

## コンテキスト変数の使用 {#using-context-variables}

たとえば、次のフライトの前に、VIP ラウンジへのアクセスについて乗客に通知したいとします。このメッセージは、ファーストクラスのチケットを購入した乗客にのみ送信する必要があります。コンテキスト変数は、この情報を追跡する柔軟な方法です。

ユーザーは、飛行機のチケットを購入するときにキャンバスに入ります。ラウンジアクセスの適格性を判断するために、コンテキストステップで`lounge_access_granted`というコンテキスト変数を作成し、その後のユーザージャーニーのステップでそのコンテキスト変数を参照します。

![旅客がVIP ラウンジアクセスに適格であるかどうかを追跡するために設定されたコンテキスト変数。]({% image_buster /assets/img/context_example4.png %})({: style="max-width:90%"})

このコンテキストステップでは、{% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} を使用して、購入したフライトのタイプが`first_class` かどうかを判断します。

次に、{% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} が`true` であるユーザーをターゲットにするメッセージステップを作成します。このメッセージは、個人化されたラウンジ情報を含むプッシュ通知となります。このコンテキスト変数に基づいて、適格な乗客は、フライト前に関連するメッセージを受け取ります。

- ファーストクラスの乗客は次のメッセージを受け取ります:「Enjoy exclusive VIP lounge access!」
- ビジネスクラスとエコノミークラスの乗客は次のメッセージを受け取ります:「Upgrade your flight for exclusive VIP lounge access.」

![購入した飛行機のチケットのタイプに応じて、送信するメッセージが異なるメッセージステップ。]({% image_buster /assets/img/context_example3.png %})({: style="max-width:90%"})

{% alert tip %}
コンテキストステップの情報を使用して、[パーソナライズされた遅延オプション]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) を追加できます。つまり、ユーザーを遅延させる変数を選択できます。
{% endalert %}

### アクションパスと終了基準の場合

次のトリガー アクションs では、プロパティ フィルターs をコンテキスト変数またはカスタム属性s と比較することができます。[**カスタムイベントを実行**] または [**購入**] のいずれかを選択できます。これらのアクション トリガーs は、基本プロパティーとネストされたプロパティーの両方のプロパティ フィルターs にも対応しています。 

- 基本プロパティーと比較する場合、使用可能な比較は、カスタムイベントで定義されたプロパティの種類と一致します。たとえば、文字列プロパティは、正規表現一致と完全に等しくなります。ブール値のプロパティはtrue またはfalse になります。 
- ネストされたプロパティと比較する場合、型は事前定義されていないため、階層化カスタム属性s の比較と同様に、ブール値、数値、ストリング、時刻、および曜日の複数のデータ型の比較を選択できます。比較時にネストされたプロパティの実際のデータ型と一致しないデータ型を選択した場合、ユーザーはアクションパスまたは終了基準と一致しません。

#### アクションパスの例

{% alert important %}
カスタム属性の比較には、アクションが実行された時点のカスタム属性を使用します。つまり、ユーザーに比較時にこのカスタム属性が入力されていない場合、またはカスタム属性が定義されたプロパティの比較と一致しない場合、ユーザーはアクションパスグループと一致しません。これは、ユーザーがアクションパスステップを入力したときに一致した場合でも同様です。
{% endalert %}

{% tabs %}
{% tab Perform custom event %}

以下のアクションパスは、基本プロパティ`source` を使用してカスタムイベント`Account_Created` を実行したユーザーをコンテキスト変数`app_source_variable` にソートするように設定されています。

![カスタムイベントの実行時にコンテキスト変数を参照するサンプルアクションパス。]({% image_buster /assets/img/context_action_path1.png %})

{% endtab %}
{% tab Make purchase %}

以下のアクションパスは、特定の製品名`shoes` の基本プロパティ`brand` とコンテキスト変数`promoted_shoe_brand` を照合するように設定されています。

![購入時にコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path2.png %})

{% endtab %}
{% endtabs %}

#### 終了基準の例

{% tabs %}
{% tab Perform custom event %}

終了基準では、キャンバス内のユーザーの移動の任意の時点で、以下の場合にキャンバスを終了します。

- カスタムイベント **Abandon Cart**を実行し
- 基本プロパティ**Cart**のItemは、コンテキスト変数`cart_item_threshold`の文字列値と一致します。

![コンテキスト変数に基づいてカスタムイベントを実行する場合にユーザーを終了するように設定された終了基準。]({% image_buster /assets/img/context_exit_criteria1.png %})

{% endtab %}
{% tab Make purchase %}

終了基準では、キャンバス内のユーザーの移動の任意の時点で、以下の場合にキャンバスを終了します。

- 彼らは"book"製品名、そして
- この購入のネストされたプロパティ"loyalty_program" は、ユーザーのカスタム属性"VIP" に等しくなります。

![ユーザーを購入した場合に終了するように設定された終了基準。]({% image_buster /assets/img/context_exit_criteria2.png %})

{% endtab %}
{% endtabs %}

### コンテキスト変数フィルターs

[Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths)および[Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)ステップsで、事前に宣言されたコンテキスト変数を使用するフィルターsを作成できます。

{% alert important %}
コンテキスト変数フィルターs は、オーディエンスパスとディシジョン分割ステップs でのみ使用できます。
{% endalert %}

コンテキスト変数は宣言され、キャンバスのスコープでのみアクセス可能です。つまり、Segment s では参照できません。コンテキスト変数フィルターs は、オーディエンスパスおよびディシジョン分割ステップs-オーディエンスパスステップs では複数のグループを表し、ディシジョン分割s はバイナリ決定を表します。

![デシジョン分割ステップのサンプルで、コンテキスト変数を含むフィルターを作成するオプションを使用します。]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}

キャンバスのコンテキスト変数の定義済みタイプと同様に、コンテキスト変数と静的値の比較には、[一致するデータ型]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types)が必要です。コンテキスト変数フィルターでは、[階層化カスタム属性 s]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/) の比較と同様に、ブール値、数値、文字列、時刻、および曜日の複数のデータタイプの比較が可能です。

{% alert note %}
コンテキスト変数と比較には同じデータ型を使用します。たとえば、コンテキスト変数が時間データ型の場合、時間比較("before"または"after"など)を使用します。一致しないデータ型を使用すると(時間コンテキスト変数との文字列比較など)、予期しない動作が発生する可能性があります。
{% endalert %}

以下は、コンテキスト変数`product_name` を正規表現`/braze/` と比較するコンテキスト変数フィルターの例です。

![正規表現"/braze/" にマッチするコンテキスト変数"product_name" のフィルター設定。]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}

#### コンテキスト変数またはカスタム属性s との比較

**コンテキスト変数またはカスタム属性**トグルと比較を選択することで、以前に定義されたコンテキスト変数またはユーザー カスタム属性s と比較するコンテキスト変数フィルターs を作成できます。これは、API-トリガー ed `context` など、ユーザーごとにダイナミックなな比較を実行する場合や、コンテキスト変数間で定義された複雑な比較ロジックを圧縮する場合に役立ちます。

{% tabs %}
{% tab Example 1 %}

ここでは、ダイナミックなの非アクティビティの後にユーザー s にパーソナライズされた通知を送信するとします。この通知には、過去3 日間にアプリにログインしていないユーザーが含まれます。

コンテキスト変数`re_engagement_date` があり、{% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} として定義されています。`3 days` は、ユーザーのカスタム属性としても格納される可変量にすることができます。したがって、`re_engagement_date` が`last_login_date` の後にある場合(ユーザープロファイルにカスタム属性として保存されている場合)、メッセージが送信されます。

![カスタム属性 s をコンテキスト変数"re_engagement_date" のパーソナライゼーション型として、カスタム属性"last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %} の後に指定したフィルター設定

{% endtab %}
{% tab Example 2 %}

次のフィルターでは、コンテキスト変数`reminder_date` を、コンテキスト変数`appointment_deadline` の前に比較します。これにより、オーディエンスパスステップでs ユーザーをグループ化し、アプリの塗布期限までに追加のリマインダーを受け取るかどうかを判断するのに役立ちます。

![コンテキスト変数をコンテキスト変数"reminder_date" のパーソナライゼーション型として、コンテキスト変数"appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %} のフィルター設定

{% endtab %}
{% endtabs %}

## ユーザー パスのプレビュー

ユーザー パスs でテストと[ プレビューを実行して、メッセージが正しいオーディエンスに送信され、コンテキスト変数が期待される結果に評価されることを確認することをお勧めします。

{% alert note %}
エディタの** プレビュー & Test Send** セクションでキャンバスをプレビューする場合、テストメッセージプレビューのタイムスタンプ**は、文字列としてプレビューs を生成するため、UTC に標準化されません。つまり、キャンバスが`time` オブジェクトを受け入れるように設定されている場合、メッセージプレビューは、キャンバスの稼働中に発生する内容をキュレートしません。ほとんどのac キュレート y をテストするには、代わりにユーザー パス s をプレビューすることをお勧めします。
{% endalert %}

無効なコンテキスト変数を作成する一般的なシナリオを必ず守ってください。ユーザー パスをプレビューするときに、コンテキスト変数、およびユーザーs と任意のコンテキスト変数を照合するオーディエンス、ディシジョン、またはアクションパス ステップの比較を使用して、パーソナライズされた遅延ステップs の結果を表示できます。

コンテキスト変数が有効な場合は、キャンバス全体で変数を参照できます。ただし、コンテキスト変数が正しく作成されていない場合、キャンバスの今後の手順も正しく実行されません。たとえば、コンテキストステップを作成してユーザーにアプリの軟膏時間を割り当て、アプリの軟膏時間の値を過去の日付に設定した場合、メッセージステップのリマインダーメールは送信されません。

## 接続されたコンテンツ文字列のJSON への変換

コンテキストステップで[コネクテッドコンテンツ呼び出し]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call)を実行すると、整合性とエラー防止のために、呼び出しから返された JSON が文字列データ型として評価されます。この文字列をJSON に変換する場合は、`as_json_string` を使用して変換します。以下に例を示します。

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## タイムゾーン整合性の標準化

タイムスタンプタイプを使用するほとんどのイベントプロパティはキャンバスですでにUTCになっていますが、いくつかの例外があります。キャンバスコンテキストを追加すると、アクション ベースのキャンバスのすべてのデフォルトタイムスタンプイベントプロパティは一貫してUTC になります。この変更は、キャンバスステップやメッセージを編集する際に、より予測可能で一貫性のあるエクスペリエンスを確保するための、より幅広い作業の一部です。この変更は、特定のキャンバスがコンテキストステップを使用しているかどうかに関係なく、すべてのアクションベースのキャンバスに影響を与えることに注意してください。

{% alert important %}
すべての状況で、目的のタイムゾーンで表されるタイムスタンプには、[Liquid time_zone フィルター s]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know) を使用することを強くお勧めします。この[よくある質問](#faq-example)を例として参照できます。
{% endalert %}

## トラブルシューティング {#troubleshooting}

### 無効なコンテキスト変数

以下の場合、コンテキスト変数は無効と見なされます。
- 埋め込み接続コンテンツへの呼び出しが失敗します。
- 実行時のLiquid 式は、データ型と一致しない値、または空(NULL) の値を返します。

たとえば、コンテキスト変数のデータ型が**Number** であるが、Liquid 式が文字列を返す場合、これは無効です。

このような状況では次のようになります。 
- ユーザーは次のステップに進みます。 
- キャンバスステップ分析では、これは_未更新_としてカウントされます。

トラブルシューティングの際には、_未更新_指標を監視して、コンテキスト変数が正しく更新されることを確認します。コンテキスト変数が無効な場合、ユーザーはコンテキストステップを過ぎてもキャンバスに留まることができますが、後のステップには適さない場合があります。

各データ型の設定例については、[コンテキスト変数データ型](#context-variable-types)を参照してください。

## よくある質問

### キャンバスコンテキストが一般的に使用可能になると、何が変わりますか?

キャンバスコンテキストが一般的に使用可能になると、次の情報がアプリされます。

- アクション ベースのキャンバスの[datetime type]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties) が[トリガーイベントプロパティ]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) のすべてのタイムスタンプは、必ず[UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) になります。 
- この変更は、特定のキャンバスがコンテキストステップを使用しているかどうかにかかわらず、アクションベースのすべてのキャンバスに影響します。

#### この変更の理由は何ですか?

この変更は、キャンバスステップやメッセージを編集するときに、より予測可能で一貫性のあるエクスペリエンスを作成するための、より幅広い作業の一部です。

#### この変更はいつ有効になりますか?

- キャンバスコンテキストの早期アクセスに参加している場合、この変更はすでにアプリ嘘になっています。 
- キャンバスコンテキストの初期アクセスに参加していない場合は、初期アクセスに参加したとき、またはキャンバスコンテキストが一般的に使用可能になったときに、この変更がアプリされます。

#### API-トリガーキャンバスまたはスケジュールされたキャンバスは、この変更の影響を受けますか?

いいえ。

#### この変更は、キャンバスのエントリプロパティーに影響しますか?

はい。これは、`canvas_entry_property`がアクションベースのキャンバスで使用されており、プロパティの種類が`time`の場合、`canvas_entry_properties`に影響します。どのような状況でも、必要なタイムゾーンで表されるタイムスタンプには、リキッド`time_zone` フィルターを使用することをお勧めします。

これを行う方法の例を次に示します。

| メッセージステップのリキッド | 出力 | これは、Liquidでタイムゾーンを正しく表現する方法ですか? |
|---|---|---|
| {% raw %}```{{canvas_entry_properties.${timestamp_property}}}```{% endraw %} | `2025-08-05T08:15:30:250-0800` | いいえ |
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 4:15pm` | いいえ
| {% raw %}```{{canvas_entry_properties.${timestamp_property} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}```{% endraw %} | `2025-08-05 8:15am` | はい |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### 新しいタイムスタンプの振る舞いが私のメッセージにどのように影響するかの実用的な例は何ですか? {#faq-example}

たとえば、メッセージステップに次の内容を含むアクションベースのキャンバスがあるとします。

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

これにより、次のメッセージが表示されます。 

```
Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!
```

Liquidを使用してタイムゾーンが指定されていないため、ここでのタイムスタンプはUTCです。 

タイムゾーンを明確に指定するには、以下のようにリキッド`time_zone` フィルターs を使用します。 

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

これにより、次のメッセージが表示されます。 

```
Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!
```

America/Los アンヘレスタイムゾーンはLiquid を使用して指定されているため、ここでのタイムスタンプはPST です。

推奨されるタイムゾーンは、以下のような支払いプロパティーの読み込むで送信することもでき、リキッドロジックで使用できます。

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

### コンテキスト変数は、Canvas エントリプロパティとはどのように異なるのですか?

コンテキストステップの初期アクセスに参加している場合は、キャンバスのエントリプロパティがキャンバスのコンテキスト変数として含まれるようになりました。つまり、Liquid スニペットでコンテキスト変数を使用する場合と同様に、Braze API を使用してキャンバスエントリのプロパティを送信し、他のステップでこれらのプロパティを参照できます。

### 変数は、1つのコンテキストステップ内で相互に参照できますか?

はい。コンテキストステップのすべての変数は、シーケンスで評価されます。つまり、以下のコンテキスト変数を設定できます。

| コンテキスト変数 | 値 | 説明 |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | ユーザーのお気に入りの料理。 |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | ユーザーに利用可能な割引コード。 |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | 以前の変数を組み合わせたパーソナライズされたメッセージ。メッセージステップでは、Liquid スニペット{% raw %}`{{context.${personalized_message}}}`{% endraw %} を使用してコンテキスト変数を参照し、各ユーザーにパーソナライズされたメッセージを配信できます。コンテキストステップを使用して、[プロモコード]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list)値を保存し、キャンバス全体の他のステップにテンプレートすることもできます。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

これは、複数のコンテキストステップにも適用されます。例えば次のシーケンスを考えてみます。
1. 最初のコンテキストステップでは、`JobInfo` という変数を作成して値 `job_title` を設定します。
2. メッセージステップは {% raw %}`{{context.${JobInfo}}}`{% endraw %} を参照し、`job_title` をユーザーに表示します。
3. その後、コンテキストステップによってコンテキスト変数が更新され、`JobInfo` の値が`job_description` に変更されます。
4. `JobInfo` を参照する以降のすべてのステップで、更新された値`job_description` が使用されるようになりました。

コンテキスト変数は、キャンバス全体で最新の値を使用します。更新を行うたびに、その変数を参照する後続のすべてのステップに影響します。
