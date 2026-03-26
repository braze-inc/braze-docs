{% multi_lang_include developer_guide/prerequisites/cordova.md %}

## Configuración de atributos personalizados del usuario

Para establecer atributos personalizados de usuario, utiliza el método `setCustomUserAttribute()`. Para obtener información más detallada, consulta la información correspondiente de [Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) e [iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift).

```javascript
BrazePlugin.setCustomUserAttribute("KEY", "VALUE");
```
