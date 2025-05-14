{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Configuración de los atributos del usuario

Braze proporciona métodos para asignar atributos a los usuarios. Podrás filtrar y segmentar a tus usuarios según estos atributos en el panel.

### Atributos predeterminados del usuario

Para configurar los atributos de usuario recogidos automáticamente por Braze, puedes utilizar los métodos de configuración que vienen con el SDK. Por ejemplo, puedes configurar el nombre de pila del usuario:

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetFirstName("first_name");
```

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetFirstName("first_name");
```

{% endtab %}
{% endtabs %}

Se admiten los siguientes atributos:

- Nombre
- Apellido
- Género
- Fecha de nacimiento
- Ciudad natal
- País
- Número de teléfono
- Correo electrónico

### Atributos personalizados del usuario

Además de nuestros métodos predefinidos de atributos de usuario, Braze también proporciona atributos personalizados utilizando `SetCustomUserAttribute` para hacer un seguimiento de los datos de tus aplicaciones.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

Consulta [las instrucciones de integración en Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) para conocer en profundidad las mejores prácticas e interfaces de seguimiento de atributos.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

Consulta [las instrucciones de integración en]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift) iOS para conocer en profundidad las mejores prácticas e interfaces de seguimiento de atributos.

{% endtab %}
{% endtabs %}
