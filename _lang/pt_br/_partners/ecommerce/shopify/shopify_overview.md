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

A integração do Braze com o Shopify fornece uma solução poderosa para empresas de eCommerce que buscam aprimorar seu engajamento com os clientes e impulsionar esforços de marketing personalizados. Essa integração conecta perfeitamente as robustas capacidades de eCommerce do Shopify com nossa avançada plataforma de engajamento com clientes, permitindo que você envie mensagens direcionadas, relevantes e oportunas aos seus usuários com base em comportamentos de compra em tempo real e dados transacionais.

## Solicitações

| Requisito | Descrição |
| --- | --- |
| Loja da Shopify | Você tem uma loja Shopify ativa. |
| Permissões de proprietário ou membro da equipe da loja Shopify | {::nomarkdown}<ul><li>Acesso a todas as configurações Gerais e da Loja Online.</li><li> Permissões adicionais de Admin:</li><ul><li>Pedidos: Visualização</li><li>Cliente: LerEscrever</li><li>Ver Eventos de Clientes (Web Pixels)</li><li>Gerenciar configurações</li><li>Ver Apps Desenvolvidos por Funcionários/Colaboradores</li><li>Gerenciar/Instalar Apps e Canais</li><li>Gerenciar/Adicionar Pixels Personalizados</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Como integrar 

O Braze oferece duas opções de integração para comerciantes do Shopify que são projetadas para atender às diversas necessidades das empresas de eCommerce: **Integração padrão** e **Integração personalizada**.

{% multi_lang_include shopify.md section='Integration Tabs' %}

## Como a integração funciona

Se você já configurou e ativou o preenchimento histórico em suas configurações de configuração, a sincronização inicial de dados começará imediatamente. O Braze importará todos os clientes e eventos de pedidos realizados nos últimos 90 dias antes da sua conexão de integração com o Shopify. Quando o Braze importar seus clientes do Shopify, atribuiremos o tipo `external_id` que você escolheu em suas configurações de configuração.

Se você planeja integrar com um ID externo personalizado (para a [integração padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users) ou a [integração personalizada]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)), será necessário adicionar seu ID externo personalizado como um metafield de cliente Shopify a todos os perfis de clientes existentes do Shopify e, em seguida, realizar o [preenchimento histórico]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill). 

Após a sincronização inicial de dados, o Braze continuará a rastrear novos dados e atualizações, diretamente do Shopify e dos SDKs do Braze.

{% alert note %}
Se você é um cliente Braze existente com campanhas ou Canvases ativas, revise [Shopify historical backfill]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) para informações importantes. Para ver quais dados específicos de clientes estão sendo preenchidos, consulte [Shopify features]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).
{% endalert %}

### Sincronização de usuários e dados

Após a integração estar ativa, a Braze coletará dados de usuários de duas fontes principais através da integração com Shopify:
- **Shopify Web Pixel API e embeds de app:** Isso alimenta o Braze Web SDK e o Javascript SDK para suportar rastreamento no site, gerenciamento de identidade, dados comportamentais de eCommerce e potencializar canais de mensagens como mensagens no app.
- **Webhooks do Shopify:** dados comportamentais de eCommerce, sincronização de produtos e coleta de assinantes

Durante a integração, você precisará selecionar quando os SDKs da Braze são inicializados e carregam seu site Shopify: 
- Na visita ao site (como início de sessão)
    - **O que faz:** Rastreia usuários anônimos—como compradores convidados—para acessar mais dados para uma personalização mais profunda 
- Na inscrição da conta (como login na conta) 
    - **O que faz:** Previne o rastreamento de usuários anônimos para uma abordagem mais conservadora e orientada à privacidade, de modo que a atividade do usuário seja rastreada *após* o usuário fazer login em sua conta

{% alert note %}
- Visitas ao site (sessões) contam para suas alocações de Usuários Ativos Mensais (MAU).
- As versões do Braze Web SDK e do JavaScript SDK serão automaticamente definidas para v5.4.0.
{% endalert %}

A Braze usa a integração com Shopify para suportar múltiplos identificadores que rastreiam seus usuários desde a experiência de compra como convidados até se tornarem usuários identificados:

| Identificador Braze | Descrição |
| --- | --- |
| Braze `device_id` | Um ID gerado aleatoriamente armazenado no navegador que rastreia a atividade de usuários anônimos através dos SDKs da Braze. |
| Alias de usuário do token do carrinho | Um alias que a Braze cria para rastrear eventos de atualização do carrinho. Este token é criado usando o token do carrinho do Shopify. |
| Alias do token de checkout do usuário | Um alias que a Braze cria quando o usuário inicia o processo de checkout. Este token é criado usando o token de checkout do Shopify. |
| Alias do ID do cliente do Shopify | O ID do cliente do Shopify é atribuído como um alias quando o ID externo é atribuído durante o login da conta ou quando um pedido é feito. |
| Braze `external_id` | Um identificador único que ajuda a rastrear clientes em dispositivos e plataformas. Isso mantém uma experiência de usuário consistente e melhora a análise de dados, evitando múltiplos perfis quando os usuários trocam de dispositivos ou reinstalam o app.<br><br>A integração do Shopify suporta os seguintes tipos `external_id`: <br><br>{::nomarkdown}<ul><li>ID do cliente do Shopify (padrão)</li><li>ID externo personalizado</li><li>E-mail com hash (SHA-256)</li><li>E-mail com hash (SHA-1)</li><li>E-mail com hash (MD5)</li><li>E-mail</li></ul>{:/}A Braze atribui um `external_id` aos seus usuários chamando o método changeUser dentro dos SDKs quando: <br><br>{::nomarkdown}<ul><li>Um usuário faz login ou cria uma conta</li><li>Um pedido é feito</li></ul>{:/}<br> Para saber mais sobre o que acontece quando você atribui um `external_id` a um perfil anônimo, consulte [Ciclo de vida do perfil do usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>A Braze também aproveitará o `external_id` para atribuir dados comportamentais de eCommerce a partir dos webhooks do Shopify.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A integração requer que os SDKs da Braze e os serviços do Shopify trabalhem juntos para rastrear e atribuir adequadamente os dados do Shopify aos usuários certos em quase tempo real. Para encontrar mais detalhes sobre os dados rastreados através da integração, veja [Dados do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

{% alert note %}
- Se você estiver testando a integração, aconselhamos que use o modo incógnito ou limpe seus cookies para redefinir o `device_id` da Braze e imitar o comportamento de um usuário anônimo.
- Embora um ID de cliente do Shopify seja gerado quando um e-mail é inserido no rodapé da newsletter do Shopify ou durante o processo de checkout antes de um pedido ser feito, esse ID de cliente não é acessível através dos Web Pixels do Shopify. Por causa disso, a Braze não pode usar o método `changeUser` nessas duas situações.
{% endalert %}

### Sincronizando as permissões de marketing por e-mail e SMS do Shopify.

Se você ativar a coleta de assinantes nas configurações de sua configuração, precisará atribuir um grupo de inscrições para cada loja que conectar ao Braze. Isso significa que seus clientes serão categorizados como "inscritos" ou "não inscritos" no grupo de inscrições da sua loja.

O status de aceitação de marketing do Shopify para e-mail e marketing por SMS pode ser atualizado das seguintes maneiras:
- **Atualização manual:** Você pode alterar manualmente o status de aceitação de marketing por e-mail ou SMS de um usuário no seu admin do Shopify.
- **Rodapé do boletim informativo do Shopify:** Se um usuário inserir seu e-mail no rodapé padrão do boletim informativo do Shopify, seu status de aceitação será atualizado.
- **Processo de checkout:** Se um usuário atualizar seu status de aceitação durante o checkout.

{% alert note %}
O status de aceitação de marketing por e-mail do Shopify não mudará o [estado global de inscrição por e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) de um usuário no Braze. O estado de inscrição padrão quando um perfil de usuário é criado é "inscrito". Lembre-se de usar o grupo de inscrições como parte dos critérios de entrada da sua campanha ou Canvas.
{% endalert %}

Esta tabela mostra quais estados de aceitação de marketing do Shopify correlacionam-se com os status dentro do seu grupo de inscrições do Braze. 

| Estado de aceitação de marketing do Shopify | Estado do grupo de inscrições do Braze |
| --- | --- |
| E-mail está inscrito | Inscreveu-se |
| E-mail está não inscrito | Cancelou inscrição |
| E-mail está pendente de confirmação | Cancelou inscrição |
| O e-mail é inválido | Cancelou inscrição |
| SMS inscrito | Inscreveu-se |
| SMS não inscrito | Cancelou inscrição |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Formulários de inscrição

#### Rodapé da newsletter do Shopify

Usuários que inserem seu endereço de e-mail no rodapé da newsletter do Shopify experimentarão um desses fluxos de trabalho:

##### Usuários que não fizeram login em sua conta

1. Braze recebe um webhook de entrada do Shopify sempre que um cliente é criado ou atualizado.
2. Braze cria um perfil de usuário contendo o endereço de e-mail e o alias de ID do cliente do Shopify associados a esse usuário.
3. O SDK do Braze atualiza o perfil anônimo com o endereço de e-mail.

{% alert note %}
Isso pode resultar em um perfil duplicado até que o usuário se identifique criando sua conta, fazendo login em sua conta ou fazendo um pedido. Braze oferece ferramentas de mesclagem em massa para ajudar a automatizar a reconciliação de perfis duplicados. Consulte [Usuários duplicados]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/) para mais detalhes.
{% endalert %}

##### Usuários que já fizeram login em sua conta

Braze criará um perfil de usuário contendo o endereço de e-mail e o alias de ID do cliente do Shopify associados a esse usuário. Braze não atualizará o endereço de e-mail do usuário logado, porque assumimos que o Shopify já forneceu essas informações.

#### Formulários de inscrição do Braze

Braze fornece dois tipos de modelos de formulários de inscrição:
- **[Formulários de inscrição por e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/email_capture/):** Crie esses usando o editor de arrastar e soltar.
- **[Formulário de captura de e-mail do editor tradicional]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/):** Um formulário mais simples para capturar endereços de e-mail.

Quando você usa esses modelos de formulários de inscrição, o Braze atualiza automaticamente o status global de inscrição por e-mail no perfil do usuário. Para mais detalhes sobre como o estado global de inscrição por e-mail é tratado, incluindo informações sobre validação de e-mail, consulte a documentação para cada tipo de modelo de formulário.

{% alert note %}
- Certifique-se de incluir critérios de entrada em sua campanha ou Canvas que incluam tanto o status global de inscrição por e-mail quanto o grupo de inscrições que estão conectados à sua loja Shopify. Isso ajudará a garantir que você esteja direcionando o público certo. 
- A Braze coleta informações dos visitantes, como endereços de e-mail e números de telefone, por meio de mensagens no navegador. Essas informações são então enviadas para a API de Visitantes da Shopify, mas não criam um perfil de cliente na Shopify. Para mais detalhes, consulte [API de Visitantes](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Formulários de inscrição de terceiros 

Se você estiver usando uma plataforma de terceiros ou um plugin da Shopify para seus formulários de inscrição, precisará trabalhar com seus desenvolvedores para integrar o código do SDK da Braze para capturar o endereço de e-mail e o status global de inscrição por e-mail das submissões de formulário. Para saber mais, revise [configuração de integração padrão da Shopify]({{site.baseurl}}/shopify_standard_integration/) e [configuração de integração personalizada da Shopify]({{site.baseurl}}/shopify_custom_integration/).

### Sincronização de produtos 

A Braze suporta a capacidade de sincronizar os produtos da sua loja Shopify em um catálogo da Braze. Para mais detalhes, consulte [sincronizações de produtos da Shopify]({{site.baseurl}}/shopify_catalogs/).

## Solicitações de titulares de dados

Como parte da integração da plataforma Braze com a Shopify, a Braze recebe automaticamente [webhooks de conformidade da Shopify](https://shopify.dev/docs/apps/build/privacy-law-compliance/). No entanto, como os clientes são os controladores de dados dos dados de seus Usuários Finais, os clientes devem realizar quaisquer ações necessárias para atender às Solicitações de Titulares de Dados recebidas em relação aos dados de Usuários Finais na Braze (incluindo dados de Usuários Finais recebidos por meio da integração com a Shopify). Consulte nossa documentação de [Assistência Técnica em Proteção de Dados]({{site.baseurl}}/dp-technical-assistance) para mais detalhes.
