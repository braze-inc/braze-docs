---
nav_title: ユーザー IDを設定する
article_title: Braze SDKを通じてユーザー IDを設定する
page_order: 1.1
description: "Braze SDKでユーザーIDを設定する方法を学習する。"

---

# ユーザー IDを設定する

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

![Braze アクションタグ構成設定を示すダイアログボックス。設定項目には「タグタイプ」と「外部ユーザー ID」が含まれる。]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
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

{% alert note %}
トリガー`changeUser()`が呼び出されると、現在のユーザーのセッションを閉じる過程でデータフラッシュが発生する。SDKは新しいユーザーに切り替える前に、前のユーザーに関する保留中のデータを自動的にフラッシュする。したがって、.`changeUser()`を呼び出す前に手動でデータフラッシュを要求する必要はない。
{% endalert %}

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

{% tab react native %}
```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```
{% endtab %}
{% endtabs %}

## IDネーミングのベストプラクティス {#naming-best-practices}

ユーザー ID は、[汎用一意識別子 (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier) 標準を使用して作成することをおすすめします。UUID は、ランダムで適切に分散された 128 ビットの文字列です。

あるいは、既存の一意識別子 (名前やメールアドレスなど) をハッシュ化してユーザー ID を生成することもできます。その場合は、必ず[SDK認証を]({{site.baseurl}}/developer_guide/sdk_integration/authentication/)実装し、ユーザーの偽装やなりすましを防いでほしい。

{% alert warning %}
ユーザー IDには推測されやすい値や連番を使用してはならない。これにより、組織が悪意のある攻撃やデータ漏洩に晒される可能性がある。

セキュリティを強化するには、[SDK認証]({{site.baseurl}}/developer_guide/sdk_integration/authentication/)を使用する。
{% endalert %}

最初からユーザーIDに正しい名前をつけることが重要だが、将来的にはいつでも [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/)エンドポイントを使って変更することができる。

| 推奨されないIDの種類 | 例として推奨されない |
| ------------ | ----------- |
| ユーザーが閲覧可能なプロファイル ID またはユーザー名 | JonDoe829525552 |
| 電子メールアドレス | Anna@email.com |
| 自動増分するユーザー ID | 123 |
{: .reset-td-br-1 .reset-td-br-2}

{% alert warning %}
ユーザー ID の作成方法に関する詳細を共有することは避けるべきだ。これは組織を悪意のある攻撃やデータ流出の危険に晒す可能性があるからだ。
{% endalert %}
