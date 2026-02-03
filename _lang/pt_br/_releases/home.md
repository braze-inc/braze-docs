---
nav_title: Início
article_title: O que há de novo no Braze
description: "As notas de versão do Braze são publicadas mensalmente para que você possa se manter atualizado sobre os principais lançamentos de produtos, aprimoramentos contínuos de produtos, parcerias do Braze, alterações significativas no SDK e depreciações de recursos."
page_order: 0
search_rank: 1
page_type: reference

---

# O que há de novo no Braze

{% alert tip %}
Para obter mais informações sobre qualquer uma das atualizações listadas nesta página, entre em contato com o gerente da sua conta ou [abra um tíquete de suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Você também pode consultar nossos [Changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs) para obter mais informações sobre nossas versões mensais do SDK, melhorias e alterações significativas.
{% endalert %}

{% details January 8, 2026 %}
## Lançamento em 8 de janeiro de 2026

### Dados e relatórios

#### Eventos recomendados para e-commerce

{% multi_lang_include release_type.md release="Early access" %}

Para combinar os eventos recomendados de comércio eletrônico com o evento de compra existente, adicionamos o [ evento de conversão "Places Order"]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/ecommerce_use_cases/#conversions-report), que é semelhante a "Makes Purchase".

#### Atualizações dos eventos do Currents

{% multi_lang_include release_type.md release="General availability" %}

As seguintes alterações foram feitas no Currents na Versão 4:

* O campo muda para o tipo de evento `users.behaviors.pushnotification.TokenStateChange`:
    * Adição do novo campo `string` `push_token` : Push token do evento
* O campo muda para o tipo de evento `users.messages.pushnotification.Bounce`:
    * Adição do novo campo `string` `push_token` : Push token do evento
* O campo muda para o tipo de evento `users.messages.pushnotification.Send`:
    * Adição do novo campo `string` `push_token` : Push token do evento
* O campo muda para o tipo de evento `users.messages.rcs.Click`:
    * Adição do novo campo `string` `canvas_variation_name` : Nome da variante do canva recebida por este usuário
    * O campo `user_phone_number` agora é *opcional*.
* O campo muda para o tipo de evento `users.messages.rcs.InboundReceive`:
    * O campo `user_id` agora é *opcional*.
* O campo muda para o tipo de evento `users.messages.rcs.Rejection`:
    * Adição do novo campo `string` `canvas_step_message_variation_id` : API ID da variação da mensagem da etapa do canva que este usuário recebeu

Consulte o [registro de alterações]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) para ver as alterações de eventos de cada versão.

#### Exportar registros de sincronização por todas as linhas

{% multi_lang_include release_type.md release="Early access" %}

No [painel **Registro de sincronização** de ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/#exporting-sync-logs), você pode optar por exportar os registros em nível de linha para uma sincronização executada por:

* Linhas com erros Faz o download de um arquivo que contém apenas as linhas com status de **erro**.
* Todas as linhas Faz o download de um arquivo que contém todas as linhas processadas na execução.

### Canais e pontos de contato

#### Conector de WhatsApp do tipo "traga seu próprio aparelho" (BYO)

O [conector Bring Your Own (BYO) WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/byo_connector/) oferece uma parceria entre a Braze e a Infobip, na qual você dá à Braze acesso ao seu Infobip WhatsApp Business Manager (WABA). Isso permite que você gerencie e pague pelos custos de mensagens diretamente com a Infobip e, ao mesmo tempo, use a Braze para segmentação, personalização e orquestração de campanhas. 

#### Banners no canva

{% multi_lang_include release_type.md release="Early access" %}

Você pode selecionar **Banners** como um canal de mensagens em uma [etapa de Mensagem]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step) para o Canvas. Você pode usar o editor de arrastar e soltar para criar mensagens personalizadas em linha, proporcionando experiências não intrusivas e contextualmente relevantes que são atualizadas automaticamente no início de cada sessão do usuário. 

#### BCC dinâmico

{% multi_lang_include release_type.md release="General availability" %}

Com o [BCC dinâmico]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=bcc%20address#dynamic-bcc), você pode usar Liquid em seu endereço BCC. Observe que esse recurso está disponível apenas nas **Preferências de e-mail** e não pode ser definido na própria campanha. É permitido apenas um endereço BCC por destinatário de e-mail.

#### Limites de taxa baseados em canais

Como alternativa a um limite de taxa que é compartilhado em toda uma campanha multicanal ou Canvas, você pode selecionar um limite de taxa específico por canal. Nesse caso, o limite de taxa se aplicará a cada um dos canais selecionados. Por exemplo, você pode definir sua campanha ou Canvas para enviar um máximo de 5.000 webhooks e 2.500 mensagens SMS por minuto em toda a campanha ou Canvas. Para obter mais detalhes, consulte [Limitação de taxa e limitação de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting).

### Parcerias

#### LILT - Localização

[O LILT]({{site.baseurl}}/partners/lilt/) é a solução completa de IA para tradução empresarial e criação de conteúdo. A LILT permite que organizações globais dimensionem e otimizem suas operações de conteúdo, produtos, comunicações e suporte, com agentes de IA e fluxos de trabalho totalmente automatizados.

### Atualizações de última hora do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android 40.1.1](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4011):
- [Android SDK 40.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#4010)
- [Swift SDK 14.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Remove o Feed de notícias.
        - Isso remove totalmente todos os elementos da interface do usuário, modelos de dados e ações associadas ao Feed de notícias.
- [Web SDK 6.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details December 9, 2025 %}

## 9 de dezembro de 2025

### Dados e relatórios

#### Adição do Google Tag Manager a uma página de destino

Para adicionar o Google Tag Manager às suas páginas de destino, adicione um bloco de código personalizado à sua página de destino no editor de arrastar e soltar e, em seguida, [insira o código do Tag Manager]({{site.baseurl}}/user_guide/engagement_tools/landing_pages#adding-google-tag-manager-to-a-landing-page) no bloco.

### Orquestração

#### Caso de uso do SMS Liquid

O caso de uso [Responder com mensagens diferentes com base na palavra-chave do SMS de entrada]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/liquid_use_cases#sms-keyword-response) incorpora o processamento dinâmico de palavras-chave do SMS para responder a mensagens de entrada específicas com diferentes cópias de mensagens. Por exemplo, você pode enviar respostas diferentes quando alguém envia a mensagem "START" (iniciar) ou "JOIN" (participar).

#### Listagem de permissões para conteúdo conectado

Você pode permitir que URLs específicos da lista sejam usados para o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call). Para acessar esse recurso, entre em contato com o gerente de sucesso do cliente.

### Canais e pontos de contato

#### Codificação de caracteres de SMS

Nossa [calculadora de segmentos de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/#segment-calculator) agora tem codificação de caracteres! Selecione **Display Character Encoding (Exibir codificação de caracteres** ) para identificar quais caracteres são codificados como GSM-7 ou UCS-2. 

![Calculadora de segmento de SMS com uma amostra de mensagem SMS inserida na caixa de texto e com a codificação de caracteres ativada.]({% image_buster /assets/img/sms/character_encoding.png %}){: style="max-width:70%;"}

#### Mensagens do WhatsApp com otimização

Como a API do MM para WhatsApp não oferece 100% de capacidade de entrega, é importante entender como redirecionar os usuários que talvez não tenham recebido sua mensagem em outros canais. 

Para redirecionar os usuários, recomendamos criar um segmento de usuários que não receberam uma mensagem específica. Para fazer isso, filtre pelo código de erro `131049`, que indica que uma mensagem de modelo de marketing não foi enviada devido à aplicação do limite de modelo de marketing por usuário do WhatsApp. Você pode fazer isso [usando o Braze Currents ou as Extensões de Segmento SQL]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/#retargeting-users-on-other-braze-channels).

### Parcerias

#### OtherLevels - Conteúdo dinâmico

[A OtherLevels]({{site.baseurl}}/partners/otherlevels/) é uma plataforma de experiência que usa IA generativa para transformar a maneira como as marcas esportivas, editoras e operadoras se conectam com seus clientes, transformando o conteúdo tradicional em experiências de mídia avançada e vídeo personalizado de acordo com a marca em escala.

### SDK

#### Atualizações de última hora do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Web SDK 6.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details November 11, 2025 %}

## 11 de novembro de 2025

### Flexibilidade de dados

#### `Live Activities Push to Start Registered for App` filtro de segmentação

O filtro `Live Activities Push to Start Registered for App` segmenta os usuários de acordo com o fato de eles estarem registrados para iniciar uma Live Activity por meio de notificações push do iOS para um aplicativo específico.

#### Extensão do segmento SQL do RFM

Você pode criar uma [extensão de segmento RFM (recência, frequência, monetário)]({{site.baseurl}}/rfm_segments/) para direcionar seus melhores usuários, medindo seus hábitos de compra.

A análise de RFM é uma técnica de marketing que identifica seus melhores usuários pontuando-os em uma escala de 0 a 3 para cada categoria (recência, frequência, monetária), em que 3 é a melhor pontuação e 0 é a pior. Os valores de recência, frequência e monetários são todos baseados em dados de um intervalo de tempo específico de sua escolha.

#### Atributos personalizados - Valores 

Ao visualizar um relatório de uso, selecione a [guia**Valores**]({{site.baseurl}}/user_guide/data/activation/custom_data/custom_attributes/#values-tab) para visualizar os principais valores dos atributos personalizados selecionados com base em uma amostra de aproximadamente 250.000 usuários.

#### Registros de sincronização e observabilidade para ingestão de dados na nuvem

{% multi_lang_include release_type.md release="General availability" %}

O [painel]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) Cloud Data Ingestion (CDI) [Sync Log]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/sync_logs/) permite monitorar todos os dados processados pelo CDI, verificar se os dados foram sincronizados com êxito e diagnosticar quaisquer problemas com dados "incorretos" ou ausentes.

#### Lançamentos de sinalizadores de recursos de várias regras

Use [lançamentos de sinalizadores de recursos com várias regras]({{site.baseurl}}/developer_guide/feature_flags/create/#multi-rule-feature-flag-rollouts) para definir uma sequência de regras para avaliar os usuários, o que permite uma segmentação precisa e lançamentos de recursos controlados. Esse método é ideal para implementar o mesmo recurso em diversos públicos.

#### Mapeamento para campos de catálogo para blocos de produtos do tipo arrastar e soltar

Nas configurações do catálogo, você pode selecionar o botão de alternância **Product blocks (Blocos de produtos** ) para [mapear para campos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) e informações [específicos]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/product_blocks/#catalog-setup) em seu catálogo. Isso permite que você selecione os campos a serem usados como título do produto, URL do produto e URL da imagem.

#### Eventos de interrupção por limite de frequência no Currents

Ao usar Currents, agora você pode fazer referência a `abort_type` nos eventos de cancelamento de canal. Identifica que uma mensagem foi abortada devido ao limite de frequência e inclui a regra de limite de frequência que causou o aborto. Isso ajuda a informar como você configura suas regras de limite de frequência. Consulte [Eventos de engajamento de mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events) para obter detalhes específicos do evento Currents.

### Canais robustos

#### Imagens de linha de fundo 

{% multi_lang_include release_type.md release="General availability" %}

Você pode [adicionar uma imagem de linha de fundo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#background-image) a uma mensagem in-app ou landing page no painel **de propriedades da linha**. Ative a opção **Imagem de fundo** e, em seguida, forneça o URL da imagem ou selecione uma imagem na [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/). Por fim, configure seu texto alternativo, tamanho, posição e se a imagem se repete para criar padrões na linha.

![Uma imagem de fundo em linha de uma pizza que tem um padrão de repetição horizontal.]({% image_buster /assets/img_archive/background_row.png %})

#### Copiar link da prévia

Use o **link Copiar visualização** em seus [banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#step-5-test-your-message-optional), [rodapés personalizados de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/custom_email_footer/#creating-your-custom-footer) e [páginas de opt-in e cancelamento de assinatura de e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/?tab=custom%20footer#subscription-pages-and-footers) para gerar um link compartilhável que mostre como seu conteúdo será exibido para um usuário aleatório.

#### Mensagens do WhatsApp com entrega otimizada

Use os sistemas avançados de IA do Meta para entregar suas mensagens de marketing a mais usuários que têm maior probabilidade de se envolver com elas, aumentando significativamente a capacidade de entrega e o envolvimento com as mensagens.

[As mensagens do WhatsApp com entrega otimizada]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/optimized_delivery/) são enviadas usando a nova [API Marketing Messages Lite](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/) da Meta, que oferece desempenho superior em comparação com a API tradicional da nuvem. Esse novo pipeline de envio ajuda você a alcançar melhor os usuários que valorizam e desejam receber suas mensagens.

#### WhatsApp Flows

Ao incorporar uma mensagem do WhatsApp Flow em um Braze Canvas ou em uma campanha, talvez você queira capturar e utilizar informações específicas que os usuários enviam por meio do Flow. O Braze precisa receber informações adicionais sobre a estrutura da resposta do usuário, especificamente a forma esperada da resposta JSON, para gerar o esquema de atributo personalizado aninhado (NCA) necessário.

Agora você pode fornecer ao Braze as informações sobre a estrutura da resposta salvando [a resposta do fluxo como um atributo personalizado]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=recommended%20method#step-1-generate-the-flow-custom-attribute) e concluindo um envio de teste.

#### Visualização editável do usuário

Você pode [editar campos individuais de um usuário aleatório ou existente]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/sending_test_messages/?tab=webhook#customizing-an-existing-user) para ajudar a testar o conteúdo dinâmico em sua mensagem. Selecione **Edit (Editar** ) para converter o usuário selecionado em um usuário personalizado que possa ser modificado.

![A guia "Preview as a User" (Visualizar como usuário) com um botão "Edit" (Editar).]({% image_buster /assets/img_archive/edit_user_preview.png %}){: style="max-width:50%;"}

### Automação de IA e ML

#### BrazeAI Decisioning Studio™ Go

Agora você pode configurar sua integração com o [BrazeAI Decisioning Studio™ Go]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go) consultando estes artigos de configuração para:

- [Braze]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_braze)
- [Klaviyo]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_klaviyo)
- [Nuvem de marketing da Salesforce]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/go/configuring_sfmc)

#### Novos recursos para agentes do Braze

{% multi_lang_include release_type.md release="Beta" %}

Agora você pode personalizar seu [Braze Agent]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents):

- Aplicação de [diretrizes de marca]({{site.baseurl}}/user_guide/administrative/app_settings/brand_guidelines) para que seu agente siga em sua resposta. 
- Fazer referência a um catálogo para personalizar ainda mais sua mensagem.
- Estruturar a saída de um agente fornecendo o [formato de saída]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#output-format).
- Ajustar a [temperatura]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents/#temperature) para o nível de desvio da produção de seu agente.

### Modelos ChatGPT com operador <sup>BrazeAITM</sup> 

{% multi_lang_include release_type.md release="Beta" %}

Você pode selecionar entre esses modelos de GPT para usar em diferentes tipos de solicitação com o [Operator]({{site.baseurl}}/user_guide/brazeai/operator):

- GPT-5 Nano
- GPT-5 mini (padrão)
- GPT-5

### Novas parcerias Braze

#### StackAdapt - Publicidade

[A StackAdapt]({{site.baseurl}}/partners/stackadapt/) é uma plataforma de marketing baseada em IA que oferece publicidade direcionada e orientada para o desempenho. Ele permite que você sincronize os dados do perfil do usuário do Braze com o StackAdapt Data Hub. Ao conectar as duas plataformas, você pode criar uma visão unificada de seus clientes e ativar dados primários para melhorar o desempenho dos anúncios.

#### Cloudinary - Conteúdo dinâmico

[O Cloudinary]({{site.baseurl}}/partners/cloudinary/) é uma plataforma de imagem e vídeo que permite gerenciar, editar, otimizar e fornecer imagens e vídeos em grande escala para qualquer campanha em todos os canais e jornadas de clientes. Quando integrado e ativado, o gerenciamento de mídia do Cloudinary potencializará e fornecerá o fornecimento de ativos dinâmicos, contextuais e personalizados para suas campanhas e Canvases do Braze.

#### Kameleoon - Teste A/B

[O Kameleoon]({{site.baseurl}}/partners/kameleoon/) é uma solução de otimização com experimentos, personalização com IA e recursos de gerenciamento de recursos em uma única plataforma unificada.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [React Native SDK 18.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/16.1.0/CHANGELOG.md)
    - Corrige o tipo de Typescript para o retorno de chamada de `subscribeToInAppMessage` e `addListener` para `Braze.Events.IN_APP_MESSAGE_RECEIVED`.
        - Esses ouvintes agora retornam corretamente um retorno de chamada com o novo tipo `InAppMessageEvent`. Anteriormente, os métodos eram anotados para retornar um tipo `BrazeInAppMessage`, mas na verdade estavam retornando um `String`.
         - Se estiver usando uma das APIs de assinatura, certifique-se de que o comportamento das suas mensagens no aplicativo não seja alterado após a atualização para esta versão. Veja nosso código de amostra em `BrazeProject.tsx`.
    - As APIs `logInAppMessageClicked`, `logInAppMessageImpression` e `logInAppMessageButtonClicked` agora aceitam apenas um objeto `BrazeInAppMessage` para corresponder à sua interface pública existente.
        - Anteriormente, ele aceitava tanto um objeto `BrazeInAppMessage` quanto um `String`.
    - `BrazeInAppMessage.toString()` agora retorna uma string legível em vez da representação de string JSON.
        - Para obter a representação da string JSON de uma mensagem in-app, use `BrazeInAppMessage.inAppMessageJsonString`.
    - No iOS, `[[BrazeReactUtils sharedInstance] formatPushPayload:withLaunchOptions:]` foi movido para `[BrazeReactDataTranslator formatPushPayload:withLaunchOptions:]`.
        - Esse novo método agora é um método de classe em vez de um método de instância.
    - Adiciona anotações de anulabilidade aos métodos do site `BrazeReactUtils`.
    - Remove os seguintes métodos e propriedades obsoletos da API:
        - `getInstallTrackingId(callback:)` a favor de `getDeviceId`.
        - `registerAndroidPushToken(token:)` a favor de `registerPushToken`.
        - `setGoogleAdvertisingId(googleAdvertisingId:adTrackingEnabled:)` a favor de `setAdTrackingEnabled`.
        - `PushNotificationEvent.push_event_type` a favor de `payload_type`.
        - `PushNotificationEvent.deeplink` a favor de `url`.
        - `PushNotificationEvent.content_text` a favor de `body`.
        - `PushNotificationEvent.raw_android_push_data` a favor de `android`.
        - `PushNotificationEvent.kvp_data` a favor de `braze_properties`.
    - Atualiza os vínculos da versão nativa do Android SDK [do Braze Android SDK 39.0.0 para 40.0.2](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.2#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SDK do .NET MAUI (Xamarin) Versão 8.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Atualizada a vinculação do iOS de [SDK Swift da Braze 12.1.0 para o 13.3.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.1.0...13.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Isso inclui suporte ao Xcode 26.
- [Flutter SDK 16.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Atualiza a ponte nativa do Android do [Braze Android SDK 39.0.0 para o 40.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v39.0.0...v40.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)
- [Braze Swift SDK 13.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK 6.3.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Android SDK 40.0.0-40.0.2](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)

{% enddetails %}

{% details October 14, 2025 %}

## Liberação em 14 de outubro de 2025

### BrazeAI Decisioning Studio™

[O BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) substitui os testes A/B por decisões de IA que personalizam tudo e maximizam qualquer métrica: gere dólares, não cliques. Com o BrazeAI Decisioning Studio™, você pode otimizar qualquer KPI de negócios. Consulte a nossa seção dedicada [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) para ver exemplos de casos de uso e os principais recursos.

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
- `message_id` 
  - `users.messages.whatsapp.InboundReceive`
- `message_id` 
  - `users.messages.whatsapp.Send`
  - `users.messages.whatsapp.Delivery`
  - `users.messages.whatsapp.Failure`
  - `users.messages.whatsapp.Read`

#### Listas de supressão

{% multi_lang_include release_type.md release="General availability" %}

[As listas de supressão]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) são grupos de usuários que não recebem automaticamente nenhuma campanha ou Canvases. As listas de supressão são definidas por filtros de segmento, e os usuários entram e saem das listas de supressão à medida que atendem aos critérios de filtro.

#### Personalização sem cópia

{% multi_lang_include release_type.md release="Early access" %}

Sincronize os acionadores do Canvas usando a ingestão de dados na nuvem para [personalização de cópia zero]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/zero_copy_sync/). Esse recurso acessa informações específicas do usuário da sua solução de armazenamento de dados e as transmite para um Canvas de destino. As etapas do Canvas podem, opcionalmente, incluir campos de personalização que não são mantidos nos perfis de usuário do Braze.

#### Variáveis de contexto do Canvas para as etapas de Caminhos do público e Divisão de decisões

{% multi_lang_include release_type.md release="Early access" %}

Você pode [criar filtros de variáveis]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/context_variables/#context-variable-filters) de contexto que usam variáveis de contexto declaradas anteriormente nas etapas [Audience Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) e [Decision Split]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split).

### Liberando a criatividade

#### Cartões de ofertas para e-mails

Use [os Deal Cards]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/gmail_promotions_tab) para fornecer informações importantes sobre a oferta diretamente na parte superior do corpo do e-mail. Isso permite que os destinatários entendam rapidamente os detalhes da oferta e tomem providências.

#### Modelos para banners

Ao [compor seu Banner]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create), agora você pode começar com um modelo em branco, usar um modelo do Braze ou selecionar um modelo de Banner salvo.

### Canais robustos

#### Listas de supressão

{% multi_lang_include release_type.md release="General availability" %}
 
As listas de supressão especificam grupos de usuários que nunca receberão mensagens. Os administradores podem criar listas de supressão com filtros de segmento para restringir um grupo de usuários da mesma forma que você faria para a segmentação.

#### Rastreamento de cliques no LINE

{% multi_lang_include release_type.md release="General availability" %}

Quando [o rastreamento de cliques LINE]({{site.baseurl}}/line/click_tracking/) está ativado, o Braze encurta automaticamente seus URLs, adiciona mecanismos de rastreamento e registra os cliques em tempo real. Enquanto o LINE oferece dados agregados de cliques, o Braze fornece informações granulares do usuário que são oportunas e acionáveis. Esses dados permitem que você crie estratégias de segmentação e redirecionamento mais direcionadas, como a segmentação de usuários com base no comportamento de cliques e o acionamento de mensagens em resposta a cliques específicos.

#### Filtragem de cliques de bots de SMS e RCS

{% multi_lang_include release_type.md release="General availability" %}

[A filtragem de cliques de bots de SMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/bot_click_filtering/) aprimora a análise de campanhas e os fluxos de trabalho, excluindo cliques suspeitos de bots. Um "clique de bot" refere-se a cliques automatizados em links encurtados em mensagens SMS e RCS, como os de rastreadores da Web, visualizações de links do Android e iOS ou software de segurança CPaaS. Esse recurso facilita a geração de relatórios precisos, a segmentação e a orquestração para envolver usuários reais.

#### Transferir números de telefone do WhatsApp

Transfira um número de telefone da WhatsApp Business Account (WABA) e seu grupo de assinatura associado [de um espaço de trabalho para outro]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/transfer_between_workspaces/) no Braze.

#### Mensagens de resposta e visualização do WhatsApp Flows

Em um Canvas, você pode criar uma etapa de mensagem do WhatsApp que use uma [mensagem de resposta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/whatsapp_flows/?tab=response%20message#configuring-whatsapp-flow-messages-and-responses) e uma mensagem de fluxo. Você também pode selecionar **Preview Flow (Visualizar fluxo** ) para visualizar o fluxo diretamente no Braze e confirmar que ele se comporta como esperado.

#### Mensagens de produto no WhatsApp

[As mensagens de produtos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/) permitem que você envie mensagens interativas do WhatsApp que exibem produtos diretamente do seu catálogo do Meta.

#### Integração do Braze e do WhatsApp com um sistema externo

[Aproveite o poder dos chatbots com IA e das transferências de agentes ao vivo]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_use_cases/external_system/) no canal do WhatsApp para otimizar suas operações de suporte ao cliente. Ao automatizar as consultas de rotina e fazer a transição perfeita para agentes humanos quando necessário, você pode melhorar significativamente os tempos de resposta e aprimorar a experiência geral do cliente.

### Automação de IA e ML

#### Agentes da Braze

{% multi_lang_include release_type.md release="Beta" %}

[Os Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) são ajudantes com tecnologia de IA que você pode criar dentro do Braze. Os agentes podem gerar conteúdo, tomar decisões inteligentes e enriquecer seus dados para que você possa oferecer experiências mais personalizadas aos clientes.

### Novas parcerias Braze

#### Jasper - Modelos

A integração [do Jasper]({{site.baseurl}}/partners/jasper/) com o Braze permite que você otimize a criação de conteúdo e a execução de campanhas. Com o Jasper, suas equipes de marketing podem gerar textos de alta qualidade e de acordo com a marca em minutos. O Braze então facilita a entrega dessas mensagens ao público certo no momento ideal. Essa integração promove fluxos de trabalho contínuos, reduz o esforço manual e gera resultados de engajamento mais sólidos.

#### Swym - Fidelidade e retargeting

[A Swym]({{site.baseurl}}/partners/swym/) ajuda as marcas de comércio eletrônico a capturar a intenção de compra com alertas de Wishlists, Save for Later, Gift Registry e Back-in-Stock. Usando dados avançados e baseados em permissões, você pode criar campanhas hiperdirecionadas e oferecer experiências de compras personalizadas que impulsionam o envolvimento, aumentam as conversões e a fidelidade.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; você pode encontrar todas as outras atualizações verificando os changelogs correspondentes do SDK.

- [SDK do Cordova 14.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Atualizamos a ponte nativa do Android do [SDK da Braze para Android 37.0.0 para o 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - A versão mínima exigida do GradlePluginKotlinVersion agora é 2.1.0.
    - Atualizamos a ponte nativa do iOS do [SDK Swift da Braze 12.0.0 para o 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Isso inclui suporte ao Xcode 26.
    - Remove o suporte ao Feed de notícias. As seguintes APIs foram removidas:
        - `launchNewsFeed`
        - `getNewsFeed`
        - `getNewsFeedUnreadCount`
        - `getNewsFeedCardCount`
        - `getCardCountForCategories`
        - `getUnreadCardCountForCategories`
- [React Native SDK 17.0.0-17.0.1](https://www.npmjs.com/package/@braze/react-native-sdk/v/17.0.1)
    - Atualiza os vínculos da versão nativa do Android SDK [do Braze Android SDK 37.0.0 para 39.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v37.0.0...v39.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Remove o suporte ao Feed de notícias. As seguintes APIs foram removidas:
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
    - Atualizamos a ponte nativa do iOS do [SDK Swift da Braze 12.0.0 para o 13.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed). Isso inclui suporte ao Xcode 26.

{% enddetails %}
{% details September 16, 2025 %}

## Liberação em 16 de setembro de 2025

### Flexibilidade de dados

#### Plataforma de dados Braze

A Braze Data Platform é um conjunto de recursos de dados abrangentes e compostáveis e integrações de parceiros que permitem que você crie experiências personalizadas e impactantes em todo o ciclo de vida do cliente. Saiba mais sobre os três trabalhos relacionados a dados a serem realizados: 

- [Unificação de dados]({{site.baseurl}}/user_guide/data/unification) :
- []({{site.baseurl}}/user_guide/data/activation)Ativação de dados
- [Distribuição de dados]({{site.baseurl}}/user_guide/data/distribution) :

#### Propriedades do banner personalizado

{% multi_lang_include release_type.md release="Early access" %}

Você pode usar propriedades personalizadas da sua campanha de banner para recuperar dados de valor-chave por meio do SDK e modificar o comportamento ou a aparência do seu aplicativo. Para saber mais, consulte [Propriedades do banner personalizado]({{site.baseurl}}/developer_guide/banners/placements/#custom-properties).

#### Autenticação por token

{% multi_lang_include release_type.md release="General availability" %}

Ao usar o conteúdo conectado na Braze, você poderá descobrir que certas APIs exigem um token em vez de um nome de usuário e senha. O Braze pode armazenar credenciais que contêm [valores de cabeçalho de autenticação de token]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call#using-token-authentication).

#### Códigos promocionais

É possível salvar códigos promocionais no perfil de um usuário por meio de uma etapa de atualização do usuário. Para obter mais informações, consulte [Como salvar códigos promocionais em perfis de usuário]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#save-to-profile).

### Liberando a criatividade

#### Piloto de brasagem

[O Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot) é um aplicativo disponível publicamente para Android e iOS que permite lançar mensagens do seu painel Braze para o seu telefone. Consulte [Introdução ao Braze Pilot]({{site.baseurl}}/user_guide/getting_started/braze_pilot/getting_started) para obter um passo a passo sobre o download do aplicativo, a inicialização da conexão com o painel do Braze e a conclusão da configuração.

### Novas parcerias Braze

#### Blings - Conteúdo visual e interativo

[A Blings]({{site.baseurl}}/partners/blings/) é uma plataforma de vídeo personalizado de última geração que permite que você ofereça experiências de vídeo em tempo real, interativas e orientadas por dados em todos os canais e em grande escala.

#### Integração padrão da Shopify com ferramenta de terceiros

Para lojas on-line do Shopify, recomendamos usar o método de integração padrão do Braze para oferecer suporte aos SDKs do Braze em seu site.

No entanto, entendemos que você pode preferir usar uma ferramenta de terceiros, como o Google Tag Manager, por isso elaboramos um guia sobre como fazer isso. Para começar, consulte [Shopify: Marcação de terceiros]({{site.baseurl}}/shopify_standard_integration_third_party_tagging/).

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Braze Flutter SDK 15.0.0](https://github.com/braze-inc/braze-flutter-sdk/blob/main/CHANGELOG.md#1500)
    - Atualiza a ponte Android nativa do Braze Android SDK `36.0.0` para `39.0.0`.
    - Atualiza a ponte nativa do iOS do Braze Swift SDK `12.0.0` para `13.2.0`. Isso inclui suporte ao Xcode 26.

- [Braze Swift SDK 7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1300)
  - Atualiza as ligações do Braze Swift SDK para exigir versões da denominação `13.0.0+` SemVer. Isso permite a compatibilidade com qualquer versão do Braze SDK de `13.0.0` até, mas não incluindo, `14.0.0`.

{% enddetails %}
{% details August 19, 2025 %}

## Liberação em 19 de agosto de 2025

### Padronização da consistência do fuso horário para o Canvas Context

{% multi_lang_include release_type.md release="Early access" %}

Se você estiver participando do [acesso antecipado à etapa de contexto do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context), todos os carimbos de data/hora com um tipo de data e hora das propriedades de eventos de acionamento em Canvases baseados em ação serão sempre normalizados para [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time). Para saber mais sobre isso, consulte [Padronização da consistência do fuso horário]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context#time-zone-consistency-standardization).

### Flexibilidade de dados

#### Domínios personalizados de autoatendimento

{% multi_lang_include release_type.md release="General access" %}

[Os domínios personalizados de autoatendimento]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/custom_domains/) permitem que você configure e gerencie seus próprios domínios personalizados para SMS, RCS e WhatsApp, diretamente do painel do Braze. Você pode adicionar, monitorar e gerenciar facilmente até 10 domínios personalizados em um só lugar.

#### Estatísticas de funil de segmento

Selecione [View funnel statistics (Exibir estatísticas do funil]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#viewing-funnel-statistics) ) para exibir as estatísticas desse grupo de filtros e ver como cada filtro adicionado afeta as estatísticas do segmento. Você verá uma contagem estimada e uma porcentagem de usuários que são direcionados por todos os filtros até esse ponto. Depois que as estatísticas forem exibidas para um grupo de filtros, elas serão atualizadas automaticamente sempre que você alterar os filtros. 

#### Novos campos de resposta para o endpoint `/campaigns/details` para notificações push

A resposta `messages` para notificações push agora inclui dois novos campos:

- `image_url`: Um URL de imagem para uma imagem de notificação do Android, uma imagem de notificação do iOS ou uma imagem de ícone de envio pela Web.
- `large_image_url`: Um URL de imagem de notificação da Web para ações de push da Web do Android, Chrome e Windows.

#### Definição de campos de PII

Selecionar e [definir determinados campos como campos de PII]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings#view-pii) afeta apenas o que os Usuários podem visualizar no painel do Braze e não afeta a forma como os dados do Usuário Final nesses campos de PII são tratados.

Consulte sua equipe jurídica para alinhar as configurações do seu painel com as normas e políticas de privacidade aplicáveis à sua empresa, inclusive aquelas relacionadas à [retenção de dados]({{site.baseurl}}/api/data_retention/).

#### Compartilhamento de um link de download do Report Builder

Você pode [compartilhar um link do painel]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/#sharing-a-report) para o relatório selecionando **Compartilhar** e, em seguida, **Compartilhar um link** ou **Enviar ou agendar um e-mail**.

### Liberando a criatividade

#### Tags de cabeçalho personalizadas para e-mails do tipo arrastar e soltar

Use as tags `<head>` para adicionar CSS e metadados em sua mensagem de e-mail. Por exemplo, você pode usar essas tags para adicionar uma folha de estilo ou um favicon. O Liquid é compatível com as tags `<head>`.

### Canais robustos

#### Práticas recomendadas difusas

Adicionamos uma [seção de práticas recomendadas]({{site.baseurl}}) para ajudá-lo a configurar cuidadosamente sua mensagem de opt-out difusa e criar uma experiência clara, compatível e positiva para seus assinantes.

#### WhatsApp Flows

{% multi_lang_include release_type.md release="Early access" %}

[O WhatsApp Flows]({{site.baseurl}}/whatsapp_flows/) é um aprimoramento do canal existente do WhatsApp, permitindo que você crie experiências de mensagens interativas e dinâmicas. 

#### Perguntas sobre produtos recebidas pelo WhatsApp

Os usuários podem responder à mensagem do seu produto ou catálogo com [perguntas sobre o produto]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/product_messages/#receiving-inbound-product-questions). Elas chegam como mensagens de entrada, que podem ser classificadas com um Action Path.

Além disso, o Braze extrai a ID do produto e a ID do catálogo dessas perguntas, portanto, se desejar automatizar as respostas ou enviar perguntas para outra equipe (como o suporte ao cliente), você poderá incluir esses detalhes.

### Automação de IA e ML

#### Novos artigos sobre casos de uso do BrazeAI

Adicionamos novos artigos de casos de uso para ajudá-lo a obter o máximo do BrazeAI™. Esses guias destacam maneiras práticas de aplicar a IA em suas estratégias de engajamento, incluindo:

- Churn previsto Identifique os clientes em risco de rotatividade e tome medidas antecipadamente.
- Eventos previstos Antecipe as principais ações do usuário e molde as experiências em tempo real.
- [Recomendações]({{site.baseurl}}/user_guide/brazeai/recommendations/use_case ): Fornecer conteúdo e produtos mais relevantes com base no comportamento do cliente.

#### Servidor MCP

{% multi_lang_include release_type.md release="Beta" %}

O [servidor Braze MCP]({{site.baseurl}}/user_guide/brazeai/mcp_server/), uma conexão segura e somente leitura, permite que ferramentas de IA, como Claude e Cursor, acessem dados Braze sem PII para responder a perguntas, analisar tendências e fornecer insights sem alterar os dados.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Swift SDK 13.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Amplia a funcionalidade do site `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` para ser acionado em caso de erros de autenticação "Opcional".
        - O método delegado `BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError:)` agora será acionado para erros de autenticação "Required" e "Optional".
        - Se você quiser tratar apenas os erros de autenticação "Required" do SDK, adicione uma verificação para garantir que `BrazeSDKAuthError.optional` seja falso dentro da implementação desse método delegado.
    - Corrige o uso do `Braze.Configuration.sdkAuthentication` para que tenha efeito quando ativado.
        - Anteriormente, o valor dessa configuração não era consumido pelo SDK e o token era sempre anexado às solicitações, se estivesse presente.
        - Agora, o SDK só anexará o token de autenticação do SDK às solicitações de rede de saída quando essa configuração estiver ativada.
    - Os definidores de todas as propriedades de `Braze.FeatureFlag` e de todas as propriedades de `Braze.Banner` foram transformados em `private`. As propriedades dessas classes agora são somente leitura.
    - Remove a propriedade `Braze.Banner.id`, que foi descontinuada na versão `11.4.0`.
        - Em vez disso, use `Braze.Banner.trackingId` para ler o ID de rastreamento de campanha de um banner.
- [React Native SDK 16.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Atualiza as ligações da versão nativa do Android SDK do [Braze Android SDK 36.0.0 para 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualiza as ligações da versão nativa do Swift SDK do [Braze Swift SDK 12.0.0 para 13.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/12.0.0...13.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - O evento `sdkAuthenticationError` agora será acionado para erros de autenticação "Required" e "Optional".
- [Xamarin SDK 7.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/7.0.0/CHANGELOG.md)
    - Adição de suporte ao .NET 9.0 para os vínculos com iOS e Android.
        - Isso remove o suporte ao .NET 8.0.
        - Isso requer uma [versão mínima do iOS 12.2](https://learn.microsoft.com/en-us/dotnet/maui/whats-new/dotnet-9?view=net-maui-9.0).
    - Atualização da vinculação do Android do [Braze Android 32.0.0 para 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v32.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizada a vinculação do iOS de [SDK Swift da Braze 10.0.0 para o 12.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.0.0...12.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Esta versão contém APIs para o recurso Banners, mas atualmente não é totalmente compatível com este SDK. Se desejar usar Banners em seu aplicativo .NET MAUI, entre em contato com o gerente de suporte ao cliente antes de integrá-lo ao aplicativo.
- [SDK do Cordova 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Atualizada a implementação interna do método `enableSdk` no iOS para usar `setEnabled`: em vez de `_requestEnableSDKOnNextAppRun`, que foi preterido no Swift SDK.
    - A chamada desse método não exige mais que o aplicativo seja reiniciado para ter efeito. O SDK será ativado assim que esse método for executado.
    - Atualizamos a ponte Android nativa do [Braze Android SDK `36.0.0` para `37.0.0`](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

{% enddetails %}
{% details July 22, 2025 %}

## Liberação em 22 de julho de 2025

### Exportação de eventos de segurança com o Amazon S3

Você pode [exportar]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/) automaticamente [os Security Events para o Amazon S3]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/security_export_s3/), um provedor de armazenamento em nuvem, com um trabalho diário que é executado à meia-noite UTC. Uma vez configurado, você não precisa exportar manualmente os Security Events do painel.

### Flexibilidade de dados

#### importação de CSV

{% multi_lang_include release_type.md release="General availability" %}

Você pode usar a importação de CSV para registrar e atualizar atributos de usuário e eventos personalizados no Braze, como `first_name`, `last_destination_searched` e `trip_booked`. Para começar, consulte [Importação de CSV]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/csv_import).

#### Alertas de uso da API

{% multi_lang_include release_type.md release="General availability" %}

Os alertas de uso da API fornecem visibilidade crítica do uso da API, permitindo que você detecte proativamente o tráfego inesperado. Ao configurar esses alertas para rastrear os principais volumes de solicitações de API, você pode receber notificações em tempo real e resolver problemas antes que eles afetem suas campanhas de marketing.

#### Limites de taxa da API do espaço de trabalho

Com os limites de taxa de API do workspace, você pode definir um número máximo de solicitações de API que um workspace pode fazer para um endpoint de ingestão específico, como dados do `/users/track` ou do SDK. Você também pode aplicar limites de taxa a um grupo de espaços de trabalho, o que significa que o limite é compartilhado por todos os espaços de trabalho desse grupo.

#### Novos eventos do Currents

Esses novos eventos foram adicionados ao glossário do Currents:

- [Eventos de abortamento de banner]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-abort-events)
- [Eventos de clique no banner]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-click-events)
- [Eventos de impressão de banner]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-impression-events)
- [Banner Eventos visualizados]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#banner-viewed-events)
- [Eventos de falha do webhook]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/#webhook-failure-events)

#### Intervalo de tempo padrão para análise de campanha

Por padrão, o intervalo de tempo do [**Análise de campanhas**]({{site.baseurl}}/user_guide/analytics/reporting/campaign_analytics/) exibirá os últimos 90 dias a partir da hora atual. Isso significa que, se a campanha tiver sido lançada há mais de 90 dias, a análise será exibida como "0" para o intervalo de tempo determinado. Para visualizar todas as análises de campanhas mais antigas, ajuste o intervalo de tempo do relatório.

#### Comportamento atualizado para a etapa Canvas Experiment Paths

Se o seu Canvas tiver um [experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) ativo ou em andamento e você atualizar o Canvas ativo (mesmo que não seja na etapa Caminho do experimento), o experimento em andamento será encerrado. Para reiniciar o experimento, você pode desconectar o Caminho do Experimento existente e iniciar um novo, ou duplicar o Canvas e iniciar um novo Canvas. 

Para saber mais, consulte [Editar canvas após o lançamento]({{site.baseurl}}/post-launch_edits/).

#### Limite de taxa mais rápido disponível para o endpoint `/users/export/ids` 

Você também pode aumentar [o limite de taxa do ponto de extremidade /users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/#rate-limit) para 40 solicitações por segundo, atendendo aos seguintes requisitos:

- Seu espaço de trabalho tem o limite de taxa padrão (250 solicitações por minuto) ativado. Entre em contato com o gerente da sua conta Braze para obter mais assistência na remoção de qualquer limite de tarifa pré-existente que você possa ter.
- Sua solicitação inclui o parâmetro fields_to_export para listar todos os campos que você deseja receber.

#### Nova tradução para endpoints de modelos de e-mail

{% multi_lang_include release_type.md release="Early access" %}

Use esses pontos de extremidade para visualizar e fazer atualizações nas traduções e localidades dos modelos de e-mail:

- [GET: Veja as traduções originais]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_source_template)
- [GET: Exibir uma tradução e localidade específicas para o ponto de extremidade do modelo de e-mail]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_locale_template)
- [GET: Exibir todas as traduções e localidades de um modelo de e-mail]({{site.baseurl}}/api/endpoints/translations/email_templates/get_view_translation_template)
- [PUT: Atualizar traduções para um modelo de e-mail]({{site.baseurl}}/api/endpoints/translations/email_templates/put_update_template)

### Liberando a criatividade

#### Landing pages

Você pode tornar sua página de destino [responsiva ao tamanho do dispositivo do usuário]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages#step-3-customize-the-page) empilhando colunas verticalmente em telas menores. Para ativar isso, adicione uma coluna à linha que deseja tornar responsiva e, em seguida, ative a opção **Empilhar verticalmente em telas menores** na seção **Personalizar colunas**.

### Canais robustos

#### Filtragem de bots para e-mails

{% multi_lang_include release_type.md release="General availability" %}

Configure a filtragem de bots em suas [Preferências de e-mail]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings) para excluir todos os cliques suspeitos de máquinas ou bots. Um "clique de bot" em e-mail refere-se a um clique em hiperlinks em um e-mail gerado por um programa automatizado. Ao filtrar esses cliques de bots, você pode acionar intencionalmente e enviar mensagens para destinatários que estejam engajados.

#### Blocos de produtos do tipo arrastar e soltar

{% multi_lang_include release_type.md release="Early access" %}

O [editor de arrastar e soltar]({{site.baseurl}}/dnd_product_blocks/) permite que você adicione e configure rapidamente blocos de produtos às suas mensagens para exibir produtos sem interrupções, sem a necessidade de criar código Liquid personalizado. No momento, o recurso de arrastar e soltar blocos de produtos está disponível apenas para e-mail.

#### Texto abrangente para páginas de destino e mensagens no aplicativo

O Span text permite que você aplique um estilo específico a blocos de texto sem código personalizado para suas [páginas de destino]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/#step-3-customize-the-page) e [mensagens no aplicativo]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/style_settings/#blocks). Para isso, realce o texto que você deseja estilizar e selecione **Wrap with span como estilo**. 

#### Clique no anúncio para WhatsApp

[Os anúncios que clicam no WhatsApp]({{site.baseurl}}/whatsapp_use_cases/) são uma maneira eficiente de atrair clientes novos e existentes a partir de anúncios do Meta no Facebook, Instagram ou outras plataformas. Use esses anúncios para promover seus produtos e serviços e, ao mesmo tempo, conscientizar os usuários sobre sua presença no WhatsApp. 

### Novas parcerias Braze

#### API de visitação do Shopify - Comércio eletrônico

A Braze coleta informações dos visitantes, como endereços de e-mail e números de telefone, por meio de mensagens no navegador. Essas informações são então enviadas para a Shopify. Esses dados ajudam os comerciantes a reconhecer os visitantes de suas lojas e a criar uma experiência de compra mais personalizada.

#### Okendo - Comércio eletrônico

A integração entre a Braze e [a Okendo]({{site.baseurl}}/partners/okendo/) funciona em vários produtos da plataforma da Okendo, incluindo avaliações, fidelidade, indicações, pesquisas e questionários. O Okendo envia eventos personalizados e atributos do usuário para o Braze, que podem ser usados para personalizar e acionar mensagens.

#### Lemnisk - Plataforma de dados do cliente

A integração entre a Braze e [a Lemnisk]({{site.baseurl}}/partners/lemnisk/) permite que as marcas e as empresas aproveitem todo o potencial da Braze, atuando como uma camada de inteligência liderada pelo CDP que unifica os dados do usuário em todas as plataformas em tempo real e envia as informações e os comportamentos do usuário coletados para a Braze em tempo real.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Web SDK 6.0.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
    - Removidos a propriedade `Banner.html`, os métodos `logBannerClick` e `logBannerImpressions`. Em vez disso, use o [`insertBanner`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#insertbanner) que gerencia automaticamente o rastreamento de impressões e cliques.
    - Removido o suporte ao recurso legado do Feed de notícias. Isso inclui a remoção da classe Feed e de seus métodos associados.
    - Os campos criados e categorias que eram usados pelos cartões legados do Feed de notícias foram removidos das [`Card`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.card.html) subclasses.
    - O campo linkText também foi removido da subclasse [`ImageOnly`](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.imageonly.html) Card e de seu construtor.
    - Definições esclarecidas e tipos atualizados para observar que determinados métodos do SDK retornam explicitamente indefinidos quando o SDK não é inicializado, alinhando as tipagens com o comportamento real do tempo de execução. Isso poderia introduzir novos erros de TypeScript em projetos que dependiam das tipagens anteriores (incompletas).
    - As imagens de mensagens no aplicativo com `cropType` de `CENTER_CROP` (como `FullScreenMessage` por padrão) agora são renderizadas por meio de uma tag `<img>` em vez de `<span>` para melhorar a acessibilidade. Isso pode interromper as personalizações de CSS existentes para a classe `.ab-center-cropped-img` ou seus filhos.
- [SDK do Cordova 13.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1300)
    - Atualizada a implementação interna do iOS do método `enableSdk` para usar setEnabled: em vez de `_requestEnableSDKOnNextAppRun`, que foi preterido no Swift SDK.
        - A chamada desse método não exige mais que o aplicativo seja reiniciado para ter efeito. O SDK será ativado assim que esse método for executado.
    - Atualizamos a ponte nativa do Android do [SDK da Braze para Android 36.0.0 para o 37.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v36.0.0...v37.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Android SDK 37.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 12.0.1-12.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)

{% enddetails %}
{% details June 24, 2025 %}

## Liberação em 24 de junho de 2025

### BrazeAI Decisioning Studio™

[O BrazeAI Decisioning Studio™](https://www.braze.com/product/brazeai-decisioning-studio/) substitui os testes A/B por decisões de IA que personalizam tudo e maximizam qualquer métrica: gere dólares, não cliques - com o BrazeAI Decisioning Studio™, você pode otimizar qualquer KPI de negócios. Consulte a nossa seção dedicada [BrazeAI Decisioning Studio™]({{site.baseurl}}/user_guide/brazeai/decisioning_studio) para ver exemplos de casos de uso e os principais recursos.

### Novos tutoriais do SDK

Cada tutorial do Braze SDK oferece instruções passo a passo, juntamente com um código de amostra completo. Escolha um tutorial abaixo para começar:

- [Exibição de banners]({{site.baseurl}}/developer_guide/banners/tutorial_displaying_banners)
- [Personalização do estilo de mensagens no aplicativo]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/customizing_message_styling)
- [Exibição condicional de mensagens no aplicativo]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/conditionally_displaying_messages)
- [Adiamento de mensagens in-app acionadas]({{site.baseurl}}/developer_guide/in_app_messages/tutorials/deferring_triggered_messages)

### Flexibilidade de dados

#### Provisionamento SAML just-in-time

{% multi_lang_include release_type.md release="General availability" %}

Use [o provisionamento SAML just-in-time]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit) para permitir que os novos usuários do painel criem uma conta Braze em seu primeiro login. Isso elimina a necessidade de os administradores criarem manualmente uma conta para um novo usuário do dashboard, escolherem suas permissões, atribuírem a ele um espaço de trabalho e esperarem que ele ative sua conta.

#### Filtros por seleção

Agora você pode adicionar até 10 filtros por [seleção]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections).

#### Armazenamento do catálogo

O tamanho do armazenamento da versão gratuita dos catálogos é de até 100 MB. Você pode ter itens ilimitados, desde que eles tenham menos de 100 MB.

#### Número de linhas sincronizadas com o Cloud Data Ingestion

Por padrão, para a ingestão de dados na nuvem, cada execução pode sincronizar até 500 milhões de linhas. Todas as sincronizações com mais de 500 milhões de novas linhas serão interrompidas.

Consulte as [limitações do produto Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/cloud_ingestion/overview/#product-limitations) para obter mais detalhes.

### Canais robustos

#### Teste de acessibilidade no Inbox Vision

{% multi_lang_include release_type.md release="General availability" %}

Use o [teste de acessibilidade]({{site.baseurl}}/user_guide/message_building_by_channel/email/inbox_vision/#accessibility-testing) no Inbox Vision para destacar os problemas de acessibilidade que podem existir em seu e-mail. 

O teste de acessibilidade analisa o conteúdo de seu e-mail em relação a alguns requisitos AA das [Diretrizes de Acessibilidade de Conteúdo da Web](https://www.w3.org/WAI/standards-guidelines/wcag/) (WCAG) 2.2. Isso pode fornecer informações sobre quais elementos não estão atendendo aos padrões de acessibilidade.

#### Rastreamento de cliques para o WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

Você pode ativar [o rastreamento de cliques]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking) nas mensagens de resposta e de modelo para ver os dados de cliques nos relatórios de desempenho do WhatsApp e poder segmentar os usuários com base em quem clicou em quê.

#### Vídeos para WhatsApp

{% multi_lang_include release_type.md release="General availability" %}

Você pode [incorporar vídeos]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create/#supported-whatsapp-features) no corpo do texto das mensagens enviadas pelo WhatsApp. Esses arquivos devem ser hospedados por meio de URL ou na [biblioteca de mídia do Braze]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library).

### Novas parcerias Braze

#### Stripe - Comércio eletrônico

A integração entre o Braze e o [Stripe]({{site.baseurl}}/partners/stripe) permite que você acione mensagens no Braze com base em eventos do Stripe, como avaliação iniciada, assinatura ativada, cancelamento de assinatura e muito mais.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [React Native SDK 15.0.1](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.1-14.0.2](https://pub.dev/packages/braze_plugin/changelog)
- [SDK do Cordova 12.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1200)
    - Atualizamos a ponte nativa do Android do [SDK da Braze para Android 35.0.0 para o 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizamos a ponte nativa do iOS do [SDK Swift da Braze 11.6.1 para o 12.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/11.6.1...12.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Segmento Kotlin 4.0.0-4.0.1](https://github.com/braze-inc/braze-segment-kotlin/blob/4.0.0/CHANGELOG.md#400)
    - Atualização do Braze Android SDK [de 35.0.0 para 36.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v35.0.0...v36.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed)

{% enddetails %}
{% details May 27, 2025 %}

## Liberação em 27 de maio de 2025

### Flexibilidade de dados

#### Cópia de telas entre espaços de trabalho

{% multi_lang_include release_type.md release="General availability" %}

Agora você pode copiar Canvases entre espaços de trabalho. Isso permite que você inicie a composição da sua mensagem começando com uma cópia de um Canvas em um espaço de trabalho diferente. Para obter mais informações sobre o que é copiado, consulte [Cópia de campanhas e telas entre espaços de trabalho]({{site.baseurl}}/copying_to_workspaces/).

#### Regras de mensagens para o fluxo de trabalho de aprovação 

{% multi_lang_include release_type.md release="General availability" %}

Use [regras de mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/approvals/messaging_rules) em seu fluxo de trabalho de aprovação para limitar o número de usuários alcançáveis antes que seja necessária uma aprovação adicional - dessa forma, você pode revisar suas campanhas e Canvases antes de atingir um público maior.

#### Diagramas de relacionamento de entidades para Snowflake e Braze

No início deste ano, criamos tabelas de relacionamento de entidades para dados compartilhados entre o Snowflake e o Braze. Este mês, adicionamos [novos diagramas interativos]({{site.baseurl}}/partners/data_and_analytics/data_warehouses/snowflake/entity_relationships/), nos quais você pode se deslocar, agarrar e ampliar os detalhes de cada tabela, dando-lhe uma ideia melhor de como seus dados interagem com o Braze.

### Liberando a criatividade

#### Eventos recomendados

{% multi_lang_include release_type.md release="Early access" %}

[Os eventos recomendados]({{site.baseurl}}/user_guide/data/custom_data/recommended_events) são mapeados para os casos de uso mais comuns de comércio eletrônico. Ao usar os eventos recomendados, você pode desbloquear modelos pré-construídos do Canvas, painéis de relatórios que mapeiam o ciclo de vida do cliente e muito mais.

### Canais robustos

#### Canal de banners

{% multi_lang_include release_type.md release="General availability" %}

Com os [Banners]({{site.baseurl}}/user_guide/message_building_by_channel/banners), você pode criar mensagens personalizadas para seus usuários, ao mesmo tempo em que amplia o alcance de seus outros canais, como e-mail ou notificações push. Você pode incorporar Banners diretamente no seu aplicativo ou site, o que lhe permite interagir com os usuários por meio de uma experiência que parece natural.

#### Canal de serviços de comunicação avançada (RCS)

{% multi_lang_include release_type.md release="General availability" %}

[Os Rich Communication Services (RCS)]({{site.baseurl}}/about_rcs/) aprimoram o SMS tradicional, permitindo que as marcas enviem mensagens não apenas informativas, mas também muito mais envolventes. Agora com suporte para Android e iOS, o RCS traz recursos como mídia de alta qualidade, botões interativos e perfis de remetente com marca diretamente para os aplicativos de mensagens pré-instalados dos usuários, eliminando a necessidade de baixar um aplicativo separado.

#### Página Configurações de envio

{% multi_lang_include release_type.md release="General availability" %}

Use a [página**Push Settings (Configurações de push**]({{site.baseurl}}/user_guide/administrative/app_settings/push_settings) ) para definir as principais configurações de suas notificações push, incluindo o Push Time to Live (TTL) e a prioridade FCM padrão para campanhas do Android. Essas configurações ajudam a otimizar a entrega e a eficácia das suas notificações por push, garantindo uma melhor experiência para os usuários.

#### Códigos promocionais para campanhas de mensagens in-app

{% multi_lang_include release_type.md release="Early access" %}

Você pode usar [códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes) em campanhas de mensagens in-app inserindo um [snippet de lista de códigos promocionais]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes#creating-a-promotion-code-list) no corpo da mensagem da sua campanha de mensagens in-app.

#### Tratamento de erros de webhook e limitação de taxa

[Sobre webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/understanding_webhooks/#webhook-error-handling-and-rate-limiting) tem uma nova seção que descreve como o Braze lida com erros de webhook e limitação de taxa.

#### Locais de mensagens no aplicativo

Depois de [adicionar localidades]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/using_locales) ao seu espaço de trabalho, você pode segmentar usuários em diferentes idiomas em uma única mensagem in-app.

#### Amazon SES como um provedor de envio de e-mail (ESP)

Agora você pode usar o Amazon SES como um ESP, da mesma forma que usaria o SendGrid e o SparkPost. Consulte [SSL no Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ssl#what-is-a-cdn-and-why-do-i-need-it) e [Universal Links e App Links]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) para conhecer as nuances da configuração de SSL e do rastreamento de cliques em uma base de link a link.

### Novas parcerias Braze

#### Eagle Eye - Lealdade

A integração bidirecional entre a Braze e [a Eagle Eye]({{site.baseurl}}/partners/eagle_eye/) permite que você ative dados promocionais e de fidelidade diretamente na Braze, permitindo que os profissionais de marketing personalizem o envolvimento do cliente usando dados em tempo real, como saldos de pontos, promoções e atividades de recompensa.

#### Eppo - Testes A/B

A integração entre o Braze e [o Eppo]({{site.baseurl}}/partners/eppo/) permite que você configure testes A/B no Braze e analise os resultados no Eppo para descobrir insights e vincular o desempenho da mensagem a métricas comerciais de longo prazo, como receita ou retenção.

#### Mencione-me - Indicações

Juntos, [o Mention Me](https://www.mention-me.com/) e o Braze podem ser sua porta de entrada para atrair clientes premium e promover uma fidelidade inabalável à marca. Ao integrar perfeitamente os dados de referência primários ao Braze, você pode oferecer experiências omnichannel altamente personalizadas direcionadas aos fãs da sua marca. Para começar, consulte [Technology Partners: Mencione-me]({{site.baseurl}}/partners/mention_me).

#### Shopify - Ecommerce

[Conecte vários domínios de lojas da Shopify]({{site.baseurl}}/shopify_connecting_multiple_stores/) a um único espaço de trabalho para ter uma visão holística de seus clientes em todos os mercados. Crie e lance programas e jornadas de automação em um único espaço de trabalho sem duplicar esforços em lojas regionais.

### Outro

#### Atualização para a criação de mensagens acessíveis no Braze

Atualizamos nosso artigo [Criando mensagens acessíveis no Braze]({{site.baseurl}}/help/accessibility/) com orientações mais claras e prescritivas sobre a criação de mensagens acessíveis. Esse artigo agora inclui práticas recomendadas expandidas para estrutura de conteúdo, texto alternativo, botões e contraste de cores, além de uma nova seção sobre o tratamento de ARIA para mensagens HTML personalizadas. 

Essa atualização faz parte de nosso esforço mais amplo para oferecer suporte a experiências de mensagens mais acessíveis no Braze. Sabemos que a acessibilidade é uma área em evolução e continuaremos compartilhando o que aprendermos.

{% multi_lang_include accessibility/feedback.md %}

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 36.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Esta versão reverte o aumento da versão mínima do Android SDK do Braze Android SDK de API 21 para API 25 introduzido na versão 34.0.0. Isso permite que o SDK seja novamente compilado em aplicativos compatíveis já com a API 21. Observe que, embora estejamos reintroduzindo a capacidade de compilação, não estamos reintroduzindo o suporte formal para a API 25 do < e não podemos garantir que o SDK funcionará como pretendido nos dispositivos que executam essas versões.
    - Se o seu aplicativo for compatível com essas versões, você deverá fazê-lo:
        - Valide se sua integração do SDK funciona como pretendido em dispositivos físicos (não apenas emuladores) para essas versões de API.
        - Se não for possível validar o comportamento esperado, você deverá chamar [disableSDK](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze/-companion/disable-sdk.html) ou não inicializar o SDK nessas versões. Caso contrário, poderá causar efeitos colaterais não intencionais ou degradar o desempenho dos dispositivos dos usuários finais.
    - Foi corrigido um problema em que as mensagens no aplicativo causavam uma leitura no thread principal.
    `BrazeInAppMessageManager.displayInAppMessage` agora é uma função de suspensão do Kotlin.
        - Se você não chamar essa função diretamente, não precisará fazer nenhuma alteração.
    - BOM do AndroidX Compose atualizado para 2025.04.01 para lidar com atualizações nas APIs do Jetpack Compose.
- [React Native SDK 15.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Atualiza a ponte nativa do Android do Braze Android SDK 35.0.0 para o 36.0.0
    - Atualiza as ligações da versão nativa do iOS do Braze Swift SDK 11.9.0 para 12.0.0.
    - Atualiza a representação da unidade de PushNotificationEvent.timestamp para milissegundos no iOS.
        - Anteriormente, esse valor era representado em segundos no iOS. Isso agora corresponderá à implementação existente do Android.
- [Web SDK 5.9.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- [Flutter SDK 14.0.0 5.9.0](https://pub.dev/packages/braze_plugin/changelog)
    - Esta versão reverte o aumento da versão mínima do Android SDK do Braze Android SDK de API 21 para API 25 introduzido na versão 34.0.0. Isso permite que o SDK seja novamente compilado em aplicativos compatíveis já com a API 21. No entanto, não estamos reintroduzindo o suporte formal para < API 25. Leia mais aqui.
    - Atualiza a ponte nativa do Android do Braze Android SDK 35.0.0 para o 36.0.0
    - Atualiza a ponte nativa do iOS do Braze Swift SDK 11.9.0 para o 12.0.0

{% enddetails %}
