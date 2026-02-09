Antes de que puedas enviar una notificación push de iOS utilizando Braze, tienes que cargar tu archivo de notificación push `.p8`, como se describe en [la documentación para desarrolladores de Apple:](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns)

1. En tu cuenta de desarrollador de Apple, ve a [**Certificados, identificadores & Perfiles**](https://developer.apple.com/account/ios/certificate).
2. En **Claves**, selecciona **Todas** y haz clic en el botón de añadir (+) de la esquina superior derecha.
3. En **Descripción de la** clave, introduce un nombre único para la clave de firma.
4. En **Servicios clave**, selecciona la casilla **Servicio de notificaciones push de Apple (APN)** y, a continuación, haz clic en **Continuar**. Haz clic en **Confirmar**.
5. Nota el ID de la clave. Haz clic en **Descargar** para generar y descargar la clave. Asegúrate de guardar el archivo descargado en un lugar seguro, ya que no puedes descargarlo más de una vez.
6. En Braze, ve a **Configuración** > **Configuración de la aplicación** y carga el archivo `.p8` en **Certificado Apple Push**. Puedes subir tu certificado push de desarrollo o de producción. Para probar las notificaciones push después de que tu aplicación esté en vivo en el App Store, se recomienda configurar un espacio de trabajo separado para la versión de desarrollo de tu aplicación.
7. Cuando se te solicite, introduce el [ID del paquete](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), el [ID de la llave](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) y el [ID del equipo](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id) de tu aplicación. También tendrás que especificar si quieres enviar notificaciones al entorno de desarrollo o de producción de tu aplicación, que se define por su perfil de aprovisionamiento. 
8. Cuando haya terminado, seleccione **Guardar**.

