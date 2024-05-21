---
nav_title: 準備ガイド
article_title: アプリ内メッセージ準備ガイド
page_order: 0.5

page_type: reference
description: "この記事では、アプリ内メッセージを作成する前に考慮すべきいくつかの質問とベストプラクティスについて説明します。"
channel: in-app messages

---

# アプリ内メッセージ準備ガイド

> アプリ内メッセージを作成する前に、次のトピックをいくつか検討して、メッセージをすばやく簡単に作成できるようにしてください。

## 一般的な注意事項

- キャンペーンを作成する場合、このメッセージのバリエーションをいくつ表示しますか?バリアントテストのアイデアについては、[さまざまなチャネル向けのヒントをご覧ください]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels)。
- キャンバスを作成する場合、このメッセージはそのステップで他のメッセージチャネルとペアリングされますか？
- [メッセージをいつ期限切れにしたいですか]({{site.baseurl}}/canvas_in-app_messages/)?

## ターゲティングに関する考慮事項

- アプリ内メッセージは、定期的にアプリにアクセスするユーザーに最適です。このオーディエンスを含めていますか？
- ユーザーにメッセージをどこで見てもらいたいですか?お使いの Web アプリで?モバイルアプリで？
- どのイベントがこのメッセージをトリガーすべきか?
- アプリの古いバージョンを使用しているユーザーはいますか?その場合、メッセージの一部の要素が表示されない可能性があります。
- このメッセージは、どのタイプのデバイス向けに作成されていますか?「プレビュー」ボックスまたは「**テスト**」**タブを使用してメッセージをプレビューできることを忘れないでください**。詳細については、「[テスト]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/)」を参照してください。

## コンテンツに関する考慮事項

- このメッセージではどの言語を使用しますか？
- ヘッダーと本文のコピーは何ですか?それらは人目を引き、ユーザーにとって関連性があるか?
- アプリ内メッセージは一定時間だけ表示されます。コピーは簡潔で覚えやすいですか？
- [Liquidを使用してカスタムコピーを追加しますか]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)？
- フルスクリーンのアプリ内メッセージの場合、[画像やその他のメディアはセーフゾーン内にありますか]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)？
- アンケートのアプリ内メッセージに、属性または送信を記録しますか？確認ページを設定しましたか？

## 変換に関する考慮事項

- このメッセージの目的は何ですか?それをメッセージでどのように表現できますか?
- ボタンにはユーザーにとってわかりやすいオプションがありますか?[主に行動を促すフレーズは何ですか]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)?
- [他のアプリ内コンテンツへのディープリンクは行っていますか][1]？このアプリ内メッセージを使用して、[許可リクエストまたはプッシュプライミングリクエストの送信と承認を行っていますか][21]？
- メッセージ終了オプションはありますか?そうでない場合は、いつでもこのスニペットをコピーして貼り付けてクイックボタンを作成できます。
    ```html
    <a href="appboy://close">X</a>
    ```


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content
[21]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
