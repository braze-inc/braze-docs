---
nav_title: デフォルト値の設定
article_title: Liquid のデフォルト値の設定
page_order: 5
description: "このリファレンス記事では、メッセージで使用するパーソナライゼーション 属性のデフォルト フォールバックを設定する方法について説明します。"

---

# デフォルト値を設定する

{% raw %}

> 既定のフォールバックは、メッセージで使用する任意のパーソナライゼーション 属性に設定できます。この記事では、デフォルト値の仕組み、設定方法、メッセージングでの使用方法について説明する。

## 仕組み

デフォルト値を追加するには、[Liquid フィルター](http://docs.shopify.com/themes/liquid-documentation/filters)を「デフォルト」という名前で指定します (インラインでフィルターを区別するには `|` を使用します)。

```
| default: 'Insert Your Desired Default Here'
```

デフォルト値が提供されておらず、フィールドが存在しないか、ユーザーに設定されていない場合、メッセージの中でフィールドは空白になる。

次の例は、デフォルトを追加するための正しい構文を示しています。この場合、ユーザーの`first_name` フィールドが空の場合や利用できない場合は、「Valued User」という文字が属性`{{ ${first_name} }}` に置き換わる。

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

Janet Doe という名前のユーザーには、次のいずれかの方法でメッセージが表示されます。

```
Hi Janet, thanks for using the App!
```

または。。。

```
Hi Valued User, thanks for using the App!
```
{% endraw %}

{% alert important %}
空の値にはデフォルト値が表示されるが、空白の値には表示されない。空の値には何も含まれないが、空白の値には空白文字（スペースなど）が含まれ、他の文字は含まれない。例えば、空の文字列は`""` のようになり、空白からなる文字列は`" "` のようになります。
{% endalert %}

## 異なるデータ型にデフォルト値を設定する

上の例は、文字列にデフォルトを設定する方法を示している。値が `empty` 、`nil` (未定義)、または `false` の任意の Liquid データ型 (文字列、ブール値、配列、オブジェクト、数値を含む) のデフォルト値を設定できます。

### ユースケース:ブール値

例えば、`premium_user` というブーリアンカスタム属性があり、ユーザーのプレミアムステータスに基づいてパーソナライズされたメッセージを送信したいとしよう。プレミアムステータスを設定していないユーザーもいるので、そのようなユーザーを捕捉するためにデフォルト値を設定する必要がある。

1. `premium_user` 属性に`is_premium_user` という変数を割り当て、デフォルト値を `false` とします。つまり、`premium_user` が`nil` の場合、`is_premium_user` のデフォルト値は `false` になります。 

{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
```

{: start="2"}
2\.次に、条件付きロジックを使用して、`is_premium_user` が `true` の場合に送信するメッセージを指定します。言い換えれば、`premium_user` が`true` の場合、何を送ればいいのか、ということだ。また、ユーザーの名が不明な場合に備えて、ユーザーの名にもデフォルト値を割り当てます。

```liquid
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
```

{: start="3"}
3\.最後に、`is_premium_user` が`false` の場合（つまり `premium_user` が`false` または`nil` の場合）に送信するメッセージを指定します。その後、条件ロジックを閉じます。

```liquid
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
```liquid
{% assign is_premium_user = {{custom_attribute.${premium_user}}} | default: false %}
{% if is_premium_user %}
Hi {{${first_name} | default: 'premium user'}}, thank you for being a premium user!
{% else %}
Hi {{${first_name} | default: 'valued user'}}, consider upgrading to premium for more benefits!
{% endif %}
```
{% endraw %}
{% enddetails %}

### ユースケース:数値

例えば、`reward_points` という数値のカスタム属性があり、ユーザーの報酬ポイントをメッセージとして送信したいとしよう。報酬ポイントが設定されていないユーザーもいるので、そのようなユーザーを考慮してデフォルト値を設定する必要がある。

1. メッセージの開始時に、ユーザーの名を指定します。ユーザーの名が不明な場合はデフォルト値 `Valued User` を使用します。

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\.カスタム属性 `reward_points` とデフォルト値 `0` を使用して、ユーザーのリワードポイント数をメッセージの最後に記載します。`reward_points` の値が `nil` であるすべてのユーザーには、リワードポイントとして `0` がメッセージに記載されます。

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}, you have {{custom_attribute.${reward_points} | default: 0}} reward points.
```
{% endraw %}

### ユースケース:オブジェクト

例えば、`city` と`state` のプロパティを含む、`location` という階層化カスタム属性オブジェクトがあるとしよう。これらのプロパティが設定されていない場合は、ユーザーが設定するように促したい。

1. ユーザーを名で呼び、名前がわからない場合に備えてデフォルト値を含める。

{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}},
```
{% endraw %}

{: start="2"}
2\.ユーザーの位置情報を確認したいというメッセージを書く。

{% raw %}
```liquid
We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.
```
{% endraw %}

{: start="3"}
3\.ユーザーの所在地をメッセージに挿入し、addressプロパティが設定されていない場合のデフォルト値を割り当てる。

{% raw %}
```liquid
Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
```liquid
Hi {{${first_name} | default: 'valued user'}}

We'd like to confirm the location associated with your account. We use this location to send you promotions and offers for stores nearest you. You can update your location in your profile settings.

Your location:
City: {{custom_attribute.${address.city} | default: 'Unknown'}}
State: {{custom_attribute.${address.state} | default: 'Unknown'}}
```
{% endraw %}
{% enddetails %}

### ユースケース:配列

例えば、`destination` と`departure_date` というプロパティを持つトリップを含む、`upcoming_trips` という配列カスタム属性があるとしよう。スケジュールされた旅行の有無に基づき、パーソナライズされたメッセージをユーザー群に送りたい。

1. `upcoming_trips` が`empty` の場合、メッセージを送信しないことを指定する条件付きロジックを書く。

{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == empty %}
{% abort_message('No upcoming trips scheduled') %}
```
{% endraw %}

{: start="2"}
2\.`upcoming_trips` にコンテンツがある場合に送信するメッセージを指定する：<br><br>**2a.**ユーザーを指定し、ユーザーの名前が不明な場合に備えてデフォルト値を含めます。<br>**2b.**`for` タグを使用して、`upcoming_trips` に含まれる各トリップのプロパティ (または情報) を取得することを指定します。<br>**2c.**メッセージにプロパティを列挙し、`departure_date` が設定されていない場合のデフォルト値を含める。(トリップの作成には`destination` が必要なので、デフォルト値を設定する必要はないとしよう)。<br>**2d.**`for` タグを閉じ、次に条件ロジックを閉じます。

{% raw %}
```liquid
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}

{% details 完全な Liquid コード %}
{% raw %}
```liquid
{% if {{custom_attribute.${upcoming_trips}}} == blank %}
{% abort_message('No upcoming trips scheduled') %}
{% else %}
Hello {{${first_name} | default: 'fellow traveler'}},
  Here are your upcoming trips:
  <ul>
  {% for trip in {{custom_attribute.${upcoming_trips}}} %}
    <li>
      Destination: {{trip.destination}}
      Departure Date: {{trip.departure_date | default: 'Date not set'}}
    </li>
  {% endfor %}
  </ul>
{% endif %}
```
{% endraw %}
{% enddetails %}

[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[37]:#accounting-for-null-attribute-values
