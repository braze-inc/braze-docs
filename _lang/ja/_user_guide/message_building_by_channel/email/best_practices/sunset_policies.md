---
nav_title: 日没政策
article_title: 電子メールのサンセットポリシー
page_order: 8
page_type: reference
description: "この記事では、日没ポリシーを取り巻くベストプラクティスと、解放されたユーザへのメッセージを停止した方が良い状況を理解する方法について説明します。"
channel: email

---

# 日没政策

> キャンペーンをできるだけ多くのユーザに送ろうとする誘惑に駆られるかもしれませんが、実際には、解放されたユーザへのメッセージを停止することが有利な状況があります。 

メールの場合、送信IP には、エンゲージメント、スパムレポート、ブロックリストなどの要因となるレピュテーションスコアがあります。[Sender](https://www.senderscore.org/ "Sender")または[Outlook's Smart Network Data Service](https://postmaster.live.com/snds/ "Outlook's Smart Network Data Service")のようなツールを使用して、レピュテーションスコアを監視できます。レピュテーションスコアが一貫して低い場合、ISP とメールボックスフィルタは、すべての受信者(参加している受信者も含む)に対して、自動的にメールをスパムまたは低優先度フォルダにソートします。サンセットポリシーを作成すると、有効な受信者にのみメールを配信できます。 

セグメンテーションフィルタを使用すると、メール、プッシュ、アプリ内通知のサンセットポリシーを簡単に実装できるため、メッセージがスパムのように表示されないようにすることができます。サンセットポリシーを作成する際に考慮すべき事項を次に示します。

- "unengaged" user とは何ですか? 
- エンゲージメントはクリック、購入、アプリの使用、またはこれらの動作の組み合わせによって定義されていますか? 
- エンゲージメントの経過は、メッセージの送信を停止するのにどのくらい必要ですか?
- セグメントから除外する前に、ユーザーに特別なキャンペーンを配信していただけますか?
- あなたのサンセットポリシーはどのメッセージングチャンネルに適用されますか? 

たとえば、[AppleのMail Privacy Protection (MPP)]({{site.baseurl}}/user_guide/message_building_by_channel/email/mpp/)を選択したユーザーがいる場合、これがメールキャンペーンと配信可能性メトリクスにどのように影響するかを検討し、サンセットポリシーの最適な構成方法を決定します。

キャンペーンにサンセットポリシーを組み込むには、[segment][19] を作成します。これにより、メールをスパムとしてマークしたユーザや、一定期間メッセージとやり取りしたことがないユーザが自動的に除外されます。  

これらのセグメントを設定するには、フィルタドロップダウンの**Marketing Activity** セクションの下にある`Has Marked You As Spam` および`Last Engaged With Message` フィルタを選択します。 

`Last Engaged With Message` フィルタを適用する場合は、ユーザがインタラクションしたかどうか(プッシュ、メール、またはアプリ内通知)、およびユーザが最後にインタラクションした日数を指定します。セグメントを作成した後、[メッセージングチャネル]({{site.baseurl}}/user_guide/message_building_by_channel/)でこのセグメントをターゲットにすることを選択します。

![Segment Details page with the filter "Last Engaged with Message" selected.][20]

Braze は、スパムとしてマークしたユーザへのメールの送信を自動的に停止しますが、`Has Marked You As Spam` フィルタを使用すると、これらのユーザに対象を絞ったプッシュメッセージとアプリ内通知を送信することもできます。このフィルタは、[キャンペーンのターゲット変更][21] に役立ちます。たとえば、機能を思い出させたり、メールを開いていないときに表示されなくなってしまったことを伝えるメッセージを、管理されていないユーザーに送信できます。

Sunset ポリシーは、失効しているユーザーを対象としたメールキャンペーンで特に役立ちます。これらのキャンペーンは、一定期間アプリとやり取りしたことがないセグメントに焦点を当てていますが、未設定の受信者を繰り返し含めると、メールの配信可能性が危険にさらされます。Sunset ポリシーを使用すると、スパムフォルダにランディングせずにユーザーを失効させることができます。

[19]: {{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#creating-a-segment
[20]: {% image_buster /assets/img_archive/email_sunset_policies_new.png %}
[21]: {{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/retargeting_campaigns/#retargeting-campaigns
