---
nav_title: Web SDKトラッキングを無効にする
article_title: Web SDKトラッキングを無効にする
platform: Web
page_order: 6
page_type: reference
description: "この記事では、Web SDK トラッキングの無効化、その理由、方法、および Web に対する影響について説明します。"

---

# Web SDKトラッキングを無効にする

{% multi_lang_include archive/web-v4-rename.md %}

> データプライバシー規制に準拠するために、Web SDKでのデータトラッキング活動はメソッド[`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk)を使用して完全に停止できます。 

このメソッドは、`disableSDK()`が呼び出される前に記録されたすべてのデータを同期し、このページおよび将来のページ読み込みのためのBraze Web SDKへのすべての後続の呼び出しを無視させます。後の時点でデータ収集を再開したい場合は、[`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) メソッドを使用してデータ収集を再開できます。

ユーザーにトラッキングを停止するオプションを提供したい場合は、クリック時に`disableSDK()`を呼び出すリンクまたはボタンと、ユーザーが再度オプトインできるように`enableSDK()`を呼び出すリンクまたはボタンの2つを含むシンプルなページを作成することをお勧めします。これらのコントロールを使用して、他のデータサブプロセッサを介してトラッキングを開始または停止することもできます。

Braze SDKは`disableSDK()`を呼び出すために初期化する必要はないことに注意してください。これにより、完全に匿名のユーザーのトラッキングを無効にすることができます。逆に、`enableSDK()`はBraze SDKを初期化しないため、トラッキングを有効にするにはその後`initialize()`を呼び出す必要があります。
