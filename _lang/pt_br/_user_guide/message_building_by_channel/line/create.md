---
nav_title: Criação de uma mensagem LINE
article_title: Criação de uma mensagem LINE
page_order: 1
description: "Este artigo aborda como criar uma campanha de mensagem LINE ou Canvas."
page_type: reference
tool:
 - Campaigns
channel:
 - LINE
alias: /line/create/
---

# Criação de uma mensagem LINE

> As campanhas do LINE podem alcançar diretamente e conversar de forma programática com seus clientes. Você pode usar o Liquid e outros conteúdos dinâmicos para criar uma experiência pessoal com seus usuários e criar um ambiente que promova e aprimore uma experiência discreta do usuário com a sua marca.

## Pré-requisitos

Antes de criar uma mensagem LINE, faça o seguinte:

1. Leia a visão geral do LINE.
2. Reconhecer políticas, limites e regras de conteúdo.
3. [Configure sua conexão LINE]({{site.basesurl}}/user_guide/message_building_by_channel/line/line_setup/).

O envio de mensagens LINE a partir do Braze será feito com os créditos de mensagens de sua conta.

## Etapa 1: Escolha onde construir sua mensagem

Não tem certeza se sua mensagem deve ser enviada por meio de uma campanha ou de um Canvas? As campanhas são melhores para campanhas de mensagens únicas e simples, enquanto os Canvases são melhores para jornadas de usuários em várias etapas.

{% tabs %}
{% tab Campaign %}

**Passos:**

1. Vá para **Messaging** > **Campaigns** ( **Mensagens** > **Campanhas** ) e selecione **Create Campaign (Criar campanha**).
2. Selecione **LINE** ou, para campanhas direcionadas a vários canais, selecione **Multichannel Campaign (Campanha multicanal**).
3. Dê à sua campanha um nome claro e significativo.
4. Adicione [equipes]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/teams/) e [tags]({{site.baseurl}}/user_guide/administrative/app_settings/tags/) conforme necessário.
   * As tags facilitam a localização de suas campanhas e a criação de relatórios a partir delas.
5. Adicione e nomeie quantas variantes forem necessárias para sua campanha. Você pode escolher diferentes plataformas, tipos de mensagens e layouts para cada uma de suas variantes adicionadas. Para obter mais informações sobre esse tópico, consulte [Testes multivariados e A/B]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/).

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

## Etapa 2: Escreva sua mensagem LINE

Escreva sua mensagem usando personalização (como Liquid ou Connected Content) conforme necessário. O LINE permite até cinco balões de mensagem em cada mensagem, que podem ter qualquer um dos layouts de mensagens disponíveis: texto, imagem, rich ou baseado em cartão.

\![Compositor de linha com uma mensagem exibida na visualização.]({% image_buster /assets/img/line/line_composer.png %})

### Dicas

#### Usando líquido

Se você planeja usar o Liquid, certifique-se de incluir um valor padrão para sua personalização. Isso evitará que os destinatários com perfis de usuário incompletos recebam um espaço reservado em branco. Por exemplo, em vez de um usuário receber a mensagem "Hi, !", ele pode receber a mensagem "Hi, new subscriber!".

#### Criação de mensagens da direita para a esquerda

A aparência final das mensagens da direita para a esquerda depende muito de como os provedores de serviços as processam. Para obter práticas recomendadas sobre como criar mensagens da direita para a esquerda que sejam exibidas da forma mais precisa possível, consulte [Criação de mensagens da direita para a esquerda]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/right_to_left_messages/).

## Etapa 3: Visualize e teste sua mensagem

Alterne para a guia **Teste** para enviar uma mensagem LINE de teste para grupos de teste de conteúdo ou usuários individuais, ou visualize a mensagem como um usuário diretamente no Braze.

\![A guia "Tests" (Testes) exibe uma visualização de uma mensagem de teste.]({% image_buster /assets/img/line/test_preview.png %})

## Etapa 4: Crie o restante de sua campanha ou Canvas

{% tabs %}
{% tab Campaign %}

Crie o restante de sua campanha. Consulte as seções a seguir para obter mais detalhes sobre a melhor forma de usar nossas ferramentas para criar mensagens LINE.

### Escolha o cronograma de entrega ou o acionador

As mensagens do LINE podem ser entregues com base em um horário programado, uma ação ou um acionador de API. Para obter mais informações sobre opções de agendamento e acionadores, consulte [Agendamento de sua campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/).

É possível especificar controles de entrega, como permitir que os usuários se tornem [reelegíveis]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) para receber a campanha ou ativar regras [de limite de frequência]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping). Para a entrega baseada em ação, você também pode definir a duração da campanha e o [Quiet Hours]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/time_based_campaign/#quiet-hours).

### Escolha os usuários a serem alvos

[Direcione os usuários]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/targeting_users/) escolhendo segmentos ou filtros para restringir seu público. Você já deve ter escolhido o grupo de assinatura, que restringe os usuários pelo nível ou categoria de comunicação que desejam ter com você. 

Selecione o público-alvo maior de seus segmentos e, opcionalmente, restrinja esse segmento ainda mais com nossos [filtros]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters/). Você receberá automaticamente um instantâneo de como é a população desse segmento aproximado no momento. Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes de a mensagem ser enviada.

### Selecionar eventos de conversão

O Braze permite que você rastreie a frequência com que os usuários realizam ações específicas, [eventos de conversão]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/conversion_events/), após receberem uma campanha. Você tem a opção de permitir um período de até 30 dias durante o qual uma conversão será contada se o usuário realizar a ação especificada.

Os eventos de conversão ajudam a medir o sucesso de sua campanha. Por exemplo:

- Se você estiver usando o geotargeting para acionar uma mensagem LINE que tenha como objetivo final que o usuário faça uma compra, defina o evento de conversão como `Purchase`.
- Se estiver tentando direcionar o usuário para o seu aplicativo, defina o evento de conversão como `Starts Session`.

Você também pode definir eventos de conversão personalizados com base em seu caso de uso específico. Seja criativo e pense em como você deseja medir o sucesso dessa campanha.

{% endtab %}
{% tab Canvas %}

Se ainda não o fez, preencha as seções restantes do seu Canvas. Para obter mais detalhes sobre como criar o restante de seu Canvas, usar testes multivariados e Intelligent Selection, entre outros, consulte [Criação de um Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/).

{% endtab %}
{% endtabs %}

## Etapa 5: Revisão e implementação

Depois de terminar de criar a última parte de sua campanha ou Canvas, revise seus detalhes, teste-a e envie-a!

Em seguida, confira [os relatórios LINE]({{site.baseurl}}/line/reporting/) para saber como acessar os resultados de suas campanhas LINE.


