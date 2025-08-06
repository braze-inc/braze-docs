---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "Este artículo de referencia describe la asociación entre Braze y Personalize.AI, una plataforma empresarial SaaS basada en IA que impulsa el crecimiento de los ingresos a partir de recomendaciones personalizadas."
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) se asocia con Braze para generar ingresos adicionales entregando mensajes personalizados y ofertas enviadas a través de Braze. 

La integración de Braze y Personalize.AI te permite exportar datos de Personalize.AI a la plataforma Braze para la personalización y segmentación de mensajes.

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Instancia de Personalize.AI | Se necesita una instancia de Personalize.AI para aprovechar esta asociación. |
| Clave de API REST de Braze | Una clave Braze REST API con todos los permisos. <br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | La URL de su punto final REST. Tu punto final dependerá de la [URL Braze de tu instancia]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

* Desplegar pruebas, incluida la estratificación flexible, para obtener resultados a partir de las opiniones de los clientes
* Proporcionar recomendaciones personalizadas para artículos y ofertas, incluyendo el tratamiento, el momento y el contenido
* Identificar objetivos prioritarios y dirigirse a tu audiencia óptima a través de Braze
* Identificar las oportunidades de reactivación de la interacción de los usuarios rezagados
* Aprovechar los datos de geolocalización para encontrar la audiencia adecuada para las ubicaciones de nueva apertura
* Utilizar el modelado de parecidos para basarte en los limitados datos disponibles de los usuarios más nuevos, emparejándolos con las recomendaciones más relevantes
* Identificar las formas adecuadas de interacción con los clientes a lo largo de su ciclo de vida 
* Evaluar proactivamente la probabilidad de abandono de los clientes y asigna una puntuación de riesgo para encontrar indicadores tempranos de abandono
* Dirigirse a los clientes con intervenciones personalizadas para evitar que se vuelvan inactivos

## Integración

### Configura una conexión con Braze en Personalize.AI

1. En Personalize.AI, ve a la pestaña **Integraciones**, situada en **Operacionalización**, en tu instancia de Personalize.AI.
2. Haz clic en **Braze**. 
3. Configura tu integración con Braze.
    * **Nombre de la conexión:** Ponle nombre a tu conexión. Así es como se hará referencia a tu integración en Personalize.AI.
    * **Frecuencia de sincronización:** La frecuencia de sincronización controla la frecuencia con la que Personalize.AI exporta datos a Braze. Selecciona **Diaria**, **Semanal** o **Mensual**. 
    * **Clave de API:** Añade tu clave de API Braze.
    * **URL DE LA API:** Añade la URL de tu punto final REST Braze.
4. Haz clic en **EXPORTAR** para exportar los datos a Braze.

Una vez exportados tus datos, Personalize.AI seguirá pasando datos a Braze a los intervalos determinados por la frecuencia de sincronización que establezcas durante la integración.

## Uso de esta integración

Personalize.AI exporta a Braze los identificadores utilizados para la personalización. Estos atributos personalizados indican el momento, el contenido, el tratamiento y las ofertas para cada cliente. Dependiendo de la integración, los campos pueden pasarse como un evento o introducirse en [las API de contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/public_apis/) en lugar de almacenarse en el perfil del cliente. Personalize.AI admite el uso de `external_id` como identificador.

Los atributos de datos importados en Braze se nombran intuitivamente para su uso en Canvas, siguiendo una terminología coherente. Por ejemplo, el atributo `C402_Target_Variant` en Personalize.AI se exportaría a Braze como `"P.AI_Model_Treatment"`. Los atributos exportados desde Personalize.AI están diseñados para no interferir con ningún atributo existente ni con el seguimiento de su uso. Estos atributos se validan continuamente para confirmar que puedes hacer referencia a ellos con confianza. 

Por ejemplo, aquí tienes un conjunto de atributos de cliente relacionados con un ejemplo de Canvas centrado en el abandono.

| Personalize.AI atributo | Valor |
| ----------- | ------------- | 
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Churn_Mitigation" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | Tratamiento |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | $3 |
| `C4_Item_Recom` | "Ensalada César" |
| `C4_Subject_Line` | "Te echamos de menos" |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


