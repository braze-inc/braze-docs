---
nav_title: Survicate
article_title: Survicate
description: "Este artículo de referencia describe la asociación entre Braze y Survicate, una plataforma de opiniones de clientes que te ayuda a recopilar, analizar y actuar sobre la información de los clientes en múltiples canales y a lo largo del recorrido del usuario."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

![Un ejemplo de lo que podría ser un cuestionario HTML incrustado (primera pregunta) en un correo electrónico Braze.]({% image_buster /assets/img/survicate/survicate_asset_1.png %}){: style="float:right;max-width:40%;border:0; margin-left:8px;"}

> [Survicate](https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter) es una plataforma de opiniones de clientes que te ayuda a recopilar, analizar y actuar sobre la información de los clientes en múltiples canales y a lo largo del recorrido del usuario.  

_Esta integración está mantenida por Survicate._

## Sobre la integración

Con la integración de Braze y Survicate, puedes incrustar cuestionarios directamente en tus correos electrónicos Braze para aumentar las tasas de respuesta. Las respuestas a los cuestionarios se sincronizan automáticamente con los perfiles de usuario Braze como atributos o eventos personalizados. La información en tiempo real facilita el seguimiento y el análisis de las opiniones junto con los datos de clientes y la creación de seguimientos específicos.

## Ejemplos

Braze y Survicate trabajan juntos para cubrir una amplia gama de casos de uso, ayudándote a recopilar información accionable de los usuarios y a mejorar la experiencia del cliente:

- Medir la satisfacción del cliente (como CSAT, NPS o CES)
- Recoger opiniones sobre el producto
- Realizar estudios de usuarios o de mercado
- Recopila información en las fases críticas del recorrido del cliente
- Desencadena flujos de trabajo personalizados y automatiza campañas de seguimiento basadas en las opiniones de los clientes.

## Características principales de la integración

La integración de Survicate y Braze ofrece sincronización de datos en tiempo real, por lo que la información más actualizada de los cuestionarios de Survicate está disponible inmediatamente en Braze. Basándote en las respuestas a los cuestionarios, puedes utilizar estos datos para emprender acciones oportunas y personalizadas.

- **Envía las respuestas de los cuestionarios a Braze como atributos personalizados de usuario**: Enriquece los perfiles de usuario de Braze con datos procedentes de respuestas a cuestionarios.
- **Desencadena eventos personalizados en Braze**: Utiliza eventos basados en respuestas a cuestionarios para dirigirte a grupos específicos o iniciar campañas de seguimiento.
- **Construye segmentos detallados**: Crea segmentos Braze utilizando los datos de los cuestionarios Survicate para personalizar aún más tu alcance.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Survicate | Necesitas una cuenta de Survicate para activar esta integración. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Crea tu cuestionario en Survicate

1. En tu panel de Survicate, selecciona **Crear nuevo cuestionario**.
2. Elige tu canal de encuesta: **correo electrónico, enlace, sitio web, encuestas en el producto y en la aplicación móvil**. 
3. Diseña tu cuestionario desde cero, utiliza el creador de cuestionarios de IA o selecciona entre más de 100 plantillas listas para usar.

![Cuatro opciones para crear un cuestionario: empezar desde cero, utilizar una plantilla, creación asistida por IA e importar preguntas.]({% image_buster /assets/img/survicate/survicate_asset_3.png %})

### Paso 2: Identifica automáticamente a los encuestados con los correos electrónicos Braze

1. Cuando tu cuestionario esté listo, ve a la pestaña **Configurar**.
2. Para *Identificar a los encuestados con*, selecciona **Braze**. Esto vincula automáticamente las respuestas a tus perfiles de cliente Braze, por lo que no hay necesidad de pedir datos de contacto en tu cuestionario.

![Se selecciona a Braze como encuestado.]({% image_buster /assets/img/survicate/survicate_asset_2.png %})

### Paso 3: Conecta la integración

1. A continuación, en la **pestaña Conectar**, busca Braze y selecciona **Conectar** para integrar. 
2. Introduce la clave de API del espacio de trabajo de tu cuenta Braze y la URL de la instancia de Braze.

![Campos para introducir la clave de API del espacio de trabajo y la URL de la instancia de Braze.]({% image_buster /assets/img/survicate/image1.png %})

### Paso 4: Comparte tu cuestionario

1. A continuación, en la pestaña **Compartir**, elige dónde quieres colocar tu cuestionario. Las opciones incluyen:
- **Enlace directo**: Copia el enlace para utilizarlo en Braze como botón o hipervínculo.
- **Embed primera pregunta**: Copia el código HTML para incrustar la primera pregunta del cuestionario directamente en el cuerpo de un correo electrónico Braze.
- **Lanza un cuestionario en tu sitio web o dentro del producto**: Instala el código de seguimiento una vez, y configura los cuestionarios en vivo directamente desde el panel de Survicate.

### Paso 5: Añade el cuestionario a tu campaña de correo electrónico Braze

1. En Braze, pega el enlace de la encuesta o el código HTML en el contenido de tu campaña de correo electrónico.
2. Empieza a recoger opiniones y haz un seguimiento de las respuestas directamente en Survicate.


