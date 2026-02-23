{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Definição de atributos personalizados do usuário

Para definir atributos personalizados do usuário, use o método `setCustomUserAttribute()`. Para saber mais, consulte as informações relevantes sobre [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) e [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift).

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```
