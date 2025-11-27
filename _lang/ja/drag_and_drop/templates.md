{% if include.section == "SDK requirements" %}

## 前提条件

### 最小の SDK バージョン

ドラッグアンドドロップエディタを使用して作成されたメッセージは、次の最小SDKバージョンのユーザーにのみ送信できます。詳しくは、[ドラッグ＆ドロップでアプリ内メッセージを作成するを参照のこと：前提条件

{% sdk_min_versions swift:5.0.0 android:8.0.0 web:2.5.0 %}

### テキストリンクのSDKバージョン

メッセージを削除しないテキストリンクを含めるには、以下の最低SDKバージョンが必要である：

{% sdk_min_versions swift:6.2.0 android:26.0.0 %}

{% alert warning %}
アプリ内メッセージにURLへリダイレクトするリンクを含み、ユーザーが指定された最小SDKバージョンを使用していない場合、リンクをクリックするとメッセージが閉じ、ユーザーはフォームを送信するためにメッセージに戻ることができない。
{% endalert %}

{% endif %}

{% if include.section == "message style" %}

テンプレートをカスタマイズする前に、サイドメニューを使用してメッセージ全体のメッセージレベルのスタイルを設定できます。例えば、メッセージに含まれるすべてのテキストのフォントやすべてのリンクの色をカスタマイズしたい場合があります。メッセージをモーダルまたは全画面表示タイプにすることもできます。

{% endif %}


<!-- Add this below after the disclaimers are added to all email sign-up templates: "We have provided a placeholder disclaimer in the template solely as an example, but this should not be relied upon for compliance purposes."-->

{% if include.section == "email disclaimer" %}

メッセージには、オプトインの文章とブランドのプライバシーポリシーおよび利用規約へのリンクを含めることをお勧めします。法務チームと協力して、特定のブランドに合わせた文章を作成してください。

{% alert note %}
配信可能性のベストプラクティスは、法的要件を超えることが多いため、必ずメール送信に関する明示的な同意を得て、またユーザーが簡単に拒否できるようにすることをお勧めします。
{% endalert %}

{% endif %}

{% if include.section == "email validation" %}

もしユーザーが受け付けられない特殊文字を含むメールアドレスを入力した場合、一般的なエラーインジケーターが表示され、フォームを送信することができない。このエラーメッセージはカスタマイズできない。**プレビュー & テスト** タブおよびテストデバイスでエラーの動作を確認できます。Braze が [メール アドレスの検証]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/email_validation/) でメール アドレスをどのようにフォーマットするかの詳細をご覧ください。

{% endif %}

{% if include.section == "email double opt-in" %}

### ダブルオプトイン認証

リストにサインアップした人がリストにサインアップするつもりであり、正しいメールアドレスを提供したことを確認するために、メールサインアップフォームを介してサインアップした人から[ダブルオプトイン](https://www.braze.com/resources/articles/embracing-the-email-double-opt-in)フローを送信して、再確認を取得することをお勧めします。

これを設定する方法のひとつにキャンバスがある：

1. アクションベースのキャンバスを作成し、ユーザーがメールアドレスをBrazeに追加したときにトリガーするように設定します。プラットフォームに不慣れなユーザーをターゲットにできるようにしてください（例えば、キャンバス内でフィルターのないSegmentを使用するなど）。
2. {% raw %}`{{${set_user_to_opted_in_url}}}`{% endraw %} Liquidタグへのハイパーリンクを持つCTA付きメールメッセージステップを作成する。これにより、ユーザーのメールサブスクリプション状態が`opted_in`に変更されます。ボタンをクリックすると。
3. [アクション パス ステップ]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths#action-paths)を追加します。
4. 最初のパスでは、ユーザーがのサブスクリプションステータスを `opted_in` に変更したときにメールをトリガーします。このメールで、ユーザーにメールアドレスが確認されたことを通知する必要があります。
5. ウィンドウの有効期限が切れた後、キャンバスを終了するための別のパスを設定します。

{% endif %}

{% if include.section == "reporting" %}

キャンペーンの開始後、リアルタイムで結果を分析して、キャンペーンにエンゲージしたユーザー数を確認できます。サブスクリプショングループにオプトインしたユーザーの数を確認するには、アプリ内メッセージを受信してフォームを送信したユーザーをフィルター処理して、サブスクリプショングループに登録したユーザーの[セグメントを作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)します。

{% endif %}