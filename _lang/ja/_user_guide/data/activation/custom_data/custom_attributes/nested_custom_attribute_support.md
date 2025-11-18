---
nav_title: 階層化カスタム属性
article_title: 階層化カスタム属性
alias: "/nested_custom_attribute_support/"
page_order: 1
page_type: reference
description: "このリファレンス記事では、階層化カスタム属性をカスタム属性のデータ型として使用する方法について、制限事項や使用例を含めて説明します。"
---

# 階層化カスタム属性

> このページでは、ネストされたカスタム属性について説明します。これにより、属性のセットを別の属性のプロパティとして定義できます。つまり、カスタム属性オブジェクトを定義するときに、そのオブジェクトに一連の追加属性を定義できます。

{% multi_lang_include nested_attribute_objects/about_nested_attributes.md %}

{% multi_lang_include nested_attribute_objects/supported_data_types.md %}

## 制限事項

- ネストされたカスタム属性は、Braze SDKまたはAPIを介して送信されるカスタム属性を対象としています。 
- オブジェクトの最大サイズは100KB です。
- キー名と文字列値のサイズ上限は 255 文字です。
- キー名にスペースを含めることはできません。
- ピリオド(`.`) とドル記号(`$`) は、ネストされたカスタム属性をユーザープロファイルに送信しようとする場合、API ペイロードではサポートされていない文字です。
- すべての Braze パートナーが階層化カスタム属性をサポートしているわけではありません。特定のパートナー連携がこの機能をサポートしているかどうかを確認するには、[パートナーのドキュメント]({{site.baseurl}}/partners/home)を参照してください。
- 階層化カスタム属性は、接続オーディエンスの API 呼び出しを行うときのフィルターとして使用できません。

## API の例

{% tabs local %}
{% tab Create %}
以下は、「再生回数が最も多い曲」オブジェクトを使用した `/users/track` の例です。曲のプロパティをキャプチャするために、`most_played_song` をオブジェクトとして、また一連のオブジェクトプロパティのセットとともにリストする API リクエストを送信します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "genre": "Jazz",
        "play_analytics": {
            "count": 1000,
            "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% endtab %}
{% tab Update %}
既存のオブジェクトを更新するには、リクエストに `_merge_objects` パラメーターを含む POST を `users/track` に送信します。これにより、更新内容が既存のオブジェクトデータとディープマージされます。ディープマージでは、オブジェクトの最初のレベルのみではなく、すべてのレベルが別のオブジェクトに確実にマージされます。この例では、すでに `most_played_song` オブジェクトが Braze にあり、ここでは新規フィールド `year_released` を `most_played_song` オブジェクトに追加します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "_merge_objects": true,
      "most_played_song": {
          "year_released": 1960
      }
    }
  ]
}
```

このリクエストが受信されると、カスタム属性オブジェクトは以下のようになります。

```json
"most_played_song": {
  "song_name": "Solea",
  "artist_name" : "Miles Davis",
  "album_name": "Sketches of Spain",
  "year_released": 1960,
  "genre": "Jazz",
  "play_analytics": {
     "count": 1000,
     "top_10_listeners": true
  }
}
```

{% alert warning %}
`_merge_objects` を `true` に設定する必要があります。設定しない場合、オブジェクトが上書きされます。`_merge_objects`  のデフォルト値は `false` です。
{% endalert %}

{% endtab %}
{% tab Delete %}
カスタム属性オブジェクトを削除するには、カスタム属性オブジェクトを `null` に設定して、POST を `users/track` に送信します。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": null
    }
  ]
}
```

{% alert note %}
この方法は、[ オブジェクトの配列]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes/array_of_objects)内のネストされたキーを削除するためには使用できません。
{% endalert %}

{% endtab %}
{% endtabs %}

## SDK の例

{% sdk_min_versions android:25.0.0 ios:6.1.0 web:4.7.0 %}

{% tabs local %}
{% tab Android SDK %}

**作成**
```kotlin
val json = JSONObject()
    .put("song_name", "Solea")
    .put("artist_name", "Miles Davis")
    .put("album_name", "Sketches of Spain")
    .put("genre", "Jazz")
    .put(
        "play_analytics",
        JSONObject()
            .put("count", 1000)
            .put("top_10_listeners", true)
    )

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json)
}
```

**更新**
```kotlin
val json = JSONObject()
    .put("year_released", 1960)

braze.getCurrentUser { user ->
    user.setCustomUserAttribute("most_played_song", json, true)
}
```

**削除**
```kotlin
braze.getCurrentUser { user ->
    user.unsetCustomUserAttribute("most_played_song")
}
```

{% endtab %}
{% tab Swift SDK %}

**作成**
```swift
let json: [String: Any?] = [
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": [
    "count": 1000,
    "top_10_listeners": true,
  ],
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json)
```

**更新**
```swift
let json: [String: Any?] = [
  "year_released": 1960
]

braze.user.setCustomAttribute(key: "most_played_song", dictionary: json, merge: true)
```

**削除**
```swift
braze.user.unsetCustomAttribute(key: "most_played_song")
```

{% endtab %}
{% tab Web SDK %}

**作成**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "song_name": "Solea",
  "artist_name": "Miles Davis",
  "album_name": "Sketches of Spain",
  "genre": "Jazz",
  "play_analytics": {
    "count": 1000,
    "top_10_listeners": true
  }
};
braze.getUser().setCustomUserAttribute("most_played_song", json);
```

**更新**
```javascript
import * as braze from "@braze/web-sdk";
const json = {
  "year_released": 1960
};
braze.getUser().setCustomUserAttribute("most_played_song", json, true);

```

**削除**
```javascript
import * as braze from "@braze/web-sdk";
braze.getUser().setCustomUserAttribute("most_played_song", null);
```

{% endtab %}
{% endtabs %}

## 日付をオブジェクトプロパティとして取得

日付をオブジェクトプロパティとして取得するには、`$time` キーを使用する必要があります。次の例では、「Important Dates」オブジェクトを使用して、`birthday` および `wedding_anniversary` のオブジェクトプロパティのセットを取得しています。これらの日付値は `$time` キーを持つオブジェクトであり、null 値にはできません。

{% alert note %}
最初に日付をオブジェクトプロパティとして取得していない場合は、すべてのユーザーについて `$time` キーを使用してこのデータを再送信することをお勧めします。そうしない場合、`$time` 属性を使用したときにセグメントが不完全になる可能性があります。ただし、ネストされたカスタム属性の`$time` の値が正しくフォーマットされていない場合、ネストされたカスタム属性全体は更新されません。
{% endalert %}

```json
{
  "attributes": [ 
    {
      "external_id": "time_with_nca_test",
      "important_dates": {
        "birthday": {"$time" : "1980-01-01"},
        "wedding_anniversary": {"$time" : "2020-05-28"}
      }
    }
  ]
}
```

{% alert note %}
ネストされたカスタム属性の場合、年が0 より小さいか3000 より大きい場合、Braze はこれらの値をユーザーに保存しません。
{% endalert %}

## Liquid のテンプレート作成

次の Liquid のテンプレート作成例では、前述した API リクエストから保存されたカスタム属性オブジェクトのプロパティを参照し、メッセージングでそれらを使用する方法を示します。

パーソナライゼーションタグ `custom_attribute` とドット表記を使用して、オブジェクトのプロパティにアクセスします。オブジェクトの名前 (およびオブジェクト配列を参照する場合は配列内の位置) を指定し、その後にドット (ピリオド) とプロパティ名を指定します。

{% raw %}
`{{custom_attribute.${most_played_song}[0].artist_name}}` — "Miles Davis"
<br> `{{custom_attribute.${most_played_song}[0].song_name}}` — "Solea"
<br> `{{custom_attribute.${most_played_song}[0].play_analytics.count}}` — "1000"
{% endraw %}

![リキッドを使って曲名とリスナーがその曲を再生した回数をテンプレートする]]({% image_buster /assets/img_archive/nca_liquid_2.png %})

## セグメンテーション

階層化カスタム属性に基づいてセグメントを構成し、ユーザーのターゲットをより細かく設定できます。そのためには、カスタム属性オブジェクトに基づいてセグメントにフィルターを適用し、セグメンテーションの基準にするプロパティ名と関連する値へのパスを指定します。そのパスがどのようなものかわからない場合は、[スキーマを生成](#generate-schema)し、Braze の階層化オブジェクトエクスプローラーを使用してそのパスを自動入力できます。

プロパティにパスを追加した後、**Validate** を選択して、path フィールドの値が有効であることを確認します。

![リスナーが指定された回数だけ曲を再生した、最も再生された曲カスタム属性に基づくフィルタリング]({% image_buster /assets/img_archive/nca_segmentation_2.png %})

階層化カスタム属性を使用してセグメント化するには、[**階層化カスタム属性**] フィルターを選択してドロップダウンを表示し、そこから特定の階層化カスタム属性を選択します。

![]({% image_buster /assets/img_archive/nested_custom_attributes.png %}){: style="max-width:70%;"}

階層化カスタム属性でのセグメンテーションを使用する場合、データ型ごとにグループ化された新しい比較演算子にアクセスできます。たとえば、`play_analytics.count` は数値であるため、**Number** カテゴリの下でコンパレータを選択できます。

![階層化カスタム属性のデータタイプに基づいて演算子を選択するユーザー]({% image_buster /assets/img_archive/nca_comparator.png %})

### 時間データ型へのフィルター適用

時間の階層化カスタム属性にフィルターを適用する場合、日付値を比較するときに [**年間通算日**] または [**時刻**] のカテゴリにある演算子を使用できます。 

[**年間通算日**] カテゴリの演算子を選択すると、階層化カスタム属性値のタイムスタンプ全体ではなく、比較対象として月と日のみがチェックされます。[**時刻**] カテゴリの演算子を選択すると、年を含むタイムスタンプ全体が比較されます。

### 多条件セグメンテーション

1 つのオブジェクト内で複数の条件に一致するセグメントを作成するには、**多条件セグメンテーション**を使用します。これにより、指定されたすべての条件に一致するオブジェクト配列がユーザーに少なくとも 1 つある場合、ユーザーはセグメントに入れられます。例えば、キーが空白でなく、かつ数値が 0 より大きい場合に、ユーザーはこのセグメントに該当します。

[**セグメントの Liquid をコピー**] 機能を使用してこのセグメントの Liquid コードを生成し、メッセージで使用することもできます。例えば、口座オブジェクトの配列と、アクティブで課税対象口座を持つ顧客を対象とするセグメントがあるとします。アクティブで課税対象口座のいずれかに関連する口座の目標について、顧客に貢献してもらうには、顧客に働きかけるメッセージを作成する必要があります。 

![マルチクライテリアSegmentの選択されたチェックボックスを持つサンプルSegment。]({% image_buster /assets/img_archive/nca_multi_criteria.png %})

[**セグメントの Liquid をコピー**] を選択すると、Braze によりアクティブで課税対象の口座のみを含むオブジェクト配列を返す Liquid コードが自動的に生成されます。

{% raw %}

```
{% assign segmented_nested_objects = '' | split: '' %}
{% assign obj_array = {{custom_attribute.${accounts}}} %}
{% for obj in obj_array %}
  {% if obj["account_type"] == 'taxable' and obj["active"] == true %}
    {% assign segmented_nested_objects = obj_array | slice: forloop.index0 | concat: segmented_nested_objects | reverse %}
  {% endif %}
{% endfor %}
```

ここから、`segmented_nested_objects` を使用してメッセージをカスタマイズできます。この例では、最初のアクティブな課税対象アカウントから目標を取得し、パーソナライズします。

```
Get to your {{segmented_nested_objects[0].goal}} goal faster, make a deposit using our new fast deposit feature!
```

{% endraw %}

これにより、顧客に次のメッセージが返されます。「Get to your retirement goal faster, make a deposit using our new fast deposit feature!」 (退職の目標をより早く達成しましょう。預金には弊社の新しい高速入金機能が便利です)

### 階層化オブジェクトエクスプローラーを使用したスキーマの生成{#generate-schema}

階層化オブジェクトのパスを記憶しなくても、オブジェクトのスキーマを生成してセグメントフィルターを作成できます。そのためには、次のステップを実行します。

#### ステップ 1: スキーマの生成

この例では、さきほど Braze に送信した `accounts` オブジェクト配列があるとします。

```json
"accounts": [
  {"type": "taxable",
  "balance": 22500,
  "active": true},
  {"type": "non-taxable",
  "balance": 0,
  "active": true},
 ]
```

Braze ダッシュボードで、**データ設定** > **カスタム属性** に移動します。

オブジェクトまたはオブジェクト配列を検索します。**Attribute Name**列で、**Generate Schema**を選択します。

![]({% image_buster /assets/img_archive/nca_generate_schema.png %})

{% alert tip %}
送信したデータ量によっては、スキーマの生成に数分かかる場合があります。
{% endalert %}

スキーマが生成されると、[**スキーマを生成**] ボタンの代わりに新しい <i class="fas fa-plus"></i> プラスボタンが表示されます。これをクリックすると、この階層化カスタム属性について Braze の把握している内容を確認できます。 

スキーマの生成中に、Braze は以前に送信されたデータを確認し、この属性に関するデータの最適な表現を作成します。また、Braze は階層化された値のデータ型を分析して追加します。これは、指定された階層化属性について、Braze に送信された以前のデータをサンプリングすることによって行われます。

この `accounts` オブジェクト配列では、そのなかに次の内容を含むオブジェクトがあることがわかります。

- ブール型で `active` のキーを含む (口座がアクティブかどうかは無関係)
- 数値型で `balance` (口座残高) のキーを含む
- 文字列型で `type` (非課税口座または課税対象口座) のキーを含む

![]({% image_buster /assets/img_archive/nca_schema.png %}){: style="max-width:50%" }

データの分析と表現の作成が完了したので、セグメントを作成します。

#### ステップ 2: セグメントの作成

入金を促すメッセージの送信先として、残高が 100 未満の顧客をターゲットにします。

セグメントを作成してフィルター `Nested Custom Attribute` を追加し、オブジェクトまたはオブジェクト配列を検索して選択します。ここでは、`accounts` オブジェクト配列を追加しました。 

![]({% image_buster /assets/img_archive/nca_segment_schema.png %})

[パス] フィールドの <i class="fas fa-plus"></i> プラスボタンを選択します。これにより、オブジェクトまたはオブジェクト配列の表現が表示されます。リストされている項目のいずれかを選択すると、Braze によりそれらが [パス] フィールドに挿入されます。この例では、残高を取得する必要があります。残高を選択すると、パス (この例では `[].balance`) が [パス] フィールドに自動的に入力されます。

![]({% image_buster /assets/img_archive/nca_segment_schema2.png %}){: style="max-width:70%" }

**Validate**を選択して、パスフィールドの内容が有効であることを確認し、必要に応じて残りのフィルタを構築できます。ここでは、残高が 100 未満でなければならないと指定しました。

![]({% image_buster /assets/img_archive/nca_segment_schema_3.png %})

操作完了です。データの構造を知らなくても、階層化カスタム属性を使用してセグメントを作成しました。Braze の階層化オブジェクトエクスプローラーによってデータが視覚的に表現されるため、セグメントの作成に必要なものを調べて正確に選択できました。

### 階層化カスタム属性の変更のトリガー

階層化カスタム属性オブジェクトを変更するタイミングをトリガーできます。このオプションは、オブジェクト配列の変更には使用できません。パスエクスプローラーを表示するオプションが表示されない場合は、スキーマを生成したかどうかを確認してください。 

![]({% image_buster /assets/img_archive/nca_triggered_changes2.png %})

例えば、次のアクションベースのキャンペーンでは、[**カスタム属性値を変更**] の新しいトリガーアクションを追加して、基本設定で最寄りのオフィスを変更したユーザーをターゲットにすることができます。 

![]({% image_buster /assets/img_archive/nca_triggered_changes.png %})

### パーソナライゼーション

[**パーソナライゼーションの追加**] モーダルを使用して、階層化カスタム属性をメッセージングに挿入することもできます。[パーソナライゼーションタイプ] として [**階層化カスタム属性**] を選択します。次に、最上位の属性と属性キーを選択します。 

例えば、以下のパーソナライゼーションモーダルでは、ユーザーの基本設定に基づいて最寄りのオフィスの階層化カスタム属性が挿入されます。

![]({% image_buster /assets/img_archive/nca_personalization.png %}){: style="max-width:70%" }

{% alert tip %}
階層化カスタム属性を挿入するオプションが表示されない場合は、スキーマが生成されていることを確認してください。
{% endalert %}

### スキーマの再生成{#regenerate-schema}

スキーマは、その生成後、 24 時間に 1 回再生成できます。このセクションでは、スキーマを再生成する方法について説明します。スキーマの詳細については、この記事の[スキーマの生成](#generate-schema)に関するセクションを参照してください。

階層化カスタム属性のスキーマを再生成するには、次の手順に従います。:

1. **[データ設定**] > [**カスタム属性**] に移動します。
2. 階層化カスタム属性を検索します。
3. 属性の**Attribute Name** 列で、<i class="fas fa-plus"></i> を選択してスキーマを管理します。
4. モーダルが表示されます。[**スキーマを再生成**] を選択します。

スキーマが最後に再生成されてから 24 時間以内は、スキーマを再生成するオプションが無効になります。スキーマを再生成しても、新しいオブジェクトの検出のみが行われ、現在スキーマに存在するオブジェクトは削除されません。

{% alert important %}
既存のオブジェクトを含むオブジェクト配列のスキーマをリセットするには、新しいカスタム属性を作成する必要があります。スキーマの再生成では既存のオブジェクトは削除されません。
{% endalert %}

スキーマの再生成後にデータが期待どおりに表示されない場合は、属性が十分に頻繁に取り込まれない可能性があります。ユーザーデータは、指定した階層化属性について Braze に送信された以前のデータに基づいてサンプリングされます。十分な量の属性が取り込まれていないと、スキーマ用として選択されません。

## データポイント

送信されるキーはすべてデータポイントを 1 消費します。例えば、次のオブジェクトがユーザープロファイルで初期化されると、データポイント 7 がカウントされます。

```json
{
  "attributes": [
    {
      "external_id": "user_id",
      "most_played_song": {
        "song_name": "Solea",
        "artist_name": "Miles Davis",
        "album_name": "Sketches of Spain",
        "year_released": 1960,
        "genre": "Jazz",
        "play_analytics": {
          "count": 1000,
          "top_10_listeners": true
        }
      }
    }
  ]
}
```

{% alert note %}
カスタム属性オブジェクトを `null` に更新しても、データポイント 1 が消費されます。
{% endalert %}

