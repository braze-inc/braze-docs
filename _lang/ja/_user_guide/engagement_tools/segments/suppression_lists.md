---
nav_title: 抑制リスト
article_title: 抑制リスト
page_order: 3
page_type: reference
tool: Segments
description: "このページでは、抑制リストを使用して、メッセージを受信しないユーザを指定する方法について説明します。"

---

# 抑制リスト

> 除外リストは、自動的にキャンペーンやキャンバスを受信しないユーザーのグループです。除外リストはSegment フィルターs で定義され、ユーザーs はフィルター基準を満たすときに除外リストに入り、終了します。また、除外タグs を設定して、除外一覧がこれらのタグs でsまたはキャンバスをアプリしないようにすることもできます。キャンペーン s またはキャンバスからのメッセージ(例外タグs を除く) は、ターゲットSegments にあるサプレッションリストユーザーに到達します。

## 抑制リストを使用する理由

除外リストはダイナミックなで、すべての形式のメッセージングに自動的にアプリされますが、選択したタグに除外を設定できます。選択した例外タグがキャンペーンまたはキャンバスで使用されている場合、その抑制リストはそのキャンペーンまたはキャンバスには適用されません。キャンペーンまたは例外タグを含むキャンバスからのメッセージは、ターゲットセグメントの一部である抑制リストユーザーに到達します。

### 除外リストの影響を受けるメッセージの種類とチャネル

除外リストは、[フィーチャーフラグs]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/feature_flags/)を除くすべてのメッセージタイプとチャネルsにアプリします。つまり、サプレッションリストは、以下を含むすべてのチャネルs、キャンペーンs、およびキャンバスにデフォルト アプリで表示されます。
- [APIキャンペーン]({{site.baseurl}}/api/api_campaigns/)
- API によりトリガーされるキャンペーンとキャンバス
- [トランザクションメール]({{site.baseurl}}/user_guide/message_building_by_channel/email/transactional_message_api_campaign/)

除外リストがアプリしない唯一のメッセージ種別は、フィーチャーフラグ s です。サプレッションリスト内のユーザはフィーチャーフラグs からは除外されず、他のすべてのチャネルs から除外されます。 

除外タグs を使用して、除外リストユーザーs を特定のキャンペーンおよびキャンバスがターゲットにすることができます。詳しくは、[抑止リストの設定](#setup)のステップ 4を参照してください。除外タグs を除外リストに追加しない場合、除外リスト内のユーザーs は、フィーチャーフラグs 以外のメッセージングの対象になりません。 

{% alert note %}
除外リストは、`campaign_id` でBraze ダッシュボード内に作成されたAPI キャンペーンs にアプリされます。除外リストは、関連付けられた`campaign_id`なしで[Braze メッセージング エンドポイント s]({{site.baseurl}}/api/endpoints/messaging/)経由で送信されたメッセージにはアプリしません。
{% endalert %}

<<<<<<< HEAD
!["Exception Settings" にチェックボックスを付けて、抑制一覧をAPI-トリガー ed キャンペーン s およびキャンバスにアプリしないようにします。]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}
=======
\!["Exception Settings" にチェックボックスを付けて、抑制一覧をAPI-トリガー ed キャンペーン s およびキャンバスにアプリしないようにします。]({% image_buster /assets/img/suppression_list_checkbox.png %}){: style="max-width:70%;"}
>>>>>>> main

## サプレッションリストの設定 {#setup}

{% alert note %}
すべてのユーザーs はサプレッションリストを表示できますが、[admin permissions]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/?tab=admin#list-of-permissions) を持つユーザーs のみがサプレッションリストを作成および管理できます。
{% endalert %}

<<<<<<< HEAD
1. [**オーディエンス**] > [**抑制リスト**] に移動します。<br><br>!["Suppression Lists"ページ。3つの抑制リストのリストがあります。]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. **抑制リストの作成**を選択し、名前を追加します。<br><br>![&quot と呼ばれるウィンドウ;除外リスト&クォートを作成します。名前を入力するフィールドがあります。]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
=======
1. [**オーディエンス**] > [**抑制リスト**] に移動します。<br><br>\!["Suppression Lists"ページ。3つの抑制リストのリストがあります。]({% image_buster /assets/img/suppression_lists_home.png %})<br><br>
2. **抑制リストの作成**を選択し、名前を追加します。<br><br>\![&quot と呼ばれるウィンドウ;除外リスト&クォートを作成します。名前を入力するフィールドがあります。]({% image_buster /assets/img/create_suppression_list.png %}){: style="max-width:80%;"}<br><br>
>>>>>>> main
3. セグメントフィルタを使用して、抑制リスト内のユーザを識別します。少なくとも1 つを選択する必要があります。

{% alert important %}
設定プロセスは[セグメント作成]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/)と似ていますが、抑制リストは**do not**がセグメントメンバーシップに関係なくメッセージを送信したいユーザのグループです。
{% endalert %}

<<<<<<< HEAD
![最後の開封が90日間以上前にメールしたユーザー sのフィルターを持つサプレッションリストビルダー。]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4\.セグメント名の下にあるボックスをチェックして、タグに基づいて例外を設定するかどうかを決定します(詳細については、[抑制リストを使用する理由?](#why-use-suppression-lists)を参照してください)。次に、この抑制リストのユーザがまだ受信すべきキャンペーンまたはキャンバスのタグを追加します。<br><br>つまり、例外タグ「配送確認」を追加すると、抑制リスト内のユーザーは、タグ「配送確認」を使用するユーザーを除き、すべてのメッセージングから除外されます。<br><br>![The "Shipping List Details" section with an exception タグ アプリlied called "Shipping confirmation".]({% image_buster /assets/img/exception_tags.png %})<br><br>
=======
\![最後の開封が90日間以上前にメールしたユーザー sのフィルターを持つサプレッションリストビルダー。]({% image_buster /assets/img/suppression_list_filters.png %})

{: start="4"}
4\.セグメント名の下にあるボックスをチェックして、タグに基づいて例外を設定するかどうかを決定します(詳細については、[抑制リストを使用する理由?](#why-use-suppression-lists)を参照してください)。次に、この抑制リストのユーザがまだ受信すべきキャンペーンまたはキャンバスのタグを追加します。<br><br>つまり、例外タグ「配送確認」を追加すると、抑制リスト内のユーザーは、タグ「配送確認」を使用するユーザーを除き、すべてのメッセージングから除外されます。<br><br>\![The "Shipping List Details" section with an exception タグ アプリlied called "Shipping confirmation".]({% image_buster /assets/img/exception_tags.png %})<br><br>
>>>>>>> main
5. 抑制リストを保存または有効化します。
- 保存すると、抑制リストは保存されますが、アクティブにはなりません。つまり、有効にはなりません。サプレッションリストはアクティブにするまで非アクティブのままになり、非アクティブなサプレッションリストはメッセージングに影響を与えません(ユーザーはメッセージから除外されません)。
- 有効にすると、抑制リストが保存され、すぐに有効になります。つまり、抑制リスト内のユーザは、すぐにキャンペーンまたはキャンバスから除外されます(例外タグを含むユーザを除く)。

{% alert note %}
管理者のみが抑制リストを保存または有効化できます。ベータには、一度に最大5 つのアクティブサプレッションリストを含めることができます。
{% endalert %}

抑制リストは、不要になった時点で非アクティブ化またはアーカイブできます。 
- 無効にするには、アクティブな抑制リストを選択し、**Deactivate** を選択します。非アクティブにされた抑制リストは、後で再びアクティブ化できます。
- アーカイブするには、**Suppression Lists** ページから行います。

## 抑制リストの使用

抑制リストでユーザがメッセージを受信できないかどうかを確認するには、キャンペーンまたはキャンバス内の**Target Audience** ステップで**User Lookup** を使用します。ここでは、ユーザーがどの抑制リストに含まれているかを確認できます。

<<<<<<< HEAD
![" ユーザー Lookup" ユーザーがサプレッションリストにあることを示すウィンドウ。]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}
=======
\![" ユーザー Lookup" ユーザーがサプレッションリストにあることを示すウィンドウ。]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}
>>>>>>> main

{% alert tip %}
適用された抑制リストは、[**要約**] ステップにも表示されます。
{% endalert %}

キャンペーンまたはキャンバスの作成中に、**ユーザールックアップ**を**ターゲットオーディエンス**ステップ内で使用してユーザーを検索し、それらがターゲットオーディエンスに存在しない場合は、それらが含まれている抑制リストを確認できます。 

<<<<<<< HEAD
![" ユーザー Lookup" ユーザーがサプレッションリストにあることを示すウィンドウ。]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}
=======
\![" ユーザー Lookup" ユーザーがサプレッションリストにあることを示すウィンドウ。]({% image_buster /assets/img/suppression_list_user_lookup.png %}){: style="max-width:70%;"}
>>>>>>> main

### キャンペーン 

ユーザが抑制リストに含まれている場合、その抑制リストが適用されるキャンペーンは受信されません。除外リストがアプリしない場合については、[除外リストの影響を受けるメッセージの種類とチャネル](#message-types-and-channels-affected-by-suppression-lists)を参照してください。

<<<<<<< HEAD
!["Suppression Lists" セクション。&quot と呼ばれる1 つのアクティブなサプレッションリストがあります。マーケティングヘルススコア&クォートが低くなります。]({% image_buster /assets/img/active_suppression_list.png %})
=======
\!["Suppression Lists" セクション。&quot と呼ばれる1 つのアクティブなサプレッションリストがあります。マーケティングヘルススコア&クォートが低くなります。]({% image_buster /assets/img/active_suppression_list.png %})
>>>>>>> main

### キャンバス 

ユーザーが除外リストに追加された時点から、キャンバスには入りません。すでにキャンバスに入っている場合は、メッセージステップは受信されません。つまり、除外リストに追加されたユーザーがすでにキャンバス内にある場合、次回のメッセージステップまでキャンバスを進み、その時点でメッセージステップを受信せずにキャンバスを終了します。 

たとえば、キャンバスにユーザアップデートステップがあり、その後にメッセージステップがあるとします。ユーザーがキャンバスに入り、サプレッションリストに追加された場合でも、そのユーザーはユーザー 更新 ステップを通過し(ここでは更新 d)、メッセージステップで終了します。この時点で、終了したメトリクスに含まれます。
