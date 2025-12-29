---
nav_title: Temas en modo oscuro
article_title: Modo oscuro para mensajes dentro de la aplicación
page_order: 5
description: "Este artículo de referencia cubre la compatibilidad con el modo oscuro de los mensajes dentro de la aplicación Braze, incluyendo cómo configurar un tema de modo oscuro y consideraciones de compatibilidad."
channel:
  - in-app messages

---

# Temas del modo oscuro

> El modo oscuro ofrece a los usuarios la oportunidad de establecer una preferencia de color para todo el sistema (introducido en [Android 10](https://developer.android.com/guide/topics/ui/look-and-feel/darktheme) e [iOS 13](https://developer.apple.com/documentation/appkit/supporting_dark_mode_in_your_interface/)). Los temas "Oscuros" están pensados para ahorrar batería y reducir la fatiga visual de los usuarios, a la vez que proporcionan a los desarrolladores de aplicaciones una forma más fácil de implementar los temas de color oscuro que prefieren los usuarios.

Los mensajes dentro de la aplicación Braze admiten la adición de un tema Oscuro alternativo para ayudar a entregar el mensaje del color correcto a tus usuarios en función de sus preferencias, y ayuda a proporcionar coherencia con el diseño de tu aplicación.

## Cómo funciona el modo oscuro

Los usuarios con versiones de al menos Android 10 o iOS 13 y posteriores pueden alternar entre activar o desactivar el modo oscuro en la configuración de su dispositivo.

Cuando el modo oscuro está habilitado, los menús y pantallas nativos del dispositivo (notificaciones push, configuración del dispositivo, etc.) cambiarán a un color gris oscuro. Las aplicaciones también pueden elegir admitir el modo oscuro especificando los temas alternativos en el código de la aplicación.

## Configuración de un tema en modo oscuro

La nueva opción Modo oscuro, situada en la pestaña Estilo al [crear un mensaje dentro de la aplicación]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/), te permite añadir fácilmente un tema de color alternativo para los usuarios que estén en Modo oscuro en su dispositivo.

El usuario cambia entre los estilos Modo claro y Modo oscuro en la pestaña Estilo al crear un mensaje dentro de la aplicación.]({% image_buster /assets/img_archive/iam-dark-mode.gif %})

Cuando esta opción está habilitada, puedes elegir colores de tema oscuro para tu mensaje dentro de la aplicación utilizando el selector de color, o seleccionando [Perfiles de color]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) existentes para reutilizar los temas Oscuro o Claro existentes.

{% alert note %}
Puedes utilizar esta característica aunque tu aplicación no ofrezca su propio tema oscuro. Sin embargo, los dispositivos que no admitan el modo oscuro mostrarán el tema claro predeterminado. Cambiar el tema del dispositivo en Android mientras se muestra un mensaje dentro de la aplicación no cambiará el tema utilizado para ese mensaje dentro de la aplicación.
{% endalert %}

### Uso sistemático del modo oscuro

Para utilizar el modo oscuro para todos los mensajes dentro de la aplicación, ve a **Plantillas** > Plantillas de mensajes dentro de la aplicación **.**

Desde ahí, selecciona [Crear perfil de color]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#color-profile) en el menú desplegable. Crea un perfil de color que se ajuste a tu tema de modo oscuro. Entonces, cada vez que crees una versión en modo oscuro de un mensaje dentro de la aplicación, podrás seleccionar ese perfil de color y mantener la coherencia del aspecto de tus mensajes dentro de la aplicación.

## Compatibilidad

- Tus usuarios deben tener dispositivos iOS versión 13 o superior, o dispositivos Android versión 10 o superior.
- Se requiere Braze iOS SDK v3.21.0+ Braze Android SDK v3.8.0+.

{% alert note %}
Las aplicaciones en modo oscuro se introdujeron con Android 10 e iOS 13. A los usuarios que no hayan actualizado sus teléfonos al menos a estas versiones sólo se les mostrará el tema claro. <br><br>Las campañas seguirán sirviéndose a todos los usuarios elegibles para la audiencia que hayas seleccionado, independientemente de la configuración del modo oscuro de los usuarios o de la versión del sistema operativo.
{% endalert %}

## Usar mensajes HTML dentro de la aplicación

Para crear un tema Oscuro y Claro para los mensajes HTML dentro de la aplicación, puedes utilizar la función [`prefers-color-scheme`](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) característica CSS media para detectar las preferencias del usuario.

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

