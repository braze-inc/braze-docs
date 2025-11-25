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
コンテキストステップは現在早期アクセス段階です。この初期のアクセスに参加したい場合は、Braze アカウントマネージャーに連絡してください。<br><br>キャンバスコンテキストステップへの早期アクセスを選ぶと、すべてのキャンバスでタイムスタンプがどのように扱われるかが変更される。これについては、「[タイムゾーンの一貫性の標準化](#time-zone-consistency-standardization)」を参照のこと。
{% endalert %}

## 仕組み

<<<<<<< HEAD
![キャンバスの最初のステップとしてのコンテクスト・ステップ。]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
=======
\![キャンバスの最初のステップとしてのコンテクスト・ステップ。]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}
>>>>>>> main

コンテキスト・ステップでは、ユーザーが特定のキャンバス内を移動する間に一時的なデータを作成し、使用することができる。このデータは、そのCanvas ジャーニー内にのみ存在し、異なるCanvase 間やセッション外では保持されません。

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

例えば、{% raw %}`{{context.${flight_time}}}`{% endraw %} 、ユーザーのスケジュールされたフライト時間を返すことができる。

ユーザーがキャンバスにエントリするたびに (以前にキャンバスにエントリしたことがある場合でも)、コンテキスト変数は、最新のエントリデータとキャンバス設定に基づいて再定義されます。このステートフルなアプローチにより、各キャンバスエントリーは独立系のコンテキストを維持することができ、ユーザーは各ステートに固有のコンテキストを保持しながら、同じ旅の中で複数のアクティブステートを持つことができる。

例えば、顧客に2つのフライトの予定がある場合、2つの別々のカスタマージャーニーの状態が同時に実行される。これにより、ニューヨーク行きの午後2時のフライトに関するパーソナライズされたリマインダーを送る一方で、ロサンゼルス行きの明日の午前8時のフライトに関する異なる更新を送ることができ、各メッセージが特定の予約に関連したものに保たれる。

## 考慮事項

- コンテクスト・ステップごとに、最大10個のコンテクスト変数を持つことができる。
- 各コンテキスト変数名は100文字まで。
- コンテキスト変数名は有効な識別子（文字、数字、アンダースコアのみ）でなければならない。
- コンテキスト変数の定義は10,240文字まで可能である。 
- APIトリガーのキャンバスに渡されるコンテキスト変数は、キャンバスのコンテキストステップで作成されるコンテキスト変数と同じ名前空間を共有する。つまり、`/canvas/trigger/send` [エンドポイントコンテキストオブジェクトで]({{site.baseurl}}/api/objects_filters/context_object)変数`purchased_item` を送信した場合、それは{% raw %}`{context.${purchased_item}}`{% endraw %} として参照することができ、キャンバスのコンテキストステップでその変数を再宣言すると、以前に送信されたものが上書きされる。
- コンテキスト・ステップごとに最大50KBまで保存でき、ステップごとに最大10個の変数を分散して保存できる。1ステップの合計が50KBを超える変数サイズは、ユーザーに対して評価されず、保存もされない。これらのサイズは順番に計算される。例えば、コンテキスト・ステップに3つの変数があるとする：
  - 変数1：30 KB
  - 変数2：19 KB
  - 変数3：2 KB
  - つまり、他のすべてのコンテキスト変数の合計が50KBを超えるため、変数3は評価も保存もされない。

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
コンテキスト変数のデータ型は、[カスタムイベントと]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format)同じである。<br><br>ネストしたオブジェクトやオブジェクトの配列には、[`as_json_string` Liquidフィルターを](#converting-connected-content-strings-to-json)使う。コンテキストのステップで同じオブジェクトを作成する場合は、`as_json_string` を使ってオブジェクトをレンダリングする必要がある。 {%raw%}```{{context.${object_array} | as_json_string }}```{%endraw%}
{% endalert %}

| データタイプ | 変数名の例 | 値の例 |
|---|---|---|
|ブール値| loyalty_program |{% raw %}<code>真の</code>{% endraw %}| 
|数値| credit_score |{% raw %}<code>740{% endraw %}|
|string| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|配列| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|時間（UTC） | last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|オブジェクト (フラット化) | user_profile|{% raw %}<code>{<br> "first_name": "{{user.first_name}}",<br> "last_name": "{{user.last_name}}",<br> 「メール": "{{user.email}}"、<br> "loyalty_points": {{user.loyalty_points}},<br> "preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

デフォルトでは、時刻のデータ型はUTCである。文字列データ型を使って時間値を格納する場合、PSTのような異なるタイムゾーンとして時間を定義することができる。 

例えば、ユーザーの誕生日の前日にメッセージを送信する場合、前日送信に関連するLiquidロジックがあるため、コンテキスト変数をtimeデータ型として保存する。しかし、クリスマス（12月25日）にホリデー・メッセージを送るのであれば、ダイナミックな変数として時刻を参照する必要はないだろうから、文字列データ型を使うのが望ましいだろう。

## コンテキスト変数の使用 {#using-context-variables}

たとえば、次のフライトの前に、VIP ラウンジへのアクセスについて乗客に通知したいとします。このメッセージは、ファーストクラスのチケットを購入した乗客にのみ送信する必要があります。コンテキスト変数は、この情報を追跡する柔軟な方法です。

ユーザーは、飛行機のチケットを購入するときにキャンバスに入ります。ラウンジアクセスの適格性を判断するために、コンテキストステップで`lounge_access_granted`というコンテキスト変数を作成し、その後のユーザージャーニーのステップでそのコンテキスト変数を参照します。

<<<<<<< HEAD
![乗客がVIPラウンジを利用できるかどうかを追跡するために設定されたコンテキスト変数である。]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}
=======
\![乗客がVIPラウンジを利用できるかどうかを追跡するために設定されたコンテキスト変数である。]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}
>>>>>>> main

このコンテキストステップでは、{% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} を使用して、購入したフライトのタイプが`first_class` かどうかを判断します。

次に、{% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} が`true` であるユーザーをターゲットにするメッセージステップを作成します。このメッセージは、個人化されたラウンジ情報を含むプッシュ通知となります。このコンテキスト変数に基づいて、適格な乗客は、フライト前に関連するメッセージを受け取ります。

- ファーストクラスの乗客は次のメッセージを受け取ります:「Enjoy exclusive VIP lounge access!」
- ビジネスクラスとエコノミークラスの乗客は次のメッセージを受け取ります:「Upgrade your flight for exclusive VIP lounge access.」

<<<<<<< HEAD
![購入した航空券の種類によって、送信するメッセージが異なるメッセージステップ。]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}
=======
\![購入した航空券の種類によって、送信するメッセージが異なるメッセージステップ。]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}
>>>>>>> main

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

<<<<<<< HEAD
![カスタムイベントを実行するときにコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path1.png %})
=======
\![カスタムイベントを実行するときにコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path1.png %})
>>>>>>> main

{% endtab %}
{% tab Make purchase %}

以下のアクションパスは、特定の製品名`shoes` の基本プロパティ`brand` をコンテキスト変数`promoted_shoe_brand` にマッチさせるように設定されている。

<<<<<<< HEAD
![購入時にコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path2.png %})
=======
\![購入時にコンテキスト変数を参照するアクションパスの例。]({% image_buster /assets/img/context_action_path2.png %})
>>>>>>> main

{% endtab %}
{% endtabs %}

#### 終了基準の例

{% tabs %}
{% tab Perform custom event %}

終了基準とは、ユーザーがキャンバス内を移動するどの時点でも、以下の場合にキャンバスから退出するというものである：

- 彼らはカスタムイベント**Abandon Cartを**実行する。
- **Cartの**基本プロパティ**Itemは**、コンテキスト変数`cart_item_threshold` の文字列値と一致する。

<<<<<<< HEAD
![コンテクスト変数に基づくカスタムイベントをユーザーが実行した場合、ユーザーを終了させるための終了基準設定。]({% image_buster /assets/img/context_exit_criteria1.png %})
=======
\![コンテクスト変数に基づくカスタムイベントをユーザーが実行した場合、ユーザーを終了させるための終了基準設定。]({% image_buster /assets/img/context_exit_criteria1.png %})
>>>>>>> main

{% endtab %}
{% tab Make purchase %}

終了基準とは、ユーザーがキャンバス内を移動するどの時点でも、以下の場合にキャンバスから退出するというものである：

- 彼らは「本」という商品名のために特定の購入をする。
- その購入のネストされたプロパティ"loyalty_program" は、ユーザーのカスタム属性「VIP」と等しい。

<<<<<<< HEAD
![ユーザーが購入した場合に終了するように設定された終了基準。]({% image_buster /assets/img/context_exit_criteria2.png %})
=======
\![ユーザーが購入した場合に終了するように設定された終了基準。]({% image_buster /assets/img/context_exit_criteria2.png %})
>>>>>>> main

{% endtab %}
{% endtabs %}

### コンテキスト変数フィルター

[オーディエンスパスと]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) [条件分岐]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split)ステップで、以前に宣言したコンテキスト変数を使用するフィルターを作成できる。

{% alert important %}
コンテキスト変数フィルターは、オーディエンスパスと条件分岐ステップでのみ使用できる。
{% endalert %}

つまり、セグメンテーションの中で参照することはできない。オーディエンスパスのステップは複数のグループを表し、条件分岐のステップは二値決定を表す。

<<<<<<< HEAD
![条件分岐ステップの例では、コンテキスト変数でフィルターを作成することができる。]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}
=======
\![条件分岐ステップの例では、コンテキスト変数でフィルターを作成することができる。]({% image_buster /assets/img/context_decision_split.png %}){: style="max-width:90%;"}
>>>>>>> main

キャンバスのコンテキスト変数があらかじめ定義された型を持っているのと同様に、コンテキスト変数とスタティック値の比較も、[データ型が一致して]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/#supported-data-types)いなければならない。コンテキスト変数フィルターは、階層[化されたカスタム属性の]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/nested_custom_attribute_support/)比較と同様に、ブーリアン、数値、文字列、時刻、曜日について、複数のデータ型にまたがる比較を可能にする。

{% alert note %}
コンテキスト変数と比較には同じデータ型を使う。例えば、コンテキスト変数が時間データ型の場合、時間比較（"before "や "after "など）を使う。不一致のデータ型（時間コンテキスト変数との文字列比較など）を使用すると、予期せぬ動作を引き起こす可能性がある。
{% endalert %}

以下は、コンテキスト変数`product_name` を正規表現`/braze/` と比較するコンテキスト変数フィルターの例である。

<<<<<<< HEAD
![コンテキスト変数"product_name" 、正規表現"/braze/"にマッチするようにフィルターが設定されている。]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}
=======
\![コンテキスト変数"product_name" 、正規表現"/braze/"にマッチするようにフィルターが設定されている。]({% image_buster /assets/img/context_variable_filter1.png %}){: style="max-width:90%;"}
>>>>>>> main

#### コンテキスト変数やカスタム属性との比較

**コンテキスト変数またはカスタム属性と比較する**トグルを選択することにより、以前に定義されたコンテキスト変数またはユーザーカスタム属性と比較するコンテキスト変数フィルターを構築することができる。これは、APIトリガー（`context` ）のようにユーザーごとにダイナミックな比較を実行する場合や、コンテキスト変数にまたがって定義された複雑な比較ロジックを凝縮する場合に便利である。

{% tabs %}
{% tab Example 1 %}

例えば、過去3日間アプリにログインしていないユーザーを含むダイナミックな非アクティブ期間の後に、パーソナライズされたリマインダーをユーザーに送信したいとしよう。

コンテキスト変数`re_engagement_date` は、{% raw %}`{{now | minus: 3 | append: ' days'}}`{% endraw %} と定義されている。なお、`3 days` 、ユーザーのカスタム属性として保存されることもある。つまり、`re_engagement_date` （ユーザープロファイルのカスタム属性として保存されている）が`last_login_date` （ユーザープロファイルのカスタム属性として保存されている）の後であれば、メッセージが送られる。

<<<<<<< HEAD
![カスタム属性をパーソナライゼーション・タイプとするフィルター・セットアップのコンテキスト変数"re_engagement_date" 、カスタム属性"last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %}の後に続く)
=======
\![カスタム属性をパーソナライゼーション・タイプとするフィルター・セットアップのコンテキスト変数"re_engagement_date" 、カスタム属性"last_login_date".]({% image_buster /assets/img/context_variable_filter2.png %}の後に続く)
>>>>>>> main

{% endtab %}
{% tab Example 2 %}

次のフィルターは、コンテキスト変数`reminder_date` がコンテキスト変数`appointment_deadline` より前にあることを比較する。これは、オーディエンスパスのステップでユーザーをグループ化し、予約締め切り前に追加リマインダーを受け取るべきかどうかを判断するのに役立つ。

<<<<<<< HEAD
![コンテキスト変数"appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %}のパーソナライゼーションタイプ"reminder_date" としてコンテキスト変数を使ったフィルターセットアップ)
=======
\![コンテキスト変数"appointment_deadline".]({% image_buster /assets/img/context_variable_filter3.png %}のパーソナライゼーションタイプ"reminder_date" としてコンテキスト変数を使ったフィルターセットアップ)
>>>>>>> main

{% endtab %}
{% endtabs %}

## ユーザーパスをプレビューする

メッセージが適切なオーディエンスに送信され、コンテキストの変数が期待される結果に対して評価されていることを確認するために、[ユーザーパスを]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths)テストし[プレビューする]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths)ことをお勧めする。

{% alert note %}
エディターの**Preview& Test Send**セクションでキャンバスをプレビューしている場合、このパネルは文字列としてプレビューを生成するため、テストメッセージプレビューのタイムスタンプはUTCに標準化さ**れない**。つまり、キャンバスが`time` オブジェクトを受け入れるように設定されている場合、メッセージ・プレビューはキャンバスがライブのときに発生することを正確にプレビューしない。キャンバスを最も正確にテストするには、ユーザーパスをプレビューすることをお勧めする。
{% endalert %}

無効なコンテキスト変数を作成する一般的なシナリオを必ず観察すること。ユーザーパスをプレビューする際、コンテキスト変数を使用してパーソナライズされたDelayステップの結果、およびユーザーを任意のコンテキスト変数に一致させるオーディエンス、意思決定、またはアクションパスのステップ比較を表示することができる。

コンテキスト変数が有効な場合は、キャンバス全体で変数を参照できます。しかし、コンテキスト変数が正しく作成されなかった場合、キャンバスの今後のステップも正しく実行されない。例えば、ユーザーにアポイントメントタイムを割り当てるためにコンテキストステップを作成し、アポイントメントタイムの値を過去の日付に設定した場合、メッセージステップのリマインダーメールは送信されない。

## 接続されたコンテンツ文字列のJSON への変換

コンテキストステップで[コネクテッドコンテンツ呼び出し]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call)を実行すると、整合性とエラー防止のために、呼び出しから返された JSON が文字列データ型として評価されます。この文字列をJSON に変換する場合は、`as_json_string` を使用して変換します。以下に例を示します。

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

## タイムゾーンの一貫性の標準化

キャンバスコンテキストの追加により、アクションベースのキャンバスの[トリガーイベントプロパティから]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties) [datetimeタイプを]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#custom-event-properties)持つすべてのタイムスタンプは、常に[UTCに](https://en.wikipedia.org/wiki/Coordinated_Universal_Time)正規化される。以前は、[例外を]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)除き、イベントプロパティのタイムスタンプはUTCに正規化されていた。これでキャンバスのステップやメッセージの編集がより一貫したものになる。

この変更がキャンバスのタイムスタンプにどのような影響を与えるかの例を考えてみよう。アクション・ベースのキャンバスで、イベント・プロパティをキャンバスの最初のステップで使い、次のメッセージ・ステップを使うとしよう： 

{% raw %}
`Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!`
{% endraw %}

<<<<<<< HEAD
![メッセージ・ステップを最初のステップとするコンテクスト・ジャーニー。]({% image_buster /assets/img/context_timezone_example.png %}){: style="max-width:50%"}
=======
\![メッセージ・ステップを最初のステップとするコンテクスト・ジャーニー。]({% image_buster /assets/img/context_timezone_example.png %}){: style="max-width:50%"}
>>>>>>> main

ステップはまた、次のようなイベントペイロードを持つ： 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
}
```

歴史的に見れば、メッセージはこうだろう： `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

キャンバス・コンテキストの早期アクセスによって、メッセージはこうなる：`Your appointment is scheduled for 2025-08-05 4:15pm, we’ll see you then!` これは、タイムスタンプがUTCであるためで、太平洋時間（元のペイロードで`-08:00`)で指定されたタイムゾーンより8時間進んでいる。

{% alert important %}
このタイムスタンプの変化を考慮するため、どのような状況においても、タイムスタンプが希望するタイムゾーンで表現されるように[Liquidフィルターを使用する]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)ことを強く推奨する。
{% endalert %}

### Liquidを使用して、希望するタイムゾーンでのタイムスタンプを示す。

次のLiquidのスニペットを考えてみよう：

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: "America/Los_Angeles" | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

このロジックの結果は以下のようになる： `Your appointment is scheduled for 2025-08-05 8:15am, we'll see you then!`

優先タイムゾーンは、イベントプロパティのペイロードで送信し、Liquidロジックで使用することもできる： 

```
{
  "appointment_time": "2025-08-05T08:15:30:250-0800"
  "user_timezone": "America/Los_Angeles"
}
```

これはLiquidスニペットの例である：

{% raw %}
```
Your appointment is scheduled for {{canvas_entry_properties.${appointment_time} | time_zone: canvas_entry_properties.${user_timezone} | date: "%Y-%m-%d %l:%M %p"}}, we'll see you then!
```
{% endraw %}

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

### コンテキスト変数は、Canvas エントリプロパティとはどのように異なるのですか?

コンテキストステップの初期アクセスに参加している場合は、キャンバスのエントリプロパティがキャンバスのコンテキスト変数として含まれるようになりました。つまり、Liquid スニペットでコンテキスト変数を使用する場合と同様に、Braze API を使用してキャンバスエントリのプロパティを送信し、他のステップでこれらのプロパティを参照できます。

### 変数は、1つのコンテキストステップ内で相互に参照できますか?

はい。コンテキストステップのすべての変数は、シーケンスで評価されます。つまり、以下のコンテキスト変数を設定できます。

| コンテキスト変数 | 値 | 説明 |
|---|---|---|
|`favorite_cuisine`| {% raw %}`{{custom_attribute.${Favorite Cuisine}}}`{% endraw %} | ユーザーのお気に入りの料理。 |
|`promo_code`| {% raw %}`EATFRESH`{% endraw %} | ユーザーに利用可能な割引コード。 |
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{context.promo_code}} "on delivery from your favorite" {{context.favorite_cuisine}} restaurants!"`{% endraw %} | 以前の変数を組み合わせたパーソナライズされたメッセージ。メッセージステップでは、Liquid スニペット{% raw %}`{{context.${personalized_message}}}`{% endraw %} を使用してコンテキスト変数を参照し、各ユーザーにパーソナライズされたメッセージを配信できます。また、Contextステップを使って[プロモコードの]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list)値を保存し、キャンバス全体の他のステップでテンプレート化することもできる。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

これは、複数のコンテキストステップにも適用されます。例えば次のシーケンスを考えてみます。
1. 最初のコンテキストステップでは、`JobInfo` という変数を作成して値 `job_title` を設定します。
2. メッセージステップは {% raw %}`{{context.${JobInfo}}}`{% endraw %} を参照し、`job_title` をユーザーに表示します。
3. その後、コンテキストステップによってコンテキスト変数が更新され、`JobInfo` の値が`job_description` に変更されます。
4. `JobInfo` を参照する以降のすべてのステップで、更新された値`job_description` が使用されるようになりました。

コンテキスト変数は、キャンバス全体で最新の値を使用します。更新を行うたびに、その変数を参照する後続のすべてのステップに影響します。

### キャンバスコンテキストのタイムゾーン一貫性の標準化は、APIトリガーのキャンバスに影響を与えるか？

いや、この変更はアクショントリガーのキャンバスにしか影響しない。APIトリガーのCanvasesに送られるタイムスタンプは、時間型ではなく文字列型であるため、元のタイムゾーンは常に保持される。

### これは、キャンバスのエントリー・プロパティやイベント・プロパティに記されている例外イベントとどのように関係しているのか？

キャンバスコンテキストの早期アクセスに参加すると、キャンバスコンテキストのステップを使用しているかどうかにかかわらず、[これらの例外が]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties/#things-to-know)なくなる。
