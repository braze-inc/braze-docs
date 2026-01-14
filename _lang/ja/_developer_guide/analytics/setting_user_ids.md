---
nav_title: ユーザー ID の設定
article_title: Braze SDKによるユーザーIDの設定
page_order: 1.1
description: "Braze SDKでユーザーIDを設定する方法を学習する。"

---

# ユーザー ID の設定

> Braze SDKでユーザーIDを設定する方法を学習する。これは、デバイスやプラットフォームを超えてユーザーを追跡し、[ユーザーデータAPIを通じて]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)ユーザーデータをインポートし、[メッセージングAPIを通じて]({{site.baseurl}}/api/endpoints/messaging/)ターゲットメッセージを送信するための一意の識別子である。ユーザーに固有の ID を割り当てない場合、Braze は代わりに匿名 ID を割り当てますが、あなたが割り当てるまでこれらの機能を使用することはできません。

{% alert note %}
リストされていないラッパーSDK の場合は、代わりに関連するネイティブAndroid またはSwift メソッドを使用します。
{% endalert %}

## 匿名ユーザーについて

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

## ユーザーIDの設定

ユーザーIDを設定するには、ユーザーが最初にログインした後、`changeUser()` メソッドを呼び出す。ID は一意であり、[命名のベストプラクティス](#naming-best-practices)に従っている必要があります。

代わりに一意な識別子をハッシュする場合は、ハッシュ関数の入力を正規化するようにしてほしい。たとえば、メールアドレスをハッシュする場合は、先頭または末尾のスペースを削除し、ローカライズを考慮します。

{% tabs local %}
{% tab WEB %}
標準のWeb SDK 実装では、以下の方法を使用できます。

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

代わりに Google Tag Manager を使いたい場合は、**Change User** タグタイプを使って [`changeUser`メソッド](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)を呼び出すことができます。ユーザーがログインするとき、あるいは一意の識別子（`external_id` ）で識別されるときは、必ずこれを使用する。

現行のユーザーの一意のID を**外部ユーザー ID** フィールドに入力してください。通常は、Web サイトから送信されたデータレイヤー変数を使用して入力します。

![Braze アクションタグ構成設定を示すダイアログボックス。設定項目は「タグタイプ」と「外部ユーザーID」だ。]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
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
{% endtabs %}

{% alert warning %}
**ユーザーがログアウトしたときに、静的なデフォルト ID を割り当てたり、`changeUser()` を呼び出したりしないでください。**そうすることで、共有デバイスに以前ログインしたユーザーを再度エンゲージメントすることができなくなります。その代わりに、すべてのユーザーIDを別々に管理し、アプリのログアウト・プロセスで以前にログインしたユーザーに切り替えることができるようにする。新しいセッションが始まると、Braze は新しくアクティブになったプロファイルのデータを自動的に更新します。
{% endalert %}

## ユーザーのエイリアス

### 仕組み

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### ユーザーエイリアスの設定

ユーザーエイリアスは、名前とラベルの 2 つの部分で構成されます。名前は識別子そのものを指し、ラベルはその識別子が属するタイプを指す。例えば、サードパーティのカスタマーサポートプラットフォームに外部ID`987654` を持つユーザーがいる場合、Brazeでそのユーザーに`987654` という名前と`support_id` というラベルのエイリアスを割り当てることで、プラットフォーム間でそのユーザーを追跡することができる。

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
{% endtabs %}

## IDネーミングのベストプラクティス {#naming-best-practices}

ユーザー ID は、[汎用一意識別子 (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier) 標準を使用して作成することをおすすめします。UUID は、ランダムで適切に分散された 128 ビットの文字列です。

あるいは、既存の一意識別子 (名前やメールアドレスなど) をハッシュ化してユーザー ID を生成することもできます。その場合は、必ず[SDK認証を]({{site.baseurl}}/developer_guide/authentication/)実装し、ユーザーの偽装やなりすましを防いでほしい。

最初からユーザーIDに正しい名前をつけることが重要だが、将来的にはいつでも [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/)エンドポイントを使って変更することができる。

| おすすめ | 推奨しない |
| ------------ | ----------- |
| 123e4567-e89b-12d3-a456-836199333115 | JonDoe829525552 |
| 8c0b3728-7fa7-4c68-a32e-12de1d3ed2d5 | Anna@email.com |
| f0a9b506-3c5b-4d86-b16a-94fc4fc3f7b0 | CompanyName-1-2-19 |
| 2d9e96a1-8f15-4eaf-bf7b-eb8c34e25962 | jon-doe-1-2-19 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
ユーザーIDの作成方法の詳細を共有することは、悪意のある攻撃やユーザーデータの持ち出しに組織をさらす可能性があるため、避けること。
{% endalert %}
