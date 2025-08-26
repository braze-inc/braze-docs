---
nav_title: Knak
article_title: Knak
alias: /partners/knak/
description: "Este artículo de referencia describe la asociación entre Braze y Knak, una plataforma de creación de campañas que permite crear correos electrónicos totalmente receptivos en cuestión de minutos u horas en lugar de días o semanas, y exportarlos como plantillas Braze listas para usar."
page_type: partner
search_tag: Knak

---

# Knak

> [Knak](https://knak.com/) es la primera plataforma de creación de campañas creada para que los equipos de marketing de las empresas la utilicen internamente. Su plataforma de arrastrar y soltar permite crear correos electrónicos de gran calidad para las marcas y páginas principales en cuestión de minutos, sin necesidad de código ni de asistencia externa.

_Esta integración está mantenida por Knak._

## Sobre la integración

La integración de Braze y Knak permite crear correos electrónicos totalmente receptivos en cuestión de minutos u horas, en lugar de días o semanas, y exportarlos como plantillas Braze listas para usar. Knak está pensado para los profesionales del marketing que desean mejorar la creación de mensajes de correo electrónico para las campañas gestionadas en Braze, sin necesidad de agencias externas ni de codificación manual. 

## Requisitos previos

| Requisito | Descripción |
| ----------- | ----------- |
| Cuenta Knak | Se necesita una cuenta Knak para beneficiarse de esta asociación. |
| Clave REST API de Braze | Una clave Braze REST API con permisos **Templates** completos. <br><br>Puede crearse en el panel Braze desde **Configuración** > **Claves API**. |
| Punto final REST Braze | [La URL de tu punto final REST]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Tu punto final dependerá de la URL Braze de tu instancia. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos prácticos

Knak está pensado para los profesionales del marketing que desean mejorar la creación de sus mensajes de correo electrónico, sin necesidad de codificación ni ayuda externa. Es ideal para quienes:
- Actualmente utilizan plantillas sencillas para los correos electrónicos y quieren mejorar su juego
- Depender de agencias o desarrolladores externos para crear correos electrónicos para Braze
- Quiere recuperar el control creativo sobre la creación de activos y llegar al mercado mucho más rápido

## Integración

### Paso 1: Configure su integración

En Knak, vaya a **Integraciones > Plataformas > + Añadir nueva integración**.

![Añadir botón de integración]({% image_buster /assets/img/knak/integration-setup-step-2-add-new-integration.png %})

A continuación, selecciona la plataforma **Braze** y proporciona la clave de API Braze y el punto final REST. Haga clic en **Crear nueva integración** para completar su integración. 

![Crear nueva integración]({% image_buster /assets/img/knak/integration-setup-step-4-add-api-key.png %})

### Paso 2: Sincroniza tus plantillas Knak

En Knak, localiza un correo electrónico que quieras sincronizar con Braze y selecciona **Publicar** y luego **Sincronizar**.

![Knak integración 1]({% image_buster /assets/img/knak/integration-post-step-1-sync.png %})

A continuación, verifique el nombre del correo electrónico y haga clic en **Sincronizar**.

![Knak integración 2]({% image_buster /assets/img/knak/integration-post-step-2-asset-name.png %})

## Utilización de la integración

Puede encontrar los correos electrónicos de Knak que haya cargado en Braze, en **Compromiso > Plantillas y medios**. Serán bonitos, acordes con la marca y totalmente receptivos. El único límite es tu propia creatividad.


