---
nav_title: Lançamento com o fluxo do Canvas
article_title: Lançamento com o Canvas Flow
page_order: 3
description: "Este artigo de referência aborda como preparar e testar um Canvas criado com o Canvas Flow antes do lançamento."
page_type: reference
tool: Canvas
---

# Lançamento com o Canvas Flow

> Este artigo de referência aborda como preparar e testar um Canvas criado usando o Canvas Flow antes do lançamento. Isso inclui a identificação de pontos de verificação importantes do Canvas, como condições de entrada do Canvas, resumos de público-alvo e segmentos de usuários.

Ao se preparar para lançar seu Canvas, a Braze recomenda que você verifique seu Canvas em cada estágio do construtor de Canvas para verificar as configurações que podem afetar o envio de mensagens, incluindo:
* [Condições da corrida](#race-conditions)
* [Prazos de entrega](#delivery-times)
* [Segmentos de usuários](#segment-users)

## Condições da corrida 

Considere as [condições de corrida]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) que podem ocorrer antes de lançar seu Canvas. 

Para entrar em um Canvas, os usuários devem estar na audiência de entrada antes que a programação de entrada ocorra, independentemente de o Canvas ser programado, baseado em ação ou acionado por API. 

Um Action-Based Canvas que entra nos usuários quando eles fazem qualquer compra durante o horário local do usuário de 30 de abril de 2025 às 12 horas a 7 de maio de 2025 às 12 horas.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Observe que os usuários que se qualificarem para o seu público de entrada após o lançamento do Canvas não entrarão no Canvas.

{% alert tip %}
Confira [Tipos de programação de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule) para obter orientações e detalhes sobre quando usar a entrega programada, baseada em ação ou acionada por API para seu Canvas!
{% endalert %}

### Revisar filtros de público-alvo de entrada

Em geral, evite configurar um Canvas baseado em ação ou acionado por API com o mesmo acionador que o filtro de público-alvo. Por exemplo, depois que um Canvas for lançado, os usuários que executarem uma ação específica serão incluídos no público-alvo de entrada, portanto, não há necessidade de adicionar o evento como um filtro de público-alvo. 

Para obter mais detalhes sobre os filtros de segmentação disponíveis para direcionar seu público, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

### Lote de várias solicitações de API

Faça suas solicitações na mesma chamada de API, em vez de várias chamadas, para confirmar que o perfil do usuário foi criado ou atualizado primeiro. Consulte [Uso de vários pontos de extremidade]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints) para obter mais exemplos.

### Adicionar um atraso

Outra opção para evitar condições de corrida é usar a etapa Delay (idealmente definida para 5 minutos) como a primeira etapa do Canvas. 

Isso dá tempo para que atributos, endereços de e-mail e tokens push sejam processados em novos perfis de usuário antes de serem direcionados para as etapas seguintes do Canvas. Sem essa etapa de atraso, é possível que um e-mail seja enviado a um usuário cujo e-mail ainda não tenha sido atualizado.

## Prazos de entrega

A definição de um tempo de entrega do Canvas em tempo real pode levar ao aumento do engajamento e das taxas de conversão. Anote o prazo de entrega que você definiu para seu Canvas. Para ajudar a aumentar o engajamento e as taxas de conversão, é melhor acionar os Canvases em tempo real, em vez de em uma base programada e recorrente.

Se você selecionou uma entrega programada para o seu Canvas, a Braze recomenda programar o Canvas pelo menos 24 horas antes do lançamento para permitir ajustes no Canvas.

## Segmentos de usuários

Antes de saturar demais a jornada do usuário do Canvas Flow com componentes, considere como manter uma jornada do usuário simples. Use a visualização simplificada no editor do Canvas para ter uma ideia melhor de como a jornada do usuário se ramifica. 

Há quatro componentes principais que podem ser usados para segmentar seus usuários de maneira simples e eficaz:

* [Caminhos do público](#audience-paths)
* [Divisão da decisão](#decision-split)
* [Caminhos de ação](#action-paths)
* [Caminhos de experimentos](#experiment-paths)

### Caminhos do público

Use as etapas de [Caminhos de público-alvo]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) para segmentar usuários no Canvas com base em atributos personalizados, eventos personalizados e dados de envolvimento de mensagens anteriores dos perfis de usuário.

### Divisão da decisão

A etapa de [divisão de decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) permite enviar os usuários para diferentes caminhos da jornada do usuário com base em suas respostas a uma pergunta polar.

### Caminhos de ação

[Os caminhos de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) se concentram na segmentação de usuários com base em comportamentos em tempo real, como eventos personalizados, eventos de compra e alterações de atributos personalizados. 

### Caminhos de experimentos

Semelhante aos Caminhos de Ação, você pode aproveitar as etapas [dos Caminhos de Experimentação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) no seu Canvas para testar vários caminhos do Canvas em comparação uns com os outros, juntamente com um grupo de controle. Isso rastreia o desempenho do caminho, permitindo que você tome decisões informadas ao criar sua jornada do Canvas. 

## Testes antes do lançamento

Depois de revisar os detalhes do seu Canvas, consulte [Envio de Canvases de teste]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) para conhecer os diferentes métodos que podem ser usados para testar seu Canvas com usuários de teste.

## Lista de verificação de lançamento

### Verifique a disponibilidade do usuário

- Certifique-se de que seus usuários atendam aos critérios de segmentação.
- Confirme se o estado da assinatura é "subscribed" ou "opted-in" e se o token Push existe. Se você adicionou essas regras como regras de entrada do Canvas, é possível que os usuários tenham cancelado a assinatura entre a entrada no Canvas e o recebimento da etapa Mensagem.
- Confirme se elas correspondem às configurações de envio do Canvas. (Se os usuários estiverem "inscritos", mas as configurações forem "opt-in", os usuários não serão ativados para o canal).
- Se o limite global de frequência estiver ativado para o Canvas, verifique se as regras estão limitando o número de vezes que cada usuário pode receber uma mensagem de um canal específico.
- Se o Quiet Hours estiver ativado, o horário de envio da mensagem poderá ser afetado, o que significa que a mensagem poderá ser enviada no próximo horário disponível (quando o Quiet Hours terminar) ou ser totalmente cancelada.
- Verifique a disponibilidade do usuário para filtros adicionais na etapa do Canvas.

### Confirmar que eles realizaram o evento personalizado ou a compra de pré-requisito

- Verifique se há uma condição de corrida, que afeta as mensagens que os usuários recebem se acionarem várias ações ao mesmo tempo.
- Certifique-se de que não haja filtros específicos na etapa que possam ter impedido os usuários de receber a mensagem.
- Procurar conflitos entre diferentes etapas dentro do mesmo Canvas. Por exemplo, os usuários que não receberam a mensagem podem ser interrompidos por um filtro que exige a conclusão de outra etapa em um ramo diferente.
- Confirme se os usuários atendem às regras de validação adicionais.
- Confirme se a etapa do Canvas estava conectada à etapa anterior no momento do envio.

### Confirme se o Canvas foi salvo corretamente e se todas as etapas são válidas

Se o seu Canvas não estiver carregando e não progredir, isso pode ser causado quando uma versão anterior do Canvas não foi salva corretamente e contém etapas inválidas. Você pode duplicar o Canvas no painel. Se o problema persistir, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

## Solução de problemas

{% details Why are my users not receiving my Canvas messages? %}
**Verifique a disponibilidade do usuário**
- Certifique-se de que eles atendam a seus critérios de segmentação.
- Confirme se o estado da assinatura de push é "subscrito" ou "aceito" **e** se o status de ativação **de push** está definido como "verdadeiro". Se você adicionou essas regras como regras de entrada do Canvas, é possível que os usuários tenham cancelado a assinatura entre a entrada no Canvas e o recebimento da etapa Mensagem.
- Confirme se elas correspondem às configurações de envio do Canvas. (Se os usuários estiverem "inscritos", mas as configurações forem "opt-in", os usuários não serão ativados para o canal).
- Se o limite global de frequência estiver ativado para o Canvas, verifique se as regras estão limitando o número de vezes que cada usuário pode receber uma mensagem de um canal específico. 
- Se o Quiet Hours estiver ativado, o horário de envio da mensagem poderá ser afetado, o que significa que a mensagem poderá ser enviada no próximo horário disponível (quando o Quiet Hours terminar) ou ser totalmente cancelada.

**Verifique a disponibilidade do usuário para filtros adicionais em sua etapa do Canvas**
- Confirme que eles realizaram o evento personalizado ou a compra de pré-requisito.
- Verifique se há uma [condição de corrida]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/), que afeta as mensagens que os usuários recebem se acionarem várias ações ao mesmo tempo.
- Certifique-se de que não haja filtros específicos na etapa que possam ter impedido os usuários de receber a mensagem.
- Procurar conflitos entre diferentes etapas dentro do mesmo Canvas. Por exemplo, os usuários que não receberam a mensagem podem ser interrompidos por um filtro que exige a conclusão de outra etapa em um ramo diferente.
- Confirme se os usuários atendem às regras de validação adicionais.
- Confirme se a etapa do Canvas estava conectada à etapa anterior no momento do envio.
{% enddetails %}

