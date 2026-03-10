---
nav_title: Início
article_title: Novidades no Braze
description: "As notas de lançamento do Braze são publicadas mensalmente para que você possa se manter atualizado sobre os principais lançamentos de produtos, melhorias contínuas, parcerias do Braze, mudanças drásticas no SDK e descontinuações de recursos."
page_order: 0
search_rank: 1
page_type: reference

---

# Novidades no Braze

{% alert tip %}
Para mais informações sobre qualquer uma das atualizações listadas nesta página, entre em contato com o gerente da sua conta ou [abra um ticket de suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Confira nossos [Registros de Alterações do SDK]({{site.baseurl}}/developer_guide/changelogs) para mais informações sobre nossos lançamentos mensais de SDK, melhorias e mudanças drásticas.
{% endalert %}

{% details March 5, 2026 %}

## lançamento de 5 de março de 2026

### Dados & Relatórios

#### Novo centro de dados

{% multi_lang_include release_type.md release="General availability" %}

O Braze lançou um novo [centro de dados]({{site.baseurl}}/user_guide/data/data_centers/): JP-01. Você pode se inscrever em centros de dados específicos da região ao configurar sua conta Braze.

#### Variáveis de contexto

{% multi_lang_include release_type.md release="General availability" %}

[Variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables) são peças temporárias de dados que você pode criar e usar dentro da jornada de um usuário através de um Canvas específico. Cada vez que um usuário entra no Canvas—mesmo que já tenha entrado antes— as variáveis de contexto serão redefinidas com base nos dados de entrada mais recentes e na configuração do Canvas. Essa abordagem permite que cada entrada no Canvas mantenha seu próprio contexto independente, permitindo que os usuários tenham múltiplos estados ativos dentro da mesma jornada, enquanto retêm o contexto específico para cada estado.

#### Fontes de Ingestão de Dados na Nuvem

{% multi_lang_include release_type.md release="Early access" %}

[Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/file_storage_integrations/#setting-up-cloud-data-ingestion-in-braze) tem uma nova interface que separa fontes de sincronizações, permitindo que você reutilize uma única fonte em qualquer número de sincronizações. Isso reduz a configuração duplicada e simplifica a configuração quando você tem várias sincronizações. Se você tiver sincronizações existentes, elas serão automaticamente migradas para a nova estrutura de fontes e sincronizações sem tempo de inatividade. Para começar, vá para **Ingestão de Dados na Nuvem** > **Fontes** para visualizar, editar ou criar fontes, e então selecione uma fonte no menu suspenso ao criar uma sincronização.

#### Campos adicionais para eventos Currents e Data Share

{% multi_lang_include release_type.md release="General availability" %}

[Os eventos de Compartilhamento de Dados e Correntes]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04) agora incluem os seguintes novos campos para aprofundar os dados disponíveis para análises e sistemas a jusante:

- `agentconsole.AgentExecuted`: Adicionado `error` (string)—uma descrição de qualquer erro que ocorreu.
- `agentconsole.ToolInvocation`: Adicionado `request_id` (string)—um ID único para a solicitação geral do LLM e execução completa.
- `users.messages.rcs.InboundReceive`: Adicionado `canvas_variation_name` (string)—o nome da variação do Canvas que o usuário recebeu.

#### Campos de Campanha e Canvas para Compartilhamento de Dados do Snowflake

{% multi_lang_include release_type.md release="General availability" %}

[O Compartilhamento de Dados do Snowflake]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs/#changes-for-data-sharing-3) agora inclui campos adicionais refletindo informações de Campanha e Canvas em 66 tabelas existentes, incluindo:

- `campaign_name`
- `canvas_name`
- `canvas_step_name`
- `canvas_variation_name`
- `message_variation_name`
- `conversion_behavior`
- `experiment_split_name`

#### Validação pré-importação de CSV e relatórios de erro

{% multi_lang_include release_type.md release="General availability" %}

[As importações de usuários CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import) agora suportam validação pré-importação e relatórios de erro detalhados. Antes de importar, selecione **Validar arquivo antes de importar** na página **Importar Usuários**—a Braze irá escanear seu arquivo e gerar um relatório identificando linhas que falharão completamente (erros) e linhas que terão sucesso com alguns valores ignorados (avisos). Você pode baixar o relatório, corrigir seu CSV e re-enviar, ou prosseguir como está. Após a conclusão da importação, um relatório baixável de quaisquer linhas que falharam também estará disponível, com a razão exata para cada problema.

#### Painel de diagnósticos de mensagens

{% multi_lang_include release_type.md release="Early access" %}

O [Painel de Diagnósticos de Mensagens]({{site.baseurl}}/user_guide/analytics/dashboard/diagnostics_dashboard) fornece uma visão geral dos resultados do envio de mensagens, permitindo que você identifique tendências e diagnostique problemas potenciais na sua configuração de mensagens. Este painel pode ajudá-lo a entender por que mensagens de suas campanhas ou Canvases podem não ter sido enviadas como esperado.

### BrazeAI<sup>TM</sup>

#### Agentes Braze no Console de Agentes

{% multi_lang_include release_type.md release="General availability" %}

[Os Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/) são assistentes impulsionados por IA que você pode criar dentro da Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências de cliente mais personalizadas. Quando você cria um agente, define seu propósito e estabelece diretrizes para como ele deve se comportar. Depois que estiver ativo, o agente pode ser [implantado]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents) na Braze para gerar cópias personalizadas, tomar decisões em tempo real ou atualizar campos de catálogo.

### Orquestração

#### Permissões de usuário granulares

{% multi_lang_include release_type.md release="Early access" %}

A Braze está introduzindo [permissões granulares]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/), uma forma mais flexível de gerenciar o acesso dos usuários. Consulte [Migrando para permissões granulares]({{site.baseurl}}/granular_permissions_migration/) para aprender sobre o processo de migração, incluindo como as permissões legadas se mapeiam para permissões granulares.

#### Limitação de taxa baseada em canal

{% multi_lang_include release_type.md release="General availability" %}

Ao definir um limite de taxa de entrega para uma campanha ou Canvas multicanal, você pode optar por definir um limite compartilhado ou um [limite baseado em canal]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#multichannel-campaigns-and-canvases). Quando uma campanha ou Canvas multicanal utiliza limitação de taxa baseada em canal, o limite de taxa se aplica a cada um dos canais selecionados. Por exemplo, você pode configurar sua campanha ou Canvas para enviar um máximo de 5.000 webhooks e 2.500 mensagens SMS por minuto em toda a campanha ou Canvas.

#### Passo do Contexto do Canvas

{% multi_lang_include release_type.md release="General availability" %}

[Os passos do Contexto do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) permitem que você crie e atualize uma ou mais variáveis para um usuário à medida que ele avança por um Canvas. Por exemplo, se você tiver um Canvas que gerencia descontos sazonais, pode usar uma variável de contexto para armazenar um código de desconto diferente cada vez que um usuário entra no Canvas.

### Canais & Pontos de Contato

#### Traduzir localidades em Blocos de Conteúdo

{% multi_lang_include release_type.md release="Early access" %}

Depois de adicionar localidades ao seu espaço de trabalho, você pode [direcionar usuários em diferentes idiomas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/) tudo dentro de um Bloco de Conteúdo.

### Parcerias

#### Algolia - Recomendações de Pesquisa

[Algolia]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/algolia) é uma plataforma de busca e descoberta que ajuda desenvolvedores a criar experiências de busca rápidas, relevantes e escaláveis. Com uma abordagem poderosa de API-first, a Algolia combina algoritmos de classificação avançados com insights impulsionados por IA para uma busca no site, navegação e descoberta de conteúdo personalizados sem interrupções.

#### Anthropic - Provedor de Modelos de IA

[Anthropic]({{site.baseurl}}/partners/ai_model_providers/anthropic) é uma empresa de segurança e pesquisa de IA que desenvolve o Claude, um assistente de IA de última geração criado para ser útil, honesto e seguro para uma ampla gama de tarefas linguísticas.

#### Canva - Personalização de Mensagens - Estúdio Criativo

[Canva]({{site.baseurl}}/partners/canva) sincroniza suas imagens no Canva diretamente com a biblioteca de mídia da Braze, otimizando seu fluxo de trabalho criativo e mantendo seus ativos visuais atualizados em todos os seus canais de mensagem.

#### DOTS.ECO \- Recompensas

[DOTS.ECO]({{site.baseurl}}/partners/additional_channels_and_extensions/extensions/rewards/dots_eco) permite que você recompense os usuários com impacto ambiental no mundo real por meio de certificados digitais rastreáveis. Cada certificado pode incluir metadados como uma URL de certificado compartilhável e uma URL de imagem, para que os usuários possam visualizar (e revisitar) sua prova de impacto.

#### Figma - Personalização de Mensagens - Estúdio Criativo

[Figma]({{site.baseurl}}/partners/figma) é uma plataforma de design colaborativo que permite criar, projetar e prototipar produtos. Use esta integração para enviar imagens e ativos visuais do Figma diretamente para a biblioteca de mídia do Braze.

#### Flybuy - Personalização de Mensagens - Localização

[Flybuy]({{site.baseurl}}/partners/message_personalization/location/flybuy) da Radius Networks é a principal plataforma de localização omnichannel que utiliza tecnologia impulsionada por IA para otimizar a velocidade de serviço em retirada, entrega, drive-thru e refeições no local. Por meio de sua suíte de marketing integrada, o Flybuy também permite que as marcas enviem mensagens hiper-direcionadas e baseadas em momentos, ajudando a aumentar o engajamento, aumentar o tamanho do pedido e apoiar iniciativas de fidelidade mais amplas.

#### Google Gemini - Provedor de Modelos de IA

[Google Gemini]({{site.baseurl}}/partners/ai_model_providers/google_gemini) é a família de modelos de IA do Google que combina raciocínio avançado em texto, código e imagens para ajudar as marcas a oferecer experiências mais inteligentes e personalizadas.

#### Limbik - Personalização de Mensagens - Motores de Personalização

[Limbik]({{site.baseurl}}/partners/message_personalization/dynamic_content/personalization_engines/limbik) é sua camada de ressonância de IA—prevendo como o público real interpreta e responde a mensagens, conceitos e saídas de IA antes que cheguem ao mercado. Impulsionado por pesquisa primária contínua em mais de 60 países e 25 idiomas, o Limbik oferece públicos sintéticos validados por humanos—populações digitais que simulam a resposta do público real em velocidade de máquina e com precisão de nível de pesquisa (95% de confiança, margem de erro de 1,5% a 3%). O Limbik oferece a capacidade de garantir imediatamente que sua mensagem ressoe com o que seu público-alvo acredita e sente.

#### Linkrunner - Orquestração de Mensagens - Atribuição

[Linkrunner]({{site.baseurl}}/partners/message_orchestration/attribution/linkrunner) é uma plataforma de atribuição e análise móvel que ajuda você a rastrear e analisar suas campanhas de aquisição de usuários.

#### Mailizio - Orquestração de Mensagens - Modelos

[Mailizio]({{site.baseurl}}/partners/message_orchestration/templates/Mailizio) é uma plataforma de criação e gerenciamento de e-mails que facilita o design de conteúdo reutilizável e seguro para a marca usando um editor visual intuitivo. Com a integração do Mailizio ao Braze, você pode exportar seus blocos de conteúdo e modelos de e-mail, e então gerar automaticamente mensagens no aplicativo a partir desses mesmos ativos, permitindo uma implantação de campanha rápida e totalmente controlada.

#### Open Loyalty - Dados e Análises - Fidelidade

O [Open Loyalty]({{site.baseurl}}/partners/data_and_analytics/loyalty/openloyalty) é uma plataforma de programa de fidelidade baseada em nuvem que permite construir e gerenciar a fidelidade e programas de recompensas dos clientes. A integração entre Braze e Open Loyalty sincroniza dados de fidelidade—como saldo de pontos, mudanças de nível e avisos de expiração—diretamente no Braze em tempo real. Isso permite que você acione mensagens personalizadas (Email, Push, SMS) quando o status de fidelidade de um usuário muda.

#### OpenAI - Provedor de Modelos de IA

A [OpenAI]({{site.baseurl}}/partners/ai_model_providers/openai) cria modelos avançados de IA, como o GPT, que permitem a compreensão e a geração de linguagem natural, capacitando as marcas a construir e escalar interações significativas com os clientes.

#### Shopgate - Canais

O [Shopgate]({{site.baseurl}}/partners/additional_channels_and_extensions/additional_channels/shopgate) é uma plataforma de comércio móvel e omnichannel que ajuda os comerciantes a criar aplicativos de compras e melhorar a eficiência das lojas físicas por meio de ferramentas de atendimento e clienteling, que significa suporte personalizado ao cliente na loja com base em dados do cliente.

#### Splio - Dados e Análises - Importação de Coorte

O [Splio]({{site.baseurl}}/partners/data_and_analytics/cohort_import/splio) é uma ferramenta de criação de público que permite aumentar o número de campanhas e a receita sem prejudicar a experiência do cliente, e fornece análises para rastrear a performance das campanhas de CRM tanto online quanto offline.

### SDK

#### Atualizações de quebra de SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 41.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 17.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Swift SDK 14.0.2](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Xamarin SDK 9.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Atualizamos a vinculação do Android de [Braze Android SDK 37.0.0 para 41.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v41.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizamos a vinculação do iOS de [Braze Swift SDK 13.3.0 para 14.0.1](https://github.com/braze-inc/braze-swift-sdk/compare/13.3.0...14.0.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Adicionadas novas dependências transitivas do NuGet exigidas pelo SDK da Braze para Android:
        - Xamarin.AndroidX.DataStore.Preferences (1.1.7.1)
        - Xamarin.KotlinX.Serialization.Json.Jvm (1.9.0.2)
        - Xamarin.Kotlin.StdLib foi atualizado de 2.0.21.3 para 2.3.0.1. Se o seu projeto fixar explicitamente este pacote em uma versão mais antiga, você precisará atualizá-lo para evitar erros de restauração.
    - Removida a funcionalidade de Feed de Notícias.
        - Esta funcionalidade foi removida do SDK nativo do Android na versão [38.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v38.0.0).
        - Esta funcionalidade foi removida do SDK nativo do Swift na versão [14.0.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/14.0.0).
    - O caso de enumeração BRZInAppMessageDismissalReason.BRZInAppMessageDismissalReasonWipeData foi renomeado para BRZInAppMessageDismissalReason.WipeData.
- [Plug-in Expo 4.0.0](https://github.com/braze-inc/braze-expo-plugin/releases/tag/4.0.0)
    - Esta versão requer a versão 19.0.0 do SDK React Native do Braze.
    - (Android) Corrigido um vazamento de memória na camada de persistência de dados.
    - (Android) Adicionado suporte para Braze.getInitialPushPayload() para lidar com links profundos de notificações push quando o aplicativo é iniciado a partir de um estado encerrado. Isso resolve um problema em que links profundos de notificações push não eram tratados no Android quando o aplicativo era iniciado a frio.
- [React Native SDK 19.0.0](https://github.com/braze-inc/braze-react-native-sdk/releases/tag/19.0.0)
    - Atualiza as ligações da versão do SDK nativo do Swift do Braze Swift SDK 13.3.0 para 14.0.1.
    - Atualiza as ligações da versão do SDK nativo do Android do Braze Android SDK 40.0.2 para 41.0.0.

{% enddetails %}

{% details February 5, 2026 %}

## lançamento de 5 de fevereiro de 2026

### BrazeAI<sup>TM</sup>

#### Otimizador de conteúdo

{% multi_lang_include release_type.md release="Beta" %}

[Otimizador de Conteúdo]({{site.baseurl}}/user_guide/brazeai/content_optimizer) é um passo contínuo de teste de conteúdo de alta variação que oferece otimização automatizada de engajamento. Usando uma interface arrastável e soltar semelhante ao passo de mensagem, defina os componentes a serem testados, gere variantes usando IA (ou insira-as manualmente) e use tags Liquid para mapear esses componentes ao conteúdo da sua mensagem.

Baseado em um otimizador multi-braço não contextual, o Otimizador de Conteúdo envia uma única mensagem por usuário, determinando qual combinação de variantes de componentes entregar com base em recomendações preditivas. À medida que o passo coleta dados ao longo do tempo, variantes de alto desempenho naturalmente aumentam na alocação de envio, enquanto variantes de baixo desempenho diminuem. O Otimizador de Conteúdo funciona melhor com Canvases de envio repetido que têm um volume diário consistente de usuários (pelo menos alguns milhares de usuários por dia) para permitir a otimização contínua.

### Dados & Relatórios

#### Eventos recomendados para e-commerce

{% multi_lang_include release_type.md release="Early access" %}

Para combinar eventos recomendados para e-commerce com o evento de compra existente, adicionamos o evento de conversão ["Faz Pedido"]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report), que é semelhante a "Faz Compra".

### Canais & Pontos de Contato

#### Traduzir localidades em banners

{% multi_lang_include release_type.md release="Early access" %}

Depois de adicionar localidades ao seu espaço de trabalho, [direcionar usuários em diferentes idiomas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales#translating-locales) tudo dentro de um único banner.

#### Configurar largura para Blocos de Conteúdo arraste-e-solte

[Ajuste a largura de seu Bloco de Conteúdo]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) selecionando o botão no menu de navegação. A largura padrão é 100% quando não especificada nas configurações de estilo global do seu e-mail; caso contrário, as configurações globais serão respeitadas.

![Uma seta de dois lados com uma opção para editar a largura.]({% image_buster /assets/img_archive/content_block_width_updated.png %}){: style="max-width:30%;" }

#### Usar aquecimento de IP automatizado

{% multi_lang_include release_type.md release="Early access" %}

Use [o aquecimento de IP automatizado]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/#automated-ip-warming) para aumentar gradualmente seu volume de envio diário, permitindo que os provedores de caixa de entrada aprendam e confiem em seus padrões de envio. A Braze envia primeiro para seus assinantes mais engajados, o que permite que o volume diário cresça em um ritmo que corresponde às melhores práticas.

### Parcerias

#### LinkedIn – Sincronização de público do Canvas

Usando o [Braze Audience Sync no LinkedIn]({{site.baseurl}}/partners/canvas_audience_sync/linkedin_audience_sync/), adicione dados de usuários de sua integração Braze às listas de clientes do LinkedIn para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais. Qualquer critério normalmente usado para disparar uma mensagem (como push, e-mail, SMS e webhook) em um Braze Canvas com base em dados de usuários agora pode disparar um anúncio para esse usuário em suas listas de clientes do LinkedIn.

#### Oracle Crowdtwist - Análise de dados &

[Oracle Crowdtwist]({{site.baseurl}}/partners/crowdtwist) é uma solução de fidelidade do cliente nativa da nuvem líder para capacitar marcas a oferecer experiências personalizadas ao cliente. Sua solução oferece mais de 100 caminhos de engajamento prontos para uso, proporcionando um rápido retorno sobre o investimento para os profissionais de marketing desenvolverem uma visão mais completa do cliente.

#### Fullstory - Conteúdo Dinâmico

A plataforma de dados comportamentais [do Fullstory]({{site.baseurl}}/partners/fullstory/) ajuda líderes de tecnologia a tomar decisões melhores e mais informadas. Ao injetar dados comportamentais digitais em sua pilha de análises, a tecnologia patenteada do Fullstory desbloqueia o poder de dados comportamentais de qualidade em escala – transformando cada visita digital em insights acionáveis. 

#### Open Loyalty - Análise de dados &

O [Open Loyalty]({{site.baseurl}}/partners/openloyalty) é uma plataforma de programa de fidelidade baseada em nuvem que permite construir e gerenciar a fidelidade e programas de recompensas dos clientes. A integração entre Braze e Open Loyalty sincroniza dados de fidelidade—como saldo de pontos, mudanças de nível e avisos de expiração—diretamente no Braze em tempo real. Isso permite que você acione mensagens personalizadas (Email, Push, SMS) quando o status de fidelidade de um usuário muda.

#### DOTS.ECO \- Extensões

[DOTS.ECO]({{site.baseurl}}/partners/docs.eco) permite que você recompense os usuários com impacto ambiental no mundo real por meio de certificados digitais rastreáveis. Cada certificado pode incluir metadados como uma URL de certificado compartilhável e uma URL de imagem, para que os usuários possam visualizar (e revisitar) sua prova de impacto.

#### Mailizio - Orquestração de mensagens

[Mailizio]({{site.baseurl}}/partners/mailizio/) é uma plataforma de criação e gerenciamento de e-mails que facilita o design de conteúdo reutilizável e seguro para a marca usando um editor visual intuitivo. Com a integração do Mailizio ao Braze, exporte seus blocos de conteúdo e modelos de e-mail, e então gere automaticamente mensagens no aplicativo a partir desses mesmos ativos, permitindo uma implantação de campanha rápida e totalmente controlada.

### APIs

#### APIs POST da biblioteca de mídia

{% multi_lang_include release_type.md release="General availability" %}

Ativos da Biblioteca de Mídia agora podem ser adicionados via API, permitindo que clientes, parceiros e agências automatizem ainda mais os fluxos de criação de mensagens. Use a [API]({{site.baseurl}}/api/endpoints/media_library/manage_assets/create) para enviar um arquivo de ativo diretamente ou copiar um arquivo de uma URL existente. Esse recurso desbloqueia capacidades de integração e automação.

### Currents e Datashare

#### Eventos da Console do Agente para destinos de Armazenamento e Datashare

{% multi_lang_include release_type.md release="General availability" %}

Dois novos [eventos](http://braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events) estão agora disponíveis para destinos de Armazenamento (AWS S3, GCS e Azure Blob Storage) e Snowflake Datashare: `agentconsole.AgentExecuted` e `agentconsole.ToolInvocation`. Esses eventos permitem que você analise o uso da Console do Agente e detalhes em seus sistemas downstream, ajudando você a entender e aproveitar ao máximo o uso do seu agente. Agentes permitem que você crie e implante agentes inteligentes que podem realizar tarefas específicas no Braze, incluindo gerar conteúdo em canvases ou catálogos e direcionar usuários por diferentes caminhos com base em decisões inteligentes. Para mais informações, veja o [changelog do Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Novos eventos de 'Retry' para canais individuais

{% multi_lang_include release_type.md release="General availability" %}

Novos [eventos de retry](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) estão agora disponíveis para e-mail, LINE, notificações push, SMS, webhooks e canais do WhatsApp. Esses eventos fornecem visibilidade sobre quando o limite de frequência resulta no adiamento de uma mensagem agendada em vez de ser abortada. Quando uma mensagem é despriorizada ou tem limite de frequência, agora pode ser reprocessada dentro de uma janela de retry configurada, dando a você uma melhor visão sobre os padrões de entrega de mensagens e os impactos do limite de frequência. Para mais informações, veja o [changelog do Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Adicionar novo campo 'time_ms' ao evento TokenStateChange

{% multi_lang_include release_type.md release="General availability" %}

Um novo campo `time_ms` foi adicionado ao evento [`users.behaviors.pushnotification.TokenStateChange`](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events), fornecendo granularidade em nível de milissegundo para rastrear mudanças no estado do token de push. Essa precisão aprimorada ajuda você a entender o status mais recente de um token de push quando várias mudanças ocorrem dentro do mesmo segundo, dando a você confiança em sistemas downstream de que você tem o status de assinatura correto. Para mais informações, veja o [changelog do Currents](https://www.braze.com/docs/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs#changes-in-version-5-release-date-2026-02-04).

#### Enviar usuário anônimo para Destinos Tealium

{% multi_lang_include release_type.md release="General availability" %}

Eventos que não têm um ID de usuário externo definido agora podem ser transmitidos para destinos [Tealium]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/tealium/tealium_for_currents?redirected=1#tealium-for-currents). Quando você seleciona a caixa de seleção "Incluir eventos de usuários anônimos" na sua integração Currents, eventos sem um ID de usuário externo serão enviados para o destino em vez de serem suprimidos. Essa capacidade é crítica para análises a jusante e casos de uso envolvendo usuários não identificados e anônimos.

##### Enviar usuário anônimo para Destinos CustomHTTP

{% multi_lang_include release_type.md release="Beta" %}

Eventos que não têm um ID de usuário externo definido agora podem ser transmitidos para destinos CustomHTTP. Quando você seleciona a caixa de seleção "Incluir eventos de usuários anônimos" na sua integração Currents, eventos sem um ID de usuário externo serão enviados para o destino em vez de serem suprimidos. Essa capacidade é crítica para análises a jusante e casos de uso envolvendo usuários não identificados e anônimos.

#### Evento de Abertura de Email — "machine_open" campo

O [evento de Abertura de Email]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-open-events) agora gera o valor do campo "machine_open" para relatar a métrica [_Abertura de Máquina_]({{site.baseurl}}/user_guide/analytics/reporting/report_metrics#machine-opens). 

### SDK

As seguintes atualizações do SDK foram lançadas. Swift SDK v14.0.1 corrige um problema com o manuseio de links universais. Android SDK v40.2.0 corrige um possível vazamento de memória e resolve um problema com várias sessões sendo abertas quando atividades transparentes estão presentes. Expo SDK v3.2.0 adiciona a opção `forwardUniversalLinks` (padrão: falso) para configurar o manuseio de links universais pelo SDK nativo Swift.

#### Atualizações de quebra de SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 41.0.0](https://github.com/braze-inc/braze-android-sdk/releases/tag/v41.0.0)
    - Renomeado `BrazeConfig.Builder.setIsLocationCollectionEnabled()` para `setIsAutomaticLocationCollectionEnabled()`.
    - Renomeado `BrazeConfig.isLocationCollectionEnabled` para `isAutomaticLocationCollectionEnabled`.
    - Renomeado `BrazeConfigurationProvider.isLocationCollectionEnabled` para `isAutomaticLocationCollectionEnabled`.
- [Android SDK 40.2.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4020)
- [Plug-in Expo 3.2.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
- [Swift SDK 14.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}

{% details January 8, 2026 %}
## Lançamento em 8 de janeiro de 2026

### Dados & Relatórios

#### Atualizações para eventos Currents

{% multi_lang_include release_type.md release="General availability" %}

As seguintes alterações foram feitas no Currents na Versão 4:

* Alterações de campo para o tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adicionado novo campo `string` `push_token`: Token de push do evento
* Alterações de campo para o tipo de evento `users.messages.pushnotification.Bounce`:
    * Adicionado novo campo `string` `push_token`: Token de push do evento
* Alterações de campo para o tipo de evento `users.messages.pushnotification.Send`:
    * Adicionado novo campo `string` `push_token`: Token de push do evento
* Alterações de campo para o tipo de evento `users.messages.rcs.Click`:
    * Adicionado novo campo `string` `canvas_variation_name`: Nome da variante do canva recebida por este usuário
    * O campo `user_phone_number` agora é *opcional*.
* Alterações de campo para o tipo de evento `users.messages.rcs.InboundReceive`:
    * O campo `user_id` agora é *opcional*.
* Alterações de campo para o tipo de evento `users.messages.rcs.Rejection`:
    * Adicionado novo campo `string` `canvas_step_message_variation_id`: API ID da variação da mensagem da etapa do canva que este usuário recebeu

Consulte o [changelog de Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) para as alterações do evento em cada versão.

#### Exportar logs de sincronização por todas as linhas

{% multi_lang_include release_type.md release="Early access" %}

No [painel de Ingestão de Dados na Nuvem **Log de Sincronização**]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), escolha exportar os logs em nível de linha para uma execução de sincronização por:

* **Linhas com erros:** Baixa um arquivo contendo apenas as linhas que tiveram um status de **Erro**.
* **Todas as linhas:** Baixa um arquivo contendo todas as linhas processadas na execução.

### Canais & Pontos de Contato

#### Conector WhatsApp Traga Seu Próprio (BYO)

O [Conector WhatsApp Traga Seu Próprio (BYO)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/) oferece uma parceria entre Braze e Infobip, na qual você dá acesso ao Braze ao seu Gerenciador de Negócios do WhatsApp (WABA) da Infobip. Isso permite que você gerencie e pague pelos custos de mensagens diretamente com a Infobip enquanto usa o Braze para segmentação, personalização e orquestração de campanhas. 

#### Banners no canva

{% multi_lang_include release_type.md release="Early access" %}

Selecione **Banners** como um canal de mensagens em um [Passo de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) para Canvas. Use o editor de arrastar e soltar para criar mensagens inline personalizadas, proporcionando experiências não intrusivas e contextualmente relevantes que se atualizam automaticamente no início de cada sessão do usuário. 

#### BCC dinâmico

{% multi_lang_include release_type.md release="General availability" %}

Com [BCC dinâmico]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc), use Liquid no seu endereço BCC. Observe que este recurso está disponível apenas em **Preferências de Email** e não pode ser definido na própria campanha. Apenas um endereço BCC por destinatário de email é permitido.

#### Limites de taxa baseados em canal

Como alternativa a um limite de taxa que é compartilhado em toda uma campanha ou Canvas multicanal, selecione um limite de taxa específico por canal. Nesse caso, o limite de taxa se aplicará a cada um dos seus canais selecionados. Por exemplo, defina sua campanha ou Canvas para enviar um máximo de 5.000 webhooks e 2.500 mensagens SMS por minuto ao longo da campanha ou Canvas. Para mais detalhes, veja [Limitação de taxa e controle de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting).

### Parcerias

#### LILT - Localização

[LILT]({{site.baseurl}}/partners/lilt/) é a solução completa de IA para tradução empresarial e criação de conteúdo. A LILT permite que organizações globais escalem e otimizem seu conteúdo, produtos, comunicações e operações de suporte, com agentes de IA e fluxos de trabalho totalmente automatizados.

### Atualizações de quebra de SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011)
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Remove o Feed de Notícias.
        - Isso remove completamente todos os elementos da interface do usuário, modelos de dados e ações associadas ao Feed de Notícias.
- [Web SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 9 de dezembro de 2025

### Dados & Relatórios

#### Adicionando o Google Tag Manager a uma página de destino

Para adicionar o Google Tag Manager às suas páginas de destino, adicione um bloco de Código Personalizado à sua página de destino no editor de arrastar e soltar, e então [insira o código do Tag Manager]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) no bloco.

### Orquestração

#### Caso de uso do SMS Liquid

O caso de uso [Responder com mensagens diferentes com base na palavra-chave SMS recebida]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) incorpora o processamento dinâmico de palavras-chave SMS para responder a mensagens recebidas específicas com diferentes cópias de mensagem. Por exemplo, você pode enviar respostas diferentes quando alguém envia um SMS com "START" em vez de "JOIN".

#### Lista de permissões para Conteúdo Conectado

Você pode adicionar URLs específicas à lista de permissões para serem usadas para [Conteúdo Conectado]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call). Para acessar este recurso, entre em contato com seu gerente de sucesso do cliente.

### Canais & Pontos de Contato

#### Codificação de caracteres SMS

Nosso [calculador de segmentos SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator) agora tem codificação de caracteres! Selecione **Exibir Codificação de Caracteres** para identificar quais caracteres estão codificados como GSM-7 ou UCS-2. 

![Calculador de segmentos SMS com uma mensagem SMS de exemplo inserida na caixa de texto e a codificação de caracteres ativada.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Mensagens do WhatsApp com otimização

Como a API MM para WhatsApp não oferece 100% de entregabilidade, é importante entender como redirecionar usuários que podem não ter recebido sua mensagem em outros canais. 

Para redirecionar usuários, recomendamos construir um segmento de usuários que não receberam uma mensagem específica. Para fazer isso, filtre pelo código de erro `131049`, que indica que uma mensagem de modelo de marketing não foi enviada devido à aplicação do limite de modelo de marketing por usuário do WhatsApp. Você pode fazer isso [usando Braze Currents ou Extensões de Segmento SQL]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Parcerias

#### OtherLevels - Conteúdo dinâmico

[OtherLevels]({{site.baseurl}}/partners/otherlevels/) é uma plataforma de experiência que usa IA generativa para transformar a forma como marcas esportivas, publicadores e operadores se conectam com seus clientes, transformando conteúdo tradicional em vídeo personalizado e experiências de mídia rica em escala.

### SDK

#### Atualizações de quebra de SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## 11 de novembro de 2025

### Flexibilidade de dados

#### `Live Activities Push to Start Registered for App` filtro de segmentação

O filtro `Live Activities Push to Start Registered for App` segmenta seus usuários com base em se eles estão registrados para iniciar uma Atividade Ao Vivo por meio de notificações push do iOS para um aplicativo específico.

#### Extensão de Segmento RFM SQL

Você pode criar uma [Extensão de Segmento RFM (recência, frequência, monetário)]({{site.baseurl}}/rfm_segments/) para segmentar seus melhores usuários medindo seus hábitos de compra.

A análise RFM é uma técnica de marketing que identifica seus melhores usuários pontuando-os em uma escala de 0 a 3 para cada categoria (recência, frequência, monetário), onde 3 é a melhor pontuação e 0 é a pior. Os valores de recência, frequência e monetário são todos baseados em dados de um intervalo de tempo específico de sua escolha.

#### Atributos personalizados — Valores 

Ao visualizar um relatório de uso, selecione a aba [**Valores**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) para ver os principais valores dos atributos personalizados selecionados com base em uma amostra de aproximadamente 250.000 usuários.

#### Logs de sincronização e observabilidade para Ingestão de Dados na Nuvem

{% multi_lang_include release_type.md release="General availability" %}

O painel [Logs de Sincronização do CDI]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) permite monitorar todos os dados processados pelo CDI, verificar se os dados foram sincronizados com sucesso e diagnosticar quaisquer problemas com dados "incorretos" ou ausentes.

#### Implantações de bandeira de recurso com múltiplas regras

Use [implantações de bandeira de recurso com múltiplas regras]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) para definir uma sequência de regras para avaliar usuários, o que permite segmentação precisa e lançamentos controlados de recursos. Esse método é ideal para implantar o mesmo recurso para públicos diversos.

#### Mapeamento para campos de catálogo para blocos de produtos arrastar e soltar

Nas configurações do seu catálogo, você pode selecionar o botão **Blocos de produtos** para [mapear para campos específicos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) e informações no seu catálogo. Isso permite que você selecione quais campos usar como título do produto, URL do produto e URL da imagem.

#### Eventos de interrupção por limite de frequência no Currents

Ao usar o Currents, você pode agora referenciar `abort_type` nos eventos de interrupção do canal. Isso identifica que uma mensagem foi interrompida devido ao limite de frequência e inclui qual regra de limite de frequência causou a interrupção. Isso ajuda a informar como você configura suas regras de limite de frequência. Consulte [Eventos de engajamento de mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) para detalhes específicos dos eventos do Currents.

### Canais robustos

#### Imagens de fundo de linha 

{% multi_lang_include release_type.md release="General availability" %}

Você pode [adicionar uma imagem de fundo de linha]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image) a uma mensagem no aplicativo ou página de destino no painel **Propriedades da linha**. Ative **Imagem de fundo** e, em seguida, forneça uma URL de imagem ou selecione uma imagem da [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). Por fim, configure seu texto alternativo, tamanho, posição e se a imagem se repete para criar padrões ao longo da linha.

![Uma imagem de fundo de linha de uma pizza que tem um padrão de repetição horizontal.]({% image_buster /assets/img_archive/background_row.png %})

#### Copiar link da prévia

Use **Copiar link de visualização** em seus [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), [rodapés personalizados de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer) e [páginas de opt-in e cancelamento de inscrição de e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers) para gerar um link compartilhável que mostra como seu conteúdo ficará para um usuário aleatório.

#### Mensagens do WhatsApp com entrega otimizada

Use os sistemas avançados de IA da Meta para entregar suas mensagens de marketing a mais usuários que têm maior probabilidade de interagir com elas, aumentando significativamente a entregabilidade e o engajamento das mensagens.

[Mensagens do WhatsApp com entrega otimizada]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) são enviadas usando a nova [API Marketing Messages Lite](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) da Meta, que oferece desempenho superior em comparação com a tradicional API Cloud. Esse novo pipeline de envio ajuda você a alcançar melhor os usuários que valorizam e desejam receber suas mensagens.

#### Fluxos do WhatsApp

Ao incorporar uma mensagem de Flow do WhatsApp em um Canvas ou campanha do Braze, você pode querer capturar e utilizar informações específicas que os usuários enviam através do Flow. O Braze precisa receber informações adicionais sobre a estrutura da resposta do usuário, especificamente a forma esperada da resposta JSON, para gerar o esquema de atributo personalizado aninhado (NCA) necessário.

Agora você pode fornecer ao Braze as informações sobre a estrutura da resposta [salvando a resposta do Flow como um atributo personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) e completando um envio de teste.

#### Pré-visualização editável do usuário

Você pode [editar campos individuais de um usuário aleatório ou existente]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user) para ajudar a testar conteúdo dinâmico dentro da sua mensagem. Selecione **Editar** para converter o usuário selecionado em um usuário personalizado que você pode modificar.

![A aba "Visualizar como um Usuário" com um botão "Editar".]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Automação de IA e ML

#### BrazeAI Decisioning Studio™ Go

Agora você pode configurar sua integração com [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go) consultando estes artigos de configuração para:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Salesforce Marketing Cloud]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Novos recursos para Agentes Braze

{% multi_lang_include release_type.md release="Beta" %}

Agora você pode personalizar seu [Agente Braze]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents) ao:

- Aplicar [diretrizes de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) para que seu agente siga em suas respostas. 
- Consultar um catálogo para personalizar ainda mais sua mensagem.
- Estruturar a saída de um agente fornecendo o [formato de saída]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format).
- Ajustar a [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) para o nível de desvio da saída do seu agente.

### Modelos ChatGPT com BrazeAI Operator<sup>TM</sup>

{% multi_lang_include release_type.md release="Beta" %}

Você pode selecionar entre esses modelos GPT para usar em diferentes tipos de solicitações com [Operator]({{site.baseurl}}/user_guide/brazeai/operator):

- GPT-5 nano
- GPT-5 mini (padrão)
- GPT-5

### Novas parcerias Braze

#### StackAdapt - Publicidade

[StackAdapt]({{site.baseurl}}/partners/stackadapt/) é uma plataforma de marketing impulsionada por IA que oferece publicidade direcionada e orientada por desempenho. Ela permite que você sincronize os dados do perfil do usuário do Braze no StackAdapt Data Hub. Ao conectar as duas plataformas, você pode criar uma visão unificada de seus clientes e ativar dados de primeira parte para melhorar o desempenho dos anúncios.

#### Cloudinary - Conteúdo dinâmico

[Cloudinary]({{site.baseurl}}/partners/cloudinary/) é uma plataforma de imagem e vídeo que permite gerenciar, editar, otimizar e entregar imagens e vídeos em grande escala para qualquer campanha em todos os canais e jornadas do cliente. Quando integrado e habilitado, o gerenciamento de mídia do Cloudinary fornecerá e impulsionará a entrega dinâmica, contextual e personalizada de ativos para suas campanhas e Canvases do Braze.

#### Kameleoon - Testes A/B

[Kameleoon]({{site.baseurl}}/partners/kameleoon/) é uma solução de otimização com experimentos, personalização impulsionada por IA e recursos de gerenciamento em uma única plataforma unificada.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Corrige o tipo Typescript para o callback de `subscribeToInAppMessage` e `addListener` para `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Esses ouvintes agora retornam corretamente um callback com o novo tipo `InAppMessageEvent`. Anteriormente, os métodos foram anotados para retornar um tipo `BrazeInAppMessage`, mas na verdade estavam retornando um `String`.
         - Se você estiver usando qualquer uma das APIs de assinatura, certifique-se de que o comportamento de suas mensagens no aplicativo não seja alterado após a atualização para esta versão. Veja nosso código de exemplo em `BrazeProject.tsx`.
    - As APIs `logInAppMessageClicked`, `logInAppMessageImpression` e `logInAppMessageButtonClicked` agora aceitam apenas um objeto `BrazeInAppMessage` para corresponder à sua interface pública existente.
        - Anteriormente, aceitava tanto um objeto `BrazeInAppMessage` quanto um `String`.
    - `BrazeInAppMessage.toString()` agora retorna uma string legível por humanos em vez da representação de string JSON.
        - Para obter a representação de string JSON de uma mensagem no aplicativo, use `BrazeInAppMessage.inAppMessageJsonString`.
    - No iOS, `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` foi movido para `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - Este novo método agora é um método de classe em vez de um método de instância.
    - Adiciona anotações de nulabilidade aos métodos `BrazeReactUtils`.
    - Remove os seguintes métodos e propriedades obsoletos da API:
        - `getInstallTrackingId(callback:)` em favor de `getDeviceId`.
        - `registerAndroidPushToken(token:)` em favor de `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` em favor de `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` em favor de `payload_type`.
        - `PushNotificationEvent.deeplink` em favor de `url`.
        - `PushNotificationEvent.content_text` em favor de `body`.
        - `PushNotificationEvent.raw_android_push_data` em favor de `android`.
        - `PushNotificationEvent.kvp_data` em favor de `braze_properties`.
    - Atualiza as ligações da versão nativa do SDK Android [do Braze Android SDK 39.0.0 para 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [.NET MAUI (Xamarin) SDK Versão 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Atualizada a vinculação do iOS [do Braze Swift SDK 12.1.0 para 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Isso inclui suporte ao Xcode 26.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Atualiza a ponte nativa do Android [do Braze Android SDK 39.0.0 para 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## Liberação em 14 de outubro de 2025

### BrazeAI Decisioning Studio™

[O BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) substitui os testes A/B por decisões de IA que personalizam tudo e maximizam qualquer métrica: gere dólares, não cliques. Com o BrazeAI Decisioning Studio™, você pode otimizar qualquer KPI de negócios. Consulte nossa seção dedicada [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) para casos de uso e recursos principais.

### Flexibilidade de dados

#### Novos eventos do Currents

Esses novos eventos foram adicionados ao [glossário do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events):

- `users.messages.rcs.Click`
- `users.messages.rcs.Rejection`
- `users.messages.line.Abort`
- `users.messages.line.Send`
- `users.messages.line.InboundReceive`
- `users.messages.line.Click`
- `users.messages.rcs.Delivery`
- `users.messages.rcs.InboundReceive`
- `users.messages.rcs.Read`
- `users.messages.rcs.Send`
- `users.messages.rcs.Abort`
- `users.messages.inappmessage.Abort`

Esses novos campos foram adicionados aos seguintes eventos do Currents:

- `is_sms_fallback`: 
  - `users.messages.sms.Delivery`
  - `users.messages.sms.DeliveryFailure`
  - `users.messages.sms.Rejection`
- `message_id`, `in_reply_to`, `flow_id`, `flow_response_json`, `product_id`, `catalog_id`: 
  - `users.messages.whatsapp.InboundReceive`
- `message_id`, `flow_id`, `template_name`: 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Listas de supressão

{% multi_lang_include release_type.md release="General availability" %}

Listas de supressão [Supression lists]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) são grupos de usuários que automaticamente não recebem campanhas ou Canvases. As listas de supressão são definidas por filtros de segmento, e os usuários entram e saem das listas de supressão conforme atendem aos critérios do filtro.

#### Personalização sem cópia

{% multi_lang_include release_type.md release="Early access" %}

Sincronize os gatilhos do Canvas usando a Ingestão de Dados em Nuvem para [personalização sem cópia]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). Esse recurso acessa informações específicas do usuário da sua solução de armazenamento de dados e as passa para um Canvas de destino. Os passos do Canvas podem opcionalmente incluir campos de personalização que não são persistidos nos perfis de usuário do Braze.

#### Variáveis de Contexto do Canvas para Caminhos de Audiência e passos de Divisão de Decisão

{% multi_lang_include release_type.md release="Early access" %}

Você pode [criar filtros de variáveis de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters) que usam variáveis de contexto previamente declaradas em [Caminhos de Audiência]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) e [Divisão de Decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) passos.

### Liberando a criatividade

#### Cartões de Oferta para e-mails

Use [Cartões de Oferta]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab) para fornecer informações chave sobre ofertas diretamente no topo dos corpos dos e-mails. Isso permite que os destinatários entendam rapidamente os detalhes da oferta e tomem uma ação.

#### Modelos para Banners

Quando você [compor seu Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create), agora pode começar com um modelo em branco, usar um modelo da Braze ou selecionar um modelo de Banner salvo.

### Canais robustos

#### Listas de supressão

{% multi_lang_include release_type.md release="General availability" %}
 
As [listas de supressão]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists/) especificam grupos de usuários que nunca receberão mensagens. Os administradores podem criar listas de supressão com filtros de segmento para restringir um grupo de usuários da mesma forma que você faria para a segmentação.

#### Rastreamento de cliques no LINE

{% multi_lang_include release_type.md release="General availability" %}

Quando [o rastreamento de cliques no LINE]({{site.baseurl}}/line/click_tracking/) está ativado, a Braze encurta automaticamente seus URLs, adiciona mecanismos de rastreamento e registra cliques em tempo real. Enquanto o LINE oferece dados agregados de cliques, a Braze fornece informações granulares de usuários que são oportunas e acionáveis. Esses dados permitem que você crie segmentações e estratégias de retargeting mais direcionadas, como segmentar usuários com base no comportamento de cliques e acionar mensagens em resposta a cliques específicos.

#### Filtragem de cliques de bots em SMS e RCS

{% multi_lang_include release_type.md release="General availability" %}

A [filtragem de cliques de bots em SMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) aprimora a análise de campanhas e fluxos de trabalho ao excluir cliques suspeitos de bots. Um "clique de bot" refere-se a cliques automatizados em links encurtados em mensagens de SMS e RCS, como aqueles de rastreadores da web, pré-visualizações de links do Android e iOS, ou software de segurança CPaaS. Esse recurso facilita relatórios precisos, segmentação e orquestração para engajar usuários reais.

#### Transferir números de telefone do WhatsApp

Transfira um número de telefone de Conta Comercial do WhatsApp (WABA) e seu grupo de assinatura associado [de um espaço de trabalho para outro]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) dentro da Braze.

#### Mensagens de resposta e pré-visualização de Fluxos do WhatsApp

Em um Canvas, você pode criar um passo de mensagem do WhatsApp que usa uma [mensagem de resposta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) e mensagem de fluxo. Você também pode selecionar **Pré-visualizar Fluxo** para visualizar o Fluxo diretamente na Braze para confirmar que ele se comporta como esperado.

#### Mensagens de produto no WhatsApp

As [mensagens de produto]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/) permitem que você envie mensagens interativas no WhatsApp que exibem produtos diretamente do seu catálogo Meta.

#### Integrando Braze e WhatsApp com um sistema externo

[Aproveite o poder de chatbots de IA e transferências para agentes ao vivo]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) no canal do WhatsApp para otimizar suas operações de suporte ao cliente. Ao automatizar consultas rotineiras e transitar perfeitamente para agentes humanos quando necessário, você pode melhorar significativamente os tempos de resposta e aprimorar a experiência geral do cliente.

### Automação de IA e ML

#### Agentes da Braze

{% multi_lang_include release_type.md release="Beta" %}

[Agentes Braze]({{site.baseurl}}/user_guide/brazeai/agents/) são assistentes impulsionados por IA que você pode criar dentro do Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências de cliente mais personalizadas.

### Novas parcerias Braze

#### Jasper - Modelos

A integração do [Jasper]({{site.baseurl}}/partners/jasper/) com o Braze permite que você otimize a criação de conteúdo e a execução de campanhas. Com o Jasper, suas equipes de marketing podem gerar cópias de alta qualidade e alinhadas à marca em minutos. O Braze então facilita a entrega dessas mensagens para o público certo no momento ideal. Essa integração promove fluxos de trabalho contínuos, reduz o esforço manual e gera resultados de engajamento mais fortes.

#### Swym - Fidelidade e retargeting

[Swym]({{site.baseurl}}/partners/swym/) ajuda marcas de eCommerce a capturar a intenção de compra com Listas de Desejos, Salvar para Depois, Registro de Presentes e alertas de Volta ao Estoque. Usando dados ricos e baseados em permissões, você pode criar campanhas hiper-direcionadas e oferecer experiências de compra personalizadas que impulsionam o engajamento, aumentam as conversões e elevam a fidelidade.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. Atualizações importantes estão listadas abaixo; você pode encontrar todas as outras atualizações verificando os changelogs correspondentes do SDK.

- [SDK do Cordova 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Atualizamos a ponte nativa do Android [do SDK da Braze para Android 37.0.0 para o 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - A versão mínima requerida do GradlePluginKotlinVersion agora é 2.1.0.
    - Atualizamos a ponte nativa do iOS [do SDK Swift da Braze 12.0.0 para o 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Isso inclui suporte para Xcode 26.
    - Remove o suporte para Feed de Notícias. As seguintes APIs foram removidas:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Atualiza as ligações da versão nativa do SDK Android [de Braze Android SDK 37.0.0 para 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Remove o suporte para Feed de Notícias. As seguintes APIs foram removidas:
        - `launchNewsFeed`
        - `requestFeedRefresh`
        - `getNewsFeedCards`
        - `logNewsFeedCardClicked`
        - `logNewsFeedCardImpression`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
        - `Braze.Events.NEWS_FEED_CARDS_UPDATED`
        - `Braze.CardCategory`
- [Web SDK 6.2.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 15.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [Unity SDK 10.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md)
    - Atualizamos a ponte nativa do iOS [do SDK Swift da Braze 12.0.0 para o 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Isso inclui suporte para Xcode 26.

{% enddetails %}
{% details September 16, 2025 %}

## Liberação em 16 de setembro de 2025

### Flexibilidade de dados

#### Plataforma de dados Braze

A Braze Data Platform é um conjunto abrangente e composto de capacidades de dados e integrações de parceiros que permite criar experiências personalizadas e impactantes ao longo do ciclo de vida do cliente. Saiba mais sobre os três trabalhos relacionados a dados que precisam ser feitos: 

- [Unificação de dados]({{site.baseurl}}/user_guide/data/unification)
- [Ativação de dados]({{site.baseurl}}/user_guide/data/activation)
- [Distribuição de dados]({{site.baseurl}}/user_guide/data/distribution)

#### Propriedades de Banner personalizadas

{% multi_lang_include release_type.md release="Early access" %}

Você pode usar propriedades personalizadas da sua campanha de Banner para recuperar dados chave-valor através do SDK e modificar o comportamento ou a aparência do seu aplicativo. Para saber mais, veja [Propriedades de Banner personalizadas]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Autenticação por token

{% multi_lang_include release_type.md release="General availability" %}

Ao usar o conteúdo conectado na Braze, você poderá descobrir que certas APIs exigem um token em vez de um nome de usuário e senha. A Braze pode armazenar credenciais que contêm [valores de cabeçalho de autenticação de token]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication).

#### Códigos promocionais

Você pode salvar códigos de promoção no perfil de um usuário através de uma etapa de Atualização de Usuário. Para mais informações, consulte [Salvando códigos de promoção em perfis de usuários]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile).

### Liberando a criatividade

#### Braze Pilot

[Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot) é um aplicativo disponível publicamente para Android e iOS que permite enviar mensagens do seu painel Braze para o seu telefone. Confira [Introdução ao Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) para um guia sobre como baixar o aplicativo, inicializar a conexão com seu painel Braze e completar a configuração.

### Novas parcerias Braze

#### Blings - Conteúdo visual e interativo

[Blings]({{site.baseurl}}/partners/blings/) é uma plataforma de vídeo personalizada de próxima geração que permite entregar experiências de vídeo interativas e baseadas em dados em tempo real em larga escala.

#### Integração padrão do Shopify com ferramenta de terceiros

Para lojas online do Shopify, recomendamos usar o método de integração padrão da Braze para suportar os SDKs da Braze em seu site.

No entanto, entendemos que você pode preferir usar uma ferramenta de terceiros, como o Google Tag Manager, então preparamos um guia sobre como você pode fazer isso. Para começar, consulte [Shopify: Tagueamento de terceiros]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Atualiza a ponte nativa do Android do SDK da Braze `36.0.0` para `39.0.0`.
    - Atualiza a ponte nativa do iOS do SDK Swift da Braze `12.0.0` para `13.2.0`. Isso inclui suporte para Xcode 26.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Atualiza as ligações do Braze Swift SDK para exigir versões da denominação `13.0.0+` SemVer. Isso permite a compatibilidade com qualquer versão do Braze SDK de `13.0.0` até, mas não incluindo, `14.0.0`.

{% enddetails %}
{% details August 19, 2025 %}

## Liberação em 19 de agosto de 2025

### Padronização da consistência de fuso horário para o Contexto Canvas

{% multi_lang_include release_type.md release="Early access" %}

Se você está participando do [acesso antecipado ao passo do Contexto Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), todos os timestamps com um tipo de data e hora das propriedades de eventos de disparo em Canvases baseados em ações serão sempre normalizados para [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Para saber mais sobre isso, consulte [padronização da consistência de fuso horário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization).

### Flexibilidade de dados

#### Domínios personalizados de autoatendimento

{% multi_lang_include release_type.md release="General access" %}

[Domínios personalizados de autoatendimento]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) permitem que você configure e gerencie seus próprios domínios personalizados para SMS, RCS e WhatsApp—diretamente do seu painel da Braze. Você pode facilmente adicionar, monitorar e gerenciar até 10 domínios personalizados em um só lugar.

#### Estatísticas do funil de segmentos

Selecione [Exibir estatísticas do funil]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) para exibir as estatísticas para esse grupo de filtros e ver como cada filtro adicionado impacta suas estatísticas de segmento. Você verá uma contagem estimada e uma porcentagem para os usuários que são segmentados por todos os filtros até aquele ponto. Uma vez que as estatísticas são exibidas para um grupo de filtros, elas serão atualizadas automaticamente sempre que você alterar os filtros. 

#### Novos campos de resposta para o endpoint `/campaigns/details` para notificações push

A resposta `messages` para notificações push agora inclui dois novos campos:

- `image_url`: Uma URL de imagem para uma notificação de imagem do Android, uma imagem de notificação do iOS ou uma imagem de ícone de push da web.
- `large_image_url`: Uma URL de imagem de notificação da web para ações de push do Android Chrome e do Windows.

#### Definindo campos de PII

Selecionar e [definir certos campos como campos de PII]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) afeta apenas o que os Usuários podem ver no painel da Braze e não impacta como os dados do Usuário Final em tais campos de PII são tratados.

Consulte sua equipe jurídica para alinhar as configurações do seu painel com quaisquer regulamentos e políticas de privacidade aplicáveis à sua empresa, incluindo aqueles relacionados à [retenção de dados]({{site.baseurl}}/api/data_retention/).

#### Compartilhando um link de download do Report Builder

Você pode [compartilhar um link do painel]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) para o relatório selecionando **Compartilhar** e depois **Compartilhar um link** ou **Enviar ou agendar um e-mail**.

### Liberando a criatividade

#### Tags de cabeçalho personalizadas para e-mails arrastar e soltar

Use `<head>` tags para adicionar CSS e metadados na sua mensagem de e-mail. Por exemplo, você pode usar essas tags para adicionar uma folha de estilo ou favicon. Liquid é suportado em `<head>` tags.

### Canais robustos

#### Melhores práticas de opt-out fuzzy

Adicionamos uma [seção de melhores práticas]({{site.baseurl}}) para ajudar você a configurar cuidadosamente sua mensagem de opt-out fuzzy e criar uma experiência clara, conforme e positiva para seus assinantes.

#### Fluxos do WhatsApp

{% multi_lang_include release_type.md release="Early access" %}

[Fluxos do WhatsApp]({{site.baseurl}}/whatsapp_flows/) é uma melhoria ao canal existente do WhatsApp, permitindo que você crie experiências de mensagens interativas e dinâmicas. 

#### Perguntas sobre produtos recebidas pelo WhatsApp

Os usuários podem responder à sua mensagem de produto ou catálogo com [perguntas sobre produtos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions). Essas chegam como mensagens recebidas, que podem ser classificadas com um Caminho de Ação.

Além disso, a Braze extrai o ID do produto e o ID do catálogo dessas perguntas, para que, se você desejar automatizar respostas ou enviar perguntas para outra equipe (como suporte ao cliente), você possa incluir esses detalhes.

### Automação de IA e ML

#### Novos artigos de casos de uso do BrazeAI™

Adicionamos novos artigos de casos de uso para ajudá-lo a aproveitar ao máximo o BrazeAI™. Esses guias destacam maneiras práticas de aplicar IA às suas estratégias de engajamento, incluindo:

- [Churn previsto]({{site.baseurl}}/user_guide/brazeai/predictive_churn/use_case): Identifique clientes em risco de churn e tome medidas precoces.
- [Eventos previstos]({{site.baseurl}}/user_guide/brazeai/predictive_events/use_case): Antecipe ações-chave dos usuários e molde experiências em tempo real.
- [Recomendações]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): Entregue conteúdo e produtos mais relevantes com base no comportamento do cliente.

#### Servidor MCP

{% multi_lang_include release_type.md release="Beta" %}

O [servidor MCP do Braze]({{site.baseurl}}/user_guide/brazeai/mcp_server/), uma conexão segura e somente leitura, permite que ferramentas de IA como Claude e Cursor acessem dados do Braze não PII para responder perguntas, analisar tendências e fornecer insights sem alterar os dados.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Estende a funcionalidade de `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` para ser acionada para erros de autenticação "Opcionais".
        - O método delegado `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` agora será acionado para erros de autenticação "Obrigatórios" e "Opcionais".
        - Se você quiser lidar apenas com erros de autenticação "Obrigatórios" do SDK, adicione uma verificação garantindo que `BrazeSDKAuthError.optional` seja falso dentro da sua implementação deste método delegado.
    - Corrige o uso de `Braze.Configuration.sdkAuthentication` para ter efeito quando habilitado.
        - Anteriormente, o valor dessa configuração não era consumido pelo SDK e o token era sempre anexado às solicitações se estivesse presente.
        - Agora, o SDK só anexará o token de autenticação do SDK às solicitações de rede de saída quando essa configuração estiver habilitada.
    - Os setters para todas as propriedades de `Braze.FeatureFlag` e todas as propriedades de `Braze.Banner` foram tornados `private`. As propriedades dessas classes agora são somente leitura.
    - Remove a propriedade `Braze.Banner.id`, que foi descontinuada na versão `11.4.0`.
        - Em vez disso, use `Braze.Banner.trackingId` para ler o ID de rastreamento da campanha de um banner.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Atualiza as ligações da versão nativa do SDK Android do [Braze Android SDK 36.0.0 para 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualiza as ligações da versão nativa do SDK Swift do [Braze Swift SDK 12.0.0 para 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - O evento `sdkAuthenticationError` agora será acionado para erros de autenticação tanto "Obrigatórios" quanto "Opcionais".
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Adicionada suporte para .NET 9.0 para as ligações iOS e Android.
        - Isso remove o suporte ao .NET 8.0.
        - Isso requer uma [versão mínima do iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Atualizada a vinculação do Android do [Braze Android 32.0.0 para 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizada a vinculação do iOS do [Braze Swift SDK 10.0.0 para 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Esta versão contém APIs para o recurso de Banners, mas atualmente não é totalmente suportada por este SDK. Se você deseja usar Banners em seu aplicativo .NET MAUI, entre em contato com seu gerente de suporte ao cliente antes de integrar em seu aplicativo.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Atualizada a implementação interna do iOS do método `enableSdk` para usar `setEnabled`: em vez de `_requestEnableSDKOnNextAppRun`, que foi descontinuado no SDK Swift.
    - Chamar este método não requer mais que o aplicativo seja reiniciado para ter efeito. O SDK agora será ativado assim que este método for executado.
    - Atualizamos a ponte nativa do Android do [Braze Android SDK `36.0.0` para `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

{% enddetails %}
{% details July 22, 2025 %}

## Lançamento em 22 de julho de 2025

### Exportação de eventos de segurança com Amazon S3

Você pode automaticamente [exportar eventos de segurança para a Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/), um provedor de armazenamento em nuvem, com um trabalho diário que é executado à meia-noite UTC. Uma vez configurado, você não precisa exportar manualmente os eventos de segurança do painel.

### Flexibilidade de dados

#### importação de CSV

{% multi_lang_include release_type.md release="General availability" %}

Você pode usar a importação CSV para registrar e atualizar atributos de usuários e eventos personalizados no Braze, como `first_name`, `last_destination_searched` e `trip_booked`. Para começar, veja [Importação CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### Alertas de uso da API

{% multi_lang_include release_type.md release="General availability" %}

Os alertas de uso da API fornecem visibilidade crítica sobre o uso da sua API, permitindo que você detecte proativamente tráfego inesperado. Ao configurar esses alertas para rastrear volumes de solicitações de API chave, você pode receber notificações em tempo real e resolver problemas antes que eles impactem suas campanhas de marketing.

#### Limites de taxa da API do workspace

Com os limites de taxa da API do workspace, você pode definir um número máximo de solicitações de API que um workspace pode fazer para um endpoint de ingestão específico, como `/users/track` ou dados de SDK. Você também pode aplicar limites de taxa a um grupo de workspaces, o que significa que o limite é compartilhado entre todos os workspaces desse grupo.

#### Novos eventos do Currents

Esses novos eventos foram adicionados ao glossário do Currents:

- [Eventos de Abort do Banner]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Eventos de Clique do Banner]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Eventos de Impressão do Banner]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [Eventos de Visualização do Banner]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Eventos de Falha de Webhook]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### Intervalo de tempo padrão para análises de campanha

Por padrão, o intervalo de tempo para [**Análises de Campanha**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) exibirá os últimos 90 dias a partir do momento atual. Isso significa que, se a campanha foi lançada há mais de 90 dias, as análises serão exibidas como "0" para o intervalo de tempo dado. Para visualizar todas as análises de campanhas mais antigas, ajuste o intervalo de tempo de relatório.

#### Comportamento atualizado para a etapa de Caminhos de Experimento do Canvas

Se o seu Canvas tiver um [experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) ativo ou em andamento e você atualizar o Canvas ativo (mesmo que não seja a etapa do Caminho de Experimento), o experimento em andamento será encerrado. Para reiniciar o experimento, você pode desconectar o Caminho de Experimento existente e lançar um novo, ou duplicar o Canvas e lançar um novo Canvas. 

Para saber mais, consulte [Editar canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).

#### Limite de taxa mais rápido disponível para o endpoint `/users/export/ids`

Você também pode aumentar o [limite de taxa para o endpoint /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) para 40 requisições por segundo atendendo aos seguintes requisitos:

- Seu espaço de trabalho tem o limite de taxa padrão (250 requisições por minuto) habilitado. Entre em contato com seu gerente de conta da Braze para mais assistência na remoção de qualquer limite de taxa pré-existente que você possa ter.
- Sua solicitação inclui o parâmetro fields_to_export para listar todos os campos que você deseja receber.

#### Nova tradução para endpoints de templates de email

{% multi_lang_include release_type.md release="Early access" %}

Use esses endpoints para visualizar e fazer atualizações nas traduções e locais para templates de email:

- [GET: Visualizar as traduções de origem]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET: Visualizar uma tradução específica e local para o endpoint de template de email]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_locale_template)
- [GET: Visualizar todas as traduções e locais para um template de email]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_template)
- [PUT: Atualizar traduções para um template de email]({{site.baseurl}}/api/endpoints/translations/email_templates/put_update_template)

### Liberando a criatividade

#### Landing pages

Você pode tornar sua página de destino [responsiva ao tamanho do dispositivo de um usuário]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) empilhando colunas verticalmente em telas menores. Para habilitar isso, adicione uma coluna na linha que você deseja tornar responsiva e, em seguida, ative **Empilhar verticalmente em telas menores** na seção **Personalizar colunas**.

### Canais robustos

#### Filtragem de bots para emails

{% multi_lang_include release_type.md release="General availability" %}

Configure a filtragem de bots em suas [Preferências de Email]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) para excluir todos os cliques suspeitos de máquinas ou bots. Um "clique de bot" em email refere-se a um clique em hyperlinks dentro de um email gerado por um programa automatizado. Ao filtrar esses cliques de bots, você pode intencionalmente acionar e entregar mensagens a destinatários que estão engajados.

#### Blocos de produtos arrastar e soltar

{% multi_lang_include release_type.md release="Early access" %}

O [editor de arrastar e soltar]({{site.baseurl}}/dnd_product_blocks/) permite que você adicione e configure rapidamente blocos de produtos em suas mensagens para exibições de produtos sem costura, sem a necessidade de criar código Liquid personalizado. O recurso de bloco de produto arrastar e soltar está atualmente disponível apenas para e-mail.

#### Texto de span para páginas de destino e mensagens no aplicativo

O texto de span permite que você aplique estilos específicos a blocos de texto sem código personalizado para suas [páginas de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) e [mensagens no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks). Para fazer isso, destaque o texto que você deseja estilizar e, em seguida, selecione **Envolver com span para estilo**. 

#### Anúncio Clique para WhatsApp

[Anúncios que clicam para WhatsApp]({{site.baseurl}}/whatsapp_use_cases/) são uma maneira eficiente de trazer novos e antigos clientes dos anúncios do Meta no Facebook, Instagram ou outras plataformas. Use esses anúncios para promover seus produtos e serviços enquanto torna os usuários cientes da sua presença no WhatsApp. 

### Novas parcerias Braze

#### API Visitory do Shopify — eCommerce

A Braze coleta informações dos visitantes, como endereços de e-mail e números de telefone, por meio de mensagens no navegador. Essas informações são então enviadas para o Shopify. Esses dados ajudam os comerciantes a reconhecer os visitantes de sua loja e criar uma experiência de compra mais personalizada.

#### Okendo — eCommerce

A integração da Braze e [Okendo]({{site.baseurl}}/partners/okendo/) funciona em vários produtos na plataforma da Okendo, incluindo Avaliações, Fidelidade, Referências, Pesquisas e Questionários. A Okendo envia eventos personalizados e atributos de usuário para a Braze, que podem ser usados para personalizar e acionar mensagens.

#### Lemnisk — Plataforma de Dados do Cliente

A integração da Braze e [Lemnisk]({{site.baseurl}}/partners/lemnisk/) permite que marcas e empresas desbloqueiem todo o potencial da Braze, atuando como uma camada de inteligência liderada por CDP que unifica dados de usuários em várias plataformas em tempo real, e enviando as informações e comportamentos do usuário coletados para a Braze em tempo real.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Web SDK 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Removido o `Banner.html` propriedade, `logBannerClick` e `logBannerImpressions` métodos. Em vez disso, use [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner), que gerencia automaticamente o rastreamento de impressões e cliques.
    - Removido o suporte para o recurso legado de Feed de Notícias. Isso inclui a remoção da classe Feed e seus métodos associados.
    - Os campos created e categories que eram usados por cartões de Feed de Notícias legados foram removidos das subclasses de [`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html).
    - O campo linkText também foi removido da subclasse Card de [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) e seu construtor.
    - Esclarecemos definições e atualizamos tipos para notar que certos métodos do SDK retornam explicitamente undefined quando o SDK não está inicializado, alinhando os tipos com o comportamento real em tempo de execução. Isso pode introduzir novos erros de TypeScript em projetos que dependiam dos tipos anteriores (incompletos).
    - As imagens de mensagens no aplicativo com `cropType` de `CENTER_CROP` (como `FullScreenMessage` por padrão) agora são renderizadas via uma tag `<img>` em vez de `<span>` para melhorar a acessibilidade. Isso pode quebrar personalizações CSS existentes para a classe `.ab-center-cropped-img` ou seus filhos.
- [Cordova SDK 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Atualizamos a implementação interna do iOS do método `enableSdk` para usar setEnabled: em vez de `_requestEnableSDKOnNextAppRun`, que foi descontinuado no SDK Swift.
        - Chamar este método não requer mais que o aplicativo seja reiniciado para ter efeito. O SDK agora será ativado assim que este método for executado.
    - Atualizamos a ponte nativa do Android do [SDK da Braze para Android 36.0.0 para o 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Android SDK 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
