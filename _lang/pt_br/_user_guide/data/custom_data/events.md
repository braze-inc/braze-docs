---
nav_title: Eventos
article_title: Eventos
page_order: 0
page_type: reference
description: "Este artigo descreve os diferentes eventos no Braze - eventos padrão, eventos de compra e eventos personalizados - e suas finalidades."
---

# Eventos 

> Esta página cobre os diferentes eventos no Braze e seu propósito.

Braze usa alguns tipos de eventos diferentes para fornecer uma compreensão abrangente do comportamento do usuário e do engajamento com sua marca. Cada tipo de evento tem uma finalidade específica:

- [Eventos padrão](#standard-events): Fornecer uma compreensão básica do engajamento do usuário com seu app ou site.
- [Eventos de compra](#purchase-events): Crucial para entender o comportamento de compra do usuário e para o rastreamento da receita. 
- [Eventos personalizados](#custom-events): Forneça insights mais profundos sobre os comportamentos dos usuários que são exclusivos do seu app ou empresa.

Ao rastrear esses diferentes tipos de eventos, você pode obter uma compreensão mais profunda de seus usuários, o que pode informar suas estratégias de marketing, ajudá-lo a otimizar seu app e capacitá-lo a fornecer uma experiência de usuário mais personalizada. Vamos mergulhar!

## Eventos padrão

No Braze, os eventos padrão são ações predefinidas que os usuários podem realizar no seu app e que o Braze rastreia automaticamente após a integração do SDK do Braze. Aqui estão alguns exemplos de eventos padrão:

- Lançamento do app
- [Compra](#purchase-events)
- Início da sessão
- Fim da sessão
- Clique na notificação por push
- Abriu o e-mail

Como profissional de marketing, você pode usar esses eventos padrão para entender o comportamento do usuário e o engajamento com seu app. Por exemplo, você pode ver com que frequência os usuários estão lançando seu app ou quantas compras estão sendo feitas. Essas informações podem ser valiosas quando se trata de criar campanhas de marketing direcionadas.

É importante notar que, embora os eventos padrão sejam automaticamente rastreados pelo Braze, os eventos de compra, os eventos personalizados e os atributos personalizados precisam ser configurados pela sua equipe de desenvolvimento com base em suas necessidades e objetivos específicos.

## Eventos de compra

Os eventos de compra são uma forma de registrar e rastrear as compras feitas pelos seus usuários. Eles são um tipo de evento padrão que está disponível por padrão depois que você integra o SDK da Braze. Por isso, quando você usa eventos de compra para rastrear compras, pode monitorar sua receita ao longo do tempo e em diferentes fontes de receita diretamente da Braze.

Os eventos de compra registram as seguintes informações importantes sobre uma compra:

- ID do produto (normalmente, o nome ou a categoria do produto)
- Moeda
- Preço
- Quantidade

Em seguida, é possível usar esses dados para segmentar seus usuários com base no valor do tempo de vida, na frequência de compra, em compras específicas e muito mais.

O Braze também oferece suporte a compras em várias moedas. Se uma compra for informada em uma moeda diferente de USD, ela será exibida no dashboard da Braze em USD, com base na taxa de câmbio na data em que a compra foi informada.

Para saber mais, acesse nosso artigo dedicado a [eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/).

{% details Implementação de exemplo %}

Nota que a implementação real dos eventos de compra exigirá algum conhecimento técnico, pois envolve a integração do SDK Braze com seu app. O gerente de sucesso do cliente orientará sua equipe nesse processo como parte da integração, mas as etapas gerais são as seguintes:

1. **Integrar o SDK do Braze:** Antes de registrar qualquer evento, você precisa integrar o SDK do Braze em seu app.
2. **Registre o evento de compra:** Após a integração do SDK, é possível registrar um evento de compra sempre que um usuário fizer uma compra em seu app. Normalmente, isso é feito na função ou no método chamado quando uma compra é concluída.

Veja um exemplo de como registrar um evento de compra em um app iOS usando Swift:

```swift
Appboy.sharedInstance()?.logPurchase("product_name", inCurrency: "USD", atPrice: NSDecimalNumber(string: "1.99"), withQuantity: 1)
```

Neste exemplo, "product_name" é o nome do produto que foi comprado, "USD" é a moeda da compra, "1,99" é o preço do produto e "1" é a quantidade comprada.

{:start="3"}
3\. **Visualize o evento de compra no dashboard da Braze:** Depois que o evento de compra for registrado, você poderá visualizá-lo no dashboard da Braze. Você pode usar esses dados para analisar sua receita, segmentar seus usuários e muito mais.

Lembre-se de que a implementação exata pode variar dependendo da plataforma (iOS, Android, Web) e dos requisitos específicos de seu app. 

{% enddetails %}

## Eventos personalizados

Eventos personalizados são eventos que você define com base nas ações específicas que deseja rastrear em seu app ou site. O Braze não os rastreia automaticamente—você deve configurar manualmente esses eventos na sua implementação do SDK do Braze. Os eventos personalizados podem ser qualquer coisa, desde um usuário que completa um nível em um jogo até um usuário que atualiza suas informações de perfil.

Veja um exemplo de como registrar um evento personalizado em um app iOS usando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("completed_level")
```

Neste exemplo, "completed_level" é o nome do evento personalizado que é registrado quando um usuário completa um nível em um jogo. Esse evento personalizado é então registrado no perfil do usuário no Braze, que pode ser usado para disparar campanhas e personalizar o envio de mensagens.

Para saber mais, visite nosso artigo dedicado a [eventos personalizados]({{site.baseurl}}/user_guide/data/custom_data/custom_events/).

{% details Implementação de exemplo %}

Semelhante aos eventos de compra, os eventos personalizados exigem configuração adicional. Aqui está um processo geral para implementar eventos personalizados no Braze:

1. **Integrar o SDK do Braze:** Antes de registrar qualquer evento, você precisa integrar o SDK do Braze em seu app.
2. **Defina seu evento personalizado:** Decida qual ação em seu app você deseja rastrear como um evento personalizado. Pode ser qualquer coisa que seja significativa para o seu app, como um usuário que completa um nível em um jogo, um usuário que atualiza seu perfil ou um usuário que faz um tipo específico de compra.
3. **Registre o evento personalizado:** Depois de definir o evento personalizado, é possível registrá-lo no código do app. Normalmente, isso é feito na função ou no método que é chamado quando a ação ocorre.

Veja um exemplo de como registrar um evento personalizado em um app iOS usando Swift:

```swift
Appboy.sharedInstance()?.logCustomEvent("updated_profile")
```

Neste exemplo, "updated_profile" é o nome do evento personalizado que é registrado quando um usuário atualiza seu perfil.

{:start="4"}
4\. **Adicione propriedades ao seu evento personalizado (opcional):** Se quiser capturar detalhes adicionais sobre o evento personalizado, você pode adicionar propriedades a ele. Isso é feito passando um dicionário de propriedades ao registrar o evento.

Aqui está um exemplo de como registrar um evento personalizado com propriedades em um app iOS usando Swift:

```swift
let properties: [AnyHashable: Any] = ["Property Name": "Property Value"]
Appboy.sharedInstance()?.logCustomEvent("updated_profile", withProperties: properties)
```

Neste exemplo, o evento personalizado tem uma propriedade chamada "Property Name" (Nome da propriedade) com um valor de "Property Value" (Valor da propriedade).

{:start="5"}
5\. **Visualize o evento personalizado no dashboard do Braze:** Depois que o evento personalizado for registrado, você poderá visualizá-lo no dashboard da Braze. É possível usar esses dados para analisar o comportamento do usuário, segmentar seus usuários e muito mais.

{% enddetails %}

<!--

### Using custom events instead of purchase events to track purchases

You might prefer to use custom events to track purchases if you need to capture more specific or additional information about the purchase that the standard purchase event doesn't cover. Here's what you can do with custom events that you can't accomplish with purchase events:

- **Custom definitions:** Custom events can be defined based on any significant action within your app. This level of customization is not available with standard purchase events, which are predefined and specifically designed to track purchases.
- **Additional properties:** You can log additional properties to custom events that provide more context about the event. For example, you could log a custom event when a user makes a purchase and include properties such as the product category or the payment method. This is not possible with standard purchase events, which have a fixed schema that only tracks the product name, currency, price, and quantity.
- **Event frequency:** Custom events allow you to track the frequency of specific actions. With purchase events, you can only track the occurrence of purchases, not other types of actions.

#### Use case 1

Let's say you have an eCommerce app, and you want to track the purchase itself and the product category. The standard purchase event in Braze does not capture this level of detail, so you could use a custom event instead.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Product Category": "Electronics"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the product category is "Electronics". Now you can segment your users based on the product categories they purchase from.

#### Use case 2

Consider a fitness app where users can purchase personal training sessions or premium workout plans. In this case, you might want to track these purchases as custom events to capture additional details about the purchase.

Here's an example of how you might do this in an iOS app using Swift:

```swift
let properties: [AnyHashable: Any] = ["Workout Plan": "10 Sessions Personal Training"]
Appboy.sharedInstance()?.logCustomEvent("Purchase", withProperties: properties)
```

In this example, "Purchase" is the name of the custom event, and the properties dictionary contains additional information about the event. In this case, the workout plan is "10 Sessions Personal Training". Now you can segment your users based on the types of workout plans they purchase.

-->


