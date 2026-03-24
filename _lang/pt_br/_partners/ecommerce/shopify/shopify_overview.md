---
nav_title: Visão geral do Shopify
article_title: "Visão geral do Shopify"
description: "Este artigo de referência descreve a parceria entre a Braze e a Shopify, uma empresa de comércio global, que permite conectar sua loja da Shopify com a Braze para passar webhooks selecionados da Shopify para a Braze. Aproveite as estratégias de mensagens integradas entre canais da Braze e o Canvas para incentivar os clientes a completarem suas compras ou redirecionar os usuários com base nas compras anteriores."
page_type: partner
search_tag: Partner
alias: /shopify_overview/
page_order: 0
---

# Visão geral do Shopify

> [A Shopify](https://www.shopify.com/) é uma empresa líder em comércio global que fornece ferramentas confiáveis para iniciar, crescer, comercializar e gerenciar negócios de qualquer tamanho. A Shopify torna o comércio melhor para todo mundo com uma plataforma e serviços projetados para confiabilidade, enquanto oferece uma melhor experiência de compra para consumidores em todos os lugares.

A integração da Braze com a Shopify fornece uma solução poderosa para empresas de eCommerce que buscam aprimorar seu engajamento com os clientes e impulsionar esforços de marketing personalizados. Essa integração conecta perfeitamente as robustas capacidades de eCommerce da Shopify com nossa avançada plataforma de engajamento com clientes, permitindo que você envie mensagens direcionadas, relevantes e oportunas aos seus usuários com base em comportamentos de compra em tempo real e dados transacionais.

## Requisitos

| Requisito | Descrição |
| --- | --- |
| Loja da Shopify | Você tem uma loja Shopify ativa. |
| Permissões de proprietário ou membro da equipe da loja Shopify | {::nomarkdown}<ul><li>Acesso a todas as configurações Gerais e da Loja Online.</li><li> Permissões adicionais de administrador:</li><ul><li>Pedidos: Visualização</li><li>Cliente: LerEscrever</li><li>Ver Eventos de Clientes (Web Pixels)</li><li>Gerenciar configurações</li><li>Ver Apps Desenvolvidos por Funcionários/Colaboradores</li><li>Gerenciar/Instalar Apps e Canais</li><li>Gerenciar/Adicionar Pixels Personalizados</li></ul></ul>{:/} |
{: .reset-td-br-1 .reset-td-br_2 role="presentation" }

## Como integrar 

A Braze oferece duas opções de integração para comerciantes da Shopify, projetadas para atender às diversas necessidades das empresas de eCommerce: **Integração padrão** e **Integração personalizada**.

{% multi_lang_include shopify.md section='Integration Tabs' %}

## Como a integração funciona

Se você já configurou e ativou o preenchimento histórico nas suas configurações, a sincronização inicial de dados começará imediatamente. A Braze importará todos os clientes e eventos de pedidos realizados nos últimos 90 dias antes da sua conexão de integração com a Shopify. Quando a Braze importar seus clientes da Shopify, atribuiremos o tipo de `external_id` que você escolheu nas suas configurações.

Se você planeja integrar com um ID externo personalizado (para a [integração padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/#step-4-configure-how-you-manage-users) ou a [integração personalizada]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/#step-6-configure-how-you-manage-users-optional)), será necessário adicionar seu ID externo personalizado como um metafield de cliente Shopify a todos os perfis de clientes Shopify existentes e, em seguida, realizar o [preenchimento histórico]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill). 

Após a sincronização inicial de dados, a Braze continuará rastreando novos dados e atualizações, diretamente da Shopify e dos SDKs da Braze.

{% alert note %}
Se você é um cliente existente da Braze com campanhas ou Canvas ativos, revise o [preenchimento histórico da Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#historical-backfill) para informações importantes. Para ver quais dados específicos de clientes estão sendo preenchidos, consulte os [recursos da Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).
{% endalert %}

### Sincronização de usuários e dados

Após a integração estar ativa, a Braze reunirá dados de usuários de duas fontes principais por meio da integração com a Shopify:
- **Shopify Web Pixel API e embeds de app:** Isso alimenta o Braze Web SDK e o Javascript SDK para suportar rastreamento no site, gerenciamento de identidade, dados comportamentais de eCommerce e potencializar canais de envio de mensagens como mensagens no app.
- **Webhooks da Shopify:** dados comportamentais de eCommerce, sincronização de produtos e coleta de assinantes

Durante a integração, você precisará selecionar quando os SDKs da Braze são inicializados e carregam seu site Shopify: 
- Na visita ao site (como início de sessão)
    - **O que faz:** Rastreia usuários anônimos — como compradores convidados — para acessar mais dados para uma personalização mais profunda 
- Na inscrição da conta (como login na conta) 
    - **O que faz:** Evita o rastreamento de usuários anônimos para uma abordagem mais conservadora e orientada à privacidade, de modo que a atividade do usuário seja rastreada *após* o usuário fazer login em sua conta

{% alert note %}
- Visitas ao site (sessões) contam para suas alocações de Usuários Ativos Mensais (MAU).
- As versões do Braze Web SDK e do JavaScript SDK serão automaticamente definidas para v5.4.0.
{% endalert %}

A Braze usa a integração com a Shopify para suportar múltiplos identificadores que rastreiam seus usuários desde a experiência de compra como convidados até se tornarem usuários identificados:

| Identificador da Braze | Descrição |
| --- | --- |
| Braze `device_id` | Um ID gerado aleatoriamente armazenado no navegador que rastreia a atividade de usuários anônimos por meio dos SDKs da Braze. |
| Alias de usuário do token do carrinho | Um alias que a Braze cria para rastrear eventos de atualização do carrinho. Esse token é criado usando o token do carrinho da Shopify. |
| Alias de usuário do token de checkout | Um alias que a Braze cria quando o usuário inicia o processo de checkout. Esse token é criado usando o token de checkout da Shopify.<br><br> Se um cliente usar o Shop Pay como opção de checkout acelerado, a Shopify pode ignorar certos eventos padrão de checkout e impedir que a Braze receba os dados necessários para adicionar o alias do token de checkout. |
| Alias do ID do cliente da Shopify | O ID do cliente da Shopify é atribuído como um alias quando o ID externo é atribuído durante o login da conta ou quando um pedido é feito. |
| Braze `external_id` | Um identificador único que ajuda a rastrear clientes em dispositivos e plataformas. Isso mantém uma experiência de usuário consistente e melhora a análise de dados, evitando múltiplos perfis quando os usuários trocam de dispositivo ou reinstalam o app.<br><br>A integração da Shopify suporta os seguintes tipos de `external_id`: <br><br>{::nomarkdown}<ul><li>ID do cliente da Shopify (padrão)</li><li>ID externo personalizado</li><li>E-mail com hash (SHA-256)</li><li>E-mail com hash (SHA-1)</li><li>E-mail com hash (MD5)</li><li>E-mail</li></ul>{:/}A Braze atribui um `external_id` aos seus usuários chamando o método changeUser dentro dos SDKs quando: <br><br>{::nomarkdown}<ul><li>Um usuário faz login ou cria uma conta</li><li>Um pedido é feito</li></ul>{:/}<br> Para saber mais sobre o que acontece quando você atribui um `external_id` a um perfil anônimo, consulte [Ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle#what-happens-when-you-identify-anonymous-users).<br><br>A Braze também aproveitará o `external_id` para atribuir dados comportamentais de eCommerce downstream a partir dos webhooks da Shopify.|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

A integração requer que os SDKs da Braze e os serviços da Shopify trabalhem juntos para rastrear e atribuir adequadamente os dados da Shopify aos usuários certos em tempo quase real. Para mais detalhes sobre os dados rastreados por meio da integração, veja [Dados da Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

{% alert note %}
- Se você estiver testando a integração, aconselhamos que use o modo anônimo ou limpe seus cookies para redefinir o `device_id` da Braze e simular o comportamento de um usuário anônimo.
- Embora um ID de cliente da Shopify seja gerado quando um e-mail é inserido no rodapé da newsletter da Shopify ou durante o processo de checkout antes de um pedido ser feito, esse ID de cliente não é acessível por meio dos Web Pixels da Shopify. Por causa disso, a Braze não pode usar o método `changeUser` nessas duas situações.
{% endalert %}

### Sincronizando as permissões de marketing por e-mail e SMS da Shopify

Se você ativar a coleta de assinantes nas suas configurações, precisará atribuir um grupo de inscrições para cada loja que conectar à Braze. Isso significa que seus clientes serão categorizados como "inscritos" ou "não inscritos" no grupo de inscrições da sua loja.

O status de aceitação de marketing da Shopify para e-mail e marketing por SMS pode ser atualizado das seguintes maneiras:
- **Atualização manual:** Você pode alterar manualmente o status de aceitação de marketing por e-mail ou SMS de um usuário no seu admin da Shopify.
- **Rodapé da newsletter da Shopify:** Se um usuário inserir seu e-mail no rodapé padrão da newsletter da Shopify, seu status de aceitação será atualizado.
- **Processo de checkout:** Se um usuário atualizar seu status de aceitação durante o checkout.

{% alert note %}
O status de aceitação de marketing por e-mail da Shopify não mudará o [estado global de inscrição por e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions/) de um usuário na Braze. O estado de inscrição padrão quando um perfil de usuário é criado é "inscrito". Lembre-se de usar o grupo de inscrições como parte dos critérios de entrada da sua campanha ou Canvas.
{% endalert %}

Esta tabela mostra quais estados de aceitação de marketing da Shopify correspondem aos status dentro do seu grupo de inscrições da Braze. 

| Estado de aceitação de marketing da Shopify | Estado do grupo de inscrições da Braze |
| --- | --- |
| E-mail inscrito | Inscrito |
| E-mail não inscrito | Não inscrito |
| E-mail pendente de confirmação | Não inscrito |
| E-mail inválido | Não inscrito |
| SMS inscrito | Inscrito |
| SMS não inscrito | Não inscrito |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

### Formulários de inscrição

#### Rodapé da newsletter da Shopify

Os usuários que inserem seu endereço de e-mail no rodapé da newsletter da Shopify passarão por um destes fluxos de trabalho:

##### Usuários que não fizeram login em sua conta

1. A Braze recebe um webhook de entrada da Shopify sempre que um cliente é criado ou atualizado.
2. A Braze cria um perfil de usuário contendo o endereço de e-mail e o alias do ID do cliente da Shopify associados a esse usuário.
3. O SDK da Braze atualiza o perfil anônimo com o endereço de e-mail.

{% alert note %}
Isso pode resultar em um perfil duplicado até que o usuário se identifique criando sua conta, fazendo login em sua conta ou fazendo um pedido. A Braze oferece ferramentas de mesclagem em massa para ajudar a automatizar a reconciliação de perfis duplicados. Consulte [Usuários duplicados]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/) para mais detalhes.
{% endalert %}

##### Usuários que já fizeram login em sua conta

A Braze criará um perfil de usuário contendo o endereço de e-mail e o alias do ID do cliente da Shopify associados a esse usuário. A Braze não atualizará o endereço de e-mail do usuário logado, porque assumimos que a Shopify já forneceu essas informações.

#### Formulários de inscrição da Braze

A Braze fornece dois tipos de modelos de formulários de inscrição:
- **[Formulários de inscrição por e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/email_capture/):** Crie usando o editor de arrastar e soltar.
- **[Formulário de captura de e-mail do editor tradicional]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/email_capture_form/):** Um formulário mais simples para capturar endereços de e-mail.

Quando você usa esses modelos de formulários de inscrição, a Braze atualiza automaticamente o status global de inscrição por e-mail no perfil do usuário. Para mais detalhes sobre como o estado global de inscrição por e-mail é tratado, incluindo informações sobre validação de e-mail, consulte a documentação de cada tipo de modelo de formulário.

{% alert note %}
- Certifique-se de incluir critérios de entrada na sua campanha ou Canvas que incluam tanto o status global de inscrição por e-mail quanto o grupo de inscrições conectados à sua loja Shopify. Isso ajudará a garantir que você esteja direcionando o público certo. 
- A Braze coleta informações dos visitantes, como endereços de e-mail e números de telefone, por meio de mensagens no navegador. Essas informações são então enviadas para a API de Visitantes da Shopify, mas não criam um perfil de cliente na Shopify. Para mais detalhes, consulte [API de Visitantes](https://shopify.dev/docs/api/web-pixels-api/emitting-data#visitor-api).
{% endalert %}

#### Formulários de inscrição de terceiros 

Se você estiver usando uma plataforma de terceiros ou um plugin da Shopify para seus formulários de inscrição, precisará trabalhar com seus desenvolvedores para integrar o código do SDK da Braze para capturar o endereço de e-mail e o status global de inscrição por e-mail das submissões de formulário. Para saber mais, revise a [configuração de integração padrão da Shopify]({{site.baseurl}}/shopify_standard_integration/) e a [configuração de integração personalizada da Shopify]({{site.baseurl}}/shopify_custom_integration/).

### Sincronização de produtos 

A Braze suporta a capacidade de sincronizar os produtos da sua loja Shopify em um catálogo da Braze. Para mais detalhes, consulte [sincronizações de produtos da Shopify]({{site.baseurl}}/shopify_catalogs/).

## Solicitações de titulares de dados

Como parte da integração da plataforma da Braze com a Shopify, a Braze recebe automaticamente os [webhooks de conformidade da Shopify](https://shopify.dev/docs/apps/build/privacy-law-compliance/). No entanto, como os clientes são os controladores de dados dos dados de seus Usuários Finais, os clientes devem realizar quaisquer ações necessárias para atender às Solicitações de Titulares de Dados recebidas em relação aos dados de Usuários Finais na Braze (incluindo dados de Usuários Finais recebidos por meio da integração com a Shopify). Consulte nossa documentação de [Assistência Técnica em Proteção de Dados]({{site.baseurl}}/dp-technical-assistance) para mais detalhes.