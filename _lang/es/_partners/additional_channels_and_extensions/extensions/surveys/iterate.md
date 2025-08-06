---
nav_title: Iterate
article_title: Iterate
alias: /partners/iterate/
description: "Este artículo de referencia describe la asociación entre Braze e Iterate, que le permite enriquecer los datos de los clientes utilizando encuestas para añadir información adicional."
page_type: partner
search_tag: Partner

---

# Iterate

> [Iterate](https://iteratehq.com) facilita el aprendizaje de sus clientes, ofreciendo herramientas de investigación inteligentes y fáciles de usar que se parecen a su marca.

_Esta integración la mantiene Iterate._

## Sobre la integración

La integración de Iterate con Braze le permite entregar encuestas Iterate de forma nativa y sin problemas dentro de su producto o campañas. Las respuestas a las encuestas pueden registrarse como atributos de usuario personalizados en Braze, lo que le permite construir una imagen completa de sus usuarios o crear nuevas y potentes audiencias y segmentos.

Con el SDK de Braze instalado en su aplicación o sitio web, puede utilizar las herramientas de segmentación y orientación disponibles en Braze para enviar encuestas a través de mensajes integrados en la aplicación a una parte específica de su audiencia en función de cualquier activador o segmento personalizado. Las encuestas de Iterate también pueden incrustarse directamente en sus campañas de correo electrónico o incluirse como enlaces en sus campañas push o de otro tipo.

## Requisitos previos

| Requisito | Origin |
|---|---|
|Cuenta Iterate | Se necesita una [cuenta de Iterate](https://iteratehq.com) para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave de API REST de Braze con permisos `users.track`. Para enviar cuestionarios a través de mensajes dentro de la aplicación Braze, también necesitarás el permiso `kpi.mau.data_series`.<br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**.|
| Punto final REST Braze  | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos prácticos

Con Iterate, puedes recopilar casi cualquier tipo de datos. Desde información personal (nombre, edad, correo electrónico), datos de rendimiento (NPS, satisfacción del cliente, puntuaciones con estrellas), preferencias (dispositivo preferido, frecuencia de comunicación preferida) o personalidad (libro, perro o gato favoritos). Lo que preguntes depende enteramente de ti, y del tipo de datos que quieras recopilar o de audiencias que quieras crear.

## Integración

### Para empezar: Conectar Braze con Iterate

Inicie sesión en su cuenta de Iterate y añada su punto final Braze REST y su clave API REST en la página **Configuración de la empresa**.

### Envíe las encuestas como un mensaje dentro de la aplicación

#### Paso 1: Crea tu cuestionario

Antes de crear tu encuesta, activa la opción **Activar encuestas por mensaje dentro de la aplicación** en la configuración de Iterate.

A continuación, cree una nueva encuesta en Iterate y añada las preguntas pertinentes. Si lo considera oportuno, también puede incluir un mensaje de aviso que se mostrará antes de la encuesta. Seleccione **Enviar a través de Braze In-App Message** como tipo de encuesta.

Una vez completada la encuesta, en la pestaña **Publicar**, copie el fragmento de código que aparece en **Copiar y pegue el código de incrustación**.

#### Paso 2: Comparte tu cuestionario

En Braze, crea una nueva campaña de mensajería dentro de la aplicación, selecciona **Código personalizado** como tipo de mensajería y pega tu fragmento de código en el mensaje. A continuación, seleccione **Esperar a que el usuario se retire** como comportamiento del mensaje al hacer clic.

Continúa configurando tu campaña como lo harías con cualquier otra campaña de mensajería dentro de la aplicación, eligiendo un método de entrega y dirigiéndote a una audiencia.

### Envíe encuestas por correo electrónico o push

#### Paso 1: Crea tu cuestionario

Cree una nueva encuesta por correo electrónico o enlace en Iterate y añada las preguntas pertinentes de la encuesta. Una vez redactadas las preguntas y personalizado el diseño, seleccione **Enviar encuesta > Integraciones > Braze**.

A continuación, verás las opciones de configuración para enviar respuestas a Braze. Active la integración para poder enviar las respuestas de esa encuesta a Braze. 

#### Paso 2: Comparte tu cuestionario

Su encuesta puede compartirse de dos maneras: incrustando la primera pregunta en su mensaje o incluyendo un enlace directo a la encuesta en la plataforma Iterate.

![Iterar opciones de enlace]({% image_buster /assets/img/iterate.png %})

- **Incrustar el código**
  - Copie el fragmento de código en **Código de incrustación de correo electrónico** dentro de la sección de integración Braze de la pestaña **Enviar encuesta**. Inserte el código en el HTML de su correo electrónico Braze donde desee que aparezca el comienzo de la encuesta. 
  - Si tiene dificultades para mostrar las preguntas de la encuesta o si no tienen el formato correcto, deberá ir a la pestaña **Información de envío** en el compositor de mensajes y desmarcar **CSS en línea**.
- **Incluir un enlace**
  - Copie el enlace que aparece en **Enlace de encuesta** en la sección Integración Braze de la pestaña **Enviar encuesta**. Tenga en cuenta que el líquido incluido en el enlace {% raw %}`?user_braze_id={{${braze_id}}}`{% endraw %} se sustituirá automáticamente para cada usuario al enviarlo.

### Próximos pasos: Crea campañas de seguimiento

A medida que los usuarios respondan, verás cómo sus perfiles se llenan de datos en tiempo real. Estos datos pueden utilizarse para segmentar a los usuarios y enviar campañas de seguimiento personalizadas. Por ejemplo, si envía la pregunta "¿Le gustan nuestros productos?", puede crear segmentos de usuarios que tengan el atributo de usuario personalizado `Do you enjoy our products?` que hayan respondido "Sí" o "No" y dirigirse a estos usuarios.

## Eventos personalizados Braze

Cuando un usuario responde a una pregunta de la encuesta, Iterate activa un evento personalizado dentro de Braze denominado `survey-question-response`. Los eventos personalizados le permiten activar cualquier número y tipo de campañas de seguimiento.

## Personalizar los nombres de los atributos de usuario

Por defecto, el atributo de usuario creado para una pregunta es el mismo que el prompt.
En algunos casos, es posible que desee personalizarlo. Para ello, haga clic en el menú desplegable **Personalizar nombres de atributos de usuario** en el paso **Crear su encuesta** e introduzca los nombres personalizados que desee.


