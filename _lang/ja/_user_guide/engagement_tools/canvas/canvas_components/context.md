---
nav_title: コンテキスト 
article_title: コンテキスト 
alias: /context/
page_order: 1.5
page_type: reference
description: "このリファレンス記事では、キャンバスでコンテキストステップを作成して使用する方法について説明します。"
tool: Canvas

---

# コンテキスト

> コンテキストステップを使用すると、ユーザーがキャンバス内を移動するときに、ユーザーの変数を1つ以上作成、更新できます。例えば季節割引を管理するキャンバスでは、コンテキスト変数を使用して、ユーザーがキャンバスにエントリするたびに異なる割引コードを保存できます。

{% alert important %}
コンテキストステップは現在早期アクセス段階です。この初期のアクセスに参加したい場合は、Braze アカウントマネージャーに連絡してください。
{% endalert %}

## CDI の仕組み

![キャンバスの最初のステップとしてのコンテキストステップ。]({% image_buster /assets/img/context_step3.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

コンテキストステップを使用すると、特定のキャンバス内でのユーザーのジャーニーで、一時データを作成して使用できます。このデータは、そのCanvas ジャーニー内にのみ存在し、異なるCanvase 間やセッション外では保持されません。

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

例えば、
{% raw %}`{{context.${flight_time}}}{% endraw %}` は、ユーザーの予定飛行時間を返します。

ユーザーがキャンバスにエントリするたびに (以前にキャンバスにエントリしたことがある場合でも)、コンテキスト変数は、最新のエントリデータとキャンバス設定に基づいて再定義されます。これにより、複数のエントリを持つユーザーに対しても、ジャーニーはパーソナライズされた正確な状態になります。

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

### ステップ 3:ユーザーパスのテスト(オプション)

コンテキスト変数が有効な場合は、キャンバス全体で変数を参照できます。ただし、コンテキスト変数が正しく作成されていない場合、キャンバスの今後の手順も正しく実行されません。メッセージが適切なユーザーに送信されるように、テストと[ユーザーパス]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/preview_user_paths)のプレビューを行うことをお勧めします。[無効なコンテキスト変数](#troubleshooting)を作成する一般的なシナリオを探します。

例えば、ユーザーに予約時刻を割り当てるコンテキストステップを作成したが、予約時刻の値を過去の日付に設定した場合、メッセージステップで作成したリマインダーメールが送信されることはありません。 

## コンテキスト変数のデータ型 {#context-variable-types}

ステップで作成または更新されるコンテキスト変数には、次のデータ型を割り当てることができます。

{% alert note %}
コンテキスト変数は、[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/#expected-format)と同じデータ型の期待される形式を持ちますが、コンテキスト変数はネストされたオブジェクトをサポートしていません。
{% endalert %}

| データタイプ | 変数名の例 | 値の例 |
|---|---|---|
|ブール値| loyalty_program |{% raw %}<code>true</code>{% endraw %}| 
|数値| credit_score |{% raw %}<code>740{% endraw %}|
|string| product_name |{% raw %}<code>green_tea</code>{% endraw %} |
|配列| favorite_products|{% raw %}<code>["wireless_headphones", "smart_homehub", "fitness_tracker_swatch"]</code>{% endraw %}|
|時刻| last_purchase_date|{% raw %}<code>2025-12-25T08:15:30:250-0800</code>{% endraw %}|
|オブジェクト (フラット化) | user_profile|{% raw %}<code>{<br>&emsp;"first_name": "{{user.first_name}}",<br>&emsp;"last_name": "{{user.last_name}}",<br>&emsp;"email": "{{user.email}}",<br>&emsp;"loyalty_points": {{user.loyalty_points}},<br>&emsp;"preferred_categories": {{user.preferred_categories}}<br>}</code>{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## コンテキスト変数の使用 {#using-context-variables}

たとえば、次のフライトの前に、VIP ラウンジへのアクセスについて乗客に通知したいとします。このメッセージは、ファーストクラスのチケットを購入した乗客にのみ送信する必要があります。コンテキスト変数は、この情報を追跡する柔軟な方法です。

ユーザーは、飛行機のチケットを購入するときにキャンバスに入ります。ラウンジアクセスの適格性を判断するために、コンテキストステップで`lounge_access_granted`というコンテキスト変数を作成し、その後のユーザージャーニーのステップでそのコンテキスト変数を参照します。

![旅客がVIP ラウンジアクセスに適格であるかどうかを追跡するために設定されたコンテキスト変数。]({% image_buster /assets/img/context_example4.png %}){: style="max-width:90%"}

このコンテキストステップでは、{% raw %}`{{custom_attribute.${purchased_flight}}}`{% endraw %} を使用して、購入したフライトのタイプが`first_class` かどうかを判断します。

次に、{% raw %}`{{context.${lounge_access_granted}}}`{% endraw %} が`true` であるユーザーをターゲットにするメッセージステップを作成します。このメッセージは、個人化されたラウンジ情報を含むプッシュ通知となります。このコンテキスト変数に基づいて、適格な乗客は、フライト前に関連するメッセージを受け取ります。

- ファーストクラスの乗客は次のメッセージを受け取ります:「Enjoy exclusive VIP lounge access!」
- ビジネスクラスとエコノミークラスの乗客は次のメッセージを受け取ります:「Upgrade your flight for exclusive VIP lounge access.」

![購入した飛行機のチケットのタイプに応じて、送信するメッセージが異なるメッセージステップ。]({% image_buster /assets/img/context_example3.png %}){: style="max-width:90%"}

{% alert tip %}
コンテキストステップの情報を使用して、[パーソナライズされた遅延オプション]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) を追加できます。つまり、ユーザーを遅延させる変数を選択できます。
{% endalert %}

## 接続されたコンテンツ文字列のJSON への変換

コンテキストステップで[コネクテッドコンテンツ呼び出し]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call)を実行すると、整合性とエラー防止のために、呼び出しから返された JSON が文字列データ型として評価されます。この文字列をJSON に変換する場合は、`as_json_string` を使用して変換します。以下に例を示します。

{%raw%}
```liquid
{% connected_content http://example.com :save product %}
{{ product | as_json_string }}
```
{%endraw%}

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
|`personalized_message`|  {% raw %}`"Enjoy a discount of" {{promo_code}} "on delivery from your favorite" {{favorite_cuisine}} restaurants!"`{% endraw %} | 以前の変数を組み合わせたパーソナライズされたメッセージ。 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

メッセージステップでは、Liquid スニペット{% raw %}`{{context.${personalized_message}}}`{% endraw %} を使用してコンテキスト変数を参照し、各ユーザーにパーソナライズされたメッセージを配信できます。

これは、複数のコンテキストステップにも適用されます。例えば次のシーケンスを考えてみます。
1. 最初のコンテキストステップでは、`JobInfo` という変数を作成して値 `job_title` を設定します。
2. メッセージステップは {% raw %}`{{context.${JobInfo}}}`{% endraw %} を参照し、`job_title` をユーザーに表示します。
3. その後、コンテキストステップによってコンテキスト変数が更新され、`JobInfo` の値が`job_description` に変更されます。
4. `JobInfo` を参照する以降のすべてのステップで、更新された値`job_description` が使用されるようになりました。

コンテキスト変数は、キャンバス全体で最新の値を使用します。更新を行うたびに、その変数を参照する後続のすべてのステップに影響します。


