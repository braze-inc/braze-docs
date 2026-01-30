---
nav_title: Configuração de integração padrão da Shopify
article_title: "Configuração de integração padrão da Shopify"
description: "Este artigo de referência descreve como configurar a integração padrão do Shopify."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# Configuração da integração padrão do Shopify

> Esta página o orienta sobre como integrar o Braze ao Shopify usando nossa integração padrão para usuários com uma loja on-line do Shopify. Se você usa um site headless da Shopify ou está procurando implementar soluções mais personalizadas, consulte a [configuração de integração personalizada da Shopify]({{site.baseurl}}/shopify_custom_integration/).

## Etapa 1: Conecte sua loja da Shopify

1. Na Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e depois procure "Shopify".

{% alert note %}
Se estiver usando a navegação mais antiga, poderá encontrar **Technology Partners** em **Integrations**.
{% endalert %}

{: start="2"}
2\. Na página do parceiro do Shopify, selecione **Iniciar configuração** para iniciar o processo de integração.<br><br>![Página de integração do Shopify com botão para iniciar a configuração.]({% image_buster /assets/img/Shopify/begin_setup.png %})<br><br> 
3\. Na loja de aplicativos da Shopify, instale o aplicativo Braze.<br><br>![A página da loja de aplicativos Braze com um botão para instalar o aplicativo.]({% image_buster /assets/img/Shopify/shopify_log_in.png %}){: style="max-width:70%;"}

{% alert note %}
Se sua conta da Shopify estiver associada a mais de uma loja, você poderá alterar a loja em que está registrado selecionando o ícone da loja no canto superior direito da página e selecionando **Alternar lojas**.
{% endalert %}

{: start="4"}
4\. Depois de instalar o app Braze, você será redirecionado ao Braze para confirmar o espaço de trabalho que deseja conectar ao Shopify. Uma loja da Shopify pode se conectar a apenas um espaço de trabalho. Se precisar mudar, selecione o espaço de trabalho correto.<br><br>![Uma janela solicita a confirmação de que você está no espaço de trabalho correto.]({% image_buster /assets/img/Shopify/confirm_workspace1.png %}){: style="max-width:70%;"}

{: start="5"}
5\. Selecione **Iniciar configuração**.<br><br>!["Configurações de integração" com campo para inserir o domínio e um botão para iniciar a configuração.]({% image_buster /assets/img/Shopify/choose_account.png %})

## Etapa 2: Ativar os SDKs do Braze Web

Para lojas on-line do Shopify, você pode selecionar a configuração padrão para implementar automaticamente o Braze Web SDK e o JavaScript SDK.

![Etapa "Ativar Web SDK" com opções para implementar por meio de uma configuração padrão ou personalizada.]({% image_buster /assets/img/Shopify/sdk_setup.png %})

Depois de selecionar a jornada de integração da configuração padrão, você precisará escolher quando o Braze deve inicializar e carregar os SDKs em uma das seguintes opções: 
- Na visita ao local, como no início da sessão
    - Rastreamento de usuários identificados e anônimos
- Após o registro da conta, como o login da conta
    - Rastreia apenas usuários identificados
    - Começa o rastreamento de dados quando os visitantes do site inscrevem-se ou fazem login em suas contas

## Etapa 3: Configure seus dados da Shopify

### Configuração de dados padrão

Agora você selecionará os dados do Shopify que deseja rastrear.

![Seção "Tracking Shopify data" (Rastreamento de dados do Shopify) com uma caixa de seleção para rastrear eventos comportamentais e atribuições de usuários.]({% image_buster /assets/img/Shopify/tracking_shopify_data.png %})

Os seguintes eventos serão ativados por padrão na integração padrão.

| Eventos recomendados pelo Braze | Eventos personalizados da Shopify | Atributos personalizados da Shopify |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Produto visualizado</li><li>Carrinho atualizado</li><li>Checkout iniciado</li><li>Pedido feito</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_account_login</li><li>shopify_paid_order</li><li>shopify_order_canceled</li><li>shopify_order_refunded</li><li>shopify_order_fulfilled</li><li>shopify_order_partially_fulfilled</li></ul>{:/} | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li><li>shopify_province</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

Para saber mais sobre os dados rastreados por meio da integração, consulte [Recursos de dados do Shopify]({{site.baseurl}}/shopify_data_features/).

{% multi_lang_include alerts/important_alerts.md alert='Shopify customer create' %}

### Configuração histórica de aterro

Por meio da configuração padrão, você tem a opção de realizar um carregamento inicial de seus clientes e pedidos do Shopify dos últimos 90 dias antes da conexão de integração com o Shopify. Para isso, marque a caixa de seleção para incluir o carregamento inicial de dados como parte de sua integração. 

![Alternância de backfill de dados históricos.]({% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %})

Essa tabela contém os dados que serão carregados inicialmente por meio do backfill.

| Eventos recomendados pelo Braze | Eventos personalizados da Shopify | Atribuições padrão do Braze | Status das inscrições no Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Pedido feito</li></ul>{:/}  | {::nomarkdown}<ul><li>shopify_tags</li><li>shopify_total_spent</li><li>shopify_order_count</li><li>shopify_last_order_id</li><li>shopify_last_order_name</li><li>shopify_zipcode</li>shopify_province</li></ul>{:/} | {::nomarkdown}<ul><li>E-mail</li><li>Nome</li><li>Sobrenome</li><li>Telefone</li><li>Cidade</li><li>País</li></ul>{:/} | {::nomarkdown}<ul><li>Inscrições de envio de e-mail marketing associadas a esta loja Shopify</li><li>Inscrições de marketing por SMS associadas a esta loja da Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

À medida que seus registros de clientes do Shopify forem carregados no Braze, o ID do cliente do Shopify será usado como o ID externo do Braze. 

{% alert note %}
Se você já é cliente do Braze com campanhas ativas ou Canvas, consulte [os recursos de dados do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) para obter mais detalhes.
{% endalert %}

### (Avançado) Configuração de rastreamento de dados personalizados

Com os SDKs do Braze, você pode rastrear eventos personalizados ou atributos personalizados que vão além dos eventos padrão para essa integração. Os eventos personalizados capturam interações exclusivas em sua loja, como:

<style>
#custom-data td {
    word-break: break-word;
    width: 50%;
}
</style>

<table style="width: 100%;">
  <thead>
    <tr>
      <th style="width: 50%;">Eventos personalizados</th>
      <th style="width: 50%;">Atributos personalizados</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>
        <ul>
          <li>Como usar um código de desconto personalizado</li>
          <li>Como interagir com uma recomendação personalizada de produto</li>
          <li>Como adicionar uma mensagem de presente ao pedido</li>
        </ul>
      </td>
      <td>
        <ul>
          <li>Marcas ou produtos favoritos</li>
          <li>Categorias de compras de preferência</li>
          <li>Status de cadastro ou fidelidade</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

O rastreamento de dados personalizados fornece insights mais profundos sobre o comportamento do usuário e oferece suporte à personalização adicional. Para implementar eventos personalizados, é necessário editar [o código do tema de](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) sua [loja](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) no arquivo `theme.liquid`. Talvez você precise da ajuda de seus desenvolvedores.

Por exemplo, o snippet JavaScript a seguir rastreia se o usuário atual está inscrito em uma newsletter e registra essa informação como um evento personalizado no perfil de usuário na Braze:

```json
braze.logCustomEvent(
  “subscribed_to_newsletter”,
  {
    newsletterName: ‘News and Offers’,
    customerEmail: ‘customer_1@gmail.com’,
    sendOffers: true
  }
);

```

O SDK deve ser inicializado (ouvindo a atividade) no dispositivo de um usuário para registrar eventos ou atributos personalizados. Para saber mais sobre o registro de dados personalizados, consulte o [objeto User](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) e o [objeto logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

## Etapa 4: Configurar como gerenciar usuários {#step-4}

Selecione seu tipo de `external_id` no menu suspenso. 

![Seção "Coletar assinantes".]({% image_buster /assets/img/Shopify/external_id_standard.png %})

{% alert important %}
Usar um endereço de e-mail ou um endereço de e-mail com hash como sua ID externa Braze pode simplificar o gerenciamento de identidade em suas fontes de dados. No entanto, é importante considerar os possíveis riscos à privacidade do usuário e à segurança dos dados.<br><br>

- **Informações que podem ser adivinhadas:** Os endereços de e-mail são facilmente adivinháveis, o que os torna vulneráveis a ataques.
- **Risco de exploração:** Se um usuário mal-intencionado alterar seu navegador da Internet para enviar o endereço de e-mail de outra pessoa como sua ID externa, ele poderá acessar mensagens confidenciais ou informações de conta.
{% endalert %}

Por padrão, o Braze converte automaticamente os e-mails do Shopify em letras minúsculas antes de usá-los como ID externo. Se estiver usando e-mail ou envio de e-mail com hash como ID externo, confirme se os endereços de e-mail também foram convertidos em letras minúsculas antes de atribuí-los como ID externo ou antes de fazer o hash a partir de outras fontes de dados. Isso ajuda a evitar discrepâncias nas IDs externas e evita a criação de perfis de usuário duplicados no Braze.

{% alert note %}
As próximas etapas dependem da seleção de sua ID externa:<br><br>
- **Se você selecionou um tipo de ID externo personalizado:** Conclua as etapas 4.1-4.3 para definir sua configuração de ID externa personalizada.
- **Se você selecionou o ID do cliente da Shopify, e-mail ou e-mail com hash:** Pule as etapas 4.1-4.3 e vá diretamente para a etapa 4.4.
{% endalert %}

### Etapa 4.1: Criar o metacampo `braze.external_id` 

1. Em seu painel de administração do Shopify, acesse **Configurações** > **Metacampos e metaobjetos**.
2. Selecione **Clientes** > **Adicionar definição**.
3. Em **Name**, digite `braze.external_id`. 
4. Selecione o namespace e a chave gerados automaticamente (`custom.braze_external_id`) para editá-los e alterá-los para `braze.external_id`.
5. Em **Type**, selecione **ID Type**.

Depois que o metacampo for criado, preencha-o para seus clientes. Recomendamos as seguintes abordagens:

- **Ouça os webhooks de criação de clientes:** Configure um webhook para ouvir os [eventos do`customer/create` ](https://help.shopify.com/en/manual/fulfillment/setup/notifications/webhooks). Isso permite que você escreva o metacampo quando um novo cliente é criado.
- **Preencher os clientes existentes:** Use a [Admin API](https://shopify.dev/docs/api/admin-graphql) ou a [Customer API](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para preencher novamente o metacampo de clientes criados anteriormente.

### Etapa 4.2: Crie um ponto de extremidade para recuperar sua ID externa

Você deve criar um endpoint público que o Braze possa chamar para recuperar o ID externo. Isso permite que o Braze busque o ID em cenários em que o Shopify não pode fornecer o metacampo `braze.external_id` diretamente.

#### Especificações do endpoint

**Método:** OBTER

O Braze envia os seguintes parâmetros para seu endpoint:

| Parâmetro            | Obrigatória | Tipo de dados | Descrição                                                      |
|----------------------|----------|-----------|------------------------------------------------------------------|
| shopify_customer_id  | Sim      | String    | O ID do cliente da Shopify.                                         |
| shopify_storefront   | Sim      | String    | O nome da loja para a solicitação. Ex: `<storefront_name>.myshopify.com` |
| email_address        | Não       | String    | O endereço de e-mail do usuário registrado. <br><br>Esse campo pode estar ausente em determinados cenários de webhook. Sua lógica de endpoint deve levar em conta os valores nulos aqui (por exemplo, busque o e-mail usando o shopify_customer_id se sua lógica interna exigir isso). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

#### Exemplo de endpoint

```http
GET https://mystore.com/custom_id?shopify_customer_id=1234&email_address=bob@braze.com&shopify_storefront=dev-store.myshopify.com
```

#### Resposta esperada
O Braze espera um código de status `200` retornando o JSON do ID externo:
```json
{
  "external_id": "my_external_id"
}
```

#### Validação
É fundamental validar se os sites `shopify_customer_id` e `email_address` (se houver) correspondem aos valores do cliente na Shopify. Você pode usar a [API](https://shopify.dev/docs/api/admin-graphql) [do](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) [Shopify Admin](https://shopify.dev/docs/api/admin-graphql) ou [a API do cliente](https://shopify.dev/docs/api/admin-rest/2025-04/resources/customer) para validar esses parâmetros e recuperar o metacampo `braze.external_id` correto.

#### Comportamento de falha e fusão
Qualquer código de status diferente de `200` é considerado uma falha.

- **Implicações da fusão:** Se o endpoint falhar (não retornar`200` ou atingir o tempo limite), o Braze não poderá recuperar a ID externa. Consequentemente, a fusão entre o usuário do Shopify e o perfil do usuário do Braze não ocorrerá nesse momento.
- **Lógica de repetição:** O Braze poderá tentar novas tentativas de rede padrão imediatas, mas se a falha persistir, a mesclagem será adiada até o próximo evento de qualificação (por exemplo, a próxima vez que o usuário atualizar seu perfil ou concluir um checkout).
- **Capacidade de suporte:** Para dar suporte à mesclagem de usuários em tempo hábil, certifique-se de que o seu endpoint esteja altamente disponível e lide com o campo opcional `email_address` de forma adequada.

### Etapa 4.3: Insira sua ID externa

Repita [a etapa 4](#step-4) e insira o URL do endpoint depois de selecionar ID externa personalizada como o tipo de ID externa do Braze.

#### Considerações

- Se seu ID externo não for gerado quando o Braze enviar uma solicitação ao seu endpoint, a integração usará por padrão o ID do cliente do Shopify quando a função `changeUser` for chamada. Essa etapa é crucial para mesclar o perfil do usuário anônimo com o perfil do usuário identificado. Como resultado, pode haver um período temporário durante o qual diferentes tipos de IDs externas existam em seu espaço de trabalho.
- Quando a ID externa estiver disponível no metacampo `braze.external_id`, a integração priorizará e atribuirá essa ID externa. 
    - Se o ID do cliente do Shopify tiver sido definido anteriormente como o ID externo do Braze, ele será substituído pelo valor do metacampo `braze.external_id`. 

### Etapa 4.4: Colete suas aceitações de e-mail ou SMS do Shopify (opcional)

Você tem a opção de coletar suas aceitações de marketing por e-mail ou SMS no Shopify. 

Se você usar os canais de e-mail ou SMS, poderá sincronizar seus estados de aceitação de marketing por e-mail e SMS no Braze. Se você sincronizar as aceitações de e-mail marketing do Shopify, o Braze criará automaticamente um grupo de inscrições para e-mail para todos os usuários associados a essa loja específica. Você precisa criar um nome exclusivo para esse grupo de inscrições.

![Seção "Coletar assinantes" com a opção de coletar aceitação de marketing por e-mail ou SMS.]({% image_buster /assets/img/Shopify/collect_email_subscribers.png %})

{% alert note %}
Conforme mencionado na [visão geral do Shopify]({{site.baseurl}}/shopify_overview/), se você quiser usar um formulário de captura de terceiros, seus desenvolvedores precisarão integrar o código do Braze SDK. Isso permitirá que você capture o endereço de e-mail e o status global da inscrição de e-mail dos envios de formulários. Especificamente, você precisa implementar e testar esses métodos em seu arquivo `theme.liquid`:<br><br>
- [setEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Define o endereço de e-mail no perfil do usuário
- [setEmailNotificationSubscriptionType](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Atualiza o status da inscrição global de e-mail
{% endalert %}

## Etapa 5: Sincronizar produtos (opcional)

Você pode sincronizar todos os produtos de sua loja Shopify com um catálogo Braze para uma personalização mais profunda do envio de mensagens. As atualizações automáticas ocorrem quase em tempo real para que seu catálogo reflita os detalhes atualizados dos produtos. Para saber mais, confira a [sincronização de produtos da Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_catalogs/).

![Etapa 4 do processo de configuração com "Shopify Variant ID" como o "Catalog product identifier" (Identificador de produto do catálogo).]({% image_buster /assets/img/Shopify/sync_products_step1.png %}){: style="max-width:80%;"}

## Etapa 6: Ativar canais (opcional)

É possível ativar as mensagens no app sem usar um desenvolvedor, configurando-as em sua instalação.

![Etapa de configuração para ativar os canais, sendo que a opção disponível é o envio de mensagens no navegador.]({% image_buster /assets/img/Shopify/activate_channels_standard.png %})

{% alert note %}
O Braze coleta informações dos visitantes, como endereços de e-mail e números de telefone, por meio de mensagens no navegador. Essas informações são enviadas para a Shopify. Esses dados ativam os comerciantes a reconhecer os visitantes de suas lojas e a criar uma experiência de compra mais personalizada. Para obter mais detalhes, consulte [API do visitante](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

### Suporte a canais SDK adicionais

Os SDKs da Braze ativam vários canais de envio de mensagens, incluindo cartões de conteúdo.

#### Cartões de conteúdo e Feature Flags

Para adicionar cartões de conteúdo ou sinalizadores de recursos, você precisará colaborar com seus desenvolvedores para inserir o código SDK necessário diretamente em seu arquivo `theme.liquid`. Para obter instruções detalhadas, consulte [Integração do SDK do Braze]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### Notificações por push na Web

Atualmente, não há suporte para web push na integração com o Shopify. Para solicitar suporte, envie uma solicitação de produto por meio do [portal do produto Braze]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Etapa 7: Concluir configuração

1. Depois de fazer as configurações, selecione **Finish Setup** (Concluir configuração).
2. Ative a incorporação do app Braze nas configurações do tema do Shopify. Selecione **Open Shopify** para ser redirecionado à sua conta do Shopify e ativar a incorporação do app nas configurações de tema da sua loja. 

![Banner que diz que você precisa ativar a incorporação do app Braze no Shopify e contém um botão para abrir o Shopify.]({% image_buster /assets/img/Shopify/open_shopify.png %})

{: start="3"}
3\. Depois de ativar a incorporação do app, sua configuração estará concluída!
Confirme que você pode visualizar suas configurações de integração, o status da sincronização inicial de dados e seus eventos ativos do Shopify. <br><br>![Página do parceiro da Shopify exibindo as configurações de integração.]({% image_buster /assets/img/Shopify/install_complete.png %})