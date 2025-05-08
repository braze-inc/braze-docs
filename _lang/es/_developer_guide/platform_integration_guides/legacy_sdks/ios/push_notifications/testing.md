---
nav_title: Prueba
article_title: Pruebas de notificación push para iOS
platform: iOS
page_order: 29
description: "Este artículo de referencia cubre las pruebas push de línea de comandos para tus notificaciones push de iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Prueba {#push-testing}

Si quieres probar las notificaciones dentro de la aplicación y las notificaciones push a través de la línea de comandos, puedes enviar una única notificación a través del terminal mediante CURL y la [API de mensajería]({{site.baseurl}}/api/endpoints/messaging/). Tendrás que sustituir los siguientes campos por los valores correctos para tu caso de prueba:

Campos obligatorios:

- `YOUR-API-KEY-HERE` - disponible en **Configuración** > **Claves de API**. Asegúrate de que la clave está autorizada para enviar mensajes a través del punto final de la API REST `/messages/send`. 
- `EXTERNAL_USER_ID` - disponible en la página **Buscar usuarios**.
- `REST_API_ENDPOINT_URL` - que aparece en Braze [Instancias]({{site.baseurl}}/api/basics/#endpoints. Asegúrate de que utilizas el punto final que corresponde a la instancia de Braze en la que está tu espacio de trabajo.

{% alert note %}
Si utilizas la [navegación antigua]({{site.baseurl}}/navigation), estas páginas se encuentran en una ubicación diferente: <br>- **Las claves de API** se encuentran en **Consola para desarrolladores** > **Configuración de API** <br>- **Buscar usuarios** se encuentra en **Usuarios** > **Búsqueda de usuarios**
{% endalert %}

Campos opcionales:
- `YOUR_KEY1` (opcional)
- `YOUR_VALUE1` (opcional)

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Bearer YOUR-API-KEY-HERE" -d '{
  "external_user_ids":["EXTERNAL_USER_ID"],
  "messages": {
    "apple_push": {
      "alert":"Test push",
      "extra": {
        "YOUR_KEY1":"YOUR_VALUE1"
      }
    }
  }
}' https://{REST_API_ENDPOINT_URL}/messages/send 
```
