---
nav_title: Criação de uma mensagem SMS
article_title: Criação de uma mensagem SMS
page_order: 5
description: "Este artigo de referência aborda as etapas envolvidas no desenvolvimento e na criação de uma mensagem SMS."
page_type: reference
alias: /create_sms_message/
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# Criação de uma mensagem SMS

> As campanhas de SMS são excelentes para alcançar diretamente e conversar de forma programática com seus clientes. Você pode usar o Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promova e aprimore uma experiência discreta do usuário com a sua marca. 

## Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canvas? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto os Canvases são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campaign %}

**Passos:**

1. Vá para **Messaging** > **Campaigns** ( **Mensagens** > **Campanhas** ) e selecione **Create Campaign (Criar campanha**).
2. Selecione **SMS** ou, para campanhas direcionadas a vários canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para obter mais informações sobre esse tópico, consulte [Testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Selecione um [grupo de assinatura]({{site.baseurl}}/sms_rcs_subscription_groups/) para garantir o envio da mensagem aos usuários adequados. Ao selecionar um grupo de assinatura, o Braze adicionará automaticamente um filtro de segmentação, garantindo que somente os usuários inscritos recebam a campanha. Somente os códigos longos e curtos que pertencem a esse grupo de assinatura serão usados para enviar SMS aos usuários-alvo.

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, componha sua mensagem antes de adicionar outras variantes. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Passos:**

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o compositor de Canvas.
2. Depois de configurar seu Canvas, adicione uma etapa no construtor do Canvas. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique um atraso conforme necessário.
4. Filtre seu público para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e acrescentando filtros adicionais. As opções de público serão verificadas após o atraso no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento de avanço]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de mensagens que você gostaria de associar à sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Componha sua mensagem SMS

Escreva sua mensagem usando idiomas e personalização (Liquid, Connected Content e emojis) conforme necessário. Certifique-se de respeitar nossos limites de cópia de mensagem para reduzir suas chances de cobranças por excesso.

{% alert important %}
Antes de continuar, leia nossas diretrizes para [segmentos de mensagens SMS e limites de cópia]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/). Os segmentos de mensagens SMS são os lotes de caracteres que as operadoras de telefonia usam para medir as mensagens de texto. As mensagens são cobradas por segmento de mensagem, portanto, é uma boa ideia entender as nuances de como as mensagens serão divididas.
{% endalert %}

\![Compositor de SMS no Braze com a mensagem "Hi first_name, we appreciate your support! Por que não passar em uma de nossas lojas e mostrar este SMS para obter um desconto exclusivo? Responda STOP para parar de receber nossas mensagens."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Adição de um cartão de contato

Você pode adicionar um cartão de contato à sua mensagem SMS para facilitar aos clientes a inclusão de suas informações comerciais e de contato nos contatos deles. Você pode atribuir propriedades comuns a esses cartões, como o nome da empresa, o número de telefone, o endereço, o e-mail e uma pequena foto. Consulte [os cartões de contato]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) para saber mais.

### Dicas

#### Usando líquido

{% raw %}
Se você planeja usar o Liquid, certifique-se de incluir um valor padrão para a personalização escolhida para que, caso o perfil do usuário do destinatário esteja incompleto, ele não receba um espaço reservado em branco `Hi, !`, em vez do nome ou de uma frase coerente.
{% endraw %}

#### Geração de cópia de IA

Precisa de ajuda para criar um texto incrível? Tente usar o [assistente de redação de IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto e a IA gerará um texto de marketing semelhante ao humano para ser usado em suas mensagens.

Abra o botão AI Copywriter, localizado no campo Message (Mensagem) do compositor de SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Criação de mensagens da direita para a esquerda

A aparência final das mensagens da direita para a esquerda depende muito de como os provedores de serviços as processam. Para obter práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Etapa 3: Visualize e teste sua mensagem

A Braze sempre recomenda que você visualize e teste sua mensagem antes de enviá-la. Mude para a guia **Teste** para enviar um SMS de teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, ou visualize a mensagem como um usuário diretamente no Braze.

Visualização da cópia do SMS na guia Teste do compositor. Na seção de perfil, o campo First Name está definido como "James". Na seção de visualização, o SMS agora diz "Hi James, we appreciate your support!".]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
Se você quiser testar em quantos segmentos o seu SMS pode ser dividido, teste o tamanho da sua cópia com a nossa [calculadora de segmentos de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).
{% endalert %}

## Etapa 4: Crie o restante de sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

Em seguida, crie o restante de sua campanha. Consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar mensagens SMS.

#### Escolha o cronograma de entrega ou o acionador

As mensagens SMS podem ser entregues com base em um horário programado, em uma ação ou em um acionador de API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para a entrega baseada em ação, você também pode definir a duração da campanha e o [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Nessa etapa, também é possível especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha ou ativar regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários a serem alvos

Em seguida, você precisa [segmentar os usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você já deve ter escolhido o grupo de assinatura, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você. 

{% multi_lang_include target_audiences.md %}

Nessa etapa, você selecionará o público-alvo maior de seus segmentos e restringirá ainda mais esse segmento com nossos filtros, se desejar. Você receberá automaticamente uma prévia de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes de a mensagem ser enviada.

{% alert tip %}
Tem interesse em SMS retargeting? Acesse nosso [artigo sobre]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) SMS [retargeting]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) para saber mais.
{% endalert %}

#### Selecionar eventos de conversão

O Braze permite que você rastreie a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso de sua campanha. Por exemplo:

- Se estiver usando o geotargeting para acionar uma mensagem SMS que tenha como objetivo final que o usuário faça uma compra, defina o evento de conversão como `Purchase`.
- Se estiver tentando direcionar o usuário para o seu aplicativo, defina o evento de conversão como `Starts Session`.

Você também pode definir eventos de conversão personalizados com base em seu caso de uso específico. Seja criativo e pense em como você realmente deseja medir o sucesso dessa campanha.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canvas. Para obter mais detalhes sobre como criar o restante do seu Canvas, implementar testes multivariados e Intelligent Selection e muito mais, consulte a etapa [Criar seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) da nossa documentação do Canvas.

{% endtab %}
{% endtabs %}

## Etapa 5: Revisão e implementação

Depois de terminar de criar a última parte de sua campanha ou Canvas, revise seus detalhes, teste-a e envie-a!

Em seguida, confira [os relatórios de SMS]({{site.baseurl}}/sms_mms_rcs_reporting/) para saber como acessar os resultados de suas campanhas de SMS.
