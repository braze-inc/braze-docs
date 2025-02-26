---
nav_title: テスト
article_title: コンテンツカードのテスト
page_order: 3
description: "このリファレンス記事では、コンテンツカードをプレビューしてテストする方法、およびいくつかのベストプラクティスについて説明します。"
channel:
  - content cards
  
---

# コンテンツカードのテスト

> キャンペーンを送信する前に、必ずコンテンツカードをテストすることが非常に重要です。私たちのプレビューおよびテスト機能は、コンテンツカードを確認するための2つの方法を提供します。メッセージを作成しながら視覚化するのに役立つように、メッセージをプレビューしたり、自分自身や特定のユーザーのデバイスにテストメッセージを送信したりできます。両方を活用することをお勧めします。

## プレビュー

カードを作成しながらプレビューできます。これにより、ユーザーの視点から最終メッセージがどのように見えるかを視覚化するのに役立ちます。

作成者の**プレビュー**タブでは、メッセージの表示がユーザーのデバイスでの実際のレンダリングと同じでない場合があります。メディア、コピー、パーソナライゼーション、およびカスタム属性が正しく生成されることを確認するために、常にデバイスにテストメッセージを送信することをお勧めします。

## テスト

テストを[コンテンツテストグループ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups)または個々のユーザーに送信するには、送信する前にテストデバイスでプッシュが有効になっており、テストユーザーの有効なプッシュトークンが登録されている必要があります。iOSユーザーの場合、テストコンテンツカードを表示するには、Brazeから送信されたプッシュ通知をタップする必要があります。この動作はテストコンテンツカードにのみ適用されます。

### メッセージをユーザーとしてプレビュー

**テスト**タブからメッセージをプレビューすることも、ユーザーとして行うことができます。特定のユーザーやランダムなユーザーを選択するか、カスタムユーザーを作成できます。

![Custom_User_Preview][3]

### テストチェックリスト

- 画像やメディアは期待通りに表示され、機能しているか？
- リキッドは期待通りに機能しているか？Liquid が情報を返さない場合、[デフォルトの属性値]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/conditional_logic/#accounting-for-null-attribute-values)を考慮したか?
- あなたのコピーは明確で簡潔で正しいですか？
- リンクはユーザーを目的の場所に誘導していますか？

## デバッグ

コンテンツカードが送信された後、開発者コンソールの[イベントユーザーログ]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/)から問題を分解またはデバッグできます。 

一般的なユースケースは、ユーザーが特定のコンテンツカードを見られない理由をデバッグしようとすることです。そのためには、セッション開始時にSDKに配信されたコンテンツカードをインプレッションの前に**イベントユーザーログ**で確認し、それらを特定のキャンペーンに遡ることができます。

1. **設定** > **イベントユーザーログ** に移動します。
{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、[**イベントユーザーログ**] は **[開発者コンソール**] にあります。
{% endalert %}

{:start="2"}
2\.テストユーザーのSDKリクエストを見つけて展開します。
3\.[**生データ**] をクリックします。
4\.セッションの`id`を見つけてください。次に例の抜粋を示します:

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

5. [Base64 Decode and Encode](https://www.base64decode.org/)のようなデコードツールを使用して、Base64形式から`id`をデコードし、関連する`campaign_id`を見つけます。この例では、次のようになります。

    ```
    6185005a9d9bee79387cce43_$_cc=c3b25740-f113-c047-4b1d-d296f280af4f&mv=6185005b9d9bee79387cce45&pi=cmp
    ```

    ここで、`6185005a9d9bee79387cce43` は `campaign_id` です。<br><br>

6. **キャンペーン**ページに移動し、`campaign_id`を検索します。

![[キャンペーン] ページでの campaign_id の検索][1]

そこから、メッセージ設定とコンテンツを確認して、ユーザーが特定のコンテンツカードを見られない理由を詳しく調べることができます。

[1]: {% image_buster /assets/img_archive/cc_debug.png %}
[3]: {% image_buster /assets/img/cc-user-preview.png %}
