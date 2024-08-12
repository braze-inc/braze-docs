---
nav_title: テスト中...
article_title: コンテンツカードのテスト
page_order: 3
description: "この参考記事では、コンテンツカードをプレビューしてテストする方法と、いくつかのベストプラクティスについて説明します。"
channel:
  - content cards
  
---

# コンテンツカードのテスト

> キャンペーンを送信する前に、必ずコンテンツカードをテストすることが非常に重要です。プレビューおよびテスト機能では、コンテンツカードを2つの方法で確認できます。メッセージをプレビューして作成時に視覚化したり、テストメッセージを自分または特定のユーザーのデバイスに送信したりできます。両方を活用することをおすすめします。

## プレビュー

作成中にカードをプレビューできます。これにより、最終的なメッセージがユーザーの視点からどのように見えるかを視覚化できます。

コンポーザーの「**プレビュー**」タブでは、メッセージの表示がユーザーのデバイスでの実際のレンダリングと同じではない場合があります。メディア、コピー、パーソナライゼーション、カスタム属性が正しく生成されることを確認するために、常にテストメッセージをデバイスに送信することをお勧めします。

## テスト

[コンテンツテストグループまたは個々のユーザーにテストを送信するには]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups)、送信前にテストユーザー用に登録された有効なプッシュトークンを使用して、テストデバイスでプッシュを有効にする必要があります。iOS ユーザーの場合、テストコンテンツカードを表示するには、Braze から送信されたプッシュ通知をタップする必要があります。この動作はテストコンテンツカードにのみ適用されます。

### ユーザーとしてメッセージをプレビュー

また、**テストタブからメッセージをユーザーと同じようにプレビューすることもできます**。特定のユーザーまたはランダムユーザーを選択するか、カスタムユーザーを作成できます。

![Custom\_User\_Preview][3]

### テストチェックリスト

- 画像やメディアは期待どおりに表示され、動作しますか？
- Liquidは期待どおりに機能しますか？[Liquidが情報を返さない場合のデフォルトの属性値を考慮しましたか]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values)？
- コピーは明確、簡潔、正確ですか？
- リンクはユーザーを本来あるべき場所に誘導していますか？

## デバッグ

コンテンツカードが送信されたら、[開発者コンソールのイベントユーザーログから問題を分析またはデバッグできます]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/)。 

一般的なユースケースは、ユーザーが特定のコンテンツカードを見ることができない理由をデバッグすることです。そのためには、**セッション開始時にインプレッションが発生する前にSDKに配信されたコンテンツカードをイベントユーザーログで確認し**、特定のキャンペーンまでさかのぼることができます。

1. **[設定] > [**イベントユーザーログ**]** に移動します。
{% alert note %}
[古いナビゲーションを使用している場合は]({{site.baseurl}}/navigation)、****開発者コンソールにイベントユーザーログが表示されます****。
{% endalert %}

{:start="2"}
2\.テストユーザー用の SDK リクエストを見つけて展開します。
3\.[**未加工データ**] をクリックします。
4\.`id`セッションに合うものを見つけてください。以下は抜粋の例です。

    ```json
    [
      {
        "session_id": "D1B051E6-469B-47E2-B830-5A728D1D4AC5",
        "data": {
          "ids": [
            "NjE4NTAwNWE5ZDliZWU3OTM4N2NjZTQzXyRfY2M9YzNiMjU3NDAtZjExMy1jMDQ3LTRiMWQtZDI5NmYyODBhZjRmJm12PTYxODUwMDViOWQ5YmVlNzkzODdjY2U0NSZwaT1jbXA="
          ]
        },
        "name": "cci",
        "time": 1636106490.155
      }
    ]
    ```

5. Base64 [Decode や Encode などのデコードツールを使用して Base64 `id` 形式からデコードし](https://www.base64decode.org/)、関連するものを見つけます。`campaign_id`この例では、この結果は次のようになります。

    ```
    6185005a9d9bee79387cce43_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    `6185005a9d9bee79387cce43`はどこにありますか`campaign_id`.<br><br>

6. 「**キャンペーン**」ページに移動して、を検索してください`campaign_id`。

![キャンペーンページでキャンペーン ID を検索] [1]

そこから、メッセージ設定とコンテンツを確認して掘り下げて、ユーザーに特定のコンテンツカードが表示されない理由を特定できます。

[1]: {% image_buster /assets/img_archive/cc_debug.png %}
[3]: {% image_buster /assets/img/cc-user-preview.png %}
