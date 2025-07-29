---
nav_title: Criação de uma mensagem SMS
article_title: Criação de uma mensagem SMS
page_order: 5
description: "Este artigo de referência aborda as etapas envolvidas na construção e criação de uma mensagem SMS."
page_type: reference
alias: /create_sms_message/
tool:
  - Campaigns
channel:
  - SMS
search_rank: 1
---

# Criação de uma mensagem SMS

> As campanhas de SMS são excelentes para alcançar diretamente e conversar de forma programática com seus clientes. É possível usar o Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promova e aprimore uma experiência discreta do usuário com sua marca. 

## Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canva? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto as canvas são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campanha %}

**Etapas:**

1. Acesse **Envio de mensagens** > **Campanhas** e selecione **Criar campanha**.
2. Selecione **SMS** ou, para campanhas com direcionamento para vários canais, selecione **Multicanal**.
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [times]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas. Por exemplo, ao usar o [Report Builder]({{site.baseurl}}/user_guide/analytics/reporting/report_builder/), você pode filtrar por tags específicas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para saber mais sobre esse tópico, consulte [Testes multivariantes e testes A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).
6. Selecione um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) para garantir o envio da mensagem para os usuários adequados. Ao selecionar um grupo de inscrições, o Braze adicionará automaticamente um filtro de segmentação, garantindo que apenas os usuários inscritos recebam a campanha. Somente os códigos longos e curtos que pertencem a esse grupo de inscrições serão usados para enviar SMS aos usuários direcionados.

{% alert tip %}
Se todas as mensagens em sua campanha forem semelhantes ou tiverem o mesmo conteúdo, crie sua mensagem antes de adicionar variantes adicionais. Em seguida, você pode selecionar **Copiar da variante** no menu suspenso **Adicionar variante**.
{% endalert %}

{% endtab %}
{% tab Canvas %}

**Etapas:**

1. [Crie seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) usando o criador do Canvas.
2. Depois de configurar seu canvas, adicione uma etapa no construtor do canva. Dê um nome claro e significativo à sua etapa.
3. Escolha uma [programação de etapas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/time_based_canvas/#schedule-delay) e especifique uma postergação, conforme necessário.
4. Filtre seu público para esta etapa, conforme necessário. Você pode refinar ainda mais os destinatários dessa etapa especificando segmentos e adicionando filtros adicionais. As opções de público serão verificadas após a postergação no momento em que as mensagens forem enviadas.
5. Escolha seu [comportamento para avançar]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/advancement/).
6. Escolha quaisquer outros canais de envio de mensagens que gostaria de associar à sua mensagem.

{% endtab %}
{% endtabs %}

## Etapa 2: Crie sua mensagem SMS

Escreva sua mensagem usando idiomas e personalização (Liquid, conteúdo conectado e emojis) conforme necessário. Certifique-se de respeitar nossos limites de cópia de mensagens para reduzir suas chances de cobranças excedentes.

{% alert important %}
Antes de continuar, leia nossas diretrizes para [segmentos de mensagens SMS e limites de cópia]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/). Os segmentos de mensagens SMS são os lotes de caracteres que as operadoras telefônicas usam para medir as mensagens de texto. As mensagens são cobradas por segmento de mensagem, portanto, é uma boa ideia entender as nuances de como as mensagens serão divididas.
{% endalert %}

![Criador de mensagem SMS na Braze com a mensagem "Olá, first_name, agradecemos seu apoio! Por que não passar em uma de nossas lojas e mostrar este SMS para obter um desconto exclusivo? Responda STOP para parar de receber nossas mensagens."]({% image_buster /assets/img/sms_campaign_compose.png %})

### Adição de um cartão de contato

É possível adicionar um cartão de contato à sua mensagem SMS para facilitar aos clientes a inclusão da sua empresa e das informações de contato nos contatos deles. É possível atribuir propriedades comuns a esses cartões, como o nome da empresa, o número de telefone, o endereço, o e-mail e uma pequena foto. Confira os [cartões de contato]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/contact_card/) para saber mais.

### Dicas

#### Usando Liquid

{% raw %}
Se planeja usar o Liquid, certifique-se de incluir um valor padrão para a personalização escolhida para que, caso o perfil do usuário do destinatário esteja incompleto, ele não receba um espaço reservado em branco `Hi, !`, em vez do nome ou de uma frase coerente.
{% endraw %}

#### Geração de cópia de IA

Precisa de ajuda para criar um texto incrível? Tente usar o [Assistente de Copywriting da IA]({{site.baseurl}}/user_guide/brazeai/generative_ai/copywriting/). Insira o nome ou a descrição de um produto e a IA gerará uma cópia de marketing semelhante à humana para uso em seu envio de mensagens.

![Botão "Abrir AI Copywriter", localizado no campo Mensagem do criador de mensagens SMS.]({% image_buster /assets/img/ai_copywriter/ai_copywriter_sms.png %}){: style="max-width:60%"}

#### Criação de mensagens da direita para a esquerda

A aparência final das mensagens da direita para a esquerda depende muito de como os prestadores de serviço as processam. Para obter práticas recomendadas sobre o envio de mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Etapa 3: Pré-visualize e teste sua mensagem

O Braze sempre recomenda que você faça uma prévia e teste sua mensagem antes de enviá-la. Alterne para a guia **Test (Teste** ) para enviar um SMS de teste para [grupos de teste de conteúdo]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#content-test-groups) ou usuários individuais, ou faça uma prévia da mensagem como um usuário diretamente no Braze.

![Pré-visualização da cópia do SMS na guia Teste do criador. Na seção de perfil, o campo Nome está definido como "James". Na seção de prévia, o SMS agora diz "Olá, James, agradecemos seu apoio!"]({% image_buster /assets/img/sms_campaign_test.png %})

{% alert tip %}
Se você quiser testar em quantos segmentos o seu SMS pode ser dividido, teste o tamanho da sua cópia com a nossa [calculadora de segmentos de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).
{% endalert %}

## Etapa 4: Crie o restante de sua campanha ou Canva

{% tabs %}
{% tab Campanha %}

Em seguida, crie o restante de sua campanha. Consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar mensagens SMS.

#### Escolha a programação ou o disparo da entrega

As mensagens SMS podem ser enviadas com base em um horário programado, em uma ação ou em um disparo da API. Para obter mais informações, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

Para entrega baseada em ação, você também pode definir a duração da campanha e o [Horário de silêncio]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

Nessa etapa, também é possível especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha ou ativar regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping).

#### Escolha os usuários a serem direcionados

Em seguida, é necessário direcionar [os usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você já deve ter escolhido o grupo de inscrições, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você. Nessa etapa, você selecionará o público maior de seus segmentos e restringirá ainda mais esse segmento com nossos Filtros, se desejar. Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento de mensagens é sempre calculada imediatamente antes do envio da mensagem.

{% alert tip %}
Tem interesse em redirecionamento por SMS? Acesse nosso [artigo sobre redirecionamento]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/retargeting/) de SMS para saber mais.
{% endalert %}

#### Selecionar eventos de conversão

O Braze permite rastrear a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso de sua campanha. Por exemplo:

- Se estiver usando o geotargeting para disparar uma mensagem SMS que tenha como objetivo final que o usuário faça uma compra, defina o evento de conversão como `Purchase`.
- Se estiver tentando direcionar o usuário para o seu app, defina o evento de conversão como `Starts Session`.

Também é possível definir eventos personalizados de conversão com base em seu caso de uso específico. Seja criativo e pense em como você realmente deseja medir o sucesso dessa campanha.

{% endtab %}

{% tab Canvas %}

Se ainda não tiver feito isso, conclua as seções restantes do seu componente do Canva. Para obter mais detalhes sobre como criar o restante de seu Canvas, implementar testes multivariantes e Intelligent Selection e muito mais, consulte a etapa [Construir seu Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-3-build-your-canvas) de nossa documentação do Canvas.

{% endtab %}
{% endtabs %}

## Etapa 5: Revisão e implementação

Depois de terminar de criar a última parte de sua campanha ou Canva, revise seus detalhes, teste-a e envie-a!

Em seguida, confira [os relatórios de SMS]({{site.baseurl}}/sms_mms_rcs_reporting/) para saber como acessar os resultados de suas campanhas de SMS.
