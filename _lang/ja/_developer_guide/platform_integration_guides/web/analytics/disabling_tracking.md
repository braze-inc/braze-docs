---
nav_title: Web SDK トラッキングの無効化
article_title: Web SDK トラッキングの無効化
platform: Web
page_order: 6
page_type: reference
description: "この記事では、Web SDK トラッキングの無効化、その理由、方法、および Web に対する影響について説明します。"

---

# Web SDKトラッキングを無効にする

{% multi_lang_include archive/web-v4-rename.md %}

> データプライバシー規制に準拠するために、Web SDK のデータトラッキングアクティビティは [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) メソッドを使用して完全に停止できます。 

このメソッドにより、`disableSDK()` の呼び出し前にロギングされたデータが同期され、このページと将来のページの読み込みに対するその後の Braze Web SDK の呼び出しはすべて無視されます。後の時点でデータ収集を再開するには、[`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk) メソッドを使用します。

ユーザーにトラッキングを停止するオプションを提供したい場合は、クリック時に`disableSDK()`を呼び出すリンクまたはボタンと、ユーザーが再度オプトインできるように`enableSDK()`を呼び出すリンクまたはボタンの2つを含むシンプルなページを作成することをお勧めします。これらのコントロールを使用して、他のデータサブプロセッサを介してトラッキングを開始または停止することもできます。

Braze SDKは`disableSDK()`を呼び出すために初期化する必要はないことに注意してください。これにより、完全に匿名のユーザーのトラッキングを無効にすることができます。逆に、`enableSDK()` は Braze SDK を初期化しないため、トラッキングを有効にするには、後で `initialize()` も呼び出す必要があります。
