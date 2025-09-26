---
nav_title: Peak
article_title: Peak
description: "Este artículo de referencia describe la asociación entre Braze y Peak, una plataforma de inteligencia de decisiones, que permite predecir la probabilidad de cancelación y los atributos basados en los comportamientos e interacciones de los clientes, e importarlos a Braze para utilizarlos en la segmentación y selección de clientes."
alias: /partners/Peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://platform.peak.ai/), una plataforma de inteligencia de decisiones, es un sistema integral en el que la inteligencia de decisiones es la aplicación comercial de la IA para mejorar la toma de decisiones empresariales, aumentando los ingresos y los beneficios.

_Esta integración la mantiene Peak._

## Sobre la integración

La alianza entre Braze y Peak permite predecir la probabilidad de pérdida de clientes y los atributos basados en los comportamientos e interacciones de los clientes, e importarlos a Braze para utilizarlos en la segmentación y selección de clientes. 

## Requisitos previos

Como punto de partida, un inquilino de Peak debe alojar la integración entre Peak y Braze. Tradicionalmente se crea durante la incorporación de los clientes de Peak. Además, inicialmente se requiere una solución de inteligencia de decisiones, ya que genera los resultados basados en IA que posteriormente se integrarán en Braze.

| Requisito | Descripción |
| ----------- | ----------- |
| Inquilino de Peak | Se requiere una instancia de la plataforma Peak, conocida como inquilino (en inglés, tenant) para alojar y orquestar la integración. |
| Solución de inteligencia para la toma de decisiones | La integración entre Peak y Braze se basa en resultados impulsados por IA y, por lo tanto, requiere una solución desplegada por Peak o el cliente dentro de su inquilino. |
| Clave de API REST de Braze | Una clave de API REST de Braze con permisos `users.track`. <br><br>Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |

## Integración

La inteligencia de clientes de la solución Peak utiliza un modelo para predecir una serie de atributos prospectivos basados en los comportamientos e interacciones de los clientes. Estos atributos se almacenan en Peak y pueden utilizarse para generar una segmentación predictiva, incluida la probabilidad de que un cliente abandone. La actualización de estos atributos predictivos se basará en una cadencia configurable (diaria o semanal).

### Paso 1: Ejecutar el modelo y extraer los clientes

La integración se activa tras la ejecución del modelo de IA y el recálculo de los atributos predictivos del cliente. Estos resultados de IA se almacenan en Peak, incluso cuando un atributo se actualiza con un nuevo estado o valor.

En función de cuándo se han actualizado los atributos, se realiza una selección para recopilar todos los clientes con atributos predictivos actualizados desde la última sincronización entre Peak y Braze.

### Paso 2: Actualizar Braze

Con los clientes actualizados y los atributos asociados, Peak los enviará por POST a Braze mediante el [punto final`/user/track` ]({{site.baseurl}}/api/endpoints/user_data/post_user_track/), utilizando el encabezado [masivo]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates).

Al recibir los códigos de estado correctos de la API, Peak registrará la sincronización correcta entre Peak y Braze.

### Paso 3: Uso de esta integración

Una vez que la sincronización entre Peak y Braze se ha realizado correctamente, los usuarios actualizados incluyen ahora los nuevos atributos. Utiliza estos atributos en campañas y lienzos para dirigirte a los usuarios y personalizar los mensajes.


