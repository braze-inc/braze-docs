---
nav_title: Notificaciones push
article_title: Notificaciones push para Windows Universal
platform: Windows Universal
page_order: 1
description: "En este artículo se cubren las instrucciones de integración de notificaciones push para la plataforma Universal de Windows."
channel: push 
hidden: true
---

# Integración de notificaciones push
{% multi_lang_include archive/windows_deprecation.md %}

![Un ejemplo de push universal de Windows.][10]{: style="float:right;max-width:40%;margin-left:15px;"}

Una notificación push es una alerta fuera de la aplicación que aparece en la pantalla del usuario cuando se produce una actualización importante. Las notificaciones push son una forma valiosa de proporcionar a tus usuarios contenido relevante y urgente, o de reactivar su interacción con tu aplicación.

Visita nuestra [documentación][9] para conocer otras buenas prácticas.

## Paso 1: Configura tu aplicación para push

Asegúrate de que en tu archivo `Package.appxmanifest` están configurados los siguientes ajustes:

Dentro de la pestaña **Aplicación**, asegúrate de que `Toast Capable` está en `YES`.

## Paso 2: Configurar el panel de Braze

1. [Encuentra tu SID y tu secreto de cliente][4]
2. En la página **Configuración** del panel de Braze, añade el SID y el Secreto del cliente en tu configuración.<br>![][6]

## Paso 3: Actualización para el registro abierto en segundo plano

En tu método `OnLaunched`, después de haber llamado a `OpenSession` añade el siguiente fragmento de código.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);          
}
```

## Paso 4: Crear controladores de eventos

Para escuchar los eventos que se disparan cuando se recibe el push y se activa (clic del usuario), crea controladores de eventos y añádelos a los eventos de `PushManager`:

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

Tus controladores de eventos deben tener las firmas:

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## Paso 5: Vinculación en profundidad desde push a tu aplicación

### Parte 1: Crear vínculos profundos para tu aplicación

Los vínculos profundos se utilizan para dirigir a los usuarios desde fuera de tu aplicación directamente a una determinada pantalla o página de tu aplicación. Normalmente, esto se hace registrando un esquema de URL (por ejemplo, myapp://mypage) en un sistema operativo y registrando tu aplicación para que maneje ese esquema; cuando se pide al sistema operativo que abra una URL de ese formato, transfiere el control a tu aplicación.

El soporte de vínculos profundos de WNS difiere de esto, ya que lanza tu aplicación con datos sobre dónde enviar al usuario. Cuando se crea un push WNS, puede incluir una cadena de lanzamiento que se transmite al `OnLaunched` de tu aplicación cuando se hace clic en el push y se abre tu aplicación. Ya utilizamos esta cadena de lanzamiento para hacer el seguimiento de la campaña, y damos a los usuarios la posibilidad de añadir sus propios datos, que pueden ser analizados y utilizados para navegar por el usuario cuando se lanza la aplicación.

Si especificas una cadena de lanzamiento adicional en el panel o en la API REST, se añadirá al final de la cadena de lanzamiento que creemos, después de la clave "abextras=". Así, un ejemplo de cadena de lanzamiento podría ser `ab_cn_id=_trackingid_abextras=page=settings`, en la que has especificado `page=settings` en el parámetro extra de la cadena de lanzamiento para poder analizarla y dirigir al usuario a la página de configuración.

### Parte 2: Vinculación en profundidad a través del panel

Especifica la cadena que se añadirá a la cadena de lanzamiento en el campo "Configuración de cadena de lanzamiento adicional" de la configuración de notificaciones push.

![][15]

### Parte 3: Vinculación en profundidad a través de la API REST

Braze también permite enviar vínculos profundos a través de la API REST. [Los objetos push de la plataforma Universal de Windows][13] aceptan un parámetro opcional `extra_launch_string`.

[4]: http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx
[6]: {% image_buster /assets/img_archive/windows_sid.png %} "Panel SID de Windows"
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[10]: {% image_buster /assets/img_archive/windows_uni_push_sample.png %}
[13]: {{site.baseurl}}/api/objects_filters/messaging/windows_objects/
[15]: {% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Acción de clic en vínculos profundos"
