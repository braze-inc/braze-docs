---
nav_title: Odicci
article_title: Odicci
description: "Guía paso a paso para integrar Odicci con Braze para campañas de marketing personalizadas"
alias: /partners/odicci/
page_type: partner
search_tag: Partner
---

# Integración de Odicci con Braze

> Aprende a integrar Braze con [Odicci](https://www.odicci.com/), una plataforma que permite a las empresas captar, fidelizar y retener a sus clientes mediante experiencias omnicanales basadas en la fidelización.

{% alert tip %}
Consulta el [Centro de Ayuda de Odicci](https://help.odicci.com) para obtener más recursos y preguntas frecuentes.
{% endalert %}

## Ejemplos

Puedes conectar la plataforma Odicci con Braze para compartir datos y gestionar campañas fácilmente, lo que incluye:

- Envío automático a Braze de los datos de audiencia recogidos en las experiencias Odicci.
- Desencadenar campañas de marketing personalizadas basadas en las interacciones de los usuarios.
- Mapeado de campos entre Odicci y Braze para garantizar una sincronización precisa de los datos.

## Ejemplo

Un comercio minorista utiliza las experiencias gamificadas de Odicci para recopilar direcciones de correo electrónico para una campaña de marketing.

1. Un cliente completa un juego en Odicci, facilitando su dirección de correo electrónico.
2. Odicci sincroniza automáticamente estos datos con Braze.
3. Braze desencadena un correo electrónico personalizado de "Gracias" e incluye un código de descuento.

## Requisitos previos

Antes de empezar, necesitarás lo siguiente:

| Requisito previo             | Descripción                                                               |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Un relato de Odicci            | Se requiere una cuenta de Odicci con acceso a la sección **Integraciones** para aprovechar esta integración.|
| Clave de API REST de Braze        | Una clave de API REST de Braze con los permisos `users.track` y 'campaigns.list'. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración de Odicci

### Paso 1: Habilitar la integración en Odicci

1. Accede a tu cuenta Odicci.
2. Ve a la sección **Configuración > Integraciones**.
3. Busca la integración **Braze** y haz clic en **Conectar**.

   ![Conectar Integración Braze]({% image_buster /assets/img/odicci/braze_connect.png %})

4. Introduce tu clave de API REST Braze en el campo correspondiente.
5. Guarda la configuración para activar la integración a nivel de cuenta.

### Paso 2: Obtén tu clave de API REST Braze

1. Accede a tu cuenta Braze.
2. Ve a **Consola para desarrolladores > Claves de API REST.**
3. Crea una nueva clave de API o copia una existente con el permiso `users.track`.

### Paso 3: Activar la integración a nivel de experiencia

1. Crea o abre una **Experiencia** en Odicci Studio.
2. Ve a **Studio > Configuración > Integraciones.**
3. Localiza la casilla **Braze** y márcala para activar la integración para la experiencia.
4. Guarda los cambios.

### Paso 4: Campos mapeados

1. Tras activar la integración, permanece en la sección **Estudio > Configuración > Integraciones**.
2. Mapea los campos de tu experiencia Odicci (e.g., `Email`, `Name`) a sus campos correspondientes en Braze.
3. Guarda tu configuración.

   ![Configuración del mapeado de campos]({% image_buster /assets/img/odicci/braze_field_mapping.png %})

### Paso 5: Probar la integración

1. Ejecuta la experiencia en Odicci para recopilar datos de prueba.
2. Verifica que los datos se sincronizan correctamente con Braze comprobando el panel de Braze o los registros de datos.
3. Asegúrate de que los campos mapeados se rellenan correctamente en Braze.

## Solución de problemas

Si tienes problemas con la integración, considera las siguientes soluciones. Si necesitas más ayuda, ponte en contacto con [el servicio de asistencia de Odicci](https://help.odicci.com).

### La clave de API no es válida

Comprueba dos veces tu clave de API Braze y asegúrate de que tiene los permisos necesarios. A continuación, vuelve a introducir la clave de API en la configuración de integración de Odicci.

### Los datos no se sincronizan

Comprueba que los campos de la sección **Mapeado de campos** están correctamente configurados. A continuación, asegúrate de que la clave de API tiene permisos para la importación de datos de usuarios.

### Campaña no desencadenada

Comprueba la configuración de la campaña Braze para asegurarte de que la audiencia o las condiciones de desencadenamiento son correctas.
