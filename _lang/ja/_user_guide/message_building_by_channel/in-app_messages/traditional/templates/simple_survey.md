---
nav_title: "シンプルな調査"
article_title: シンプルな調査のアプリ内メッセージ
page_order: 1.5
page_type: reference
description: "このリファレンス記事では、アプリ内メッセージアンケートを使用して、ユーザー属性、インサイト、および好みを収集し、キャンペーン戦略を強化する方法について説明します。"
channel:
  - in-app messages
tool:
  - Templates
---

# シンプルな調査

> **シンプル調査**アプリ内メッセージテンプレートを使用して、ユーザー属性、インサイト、および好みを収集し、キャンペーン戦略を強化します。 

たとえば、ユーザーにアプリの使い方について尋ねたり、個人的な好みについて詳しく聞いたり、特定の機能に対する満足度について尋ねたりすることができます。

![通知の好み、食事の好み、および顧客満足度調査の 3 つのシンプルな調査のメッセージ。アンケートで選択されたオプションは、そのユーザーについて記録されるカスタム属性に対応します。]({% image_buster /assets/img/iam/iam-survey.png %})

## SDK 要件 {#supported-sdk-versions}

このアプリ内メッセージは、[Flex CSS](https://caniuse.com/flexbox)をサポートするデバイスにのみ配信され、少なくとも次の[SDKバージョン]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions)が必要です。 

{% sdk_min_versions ios:3.23.0 android:8.0.0 web:2.5.0 %}

{% alert note %}
Web SDK を介して HTML アプリ内メッセージを有効にするには、初期化オプション `allowUserSuppliedJavascript` を Braze に指定する必要があります。
{% endalert %}

## 調査の作成{#create}

[アプリ内メッセージ][1]を作成する際は、**シンプル調査**を**メッセージタイプ**として選択してください。

![]({% image_buster /assets/img/iam/survey-message-type.png %}){: style="max-width:80%"}

この調査テンプレートは、モバイルアプリと Web ブラウザーの両方でサポートされています。必ず、使用している SDK が、この機能に必要な[SDK の最小バージョン](#supported-sdk-versions)以降であることを確認してください。

### ステップ 1:調査の質問の追加

調査の作成を開始するには、質問を調査の [**ヘッダー**] フィールドに追加します。必要に応じて、調査の質問の下に表示されるオプションの**本文**メッセージを追加できます。

![シンプルな調査エディターの [作成] タブ。ヘッダー、オプションの本文、およびオプションのヘルパーテキストのフィールドがあります。]({% image_buster /assets/img/iam/iam-survey2.png %}){: style="max-width:80%"}

{% alert tip %}
これらのフィールドには Liquid と絵文字の両方を含めることができるため、内容を工夫できます。
{% endalert %}

### ステップ 2:単一選択または複数選択{#single-multiple-choice}のいずれかを選択してください

**単一選択**または**複数選択**を使用して、ユーザーが1つの選択肢のみを選択するか、複数の選択肢を選択できるようにコントロールします。調査には最大 12 個の選択肢を追加できます。

![「複数選択肢の選択」が選択された選択肢のドロップダウン。]({% image_buster /assets/img/iam/single-multiple-choice.png %}){: style="max-width:60%"}

{% alert tip %}
あなたの**ヘルパーテキスト**は、**単一選択**と**複数選択**を切り替えると、自動的に更新され、ユーザーが選択できる選択肢の数を知らせます。
{% endalert %}

### ステップ 3:カスタム属性の収集{#custom-attributes}

[**送信時に属性をログに記録する**] を選択し、ユーザーの送信内容に基づいて属性を収集します。このオプションを使用して、新しいセグメントとリターゲティングキャンペーンを作成できます。例えば、満足度調査では、満足していなかったすべてのユーザーにフォローアップのメールを送ることができます。

![[送信時に属性をログに記録する] を選択した選択肢のドロップダウン。]({% image_buster /assets/img/iam/collect-attributes.png %}){: style="max-width:60%"}

各選択肢にカスタム属性を追加するには、ドロップダウンメニューからカスタム属性名を選択（または新しいものを作成）し、この選択肢が送信されたときに設定する値を入力します。[設定ページ][5]で新しいカスタム属性を作成できます。

例えば、通知設定の調査では、各選択肢をブール値（true/false）の属性にして、ユーザーが興味のあるトピックを選択できるようにすることができます。ユーザーが「プロモーション」を選択すると、カスタム属性`Promotions Topic`が`true`に設定された[ユーザープロファイル][3]が更新されます。ユーザーが選択肢をオンにしない場合、その同じ属性は変更されません。

![]({% image_buster /assets/img/iam/iam-survey3.png %}){: style="max-width:60%"}

その後、`Promotions Topic = true`を持つユーザーのためにセグメントを作成して、プロモーションに興味のあるユーザーだけが関連するキャンペーンを受け取るようにすることができます。

{% alert important %}
カスタム属性の収集が有効になっている場合、同じカスタム属性名を共有する選択肢は配列に結合されます。
{% endalert %}

#### カスタム属性のデータ型

カスタム属性のデータ型は、調査の設定方法に応じて重要です。

- **多岐選択:**カスタム属性のデータ型は配列でなければなりません。カスタム属性が異なるデータ型に設定されている場合、応答は記録されません。
- **単一選択:**カスタム属性のデータ型_は_配列であってはなりません。属性が配列の場合、応答は記録されません。

#### 応答のみの記録

あるいは、**応答のみを記録することを選択できます（属性なし）**。このオプションを選択すると、調査の回答はボタンクリックとして記録されますが、カスタム属性はユーザープロファイルに記録されません。つまり、各調査オプションのクリック指標を表示できますが ([分析](#analytics)を参照)、その選択はユーザープロファイルに反映されません。

これらのクリックメトリクスはリターゲティングには利用できません。

### ステップ 4:提出の動作を選択

ユーザーが回答を送信すると、確認ページを表示するか、メッセージを閉じるかを選択できます。

確認ページは、ユーザーの時間に感謝したり、追加情報を提供したりするのに最適な場所です。このページのコールトゥアクションをカスタマイズして、ユーザーをアプリやWebサイトの別のページに誘導できます。

[**調査**] タブの下部にある [**送信ボタン**] セクションで、ボタンのテキストとクリック時の動作を編集します。

![クリック時の動作が「回答を送信して確認ページを表示」に設定されています。]({% image_buster /assets/img/iam/confirmation-option.png %}){: style="max-width:60%"}

確認ページを追加する場合は、メッセージをカスタマイズするために**確認ページ**タブに切り替える:

![シンプルな調査エディターの [確認ページ] タブ。利用可能なフィールドは、ヘッダー、オプションの本文、ボタンテキスト、およびボタンのクリック動作です。]({% image_buster /assets/img/iam/confirmation-page.png %}){: style="max-width:80%"}

アプリやWeb サイトの別のページにユーザーを誘導したい場合は、ボタンの**クリック時の動作**を変更してください。

### ステップ 5: メッセージをスタイリッシュにする（オプション） {#styling}

メッセージのフォントカラーとアクセントカラーは、**カラーテーマ**ピッカーを使用してカスタマイズできます。

![ユーザーがカラーパレットをクリックした後、カラーテーマピッカーが展開されたシンプルな調査エディターの [作成] タブ。]({% image_buster /assets/img/iam/color-theme-picker.png %}){: style="max-width:80%"}

## 結果の分析{#analytics}

キャンペーンの開始後、リアルタイムで結果を分析して、選択した各選択肢の内訳を確認できます。[カスタム属性の収集](#custom-attributes)を有効にしている場合、調査を送信したユーザー向けに新しいセグメントやフォローアップキャンペーンを作成することもできます。

{% alert note %}
削除された調査の選択肢は分析に表示されますが、新しいユーザーには選択肢として表示されません。
{% endalert %}

調査指標の定義については、[レポート指標用語集][11]を参照し、「アプリ内メッセージ」でフィルターしてください。

![調査の各選択肢およびボタンのクリック分析を含む [アプリ内メッセージのパフォーマンス] パネル。]({% image_buster /assets/img/iam/iam-survey-analytics.png %}){: style="max-width:95%"}

[アプリ内メッセージ][4]レポートをチェックして、キャンペーンの指標を確認してください。

### Currents{#currents}

選択したオプションは、[**アプリ内メッセージクリックイベント**][6] `button_id`フィールドの下で自動的にCurrentsに流れます。各選択肢は、その普遍的に一意の識別子（UUID）と共に送信されます。

## ユースケース

### ユーザー満足度

**目的:**顧客満足度を測定し、低評価を残したユーザーにウィンバックキャンペーンを送信します。

このユースケースでは、「非常に不満」から「非常に満足」までの選択肢を持つ単一選択を使用します。各選択肢にはカスタム属性`customer_satisfaction`が1から5の数字に設定されており、1が最も満足していない状態で、5が最も満足している状態です。

調査の開始後、「非常に不満」または「不満」と報告したユーザー、つまり`customer_satisfaction`が 1 または 2 に設定されているユーザーを、奪還キャンペーンのターゲットにすることができます。

![][7]

### 顧客の目的の特定

**目的:**ユーザーがアプリにアクセスする上位の理由を特定します。

このユースケースでは、単一選択を使用します。各選択肢は、ユーザーがアプリを訪れる一般的な理由です。各選択肢には、カスタム属性`product_goal`がユースケースのトピックに設定されています。 

例えば、ユーザーが「アカウントのアップグレード」を選択すると、それがユーザーのプロファイルに`product_goal = upgrade`を設定します。

![][8]

### コンバージョン率を向上させる

**目的:**顧客がアップグレードや購入をしない理由を理解します。

このユースケースでは単一選択を使用し、各選択肢にユーザーがプレミアムアカウントにアップグレードしない一般的な理由を提示します。各選択肢には、ユーザーの選択に設定されたカスタム属性`upgrade_reason`があります。 

例えば、ユーザーが「高すぎる」を選択すると、それがユーザーのプロファイルに`upgrade_reason = expensive`を設定します。これらのユーザーを割引や無料トライアルなどのプロモーションキャンペーンの対象にすることができます。

![][9]

### お気に入りの機能

**目的:**顧客がどの機能を楽しく使用しているかを理解します。

このユースケースでは、各選択肢がアプリの機能である複数選択を使用します。各選択肢には、ユーザーの選択に設定されたカスタム属性`favorite_features`があります。このユースケースでは多岐選択を使用するため、ユーザーが調査を完了すると、ユーザープロファイルの `favorite_features` 属性が、選択されたすべてのオプションからなる配列に設定されて更新されます。

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
