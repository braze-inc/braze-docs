---
nav_title: ダークモードのテーマ
article_title: アプリ内メッセージのダークモード
page_order: 5
description: "このリファレンス記事では、Brazeアプリ内メッセージのダークモードサポートについて、ダークモードテーマの設定方法や互換性の考慮事項を含めて説明します。"
channel:
  - in-app messages

---

# ダークモードテーマ

> ダークモードは、ユーザーにシステム全体のカラープリファレンスを設定する機会を提供します（[Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme)および[iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)で導入されました）。「ダーク」テーマはバッテリー寿命を節約し、ユーザーの目の負担を軽減することを目的としており、アプリ開発者にとってユーザーが好むダークカラーテーマを実装するための簡単な方法を提供します。

Braze のアプリ内メッセージは、切り替え用のダークテーマの追加をサポートしているため、ユーザーの好みに合わせて適切な色のメッセージを配信したり、アプリのデザインとの一貫性を維持したりするうえで役立ちます。

## ダークモードの仕組み

Android 10 以降または iOS 13 以降のバージョンを使用しているユーザーは、デバイスの設定でダークモードのオン / オフを切り替えることができます。

ダークモードが有効になっている場合、デバイスのネイティブメニューと画面（プッシュ通知、デバイス設定など）はダークグレーに変更されます。また、アプリのコードで代替テーマを指定することにより、アプリでダークモードをサポートすることもできます。

## ダークモードテーマの設定

この新しい [ダークモード] オプションは、[アプリ内メッセージの作成]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/)画面の [スタイル] タブにあり、デバイスをダークモードにしているユーザー向けに代替のカラーテーマを簡単に追加できます。

<<<<<<< HEAD
![アプリ内メッセージ作成時のスタイルタブのライトモードスタイルとダークモードスタイルの間のユーザー切り替える]]({% image_buster /assets/img_archive/iam-dark-mode.gif %})
=======
\![アプリ内メッセージ作成時のスタイルタブのライトモードスタイルとダークモードスタイルの間のユーザー切り替える]]({% image_buster /assets/img_archive/iam-dark-mode.gif %})
>>>>>>> main

このオプションを有効にすると、カラーピッカーを使用してアプリ内メッセージのダークテーマの色を選択するか、既存の[カラープロファイル]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile)を選択して既存のダークまたはライトテーマを再利用できます。

{% alert note %}
アプリが独自のダークテーマを提供していなくても、この機能を使用できます。ただし、ダークモードをサポートしていないデバイスでは、デフォルトでライトテーマが表示されます。Androidでアプリ内メッセージが表示されている間にデバイスのテーマを変更しても、そのアプリ内メッセージに使用されるテーマは変更されません。
{% endalert %}

### ダークモードを一貫して使用する

すべてのアプリ内メッセージにダークモードを使用するには、**テンプレート** > **アプリ内メッセージテンプレート** に移動します。

そこから、ドロップダウンから[カラー プロファイルを作成]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile)を選択します。ダークモードのテーマに合わせたカラープロファイルを作成します。次に、アプリ内メッセージのダークモードバージョンを作成するたびに、そのカラープロファイルを選択して、アプリ内メッセージの外観を一貫性のあるものに保つことができます。

## 互換性

- お客様はiOSデバイスのバージョン13以上、またはAndroidデバイスのバージョン10以上である必要があります。
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ が必要です。

{% alert note %}
ダークモードアプリは、Android 10およびiOS 13で導入されました。ユーザーが電話をこれらのバージョン以降にアップグレードしていない場合、ライトテーマのみが表示されます。<br><br>選択したオーディエンスに該当するすべてのユーザーに対してキャンペーンは引き続き提供されます。ユーザーのダークモード設定やOSバージョンに関係なく。
{% endalert %}

## アプリ内メッセージでHTMLを使用する

HTMLのアプリ内メッセージにダークテーマとライトテーマを作成するには、ユーザーの好みを検出するために[`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme)CSSメディア機能を使用できます。

以下に例を示します。

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

