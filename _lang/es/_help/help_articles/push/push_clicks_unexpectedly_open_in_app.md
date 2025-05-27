---
nav_title: Los clics push se abren inesperadamente en la aplicación
article_title: Los clics push se abren inesperadamente en la aplicación
page_type: solution
description: "Este artículo de ayuda explica cómo solucionar problemas cuando se espera que un enlace push se abra en un navegador web y no en la aplicación."
channel: push
---

# Los clics push se abren inesperadamente en la aplicación

Si tienes problemas con los enlaces de las notificaciones push que se abren inesperadamente en tu aplicación en lugar de en tu navegador Web, puede que haya un problema con la configuración de tu campaña o con la implementación del SDK. Consulta estos pasos para obtener ayuda.

## Verificar el comportamiento al hacer clic

En tu campaña o paso en Canvas, comprueba que la opción **Abrir URL Web dentro de la aplicación móvil** no está seleccionada. Si es así, borra la selección y relánzala. 

![Campo "Comportamiento al hacer clic" de la configuración de un push establecido en "Abrir URL web" con "Abrir URL web dentro de la aplicación móvil" desmarcado.]({% image_buster /assets/img/push_on_click.png %})

La interacción predeterminada para el comportamiento al hacer clic "Abrir URL Web" difiere según la versión del SDK. Para las versiones del SDK iOS 2.29.0 y Android 2.0.0 y superiores, esta opción está seleccionada por defecto y las URL web se abrirán en una vista web dentro de la aplicación. Antes de estas versiones, esta opción estaba desactivada por defecto y las URL web se abrían en el navegador web predeterminado del dispositivo.

Si este no es el problema, puede que haya un problema con tu implementación de push. 

## Doble comprobación de la integración push

Si los enlaces de tus notificaciones push se abren en la aplicación de forma inesperada, puede deberse a problemas con la integración de tus notificaciones push o con tu configuración personalizada. Sigue estos pasos para solucionar problemas:

1. **Revisa la implementación del delegado push:** Asegúrate de que el delegado push de Braze se implementa correctamente. Para obtener instrucciones detalladas, consulta la guía de integración de notificaciones push de tu [plataforma]({{site.baseurl}}/developer_guide/home/).
2. **Inspecciona el manejo personalizado de los enlaces:** Comprueba si la aplicación incluye un tratamiento personalizado para todos los enlaces `https://`. Las configuraciones personalizadas pueden anular los comportamientos predeterminados. Colabora con tu equipo de desarrolladores para revisar y ajustar estas configuraciones si es necesario.
3. **Verifica el registro push de iOS:** Para iOS, revisa el paso 1 de la guía de integración push sobre el [registro de notificaciones push con APNs]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration/#step-1-register-for-push-notifications-with-apns). Asegúrate de que tu objeto delegado se asigna de forma sincrónica antes de que la aplicación termine de ejecutarse. Este paso debe completarse en el método `application:didFinishLaunchingWithOptions:`.
4. **Prueba tu integración:** Tras realizar los ajustes, prueba el comportamiento de las notificaciones push tanto en dispositivos iOS como Android para confirmar que el problema se ha resuelto.

Si el problema persiste, ponte en contacto con [el soporte de Braze]({{site.baseurl}}/support_contact) para obtener más ayuda.


*Última actualización: 6 de diciembre de 2024*