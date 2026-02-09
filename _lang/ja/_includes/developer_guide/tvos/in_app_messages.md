{% alert important %}
アプリ内メッセージングはSwift SDKを使ったヘッドレスUIでサポートされており、tvOS用のデフォルトUIやビューは含まれていないため、独自のカスタムUIを実装する必要があることを覚えておこう。
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/swift.md %}

## アプリ内メッセージを有効にする

### ステップ 1: 新しいiOSアプリを作成する

Braze で、[**設定**] > [**アプリの設定**] を選択し、[**アプリの追加**] を選択します。tvOS アプリの名前を入力し、_tvOS ではなく_、**iOS** を選択し、**アプリの追加**を選択します。

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
**tvOS**チェックボックスを選択すると、tvOS用のアプリ内メッセージをカスタマイズできなくなる。
{% endalert %}

### ステップ2:アプリのAPIキーを取得する

アプリの設定で、新しいtvOSアプリを選択し、アプリのAPIキーをメモする。このキーを使って Xcode でアプリを設定します。

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### ステップ 3:BrazeKitを統合する

アプリの API キーを使用して、Xcode で [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) を tvOS プロジェクトに統合します。Braze Swift SDK から BrazeKit を統合するだけでよいです。

### ステップ 4:カスタムUIを作成する

BrazeはtvOS上でアプリ内メッセージのデフォルトUIを提供していないため、自分でカスタマイズする必要がある。完全なチュートリアルについては、ステップ・バイ・ステップのチュートリアルを参照のこと：[tvOSのアプリ内メッセージをカスタマイズする](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization)。サンプルプロジェクトについては、[Braze Swift SDKのサンプル](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#inappmessages-custom-ui)を参照してください。
