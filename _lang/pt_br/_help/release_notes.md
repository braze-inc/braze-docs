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

## Lançamento em 12 de novembro de 2024
 
### Flexibilidade de dados
 
#### Limite de velocidade para `/users/track`

O limite de velocidade para o [`/users/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) foi atualizado para 3.000 a cada 3 segundos.
 
### Liberando a criatividade

#### Casos de Uso do canva

Reunimos alguns casos de uso que mostram as diferentes maneiras de aproveitar um Canvas Braze. Se você está procurando inspiração, escolha um caso de uso abaixo para começar.

- [Carrinho abandonado]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/abandoned_cart/)
- [De Volta em Estoque]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/back_in_stock/)
- [Adopção de Recursos]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/feature_adoption/)
- [Usuário Inativo]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/lapsed_user/)
- [Onboarding]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/onboarding/)
- [Feedback Pós-Compra]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/post_purchase_feedback/)

### Canais robustos

#### LINE

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

A integração LINE do Braze agora está geralmente disponível! LINE é o aplicativo de envio de mensagens mais popular no Japão, com mais de 95 milhões de usuários ativos mensais. Além do envio de mensagens, o LINE oferece a seus usuários uma plataforma "tudo em um" para redes sociais, jogos, compras e pagamentos.

Para começar, veja nossa [documentação LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/).
 
#### Sincronização de Público do LinkedIn

{% multi_lang_include release_type.md release="Beta" %}

Agora você pode usar o LinkedIn com [Braze Audience Sync]({{site.baseurl}}/partners/canvas_steps/), uma ferramenta que ajuda a ampliar o alcance de suas campanhas para muitas das principais tecnologias sociais e de publicidade. Para se juntar ao beta, entre em contato com seu Gerente de Sucesso da Braze.
 
### Melhorando o guia do desenvolvedor
 
Estamos no processo de fazer grandes melhorias no [Braze Developer Guide]({{site.baseurl}}/developer_guide/home/). Como uma primeira etapa, simplificamos a navegação e reduzimos o número de seções aninhadas. 

|Antes|Após|
|------|-----|
|!["O antigo guia de navegação para o Braze Developer Guide."]({% image_buster /assets/img/release_notes/developer_guide_improvements/old_navigation.png %})|!["A nova navegação para o Guia do Desenvolvedor Braze."]({% image_buster /assets/img/release_notes/developer_guide_improvements/new_navigation.png %})|

### Novas parcerias Braze
 
#### MeuCartãoPostal

[MyPostcard](https://www.mypostcard.com/), um aplicativo global líder em cartões postais, capacita você a executar campanhas de mala direta com facilidade, proporcionando uma maneira perfeita e lucrativa de se conectar com seus clientes. Para começar, veja [Integrando MyPostcard com Braze]({{site.baseurl}}/partners/message_orchestration/additional_channels/direct_mail/mypostcard/).
 
### Atualizações do SDK
 
As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.
 
- [Plugin Expo 3.0.0](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md)
    - Esta versão requer 13.1.0 do SDK Braze React Native.
    - Substitui a chamada do método BrazeAppDelegate do iOS de BrazeReactUtils.populateInitialUrl por BrazeReactUtils.populateInitialPayload.
        - Esta atualização resolve um problema em que eventos de push abertos não seriam acionados ao clicar em uma notificação enquanto o aplicativo está em um estado terminado.
        - Para aproveitar totalmente esta atualização, substitua todas as chamadas de Braze.getInitialURL por Braze.getInitialPushPayload no seu código JavaScript. A URL inicial agora pode ser acessada através da propriedade url da carga útil do push inicial.
- [Braze Segment SWIFT Plugin 5.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md)
    - Atualiza as ligações do SDK Braze Swift para exigir lançamentos da denominação SemVer 11.1.1+.
    - Isso permite compatibilidade com qualquer versão do SDK Braze de 11.1.1 até, mas não incluindo, 12.0.0.
    - Consulte a entrada do changelog para 11.1.1 Para saber mais sobre possíveis mudanças que podem causar problemas.

## lançamento de 15 de outubro de 2024

### Flexibilidade de dados

#### Campanhas e canvas

Enquanto cria campanhas e canvas, você pode calcular o número exato de usuários alcançáveis em seu público-alvo em vez da estimativa padrão, selecionando [Calcular estatísticas exatas]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment/#statistics-for-segment-size).

#### API Android objects

O [`android_priority` parâmetro]({{site.baseurl}}/api/objects_filters/messaging/android_object/#additional-parameter-details) aceitará valores "normal" ou "alto" para especificar a prioridade do remetente FCM. Por padrão, as mensagens de notificação são enviadas com alta prioridade, e as mensagens de dados são enviadas com prioridade normal.

Para saber mais sobre como diferentes valores impactam a entrega, veja [prioridade da mensagem Android](https://firebase.google.com/docs/cloud-messaging/android/message-priority/).

#### SDK

Use o [Braze SDK's built-in debugger]({{site.baseurl}}/developer_guide/platform_wide/debugging/) para solucionar problemas em seus canais com suporte a SDK sem precisar ativar o registro detalhado em seu app.

#### Atividades ao vivo

Atualizamos as [perguntas frequentes]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/faq/) para Swift Live Activities com algumas novas perguntas e respostas.

#### Eventos personalizados

[Objetos de propriedades de evento]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#custom-event-properties) que contêm valores de array ou objeto agora podem ter uma carga útil de propriedade de evento de até 100 KB.

#### Números aleatórios de baldes

Use [reentrada aleatória do público com números de bucket aleatórios]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/#random-audience-re-entry-using-random-bucket-numbers) para Testes A/B ou direcionamento de grupos de usuários específicos em suas campanhas.

#### Extensões de segmento

Você pode [atualizar extensões de segmento em um cronograma recorrente]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#setting-up-a-recurring-refresh) selecionando a frequência com que as extensões serão atualizadas (diariamente, semanalmente ou mensalmente) e o horário específico em que a atualização ocorrerá.

### Canais robustos

#### SMS

Adicionamos [Adicionando parâmetros UTM]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#using-link-shortening) para demonstrar como você pode usar parâmetros UTM em uma mensagem SMS, para que você acompanhe a performance das campanhas em ferramentas de análise de dados de terceiros, como o Google Analytics.

#### Páginas de destino

[Conecte seu próprio domínio]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/connect_domain/) ao seu espaço de trabalho Braze para personalizar as URLs da sua landing page com sua marca.

#### LINE e Braze

{% multi_lang_include release_type.md release="Beta" %}

Adicionamos nova documentação:

- [Tipos de mensagem LINE]({{site.baseurl}}/line/create/message_types/) abrange os tipos de mensagem LINE que você pode compor, incluindo aspectos e limitações, e faz parte da coleção beta do LINE.
- [O link de conta do usuário]({{site.baseurl}}/line/line_setup/#user-account-linking) permite que os usuários vinculem sua conta LINE à conta de usuário do seu app. Você pode então usar Liquid no Braze, como {% raw %}`{{line_id}}`{% endraw %}, para criar uma URL personalizada para o usuário que passa o ID do LINE do usuário de volta para o seu site ou app, que pode então ser associado a um usuário conhecido.

#### WhatsApp e Braze

[Contas do WhatsApp Business (WABA)]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/#step-2-whatsapp-setup) agora podem ser compartilhadas com vários Provedores de Soluções Empresariais.

### Novas parcerias Braze

#### Hino Futuro - Conteúdo Dinâmico

A Braze e a [Future Anthem]({{site.baseurl}}/partners/message_personalization/dynamic_content/future_anthem/) parceria aproveitam a IA Amplifier para oferecer personalização de conteúdo, experiências em tempo real e públicos dinâmicos. Amplificador IA funciona em esportes, cassinos e loteria, permitindo que você melhore os perfis de jogadores Braze com atributos de jogadores específicos da indústria, como um jogo favorito, pontuação de engajamento, próxima aposta esperada e mais.

### Configurações

#### Criptografia em nível de campo de identificador

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Usando [identificador de criptografia em nível de campo]({{site.baseurl}}/user_guide/data_and_analytics/field_level_encryption/), você pode criptografar endereços de e-mail de forma integrada com o AWS Key Management Service (KMS) para minimizar informações pessoalmente identificáveis (IPI) compartilhadas no Braze. A criptografia substitui dados confidenciais por texto cifrado, que é uma informação criptografada ilegível.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [SWIFT SDK 10.3.1](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [SWIFT SDK 11.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
    - Adiciona suporte para [SWIFT 6 verificação de concorrência estrita](https://developer.apple.com/documentation/swift/adoptingswift6)
        - As classes e tipos de dados Braze relevantes agora estão em conformidade com o `Sendable` protocolo e podem ser usados com segurança em contextos de concorrência.
        - As APIs exclusivas da thread principal agora estão marcadas com o atributo `@MainActor`.
        - Recomendamos o uso do Xcode 16.0 ou posterior para aproveitar esses recursos enquanto minimiza o número de avisos gerados pelo compilador. Versões anteriores do Xcode ainda podem ser usadas, mas alguns recursos podem gerar avisos.
    - Ao integrar o suporte a notificação por push manualmente, pode ser necessário atualizar a `UNUserNotificationCenterDelegate` conformidade para usar o `@preconcurrency` atributo para evitar avisos.
        - Aplicar o atributo `@preconcurrency` na conformidade do protocolo está disponível apenas no Xcode 16.0 ou posterior. Referencie nosso código de integração de amostra [aqui](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/PushNotifications-Manual).
- [React Native SDK 13.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1300)
    - Atualiza as ligações nativas da versão Android de [Braze Android SDK 31.1.0 para 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v31.1.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualiza os bindings da versão nativa do iOS do [Braze SWIFT SDK 10.3.0 para 11.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/10.3.0...11.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Flutter SDK 11.1.0](https://pub.dev/packages/braze_plugin/changelog#1110)
- [SWIFT SDK 11.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1110)
- [Android SDK 33.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3300)
    - Atualizado Kotlin de 1.8 para Kotlin 2.0.
- [Web SDK 5.5.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md#550)

## lançamento de 17 de setembro de 2024

### Flexibilidade de dados

#### Braze Cloud Data Ingestion para S3

Você pode usar [Cloud Data Ingestion (CDI) for S3]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/file_storage_integrations/#aws-definitions) para integrar diretamente um ou mais buckets S3 na sua conta AWS com Braze. Quando novos arquivos são publicados no S3, uma mensagem é postada no SQS, e a Ingestão de dados para a nuvem da Braze recebe esses novos arquivos.

#### Limite de frequência aumentado

O limite de frequência para o [/users/export/ids]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier) tipo de solicitação aumentou para 2.500 solicitações por minuto.

#### Usuários ativos mensais CY 24-25

Para os clientes que adquiriram Usuários Ativos Mensais - CY 24-25, a Braze gerencia diferentes limites de taxa em seu `/users/track` endpoint. Para mais detalhes, consulte [POST: Rastreamento de usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#monthly-active-users-cy-24-25). 

### Liberando a criatividade

#### Modelo de itens de catálogo, incluindo Liquid

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Use o `:rerender` flag em uma tag Liquid para [renderizar o conteúdo Liquid de um item do catálogo]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/catalog/#using-liquid). Por exemplo, se você renderizar o seguinte conteúdo Liquid:

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

#### Mensagens de resposta do WhatsApp

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Você pode usar [mensagens de resposta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#response-messages) para responder a mensagens do WhatsApp recebidas de seus usuários. Essas mensagens são criadas no app do Braze durante sua experiência de composição e podem ser editadas a qualquer momento. É possível usar o Liquid para fazer a correspondência entre o idioma da mensagem de resposta e os usuários apropriados.

#### Modelos de canva

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Crie [modelos de canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_templates/) para refinar seu envio de mensagens, criando uma estrutura consistente que pode ser facilmente personalizada para atender aos seus objetivos específicos em seus canvases.

#### Páginas de destino

{% multi_lang_include release_type.md release="Beta" %}

Braze [landing pages]({{site.baseurl}}/user_guide/engagement_tools/landing_pages) são páginas da web independentes que podem impulsionar sua estratégia de aquisição de usuários e engajamento.

#### Mudanças desde a última visualização

Você pode ver o número de atualizações em seus [canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics/#changes-since-last-viewed), campanhas e [segmentos]({{site.baseurl}}/user_guide/engagement_tools/segments/managing_segments/#changes-since-last-viewed) por outros membros de sua equipe consultando a métrica *Alterações Desde a Última Visualização* nas respectivas páginas de visão geral (como a página de visão geral para uma [campanha de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#changes-since-last-viewed)). 

#### Solução de problemas de solicitações de webhook e Conteúdo Conectado 

[Este artigo]({{site.baseurl}}/help/help_articles/api/webhook_connected_content_errors) aborda como solucionar códigos de erro de webhook e Conteúdo Conectado, incluindo quais são os erros e os passos para resolvê-los.

### Novas parcerias Braze

#### Inbox Monster - análise de dados

[Inbox Monster]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/inbox_monster/) é uma plataforma de sinais de caixa de entrada que ajuda marcas empresariais a garantir cada envio. É um conjunto integrado de soluções para entregabilidade, renderização criativa e monitoramento de SMS, que capacita as equipes modernas de gerenciamento de relacionamento com o cliente (CRM) e acaba com os medos de envio.

#### SessionM - Fidelidade

[SessionM]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/sessionm/) é uma plataforma de engajamento e fidelidade do cliente que fornece recursos de gerenciamento de campanhas e soluções de gerenciamento de fidelidade para ajudar os profissionais de marketing a impulsionar o alcance direcionado para aumentar o engajamento e a lucratividade.

### Automação de IA e ML

#### Recomendações de itens em alta

Além do modelo "IA Personalizado", o recurso de [recomendações de itens de IA]({{site.baseurl}}/user_guide/sage_ai/recommendations/about_item_recommendations/#trending) também inclui um modelo de recomendação para "Tendências", que apresenta itens que tiveram o impulso mais positivo quando se trata de interações recentes do usuário.

### Configurações

#### Funções

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

[Funções]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#creating-a-role) permitem mais estrutura ao agrupar suas permissões personalizadas individuais com controles de acesso ao espaço de trabalho. Isso é especialmente útil se você tiver muitas marcas ou espaços de trabalho regionais em um dashboard. Com funções, você pode adicionar usuários do dashboard aos espaços de trabalho certos e conceder diretamente as permissões associadas. 

#### Relatório de evento de segurança

Adicionamos uma lista completa dos [eventos de segurança]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/security_settings/#downloading-a-security-event-report) que podem aparecer no seu relatório de eventos de segurança baixado.

#### Relatório de uso de mensagens

{% multi_lang_include release_type.md release="Acesso antecipado" %}

O [painel de uso de mensagens]({{site.baseurl}}/message_usage/) fornece insights de autoatendimento sobre o uso de crédito do seu SMS e WhatsApp para uma visão abrangente do uso histórico e atual em comparação com as alocações do contrato. Essas percepções podem reduzir sua confusão e ajudá-lo a fazer ajustes para prevenir riscos de excedente.

### SDK

#### Inicialização atrasada para o SDK Braze SWIFT

Configure [inicialização atrasada]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/advanced_use_cases/delayed_initialization/) para inicializar seu SDK Braze Swift de forma assíncrona, garantindo que o manuseio de notificação por push seja preservado. Isso pode ser útil quando você precisa configurar outros serviços antes de inicializar o SDK, como buscar dados de configuração de um servidor ou aguardar o consentimento do usuário.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 32.1.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md#3210)
- [Segmento Kotlin SDK 2.0.0](https://github.com/braze-inc/braze-segment-kotlin/blob/main/CHANGELOG.md#200)
- [SWIFT SDK 10.1.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1010)
- [React Native SDK 12.1.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1210)
- [Cordova SDK 10.0.0](https://github.com/braze-inc/braze-cordova-sdk/blob/master/CHANGELOG.md#1000)
    - Esta versão agora requer Cordova Android 13.0.0.
    - Consulte o [Cordova release announcement](https://cordova.apache.org/announcements/2024/05/23/cordova-android-13.0.0.html) para uma lista completa dos requisitos de dependência do projeto.- Atualizado o bridge nativo Android [de Braze Android SDK 30.3.0 para 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizado o bridge nativo do iOS [do Braze SWIFT SDK 9.2.0 para 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.2.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SWIFT SDK 10.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1020)
- [Unity 7.0.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#700)
    - Atualizado o bridge nativo Android [do Braze Android SDK 30.3.0 para 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.3.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizado o bridge nativo do iOS [do Braze SWIFT SDK 9.0.0 para 10.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Braze Segment SWIFT Plugin 4.0.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#400)
    - Atualiza as ligações do SDK Braze Swift para exigir lançamentos da denominação `10.2.0+` SemVer.
        - Isso permite compatibilidade com qualquer versão do SDK Braze de `10.2.0` até, mas não incluindo, `11.0.0`.
        - Consulte a entrada do changelog para [`10.0.0`](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1000) para saber mais sobre possíveis mudanças que quebram a compatibilidade.
- [Flutter SDK 11.0.0](https://pub.dev/packages/braze_plugin/changelog#1100)
    - Atualiza a ponte nativa Android [do Braze Android SDK 30.4.0 para 32.1.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Altera o comportamento de `wipeData()` no Android para reter assinaturas externas (como `subscribeToContentCards()`) após ser chamado.
    - Atualiza a ponte nativa do iOS [do Braze SWIFT SDK 9.0.0 para 10.2.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.2.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [SWIFT SDK 10.3.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#1030)
- [Unity 7.1.0](https://github.com/braze-inc/braze-unity-sdk/blob/master/CHANGELOG.md#710)
- [React Native SDK 12.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md#1220)

## Lançamento em 20 de agosto de 2024

### Novos casos de uso

#### Catálogos

Você pode trazer qualquer tipo de dados para um catálogo. Normalmente, os dados são metadados sobre ofertas, como produtos, descontos, promoções, eventos e similares. Leia nossos [casos de uso]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs) e aprenda como você pode usar esses dados para segmentar usuários com mensagens altamente relevantes.

#### Intelligence Suite

O Intelligence Suite oferece recursos avançados para analisar o histórico do usuário e a performance da campanha e do Canva e, em seguida, fazer ajustes automáticos para aumentar o engajamento, a visualização e as conversões. Para alguns exemplos de como esses recursos podem beneficiar diferentes indústrias, confira nossos [casos de uso]({{site.baseurl}}/user_guide/brazeai/intelligence).

### Atualização do dashboard inicial

Você pode [continuar de onde parou]({{site.baseurl}}/user_guide/data_and_analytics/analytics/home_dashboard/#pick-up-where-you-left-off) no dashboard do Braze com fácil acesso aos arquivos que você editou ou criou recentemente. Essa seção aparece na parte superior da página **inicial** do dashboard do Braze.

### Flexibilidade de dados

#### Modelos de Transformação de Dados e novo destino

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Construa sua Transformação de Dados usando nossa [biblioteca de modelos]({{site.baseurl}}/user_guide/data_and_analytics/data_transformation/creating_a_transformation#step-2-create-a-transformation) dedicada para ajudá-lo a começar com certas plataformas externas, em vez de código padrão. Agora você pode selecionar **POST: Envie mensagens imediatamente via API Only** como seu destino para transformar webhooks de uma plataforma de origem para enviar mensagens imediatas aos seus usuários.

#### Mesclar usuários em massa

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Se você encontrar perfis de usuário duplicados, pode [mesclar em massa]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users#bulk-merging) esses usuários para ajudar a otimizar seus dados.

#### Exportar atributos personalizados

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Você pode [exportar a lista de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#exporting-data) como um arquivo CSV selecionando **Exportar tudo** na página **Atributos Personalizados**. O arquivo CSV será gerado e um link para baixar será enviado para você por e-mail.

#### Currents IP allowlisting

Braze enviará dados de Currents dos IPs listados, que são automaticamente e dinamicamente adicionados a quaisquer chaves de API que tenham optado por [allowlisting]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/setting_up_currents).

### Canais robustos

#### Nova experiência de criador de segmentos

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Construa um segmento usando nossa [experiência atualizada]({{site.baseurl}}/user_guide/engagement_tools/segments/creating_a_segment). Os segmentos são atualizados em tempo real à medida que os dados mudam, e você pode criar quantos segmentos forem necessários para fins de direcionamento e envio de mensagens.

#### Métricas por segmentos

Use os modelos de relatório [do Query Builder]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/) para detalhar as métricas de performance de campanhas, Canvas, variantes e etapas de segmentos.

#### Aquisição de número de telefone

Para usar o canal de envio de mensagens do WhatsApp, você precisará de um número de telefone que atenda aos requisitos do WhatsApp para sua [Cloud API](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers) ou [On-Premises API](https://developers.facebook.com/docs/whatsapp/on-premises/phone-numbers). 

Você mesmo deve adquirir seu número de telefone, pois o Braze não fornecerá o número para você. Você pode comprar um telefone físico com um cartão SIM por meio de sua operadora de telefonia comercial ou usar um de nossos parceiros: Twilio ou Infoblip. **Você deve ter sua própria conta Twilio ou Infobip, pois isso não pode ser feito pela Braze.**

### Novas parcerias Braze

#### Zendesk Chat - Chat Instantâneo

A integração Braze e [Zendesk Chat]({{site.baseurl}}/partners/zendesk_chat/) utiliza webhooks de cada plataforma para configurar uma conversa SMS bidirecional. Quando um usuário solicita suporte, um ticket é criado no Zendesk. As respostas dos agentes são encaminhadas para Braze através de uma campanha de SMS acionada por API, e as respostas dos usuários são enviadas de volta para Zendesk.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 32.0.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [SWIFT SDK 10.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - As seguintes alterações foram feitas ao se inscrever em eventos Push com [`Braze.Notifications.subscribeToUpdates(payloadTypes:_:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/subscribetoupdates(payloadtypes:_:)):
        - O `update` fechamento agora será acionado por eventos "Push Opened" e "Push Received" por padrão. Anteriormente, ele só seria acionado por eventos "Push Opened".
            - Para continuar se inscrevendo apenas em eventos "Push Opened", passe `[.opened]` como parâmetro `payloadTypes`. Alternativamente, implemente seu `update` fechamento para verificar se o `type` do `Braze.Notifications.Payload` é `.opened`.
        - Ao receber uma notificação por push com `content-available: true`, o [`Braze.Notifications.Payload.type`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/notifications-swift.class/payload/type) agora será `.received` em vez de `.opened`.
    - Marca as APIs obsoletas a seguir como indisponíveis:
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
    - Remove a classe `BrazeLocation` obsoleta em favor de `BrazeLocationProvider`.
- [Xamarin SDK Versão 6.0.0](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md)
    - Adicionada a compatibilidade com .NET 8.0 para os bindings de iOS e Android, uma vez que o .NET 7.0 atingiu o fim do suporte.
        - Isso remove o suporte para .NET 7.0.
    - Atualizou a ligação Android de [Braze Android 30.4.0 para 32.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v30.4.0...v32.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizou o binding iOS de [Braze SWIFT SDK 9.0.0 para 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Ao se inscrever em eventos de notificação por push, a inscrição será acionada no iOS tanto para "Push Recebido" quanto para "Push Aberto", em vez de apenas para eventos de "Push Aberto".
- [React Native SDK 12.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/12.0.0/CHANGELOG.md)
    - Atualiza as ligações nativas da versão iOS de [Braze SWIFT SDK 9.0.0 para 10.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/9.0.0...10.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - Ao se inscrever em eventos de notificação por push, a inscrição será acionada no iOS tanto para `push_received` quanto para `push_opened`, em vez de apenas para eventos `push_opened`.

## Liberação em 23 de julho de 2024

### Atualizações do Braze Docs

#### Diátaxis e documentos do Braze

Estamos no processo de padronizar nossa documentação usando uma estrutura chamada [Diátaxis](https://diataxis.fr/). Para ajudar nossos escritores e colaboradores a criar conteúdo que se encaixe neste novo framework, criamos [modelos para cada tipo de conteúdo]({{site.baseurl}}/contributing/content_types).

#### Novo modelo de solicitação de retirada de documentos para o Braze Docs

Dedicamos um tempo para melhorar nosso modelo de pull-request (PR) para que seja mais fácil e menos confuso [contribuir com a documentação da Braze]({{site.baseurl}}/contributing/home/). Se você ainda acha que há espaço para melhorias, abra uma RP ou [envie um problema](https://github.com/braze-inc/braze-docs/issues/new?assignees=&labels=enhancement&projects=&template=request_a_feature.md&title=). O que for mais fácil!
 
### Flexibilidade de dados

#### Exportar eventos e atributos personalizados

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora você pode exportar evento personalizado e atributos personalizados usando os [`/custom_attributes`]({{site.baseurl}}/api/endpoints/export/custom_attributes/get_custom_attributes) e [`/events`]({{site.baseurl}}/api/endpoints/export/custom_events/get_custom_events_data) endpoints.

#### Novas permissões de Currents para usuários

Há duas novas configurações de permissão para os usuários: **Visualizar Integrações de Currents** e **Editar Integrações de Currents**. Saiba mais sobre [permissões do usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions). 

#### Atualização da política de retenção de dados da Snowflake
 
A partir de 27 de agosto de 2024, informações pessoalmente identificáveis (IPI) serão removidas de todos os dados de eventos de Compartilhamento Seguro de Dados do Snowflake que tenham mais de dois anos. Se você usar o Snowflake, poderá optar por reter os dados completos dos eventos em seu ambiente, armazenando uma cópia em sua conta do Snowflake antes que a política de retenção seja aplicada. Saiba mais sobre [Snowflake data retention]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/data_retention/).
 
### Liberando a criatividade

#### Mensagens no app de várias páginas

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Adicionar páginas à sua mensagem no app permite orientar os usuários por meio de um fluxo sequencial, como um fluxo de integração ou uma jornada de boas-vindas. Para saber mais, consulte [Criação de uma mensagem no app com arrastar e soltar]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/create#multi-page).

#### Encurtamento de links com Liquid

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Use [o Liquid para personalizar URLs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/#enabling-link-shortening) para encurtar automaticamente os URLs contidos nas mensagens SMS e coletar análises de dados sobre a taxa de cliques. Para experimentar, consulte [Encurtamento de link]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/).

#### Exemplos de API para catálogos

Adicionamos exemplos para o endpoint `/catalogs` usando campos de vetor. Para ver os exemplos, confira o seguinte:

- [edita vários itens do catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/patch_catalog_items_bulk)
- [Criar vários itens de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/post_create_catalog_items_bulk)
- [Atualizar itens do catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/put_update_catalog_items)
- [edita item do catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/patch_catalog_item)
- [Criar item de catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/post_create_catalog_item)
- [atualiza item do catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/synchronous/put_update_catalog_item)
- [Criar catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_management/synchronous/post_create_catalog)
 
### Canais robustos

### Várias contas do WhatsApp Business

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora é possível adicionar várias contas do WhatsApp Business e grupos de inscrições (e números de telefone) a cada espaço de trabalho. Para saber mais, consulte [Várias contas do WhatsApp Business]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/multiple_subscription_groups). 

#### Permissões geográficas de SMS

As permissões geográficas de SMS aumentam a segurança e protegem contra o tráfego fraudulento de SMS, impondo controles sobre os países para os quais você pode enviar mensagens SMS. Para saber como especificar uma lista de permissão de países para garantir que as mensagens SMS sejam enviadas apenas para regiões aprovadas, consulte [Configuração da lista de permissão de países para SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_geographic_permissions/#configuring-your-sms-country-allowlist).

#### LINE e Braze

{% multi_lang_include release_type.md release="Beta" %}

[O LINE](https://www.lycbiz.com/sites/default/files/media/jp/download/LINE%20Business%20Guide_202310-202403.pdf) é o aplicativo de envio de mensagens mais popular do Japão, com mais de 95 milhões de usuários ativos mensais. Você pode integrar suas contas LINE com o Braze para aproveitar seus dados de clientes primários e zero para enviar mensagens LINE atraentes para os clientes certos com base em suas preferências, comportamentos e interações entre canais. Para começar, consulte [LINE]({{site.baseurl}}/line).

#### Shopify: Quedas de preço e volta ao estoque

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Agora, com a Shopify, você pode criar notificações personalizadas para [quedas de preços]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/price_drop_notifications) e [itens que voltaram ao estoque]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/back_in_stock_notifications).
 
### Automação de IA e ML
 
#### Mesclagem baseada em regras para usuários duplicados

Antes, era possível localizar e mesclar usuários duplicados na Braze individualmente ou em massa. Agora você pode criar regras para controlar como as duplicatas são resolvidas, de modo que o usuário mais relevante seja mantido. Para saber mais, consulte [Mesclagem baseada em regras]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/duplicate_users/#rules-based-merging).

#### IA Liquid Assistant 

{% multi_lang_include release_type.md release="Beta" %}

O Assistente de Líquido de IA é um assistente de chat alimentado pela BrazeAI<sup>TM</sup> que ajuda a gerar o Líquido que você precisa para personalizar o conteúdo das mensagens. Você pode gerar Liquid a partir de templates, receber sugestões personalizadas de Liquid e otimizar Liquid existente com o suporte do BrazeAI<sup>TM</sup>. O IA Liquid Assistant também fornece anotações que explicam o Liquid usado, para que você possa aumentar sua compreensão do Liquid e aprender a escrever o seu próprio.

Para começar, consulte [Assistente de IA Liquid]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_liquid).
 
### SDK
 
#### Registros do SDK do Android

Reformulamos os [documentos de registro do SDK da Braze para Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/initial_sdk_setup/additional_customization_and_configuration/#logging) para facilitar a leitura e o uso em seu app. Também adicionamos descrições para cada nível de registro.

#### Notificações por push em primeiro plano do SDK do iOS

O método `subscribeToUpdates` na Braze iOS SDK agora pode detectar se uma notificação por push em primeiro plano foi recebida. Para saber mais, consulte [Integração de notificações por push do iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/push_notifications/integration).
 
#### Atualizando os documentos da Xamarin
 
Desde a [versão 4.0.0](https://github.com/braze-inc/braze-xamarin-sdk/releases/tag/4.0.0), o SDK da Braze para Xamarin usa o Swift SDK, portanto, atualizamos os trechos de código e o material de referência. Também reestruturamos a seção para facilitar a leitura e a compreensão. Para dar uma olhada, consulte [os documentos da Xamarin]({{site.baseurl}}/developer_guide/platform_integration_guides/xamarin/initial_sdk_setup).

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

[A ingestão de dados em nuvem da Braze]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/connected_sources)  agora oferece suporte ao BigQuery, Databricks, Redshift e Snowflake.

#### Migração do número de telefone do WhatsApp

Migre seu número de telefone do WhatsApp entre contas do WhatsApp Business usando o registro incorporado do Meta. Leia mais sobre [a migração de números telefônicos do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/phone_number_migration).
 
### Liberando a criatividade

#### Engajamento por dispositivo

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

O novo relatório de **engajamento por dispositivo** fornece um detalhamento dos dispositivos que seus usuários estão usando para interagir com seu e-mail. Esses dados rastreiam o engajamento por e-mail em dispositivos móveis, desktops, tablets e outros tipos de dispositivos. Saiba mais sobre [o relatório e o dashboard de desempenho de e-mail]({{site.baseurl}}/user_guide/data_and_analytics/analytics/email_performance_dashboard).

#### Propriedades do WhatsApp e do SMS Liquid no Canvas Flow

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Adicionamos suporte às [propriedades Liquid do WhatsApp e SMS no Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Agora, quando uma etapa do caminho da ação contém um disparador "Enviou uma mensagem de entrada SMS" ou "Enviou uma mensagem de entrada WhatsApp", as etapas subsequentes do Canva podem incluir uma propriedade Liquid do SMS ou do WhatsApp. Isso reflete o funcionamento das propriedades do evento no Canvas Flow. Dessa forma, você pode aproveitar suas mensagens para salvar e fazer referência a dados primários sobre perfis de usuários e envio de mensagens de conversação.
 
#### Jornadas personalizadas em telas recorrentes

{% multi_lang_include release_type.md release="Acesso antecipado" %}

As jornadas personalizadas no Canvas permitem personalizar qualquer ponto de uma jornada do Canvas para usuários individuais com base na probabilidade de conversão. Agora, as jornadas personalizadas estão disponíveis para canvas recorrentes. Saiba mais sobre as [variantes personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/personalized_paths).

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

Saiba mais sobre [as práticas recomendadas para SMS/MMS com a Braze]({{site.baseurl}}/user_guide/message_building_by_channel/sms/best_practices/best_practices), incluindo nossas recomendações para monitoramento de aceitação e bombeamento de tráfego. 

#### Rastreamento de cancelamentos de inscrição por push

Confira nosso novo [artigo de ajuda]({{site.baseurl}}/help/help_articles/push/push_unsubscribes) para obter algumas dicas para rastrear cancelamentos de inscrição push.

#### Descontinuação do Shopify `checkout.liquid`

Observe que o suporte para a Shopify `checkout.liquid` começará a ser descontinuado em agosto de 2024 e terminará em agosto de 2025. Leia mais sobre como a Braze lidará [com essa transição]({{site.baseurl}}/help/release_notes/deprecations/shopify_checkout). 

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
[Os colaboradores]({{site.baseurl}}/contributing/home) da documentação da Braze devem notar que o site agora é executado no Ruby 3.3.0. Faça upgrade de sua versão do Ruby conforme necessário.
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

Ao ajustar [as configurações multilíngues]({{site.baseurl}}/multi_language_support/), é possível direcionar usuários em diferentes idiomas e locais com mensagens diferentes, tudo em uma única mensagem de e-mail. Para editar e gerenciar o suporte a vários idiomas, é necessário ter a permissão de usuário "Manage Multi-Language Settings" (Gerenciar configurações de vários idiomas). Para adicionar a localização a uma mensagem, você precisará de permissões para editar campanhas.

#### Cabeçalho de cancelamento de inscrição com um clique no nível da mensagem

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

O cancelamento de inscrição com um clique para o cabeçalho list-unsubscribe[(RFC 8058](https://datatracker.ietf.org/doc/html/rfc8058)) fornece uma maneira fácil para os destinatários optarem pela aceitação de e-mails. É possível ajustar essa configuração de cabeçalho para ser aplicada no nível da mensagem em seus e-mails. Para saber mais sobre essa configuração, consulte [Cabeçalho de cancelamento de inscrição de e-mail em espaços de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/email_settings/#email-unsubscribe-header-in-workspaces).

#### Sobre a higienização de e-mails

Visite nosso novo artigo sobre [sanitização]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices/sanitization) para saber mais sobre o processo que ocorre quando o Braze detecta um tipo específico de JavaScript em sua mensagem de e-mail. Seu principal objetivo é impedir que agentes mal-intencionados acessem os dados de sessão de outros usuários do dashboard do Braze.

#### Contagem de inclusão para blocos de conteúdo

Depois de adicionar um bloco de conteúdo em uma campanha ou canvas ativo, é possível fazer [uma prévia desse bloco de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks/) na biblioteca de blocos de conteúdo passando o mouse sobre o bloco de conteúdo e selecionando o ícone <i class="fa fa-eye preview-icon"></i> **Preview**.

#### Status da tela

No dashboard da Braze, seus canvas são agrupados por status. Confira os diferentes [status e descrições do Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/canvas_status) para saber o que eles significam.

### Automação de IA e ML

#### Diretrizes da marca para o assistente de Copywriting de IA

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora é possível criar e aplicar [diretrizes da marca]({{site.baseurl}}/user_guide/brazeai/generative_ai/ai_copywriting/brand_guidelines/) para personalizar o estilo da cópia gerada pelo Assistente de Copywriting IA de acordo com a voz da sua marca. Defina várias diretrizes para diferentes cenários para garantir que seu tom sempre corresponda ao contexto.
 
### Novas parcerias Braze

#### Adikteev - Análise de dados

A integração entre o Braze e [a Adikteev]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/adikteev/) permite aumentar a retenção de usuários, aproveitando a tecnologia de previsão de churn da Adikteev nas campanhas do Braze CRM para direcionar prioritariamente os segmentos de usuários de alto risco.
 
#### Celebrus - Análise de dados
 
A integração da Braze com o [Celebrus]({{site.baseurl}}/partners/data_and_infrastructure_agility/analytics/celebrus) se integra perfeitamente ao SDK da Brazenos canais de aplicativos móveis e da Web, facilitando o preenchimento da Braze com dados de atividade do canal. Isso inclui insights abrangentes sobre o tráfego de visitantes em ativos digitais durante períodos específicos.
 
#### IAM Studio - Modelos de mensagens
 
Com a integração do Braze e do [IAM Studio]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates/iam_studio/), você pode inserir facilmente modelos de mensagens no app personalizáveis em suas mensagens no app do Braze, oferecendo substituição de imagem, modificação de texto, configurações de deep linking, atributos personalizados e configurações de eventos. Usando o IAM Studio, é possível reduzir o tempo de produção de mensagens e dedicar mais tempo ao planejamento de conteúdo.
 
#### Regal - Bate-papo instantâneo

Ao integrar o Braze e [a Regal]({{site.baseurl}}/partners/message_orchestration/additional_channels/messaging/regal/), você pode criar uma experiência mais consistente e personalizada em todos os pontos de contato com o cliente.

#### Dados do Tesouro - Importação de coorte
 
Com a integração entre a Braze e [o Treasure Data]({{site.baseurl}}/partners/data_and_infrastructure_agility/cohort_import/treasuredata/), é possível fazer a importação de coortes de usuários do Treasure Data para a Braze, de modo que seja possível enviar campanhas direcionadas com base em dados que podem existir apenas em seu data warehouse.
 
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
    - Atualizamos a ponte nativa do iOS [do SDK Swift da Braze 7.7.0 para o 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Plug-in Expo 2.1.1](https://github.com/braze-inc/braze-expo-plugin/blob/main/CHANGELOG.md#211)
- [Flutter SDK 10.1.0](https://pub.dev/packages/braze_plugin/changelog)
- [React Native SDK 11.0.0](https://github.com/braze-inc/braze-react-native-sdk/blob/11.0.0/CHANGELOG.md)
- [Swift SDK 9.1.0-9.2.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#920)
- Unity 6.0.0
    - Atualizamos a ponte nativa do iOS [do SDK Swift da Braze 7.7.0 para o 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualizamos a ponte nativa do Android [do SDK da Braze para Android 29.0.1 para o 30.3.0](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
- [Web SDK 5.3.1](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)
- Xamarin SDK Versão 5.0.0
    - Atualizada a vinculação do iOS [do SDK Swift da Braze 8.4.0 para o 9.0.0](https://github.com/braze-inc/braze-swift-sdk/compare/8.4.0...9.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

## Liberação em 30 de abril de 2024

### Permissões para criar ou atualizar listas de códigos promocionais

A partir de abril de 2024, os usuários precisarão da permissão "Access Campaigns, Canvas, Cards, Segments, Media Library" para criar ou atualizar listas de códigos promocionais. Consulte [Gerenciar permissões de funções limitadas e de equipe]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) para obter uma lista de nomes de permissões e suas descrições.

### Flexibilidade de dados

#### Provisionamento SAML just-in-time

{% multi_lang_include release_type.md release="Acesso antecipado" %}

[O provisionamento just-in-time]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/saml_jit) funciona com o SAML SSO para permitir que novos usuários do dashboard criem uma conta Braze em seu primeiro login. Isso elimina a necessidade de os administradores criarem manualmente uma conta para um novo usuário do dashboard, escolherem suas permissões, atribuírem a ele um espaço de trabalho e esperarem que ele ative sua conta.

#### Conjuntos de permissões e funções

Use [conjuntos de permissões]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#permission-sets-and-roles) para agrupar permissões relacionadas a áreas temáticas ou ações específicas. Esses conjuntos de permissões podem ser aplicados aos usuários do dashboard que precisam do mesmo acesso em diferentes espaços de trabalho.

#### Segmentos de ingestão de dados na nuvem

[Os segmentos de ingestão de dados do Braze Cloud]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/cdi_segments) permitem que você escreva consultas de SQL que consultem diretamente seu próprio data warehouse usando dados disponibilizados por meio de suas conexões CDI e criem um grupo de usuários que podem ser direcionados no Braze.

### Liberando a criatividade

### Modelos do Query Builder

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Usando os modelos do criador de consultas, você pode criar relatórios usando dados da Braze do Snowflake. Para acessar os modelos [do criador de consultas]({{site.baseurl}}/user_guide/data_and_analytics/query_builder/), selecione **Modelo de consulta** ao criar um relatório. Todos os modelos apresentam dados até os últimos 60 dias, mas você pode editar diretamente esse e outros valores no editor.

### Dados de performance por segmento

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Você pode detalhar [os dados de performance por segmento]({{site.baseurl}}/user_guide/data_and_analytics/reporting/viewing_and_understanding_segment_data/#performance-data-by-segment) nos modelos de relatório do Query Builder para campanhas, variantes e Canvas e etapas do Canvas por segmentos.

### Canais robustos

#### Encurtamento automático de links para envio de mensagens SMS

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Use o [encurtamento automático de links]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/?tab=manage%20responses#managing-keywords-and-auto-responses) para encurtar automaticamente os URLs estáticos em sua resposta. Isso pode ajudar a moldar sua resposta, pois o contador de caracteres será atualizado para mostrar o tamanho esperado do URL encurtado.

### Novas parcerias Braze

#### Friendbuy - Fidelidade

Aproveite a integração entre Braze e [Friendbuy]({{site.baseurl}}/partners/message_orchestration/channel_extensions/loyalty/friendbuy/) para expandir seus recursos de e-mail e SMS e, ao mesmo tempo, automatizar sem esforço as comunicações de seu programa de indicação e fidelidade. A Braze gerará perfis de clientes para todos os números de telefone de aceitação coletados via Friendbuy.

### NiftyImages - Conteúdo dinâmico

A parceria Braze e [NiftyImages]({{site.baseurl}}/partners/message_personalization/dynamic_content/niftyimages/) permite que você crie imagens dinâmicas e personalizadas para suas campanhas de e-mail mapeando suas tags de personalização Braze existentes para seus URLs NiftyImages.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Android SDK 30.4.0](https://github.com/braze-inc/braze-android-sdk/blob/master/CHANGELOG.md)
- [Plug-in Swift do Braze Segment 2.4.0](https://github.com/braze-inc/braze-segment-swift/blob/main/CHANGELOG.md#240)
- [Flutter SDK 9.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Atualiza a ponte nativa do iOS do [SDK Swift da Braze 7.7.0 para o 8.4.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.7.0...8.4.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - O direcionamento mínimo da implantação do iOS foi atualizado para 12.0.
    - Atualiza a ponte nativa do Android do [SDK da Braze para Android 29.0.1 para o 30.3.0](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.3.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - A versão mínima compatível do Dart é a 2.15.0.
- [React Native SDK 9.2.0](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
- [Swift SDK 8.3.0-8.4.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Swift SDK 9.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
    - Remove os domínios de rastreamento de privacidade padrão do manifesto de privacidade do BrazeKit.
        - Se estiver usando os [recursos de rastreamento de dados]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/privacy_manifest/) do Braze, será necessário adicionar manualmente o ponto de extremidade de rastreamento ao manifesto de privacidade no nível do app.
        - Consulte o [tutorial](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/e1-privacy-tracking) atualizado para obter orientações sobre integração.
    - Remove o obsoleto `BrazeDelegate.braze(_:sdkAuthenticationFailedWithError) method in favor of BrazeSDKAuthDelegate.braze(_:sdkAuthenticationFailedWithError)`.
        - Esse método foi originalmente descontinuado na [versão 5.14.0](https://github.com/braze-inc/braze-swift-sdk/releases/tag/5.14.0).
        - A falha na mudança para o novo método delegado não disparará um erro do compilador; em vez disso, o método `BrazeDelegate.braze(_:sdkAuthenticationFailedWithError)` que você definir simplesmente não será chamado.
- [Xamarin SDK Versão 4.0.3](https://github.com/braze-inc/braze-xamarin-sdk/blob/master/CHANGELOG.md#403)
