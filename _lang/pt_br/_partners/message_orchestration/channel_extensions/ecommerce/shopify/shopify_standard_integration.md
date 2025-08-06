---
nav_title: Configuração Padrão de Integração do Shopify
article_title: "Configuração Padrão de Integração do Shopify"
description: "Este artigo de referência descreve como configurar a integração padrão do Shopify."
page_type: partner
search_tag: Partner
alias: /shopify_standard_integration/
page_order: 1
---

# configuração padrão de integração do Shopify

> Esta página orienta você sobre como integrar o Braze com o Shopify usando nossa integração padrão para usuários com uma loja online Shopify. Se você usar um site headless do Shopify ou estiver procurando implementar soluções mais personalizadas, consulte [configuração de integração personalizada do Shopify]({{site.baseurl}}/shopify_custom_integration/).

## Etapa 1: Conecte sua loja da Shopify

1. Na Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e depois procure "Shopify".

{% alert note %}
Se você estiver usando a navegação mais antiga, pode encontrar **Parceiros de Tecnologia** em **Integrações**.
{% endalert %}

{: start="2"}
2\. Na página de parceiros do Shopify, selecione **Iniciar configuração** para começar o processo de integração.<br><br>![Página de integração do Shopify com botão para iniciar a configuração.][1]<br><br> 
3\. Na loja de aplicativos do Shopify, instale o aplicativo Braze.<br><br>![A página da loja de aplicativos Braze com um botão para instalar o aplicativo.][5]{: style="max-width:70%;"}

{% alert note %}
Se sua conta do Shopify estiver associada a mais de uma loja, você pode mudar a loja em que está logado selecionando o ícone da loja no canto superior direito da página e selecionando **Trocar lojas**.
{% endalert %}

{: start="4"}
4\. Após instalar o aplicativo Braze, você será redirecionado para o Braze para confirmar o espaço de trabalho que deseja conectar ao Shopify. Uma loja Shopify pode se conectar a apenas um espaço de trabalho. Se você precisar trocar, selecione o espaço de trabalho correto.<br><br>![Uma janela pedindo para você confirmar que está no espaço de trabalho correto.][2]{: style="max-width:70%;"}

{: start="5"}
5\. Selecione **Iniciar configuração**.<br><br>!["Configurações de integração" com campo para inserir o domínio e um botão para iniciar a configuração.][9]

## Etapa 2: Ativar SDKs Web do Braze

Para lojas online do Shopify, você pode selecionar a configuração padrão para implementar automaticamente o SDK Web do Braze e o SDK JavaScript.

![Etapa "Ativar SDK Web" com opções para implementar através de uma configuração padrão ou configuração personalizada.][3]

Após selecionar o caminho de integração padrão, você precisará escolher quando a Braze deve inicializar e carregar os SDKs a partir de uma das seguintes opções: 
- Na visita ao site, como o início da sessão
    - Rastreia tanto usuários identificados quanto anônimos
- Na inscrição da conta, como o login da conta
    - Rastreia apenas usuários identificados
    - Começa a rastrear dados quando os visitantes do site se inscrevem ou fazem login em suas contas

## Etapa 3: Configure seus dados do Shopify

### Configuração de dados padrão

Agora você selecionará os dados do Shopify que deseja rastrear.

![Seção "Rastreamento de dados do Shopify" com uma caixa de seleção para rastrear eventos comportamentais e atributos de usuário.][6]

Os seguintes eventos serão habilitados por padrão na integração padrão.

| Eventos recomendados pela Braze | Eventos personalizados da Shopify | Atributos personalizados da Shopify |
| --- | --- | --- |
| {::nomarkdown}<ul><li>Produto visualizado</li><li>Carrinho atualizado</li><li>Checkout iniciado</li><li>Pedido realizado</li></ul>{:/}  | {::nomarkdown}<ul><li>login_conta_shopify</li><li>pedido_pago_shopify</li><li>pedido_cancelado_shopify</li><li>pedido_devolvido_shopify</li><li>pedido_atendido_shopify</li><li>pedido_parcialmente_atendido_shopify</li></ul>{:/} | {::nomarkdown}<ul><li>tags do shopify</li><li>total gasto no shopify</li><li>contagem de pedidos do shopify</li><li>ID do último pedido do shopify</li><li>nome do último pedido do shopify</li><li>código postal do shopify</li><li>província do shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2  .reset-td-br-3 role="presentation"}

Para mais informações sobre os dados rastreados através da integração, consulte [Recursos de Dados do Shopify]({{site.baseurl}}/shopify_data_features/).

### Configuração de preenchimento histórico

Através da configuração padrão, você tem a opção de realizar um carregamento inicial de seus clientes e pedidos do Shopify dos últimos 90 dias antes da conexão de integração do Shopify. Para fazer isso, selecione a caixa de seleção para incluir o carregamento inicial de dados como parte de sua integração. 

![Alternar preenchimento de dados históricos.][4]

Esta tabela contém os dados que serão carregados inicialmente através do preenchimento.

| Eventos recomendados pela Braze | Eventos personalizados da Shopify | Atribuições padrão do Braze | status de inscrição do Braze |
| --- | --- | --- | --- |
| {::nomarkdown}<ul><li>Pedido realizado</li></ul>{:/}  | {::nomarkdown}<ul><li>tags do shopify</li><li>total gasto no shopify</li><li>contagem de pedidos do shopify</li><li>ID do último pedido do shopify</li><li>nome do último pedido do shopify</li><li>código postal do shopify</li>província do shopify</li></ul>{:/} | {::nomarkdown}<ul><li>E-mail</li><li>Nome</li><li>Sobrenome</li><li>Telefone</li><li>Cidade</li><li>País</li></ul>{:/} | {::nomarkdown}<ul><li>Inscrições de marketing por e-mail associadas a esta loja Shopify</li><li>Inscrições de marketing por SMS associadas a esta loja Shopify</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

À medida que os registros de clientes do Shopify são carregados no Braze, o ID do cliente do Shopify será usado como o ID externo do Braze. 

{% alert note %}
Se você é um cliente existente do Braze com campanhas ou Canvases ativas, revise [recursos de dados do Shopify]({{site.baseurl}}/shopify_data_features/#historical-backfill) para mais detalhes.
{% endalert %}

### (Avançado) Configuração de rastreamento de dados personalizados

Com os SDKs do Braze, você pode rastrear eventos personalizados ou atributos personalizados que vão além dos eventos padrão para esta integração. Eventos personalizados capturam interações únicas em sua loja, como:

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

O rastreamento de dados personalizados ajuda você a obter insights mais profundos sobre o comportamento do usuário e personalizar ainda mais sua experiência. Para implementar eventos personalizados, você precisa editar o código do tema da [vitrine](https://help.shopify.com/en/manual/online-store/themes/theme-structure/extend/edit-theme-code) em `theme.liquid` arquivo. Você pode precisar de ajuda de seus desenvolvedores.

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

O SDK deve ser inicializado (ouvindo por atividade) no dispositivo de um usuário para registrar eventos ou atributos personalizados. Para saber mais sobre o registro de dados personalizados, consulte [Objeto do usuário](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html) e [objeto logCustomEvent](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#logcustomevent).

## Etapa 4: Configure como você gerencia os usuários

Primeiro, selecione seu `external_id` no menu suspenso. 

Seção ![“Coletar assinantes”][10].

{% alert important %}
Usar um endereço de e-mail ou um endereço de e-mail hash como seu ID externo do Braze pode ajudar a simplificar a gestão de identidade entre suas fontes de dados. No entanto, é importante considerar os riscos potenciais à privacidade do usuário e à segurança dos dados.<br><br>

- **Informações Adivinháveis:** Os endereços de e-mail são facilmente adivinháveis, o que os torna vulneráveis a ataques.
- **Risco de Exploração:** Se um usuário mal-intencionado alterar seu navegador da Internet para enviar o endereço de e-mail de outra pessoa como sua ID externa, ele poderá acessar mensagens confidenciais ou informações de conta.
{% endalert %}

Em segundo lugar, você tem a opção de coletar suas aceitações de marketing por e-mail ou SMS do Shopify. 

Se você usar os canais de e-mail ou SMS, pode sincronizar os estados de aceitação de marketing por e-mail e SMS no Braze. Se você sincronizar as aceitações de marketing por e-mail do Shopify, o Braze criará automaticamente um grupo de assinaturas de e-mail para todos os usuários associados a essa loja específica. Você precisa criar um nome único para este grupo de assinaturas.

Seção ![“Coletar assinantes” com a opção de coletar aceitações de marketing por e-mail ou SMS.][13]

{% alert note %}
Conforme mencionado em [visão geral do Shopify]({{site.baseurl}}/shopify_overview/), se você quiser usar um formulário de captura de terceiros, seus desenvolvedores precisam integrar o código do SDK do Braze. Isso permitirá que você capture o endereço de e-mail e o status global de assinatura de e-mail a partir das submissões do formulário. Especificamente, você precisa implementar e testar esses métodos no seu `theme.liquid` arquivo:<br><br>
- [definirEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemail): Define o endereço de e-mail no perfil do usuário
- [definirTipoDeInscriçãoDeNotificaçãoPorEmail](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#setemailnotificationsubscriptiontype): Atualiza o status global de inscrição por e-mail
{% endalert %}

## Etapa 5: Sincronizar produtos (opcional)

Você pode sincronizar todos os produtos da sua loja Shopify para um catálogo Braze para uma personalização de mensagens mais profunda. Atualizações automáticas ocorrem em quase tempo real, então seu catálogo sempre reflete os detalhes mais recentes dos produtos. Para saber mais, confira [sincronização de produtos Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_catalogs/).

![Etapa 4 do processo de configuração com "ID da Variante Shopify" como o "identificador do produto do catálogo".][11]{: style="max-width:80%;"}

## Etapa 6: Ativar Canais (opcional)

Você pode ativar mensagens no aplicativo sem usar um desenvolvedor, configurando-as na sua configuração.

![Etapa de configuração para ativar canais, com a opção disponível sendo mensagens no navegador.][13]

### Suportando canais SDK adicionais

Os SDKs Braze habilitam vários canais de mensagens, incluindo mensagens no aplicativo e Cartões de Conteúdo.

#### Cartões de Conteúdo e Flags de Recursos

Para adicionar cartões de conteúdo ou flags de recursos, você precisará colaborar com seus desenvolvedores para inserir o código SDK necessário diretamente no seu `theme.liquid` arquivo. Para instruções detalhadas, consulte [Integrando o SDK Braze]({{site.baseurl}}/developer_guide/sdk_integration/). 

#### Notificações web push

Web push atualmente não é suportado para a integração Shopify. Se você quiser ver isso suportado no futuro, envie uma solicitação de produto através do [Braze product portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

Se você deseja ver isso suportado no futuro, envie uma solicitação de produto através do Braze [product portal]({{site.baseurl}}/user_guide/administrative/access_braze/portal/).

## Etapa 7: Concluir configuração

1. Depois de fazer as configurações, selecione **Finish Setup** (Concluir configuração).
2. Ative a incorporação do app Braze nas configurações do tema do Shopify. Selecione **Abrir Shopify** para ser redirecionado para sua conta Shopify para ativar a incorporação do app nas configurações do tema da sua loja. 

![Banner que diz que você precisa ativar a incorporação do app Braze no Shopify e contém um botão para abrir o Shopify.][7]

{: start="3"}
3\. Depois de ativar a incorporação do app, sua configuração está completa!
Confirme se você pode visualizar suas configurações de integração, o status da sincronização inicial de dados e seus eventos ativos do Shopify. <br><br>![Página de parceiro do Shopify exibindo as configurações de integração.][8]

[1]: {% image_buster /assets/img/Shopify/begin_setup.png %}
[2]: {% image_buster /assets/img/Shopify/confirm_workspace1.png %}
[3]: {% image_buster /assets/img/Shopify/sdk_setup.png %}
[4]: {% image_buster /assets/img/Shopify/historical_data_backfill_sync.png %}
[5]: {% image_buster /assets/img/Shopify/shopify_log_in.png %}
[6]: {% image_buster /assets/img/Shopify/tracking_shopify_data.png %}
[7]: {% image_buster /assets/img/Shopify/open_shopify.png %}
[8]: {% image_buster /assets/img/Shopify/install_complete.png %}
[9]: {% image_buster /assets/img/Shopify/choose_account.png %}
[10]: {% image_buster /assets/img/Shopify/collect_email_subscribers.png %}
[11]: {% image_buster /assets/img/Shopify/sync_products_step1.png %}
[12]: {% image_buster /assets/img/Shopify/configure_settings.png %}
[13]: {% image_buster /assets/img/Shopify/collect_email_subscribers_2.png %}