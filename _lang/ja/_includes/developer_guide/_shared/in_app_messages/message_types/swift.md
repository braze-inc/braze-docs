{% tab swift %}
各アプリ内メッセージタイプは、コンテンツ、画像、アイコン、クリックアクション、分析、表示、配信に渡って高度にカスタマイズできます。これらは列挙型の`Braze.InAppMessage`で、すべてのアプリ内メッセージsの基本的な振る舞いと形質を定義します。アプリ内メッセージのプロパティーと使用法の完全な一覧については、[`InAppMessage` クラス](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage) を参照してください。

これらは、Braze で使用可能なアプリ内メッセージタイプと、end-ユーザー s の外観です。

{% subtabs %}
{% subtab Slideup %}

[`Slideup`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/slideup-swift.struct) アプリ内メッセージ s にはこの名前が付けられます。これは、slide up" または"slide down" が、スクリーンの上部または下部にあるためです。画面の一部分だけを覆い、効果的で邪魔にならないメッセージング機能を提供します。

![電話機の画面の上部と下部にスライド式で表示されたアプリ内メッセージ。]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width:35%;border:none;"}


{% endsubtab %}
{% subtab Modal %}

[`Modal`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modal-swift.struct) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。よりクリティカルなメッセージングに有用で、最大2つのアナリティクス対応ボタンを装備できる。

![電話機の画面の中央に表示されたモーダルアプリ内メッセージ。]({% image_buster /assets/img/modal-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Modal Image %}

[`Modal Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/modalimage-swift.struct) アプリ内メッセージは画面中央に表示され、半透明のパネルに囲まれます。これらのメッセージは、ヘッダーやメッセージテキストがないことを除けば、`Modal` タイプに似ている。よりクリティカルなメッセージングに有用で、最大2つのアナリティクス対応ボタンを装備できる。

![電話機の画面の中央に表示されたモーダル画面のアプリ内メッセージ。]({% image_buster /assets/img/modal-full-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Fullscreen %}

[`Full`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/full-swift.struct) アプリ内メッセージは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`Full` アプリ内メッセージの上半分には画像が含まれ、下半分にはテキストと最大2つの分析対応ボタンが表示されます。

![携帯電話の画面全体に表示されるフルスクリーンのアプリ内メッセージ。]({% image_buster /assets/img/full-screen-header-text.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Full Screen Image %}

[`Full Image`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/fullimage-swift.struct) アプリ内メッセージは、ヘッダーやメッセージテキストがないことを除けば、`Full` アプリ内メッセージと似ている。このメッセージタイプは、ユーザーコミュニケーションの内容とインパクトを最大化するのに有効です。`Full Image` アプリ内メッセージには画面全体に広がる画像が含まれ、オプションで最大2つの分析対応ボタンが表示されます。

![携帯電話の画面全体に表示されるフルスクリーン画像のアプリ内メッセージ。]({% image_buster /assets/img/full-screen-image.png %}){: style="max-width:35%;border:none;"}

{% endsubtab %}
{% subtab Custom HTML %}

[`HTML`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/html-swift.struct) アプリ内メッセージは、完全にカスタマイズされたユーザーコンテンツを作成するのに便利です。ユーザー定義の HTML アプリ内のフルメッセージコンテンツは、`WKWebView` に表示され、必要に応じて画像やフォントなどの他のリッチコンテンツを含めることができます。これにより、メッセージの外観と機能を完全に制御できます。<br><br>iOS アプリ内メッセージは、HTML 内から Braze Web SDK のメソッドを呼び出すための JavaScript `brazeBridge` インターフェイスをサポートしています。詳細については、[ベストプラクティス]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/)を参照してください。

次の例は、ページ分割された HTML の完全アプリ内メッセージを示しています。

![コンテンツのカルーセルとインタラクティブなボタンを備えたHTMLのアプリ内メッセージ。]({% image_buster /assets/img_archive/ios-html-full-iam.gif %})

現在、iOS と Android のプラットフォームでは、iFrame でのカスタム HTML アプリ内メッセージの表示はサポートしていません。

{% endsubtab %}
{% subtab Control %}

[`Control`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/control-swift.struct) アプリ内メッセージには UI コンポーネントは含まれず、主に分析用に使用されます。このタイプは、コントロールグループに送信されたアプリ内メッセージの受信を確認するために使用される。

インテリジェントセレクションとコントロールグループについては、[インテリジェントセレクション]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_selection/)を参照してください。

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
