---
nav_title: アクション通過メールキャンペーン
article_title: アクション通過メールキャンペーン
page_order: 10

description: "このリファレンス記事では、新しいBraze Trans アクション アルメールキャンペーンを作成および設定する方法について説明します。"
page_type: reference
tool:
  - Campaigns
channel: email
alias: "/api/api_campaigns/transactional_campaigns"

---

# アクション間の電子メールキャンペーン

> Braze Trans アクション al E メールは、送信者と受信者間で合意されたトランスアクションを容易にするために送信されます。このリファレンス記事では、Braze ダッシュボードでtrans アクション al メール キャンペーンを作成し、[`/transactional/v1/campaigns/{campaign_id}/send` エンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) のAPI コールに含める`campaign_id` を生成する方法について説明します。

{% alert important %}
Braze Trans アクション アルメールは、一部のBrazeの一部としてのみ利用可能です。詳しくは、Braze 顧客のサクセスマネージャーに到達するか、[サポートチケット]({{site.baseurl}}/braze_support/)を開封してください。
{% endalert %}

trans アクション al メール キャンペーン型は、お客様と顧客との間で合意されたやり取りを容易にするために、自動化された非プロモーションメールを送信する目的で構築されています。これには以下のような情報が含まれます。

- 注文確認
- パスワードのリセット
- 請求アラート
- 出荷警告

つまり、trans アクション al メール s を使用して、スピードが最も重要な単一のユーザーに対して、サービスから発信されるビジネスクリティカルな通知s を送信できます。 

{% alert important %}
Trans アクション al メール は、Trans アクション al キャンペーン s とは異なり、追加費用なしでユーザー s を対象とすることができます。たとえば、Trans アクション al キャンペーン s には、ユーザーがカートにアイテムを追加した後に送信されるメッセージを含めることができます。詳細については、[オーディエンスターゲットオプション]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users/)を参照してください。
{% endalert %}

## ステップ 1:新しいキャンペーンを作成する

新しいトランスアクションのすべてのメール キャンペーンを作成するには、キャンペーンを作成し、**Trans al メール**をメッセージング チャネルとして選択します。

![「キャンペーンの作成」ドロップダウンで、トランスアクション al メールの選択肢が強調表示されます。][1]{: style="float:right;max-width:30%;margin-left:15px;"}

これで、トランスアクションのすべてのメール キャンペーンの設定に進むことができます。

## ステップ 2:キャンペーンの設定

トランザクションアクション メール キャンペーンs のキャンペーン作成フローは、[標準メール キャンペーン]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/) と比較して簡略化されており、ビジネスクリティカルなトランザクションアクション メールがすべてのユーザーs に到達できるようになっています。

そのため、他のBraze キャンペーンタイプに精通している設定が、このキャンペーンタイプを設定する際に必要とされない場合があります。

- **Delivery**ステップが簡略化され、スケジュールオプションが削除されました。Trans アクション al メール s は、**Delivery** ページに表示されているキャンペーン ID を使用して、Braze REST API からトリガーされます。再適格性コントロールs やフリークエンシーキャップ 設定s などの追加の設定s も削除され、サービストリガーがリクエストを送信したときに、これらの重要なトランスアクションアラートに対してすべてのユーザーが到達可能であることが確認されました。
- **Target Users**ステップが削除されました。trans アクション al メール はユーザー群全体を適格(配信停止 d ユーザー s を含む)として登録するため、フィルター s またはSegment s を指定する必要はありません。そのため、このメッセージを受信する必要のあるユーザにアプリするロジックがある場合は、そのロジックをアプリにしてから、特定のユーザーにメッセージをトリガーするようにAPI リクエストをBrazeするかどうかを決定することをお勧めします。
- **コンバージョン**ステップが削除されました。Trans アクション al メール s は現時点ではコンバージョンイベント "トラッキング に対応していません。

![トランスアクションの電子メールキャンペーンを作成するためのコンポーズ、配信、および確認ワークフロー。][2]

トランスアクションのすべてのメール キャンペーンを設定するには、次のステップに従います。

1. メッセージを送信した後、**Campaigns** ページで結果を確認できるように、説明的な名前を追加します。
2. メールを作成するか、テンプレートから選択します。
3. `campaign_id` を書き留めます。API キャンペーンを保存した後、[Trans アクション al E メールエンドポイント]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_transactional_message) の記事に記載されているAPI リクエストに、生成された`campaign_id` フィールドs を含める必要があります。
4. **キャンペーンを保存**をクリックすると、API キャンペーンを開始するように設定されます!

{% alert note %}
ワンクリックリスト-配信停止 設定trans アクション al メール キャンペーン s デフォルト s to **他のメール キャンペーン s と同様にワークスペース デフォルト** を使用します。これはトランスアクションのメッセージングを対象としているため、Braze はワンクリック配信停止を追加しません。このキャンペーンにワンクリック配信停止を追加するには、[この設定]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#message-level-one-click-list-unsubscribe)を**送信情報**で編集します。
{% endalert %}

### trans アクション al メール s で禁止されたタグs

`Connected Content`および`Promotion Code`流動タグsは、trans アクション al メール キャンペーン s内では使用できません。

`Connected Content`タグを使用すると、送信プロセス中に送信APIリクエストを行うためのBrazeが必要になります。これにより、リクエストした外部サービスに遅延が発生している場合に、メッセージ送信プロセスが遅くなる可能性があります。同様に、`Promotion Code`タグは、Brazeがプロモーションの有効性を評価するために追加の処理を実行することを要求します。これは、送信処理が利用できない場合には、送信処理が遅くなる可能性があります。

そのため、trans アクション al メール キャンペーンのフィールドに`Connected Content` または`Promotion Code` タグ s を含めることはできません。


[1]: {% image_buster /assets/img/transactional_email_campaign.png %}
[2]: {% image_buster /assets/img/transactional_campaign_compose.png %}
