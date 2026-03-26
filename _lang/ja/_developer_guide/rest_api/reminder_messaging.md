---
nav_title: ユーザー選択リマインダーメッセージング
article_title: ユーザー選択リマインダーメッセージング
page_order: 5
page_type: reference
description: "このリファレンス記事では、Braze のランディングページ、カスタム属性、キャンペーンを使用して、今後のイベントや予定に関するパーソナライズ済みリマインダーメッセージにユーザーがサインアップできるようにする方法を説明します。"
---

# ユーザー選択リマインダーメッセージング

> Braze の[ランディングページ]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/)、カスタム属性、キャンペーンを使用して、今後のイベントや予定に関するリマインダーメッセージをいつ受け取りたいかをユーザーが選択できるようにします。このアプローチにより、技術的な知識がない Braze ユーザーでもリマインダーサインアップページのコンテンツを作成・編集でき、ユーザーが選択した設定は Braze を活用したすべてのメッセージングにおけるセグメンテーション、ターゲティング、パーソナライゼーションに活用できます。

このアプローチでは、以下のことが可能です。

- 今後のイベントに対するリマインダーメッセージの日付をユーザー自身が選択できます。
- Braze のランディングページを使用してユーザーから直接設定を取得し、ユーザープロファイルに書き込みます。追加のバックエンドは不要です。
- ユーザーが選択した日付にメッセージを送信するため、メッセージの関連性と許可ベースの配信が維持されます。
- メッセージ遅延、フォローアップリターゲティング、AB テストなどの追加の Braze 機能でユースケースを拡張できます。

## 前提条件

このガイドを完了するには、以下が必要です。

| 要件 | 説明 |
| --- | --- |
| ランディングページへのアクセス | Braze で[ランディングページ]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/)を作成するためのアクセスと権限。 |
| HTML と JavaScript の知識 | ランディングページをカスタマイズするための HTML と JavaScript の基本的な知識。[オプション B](#option-b-personal-dates-custom-code-block) でのみ必要です。 |
| Liquid の知識 | パーソナライズ済み変数をテンプレート化するための [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) の基本的な知識。 |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## ステップ 1: ランディングページを作成し、メッセージからリンクする

まず、[Braze のランディングページを作成]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/)します。次に、ユーザーをランディングページにリンクするメッセージ（メールなど）を作成します。

{% raw %}
ランディングページのアクティビティを受信者のユーザープロファイルに自動的に関連付けるには、Braze メッセージからページにリンクする際に `{% landing_page_url %}` Liquid タグを使用します。例:

```html
<a href="{% landing_page_url your-page-url-handle %}">Sign up for reminders</a>
```
{% endraw %}

ユーザーがこのリンクをクリックすると、Braze が自動的にユーザーを識別するため、送信された設定は既存のプロファイルに書き込まれます。手動での URL パラメーターは不要です。詳細なウォークスルーについては、[フォームを通じてユーザーを追跡する]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/tracking_users/)を参照してください。

## ステップ 2: ランディングページで設定を取得する

ユーザー設定の取得方法は、共通の日付を収集するか、パーソナルな日付を収集するかによって異なります。ユースケースに合ったオプションを選択してください。

### オプション A: 共通の日付（ドラッグ＆ドロップフォームブロック）

多くのユーザーが同じ日付を共有するイベント（祝日やスポーツイベントなど）の場合、ドラッグ＆ドロップエディターの組み込み[**チェックボックス**フォームブロック]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#form-blocks)を使用して設定を取得します。各チェックボックスは、フォームが送信されるとユーザーのプロファイルにブール値のカスタム属性（`true` または `false`）をネイティブに設定します。カスタムコードは不要です。

例えば、カスタム属性 `super_bowl_2026_reminder` にマッピングされた「Super Bowl 2026 リマインダー」というラベルのチェックボックスを追加します。ユーザーがチェックボックスをオンにしてフォームを送信すると、Braze は以下を設定します。

```
super_bowl_2026_reminder = true
```

これらのブール値属性は、[セグメントフィルター]({{site.baseurl}}/user_guide/engagement_tools/segments/)で直接使用して、リマインダーメッセージのターゲットオーディエンスを構築できます。

### オプション B: パーソナルな日付（カスタムコードブロック）

各ユーザーに固有の日付（誕生日や記念日など）の場合、ランディングページの[**カスタムコード**ブロック]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#basic-blocks)を使用して日付を取得し、`lpBridge` API を使用して Braze に書き込みます。このアプローチでは、日付入力（またはピッカー）が提供され、ドラッグ＆ドロップフォームブロックではサポートされていない[階層化カスタム属性のオブジェクト配列]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/array_of_objects/)に設定を保存できます。

ユーザーが {% raw %}`{% landing_page_url %}`{% endraw %} Liquid タグを通じてアクセスすると、Braze はすでにユーザーを認識しているため、スクリプトは以下のことだけを行う必要があります。

1. フォーム送信ボタンのクリックをリッスンします。
2. カスタム入力から日付値を読み取ります。
3. `lpBridge` API を使用して階層化カスタム属性を設定し、データを Braze にフラッシュします。

これらの設定は、階層化カスタム属性のオブジェクト配列を使用して保存します。この構造により、ユーザーごとに複数のリマインダーを保存でき、`next_reminder_name` や `last_reminder_date` などの派生フィールドを後から追加できます。

#### スクリプトの例

以下のスクリプト例では、デフォルトのボタン動作を無効にし、ボタンクリック時にカスタムメソッドを実行します。要素 ID と属性値をご自身のものに置き換えてください。

```html
<script async="true">
  // Set IDs (as found by inspecting your landing page preview) and success message
  const registerButtonId = "YOUR_BUTTON_ID";
  const messageDivId = "YOUR_MESSAGE_DIV_ID";
  const successMessage = "You're all set! We'll send your reminder.";

  // Wait for page content to load
  document.addEventListener("DOMContentLoaded", () => {
    // Remove the default redirect event from the Braze Message Handler Script
    props[registerButtonId].onclickContract[0].brazeEvents =
      props[registerButtonId].onclickContract[0].brazeEvents.filter(
        (event) => event.eventType !== "REDIRECT"
      );

    const registerButton = document.getElementById(registerButtonId);
    if (registerButton) {
      registerButton.addEventListener("click", async (event) => {
        event.preventDefault();

        // Set the custom attribute (replace with your actual key/value)
        await window.lpBridge.setCustomUserAttribute("key", "value");

        // Flush data to Braze
        await window.lpBridge.requestImmediateDataFlush();

        // Remove the button and update the message
        registerButton.remove();
        const messageDiv = document.getElementById(messageDivId);
        if (messageDiv) {
          messageDiv.innerHTML = successMessage;
        }
      });
    }
  });
</script>
```

ランディングページコンポーネントの要素 ID を見つけるには、ページをプレビューし、右クリックしてブラウザで**検証**を選択します。HTML 内でボタンとメッセージコンポーネントの ID を確認してください。

## ステップ 3: リマインダーメッセージを設定してトリガーする

ランディングページを通じてカスタム属性を収集した後、今後のイベントについてユーザーにメッセージを送信するキャンペーンを作成します。

### オプション A: 共通の日付 {#step-3-option-a-shared-dates}

ブール値のカスタム属性（[ステップ 2](#option-a-shared-dates-dnd-form-blocks) のオプション A）を使用した場合、その属性をセグメントフィルターとして使用してリマインダーメッセージのオーディエンスを構築します。次に、イベント前にスケジュールされた新しいキャンペーンを作成し、選択したコンテンツでこのグループをターゲットにします。

### オプション B: パーソナルな日付 {#step-3-option-b-personal-dates}

階層化カスタム属性（[ステップ 2](#option-b-personal-dates-custom-code-block) のオプション B）を使用した場合、**階層化カスタム属性**オーディエンスフィルターを使用して、特定の時間枠内（例えば、2日後）にリマインダー日付があるすべてのユーザーを選択します。

継続的にリマインダーを送信するには、毎日繰り返しのキャンペーンを設定して、時間枠内に今後のリマインダーがあるユーザーが毎日メッセージを受信できるようにします。

## ステップ 4: 統合を検証する

セットアップが完了したら、統合を検証します。

1. ランディングページへのリンクを自分に送信し、フォームを完了します。
2. Braze ダッシュボードでユーザープロファイルに移動し、カスタム属性が表示されていることを確認します。
3. テストリマインダーメッセージを自分のプロファイルに送信し、パーソナライズ済みの詳細が正しくレンダリングされることを確認します。
4. キャンペーンを起動する際に、結果を注意深く監視します。

## 考慮事項

- 日付ベースのカスタム属性に基づいてメッセージを送信する方法の詳細な例については、[REST API メッセージングガイド]({{site.baseurl}}/developer_guide/rest_api/messaging/)のメールのユースケースを参照してください。
- ランディングページを複製したり、フィールドを置き換えたりすると、コンポーネント ID が変更されます。新しい ID を反映するようにカスタムコードブロックを更新してください。
- 階層化カスタム属性は、オブジェクト配列内の各キーに対して[データポイント]({{site.baseurl}}/user_guide/data/infrastructure/data_points/)を消費します。カスタム属性オブジェクトを null に更新する場合もデータポイントを消費します。
- このガイドで紹介しているコードは、説明のための例です。本番環境にデプロイする前に、すべてのコードとコンポーネントをご自身の環境で十分にテストしてください。