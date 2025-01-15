---
nav_title: 階層化オブジェクト
article_title: カスタムイベント内の階層化オブジェクト
page_order: 1
page_type: reference
description: "この記事では、階層化 JSON データをカスタムイベントと購入のプロパティとして送信する方法と、メッセージングでそれらの階層化オブジェクトを使用する方法について説明します。"
---

# カスタムイベント内の階層化オブジェクト

> この記事では、階層化 JSON データをカスタムイベントと購入のプロパティとして送信する方法と、メッセージングでそれらの階層化オブジェクトを使用する方法について説明します。

階層化オブジェクト (別のオブジェクト内にあるオブジェクト) を使用して、階層化された JSON データをカスタムイベントや購入のプロパティとして送信できます。この階層化されたデータは、メッセージ内のパーソナライズされた情報のテンプレート化、メッセージ送信のトリガー、およびセグメンテーションに使用できます。

## 制限事項

- 階層化トされたデータは、[カスタムイベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/)と[購入イベント]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/purchase_events/)の両方でサポートされていますが、他のイベントタイプではサポートされていません。
- 配列またはオブジェクト値を含むイベントプロパティオブジェクトには、最大 10 KB のイベントプロパティペイロードを設定できます。
- 購入イベントに対してイベントプロパティスキーマを生成することはできません。
- イベントプロパティスキーマは、過去 24 時間のカスタムイベントをサンプリングすることで生成されます。

### 最小の SDK バージョン

次の SDK バージョンでは、階層化オブジェクトがサポートされています。

{% sdk_min_versions swift:5.0.0 android:1.0.0 web:3.3.0 %}

## ステップ 1: スキーマの生成

カスタムイベント内の階層化データにアクセスするには、階層化イベントプロパティを使用して、各イベントのスキーマを生成します。スキーマを生成するには、次のステップに従います。

1. [**データ設定**] > [**カスタムイベント**] に移動します。
2. 階層化プロパティを持つイベントについて、[**プロパティの管理**] を選択します。
3. スキーマを生成するには、<i class="fas fa-arrows-rotate"></i> ボタンを選択する。スキーマを表示するには、<i class="fas fa-plus"></i> プラスボタンを選択する。

![][6]{: style="max-width:80%;"}

## ステップ 2: 階層化オブジェクトの使用

スキーマを生成すると、セグメンテーション中およびパーソナライゼーション中に階層化データを参照できます。使用例については、以下のセクションを参照してください。

- [API リクエストの本文](#api-request-body)
- [Liquid のテンプレート作成](#liquid-templating)
- [メッセージのトリガー](#message-triggering)
- [セグメンテーション](#segmentation)
- [パーソナライゼーション](#personalization)

### API リクエストの本文

{% tabs %}
{% tab 音楽の例 %}

以下は、「Created Playlist」(作成された再生リスト) カスタムイベントの `/users/track` の例です。再生リストが作成されたら、再生リストのプロパティを収集するために、プロパティとして「songs」(曲) と 曲の階層化プロパティの配列をリストする API リクエストを送信します。

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
{% tab レストランの例%}

以下は、「Ordered」(注文を受けた) カスタムイベントの`/users/track` の例です。注文が完了した後、その注文のプロパティを収集するために、プロパティとして「r_details」とその注文の階層化プロパティをリストする API リクエストを送信します。

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

### Liquid のテンプレート作成

次の Liquid テンプレートの例は、前述の API リクエストから保存された階層化プロパティを参照し、Liquid メッセージングで使用する方法を示しています。Liquid とドット表記を使用して、階層化されたデータを詳細に検索し、メッセージに含める特定のノードを検出します。

{% tabs %}
{% tab 音楽の例 %}
「Created Playlist」(作成した再生リスト) イベントによってトリガーされるメッセージ内の Liquid でのテンプレート。

{% raw %}
`{{event_properties.${songs}[0].album.name}}`:"Nevermind"<br>
`{{event_properties.${songs}[1].title}}`:"While My Guitar Gently Weeps"
{% endraw %}

{% endtab %}
{% tab レストランの例 %}
「Ordered」(注文を受けた) イベントによってトリガーされるメッセージ内の Liquid でのテンプレート:

{% raw %}
`{{event_properties.${r_details}.location.city}}`:"Montclair"
{% endraw %}

{% endtab %}
{% endtabs %}

### メッセージのトリガー

これらのプロパティを使用してキャンペーンをトリガーするには、カスタムイベントまたは購入を選択し、**階層化プロパティ**フィルターを追加します。メッセージのトリガーはまだアプリ内メッセージでサポートされていませんが、メッセージ内の Liquid パーソナライゼーションの階層化プロパティは引き続き表示されます。

{% tabs %}
{% tab 音楽の例 %}

「Created Playlist」イベントから階層化プロパティを持つキャンペーンをトリガーします。

![ユーザーがカスタムイベントでプロパティフィルター用にネストされたプロパティを選択。]({% image_buster /assets/img/nested_object2.png %})

トリガー条件 `songs[].album.yearReleased` [である] 「1968」は、1968 年にリリースされたアルバムに収録されたいずれかの曲があるイベントと一致します。配列の内部を詳しく調べるために大かっこ (`[]`) の表記を使用し、その配列内の**いずれかの**項目がイベントプロパティと一致すれば、「一致」になります。

{% alert important %}
**does not equal**フィルターは、配列内のどのプロパティも指定された値と等しくない場合にのみマッチする。<br><br>たとえば、キャンバス A のアクションベースのカスタムイベントの階層化プロパティフィルターが「smartwatch」と**等しく**、キャンバス B のアクションベースのカスタムイベントの階層化プロパティフィルターが「simphone」と**等しくない**とします。プロパティに「smartwatch」と「simphone」があれば、両方のキャンバスがトリガーされます。しかし、プロパティに "simphone "や "sim only "があれば、どちらのキャンバスもトリガーしない。
{% endalert %}

{% endtab %}
{% tab レストランの例 %}

「Ordered」 (注文された) イベントから階層化プロパティを持つキャンペーンをトリガーします。

![ユーザーがカスタムイベントのプロパティフィルター「r_details.name is McDonalds」を追加。]({% image_buster /assets/img/nested_object1.png %})

`r_details.name`:"Mcdonalds"<br>
`r_details.location.city`:"Montclair"
{% endtab %}
{% endtabs %}

{% alert note %}
イベントプロパティに `[]` または `.` の文字が含まれている場合は、チャンクを二重引用符で囲んでエスケープします。例えば、 `"songs[].album".yearReleased` はリテラルプロパティ `"songs[].album"` を持つイベントと一致します。
{% endalert %}

### セグメンテーション

階層化イベントプロパティに基づいてユーザーをセグメント化するには、[セグメントエクステンション]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/)を使用する必要があります。スキーマを生成すると、階層化オブジェクトエクスプローラーが [セグメンテーション] セクションに表示されます。 

![][4]

セグメンテーションでは、トリガーと同じ表記法を使用します (「[メッセージのトリガー](#message-triggering)」を参照)。

### パーソナライゼーション

[**パーソナライゼーションの追加**] モーダルを使用して、[パーソナライゼーションタイプ] として [**イベントの詳細プロパティ**] を選択します。これにより、スキーマの生成後に階層化イベントプロパティを追加するオプションを使用できます。

![][5]{: style="max-width:70%;"}

## よくある質問

### 階層化オブジェクトを使用すると、データポイントが追加で消費されますか?

この機能を追加したことによって消費されるデータポイントに変更はありません。階層化オブジェクトに基づくセグメンテーションでは、セグメントエクステンションが使用されるため、追加のデータポイントは使用されません。

### 送信できる階層化データの量はどの程度ですか?

1 つ以上のイベントのプロパティにネストされたデータが含まれている場合、1 つのイベントのすべての組み合わせプロパティの最大ペイロードは100KB です。そのサイズ制限を超えたリクエストは拒否されます。

[4]: {% image_buster /assets/img_archive/nested_event_properties_segmentation.png %}
[5]: {% image_buster /assets/img_archive/nested_event_properties_personalization.png %}
[6]: {% image_buster /assets/img_archive/schema_generation_example.png %}