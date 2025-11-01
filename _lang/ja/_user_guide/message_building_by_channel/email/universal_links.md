---
nav_title: ユニバーサルリンクとアプリリンク
article_title: ユニバーサルリンクとアプリリンク
page_order: 6.4
page_type: reference
description: "このヘルプ記事では、AppleユニバーサルリンクとAndroidアプリリンクの設定方法について説明します。"
channel: email
---

# ユニバーサルリンクとアプリリンク

Apple ユニバーサルリンクと Android アプリリンクは、Web コンテンツとモバイルアプリ間のシームレスな移行を実現するために考案されたメカニズムです。ユニバーサル・リンクはiOSに特有のものだが、Androidアプリ・リンクはAndroidアプリでも同じ役割を果たす。

## ユニバーサルリンクとアプリリンクの仕組み

ユニバーサルリンク (iOS) とアプリリンク (Android) は、Web ページとアプリ内のコンテンツの両方を指す標準的なウェブリンク (`http://mydomain.com`) です。

ユニバーサルリンクまたはアプリリンクが開かれると、オペレーティングシステムはインストールされているアプリがそのドメインに登録されているかどうかを確認します。アプリが見つかった場合、Webページを読み込むことなくすぐに起動されます。アプリが見つからない場合、Web URLはユーザーのデフォルトのWebブラウザで読み込まれます。これもそれぞれApp StoreまたはGoogle Play Storeにリダイレクトするように設定できます。

簡単に言えば、ユニバーサルリンクはWebサイトが特定のアプリ画面とそのWebページを関連付けることを可能にします。そのため、ユーザーがアプリ画面に対応するWebページへのリンクをクリックすると、アプリが直接開くことができます（アプリが現在インストールされている場合）。

この表は、ユニバーサルリンクと従来のディープリンクの主な違いを概説しています:

|                        | ユニバーサルリンクとアプリリンク                                  | ディープリンク                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| プラットフォーム互換性 | iOS（バージョン9以降）およびAndroid（バージョン6.0以降）  | さまざまなモバイルOSで使用されます    |
| 目的                | iOS および Android デバイスの Web コンテンツとアプリコンテンツをシームレスにリンクする | 特定のアプリコンテンツへのリンク |
| 機能               | コンテキストに基づいてWebページまたはアプリのコンテンツに誘導します           | 特定のアプリ画面を開きます   |
| アプリインストール       | アプリがインストールされている場合はアプリを開き、それ以外の場合はWebコンテンツを開きます | アプリのインストールが必要です |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## ユースケース

ユニバーサルリンクとアプリリンクは、メールキャンペーンで最も一般的に使用されます。メールはデスクトップとモバイルの両方のデバイスから開いてクリックすることができます。

いくつかのチャンネルはこれらのリンクではうまく機能しません。たとえば、プッシュ通知、アプリ内メッセージ、およびコンテンツカードでは、スキームベースのディープリンク (`mydomain://`) を使用する必要があります。

{% alert note %}
Android アプリリンクでは、他の Web URL とは別にドメインからのリンクを処理するために、カスタム `IBrazeDeeplinkHandler` ロジックが必要です。他のチャネルではメールではなく、ディープリンクを使用し、リンクの方法を統一する方が簡単かもしれません。
{% endalert %}

## 前提条件

ユニバーサルリンクとアプリリンクを使用するには:

- あなたのWeb サイトはHTTPS経由でアクセス可能でなければなりません
- あなたのアプリはApp Store（iOS）またはGoogle Playストア（Android）で利用可能でなければなりません

## ユニバーサルリンクとアプリリンクの設定

アプリがユニバーサルリンクまたはアプリリンクをサポートするためには、iOSとAndroidの両方でリンクドメインに特別な権限ファイルをホストする必要があります。このファイルには、どのアプリがそのドメインからのリンクを開封できるか、そしてiOSの場合、これらのアプリが開封できるパスが定義されています。

- **iOS:**Apple App Site Association(AASA)ファイル
- **Android :**デジタル資産リンクファイル

この権限ファイルに加えて、アプリ内で設定されているアプリが開封できるリンクドメインのハードコーディングされた定義があります。

- **iOS:**Xcodeで「関連ドメイン」として設定
- **Android :**アプリの`AndroidManifest.xml`ファイルで定義されています

この2つの部分からなるドメイン-アプリの関連付けは、ユニバーサルリンクまたはアプリリンクが機能するために必要であり、特定のドメインからのリンクを任意のアプリがハイジャックしたり、特定のアプリを任意のドメインが開いたりするのを防ぎます。

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

これらの手順は、Appleの開発者ドキュメントから適応されています。詳細については、[アプリやウェブサイトがあなたのコンテンツにリンクすることを許可する](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc)を参照してください。

### ステップ 1: アプリ資格の設定

{% alert note %}
[Xcode 13 以降](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/)では、Xcode は資格プロビジョニングを自動的に処理できます。おそらく[ステップ 1c](#step-1c)にスキップして、問題が発生した場合はこれらの指示に戻ることができます。
{% endalert %}

#### ステップ 1a: アプリ {#step-1a} の登録

1. developer.apple.comを実行してログインしてください。
2. **Certificates, Identifiers& Profiles** をクリックする。
3. **識別子**をクリックします。
4. アプリ識別子がまだ登録されていない場合は、+ をクリックして作成します。
   a. **名前**を入力してください。これはあなたが望むものなら何でもかまいません。
   b. **バンドルID**を入力します。適切なビルドターゲットのXコードプロジェクトの**General**タブからバンドルIDを見つけることができます。

#### ステップ 1b: アプリ識別子で関連ドメインをオンにする

1. 既存または新しく作成したApp Identifier で、**App Services** セクションを見つけます。
2. [**関連ドメイン**] を選択します。
3. [**保存**] をクリックします。

\![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### ステップ1c: Xcodeプロジェクトで関連ドメインをオンにする {#step-1c}

続行する前に、Xcode プロジェクトで、アプリ識別子を登録した場所と同じチームが選択されていることを確認してください。 

1. Xcode で、プロジェクトファイルの**Capabilities**タブに移動します。
2. **関連ドメイン**をオンにします。

##### トラブルシューティングのヒント

「識別子 'your-app-id' を持つアプリIDは利用できません」というエラーが表示された場合。別の文字列を入力してください", 次のことを行ってください:

1. 選択したチームが正しいことを確認してください。
2. Xcode プロジェクトのバンドル ID ([ステップ1a](#step-1a)) が、アプリ識別子の登録に使用されたものと一致していることを確認します。

#### ステップ1d: ドメイン資格の追加

[ドメイン] セクションで、適切なドメインタグを追加します。`applinks:` をプレフィックスとして使用する必要があります。この場合、`applinks:yourdomain.com`を追加したことがわかります。

\![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### ステップ1e: ビルド時に権利ファイルが含まれていることを確認してください

プロジェクトブラウザで、新しい資格ファイルが [**ターゲットメンバーシップ**] で選択されていることを確認します。

Xcodeはこれを自動的に処理するはずです。

### ステップ2:Web サイトをホストするようにAASAファイルを構成する

iOSでネイティブアプリとWebサイトのドメインを関連付けるには、WebサイトにApple App Site Association (AASA)ファイルをホストする必要があります。このファイルは、iOS に対するドメイン所有権を安全に検証する手段となります。iOS 9より前では、開発者は検証なしで任意の URI スキームを登録してアプリを開くことができました。しかし、AASAを使用すると、このプロセスははるかに安全で信頼性が高くなります。

AASAファイルには、アプリのリストと、ユニバーサルリンクとして含めるべきまたは除外するべきドメイン上のURLパスを含むJSONオブジェクトが含まれています。こちらはサンプルのAASAファイルです：

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

- `appID`: お使いのアプリの**チームID**（チームIDを取得するには`https://developer.apple.com/account/#/membership/`に移動）と**バンドル識別子**を組み合わせて構築されます。上記の例では、「JHGFJHHYX」はチームIDであり、「com.facebook.ios」はバンドルIDです。
- `paths`: 関連付けから含まれるまたは除外されるパスを指定する文字列の配列。パスの前に`NOT`を使用してパスを無効にすることができます。この例では、このパス上のすべてのリンクはアプリを開くのではなく、Webに移動します。ディレクトリ内のすべてのパスを有効にするために`*`をワイルドカードとして使用でき、単一の文字に一致させるために`?`を使用できます（例えば、/archives/201?/は2010年から2019年までのすべての数字に一致します）。

{% alert note %}
これらの文字列は大文字と小文字を区別し、クエリ文字列とフラグメント識別子は無視されます。
{% endalert %}

### ステップ 3:ドメインにAASAファイルをホストする

AASA ファイルの準備ができたら、ドメインで`https://<<yourdomain>>/apple-app-site-association` または`https://<<yourdomain>>/.well-known/apple-app-site-association` のいずれかでAASA ファイルをホストできます。

`apple-app-site-association`ファイルをHTTPS Webサーバーにアップロードします。ファイルをサーバーのルートまたは`.well-known`サブディレクトリに配置できます。ファイル名に`.json`を追加しないでください。

{% alert important %}
iOSは安全な接続（HTTPS）を介してのみAASAファイルの取得を試みます。
{% endalert %}

AASAファイルをホスティングする際は、ファイルがこれらのガイドラインに従っていることを確認してください:

- HTTPS経由で提供されます。
- `application/json` MIME タイプを使用します。
- 128 KB を超えない（iOS 9.3.1 以降の要件）

### ステップ 4:ユニバーサルリンクを処理するためにアプリを準備する

iOSデバイスでユーザーがユニバーサルリンクをタップすると、デバイスはアプリを起動し、[NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity)オブジェクトを送信します。その後、アプリはNSUserActivity オブジェクトを照会して、起動方法を判断できます。

アプリでユニバーサルリンクを使用するには、次のステップを実行します。

1. お使いのアプリがサポートするドメインを指定する権利を追加します。
2. アプリデリゲートを更新して、NSUserActivityオブジェクトを受け取ったときに適切に応答するようにします。

Xコード では、**Capabilities** タブの**Associated Domains** セクションを開封し、`applinks:` の接頭辞を付けたアプリがサポートするドメインごとにエントリを追加します。たとえば `applinks:www.mywebsite.com` です。

{% alert note %}
Apple は、このリストを20～30のドメインに制限することを推奨しています。
{% endalert %}

### ステップ 5: ユニバーサルリンクをテストする

ユニバーサルリンクをメールに追加して、テストデバイスに送信します。SafariのURLフィールドにユニバーサルリンクを直接貼り付けても、アプリが自動的に開封されることはありません。この操作を行うと、手動でWeb サイトを引き下げて、対応するアプリを開封するように求めるプロンプトが上部に表示されます。

{% endtab %}

<!--Android instructions-->
{% tab Android %}

これらの手順は、Android開発者ドキュメントから適応されています。詳細については、[Androidアプリリンクの追加](https://developer.android.com/training/app-links#add-app-links)および[アプリコンテンツへのディープリンクの作成](https://developer.android.com/training/app-links/deep-linking)を参照してください。

{% alert note %}
Android アプリリンクでは、他の Web URL とは別にドメインからのリンクを処理するために、カスタム `IBrazeDeeplinkHandler` ロジックが必要です。他のチャネルではメールではなく、ディープリンクを使用し、リンクの方法を統一する方が簡単かもしれません。
{% endalert %}

### ステップ 1:ディープリンクを作成

まず、Androidアプリのディープリンクを作成する必要があります。これは、[インテントフィルター](https://developer.android.com/guide/components/intents-filters)を`AndroidManifest.xml`ファイルに追加することで実行できます。インテントフィルターには`VIEW`アクションと`BROWSABLE`カテゴリ、およびデータ要素にWebサイトのURLを含める必要があります。

### ステップ2:アプリをWebサイトに関連付ける

アプリをWebサイトに関連付ける必要があります。そのために、デジタルアセットリンクファイルを作成します。このファイルは JSON 形式である必要があり、Web サイトへのリンクを開封できる Android アプリに関する詳細が含まれています。Web サイトの`.well-known` ディレクトリーに配置する必要があります。

### ステップ 3:アプリのマニフェストファイルを更新してください

`AndroidManifest.xml` ファイルで、アプリライケーション要素内にメタデータ要素を追加します。meta-data要素には、"asset_statements" の`android:name` 属性と、WebサイトのURLを含む文字列配列のリソース・ファイルをポイントする`android:resource` 属性を指定する。

### ステップ 4: アプリをディープリンクに対応させる準備をする

Androidアプリでは、受信したディープリンクを処理する必要があります。これを行うには、アクティビティを開始したインテントを取得し、そこからデータを抽出します。

### ステップ 5: ディープリンクのテスト

最後に、ディープリンクをテストできます。メッセージングアプリやメールを通じて自分にリンクを送信し、それをクリックします。すべてが正しく設定されている場合は、アプリが開かれます。

{% endtab %}
{% endtabs %}

## ユニバーサルリンク、アプリリンク、クリックトラッキング

{% alert note %}
クリックトラッキングリンクは通常、メールのオンボーディングの一部として設定されます。これがカスタマーオンボーディング中に完了しなかった場合は、アカウントマネージャーに連絡してサポートを受けてください。
{% endalert %}

私たちのメール送信パートナーであるSendGridとSparkPostは、クリックトラッキングドメインを使用してすべてのリンクをラップし、BrazeのメールでクリックトラッキングのためのURLパラメータを含めます。

例えば、`https://www.example.com`のようなリンクは`https://links.email.example.com/uni/wf/click?upn=abcdef123456…`のようになります。

メールリンクをクリックトラッキングでユニバーサルリンクまたはアプリリンクとして機能させるには、追加の設定が必要です。クリックトラッキングドメイン (`links.email.example.com`) を、アプリを開くことが許可されているドメインとして必ず追加してください。また、クリックトラッキングドメインは、AASA (iOS) またはデジタルアセットリンク (Android) ファイルを提供する必要があります。これにより、クリックトラッキング付きのメールリンクがシームレスに機能するようになります。

すべてのクリックトラッキングリンクをユニバーサルリンクまたはアプリリンクにしたくない場合は、メール送信パートナーに基づいて、どのリンクをユニバーサルリンクにするかを指定できます。詳細については、次のセクションを参照してください。

### SendGrid

SendGridのクリックトラッキングリンクをユニバーサルリンクとして扱うには:

1. AASA または AndroidManifest の pathPrefix 値を設定して、URL パスに `/uni/` が含まれているリンクのみをユニバーサルリンクとして扱うようにします。
2. リンクのアンカータグ（`<a>`）に属性`universal="true"`を追加します。これにより、ラップされたリンクのURLパスが`/uni/`を含むように変更されます。

{% alert note %}
AMPメールの場合、この属性はdata-universal="true"である必要があります。
{% endalert %}

以下に例を示します。

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\.アプリがラップされたリンクを適切に処理するように設定されていることを確認してください。[SendGrid クリックトラッキングリンクの解決](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links)に関する SendGrid の記事を参照し、ご使用のオペレーティングシステムのステップに従ってください。この記事には、[iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios)および[Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android)のサンプルコードが含まれています。

この構成では、URL パスに `/uni/` が含まれるリンクはユニバーサルリンクとして機能し、それ以外のリンクは Web リンクとして機能します。

### SparkPost

SparkPostのクリックトラッキングリンクをユニバーサルリンクとして扱うには、メールのドラッグアンドドロップエディタの属性セクションに次の属性を追加するか、リンクのHTMLを手動で編集してリンクのアンカータグに次の属性を含めます: `data-msys-sublink="custom_path"`。

このカスタムパスにより、その値を持つURLをユニバーサルリンクとして選択的に処理できます。

以下に例を示します。

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

次に、アプリがカスタムパスを適切に処理するように設定されていることを確認してください。[SparkPost クリックトラッキングの使用](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links)に関する SparkPost の記事を参照してください。この記事には、[iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost)および[Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost)のサンプルコードが含まれています。

### リンクごとのクリック追跡をオフにする

HTMLエディターではメールメッセージに、ドラッグ＆ドロップエディターではHTMLブロックにHTMLコードを追加することで、特定のリンクのクリック追跡をオフにすることができる。

#### SendGrid

メールサービスプロバイダーが SendGrid の場合は、次のような HTML コード `clicktracking=off` を使用します。

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost 

メールサービスプロバイダーが SparkPost の場合は、次のような HTML コード `data-msys-clicktrack="0"` を使用します。

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

メールサービスプロバイダーが Amazon SES の場合は、次のような HTML コード `ses:no-track` を使用します。

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### ドラッグアンドドロップエディタ

ドラッグ＆ドロップでメールエディターを使用する場合、リンクがテキスト、ボタン、画像写真に添付されている場合は、カスタム属性としてHTMLコードを入力する。

##### テキストリンクのカスタム属性

#### SendGrid

カスタム属性として以下を選択します。

- **名前:** `clicktracking`
- **値:** `off`

#### SparkPost

カスタム属性として以下を選択します。

- **名前:** `data-msys-clicktrack`
- **値:** `0`

\![テキストリンクのカスタム属性。]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### ボタンまたは画像のカスタム属性

#### SendGrid

カスタム属性として以下を選択します。

- **名前:** `clicktracking`
- **値:** `off`
- **タイプ:**リンク

#### SparkPost

カスタム属性として以下を選択します。

- **名前:** `data-msys-clicktrack`
- **値:** `0`
- **タイプ:**リンク

\![ボタンのカスタム属性。]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### クリックトラッキングによるユニバーサルリンクのトラブルシューティング

メールでユニバーサルリンクが期待通りに機能しない場合、例えば受信者がメールアプリからWebブラウザに移動し、最終的にアプリにリダイレクトされる場合は、ユニバーサルリンクの設定をトラブルシューティングするためのこれらのヒントを参照してください。

#### リンクファイルの場所を確認する

AASA ファイル(iOS) またはデジタルアセットリンクファイル (Android) が正しい場所にあることを確認してください。

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

これらのファイルが常に公開アクセス可能であることを確認することが重要です。アクセスできない場合は、メールのユニバーサルリンクの設定でステップを見逃した可能性があります。

#### ドメイン定義を確認する

アプリを開くことが許可されているドメインの定義が正しいことを確認してください。

- **iOS:**アプリ用に Xcode で設定された関連ドメインを確認します ([ステップ1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c))。クリックトラッキングドメインがそのリストに含まれていることを確認してください。
- **Android :**アプリ情報ページを開封します（アプリアイコンを長押しして、ⓘをクリックします）。アプリ情報メニュー内で、**デフォルトで開封**を見つけてタップします。これにより、アプリを開くことが許可されているすべての検証済みリンクが表示されます。クリックトラッキングドメインがそのリストに含まれていることを確認してください。

