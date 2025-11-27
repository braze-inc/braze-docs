{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## カスタムユーザー属性の設定

カスタムユーザー属性を設定するには、`setCustomUserAttribute()` メソッドを使用する。より詳細な情報については、関連する[Androidと]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) [iOSの]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift)情報を参照のこと。

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```
