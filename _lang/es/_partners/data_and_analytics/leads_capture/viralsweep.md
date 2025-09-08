---
nav_title: ViralSweep
article_title: ViralSweep
alias: /partners/viralsweep/
description: "Este artículo de referencia describe la asociación entre Braze y ViralSweep, un servicio de software que permite a las marcas crear, ejecutar y gestionar promociones de marketing digital como sorteos, concursos, premios instantáneos, listas de espera, promociones por recomendación, etc."
page_type: partner
search_tag: Partner

---

# ViralSweep

> [ViralSweep](https://viralsweep.com) es un servicio de software que permite a las marcas crear, ejecutar y gestionar promociones de marketing digital como sorteos, concursos, premios instantáneos, listas de espera, promociones por recomendación, etc. 

_Esta integración está mantenida por ViralSweep._

## Sobre la integración

La integración de Braze y ViralSweep le permite celebrar sorteos y concursos en la plataforma ViralSweep (haciendo crecer sus listas de correo electrónico y SMS) y, a continuación, enviar la información de participación en sorteos o concursos a Braze para utilizarla en campañas o lienzos. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta ViralSweep | Para beneficiarse de esta asociación se requiere una cuenta de ViralSweep que utilice el plan de negocio. |
| Clave REST API de Braze | Una clave de API REST de Braze con todos los datos de usuario y permisos de correo electrónico. <br><br> Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
|Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la URL Braze de [tu instancia]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Paso 1 : Conecta con Braze dentro de ViralSweep

En ViralSweep, vaya a **Integraciones > Correo electrónico y SMS > Añadir servicio** y seleccione **Braze**. 

![]({% image_buster /assets/img/viralsweep/connect.gif %})

### Paso 2 : Añadir credenciales Braze

En la ventana de configuración de integraciones, proporciona tu clave de API REST de Braze y tu punto final REST. Asegúrate de que el punto final que proporcionas no incluye `https://`, por ejemplo, `dashboard-03.braze.com`. 

![Página de integración del servicio ViralSweep que solicita al usuario la clave de API de Braze y la URL del panel de Braze.]({% image_buster /assets/img/viralsweep/connect2.png %}){: style="max-width:40%;"}

Haz clic en **Conectar**.

### Paso 3 : Añadir credenciales Braze
¡Estás conectado! La promoción está ahora conectada a Braze, y todas las entradas recogidas por ViralSweep se enviarán a Braze automáticamente.

## Preguntas más frecuentes

### ¿Qué campos pasa ViralSweep a Braze?
- Nombre
- Apellido
- Dirección de correo electrónico
- Dirección
- Dirección 2
- Localidad
- Estado
- Código postal
- País
- Fecha de nacimiento
- Teléfono
- ID de la promoción
- Enlace de referidos
- Nombre de la campaña de seguimiento

### ¿Actualiza ViralSweep a los suscriptores?
Sí. Si organiza una promoción y ViralSweep pasa a alguien a Braze, y luego organiza otra promoción en el futuro y entra la misma persona, la información de esa persona se actualizará automáticamente en Braze (si se proporciona nueva información). Principalmente, la URL de referencia se actualizará con la URL más reciente de cada promoción en la que participen, y el campo ID de promoción contendrá el ID de todas las promociones en las que hayan participado.

## Solución de problemas

Si te has conectado a Braze y no se están añadiendo datos a tu cuenta, puede deberse a que:

- **El correo electrónico ya existe en Braze**<br>
Es posible que la dirección de correo electrónico introducida en la promoción ya figure en su cuenta Braze, por lo que no se añadirá de nuevo; sólo se actualizará si se facilita nueva información para ese contacto.<br><br>
- **Correo electrónico ya introducido en ViralSweep**<br>
La dirección de correo electrónico introducida en la promoción ya ha sido introducida anteriormente, por lo que no se pasa de nuevo a Braze. Esto puede ocurrir si configuras tu integración Braze después de haber entrado en la promoción.


