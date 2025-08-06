---
nav_title: ActionIQ
article_title: ActionIQ
description: "Este artículo de referencia cubre la integración de Braze y ActionIQ.  Esta integración permite a las marcas sincronizar y asignar sus datos de ActionIQ directamente a Braze."
alias: /partners/actioniq/
page_type: partner
search_tag: ActionIQ
---

# ActionIQ

>  



## Sobre la integración

 

- 
- Reenvíe los eventos rastreados por ActionIQ a Braze en tiempo real para activar campañas personalizadas y específicas.
- 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta ActionIQ | Se requiere una cuenta ActionIQ para aprovechar esta integración. |
| Clave REST API de Braze |   <br><br> |
| Punto final REST Braze | [La URL de tu punto final REST][1]. Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integraciones

### Membresía de la audiencia

Esta integración se utiliza para sincronizar la pertenencia a la audiencia de ActionIQ con Braze mediante la creación de atributos personalizados que indican si un perfil de Braze forma parte de un segmento. Cada público de ActionIQ corresponde a un único atributo booleano personalizado.

La convención de nomenclatura estándar para el atributo personalizado creado es: `AIQ_<Audience ID>_<Split ID>`.


1. 
2. 
3. 
4.  
5. Una vez creado el segmento, puede seleccionarlo como filtro de audiencia al crear una campaña o Canvas.



#### Requisitos

 Puede crearse en el panel Braze desde **Configuración** > **Claves API**. 

En ActionIQ, configura una conexión Braze proporcionando tu clave de API REST y el punto final REST Braze. 

Para que coincida con los consumidores en la plataforma Braze, se deben incluir los siguientes identificadores en su configuración de activación:
- `braze_id`
- `external_id`

### Eventos

  

#### Requisitos

 Puede crearse en el panel Braze desde **Configuración** > **Claves API**. 

La integración de eventos envía la siguiente información a Braze:
- Nombre de evento
- Identificador del consumidor ( `braze_id` o `external_id`)
- Marca de tiempo
- Propiedades de evento, que se rellenan con cualquier atributo adicional en la configuración de exportación

### Campañas activadas

 

 

#### Requisitos

 Puede crearse en el panel Braze desde **Configuración** > **Claves API**.


- Identificador del consumidor ( `braze_id` o `external_id`)
- ID de campaña


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: https://www.actioniq.com/