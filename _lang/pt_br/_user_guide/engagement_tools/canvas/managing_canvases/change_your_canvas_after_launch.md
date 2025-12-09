---
nav_title: Edição de telas após o lançamento
article_title: Edição de telas após o lançamento
page_order: 0
description: "Este artigo de referência aborda os diferentes aspectos de um Canvas que podem ser alterados após o lançamento inicial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Edição de telas após o lançamento

> Este artigo de referência aborda o que pode ser alterado em um Canvas após o lançamento inicial.

Você pode editar seus Canvases após o lançamento:

* Inserção de novas etapas do Canvas na jornada do usuário
* Adição de novas variantes e conexões
* Ajuste da distribuição de variantes
* Interromper ou retomar todas as etapas do Canvas

{% alert note %}
A distribuição da variante de controle só pode ser reduzida após o lançamento.
{% endalert %}

Tenha em mente as seguintes edições permitidas do Canvas após o lançamento, dependendo do fluxo de trabalho com o qual o Canvas foi criado. Se o seu Canvas usar o fluxo de trabalho original do Canvas, você precisará clonar o Canvas Flow primeiro para realizar as edições pós-lançamento.

Você pode excluir qualquer um dos itens a seguir em sua jornada de usuário:

- [Etapas do Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/about/)
- Variantes de tela 
- Conexões entre as etapas do Canvas

Se quiser editar ou adicionar mais etapas à jornada do usuário do Canvas, os detalhes a seguir serão aplicados:

- Os usuários que ainda não entraram no Canvas são elegíveis para todas as etapas recém-criadas. 
- Se as configurações de entrada do Canvas permitirem que os usuários entrem novamente nas etapas, os usuários que já foram aprovados nas etapas recém-criadas estarão qualificados para entrar novamente.
- Os usuários que estão atualmente em um Canvas lançado, mas não atingiram os pontos da jornada do usuário em que novas etapas são adicionadas, estão qualificados para receber essas etapas recém-adicionadas. 

Se você excluir uma etapa [de Atraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) ou [Caminhos de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), poderá opcionalmente redirecionar os usuários que estão aguardando na etapa para outra etapa do Canvas. Para atrasos, os usuários permanecerão na etapa até o final do período de atraso. Para os Caminhos de Ação, os usuários permanecerão na etapa até o final da janela de avaliação.

Observe que quando você inicia um Canvas inicialmente, o Braze enfileira os usuários para a etapa da mensagem em que eles estão, e não para todas as mensagens subsequentes no Canvas. Se você fizer uma edição no Canvas após o lançamento, alguns usuários já estarão na fila e não receberão as alterações. Se você interromper o Canvas, duplicá-lo, alterá-lo e lançar essa nova versão, o Canvas reavaliará todos os usuários novamente, não apenas os usuários que ainda não foram enfileirados.

Consulte a seção [Práticas recomendadas](#best-practices) para obter casos de uso específicos de edição. Em geral, é uma prática recomendada evitar a edição de Canvases ao vivo, pois pode haver um comportamento inesperado.

{% details Expand for original Canvas editor details %}

Não é possível editar ou excluir conexões existentes e não é possível inserir uma etapa entre etapas conectadas existentes. Se quiser editar ou adicionar mais etapas à jornada do usuário do Canvas, os detalhes a seguir serão aplicados:

- Os usuários que ainda não entraram no Canvas são elegíveis para todas as etapas recém-criadas. 
- Se as configurações de entrada do Canvas permitirem que os usuários entrem novamente nas etapas, os usuários que já foram aprovados nas etapas recém-criadas estarão qualificados para entrar novamente.
- Os usuários que estão atualmente em um Canvas lançado, mas que não alcançaram as etapas recém-adicionadas na jornada do usuário, estão qualificados para receber essas etapas recém-adicionadas.
- Se uma etapa de Atraso for a última etapa no Canvas, os usuários que alcançarem essa etapa serão automaticamente avançados para fora do Canvas e não receberão nenhuma etapa recém-criada.

{% alert important %}
Se as configurações de **Atraso** ou **Janela** forem atualizadas para uma etapa do Canvas, os usuários que estiverem nessa etapa no momento da atualização obedecerão ao tempo de atraso que foi atribuído quando eles entraram nela originalmente. Somente os novos usuários que entrarem no Canvas e aqueles que ainda não foram colocados na fila para essa etapa receberão a mensagem no momento da atualização.
{% endalert %}

A interrupção de um Canvas não encerrará os usuários que estiverem esperando para receber uma mensagem. Se você reativar o Canvas e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o tempo em que a mensagem deveria ter sido enviada já tenha passado, então eles não a receberão).

{% enddetails %}

## Detalhes da tela

Você pode editar as seguintes configurações e informações do Canvas depois que um Canvas for iniciado:

* Nome e descrição do Canvas
* Equipes e etiquetas
* Tipo de entrada, cronograma e controles
* Status da assinatura
* Limitação de taxa
* Limite de frequência
* Horário de silêncio
* Público-alvo

Após o lançamento do Canvas:

- Os eventos de conversão não podem ser editados. 
- As etapas a seguir não podem ser adicionadas ou removidas e não podem ser reordenadas para ajustar a classificação: [Caminhos do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths/), [caminhos da ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/) e [caminhos do experimento]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step/).
  - **Solução alternativa 1:** Crie um novo Caminho do público-alvo, Caminho da ação ou Caminho do experimento e reconfigure os caminhos para essa nova etapa.
  - **Solução alternativa 2:** Duplique o Canvas para fazer suas edições.

### Etapas individuais

Para etapas individuais do Canvas, você pode editar os seguintes detalhes após o lançamento:

* Nome
* Conteúdo da mensagem
* Gatilhos
* Público
* Eventos de exceção
* Atrasos

No entanto, o tipo de cronograma e as porcentagens de controle da etapa não são editáveis após o lançamento. Para as etapas de Caminhos de ação e Caminhos de público-alvo, as classificações não são editáveis após o lançamento.

### Porcentagens de variantes de tela

Depois de lançar um Canvas, você só pode diminuir as porcentagens da variante de controle. Se uma porcentagem de variante for modificada no Canvas, você descobrirá que seus usuários podem ser redistribuídos para outras variantes.

Inicialmente, esses usuários recebem aleatoriamente uma variante específica antes de receberem uma campanha pela primeira vez. A partir de então, cada vez que a campanha for recebida (ou o usuário entrar novamente em uma variante do Canvas), ele receberá a mesma variante, a menos que as porcentagens da variante sejam modificadas.

Se as porcentagens de variantes mudarem, os usuários poderão ser redistribuídos para outras variantes. Os usuários permanecerão nessas variantes até que as porcentagens sejam modificadas novamente. Observe que, para Canvases que usam ramificação com filtros `NOT` com números de balde aleatórios, os usuários podem não receber a mesma ramificação todas as vezes em sua jornada de usuário quando entrarem novamente no Canvas.

#### Grupos de controle

Os grupos de controle permanecem consistentes se a porcentagem da variante não for alterada. Se a porcentagem de um grupo de controle for diminuída ou aumentada, os usuários que receberam mensagens anteriormente não poderão entrar no grupo de controle em um envio posterior, e nenhum usuário do grupo de controle jamais receberá uma mensagem.

### Hora de envio local

As telas programadas para serem lançadas em um horário de envio local podem ser editadas até 24 horas antes do horário de envio programado. Essa janela é chamada de "zona de segurança". 

{% alert tip %}
Se você pretende fazer edições maiores que levem à criação de uma nova cópia do Canvas, lembre-se de excluir os usuários que receberam o primeiro Canvas e reajuste os horários da programação do Canvas para permitir o envio por fuso horário.
{% endalert %}

### Exclusão de variantes

Quando as variantes são excluídas de um Canvas, ocorre o seguinte:

- As etapas dentro da variante (incluindo aquelas compartilhadas por outras variantes) serão excluídas. 
- As análises de etapa e as análises de nível superior do Canvas, como _Total de entradas_, _Total de saídas_ e _Taxa de conversão_, serão excluídas.
- Os usuários em variantes excluídas são encerrados das etapas, e as mensagens seguintes não são enviadas.

### Propriedades de entrada de tela

As propriedades de entrada do Canvas não são modeladas em etapas quando enviadas. Isso significa que quando as propriedades de entrada do Canvas forem editadas após o lançamento do Canvas, essas alterações só serão aplicadas aos novos usuários que entrarem no Canvas. Se o seu Canvas permitir que os usuários entrem novamente no Canvas, todos os usuários que entrarem novamente serão determinados pelas propriedades de entrada atualizadas do Canvas.

## Práticas recomendadas

Confira estas práticas recomendadas para ter em mente ao editar ou adicionar algo ao seu Canvas depois que ele for lançado.

{% alert important %}
Em geral, evite fazer alterações enquanto o Canvas estiver ativo e enfileirando usuários.
{% endalert %}

### Etapas desconectadas

Você pode iniciar seu Canvas com etapas desconectadas e também salvar esses Canvases após o lançamento. Antes de desconectar uma etapa do seu fluxo de trabalho, recomendamos verificar a exibição de análise das etapas para usuários pendentes.

Digamos que um usuário esteja em uma etapa desconectada do seu fluxo de trabalho do Canvas. Esse usuário avançará para a etapa seguinte, se houver uma. As configurações da etapa ditarão como o usuário deve avançar. 

Ao criar ou editar etapas desconectadas, você pode fazer alterações nessas etapas independentes sem precisar conectá-las diretamente ao restante do Canvas. Isso ajuda a testar suas etapas antes de iniciar o Canvas novamente. 

### Etapa do caminho do experimento

Se o seu Canvas tiver um experimento de Caminho vencedor ou Caminho personalizado ativo ou em andamento e você atualizar o Canvas ativo, independentemente de atualizar a própria etapa do Caminho do experimento, o experimento em andamento será encerrado e a etapa do experimento não determinará um caminho vencedor ou caminhos personalizados. Para reiniciar o experimento, você pode desconectar o Caminho do Experimento existente e iniciar um novo, ou duplicar o Canvas e iniciar um novo Canvas. Caso contrário, os usuários percorrerão o caminho do experimento como se nenhum método de otimização tivesse sido selecionado.

### Atrasos de tempo

A edição de telas com atrasos de tempo pode ser um pouco complicada! Portanto, tenha em mente os detalhes a seguir ao fazer edições em seus Canvases.

Se você atualizar o atraso em uma etapa de Atraso ou janela de avaliação na etapa Caminhos de ação, somente os novos usuários que entrarem no Canvas e os usuários que não estiverem na fila para essa etapa receberão a mensagem com o atraso atualizado.

Se você excluir uma etapa com um atraso de tempo (como Atraso ou Caminhos de ação) e decidir redirecionar esses usuários para outra etapa do Canvas, os usuários só serão redirecionados após a conclusão do atraso de tempo da etapa. Por exemplo, digamos que você exclua uma etapa de Atraso com um dia de atraso e redirecione esses usuários para uma etapa de Mensagem. Nesse caso, os usuários só serão redirecionados após o término do prazo de um dia.

Se o seu Canvas tiver uma ou mais etapas de Caminhos de Experimentos, a exclusão de etapas poderá invalidar os resultados dessa etapa.

### Parando as telas

A interrupção de um Canvas não encerrará os usuários que estão aguardando em uma etapa. Se você reativar o Canvas e os usuários ainda estiverem esperando, eles concluirão a etapa e passarão para a próxima etapa. No entanto, se o tempo em que o usuário deveria ter avançado para a próxima etapa já tiver passado, ele sairá do Canvas. 

Por exemplo, digamos que você tenha um Canvas criado usando o fluxo de trabalho Canvas Flow definido para ser lançado às 14h com uma variante com duas etapas: uma etapa de Atraso com uma hora de atraso que vai para uma etapa de Mensagem. 

Um usuário entra nesse Canvas às 2:01 pm e entra na etapa Delay ao mesmo tempo. Isso significa que o usuário será programado para passar para a próxima etapa da jornada do usuário (a etapa Mensagem) às 15h01min. Se você interromper o Canvas às 14h30min e reativá-lo às 15h30min, o usuário sairá do Canvas, pois já passa das 15h01min. No entanto, se você reativar o Canvas às 14:40h, o usuário passará para a etapa de Mensagem, conforme esperado, às 15:01h.

## Coisas para saber

Os seguintes problemas comuns podem ser acionados ao editar ou adicionar mais componentes a qualquer outro componente em um Canvas após o lançamento. 

{% alert important %}
Os problemas a seguir são evitáveis. Se precisar fazer edições em um Canvas depois de ele ter sido lançado, recomendamos primeiro confirmar se todos os usuários que já entraram no Canvas concluíram a jornada do usuário. Além disso, sugerimos que você não exclua etapas que já tenham processado pelo menos um usuário.
{% endalert %}

- Dados de relatório ausentes (quando as variantes de mensagem são excluídas e adicionadas novamente)
- Os usuários não estão seguindo o caminho esperado
- As mensagens são enviadas em momentos inesperados
- As edições não substituem os dados do Currents, portanto, você pode notar discrepâncias entre as etapas do Canvas (como `canvas_step_ids` que não existe no Canvas devido à exclusão)
- Os usuários podem receber a mesma mensagem duas vezes
- Os usuários são impedidos de receber mensagens devido ao limite de taxa existente
  - Quando os usuários são despachados para um Canvas, o limite de taxa aplicado ao Canvas quando um usuário é despachado é aplicado ao usuário. Depois que o Canvas é enviado, o limite de taxa não pode ser editado para esse usuário, portanto, aumentar ou diminuir o limite de taxa após o lançamento não afetará os usuários que já foram enviados.