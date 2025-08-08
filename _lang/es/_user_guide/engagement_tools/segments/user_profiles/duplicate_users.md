---
nav_title: Usuarios duplicados
article_title: Usuarios duplicados
description: "Aprenda a encontrar y fusionar usuarios duplicados en su panel Braze."
page_order: 0
---

# Duplicar usuarios

> Aprenda a encontrar y fusionar usuarios duplicados, para que pueda maximizar la eficacia de sus campañas y Canvases.

{% alert tip %}
Para fusionar usuarios duplicados utilizando la API REST de Braze, consulta [POST: Fusionar usuarios]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/).
{% endalert %}

## Fusión individual

Si una búsqueda de usuarios devuelve perfiles duplicados, puede fusionar cada perfil individualmente desde el perfil del usuario en el panel Braze.

### Paso 1: Buscar un perfil duplicado

En Braze, seleccione **Audiencia** > **Búsqueda de usuarios**.

![Azulejo "Búsqueda de usuarios" resaltado en el menú de navegación.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_search_users.png %}){: style="max-width:60%;"}

Introduzca un identificador único, como una dirección de correo electrónico o un número de teléfono, para el perfil duplicado y, a continuación, seleccione **Buscar**.

![La página de "Búsqueda de usuarios" en el panel de Braze.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/search_user.png %}){: style="max-width:60%;"}

### Paso 2: Fusionar duplicados

Para iniciar el proceso de fusión, selecciona **Fusionar duplicados**.

![Uno de los perfiles del usuario duplicado.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_duplicates.png %}){: style="max-width:50%;"}

Elija qué perfil de usuario desea conservar y cuál fusionar y, a continuación, seleccione **Fusionar perfiles**. Repita este proceso hasta que haya fusionado todos los perfiles duplicados.

![La página de fusión individual de un perfil duplicado.]({% image_buster /assets/img/audience_management/duplicate_users/individual_merging/select_merge_profiles.png %}){: style="max-width:80%;"}

{% alert warning %}
Los perfiles de usuario duplicados no pueden recuperarse tras la fusión.
{% endalert %}

## Fusión masiva

Al fusionar usuarios duplicados de forma masiva, Braze busca perfiles con identificadores coincidentes (como una dirección de correo electrónico) y fusiona todos sus datos en el perfil actualizado más recientemente con un `external_id`. Si no hay perfiles con `external_id`, se utilizará en su lugar el perfil actualizado más recientemente sin `external_id`.

### Paso 1: Ir a Gestionar audiencia

En el panel de control de Braze, seleccione **Audiencia** > **Gestionar audiencia**.

![El mosaico "Gestionar audiencia" aparece resaltado en el menú de navegación.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_manage_audience.png %}){: style="max-width:60%;"}

### Paso 2: Vista previa de los resultados (opcional)

Para previsualizar los resultados antes de fusionar los duplicados, seleccione **Generar lista de duplicados**.

![La página "Gestionar audiencia" con la opción "Generar lista de duplicados" resaltada.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_generate_list.png %})

Braze generará su vista previa y se la enviará a su dirección de correo electrónico como archivo CSV.

![Un correo electrónico de Braze con un enlace al archivo CSV generado.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/example_email.png %}){: style="max-width:60%;"}

En el siguiente ejemplo, Braze utiliza el ID externo del usuario para marcar perfiles duplicados e identificar cuál conservar. Si estos perfiles se fusionan de forma masiva, Braze utilizará el perfil con un ID externo como nuevo perfil principal del usuario.

{% tabs local %}
{% tab ejemplo de fichero csv %}
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

### Paso 3: Fusiona tus duplicados

Si está satisfecho con los resultados de la vista previa, seleccione **Fusionar todos los duplicados**.

{% alert warning %}
Los perfiles de usuario duplicados no pueden recuperarse tras la fusión.
{% endalert %}

![La página "Gestionar audiencia" con la opción "Fusionar todos los duplicados" resaltada.]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_merge_profiles.png %}){: style="max-width:70%;"}

## Fusión basada en reglas

Puede utilizar reglas para controlar cómo se resuelven los perfiles duplicados al ejecutar una fusión, de modo que se mantenga el perfil de usuario más relevante. Una vez establecidas las reglas, Braze conservará los perfiles que coincidan con sus criterios.

### Paso 1: Define tus reglas

1. Vaya a **Audiencia** > **Gestionar audiencia** > **Editar reglas**.
2. En la sección **Perfil a conservar** del panel **Editar reglas**, seleccione el **Identificador** de los perfiles que se conservarán al fusionar duplicados. Puede ser la dirección de correo electrónico o el número de teléfono.
3. En la sección **Resolver vínculos**, seleccione los criterios para determinar cómo resolver los vínculos entre perfiles con criterios coincidentes de **Perfil a mantener**. Puede seleccionar lo siguiente:<br>
- **Resuelve los empates utilizando**: Fecha de creación, Fecha de actualización, Última sesión
- **Priorización**: Más reciente, Más antiguo

![El panel "Editar reglas" con secciones para seleccionar opciones de "Perfil a mantener" y "Resolver vínculos".]({% image_buster /assets/img/audience_management/duplicate_users/edit_rules.png %}){: style="max-width:40%;"}

Por ejemplo, podrías conservar el perfil que tiene un número de teléfono. Si varios usuarios tienen el mismo número de teléfono, podría resolver los empates utilizando el campo **Fecha de actualización** y dar prioridad al usuario actualizado más recientemente.

### Paso 2: Vista previa de los resultados (opcional)

Después de guardar sus reglas, puede previsualizar cómo funcionarán seleccionando **Generar una lista de duplicados**. Braze generará su vista previa y se la enviará a su dirección de correo electrónico como un archivo CSV que muestra qué usuarios se conservarían y fusionarían si se aplicaran sus reglas. 

### Paso 3: Fusionar duplicados

Si está satisfecho con los resultados de la vista previa, vuelva a la página **Gestionar público** y seleccione **Fusionar todos los duplicados**.

{% alert warning %}
Los perfiles de usuario duplicados no pueden recuperarse tras la fusión.
{% endalert %}

## Fusión programada

Similar a la fusión basada en reglas, la fusión programada te permite automatizar la fusión de perfiles de usuario diariamente mediante reglas preconfiguradas.

![La página "Gestionar audiencia" con el botón "programar".]({% image_buster /assets/img/audience_management/duplicate_users/bulk_merging/select_scheduled_merge_rules.png %})

Una vez activada la característica, Braze asignará automáticamente una franja horaria para realizar el proceso de fusión diariamente, aproximadamente a las 12 de la mañana en la zona horaria de la empresa del usuario. Puedes desactivar la fusión programada en cualquier momento. Braze notificará a los administradores de tu espacio de trabajo 24 horas antes de que se produzca la fusión programada, proporcionando un recordatorio y tiempo para revisar la configuración.

{% alert warning %}
Los perfiles de usuario duplicados no pueden recuperarse tras la fusión.
{% endalert %}
