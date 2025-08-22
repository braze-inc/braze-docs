---
nav_title: DataGrail
article_title: DataGrail
description: "Este artículo de referencia describe la asociación entre Braze y DataGrail, una plataforma de gestión de la privacidad, que permite detectar los datos de los consumidores recopilados y almacenados en Braze para procesar rápidamente las DSR."
alias: /partners/datagrail/
page_type: partner
search_tag: Partner

---

# DataGrail

> [DataGrail](https://www.datagrail.io/), una plataforma de gestión de la privacidad, ayuda a fomentar la confianza de los consumidores y a eliminar los negocios de riesgo. Con la detección continua del sistema y el cumplimiento automatizado de las solicitudes de los interesados (DSR), DataGrail potencia los programas de privacidad, apoyando el cumplimiento de las leyes y normativas de privacidad en evolución, como el RGPD, la CCPA y la CPRA. 

_Esta integración está mantenida por DataGrail._

## Sobre la integración

La integración de Braze y DataGrail permite detectar los datos de los consumidores recopilados y almacenados en Braze para procesar rápidamente las DSR (solicitudes de acceso, eliminación y no venta). Braze se sumará a un proyecto preciso de dónde viven los datos de los consumidores en su organización con el mapeo de datos automatizado - no se necesitan más encuestas u hojas de cálculo para mantener un marco de privacidad o producir un registro de actividades de procesamiento (RoPA). 

## Requisitos previos

| Requisitos | Descripción |
|---|---|
| Cuenta DataGrail | Una cuenta DataGrail para aprovechar esta asociación.<br>Póngase en contacto con su administrador o envíe un correo electrónico a support@datagrail.io si tiene algún problema o pregunta sobre la integración. |
| Clave API Braze | Una clave de API REST de Braze con permisos `events.list`, `users.export.ids`, `users.delete` y `users.track`.<br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Instancia de soldadura | Puedes obtener tu instancia de Braze a través de tu administrador de incorporación a Braze o en la [página de resumen de la API]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

Inicia sesión en el portal DataGrail y selecciona **Conectar** en la página de integración de Braze. A continuación, introduce tu instancia y tu clave de API de Braze y selecciona **Conectar Braze**.

Si hay cuentas Braze adicionales que integrar:
1. Selecciona **Editar conexión** en la página de integración de Braze.
2. En el desplegable, selecciona **+Añadir nueva conexión**.
3. En **Nombre de conexión**, introduzca un nuevo nombre para identificar esta cuenta independiente (por ejemplo, Cuenta de formación Braze).
4. Introduzca una instancia de Braze y una clave API independientes para esta nueva cuenta.
5. Selecciona **Conectar**.

Envíe un correo electrónico a DataGrail a support@datagrail.io si tiene algún problema o pregunta sobre su integración.

