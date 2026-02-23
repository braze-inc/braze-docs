{% multi_lang_include developer_guide/prerequisites/android.md %}

## 메시지 데이터 로깅

캠페인의 분석을 처리하기 위해 특정 함수가 호출되는지 확인해야 합니다.

### 표시된 메시지

메시지가 표시되거나 확인되면 노출 횟수를 기록합니다.

```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

### 클릭한 메시지

사용자가 메시지를 클릭하면 클릭을 기록한 다음, `in_app_message.click_action`을 처리합니다.

```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

### 클릭한 버튼

사용자가 버튼을 클릭하면 버튼 클릭을 기록한 다음, `inappmessage.buttons[selected].click_action`을 처리합니다.

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

### 메시지 처리 후

인앱 메시지를 처리한 후에는 해당 필드를 지워야 합니다.

```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
