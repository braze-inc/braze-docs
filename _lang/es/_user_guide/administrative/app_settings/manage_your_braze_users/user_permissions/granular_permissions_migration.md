---
nav_title: Migración de permisos granulares
article_title: Migración a permisos granulares
page_order: 3
page_type: reference
alias: /granular_permissions_migration/
description: "Este artículo de referencia explica cómo prepararse para la migración a permisos de usuario granulares en Braze."
tool: Dashboard
---

# Migración a permisos granulares

> Gestionar quién puede acceder a tu cuenta y realizar acciones específicas es fundamental tanto para la seguridad como para la eficiencia operativa. Para ofrecerte un mayor control, Braze introduce permisos granulares, una forma más flexible y precisa de gestionar el acceso de los usuarios a tu cuenta.

La migración incluye las siguientes ventajas:

- **Control más preciso:** Los permisos granulares ofrecen más control, mayor seguridad y una supervisión más clara. Los usuarios solo obtienen el acceso que necesitan.
- **Mapeado automático:** Todos los permisos actuales están mapeados automáticamente a sus [equivalentes granulares](#legacy-to-granular-permissions-mapping). Tus usuarios mantendrán el mismo nivel de acceso a menos que tú lo cambies.

## Qué revisar

Cuando se planifique la migración para tu empresa, los administradores de Braze recibirán correos electrónicos y banners en el panel de control notificándoles la migración de permisos granulares. Para prepararte para la migración, recomendamos que un administrador de Braze haga lo siguiente.

1. Identifica los usuarios, roles o conjuntos de permisos que puedan necesitar actualizarse para obtener un acceso más personalizado después de la migración al nuevo marco de permisos. 
2. Si tu empresa ha realizado la automatización del aprovisionamiento de usuarios mediante SCIM o herramientas de cumplimiento que se basan en [cadenas de permisos]({{site.baseurl}}/scim_api_appendix/), actualízalas para que se ajusten a la nueva estructura granular. 
3. Informa a tus usuarios de Braze de cualquier cambio próximo para evitar confusiones.
4. En la fecha y hora programadas para la migración, tu empresa migrará automáticamente a permisos granulares. No es necesario que los administradores de la empresa realicen ninguna otra acción.

{% alert important %}
La posibilidad de actualizar los permisos se bloqueará 15 minutos antes de la hora prevista para la migración. Esto significa que no podrás cambiar ningún permiso hasta que finalice la migración, lo que prevemos que tardará hasta 15 minutos.
{% endalert %}

## Mapeo de permisos granulares heredados

Esta tabla muestra cómo están mapados cada uno de los permisos heredados con los permisos granulares. Consulta esta tabla mientras actualizas tus permisos. Por ejemplo, para conceder a un usuario el mismo acceso que el permiso heredado «Gestionar configuración de correo electrónico», ese usuario debe tener los permisos granulares «Ver configuración de correo electrónico» y «Editar configuración de correo electrónico».

| | Permisos heredados | Permisos granulares |
|---------------|---------------|---------------|
| **Nivel** | **Apellidos** | **Apellidos** |
| Administrador | Administrador | Administrador |
| Espacio de trabajo | Administrador del espacio de trabajo | Administrador del espacio de trabajo |
| Empresa | Crear y eliminar espacios de trabajo | Crear y eliminar espacios de trabajo |
| Empresa | Administrar configuración de empresa | Administrar configuración de empresa |
| Espacio de trabajo | Acceda a Campañas, Lienzos, Tarjetas, Bloques de contenido, Banderas de características, Segmentos, Mediateca, Ubicaciones, Códigos de promoción y Centros de preferencias. | Ver campañas<br>Editar campañas<br>Archivar campañas<br>Ver Canvas<br>Editar Canvas<br>Archivar Canvas<br>Ver las reglas de limitación de frecuencia<br>Editar reglas de limitación de frecuencia<br>Ver priorización de mensajes<br>Editar priorización de mensajes<br>Ver bloques de contenido<br>Ver las feature flags<br>Editar conmutador de características<br>Archiva feature flags<br>Ver segmentos<br>Editar segmentos<br>Editar grupo de control global<br>Ver plantillas IAM<br>Editar plantillas IAM<br>Archivar plantillas IAM<br>Ver plantillas de correo electrónico<br>Editar plantilla de correo electrónico<br>Archivar plantillas de correo electrónico<br>Ver plantillas webhook<br>Editar plantillas webhook<br>Archivar plantillas webhook<br>Ver plantillas de enlaces<br>Editar plantillas de enlaces<br>Ver activos de la biblioteca de medios<br>Ver ubicaciones<br>Editar ubicaciones<br>Ubicación de los archivos<br>Ver códigos promocionales<br>Editar códigos promocionales<br>Códigos promocionales de las exportaciones<br>Ver centros de preferencia<br>Editar centros de preferencia<br>Editar informes<br>Ver plantillas de banners<br>Ver configuración multilingüe<br>Utilizar operador<br>Ver agentes de Decisioning Studio<br>Ver evento de conversión de Decisioning Studio |
| Espacio de trabajo | Acceso a la consola para desarrolladores | Ver las claves de API<br>Editar claves de API<br>Ver grupos internos<br>Editar grupos internos<br>Eliminar grupos internos<br>Ver registro de actividad de mensajes<br>Ver registro de usuarios del evento<br>Ver identificadores de la API<br>Ver panel de uso de la API<br>Ver límites de la API<br>Ver alertas de uso de la API<br>Editar alertas de uso de la API<br>Ver depurador de SDK<br>Editar depurador de SDK |
| Espacio de trabajo | Aprobar y denegar campañas | Aprobar campañas |
| Espacio de trabajo | Aprobar y denegar Canvas | Aprobar Canvas |
| Espacio de trabajo | Exportar datos de usuario | Exportar datos de usuario |
| Espacio de trabajo | Importar y actualizar datos de usuario | Ver Importar usuarios<br>Importar usuarios<br>Editar datos de usuario |
| Espacio de trabajo | Editar segmentos | Archivar segmentos |
| Espacio de trabajo | Lanzar y administrar bloques de contenido | Editar bloque de contenido<br>Archivar bloques de contenido<br>Lanzar bloques de contenido |
| Espacio de trabajo | Administrar la biblioteca multimedia | Editar activos de la biblioteca de medios<br>Eliminar activos de la biblioteca de medios |
| Espacio de trabajo | Lanzar centros de preferencias | Lanzar centros de preferencias |
| Espacio de trabajo | Administrar aplicaciones | Ver configuración de la aplicación<br>Editar configuración de la aplicación<br>Ver configuración push<br>Editar configuración push<br>Editar plantillas de banners<br>Plantillas de banners de archivo |
| Espacio de trabajo | Administrar permisos para el dashboard de catálogos | Ver catálogos<br>Editar catálogos<br>Exportar catálogos<br>Eliminar catálogos |
| Espacio de trabajo | Administrar usuarios del dashboard | Editar usuarios del panel |
| Espacio de trabajo | Administrar configuración del correo electrónico | Ver configuración del correo electrónico<br>Editar configuración de correo electrónico |
| Espacio de trabajo | Administrar eventos, atributos, compras | Ver atributos personalizados<br>Editar atributos personalizados<br>Atributos personalizados de la lista de bloqueo<br>Eliminar atributos personalizados<br>Exportar atributos personalizados<br>Ver eventos personalizados<br>Editar eventos personalizados<br>Eventos personalizados de la lista de bloqueo<br>Eliminar eventos personalizados<br>Exportar eventos personalizados<br>Editar segmentación de propiedades de eventos personalizados<br>Ver productos<br>Editar productos<br>Productos de la lista de bloqueo<br>Editar segmentación de propiedades de compra |
| Espacio de trabajo | Administrar integraciones externas | Editar socios tecnológicos<br>Editar la ingesta de datos en la nube |
| Espacio de trabajo | Administrar configuración en varios idiomas | Editar configuración de localización<br>Borrar configuración de localización |
| Espacio de trabajo | Administrar grupos de suscripción | Editar suscripciones |
| Espacio de trabajo | Gestionar etiquetas | Ver etiquetas<br>Editar etiquetas<br>Borrar etiquetas |
| Espacio de trabajo | Gestionar equipos | Ver equipos<br>Modificar equipos<br>Archivar equipos |
| Espacio de trabajo | Ver transformaciones de datos | Ver transformación de datos |
| Espacio de trabajo | Editar transformaciones de datos | Editar transformación de datos |
| Espacio de trabajo | Administrar el cifrado de datos de usuario | Editar identificador Cifrado a nivel de campo |
| Espacio de trabajo | Enviar campañas, Canvas | Lanzar campañas<br>Lanzar Canvas |
| Espacio de trabajo | Ver datos de facturación | Ver datos de facturación |
| Espacio de trabajo | Visualizar integraciones de Currents | Visualizar integraciones de Currents |
| Espacio de trabajo | Editar integraciones de Currents | Editar integraciones de Currents |
| Espacio de trabajo | Ver atributos personalizados marcados como Información personal identificable (PII) | Ver atributos personalizados marcados como Información personal identificable (PII) |
| Espacio de trabajo | Ver PII | Ver PII |
| Espacio de trabajo | Ver perfiles de usuarios que cumplen las reglas de PII | Ver perfiles de usuarios que cumplen las reglas de PII |
| Espacio de trabajo | Ver datos de consumo | Ver datos de consumo |
| Espacio de trabajo | Fusionar usuarios duplicados | Fusionar usuarios duplicados |
| Espacio de trabajo | Vista previa de usuarios duplicados | Vista previa de usuarios duplicados |
| Espacio de trabajo | Crear y editar plantillas de Canvas | Editar plantillas de Canvas |
| Espacio de trabajo | Ver plantillas de Canvas | Ver plantillas de Canvas |
| Espacio de trabajo | Archivar plantillas de Canvas | Archivar plantillas de Canvas |
| Espacio de trabajo | Publicar páginas de inicio | Publicar páginas de inicio |
| Espacio de trabajo | Crear borradores de página de inicio | Editar borradores de páginas de destino |
| Espacio de trabajo | Acceder a páginas de inicio | Ver páginas de inicio |
| Espacio de trabajo | Crea y edita plantillas de páginas de inicio | Editar plantillas de páginas de destino |
| Espacio de trabajo | Ver plantillas de páginas de inicio | Ver plantillas de páginas de inicio |
| Espacio de trabajo | Archiva plantillas de páginas de inicio | Archiva plantillas de páginas de inicio |
| Espacio de trabajo | Ver agentes de IA personalizados | Ver agentes de IA personalizados |
| Espacio de trabajo | Editar agentes de IA personalizados | Editar agentes de IA personalizados<br> Archivo Agentes de IA personalizados |
| Espacio de trabajo | Ver Colocaciones | Ver Colocaciones |
| Espacio de trabajo | Editar ubicaciones | Editar ubicaciones |
| Espacio de trabajo | Archivar colocaciones | Archivar colocaciones |
| Espacio de trabajo | Nuevo | Ver fusionar usuarios |
| Espacio de trabajo | Nuevo | Ver los registros de eliminación de usuarios |
| Espacio de trabajo | Nuevo | Borrar usuarios del panel |
| Espacio de trabajo | Nuevo | Ver plantillas de banners |
| Espacio de trabajo | Nuevo | Editar plantillas de banners |
| Espacio de trabajo | Nuevo | Plantillas de banners de archivo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Preguntas más frecuentes

### ¿Puedes optar por no participar en la migración o revertirla?

Braze no admite la reversión de la migración. Te ayudaremos durante la migración y la supervisaremos de cerca para resolver rápidamente cualquier problema que pueda surgir.

### ¿Los usuarios actuales perderán acceso a Braze durante la migración?

No, no habrá tiempo de inactividad en Braze durante la migración. Sin embargo, las actualizaciones de los permisos se bloquearán durante la migración. Prevemos que la migración tardará hasta 15 minutos en completarse.