---
nav_title: Temas en modo oscuro
article_title: Modo oscuro para los mensajes de la aplicación
page_order: 5
description: "Este artículo de referencia trata la compatibilidad con el modo oscuro de los mensajes in-app de Braze, incluyendo cómo configurar un tema de modo oscuro y consideraciones de compatibilidad."
channel:
  - in-app messages

---

# Temas para el modo oscuro

> El Modo Oscuro ofrece a los usuarios la oportunidad de establecer una preferencia de color para todo el sistema (introducido en [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) e [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Los temas "oscuros" están pensados para ahorrar batería y reducir la fatiga visual de los usuarios, al tiempo que ofrecen a los desarrolladores de aplicaciones una forma más sencilla de implementar los temas de color oscuro que prefieren los usuarios.

Los mensajes Braze in-app admiten la adición de un tema oscuro alternativo para ayudar a transmitir el mensaje de color correcto a los usuarios en función de sus preferencias, y ayuda a mantener la coherencia con el diseño de la aplicación.

## Cómo funciona el modo oscuro

Los usuarios con versiones de al menos Android 10 o iOS 13 y posteriores pueden activar o desactivar el Modo Oscuro en los ajustes de su dispositivo.

Cuando el Modo Oscuro está activado, los menús y pantallas nativos del dispositivo (notificaciones push, ajustes del dispositivo, etc.) cambiarán a un gris oscuro. Las aplicaciones también pueden elegir admitir el modo oscuro especificando los temas alternativos en el código de la aplicación.

## Configuración de un tema en modo oscuro

La nueva opción Modo oscuro, situada en la pestaña Estilo al [crear un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), te permite añadir fácilmente un tema de color alternativo para los usuarios que estén en Modo oscuro en su dispositivo.

![Cambio de usuario entre los estilos Modo claro y Modo oscuro en la pestaña Estilo al crear un mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Cuando esta opción está activada, puedes elegir colores oscuros para tu mensaje dentro de la aplicación utilizando el selector de color, o seleccionando los [perfiles de color]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) existentes para reutilizar los temas oscuros o claros.

{% alert note %}
Puedes utilizar esta función aunque tu aplicación no ofrezca su propio tema oscuro. Sin embargo, los dispositivos que no admitan el modo oscuro mostrarán el tema claro por defecto. Cambiar el tema del dispositivo en Android mientras se muestra un mensaje de la aplicación no cambiará el tema que se utiliza para ese mensaje de la aplicación.
{% endalert %}

### Usar el modo oscuro de manera sistemática

Para utilizar el modo oscuro en todos los mensajes de la aplicación, ve a **Plantillas** > **Plantillas de mensajes de la aplicación**.

Desde allí, seleccione [Crear perfil de color]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) en el menú desplegable. Crea un Perfil de Color que se alinee con tu tema de Modo Oscuro. A continuación, cada vez que crees una versión en modo oscuro de un mensaje integrado en la aplicación, podrás seleccionar ese perfil de color y mantener la coherencia del aspecto de tus mensajes integrados en la aplicación.

## Compatibilidad

- Tus usuarios deben tener dispositivos iOS versión 13 o superior, o dispositivos Android versión 10 o superior.
- Se requiere el SDK para iOS de Braze v3.21.0+ y el SDK para Android de Braze v3.8.0+.

{% alert note %}
Las aplicaciones en modo oscuro se introdujeron con Android 10 e iOS 13. A los usuarios que no hayan actualizado sus teléfonos al menos a estas versiones solo se les mostrará el tema claro. <br><br>Las campañas se seguirán sirviendo a todos los usuarios que cumplan los requisitos para la audiencia que hayas seleccionado, independientemente de la configuración del modo oscuro de los usuarios o de la versión del sistema operativo.
{% endalert %}

## Uso de mensajes HTML en la aplicación

Para crear un tema oscuro y claro para los mensajes HTML dentro de la aplicación, puedes utilizar la característica [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) multimedia CSS para detectar las preferencias del usuario.

Por ejemplo:

```css
@media (prefers-color-scheme: dark) {
  body {
    background: #333;
    color: white;
  }
}

@media (prefers-color-scheme: light) {
  body {
    background: white;
    color: #555;
  }
}
```

