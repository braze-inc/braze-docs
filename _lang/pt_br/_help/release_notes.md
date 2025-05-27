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

> O Braze divulga informações sobre atualizações de produtos em uma cadência mensal, alinhando-se com os principais lançamentos de produtos, embora o produto seja atualizado com melhorias diversas semana a semana.
> <br>
> <br>

> Para saber mais sobre qualquer uma das atualizações listadas nesta seção, entre em contato com o gerente da sua conta ou [abra um ticket de suporte]({{site.baseurl}}/user_guide/administrative/access_braze/support/). Você também pode conferir [nossos Changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs) para ver mais informações sobre nossos lançamentos, atualizações e aprimoramentos mensais do SDK.
 
## lançamento de 1 de abril de 2025

### Atualizações na navegação do Braze

A navegação atualizada no Braze foi projetada para ajudá-lo a acessar eficientemente recursos e conteúdo em vários dispositivos. Observe que a opção de alternar entre versões de navegação não está mais disponível. Saiba mais em nosso artigo dedicado [Navegando no Braze]({{site.baseurl}}/user_guide/administrative/access_braze/navigation).

### Descomplicando o Guia do Desenvolvedor

Anteriormente, muitas tarefas em nível de plataforma estavam divididas em várias páginas, como a integração do SDK Swift que estava dividida em seis páginas. Além disso, recursos compartilhados foram documentados individualmente para cada plataforma, o que significa que pesquisar um tópico como "Configuração de Notificações por Push" retornaria 10 páginas diferentes.

**Antes:**

![A documentação anterior do Swift localizada na seção Guias de Integração de Plataforma.]({% image_buster /assets/img/before_swift.png %})

Agora, as tarefas em nível de plataforma foram mescladas em páginas únicas e os recursos compartilhados do SDK agora existem na mesma página (com a ajuda de nosso novo recurso de guia de SDK). Por exemplo, agora há apenas uma página para Integrar o SDK do Braze, onde você pode alternar entre plataformas selecionando uma guia na parte superior da página. Quando você faz isso, até o índice da página será atualizado para refletir a guia atualmente selecionada.

**Depois:**

![A documentação atualizada do Swift localizada na guia Swift do artigo Integrando o SDK.]({% image_buster /assets/img/after_swift.png %})

![A documentação atualizada do Android localizada na guia Android do artigo Integrando o SDK.]({% image_buster /assets/img/after_android.png %})

### Contribuição para a documentação da Braze

Se você não sabia, nossos documentos são totalmente de código aberto! Você pode aprender como em nosso [Guia de Contribuição]({{site.baseurl}}/contributing/home). Este mês, documentamos algumas funcionalidades do site, como [forçar seções a se expandirem automaticamente]({{site.baseurl}}/contributing/content_management/sections#forcing-auto-expand) e [renderizar conteúdo gerado por API]({{site.baseurl}}/contributing/generating_a_preview#step-2-start-a-local-server).

### Flexibilidade de dados

#### Atualização das propriedades de entrada do Canvas

As propriedades de entrada do Canvas agora fazem parte das [variáveis de contexto do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_entry_properties_event_properties). Cada variável de contexto inclui um nome, um tipo de dados e um valor que pode incluir Liquid. Para saber mais, consulte o [componente de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context).

#### Atualizações nos filtros de segmentação para filtros de número de telefone

Os filtros de segmentação foram atualizados para refletir mudanças em dois filtros de número de telefone:

- [Número de telefone não formatado]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#unformatted-phone-number) (anteriormente **Número de telefone**): Segmenta seus usuários pelo número de telefone não formatado.
- [Número de telefone]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#phone-number) (anteriormente **Número de telefone de envio**): Segmenta seus usuários pelo campo de número de telefone E.164 formatado.

#### Excluir dados personalizados

À medida que você cria campanhas e segmentos direcionados, pode descobrir que não precisa mais de um evento personalizado ou atributo personalizado. Agora você pode [excluir esses dados personalizados]({{site.baseurl}}/user_guide/data/custom_data/managing_custom_data#deleting-custom-data) e remover suas referências do seu app.

#### Importar usuários com endereços de e-mail e números de telefone

Agora você pode usar um endereço de e-mail ou número de telefone para [importar usuários]({{site.baseurl}}/user_guide/data/user_data_collection/user_import/#importing-with-email-addresses-and-phone-numbers) e omitir um ID externo ou alias de usuário.

#### Solução de problemas de login iniciado pelo prestador de serviço

O login iniciado pelo Prestador de Serviço (SP) agora tem uma [seção de solução de problemas]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up/#troubleshooting) para ajudá-lo a resolver problemas com SAML e questões de login único.

#### Solução de problemas de importação de usuários

A [seção de solução de problemas de importação de usuários]({{site.baseurl}}/user_guide/data/user_data_collection/user_import#troubleshooting) tem novas entradas e atualizações, incluindo como solucionar linhas ausentes em seus arquivos CSV importados.

#### Perguntas frequentes sobre Extensões de Segmento

Confira nossas [perguntas frequentes]({{site.baseurl}}/user_guide/engagement_tools/segments/segment_extension/#frequently-asked-questions) sobre Extensões de Segmento, incluindo como você pode criar uma Extensão de Segmento que usa vários eventos personalizados.

#### Atrasos personalizados e estendidos

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Você pode configurar um [atraso personalizado]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step#personalized-delays) para seus usuários e usar isso com uma etapa de Contexto para selecionar a variável de contexto a ser atrasada.

Você também pode agora estender etapas de postergação por até dois anos. Por exemplo, se você estiver integrando novos usuários para seu app, pode adicionar uma postergação estendida de dois meses antes de enviar uma etapa de envio de mensagens para incentivar os usuários que não iniciaram uma sessão.

#### Atributos de perfil de usuário padrão para Snowflake

{% multi_lang_include release_type.md release="Beta" %}

Agora existem três [atributos de perfil de usuário padrão]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/snowflake/user_attributes) no Snowflake. Cada visualização é projetada para um caso de uso específico com suas próprias considerações de performance. Por exemplo, você pode receber um instantâneo periódico dos atributos padrão de um perfil de usuário.

### Canais robustos

#### Fundamentos de envio de mensagens

[Fundamentos de Envio de Mensagens]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals) é uma nova seção em Ferramentas de Engajamento que abriga os conceitos e termos compartilhados para campanhas e canva, como arquivamento e localização de mensagens.

#### Domínios personalizados do WhatsApp

Agora você pode atribuir [domínios personalizados]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/custom_domains/) a um ou vários grupos de inscrição do WhatsApp.

#### Mensagens no app acionadas para Canvas

Agora você pode selecionar um [gatilho para suas mensagens no app]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/canvas_by_channel/in-app_messages_in_canvas) para ser acionado no início da sessão, ou por eventos e compras personalizados. Após qualquer postergação passar e as opções de público serem verificadas, as mensagens no app são ativadas quando um usuário chega à etapa de mensagem. Se um usuário iniciar uma sessão e realizar o evento de gatilho para a mensagem no app, o usuário verá a mensagem no app. 

#### Limitar volume de entrada para Canvas

Você pode limitar o número de pessoas que potencialmente entrariam neste Canvas por uma cadência selecionada (diária, duração do Canvas ou toda vez que o Canvas é agendado). Por exemplo, você pode [definir os controles de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas?tab=action-based%20delivery#step-2c-set-your-target-entry-audience) para permitir que o Canvas envie apenas para 5.000 usuários por dia.

#### Novo caso de uso: Sistema de e-mail de lembrete de reserva

Saiba como você pode usar os recursos do Braze para [construir um serviço de mensagens de e-mail de lembrete de reserva]({{site.baseurl}}/user_guide/engagement_tools/canvas/ideas_and_strategies/booking_use_case). O serviço permitirá que os usuários agendem compromissos e enviarão mensagens aos usuários com lembretes de seus compromissos futuros. Embora este caso de uso utilize mensagens de e-mail, você pode enviar mensagens em qualquer canal, ou em múltiplos canais, com base em uma única atualização no perfil do usuário.

#### Rastreamento de cliques para links específicos

Você pode [desativar o rastreamento de cliques]({{site.baseurl}}/user_guide/message_building_by_channel/email/universal_links#turning-off-click-tracking-on-a-link-to-link-basis) para links específicos adicionando código HTML à sua mensagem de e-mail no editor de HTML ou a componentes no editor de arrastar e soltar.

#### Gerenciamento dinâmico do serviço de Notificações por Push da Apple

[O gerenciamento dinâmico do gateway APNs]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=swift#swift_dynamic-apns-gateway-management) melhora a confiabilidade e eficiência das notificações por push do iOS, detectando automaticamente o ambiente APNs correto. Anteriormente, você selecionava manualmente os ambientes APNs (desenvolvimento ou produção) para suas notificações por push, o que às vezes levava a configurações de gateway incorretas, falhas de entrega e erros BadDeviceToken.

#### Suporte Flutter para Cartões Banner

{% multi_lang_include release_type.md release="Acesso antecipado" %}

Os Cartões Banner agora suportam Flutter. Além disso, toda a documentação dos Cartões Banner foi reformulada para facilitar a usabilidade. Confira os seguintes artigos para começar:

- [Sobre os Cartões Banner]({{site.baseurl}}/developer_guide/banner_cards)
- [Como criar campanhas de Cartões Banner]({{site.baseurl}}/developer_guide/banner_cards/creating_campaigns)
- [Como incorporar Cartões Banner em seu app]({{site.baseurl}}/developer_guide/banner_cards/embedding_cards)

#### Rastreamento de cliques do WhatsApp

{% multi_lang_include release_type.md release="Acesso antecipado" %}

[O rastreamento de cliques]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/click_tracking/) permite que você meça quando alguém toca em um link na sua mensagem do WhatsApp—dando a você uma visão clara do que está impulsionando o engajamento. A Braze encurta seus URLs, adiciona rastreamento nos bastidores e registra eventos de cliques à medida que acontecem.

#### Perguntas frequentes sobre push

Confira nosso novo artigo [FAQ sobre Push]({{site.baseurl}}/user_guide/message_building_by_channel/push/faq) que aborda algumas das perguntas mais frequentes que surgem ao configurar campanhas de push.

#### Solução de problemas de push

[Resolução de problemas de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/troubleshooting) fornece uma série de etapas para ajudá-lo a navegar pelos desafios de entrega com notificações por push. Por exemplo, se você está enfrentando desafios de entrega com notificações por push, compilamos etapas que você pode seguir para solucionar o problema.

### Novas parcerias Braze

#### Movable Ink Da Vinci - Conteúdo Dinâmico

A integração Braze e Movable Ink [Da Vinci]({{site.baseurl}}/partners/movable_ink_da_vinci) capacita as marcas a entregar mensagens altamente personalizadas aproveitando o motor de decisão de conteúdo impulsionado por IA do Da Vinci. O Da Vinci seleciona o conteúdo mais relevante para cada usuário e implanta mensagens de forma contínua através do Braze.

### Atualizações do SDK

As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.

- [Flutter SDK 13.0.0](https://pub.dev/packages/braze_plugin/changelog)
    - Atualiza a ponte nativa do Android de [Braze Android SDK 33.0.0 para 35.0.0](https://github.com/braze-inc/braze-android-sdk/compare/v33.0.0...v35.0.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
        - A versão mínima do SDK do Android necessária é 25. Veja mais detalhes [aqui](https://github.com/braze-inc/braze-android-sdk?tab=readme-ov-file#version-information).
- [Swift SDK v11.8.0-11.9.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md)
- [Web SDK v5.8.0](https://github.com/braze-inc/braze-web-sdk/blob/master/CHANGELOG.md)

## Lançamento em 4 de março de 2025

### Prorrogações

A Braze atualizou nossa definição do que é um soft bounce e está enviando um novo evento chamado [adiamentos]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting/#email-performance) a partir de 25 de fevereiro de 2025 às 10h EST.

Para clientes do Sendgrid, fizemos uma alteração para separar os eventos de adiamento dos nossos eventos de soft bounce. Contamos eventos adiados como um evento de soft bounce. Isso impacta qualquer cliente do Sendgrid que use Currents, Query Builder, SQL Extension, Snowflake Data Sharing ou nosso produto de E-mail de Transação.

#### Comportamento anterior

Antes de 25 de fevereiro de 2025, um evento adiado para um endereço de e-mail em uma campanha ou Canvas registra um evento de soft bounce toda vez. Como resultado, os adiamentos são incluídos como parte dos dados de soft bounce. Isso pode resultar em um usuário ou uma campanha relatando mais eventos de soft bounce do que o esperado. 

#### Novo comportamento

A partir de 25 de fevereiro de 2025, um evento adiado não registrará mais um evento de soft bounce toda vez. Em vez disso, registraremos um evento de soft bounce uma vez por envio para o endereço de e-mail, não importa quantas vezes o e-mail seja reencaminhado ou adiado.

#### O que isso significa

Você notará uma queda considerável no volume de eventos de soft bounce a partir de 25 de fevereiro de 2025, resultando nas seguintes mudanças potenciais:

- Diminuição nos soft bounces para quaisquer relatórios construídos usando o Query Builder
- Tamanho de segmento menor usando SQL Extensions se você estiver direcionando usuários que tiveram soft bounces X vezes durante o período Y
- Queda no número de eventos de soft bounce entregues usando Currents e qualquer uma de nossas funcionalidades usando Snowflake
- Queda no número de soft bounces para o produto de e-mail de transação

Para clientes do Sparkpost, não há impacto nos dados de eventos de soft bounce, em vez disso, você começará a receber um novo evento de e-mail, adiamento, em Currents e Snowflake.

### Descomplicando o Guia do Desenvolvedor

Conteúdo idêntico que é compartilhado entre vários SDKs está começando a ser mesclado usando o novo recurso de abas de SDK do site de docs. Este mês [integração de SDK]({{site.baseurl}}/developer_guide/sdk_integration/), [inicialização de SDK]({{site.baseurl}}/developer_guide/sdk_initialization/) e [Cartões de Conteúdo]({{site.baseurl}}/developer_guide/content_cards/) foram combinados. Fique atento para mais atualizações nos próximos meses.

### Flexibilidade de dados
 
#### IDs Braze para perfis de usuário

Um perfil de usuário agora inclui um [ID Braze]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles#user-profiles). Você pode usar isso ao procurar perfis de usuário.

#### Prorrogações

A Braze atualizou nossa definição do que é um soft bounce e está enviando um novo evento chamado [adiamentos]({{site.baseurl}}/user_guide/message_building_by_channel/email/reporting_and_analytics/email_reporting#email-performance), que é quando um e-mail não foi entregue imediatamente, mas a Braze tentará reenviar o e-mail por até 72 horas após essa falha temporária de entrega para maximizar as chances de entrega bem-sucedida antes que as tentativas para essa campanha específica sejam interrompidas.

#### Relacionamentos de entidades Snowflake
 
Mapeamos os [esquemas de tabelas brutas](https://www.braze.com/docs/assets/download_file/data-sharing-raw-table-schemas.txt) para Snowflake e os relacionamentos de entidades Braze para uma nova [página de docs amigável ao usuário](https://www.braze.com/docs/partners/data_and_infrastructure_agility/data_warehouses/snowflake/entity_relationships). Inclui uma divisão das `USER_MESSAGES` tabelas pertencentes a cada canal, bem como descrições para as chaves primárias, estrangeiras e nativas de cada tabela.

#### Gerenciamento de identidade para IDs externos

Usar um endereço de e-mail ou um endereço de e-mail hash como seu ID externo do Braze pode simplificar o gerenciamento de identidade entre suas fontes de dados; no entanto, é importante considerar os [riscos potenciais]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/#identified-user-profiles) para a privacidade do usuário e a segurança dos dados.
 
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

Ao configurar uma etapa de Atraso na jornada do usuário do seu Canvas, você pode agora criar um atraso de até 2 anos.

#### Revertendo a sincronização automática

Ao [compor uma mensagem de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/html_editor/creating_an_email_campaign/#step-3-compose-your-email), você pode reverter para a sincronização automática na guia Plaintext selecionando o ícone Regenerar a partir do HTML, que só aparece se o texto simples não estiver sincronizando.

![O botão de reverter para sincronização automática no Braze.]({% image_buster /assets/img/release_notes/2025_05_04/regenerate_from_html.png %})
 
### Canais robustos

#### Atualizações ao vivo do Android

Embora as Atualizações Ao Vivo não estejam oficialmente disponíveis até
[Android 16](https://android-developers.googleblog.com/2025/01/first-beta-android16.html), nossa página [Atualizações Ao Vivo para Android]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=android&tab=local) mostra como emular seu comportamento, para que você possa exibir notificações interativas na tela de bloqueio semelhantes a [Atividades Ao Vivo para o SDK Swift Braze]({{site.baseurl}}/developer_guide/push_notifications/live_notifications/?sdktab=swift). Ao contrário das Atualizações Ao Vivo oficiais, essa funcionalidade pode ser implementada para versões mais antigas do Android.

#### Copiando campanhas com feature flags entre espaços de trabalho

Agora você pode [copiar campanhas com feature flags entre espaços de trabalho]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/copying_to_workspace/#copying-campaigns-with-feature-flags). Para fazer isso, certifique-se de que o espaço de trabalho de destino tenha um experimento de feature flag configurado com um ID que corresponda à feature flag referenciada na campanha original.

#### Novos tipos de mensagens do WhatsApp suportados

As mensagens do WhatsApp agora suportam [mensagens de vídeo, áudio e documentos de saída]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#outbound-messages). Entre em contato com seu gerente de conta Braze se estiver interessado em participar do acesso antecipado.

#### Mensagens da direita para a esquerda

[Criando mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/) abrange as melhores práticas para elaborar mensagens em idiomas que leem da direita para a esquerda, para que suas mensagens sejam exibidas com precisão o máximo possível.
 
### Automação de IA e ML
 
#### Recomendações de itens

[Usando recomendações de itens em mensagens]({{site.baseurl}}/user_guide/brazeai/recommendations/using_recommendations) abrange o objeto `product_recommendation` Liquid e inclui um tutorial para ajudá-lo a colocar esse conhecimento em prática.

### Novas parcerias Braze
 
#### Email Love - Extensões de Canal
 
A parceria entre Braze e [Email Love]({{site.baseurl}}/partners/message_orchestration/channel_extensions/email_templates) aproveita o recurso Exportar para Braze do Email Love e a API Braze para fazer upload de seus modelos de e-mail para o Braze de forma integrada.

#### VWO - Testes A/B
 
A integração entre Braze e [VWO]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/vwo) permite que você aproveite os dados de experimentos do VWO para criar segmentos segmentados e entregar campanhas personalizadas.
 
### Atualizações do SDK
 
As seguintes atualizações do SDK foram lançadas. As atualizações de última hora estão listadas abaixo; todas as outras atualizações podem ser encontradas verificando os changelogs correspondentes do SDK.
 
- [React Native](https://github.com/braze-inc/braze-react-native-sdk/blob/master/CHANGELOG.md)
    - Aumenta a versão mínima de requisito do React Native para [0.71.0](https://reactnative.dev/blog/2023/01/12/version-071). Para mais informações, consulte [Política de Suporte a Lançamentos](https://github.com/reactwg/react-native-releases#releases-support-policy) no Grupo de Trabalho React.
    - Aumenta a versão mínima do iOS exigida para 12.0.
    - Atualiza os bindings da versão nativa do iOS de [Braze Swift SDK 7.5.0 para 8.1.0](https://github.com/braze-inc/braze-swift-sdk/compare/7.5.0...8.1.0#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).
    - Atualiza os bindings da versão nativa do Android de [Braze Android SDK 29.0.1 para 30.1.1](https://github.com/braze-inc/braze-android-sdk/compare/v29.0.1...v30.1.1#diff-06572a96a58dc510037d5efa622f9bec8519bc1beab13c9f251e97e657a9d4ed).

## lançamento de 4 de fevereiro de 2025

### melhorias na documentação do Braze

#### Guia de Contribuição
Nossas atualizações recentes no [Guia de Contribuição]({{site.baseurl}}/contributing/your_first_contribution) facilitam a contribuição de usuários não técnicos para a documentação do Braze.

#### reforma de Dados e Análises
Para facilitar a sua busca, separamos os artigos anteriormente agrupados sob "Dados & Análises" em [Dados]({{site.baseurl}}/user_guide/data) e [Análises]({{site.baseurl}}/user_guide/analytics). 

#### Guia do desenvolvedor
Fizemos uma grande limpeza em todos os documentos do [Guia do Desenvolvedor Braze]({{site.baseurl}}/developer_guide/home), que incluiu a fusão de "como fazer" que estavam divididos em várias páginas em uma única página.

Há também uma nova [página de referência do SDK]({{site.baseurl}}/developer_guide/references) que lista toda a documentação de referência e repositórios para cada SDK do Braze.

##### SDK do Braze para Unreal Engine
Migramos e reescrevemos todo o conteúdo do README do repositório GitHub do SDK do Braze para Unreal Engine para sua [seção dedicada na documentação do Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unreal%20engine).

### Flexibilidade de dados

#### Painel de uso da API

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

O [painel de uso da API]({{site.baseurl}}/user_guide/analytics/dashboard/api_usage_dashboard) permite monitorar seu tráfego REST API para o Braze e entender suas tendências no uso de nossas APIs REST e solucionar quaisquer problemas potenciais.

#### Adicionando tags a atributos personalizados

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Você pode [adicionar tags a um atributo personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_attributes#adding-tags) após sua criação se tiver a permissão "Gerenciar Eventos, Atributos, Compras". As tags podem então ser usadas para filtrar a lista de atributos.

#### Seleções de catálogo e endpoints de campos de catálogo assíncronos 

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Os seguintes endpoints estão agora geralmente disponíveis:
* [POST: Criar Campos de Catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/post_create_catalog_fields)
* [DELETE: Excluir Campo de Catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_fields/asynchronous/delete_catalog_field)
* [DELETE: Excluir Seleção de Catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/delete_catalog_selection)
* [POST: Criar Seleção de Catálogo]({{site.baseurl}}/api/endpoints/catalogs/catalog_selections/asynchronous/post_create_catalog_selections)

#### Usando um endereço de e-mail para disparar campanhas ou Canvases

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora você pode especificar um destinatário pelo endereço de e-mail para disparar suas [campanhas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/targeting_users) e [canvases]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/?tab=target%20audience#step-2c-set-your-target-entry-audience).

#### Usando um número de telefone para identificar um usuário via a API

{% multi_lang_include release_type.md release="Disponibilidade geral" %}

Agora você pode usar um número de telefone, além de um apelido e endereço de e-mail, para identificar um usuário através do [`/users/identify` ponto de extremidade da API]({{site.baseurl}}/api/endpoints/user_data/post_user_identify)

#### Obtendo um rastreamento SAML
Adicionamos [etapas sobre como obter um rastreamento SAML]({{site.baseurl}}/user_guide/administrative/access_braze/single_sign_on/set_up#obtaining-a-saml-trace), o que ajuda você a resolver problemas sobre SAML SSO com o Suporte de forma mais eficiente.
 
#### Data centers específicos da região
À medida que a Braze está crescendo para atender novas áreas, adicionamos um [artigo sobre os data centers da Braze]({{site.baseurl}}/user_guide/data/data_centers) para esclarecer nossa abordagem operacional.
 
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
Adicionamos novos modelos de Canvas para [integração de usuários com uma pesquisa de preferências]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey) e [criação de um cadastro de e-mail com aceitação dupla]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup).

#### Gerenciando leads com Salesforce Sales Cloud para B2B
Uma maneira de os profissionais de marketing B2B usarem a Braze é através de uma integração com o Salesforce Sales Cloud. Leia mais sobre como implementar este [caso de uso]({{site.baseurl}}/user_guide/getting_started/b2b_use_cases/b2b_salesforce_sales_cloud).
 
### Canais robustos

#### Listas de supressão

{% multi_lang_include release_type.md release="Beta" %}
 
[Listas de supressão]({{site.baseurl}}/user_guide/engagement_tools/segments/suppression_lists) especificam grupos de usuários que nunca receberão mensagens. Os administradores podem criar listas de supressão com filtros de segmento para restringir um grupo de usuários da mesma forma que você faria para segmentação.

### Novas parcerias Braze

#### Construtor - Conteúdo dinâmico
[Construtor]({{site.baseurl}}/partners/message_personalization/dynamic_content/constructor) é uma plataforma de busca e descoberta de produtos que utiliza IA e machine learning para oferecer experiências de busca, recomendações e navegação personalizadas para sites de ecommerce e varejo.
 
#### Trustpilot - Conteúdo dinâmico
[Trustpilot]({{site.baseurl}}/partners/message_personalization/dynamic_content/trustpilot) é uma plataforma de avaliações online que permite que seus clientes compartilhem feedback e permite que você gerencie e responda a avaliações.

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

Adicionamos modelos do Braze Canvas para [inscrição por e-mail com aceitação dupla]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/email_signup/) e [integração com pesquisa de preferências]({{site.baseurl}}/user_guide/engagement_tools/canvas/get_started/braze_templates/preference_survey/).

#### Mudanças na política de aceitação do WhatsApp

A Meta recentemente atualizou sua [política de aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Para informações adicionais, consulte [atualizações de produtos do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/meta_resources/).

#### Ferramenta de largura para Blocos de Conteúdo no editor de arrastar e soltar de e-mail

Você pode [ajustar a largura]({{site.baseurl}}/user_guide/message_building_by_channel/email/drag_and_drop/dnd_content_blocks/#using-the-editor-to-add-a-content-block) do seu Bloco de Conteúdo no editor de e-mail de arrastar e soltar. A largura padrão é 100%.

### Flexibilidade de dados

#### Filtro de segmento de Soft Bounced

Segmente seus usuários de acordo com o número de soft bounces X vezes em Y dias. Para saber mais, consulte [glossário de filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters#soft-bounced).

#### Visão geral de usuários anônimos

[Usuários anônimos]({{site.baseurl}}/user_guide/data/user_data_collection/user_profile_lifecycle/anonymous_users/) fornece uma visão geral de usuários anônimos e aliases de usuários, destacando sua importância e como podem ser aproveitados em suas mensagens.

#### Membro do Grupo de Controle Global

Você pode [visualizar a membresia do Grupo de Controle Global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#view-whether-a-user-is-in-a-global-control-group) acessando a **guia de Engajamento** do perfil de um usuário individual e rolando até a seção **Diversos**.

### Novas parcerias Braze

#### Justuno - Captura de leads

[Justuno]({{site.baseurl}}/partners/data_and_infrastructure_agility/leads_capture/justuno/) permite que você crie experiências de visitante totalmente otimizadas para todos os seus públicos com segmentos dinâmicos, oferecendo o direcionamento mais avançado disponível—tudo isso sem impactar a velocidade do site ou aumentar o trabalho de desenvolvimento.

#### Odicci - Plataforma de dados do cliente

Integre Braze com [Odicci]({{site.baseurl}}/partners/message_personalization/dynamic_content/odicci/), uma plataforma que capacita empresas a adquirir, engajar e reter clientes por meio de experiências omnicanal impulsionadas pela fidelidade.

#### Optimizely - Testes A/B

A integração entre Braze e [Optimizely]({{site.baseurl}}/partners/data_and_infrastructure_agility/ab_testing/optimizely/) é uma integração bidirecional que permite que você:

- Sincronize seus segmentos e eventos de cliente Braze com a Plataforma de Dados Optimizely (ODP) todas as noites para enriquecer os perfis de cliente, relatórios e segmentação da Optimizely.
- Envie eventos Braze Currents do Braze para a ferramenta de relatórios da Optimizely.
- Sincronize os dados de cliente e eventos do ODP com o Braze para enriquecer seus dados de cliente Braze e disparar o envio de mensagens Braze com base em eventos de cliente no ODP.

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

Use o [depurador integrado do Braze SDK]({{site.baseurl}}/developer_guide/debugging/) para solucionar problemas dos seus canais com SDK sem precisar ativar o registro detalhado no seu aplicativo.

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

[Conecte seu próprio domínio]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/customizing_urls/) ao espaço de trabalho do Braze para personalizar os URLs da landing page com sua marca.

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

Usando a [ criptografia no nível do campo do identificador]({{site.baseurl}}/user_guide/analytics/field_level_encryption/), é possível criptografar perfeitamente os endereços de e-mail com o AWS Key Management Service (KMS) para minimizar as informações de identificação pessoal (IPI) compartilhadas no Braze. A criptografia substitui dados confidenciais por texto cifrado, que é uma informação criptografada ilegível.

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

O [dashboard de uso de mensagens]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_campaign_analytics/message_usage/) fornece insights de autoatendimento sobre o uso de créditos de SMS e WhatsApp para uma visão abrangente do uso histórico e atual em comparação com as atribuições do contrato. Essas percepções podem reduzir sua confusão e ajudá-lo a fazer ajustes para prevenir riscos de excedente.

### SDK

#### Postergação da inicialização do Braze Swift SDK

Configure a [inicialização postergada]({{site.baseurl}}/developer_guide/sdk_initalization/?sdktab=swift) para inicializar o SDK do Braze Swift de forma assíncrona e, ao mesmo tempo, garantir que o tratamento das notificações por push seja preservado. Isso pode ser útil quando for necessário configurar outros serviços antes de inicializar o SDK, como buscar dados de configuração de um servidor ou aguardar o consentimento do usuário.

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
