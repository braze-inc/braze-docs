---
nav_title: Jacquard
article_title: Jacquard
alias: /partners/jacquard/
page_order: 1
description: "Este artículo de referencia describe la asociación entre Braze y Jacquard Dynamic Optimisation que aprovecha Braze Currents y Connected Content para recopilar información de seguimiento de clics de sus suscriptores a través de webhooks. A continuación, Jacquard relaciona esos eventos con sus variantes lingüísticas para optimizar el lenguaje en tiempo real."
page_type: partner
search_tag: Partner
---

# Optimización dinámica Jacquard

> [Jacquard](https://www.jacquard.com/) aúna inteligencia artificial, lingüística computacional y un espíritu centrado en el cliente para ayudar a desplegar el lenguaje de la marca, a escala, a través de canales personalizados según la voz de su marca.

La optimización dinámica, impulsada por Jacquard X, aprovecha Braze Currents y Connected Content para recopilar información de seguimiento de clics de sus suscriptores a través de webhooks. A continuación, Jacquard relaciona esos eventos con sus variantes lingüísticas para optimizar el lenguaje en tiempo real. 

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta jacquard | Es necesario tener una [cuenta Jacquard](https://www.jacquard.com/) para beneficiarse de esta asociación. |
| Token de servidor de conexión de Jacquard | Una larga cadena de caracteres que servirá como contraseña de tu campaña Braze para acceder a tu idioma Jacquard.<br><br>Puedes solicitarlo a tu administrador del éxito del cliente de Jacquard si aún no te lo ha proporcionado. |
| Currents | Para exportar datos a Currents, debe tener configurado [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) en su cuenta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Solicitar credenciales de Jacquard Amazon S3

Necesitará que Jacquard configure un cubo Amazon S3 dedicado para recibir sus eventos de seguimiento de clics desde Braze. Ponte en contacto con tu administrador del éxito del cliente de Jacquard para iniciar este proceso. Cuando se cree el contenedor, se te proporcionarán credenciales únicas para crear tu Current. 

### Paso 2: Crear corriente

1. En Braze, seleccione **Corrientes > Crear nueva corriente > Exportación de datos de Amazon S3**. 
2. A continuación, ponle un nombre a tu Corriente e introduce un correo electrónico de contacto.
3. Añada su ID de clave de acceso de Jacquard AWS y su clave de acceso secreta en el cuadro de credenciales. A continuación, añade "phrasee-braze-currents-exports" como nombre de contenedor de AWS S3. 
4. Por último, añade la carpeta del contenedor de S3 de AWS que recibiste de tu administrador del éxito del cliente de Jacquard. Probablemente será el nombre de su empresa.
5. En **Configuración general**, marque la casilla "Incluir eventos de usuarios anónimos" y, en **Gestionar eventos de compromiso**, marque "Clic por correo electrónico".
6. Cuando haya terminado, seleccione **Lanzar actual**.

### Paso 3: Solicitud de eliminación de información de identificación personal (PII).

A continuación, ponte en contacto con el equipo de tu cuenta Braze para asegurarte de que no se transmite a Jacquard ninguna información que pueda identificarte personalmente.

Por defecto, la Corriente incluirá ciertos atributos PII como el correo electrónico y la dirección. Jacquard no puede recibir ni recibirá PII, por lo que es fundamental que solicite al equipo de su cuenta Braze que desactive esta opción para cualquier dato de eventos que se transmita a Jacquard.

### Paso 4: Fragmentos de código de Jacquard X 

Ponte en contacto con el equipo de tu cuenta Jacquard para obtener los fragmentos de código necesarios.

Estos fragmentos aprovechan [el Contenido Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content) y, una vez colocados en sus correos electrónicos, extraerán dinámicamente el idioma y un píxel de seguimiento para que Jacquard pueda optimizar su idioma en tiempo real utilizando Jacquard X.


