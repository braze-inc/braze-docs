---
nav_title: Notas de versão
article_title: Notas de versão
page_order: 4
layout: dev_guide
guide_top_header: "Notas de versão"
guide_top_text: "É aqui que você pode encontrar todas as atualizações da plataforma Braze, com as seguintes <a href='/docs/help/release_notes/#most-recent'>atualizações mais recentes da plataforma</a>."
page_type: landing
search_rank: 1
description: "Esta landing page contém as notas de versão do Braze. É aqui que você pode encontrar todas as atualizações da plataforma Braze e dos SDKs, bem como uma lista de recursos obsoletos."

guide_featured_title: "Notas de versão"
guide_featured_list:
  - name: 2025
    link: /docs/help/release_notes/2025/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2024
    link: /docs/help/release_notes/2024/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2023
    link: /docs/help/release_notes/2023/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2022
    link: /docs/help/release_notes/2022/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2021
    link: /docs/help/release_notes/2021/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2020
    link: /docs/help/release_notes/2020/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2019
    link: /docs/help/release_notes/2019/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2018
    link: /docs/help/release_notes/2018/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2017
    link: /docs/help/release_notes/2017/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: 2016
    link: /docs/help/release_notes/2016/
    image: /assets/img/braze_icons/calendar-check-02.svg
  - name: Depreciações
    link: /docs/help/release_notes/deprecations/
    image: /assets/img/braze_icons/calendar-minus-01.svg
  - name: Changelogs do SDK
    link: /docs/developer_guide/changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Notas de versão mais recentes da Braze {#most-recent}

> O Braze divulga informações sobre atualizações de produtos em uma cadência mensal, alinhando-se com os principais lançamentos de produtos, embora o produto seja atualizado com melhorias diversas semana a semana.<br><br>Para saber mais sobre qualquer uma das atualizações listadas nesta seção, entre em contato com o gerente da sua conta ou [abra um ticket de suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Você também pode conferir [nossos Changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs) para ver mais informações sobre nossos lançamentos, atualizações e aprimoramentos mensais do SDK.

## lançamento de 24 de junho de 2025

### OfferFit by Braze

[OfferFit](https://www.offerfit.ai/) substitui testes A/B com decisões de IA que personalizam tudo e maximizam qualquer métrica: gere dólares, não cliques—com OfferFit, você pode otimizar qualquer KPI de negócios. Consulte nossa seção dedicada [OfferFit by Braze]({{site.baseurl}}/user_guide/offerfit) para casos de uso e recursos principais.

### Novos tutoriais de SDK

Cada tutorial de SDK da Braze oferece instruções passo a passo junto com código de exemplo completo. Escolha um tutorial abaixo para começar:

- [Exibindo Banners]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Personalizando o estilo da mensagem no app]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [Exibindo mensagens no app condicionalmente]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [Adiar mensagens no app acionadas]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### Flexibilidade de dados

#### Provisionamento SAML just-in-time

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Use [provisionamento SAML just-in-time]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit) para permitir que novos usuários do dashboard criem uma conta Braze em seu primeiro login. Isso elimina a necessidade de os administradores criarem manualmente uma conta para um novo usuário do dashboard, escolherem suas permissões, atribuírem a ele um espaço de trabalho e esperarem que ele ative sua conta.

#### Filtros por seleção

Agora você pode adicionar até 10 filtros por [seleção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections).

#### Armazenamento do catálogo

O tamanho de armazenamento para a versão gratuita de [catálogos]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#catalog-storage) é de até 100 MB. Você pode ter itens ilimitados desde que estejam abaixo de 100 MB.

#### Número de linhas sincronizadas com a Ingestão de Dados na Nuvem

Por padrão, para a Ingestão de Dados na Nuvem, cada execução pode sincronizar até 500 milhões de linhas. Qualquer sincronização com mais de 500 milhões de novas linhas será interrompida.

Consulte [limitações do produto de Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations) para mais detalhes.

### Canais robustos

#### Teste de acessibilidade no Inbox Vision

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Use [Teste de acessibilidade]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) no Inbox Vision para destacar problemas de acessibilidade que podem existir com seu e-mail. 

O teste de acessibilidade analisa o conteúdo do seu e-mail em relação a algumas [Diretrizes de Acessibilidade para Conteúdo da Web](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2 AA requisitos. Isso pode fornecer insights sobre quais elementos não estão atendendo aos padrões de acessibilidade.

#### Rastreamento de cliques para WhatsApp

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Você pode ativar [o rastreamento de cliques]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking) tanto em mensagens de resposta quanto em mensagens de modelo para ver dados de cliques em seus relatórios de desempenho do WhatsApp e poder segmentar usuários com base em quem clicou em quê.

#### Vídeos para WhatsApp

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Você pode [incorporar vídeos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features) dentro do texto do corpo para mensagens de WhatsApp enviadas. Esses arquivos devem ser hospedados através de URL ou na [biblioteca de mídia Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library).

### Novas parcerias Braze

#### Stripe - eCommerce

A integração entre Braze e [Stripe]({{site.baseurl}}/partners/stripe) permite que você dispare mensagens no Braze com base em eventos do Stripe, como início de teste, inscrição ativada, cancelamento de inscrição e mais.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [Cordova SDK 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - Atualizado a ponte nativa do Android [do Braze Android SDK 35.0.0 para 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizado a ponte nativa do iOS [do Braze Swift SDK 11.6.1 para 12.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Segment Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Atualizado o Braze Android SDK [de 35.0.0 para 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

## Lançamento em 27 de maio de 2025

### Flexibilidade de dados

#### Copiando Canvases entre espaços de trabalho

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora você pode copiar Canvases entre espaços de trabalho. Isso permite que você inicie a composição da sua mensagem começando com uma cópia de um canva em um espaço de trabalho diferente. Para mais informações sobre o que é copiado, consulte [Cópia de campanhas e Canvases entre espaços de trabalho]({{site.baseurl}}/copying_to_workspaces/).

#### Regras de envio de mensagens para fluxo de aprovação 

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Use [regras de envio de mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules) em seu fluxo de aprovação para limitar o número de usuários alcançáveis antes que uma aprovação adicional seja necessária—dessa forma, você pode revisar suas campanhas e Canvases antes de direcionar um público maior.

#### Diagramas de relacionamento de entidades para Snowflake e Braze

No início deste ano, criamos tabelas de relacionamento de entidades para dados compartilhados entre Snowflake e Braze. Este mês, adicionamos [novos diagramas interativos]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/) onde você pode mover, arrastar e ampliar os detalhes de cada tabela, dando uma ideia melhor de como seus dados interagem com Braze.

### Liberando a criatividade

#### Eventos recomendados

{% multi_lang_include release_type.md release="Acesso antecipado" %}

[Eventos recomendados]({{site.baseurl}}/user_guide/data/custom_data/recommended_events) mapeiam para os casos de uso mais comuns de eCommerce. Ao usar eventos recomendados, você pode desbloquear modelos de Canvas pré-construídos, painéis de relatórios que mapeiam para o ciclo de vida do cliente e muito mais.

### Canais robustos

#### Canal de Banners

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Com [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners), você pode criar mensagens personalizadas para seus usuários, enquanto amplia o alcance de seus outros canais, como e-mail ou notificações por push. Você pode incorporar Banners diretamente em seu app ou site, o que permite que você interaja com os usuários através de uma experiência que parece natural.

#### Canal de Serviços de Comunicação Ricos (RCS)

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

[Serviços de Comunicação Ricos (RCS)]({{site.baseurl}}/about_rcs/) aprimora o SMS tradicional, permitindo que as marcas entreguem mensagens que são não apenas informativas, mas também muito mais envolventes. Agora suportado tanto no Android quanto no iOS, o RCS traz recursos como mídia de alta qualidade, botões interativos e perfis de remetente de marca diretamente nos aplicativos de mensagens pré-instalados dos usuários, eliminando a necessidade de baixar um aplicativo separado.

#### Página de Configurações de Push

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Use a [**página de Configurações de Push**]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings) para configurar as principais configurações para suas notificações por push, incluindo o Tempo de Vida do Push (TTL) e a prioridade padrão do FCM para campanhas Android. Essas configurações ajudam a otimizar a entrega e a eficácia de suas notificações por push, garantindo uma melhor experiência para seus usuários.

#### Códigos de promoção para campanhas de mensagens no app

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Você pode usar [códigos de promoção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) em campanhas de mensagens no app inserindo um [trecho de lista de códigos de promoção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) no corpo da mensagem da sua campanha de mensagem no app.

#### Tratamento de erros de webhook e limitação de taxa

[Sobre webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#webhook-error-handling-and-rate-limiting) tem uma nova seção que descreve como a Braze lida com erros de webhook e limitação de taxa.

#### Locais de mensagens no app

Após [adicionar locais]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/using_locales) ao seu espaço de trabalho, você pode segmentar usuários em diferentes idiomas dentro de uma única mensagem no app.

#### Amazon SES como um Provedor de Envio de E-mail (ESP)

Agora você pode usar o Amazon SES como um ESP, semelhante a como você usaria o SendGrid e o SparkPost. Consulte [SSL na Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) e [Links Universais e Links de Aplicativos]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) para nuances na configuração de SSL e rastreamento de cliques em uma base de link para link.

### Novas parcerias Braze

#### Eagle Eye - Fidelidade

A integração bidirecional entre a Braze e [Eagle Eye]({{site.baseurl}}/partners/eagle_eye/) permite que você ative dados de fidelidade e promoção diretamente na Braze, permitindo que os profissionais de marketing personalizem o engajamento do cliente usando dados em tempo real, como saldos de pontos, promoções e atividades de recompensas.

#### Eppo - Testes A/B

A integração entre a Braze e [Eppo]({{site.baseurl}}/partners/eppo/) permite que você configure testes A/B na Braze e analise os resultados no Eppo para descobrir insights e vincular o desempenho das mensagens a métricas de negócios de longo prazo, como receita ou retenção.

#### Mention Me - Referências

Juntas, [Mention Me](https://www.mention-me.com/) e Braze podem ser seu portal para atrair clientes premium e fomentar uma lealdade à marca inabalável. Ao integrar perfeitamente dados de referência de primeira parte na Braze, você pode oferecer experiências omnicanal altamente personalizadas direcionadas aos fãs da sua marca. Para começar, veja [Parceiros de Tecnologia: Mention Me]({{site.baseurl}}/partners/mention_me).

#### Shopify - eCommerce

[Conecte vários domínios de loja Shopify]({{site.baseurl}}/shopify_connecting_multiple_stores/) a um único espaço de trabalho para ter uma visão holística de seus clientes em todos os mercados. Crie e lance programas de automação e jornadas em um único espaço de trabalho sem duplicar esforços entre lojas regionais.

### Outro

#### Atualização para Construir mensagens acessíveis no Braze

Atualizamos nosso artigo [Construir mensagens acessíveis no Braze]({{site.baseurl}}/help/accessibility/) com orientações mais claras e prescritivas sobre como criar mensagens acessíveis. Este artigo agora inclui práticas recomendadas expandidas para estrutura de conteúdo, texto alternativo, botões e contraste de cores, junto com uma nova seção sobre o manuseio de ARIA para mensagens HTML personalizadas. 

Esta atualização faz parte de nosso esforço mais amplo para apoiar experiências de mensagens mais acessíveis no Braze. Sabemos que a acessibilidade é uma área em evolução e continuaremos compartilhando o que aprendemos.

{% multi_lang_include accessibility/feedback.md %}

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 36.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Esta versão reverte o aumento para a versão mínima do SDK Android do Braze de API 21 para API 25 introduzido na 34.0.0. Isso permite que o SDK seja novamente compilado em aplicativos que suportam versões tão antigas quanto a API 21. Observe que, embora estejamos reintroduzindo a capacidade de compilar, não estamos reintroduzindo suporte formal para < API 25 e não podemos garantir que o SDK funcionará como pretendido em dispositivos que executam essas versões.
    - Se seu aplicativo suporta essas versões, você deve:
        - Validar sua integração do SDK funciona como pretendido em dispositivos físicos (não apenas emuladores) para essas versões de API.
        - Se você não puder validar o comportamento esperado, deve chamar [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) ou não inicializar o SDK nessas versões. Caso contrário, você pode causar efeitos colaterais indesejados ou desempenho degradado nos dispositivos de seus usuários finais.
    - Corrigido um problema em que mensagens no aplicativo causariam uma leitura na thread principal.
    `BrazeInAppMessageManager.displayInAppMessage` agora é uma função suspensa Kotlin.
        - Se você não chamar esta função diretamente, não precisa fazer nenhuma alteração.
    - AndroidX Compose BOM atualizado para 2025.04.01 para lidar com atualizações nas APIs do Jetpack Compose.
- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Atualiza a ponte nativa do Android do Braze Android SDK 35.0.0 para 36.0.0.
    - Atualiza as ligações da versão nativa do iOS do Braze Swift SDK 11.9.0 para 12.0.0.
    - Atualiza a representação da unidade de PushNotificationEvent.timestamp para milissegundos no iOS.
        - Anteriormente, esse valor seria representado em segundos no iOS. Isso agora corresponderá à implementação existente do Android.
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - Esta versão reverte o aumento para a versão mínima do SDK Android do Braze de API 21 para API 25 introduzido na 34.0.0. Isso permite que o SDK seja novamente compilado em aplicativos que suportam versões tão antigas quanto a API 21. No entanto, não estamos reintroduzindo suporte formal para < API 25. Leia mais [aqui](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3600).
    - Atualiza a ponte nativa do Android do Braze Android SDK 35.0.0 para 36.0.0.
    - Atualiza a ponte nativa do iOS do Braze Swift SDK 11.9.0 para 12.0.0.

## Lançamento de 29 de abril de 2025

### Solução de problemas de acesso ao Braze

[Solução de problemas de acesso ao Braze]({{site.baseurl}}/user_guide/administrative/access_braze/troubleshooting/) ajuda você a navegar por problemas que pode ter ao tentar acessar o Braze, como ser bloqueado de sua conta ou trabalhar com um dashboard do Braze que não funcionará como esperado.

### Flexibilidade de dados

#### Perguntas frequentes sobre Currents

Você pode encontrar respostas para algumas perguntas frequentes sobre Currents na nova página [Perguntas frequentes]({{site.baseurl}}/user_guide/data/braze_currents/faq/).

#### Usuários anônimos

Confira as seguintes seções em [Usuários anônimos]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) para novos detalhes sobre como os usuários anônimos funcionam e por que você pode querer atribuir a eles aliases de usuário:
- [Como funciona?]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#how-it-works) 
- [Atribuição de aliases de usuário]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/#assigning-user-aliases)

#### Rascunhos de campanhas

[Salvar rascunhos]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/#campaign-drafts) pode ajudar você a fazer alterações em larga escala em campanhas ativas. Ao criar um rascunho, você pode testar as alterações planejadas antes do seu próximo lançamento.

#### Identificando e mesclando usuários

Ao [identificar]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) ou [mesclar usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/), você pode agora usar o parâmetro `least_recently_updated` no array `prioritization` para priorizar o usuário menos recentemente atualizado.

#### Mesclagem de usuários agendada

[Mesclagem agendada]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#scheduled-merging) permite automatizar a mesclagem de perfis de usuários diariamente usando regras pré-configuradas. O Braze notificará os administradores de seu espaço de trabalho 24 horas antes da mesclagem programada, fornecendo um lembrete e tempo para revisar a configuração.

#### Objeto do destinatário

Agora você pode incluir `braze_id` no [objeto do destinatário]({{site.baseurl}}/api/objects_filters/recipient_object/), o que permite solicitar ou escrever informações em nossos endpoints.

#### Novos data centers

A Braze lançou dois novos [data centers]({{site.baseurl}}/user_guide/data/data_centers/): US-10 e ID-01. Você pode se inscrever para data centers específicos da região ao configurar sua conta Braze. 

### Liberando a criatividade

#### Modelos de página de destino

Use [modelos de página de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#using-landing-page-templates) para criar modelos para suas próximas campanhas. Esses modelos podem ser acessados e gerenciados tanto no editor de página de destino quanto na seção **Modelos** do dashboard.

#### Campo de formulário da página de destino

Ao personalizar sua página de destino, você pode escolher se um campo de formulário é [obrigatório ou opcional]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page). Campos obrigatórios devem ser preenchidos antes que o formulário possa ser enviado. Campos opcionais podem ser deixados em branco ou não selecionados por um usuário.

#### Modelos pré-construídos do Canvas

A Braze Canvas oferece vários [modelos pré-construídos]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/) adaptados especificamente para profissionais de marketing de eCommerce, facilitando a implementação de estratégias essenciais. Esta página oferece alguns modelos-chave que você pode usar para aprimorar suas jornadas de clientes.

### Canais robustos

#### Vídeos do WhatsApp

{% multi_lang_include release_type.md release="Acesso antecipado" %}

[Arquivos de vídeo do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages) agora podem ser hospedados através de uma URL ou na biblioteca de mídia da Braze.

#### Mensagens de lista do WhatsApp

[Listar mensagens]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/message_processing/user_messages#list-messages/) aparecem como uma mensagem de corpo com uma lista de opções clicáveis. Cada lista pode ter várias seções, e cada lista pode ter até 10 linhas.

#### Copiar link da prévia

Use **Copiar link de prévia** no seu HTML e arraste e solte [mensagens de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/overview/#step-3-add-your-sending-information), [modelos de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/email_template/#step-5-preview-and-test-your-message), e [Blocos de Conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) para gerar um link compartilhável que mostra como seu conteúdo ficará para um usuário aleatório.

#### Diagrama de registro de push

Revitalizamos nossa documentação de notificações por push no Guia do Usuário e adicionamos um novo diagrama para ajudar a visualizar [como o registro de push se parece em uma escala maior]({{site.baseurl}}/user_guide/message_building_by_channel/push/push_registration/#what-does-this-look-like-on-a-broader-scale).

### Novas parcerias Braze

#### Categorias de parceiros atualizadas

Atualizamos a [seção de Parceiros de Tecnologia]({{site.baseurl}}/partners/home/) com novas categorias e subcategorias para melhorar sua experiência de navegação.

#### Shopify (nova versão) - eCommerce

Uma nova versão da integração do Shopify será lançada em fases a partir de abril, com base no tipo de loja Shopify e no ID externo usado para configurar a integração inicial.

**A versão mais antiga da integração será descontinuada em 28 de agosto de 2025. Você deve atualizar para a versão mais nova da integração antes de 28 de agosto de 2025.**

Novos clientes da Braze: A partir de abril de 2025, a Braze começará a lançar gradualmente o novo conector Shopify para novos onboardings e atualização de clientes existentes. Para saber mais sobre a nova integração padrão, consulte [integração padrão do Shopify]({{site.baseurl}}/shopify_standard_integration/).

#### Apenas Palavras - Conteúdo Dinâmico

[Apenas Palavras]({{site.baseurl}}/partners/just_words/) hiperpersonaliza o envio de mensagens em escala nos canais de marketing de ciclo de vida, permitindo que você teste dinamicamente centenas de variações e atualize automaticamente o conteúdo de baixo desempenho.

#### Tapcart - eCommerce

[Tapcart]({{site.baseurl}}/partners/ecommerce/tapcart/) é uma plataforma líder de comércio móvel para marcas impulsionadas pelo Shopify, permitindo que os comerciantes criem aplicativos móveis personalizados que oferecem experiências de compra personalizadas e envolventes que seus clientes adoram.

### SDKs

#### Gerenciamento de versão do SDK da Braze

Agora você pode aprender sobre [gerenciamento de versão]({{site.baseurl}}/developer_guide/sdk_integration/version_management/) para o SDK da Braze, para que seu app possa ficar atualizado com os últimos recursos e melhorias de qualidade.

#### auditoria de documentos SDK

Atualmente, estamos auditando todo o nosso [conteúdo SDK para desenvolvedores]({{site.baseurl}}/developer_guide/) para garantir que todos os nossos exemplos de código sejam úteis e precisos. Até agora, fizemos uma variedade de atualizações em nossos documentos Android e Swift, e mais estão a caminho.

### Contribuição para a documentação da Braze

#### Suporte offline para colaboradores do Braze

Se você é um colaborador dos Documentos Braze, agora pode gerar seu site de documentos local completamente offline. Para começar, veja [Contribuindo para os Documentos Braze]({{site.baseurl}}/contributing/home/).

#### Resolvendo problemas com seu fork dos Documentos Braze

Para colaboradores dos Documentos Braze que estão tendo problemas para direcionar nosso repositório a partir de seu fork, criamos [passos de solução de problemas]({{site.baseurl}}/contributing/troubleshooting/#missing-base-repository) para ajudar você a voltar ao caminho certo.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [SDK Braze Unity 8.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
    - Atualizado a ponte nativa do iOS de [Braze Swift SDK 10.3.0 para 11.9.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.9.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizado a ponte nativa do Android de [Braze Android SDK 32.1.0 para 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - A versão mínima do SDK Android exigida é 25. Veja mais detalhes [aqui](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Braze Segment Kotlin 3.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md)
    - Atualizado o SDK Braze Android [de 32.1.0 para 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - A versão mínima do SDK Android exigida é 25. Veja mais detalhes [aqui](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Braze Swift SDK 12.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200)
    - Os XCFrameworks estáticos distribuídos agora incluem seus recursos diretamente em vez de depender de pacotes de recursos externos.
        - Ao integrar manualmente os XCFrameworks estáticos, você deve selecionar a opção *Incorporar e Assinar* para cada XCFramework na seção *Frameworks, Bibliotecas e Conteúdo Incorporado* das *Configurações Gerais* do seu alvo.
        - Nenhuma alteração é necessária para integrações do Swift Package Manager ou CocoaPods.
- [Braze Segment Swift 6.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Atualiza as ligações do SDK Swift do Braze para exigir lançamentos da denominação SemVer `12.0.0` ou superior.
        - Isso permite a compatibilidade com qualquer versão do Braze SDK de `12.0.0` até, mas não incluindo, `13.0.0`.
        - Consulte a entrada do changelog de [`12.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1200) Para saber mais sobre possíveis mudanças significativas.

## Lançamento de 1 de abril de 2025

### Atualizações na navegação do Braze

A navegação atualizada no Braze foi projetada para ajudar você a acessar eficientemente recursos e conteúdos em diferentes dispositivos. Observe que a opção de alternar entre versões de navegação não está mais disponível. Saiba mais em nosso artigo dedicado [Navegando no Braze]({{site.baseurl}}/user_guide/administrative/access_braze/navigation).

### Descomplicando o Guia do Desenvolvedor

Anteriormente, muitas tarefas em nível de plataforma eram divididas em várias páginas, como a integração do SDK Swift, que era dividida em seis páginas. Além disso, recursos compartilhados eram documentados individualmente para cada plataforma, o que significava que pesquisar um tópico como "Configuração de Notificações por Push" retornaria 10 páginas diferentes.

**Antes:**

![A documentação anterior do Swift localizada na seção Guias de Integração de Plataforma.]({% image_buster /assets/img/before_swift.png %})

Agora, as tarefas em nível de plataforma foram mescladas em páginas únicas e os recursos compartilhados do SDK agora existem na mesma página (com a ajuda do nosso novo recurso de guia de SDK). Por exemplo, agora há apenas uma página para Integrar o SDK do Braze, onde você pode alternar entre plataformas selecionando uma guia na parte superior da página. Quando você faz isso, até o índice da página será atualizado para refletir a guia atualmente selecionada.

**Depois:**

![A documentação atualizada do Swift localizada na guia Swift do artigo Integrando o SDK.]({% image_buster /assets/img/after_swift.png %})

![A documentação atualizada do Android localizada na guia Android do artigo Integrando o SDK.]({% image_buster /assets/img/after_android.png %})

### Contribuição para a documentação da Braze

Se você não sabia, nossos documentos são totalmente de código aberto! Você pode aprender como em nosso [Guia de Contribuição]({{site.baseurl}}/contributing/home). Este mês, documentamos algumas funcionalidades do site, como [forçar seções a se expandirem automaticamente]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand) e [renderizar conteúdo gerado por API]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server).

### Flexibilidade de dados

#### Atualizar as propriedades de entrada do canva

As propriedades de entrada do canva agora fazem parte das [variáveis de contexto do canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Cada variável de contexto inclui um nome, um tipo de dados e um valor que pode incluir Liquid. Para saber mais, consulte o [componente de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

#### Atualizações nos filtros de segmentação para filtros de número de telefone

Os filtros de segmentação foram atualizados para refletir mudanças em dois filtros de número de telefone:

- [Número de telefone não formatado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (anteriormente **Número de telefone**): Segmenta seus usuários pelo número de telefone não formatado.
- [Número de telefone]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (anteriormente **Número de telefone de envio**): Segmenta seus usuários pelo campo de número de telefone E.164 formatado.

#### Excluir dados personalizados

À medida que você cria campanhas e segmentos direcionados, pode descobrir que não precisa mais de um evento personalizado ou atributo personalizado. Agora você pode [excluir esses dados personalizados]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data) e remover suas referências do seu app.

#### Importar usuários com endereços de e-mail e números de telefone

Agora você pode usar um endereço de e-mail ou número de telefone para [importar usuários]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#importing-with-email-addresses-and-phone-numbers) e omitir um ID externo ou alias de usuário.

#### Solução de problemas de login iniciado pelo prestador de serviço

O login iniciado pelo prestador de serviço (SP) agora tem uma [seção de solução de problemas]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting) para ajudá-lo a resolver problemas com SAML e questões de login único.

#### Solução de problemas de importação de usuários

A [seção de solução de problemas de importação de usuários]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting) tem novas entradas e atualizações, incluindo como solucionar linhas ausentes em seus arquivos CSV importados.

#### Perguntas frequentes sobre extensões de segmento

Confira nossas [perguntas frequentes]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions) sobre extensões de segmento, incluindo como você pode criar uma extensão de segmento que usa vários eventos personalizados.

#### Atrasos personalizados e estendidos

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Você pode configurar uma [postergação personalizada]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays) para seus usuários e usar isso com uma etapa de Contexto para selecionar a variável de contexto a ser postergada.

Agora você também pode estender as etapas de postergação por até dois anos. Por exemplo, se você estiver integrando novos usuários para seu app, pode adicionar uma postergação estendida de dois meses antes de enviar uma etapa de Mensagem para lembrar os usuários que não iniciaram uma sessão.

#### Atributos de perfil de usuário padrão para Snowflake

{% multi_lang_include release_type.md release="Beta" %}

Agora existem três [atributos de perfil de usuário padrão]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/user_attributes/) no Snowflake. Cada visualização é projetada para um caso de uso específico com suas próprias considerações de performance. Por exemplo, você pode receber um instantâneo periódico dos atributos padrão de um perfil de usuário.

### Canais robustos

#### Fundamentos de envio de mensagens

[Fundamentos de Envio de Mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals) é uma nova seção em Ferramentas de Engajamento que abriga os conceitos e termos compartilhados para campanhas e Canvases, como arquivamento e localização de mensagens.

#### Domínios personalizados do WhatsApp

Agora você pode atribuir [domínios personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/) a um ou vários grupos de inscrição do WhatsApp.

#### Mensagens no app acionadas para Canvas

Agora você pode selecionar um [gatilho para suas mensagens no app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) para ser acionado no início da sessão, ou por eventos e compras personalizados. Após qualquer postergação passar e as opções de público serem verificadas, as mensagens no app são ativadas quando um usuário chega à etapa de Mensagem. Se um usuário iniciar uma sessão e realizar o evento de gatilho para a mensagem no app, o usuário verá a mensagem no app. 

#### Limitar o volume de entrada para Canvas

Você pode limitar o número de pessoas que potencialmente entrariam neste Canvas por uma cadência selecionada (diária, duração do Canvas ou toda vez que o Canvas for agendado). Por exemplo, você pode [definir os controles de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience) para permitir que o Canvas envie apenas para 5.000 usuários por dia.

#### Novo caso de uso: Sistema de lembrete de e-mail de reserva

Aprenda como você pode usar os recursos do Braze para [construir um serviço de envio de e-mail de lembrete de agendamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case). O serviço permitirá que os usuários agendem compromissos e enviará mensagens aos usuários com lembretes de seus compromissos futuros. Embora este caso de uso utilize mensagens de e-mail, você pode enviar mensagens em qualquer canal, ou em múltiplos canais, com base em uma única atualização no perfil do usuário.

#### Rastreamento de cliques para links específicos

Você pode [desativar o rastreamento de cliques]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) para links específicos adicionando código HTML à sua mensagem de e-mail no editor de HTML ou a componentes no editor de arrastar e soltar.

#### Gerenciamento dinâmico do serviço de Notificações por Push da Apple

[O gerenciamento dinâmico do gateway APNs]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management) melhora a confiabilidade e eficiência das notificações por push do iOS, detectando automaticamente o ambiente APNs correto. Anteriormente, você selecionava manualmente os ambientes APNs (desenvolvimento ou produção) para suas notificações por push, o que às vezes levava a configurações de gateway incorretas, falhas de entrega e erros de BadDeviceToken.

#### Suporte Flutter para Banners

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Os Banners agora suportam Flutter. Além disso, toda a documentação dos Banners foi reformulada para facilitar a usabilidade. Confira os seguintes artigos para começar:

- [Sobre Banners]({{site.baseurl}}/developer_guide/banners/)
- [Como criar campanhas de Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/creating_campaigns/)
- [Incorporando Banners em seu app]({{site.baseurl}}/developer_guide/banners/creating_placements/)

#### Rastreamento de cliques do WhatsApp

{% multi_lang_include release_type.md release="Acesso antecipado" %}

[O rastreamento de cliques]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/) permite que você meça quando alguém toca em um link na sua mensagem do WhatsApp—dando a você uma visão clara do que está impulsionando o engajamento. O Braze encurta suas URLs, adiciona rastreamento nos bastidores e registra eventos de cliques à medida que acontecem.

#### Perguntas frequentes sobre push

Confira nosso novo artigo [FAQ sobre Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq) que aborda algumas das perguntas mais frequentes que surgem ao configurar campanhas de push.

#### Solução de problemas de push

[Solução de problemas de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting) fornece uma série de etapas para ajudá-lo a navegar pelos desafios de entrega com notificações por push. Por exemplo, se você está enfrentando desafios de entrega com notificações por push, compilamos etapas que você pode seguir para solucionar o problema.

### Novas parcerias Braze

#### Movable Ink Da Vinci - Conteúdo Dinâmico

A integração Braze e Movable Ink [Da Vinci]({{site.baseurl}}/partners/movable_ink_da_vinci) capacita as marcas a entregar mensagens altamente personalizadas aproveitando o motor de decisão de conteúdo impulsionado por IA do Da Vinci. O Da Vinci seleciona o conteúdo mais relevante para cada usuário e implanta mensagens de forma integrada através do Braze.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Flutter SDK 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Atualiza a ponte nativa do Android de [Braze Android SDK 33.0.0 para 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - A versão mínima do SDK Android exigida é 25. Veja mais detalhes [aqui](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Swift SDK v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## Lançamento em 4 de março de 2025

### Prorrogações

A Braze atualizou nossa definição do que é um soft bounce e está enviando um novo evento chamado [adiamentos]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance) a partir de 25 de fevereiro de 2025 às 10h EST.

Para clientes do Sendgrid, fizemos uma mudança para separar eventos de adiamento de nossos eventos de soft bounce. Contamos eventos adiados como um evento de soft bounce. Isso impacta qualquer cliente do Sendgrid que use Currents, Query Builder, SQL Extension, Snowflake Data Sharing ou nosso produto de E-mail de Transação.

#### Comportamento anterior

Antes de 25 de fevereiro de 2025, um evento adiado para um endereço de e-mail em uma campanha ou Canvas registra um evento de soft bounce toda vez. Como resultado, os adiamentos são incluídos como parte dos dados de soft bounce. Isso pode resultar em um usuário ou uma campanha relatando mais eventos de soft bounce do que o esperado. 

#### Novo comportamento

A partir de 25 de fevereiro de 2025, um evento adiado não registrará mais um evento de soft bounce toda vez. Em vez disso, registraremos um evento de soft bounce uma vez por envio para o endereço de e-mail, não importa quantas vezes o e-mail seja refeito ou adiado.

#### O que isso significa

Você notará uma queda considerável no volume de eventos de soft bounce a partir de 25 de fevereiro de 2025, resultando nas seguintes mudanças potenciais:

- Diminuição nos soft bounces para quaisquer relatórios construídos usando o Query Builder
- Tamanho de segmento menor usando SQL Extensions se você estiver direcionando usuários que tiveram soft bounce X vezes durante o período Y
- Queda no número de eventos de soft bounce entregues usando Currents e qualquer uma de nossas funcionalidades usando Snowflake
- Queda no número de soft bounces para o produto de e-mail de transação

Para clientes do Sparkpost, não há impacto nos dados de eventos de soft bounce, em vez disso, você começará a receber um novo evento de e-mail, adiamento, em Currents e Snowflake.

### Descomplicando o Guia do Desenvolvedor

Conteúdo idêntico que é compartilhado entre vários SDKs está começando a ser mesclado usando o novo recurso de tabulação de SDK do site de docs. Este mês [integração de SDK]({{site.baseurl}}/developer_guide/sdk_integration/), [inicialização de SDK]({{site.baseurl}}/developer_guide/sdk_initialization/) e [Cartões de Conteúdo]({{site.baseurl}}/developer_guide/content_cards/) foram combinados. Fique atento para mais atualizações nos próximos meses.

### Flexibilidade de dados
 
#### IDs Braze para perfis de usuário

Um perfil de usuário agora inclui um [ID Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles). Você pode usar isso ao procurar perfis de usuário.

#### Prorrogações

A Braze atualizou nossa definição do que é um soft bounce e está enviando um novo evento chamado [adiamentos]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance), que é quando um e-mail não foi entregue imediatamente, mas a Braze tentará reenviar o e-mail por até 72 horas após essa falha temporária de entrega para maximizar as chances de entrega bem-sucedida antes que as tentativas para essa campanha específica sejam interrompidas.

#### Relacionamentos de entidades Snowflake
 
Mapeamos os [esquemas de tabela bruta](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt) para Snowflake e os relacionamentos de entidades Braze para uma nova [página de docs amigável ao usuário](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships). Inclui uma divisão das `USER_MESSAGES` tabelas pertencentes a cada canal, bem como descrições para as chaves primárias, estrangeiras e nativas de cada tabela.

#### Gerenciamento de identidade para IDs externos

Usar um endereço de e-mail ou um endereço de e-mail hash como seu ID externo do Braze pode simplificar a gestão de identidade entre suas fontes de dados; no entanto, é importante considerar os [riscos potenciais]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) à privacidade do usuário e à segurança dos dados.
 
### Liberando a criatividade

#### Tutoriais Liquid

Adicionados três [tutoriais Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/operators/#tutorials) sobre como usar operadores nos seguintes cenários.

<table border="1">
  <tr>
    <td>Escolhendo uma mensagem com um atributo personalizado inteiro.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/integer.png %}" alt="A etapa de composição no Braze mostrando uma mensagem com um atributo personalizado inteiro." /></td>
  </tr>
  <tr>
    <td>Escolhendo uma mensagem com um atributo personalizado de string.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/string.png %}" alt="A etapa de composição no Braze mostrando uma mensagem com um atributo personalizado de string." /></td>
  </tr>
  <tr>
    <td>Abortando uma mensagem com base na localização.</td>
    <td><img src="{% image_buster /assets/img/release_notes/2025_05_04/location.png %}" alt="A etapa de composição no Braze mostrando uma mensagem sendo abortada com base na localização." /></td>
  </tr>
</table>
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

#### Etapas de contexto para Canvas
 
{% multi_lang_include release_type.md release="Acesso antecipado" %}
 
Use [etapas de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) para criar ou atualizar um conjunto de variáveis que representam o contexto de um usuário (ou insights sobre o comportamento desse usuário) enquanto eles se movem por um Canvas.

#### Atraso personalizado

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Você pode configurar um [atraso personalizado]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) para seus usuários selecionando o **Personalizar atraso** no seu passo de Atraso. Você pode usar isso com uma etapa de Contexto para selecionar uma variável de contexto para atrasar.

Ao configurar uma etapa de Atraso na jornada do usuário do seu Canvas, você agora pode criar um atraso de até 2 anos.

#### Revertendo a sincronização automática

Ao [compor uma mensagem de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email), você pode reverter para a sincronização automática na guia de Texto Simples selecionando o ícone Regenerar a partir do HTML, que só aparece se o texto simples não estiver sincronizando.

![O botão de reverter para sincronização automática no Braze.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### Canais robustos

#### Atualizações ao Vivo do Android

Embora as Atualizações ao Vivo não estejam oficialmente disponíveis até
[Android 16](https://android-developers.googleblog.com/2025/01/first-beta-android16.html), nossa [Atualizações Ao Vivo para Android]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=android&tab=local) página mostra como emular seu comportamento, para que você possa exibir notificações interativas na tela de bloqueio semelhantes a [Atividades Ao Vivo para o SDK Swift Braze]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift). Diferente das Atualizações Ao Vivo oficiais, essa funcionalidade pode ser implementada para versões mais antigas do Android.

#### Copiando campanhas com feature flags entre espaços de trabalho

Agora você pode [copiar campanhas com feature flags entre espaços de trabalho]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/#copying-campaigns-with-feature-flags). Para fazer isso, certifique-se de que o espaço de trabalho de destino tenha um experimento de feature flag configurado com um ID que corresponda à feature flag referenciada na campanha original.

#### Novos tipos de mensagens do WhatsApp suportados

Mensagens do WhatsApp agora suportam [vídeo, áudio e mensagens de documentos de saída]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages). Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.

#### Mensagens da direita para a esquerda

[Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) cobre as melhores práticas para elaborar mensagens em idiomas que leem da direita para a esquerda, para que suas mensagens sejam exibidas com precisão o máximo possível.
 
### Automação de IA e ML
 
#### Recomendações de itens

[Usando recomendações de itens em mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations) cobre o `product_recommendation` objeto Liquid e inclui um tutorial para ajudá-lo a colocar esse conhecimento em prática.

### Novas parcerias Braze
 
#### Email Love - Extensões de Canal
 
A parceria entre Braze e [Email Love]({{site.baseurl}}/partners/message_orchestration/) aproveita o recurso Exportar para Braze do Email Love e a API Braze para fazer upload de seus modelos de e-mail para o Braze de forma contínua.

#### VWO - Testes A/B
 
A integração entre Braze e [VWO]({{site.baseurl}}/partners/data_and_analytics/ab_testing/vwo/) permite que você aproveite os dados de experimentos do VWO para criar segmentos direcionados e entregar campanhas personalizadas.
 
### Atualizações do SDK
 
As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Aumenta a versão mínima exigida do React Native para [0.71.0](https://reactnative.dev/blog/2023/01/12/version-071). Para mais informações, consulte [Política de Suporte a Lançamentos](https://github.com/reactwg/react-native-releases#releases-support-policy) no Grupo de Trabalho React.
    - Aumenta a versão mínima exigida do iOS para 12.0.
    - Atualiza os bindings da versão nativa do iOS de [Braze Swift SDK 7.5.0 para 8.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualiza os bindings da versão nativa do Android de [Braze Android SDK 29.0.1 para 30.1.1](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

## Lançamento em 4 de fevereiro de 2025

### Melhorias nos Docs do Braze

#### Guia de Contribuição
Nossas atualizações recentes no [Guia de Contribuição]({{site.baseurl}}/contributing/your_first_contribution) facilitam a contribuição de usuários não técnicos para os Docs do Braze.

#### Reformulação de Dados e Análises
Para facilitar a busca do que você procura, separamos os artigos anteriormente agrupados sob "Dados & Análises" em [Dados]({{site.baseurl}}/user_guide/data) e [Análises]({{site.baseurl}}/user_guide/analytics). 

#### Guia do desenvolvedor
Fizemos uma grande limpeza em todos os docs do [Guia do Desenvolvedor Braze]({{site.baseurl}}/developer_guide/home), que incluiu a fusão de "como fazer" que estavam divididos em várias páginas em uma única página.

Há também uma nova [página de referência do SDK]({{site.baseurl}}/developer_guide/references) que lista toda a documentação de referência e repositórios para cada SDK do Braze.

##### SDK do Braze para Unreal Engine
Migramos e reescrevemos todo o conteúdo do README do repositório GitHub do SDK do Braze para Unreal Engine em sua [seção dedicada nos Docs do Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine).

### Flexibilidade de dados

#### Painel de uso da API

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

O [painel de uso da API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard) permite monitorar seu tráfego REST API de entrada no Braze para entender suas tendências dentro do uso de nossas APIs REST e solucionar quaisquer problemas potenciais.

#### Adicionando tags a atributos personalizados

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Você pode [adicionar tags a um atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#adding-tags) após sua criação se você tiver a permissão "Gerenciar Eventos, Atributos, Compras". As tags podem então ser usadas para filtrar a lista de atributos.

#### Seleções de catálogo e endpoints de campos de catálogo assíncronos 

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Os seguintes endpoints estão agora geralmente disponíveis:
* [POST: Criar Campos de Catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)
* [DELETE: Excluir Campo de Catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)
* [DELETE: Excluir Seleção de Catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)
* [POST: Criar Seleção de Catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections)

#### Usando um endereço de e-mail para disparar campanhas ou Canvases

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora você pode especificar um destinatário por endereço de e-mail para disparar suas [campanhas]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) e [Canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience).

#### Usando um número de telefone para identificar um usuário via a API

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora você pode usar um número de telefone, além de um alias e endereço de e-mail, para identificar um usuário através do endpoint da API [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)

#### Obtendo um rastreamento SAML
Adicionamos [passos sobre como obter um rastreamento SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace), o que ajuda você a resolver problemas sobre SSO SAML com o Suporte de forma mais eficiente.
 
#### Data centers específicos por região
À medida que a Braze cresce para atender novas áreas, adicionamos um [artigo sobre os data centers da Braze]({{site.baseurl}}/user_guide/data/data_centers) para esclarecer nossa abordagem operacional.
 
### Liberando a criatividade
 
#### Notificações de queda de preço e notificações de volta ao estoque

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora você pode notificar os clientes quando um item está de volta ao estoque configurando [notificações de volta ao estoque]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/back_in_stock_notifications) através de um Canvas e catálogo.

Você também pode criar [notificações de queda de preço]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog_triggers/price_drop_notifications) para notificar os clientes quando o preço de um item diminuiu configurando notificações de queda de preço em um catálogo e Canvas.

#### Prévia para seleção 

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Após criar uma seleção, você pode [ver o que uma seleção retornaria]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/#test-and-preview) para um usuário aleatório ou um usuário específico.

#### Modelo de itens de catálogo, incluindo Liquid 

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Você pode [modelar itens de catálogo que incluem Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/using_catalogs/#using-liquid).

#### Modelos de canva
Adicionamos novos modelos de Canvas para [integrar usuários com uma pesquisa de preferências]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey) e [criar um cadastro de e-mail com dupla aceitação]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup).

#### Gerenciando leads com Salesforce Sales Cloud para B2B
Uma maneira de os profissionais de marketing B2B usarem a Braze é através de uma integração com o Salesforce Sales Cloud. Leia mais sobre como implementar este [caso de uso]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud).
 
### Canais robustos

#### Listas de supressão

{% multi_lang_include release_type.md release="Beta" %}
 
[Listas de supressão]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) especificam grupos de usuários que nunca receberão mensagens. Os administradores podem criar listas de supressão com filtros de segmento para restringir um grupo de usuários da mesma forma que você faria para segmentação.

### Novas parcerias Braze

#### Construtor - Conteúdo dinâmico
[Construtor]({{site.baseurl}}/partners/ecommerce/product_search_recommendations/constructor/) é uma plataforma de busca e descoberta de produtos que usa IA e machine learning para oferecer experiências de busca, recomendações e navegação personalizadas para sites de ecommerce e varejo.
 
#### Trustpilot - Conteúdo dinâmico
[Trustpilot]({{site.baseurl}}/partners/trustpilot/) é uma plataforma de avaliações online que permite que seus clientes compartilhem feedback e permite que você gerencie e responda a avaliações.

### Atualizações do SDK
 
As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.
 
- [Braze Android SDK 34.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3400)
    - Atualizou a versão mínima do SDK de 21 (Lollipop) para 25 (Nougat).

## Lançamento em 7 de janeiro de 2025

### Liberando a criatividade

#### Modelos de mensagens no aplicativo

Adicionamos [modelos]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/) para mensagens no aplicativo com arrastar e soltar.

#### Gerenciamento de leads do B2B Salesforce Sales Cloud

[Gerenciando leads com Salesforce Sales Cloud]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud/) demonstra como usar webhooks do Braze para criar e atualizar leads no Salesforce Sales Cloud através de uma integração enviada pela comunidade.

### Canais robustos

#### Modelos de canva

Adicionamos modelos do Braze Canvas para [inscrição por e-mail com dupla aceitação]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/) e [integração com pesquisa de preferências]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/).

#### Mudanças na política de aceitação do WhatsApp

A Meta recentemente atualizou sua [política de aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Para informações adicionais, consulte [atualizações de produtos do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/).

#### Ferramenta de largura para Blocos de Conteúdo no editor de arrastar e soltar de e-mail

Você pode [ajustar a largura]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) do seu Bloco de Conteúdo no editor de e-mail de arrastar e soltar. A largura padrão é 100%.

### Flexibilidade de dados

#### Filtro de segmento de Soft Bounced

Segmente seus usuários de acordo com o número de soft bounces X vezes em Y dias. Para mais informações, consulte [glossário de filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced).

#### Visão geral de usuários anônimos

[Usuários anônimos]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) fornece uma visão geral de usuários anônimos e aliases de usuários, destacando sua importância e como podem ser aproveitados em suas mensagens.

#### Membro do Grupo de Controle Global

Você pode [visualizar a associação do Grupo de Controle Global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group) indo para a **guia de Engajamento** do perfil de um usuário individual e rolando até a seção **Diversos**.

### Novas parcerias Braze

#### Justuno - Captura de leads

[Justuno]({{site.baseurl}}/partners/data_and_analytics/leads_capture/justuno/) permite que você crie experiências de visitante totalmente otimizadas para todos os seus públicos com segmentos dinâmicos, oferecendo o direcionamento mais avançado disponível—tudo isso sem impactar a velocidade do site ou aumentar o trabalho de desenvolvimento.

#### Odicci - plataforma de dados do cliente

Integre Braze com [Odicci]({{site.baseurl}}/partners/odicci/), uma plataforma que capacita as empresas a adquirir, engajar e reter clientes por meio de experiências omnicanal impulsionadas pela fidelidade.

#### Optimizely - Testes A/B

A integração entre Braze e [Optimizely]({{site.baseurl}}/partners/data_and_analytics/ab_testing/optimizely/) é uma integração bidirecional que permite que você:

- Sincronize seus segmentos e eventos de cliente Braze com a Plataforma de Dados Optimizely (ODP) todas as noites para enriquecer os perfis, relatórios e segmentação de clientes da Optimizely.
- Envie eventos Braze Currents do Braze para a ferramenta de relatórios da Optimizely.
- Sincronize os dados e eventos de clientes do ODP com o Braze para enriquecer seus dados de cliente Braze e disparar o envio de mensagens do Braze com base em eventos de clientes no ODP.

## Liberação em 10 de dezembro de 2024

### Local do usuário do SDK por endereço IP

A partir de 26 de novembro de 2024, o Braze detectará os locais dos usuários do país geolocalizado usando o endereço IP do início da primeira sessão do SDK. O Braze usará o endereço IP para definir o valor do país nos perfis de usuário criados por meio do SDK, e essa configuração de país baseada em IP estará disponível durante e após a primeira sessão. Consulte o [monitoramento de localização]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences/location_tracking/) para obter mais detalhes.

### Configuração de acesso elevado

O [Elevated Access]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#elevated-access) adiciona uma camada extra de segurança para ações confidenciais em seu dashboard do Braze. Quando ativo, os usuários precisam verificar novamente sua conta antes de exportar um segmento ou visualizar uma chave de API. Para usar o Acesso elevado, acesse **Configurações** > **Configurações administrativas** > **Configurações de segurança** e ative-o.

### Permissão para visualizar informações de identificação pessoal (IPI)

Para os administradores, é possível [permitir que os usuários visualizem IPI]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) conforme definido pela sua empresa no dashboard em prévias de mensagens que usam variáveis Liquid para acessar as propriedades do usuário. 

Para espaços de trabalho, é possível permitir que os usuários visualizem IPI conforme definido pela sua empresa no dashboard ou visualizem os perfis de usuário, mas redigindo os campos que sua empresa identificou como IPI.

### Flexibilidade de dados

#### Esquemas de data lake

Os seguintes esquemas foram adicionados aos esquemas de tabelas brutas:
- `USERS_CANVASSTEP_PROGRESSION_SHARED`: Eventos de progressão para um usuário em um Canva
- `CHANGELOGS_GLOBALCONTROLGROUP_SHARED`: Identifique quais números de baldes aleatórios estão no Grupo de Controle Global atual e anterior
- `USERS_MESSAGES_FEATUREFLAG_IMPRESSION_SHARED`: Eventos de impressão para quando um usuário visualiza um Feature Flag

#### Segmentação baseada em contas

A [segmentação baseada em contas B2B (business-to-business)]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/account_based_segmentation/) pode ser feita de duas maneiras, dependendo de como você configurou seu modelo de dados B2B:

- Ao usar catálogos para seus business objects
- Ao usar fontes conectadas para seus business objects

#### Filtros de segmentação

Consulte [Filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters) de segmentação para obter a lista completa de filtros de segmentação e suas descrições.

##### Perfil de usuário criado em

Segmente seus usuários de acordo com a data de criação do perfil de usuário. Se um usuário tiver sido adicionado por CSV ou API, esse filtro refletirá a data em que ele foi adicionado. Se o usuário não for adicionado por CSV ou API e tiver sua primeira sessão rastreada pelo SDK, esse filtro refletirá a data dessa primeira sessão.

##### Envio de número de telefone

Segmente seus usuários pelo campo de número de telefone e.164. Você pode usar expressões regulares com esse filtro para segmentar por números de telefone com um código de país específico.

### Novas parcerias Braze

#### Narvar - eCommerce

A integração Braze e [Narvar](https://corp.narvar.com/) ativa as marcas para aproveitar os eventos de notificação do Narvar para disparar mensagens diretamente do Braze, mantendo os clientes informados com atualizações oportunas.

#### Zeotap para Currents - Plataforma de dados do cliente

A integração entre o Braze e o [Zeotap](https://zeotap.com/) permite que você amplie a escala e o alcance de suas campanhas, sincronizando os segmentos de clientes do Zeotap com os perfis de usuários do Braze. Com o [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), você também pode conectar dados ao Zeotap para torná-los acionáveis em todo o growth stack.

#### Notificar - Conteúdo dinâmico

A integração do Braze e do [Notify](https://notifyai.io/) permite que os profissionais de marketing promovam efetivamente o engajamento em várias plataformas. Em vez de depender de métodos tradicionais de marketing, uma campanha disparada pela API do Braze pode aproveitar os recursos do Notify para fornecer envio de mensagens personalizadas por meio de vários canais, incluindo e-mail, SMS, notificações por push e muito mais.

#### Contentful - Conteúdo dinâmico

A integração entre o Braze e o [Contentful](https://www.contentful.com/) permite que você use dinamicamente o Connected Content para extrair conteúdo do Contentful para suas campanhas no Braze.

#### Outgrow - Captura de leads 

A integração Braze e [Outgrow](https://outgrow.co/) permite transferir automaticamente os dados de usuários da Outgrow para o Braze, ativando campanhas altamente personalizadas e direcionadas.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Web SDK 5.6.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 12.0.0](https://github.com/braze-inc/braze-flutter-sdk/releases/tag/12.0.0)
    - Atualiza a ponte nativa do iOS do [Braze Swift SDK 10.3.1 para o 11.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.1...11.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
    - Atualiza a ponte nativa do Android do [Braze Android SDK 32.1.0 para o 33.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.1.0...v33.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Swift SDK 11.0.1](https://github.com/braze-inc/braze-swift-sdk/blob/11.0.1/CHANGELOG.md)
