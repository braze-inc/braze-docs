---
nav_title: Edite Canvases após o lançamento
article_title: Edite Canvases Após o Lançamento
page_order: 0
description: "Este artigo de referência aborda os diferentes aspectos de um Canva que podem ser alterados após o lançamento inicial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Edite Canvases após o lançamento

> Este artigo de referência aborda o que pode ser alterado em um Canva após o lançamento inicial.

Você pode editar suas Canvas após o lançamento:

* Inserção de novas etapas do Canva na jornada do usuário
* Adição de novas variantes e conexões
* Ajuste da distribuição de variantes
* Interromper ou retomar todas as etapas do Canva

{% alert note %}
A distribuição da variante de controle só pode ser reduzida após o lançamento.
{% endalert %}

Você pode excluir qualquer um dos itens a seguir em sua jornada de usuário:

- [Etapas do canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Variantes da tela 
- Conexões entre as etapas do Canva

Se você quiser editar ou adicionar mais etapas à jornada do usuário do seu Canvas, os seguintes detalhes se aplicam:

- Os usuários que ainda não entraram no Canva são elegíveis para todas as etapas recém-criadas. 
- Se as configurações de entrada do Canva permitirem que os usuários entrem novamente nas etapas, os usuários que já passaram nas etapas recém-criadas serão elegíveis para entrar novamente.
- Os usuários que estão atualmente em um Canvas lançado, mas que não atingiram os pontos da jornada do usuário em que novas etapas são adicionadas, são elegíveis para receber essas etapas recém-adicionadas. 

Se você excluir uma etapa [de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) ou [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), poderá opcionalmente redirecionar os usuários que estão aguardando na etapa para outra etapa do Canva. Para Postergações, os usuários permanecem na etapa até o final do período de postergação. Para Jornadas de Ação, os usuários permanecem na etapa até o final da janela de avaliação.

Observe que, ao iniciar um Canvas inicialmente, o Braze enfileira os usuários para a etapa de mensagens em que eles se encontram, e não para todas as mensagens subsequentes no Canvas. Se você fizer uma edição no Canvas após o lançamento, alguns usuários podem já estar na fila e podem não receber as alterações. Se você parar o Canvas, duplicá-lo, mudar e lançar esta nova versão, o Canvas reavalia todos os usuários novamente, não apenas os usuários que ainda não estavam na fila.

Consulte a seção [Práticas recomendadas](#best-practices) para obter casos de uso específicos de edição. Em geral, é uma prática recomendada evitar a edição de canvas ativos, pois pode haver um comportamento inesperado.

{% details Expand for original Canvas editor details %}

Tenha em mente as seguintes edições permitidas no Canvas após o lançamento, dependendo de qual fluxo de trabalho seu Canvas foi criado. Se o seu Canvas usa o fluxo de trabalho original do Canvas, você precisará cloná-lo para o Canvas Flow primeiro para realizar edições pós-lançamento.

Você não pode editar ou excluir conexões existentes, e não pode inserir uma etapa entre etapas conectadas existentes. Se você quiser editar ou adicionar mais etapas à jornada do usuário do seu Canvas, os seguintes detalhes se aplicam:

- Os usuários que ainda não entraram no Canva são elegíveis para todas as etapas recém-criadas. 
- Se as configurações de entrada do Canva permitirem que os usuários entrem novamente nas etapas, os usuários que já passaram nas etapas recém-criadas serão elegíveis para entrar novamente.
- Os usuários que estão atualmente em um Canvas lançado, mas que não alcançaram as etapas recém-adicionadas na jornada do usuário, são elegíveis para receber essas etapas recém-adicionadas.
- Se uma etapa de postergação for a última etapa do Canva, os usuários que alcançarem essa etapa serão automaticamente avançados para fora do Canvas e não receberão nenhuma etapa recém-criada.

{% alert important %}
Se você atualizar as configurações de **Postergação** ou **Janela** para uma etapa do Canvas, os usuários que estão atualmente nessa etapa no momento da atualização seguem o tempo de postergação que foi atribuído quando entraram originalmente. Apenas novos usuários que entram no Canvas e aqueles que ainda não foram colocados na fila para essa etapa recebem a mensagem no horário atualizado.
{% endalert %}

Parar um Canvas não faz com que os usuários que estão esperando para receber uma mensagem saiam. Se você reativar o Canvas e os usuários ainda estiverem esperando pela mensagem, eles recebem a mensagem (a menos que o horário em que deveriam ter recebido a mensagem já tenha passado, então eles não a recebem).

{% enddetails %}

## Detalhes da tela

Você pode editar as seguintes configurações e detalhes após lançar um Canvas:

* Nome e descrição da tela
* Equipes e tags
* Tipo de entrada, cronograma e controles
* Status da inscrição
* Limite de taxa
* Limite de frequência
* Horário de silêncio
* Público alvo

Após o lançamento do Canva:

- Os eventos de conversão não podem ser editados. 
- Os seguintes passos não podem ser adicionados ou removidos, e não podem ser reordenados para ajustar a classificação: [Jornadas do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), and [jornadas experimentais]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).
  - **Solução alternativa 1:** Crie uma nova jornada do público, jornada de ação ou jornada experimental e reconfigure os caminhos para essa nova etapa.
  - **Solução alternativa 2:** Duplique o canva para fazer suas edições.

### Etapas individuais

Para etapas individuais do Canva, você pode editar os seguintes detalhes após o lançamento:

* Nome
* Conteúdo das mensagens
* Gatilhos
* Público
* Eventos de exceção
* Postergações (apenas para etapas de Postergação)

No entanto, o tipo de programação e as porcentagens de controle da etapa não são editáveis após o lançamento. Para etapas de Jornadas de Ação e Caminhos de Público, as classificações e janelas de avaliação não são editáveis após o lançamento.

### Porcentagens de variantes de tela

Depois de lançar um canva, só é possível diminuir as porcentagens da variante de controle. Se uma porcentagem de variante for modificada no Canva, você verá que seus usuários poderão ser redistribuídos para outras variantes.

Inicialmente, esses usuários são atribuídos aleatoriamente a uma variante específica antes de receberem uma campanha pela primeira vez. A partir de então, cada vez sucessiva que a campanha for recebida (ou o usuário reentrar em uma variante do Canvas), eles recebem a mesma variante, a menos que as porcentagens das variantes sejam modificadas.

Se as porcentagens de variantes mudarem, os usuários poderão ser redistribuídos para outras variantes. Os usuários permanecem nessas variantes até que as porcentagens sejam modificadas novamente. Note que, para Canvas que usam ramificação com filtros `NOT` com números de balde aleatórios, os usuários podem não receber a mesma ramificação todas as vezes em sua jornada de usuário quando entrarem novamente no Canvas.

#### Grupos de controle

Os grupos de controle permanecem consistentes se a porcentagem da variante não for alterada. Se a porcentagem de um grupo de controle for diminuída ou aumentada, os usuários que receberam mensagens anteriormente não poderão entrar no grupo de controle em um envio posterior, nem nenhum usuário do grupo de controle jamais receberá uma mensagem.

### Tempo de envio local

Canvases programados para lançar em um horário de envio local podem ser editados até 24 horas antes do horário de envio programado. Essa janela é chamada de "zona de segurança". 

{% alert tip %}
Caso pretenda fazer edições maiores que levem à criação de uma nova cópia do Canvas, lembre-se de excluir os usuários que receberam o primeiro Canvas e reajuste os horários da programação do Canvas para permitir o envio por fuso horário.
{% endalert %}

Quando um cronograma de entrada é definido para inserir usuários imediatamente após o lançamento, o Canvas é lançado no horário mais próximo em incrementos de 5 minutos. Por exemplo, se você atualizar um Canva para que os usuários entrem imediatamente às 8:31 PST, o horário de lançamento é definido para 8:30 PST e no fuso horário da empresa.

### Exclusão de variantes

Quando as variantes são excluídas de um Canva, ocorre o seguinte:

- As etapas dentro da variante (incluindo aquelas compartilhadas por outras variantes) são excluídas. 
- As análises da etapa e as análises de nível superior para o Canva, como _Total Entries_, _Total Exits_ e _Conversion Rate_, são excluídas.
- Os usuários das variantes excluídas são excluídos das etapas e as mensagens seguintes não são enviadas.

### Propriedades de entrada da tela

As propriedades de entrada do canva não estão no formato de modelos em etapas quando enviadas. Isso significa que, quando as propriedades de entrada do Canva são editadas após o lançamento do Canva, essas alterações se aplicam apenas a novos usuários que entram no Canva. Se o seu Canva permitir que os usuários reentrem no Canva, qualquer usuário que reentrar é determinado pelas propriedades de entrada do Canva atualizadas.

## Melhores práticas

Confira estas melhores práticas a serem lembradas ao editar ou adicionar ao seu canva após seu lançamento.

{% alert important %}
Em geral, evite fazer alterações enquanto o Canva está ativo e enfileirando usuários.
{% endalert %}

### Etapas desconectadas

Você pode iniciar seu Canvas com etapas desconectadas e também salvar esses Canvases após o lançamento. Antes de desconectar uma etapa do seu fluxo de trabalho, recomendamos verificar a exibição de análise de dados das etapas para usuários pendentes.

Digamos que um usuário esteja em uma etapa desconectada do seu fluxo de trabalho do Canva. Este usuário avança para a etapa subsequente, se houver uma. As configurações da etapa ditam como o usuário deve avançar. 

Ao criar ou editar etapas desconectadas, você pode fazer alterações nessas etapas independentes sem precisar conectá-las diretamente ao restante do Canva. Isso ajuda a testar suas etapas antes de relançar seu Canva. 

### Etapa da jornada experimental

Se o seu Canva tiver um experimento de Caminho Vencedor ou Caminho Personalizado ativo ou em andamento e você atualizar o Canva ativo (independentemente de atualizar a etapa do Caminho do Experimento em si), o experimento em andamento termina, e a etapa do Caminho do Experimento não determina um caminho vencedor ou caminhos personalizados. Para reiniciar o experimento, você pode desconectar o Caminho do Experimento existente e lançar um novo, ou duplicar o Canva e lançar um novo Canva. Caso contrário, os usuários fluem pelo caminho do experimento como se nenhum método de otimização tivesse sido selecionado.

### Postergação de tempo

Editar Canvases com atrasos de tempo pode ser um pouco complicado, então tenha em mente os seguintes detalhes ao fazer edições em seus Canvases:

- Se você atualizar o atraso em uma etapa de Atraso, apenas novos usuários entrando no Canva e usuários que não foram enfileirados para essa etapa recebem a mensagem no horário de atraso atualizado.
- Se você excluir uma etapa com um atraso de tempo (como Atraso ou Jornadas de Ação) e decidir redirecionar esses usuários para outra etapa do Canva, os usuários são redirecionados apenas após o atraso de tempo da etapa ter sido concluído. Por exemplo, digamos que você exclua uma etapa de Atraso com um atraso de um dia e redirecione esses usuários para uma etapa de Mensagem. Nesse caso, os usuários são redirecionados apenas após o atraso de um dia ter sido concluído.
- Se o seu Canva tiver uma ou mais etapas de jornadas experimentais, a exclusão de etapas poderá invalidar os resultados dessa etapa.

### Interrompendo canvas

Parar um Canva não sai dos usuários que estão esperando em uma etapa. Se você reativar o Canva e os usuários ainda estiverem esperando, eles completam a etapa e avançam para a próxima etapa. No entanto, se o tempo que o usuário deveria ter avançado para a próxima etapa já tiver passado, ele sai do Canva. 

Por exemplo, digamos que você tenha um Canva criado usando o fluxo de trabalho Canvas Flow programado para ser iniciado às 14h com uma variante com duas etapas: uma etapa de postergação com um atraso de uma hora que vai para uma etapa de Mensagem. 

Um usuário entra nesse canva às 14h01 e entra na etapa do canva ao mesmo tempo. Isso significa que o usuário está programado para passar para a próxima etapa da jornada do usuário (a etapa de Mensagem) às 15h01. Se você parar o Canva às 14h30 e reativar o Canva às 15h30, o usuário sai do Canva, pois já é depois das 15h01. No entanto, se você reativar o Canva às 14h40, o usuário avança para a etapa de Mensagem como esperado às 15h01.

## Coisas para saber

Os seguintes problemas comuns podem ser acionados ao editar ou adicionar mais componentes a qualquer outro componente em um Canva após o lançamento. 

{% alert important %}
Os seguintes problemas são evitáveis. Se você precisar fazer edições em um Canva após ele ter sido lançado, recomendamos primeiro confirmar que todos os usuários que já entraram no Canva completaram sua jornada do usuário. Além disso, sugerimos que você não exclua etapas que já foram processadas por pelo menos um usuário.
{% endalert %}

- Dados de relatório ausentes (quando variantes de mensagem são excluídas e re-adicionadas)
- Os usuários não estão seguindo o caminho esperado
- As mensagens são enviadas em horários inesperados
- As edições não sobrescrevem os dados Currents, então você pode notar discrepâncias entre as etapas do Canva (como `canvas_step_ids` que não existem no Canva devido à exclusão)
- Os usuários podem receber a mesma mensagem duas vezes
- Os usuários não receberão mensagens devido ao limite de frequência existente
  - Quando você atualiza o limite de frequência em um Canva ativo, o novo limite de frequência entra em vigor para todos os envios de mensagens futuros, incluindo usuários que já estão no Canva. No entanto, devido ao cache interno (de até 30 segundos), pode haver um breve atraso antes que o novo limite de frequência seja totalmente aplicado. Observe que o Braze coloca os usuários na fila para a etapa de Mensagem em que estão atualmente, então o limite de frequência em vigor quando a mensagem de cada etapa é realmente enviada é o que se aplica.
- Quando um Canva é [parado automaticamente]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/about_statuses/#available-statuses), os rascunhos pós-lançamento do Canva também são excluídos.
