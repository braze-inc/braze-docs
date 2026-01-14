---
nav_title: チュートリアル
article_title: "チュートリアル：Liquid コードの記述"
page_order: 11
description: "このリファレンスページには、Liquid コードの使用を開始するのに役立つ、初心者向けのチュートリアルが含まれています。"
page_type: tutorial
---

# チュートリアル：Liquid コードの記述

> Liquid は初めてですか?これらのチュートリアルは、初心者向けのユースケース用のLiquidコードの作成を開始する際に役立ちます。各チュートリアルでは、条件付きロジックや演算子など、学習目標のさまざまな組み合わせについて説明します。

これらのチュートリアルを終了すると、次のことが可能になります。

- 一般的なユースケースのためのリキッドコードの記述
- 文字列の組み合わせユーザーデータに基づいてメッセージをパーソナライズするための流動的な条件付きロジック
- 変数とフィルタを使用して、属性の値を使用する方程式を記述します
- リキッドコードの基本的なコマンドを認識し、コードの動作についての一般的な理解を形成します

| チュートリアル | 学習目標 |
| --- | --- |
| [ユーザーセグメントのメッセージをパーソナライズする](#segments) | デフォルト値、条件付き論理 |
| [放棄されたカートのリマインダー](#reminders) | 演算子、条件付き論理 |
| [イベントカウントダウン](#countdown) | 変数、日付フィルター |
| [月別誕生日メッセージ](#birthday) | 変数、日付フィルター、演算子 |
| [お気に入りの製品のプロモーションを行う](#favorite-product) | 変数、日付フィルター、方程式、演算子 |
{: .reset-br-td-1 .reset-br-td-2}

## パーソナライズされたユーザーセグメントのメッセージ {#segments}

VIP の顧客や新規サブスクライバーなど、さまざまなユーザーセグメントのメッセージをカスタマイズします。

1. ユーザーの名がある場合とない場合で異なるパーソナライズされた挨拶をメッセージの冒頭に組み込みます。これを行うには、属性`first_name` と`first_name` が空白の場合に使用するデフォルト値を含むLiquid タグを作成します。このシナリオでは、「traveler」をデフォルト値として使用します。

{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
```
{% endraw %}

{: start="2"}
2\.では、ユーザーがVIP カスタマーである場合に送信するメッセージを提供しましょう。ここでは、`if` という条件付きロジックタグを使用する必要があります。このタグは、`vip_status` カスタム属性が`VIP` と等しい場合に次の Liquid が実行されることを示します。この場合、特定のメッセージが送信されます。

{% raw %}
```liquid
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
```
{% endraw %}

{: start="3"}
3\.新規サブスクライバーであるユーザーに、カスタマイズされたメッセージを送信します。条件付きロジックタグ`elsif` を使用して、ユーザの`vip_status` が`new` の場合、次のメッセージが送信されることを指定します。

{% raw %}
```liquid
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
```
{% endraw %}

{: start="4"}
4. VIPや新規でないユーザーはどうでしょうか。`else` タグを持つ他のすべてのユーザーにメッセージを送信できます。これは、前の条件が満たされない場合に、次のメッセージを送信することを指定します。次に、`endif` タグを使用して条件付きロジックを閉じることができます。これは、これ以上考慮するVIP ステータスがないためです。

{% raw %}
```liquid
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
Happy summer, {{${first_name} | default: "traveler"}}!
{% if {{custom_attribute.${vip_status}}} == 'VIP' %}
Thank you for being a VIP customer! Enjoy your exclusive discount code: VIPSUMMR464.
{% elsif {{custom_attribute.${vip_status}}} == 'new' %}
Thank you for subscribing! Enjoy your welcome discount code: NEWTRAVEL257.
{% else %}
Thanks for traveling with us! Enjoy your unique discount code: SUMMRTRVLS240.
{% endif %}
```
{% endraw %}
{% enddetails %}

## 放棄されたカートのリマインダー {#reminders}

パーソナライズされたメッセージを送信して、ユーザーにカートに残されたアイテムを思い出させましょう。さらにカートに入っている商品の数に基づいて、送信するメッセージをカスタマイズします。商品が3つ以下の場合は、すべての商品を一覧表示します。3つ以上の商品があれば、もっと簡潔なメッセージを送ります。

1. オペレータ`!=` で液体条件付きロジックを開き、ユーザのカートが空かどうかを確認してみましょう。これは"not equal" を意味します。この場合、空白値に等しくないカスタム属性`cart_items` に条件を設定します。

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
```
{% endraw %}

{: start="2"}
2\.次に焦点を絞り、演算子「>」 (「より大きい」) を使用して、カートに入っている商品が4つ以上であるかどうかを確認する必要があります。

{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
```
{% endraw %}

{: start="3"}
3\.最初の名前でユーザを挨拶するメッセージを記述するか、それが利用できない場合はデフォルト値として"there" を使用します。カートに3つ以上の項目がある場合は、何を記載すべきかを含める。完全なリストでユーザを圧倒したくないので、最初の3 つの`cart_items` をリストしましょう。

{% raw %}
```liquid
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
```
{% endraw %}

{: start="4"}
4. `else` タグを使用して、前の条件が満たされていない場合 (つまり `cart_items` が空白または3未満の場合) の処理を指定し、送信するメッセージを入力します。商品が3つの場合はあまり場所を取らないので、すべて表示できます。Liquid 演算子`join` および`,` を使用して、項目をカンマで区切ってリストすることを指定します。`endif` でロジックを閉じます。

{% raw %}
```liquid
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you. 
{% endif %}
```
{% endraw %}

{: start="5"}
5. `else` と `abort_message` を使用して、カートが前の条件のいずれにも一致しない場合にメッセージを送信しないことを Liquid コードに指示します。つまり、カートが空の場合です。`endif` でロジックを閉じます。

{% raw %}
```liquid
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${cart_items}}} != blank %}
{% if {{custom_attribute.${cart_items}}} | size > 3 %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items {{custom_attribute.${cart_items[0]}}}, {{custom_attribute.${cart_items[1]}}}, {{custom_attribute.${cart_items[2]}}}, and others are waiting for you.
{% else %}
Hi {{${first_name} | default: 'there'}}, don't forget to complete your purchase! Your items: {{{custom_attribute.${cart_items}}} | join: ', '}  are waiting for you.
{% endif %}
{% else %}
{% abort_message('No items in cart') %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## イベントカウントダウン {#countdown}

記念セールまでの残り日数を記載したメッセージをユーザーに送りましょう。これを行うには、変数を使用して、属性の値を操作する方程式を作成します。

1. まず、変数 `sale_date` をカスタム属性 `anniversary_date` に割り当て、`date: "s"` フィルターを適用します。これにより、`anniversary_date` が秒単位のタイムスタンプ形式に変換され、その値が`sale_date` に割り当てられます。

{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
```
{% endraw %}

{: start="2"}
2\.また、今日のタイムスタンプをキャプチャする変数を割り当てる必要があります。変数 `today` を `now` (現在の日時) に割り当て、`date: "%s"` フィルターを適用します。

{% raw %}
```liquid
{% assign today =  'now' | date: "%s"  %}
```
{% endraw %}

{: start="3"}
3\.次に、現時点 (`today`) と Anniversary Sale (`sale_date`) の間の秒数を計算します。これを行うには、変数 `difference` を、`sale_date` から`today` を引いた値に割り当てます。

{% raw %}
```liquid
{% assign difference =  event_date | minus: today %}
```
{% endraw %}

{: start="4"}
4. ここで、`difference` をメッセージで参照できる値に変換する必要があります。これは、セールまでに何秒あるかをユーザに伝えるのが理想的ではないためです。`difference_days` を`event_date` に割り当て、`86400` で割り、日数を取得します。

{% raw %}
```liquid
{% assign difference_days = difference | divided_by: 86400 %}
```
{% endraw %}

{: start="5"}
5. 最後に、送信するメッセージを作成しましょう。

{% raw %}
```liquid
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign sale_date = {{custom_attribute.${anniversary_date}}} | date: "%s" %}
{% assign today =  'now' | date: "%s"  %}
{% assign difference =  event_date | minus: today %}
{% assign difference_days = difference | divided_by: 86400 %}
Get ready! Our Anniversary Sale is in {{ difference_days }} days!
```
{% endraw %}
{% enddetails %}

## 月別誕生日メッセージ {#birthday}

今日の月内に誕生日を迎えるすべてのユーザーに特別なプロモーションを送りましょう。今月は誕生日のないユーザーはメッセージを受け取りません。

1. まず、当月を取得します。変数`this_month` を`now` (現在の日付と時刻) に割り当て、`date: "%B"` フィルタを使用して変数が月に等しくなるように指定します。

{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
```
{% endraw %}

{: start="2"}
2\.では、ユーザの`date_of_birth` から誕生月を引き出しましょう。変数 `birth_month` を `date_of_birth` に割り当て、`date: "%B"` フィルターを使用します。

{% raw %}
```liquid
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
```
{% endraw %}

{: start="3"}
3\.ここで、月を値として持つ2 つの変数があるので、それらを条件付きロジックと比較できます。`date_of_birth` がユーザーの `birth_month` と等しいという条件を設定します。

{% raw %}
```liquid
{% if {{this_month}} == {{birth_month}} %}
```
{% endraw %}

{: start="4"}
4. 今月もユーザーの誕生月であれば、送信するメッセージを作成してみましょう。

{% raw %}
```liquid
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
```
{% endraw %}

{: start="5"}
5. `else` タグを使用して、条件が満たされない場合の動作を指定します(この月はユーザの誕生月ではないため)。

{% raw %}
```liquid
{% else %} 
```
{% endraw %}

{: start="6"}
6. ユーザーの誕生月が今月でない場合はメッセージを送信しないので、`abort_message` を使用してメッセージをキャンセルし、`endif` で条件付きロジックを閉じます。

{% raw %}
```liquid
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% assign this_month = 'now' | date: "%B" %}
{% assign birth_month = {{${date_of_birth}}} | date: "%B" %}
{% if {{this_month}} == {{birth_month}} %}
We heard {{this_month}} is a special month! Enjoy a 50% discount on your purchase with code BIRTHDAY50 until the end of {{this_month}}.
{% else %} 
{% abort_message("Not their birthday month") %}
{% endif %}
```
{% endraw %}
{% enddetails %}

## お気に入りの製品のプロモーション {#favorite-product}

最終購入日が6ヶ月以上前であれば、ユーザーのお気に入りの商品をプロモートしましょう。

1. まず、条件付きロジックを使用して、ユーザーのお気に入りの製品と最終購入日があるかどうかを確認します。

{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
```
{% endraw %}

{: start="2"}
2\.それから、ユーザーのお気に入りの商品や最終購入日がない場合は、メッセージを送信しないでくださいと記載します。

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="3"}
3\.`else` を使用して、上記の条件が満たされない場合の動作を指定します(_do_ にはユーザのお気に入りの製品と最終購入日が含まれているため)。

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="4"}
4. 購入日がある場合は、変数に割り当てる必要があります。これにより、今日の日付と比較できます。まず、本日の日付の値を作成します。このために、変数 `today` を `now` (現在の日時) に割り当て、`date: "%s"` フィルターを使用してこの値を秒単位のタイムスタンプ形式に変換します。`plus: 0` フィルタを追加して、"0" をタイムスタンプに追加します。これはタイムスタンプの値を変更しませんが、将来の方程式でタイムスタンプを使用する場合に役立ちます。


{% raw %}
```liquid
{% assign today = 'now' | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="5"}
5. 次に、変数`last_purchase_date` をカスタム属性`last_purchase_date` に割り当て、`date: "s"` フィルタを使用して、最後の購入日を秒単位でキャプチャします。`plus: 0` フィルタを再度追加します。

{% raw %}
```liquid
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
```
{% endraw %}

{: start="6"}
6. 最終購入日と本日の日付は秒単位であるため、6ヶ月間の秒数を計算する必要があります。式(約6ヶ月×30.44日×24時間×60分×60秒)を作成し、変数`six_months`に代入します。`times` を使用して、時間単位の乗算を指定します。

{% raw %}
```liquid
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
```
{% endraw %}

{: start="7"}
7. すべての時間値が秒単位になったので、方程式でそれらの値を使用できます。`today_minus_last_purchase_date` という変数を割り当てます。この変数は今日の値を取り、`last_purchase_date` からこの値を差し引きます。これにより、前回の購入から何秒経過したかがわかります。

{% raw %}
```liquid
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
```
{% endraw %}

{: start="8"}
8. 次に、条件付きロジックで時間値を直接比較します。`today_minus_last_purchase_date` が6か月以上である (`>=`) という条件を定義します。つまり最後の購入日は少なくとも6か月前です。

{% raw %}
```liquid
{% if today_minus_last_purchase_date >= six_months %}
```
{% endraw %}

{: start="9"}
9\.最後の購入が少なくとも6ヶ月前だった場合に送信するメッセージを作成してみましょう。

{% raw %}
```liquid
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
```
{% endraw %}

{: start="10"}
10\.`else` タグを使用して、条件が満たされていない場合にどうなるかを指定します(購入が少なくとも6 か月前ではなかったため)。

{% raw %}
```liquid
{% else %}
```
{% endraw %}

{: start="11"}
11\.メッセージをキャンセルする `abort_message` を含めます。

{% raw %}
```liquid
{% abort_message("No favorite product or last purchase date") %}
```
{% endraw %}

{: start="12"}
12\.最後に、2つの`endif` タグで Liquid を終了します。1番目の `endif` は、お気に入りの製品または最終購入日の条件付きチェックを閉じ、2番目の`endif` は、最終購入日が6か月以上前であることの条件付きチェックを閉じます。

{% raw %}
```liquid
{% endif %}
{% endif %}
```
{% endraw %}

{% details Full Liquid code %}
{% raw %}
```liquid
{% if {{custom_attribute.${favorite_product}}} == blank or {{custom_attribute.${last_purchase_date}}} == blank %}
{% abort_message("No favorite product or last purchase date") %}
{% else %}
{% assign today = 'now' | date: "%s" | plus: 0 %}
{% assign last_purchase_date = {{custom_attribute.${last_purchase_date}}} | date: "%s" | plus: 0 %}
{% assign six_months = 6 | times: 30.44 | times: 24 | times: 60 | times: 60 %}
{% assign today_minus_last_purchase_date = {{today | minus: last_purchase_date}} %}
{% if today_minus_last_purchase_date >= six_months %}
We noticed it’s been a while since you last purchased {{custom_attribute.${favorite_product}}}. Have you checked out our latest offerings?
{% else %}
{% abort_message("Last purchase was less than six months ago") %}
{% endif %}
{% endif %}
```
{% endraw %}
{% enddetails %}
