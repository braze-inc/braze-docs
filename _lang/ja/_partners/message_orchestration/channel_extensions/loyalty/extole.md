---
nav_title: Extole
article_title: Extole
description: "この記事では、Braze Extole のパートナーシップにつて説明します。Extole はリファラルマーケティング企業であり、友人紹介プログラムと成長プログラムから顧客イベントと属性を取り込むことができるようにします。"
alias: /partners/extole/
page_type: partner
search_tag: Partner

---

# Extole

> SaaS企業である[Extole](https://www.extole.com/)社は、友達紹介マーケティングの業界リーダーであり、顧客獲得を増やすための効果的な紹介マーケティング・プログラムの作成と最適化を支援している。

_この統合は Extole によって管理されます。_

## 統合について

Braze と Extole の統合により、Extole の友人紹介プログラムや成長プログラムから顧客イベントや属性を Braze に取り込むことができ、顧客の獲得、エンゲージメント、ロイヤルティを高める、よりパーソナライズされたマーケティングキャンペーンを作成できるようになります。パーソナライズされた共有コードやリンクなど、Extoleのコンテンツ属性をBrazeのコミュニケーションに動的に取り込むこともできる。

## 前提条件

| 必要条件 | 説明 |
| ----------- | ----------- |
| Extole アカウント | このパートナーシップを活用するには、Extole アカウントが必要です。 |
| Braze REST API キー | `users.track` 権限を持つ Braze REST API キー。これはBrazeのダッシュボードで**設定** > **APIキー**から作成できます。 |
| Braze API URL | あなたのBraze API URLは、あなたの[Brazeインスタンスに]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)固有である。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ユースケース

以下の使用例では、ExtoleとBrazeの統合を活用する方法をいくつか紹介している。Extole の実装マネージャーおよびカスタマーサクセスマネージャーと協力して、お客様の自社固有のニーズに対応するオプションを開発します。

- 紹介プログラムやエンゲージメントプログラムのカスタムイベントを活用して、BrazeのキャンペーンやCanvasをトリガーする。
- Extoleを使用したプログラムのデータを使用して、カスタムセグメント、ダッシュボード、レポートを作成する。
- Braze でユーザーをマーケティングリストに自動的に登録または登録解除する

## 統合

統合を迅速に起動して実行するには、次の手順を実行します。Extole の実装およびカスタマーサクセスマネージャーがこのプロセスを支援し、ご質問に回答します。

### Brazeアカウントに接続する

1. My Extoleアカウントの[パートナー](https://my.extole.com/partners)ページでBrazeインテグレーションを選択する。
2. Braze 統合で [**インストール**] を選択し、Extole と Braze の接続を開始します。
3. Braze REST API キーをはじめとする必須フィールドを入力します。 
4. Braze API URLを入力する。このURLは、Brazeアカウントがどのインスタンスにプロビジョニングされているかによって異なる。
5. Brazeに送信したいExtoleイベントを追加する。デフォルトのイベント、イベントプロパティ、およびユーザー属性は、[Extole イベントの表](https://dev.extole.com/docs/braze#extole-program-events)で説明されています。
6. `FULFILLED` 状態以外に、Braze に送信するリワードの状態を追加します。利用可能なリワードの状態の説明については、[Extole リワードの表](https://dev.extole.com/docs/braze#extole-rewards)を参照してください。
7. Braze外部IDキーマッピングを選択する。これが、ExtoleがBrazeでユーザー・プロフィールを更新する方法だ。Braze の external ID キーを Extole のユーザーの`email_address` または`partner_user_id` にマッピングできます。より安全なので、`email_address` の代わりに`external_id` を使用することをお勧めする。
8. 設定を保存して接続を完了する。これで、ExtoleのイベントがBrazeのアカウントに流れるようになった。

### Extole プログラムイベント

以下は、ExtoleがBrazeに送信するデフォルトのイベント、イベントプロパティ、ユーザー属性である。追加する Extole イベントを特定して統合に追加するには、Extole 実装またはカスタムサクセスマネージャーにご連絡ください。

| イベント | 説明 | イベントプロパティ | ユーザー属性 |
| ----------- | ----------- | ----------- | ----------- |
| `extole_created_share_link` | 参加者は、Extole Share Experience にメールを入力して、共有リンクを作成します。 | イベント名  <br>イベント時間  <br>パートナー (Extole)  <br>ファンネル (アドボケイトまたは友人)  <br>プログラム | <br>external ID <br>メール  <br>リンクを共有する |
| `extole_shared` | 参加者が自分の紹介リンクを友人にシェアする。 | イベント名  <br>イベント時間  <br>パートナー (Extole)  <br>external ID  <br>ファンネル (アドボケイトまたは友人)  <br>プログラム  <br>シェアチャンネル | メール <br>名 <br>姓 |
| `outcome` - 結果は、プログラムのコンフィギュレーション（`extole_shipped` や`extole_converted` など）に基づいてダイナミックに変化する。| 参加者が、プログラムに設定されている目的の成果イベントをコンバージョンまたは完了た。 | プログラムごとのダイナミック | メール <br>名 <br>姓 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Extole のサブスクリプション状態

| サブスクリプションの状態 | 説明 | イベントプロパティ | ユーザー属性 |
| ----------- | ----------- | ----------- | ----------- |
| `subscribed` | 参加者がマーケティングメッセージの受信をオプトインした。 | 該当なし | メール  <br>リストのタイプ  <br>external ID  <br>メール購読 (オプトイン) |
| `unsubscribed` | 参加者が Extole メールコミュニケーションの受信をオプトアウトした。| メール  <br>external ID  <br>サブスクリプション状態 (サブスクリプション解除)  <br>サブスクリプショングループ ID  | リストのタイプ |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

### Extrail のリワード

デフォルトでは、Extoleは `FULFILLED` 状態のリワードイベントを Braze に送信します。このため、Braze キャンペーンまたはキャンバスを通じてリワード通知をトリガーできます。その他のリワード状態については、以下の表を参照してください。

| リワード状態 | 説明 | イベントプロパティ | ユーザー属性 |
| ----------- | ----------- | ----------- | ----------- |
| `FULFILLED` | デフォルトの状態。リワードには、Extole リワードサプライヤーによって価値 (クーポンやギフトカードなど)が割り当てられています。 | メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `EARNED` | リワードが作成され、人物に関連付けられています。 | メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `SENT` | リワードが履行され、受領者にメールまたはデバイスで送信されました。 | メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `REDEEMED` | リワードは、Extole に送信されたコンバージョンイベントまたは引き換えイベントで証明されているように受領者によって使用されています。| メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `FAILED` | 問題が発生したため、リワードを発行または送付できませんでした。注意する必要があります。 | メール <br>額面  <br>クーポンコード  <br>額面タイプ  | メール <br>名  <br>姓 |
| `CANCELED` | リワードは無効化されました。インベントリに戻されます。 | メール <br>額面  <br>額面タイプ  | メール <br>名  <br>姓 |
| `REVOKED` | 履行されたリワードが無効化されました。たとえば、Extole がサプライヤーギフトカードを依頼したが、カードが誤って送付されたと判断した場合などです。サプライヤーがリワードの取り消しに対応している場合、Extole は資金の払い戻しを依頼し、リワードは無効になります。 | メール <br>額面   <br>額面タイプ  | メール <br>名  <br>姓 |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }


## カスタマイズ

### Brazeでユーザーを検索し、作成する

Extole に external ID (ユーザー ID) がない新しいメールや SMS サブスクリプションなどの特定のユースケースでは、Extole は Braze の[識別子によるユーザープロファイルのエクスポートのエンドポイント]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)を使用して、ユーザーの ID を確認できます。ユーザーがBrazeに存在する場合、Extoleはプロフィール属性を追加・更新する。リクエストがユーザープロファイルを返さない場合、Extoleは`/users/track` エンドポイントを使用して、ユーザーのメールアドレスをエイリアス名とするユーザーエイリアスを作成する。

## この統合を使う

アカウントを接続すると、何もしなくても自動的にExtoleからBrazeにイベントが流れ始める。Braze に送信されるイベントのライブビューは、Extole の Outbound Webhook Center でトラブルシューティングのために参照できます。 

