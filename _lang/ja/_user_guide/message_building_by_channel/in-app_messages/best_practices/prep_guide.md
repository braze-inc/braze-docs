---
nav_title: 準備ガイド
article_title: アプリ内メッセージ準備ガイド
page_order: 0.5

page_type: reference
description: "この記事では、アプリ内メッセージを作成する前に考慮すべきいくつかの質問とベストプラクティスについて説明します。"
channel: in-app messages

---

# アプリ内メッセージ準備ガイド

> アプリ内メッセージを作成する前に、以下のトピックを考慮する必要があります。そうすることでメッセージの作成が迅速かつ容易になります。

## 一般的な考慮事項

- キャンペーンを作成する場合、このメッセージのバリアントをいくつ表示しますか？バリアントテストのアイデアについては、[さまざまなチャネルのヒント]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/create_multivariate_campaign/#tips-different-channels)をチェックしてください。
- キャンバスを構築している場合、そのメッセージはそのステップで他のメッセージングチャネルとペアになりますか？
- [メッセージをいつ期限切れにしますか]({{site.baseurl}}/canvas_in-app_messages/)?

## ターゲット設定の考慮事項

- アプリ内メッセージは、定期的にアプリを訪れるユーザーに最適です。このオーディエンスを含めますか?
- あなたのメッセージをユーザーにどこで見せたいですか？貴社の Webアプリで表示しますか?貴社のモバイルアプリで表示しますか?
- どのイベントがこのメッセージをトリガーする必要がありますか？
- ユーザーの中に、古いバージョンのアプリを使用している人はいますか?もしそうなら、彼らはあなたのメッセージのいくつかの要素を見ることができないかもしれません。
- このメッセージはどのタイプのデバイス用に作成しますか?覚えておいてください、メッセージは**プレビュー**ボックスまたは**テスト**タブを使用してプレビューできます。詳細については[テスト]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/)を参照してください。

## コンテンツの考慮事項

- このメッセージで使用する言語は何ですか？
- ヘッダーと本文コピーは何ですか?それらはあなたのユーザーにとって目を引くものであり、関連性がありますか？
- アプリ内メッセージは、設定された時間だけ表示されます。あなたのコピーは簡潔で記憶に残るものですか？
- カスタムコピーを追加するために[Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/using_liquid/)を使用しますか？
- 全画面アプリ内メッセージの場合、画像やその他のメディアは[安全ゾーン]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone)内にありますか？
- アプリ内メッセージの調査では、属性または送信を記録しますか?確認ページを設定しましたか？

## コンバージョンの考慮事項

- このメッセージの目的は何ですか？それをメッセージでどのように表現できますか？
- あなたのボタンは、ユーザーにとって意味のあるオプションを提供していますか？あなたの[主なコール・トゥ・アクション]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/#buttons)は何ですか？
- [ディープリンクを使用して他のアプリ内コンテンツにリンクしていますか]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/deep_linking_to_in-app_content/#deep-linking-to-in-app-content)？このアプリ内メッセージを使用して、[許可またはプッシュプライミングリクエスト]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/)を送信および受信していますか？
- メッセージ終了オプションはありますか？もしそうでない場合は、このスニペットをコピーして貼り付けることで、すぐにボタンを作成できます。
    ```html
    <a href="appboy://close">X</a>
    ```


