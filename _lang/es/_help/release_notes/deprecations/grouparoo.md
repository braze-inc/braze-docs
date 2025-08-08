---
nav_title: Grouparoo
page_order: 1
description: "Este artículo describe la asociación entre Braze y Grouparoo, una herramienta de ETL inversa de código abierto que facilita la alimentación de sus herramientas de marketing, ventas y asistencia utilizando los datos de su almacén de datos."
page_type: update

---

# Grouparoo

{% alert update %}
La compatibilidad con Grouparoo se interrumpió a partir de abril de 2022.
{% endalert %}

> [Grouparoo](https://www.grouparoo.com/) es una herramienta ETL inversa de código abierto que facilita el uso de los datos de su almacén en sus herramientas de marketing, ventas y asistencia. La configuración se realiza en una interfaz de usuario centrada en el modelo, lo que permite a los miembros no técnicos del equipo configurar y programar sincronizaciones de datos en apoyo de las operaciones.

La integración de Braze y Grouparoo facilita la explotación de los datos almacenados en un almacén enviándolos a Braze. Cuando configuras programas de sincronización automática, puedes mejorar constantemente las comunicaciones con los clientes con información actualizada.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta y proyecto Grouparoo | Para beneficiarse de esta asociación es necesario disponer de una cuenta y un proyecto de Grouparoo.<br><br>Esta integración es posible utilizarla con la edición comunitaria gratuita y las soluciones empresariales proporcionadas por Grouparoo. La configuración tendrá lugar en la interfaz de usuario de configuración de Grouparoo. |
| Clave de API REST de Braze | Una clave de API REST de Braze con usuarios y permisos de seguimiento. <br><br> Puede crearse en el dashboard de Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST](https://www.grouparoo.com/). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1: Crear una aplicación Braze en Grouparoo

En Grouparoo, ve a **Aplicaciones** y selecciona **Braze** para crear una nueva aplicación Braze. En el modal que aparece, proporcione su clave de API Braze y el punto final REST.

![]({% image_buster /assets/img/grouparoo/add-app.png %})

### Paso 2: Configurar un modelo y una fuente de datos

Esta integración requiere que tenga un modelo existente y una fuente de datos configurada antes de continuar con el siguiente paso. Si no lo tiene configurado, visite la documentación de Grouparoo para aprender a configurar un [modelo](https://www.grouparoo.com/docs/config/models) y una [fuente de datos](https://www.grouparoo.com/docs/config/sources).

### Paso 3: Crear un destino Braze en Grouparoo

#### Selecciona el modo de sincronización

En Grouparoo, selecciona tu modelo en la barra de navegación. A continuación, desplácese hasta la sección **Destinos** y haga clic en **Añadir nuevo destino**.

A continuación, selecciona la aplicación **Braze** que has creado, asigna un nombre al destino y selecciona el modo de sincronización que desees de entre los siguientes:
- **Sincronización**: Añada, actualice y elimine usuarios de Braze según sea necesario. Esta opción busca nuevos registros, cambios en registros existentes y eliminaciones.
- **Adición**: Añade y actualiza los usuarios de Braze según sea necesario, pero no elimines a nadie. Esta opción busca nuevos usuarios para añadir a Braze y cambios en los usuarios Braze existentes, pero no realiza un seguimiento de las eliminaciones.
- **Enriquecimiento**: Actualice sólo los usuarios que ya existen en Braze. No añada ni elimine usuarios. Esta opción sólo actualizará los usuarios existentes en Braze.

#### Asignación de campos de propiedad

A continuación, debe asignar campos de propiedad Grouparoo a campos de propiedad Braze. 

![Ejemplo de campos de asignación de propiedades. Grouparoo userID está configurado para mapeado a external_id. email, firstName y lastName están configurados como campos grouparoo equivalentes a "email", "first_name" y "last_name".]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Asegúrese de que el campo Braze `external_id` está asignado a la clave primaria de su tabla de origen. Asigne el resto de los campos según sea necesario para su caso de uso.

Sección **Propiedades del registro de envío**: Una lista de campos de perfil de usuario preestablecidos disponibles para asignar datos. Cualquiera de estos puede ser sincronizado desde las propiedades de Grouparoo.

Sección **opcional de campos de perfil de usuario de Braze**: Crear campos de perfil de usuario Braze personalizados opcionales. Si hace clic en **Añadir nuevo campo de perfil de usuario Braze**, verá todas las propiedades disponibles que puede asignar a Braze. El nombre de cualquier campo nuevo que cree será el mismo que el de la propiedad Grouparoo, pero puede cambiarle el nombre.

#### Grupos Grouparoo

Además de la asignación, también puede optar por añadir grupos Grouparoo a los grupos de suscripción Braze. 

![En "Grupos de suscripción Braze" de la ventana de configuración del destino Grouparoo, el grupo Grouparoo "Alto valor con compra reciente de automóvil" se añadirá al grupo de suscripción Braze "Alto valor con compra reciente de automóvil".]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
Encontrará más detalles y actualizaciones sobre esta integración en [la documentación de Grouparoo](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}

