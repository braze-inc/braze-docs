---
nav_title: Espacios de trabajo
article_title: "Cómo empezar: Espacios de trabajo"
page_order: 3
page_type: reference
description: "Todo lo que haces en la plataforma Braze ocurre dentro de un espacio de trabajo. Este artículo describe cómo funcionan y qué consideraciones importantes hay que tener en cuenta al planificar los espacios de trabajo en Braze."
---

# Cómo empezar: Espacios de trabajo

Todo lo que haces en la plataforma Braze ocurre dentro de un espacio de trabajo. Los espacios de trabajo actúan como silos separados de datos y le permiten mantener separadas diferentes marcas o actividades. Varias versiones de su sitio web o aplicación móvil pueden enviar datos al mismo espacio de trabajo. Nos referimos a los diferentes sitios y apps que se reúnen dentro de un espacio de trabajo como "instancias de app".

## Comprender los espacios de trabajo

Los espacios de trabajo tienen dos objetivos fundamentales:

- **Unificar los datos de los usuarios:** Cuando varias instancias de la aplicación se encuentran en un espacio de trabajo, puede recopilar y dirigir los datos del usuario sin problemas a través de diferentes versiones de su aplicación, como iOS, Android y web. De este modo, siempre dispondrá de información actualizada sobre cada usuario, independientemente de la plataforma que utilice.
- **Separar actividades distintas:** Los espacios de trabajo también permiten mantener separadas distintas marcas o actividades. Por ejemplo, si tiene varias submarcas con diferentes bases de usuarios, es beneficioso crear espacios de trabajo separados para cada una.

{% alert tip %}
Este enfoque es especialmente útil para empresas como las de juegos para móviles, que pueden gestionar espacios de trabajo individuales para cada uno de sus juegos, o sitios de comercio electrónico que quieren espacios de trabajo separados para cada región en la que operan.
{% endalert %}

## Planificación de los espacios de trabajo

Debe crear instancias de aplicación distintas para cada versión de su aplicación en cada plataforma. A la hora de decidir qué instancias de aplicación incluir en un espacio de trabajo, piense en los usuarios a los que desea dirigirse y agrúpelos en consecuencia.

El atractivo de tener varias instancias de la aplicación en un mismo espacio de trabajo puede ser tentador, ya que te permite limitar la tasa de mensajería en toda tu cartera de aplicaciones. Sin embargo, como práctica recomendada, sugerimos que sólo se agrupen en un espacio de trabajo diferentes versiones de la misma aplicación (o de aplicaciones muy similares).

### Espacios de trabajo compartidos

Ejemplos comunes de casos en los que querrías tener varias instancias de aplicaciones en el mismo espacio de trabajo:

- Cuando se tienen varias aplicaciones casi idénticas en diferentes plataformas
- Cuando tienes diferentes revisiones principales de la aplicación, pero quieres seguir atrayendo a los mismos usuarios cuando se actualizan.
- Cuando existen diferentes versiones de la aplicación en las que un mismo usuario puede entrar o salir (por ejemplo, de gratuita a premium).

#### Impacto en los filtros de segmentación

Cualquier aplicación que elijas tener en un espacio de trabajo tendrá sus datos agregados. Esto tendrá un impacto notable en los siguientes filtros de segmentación en Braze (esta no es una lista exhaustiva):

- Última aplicación usada
- Primera aplicación usada
- Recuento de sesiones
- Dinero gastado en la aplicación
- Suscripción Push (Esto se convierte en una situación de todo o nada: si tus usuarios se dan de baja de una aplicación, se dan de baja de todas las aplicaciones del espacio de trabajo).
- Suscripción por correo electrónico (Esto se convierte en una situación de todo o nada y puede dejarle expuesto a problemas de cumplimiento).

{% alert note %}
La agregación de datos entre instancias de aplicaciones en estos filtros es la razón por la que no recomendamos alojar aplicaciones sustancialmente diferentes en el mismo espacio de trabajo. Esto puede dificultar la selección de objetivos.
{% endalert %}

### Espacios de trabajo separados

Otras veces, puede que desee tener varios espacios de trabajo separados. Algunos ejemplos habituales son:

- Espacios de trabajo separados para los entornos de desarrollo y producción de la misma aplicación.
- Diferentes submarcas, por ejemplo, una empresa de juegos para móviles que ofrece varios juegos
- Diferentes localizaciones de la misma aplicación o sitio web que operan en diferentes países o se dirigen a diferentes idiomas.

### Consideraciones importantes

Recuerda que los espacios de trabajo actúan como silos separados de datos. Todos los datos, ya sean de usuarios o activos de marketing, se almacenan en un espacio de trabajo. Estos datos no pueden compartirse fácilmente fuera de ese espacio de trabajo. 

A continuación se enumeran todos los elementos clave que se configuran dentro de un espacio de trabajo:

- [Instancias de la aplicación](#app-instances)
- [Equipos](#teams)
- [Permisos de usuario Braze](#braze-user-permissions) (pero no usuarios Braze)
- [Conectores de corriente](#currents-connectors)
- [Perfiles de usuario](#user-profiles) y datos de usuario asociados
- [Segmentos, campañas y lienzos](#segments-campaigns-and-canvases)

#### Instancias de la aplicación

Debe crear instancias de aplicación distintas para cada versión de su aplicación en cada plataforma. Por ejemplo, si tiene versiones Free y Pro de su aplicación tanto en iOS como en Android, cree cuatro instancias de aplicación en su espacio de trabajo (aplicación gratuita para iOS, aplicación gratuita para Android, aplicación pro para iOS y aplicación pro para Android). Esto te dará cuatro claves de API para utilizar, una para cada instancia de la aplicación.

#### Equipos

[Los equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) pueden configurarse en función de la ubicación de la base de clientes, el idioma y los atributos personalizados, de modo que los miembros del equipo y los que no lo son tengan diferente acceso a las funciones de mensajería y a los datos de los clientes.

#### Permisos de usuario Braze

Los espacios de trabajo tienen definiciones independientes de acceso y permiso de usuario. [Los permisos de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/) le permiten crear controles granulares sobre a qué tiene acceso un usuario individual del cuadro de mandos o un equipo dentro de un mismo espacio de trabajo.

#### Conectores de corriente

La herramienta [Currents]({{site.baseurl}}/user_guide/data/braze_currents/) es un flujo de datos en tiempo real de sus eventos de participación que es la exportación más sólida y granular de la plataforma Braze. Los conectores Currents se incluyen con determinados paquetes Braze, y es posible que haya recibido uno inicialmente, suponiendo un único espacio de trabajo.

A la hora de decidir entre crear espacios de trabajo separados o combinados, es importante pensar en el número de conectores Currents que tiene, ya que los conectores Currents no se comparten entre espacios de trabajo. 

Por ejemplo, si tiene espacios de trabajo separados para los entornos de desarrollo y producción de la misma aplicación, active su conector Currents en el espacio de trabajo de producción. Para habilitar Currents en ambos espacios de trabajo, tendrás que comprar un conector Currents adicional.

#### Perfiles de usuario

Todos los datos persistentes asociados a un usuario se almacenan en su [perfil de usuario]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Sin embargo, los perfiles de usuario también son un gran recurso para solucionar problemas y realizar pruebas, ya que se puede acceder fácilmente a información sobre el historial de participación de un usuario, su pertenencia a un segmento, su dispositivo y su sistema operativo.

#### Segmentos, campañas y lienzos

Un segmento, una campaña o un lienzo no pueden hacer referencia o acceder a datos alojados en otro espacio de trabajo. Por el contrario, cuando varias aplicaciones se encuentran en el mismo espacio de trabajo, todas las aplicaciones tendrán sus datos agregados. Esto [repercutirá en los filtros de Braze](#impact-on-segmentation-filters).

### Visión general de cada enfoque

En la tabla siguiente se describen las ventajas e inconvenientes de estos dos enfoques de la planificación del espacio de trabajo:

- **Espacios de trabajo y perfiles de usuario separados:** Un espacio de trabajo tiene una instancia de aplicación y una persona tiene un perfil de usuario para esa instancia de aplicación.
- **Espacios de trabajo compartidos y perfiles de usuario:** Un espacio de trabajo tiene varias instancias de aplicación y una persona tiene un perfil de usuario para todas esas instancias de aplicación.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
  }
</style>

<table>
    <tr>
        <th></th>
        <th colspan="2">Espacios de trabajo separados</th>
        <th colspan="2">Espacios de trabajo compartidos</th>
    </tr>
    <tr>
        <th></th>
        <th>Beneficios</th>
        <th>Inconvenientes</th>
        <th>Beneficios</th>
        <th>Inconvenientes</th>
    </tr>
    <tr>
        <td>Segmentación</td>
        <td>La forma más segura de mantener las comunicaciones separadas. Se garantiza que las campañas se dirijan únicamente a perfiles de usuario específicos.</td>
        <td>Imposibilidad de enviar mensajes de promoción cruzada aunque se sepa que un usuario tiene otro perfil de usuario en un espacio de trabajo diferente.</td>
        <td>Puede enviar mensajes de promoción cruzada si sabe que un usuario tiene varias aplicaciones en su espacio de trabajo.<br><br>Puede hacer referencia a datos de usuario de distintas aplicaciones. Por ejemplo, Juan tiene un atributo X relevante para la aplicación 1, y un atributo Y relevante para la aplicación 2, que pueden ser referenciados en una campaña.</td>
        <td>Más margen para el error humano: podría dirigirse accidentalmente a usuarios de varias instancias de la aplicación.<br><br>Para enviar mensajes in-app, debes tener eventos personalizados específicos de la app para que una campaña no se muestre en otra app por accidente. Por ejemplo, <code>app_1_action</code> frente a <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <td>Eventos y atributos personalizados</td>
        <td>Se garantiza que los atributos y eventos personalizados son específicos de una instancia de aplicación.</td>
        <td>No se puede realizar un seguimiento del comportamiento de los usuarios en los distintos espacios de trabajo.<br><br><b>Consejo:</b> Para ello, puede utilizar varios conectores Currents.</td>
        <td>Puede realizar un seguimiento del comportamiento del usuario en todas las instancias de la aplicación en el espacio de trabajo.</td>
        <td>Los atributos y eventos personalizados se aplicarían a todas las instancias de la aplicación, lo que podría dificultar saber qué datos de un perfil de usuario son relevantes para qué instancia de la aplicación. Por ejemplo, ¿es "date_of_parking" relevante para la Aplicación 1 o para la Aplicación 2? Para evitarlo, asegúrate de utilizar convenciones de nomenclatura bien estructuradas.</td>
    </tr>
    <tr>
        <td>Limitación de frecuencia</td>
        <td>La limitación de frecuencia puede definirse por separado para cada instancia de aplicación (en función del espacio de trabajo).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>El límite de frecuencia se aplica a todas las campañas, no a cada aplicación, lo que hace más difícil evitar el exceso de mensajes a los clientes.</td>
    </tr>
    <tr>
        <td>Estado de suscripción de los perfiles de usuario</td>
        <td>El estado de suscripción de cada perfil de usuario es único para cada instancia de la aplicación.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Los estados de suscripción de un perfil de usuario se combinan en todas las instancias de la aplicación.<br><br><b>Consejo:</b> En su lugar, podrías utilizar <a href='/docs/user_guide/data/custom_data/custom_attributes'>atributos personalizados</a> para gestionar las suscripciones de tus usuarios.</td>
    </tr>
    <tr>
        <td>Permisos de usuario Braze</td>
        <td>N/A</td>
        <td>La actualización de <a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>los permisos de</a> un usuario del panel debe hacerse por separado para cada espacio de trabajo al que el usuario necesite acceder.</td>
        <td><a href='/docs/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/'>Los permisos de usuario</a> pueden configurarse una vez para un usuario del panel, y tendrán los mismos permisos para todas las instancias de la aplicación en el espacio de trabajo.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Duplicación de contenidos</td>
        <td>N/A</td>
        <td>No se pueden duplicar segmentos, campañas push o de tarjeta de contenido, ni lienzos entre espacios de trabajo.</td>
        <td>Puedes [duplicar campañas entre espacios de trabajo]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/copying_across_workspaces/) para los siguientes canales compatibles: SMS, mensajes dentro de la aplicación, correo electrónico, plantillas de correo electrónico y bloques de contenido. <br><br>Puede duplicar segmentos, campañas y lienzos para reutilizar el contenido de una aplicación a otra.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <td>Análisis</td>
        <td>Las estadísticas globales serán precisas en la página de inicio.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Las estadísticas globales se agregarán para todas las instancias de la aplicación en el área de trabajo en la página de inicio.</td>
    </tr>
</table>

## Buenas prácticas

### Configurar un espacio de trabajo de pruebas

Como práctica recomendada, siempre que tenga previsto configurar un espacio de trabajo de producción (un espacio de trabajo que enviará mensajes a usuarios reales), debe configurar también un espacio de trabajo de prueba. Un espacio de trabajo de prueba es un duplicado de su espacio de trabajo de producción sin ningún dato real del usuario. 

Esto se considera una buena práctica por varias razones:

- **Aislamiento de los cambios:** Le permite probar nuevas funciones, configuraciones o actualizaciones en un entorno aislado sin afectar a su entorno de producción en vivo. De este modo, si algo sale mal durante las pruebas, el entorno de producción no se verá afectado.
- **Pruebas precisas:** Permite realizar pruebas más precisas, ya que los datos del entorno de pruebas pueden controlarse y manipularse sin preocuparse de los datos del mundo real.
- **Depuración:** Es más fácil depurar problemas en un entorno de pruebas, ya que puedes manipular libremente el entorno sin preocuparte de afectar al entorno de producción.
- **Formación:** Los nuevos miembros del equipo pueden familiarizarse con el espacio de trabajo en un entorno seguro en el que los errores no tendrán consecuencias en el mundo real.

{% alert tip %}
El orden en que configure un espacio de trabajo de prueba y un espacio de trabajo de producción puede depender de sus necesidades y circunstancias específicas. Sin embargo, suele ser una buena idea configurar primero un espacio de trabajo de prueba. Esto le permite probar funciones, configuraciones y actualizaciones antes de implementarlas en el espacio de trabajo de producción. Cuando estés satisfecho con las pruebas y los resultados, podrás establecer tu espacio de trabajo de producción.
{% endalert %}

### Añadir administradores

Debe tener más de un usuario Braze con permisos de administrador para un mismo espacio de trabajo. Esto garantiza que haya suficientes personas en su organización para gestionar los permisos de otros usuarios.

## Próximos pasos

Una vez que hayas determinado tu plan de espacio de trabajo, es hora de crear tu espacio de trabajo y añadir instancias de aplicaciones. Para conocer los pasos, consulta [Crear y gestionar espacios de trabajo]({{site.baseurl}}/user_guide/administrative/app_settings/workspaces/).

