---
nav_title: Comportamentos de avanço
article_title: Comportamentos de avanço
page_order: 10
alias: /auto_advance/
page_type: reference
description: "Este artigo de referência descreve o comportamento de avanço e aborda vários cenários que podem surgir à medida que você avança em um Canva."
tool: Canvas

---

# Comportamentos de avanço

{% alert important %}
A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar canvas usando o editor original. Este artigo está disponível como referência para entender como seus usuários avançam pelos componentes do Canva no editor Origin. <br><br>Para componentes no Canvas Flow, o **comportamento de avanço** é definido como sempre avançar imediatamente o público, ou **Avançar imediatamente o público**. Isso também se aplica a [etapas desconectadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#disconnected-steps/).
{% endalert %}

> O recurso **Advancement Behavior (Comportamento de avanço)** permite que você escolha os critérios de avanço por meio do [componente do Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/). 

![Configurações de Comportamento de Avanço com duas opções para avançar o público quando a mensagem é enviada, ou para avançar imediatamente o público.]({% image_buster /assets/img/push-advancement-behavior.png %} "Comportamento de Avanço")

Os usuários devem atender aos critérios da etapa para poderem avançar por ela. Com as etapas [de mensagens]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), você pode ativar as validações de entrega para verificar se o público atende aos critérios de entrega no envio da mensagem. Isso contará para os critérios da etapa ao usar o Canvas Flow. Portanto, se um usuário não atender aos critérios de validação de entrega, ele sairá do canva.

Quando a opção **Avançar quando a mensagem** for enviada estiver selecionada, os usuários só avançarão para as etapas subsequentes do canva quando uma das seguintes condições ocorrer:

- Uma mensagem de e-mail é enviada
- Uma mensagem push é enviada
- Um webhook é enviado
- Uma mensagem no app é visualizada
- Um cartão de conteúdo é enviado

Quando **a opção Avançar público imediatamente** for selecionada, os usuários avançarão para as etapas subsequentes do Canva quando ocorrer uma das seguintes condições:

- Qualquer mensagem é enviada ou a mensagem no app na etapa se torna ativa
- O webhook não é enviado porque o webhook causa um erro ou erros
- Uma notificação por push ou e-mail não foi enviada porque o usuário não pode ser contactado por e-mail ou push
- Tentativa de envio do cartão de conteúdo 
- Um cartão é abortado e não é enviado
- Uma mensagem não foi enviada porque a frequência máxima já foi atingida
- Uma mensagem não foi enviada porque foi abortada

### Etapas programadas

Para um componente agendado, os usuários devem atender às opções de público da etapa para poderem avançar na etapa. Se a etapa tiver um [evento de exceção]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria/#exception-events), os usuários que realizarem o evento de exceção não avançarão na etapa.

Ao enviar um componente multicanal com o [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/), podemos enviar ou tentar enviar mensagens em vários canais em horários diferentes. O Braze avançará automaticamente os usuários no momento em que a primeira mensagem de um componente tentar ser enviada.

### Etapas baseadas em ações

Para etapas baseadas em ação, os usuários devem executar a ação-gatilho e atender às opções do público para avançar na etapa. Se a etapa tiver um evento de exceção, os usuários que realizarem o evento de exceção não avançarão na etapa.

{% alert important %}
Os usuários que avançarem em uma etapa sem receber mensagens não serão contados como um destinatário exclusivo para a etapa. Os usuários devem receber uma ou mais mensagens de uma etapa para serem contados como um destinatário único.
{% endalert %}

## Caso de uso

O avanço funciona bem quando o envio de mensagens subsequentes está relacionado às mensagens anteriores. Por exemplo, você não gostaria de enviar um push de acompanhamento sobre um e-mail que nunca foi enviado aos usuários.

Pode haver ocasiões em que você queira que os usuários continuem avançando em um Canva mesmo quando não receberem uma determinada mensagem. Por exemplo, você pode ter um push de "Boas-vindas" no Dia 3 e um e-mail de "Boas-vindas" no Dia 6. Alguns dos seus usuários podem não estar acessíveis por meio de notificações por push, pois nem todos aceitam receber mensagens por push. Talvez queira enviar o e-mail do Dia 6 a todos os usuários, mesmo que eles não tenham recebido o push do Dia 3.

Nesse cenário, é possível usar as opções de comportamento de avanço para garantir que os usuários continuem no Canva mesmo que não recebam o push do Dia 3.

Se quiser que todos os usuários recebam o e-mail do Dia 6, mesmo que não tenham recebido o push do Dia 3, defina o **Advancement Behavior** como **Immediately Advance Público** para o envio do Dia 3.

Quando você seleciona o comportamento de avanço do **público Immediately Advance** para o push do Dia 3, os usuários avançarão quando o Braze tentar enviar o push. Os usuários que corresponderem às opções de público e que não puderem ser contatados por push não receberão o push, mas serão avançados de qualquer forma.

{% details Comportamento de avanço da tela anterior %}

Antes do lançamento do Advancement Behavior, o Braze avançava os usuários por meio de um componente do Canva depois que eles recebiam uma mensagem desse componente. Por exemplo, se um componente do Canvas incluísse um e-mail e um push, os usuários não avançariam para as próximas etapas do Canvas até que o Braze enviasse o push ou o e-mail ao usuário.

Se o usuário não recebesse o push ou o e-mail, ele não avançaria para as etapas subsequentes do Canva.

Os clientes do Braze que não participaram da primeira rodada da versão beta da mensagem no app do Canvas terão a opção de comportamento de avanço "Mensagem enviada" aplicada a todas as etapas do Canva criadas antes de 30 de julho de 2019. Antes do lançamento do recurso de comportamento para avançar, o avanço do usuário ocorria quando as mensagens eram enviadas a partir das etapas do canva.

Os clientes do Braze que participaram da primeira rodada da versão beta das mensagens no aplicativo do Canvas terão a opção de comportamento de avanço "Mensagem enviada" aplicada a todas as etapas do Canva sem mensagens no aplicativo criadas antes de 30 de julho de 2019 e "Avanço do público após postergação" aplicada a todas as etapas do Canvas com mensagens no aplicativo criadas antes de 30 de julho de 2019. Antes do lançamento do recurso de comportamento para avançar, o avanço do usuário ocorria quando as mensagens no app do canva se tornavam ativas.

{% enddetails %}

