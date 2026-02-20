## トラッキングを無効にする

{% multi_lang_include archive/web-v4-rename.md %}

{% tabs %}
{% tab standard implementation %}
Web SDKのデータ追跡アクティビティを無効にするには、以下のメソッドを使用する。 [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk).これにより、`disableSDK()` が呼び出される前に記録されたすべてのデータが同期され、このページと今後のページ読み込みに対する、その後のすべてのBraze Web SDKの呼び出しが無視される。
{% endtab %}

{% tab google tag manager %}
Web トラッキングを無効または再度有効にするには、それぞれ**トラッキング無効**タグタイプまたは**トラッキング再開**タグタイプを使用します。これら2 つのオプションは、[`disableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) および[`enableSDK`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) を呼び出します。
{% endtab %}
{% endtabs %}

### ベストプラクティス

ユーザーにトラッキングを停止するオプションを提供するには、2つのリンクまたはボタンを持つシンプルなページを構築することを推奨する。1つはクリックされたときに`disableSDK()` 、もう1つは`enableSDK()` 、ユーザーがオプトインに戻れるようにする。これらのコントロールを使用して、他のデータサブプロセッサを介してトラッキングを開始または停止することもできます。

{% alert note %}
Braze SDKは、`disableSDK()` を呼び出すために初期化する必要がないため、完全匿名ユーザーのトラッキング 追跡を無効にすることができる。逆に、`enableSDK()` は Braze SDK を初期化しないため、トラッキングを有効にするには、後で `initialize()` も呼び出す必要があります。
{% endalert %}

## データトラッキングを再開する

データ収集を再開するには [`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)メソッドを使う。
