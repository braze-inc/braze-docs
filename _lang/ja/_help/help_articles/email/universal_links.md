---
nav_title: ユニバーサルリンクとアプリリンク
article_title: ユニバーサルリンクとアプリリンク
page_order: 1
page_type: solution
description: "このヘルプ記事では、AppleのユニバーサルリンクとAndroidアプリリンクを設定する方法について説明します。"
channel: email
---

# ユニバーサルリンクとアプリリンク

AppleのユニバーサルリンクとAndroidアプリリンクは、ウェブコンテンツとモバイルアプリ間のシームレスな移行を提供するために考案されたメカニズムです。ユニバーサルリンクはiOS に固有ですが、Android アプリリンクはAndroid アプリケーションに同じ目的を提供します。

## ユニバーサルリンクとアプリリンクの仕組み

ユニバーサルリンク(iOS) とアプリリンク(Android) は、ウェブページとアプリ内のコンテンツの両方を指す標準的なウェブリンク(`http://mydomain.com`) です。

ユニバーサルリンクまたはアプリリンクが開かれると、オペレーティングシステムはインストールされているアプリがそのドメインに登録されているかどうかを確認します。アプリが見つかると、ウェブページをロードせずにすぐに起動されます。アプリが見つからない場合は、Web URL がユーザーのデフォルトのWeb ブラウザにロードされます。これは、App Store またはGoogle Play Store にそれぞれリダイレクトするように設定することもできます。

通常、ユニバーサルリンクを使用すると、ウェブサイトでウェブページを特定のアプリ画面に関連付けることができるため、ユーザーがアプリ画面に対応するウェブページへのリンクをクリックすると、アプリを直接開くことができます(アプリが現在インストールされている場合)。

次の表に、ユニバーサルリンクと従来のディープリンクの主な違いを示します。

|                        | ユニバーサルリンクとアプリケーションリンク| ディープリンク|
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| プラットフォームの互換性| iOS (バージョン9 以降) およびAndroid (バージョン6.0 以降) | さまざまなモバイルOS で使用|
| 目的| iOS およびAndroid デバイス上のウェブおよびアプリコンテンツをシームレスにリンク| 特定のアプリコンテンツへのリンク|
| 機能| コンテキストに基づいてウェブページまたはアプリコンテンツに指示| 特定のアプリ画面を開きます|
| アプリのインストール| アプリがインストールされている場合はアプリを開き、それ以外の場合はウェブコンテンツを開く| アプリをインストールする必要があります|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## 使用例

メールキャンペーンでは、デスクトップデバイスとモバイルデバイスの両方からメールを開いてクリックできるため、ユニバーサルリンクとアプリリンクが最も一般的に使用されます。

これらのリンクではうまく動作しないチャネルもあります。たとえば、プッシュ通知、アプリ内メッセージ、およびコンテンツカードでは、スキームベースのディープリンク(`mydomain://`) を使用する必要があります。

{% alert note %}
Android App Link では、他のWeb URL とは別にドメインからのリンクを処理するために、カスタムの`IBrazeDeeplinkHandler` ロジックが必要です。代わりに深いリンクを使用し、メール以外のチャネルでは一貫したリンクを維持する方が簡単かもしれません。
{% endalert %}

## 前提条件

ユニバーサルリンクとアプリリンクを使用するには:

- Web サイトにはHTTPS 経由でアクセスできる必要があります
- アプリがApp Store (iOS) またはGoogle Play Store (Android) で利用可能である必要があります

## ユニバーサルリンクとアプリリンクの設定

アプリがユニバーサルリンクまたはアプリリンクをサポートするには、iOS とAndroid の両方で、リンクドメインでホストされる特別な権限ファイルが必要です。このファイルには、どのアプリケーションがそのドメインからリンクを開くことができるか、およびiOS の場合、これらのアプリケーションが開くことができるパスの定義が含まれています。

- **iOS: **Apple App Site Association(AASA)ファイル
- **Android :**デジタルアセットリンクファイル

このパーミッションファイルに加えて、アプリ内で設定されている、アプリが開くことが許可されているリンクドメインのハードコーディングされた定義があります。

- **iOS: **Xcodeで「関連ドメイン」に設定
- **Android :**アプリの`AndroidManifest.xml` ファイルで定義

この2 部ドメインアプリの関連付けは、ユニバーサルリンクまたはApp Link が動作するために必要であり、特定のドメインまたはドメインからのリンクをハイジャックするアプリが特定のアプリを開くことを防ぎます。

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

これらの手順は、Apple 開発者のドキュメントから調整されています。詳細については、[アプリとウェブサイトがコンテンツにリンクできるようにする](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc)を参照してください。

### ステップ1:アプリケーション資格の設定

{% alert note %}
[Xcode 13 以降の](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/) では、Xcode は自動的に資格のプロビジョニングを処理できます。多くの場合、[step 1c](#step-1c)にスキップし、問題がある場合はこれらの手順を再度参照することができます。
{% endalert %}

#### ステップ1a:アプリを登録する {#step-1a}

1. developer.apple.comを実行してログインします。
2. **Certificates, Identifiers & Profiles** をクリックします。
3. **Identifiers**をクリックします。
4. App Identifier がまだ登録されていない場合は、+ をクリックして作成します。
   a.a **Name**と入力します。これは好きなものなら何でも構いません。
   b.**バンドルID**を入力します。適切なビルドターゲットのXcode プロジェクトの**General** タブからバンドルID を見つけることができます。

#### ステップ1b:アプリID の関連ドメインを有効にする

1. 既存または新しく作成したApp Identifier で、**App Services** セクションを見つけます。
2. **Associated Domains**を選択します。
3. **Save**をクリックします。

![\]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### ステップ1c:Xcode プロジェクトの関連ドメインを有効にする {#step-1c}

続行する前に、Xcode プロジェクトが、App Identifier を登録したときと同じチームが選択されていることを確認してください。 

1. Xcode で、プロジェクトファイルの**Capabilities** タブに移動します。
2. **Associated Domains**をオンにします。

##### トラブルシューティングのヒント

エラー&quot が表示された場合、識別子'your-app-id' を持つアプリケーションID は使用できません。別の文字列" を入力して、次の操作を実行します。

1. 正しいチームが選択されていることを確認します。
2. Xcode プロジェクトのバンドルID ([step 1a](#step-1a)) が、App Identifier の登録に使用したものと一致していることを確認します。

#### ステップ1d:ドメイン資格の追加

domains セクションで、適切なドメインタグを追加します。`applinks:` をプレフィックスとして使用する必要があります。この場合、`applinks:yourdomain.com` が追加されたことがわかります。

![\]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### ステップ1e:エンタイトルメントファイルがビルド時に含まれていることを確認する

プロジェクトブラウザで、新しい資格ファイルが**Target Membership** で選択されていることを確認します。

Xcode はこれを自動的に処理します。

### ステップ2:AASA ファイルをホストするようにウェブサイトを設定する

ウェブサイトドメインをiOS のネイティブアプリに関連付けるには、ウェブサイトでApple App Site Association (AASA) ファイルをホストする必要があります。このファイルは、iOS に対するドメイン所有権を検証するための安全な方法として機能します。iOS 9 より前に、開発者は、確認なしでアプリを開くためにURI スキームを登録することができました。しかし、AASAでは、このプロセスははるかに安全で信頼できるものになりました。

AASA ファイルには、アプリケーションのリストと、ユニバーサルリンクとして含めるか除外する必要があるドメイン上のURL パスを含むJSON オブジェクトが含まれます。次に、サンプルのAASA ファイルを示します。

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

- `appID`:アプリの**Team ID**(`https://developer.apple.com/account/#/membership/`に移動してチームIDを取得)と**Bundle Identifier**を組み合わせて構築しました。上の例では、"JHGFJHHYX" はチームID、"com.facebook.ios" はバンドルID です。
- `paths`:関連付けに含めるパスまたは関連付けから除外するパスを指定する文字列の配列。パスを無効にするには、パスの前に`NOT` を使用できます。この例では、アプリを開く代わりに、このパス上のすべてのリンクがWeb に移動します。ワイルドカードとして`*` を使用すると、ディレクトリ内のすべてのパスを有効にし、`?` を使用して1 つの文字(次のようなもの) に一致させることができます /archives/201?/ to match all numbers from 2010–2019).

{% alert note %}
これらの文字列は大文字と小文字が区別され、クエリ文字列とフラグメント識別子は無視されます。
{% endalert %}

### ステップ3:ドメインでのAASA ファイルのホスト

AASA ファイルの準備ができたら、ドメインで`https://<<yourdomain>>/apple-app-site-association` または`https://<<yourdomain>>/.well-known/apple-app-site-association` のいずれかでAASA ファイルをホストできます。

`apple-app-site-association` ファイルをHTTPS Web サーバーにアップロードします。このファイルは、サーバのルートまたは`.well-known` サブディレクトリに配置できます。ファイル名に`.json` を追加しないでください。

{% alert important %}
iOS は、セキュアな接続(HTTPS)を介してのみAASA ファイルをフェッチしようとします。
{% endalert %}

AASA ファイルをホストしている間は、ファイルが次のガイドラインに従っていることを確認します。

- HTTPS 経由で提供されます。
- `application/json` MIME タイプを使用します。
- 128KB を超えないこと(iOS 9.3.1 以降の要件)

### ステップ 4: ユニバーサルリンクを処理するためのアプリの準備

ユーザーがiOS デバイスのユニバーサルリンクをタップすると、デバイスはアプリを起動し、[NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity) オブジェクトを送信します。その後、アプリはNSUserActivity オブジェクトを照会して、起動方法を判断できます。

アプリでユニバーサルリンクをサポートするには、次の手順を実行します。

1. アプリがサポートするドメインを指定する資格を追加します。
2. NSUserActivity オブジェクトを受信したときに適切に応答するように、アプリケーションの代理人を更新します。

Xcode で、**Associated Domains** セクションを**Capabilities** タブで開き、`applinks:` の接頭辞を付けたアプリケーションがサポートする各ドメインのエントリを追加します。たとえば、`applinks:www.mywebsite.com` です。

{% alert note %}
Apple では、このリストを20 ～30 のドメインに制限することをお勧めします。
{% endalert %}

### ステップ 5: ユニバーサルリンクのテスト

ユニバーサルリンクをメールに追加し、テストデバイスに送信します。ユニバーサルリンクを「Safari URL」フィールドに直接貼り付けると、アプリは自動的に開きません。これを行う場合は、ウェブサイトを手動でプルダウンする必要があります。そのため、上部にプロンプトが表示され、それぞれのアプリを開くように求められます。

{% endtab %}

<!--Android instructions-->
{% tab Android %}

これらの手順は、Android 開発者のドキュメントから適用されます。詳細については、[Androidアプリリンクの追加](https://developer.android.com/training/app-links#add-app-links)および[アプリコンテンツへのディープリンクの作成](https://developer.android.com/training/app-links/deep-linking)を参照してください。

{% alert note %}
Android App Link では、他のWeb URL とは別にドメインからのリンクを処理するために、カスタムの`IBrazeDeeplinkHandler` ロジックが必要です。代わりに深いリンクを使用し、メール以外のチャネルでは一貫したリンクを維持する方が簡単かもしれません。
{% endalert %}

### ステップ1:深いリンクを作成する

まず、Androidアプリのディープリンクを作成する必要があります。これを行うには、`AndroidManifest.xml` ファイルに[intent filters](https://developer.android.com/guide/components/intents-filters) を追加します。インテントフィルタには、`VIEW` アクションと`BROWSABLE` カテゴリを、データ要素のWeb サイトのURL とともに含める必要があります。

### ステップ2:アプリをウェブサイトに関連付ける

アプリをウェブサイトに関連付ける必要があります。これを行うには、デジタルアセットリンクファイルを作成します。このファイルはJSON 形式で、ウェブサイトへのリンクを開くことができるAndroid アプリの詳細が含まれています。Web サイトの`.well-known` ディレクトリに配置する必要があります。

### ステップ3:アプリのマニフェストファイルを更新する

`AndroidManifest.xml` ファイルで、アプリケーション要素内にメタデータ要素を追加します。meta-data 要素には、"asset\_statements&quot の`android:name` 属性と、ウェブサイトのURL を含む文字列配列を持つリソースファイルを指す`android:resource` 属性が必要です。

### ステップ 4: ディープリンクを扱うアプリを準備する

Android アプリでは、受信するディープリンクを処理する必要があります。これを行うには、アクティビティを開始したインテントを取得し、そこからデータを抽出します。

### ステップ 5: ディープリンクのテスト

最後に、ディープリンクをテストすることができます。メッセージアプリまたはメールでリンクを送信し、クリックします。すべてが正しく設定されている場合は、アプリが開きます。

{% endtab %}
{% endtabs %}

## ユニバーサルリンク、アプリリンク、クリックトラッキング

{% alert note %}
クリックトラッキングリンクは通常、電子メールのオンボーディングの一部として設定されます。これがカスタマーオンボーディング中に完了しなかった場合は、アカウントマネージャーに連絡してサポートを受けてください。
{% endalert %}

私たちのメール送信パートナーであるSendGridとSparkPostは、クリックトラッキングドメインを使用してすべてのリンクをラップし、Brazeメールのクリックトラッキング用のURLパラメータを含めます。

たとえば、`https://www.example.com` のようなリンクは、`https://links.email.example.com/uni/wf/click?upn=abcdef123456…` のようになります。

クリックトラッキング付きのメールリンクをユニバーサルリンクまたはアプリリンクとして機能させるには、追加の設定を行う必要があります。クリックトラッキングドメイン(`links.email.example.com`) を、アプリのオープンが許可されているドメインとして必ず追加してください。さらに、クリックトラッキングドメインは、AASA (iOS) またはデジタルアセットリンク(Android) ファイルを処理する必要があります。これにより、クリックトラッキングを使用した電子メールリンクがシームレスに機能するようになります。

すべてのクリックトラッキングリンクをユニバーサルリンクまたはアプリリンクにしたくない場合は、メール送信パートナーに基づいて、どのリンクをユニバーサルリンクにするかを指定できます。詳細については、次のセクションを参照してください。

### SendGrid

SendGridクリックトラッキングリンクをユニバーサルとして扱うには link:

1. URL パスの`/uni/` でリンクのみをユニバーサルリンクとして扱うように、AASA またはAndroidManifest パスプレフィックス値を設定します。
2. 属性`universal="true"` をリンクのアンカータグに追加します(`<a>`)。これにより、ラップされたリンクのURL パスが`/uni/` を含むように変更されます。

{% alert note %}
AMP メールの場合、この属性はdata-universal="true" にする必要があります。
{% endalert %}

例:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\.アプリがラップされたリンクを適切に処理するように設定されていることを確認します。SendGridの記事[Resolving SendGrid Click Tracking Links](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links)を参照し、お使いのオペレーティングシステムの手順に従います。この記事には、[iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) および[Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android) のサンプルコードが含まれています。

この設定では、URL パスに`/uni/` が含まれるリンクはユニバーサルリンクとして機能し、他のすべてのリンクはWeb リンクとして機能します。

### スパークポスト

SparkPostクリックトラッキングリンクをユニバーサルリンクとして扱うには、メールのドラッグアンドドロップエディタのAttributes セクションに次の属性を追加するか、リンクHTML を手動で編集してリンクのアンカータグに次の属性を含めます:`data-msys-sublink="custom_path"`。

このカスタムパスを使用すると、その値を持つURL をユニバーサルリンクとして選択的に処理できます。

次に例を示します。

```html
<a href=”https://www.example.com” data-msys-sublink="open_in_app">
```

次に、カスタムパスを適切に処理するようにアプリが設定されていることを確認します。SparkPostの記事[Using SparkPost click tracking on deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links)を参照してください。この記事には、[iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) および[Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost) のサンプルコードが含まれています。

### クリックトラッキングによるユニバーサルリンクのトラブルシューティング

メールで想定どおりにユニバーサルリンクが動作しない場合(メールアプリからウェブブラウザに受信者をナビゲートしてからアプリにリダイレクトするなど)は、これらのヒントを参照してユニバーサルリンクの設定をトラブルシューティングしてください。

#### リンクファイルの場所の確認

AASA ファイル(iOS) またはデジタルアセットリンクファイル(Android) が正しい場所にあることを確認します。

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

これらのファイルが常にパブリックにアクセスできるようにすることが重要です。それらにアクセスできない場合は、メールのユニバーサルリンクを設定する手順を見逃している可能性があります。

#### ドメイン定義の検証

アプリを開くことが許可されているドメインの定義が正しいことを確認してください。

- **iOS: **アプリのXcode に設定されている関連ドメインを確認します([step 1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c))。クリックトラッキングドメインがリストに含まれていることを確認します。
- **Android :**アプリ情報ページを開きます(アプリアイコンを長押ししてⓘをクリックします)。アプリ情報メニュー内で、**デフォルトで開く**を見つけ、それをタップします。これにより、アプリを開くことが許可されているすべての確認済みリンクが表示されます。クリックトラッキングドメインがリストに含まれていることを確認します。
