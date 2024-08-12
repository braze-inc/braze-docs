---
nav_title: ダークモードのテーマ
article_title: アプリ内メッセージのダークモード
page_order: 5
description: "このリファレンス記事では、暗いモードのテーマと互換性に関する考慮事項を設定する方法など、アプリ内のBraze メッセージの暗いモードのサポートについて説明します。"
channel:
  - in-app messages

---

# ダークモードのテーマ

> ダークモードでは、システム全体のカラー環境設定を設定できます([Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) および[iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/) で導入)。"Dark"テーマは、ユーザーが好む暗い色のテーマを実装しやすくする一方で、バッテリー寿命を節約し、ユーザーの目への負担を軽減することを目的としています。

アプリ内のメッセージをろう付けすると、代替の暗いテーマを追加することができます。これは、ユーザーの好みに基づいて適切なカラーメッセージをユーザーに配信するのに役立ち、アプリのデザインとの一貫性を提供するのに役立ちます。

## ダークモードの仕組み

バージョンがAndroid 10 またはiOS 13 以降のユーザーは、デバイスの設定でダークモードのオン/オフを切り替えることができます。

ダークモードを有効にすると、デバイスのネイティブメニューと画面(プッシュ通知、デバイス設定など)が濃いグレーに変わります。アプリは、アプリのコードで代替テーマを指定することで、ダークモードをサポートすることもできます。

## ダークモードテーマを設定する

[アプリ内メッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/)を作成するときにStyleタブにある新しいDark Modeオプションを使用すると、デバイスでDark Modeに入っているユーザーのための代替カラーテーマを簡単に追加できます。

![User switching between Light Mode style and Dark Mode styles in the Style tab when creating an in-app message.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

このオプションが有効になっている場合、カラーピッカーを使用してアプリ内メッセージのダークターカラーを選択するか、既存の[カラープロファイル][2]を選択して既存のダークターまたはライトテーマを再利用することができます。

{% alert note %}
この機能は、アプリが独自の暗いテーマを提供していない場合でも使用できます。ただし、ダークモードに対応していないデバイスでは、デフォルトでライトテーマが表示されます。アプリ内メッセージが表示されている間にAndroidのデバイステーマを変更しても、そのアプリ内メッセージで使用されるテーマは変更されません。
{% endalert %}

### ダークモードの一貫した使用

すべてのアプリ内メッセージにダークモードを使用するには、**Templates**> **アプリ内メッセージテンプレート** に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation) を使用している場合は、**Templates & Media** の下にこのページがあります。
{% endalert %}

そこから、ドロップダウンから[カラープロファイルの作成][2]を選択します。ダークモードのテーマに合わせてカラープロファイルを作成します。その後、アプリ内メッセージのダークモードバージョンを作成するたびに、そのカラープロファイルを選択し、アプリ内メッセージの外観を整合性を保つことができます。

## 互換性

- ユーザーは、iOS デバイスバージョン13 以降、またはAndroid デバイスバージョン10 以降である必要があります。
- Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+ が必要です。

{% alert note %}
Dark ModeアプリはAndroid 10とiOS 13で導入されました。電話機を少なくともこれらのバージョンにアップグレードしていないユーザーは、ライトテーマのみが表示されます。<br><br>キャンペーンは、ユーザーのダークモード設定やOS バージョンに関係なく、選択したオーディエンスに適格なすべてのユーザーに提供されます。
{% endalert %}

## HTML アプリ内メッセージの使用

HTML in-app メッセージ用のDark and Light テーマを作成するには、[`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) CSS メディア機能を使用して、ユーザーの好みを検出できます。

次に例を示します。

\`\`\`css
@media (prefers-color-scheme: dark) {
body {
background: #333;
color: white;
}
  }

@media (優先配色: ライト) {
body {
background: white;
color: #555;
}
  }
    \`\`\`

[2]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile
