---
nav_title: Lançamento com o Canvas Flow
article_title: Lançamento com o Canvas Flow
page_order: 3
description: "Este artigo de referência cobre como preparar e testar um canva construído com Canvas Flow antes do lançamento."
page_type: reference
tool: Canvas
---

# Lançamento com o Canvas Flow

> Este artigo de referência cobre como preparar e testar um canva construído com Canvas Flow antes do lançamento. Isso inclui identificar pontos de verificação importantes da canva, como condições de entrada da canva, resumos do público e segmentos de usuários.

À medida que você se prepara para lançar seu canva, a Braze recomenda que você o verifique em cada estágio do Criador de canva para configurações que podem impactar o envio de suas mensagens, incluindo:
* [Condições de corrida](#race-conditions)
* [Tempos de entrega](#delivery-times)
* [Segmentos de usuários](#segment-users)

## Condições de corrida 

Considere as [condições de corrida]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/) que podem ocorrer antes de lançar sua canva. 

Para entrar em uma canva, os usuários devem estar no público de entrada antes que o horário de entrada ocorra, independentemente de a canva estar agendada, baseada em ação ou acionada por API. 

![Uma tela baseada em ação que entra nos usuários quando eles fazem qualquer compra durante o fuso local do usuário, de 30 de abril de 2025 às 12h a 7 de maio de 2025 às 12h.]({% image_buster /assets/img_archive/launch_with_canvas_flow_example.png %}){: style="max-width:75%;"}

Observe que os usuários que se qualificarem para seu público de entrada após o lançamento do canva não entrarão no canva.

{% alert tip %}
Confira [Tipos de cronograma de entrada]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/#step-2b-set-your-canvas-entry-schedule) para orientação e detalhes sobre quando usar a entrega programada, baseada em ação ou acionada por API para seu canva!
{% endalert %}

### Revisão de filtros do público de entrada

Em geral, evite configurar um canva acionado por ação ou API com o mesmo gatilho que o filtro de público. Por exemplo, após uma canva ser lançada, os usuários que realizarem uma ação específica serão incluídos no público de entrada, então não há necessidade de adicionar o evento como um filtro de público. 

Para saber mais sobre os filtros de segmentação disponíveis para atingir seu público, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/engagement_tools/segments/segmentation_filters).

### Agrupar várias solicitações de API

Faça suas solicitações na mesma chamada de API, em vez de várias chamadas, para confirmar que o perfil do usuário é criado ou atualizado primeiro. Consulte [Usando vários endpoints]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/#using-multiple-api-endpoints) para mais exemplos.

### Adicionar uma postergação

Outra opção para evitar condições de corrida é usar a etapa de postergação (idealmente definida para 5 minutos) como a primeira etapa do seu canva. 

Isso permite tempo para que atributos, endereços de e-mail e tokens de push sejam processados para novos perfis de usuário antes de serem direcionados para as seguintes etapas do canva. Sem esta etapa de postergação, é possível que um e-mail seja enviado a um usuário cujo e-mail ainda não foi atualizado.

## Prazos de entrega

Definir um tempo de entrega do canva em tempo real pode levar ao aumento do engajamento e das taxas de conversão. Tome nota de qual horário de entrega você definiu para seu canva. Para ajudar a aumentar o engajamento e as taxas de conversão, é melhor disparar canvases em tempo real em vez de em uma base programada e recorrente.

Se você selecionou uma entrega agendada para seu canva, a Braze recomenda agendar seu canva com pelo menos 24 horas de antecedência para permitir quaisquer ajustes em seu canva.

## Segmentos de usuários

Antes de saturar demais a jornada do usuário do Canvas Flow com componentes, considere como você pode manter a jornada do usuário simples. Use a visualização simplificada no editor de canva para ter uma ideia melhor de como os caminhos da jornada do usuário se ramificam. 

Existem quatro componentes principais que você pode usar para segmentar seus usuários de maneira simples e eficaz:

* [Jornadas do público](#audience-paths)
* [Divisão de decisão](#decision-split)
* [Jornadas de ação](#action-paths)
* [Jornadas do experimento](#experiment-paths)

### Jornadas do público

Use [caminhos do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/) para segmentar usuários dentro do canva com base em atributos personalizados, eventos personalizados e dados anteriores de engajamento com mensagem dos perfis de usuário.

### Divisão de decisão

A etapa [divisão de decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split/) permite que você envie seus usuários para diferentes jornadas com base em suas respostas a uma pergunta polar.

### Jornadas de ação

[Jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) focam em segmentar usuários com base em comportamentos em tempo real, como eventos personalizados, eventos de compra e mudanças de atributos personalizados. 

### Jornadas do experimento

Semelhante às jornadas de ação, você pode aproveitar as etapas de [jornadas de experimentação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/) no seu canva para testar vários caminhos de canva entre si, junto com um grupo de controle. Isso rastreia a performance da jornada, permitindo que você tome decisões informadas ao construir seu canva. 

## Testando antes do lançamento

Depois de revisar os detalhes mais finos da sua canva, confira [Enviando canvas de teste]({{site.baseurl}}/user_guide/engagement_tools/canvas/testing_canvases/sending_test_canvases/) para diferentes métodos que você pode usar para testar sua canva com usuários de teste.

## Lista de verificação de lançamento

### Verifique a disponibilidade do usuário

- Certifique-se de que seus usuários atendam aos critérios de segmentação.
- Confirme se o estado da inscrição é "inscrito" ou "aceitação" e se o token por push existe. Se você adicionou essas regras como regras de entrada no Canvas, é possível que os usuários tenham cancelado a inscrição entre a entrada no Canvas e o recebimento da etapa de mensagens.
- Confirme se elas correspondem às configurações de envio do Canva. (Se os usuários estiverem "inscritos", mas as configurações forem "Aceitação", os usuários não serão ativados para o canal).
- Se o limite global de frequência estiver ativado para o seu Canva, verifique se as regras estão limitando o número de vezes que cada usuário pode receber uma mensagem de um canal específico.
- Se o horário de silêncio estiver ativado, o tempo de envio de mensagens poderá ser afetado, o que significa que a mensagem poderá ser enviada no próximo horário disponível (quando o horário de silêncio terminar) ou cancelada completamente.
- Verifique a disponibilidade do usuário para filtros adicionais na etapa do canva.

### Confirmar que realizaram o evento personalizado ou a compra de pré-requisito

- Verifique se há uma condição de corrida, que afeta as mensagens que os usuários recebem se dispararem várias ações ao mesmo tempo.
- Verifique se não há filtros específicos na etapa que poderiam ter bloqueado o recebimento da mensagem pelos usuários.
- Procure conflitos entre diferentes etapas do mesmo Canva. Por exemplo, os usuários que não receberam a mensagem podem ser interrompidos por um filtro que exige a conclusão de outra etapa em um ramo diferente.
- Confirme se os usuários atendem às regras de validação adicionais.
- Confirme se a etapa do Canva estava conectada à etapa anterior no momento do envio.

### Confirme se o Canva foi salvo corretamente e se todas as etapas são válidas

Se o seu Canvas não estiver carregando e não progredir, isso pode ser causado quando uma versão anterior do Canvas não foi salva corretamente e contém etapas inválidas. Você pode duplicar o Canva no dashboard. Se o problema persistir, abra um [tíquete de suporte]({{site.baseurl}}/braze_support/).

## Solução de problemas

{% details Why are my users not receiving my Canvas messages? %}
**Verifique a disponibilidade do usuário**
- Certifique-se de que eles atendam a seus critérios de segmentação.
- Confirme se o estado da inscrição push é "inscrito" ou "aceitação" **e** se o status de **capacitação push** está definido como "verdadeiro". Se você adicionou isso como regras de entrada da canva, é possível que os usuários tenham sido desinscritos entre a entrada na sua canva e o recebimento da etapa de mensagem.
- Confirme se elas correspondem às configurações de envio do Canva. (Se os usuários estiverem "inscritos", mas as configurações forem "Aceitação", os usuários não serão ativados para o canal).
- Se o limite global de frequência estiver ativado para o seu Canva, verifique se as regras estão limitando o número de vezes que cada usuário pode receber uma mensagem de um canal específico. 
- Se o horário de silêncio estiver ativado, o tempo de envio de mensagens poderá ser afetado, o que significa que a mensagem poderá ser enviada no próximo horário disponível (quando o horário de silêncio terminar) ou cancelada completamente.

**Verifique a disponibilidade do usuário para filtros adicionais na etapa do canva**
- Confirme que eles realizaram o evento personalizado ou a compra de pré-requisito.
- Verifique se há uma [condição de corrida]({{site.baseurl}}/user_guide/engagement_tools/testing/race_conditions/), que afeta as mensagens que os usuários recebem se dispararem várias ações ao mesmo tempo.
- Verifique se não há filtros específicos na etapa que poderiam ter bloqueado o recebimento da mensagem pelos usuários.
- Procure conflitos entre diferentes etapas do mesmo Canva. Por exemplo, os usuários que não receberam a mensagem podem ser interrompidos por um filtro que exige a conclusão de outra etapa em um ramo diferente.
- Confirme se os usuários atendem às regras de validação adicionais.
- Confirme se a etapa do Canva estava conectada à etapa anterior no momento do envio.
{% enddetails %}

