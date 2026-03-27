---
nav_title: ユーザー IDを設定する
article_title: Braze SDKを通じてユーザー IDを設定する
page_order: 1.1
description: "Braze SDKでユーザーIDを設定する方法を学習します。"

---

# ユーザー IDを設定する

> Braze SDKでユーザーIDを設定する方法を学習します。これは、デバイスやプラットフォームを超えてユーザーを追跡し、[ユーザーデータAPI]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)を通じてユーザーデータをインポートし、[メッセージングAPI]({{site.baseurl}}/api/endpoints/messaging/)を通じてターゲットメッセージを送信するための一意の識別子です。ユーザーに固有の ID を割り当てない場合、Braze は代わりに匿名 ID を割り当てますが、割り当てるまでこれらの機能を使用することはできません。

{% alert note %}
リストされていないラッパーSDK の場合は、代わりに関連するネイティブ Android または Swift メソッドを使用してください。
{% endalert %}

## 匿名ユーザーについて

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

### 匿名ユーザーのトラッキングを防止する

ユーザーが識別される前にデータを収集しないユースケースの場合、ユーザーがログインして `external_id` が利用可能になるまで Braze SDK の初期化を遅延させることができます。コード内にフラグを設定し、ユーザーがサインインしたときに `true` に切り替え、そのフラグが設定されている場合にのみ SDK を初期化します。

{% alert warning %}
初期化の遅延は、ユーザーがアプリを**初めて**ダウンロードしたとき（`external_id` が設定される前）にのみ行ってください。ユーザーがサインアウトしたり新しいセッションを開始したりするたびに SDK の初期化を妨げると、アプリ内メッセージやコンテンツカードアセットのプリフェッチに干渉し、それらのキャンペーンの配信エラーにつながる可能性があります。
{% endalert %}

## ユーザーIDの設定

ユーザーIDを設定するには、ユーザーが最初にログインした後に `changeUser()` メソッドを呼び出します。ID は一意であり、[命名のベストプラクティス](#naming-best-practices)に従っている必要があります。

代わりに一意な識別子をハッシュする場合は、ハッシュ関数の入力を正規化してください。たとえば、メールアドレスをハッシュする場合は、先頭または末尾のスペースを削除し、ローカライゼーションを考慮します。

{% tabs local %}
{% tab WEB %}
標準の Web SDK 実装では、以下の方法を使用できます。

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

代わりに Google Tag Manager を使いたい場合は、**Change User** タグタイプを使って [`changeUser` メソッド](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)を呼び出すことができます。ユーザーがログインするとき、あるいは一意の `external_id` 識別子で識別されるときは、必ずこれを使用してください。

現在のユーザーの一意の ID を**External User ID** フィールドに入力してください。通常は、Web サイトから送信されたデータレイヤー変数を使用して入力します。

![Braze アクションタグの設定を示すダイアログボックス。設定項目には「tag type」と「external user ID」が含まれます。]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab ANDROID %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab REACT NATIVE %}
```javascript
Braze.changeUser("YOUR_USER_ID_STRING");
```
{% endtab %}
{% endtabs %}

### `changeUser()` の仕組み

`changeUser()` を呼び出すと、以下の動作が適用されます。

- すでに設定されている**同じ**ユーザー ID で `changeUser()` を呼び出しても、セッション数には影響しません。
- **異なる**ユーザー ID で `changeUser()` を呼び出すと、現在のセッションが自動的に終了し、新しいセッションが開始されます。
- 匿名ユーザーが**新しい**ユーザー ID（Braze にまだ存在しないもの）で `changeUser()` を呼び出すと、匿名プロファイルのデータが新しい識別済みプロファイルにマージされます。
- 匿名ユーザーが**既存の**ユーザー ID で `changeUser()` を呼び出すと、匿名プロファイルのデータは識別済みプロファイルにマージされません。

{% alert note %}
`changeUser()` を呼び出すと、現在のユーザーのセッションを閉じる過程でデータフラッシュがトリガーされます。SDK は新しいユーザーに切り替える前に、前のユーザーの保留中のデータを自動的にフラッシュするため、`changeUser()` を呼び出す前に手動でデータフラッシュをリクエストする必要はありません。
{% endalert %}

{% alert warning %}
単一の共有ユーザー ID（たとえば、静的なデフォルトの external ID）を割り当てたり、ユーザーがログアウトしたときに `changeUser()` を呼び出したりしないでください。そうすると、共有デバイスで以前ログインしたユーザーに再度エンゲージすることができなくなり、すべてのデータが単一のユーザー ID に対して記録されるため、他の機能が期待どおりに動作しなくなる可能性があります。代わりに、すべてのユーザー ID を個別に管理し、アプリのログアウトプロセスで以前にログインしたユーザーに切り替えられるようにしてください。新しいセッションが始まると、Braze は新しくアクティブになったプロファイルのデータを自動的に更新します。
{% endalert %}

## ユーザーエイリアス

### 仕組み

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### ユーザーエイリアスの設定

ユーザーエイリアスは、名前とラベルの 2 つの部分で構成されます。名前は識別子そのものを指し、ラベルはその識別子が属するタイプを指します。たとえば、サードパーティのカスタマーサポートプラットフォームに external ID `987654` を持つユーザーがいる場合、Braze でそのユーザーに `987654` という名前と `support_id` というラベルのエイリアスを割り当てることで、プラットフォーム間でそのユーザーを追跡できます。

{% tabs local %}
{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab rest api %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}

{% tab react native %}
```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```
{% endtab %}
{% endtabs %}

## ID 命名のベストプラクティス {#naming-best-practices}

ユーザー ID は、[Universally Unique Identifier (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier) 標準を使用して作成することをおすすめします。UUID は、ランダムで適切に分散された 128 ビットの文字列です。

あるいは、既存の一意識別子（名前やメールアドレスなど）をハッシュ化してユーザー ID を生成することもできます。その場合は、必ず [SDK 認証]({{site.baseurl}}/developer_guide/sdk_integration/authentication/)を実装し、ユーザーのなりすましを防いでください。

{% alert warning %}
ユーザー ID には推測されやすい値や連番を使用しないでください。これにより、組織が悪意のある攻撃やデータ漏洩にさらされる可能性があります。

セキュリティを強化するには、[SDK 認証]({{site.baseurl}}/developer_guide/sdk_integration/authentication/)を使用してください。
{% endalert %}

最初からユーザー ID に正しい名前をつけることが重要ですが、将来的にはいつでも [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/) エンドポイントを使って変更できます。

| 推奨されない ID の種類 | 推奨されない例 |
| ------------ | ----------- |
| ユーザーが閲覧可能なプロファイル ID またはユーザー名 | JonDoe829525552 |
| メールアドレス | Anna@email.com |
| 自動増分するユーザー ID | 123 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
ユーザー ID の作成方法に関する詳細を共有することは避けてください。これにより、組織が悪意のある攻撃やデータ漏洩にさらされる可能性があります。
{% endalert %}