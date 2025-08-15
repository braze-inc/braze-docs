---
nav_title: Inbox Monster
article_title: Inbox Monster
alias: /partners/inbox_monster/
description: "この参考記事では、BrazeとオンラインメールマーケティングツールInbox Monsterのパートナーシップについて概説している。Inbox Monsterは、Brazeの顧客が受信トレイのパフォーマンスを向上させるための強力な配信インサイトとクリエイティブ分析を可能にするツールである。"
page_type: partner
search_tag: Partner

---

# Inbox Monster

> [Inbox Monster](https://inboxmonster.com/) は、企業ブランドがすべての送信を成功させるためのインボックスシグナルプラットフォームです。これは、最新のカスタマーリレーションシップマネジメント (CRM) チームを強化し、送信の不安を解消する、配信可能性、クリエイティブなレンダリング、SMS 監視のための統合ソリューションスイートです。

Braze と Inbox Monster の統合により、手動でのシードリストのテストを排除し、強力で実用的な受信トレイ配置シグナルの作成を自動化し、メールのクリエイティブアセットのレビューと承認のプロセスを簡素化し、配信可能性に関する貴重なインサイトを取得できます。また、クリエイティブな診断やデバイスプレビュー用のメールテンプレートをシームレスにインポートすることもできる。

## 前提条件

| 必要条件                    | 説明                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Inbox Monster プラットフォームアカウント | このパートナーシップを活用するには、Inbox Monster  プラットフォームアカウントが必要です。                                                                                                                                                                                                                                                                                                                                                                 |
| Braze REST API キー             | 以下の権限を持つBraze REST APIキー： <br> - `messages.send`<br>  - `templates.email.create`<br> - `templates.email.update`<br> - `templates.email.info`<br> - `templates.email.list`<br><br> そして、以下のホワイトリストに登録されたipを持つ：<br> - `3.136.16.19`<br>  - `3.140.233.31`<br> - `18.220.127.138`<br><br> これは、Braze ダッシュボードの [**設定**] > [**API と識別子**] の [**API キー**] タブで作成できます。 |
| Brazeアプリの識別子           | Brazeアプリ識別子。<br><br>これはダッシュボードの [**設定**] > [**API と識別子**] の [**アプリ識別子**] タブで確認できます。                                                                                                                                                                                                                                                                                                |
| Braze エンドポイント                 | [あなたのBraze エンドポイント]({{site.baseurl}}/api/basics/#endpoints)はあなたのBraze ダッシュボード URLに合わせます。<br><br> たとえば、ダッシュボード URL が`https://dashboard-03.braze.com` の場合、エンドポイントは`dashboard-03` になります。                                                                                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## 統合

Inbox Monster を統合するには、[Inbox Monster との統合](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_80147afaf3)のステップに従います。

## 使用

Inbox Monster を介してスケジュール受信トレイ配置テストを送信する方法については、[スケジュールされた受信トレイ配置テスト](https://intercom.help/inbox-monster/en/articles/9518204-scheduled-placement-tests-with-braze#h_7e74bc474e)を参照してください。
