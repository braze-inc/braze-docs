---
nav_title: eduMe
article_title: eduMe
description: "このリファレンス記事では、Braze と eduMe のパートナーシップについて説明します。eduMe はモバイルベースのトレーニングツールであり、Braze コネクテッドコンテンツを利用して、ユーザーが Braze キャンペーンで eduMe のコースやレッスンにアクセスできるようにします。"
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# eduMe

> [eduMe](https://edume.com)はモバイルベースのトレーニングツールであり、従業員はどこからでも必要なときに、成功するために必要な知識を習得できます。 

_この統合は、eduMe によって管理されます。_

## 統合について

Braze と eduMe の統合では、Braze [コネクテッドコンテンツ]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content)を利用して、ユーザーが Braze キャンペーンで eduMe のコースやレッスンにアクセスできるようにします。個人とグループの進捗状況は、eduMe レポート機能で追跡できます。

## 前提条件

| 必要条件 | 説明 |
|---|---|
| eduMeアカウント | このパートナーシップを活用するには、eduMe アカウントが必要です。 |
| eduMe API キー | eduMe のカスタマーサクセス担当者に API キーを依頼する必要があります。このキーは、Brazeコネクテッドコンテンツの呼び出しで使用される。 |
| eduMeリンク署名シークレット | eduMe のカスタマーサクセス担当者に組織のリンク署名シークレットの設定を依頼する必要があります。このシークレットは、接続コンテンツでシームレスなリンクを有効にするために使用されます。この秘密で何かをする必要はない。 |
| eduMeグループとコンテンツID | これらの識別子は、コネクテッドコンテンツ呼び出しを設定する際に必要です。これらの識別子の入手については、EduMeの顧客サービス窓口に問い合わせること。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## 統合

### コネクテッドコンテンツ呼び出しを作成する

ユーザーがコース、レッスン、eNPS アンケートを利用できるようにし、eduMe で内部ユーザー ID を使用してユーザーの進捗状況を追跡するには、次の例に示す API 呼び出しに従います。

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

1. `YOUR-EDUME-API-KEY` をeduMe API キーに置き換えます。<br><br>
2. `EDUME-CONTENT-LINK-AND-CONTENT-ID` を、対応するコンテンツリンク文字列とモジュール、レッスン、または調査 識別子に置き換えます。これらの識別子は、eduMe アカウントで確認できます。
  - コース: `getCourseLink?moduleId=12087`
  - レッスン: `getLessonLink?lessonId=25805`
  - eNPS アンケート: `getSurveyLink?surveyId=654`<br><br>
3. このリンクを通じてEduMeに到着したユーザーは、選択したEduMeチームまたはグループに追加される。`groupId` を関連するチームID またはeduMe グループID に置き換えます。履修登録が必要なコースを除き、通常はチームIDを使用するが、その場合はグループIDを使用する。<br><br>
4. `externalUserId` フィールドのマッピング先として適切なフィールドを含めます。コネクテッドコンテンツ呼び出しの例では、`driver_id` を使用しますが、フィールドは異なっている可能性があります。このIDはEduMeのレポートで利用可能で、システムとの関連付けができる。<br><br>
5. 最後に、必要に応じてメッセージをカスタマイズしてテストします。少なくとも1つのテストメッセージを送信し、eduMe コンテンツにアクセスし、レッスンまたはコースを修了し、eduMe 分析が記録されていることを確認することをお勧めします。 

