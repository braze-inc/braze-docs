{% multi_lang_include developer_guide/prerequisites/android.md %}

## メッセージデータを記録する

キャンペーンの分析を処理するために特定の関数が呼び出されることを確認する必要があります。

### 表示されるメッセージ

メッセージが表示または確認されたら、インプレッションをロギングします。

```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

### クリックされたメッセージ

ユーザーがメッセージをクリックしたら、クリックをロギングし、`in_app_message.click_action` を処理します。

```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

### クリックされたボタン

ユーザーがボタンをクリックしたら、ボタンクリックをロギングし、`inappmessage.buttons[selected].click_action` を処理します。

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

### メッセージを処理した後

アプリ内メッセージの処理後に、フィールドをクリアする必要があります。

```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
