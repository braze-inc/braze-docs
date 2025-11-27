---
nav_title: トラブルシューティング
article_title: トラブルシューティング
page_order: 23
page_type: reference
description: "このページでは、Pushメッセージングチャネルに関するさまざまな問題のトラブルシューティングステップを紹介する。"
channel: push
---

# トラブルシューティング

> このページを使用して、Pushメッセージングチャネルの問題をトラブルシューティングする。

## プッシュ通知を受信しない

プッシュ通知での配信に課題を感じているか？以下の点を確認してこの問題のトラブルシューティングを行うためのステップがいくつかあります。

- [プッシュ通知のサブスクリプションのステータス](#push-subscription-status)
- [セグメント](#segment)
- [プッシュ通知上限](#push-notification-caps)
- [レート制限](#rate-limits)
- [コントロールグループステータス](#control-group-status)
- [有効なプッシュトークン](#valid-push-token)
- [プッシュ通知タイプ](#push-notification-type)
- [現在のアプリ](#current-app)

#### プッシュ通知のサブスクリプションのステータス

プッシュ通知は、登録済みユーザーまたはオプトインしたユーザーにのみ送信できます。**ユーザー**プロファイル[]セクションの[エンゲージメント]]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab)タブでユーザープロファイルを確認し、テスト対象のワークスペースでアクティブにプッシュ登録されているかどうかを確認する。複数のアプリに登録している場合は、「**Push Registered For**」フィールドにリストアップされる：

![登録済みのプッシュ通知]({% image_buster /assets/img_archive/trouble1.png %})

Brazeエクスポートエンドポイントを使用してユーザープロファイルをエクスポートすることもできる：
- [識別子別のユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [セグメント別ユーザー数]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

どちらのエンドポイントも、デバイスごとのプッシュ有効化情報を含むプッシュトークンオブジェクトを返す。

#### セグメント

テストではなく本番のキャンペーンの場合）ターゲットにしているセグメントに該当することを確認する。**ユーザープロフィールでは**、ユーザーが現在属しているセグメントのリストが表示される。セグメンテーションはリアルタイムで更新されるため、これは常に変化する変数であることに注意してください。

![セグメント一覧]({% image_buster /assets/img_archive/trouble2.png %})

また、セグメンテーションを作成する際に、**User Lookupを**使用することで、ユーザーがセグメンテーションの一部であることを確認することができる。

![検索フィールドを備えたユーザー検索セクション。]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### プッシュ通知上限

グローバル周波数の上限を確認します。ワークスペースにグローバル頻度上限が設定されており、指定された時間枠のプッシュ通知上限をすでに超えているため、プッシュ通知を受け取れなかった可能性がある。

このためには、ダッシュボードで[グローバルフリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over)を確認します。キャンペーンがフリークエンシー・キャッピング・ルールに従うように設定されている場合、これらの設定によって影響を受けるユーザーが多数存在する。

![キャンペーン詳細]({% image_buster /assets/img_archive/trouble3.png %})

#### レート制限

キャンペーンまたはキャンバスにレート制限が設定されている場合、この制限を超過したためにメッセージングを受信できなくなる可能性があります。詳細については、「[レート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting)」を参照してください。

#### コントロールグループステータス

これが単一チャンネルのキャンペーンや、コントロールグループのあるキャンバスであれば、コントロールグループに属している可能性がある。

  1. [バリアントの分布]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants)をチェックして、コントロールグループがあるかどうかを確認します。
  2. もしそうであれば、[キャンペーンコントロールグループで]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter)フィルターするセグメントを作成し、[セグメントをエクスポートして]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv)、ユーザーIDがこのリストにあるかどうかをチェックする。

#### 有効なプッシュトークン
プッシュトークンは、送信者がプッシュ通知を持つ特定の機器を対象にするために使用する識別子です。つまり、デバイスが有効なプッシュトークンを持っていなければ、そのデバイスにプッシュ通知を送ることはできない。 

#### プッシュ通知タイプ

正しい種類のプッシュ通知を使用しているか確認する。例えば、FireTVをターゲットにしたい場合は、Androidのプッシュ・キャンペーンではなく、Kindleのプッシュ通知を使うことになる。同様に、Android をターゲットにする場合は、iOS のプッシュキャンペーンではなく、Android のプッシュ通知を使用します。Brazeのワークフローを理解するための詳細については、以下の記事をチェックしてほしい：
- [Apple プッシュ通知]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebaseクラウドメッセージング]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### 現在のアプリ

内部ユーザーでプッシュ通知をテストする場合、プッシュ通知を受け取りたいユーザーが現在該当アプリにログインしていることを確認する。これが原因で、ユーザーがプッシュを受け取らないか、またはセグメンテーション対象ではないと思われるプッシュを受け取ることがあります。

## プッシュクリックがアプリ内で予期せず開封される

プッシュ通知のリンクがWebブラウザではなくアプリで予期せず開封される問題が発生している場合、キャンペーンの設定またはSDKの実装に問題がある可能性がある。サポートが必要な場合は、以下のステップを参照してください。

### クリック時の動作を確認する

キャンペーンまたはキャンバスのステップで、[**モバイルアプリ内で Web URL を開く**] が選択されていないことを再確認します。選択されている場合は、その選択をクリアして再起動します。 

![[モバイルアプリ内で Web URL を開く] のチェックを外した状態で [Web URL を開く] に設定されたプッシュを設定する際の [クリック時の動作] フィールド。]({% image_buster /assets/img/push_on_click.png %})()

クリック時の動作 [Web URL を開く] のデフォルトのインタラクションは、SDK のバージョンによって異なります。SDKバージョンiOS 2.29.0およびAndroid 2.0.0以降では、このオプションはデフォルトで選択されており、Web URLはアプリ内のWebビューで開封される。これらのバージョン以前では、このオプションはデフォルトでクリアされ、Web URL はデバイスのデフォルトの Web ブラウザで開かれます。

これが問題でない場合は、プッシュの実装に問題がある可能性があります。 

### プッシュの統合を再確認する

プッシュ通知のリンクがアプリ内で予期せず開封される場合、プッシュ通知の統合やカスタマイズ設定に問題がある可能性がある。以下のステップに従ってトラブルシューティングを行います。

1. **プッシュデリゲートの実装を見直す: **Brazeプッシュデリゲートが正しく実装されていることを確認する。詳細な手順については、[プラットフォームの]({{site.baseurl}}/developer_guide/home/)プッシュ通知の統合ガイドを参照のこと。
2. **カスタムリンクの処理を検査する: **アプリにすべての `https://` リンクのカスタム処理が含まれるかどうかを確認します。カスタム設定によってデフォルトの動作が上書きされる可能性があります。開発者チームと協力し、必要に応じてこれらの設定を見直し、調整します。
3. **iOS のプッシュ登録を確認する: **iOSの場合は、[APNにプッシュ通知を登録する]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns)プッシュ統合ガイドのステップ1を再確認する。アプリの起動が完了する前に、デリゲートオブジェクトが同期的に割り当てられるようにします。このステップは `application:didFinishLaunchingWithOptions:` メソッドで完了する必要があります。
4. **連携をテストする: **調整後、iOSとAndroidの両方のデバイスでプッシュ通知の動作をテストし、問題が解決したことを確認する。

## Webプッシュ通知が期待通りに動作しない

ブラウザーでプッシュ通知の問題が発生した場合は、サイトの通知権限をリセットし、サイトのストレージをクリアする必要がある場合があります。サポートが必要な場合は、以下のステップを参照してください。

{% tabs %}
{% tab Chrome %}

### デスクトップのChrome をリセットする

1. クロームブラウザのURLの横にある「**サイト情報を見る**」のスライダーアイコンを選択する。
2. **通知]**で[**権限をリセット]**を選択する。
3. Chrome DevTools を開きます。オペレーティングシステムごとの関連するショートカットは次のとおりです。

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | キーボードショートカット                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\.DevTools で、**Application** タブに移動します。
5. サイドバーで、**Storage** を選択します。
6. **サイトデータの消去を**選択する。
7. 更新された設定を適用するために、Chrome でページの再読み込みを求められます。**リロードを**選択する。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

### Android で Chrome をリセットする

Android 通知ドロワーにサイトからの通知が表示されている場合:

1. プッシュ通知から<i class="fas fa-cog" title="設定s"></i>をタップし、**Site 設定s**を選択します。
2. **サイト設定s**から**クリア&リセット**をタップします。

サイトからの通知が開かれていない場合:

1. Android で Chrome を開きます。
2. <i class="fas fa-ellipsis-vertical"></i>メニューをタップします。
3. [**設定**] > [**サイトの設定**] > [**通知**] に移動します。
4. 通知が [送信前に確認する (推奨)] に設定されていることを確認します。
5. リストでサイトを見つけます。
6. エントリを選択し、[**クリアしてリセット**] をタップします。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

{% endtab %}
{% tab Firefox %}

### デスクトップのFirefox をリセットする

1. サイトURLの横に、<i class="fa-solid fa-circle-info" alt="info icon"></i> または<i class="fas fa-lock" alt="lock icon"></i> を選択する。
2. [**権限**] で、[**通知を受信**] の横にある [<i class="fa-solid fa-circle-xmark" title="この権限をクリアして再度確認"></i>] を選択して通知権限をクリアします。
3. 同じメニューで、**Clear Cookies and Site Data**を選択します。
4. 選択を確認するダイアログで、**OKを**選択する。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

### Android時にFirefox を初期化する

Androidのプッシュ権限を再設定するには、この[Mozilla サポート記事](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser) を参照してください。

{% endtab %}
{% tab Safari %}

### macOS での Safari のリセット

{% alert note %}
AppleはWindowsのSafariのWebプッシュをサポートしていないため、これらのステップはMacOSのみのものである。
{% endalert %}

1. Safari を開きます。
2. [Macのメニューバー](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac)から、**Safari**> **設定**> **Webサイト**> **通知**に進みます。
3. リストからサイトを選択します。
4. サイトの通知権限を削除するには**Removeを**選択する。
5. 次に、[**プライバシー**] > [**Web サイトデータを管理**] に移動します。
6. リストからサイトを選択します。
7. **Removeを**選択するか、すべてのサイトデータを削除するには**Remove Allを**選択する。
8. ［**完了**] を選択します。

プッシュ権限がリセットされます。サイトに新しいタブを開き、試してみてください。

{% endtab %}
{% endtabs %}

サポートが必要な場合は、[サポートチケットを]({{site.baseurl}}/braze_support/)を登録してください。

