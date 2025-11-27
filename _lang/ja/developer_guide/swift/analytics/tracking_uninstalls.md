## アンインストール追跡の設定

### ステップ 1: バックグラウンドのプッシュを有効にする

Xcode プロジェクトで、[**Capabilities**] に移動し、[**Background Modes**] が有効になっていることを確認します。詳しくは、[サイレント・プッシュ]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift)通知を参照のこと。

### ステップ 2: 内部プッシュ通知を無視する

Swift Braze SDKは、バックグラウンドプッシュ通知を使用してアンインストール追跡分析を収集する。プッシュ通知が送信されたときにアプリが不要なアクションを起こさないようにするには、[内部プッシュ通知が無視される]({{site.baseurl}}/developer_guide/push_notifications/silent/?sdktab=swift#swift_ignoring-internal-push-notifications)ようにする必要がある。

### ステップ 3: テストプッシュを送信する（オプション）

次に、Brazeのダッシュボードからテスト用のプッシュ通知を自分に送る（ユーザープロファイルは更新されないのでご安心を）。

1. **メッセージング**＞**キャンペーンと**進み、関連プラットフォームを使ってプッシュ通知キャンペーンを作成する。
2. **設定**＞**アプリ設定に**進み、関連する`true` 値を持つ`appboy_uninstall_tracking` キーを追加し、**コンテンツ利用可能フラグを追加を**チェックする。
3. [**プレビュー**] ページを使用して、テストアンインストール追跡プッシュを自分に送信します。
4. アプリがプッシュ通知を受信したときに、不要な自動アクションを行わないようにチェックする。

{% alert note %}
バッジ番号はテストプッシュ通知と一緒に送信されるが、実際のアンインストール追跡プッシュではバッジ番号は送信されない。
{% endalert %}

### ステップ 3: アンインストール追跡を有効にする

最後に、Brazeでアンインストール追跡を有効にする。完全なチュートリアルについては、[アンインストール追跡を有効にするを]({{site.baseurl}}/user_guide/data_and_analytics/tracking/uninstall_tracking/#uninstall-tracking)参照のこと。

{% alert important %}
アンインストールの追跡は不正確な場合がある。Brazeに表示される指標は、遅れたり不正確であったりする可能性がある。
{% endalert %}
