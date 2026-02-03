---
nav_title: LILT
article_title: LILT
description: "Este artículo de referencia describe la asociación entre Braze y LILT."
alias: /partners/lilt/
page_type: partner
search_tag: Partner
---

# LILT

> [LILT](https://lilt.com/) es la solución completa de IA para la traducción y la creación de contenidos empresariales. LILT habilita a las organizaciones globales para escalar y optimizar sus contenidos, productos, comunicaciones y operaciones de soporte, con agentes de IA y flujos de trabajo totalmente automatizados.

_Esta integración la mantiene LILT._

## Acerca de esta integración

El conector Braze de LILT habilita la traducción de plantillas de correo electrónico HTML con velocidad de IA y calidad de nivel empresarial. Solicita una Traducción Instantánea adaptada a tu marca o una Traducción Verificada de calidad garantizada y recibe contenido de correo electrónico multilingüe de LILT directamente en Braze. 

## Ejemplos

La integración de LILT Braze automatiza y acelera el proceso de traducción, habilitando a los equipos globales de marketing para lanzar campañas multilingües rápidamente y con coherencia de marca.

### Lanzamiento de campañas globales racionalizadas

Lanza campañas de marketing en varias regiones a la vez, sin retrasos por traducciones manuales.

- **Escenario:** Tu empresa va a lanzar un nuevo producto en 10 países.
- **Solución:** Tu equipo de marketing finaliza la plantilla de correo electrónico en inglés en Braze, la etiqueta con `LILT: Ready`, y el conector LILT extrae automáticamente el contenido. Los lingüistas de dominios específicos revisan las instrucciones de traducción de la IA en la plataforma LILT para garantizar la calidad, y el conector empuja las versiones traducidas de vuelta a Braze.
- **Beneficio:** Reduce el tiempo de comercialización de tus campañas globales de días a horas, para que todos los clientes puedan recibir el anuncio del nuevo producto en el momento óptimo.

### Localización instantánea alineada con la marca

Utiliza la IA de LILT para obtener traducciones inmediatas y ajustadas a la marca en comunicaciones urgentes.

- **Escenario:** Debes desplegar inmediatamente correos electrónicos para una venta flash, una oferta por tiempo limitado o una interrupción urgente del servicio en cinco mercados geográficos.
- **Solución:** Etiqueta la plantilla de correo electrónico con `LILT: Instant`. LILT utiliza su IA y activos lingüísticos específicos de tu empresa (como terminología y guías de estilo) para generar una traducción de alta calidad y coherente con la marca en cuestión de minutos.
- **Beneficio:** Permite comunicaciones hiperreceptivas y en tiempo real sin sacrificar la voz de la marca ni la calidad, lo que es fundamental para el marketing sensible al tiempo.

## Requisitos previos

| Requisito previo       | Descripción |                        
|-----------------------|-----------------|
| Una cuenta LILT   | Es necesario tener una cuenta LILT para beneficiarse de esta asociación.  |
| Una clave de API REST Braze  | Una clave Braze REST API con los siguientes permisos:<br>- `templates.email.create`<br>- `templates.email.update`<br>- `templates.email.info`<br>- `templates.email.list`<br>- `templates.translations.source.get`<br>- `templates.translations.update`<br>- `templates.translations.get`<br>- `templates.translations.all.get`. <br><br> Crea esta clave en el panel de Braze desde **Configuración** > **Claves de API**. |
| Un punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final depende de la URL Braze de tu instancia.  |
{: .reset-td-br-1 .reset-td-br-2 role=“presentation”}


## Integración

### Paso 1: Configurar el conector LILT Braze

1. Entra en LILT, luego ve a **Conectar** > **Nuevo conector** > **Braze**.
	
![Braze el conector en LILT.]({% image_buster /assets/img/lilt/image_1_select_connector.png %})

{: start="2"}
2\. Selecciona el flujo de trabajo de localización deseado para tu contenido Braze.

![Braze el flujo de trabajo en LILT.]({% image_buster /assets/img/lilt/image_2_select_workflow.png %})	

{: start="3"}
3\. Introduce y verifica los detalles de configuración necesarios:
- Tu clave de API Braze
- Punto final REST Braze

![Completa las credenciales de la API.]({% image_buster /assets/img/lilt/image_3_api_creds.png %})	

{: start="4"}
4\. Selecciona **Verificar** para probar la configuración. Una vez confirmada la conexión, guarda la configuración.

### Paso 2: Prepara tu espacio de trabajo Braze

1. Activa las funciones multilingües en la configuración de tu espacio de trabajo Braze.

![Configura las localizaciones en Braze.]({% image_buster /assets/img/lilt/image_4_lilt_locales.png %})	

{: start="2"}
2\. Crea las siguientes etiquetas en Braze para tu flujo de trabajo LILT: 
- `LILT: Ready`
- `LILT: In progress`
- `LILT: Sent to LILT`
- `LILT: Delivered`
- `LILT: Needs Attention`
- `LILT: Instant`

![Configura las etiquetas LILT en Braze.]({% image_buster /assets/img/lilt/image_5_lilt_tags.png %})	

{: start="3"}
### Paso 3: Enviar contenido a LILT para su traducción 

1. Después de configurar el conector Braze de LILT, utiliza etiquetas de traducción de Liquid dentro de tus plantillas de correo electrónico Braze para identificar el contenido que debe traducirse. 
- Ejemplo:  {% raw %}`{% translation id_0 %}`Hola, `{{first_name}}!{% endtranslation %}`{% endraw %}
2. Inicia la traducción actualizando la etiqueta de la plantilla para indicar el flujo de trabajo deseado: 
- Elige `LILT: Ready` para una traducción verificada
- Elige `LILT: Instant` para una traducción instantánea adaptada a tu marca
3. El conector Braze de LILT se ejecuta en el tiempo preestablecido para introducir el contenido etiquetado en LILT. Sigue el progreso de la traducción, ya que las etiquetas de contenido se actualizan automáticamente en Braze para reflejar la fase en que se encuentra tu proyecto. 
	
![Plantilla de correo electrónico Braze con etiquetas de traducción.]({% image_buster /assets/img/lilt/image_6_braze_template.png %})	