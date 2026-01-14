---
nav_title: Tinyclues
article_title: Tinyclues
alias: /partners/tinyclues/
description: "Este artículo de referencia describe la asociación entre Braze y Tinyclues, que ofrece una característica de creación de audiencia para ayudarte a enviar a más campañas objetivo, encontrar nuevas oportunidades de productos y elevar los ingresos mediante una interfaz de usuario increíblemente fácil de usar."
page_type: partner
search_tag: Partner

---

# Tinyclues

> [Tinyclues](https://www.tinyclues.com/) es una característica de creación de audiencia que ofrece la capacidad de aumentar el número de campañas y los ingresos sin perjudicar la experiencia del cliente, así como análisis para hacer un seguimiento del rendimiento de las campañas de CRM, tanto online como offline.

La integración de Braze y Tinyclues ofrece a los usuarios un camino hacia una mejor planificación y estrategia de CRM, permitiendo a los usuarios enviar campañas más específicas, encontrar nuevas oportunidades de productos y aumentar los ingresos mediante una interfaz de usuario increíblemente fácil de usar.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta Tinyclues | Es necesario tener una cuenta en Tinyclues para beneficiarse de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de importación de datos

Para integrar Braze y Tinyclues, debes configurar la plataforma Tinyclues, exportar una campaña existente de Tinyclues y crear un segmento de cohorte de usuarios en Braze que pueda utilizarse para dirigirse a los usuarios en futuras campañas.

### Paso 1: Obtener la clave de importación de datos Braze

En Braze, ve a **Integraciones de socios** > **Socios tecnológicos** y selecciona **Tinyclues**. 

Aquí encontrarás tu punto final REST y generarás tu clave de importación de datos Braze. Una vez generada la clave, puede crear una nueva o invalidar una existente.<br><br>![]({% image_buster /assets/img/tinyclues/tinyclues_6.png %}){: style="max-width:90%;"} 

Para completar la integración, tendrás que proporcionar la clave de importación de datos y el punto final REST a tu equipo de operaciones de datos de Tinyclues. Tinyclues establecerá la conexión y se pondrá en contacto contigo una vez finalizada la configuración.

### Paso 2: Exportar una campaña desde la plataforma Tinyclues

Cada vez que quieras crear una cohorte de usuarios de Tinyclues para utilizarla en Braze, tendrás que exportarla primero desde la plataforma Tinyclues.

En Tinyclues, selecciona la campaña o campañas que quieras exportar y haz clic en **Exportar campañas**. Al exportarla, la audiencia se cargará automáticamente en tu cuenta de Braze.

![]({% image_buster /assets/img/tinyclues/tinyclues_1.png %})

### Paso 3: Crea un segmento a partir de la audiencia personalizada de Tinyclues

En Braze, ve a **Segmentos**, asigna un nombre al segmento de tu cohorte Tinyclues y selecciona **Cohortes Tinyclues** como filtro. Desde aquí, puedes elegir qué cohorte de Tinyclues deseas incluir. Una vez creado tu segmento de cohorte en Tinyclues, puedes seleccionarlo como filtro de audiencia al crear una campaña o Canvas.

![]({% image_buster /assets/img/tinyclues/tinyclues_3.png %}){: style="max-width:90%;"}<br><br>
![En el creador de segmentos Braze, el filtro de atributos de usuario "cohorte de Tinyclues" se establece en "incluye" y "cohorte principal".]({% image_buster /assets/img/tinyclues/tinyclues_4.png %}){: style="max-width:90%;"}

¿Tienes problemas para localizar tu cohorte? Consulta nuestra sección de [solución de problemas](#troubleshooting) para orientarte. 

{% alert important %}
Sólo se añadirán o eliminarán de una cohorte los usuarios que ya existan en Braze. La importación de cohortes no creará nuevos usuarios en Braze.
{% endalert %}

## Uso de esta integración

Para utilizar tu segmento de Tinyclues, crea una campaña Braze o Canvas y selecciona el segmento como tu audiencia objetivo. 

![En el constructor de campañas Braze, en el paso de segmentación, el filtro "Usuarios objetivo por segmento" se establece en "cohorte de Tinyclues".]({% image_buster /assets/img/tinyclues/tinyclues_5.png %}){: style="max-width:90%;"}

## Coincidencia de usuarios

Los usuarios identificados pueden coincidir por su `external_id` o `alias`. Los usuarios anónimos pueden ser emparejados por su `device_id`. Los usuarios identificados que fueron creados originalmente como usuarios anónimos no pueden ser identificados por su `device_id`, y deben ser identificados por su `external_id` o `alias`.

## Solución de problemas

¿Tienes problemas para encontrar la cohorte correcta dentro de la lista? En Tinyclues, visualiza los detalles de tu campaña y verifica el nombre marcando la casilla **Exportar nombre de archivo**.

![La parte inferior de la página de detalles de la campaña muestra el nombre de tu cohorte.]({% image_buster /assets/img/tinyclues/tinyclues_2.png %}){: style="max-width:30%;"}

¿Todavía tienes problemas para recuperar tu audiencia? Ponte en contacto con el [equipo de Tinyclues](mailto:support@tinyclues.com) para obtener ayuda adicional.

