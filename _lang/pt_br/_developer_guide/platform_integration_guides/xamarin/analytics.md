---
nav_title: Análise de dados
article_title: Análise de dados para Xamarin
platform: 
  - Xamarin
  - iOS
  - Android
page_order: 4
description: "Este artigo aborda a análise de dados do iOS, Android e FireOS para a plataforma Xamarin."

---
 
# Análise de dados do Xamarin

> Saiba como gerar e revisar análises de dados para a plataforma Xamarin.

## Rastreamento de sessão

O Braze SDK informa os dados da sessão usados pelo dashboard do Braze para calcular o engajamento do usuário e outras análises essenciais para entender seus usuários. Com base na semântica de sessão a seguir, nosso SDK gera pontos de dados de "início de sessão" e "encerramento de sessão" que levam em conta a duração da sessão e as contagens de sessão visíveis no dashboard do Braze.

Para definir um ID de usuário ou iniciar uma sessão, use o método `ChangeUser`, que recebe um parâmetro de ID de usuário.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).ChangeUser("user_id");
```

Consulte as [instruções de integração com o Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/) para obter uma discussão detalhada sobre quando e como definir e alterar uma ID de usuário.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.ChangeUser("user_id");
```

Consulte as [instruções de integração do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_user_ids/) para obter uma discussão detalhada sobre quando e como definir e alterar uma ID de usuário.

{% endtab %}
{% endtabs %}

## Registro de eventos personalizados

É possível registrar eventos personalizados no Braze usando `LogCustomEvent` para saber mais sobre os padrões de uso do seu app e para segmentar seus usuários por suas ações no dashboard.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogCustomEvent("event_name");
```

Consulte as [instruções de integração do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/tracking_custom_events/) para obter uma discussão aprofundada sobre as práticas recomendadas e interfaces de rastreamento de eventos.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogCustomEvent("event_name");
```

Consulte as [instruções de integração do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/tracking_custom_events/) para obter uma discussão detalhada sobre as práticas recomendadas e interfaces de rastreamento de eventos.

{% endtab %}
{% endtabs %}

## Registro de compras

Registre as compras in-app usando `LogPurchase` para rastrear sua receita ao longo do tempo e entre as fontes de receita, bem como segmentar seus usuários pelo valor do tempo de vida deles.

O Braze oferece suporte a compras em várias moedas. As compras informadas em uma moeda diferente do dólar americano serão mostradas no dashboard em dólares americanos com base na taxa de câmbio na data em que foram informadas.

{% tabs %}
{% tab Android %}
```csharp
Braze.GetInstance(this).LogPurchase("product_id", "USD", new Java.Math.BigDecimal(3.50));
```

Consulte as [instruções de integração do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/logging_purchases/) para obter uma discussão detalhada sobre as melhores práticas e interfaces de rastreamento de receita.

{% endtab %}
{% tab iOS %}
```csharp
App.braze?.LogPurchase("product_id", "USD", 3.50);
```

Consulte as [instruções de integração do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/logging_purchases/) para obter uma discussão detalhada sobre as práticas recomendadas e interfaces de rastreamento de receita.

{% endtab %}
{% endtabs %}

### Registre as compras no nível do pedido

Se quiser registrar as compras no nível do pedido em vez de no nível do produto, poderá usar o nome do pedido ou a categoria do pedido como `product_id`. Consulte nossa [especificação de objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/#product-id-naming-conventions) para saber mais. 

### Chaves reservadas

As seguintes chaves são reservadas e **não podem** ser usadas como propriedades de compra:

- `time`
- `product_id`
- `quantity`
- `event_name`
- `price`
- `currency`

## Registro de atributos personalizados

O Braze fornece métodos para atribuir atribuições aos usuários. Você poderá filtrar e segmentar seus usuários de acordo com essas atribuições no dashboard.

### Atribuições padrão do usuário

Para atribuir atribuições de usuário coletadas automaticamente pela Braze, você pode usar os métodos setter fornecidos com o SDK. Por exemplo, é possível definir o nome do usuário:

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

Consulte as [instruções de integração do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_custom_attributes/) para obter uma discussão detalhada sobre as melhores práticas e interfaces de rastreamento de atribuições.

{% endtab %}
{% tab iOS %}

```csharp
App.braze?.User.SetCustomAttributeWithKey("custom_attribute_key", true);
```

Consulte as [instruções de integração do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/analytics/setting_custom_attributes/) para obter uma discussão detalhada das práticas recomendadas e interfaces de rastreamento de atribuições.

{% endtab %}
{% endtabs %}

## monitoramento de localização

Para obter um exemplo de análise de registro e rastreamento, consulte nossos aplicativos de amostra [Android MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/android-net-maui/BrazeAndroidMauiSampleApp/BrazeAndroidMauiSampleApp/MainActivity.cs) e [iOS MAUI](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/appboy-component/samples/ios-net-maui/BrazeiOSMauiSampleApp/BrazeiOSMauiSampleApp/MainPage.xaml.cs).

{% tabs %}
{% tab Android %}
Para saber mais, consulte as [instruções de integração do Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/location_tracking/).
{% endtab %}

{% tab ios %}
Para oferecer suporte ao rastreamento local, consulte [iOS: Usando o local em segundo plano](http://developer.xamarin.com/guides/cross-platform/application_fundamentals/backgrounding/part_4_ios_backgrounding_walkthroughs/location_walkthrough/) e as [instruções de integração com o iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/locations_and_geofences/).
{% endtab %}
{% endtabs %}

