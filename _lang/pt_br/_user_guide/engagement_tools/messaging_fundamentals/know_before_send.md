---
nav_title: Saiba antes de enviar
article_title: Saiba antes de enviar
description: "Depois de visitar nosso guia de pré-lançamento, consulte esta lista final de verificações ou \"pegadinhas\" para cartões de conteúdo, e-mail, mensagens no aplicativo, push e SMS."
alias: /know_before_send/
page_order: 10.2
tool:
    - Campaigns
    - Canvas
---

# Saiba antes de enviar: canais

Lance suas campanhas e Canvases com confiança! Consulte esta lista final de verificações ou "pegadinhas" para Content Cards, e-mail, mensagens no aplicativo, push e SMS.

{% alert note %}
Embora forneçamos uma extensa lista de recursos para consulta antes do envio, cada canal tem nuances individuais que continuam a crescer à medida que desenvolvemos nossos produtos. As verificações listadas abaixo são sugestões úteis, e recomendamos testar exaustivamente suas campanhas e grandes envios antes de enviar.
{% endalert %}

## Geral

#### Coisas a verificar
- [**Limites de taxa de API**](https://braze.com/resources/articles/whats-rate-limiting): Revise os [limites de taxa]({{site.baseurl}}/api/api_limits/) da API do Braze para seus espaços de trabalho para evitar erros. Se você deseja aumentar seus limites de taxa (e já está agrupando solicitações), entre em contato com seu gerente de sucesso do cliente. Lembre-se de que esse processo requer tempo de espera, portanto, planeje-se adequadamente.
- [**Substituições necessárias do limite de frequência**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping): Há algumas campanhas, como mensagens transacionais, que você desejará que sempre cheguem ao usuário, mesmo que já tenha atingido o limite de frequência (por exemplo, uma notificação de entrega). Se quiser que uma determinada campanha substitua as regras de limite de frequência, você poderá configurar isso no painel do Braze ao programar a entrega dessa campanha, desativando o limite de frequência.

#### Coisas para saber
- [**Grupos de controle global**]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group#global-control-group): Se você estiver usando um grupo de controle global, uma porcentagem de usuários não receberá nenhuma campanha ou Canvases. (Você pode criar exceções com [configurações de exclusão]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/#step-3-assign-exclusion-settings)). Para ver uma lista desses usuários, exporte-os via CSV ou [API]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/).
- [**Limites de taxa de tela**]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#rate-limiting): Em um Canvas, o limite de taxa se aplica a todo o Canvas, não às etapas individuais. Por exemplo, se você definir um limite de taxa de 10.000 mensagens por minuto em um Canvas com várias etapas, ele ainda será limitado a 10.000 mensagens porque o limite terá sido atingido na primeira etapa.
- **Limite de frequência**: 
  - As regras de limite de frequência serão aplicadas a push, e-mail, SMS e webhooks, mas não a mensagens in-app e Content Cards.
  - O limite de frequência global é programado com base no fuso horário do usuário e é calculado por dias do calendário, não por períodos de 24 horas. Por exemplo, se você configurar uma regra de limite de frequência para enviar no máximo uma campanha por dia, um usuário poderá receber uma mensagem às 23h em seu fuso horário local e estará qualificado para receber outra mensagem uma hora depois.

{% alert tip %}
Para obter mais assistência com a solução de problemas do Canvas e da campanha, entre em contato com o Suporte da Braze dentro de 30 dias após a ocorrência do problema, pois só temos os registros de diagnóstico dos últimos 30 dias.
{% endalert %}

## E-mail

#### Coisas a verificar
- **Consentimento do cliente**: Antes de enviar seus e-mails iniciais, é importante obter a permissão de seus clientes. Consulte [Consentimento e coleta de endereços]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/consent_and_address_collection/) e nossa [Política de uso aceitável do Braze](https://www.braze.com/company/legal/aup) para obter mais informações.
- **Volume previsto**: 2 milhões de e-mails por dia para um único IP é a recomendação geral, desde que esse volume tenha sido [adequadamente aquecido]({{site.baseurl}}/user_guide/onboarding_with_braze/email_setup/ip_warming#ip-warming). 
  - Se você planeja enviar consistentemente um volume maior do que esse, para evitar que os provedores limitem o recebimento de e-mails, o que resultará em uma grande quantidade de devoluções, menor taxa de entregabilidade e menor reputação do IP, considere o uso de vários endereços IP agrupados em um pool de IPs. 
  - Se você pretende enviar apenas em um período de tempo mais curto, recomendamos que verifique a rapidez com que os diferentes provedores aceitam e-mails para avaliar o número adequado de IPs a partir dos quais enviar. 

#### Coisas para saber
- **Envio de fatores de volume**: Alguns fatores que determinam os volumes de envio capazes para um IP incluem:
  - Caixas de correio: Os grandes provedores de e-mail provavelmente conseguem lidar com milhões por dia a partir de um único IP, enquanto um provedor de caixa de correio regional menor ou com uma infraestrutura menor talvez não consiga lidar com essa quantidade.
  - Reputação do remetente: Você poderá enviar um volume maior por dia a partir de um único IP se o remetente estiver preparado para esse volume e se a reputação do remetente for forte o suficiente em cada caixa de correio ou domínio para o qual ele está enviando.
- **Práticas recomendadas**: Analise [as práticas recomendadas]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) do Braze [Email]({{site.baseurl}}/user_guide/message_building_by_channel/email/best_practices) e entre em contato com a Equipe de Contas Braze se quiser saber mais sobre os serviços de entregabilidade.

## Empurrar

#### Coisas a verificar
- [**Ativado/subscrito e com push ativado**]({{site.baseurl}}/user_guide/message_building_by_channel/push/users_and_subscriptions/): Para que os usuários recebam uma mensagem push do Braze, eles precisam que seus status de assinatura sejam opt-in (iOS) ou subscribed (Android) e `Push Enabled = True`. Observe que o Android 13 introduz uma grande mudança na forma como os usuários gerenciam os aplicativos que enviam notificações push. O [guia de atualização]({{site.baseurl}}/developer_guide/platforms/android/android_13/) do Braze [Android 13 SDK]({{site.baseurl}}/developer_guide/platforms/android/android_13/) continuará a ser atualizado à medida que novas versões beta do Android 13 forem lançadas.

#### Coisas para saber
- **Web push**: Se você tiver o Braze [Web SDK configurado]({{site.baseurl}}/user_guide/message_building_by_channel/push/web), considere utilizar o Web push para envolver os usuários. O Web Push funciona da mesma forma que as notificações push de aplicativos funcionam em seu telefone. Para obter mais informações sobre a composição de um push da Web, consulte [Criação de uma notificação por push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#creating-a-push-message).
- **Direcionamento para um único aplicativo**: Analise as [diferenças na segmentação]({{site.baseurl}}/developer_guide/platform_wide/app_group_configuration/#targeting-a-singular-app) para atingir um aplicativo específico e seus usuários.

## SMS

#### Coisas a verificar
- **Alocações e rendimento**: Entenda quais alocações de SMS estão atualmente vinculadas à sua conta (código curto, código longo e similares) e [a quantidade de taxa de transferência que isso lhe proporciona]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) para confirmar que você tem taxa de transferência suficiente para enviar no tempo desejado.
- **Estimativa de segmento a partir da cópia do SMS**: Teste sua cópia de SMS na [calculadora de segmento de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#things-to-keep-in-mind-as-you-create-your-copy). Lembre-se de que o número de segmentos de SMS deve ser levado em consideração com seus recursos de taxa de transferência. (Público * segmentos de SMS = taxa de transferência necessária). Consulte as Perguntas frequentes sobre SMS para saber como [evitar excedentes]({{site.baseurl}}/sms_faq/).
- **Leis e regulamentos de SMS**: [Analise as leis, os regulamentos e a prevenção de abuso de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) para confirmar que você está usando os serviços de SMS em conformidade com todas as leis aplicáveis. Certifique-se de que você deve buscar a orientação de seu advogado antes de enviar.

#### Coisas para saber
- **Padrão de mensagens SMS**: Normalmente, as mensagens SMS são enviadas por padrão a partir do código curto no pool de remetentes.
- **ID alfanumérica do remetente**: As mensagens bidirecionais não funcionarão mais se você usar uma ID de remetente alfanumérica; agora elas são apenas unidirecionais.
- **Produção atualizada nos EUA**: A taxa de transferência mudou nos EUA com o [registro](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US) US [A2P 10DLC](https://support.twilio.com/hc/en-us/articles/1260803225669-Message-throughput-MPS-and-Trust-Scores-for-A2P-10DLC-in-the-US). Observe que não nos comprometemos com nenhum SLA de velocidade de envio contratualmente devido a vários fatores, como congestionamento de tráfego e problemas com a operadora, que podem afetar as taxas de entrega reais.
- **Grupo de assinaturas**: Para lançar uma campanha de SMS por meio do Braze, um grupo de assinatura deve ser selecionado. Além disso, para aderir à [conformidade e]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) às [diretrizes]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/) internacionais [de telecomunicações]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/), o Braze nunca enviará SMS a usuários que não tenham [se inscrito no grupo de assinatura selecionado]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#how-to-check-a-users-sms-subscription-group).

## WhatsApp

#### Coisas para saber

- [**Melhores práticas**]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_best_practices/): Analise nossas práticas recomendadas sugeridas para o WhatsApp.

## Banners

#### Coisas a verificar
- **Dimensões do banner:** Crie seus Banners usando um elemento de dimensão fixa e teste-os no editor.
- **Prioridade:** Se estiver lançando vários Banners, você poderá definir manualmente a prioridade de exibição de cada banner.

#### Coisas para saber
- **Personalização líquida:** A personalização líquida é atualizada a cada solicitação de atualização.
- **Proporção de posicionamento e banner:** Cada posicionamento de banner pode ser usado em até 10 campanhas em um espaço de trabalho.  
- **Cliques e impressões:** Os cliques e as impressões de Banners são rastreados automaticamente com o SDK.
- **Limitações:**  Atualmente, não há suporte para os seguintes recursos: Integração com o Canvas, campanhas acionadas por API e baseadas em ações, Connected Content, códigos promocionais, demissões controladas pelo usuário e `catalog_items` usando a [tag`:rerender` ]({{site.baseurl}}/user_guide/data/activation/catalogs/using_catalogs/#using-liquid).
- **Testes:** Para exibir o banner de teste, o dispositivo que você está usando deve ser capaz de receber notificações push em primeiro plano.
- **HTML personalizado:** Aproveite a [ponte JS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/html_in-app_messages/#javascript-bridge) para registrar cliques ao usar HTML personalizado para definir ações de clique, como links e botões. As ações de clique só são registradas automaticamente ao usar os componentes pré-criados no editor de arrastar e soltar.
- **Solicitação de colocações:** Até 10 posicionamentos podem ser retornados ao SDK em uma única solicitação de atualização. Cada colocação incluirá o banner de prioridade mais alta para o qual o usuário está qualificado.

## Cartões de conteúdo

#### Coisas a verificar
- **Tamanho do cartão de conteúdo**: Os campos de mensagem do Content Card são limitados a 2 KB em tamanho de pré-compressão, calculado pela adição do tamanho em bytes dos seguintes campos: título, mensagem, URL da imagem, texto do link, URLs do link e pares de valores-chave. As mensagens que excederem esse tamanho não serão enviadas. Observe que isso não inclui o tamanho da imagem, mas sim o comprimento do URL da imagem.
- **Atualização da cópia após o envio**: Depois que um cartão for enviado, você não poderá atualizar a cópia nesse mesmo cartão. Consulte [Atualização de cartões enviados]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/#updating-sent-cards) para entender como você pode abordar esse cenário.

#### Coisas para saber
- **Limite de campanhas do Content Card ativo**: Você pode ter até 500 campanhas ativas do Content Card. Essa contagem inclui Cartões de conteúdo enviados com qualquer opção de [criação de cartão]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/card_creation/).  
- [**Termos de relatório**]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/reporting/): Revise termos como total de impressões, impressões exclusivas e destinatários exclusivos, pois as definições às vezes podem causar confusão.
- **Atualização do cartão de conteúdo**: Por padrão, o Braze atualiza as solicitações do Content Card à medida que elas são sincronizadas no início da sessão, ao deslizar o dedo para baixo no feed (celular) e quando a visualização dos cartões é aberta se a última atualização tiver ocorrido há mais de um minuto.
- **Armazenamento em cache de cartões de conteúdo**: As opções de cache do Content Card podem ser encontradas em nossos documentos [do Android/FireOS]({{site.baseurl}}/developer_guide/platform_integration_guides/android/content_cards/customization/custom_styling/#customizing-card-rendering-for-android) e [da Web](https://js.appboycdn.com/web-sdk/latest/doc/modules/appboy.html#getcachedcontentcards). 
- **Limite de frequência**: O limite de frequência não se aplica aos cartões de conteúdo.
- **Impressões**: As impressões são geralmente registradas quando um cartão é visto. Por exemplo, se você tiver uma caixa de entrada cheia de Content Cards, uma impressão não será registrada até que o usuário role a tela até o Content Card específico. Há algumas nuances entre as plataformas Web, Android e iOS.  

## Mensagens no aplicativo

#### Coisas para saber
- **Acionamento de mensagens no aplicativo**: No início da sessão, o SDK solicita que todas as mensagens in-app elegíveis sejam enviadas para o dispositivo junto com seus acionadores, de modo que, se o evento for realizado durante a sessão, ele poderá receber a mensagem in-app de forma rápida e confiável.
- **Enviadas versus impressões**: Para mensagens in-app, o conceito de "enviado" é diferente dos outros canais disponíveis. Para ver uma mensagem in-app, o usuário precisa iniciar uma sessão, estar no público-alvo qualificado e executar o acionador. Por esse motivo, rastreamos as "impressões", pois elas são mais claras.
- **Acionamento**: Por padrão, as mensagens in-app são acionadas por eventos registrados pelo SDK. Se quiser acionar mensagens no aplicativo por meio de eventos enviados pelo servidor, você também poderá fazer isso por meio destes guias para [iOS]({{site.baseurl}}/developer_guide/in_app_messages/triggering_messages/?tab=swift) e [Android]({{site.baseurl}}/developer_guide/in_app_messages/customization/?sdktab=android).
- [Mensagens no aplicativo Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/in-app_messages_in_canvas/#advancement-behavior-options): Essas mensagens aparecem na primeira vez que o usuário abre o aplicativo (acionado pela sessão inicial) depois que a mensagem programada no componente Canvas é enviada a ele.
- **Chamadas de conteúdo conectado**: O uso do Connected Content permite que você envie conteúdo dinâmico em mensagens. Quando você envia mensagens por meio de um canal como as mensagens no aplicativo, isso pode criar mais conexões simultâneas com os dispositivos dos usuários (as mensagens são enviadas uma a uma, em vez de em lotes). Para gerenciar isso, recomendamos [limitar a taxa de]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting) suas mensagens.
