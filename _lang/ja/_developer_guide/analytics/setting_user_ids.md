---
nav_title: ユーザー ID の設定
article_title: Braze SDKによるユーザーIDの設定
page_order: 1.2
description: "Braze SDKでユーザーIDを設定する方法を学習する。"

---

# ユーザー ID の設定

> Braze SDKでユーザーIDを設定する方法を学習する。これは、デバイスやプラットフォームを超えてユーザーを追跡し、[ユーザーデータAPIを通じて]({{site.baseurl}}/developer_guide/rest_api/user_data/#user-data)ユーザーデータをインポートし、[メッセージングAPIを通じて]({{site.baseurl}}/api/endpoints/messaging/)ターゲットメッセージを送信するための一意の識別子である。ユーザーに固有のIDを割り当てない場合、Brazeは代わりに匿名IDを割り当てるが、割り当てるまでこれらの機能を使用することはできない。

{% alert note %}
リストにないラッパーSDKについては、代わりに関連するAndroidまたはSwiftのネイティブ・メソッドを使用する。
{% endalert %}

## 匿名ユーザーについて

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

## ユーザーIDの設定

ユーザーIDを設定するには、ユーザーが最初にログインした後、`changeUser()` メソッドを呼び出す。IDは一意でなければならず、私たちの[命名のベストプラクティスに](#naming-best-practices)従わなければならない。

代わりに一意な識別子をハッシュする場合は、ハッシュ関数の入力を正規化するようにしてほしい。例えば、メールアドレスをハッシュ化する場合、先頭や末尾のスペースを取り除き、ローカライゼーションを考慮する。

{% tabs local %}
{% tab アンドロイド %}
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

{% tab ウェブ %}
標準的なWeb SDK実装の場合、以下の方法を使用できる：

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

代わりにGoogle Tag Managerを使いたい場合は、**Change User**タグタイプを使って[`changeUser` メソッドを](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)呼び出すことができる。ユーザーがログインするとき、あるいは一意の識別子（`external_id` ）で識別されるときは、必ずこれを使用する。

現行のユーザーの一意のID を**外部ユーザー ID** フィールドに入力してください。通常は、Web サイトから送信されたデータレイヤー変数を使用して入力します。

![Braze アクションタグ構成設定を示すダイアログボックス。含まれる設定は、「タグのタイプ」と「外部ユーザーID」です。]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab コルドバ %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ロク %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab ユニティ %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab アンリアル・エンジン %}
```cpp
UBraze->ChangeUser(TEXT("YOUR_USER_ID_STRING"));
```
{% endtab %}
{% endtabs %}

{% alert warning %}
**ユーザーがログアウトしたときに、固定デフォルトIDやコール`changeUser()` を割り当てないこと。**そうすることで、共有デバイスに以前ログインしたユーザーを再度エンゲージメントすることができなくなる。その代わりに、すべてのユーザーIDを別々に管理し、アプリのログアウト・プロセスで以前にログインしたユーザーに切り替えることができるようにする。新しいセッションが始まると、Brazeは新しくアクティブになったプロファイルのデータを自動的にリフレッシュする。
{% endalert %}

## ユーザーのエイリアス

### 仕組み

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### ユーザーエイリアスの設定

ユーザーエイリアスは、名前とラベルの2つの部分で構成される。名前は識別子そのものを指し、ラベルはその識別子が属するタイプを指す。例えば、サードパーティのカスタマーサポートプラットフォームに外部ID`987654` を持つユーザーがいる場合、Brazeでそのユーザーに`987654` という名前と`support_id` というラベルのエイリアスを割り当てることで、プラットフォーム間でそのユーザーを追跡することができる。

{% tabs local %}
{% tab Android %}
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

{% tab ウェブ %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab REST API %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}
{% endtabs %}

## IDネーミングのベストプラクティス {#naming-best-practices}

ユーザーIDは[Universally Unique Identifier（UUID）](https://en.wikipedia.org/wiki/Universally_unique_identifier)標準を使って作成することを推奨する。

あるいは、既存の一意識別子（名前やメール・アドレスなど）をハッシュ化してユーザーIDを生成することもできる。その場合は、必ず[SDK認証を]({{site.baseurl}}/developer_guide/authentication/)実装し、ユーザーの偽装やなりすましを防いでほしい。

ユーザーIDに最初から正しい名前を付けることは不可欠だが、将来的にはいつでも [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration/)エンドポイントを使って変更できる。

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
