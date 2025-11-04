---
nav_title: Visão geral do Shopify
article_title: "Visão geral do Shopify"
description: "Este artigo de referência descreve a parceria com a Braze e a Shopify, uma empresa de comércio global, que permite conectar sua loja da Shopify com a Braze para passar webhooks selecionados da Shopify para a Braze. Aproveite as estratégias de mensagens integradas entre canais da Braze e o canva para incentivar os clientes a completarem suas compras ou redirecionar os usuários com base nas compras anteriores."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Visão geral do Shopify

> [A Shopify](https://www.shopify.com/) é uma empresa líder em comércio global que fornece ferramentas confiáveis para iniciar, crescer, comercializar e gerenciar negócios de qualquer tamanho. A Shopify torna o comércio melhor para todo mundo com uma plataforma e serviços projetados para confiabilidade, enquanto oferece uma melhor experiência de compra para consumidores em todos os lugares.

A integração do Braze com o Shopify oferece uma solução poderosa para empresas de comércio eletrônico que buscam aprimorar o engajamento de seus clientes e impulsionar os esforços de marketing personalizado. Essa integração conecta perfeitamente os robustos recursos de comércio eletrônico do Shopify com nossa avançada plataforma de engajamento com clientes, ativando a entrega de mensagens direcionadas, relevantes e oportunas aos seus usuários com base em comportamentos de compras e dados transacionais em tempo real.

## Solicitações

| Requisito | Descrição |
| --- | --- |
| Loja da Shopify | Você tem uma loja ativa da Shopify. |
| Permissões de proprietário da loja Shopify ou membro da equipe | {::nomarkdown}<ul><li>Acesso a todas as configurações gerais e da loja on-line.</li><li> Permissões adicionais de administrador:</li><ul><li>Pedidos: Visualização</li><li>Cliente: Leitura e gravação</li><li>Exibir eventos de clientes (pixels da Web)</li><li>Gerenciar configurações</li><li>Exibir apps desenvolvidos pela equipe/colaboradores</li><li>Gerenciar/Instalar aplicativos e canais</li><li>Gerenciar/adicionar pixels personalizados</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Como integrar 

O Braze oferece duas opções de integração para os comerciantes do Shopify que são projetadas para atender às diversas necessidades das empresas de comércio eletrônico: **Integração padrão** e **integração personalizada**.

{% multi_lang_include shopify.md section='Integration Tabs' %}

## Como a integração funciona

Se você já tiver configurado e ativado o backfill histórico em suas definições de configuração, a sincronização inicial dos dados começará imediatamente. O Braze importará todos os clientes e eventos de pedidos feitos nos últimos 90 dias antes de sua conexão de integração com o Shopify. Quando o Braze importar seus clientes do Shopify, atribuiremos o tipo de `external_id` que você escolheu em suas definições de configuração.

Se você planeja integrar com um ID externo personalizado (para a [integração padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users) ou a [integração personalizada]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)), será necessário adicionar seu ID externo personalizado como um metacampo de cliente da Shopify a todos os perfis de clientes existentes da Shopify e, em seguida, realizar o [preenchimento retroativo histórico]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill). 

Após a sincronização inicial dos dados, o Braze rastreará continuamente novos dados e atualizações, diretamente dos SDKs do Shopify e do Braze.

{% alert note %}
Se você for um cliente Braze existente com campanhas ou telas ativas, revise [o backfill histórico do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) para obter informações importantes. Para ver quais dados específicos do cliente estão sendo preenchidos, consulte [os recursos do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).
{% endalert %}

### Sincronização de dados de usuários e dados

Depois que a integração estiver ativa, o Braze coletará dados de usuários de duas fontes principais por meio da integração com o Shopify:
- **API do Shopify Web Pixel e incorporações de app:** Isso capacita o Braze Web SDK e o Javascript SDK a oferecer suporte ao rastreamento no local, ao gerenciamento de identidade, aos dados comportamentais do comércio eletrônico e aos canais de envio de mensagens, como mensagens no app.
- **Webhooks do Shopify:** dados comportamentais de comércio eletrônico, sincronização de produtos e coleta de assinantes

Durante a integração, você precisará selecionar quando os SDKs do Braze inicializarão e carregarão seu site do Shopify: 
- Durante a visita ao local (como o início da sessão)
    - **O que ele faz:** Rastreamento de usuários anônimos, como compradores convidados, para acessar mais dados para uma personalização mais profunda 
- No momento do registro da conta (como login da conta) 
    - **O que ele faz:** Impede o rastreamento de usuários anônimos para uma abordagem mais conservadora e orientada para a privacidade, de modo que a atividade do usuário é rastreada *depois que* ele faz login em sua conta

{% alert note %}
- As visitas ao site (sessões) contam para a sua cota de Usuários Ativos Mensais (MAU).
- As versões do Braze Web SDK e do JavaScript SDK serão automaticamente definidas para a versão 5.4.0.
{% endalert %}

O Braze usa a integração com o Shopify para dar suporte a vários identificadores que rastreiam seus usuários desde a experiência de compra do convidado até que eles se tornem usuários identificados:

| Identificador de Braze | Descrição |
| --- | --- |
| Braze `device_id` | Uma ID gerada aleatoriamente e armazenada no navegador que rastreia a atividade anônima do usuário por meio dos SDKs do Braze. |
| Alias de usuário de token de carrinho | Um alias que o Braze cria para rastrear eventos de atualização de carrinho. Esse token é criado usando o token do carrinho do Shopify. |
| Alias de usuário do token de checkout | Um alias que o Braze cria quando o usuário inicia o processo de checkout. Esse token é criado usando o token de checkout do Shopify. |
| Alias do ID do cliente da Shopify | O ID do cliente da Shopify é atribuído como um alias quando o ID externo é atribuído durante o login da conta ou quando um pedido é feito. |
| Braze `external_id` | Um identificador exclusivo que ajuda a rastrear clientes em dispositivos e plataformas. Isso mantém uma experiência consistente para o usuário e melhora a análise de dados, evitando vários perfis quando os usuários trocam de dispositivo ou reinstalam o app.<br><br>A integração do Shopify é compatível com os seguintes tipos de `external_id`: <br><br>{::nomarkdown}<ul><li>ID do cliente da Shopify (padrão)</li><li>ID externo personalizado</li><li>E-mail com hash (SHA-256)</li><li>E-mail com hash (SHA-1)</li><li>E-mail com hash (MD5)</li><li>E-mail</li></ul>{:/}O Braze atribui um `external_id` aos seus usuários chamando o método changeUser dentro dos SDKs quando: <br><br>{::nomarkdown}<ul><li>Um usuário registra ou cria uma conta</li><li>Um pedido é feito</li></ul>{:/}<br> Para saber mais sobre o que acontece quando você atribui um `external_id` a um perfil anônimo, consulte [Ciclo de vida do perfil do usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>A Braze também aproveitará o `external_id` para atribuir dados comportamentais de comércio eletrônico downstream a partir de webhooks do Shopify.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A integração exige que os SDKs do Braze e os serviços do Shopify trabalhem juntos para rastrear e atribuir adequadamente os dados do Shopify aos usuários certos em tempo quase real. Para obter mais detalhes sobre os dados rastreados por meio da integração, consulte [Dados do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

{% alert note %}
- Se estiver testando a integração, recomendamos que use o modo de navegação anônima ou limpe seus cookies para redefinir o Braze `device_id` e imitar o comportamento de um usuário anônimo.
- Embora um ID de cliente da Shopify seja gerado quando um e-mail é inserido no rodapé do boletim informativo da Shopify ou durante o processo de checkout antes de um pedido ser feito, esse ID de cliente não pode ser acessado pelo Shopify Web Pixels. Por esse motivo, o Braze não pode usar o método `changeUser` nessas duas situações.
{% endalert %}

### Sincronização de envios de e-mail e aceitação de marketing por SMS do Shopify

Se ativar a coleta de assinantes em suas definições de configuração, será necessário atribuir um grupo de inscrições para cada loja conectada ao Braze. Isso significa que seus clientes serão categorizados como "inscritos" ou "cancelados" no grupo de inscrições de sua loja.

O status de aceitação do Shopify marketing para e-mail e SMS marketing pode ser atualizado das seguintes maneiras:
- **Atualização manual:** É possível alterar manualmente o status de aceitação de e-mail ou SMS marketing de um usuário no admin da Shopify.
- **Rodapé do boletim informativo da Shopify:** Se um usuário inserir seu e-mail no rodapé do boletim informativo padrão da Shopify, seu status de aceitação será atualizado.
- **Processo de checkout:** Se um usuário atualizar seu status de aceitação durante o checkout.

{% alert note %}
O status de aceitação de e-mail marketing do Shopify não alterará o [estado de inscrição global]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) de [e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) de um usuário no Braze. O estado padrão da inscrição quando um perfil de usuário é criado é "inscrito". Lembre-se de usar o grupo de inscrições como parte de sua campanha ou dos critérios de entrada do Canva.
{% endalert %}

Essa tabela mostra quais estados de aceitação do Shopify marketing estão correlacionados com os status em seu grupo de inscrições do Braze. 

| Estado de aceitação do Shopify marketing | Estado do grupo de inscrições do Braze |
| --- | --- |
| O e-mail está inscrito | Inscreveu-se |
| O e-mail foi cancelado | Cancelou inscrição |
| O e-mail está aguardando confirmação | Cancelou inscrição |
| O e-mail é inválido | Cancelou inscrição |
| Assinatura de SMS | Inscreveu-se |
| SMS cancelado inscrição | Cancelou inscrição |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Formulários de inscrição-se

#### Rodapé da newsletter da Shopify

Os usuários que inserirem seu endereço de e-mail no rodapé do boletim informativo da Shopify passarão por um desses fluxos de trabalho:

##### Usuários que não registraram sua conta

1. O Braze recebe um webhook do Shopify sempre que um cliente é criado ou atualizado.
2. O Braze cria um perfil de usuário que contém o endereço de e-mail e o alias do ID do cliente Shopify que estão associados a esse usuário.
3. O SDK do Braze atualiza o perfil anônimo com o endereço de e-mail.

{% alert note %}
Isso pode resultar em um perfil duplicado até que o usuário se identifique criando sua conta, registrando sua conta ou fazendo um pedido. O Braze oferece ferramentas de mesclagem em massa para ajudá-lo a automatizar a reconciliação de perfis duplicados. Consulte [Usuários duplicados]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/) para obter mais detalhes.
{% endalert %}

##### Usuários que já fizeram o registro em suas contas

O Braze criará um perfil de usuário contendo o endereço de e-mail e o alias do ID do cliente Shopify que estão associados a esse usuário. O Braze não atualizará o endereço de e-mail do usuário registrado, porque presumimos que o Shopify já tenha fornecido essas informações.

#### Formulários de inscrição no Braze

O Braze fornece dois tipos de modelos de formulários de inscrição:
- **[Formulários de envio de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/email_capture/):** Crie-os usando o editor de arrastar e soltar.
- **[Formulário de captura de e-mail do editor tradicional]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/):** Um formulário mais simples para capturar endereços de e-mail.

Quando você usa esses modelos de formulário de inscrição, o Braze atualiza automaticamente o status global de inscrição de e-mail no perfil do usuário. Para saber mais detalhes sobre como o estado da inscrição global de e-mail é tratado, incluindo informações sobre validação de e-mail, consulte a documentação de cada tipo de modelo de formulário.

{% alert note %}
- Certifique-se de incluir critérios de entrada em sua campanha ou Canva que incluam o status da inscrição global por e-mail e o grupo de inscrições que estão conectados à sua loja Shopify. Isso ajudará a garantir que esteja direcionando o público certo. 
- O Braze coleta informações dos visitantes, como endereços de e-mail e números de telefone, por meio de mensagens no navegador. Essas informações são então enviadas para a Shopify. Esses dados ajudam os comerciantes a reconhecer os visitantes de suas lojas e a criar uma experiência de compra mais personalizada. Para obter mais detalhes, consulte [API do visitante](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Formulários de inscrição-se de terceiros 

Se estiver usando uma plataforma de terceiros ou um plug-in do Shopify para seus formulários de inscrição, precisará trabalhar com seus desenvolvedores para integrar o código do Braze SDK para capturar o endereço de e-mail e o status global de inscrição de e-mail dos envios de formulários. Para saber mais, consulte a [configuração de integração padrão da Shopify]({{site.baseurl}}/shopify_standard_integration/) e [a configuração de integração personalizada da Shopify]({{site.baseurl}}/shopify_custom_integration/).

### Sincronização de produtos 

O Braze oferece suporte à capacidade de sincronizar os produtos de sua loja do Shopify em um catálogo do Braze. Para obter mais detalhes, consulte [Sincronização de produtos da Shopify]({{site.baseurl}}/shopify_catalogs/).

## Solicitações do titular dos dados

Como parte da integração da plataforma Braze com o Shopify, o Braze recebe automaticamente [os webhooks de conformidade do Shopify](https://shopify.dev/docs/apps/build/privacy-law-compliance/). No entanto, como os clientes são os controladores de dados dos dados de seus Usuários Finais, os clientes devem realizar todas as ações necessárias para atender às Solicitações do Titular dos Dados recebidas com relação aos dados do Usuário Final no Braze (incluindo os dados do Usuário Final recebidos por meio da integração com o Shopify). Consulte nossa documentação de [Assistência Técnica de Proteção de Dados]({{site.baseurl}}/dp-technical-assistance) para obter mais detalhes.