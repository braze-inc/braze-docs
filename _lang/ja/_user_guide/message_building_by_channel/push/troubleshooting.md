---
nav_title: トラブルシューティング
article_title: プッシュのトラブルシューティング
page_order: 24
page_type: reference
description: "このページでは、プッシュメッセージングチャネルに関するさまざまな問題のトラブルシューティングステップを紹介します。"
channel: push
---

# プッシュのトラブルシューティング

> このページを使って、プッシュメッセージングチャネルの問題をトラブルシューティングできます。

## プッシュ通知を受信しない

プッシュ通知の配信に問題がありますか？以下の点を確認することで、この問題をトラブルシューティングできます。

- [プッシュサブスクリプションのステータス](#push-subscription-status)
- [セグメント](#segment)
- [プッシュ通知上限](#push-notification-caps)
- [レート制限](#rate-limits)
- [コントロールグループのステータス](#control-group-status)
- [有効なプッシュトークン](#valid-push-token)
- [プッシュ通知タイプ](#push-notification-type)
- [現在のアプリ](#current-app)

#### プッシュサブスクリプションのステータス

プッシュ通知は、購読中またはオプトインしたユーザーにのみ送信できます。**ユーザープロファイル**セクションの[エンゲージメント]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab)タブでユーザープロファイルを確認し、テスト対象のワークスペースでアクティブにプッシュ登録されているかどうかを確認します。複数のアプリに登録している場合は、「**Push Registered For**」フィールドにリストアップされます。

![登録済みのプッシュ通知]({% image_buster /assets/img_archive/trouble1.png %})

Braze エクスポートエンドポイントを使用してユーザープロファイルをエクスポートすることもできます。
- [識別子別のユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier)
- [セグメント別のユーザー]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment)

どちらのエンドポイントも、デバイスごとのプッシュ有効化情報を含むプッシュトークンオブジェクトを返します。

#### セグメント

ターゲットにしているセグメントに該当することを確認します（テストではなく本番のキャンペーンの場合）。**ユーザープロファイル**では、ユーザーが現在属しているセグメントのリストが表示されます。セグメンテーションはリアルタイムで更新されるため、これは常に変化する変数であることに注意してください。

![セグメント一覧]({% image_buster /assets/img_archive/trouble2.png %})

また、セグメントを作成する際に**User Lookup**を使用することで、ユーザーがセグメントに含まれていることを確認することもできます。

![検索フィールドを備えたユーザー検索セクション。]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:80%;"}

#### プッシュ通知上限

グローバルフリークエンシーキャップを確認します。ワークスペースにグローバルフリークエンシーキャップが設定されており、指定された時間枠のプッシュ通知上限をすでに超えているため、プッシュ通知を受け取れなかった可能性があります。

これを確認するには、ダッシュボードで[グローバルフリークエンシーキャップ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#freq-cap-feat-over)を確認します。キャンペーンがフリークエンシーキャップルールに従うように設定されている場合、これらの設定によって影響を受けるユーザーが多数存在します。

![キャンペーン詳細]({% image_buster /assets/img_archive/trouble3.png %})

#### レート制限

キャンペーンまたはキャンバスにレート制限が設定されている場合、この制限を超過したためにメッセージを受信できなくなっている可能性があります。詳細については、「[レート制限]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#rate-limiting)」を参照してください。

#### コントロールグループのステータス

これが単一チャネルのキャンペーンや、コントロールグループのあるキャンバスであれば、コントロールグループに属している可能性があります。

  1. [バリアントの分布]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing/#step-5-distribute-users-among-your-variants)を確認して、コントロールグループがあるかどうかを確認します。
  2. コントロールグループがある場合は、[キャンペーンコントロールグループ]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#in-campaign-control-group-filter)でフィルターするセグメントを作成し、[セグメントをエクスポートして]({{site.baseurl}}/user_guide/data_and_analytics/export_braze_data/segment_data_to_csv/#exporting-to-csv)、ユーザー ID がこのリストにあるかどうかを確認します。

#### 有効なプッシュトークン
プッシュトークンは、送信者がプッシュ通知で特定のデバイスをターゲットにするために使用する識別子です。つまり、デバイスが有効なプッシュトークンを持っていなければ、そのデバイスにプッシュ通知を送ることはできません。 

#### プッシュ通知タイプ

正しい種類のプッシュ通知を使用しているか確認します。例えば、FireTV をターゲットにしたい場合は、Android のプッシュキャンペーンではなく、Kindle のプッシュ通知を使用します。同様に、Android をターゲットにする場合は、iOS のプッシュキャンペーンではなく、Android のプッシュ通知を使用します。Braze のワークフローを理解するための詳細については、以下の記事を参照してください。
- [Apple Push Notification]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=swift)
- [Firebase Cloud Messaging]({{site.baseurl}}/developer_guide/push_notifications/troubleshooting/?sdktab=android)

#### 現在のアプリ

内部ユーザーでプッシュ送信をテストする場合、プッシュ通知を受け取りたいユーザーが現在該当アプリにログインしていることを確認してください。これが原因で、ユーザーがプッシュを受け取らなかったり、セグメント対象ではないと思われるプッシュを受け取ったりすることがあります。

## プッシュのクリックが予期せずアプリ内で開く

プッシュ通知のリンクが Web ブラウザではなくアプリで予期せず開く問題が発生している場合、キャンペーンの設定または SDK の実装に問題がある可能性があります。以下のステップを参照してください。

### クリック時の動作を確認する

キャンペーンまたはキャンバスステップで、[**モバイルアプリ内で Web URL を開く**] が選択されていないことを再確認します。選択されている場合は、選択をクリアして再起動します。 

![プッシュ通知の設定における「クリック時の動作」フィールドは「Web URL を開く」に設定され、「モバイルアプリ内で Web URL を開く」はチェックされていない。]({% image_buster /assets/img/push_on_click.png %})

クリック時の動作「Web URL を開く」のデフォルトのインタラクションは、SDK のバージョンによって異なります。SDK バージョン iOS 2.29.0 および Android 2.0.0 以降では、このオプションはデフォルトで選択されており、Web URL はアプリ内の Web ビューで開きます。これらのバージョンより前では、このオプションはデフォルトでクリアされ、Web URL はデバイスのデフォルトの Web ブラウザで開きます。

これが問題でない場合は、プッシュの実装に問題がある可能性があります。 

### プッシュの統合を再確認する

プッシュ通知のリンクがアプリ内で予期せず開く場合、プッシュ通知の統合やカスタマイズ設定に問題がある可能性があります。以下のステップに従ってトラブルシューティングを行います。

1. **プッシュデリゲートの実装を見直す：** Braze プッシュデリゲートが正しく実装されていることを確認します。詳細な手順については、お使いの[プラットフォーム]({{site.baseurl}}/developer_guide/home/)のプッシュ通知統合ガイドを参照してください。
2. **カスタムリンクの処理を検査する：** アプリにすべての `https://` リンクのカスタム処理が含まれているかどうかを確認します。カスタム設定によってデフォルトの動作が上書きされる可能性があります。開発者チームと協力し、必要に応じてこれらの設定を見直し、調整してください。
3. **iOS のプッシュ登録を確認する：** iOS の場合は、[APN へのプッシュ通知の登録]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns)に関するプッシュ統合ガイドのステップ 1 を再確認します。アプリの起動が完了する前に、デリゲートオブジェクトが同期的に割り当てられるようにしてください。このステップは `application:didFinishLaunchingWithOptions:` メソッドで完了する必要があります。
4. **統合をテストする：** 調整後、iOS と Android の両方のデバイスでプッシュ通知の動作をテストし、問題が解決したことを確認します。

## プッシュタイトルが iOS で切れるが Android では正しく表示される

プッシュ通知のタイトルに Liquid パーソナライゼーションが含まれており、Android では完全に表示されるのに iOS では途中で切れる場合、これは各プラットフォームがタイトル文字列内の改行文字（`\n`）を処理する方法の違いが原因です。

Android はプッシュタイトル文字列から空白、タブ、改行を自動的に除去します。iOS はそうしないため、Liquid 変数が末尾に改行を含む値に解決されると、iOS はその改行をタイトルの終わりとして扱い、残りのテキストを切り捨てます。

例えば、`Regarding your flight from {% raw %}{{${city_from}}}{% endraw %} to {% raw %}{{${city_to}}}{% endraw %}` のようなタイトルは、`city_from` 変数に末尾の改行が含まれている場合、iOS では `Regarding your flight from` と表示される可能性があります。

これを修正するには、`strip_newlines` Liquid フィルターを適用し、タイトル全体を `capture` ブロックで囲みます。

{% raw %}
```liquid
{% capture title %}Regarding your flight from {{${city_from}}} to {{${city_to}}}{% endcapture %}
{{ title | strip_newlines }}
```
{% endraw %}

## Web プッシュ通知が期待どおりに動作しない

ブラウザでプッシュ通知の問題が発生した場合は、サイトの通知権限をリセットし、サイトのストレージをクリアする必要がある場合があります。以下のステップを参照してください。

{% tabs %}
{% tab Chrome %}

### デスクトップの Chrome をリセットする

1. Chrome ブラウザで URL の横にある**「サイト情報を表示」**のスライダーアイコンを選択します。
2. **通知**の設定で、**権限のリセット**を選択します。
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
4. DevTools で、**Application** タブに移動します。
5. サイドバーで、**Storage** を選択します。
6. **サイトデータを消去する**を選択します。
7. 更新された設定を適用するために、Chrome でページの再読み込みを求められます。**再読み込み**を選択します。

プッシュ権限がリセットされました。サイトに新しいタブを開いて試してみてください。

### Android で Chrome をリセットする

Android の通知ドロワーにサイトからの通知が表示されている場合:

1. プッシュ通知から<i class="fas fa-cog" title="設定"></i>をタップし、**サイトの設定**を選択します。
2. **サイトの設定**から、**クリアしてリセット**をタップします。

サイトからの通知が表示されていない場合:

1. Android で Chrome を開きます。
2. <i class="fas fa-ellipsis-vertical"></i>メニューをタップします。
3. [**設定**] > [**サイトの設定**] > [**通知**] に移動します。
4. 通知が**送信前に確認する（推奨）**に設定されていることを確認します。
5. リストでサイトを見つけます。
6. エントリを選択し、[**クリアしてリセット**] をタップします。

プッシュ権限がリセットされました。サイトに新しいタブを開いて試してみてください。

{% endtab %}
{% tab Firefox %}

### デスクトップの Firefox をリセットする

1. サイト URL の横で、<i class="fa-solid fa-circle-info" alt="info icon"></i>または<i class="fas fa-lock" alt="lock icon"></i>を選択します。
2. [**権限**] で、[**通知を受信**] の横にある [<i class="fa-solid fa-circle-xmark" title="この権限をクリアして再度確認"></i>] を選択して通知権限をクリアします。
3. 同じメニューで、**Cookie とサイトデータを消去**を選択します。
4. 選択を確認するダイアログで、**OK** を選択します。

プッシュ権限がリセットされました。サイトに新しいタブを開いて試してみてください。

### Android で Firefox をリセットする

Android のプッシュ権限をリセットするには、この [Mozilla サポート記事](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser)を参照してください。

{% endtab %}
{% tab Safari %}

### MacOS で Safari をリセットする

{% alert note %}
これらのステップは MacOS 専用です。Apple は Windows 版 Safari の Web プッシュをサポートしていません。
{% endalert %}

1. Safari を開きます。
2. [Mac のメニューバー](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac)から、**Safari** > **設定** > **Web サイト** > **通知**に進みます。
3. リストからサイトを選択します。
4. **削除**を選択すると、そのサイトの通知権限が削除されます。
5. 次に、[**プライバシー**] > [**Web サイトデータを管理**] に移動します。
6. リストからサイトを選択します。
7. **削除**を選択するか、すべてのサイトデータを削除するには、**すべて削除**を選択します。
8. [**完了**] を選択します。

プッシュ権限がリセットされました。サイトに新しいタブを開いて試してみてください。

{% endtab %}
{% endtabs %}

## プッシュエラーメッセージ

一般的なプッシュエラーメッセージ（`DEVICE_UNREGISTERED`、`Unregistered`、`NotRegistered` など）の詳細については、「[一般的なプッシュエラーメッセージ]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_error_codes/)」を参照してください。

さらにサポートが必要な場合は、[サポートチケット]({{site.baseurl}}/braze_support/)を登録してください。