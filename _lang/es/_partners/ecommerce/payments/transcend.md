---
nav_title: Transcend
article_title: Transcend
description: "Este artículo de referencia describe la asociación entre Braze y Transcend, una plataforma de infraestructura de privacidad de datos, que ayuda a los usuarios de Braze a automatizar el cumplimiento de las solicitudes de los interesados."
alias: /partners/transcend/
page_type: partner
search_tag: Partner

---

# Transcend

> Transcend es una empresa de infraestructura de privacidad de datos que simplifica a las empresas la tarea de dar a sus usuarios el control sobre sus datos, satisfaciendo automáticamente las solicitudes de los interesados dentro de las empresas en todos sus sistemas de datos y proveedores. 

_Esta integración está mantenida por Transcend._

## Sobre la integración

La asociación de Braze y Transcend ayuda a los usuarios a automatizar las solicitudes de privacidad mediante la orquestación de datos a través de docenas de sistemas de datos, ayudando a los equipos a cumplir con regulaciones como GDPR y CCPA. Transcend proporciona a los usuarios finales un panel de control, o centro de privacidad, alojado en `privacy.\<company\>.com`, donde los usuarios pueden gestionar sus preferencias de privacidad, exportar sus datos o eliminarlos. 

## Requisitos previos

| Requisitos | Descripción |
|---|---|
| Cuenta Transcend | Se requiere una cuenta [Transcend](https://app.transcend.io/) con privilegios de administrador para beneficiarse de esta asociación. |
| Clave API Braze | Una clave de API REST Braze con permisos `users.delete, users.alias.new, users.export.ids, email.unsubscribe,` y `email.blacklist`.<br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Transcend le permite acceder de forma programática, borrar y excluir a los usuarios de la comunicación en la plataforma Braze de acuerdo con la normativa de privacidad de datos.

### Paso 1: Configurar la integración Braze
Para empezar, inicia sesión en [Transcend](https://app.transcend.io/login).
1. Vaya a **Mapa de datos > Añadir silo de datos > Braze** y seleccione el botón **Conectar**.<br><br>
2. Cuando se aprovisione tu cuenta, iniciarás sesión en una de las URL correspondientes: `https://dashboard-01.braze.com`, `https://dashboard-02.braze.com, ..., https://dashboard-01.braze.eu`.<br> Utilice la siguiente [tabla]({{site.baseurl}}/api/basics/#endpoints) para averiguar qué subdominio debe incluir en función de la URL de su panel de control.<br><br>
3. Cuando esté conectado, navegue hasta la pestaña **Centro de privacidad** de Transcend. Aquí tendrá que asignar los datos de Braze a sus prácticas de datos. Para ello, cree una nueva categoría y una nueva recopilación de datos con la convención de nomenclatura adecuada (por ejemplo, "Listas de correo o perfil de usuario"). Cuando haya terminado, pulse **Publicar**.<br><br>
4. Vuelve a tu Mapa de Datos y haz clic en el silo de datos Braze. Expanda **Gestionar puntos de datos** y seleccione en el desplegable la etiqueta de la colección (categoría) que creó en el paso anterior. También puede elegir qué acciones de datos (por ejemplo, acceso o borrado) están habilitadas para qué puntos de datos. <br><br>
5. A continuación, mientras sigues en el silo de datos Braze, expande **Gestionar identificadores**. Marque las casillas correspondientes a los identificadores que desea activar. Por ejemplo, si desea que Transcend busque usuarios por dirección de correo electrónico, marque la casilla para activar el identificador de dirección de correo electrónico.

{% alert note %}
Si los identificadores no están habilitados correctamente, Transcend puede no procesar las solicitudes de determinados usuarios.
{% endalert %}

### Paso 2: Solicitudes de prueba
Transcend recomienda probar las solicitudes a través de su Mapa de Datos antes de empezar a procesar las solicitudes de los usuarios finales.
1. Vaya al **Centro de privacidad** en Transcend y haga clic en **Ver su Centro de privacidad**.<br><br>
2. En el **Centro de privacidad**, haz clic en **Tomar el control** y, a continuación, en **Descargar mis datos**. Introduzca su correo electrónico o inicie sesión para autenticarse antes de enviar la solicitud.<br><br>
3. Consulta tu correo electrónico para recibir un mensaje de Transcend. Se le pedirá que haga clic en un enlace de verificación para comprobar la solicitud.<br><br>
4. A continuación, en el panel de **administración**, vaya a la pestaña **Solicitudes entrantes** y seleccione su solicitud. Ponte en contacto con Transcend en [support@transcend.io](mailto:support@transcend.io) si no ves la solicitud aquí.<br><br>
5. Una vez que haya hecho clic en su solicitud, vaya a la pestaña **Silos de datos** y seleccione **Braze**. Inspeccione y confirme los datos devueltos.<br><br>
6. Por último, vaya a la pestaña **Informe** y haga clic en **Aprobar y enviar**. Debería recibir el informe en la dirección de correo electrónico que envió con la solicitud.

## Retirar la integración Braze
Para eliminar el silo de datos Braze de tu Mapa de Datos Transcend:
1. Navegue hasta su **Mapa de datos** y haga clic en **Braze**. <br><br>
2. En la parte inferior de la pantalla, expanda **Quitar Braze** y haga clic en **Quitar Silo**. Se le pedirá que confirme que desea eliminar el silo. Haga clic en **Aceptar**. <br><br>
3. Confirma que se ha eliminado el silo navegando de nuevo a tu Mapa de Datos.


