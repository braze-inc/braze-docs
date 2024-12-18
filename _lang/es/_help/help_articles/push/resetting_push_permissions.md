---
nav_title: Restablecer permisos push
article_title: Restablecer permisos push
page_type: solution
description: "Este artículo de ayuda explica cómo restablecer los permisos y datos push del navegador."
channel: push
---

# Restablecer permisos push

Si tienes problemas con las notificaciones push en tu navegador, es posible que tengas que restablecer los permisos de notificación de tu sitio y borrar el almacenamiento del mismo. Consulta estos pasos para obtener ayuda.

## Reiniciar Chrome en el escritorio

1. Junto a tu URL en el navegador Chrome, haz clic en el icono deslizante **Ver información del sitio**.
2. En **Notificaciones**, haz clic en **Restablecer permiso**.
3. Abre Chrome DevTools. A continuación se indican los atajos relevantes por sistema operativo.

<style> 
table {
    max-width: 50%;
}
</style>

| OS      | Atajos de teclado                                                  |
| ------- | ------------------------------------------------------------------- |
| Mac      | `Fn` + `F12`<br>`Ctrl` + `Shift` + `I` |
| Windows | `F12`<br>`Ctrl` + `Shift` + `I` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{:start="4"}
4\. En DevTools, ve a la pestaña **Aplicación**.
5\. En la barra lateral, selecciona **Almacenamiento**.
6\. Haz clic en **Borrar datos del sitio**.
7\. Chrome te pedirá que vuelvas a cargar la página para aplicar la configuración actualizada. Haz clic en **Recargar**.

Tus permisos push se han restablecido. Abre una pestaña nueva en tu sitio y pruébalo.

## Reiniciar Chrome en Android

Si tienes una notificación de tu sitio visible en el cajón de notificaciones de tu Android:

1. Desde la notificación push, pulsa <i class="fas fa-cog" title="Configuración"></i> y selecciona **Configuración del sitio**.
2. En **Configuración del sitio**, pulsa **Borrar y reiniciar**.

Si no tienes una notificación de tu sitio abierta:

1. Abre Chrome en Android.
2. Pulsa en el menú <i class="fas fa-ellipsis-vertical"></i>.
3. Ve a **Configuración** > **Configuración del sitio** > **Notificaciones**.
4. Comprueba que las notificaciones están configuradas en "Preguntar antes de enviar (recomendado)".
5. Encuentra tu sitio en la lista.
6. Selecciona la entrada y pulsa **Borrar y Restablecer**.

Tus permisos push se han restablecido. Abre una pestaña nueva en tu sitio y pruébalo.

## Reiniciar Firefox en el escritorio

1. Junto a la URL de tu sitio, haz clic en <i class="fa-solid fa-circle-info" alt="info icon"></i> o <i class="fas fa-lock" alt="lock icon"></i>.
2. En **Permisos**, junto a **Recibir notificaciones**, selecciona <i class="fa-solid fa-circle-xmark" title="Borrar este permiso y volver a preguntar"></i> para borrar los permisos de notificación.
3. En el mismo menú, selecciona **Borrar cookies y datos del sitio**.
4. Aparecerá un cuadro de diálogo para confirmar tu elección. Haz clic en **Aceptar**.

Tus permisos push se han restablecido. Abre una pestaña nueva en tu sitio y pruébalo.

## Reiniciar Firefox en Android

Para restablecer los permisos push en Android, consulta este [artículo de soporte de Mozilla](https://support.mozilla.org/en-US/kb/clear-your-browsing-history-and-other-personal-data#w_clear-specific-items-from-your-browser).

## Reiniciar Safari en macOS

{% alert note %}
Estos pasos son solo para macOS, ya que Apple no admite notificación push web para Safari en Windows.
{% endalert %}

1. Abre Safari.
2. En la [barra de menús del Mac](https://support.apple.com/guide/mac-help/whats-in-the-menu-bar-mchlp1446/mac), ve a **Safari** > **Configuración** > **Sitios web** > **Notificaciones**.
3. Selecciona tu sitio de la lista.
4. Haz clic en **Eliminar** para suprimir los permisos de notificación del sitio.
5. A continuación, ve a **Privacidad** > **Gestionar datos del sitio web**.
6. Selecciona tu sitio de la lista.
7. Haz clic en **Eliminar**, o para eliminar todos los datos del sitio, haz clic en **Eliminar todo**.
8. Haz clic en **Listo**.

Tus permisos push se han restablecido. Abre una pestaña nueva en tu sitio y pruébalo.


*Última actualización: 12 de febrero de 2024*