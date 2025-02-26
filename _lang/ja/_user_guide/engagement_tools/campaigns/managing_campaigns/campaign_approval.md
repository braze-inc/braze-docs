---
nav_title: キャンペーンの承認
article_title: キャンペーンの承認
alias: "/campaign_approval/"
page_order: 0
page_type: reference
description: "このページでは、キャンペーンの承認プロセスの概要を説明します。"
tool: Campaigns
---

# キャンペーンの承認

> キャンペーンの承認は、キャンペーンを開始する前にワークフローにレビュープロセスを追加します。この機能は、キャンペーン確認ワークフローのステップで利用可能な状態を追加する。キャンペーンを開始するための各確認事項が承認済みであることを確認できます。

{% alert important %}
APIキャンペーンとトランザクションメールキャンペーンの構築ワークフローでは、キャンペーン承認はサポートされていない。
{% endalert %}

## キャンペーンの承認を有効にする

デフォルトでは、キャンペーンの承認設定はオフになっています。この機能を有効にするには、[**設定**] > [**承認ワークフロー**] に移動します。

{% alert note %}
[古いナビゲーション]({{site.baseurl}}/navigation)を使用している場合、このページは [**設定の管理**] > [**承認ワークフロー**] にあります。
{% endalert %}

## 承認を使用する

キャンペーンの承認を有効にした後は、「キャンペーンを承認および却下」権限が必要になります。この権限は、誰がキャンペーンの承認ステータスを更新できるかを制御します。この権限は、ワークスペースや[チーム]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/)に適用したり、[権限セット]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets)に追加したりすることもできます。

キャンペーン構築ワークフローの「**要約を確認**」ステップで、承認オプションを使用してキャンペーンの次の主要コンポーネントを承認または拒否します: **メッセージ**、**配信**、**ターゲット層**、**コンバージョンイベント**。キャンペーン承認のデフォルト状態は「**承認待ち**」です。なお、キャンペーンのコンポーネントは自己承認することが可能です。

![][1]

各セクションが承認されると、**Launch**ボタンが有効になり、キャンペーンを開始することができる！ 

[1]: {% image_buster /assets/img_archive/campaign_approval_example.png %} 
