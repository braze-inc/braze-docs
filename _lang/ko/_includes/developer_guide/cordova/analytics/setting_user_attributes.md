{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## 커스텀 사용자 속성 설정하기

커스텀 사용자 속성을 설정하려면 `setCustomUserAttribute()` 방법을 사용합니다. 자세한 내용은 관련 [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) 및 [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift) 정보를 참조하세요.

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```
