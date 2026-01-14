{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## カスタムユーザー 属性を設定するs

カスタムユーザー 属性s を設定するには、`setCustomUserAttribute()` メソッドを使用します。詳細については、関連する[Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android)および[iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)の情報を参照してください。

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```
