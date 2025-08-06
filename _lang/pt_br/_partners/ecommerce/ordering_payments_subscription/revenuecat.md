---
nav_title: RevenueCat
article_title: RevenueCat
description: "A integração do RevenueCat e Braze permite que você sincronize automaticamente os eventos do ciclo de vida de compra e inscrição dos seus clientes em todas as plataformas. Isso permite que você crie campanhas que reagem ao estágio do ciclo de vida da inscrição de seus clientes, como engajar com clientes que optaram por sair durante o período de teste gratuito ou enviar lembretes para clientes com problemas de faturamento."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> A [RevenueCat](https://www.revenuecat.com/) é a única fonte da verdade do status da sua inscrição em iOS, Android e web. Quer você esteja construindo um novo app ou já tenha milhões de assinantes, é possível usar a RevenueCat para criar compras em aplicativos multiplataforma, gerenciar seus produtos e assinantes e analisar seus dados – sem necessidade de código de servidor.

_Essa integração é mantida pelo RevenueCat._

## Sobre a integração

A integração do RevenueCat e Braze permite que você sincronize automaticamente os eventos do ciclo de vida de compra e inscrição dos seus clientes em todas as plataformas. Isso permite que você crie campanhas que reagem ao estágio do ciclo de vida da inscrição de seus clientes, como engajar com clientes que optaram por sair durante o período de teste gratuito ou enviar lembretes para clientes com problemas de faturamento.

## Pré-requisitos

No mínimo, será necessário ativar a integração do dashboard da RevenueCat para conectá-la à Braze. Se você estiver usando o SDK da Braze, poderá usar os SDKs da RevenueCat e da Braze juntos para aprimorar a integração, garantindo que o mesmo identificador de cliente seja usado em ambos os sistemas.

| Requisito | Descrição |
|---|---|
| Conta e app do RevenueCat | É necessário ter uma [conta no RevenueCat](https://app.revenuecat.com/login) para aproveitar essa parceria. Você também deve ter um app RevenueCat configurado. |
| SDK RevenueCat | Além do SDK do Braze necessário, recomendamos a instalação do [SDK do RevenueCat](https://docs.revenuecat.com/docs/configuring-sdk) para fornecer aliases de usuário ao RevenueCat. |
| Instância do Braze | Sua instância do Braze pode ser obtida com seu gerente de integração do Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints).<br><br>A RevenueCat requer que a instância da Braze envie do lado do servidor para o endpoint REST correto da Braze. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| teste da chave da API REST do Braze (opcional) | Uma chave de API de teste pode ser usada para compras de teste e produção se você quiser que essas solicitações sejam enviadas para instâncias da Braze separadas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso 

- Disparar uma campanha de integração destacando seus recursos premium quando um cliente iniciar um teste gratuito.
- Envie um lembrete para atualizar as informações de cobrança quando um evento de "Problema de Cobrança" for recebido.
- Envie uma pesquisa de feedback após um cliente cancelar um teste gratuito. 

## Integração

### Etapa 1: Definir identidade de usuário do Braze

No SDK da Braze, você pode definir o ID de usuário da Braze para corresponder ao ID de usuário do app da RevenueCat, garantindo que os eventos enviados da Braze e da RevenueCat possam ser sincronizados para o mesmo usuário.

Configure o SDK da Braze com o mesmo ID de usuário do app da RevenueCat ou use o método `.changeUser()` do SDK da Braze.

{% tabs local %}
{% tab SWIFT %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name", 
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Enviar objeto de alias de usuário para a Braze (opcional) 

Se você deseja enviar um identificador de usuário único alternativo diferente do ID de usuário do app RevenueCat, atualize os usuários com os seguintes dados como atributos de assinante do RevenueCat.

| Chave | Descrição |
|---|---|
| `$brazeAliasName` | O Braze `alias_name` no [objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
| `$brazeAliasLabel` | O Braze `alias_label` no [objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Ambos os atributos são necessários para que o [objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object/) seja enviado junto com seus dados de evento. Essas propriedades podem ser definidas manualmente, como qualquer outro [atributo de assinante do RevenueCat](https://docs.revenuecat.com/docs/subscriber-attributes). Exemplos de snippets de código são mostrados na etapa 1.

### Etapa 2: Enviar eventos do RevenueCat para a Braze

Depois de configurar o SDK de compras da RevenueCat e o SDK do Braze para ter a mesma identidade de usuário, você pode ativar a integração e configurar os nomes dos eventos no dashboard da RevenueCat.

1. Navegue até o seu projeto no dashboard da RevenueCat e encontre o cartão **Integrations** (Integrações) no menu à esquerda. Selecione **\+ Novo**.
2. Em seguida, selecione **Braze** da integração disponível e adicione sua instância da Braze e chave da API REST da Braze. 
3. Digite os nomes dos eventos que o RevenueCat enviará ou escolha os nomes dos eventos padrão. Mais detalhes sobre os eventos disponíveis podem ser encontrados na [etapa 3](#configure-event-names).
4. Selecione se deseja que a RevenueCat relate os rendimentos (após a comissão da app store) ou a receita (vendas brutas).

![Configurações do Braze no RevenueCat com campos para a instância do Braze, identificador de chave de API e identificador de sandbox.]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### Etapa 3: Configurar nomes de eventos {#configure-event-names}

Digite os nomes dos eventos que o RevenueCat enviará ou selecione entre os nomes de eventos padrão selecionando **Usar Nomes de Eventos Padrão**. Os eventos que a RevenueCat pode enviar estão descritos no gráfico a seguir.

| Evento | Descrição |
|---|---|
| Compra Inicial | A primeira compra de um produto de inscrição com renovação automática que não contém um teste gratuito. |
| Teste iniciado | O início de um período de teste gratuito de um produto de inscrição com renovação automática. |
| Teste Convertido | Quando um produto de inscrição com renovação automática é convertido de um teste gratuito para um período pago normal. |
| Teste cancelado | Quando um usuário desativa as renovações de um produto de inscrição com renovação automática durante um período de teste gratuito. |
| Renovação | Quando um produto de inscrição com renovação automática é renovado, ou um usuário recompra o produto de inscrição com renovação automática após uma interrupção na sua inscrição. |
| Cancelamento | Quando um usuário desativa as renovações de um produto de inscrição com renovação automática durante o período pago normal. |
| Compra sem inscrição | A compra de qualquer produto que não seja uma inscrição de renovação automática. |
| Expiração | Quando uma inscrição expira. |
| Problema de Cobrança | Quando houve um problema ao tentar cobrar o usuário. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para eventos que incluem receita, a RevenueCat registrará automaticamente esse valor junto com o evento na Braze, como conversões de teste e renovações.

## Usando esta integração

Depois de definir as configurações da Braze na RevenueCat, os eventos começarão a fluir automaticamente da RevenueCat para a Braze sem qualquer outra ação da sua parte.

## Personalização

### Adicione uma chave de API sandbox para testes

Se você fornecer apenas uma chave da API REST da Braze para a RevenueCat, apenas eventos de produção serão enviados. Se você também quiser enviar eventos de teste de sandbox, [crie outra chave da API REST do Braze]({{site.baseurl}}/api/basics/#app-group-rest-api-keys) e adicione-a às configurações do Braze no RevenueCat.


