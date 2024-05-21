---
nav_title: "簡単な調査"
article_title: シンプルなアンケートアプリ内メッセージ
page_order: 1.5
page_type: reference
description: "このリファレンス記事では、アプリ内メッセージアンケートを使用して、ユーザーの属性、インサイト、嗜好を収集し、キャンペーン戦略を強化する方法について説明します。"
channel:
  - in-app messages
tool:
  - Templates
---

# 簡単な調査

> **Simple Survey**アプリ内メッセージテンプレートを使用して、キャンペーン戦略に役立つユーザー属性、インサイト、嗜好を収集します。 

たとえば、アプリの使用方法をユーザーに尋ねたり、個人の好みを確認したり、特定の機能に対する満足度を尋ねたりします。

![Three simple survey messages: notification preferences, dietary preferences, and a customer satisfaction survey. The selected options in the surveys correspond to custom attributes that will be logged for that user.]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK の要件 {#supported-sdk-versions}

このアプリ内メッセージは、 [Flex CSS](https://caniuse.com/flexbox) をサポートするデバイスにのみ配信され、少なくとも次の [SDK バージョン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)が必要です。 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Web SDK を使用して HTML アプリ内メッセージを有効にするには、Braze に初期化オプションを指定する `allowUserSuppliedJavascript` 必要があります。
{% endalert %}

## アンケートの作成 {#create}

[アプリ内メッセージ][1]を作成する場合は、**メッセージタイプ**に**「簡易アンケート」**を選択します。

![\]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:80%"}

この調査テンプレートは、モバイル アプリと Web ブラウザーの両方でサポートされています。SDK が、この機能に必要な [最小 SDK バージョン](#supported-sdk-versions) であることを確認してください。

### ステップ 1:アンケートの質問を追加する

アンケートの作成を開始するには、アンケートの **ヘッダー** フィールドに質問を追加します。必要に応じて、アンケートの質問の下に表示される **オプションの [本文** ] メッセージを追加できます。

![Compose tab of the simple survey editor, with fields for a header, optional body, and optional helper text.]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:80%"}

{% alert tip %}
これらのフィールドには、Liquidと絵文字の両方を含めることができるので、凝り固まってください。
{% endalert %}

### ステップ 2:単一選択または複数選択のいずれかを選択 {#single-multiple-choice}

**[単一選択**] または **[複数選択**] を使用して、ユーザーが 1 つの選択肢のみを選択できるか、複数の選択肢を選択できるかを制御します。アンケートには最大 12 個の選択肢を追加できます。

![Choices dropdown with "Multiple-choice selection" selected.]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:60%"}

{% alert tip %}
**単一選択**と**複数選択**を切り替えると、**ヘルパー テキスト**が自動的に更新され、選択できる選択肢の数がユーザーに通知されます。
{% endalert %}

### ステップ 3:カスタム属性の収集 {#custom-attributes}

「 **送信時に属性をログに記録** する」を選択して、ユーザーの送信に基づいて属性を収集します。このオプションを使用して、新しいセグメントとリターゲティングキャンペーンを作成できます。たとえば、満足度アンケートでは、満足度の低いすべてのユーザーにフォローアップメールを送信できます。

![Choices dropdown with "Log attributes upon submission" selected.]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

各選択肢にカスタム属性を追加するには、ドロップダウンメニューからカスタム属性名を選択(または新しい属性を作成)し、この選択肢が送信されたときに設定する値を入力します。新しいカスタム属性は、 [設定ページで][5]作成できます。

たとえば、通知設定アンケートでは、各選択肢をブール値(true/false)属性にして、ユーザーが関心のあるトピックを選択できるようにすることができます。ユーザーが [プロモーション] を選択すると、カスタム属性`Promotions Topic`が に`true`設定された[ユーザー プロファイル][3]が更新されます。選択をオフのままにすると、同じ属性は変更されません。

![\]({% image_buster /assets/img/iam/iam-survey3.png %}){: style="max-width:60%"}

次に、ユーザーの `Promotions Topic = true` セグメントを作成して、プロモーションに関心のあるユーザーのみが関連するキャンペーンを受け取るようにすることができます。

{% alert important %}
カスタム属性の収集が有効な場合、同じカスタム属性名を共有する選択肢は配列に結合されます。
{% endalert %}

#### カスタム属性データ型

カスタム属性のデータタイプは、アンケートの設定方法によって異なります。

- **多肢選択:**カスタム属性のデータ型は配列である必要があります。カスタム属性が別のデータ型に設定されている場合、応答はログに記録されません。
- **単一選択:**カスタム属性のデータ型は配列であって _はなりません_ 。属性が配列の場合、応答はログに記録されません。

#### 応答のみのログ記録

または、 **応答のみをログに記録する(属性なし)**を選択することもできます。このオプションを選択すると、アンケートの回答はボタンのクリックとして記録されますが、カスタム属性はユーザーのプロファイルに記録されません。つまり、各アンケートオプションのクリック指標は引き続き表示できますが( [アナリティクス](#analytics)を参照)、その選択はユーザープロフィールには反映されません。

これらのクリック指標は、リターゲティングには使用できません。

### ステップ 4: 送信動作の選択

ユーザーが応答を送信したら、必要に応じて確認ページを表示するか、単にメッセージを閉じることができます。

確認ページは、ユーザーの時間に感謝したり、追加情報を提供したりするのに最適な場所です。このページの行動を促すフレーズをカスタマイズして、ユーザーをアプリやウェブサイトの別のページに誘導できます。

ボタンのテキストとクリック時の動作は、アンケートの下部にある **[送信ボタン** ]セクションで編集します **。** tab:

![On-click behavior set to "Submit responses and display confirmation page".]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

確認ページを追加する場合は、[ **確認ページ** ] タブに切り替えてメッセージをカスタマイズします。

![Confirmation Page tab of the simple survey editor. The available fields are header, optional body, button text, and button on-click behavior.]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:80%"}

ユーザーをアプリやウェブサイトの別のページに誘導する場合は、ボタンの [ **クリック時] の動作**を変更します。

### ステップ 5: メッセージのスタイルを設定する(オプション) {#styling}

メッセージのフォントの色とアクセントカラーは、 **カラーテーマ** ピッカーを使用してカスタマイズできます。

![Compose tab of the simple survey editor with the Color Theme picker expanded after a user has clicked on the color palette.]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## 結果の分析 {#analytics}

キャンペーンが開始されると、結果をリアルタイムで分析して、選択した各選択肢の内訳を確認できます。[カスタム属性の収集](#custom-attributes)を有効にしている場合は、アンケートを送信したユーザーに対して新しいセグメントやフォローアップキャンペーンを作成することもできます。

{% alert note %}
削除されたアンケートの選択肢は引き続きアナリティクスに表示されますが、新しいユーザーには選択肢として表示されません。
{% endalert %}

アンケート指標の定義については、 [レポート指標の用語集][11] を参照し、「アプリ内メッセージ」でフィルタリングしてください。

![In-app message performance panel with click analytics for each choice and button on the survey.]({% image_buster /assets/img/iam/iam-survey-analytics.png %}){: style="max-width:95%"}

キャンペーン指標の内訳については、 [アプリ内メッセージレポート][4] をご覧ください。

### 電流 {#currents}

選択した選択肢は、Currents の [[**アプリ内メッセージのクリックイベント**][6]`button_id`] フィールドに自動的に転送されます。各選択肢は、その汎用一意識別子 (UUID) とともに送信されます。

## ユースケース

### ユーザー満足度

**ゴール：**顧客満足度を測定し、スコアの低いユーザーにウィンバックキャンペーンを送信します。

このユースケースでは、「非常に不満」から「非常に満足」までの範囲の選択肢で、単一選択を使用します。各選択肢には、1 から 5 までの数値が設定されたカスタム属性 `customer_satisfaction` があり、1 が最も満足度が低く、5 が最も満足度が高いことを示します。

アンケートを開始したら、「非常に不満」または「不満」と回答したユーザー(1または2に設定したユーザー `customer_satisfaction` )をウィンバックキャンペーンのターゲットにすることができます。

![][7]

### 顧客目標の特定

**ゴール：**ユーザーがアプリにアクセスする主な理由を特定する。

このユースケースでは、単一選択を使用し、各選択肢がユーザーがアプリにアクセスする一般的な理由です。各選択肢には、ユースケーストピックに設定されたカスタム属性 `product_goal` があります。 

たとえば、ユーザーが「アカウントのアップグレード」を選択すると、ユーザーの `product_goal = upgrade` プロファイルに設定されます。

![][8]

### コンバージョン率の向上

**ゴール：**顧客がアップグレードや購入をしない理由を理解します。

このユースケースでは、単一選択を使用し、各選択肢がユーザーがプレミアムアカウントにアップグレードしない一般的な理由です。各選択肢には、ユーザーの選択に設定されたカスタム属性 `upgrade_reason` があります。 

たとえば、ユーザーが「高すぎる」を選択すると、ユーザーの `upgrade_reason = expensive` プロファイルに設定されます。これらのユーザーをターゲットにして、割引や無料トライアルなどのプロモーション キャンペーンを行うことができます。

![][9]

### お気に入りの機能

**ゴール：**顧客がどの機能を楽しんで使用しているかを把握します。

このユースケースでは、各選択肢をアプリの機能として、複数選択式を選択します。各選択肢には、ユーザーの選択に設定されたカスタム属性 `favorite_features` があります。このユースケースには多選択式が含まれるため、ユーザーがアンケートを完了すると、選択したすべてのオプションの配列に設定された属性で `favorite_features` プロファイルが更新されます。

![][10]

[1]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types
[3]: {{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/reporting/
[5]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/managing_custom_data
[6]: {{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/#api_fzzdoylmrtwe

[7]: {% image_buster /assets/img_archive/simple_survey_use_case_1.png %}
[8]: {% image_buster /assets/img_archive/simple_survey_use_case_2.png %}
[9]: {% image_buster /assets/img_archive/simple_survey_use_case_3.png %}
[10]: {% image_buster /assets/img_archive/simple_survey_use_case_4.png %}

[11]: {{site.baseurl}}/user_guide/data_and_analytics/report_metrics/
