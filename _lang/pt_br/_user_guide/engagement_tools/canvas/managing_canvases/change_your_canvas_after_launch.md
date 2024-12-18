---
nav_title: Edição de telas após o lançamento
article_title: Edição de telas após o lançamento
page_order: 0
description: "Este artigo de referência aborda os diferentes aspectos de um Canva que podem ser alterados após o lançamento inicial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Edição de telas após o lançamento

> Este artigo de referência aborda o que pode ser alterado em um Canva após o lançamento inicial.

Você pode editar suas Canvas após o lançamento:

* Inserção de novas etapas do Canva na jornada do usuário
* Adição de novas variantes e conexões
* Ajuste da distribuição de variantes
* Interromper ou retomar todas as etapas do Canva

{% alert note %}
A distribuição da variante de controle só pode ser reduzida após o lançamento.
{% endalert %}

Tenha em mente as seguintes edições permitidas do Canvas após o lançamento, dependendo do fluxo de trabalho com o qual o Canvas foi criado. Se o seu canva usar o fluxo de trabalho original do canva, será necessário clonar o Canvas Flow primeiro para realizar as edições pós-lançamento.

Você pode excluir qualquer um dos itens a seguir em sua jornada de usuário:

- [Etapas do canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components)
- Variantes da tela 
- Conexões entre as etapas do Canva

Se quiser editar ou adicionar mais etapas à jornada do usuário do canva, os detalhes a seguir serão aplicados:

- Os usuários que ainda não entraram no Canva são elegíveis para todas as etapas recém-criadas. 
- Se as configurações de entrada do Canva permitirem que os usuários entrem novamente nas etapas, os usuários que já passaram nas etapas recém-criadas serão elegíveis para entrar novamente.
- Os usuários que estão atualmente em um Canvas lançado, mas que não atingiram os pontos da jornada do usuário em que novas etapas são adicionadas, são elegíveis para receber essas etapas recém-adicionadas. 

Se você excluir uma etapa [de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) ou [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), poderá opcionalmente redirecionar os usuários que estão aguardando na etapa para outra etapa do Canva. Para atrasos, os usuários permanecerão na etapa até o final do período de postergação. Para as jornadas de ação, os usuários permanecerão na etapa até o final da janela de avaliação.

Observe que, ao iniciar um Canvas inicialmente, o Braze enfileira os usuários para a etapa de mensagens em que eles se encontram, e não para todas as mensagens subsequentes no Canvas. Se você fizer uma edição no Canva após o lançamento, alguns usuários já estarão na fila e não receberão as alterações. Se você interromper o canva, duplicá-lo, alterá-lo e lançar essa nova versão, o canva reavaliará todos os usuários novamente, não apenas os usuários que ainda não foram enfileirados.

Consulte a seção [Práticas recomendadas](#best-practices) para obter casos de uso específicos de edição. Em geral, é uma prática recomendada evitar a edição de canvas ativos, pois pode haver um comportamento inesperado.

{% details Editor de tela original %}

{% alert important %}
A partir de 28 de fevereiro de 2023, não será mais possível criar ou duplicar Canvas usando a experiência original do Canvas. A Braze recomenda que os clientes que usam a experiência original do Canvas migrem para o Canvas Flow. É uma experiência de edição aprimorada para criar e gerenciar melhor as telas. Saiba mais sobre a [clonagem de canvas no Canvas Flow]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/cloning_canvases/).
{% endalert %}

Não é possível editar ou excluir conexões existentes e não é possível inserir uma etapa entre etapas conectadas existentes. Se quiser editar ou adicionar mais etapas à jornada do usuário do canva, os detalhes a seguir serão aplicados:

- Os usuários que ainda não entraram no Canva são elegíveis para todas as etapas recém-criadas. 
- Se as configurações de entrada do Canva permitirem que os usuários entrem novamente nas etapas, os usuários que já passaram nas etapas recém-criadas serão elegíveis para entrar novamente.
- Os usuários que estão atualmente em um Canvas lançado, mas que não alcançaram as etapas recém-adicionadas na jornada do usuário, são elegíveis para receber essas etapas recém-adicionadas.

Se você atualizar as configurações de **Atraso** ou **Janela** de uma etapa do Canva, somente os novos usuários que entrarem no Canva e os usuários que ainda não estiverem na fila para essa etapa receberão a mensagem com a postergação atualizada. Se uma etapa de postergação for a última etapa do Canva, os usuários que alcançarem essa etapa serão automaticamente avançados para fora do Canvas e não receberão nenhuma etapa recém-criada. 

{% alert note %}
A interrupção de um Canva não encerrará os usuários que estiverem esperando para receber uma mensagem. Se você reativar o Canva e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o tempo em que a mensagem deveria ter sido enviada já tenha passado, então eles não a receberão).
{% endalert %}

{% enddetails %}

## Detalhes da tela

Você pode editar as seguintes configurações e informações do Canvas depois que um Canvas for iniciado:

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
- As jornadas [do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), as jornadas [de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) e [as jornadas experimentais]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step) não podem ser adicionadas ou removidas dessas etapas e não podem ser reordenadas para ajustar a classificação. Como solução alternativa, edite o Canva ativo e duplique a etapa, que será editável até que você inicie o rascunho.

### Etapas individuais

Para etapas individuais do Canva, você pode editar os seguintes detalhes após o lançamento:

* Nome
* Conteúdo das mensagens
* Gatilhos
* Público
* Eventos de exceção
* Postergações

No entanto, o tipo de programação e as porcentagens de controle da etapa não são editáveis após o lançamento. Para as etapas de jornadas de ação e jornadas do público, as classificações não são editáveis após o lançamento.

### Porcentagens de variantes de tela

Depois de lançar um canva, só é possível diminuir as porcentagens da variante de controle. Se uma porcentagem de variante for modificada no Canva, você verá que seus usuários poderão ser redistribuídos para outras variantes.

Inicialmente, esses usuários são atribuídos aleatoriamente a uma variante específica antes de receberem uma campanha pela primeira vez. A partir de então, cada vez que a campanha for recebida (ou o usuário entrar novamente em uma variante do Canva), ele receberá a mesma variante, a menos que as porcentagens da variante sejam modificadas.

Se as porcentagens de variantes mudarem, os usuários poderão ser redistribuídos para outras variantes. Os usuários permanecerão nessas variantes até que as porcentagens sejam modificadas novamente. Note que, para Canvas que usam ramificação com filtros `NOT` com números de balde aleatórios, os usuários podem não receber a mesma ramificação todas as vezes em sua jornada de usuário quando entrarem novamente no Canvas.

#### Grupos de controle

Os grupos de controle permanecem consistentes se a porcentagem da variante não for alterada. Se a porcentagem de um grupo de controle for diminuída ou aumentada, os usuários que receberam mensagens anteriormente não poderão entrar no grupo de controle em um envio posterior, nem nenhum usuário do grupo de controle jamais receberá uma mensagem.

### Tempo de envio local

Os canvas programados para serem lançados em um horário de envio local podem ser editados até 24 horas antes do horário de envio programado. Essa janela é chamada de "zona de segurança". 

{% alert tip %}
Caso pretenda fazer edições maiores que levem à criação de uma nova cópia do Canvas, lembre-se de excluir os usuários que receberam o primeiro Canvas e reajuste os horários da programação do Canvas para permitir o envio por fuso horário.
{% endalert %}

### Exclusão de variantes

Quando as variantes são excluídas de um Canva, ocorre o seguinte:
- As etapas dentro da variante (incluindo aquelas compartilhadas por outras variantes) serão excluídas. 
- A análise de etapas e a análise de dados de nível superior do Canva, como _Total de entradas_, _Total de saídas_ e _Taxa de conversão_, serão excluídas.
- Os usuários das variantes excluídas são excluídos das etapas e as mensagens seguintes não são enviadas.

## Melhores práticas

Confira estas práticas recomendadas que você deve ter em mente ao editar ou adicionar ao seu Canvas depois que ele for lançado usando o Canvas Flow.

### Etapas desconectadas

Você pode iniciar seu Canvas com etapas desconectadas e também salvar esses Canvases após o lançamento. Antes de desconectar uma etapa do seu fluxo de trabalho, recomendamos verificar a exibição de análise de dados das etapas para usuários pendentes.

Digamos que um usuário esteja em uma etapa desconectada do seu fluxo de trabalho do Canva. Esse usuário avançará para a etapa seguinte, se houver uma. As configurações da etapa ditarão como o usuário deve avançar. 

Ao criar ou editar etapas desconectadas, você pode fazer alterações nessas etapas independentes sem precisar conectá-las diretamente ao restante do Canva. Isso ajuda a testar suas etapas antes de iniciar o canva novamente. 

### Etapa da jornada experimental

Se o seu canvas tiver uma etapa da jornada experimental ativa ou em andamento e você atualizar o canva ativo (mesmo que não seja a etapa do caminho experimental), o experimento em andamento será reiniciado. Para evitar que seus usuários entrem novamente na jornada experimental, é possível duplicar e criar um novo Canvas em vez de atualizar o Canvas.

### Postergação de tempo

A edição de telas com postergação de tempo pode ser um pouco complicada! Portanto, lembre-se dos detalhes a seguir ao fazer edições em suas telas.

Se você atualizar o atraso em uma etapa de Atraso ou em uma janela de avaliação na etapa das jornadas de ação, somente os novos usuários que entrarem no Canva e os usuários que não estiverem na fila para essa etapa receberão a mensagem com a postergação atualizada.

Se você excluir uma etapa com um atraso de tempo (como Atraso ou Jornadas de ação) e decidir redirecionar esses usuários para outra etapa do Canva, os usuários só serão redirecionados depois que o atraso de tempo da etapa for concluído. Por exemplo, digamos que você exclua uma etapa de Atraso com uma postergação de um dia e redirecione esses usuários para uma etapa de Mensagem. Nesse caso, os usuários só serão redirecionados após a conclusão da postergação de um dia.

Se o seu Canva tiver uma ou mais etapas de jornadas experimentais, a exclusão de etapas poderá invalidar os resultados dessa etapa.

### Interrompendo canvas

A interrupção de um Canva não encerrará os usuários que estiverem aguardando em uma etapa. Se você ativar novamente o Canva e os usuários ainda estiverem esperando, eles concluirão a etapa e passarão para a próxima etapa. No entanto, se o tempo em que o usuário deveria ter avançado para a próxima etapa já tiver passado, ele sairá do Canva. 

Por exemplo, digamos que você tenha um canva criado usando o fluxo de trabalho Canvas Flow definido para ser lançado às 14h com uma variante com duas etapas: uma etapa de portergação com uma hora de postergação que vai para uma etapa de Mensagem. 

Um usuário entra nesse canva às 14h01 e entra na etapa do canva ao mesmo tempo. Isso significa que o usuário será programado para passar para a próxima etapa da jornada do usuário (a etapa Mensagem) às 15h01min. Se você interromper o canva às 14h30 e reativá-lo às 15h30, o usuário sairá do canva, pois já passa das 15h01. No entanto, se você reativar o canva às 14h40, o usuário passará para a etapa de Mensagem, conforme esperado, às 15h01.