{% multi_lang_include developer_guide/prerequisites/android.md %}

## Registro de datos de mensajes

Tendrás que asegurarte de que se llaman determinadas funciones para gestionar los análisis de tu campaña.

### Mensajes mostrados

Cuando se muestra o se ve un mensaje, registra una impresión:

```brightscript
LogInAppMessageImpression(in_app_message.id, brazetask)
```

### Mensajes con clic

Una vez que un usuario hace clic en el mensaje, registra un clic y luego procesa `in_app_message.click_action`:

```brightscript
LogInAppMessageClick(in_app_message.id, brazetask)
```

### Botones clicados

Si el usuario hace clic en un botón, registra el clic en el botón y luego procesa `inappmessage.buttons[selected].click_action`:

```brightscript
LogInAppMessageButtonClick(inappmessage.id, inappmessage.buttons[selected].id, brazetask)
```

### Después de procesar un mensaje

Después de procesar un mensaje dentro de la aplicación, debes borrar el campo:

```brightscript
m.BrazeTask.BrazeInAppMessage = invalid
```
