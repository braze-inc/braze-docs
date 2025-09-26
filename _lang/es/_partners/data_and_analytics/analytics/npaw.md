---
nav_title: NPAW
article_title: NPAW
alias: /partners/npaw/
description: "Este artículo de referencia describe la asociación entre Braze y NPAW, una plataforma inteligente de análisis de datos que proporciona información práctica a los principales profesionales de los medios de comunicación en línea."
page_type: partner
search_tag: Partner
hidden: true

---

# NPAW

> [NPAW](https://nicepeopleatwork.com/), también conocida como _Nice People at Work_, es una plataforma inteligente de análisis de datos que proporciona información práctica a los principales profesionales de los medios de comunicación en línea. Con la suite de herramientas YOUBORA de NPAW, ahora los clientes de Braze pueden aprovechar una IA predictiva y robusta para comprender mejor el comportamiento de los clientes e impulsar la participación en todas las plataformas.

# Requisitos previos

| Requisito   |Origin| Descripción |
| --------------|------|-------------|
| Clave de API de YOUBORA |[Configuración de YOUBORA](https://youbora.nicepeopleatwork.com/users/login)|Una clave de API generada al registrarse el usuario y que puede encontrarse en **Configuración** |
| ID |[Ajustes de Braze](https://dashboard.braze.com/sign_in) | YOUBORA te da la opción de vincular el software a Braze a través de un ***ID de Braze***, un ***ID de usuario externo** *o un ***ID de usuario*** |
| Punto de conexión |[Ajustes de Braze](https://dashboard.braze.com/sign_in)| Un punto final de URL totalmente personalizable y configurable a través de tu dashboard de Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

# Integración de análisis

## Acceso a la página de integraciones

Tras acceder a tu cuenta de la línea de productos YOUBORA, ve a la página Integraciones seleccionando la opción **Integraciones** en el menú desplegable de la cuenta.

![Desplegable NPAW]({% image_buster /assets/img/npaw_dropdown.png %})

## Configuración de la integración

Una vez que hayas accedido a la página de Integración, desplázate hacia abajo hasta que encuentres
la opción de integración de **Braze**. Tras hacer clic en esta opción, se ampliará y ofrecerá una serie de parámetros necesarios para rellenar:

![Integración de NPAW]({% image_buster /assets/img/npaw_integration.png %})

Rellene los datos con la información adecuada reunida a partir de la sección de requisitos previos, en la cual:
* **El nombre del conector** es una cadena **alfanumérica** que se utilizará para referirse a esta integración en el futuro. Este valor puede ser cualquier cosa, siempre que contenga **solamente** letras y números.
* **El ID de usuario** es el ID elegido previamente para vincular tu software YOUBORA con tu cuenta de Braze. Por ejemplo, si decides realizar el enlace a través de tu **ID de Braze**, selecciona **ID de Braze** en el menú desplegable para asignar el valor al campo adecuado.
* **La clave de API** es tu clave de API del paquete de herramientas de YOUBORA, anteriormente ubicada dentro de la sección **API** en **Configuración**.
* **Punto de conexión** es el punto final de URL personalizable previamente configurado en tu dashboard de Braze.

Una vez rellenados todos los campos, basta con pulsar el botón **Conectar** para establecer la conexión y guardar los cambios realizados.

## Uso de la integración NPAW

Una vez que hayas terminado de configurar tu integración con Braze, navega hasta el producto **Usuarios** y selecciona el **administrador de muestras** dentro del **administrador de secciones**.

Después de crear una muestra en el **administrador de muestras**, podrás hacer clic en el icono de tres puntos de la derecha para enviar todos los usuarios de tu muestra a Braze.

![Administrador de muestras de NPAW]({% image_buster /assets/img/npaw_sample_manager.png %})

Ahora, una vez enviados tus usuarios a Braze, puedes actuar y centrar las campañas en segmentos de usuarios para volver a captar a los usuarios inactivos, ponerte en contacto con tus usuarios más fidelizados o realizar cualquier acción en cualquier segmento de usuarios.
