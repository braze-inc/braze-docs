{% if include.content == "Differences" %}

Puedes utilizar [equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/), [conjuntos de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) y [roles de usuario]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) para gestionar el acceso y las responsabilidades de los usuarios de la empresa dentro de Braze. Cada función abarca una colección diferente de permisos y controles de acceso.

### Principales diferencias

A alto nivel, cada característica tiene un alcance diferente:
- Los conjuntos de permisos controlan lo que los usuarios de la empresa pueden hacer en todos los espacios de trabajo.
- Los roles controlan lo que los usuarios de la empresa pueden hacer en espacios de trabajo específicos.
- Los equipos controlan las audiencias a las que los usuarios de la empresa pueden llegar con sus mensajes.

| Característica | Qué puedes hacer | Ámbito de acceso |
| - | - | - |
| [Conjuntos de permisos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-permission-set) | Agrupa los permisos relacionados con áreas temáticas o acciones específicas (como «Desarrolladores» y «Especialistas en marketing») y, a continuación, aplícalos a los usuarios de la empresa que necesiten los mismos permisos en diferentes espacios de trabajo. | En toda la empresa |
| [Roles]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) | Agrupa permisos personalizados individuales y controles de acceso al espacio de trabajo (como «Especialista en marketing - Marcas de moda», donde el usuario tiene ciertos permisos asociados a su función como especialista en marketing y está limitado a los espacios de trabajo «Marcas de moda»). A continuación, asigna una función a los usuarios de la empresa para concederles directamente los permisos asociados y el acceso al espacio de trabajo. <br><br>Los usuarios con este nivel de acceso suelen ser administradores en entornos más estrictamente controlados, con muchas marcas o espacios de trabajo regionales en un solo panel. | Espacios de trabajo específicos |
| [Equipos]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/#creating-teams) | Limita el acceso de los usuarios de la empresa a los recursos en función de la audiencia (por ejemplo, la ubicación de la base de clientes, el idioma y los atributos personalizados). <br><br>Los usuarios con este nivel de acceso suelen ser responsables de un ámbito específico dentro de la marca en la que trabajan, como la creación de contenido específico para cada idioma en el caso de una marca multilingüe. | Panel específico |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endif %}