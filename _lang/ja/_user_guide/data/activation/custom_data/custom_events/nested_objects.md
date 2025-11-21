---
nav_title: ネストされたオブジェクト
article_title: カスタムイベント内の階層化オブジェクト
page_order: 1
page_type: reference
description: "この記事では、階層化 JSON データをカスタムイベントと購入のプロパティとして送信する方法と、メッセージングでそれらの階層化オブジェクトを使用する方法について説明します。"
---

# カスタムイベント内の階層化オブジェクト

> このページでは、ネストされたJSONデータをカスタムイベントおよび購入のプロパティとして送信する方法、およびメッセージングでネストされたオブジェクトを使用する方法について説明します。

階層化オブジェクト (別のオブジェクト内にあるオブジェクト) を使用して、階層化された JSON データをカスタムイベントや購入のプロパティとして送信できます。この階層化されたデータは、メッセージ内のパーソナライズされた情報のテンプレート作成、メッセージ送信のトリガー、およびユーザーのセグメント化に使用できます。

## 制限事項

- 階層化トされたデータは、[カスタムイベント]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)と[購入イベント]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/)の両方でサポートされていますが、他のイベントタイプではサポートされていません。
- 配列またはオブジェクト値を含むイベントプロパティオブジェクトには、最大 10 KB のイベントプロパティペイロードを設定できます。
- 購入イベントに対してイベントプロパティスキーマを生成することはできません。
- イベントプロパティスキーマは、過去 24 時間のカスタムイベントをサンプリングすることで生成されます。

### 最小の SDK バージョン

次の SDK バージョンでは、階層化オブジェクトがサポートされています。

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## ステップ 1: スキーマの生成

ネストされたイベントプロパティを持つ各イベントのスキーマを生成することで、カスタムイベントのネストされたデータにアクセスできます。スキーマを生成するには

1. [**データ設定**] > [**カスタムイベント**] に移動します。
2. 階層化プロパティを持つイベントについて、[**プロパティの管理**] を選択します。
3. スキーマを生成するには、<i class="fas fa-arrows-rotate"></i> ボタンを選択する。スキーマを表示するには、<i class="fas fa-plus"></i> プラスボタンを選択する。

![]({% image_buster /assets/img_archive/schema_generation_example.png %}){: style="max-width:80%;"}

今後新しいプロパティが送信される場合、それらは再生成されるまでスキーマには含まれません。スキーマは24 時間ごとに再生成できます。

## ステップ 2: 階層化オブジェクトの使用

ネストされたデータは、セグメンテーションおよびパーソナライゼーション中に参照できます。スキーマは必要ありません。使用例については、以下のセクションを参照してください。

- [API リクエストの本文](#api-request-body)
- [Liquid のテンプレート作成](#liquid-templating)
- [メッセージのトリガー](#message-triggering)
- [セグメンテーション](#segmentation)
- [パーソナライゼーション](#personalization)

### API リクエストの本文

{% tabs %}
{% tab Music Example %}

以下は、「Created Playlist」(作成された再生リスト) カスタムイベントの `/users/track` の例です。プレイリストを作成したら、以下を送信してプレイリストのプロパティをキャプチャします。
- "songs" をプロパティとしてリストするAPI リクエスト
- ソングのネストされたプロパティの配列

```
...
"properties": {
  "songs": [
    {
      "title": "Smells Like Teen Spirit",
      "artist": "Nirvana",
      "album": {
        "name": "Nevermind",
        "yearReleased": "1991"
      }
    },
    {
      "title": "While My Guitar Gently Weeps",
      "artist": "the Beatles",
      "album": {
        "name": "The Beatles",
        "yearReleased": "1968"
      }
    }
  ]
}
...
```
{% endtab %}
{% tab Restaurant Example%}

以下は、「Ordered」(注文を受けた) カスタムイベントの`/users/track` の例です。注文が完了したら、以下を送信してその注文のプロパティをキャプチャします。
- プロパティとして"r_details" をリストするAPIリクエスト
- その順序のネストされたプロパティ

```
...
"properties": {
  "r_details": {
    "name": "McDonalds",
    "identifier": "12345678",
    "location" : {
      "city": "Montclair",
      "state": "NJ"
    }
  }
}
...
```
{% endtab %}
{% endtabs %}

{% alert note %}
ネストされたカスタムイベントプロパティの場合、年が0より小さいか3000より大きい場合、Braze はこれらの値をユーザーに保存しません。
{% endalert %}

### Liquid のテンプレート作成

以下に、[前のAPI リクエスト](#api-request-body) からリクエストされたネストされたプロパティを参照するLiquid テンプレートを作成する方法を示します。

{% tabs %}
{% tab Music Example %}
「Created Playlist」(作成した再生リスト) イベントによってトリガーされるメッセージ内の Liquid でのテンプレート。

{% raw %}
`{{event_properties.${songs}[0].album.name}}`:"Nevermind"<br>
`{{event_properties.${songs}[1].title}}`:"While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab Restaurant Example %}
「Ordered」(注文を受けた) イベントによってトリガーされるメッセージ内の Liquid でのテンプレート:

{% raw %}
`{{event_properties.${r_details}.location.city}}`:"Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### メッセージのトリガー

これらのプロパティを使用してキャンペーンをトリガするには、カスタムイベントまたは購入を選択し、**ネストされたプロパティ** フィルタを追加します。メッセージのトリガーはまだアプリ内メッセージでサポートされていませんが、メッセージ内の Liquid パーソナライゼーションの階層化プロパティは引き続き表示されます。

{% tabs %}
{% tab Music Example %}

「Created Playlist」イベントから階層化プロパティを持つキャンペーンをトリガーします。

![カスタムイベントのプロパティフィルターのためにネストされたプロパティを選択するユーザー。]({% image_buster /assets/img/nested_object2.png %})

トリガー条件 `songs[].album.yearReleased` [である] 「1968」は、1968 年にリリースされたアルバムに収録されたいずれかの曲があるイベントと一致します。配列の内部を詳しく調べるために大かっこ (`[]`) の表記を使用し、その配列内の**いずれかの**項目がイベントプロパティと一致すれば、「一致」になります。

{% alert important %}
**does not equal**フィルターは、配列内のどのプロパティも指定された値と等しくない場合にのみマッチする。<br><br>たとえば、キャンバス A のアクションベースのカスタムイベントの階層化プロパティフィルターが「smartwatch」と**等しく**、キャンバス B のアクションベースのカスタムイベントの階層化プロパティフィルターが「simphone」と**等しくない**とします。プロパティに「smartwatch」と「simphone」があれば、両方のキャンバスがトリガーされます。しかし、プロパティに "simphone "や "sim only "があれば、どちらのキャンバスもトリガーしない。
{% endalert %}

{% endtab %}
{% tab Restaurant Example %}

「Ordered」 (注文された) イベントから階層化プロパティを持つキャンペーンをトリガーします。

![カスタムイベントのために、プロパティフィルタr_details.name を追加するユーザーがマクドナルドである。]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`:"Mcdonalds"<br>
`r_details.location.city`:"Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
イベントプロパティに `[]` または `.` の文字が含まれている場合は、チャンクを二重引用符で囲んでエスケープします。例えば、`"songs[].album".yearReleased` はリテラルプロパティ `"songs[].album"` を持つイベントと一致します。
{% endalert %}

### セグメンテーション

階層化イベントプロパティに基づいてユーザーをセグメント化するには、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用する必要があります。スキーマを生成すると、階層化オブジェクトエクスプローラーが [セグメンテーション] セクションに表示されます。 

![]({% image_buster /assets/img_archive/nested_event_properties_segmentation.png %})

セグメンテーションでは、トリガーと同じ表記法を使用します (「[メッセージのトリガー](#message-triggering)」を参照)。

セグメントエクステンションを編集または作成するには、「セグメントの編集」権限が必要です。

### パーソナライゼーション

[**パーソナライゼーションの追加**] モーダルを使用して、[パーソナライゼーションタイプ] として [**イベントの詳細プロパティ**] を選択します。これにより、スキーマの生成後に階層化イベントプロパティを追加するオプションを使用できます。

![]({% image_buster /assets/img_archive/nested_event_properties_personalization.png %}){: style="max-width:70%;"}

## よくある質問

### ネストされたオブジェクトを使用すると、追加のデータポイントが記録されるのか？

この機能を追加しても、データポイントの記録方法に変更はない。ネストされたオブジェクトに基づくセグメンテーションは、セグメントエクステンションを使用するため、追加のデータポイントを使用しない。

### 送信できる階層化データの量はどの程度ですか?

1 つ以上のイベントのプロパティにネストされたデータが含まれている場合、1 つのイベントのすべての組み合わせプロパティの最大ペイロードは100KB です。そのサイズ制限を超えたリクエストは拒否されます。

