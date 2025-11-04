---
nav_title: Duplicar usuarios
article_title: Usuarios duplicados
description: "Aprende a encontrar y fusionar usuarios duplicados en tu panel de Braze."
page_order: 0
---

# Duplicar usuarios

> Aprende a encontrar y fusionar usuarios duplicados, para que puedas maximizar la eficacia de tus campañas y Lienzos.

{% alert tip %}
Para fusionar usuarios duplicados utilizando la API REST de Braze, consulta [POST: Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% endalert %}

## Fusión individual

Si una búsqueda de usuarios devuelve perfiles duplicados, puedes fusionar cada perfil individualmente desde el perfil del usuario en el panel Braze.

### Paso 1: Buscar un perfil duplicado

En Braze, selecciona **Audiencia** > **Búsqueda de usuarios**.

Mosaico de "Búsqueda de usuarios" destacado en el menú de navegación.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Introduce un identificador único, como una dirección de correo electrónico o un número de teléfono, para el perfil duplicado y, a continuación, selecciona **Buscar**.

Página de "Búsqueda de usuarios" en el panel de Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Paso 2: Fusionar duplicados

Para iniciar el proceso de fusión, selecciona **Fusionar duplicados**.

\![Uno de los perfiles de usuario duplicados.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Elige qué perfil de usuario conservar y cuál fusionar y, a continuación, selecciona **Fusionar perfiles**. Repite este proceso hasta que hayas fusionado todos los perfiles duplicados.

Página de fusión individual de un perfil duplicado.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
Los perfiles de usuario duplicados no pueden recuperarse tras la fusión.
{% endalert %}

## Fusión masiva

Cuando fusionas usuarios duplicados de forma masiva, Braze encuentra perfiles con identificadores coincidentes (como una dirección de correo electrónico) y fusiona todos sus datos en el perfil actualizado más recientemente con un `external_id`. Si no hay perfiles con `external_id`, se utilizará en su lugar el perfil actualizado más recientemente sin `external_id`.

### Paso 1: Ir a Administrar audiencia

En el panel de Braze, selecciona **Audiencia** > **Gestionar audiencia**.

\![El azulejo "Gestionar audiencia" resaltado en el menú de navegación.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Paso 2: Vista previa de los resultados (opcional)

Para obtener una vista previa de los resultados antes de fusionar los duplicados, selecciona **Generar lista de duplicados**.

La página "Gestionar audiencia" con la opción "Generar lista de duplicados" resaltada.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze generará tu vista previa y te la enviará a tu dirección de correo electrónico como un archivo CSV.

Un correo electrónico de Braze con un enlace al archivo CSV generado.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

En el siguiente ejemplo, Braze utiliza el ID externo del usuario para marcar los perfiles duplicados e identificar cuál conservar. Si estos perfiles se fusionan en bloque, Braze utilizará el perfil con un ID externo como nuevo perfil principal del usuario.

{% tabs local %}
{% tab example csv file %}
| Dirección de correo electrónico | ID externo | Número de teléfono | ID de Braze | Identificador para la regla | Perfil para conservar | Perfil para fusionar |
| ---------------- | ----------- | -------------- | --------------------- | ------------------- | --------------- | ---------------- |
| alex@company.com | A8i3mkd99 | (555) 123-4567 | 65fcaa547f470494d1370 | correo electrónico | TRUE | FALSE |
| alex@company.com | | (555) 987-6543 | 65fcaa547f47d004d1348 | correo electrónico | FALSE | TRUE |
| alex@company.com | | (555) 321-0987 | 65fcaa547f47d0049135c | correo electrónico | FALSE | TRUE |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }
{% endtab %}
{% endtabs %}

#### Comportamiento de la fusión

Braze rellenará los campos vacíos del perfil conservado con los valores del perfil fusionado. Para ver una lista de los campos que se rellenarán, consulta [Comportamiento de la fusión]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/#merge-behavior).

### Paso 3: Fusiona tus duplicados

Si estás satisfecho con los resultados de la vista previa, selecciona **Fusionar todos los duplicados**.

{% alert warning %}
Los perfiles de usuario duplicados no pueden recuperarse tras la fusión.
{% endalert %}

La página "Gestionar audiencia" con la opción "Fusionar todos los duplicados" resaltada.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## Fusión basada en reglas

Puedes utilizar reglas para controlar cómo se resuelven los perfiles duplicados al ejecutar una fusión, de modo que se mantenga el perfil de usuario más relevante. Una vez establecidas las reglas, Braze conservará los perfiles que coincidan con tus criterios.

### Paso 1: Define tus normas

1. Ve a **Audiencia** > **Gestionar audiencia** > **Editar reglas**.
2. En la sección **Perfil a conservar** del panel **Editar reglas**, selecciona el **Identificador** de los perfiles que se conservarán al fusionar duplicados. Puede ser la dirección de correo electrónico o el número de teléfono.
3. En la sección **Resolver vínculos**, selecciona los criterios para determinar cómo resolver los vínculos entre perfiles con criterios coincidentes de **Perfil a mantener**. Puedes seleccionar lo siguiente:<br>
- **Resuelve los empates utilizando**: Fecha de creación, Fecha de actualización, Última sesión
- **Priorización**: Más reciente, Más antiguo

\![El panel "Editar reglas" con secciones para seleccionar opciones de "Conservar perfil" y "Resolver vínculos".]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

Por ejemplo, podrías conservar el perfil que tiene un número de teléfono. Si varios usuarios tienen el mismo número de teléfono, podrías resolver los empates utilizando el campo **Fecha de actualización** y dar prioridad al usuario actualizado más recientemente.

### Paso 2: Vista previa de los resultados (opcional)

Después de guardar tus reglas, puedes previsualizar cómo funcionarán seleccionando **Generar una lista de duplicados**. Braze generará tu vista previa y te la enviará a tu dirección de correo electrónico como un archivo CSV que muestra qué usuarios se mantendrían y fusionarían si se aplicaran tus reglas. 

### Paso 3: Fusionar duplicados

Si estás satisfecho con los resultados de la vista previa, vuelve a la página **Gestionar audiencia** y selecciona **Fusionar todos los duplicados**.

{% alert warning %}
Los perfiles de usuario duplicados no pueden recuperarse tras la fusión.
{% endalert %}

## Fusión programada

Similar a la fusión basada en reglas, la fusión programada te permite automatizar la fusión de perfiles de usuario diariamente mediante reglas preconfiguradas.

La página "Gestionar audiencia" con el botón "programar".]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

Una vez activada la característica, Braze asignará automáticamente una franja horaria para realizar el proceso de fusión diariamente, aproximadamente a las 12 de la mañana en la zona horaria de la empresa del usuario. Puedes desactivar la fusión programada en cualquier momento. Braze notificará a los administradores de tu espacio de trabajo 24 horas antes de que se produzca la fusión programada, proporcionando un recordatorio y tiempo para revisar la configuración.

{% alert warning %}
Los perfiles de usuario duplicados no pueden recuperarse tras la fusión.
{% endalert %}
