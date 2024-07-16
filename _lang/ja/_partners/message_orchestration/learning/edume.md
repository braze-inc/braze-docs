---
nav_title: eDume
article_title: eDume
description:「この参考記事では、BrazeとeDumeのパートナーシップについて概説しています。eDumeは、Braze Connected Contentを活用して、ユーザーがBrazeキャンペーンのeDumeコースやレッスンにアクセスできるようにするモバイルベースのトレーニングツールです。「
alias: /partners/edume/
page_type: partner
search_tag:Partner

---

# eDume

> [eDumeはモバイルベースのトレーニングツールで、どこにいても](https://edume.com)、必要なときに必要な知識を従業員に提供します。 

BrazeとeDumeの統合では、[Brazeコネクテッドコンテンツを活用して]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)、ユーザーがBrazeキャンペーンのeDumeコースやレッスンにアクセスできるようにします。その後、eDumeレポート機能を使用して個人およびグループの進捗状況を追跡できます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| eDume アカウント | このパートナーシップを利用するには、eDumeアカウントが必要です。 |
| デュム API キー | eDume 顧客サクセス連絡先に API キーをリクエストする必要があります。このキーは Braze コネクテッドコンテンツ通話で使用されます。 |
| eDume リンク署名シークレット | 組織のリンク署名シークレットを設定するには、eDumeの顧客サクセス担当者に依頼する必要があります。このシークレットは、コネクテッドコンテンツでシームレスリンクを有効にするために使用されます。この秘密を使って何もする必要はありません。 |
| eDume グループとコンテンツ ID | これらの識別子は、コネクテッドコンテンツ通話を設定するために必要です。これらの識別子の取得については、eDume顧客サービスの連絡先にお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### コネクテッドコンテンツ通話を作成

ユーザーにコース、レッスン、またはENP調査へのアクセスを許可し、eDumeの内部ユーザーIDと照合して進捗状況を追跡するには、次の例に示すAPI呼び出しに従ってください。

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. お使いの eDume API `YOUR-EDUME-API-KEY` キーに置き換えてください。<br><br>
2. を、`EDUME-CONTENT-LINK-AND-CONTENT-ID`対応するコンテンツリンク文字列とモジュール、レッスン、または調査識別子に置き換えます。これらの識別子はeDumeアカウントにあります。
  - Course: `getCourseLink?moduleId=12087`
  - Lesson: `getLessonLink?lessonId=25805`
  - ENPs調査: `getSurveyLink?surveyId=654`<br><br>
3. このリンクからeDumeにアクセスしたユーザーは、選択したeDumeチームまたはグループに追加されます。該当するチーム ID または eDume グループ ID `groupId` に置き換えてください。登録が必要なコースを除き、通常はチームIDを使用します。登録が必要なコースの場合は、グループIDを使用してください<br><br>
4. `externalUserId`フィールドをマップする適切なフィールドを含めます。コネクテッドコンテンツコールの例ではを使用していますが`driver_id`、フィールドは異なる可能性があります。このIDはeDumeレポートに表示され、システムと関連付けることができます。<br><br>
5. 最後に、必要に応じてメッセージをカスタマイズしてテストします。少なくとも1つのテストメッセージを送信し、eDumeコンテンツにアクセスし、レッスンまたはコースを完了し、eDume分析が記録されていることを確認することをお勧めします。 
