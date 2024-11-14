Brazeダッシュボードで、**データ設定**>**データ変換に**進む。

{% alert note %}
[古いナビゲーションを]({{site.baseurl}}/navigation)使用している場合は、「**データ」の**下に**「トランスフォーメーション」が**ある。
{% endalert %}

**トランスフォームの作成**」を選択してトランスフォームに名前を付け、編集エクスペリエンスを選択する。

![]({% image_buster /assets/img/data_transformation/data_transformation10.png %}) 変形の詳細は、編集体験のために「テンプレートを使用する」または「ゼロから始める」を選択するオプションがある。

データ変換のユースケースを含むテンプレート・ライブラリを参照するには、**Use a templateを**選択する。または、"**Start from scratch "**を選択してデフォルトのコードテンプレートを読み込む。 

ゼロから始めるのであれば、変身のための送信先を選ぶ。テンプレート・ライブラリーからコード・テンプレートを挿入することはできる。

{% details 送信先の詳細 %}
* **POST: ユーザーをトラッキングする：**ソースプラットフォームからのWebhookを、属性、イベント、購入などのユーザープロファイル更新に変換する。
* **PUT: 複数のカタログ項目を更新する：**ソースプラットフォームからのWebhookをカタログアイテムの更新に変換する。
* **DELETE: 複数のカタログ項目を削除する：**ソースプラットフォームからのWebhookをカタログアイテムの削除に変換する。
* **パッチを当てる：複数のカタログ項目を編集する：**ソースプラットフォームからのWebhookをカタログアイテムの編集に変換する。
* **POST: APIのみでメッセージを即座に送信する：**ソースプラットフォームからのWebhookを変換し、指定したユーザーに即座にメッセージを送信する。
{% enddetails %}

{% alert note %}
追加のテンプレートや送信先をご希望ですか？[製品フィードバックを]({{site.baseurl}}/user_guide/administrative/access_braze/portal/)残すことを検討する。
{% endalert %}

トランスフォームを作成すると、トランスフォームの詳細ビューが表示される。ここでは、**Webhook Detailsの**下に、このトランスフォーメーションに対して受信した最新のWebhookを表示することができ、**Transformation codeの**下に、トランスフォーメーションコードを書き込むスペースがある。

{% if include.location == "typeform" %}

![]({% image_buster /assets/img/typeform/data_transformation_typeform.png %})

次のステップで使用する**Webhook URLを**キャプチャする。

{% endif %}
