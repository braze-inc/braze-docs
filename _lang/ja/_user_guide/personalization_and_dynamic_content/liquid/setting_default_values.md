---
nav_title: デフォルト値の設定
article_title: デフォルトの液体値の設定
page_order: 5
description: "このリファレンス記事では、メッセージで使用するパーソナライゼーション 属性のデフォルト フォールバックを設定する方法について説明します。"

---

# デフォルトを設定する

{% raw %}

> 既定のフォールバックは、メッセージで使用する任意のパーソナライゼーション 属性に設定できます。 

デフォルトを追加するには、[液体フィルター][3]を"デフォルト.&quotという名前で指定します(`|`を使用して、インラインでフィルターを区別します)。

```
| default: 'Insert Your Desired Default Here'
```

デフォルトが指定されておらず、フィールドがないか、ユーザーに設定されていない場合、フィールドは空白になります。

次の例は、デフォルトを追加するための正しい構文を示しています。この例では、"Valued ユーザー" という単語は、ユーザーの`first_name` フィールドが空白または使用不可の場合、属性`{{ ${first_name} }}` を置き換えます。

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

ジャネット・ドーという名前のユーザーには、次のいずれかの方法でユーザーに耳元をアプリします。

```
Hi Janet, thanks for using the App!
```

または。。。

```
Hi Valued User, thanks for using the App!
```

{% endraw %}

[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:\#accounting-for-null-属性-values
