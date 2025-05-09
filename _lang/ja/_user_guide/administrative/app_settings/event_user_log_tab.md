---
nav_title: イベントユーザーログ
article_title: イベントユーザーログ
page_order: 7
page_type: reference
description: "このリファレンス記事では、Braze 連携における問題のデバッグやトラブルシューティングに役立つイベントユーザーログについて説明します。"

---

# イベントユーザーログ

> イベントユーザーログは、Braze 連携における問題の特定、デバッグ、その他のトラブルシューティングに役立ちます。このタブには、エラーの種類、エラーが関連したアプリ、エラーの発生時期を詳細に示すエラーのログが表示され、多くの場合にはエラーに関連する生データを表示することもできます。

{% alert tip %}
この記事に加えて、「[品質保証とデバッグツール](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/)」の Braze ラーニングコースを確認することをお勧めします。このコースでは、イベントユーザーログを使用して独自のトラブルシューティングとデバッグを行う方法を説明しています。
{% endalert %}

ログにアクセスするには、[**設定**] > [**イベントユーザーログ**] に移動します。

ログを簡単に見つけるために、以下を基準にするフィルターを適用できます。

* SDK または API
* アプリ名
* 期間
* ユーザー

各ログは複数のセクションに分かれており、次の項目があります。

* デバイス属性
* ユーザー属性
* イベント
* キャンペーンイベント
* 応答データ

[**生データ**] ボタンをクリックすると、その特定のログの生の JSON データが表示されます。

![イベントの未処理ログ][10]

イベントユーザーログは、記録後 30 日間ダッシュボードに残ります。

## トラブルシューティング

### テストユーザーの SDK ログの欠落

ユーザーを内部グループに追加したにもかかわらず、イベントユーザーログに SDK ログが表示されない場合、原因として設定オプションが不足している可能性があります。SDK ログを収集するには、その [[内部グループ]({{site.baseurl}}/user_guide/administrative/app_settings/internal_groups_tab/)] の [**内部グループ設定**] で [**グループメンバーのユーザーイベントを記録**] を必ず選択してください。

### ログ更新の遅延

これは弊社のAPIの速度に原因がある可能性があります。

SDK メソッドを呼び出す際、イベントをローカルにキャッシュして10 秒ごとにサーバーにフラッシュします。その時点の全体的な負荷に応じ、ジョブ処理キューがイベントを取り込むまでに 1 秒から数分かかります。  

探しているイベントをできるだけ早く表示するには、`requestImmediateDataFlush()` 関数を呼び出してみてください。

### セッション終了とセッション開始のタイムスタンプが酷似している (iOS)

イベントユーザーログには、Braze にセッション終了が通知されたときのタイムスタンプが表示されます。これは、次のセッションが開始される数ミリ秒前です。iOS はアプリがバックグラウンドにあるときにスレッドの実行を積極的に停止するため、Braze はアプリが再度開かれる前に、セッションが終了したことを認識できません。そのため、アプリが再度開かれるまでデータを Braze にフラッシュすることはできません。

セッション終了時刻はセッション開始の数秒前に指定されますが、イベントがフラッシュされるときに、セッション時間が個別にフラッシュされ、アプリが開いていた時間を反映して正確になります。したがって、この動作は `Median Session Duration` フィルターに影響しません。

ユーザーセッションに関連して、Braze を使用して次のようなデータを監視できます。

- ユーザーが実行したセッション数
- ユーザーの最後のセッションを開始した時点
- ユーザーがキャンペーン受信後にセッションを開始したかどうか
- ユーザーのセッション時間の中央値

これらの動作は、次のセッションでフラッシュされるセッション終了イベントの影響を受けません。

[10]: {% image_buster /assets/img_archive/rawlogs.png %}
