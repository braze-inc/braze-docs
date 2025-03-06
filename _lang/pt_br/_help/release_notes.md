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
    link: /docs/developer_guide/platform_integration_guides/sdk_changelogs/
    image: /assets/img/braze_icons/file-code-01.svg

---

# Notas de versão mais recentes da Braze {#most-recent}

> O Braze divulga informações sobre atualizações de produtos em uma cadência mensal, alinhando-se com os principais lançamentos de produtos, embora o produto seja atualizado com melhorias diversas semana a semana.
> <br>
> <br>
> Para saber mais sobre qualquer uma das atualizações listadas nesta seção, entre em contato com o gerente da sua conta ou [abra um ticket de suporte]({{site.baseurl}}/help/support/). Você também pode conferir [nossos Changelogs do SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_changelogs/) para ver mais informações sobre nossos lançamentos, atualizações e aprimoramentos mensais do SDK.

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

#### Narvar - Comércio eletrônico

A integração Braze e [Narvar](https://corp.narvar.com/) ativa as marcas para aproveitar os eventos de notificação do Narvar para disparar mensagens diretamente do Braze, mantendo os clientes informados com atualizações oportunas.

#### Zeotap para Currents - Plataforma de dados do cliente

A integração entre o Braze e o [Zeotap](https://zeotap.com/) permite que você amplie a escala e o alcance de suas campanhas, sincronizando os segmentos de clientes do Zeotap com os perfis de usuários do Braze. Com o [Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/), você também pode conectar dados ao Zeotap para torná-los acionáveis em todo o growth stack.

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

## Liberação em 12 de novembro de 2024
 
### Flexibilidade de dados
 
#### Limite de velocidade para `/users/track`

O limite de velocidade do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) foi atualizado para 3.000 por 3 segundos.
 
### Liberando a criatividade

#### Casos de uso do Canva

Reunimos alguns casos de uso que mostram as diferentes maneiras pelas quais você pode usar um Braze Canvas. Se estiver buscando inspiração, escolha um caso de uso abaixo para começar.

- [Carrinho abandonado]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [De volta ao estoque]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [Adoção de Recursos]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [Usuários inativos]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [Onboarding]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [Feedback pós-compra]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### Canais robustos

#### LINE

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

A integração do Braze com o LINE já está disponível para todos! O LINE é o aplicativo de envio de mensagens mais popular do Japão, com mais de 95 milhões de usuários ativos mensais. Além do envio de mensagens, o LINE oferece a seus usuários uma plataforma "tudo em um" para redes sociais, jogos, compras e pagamentos.

Para começar, consulte nossa [documentação do LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/).
 
#### LinkedIn Audience Sync

{% multi_lang_include release_type.md release="Beta" %}

Agora você pode usar o LinkedIn com o [Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps/), uma ferramenta que o ajuda a ampliar o alcance de suas campanhas para muitas das principais tecnologias sociais e públicas. Para participar da versão beta, entre em contato com seu gerente de sucesso do Braze.
 
### Aprimoramento do guia do desenvolvedor
 
Estamos no processo de fazer grandes melhorias no [Guia do Desenvolvedor Braze]({{site.baseurl}}/developer_guide/home/). Como primeira etapa, simplificamos a navegação e reduzimos o número de seções aninhadas. 

|Antes|Após|
|------|-----|
|!["A navegação antiga para o Guia do Desenvolvedor Braze."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["A nova navegação do Guia do Desenvolvedor Braze."]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### Novas parcerias Braze
 
#### MyPostcard

O [MyPostcard](https://www.mypostcard.com/), um app líder global de cartões postais, permite que você execute campanhas de mala direta com facilidade, proporcionando uma maneira perfeita e lucrativa de se conectar com seus clientes. Para começar, consulte [Integração do MyPostcard com o Braze]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/).
 
### Atualizações do SDK
 
As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.
 
- [Plug-in Expo 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - Esta versão requer a versão 13.1.0 do SDK React Native do Braze.
    - Substitui a chamada do método iOS BrazeAppDelegate de BrazeReactUtils.populateInitialUrl por BrazeReactUtils.populateInitialPayload.
        - Esta atualização resolve um problema em que os eventos abertos por push não eram disparados ao clicar em uma notificação enquanto o aplicativo estava em um estado finalizado.
        - Para aproveitar totalmente essa atualização, substitua todas as chamadas de Braze.getInitialURL por Braze.getInitialPushPayload em seu código JavaScript. A URL inicial agora pode ser acessada por meio da propriedade url da carga útil inicial do push.
- [Plug-in Swift do Braze Segment 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Atualiza as ligações do Braze Swift SDK para exigir versões a partir da denominação 11.1.1+ SemVer.
    - Isso permite a compatibilidade com qualquer versão do Braze SDK, desde a 11.1.1 até a 12.0.0, mas não incluindo essa versão.
    - Consulte a entrada do changelog da versão 11.1.1 para obter mais informações sobre possíveis mudanças significativas.

## Liberação em 15 de outubro de 2024

### Flexibilidade de dados

#### Campanhas e canvas

Ao criar campanhas e Canvas, é possível calcular o número exato de usuários alcançáveis em seu público-alvo, em vez da estimativa padrão, selecionando [Calcular estatísticas exatas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size).

#### Objetos Android da API

O [parâmetro `android_priority` ]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) aceitará valores "normal" ou "high" para especificar a prioridade do remetente FCM. Por padrão, as mensagens de notificação são enviadas com prioridade alta e as mensagens de dados são enviadas com prioridade normal.

Para saber mais sobre como os diferentes valores afetam a entrega, consulte [Prioridade de mensagens do Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority/).

#### SDK

Use o [depurador integrado do Braze SDK]({{site.baseurl}}/developer_guide/platform_wide/debugging/) para solucionar problemas dos seus canais com SDK sem precisar ativar o registro detalhado no seu aplicativo.

#### Atividades ao vivo

Atualizamos as [perguntas frequentes]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) sobre o Swift Live Activities com algumas perguntas e respostas novas.

#### Eventos personalizados

Os [objetos de propriedade de evento]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) que contêm valores de vetor ou objeto agora podem ter uma carga útil de propriedade de evento de até 100 KB.

#### Números aleatórios de baldes

Use a [reentrada aleatória de público com números de balde aleatórios]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) para Testes A/B ou direcionamento de grupos de usuários específicos em suas campanhas.

#### Extensões de segmento

É possível [atualizar as extensões de segmento em uma agenda recorrente]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh) selecionando a frequência com que as extensões serão atualizadas (diariamente, semanalmente ou mensalmente) e o horário específico em que a atualização ocorrerá.

### Canais robustos

#### SMS

Adicionamos [Adding UTM parameters]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) para demonstrar como você pode usar parâmetros UTM em uma mensagem SMS, para que você rastreie o desempenho das campanhas em ferramentas de análise de dados de terceiros, como o Google Analytics.

#### Landing pages

[Conecte seu próprio domínio]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/connect_domain/) ao espaço de trabalho do Braze para personalizar os URLs da landing page com sua marca.

#### LINE e Braze

{% multi_lang_include release_type.md release="Beta" %}

Adicionamos nova documentação:

- [Tipos de mensagens do LINE]({{site.baseurl}}/line/create/message_types/) abrange os tipos de mensagens do LINE que você pode criar, incluindo aspectos e limitações, e faz parte da coleção beta do LINE.
- A [vinculação de contas de usuário]({{site.baseurl}}/line/line_setup/#user-account-linking) permite que os usuários vinculem suas contas LINE à conta de usuário do seu app. Em seguida, é possível usar o Liquid no Braze, como {% raw %}`{{line_id}}`{% endraw %}, para criar um URL personalizado para o usuário que passa o LINE ID do usuário de volta para o seu site ou app, que pode então ser associado a um usuário conhecido.

#### WhatsApp e Braze

As [ contas do WhatsApp Business (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) agora podem ser compartilhadas com vários provedores de soluções empresariais.

### Novas parcerias Braze

#### Future Anthem - Conteúdo dinâmico

A parceria entre a Braze e a [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) utiliza o Amplifier IA para oferecer personalização de conteúdo, experiências em tempo real e públicos dinâmicos. O Amplifier IA funciona em esportes, cassinos e loterias, permitindo que você aprimore os perfis de jogadores do Braze com atribuições específicas do setor, como jogo favorito, pontuação de engajamento, próxima aposta esperada e muito mais.

### Configurações

#### Criptografia em nível de campo do identificador

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Usando a [ criptografia no nível do campo do identificador]({{site.baseurl}}/user_guide/data_and_analytics/field_level_encryption/), é possível criptografar perfeitamente os endereços de e-mail com o AWS Key Management Service (KMS) para minimizar as informações de identificação pessoal (IPI) compartilhadas no Braze. A criptografia substitui dados confidenciais por texto cifrado, que é uma informação criptografada ilegível.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Swift SDK 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Swift SDK 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Adiciona suporte à [verificação de simultaneidade estrita do Swift 6](https://developer.apple.com/documentation/swift/adoptingswift6)
        - As classes e os tipos de dados públicos relevantes do Braze agora estão em conformidade com o protocolo `Sendable` e podem ser usados com segurança em contextos de simultaneidade.
        - As APIs principais somente de thread agora são marcadas com o atributo `@MainActor`.
        - Recomendamos o uso do Xcode 16.0 ou posterior para aproveitar esses recursos e, ao mesmo tempo, minimizar o número de avisos gerados pelo compilador. As versões anteriores do Xcode ainda podem ser usadas, mas alguns recursos podem gerar avisos.
    - Ao integrar manualmente o suporte a notificações por push, talvez seja necessário atualizar a conformidade com `UNUserNotificationCenterDelegate` para usar a atribuição `@preconcurrency` a fim de evitar avisos.
        - A aplicação da atribuição `@preconcurrency` na conformidade do protocolo só está disponível no Xcode 16.0 ou posterior. Consulte nosso código de integração de amostra [aqui](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual).
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - Atualiza as ligações da versão nativa do Android do [Braze Android SDK 31.1.0 para 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualiza as ligações da versão nativa do iOS do [Braze Swift SDK 10.3.0 para 11.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [Swift SDK 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Android SDK 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Atualização do Kotlin de 1.8 para Kotlin 2.0.
- [Web SDK 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## Liberação em 17 de setembro de 2024

### Flexibilidade de dados

#### Ingestão de dados do Braze Cloud para S3

Você pode usar o [Cloud Data Ingestion (CDI) para S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) para integrar diretamente um ou mais buckets S3 em sua conta da AWS com o Braze. Quando novos arquivos são publicados no S3, uma mensagem é postada no SQS, e a Ingestão de dados para a nuvem da Braze recebe esses novos arquivos.

#### Usuários ativos mensais CY 24-25

Para os clientes que adquiriram o Monthly Active Users - CY 24-25, o Braze gerencia diferentes limites de frequência em seu endpoint `/users/track`. Para obter detalhes, consulte [POST: Rastreamento de usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### Liberando a criatividade

#### Modelo de itens de catálogo, incluindo Liquid

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Use o sinalizador `:rerender` em uma tag Liquid para [renderizar o conteúdo Liquid de um item do catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). Por exemplo, se você renderizar o seguinte conteúdo Liquid:

{% raw %}
```liquid
Hi ${first_name}
{% catalog_items Messages greet_msg :rerender %}
{{ items[0].Welcome_Message }}
```
{% endraw %}

Isso será exibido da seguinte forma:

{% raw %}
```
Hi Peter,
Welcome to our store, Peter!
```
{% endraw %}

### Canais robustos

#### Envio de mensagens de resposta do WhatsApp

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

É possível usar [mensagens de resposta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) para responder às mensagens recebidas do WhatsApp de seus usuários. Essas mensagens são criadas no app do Braze durante sua experiência de composição e podem ser editadas a qualquer momento. É possível usar o Liquid para fazer a correspondência entre o idioma da mensagem de resposta e os usuários apropriados.

#### Modelos de canva

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Crie [modelos de Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/) para refinar o envio de mensagens, criando uma estrutura consistente que pode ser facilmente personalizada para atender às suas metas específicas em todos os Canvas.

#### Landing pages

{% multi_lang_include release_type.md release="Beta" %}

As [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) do Braze são páginas da Web independentes que podem impulsionar sua estratégia de aquisição e engajamento de usuários.

#### Alterações desde a última visualização

É possível visualizar o número de atualizações feitas em suas [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), campanhas e [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) por outros membros de sua equipe consultando a métrica *Alterações desde a última visualização* nas respectivas páginas de visão geral (como a página de visão geral de uma [campanha de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)). 

#### Solução de problemas de solicitações de webhook e Connected Content 

[Este artigo]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) aborda como solucionar problemas de códigos de erro do webhook e do Connected Content, incluindo quais são os erros e as etapas para resolvê-los.

### Novas parcerias Braze

#### Inbox Monster - Análise de dados

A [Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) é uma plataforma de sinalização de caixa de entrada que ajuda as marcas corporativas a obterem sucesso em cada envio. Trata-se de um conjunto integrado de soluções para entregabilidade, renderização criativa e monitoramento de SMS, que capacita as equipes modernas de gestão de relacionamento com o cliente (CRM) e acaba com os sustos do envio.

#### SessãoM - Fidelidade

A [SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) é uma plataforma de engajamento com clientes e fidelidade que oferece recursos de gerenciamento de campanhas e soluções de gerenciamento de fidelidade para ajudar os profissionais de marketing a impulsionar o direcionamento para aumentar o engajamento e a lucratividade.

### Automação de IA e ML

#### Recomendações de itens de tendência

Além do modelo "IA Personalizado", o recurso de [recomendações de itens de IA]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) também inclui um modelo de recomendação para "Tendências", que apresenta itens que tiveram o impulso mais positivo quando se trata de interações recentes do usuário.

### Configurações

#### Funções

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

As [funções]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) permitem mais estrutura ao agrupar suas permissões personalizadas individuais com controles de acesso ao espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um dashboard. Com funções, você pode adicionar usuários do dashboard aos espaços de trabalho certos e conceder diretamente as permissões associadas. 

#### Relatório de eventos de segurança

Adicionamos uma lista completa dos [eventos de segurança]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) que podem aparecer em seu evento de relatório de segurança baixado.

#### Relatório de uso de mensagens

{% multi_lang_include release_type.md release="Acesso antecipado" %}

O [dashboard de uso de mensagens]({{site.baseurl}}/message_usage/) fornece insights de autoatendimento sobre o uso de créditos de SMS e WhatsApp para uma visão abrangente do uso histórico e atual em comparação com as atribuições do contrato. Essas percepções podem reduzir sua confusão e ajudá-lo a fazer ajustes para prevenir riscos de excedente.

### SDK

#### Postergação da inicialização do Braze Swift SDK

Configure a [inicialização postergada]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/) para inicializar o SDK do Braze Swift de forma assíncrona e, ao mesmo tempo, garantir que o tratamento das notificações por push seja preservado. Isso pode ser útil quando for necessário configurar outros serviços antes de inicializar o SDK, como buscar dados de configuração de um servidor ou aguardar o consentimento do usuário.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segmento Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [Swift SDK 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [SDK do Cordova 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - Esta versão agora requer o Android 13.0.0 da Cordova.
    - Consulte o [anúncio da versão do Cordova](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html) para obter uma lista completa dos requisitos de dependência do projeto.- Atualizou a ponte nativa do Android do [Braze Android SDK 30.3.0 para o 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizamos a ponte nativa do iOS do [Braze Swift SDK 9.2.0 para o 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Swift SDK 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - Atualizamos a ponte nativa do Android do [Braze Android SDK 30.3.0 para o 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizamos a ponte nativa do iOS do [Braze Swift SDK 9.0.0 para o 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Plug-in Swift do Braze Segment 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - Atualiza as ligações do Braze Swift SDK para exigir versões da denominação `10.2.0+` SemVer.
        - Isso permite a compatibilidade com qualquer versão do Braze SDK de `10.2.0` até, mas não incluindo, `11.0.0`.
        - Consulte a entrada do changelog de [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) Para saber mais sobre possíveis mudanças significativas.
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - Atualiza a ponte nativa do Android do [Braze Android SDK 30.4.0 para o 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Altera o comportamento do `wipeData()` no Android para reter inscrições externas (como `subscribeToContentCards()`) depois de ser chamado.
    - Atualiza a ponte nativa do iOS do [Braze Swift SDK 9.0.0 para o 10.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Swift SDK 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

## Liberação em 20 de agosto de 2024

### Novos casos de uso

#### Catálogos

Você pode trazer qualquer tipo de dados para um catálogo. Normalmente, os dados são metadados sobre ofertas, como produtos, descontos, promoções, eventos e similares. Leia nossos [casos de uso]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) e saiba como usar esses dados para direcionar os usuários com envios de mensagens altamente relevantes.

#### Intelligence Suite

O Intelligence Suite oferece recursos avançados para analisar o histórico do usuário e a performance da campanha e do Canva e, em seguida, fazer ajustes automáticos para aumentar o engajamento, a visualização e as conversões. Para ver alguns exemplos de como esses recursos podem beneficiar diferentes setores, confira nossos [casos de uso]({{site.baseurl}}/user_guide/brazeai/intelligence).

### Atualização do dashboard da página inicial

Você pode [continuar de onde parou]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off) no dashboard do Braze com acesso fácil aos arquivos que editou ou criou recentemente. Essa seção aparece na parte superior da página **inicial** do dashboard do Braze.

### Flexibilidade de dados

#### Modelos de transformação de dados e novos destinos

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Crie sua transformação de dados usando nossa [biblioteca de modelos]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-2-create-a-transformation) dedicada para ajudá-lo a começar com determinadas plataformas externas, em vez do código padrão. Agora você pode selecionar **POST: Envie mensagens imediatamente via API Apenas** como seu destino para transformar webhooks de uma plataforma de origem para enviar mensagens imediatas aos seus usuários.

#### Mesclar usuários em massa

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Se encontrar perfis de usuários duplicados, é possível [mesclar em massa]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) esses usuários para ajudar a simplificar os dados.

#### Exportar atributos personalizados

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

É possível [exportar a lista de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data) como um arquivo CSV selecionando **Exportar tudo** na página **Atributos personalizados**. O arquivo CSV será gerado e um link para baixar será enviado para você por e-mail.

#### Lista de permissões de IP dos Currents

O Braze enviará dados do Currents dos IPs listados, que são automática e dinamicamente adicionados a quaisquer chaves de API que tenham sido aceitas para a [listagem de permissões]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents).

### Canais robustos

#### Experiência do novo criador de segmentos

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Crie um segmento usando nossa [experiência atualizada]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment). Os segmentos são atualizados em tempo real à medida que os dados mudam, e você pode criar quantos segmentos forem necessários para fins de direcionamento e envio de mensagens.

#### Métricas por segmentos

Use os modelos de relatório do [Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) para detalhar as métricas de performance de campanhas, Canvas, variantes e etapas de segmentos.

#### Aquisição de número de telefone

Para usar o canal de envio de mensagens do WhatsApp, você precisará de um número de telefone que atenda aos requisitos do WhatsApp para sua [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers). 

Você mesmo deve adquirir seu número de telefone, pois o Braze não fornecerá o número para você. Você pode comprar um telefone físico com um cartão SIM por meio de sua operadora de telefonia comercial ou usar um de nossos parceiros: Twilio ou Infoblip. **Você deve ter sua própria conta Twilio ou Infobip, pois isso não pode ser feito pela Braze.**

### Novas parcerias Braze

#### Zendesk Chat - bate-papo instantâneo

A integração do Braze e do [Zendesk Chat]({{site.baseurl}}/partners/zendesk_chat/) usa webhooks de cada plataforma para configurar uma conversa bidirecional por SMS. Quando um usuário solicita suporte, um ticket é criado no Zendesk. As respostas dos agentes são encaminhadas ao Braze por meio de uma campanha de SMS disparada pela API, e as respostas dos usuários são enviadas de volta ao Zendesk.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 32.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - As seguintes alterações foram feitas ao assinar eventos Push com [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)):
        - O fechamento do site `update` agora será disparado pelos eventos "Push Opened" e "Push Received" por padrão. Anteriormente, ele só era disparado por eventos "Push Opened".
            - Para continuar assinando apenas os eventos "Push Opened", insira `[.opened]` para o parâmetro `payloadTypes`. Como alternativa, implemente seu fechamento `update` para verificar se o `type` do `Braze.Notifications.Payload` é `.opened`.
        - Ao receber uma notificação por push com `content-available: true`, o [`Braze.Notifications.Payload.type`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type) agora será `.received` em vez de `.opened`.
    - Marca as seguintes APIs obsoletas como indisponíveis:
        - `Braze.Configuration.Api.Flavor`
        - `Braze.Configuration.Api.flavor`
        - `Braze.Configuration.Api.SdkMetadata`
        - `Braze.Configuration.Api.addSdkMetadata(_:)`
        - `Braze.ContentCard.ClickAction.uri(_:useWebview:)`
        - `Braze.ContentCard.ClickAction.uri`
        - `Braze.InAppMessage.ClickAction.uri(_:useWebview:)`
        - `Braze.InAppMessage.ClickAction.uri`
        - `Braze.InAppMessage.ModalImage.imageUri`
        - `Braze.InAppMessage.Full.imageUri`
        - `Braze.InAppMessage.FullImage.imageUri`
        - `Braze.InAppMessage.Themes.default`
        - `Braze.deviceId(queue:completion:)`
        - `Braze._objc_deviceId(completion:)`
        - `Braze.deviceId()`
        - `Braze.User.setCustomAttributeArray(key:array:fileID:line:)`
        - `Braze.User.addToCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User.removeFromCustomAttributeArray(key:value:fileID:line:)`
        - `Braze.User._objc_addToCustomAttributeArray(key:value:)`
        - `Braze.User._objc_removeFromCustomAttributeArray(key:value:)`
        - `gifViewProvider`
        - `GifViewProvider.default`
    - Remove as APIs obsoletas:
        - `Braze.Configuration.DeviceProperty.pushDisplayOptions`
        - `Braze.InAppMessageRaw.Context.Error.extraProcessClickAction`
    - Remove a classe obsoleta `BrazeLocation` em favor de `BrazeLocationProvider`.
- [Xamarin SDK Versão 6.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Adição de suporte ao .NET 8.0 para as vinculações do iOS e do Android, pois o .NET 7.0 atingiu o suporte de ponta a ponta.
        - Isso remove o suporte ao .NET 7.0.
    - Atualização da vinculação do Android do [Braze Android 30.4.0 para 32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizada a vinculação do iOS do [Braze Swift SDK 9.0.0 para o 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Ao se inscrever em eventos de notificação por push, a inscrição será disparada no iOS para os eventos "Push Received" e "Push Opened", em vez de apenas para os eventos "Push Opened".
- [React Native SDK 12.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/12.0.0/CHANGELOG.md)
    - Atualiza as ligações da versão nativa do iOS do [Braze Swift SDK 9.0.0 para 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Ao inscrever-se em eventos de notificação por push, a inscrição será disparada no iOS para os eventos `push_received` e `push_opened`, em vez de apenas para `push_opened`.

## Liberação em 23 de julho de 2024

### Atualizações do Braze Docs

#### Diátaxis e documentos do Braze

Estamos no processo de padronizar nossa documentação usando uma estrutura chamada [Diátaxis](https://diataxis.fr/). Para ajudar nossos redatores e colaboradores a criar conteúdo que se encaixe nessa nova estrutura, criamos [modelos para cada tipo de conteúdo]({{site.baseurl}}/contributing/content_types).

#### Novo modelo de solicitação de retirada de documentos para o Braze Docs

Dedicamos um tempo para melhorar nosso modelo de pull-request (PR) para que seja mais fácil e menos confuso [contribuir com a documentação da Braze]({{site.baseurl}}/contributing/home/). Se você ainda acha que há espaço para melhorias, abra uma RP ou [envie um problema](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=). O que for mais fácil!
 
### Flexibilidade de dados

#### Exportar eventos e atributos personalizados

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora, você pode exportar eventos personalizados e atributos personalizados usando os botões de endpoints [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) e [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data).

#### Novas permissões de Currents para usuários

Há duas novas configurações de permissão para os usuários: **Visualizar Integrações de Currents** e **Editar Integrações de Currents**. Saiba mais sobre [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions). 

#### Atualização da política de retenção de dados da Snowflake
 
A partir de 27 de agosto de 2024, as informações de identificação pessoal (IPI) serão removidas de todos os dados de eventos do Snowflake Secure Data Sharing com mais de dois anos. Se você usar o Snowflake, poderá optar por reter os dados completos dos eventos em seu ambiente, armazenando uma cópia em sua conta do Snowflake antes que a política de retenção seja aplicada. Saiba mais sobre a [retenção de dados da Snowflake]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/).
 
### Liberando a criatividade

#### Mensagens no app de várias páginas

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Adicionar páginas à sua mensagem no app permite orientar os usuários por meio de um fluxo sequencial, como um fluxo de integração ou uma jornada de boas-vindas. Para saber mais, consulte [Criação de uma mensagem no app com arrastar e soltar]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page).

#### Encurtamento de links com Liquid

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Use o [Liquid para personalizar URLs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening) para encurtar automaticamente os URLs contidos nas mensagens SMS e coletar análises de dados sobre a taxa de cliques. Para experimentar, consulte [Encurtamento de link]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/).

#### Exemplos de API para catálogos

Adicionamos exemplos para o endpoint `/catalogs` usando campos de vetor. Para ver os exemplos, confira o seguinte:

- [Editar vários itens do catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [Criar vários itens de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [Atualizar itens do catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [Editar item do catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [Criar item de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [Atualizar item do catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [Criar catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### Canais robustos

### Várias contas do WhatsApp Business

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora é possível adicionar várias contas do WhatsApp Business e grupos de inscrições (e números de telefone) a cada espaço de trabalho. Para saber mais, consulte [Várias contas do WhatsApp Business]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups). 

#### Permissões geográficas de SMS

As permissões geográficas de SMS aumentam a segurança e protegem contra o tráfego fraudulento de SMS, impondo controles sobre os países para os quais você pode enviar mensagens SMS. Para saber como especificar uma lista de permissão de países para garantir que as mensagens SMS sejam enviadas apenas para regiões aprovadas, consulte [Configuração da lista de permissão de países para SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist).

#### LINE e Braze

{% multi_lang_include release_type.md release="Beta" %}

O [LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf) é o aplicativo de envio de mensagens mais popular do Japão, com mais de 95 milhões de usuários ativos mensais. Você pode integrar suas contas LINE com o Braze para aproveitar seus dados de clientes primários e zero para enviar mensagens LINE atraentes para os clientes certos com base em suas preferências, comportamentos e interações entre canais. Para começar, consulte o [LINE]({{site.baseurl}}/line).

#### Shopify: Quedas de preço e volta ao estoque

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Agora, com a Shopify, você pode criar notificações personalizadas para [quedas de preços]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) e [itens que voltaram ao estoque]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications).
 
### Automação de IA e ML
 
#### Mesclagem baseada em regras para usuários duplicados

Antes, era possível localizar e mesclar usuários duplicados na Braze individualmente ou em massa. Agora você pode criar regras para controlar como as duplicatas são resolvidas, de modo que o usuário mais relevante seja mantido. Para saber mais, consulte [Mesclagem baseada em regras]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

#### IA Liquid Assistant 

{% multi_lang_include release_type.md release="Beta" %}

O IA Liquid Assistant é um assistente de bate-papo desenvolvido pela <sup>BrazeAITM</sup> que ajuda a gerar o Liquid de que você precisa para personalizar o conteúdo das mensagens. Você pode gerar Liquid a partir de modelos, receber sugestões personalizadas de Liquid e otimizar o Liquid existente com o suporte do <sup>BrazeAITM</sup>. O IA Liquid Assistant também fornece anotações que explicam o Liquid usado, para que você possa aumentar sua compreensão do Liquid e aprender a escrever o seu próprio.

Para começar, consulte [Assistente de IA Liquid]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_liquid).
 
### SDK
 
#### Registros do SDK do Android

Reformulamos os [documentos de registro do SDK da Braze para Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging) para facilitar a leitura e o uso em seu app. Também adicionamos descrições para cada nível de registro.

#### Notificações por push em primeiro plano do SDK do iOS

O método `subscribeToUpdates` na Braze iOS SDK agora pode detectar se uma notificação por push em primeiro plano foi recebida. Para saber mais, consulte [Integração de notificações por push do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration).
 
#### Atualizando os documentos da Xamarin
 
Desde a [versão 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0), o SDK da Braze para Xamarin usa o Swift SDK, portanto, atualizamos os trechos de código e o material de referência. Também reestruturamos a seção para facilitar a leitura e a compreensão. Para dar uma olhada, consulte os [documentos da Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup).

#### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.
 
- [Swift SDK 9.3.1](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.1)
- [Web SDK 5.3.2](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#532)
    - Foi corrigida uma regressão introduzida na versão 5.2.0 que podia fazer com que as mensagens HTML no app fossem renderizadas incorretamente quando um script externo era carregado de forma síncrona.
- [Web SDK 5.4.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#540)

## Liberação em 25 de junho de 2024

### Documentos em japonês

Agora oferecemos suporte ao idioma japonês para os documentos do Braze!

![O site Braze Docs está exibindo a interface japonesa]({% image_buster /assets/img/braze-docs-japan.png %}){: style="max-width:70%;"}
 
### Flexibilidade de dados

#### Anexos para campanhas disparadas por API

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

O endpoint [`/campaigns/trigger/send` ]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) agora aceita anexos (assim como o endpoint `/messages/send` aceita anexos para e-mails). 

#### Suporte adicional a data warehouse

{% multi_lang_include release_type.md release="Acesso antecipado" %}

A [ingestão de dados em nuvem da Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources)  agora oferece suporte ao BigQuery, Databricks, Redshift e Snowflake.

#### Migração do número de telefone do WhatsApp

Migre seu número de telefone do WhatsApp entre contas do WhatsApp Business usando o registro incorporado do Meta. Leia mais sobre a [migração de números telefônicos do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration).
 
### Liberando a criatividade

#### Engajamento por dispositivo

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

O novo relatório de **engajamento por dispositivo** fornece um detalhamento dos dispositivos que seus usuários estão usando para interagir com seu e-mail. Esses dados rastreiam o engajamento por e-mail em dispositivos móveis, desktops, tablets e outros tipos de dispositivos. Saiba mais sobre [relatório e dashboard de desempenho de e-mail]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard).

#### Propriedades do WhatsApp e do SMS Liquid no Canvas Flow

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Adicionamos suporte às [propriedades Liquid do WhatsApp e SMS no Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Agora, quando uma etapa do caminho da ação contém um disparador "Enviou uma mensagem de entrada SMS" ou "Enviou uma mensagem de entrada WhatsApp", as etapas subsequentes do Canva podem incluir uma propriedade Liquid do SMS ou do WhatsApp. Isso reflete o funcionamento das propriedades do evento no Canvas Flow. Dessa forma, você pode aproveitar suas mensagens para salvar e fazer referência a dados primários sobre perfis de usuários e envio de mensagens de conversação.
 
#### Jornadas personalizadas em telas recorrentes

{% multi_lang_include release_type.md release="Acesso antecipado" %}

As jornadas personalizadas no Canvas permitem personalizar qualquer ponto de uma jornada do Canvas para usuários individuais com base na probabilidade de conversão. Agora, as jornadas personalizadas estão disponíveis para canvas recorrentes. Saiba mais sobre [variantes personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths).

#### Solução de problemas de segmentos

Trabalhando com segmentos? Aqui estão algumas [etapas de solução de problemas e considerações]({{site.baseurl}}/user_guide/engagement_tools/segments/troubleshooting) que devem ser levadas em conta.

#### Realce líquido

Aprimoramos o [código de cores que o Liquid usa]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid) para oferecer melhor suporte às diretrizes de acessibilidade.

![]({% image_buster /assets/img/liquid_color_code.png %})
 
### Canais robustos

#### Permissões geográficas de SMS

{% multi_lang_include release_type.md release="Acesso antecipado" %}

As permissões geográficas de SMS aumentam a segurança e protegem contra o tráfego fraudulento de SMS, impondo controles sobre os países para os quais você pode enviar mensagens SMS. Os administradores agora podem especificar uma lista de permissão de países para garantir que as mensagens SMS sejam enviadas apenas para regiões aprovadas. Para saber mais, consulte [Permissões geográficas de SMS]({{site.baseurl}}/sms_geographic_permissions). 

![O menu suspenso "Lista de permissão de países" com os países mais comuns exibidos na parte superior.]({% image_buster /assets/img/sms/allowlist_dropdown.png %}){: style="max-width:80%;"}

#### Práticas recomendadas para SMS/MMS

Saiba mais sobre as [práticas recomendadas para SMS/MMS com a Braze]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices), incluindo nossas recomendações para monitoramento de aceitação e bombeamento de tráfego. 

#### Rastreamento de cancelamentos de inscrição por push

Confira nosso novo [artigo de ajuda]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) para obter algumas dicas para rastrear cancelamentos de inscrição push.

#### Descontinuação do Shopify `checkout.liquid`

Observe que o suporte para a Shopify `checkout.liquid` começará a ser descontinuado em agosto de 2024 e terminará em agosto de 2025. Leia mais sobre como a Braze lidará com [essa transição]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout). 

### Atualizações do SDK
 
As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.
 
- [Swift SDK 9.3.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/9.3.0)
    - Pretere as APIs de Feature Flag existentes, que serão removidas em uma versão futura:
        - `Braze.FeatureFlag.jsonStringProperty(key:)` foi descontinuado.
        - `Braze.FeatureFlag.jsonObjectProperty(key:)` foi preterido em favor de `Braze.FeatureFlag.jsonProperty(key:)`.
- [Roku SDK 2.2.0](https://github.com/braze-inc/braze-roku-sdk/blob/main/CHANGELOG.md)
- [Plug-in do Braze Expo 2.1.2](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)

#### Documentação do tvOS

Há alguns meses, os artigos dos [cartões de conteúdo do tvOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/content_cards/tvos) e do [envio de mensagens no app]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/customization/tvos) foram descontinuados por engano. Esses documentos foram republicados na seção Swift da documentação da Braze.

{% alert note %}
Os [colaboradores]({{site.baseurl}}/contributing/home) da documentação da Braze devem notar que o site agora é executado no Ruby 3.3.0. Faça upgrade de sua versão do Ruby conforme necessário.
{% endalert %}

## Liberação em 28 de maio de 2024

### Atualizações visuais no site de documentação

Você deve ter notado que nosso site de documentação está com um visual novo e elegante! Nós o reformulamos para refletir a nova e vibrante identidade da marca Braze. Para conhecer os bastidores de nossa nova marca, leia mais em [Unveiling Our New Brand: Uma conversa com o Diretor Executivo de Criação da Braze, Greg Erdelyi](https://www.braze.com/resources/articles/unveiling-our-new-brand-a-conversation-with-braze-executive-creative-director-greg-erdelyi).

### Suporte para português e espanhol

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

A Braze agora está disponível em português e espanhol. Para alterar o idioma em que o dashboard da Braze é exibido, consulte [Configurações de idioma]({{site.baseurl}}/user_guide/administrative/access_braze/language/).

### Canais robustos

#### Configurações em vários idiomas

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Ao ajustar as [configurações multilíngues]({{site.baseurl}}/multi_language_support/), é possível direcionar usuários em diferentes idiomas e locais com mensagens diferentes, tudo em uma única mensagem de e-mail. Para editar e gerenciar o suporte a vários idiomas, é necessário ter a permissão de usuário "Manage Multi-Language Settings" (Gerenciar configurações de vários idiomas). Para adicionar a localização a uma mensagem, você precisará de permissões para editar campanhas.

#### Cabeçalho de cancelamento de inscrição com um clique no nível da mensagem

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

O cancelamento de inscrição com um clique para o cabeçalho list-unsubscribe ([RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) fornece uma maneira fácil para os destinatários optarem pela aceitação de e-mails. É possível ajustar essa configuração de cabeçalho para ser aplicada no nível da mensagem em seus e-mails. Para saber mais sobre essa configuração, consulte [Cabeçalho de cancelamento de inscrição de e-mail em espaços de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces).

#### Sobre a higienização de e-mails

Visite nosso novo artigo sobre [sanitização]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization) para saber mais sobre o processo que ocorre quando o Braze detecta um tipo específico de JavaScript em sua mensagem de e-mail. Seu principal objetivo é impedir que agentes mal-intencionados acessem os dados de sessão de outros usuários do dashboard do Braze.

#### Contagem de inclusão para blocos de conteúdo

Depois de adicionar um bloco de conteúdo em uma campanha ou canvas ativo, é possível [fazer uma prévia desse bloco de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) na biblioteca de blocos de conteúdo passando o mouse sobre o bloco de conteúdo e selecionando o ícone <i class="fa fa-eye preview-icon"></i> **Preview**.

#### Status da tela

No dashboard da Braze, seus canvas são agrupados por status. Confira os diferentes [status e descrições do Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) para saber o que eles significam.

### Automação de IA e ML

#### Diretrizes da marca para o assistente de Copywriting de IA

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora é possível criar e aplicar [diretrizes da marca]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/) para personalizar o estilo da cópia gerada pelo Assistente de Copywriting IA de acordo com a voz da sua marca. Defina várias diretrizes para diferentes cenários para garantir que seu tom sempre corresponda ao contexto.
 
### Novas parcerias Braze

#### Adikteev - Análise de dados

A integração entre o Braze e a [Adikteev]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/) permite aumentar a retenção de usuários, aproveitando a tecnologia de previsão de churn da Adikteev nas campanhas do Braze CRM para direcionar prioritariamente os segmentos de usuários de alto risco.
 
#### Celebrus - Análise de dados
 
A integração da Braze com o [Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus) se integra perfeitamente ao SDK da Brazenos canais de aplicativos móveis e da Web, facilitando o preenchimento da Braze com dados de atividade do canal. Isso inclui insights abrangentes sobre o tráfego de visitantes em ativos digitais durante períodos específicos.
 
#### IAM Studio - Modelos de mensagens
 
Com a integração do Braze e do [IAM Studio]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/), você pode inserir facilmente modelos de mensagens no app personalizáveis em suas mensagens no app do Braze, oferecendo substituição de imagem, modificação de texto, configurações de deep linking, atributos personalizados e configurações de eventos. Usando o IAM Studio, é possível reduzir o tempo de produção de mensagens e dedicar mais tempo ao planejamento de conteúdo.
 
#### Regal - Bate-papo instantâneo

Ao integrar o Braze e a [Regal]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/), você pode criar uma experiência mais consistente e personalizada em todos os pontos de contato com o cliente.

#### Dados do Tesouro - Importação de coorte
 
Com a integração entre a Braze e o [Treasure Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/), é possível fazer a importação de coortes de usuários do Treasure Data para a Braze, de modo que seja possível enviar campanhas direcionadas com base em dados que podem existir apenas em seu data warehouse.
 
#### Zapier - Automação do fluxo de trabalho
 
A parceria Braze e [Zapier]({{site.baseurl}}/partners/data_and_infrastructure_agility/workflow_automation/zapier/) aproveita a API do Braze e os webhooks do Braze para se conectar a aplicativos de terceiros e automatizar várias ações.

### Atualizações do SDK
 
As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 31.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Plug-in Swift do Braze Segment 3.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#300)
    - Atualiza as ligações do SDK Swift da Braze para exigir versões a partir da denominação 9.2.0+ SemVer.
        - Isso permite a compatibilidade com qualquer versão do SDK da Braze, desde a 9.2.0 até a 10.0.0, mas não incluindo essa versão.
        - Consulte as entradas do changelog das versões [7.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#700), [8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800) e [9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#900) para obter mais informações sobre possíveis mudanças significativas.
    - O suporte a notificações por push agora requer uma chamada para o método estático `BrazeDestination.prepareForDelayedInitialization()` o mais cedo possível no ciclo de vida do app, no método `AppDelegate.application(_:didFinishLaunchingWithOptions:)` do seu aplicativo.
- [Cordova SDK 9.0.0-9.2.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md)
    - Atualizamos a ponte nativa do iOS do [SDK Swift da Braze 7.7.0 para o 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Plug-in Expo 2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [Swift SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - Atualizamos a ponte nativa do iOS do [SDK Swift da Braze 7.7.0 para o 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizamos a ponte nativa do Android do [SDK da Braze para Android 29.0.1 para o 30.3.0](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Web SDK 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDK Versão 5.0.0
    - Atualizada a vinculação do iOS de [SDK Swift da Braze 8.4.0 para o 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
