{% multi_lang_include developer_guide/prerequisites/xamarin.md %}

## Definição das atribuições do usuário

Braze fornece métodos para atribuir atributos aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

### Atribuições padrão do usuário

Para definir as atribuições do usuário coletadas automaticamente pelo Braze, você pode usar os métodos setter fornecidos com o SDK. Por exemplo, é possível definir o nome do usuário:

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

Há suporte para as seguintes atribuições:

- Nome
- Sobrenome
- Gênero
- Data de nascimento
- Cidade
- País
- Número de telefone
- E-mail

### Atributos personalizados do usuário

Além de nossos métodos predefinidos de atribuição de usuários, a Braze também fornece atributos personalizados usando `SetCustomUserAttribute` para rastrear dados de seus aplicativos.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).CurrentUser.SetCustomUserAttribute("custom_attribute_key", true);
```

Consulte as [instruções de integração do Android]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=android) para obter uma discussão detalhada sobre as melhores práticas e interfaces de rastreamento de atribuições.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

Consulte as [instruções de integração do iOS]({{site.baseurl}}/developer_guide/analytics/setting_user_attributes/?sdktab=swift) para obter uma discussão detalhada das práticas recomendadas e interfaces de rastreamento de atribuições.

{% endtab %}
{% endtabs %}
