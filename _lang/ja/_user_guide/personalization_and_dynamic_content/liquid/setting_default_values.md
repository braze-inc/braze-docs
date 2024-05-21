---
nav_title: デフォルト値の設定
article_title: リキッドのデフォルト値の設定
page_order: 5
description: "このリファレンス記事では、メッセージで使用するパーソナライズ属性にデフォルトのフォールバック値を設定する方法について説明します。"

---

# デフォルト値の設定

{% raw %}

> メッセージで使用するパーソナライズ属性には、デフォルトのフォールバック値を設定できます。 

デフォルト値は、"default "という名前の[リキッドフィルター][3]（図のように、インラインでフィルターを区別するために`|` ）を指定することで追加できます。

```
| default: 'Insert Your Desired Default Here'
```

デフォルト値が提供されず、フィールドが存在しないか、ユーザーに設定されていない場合、そのフィールドはメッセージの中で空白になります。

次の例は、デフォルト値を追加するための正しい構文を示している。この場合、ユーザーの`first_name` フィールドが空白または利用できない場合、"Valued User "という文字が属性`{{ ${first_name} }}` に置き換わります。

```liquid
Hi {{ ${first_name} | default: 'Valued User' }}, thanks for using the App!
```

ジャネット・ドウというユーザーには、メッセージは次のように表示される：

```
Hi Janet, thanks for using the App!
```

それとも...

```
Hi Valued User, thanks for using the App!
```

{% endraw %}

[3]: http://docs.shopify.com/themes/liquid-documentation/filters
[31]:https://docs.shopify.com/themes/liquid/tags/variable-tags
[32]:https://docs.shopify.com/themes/liquid/tags/iteration-tags
[34]:{% image_buster /assets/img_archive/personalized_iflogic_.png %}
[37]:#accounting-for-null-attribute-values
