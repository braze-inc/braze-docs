## 前提条件

コンテンツカードを使用する前に、[Braze Swift SDKを]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift)アプリに統合する必要がある。その後、tvOSアプリの設定ステップを完了させる必要がある。

{% alert important %}
コンテンツカードは Swift SDK を使用するヘッドレス UI でサポートされているため、独自のカスタムUI を実装する必要があります。これには tvOS のデフォルト UI やビューは含まれません。
{% endalert %}

## tvOSアプリを設定する

### ステップ1:新しいiOSアプリを作成する

Braze で、[**設定**] > [**アプリの設定**] を選択し、[**アプリの追加**] を選択します。tvOS アプリの名前を入力し、_tvOS ではなく_、**iOS** を選択し、**アプリの追加**を選択します。

![ALT_TEXT.]({% image_buster /assets/img/tvos.png %}){: style="width:70%"}

{% alert warning %}
**tvOS**チェックボックスを選択した場合、コンテンツカードをtvOS用にカスタマイズすることはできない。
{% endalert %}

### ステップ2:アプリのAPIキーを取得する

アプリの設定で、新しいtvOSアプリを選択し、アプリのAPIキーをメモする。このキーを使って Xcode でアプリを設定します。

![ALT_TEXT]({% image_buster /assets/img/tvos1.png %}){: style="width:70%"}

### ステップ3: BrazeKitを統合する

アプリの API キーを使用して、Xcode で [Braze Swift SDK](https://github.com/braze-inc/braze-swift-sdk) を tvOS プロジェクトに統合します。Braze Swift SDK から BrazeKit を統合するだけでよいです。

### ステップ 4:カスタムUIを作成する

BrazeはtvOS上のコンテンツカードのデフォルトUIを提供していないため、自分でカスタマイズする必要がある。完全なチュートリアルについては、ステップ・バイ・ステップのチュートリアルを参照のこと：[コンテンツカードをtvOS用にカスタマイズする](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/content-cards-customization/)。サンプルプロジェクトについては、[Braze Swift SDKのサンプル](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples#contentcards-custom-ui)を参照してください。
