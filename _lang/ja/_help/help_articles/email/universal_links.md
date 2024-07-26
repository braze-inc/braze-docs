---
nav_title: ユニバーサルリンクとアプリリンク
article_title: ユニバーサルリンクとアプリリンク
page_order: 1
page_type: solution
description: "このヘルプ記事では、AppleユニバーサルリンクとAndroidアプリリンクの設定方法を説明する。"
channel: email
---

# ユニバーサルリンクとアプリリンク

AppleユニバーサルリンクとAndroidアプリリンクは、ウェブコンテンツとモバイルアプリをシームレスに移行させるために考案された仕組みである。ユニバーサルリンクがiOSに特有であるのに対し、AndroidアプリリンクはAndroidアプリに同じ目的を果たす。

## ユニバーサルリンクとアプリリンクの仕組み

ユニバーサルリンク（iOS）とアプリリンク（Android）は、Webページとアプリ内部のコンテンツの両方を指す標準的なWebリンク（`http://mydomain.com` ）である。

ユニバーサルリンクまたはApp Linkが開封されると、オペレーティングシステムは、インストールされているアプリがそのドメインに登録されているかどうかを確認する。アプリが見つかれば、Webページを読み込むことなく即座に起動する。アプリが見つからなかった場合、Web URLはユーザーのデフォルトのWebブラウザで読み込まれ、それぞれApp StoreまたはGoogle Play Storeにリダイレクトするように設定することもできる。

平たく言えば、ユニバーサルリンクはWebサイトがWebページと特定のアプリ画面を関連付けることを可能にするもので、ユーザーがアプリ画面に対応するWebページへのリンクをクリックすると、（そのアプリが現在インストールされていれば）そのアプリを直接開封することができる。

この表は、ユニバーサルリンクと従来のディープリンクの主な違いをまとめたものである：

|                        | ユニバーサルリンクとアプリリンク                                  | ディープリンク                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| プラットフォームの互換性 | iOS（バージョン9以降）およびAndroid（バージョン6.0以降）  | 様々なモバイルOSで使用されている    |
| 目的                | iOSとAndroidデバイスでWebとアプリのコンテンツをシームレスにリンクする | 特定のアプリのコンテンツにリンクする |
| 機能               | コンテキストに基づいてWebページやアプリのコンテンツに誘導する           | 特定のアプリ画面を開封する   |
| アプリのインストール       | アプリがインストールされていればアプリを開封し、そうでなければWebコンテンツを開封する | アプリのインストールが必要 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## ユースケース

ユニバーサルリンクとアプリリンクは、メールがデスクトップとモバイルデバイスの両方から開封・クリックできるため、メールキャンペーンに最もよく使用される。

チャンネルによっては、これらのリンクがうまく機能しないものもある。例えば、プッシュ通知、アプリ内メッセージ、コンテンツカードは、スキームベースのディープリンク(`mydomain://`)を使うべきである。

{% alert note %}
Androidアプリのリンクには、ドメインからのリンクを他のウェブURLとは別に扱うロジックを持つカスタム`IBrazeDeeplinkHandler` 。代わりにディープリンクを使い、メール以外のチャネルでもリンクのやり方を統一する方が簡単かもしれない。
{% endalert %}

## 前提条件

ユニバーサルリンクとアプリリンクを使用する：

- WebサイトはHTTPSでアクセスできなければならない。
- アプリがApp Store（iOS）またはGoogle Play Store（Android）で提供されていること。

## ユニバーサルリンクとアプリリンクの設定

アプリがユニバーサルリンクまたはApp Linksをサポートするためには、iOSとAndroidの両方が、リンクドメインでホストされる特別な権限ファイルを必要とする。このファイルには、どのアプリがそのドメインからのリンクを開封できるか、またiOSの場合は、これらのアプリがどのパスを開封することが許可されているかの定義が含まれている：

- **iOS: **アップルアプリサイト協会（AASA）ファイル
- **Android :**デジタル資産リンクファイル

この権限ファイルに加え、アプリ内で設定される、アプリが開封を許可されるリンクドメインのハードコード定義がある：

- **iOS: **Xcodeで "Associated Domains "として設定する。
- **Android :**アプリの`AndroidManifest.xml` ファイルで定義されている。

この2つの部分からなるドメインとアプリの関連付けは、ユニバーサルリンクやアプリリンクが機能するために必要であり、どのアプリも特定のドメインからのリンクをハイジャックしたり、どのドメインも特定のアプリを開封したりすることを防ぐ。

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

これらのステップは、アップル開発者ドキュメントからの引用である。詳しくは、[アプリやWebサイトからコンテンツへのリンクを許可する](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc)を参照のこと。

### ステップ 1:アプリの権限を設定する

{% alert note %}
[Xcode 13以降では](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/)、Xcodeが自動的にエンタイトルメントのプロビジョニングを処理することができる。[ステップ1cまで](#step-1c)スキップして、問題があればこの手順を参照すればよい。
{% endalert %}

#### ステップ 1a: アプリを登録する {#step-1a}

1. developer.apple.com 、ログインする。
2. **証明書、識別子、プロファイル**」をクリックする。
3. **識別子を**クリックする。
4. アプリ識別子がまだ登録されていない場合は、+をクリックして作成する。
   a. **名前を**入力する。これは何でも構わない。
   b. **バンドルIDを**入力する。あなたは、適切なビルドターゲットのために、Xcodeプロジェクトの**General**タブからバンドルIDを見つけることができる。

#### ステップ 1b: アプリ識別子でAssociated Domainsをオンにする。

1. 既存のアプリ識別子または新規作成したアプリ識別子で、**App Services**セクションを探す。
2. **関連ドメインを**選択する。
3. \[**保存**] をクリックします。

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### ステップ1c：XcodeプロジェクトのAssociated Domainsをオンにする {#step-1c}

先に進む前に、Xcodeプロジェクトがアプリ識別子を登録したのと同じチームを選択していることを確認する。 

1. Xcodeで、プロジェクトファイルの**Capabilities**タブに行く。
2. **関連ドメインを**オンにする。

##### トラブルシューティングのヒント

もしエラーが表示された場合、"An App ID with Identifier 'your-app-id' is not available.別の文字列を入力してください」と表示されたら、次のようにする：

1. 正しいチームが選択されていることを確認する。
2. XcodeプロジェクトのBundle ID[（ステップ1a](#step-1a)）が、アプリ識別子の登録に使用したものと一致していることを確認する。

#### ステップ1d：ドメイン・エンタイトルメントを追加する

domainsセクションに、適切なドメインタグを追加する。その前に`applinks:` を付けなければならない。このケースでは、`applinks:yourdomain.com` を追加している。

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### ステップ1e：ビルド時にエンタイトルメント・ファイルが含まれていることを確認する。

プロジェクト・ブラウザで、新しいエンタイトルメント・ファイルが**ターゲット・メンバーシップの**下に選択されていることを確認する。

Xcodeはこれを自動的に処理するはずだ。

### ステップ2:AASAファイルをホストするようにWebサイトを設定する

WebサイトのドメインとiOSのネイティブアプリを関連付けるには、WebサイトでApple App Site Association（AASA）ファイルをホストする必要がある。このファイルは、iOSに対してドメインの所有権を確認する安全な方法として機能する。iOS9以前では、開発者はアプリを開封するために、何の検証もなしに任意のURIスキームを登録することができた。しかし、AASAによって、このプロセスはより安全で信頼できるものになった。

AASAファイルには、アプリのリストと、ユニバーサルリンクとして含めるべき、または除外すべきドメイン上のURLパスを含むJSONオブジェクトが含まれている。ここにAASAファイルのサンプルがある：

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": “JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`:アプリの**チームID**（チームIDを取得するには`https://developer.apple.com/account/#/membership/` ）と**バンドル識別子を組み合わせて**構築される。上記の例では、"JHGFJHHYX "がチームIDで、"com.facebook.ios"がバンドルIDである。
- `paths`:どのパスが関連付けに含まれるか、または関連付けから除外されるかを指定する文字列の配列。パスの前に`NOT` 、パスを無効にすることができる。この例では、このパス上のリンクはすべて、アプリを開封する代わりにWebに移動する。ディレクトリ内のすべてのパスをイネーブルメントするには、`*` をワイルドカードとして使い、1文字にマッチさせるには、`?` を使う（2010年から2019年までのすべての数字にマッチさせるには、/archives/201?/のように）。

{% alert note %}
これらの文字列は大文字と小文字を区別し、クエリー文字列とフラグメント識別子は無視される。
{% endalert %}

### ステップ 3:あなたのドメインでAASAファイルをホストする

AASAファイルの準備ができたら、`https://<<yourdomain>>/apple-app-site-association` または`https://<<yourdomain>>/.well-known/apple-app-site-association` のどちらかのドメインでホストすることができる。

HTTPSウェブサーバーに`apple-app-site-association` ファイルをアップロードする。このファイルは、サーバーのルートか、`.well-known` サブディレクトリに置くことができる。ファイル名に`.json` 。

{% alert important %}
iOSは、安全な接続（HTTPS）を介してのみAASAファイルの取得を試みる。
{% endalert %}

AASAファイルをホストする際には、ファイルが以下のガイドラインに従っていることを確認すること：

- HTTPSで提供される。
- `application/json` MIMEタイプを使用する。
- 128KBを超えない（iOS 9.3.1以降の要件）

### ステップ 4:ユニバーサルリンクを扱うアプリを準備する

ユーザーがiOSデバイスでユニバーサルリンクをタップすると、デバイスはアプリを起動し、[NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity)オブジェクトを送信する。その後、アプリはNSUserActivityオブジェクトに問い合わせ、どのように起動したかを調べることができる。

アプリでユニバーサルリンクをサポートするには、以下のステップを踏む：

1. アプリがサポートするドメインを指定するエンタイトルメントを追加する。
2. アプリデリゲートがNSUserActivityオブジェクトを受信したときに適切に応答するように更新する。

Xcode で、**Capabilities**タブの**Associated Domains**セクションを開封し、アプリがサポートする各ドメインのエントリを、`applinks:` を先頭に追加する。例えば、`applinks:www.mywebsite.com` 。

{% alert note %}
アップル社は、このリストを20から30ドメイン以下に制限することを推奨している。
{% endalert %}

### ステップ 5: ユニバーサル・リンクをテストする

ユニバーサルリンクをメールに追加し、テスト用デバイスに送信する。ユニバーサルリンクをSafariのURLフィールドに直接貼り付けても、アプリは自動的に開封されない。その場合、Webサイトを手動で引き下げ、それぞれのアプリを開封するよう求めるプロンプトが上部に表示されるようにする必要がある。

{% endtab %}

<!--Android instructions-->
{% tab Android %}

これらのステップは、Android開発者ドキュメントからの引用である。詳細については、[Androidアプリリンクの追加と](https://developer.android.com/training/app-links#add-app-links) [アプリコンテンツへのディープリンクの](https://developer.android.com/training/app-links/deep-linking)作成を参照のこと。

{% alert note %}
Androidアプリのリンクには、ドメインからのリンクを他のウェブURLとは別に扱うロジックを持つカスタム`IBrazeDeeplinkHandler` 。代わりにディープリンクを使い、メール以外のチャネルでもリンクのやり方を統一する方が簡単かもしれない。
{% endalert %}

### ステップ 1:ディープリンクを作成する

まず、Androidアプリのディープリンクを作成する必要がある。これは、`AndroidManifest.xml` ファイルに[インテント・フィルターを](https://developer.android.com/guide/components/intents-filters)追加することで可能になる。インテント・フィルターには、`VIEW` アクションと`BROWSABLE` カテゴリ、そしてWebサイトのURLをデータ要素に含めること。

### ステップ2:アプリとWebサイトを関連付ける

アプリとWebサイトを関連付ける必要がある。これは、デジタルアセットリンクファイルを作成することによって行うことができる。このファイルはJSON形式でなければならず、Webサイトへのリンクを開封できるAndroidアプリの詳細が含まれている。Webサイトの`.well-known` ディレクトリに設置する。

### ステップ 3:アプリマニフェストファイルを更新する

`AndroidManifest.xml` 、application要素の内部にmeta-data要素を追加する。meta-data要素には、`android:name` "asset_statements "属性と、WebサイトのURLを含む文字列配列のリソース・ファイルをポイントする`android:resource` 。

### ステップ 4:ディープリンクを扱うアプリを準備する

Androidアプリでは、着信ディープリンクを処理する必要がある。アクティビティを開始したインテントを取得し、そこからデータを抽出することでこれを行うことができる。

### ステップ 5: ディープリンクをテストする

最後に、ディープリンクをテストすることができる。メッセージングアプリやメールで自分にリンクを送り、それをクリックする。すべてが正しく設定されていれば、アプリが開封されるはずだ。

{% endtab %}
{% endtabs %}

## ユニバーサルリンク、アプリリンク、クリックトラッキング

{% alert note %}
クリック追跡リンクは通常、メールのオンボーディングの一部として設定される。顧客オンボーディングの際にこれが完了していない場合は、アカウントマネージャーに助けを求める。
{% endalert %}

当社のメール送信パートナーであるSendGridとSparkPostは、クリック追跡ドメインを使用してすべてのリンクをラップし、Brazeのメールにクリック追跡用のURLパラメータを含める。

例えば、`https://www.example.com` のようなリンクは、`https://links.email.example.com/uni/wf/click?upn=abcdef123456…` のようになる。

クリック追跡付きのメールリンクをユニバーサルリンクまたはアプリリンクとして機能させるには、いくつかの追加設定を行う必要がある。アプリの開封を許可するドメインとして、クリック追跡ドメイン（`links.email.example.com` ）を必ず追加すること。さらに、クリック追跡ドメインは、AASA（iOS）またはDigital Asset Links（Android）ファイルを提供する必要がある。これにより、クリックトラッキング付きのメールリンクがシームレスに機能するようになる。

すべてのクリック追跡リンクをユニバーサルリンクやアプリリンクにしたくない場合は、メール送信相手に応じてどのリンクをユニバーサルリンクにするかを指定できる。詳細は以下のセクションを参照のこと。

### センドグリッド

SendGridのクリック追跡リンクをユニバーサルリンクとして扱う：

1. AASAまたはAndroidManifestのpathPrefix値を設定し、URLパスに`/uni/` を含むリンクのみをユニバーサルリンクとして扱う。
2. リンクのアンカータグ（`<a>` ）に属性`universal="true"` を追加する。これにより、ラップされたリンクのURLパスが`/uni/` を含むように変更される。

{% alert note %}
AMPメールの場合、この属性はdata-universal="true "でなければならない。
{% endalert %}

以下に例を示します。

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\.あなたのアプリがラップリンクを適切に処理するように設定されていることを確認する。SendGridの記事「[Resolving SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links)」を参照し、オペレーティングシステムに応じたステップに従う。この記事には[iOSと](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android)用のコード例が含まれている。

この設定では、URLパスに`/uni/` を含むリンクはユニバーサルリンクとして機能し、それ以外のリンクはWebリンクとして機能する。

### スパークポスト

SparkPostのクリックトラッキングリンクをユニバーサルリンクとして扱うには、メール用のドラッグ＆ドロップエディタのアトリビューションセクションに以下の属性を追加するか、リンクのHTMLを手動で編集してリンクのアンカータグに以下の属性を含める：`data-msys-sublink="custom_path"`.

このカスタムパスによって、その値を持つURLをユニバーサルリンクとして選択的に扱うことができる。

以下に例を示します。

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

そして、アプリがカスタムパスを適切に処理するように設定されていることを確認する。SparkPostの[ディープリンクでのクリックトラッキングの使用に関する](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links)記事を参照のこと。この記事には[iOSと](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost)用のコード例が含まれている。

### クリックトラッキングによるユニバーサルリンクのトラブルシューティング

受信者がメールアプリからWebブラウザに移動した後、最終的にアプリにリダイレクトされるなど、メール内でユニバーサルリンクが期待通りに動作しない場合は、以下のヒントを参考にユニバーサルリンクの設定をトラブルシューティングしよう。

#### リンクファイルの場所を確認する

AASAファイル（iOS）またはDigital Asset Linksファイル（Android）が正しい場所にあることを確認する：

- **iOSだ：** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

これらのファイルが常に一般にアクセス可能であるようにすることが重要だ。もしアクセスできない場合は、メールのユニバーサルリンク設定のステップをミスしている可能性がある。

#### ドメイン定義を確認する

アプリが開封を許可されているドメインの定義が正しいことを確認する。

- **iOS: **アプリにXcodeで設定したAssociated Domainsを確認する[（ステップ1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c)）。クリック追跡ドメインがそのリストに含まれていることを確認する。
- **Android :**アプリ情報ページを開封する（アプリのアイコンを長押ししてⓘをクリック）。アプリ情報メニューで、**デフォルトで**開封を探し、それをタップする。アプリが開封を許可されている、検証済みのリンクがすべて表示されるはずだ。クリック追跡ドメインがそのリストに含まれていることを確認する。
