---
nav_title: EduMe
article_title: EduMe
description: "Este artículo de referencia describe la asociación entre Braze y eduMe, una herramienta de formación basada en el móvil que te permite aprovechar el contenido conectado de Braze para dar a tus usuarios acceso a los cursos y lecciones de eduMe en tus campañas Braze."
alias: /partners/edume/
page_type: partner
search_tag: Partner

---

# EduMe

> [eduMe](https://edume.com) es una herramienta de formación móvil que proporciona a tus trabajadores los conocimientos que necesitan para triunfar, cuando los necesitan y dondequiera que estén. 

_Esta integración está mantenida por eduMe._

## Sobre la integración

La integración de Braze y eduMe aprovecha [el contenido conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content) de Braze para dar a tus usuarios acceso a los cursos y lecciones de eduMe en tus campañas Braze. El progreso individual y de grupo puede seguirse a través de la función de informes de EduMe.

## Requisitos previos

| Requisito | Descripción |
|---|---|
| Cuenta eduMe | Se necesita una cuenta eduMe para beneficiarse de esta asociación. |
| Clave de API de EduMe | Debes solicitar una clave de API a tu contacto de éxito del cliente de eduMe. Esta clave se utilizará en tu llamada de contenido conectado Braze. |
| Secreto de firma del enlace EduMe | Debes solicitar a tu contacto de éxito del cliente en eduMe que configure un enlace secreto de registro para tu organización. Este secreto se utiliza para habilitar enlaces sin fisuras en el Contenido conectado. No tendrás que hacer nada con este secreto. |
| ID de grupo y contenido de EduMe | Estos identificadores son necesarios para configurar tus llamadas de Contenido conectado. Ponte en contacto con el servicio de atención al cliente de eduMe para que te ayuden a obtener estos identificadores. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integración

### Crea tu llamada de contenido conectado

Para dar acceso a un usuario a un curso, lección o cuestionario eNPS, y hacer un seguimiento de su progreso con tu ID de usuario interno en eduMe, sigue la llamada a la API que se muestra en este ejemplo:

{% raw %}
```
Welcome to my Rickshaw App platform.
Access your onboarding course at:

{% connected_content
  https://connect.edume.com/
  EDUME-CONTENT-LINK-AND-CONTENT-ID&groupId=5681&externalUserId={{${driver_id}}}
  :headers {
       "x-api-key": "YOUR-EDUME-API-KEY"
  }
%}
```
{% endraw %}

1. Sustituye `YOUR-EDUME-API-KEY` por tu clave de API de eduMe.<br><br>
2. Sustituye `EDUME-CONTENT-LINK-AND-CONTENT-ID` por la cadena de enlace de contenido y el identificador de módulo, lección o cuestionario correspondientes. Puedes encontrar estos identificadores en tu cuenta de eduMe.
  - Curso: `getCourseLink?moduleId=12087`
  - Lección: `getLessonLink?lessonId=25805`
  - Cuestionario eNPS: `getSurveyLink?surveyId=654`<br><br>
3. Los usuarios que lleguen a eduMe a través de este enlace se añadirán a un equipo o grupo eduMe de tu elección. Sustituye `groupId` por el ID del equipo o del grupo eduMe correspondiente. Normalmente utilizarás el ID de equipo, excepto para los cursos que requieran inscripción, en cuyo caso deberás utilizar el ID de grupo<br><br>
4. Incluye un campo apropiado al que mapear el campo `externalUserId`. El ejemplo de llamada a contenido conectado utiliza la dirección `driver_id`, aunque es probable que tu campo sea diferente. Este ID estará disponible en los informes de eduMe, lo que te permitirá correlacionarlos con tus sistemas.<br><br>
5. Por último, personaliza y prueba tu mensaje según sea necesario. Te recomendamos que envíes al menos un mensaje de prueba, accedas al contenido de eduMe, completes la lección o el curso y compruebes que se están registrando los análisis de eduMe. 

