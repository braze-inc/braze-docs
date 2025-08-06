{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Angepasste Attribute für Nutzer:innen einstellen

Um angepasste Attribute für Nutzer:innen festzulegen, verwenden Sie die Methode `setCustomUserAttribute()`. Ausführlichere Informationen finden Sie in den entsprechenden Informationen für [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) und [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift).

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```
