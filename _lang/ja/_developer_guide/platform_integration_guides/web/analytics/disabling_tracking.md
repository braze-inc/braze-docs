---
nav_title: Web SDK トラッキングの無効化
article_title: Web SDK トラッキングの無効化
platform: Web
page_order: 6
page_type: reference
description: "この記事では、Web SDKトラッキングを無効にする理由、方法、およびWebへの影響について説明します。"

---

# Web SDK トラッキングを無効にする

{% multi_lang_include archive/web-v4-rename.md %}

> データプライバシー規制に準拠するために、iOS SDK のデータトラッキングアクティビティは [`disableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#disablesdk) メソッドを使用して完全に停止できます。 

このメソッドは、`disableSDK()`呼び出される前にログに記録されたデータを同期し、このページでの Braze Web SDK へのその後の呼び出しと今後のページの読み込みはすべて無視されます。後でデータ収集を再開したい場合は、[`enableSDK()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#enablesdk)メソッドを使用してデータ収集を再開できます。

トラッキングを停止するオプションをユーザーに提供したい場合は、2 つのリンクまたはボタンを含むシンプルなページを作成することをおすすめします。1 `disableSDK()` つはクリック時に呼び出され、もう 1 `enableSDK()` つはユーザーがオプトインできるように呼び出すものです。これらのコントロールを使用して、他のデータサブプロセッサを介して追跡を開始または停止することもできます。

なお、Braze SDK は呼び出し時に初期化する必要がないため`disableSDK()`、完全に匿名のユーザーのトラッキングを無効にすることができます。逆に、Braze SDK `enableSDK()` は初期化されないため、`initialize()`後で呼び出して追跡を有効にする必要があります。
