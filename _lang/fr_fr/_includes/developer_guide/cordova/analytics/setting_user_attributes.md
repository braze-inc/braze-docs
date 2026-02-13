{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Définition d'attributs personnalisés pour les utilisateurs

Pour définir des attributs personnalisés, utilisez la méthode `setCustomUserAttribute()`. Pour plus d'informations, reportez-vous aux informations relatives à [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) et [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift).

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```
