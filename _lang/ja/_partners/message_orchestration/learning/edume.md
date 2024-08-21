---
nav_title: エデュメ
article_title: エデュメ
description: "このリファレンス記事では、Brazeと、モバイルベースのトレーニングリングツールであるeduMeとの提携について概説します。これにより、Brazeコネクテッドコンテンツを活用して、ユーザーがあなたのBraze キャンペーンの中のeduMe講座やレッスンを利用できるようになります。"
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# エデュメ

> [eduMe](https://edume.com) は、モバイルベースのトレーニングリングツールで、必要なときに、成功するために必要な知識を、どこにいても、従業員に提供します。 

Braze とeduMe の統合は、Braze [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) を活用して、ユーザーがあなたのBraze キャンペーン s のeduMe コースとレッスンを利用できるようにします。個々のプログレスとグループプログレスは、eduMe レポートの機能を通じて追跡できます。

## 前提条件

| 要件 | 説明 |
|---|---|
| eduMeアカウント | この提携の前進タグeを考慮するためには、eduMeの勘定が必要である。 |
| エデュメAPI キー | API キーは、eduMe 顧客の成功連絡先にリクエストする必要があります。この鍵は、Braze接続内容呼び出しで使用されます。 |
| eduMeリンク署名シークレット | 組織のリンクサインシークレットを設定するには、eduMe で顧客成功コンタクトをリクエストする必要があります。このシークレットは、接続コンテンツでシームレスなリンクを有効にするために使用されます。この秘密は何もする必要はありません。 |
| eduMeグループとコンテンツID | これらの識別子は、接続コンテンツコールの設定に必要です。これらの識別子の入手方法については、eduMe 顧客の担当者までお問い合わせください。 |
{: .reset-td-br-1 .reset-td-br-2}

## 統合

### 接続コンテンツコールの作成

コース、レッスン、またはeNPS 調査をユーザーに利用できるようにし、eduMe の内部 ユーザー IDに対する進行状況を追跡するには、次の例に示すAPI 呼び出しに従います。

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
2. `EDUME-CONTENT-LINK-AND-CONTENT-ID` を、対応するコンテンツリンク文字列とモジュール、レッスン、または調査 識別子に置き換えます。これらの識別子s は、あなたのeduMe アカウントにあります。
  - コース: `getCourseLink?moduleId=12087`
  - 教訓: `getLessonLink?lessonId=25805`
  - eNPS調査: `getSurveyLink?surveyId=654`<br><br>
3. このリンクを通じてeduMeに到着したユーザーは、選択したeduMeチームまたはグループに追加されます。`groupId` を関連するチームID またはeduMe グループID に置き換えます。通常、チームID を使用しますが、登録が必要なコースはグループID を使用する必要があります<br><br>
4. `externalUserId` フィールドをマップするアプリの適切なフィールドを含めます。コネクテッドコンテンツ呼び出しの例では、`driver_id` を使用しますが、フィールドは異なっている可能性があります。このID はeduMe レポート s で利用でき、システムと関連付けることができます。<br><br>
5. 最後に、必要に応じてメッセージをカスタマイズしてテストします。少なくとも1つのテストメッセージを送信し、eduMeコンテンツにアクセスし、レッスンまたはコースを完了し、eduMe 分析が記録されていることを確認することをお勧めします。 
