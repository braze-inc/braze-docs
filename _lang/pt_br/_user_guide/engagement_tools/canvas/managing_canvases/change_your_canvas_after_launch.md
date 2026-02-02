---
nav_title: Editar telas após o lançamento
article_title: Editar telas após o lançamento
page_order: 0
description: "Este artigo de referência aborda os diferentes aspectos de um Canva que podem ser alterados após o lançamento inicial."
alias: "/post-launch_edits/"
page_type: reference
tool:
  - Canvas

---

# Editar telas após o lançamento

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

Se quiser editar ou adicionar mais etapas à jornada do usuário do Canva, os detalhes a seguir se aplicam:

- Os usuários que ainda não entraram no Canva são elegíveis para todas as etapas recém-criadas. 
- Se as configurações de entrada do Canva permitirem que os usuários entrem novamente nas etapas, os usuários que já passaram nas etapas recém-criadas serão elegíveis para entrar novamente.
- Os usuários que estão atualmente em um Canvas lançado, mas que não atingiram os pontos da jornada do usuário em que novas etapas são adicionadas, são elegíveis para receber essas etapas recém-adicionadas. 

Se você excluir uma etapa [de postergação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/) ou [jornadas de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths/), poderá opcionalmente redirecionar os usuários que estão aguardando na etapa para outra etapa do Canva. Para atrasos, os usuários permanecerão na etapa até o final do período de postergação. Para as jornadas de ação, os usuários permanecerão na etapa até o final da janela de avaliação.

Observe que, ao iniciar um Canvas inicialmente, o Braze enfileira os usuários para a etapa de mensagens em que eles se encontram, e não para todas as mensagens subsequentes no Canvas. Se você fizer uma edição no Canva após o lançamento, alguns usuários já estarão na fila e não receberão as alterações. Se você interromper o canva, duplicá-lo, alterá-lo e lançar essa nova versão, o canva reavaliará todos os usuários novamente, não apenas os usuários que ainda não foram enfileirados.

Consulte a seção [Práticas recomendadas](#best-practices) para obter casos de uso específicos de edição. Em geral, é uma prática recomendada evitar a edição de canvas ativos, pois pode haver um comportamento inesperado.

{% details Expand for original Canvas editor details %}

Tenha em mente as seguintes edições permitidas do Canvas após o lançamento, dependendo do fluxo de trabalho com o qual o Canvas foi criado. Se o seu Canvas usar o fluxo de trabalho original do Canvas, você precisará cloná-lo para o Canvas Flow primeiro para realizar edições pós-lançamento.

Não é possível editar ou excluir conexões existentes e não é possível inserir uma etapa entre etapas conectadas existentes. Se quiser editar ou adicionar mais etapas à jornada do usuário do canva, os detalhes a seguir serão aplicados:

- Os usuários que ainda não entraram no Canva são elegíveis para todas as etapas recém-criadas. 
- Se as configurações de entrada do Canva permitirem que os usuários entrem novamente nas etapas, os usuários que já passaram nas etapas recém-criadas serão elegíveis para entrar novamente.
- Os usuários que estão atualmente em um Canvas lançado, mas que não alcançaram as etapas recém-adicionadas na jornada do usuário, são elegíveis para receber essas etapas recém-adicionadas.
- Se uma etapa de postergação for a última etapa do Canva, os usuários que alcançarem essa etapa serão automaticamente avançados para fora do Canvas e não receberão nenhuma etapa recém-criada.

{% alert important %}
Se as configurações de **Atraso** ou **Janela** de uma etapa do canva forem atualizadas, os usuários que estiverem nessa etapa no momento da atualização obedecerão ao tempo de postergação atribuído quando eles entraram nela originalmente. Somente os novos usuários que entrarem no Canva e aqueles que ainda não foram colocados na fila para essa etapa receberão a mensagem no momento da atualização.
{% endalert %}

A interrupção de um Canva não encerrará os usuários que estiverem esperando para receber uma mensagem. Se você reativar o Canva e os usuários ainda estiverem aguardando a mensagem, eles a receberão (a menos que o tempo em que a mensagem deveria ter sido enviada já tenha passado, então eles não a receberão).

{% enddetails %}

## Detalhes da tela

Você pode editar as seguintes configurações e detalhes depois de iniciar um Canva:

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
* Atrasos (somente para etapas de postergação)

No entanto, o tipo de programação e as porcentagens de controle da etapa não são editáveis após o lançamento. Para as etapas de jornadas de ação e jornadas do público, as janelas de classificação e avaliação não são editáveis após o lançamento.

### Porcentagens de variantes de tela

Depois de lançar um canva, só é possível diminuir as porcentagens da variante de controle. Se uma porcentagem de variante for modificada no Canva, você verá que seus usuários poderão ser redistribuídos para outras variantes.

Inicialmente, esses usuários são atribuídos aleatoriamente a uma variante específica antes de receberem uma campanha pela primeira vez. A partir de então, cada vez que a campanha for recebida (ou o usuário entrar novamente em uma variante do Canva), ele receberá a mesma variante, a menos que as porcentagens da variante sejam modificadas.

Se as porcentagens de variantes mudarem, os usuários poderão ser redistribuídos para outras variantes. Os usuários permanecerão nessas variantes até que as porcentagens sejam modificadas novamente. Note que, para Canvas que usam ramificação com filtros `NOT` com números de balde aleatórios, os usuários podem não receber a mesma ramificação todas as vezes em sua jornada de usuário quando entrarem novamente no Canvas.

#### Grupos de controle

Os grupos de controle permanecem consistentes se a porcentagem da variante não for alterada. Se a porcentagem de um grupo de controle for diminuída ou aumentada, os usuários que receberam mensagens anteriormente não poderão entrar no grupo de controle em um envio posterior, nem nenhum usuário do grupo de controle jamais receberá uma mensagem.

### Tempo de envio local

As telas programadas para serem lançadas em um horário de envio local podem ser editadas até 24 horas antes do horário de envio programado. Essa janela é chamada de "zona de segurança". 

{% alert tip %}
Caso pretenda fazer edições maiores que levem à criação de uma nova cópia do Canvas, lembre-se de excluir os usuários que receberam o primeiro Canvas e reajuste os horários da programação do Canvas para permitir o envio por fuso horário.
{% endalert %}

Quando uma programação de entrada é definida para inserir usuários imediatamente após o lançamento, o Canva é lançado no horário mais próximo em incrementos de 5 minutos. Por exemplo, se você atualizar uma tela para inserir usuários imediatamente às 8h31 PST, o horário de lançamento será definido como 8h30 PST e no fuso horário da empresa.

### Exclusão de variantes

Quando as variantes são excluídas de um Canva, ocorre o seguinte:

- As etapas dentro da variante (incluindo aquelas compartilhadas por outras variantes) serão excluídas. 
- A análise de etapas e a análise de dados de nível superior do Canva, como _Total de entradas_, _Total de saídas_ e _Taxa de conversão_, serão excluídas.
- Os usuários das variantes excluídas são excluídos das etapas e as mensagens seguintes não são enviadas.

### Propriedades de entrada da tela

As propriedades de entrada do canva não estão no formato de modelos em etapas quando enviadas. Isso significa que, quando as propriedades de entrada do Canvas forem editadas após o lançamento do Canvas, essas alterações só serão aplicadas aos novos usuários que entrarem no Canvas. Se o seu canva permitir que os usuários reentrem no canva, qualquer usuário que reentrar será determinado pelas propriedades de entrada do canva atualizadas.

## Melhores práticas

Confira estas melhores práticas a serem lembradas ao editar ou adicionar ao seu canva após seu lançamento.

{% alert important %}
Em geral, evite fazer alterações enquanto o Canva estiver ativo e enfileirando usuários.
{% endalert %}

### Etapas desconectadas

Você pode iniciar seu Canvas com etapas desconectadas e também salvar esses Canvases após o lançamento. Antes de desconectar uma etapa do seu fluxo de trabalho, recomendamos verificar a exibição de análise de dados das etapas para usuários pendentes.

Digamos que um usuário esteja em uma etapa desconectada do seu fluxo de trabalho do Canva. Esse usuário avançará para a etapa seguinte, se houver uma. As configurações da etapa ditarão como o usuário deve avançar. 

Ao criar ou editar etapas desconectadas, você pode fazer alterações nessas etapas independentes sem precisar conectá-las diretamente ao restante do Canva. Isso ajuda a testar suas etapas antes de lançar o Canvas novamente. 

### Etapa da jornada experimental

Se o seu Canva tiver um experimento de caminho vencedor ou caminho personalizado ativo ou em andamento e você atualizar o Canva ativo (independentemente de atualizar a etapa do caminho experimental), o experimento em andamento será encerrado e a etapa de caminhos experimentais não determinará um caminho vencedor ou caminhos personalizados. Para reiniciar o experimento, é possível desconectar a jornada experimental existente e iniciar uma nova, ou duplicar o Canvas e iniciar um novo Canvas. Caso contrário, os usuários percorrerão a jornada experimental como se nenhum método de otimização tivesse sido selecionado.

### Postergação de tempo

A edição de telas com postergação de tempo pode ser um pouco complicada! Portanto, lembre-se dos detalhes a seguir ao fazer edições em suas telas.

Se você atualizar a postergação em uma etapa de Atraso, somente os novos usuários que entrarem no Canva e os usuários que não estiverem na fila para essa etapa receberão a mensagem no tempo de atraso atualizado.

Se você excluir uma etapa com um atraso de tempo (como Atraso ou Jornadas de ação) e decidir redirecionar esses usuários para outra etapa do Canva, os usuários só serão redirecionados depois que o atraso de tempo da etapa for concluído. Por exemplo, digamos que você exclua uma etapa de Atraso com uma postergação de um dia e redirecione esses usuários para uma etapa de Mensagem. Nesse caso, os usuários só serão redirecionados após a conclusão da postergação de um dia.

Se o seu Canva tiver uma ou mais etapas de jornadas experimentais, a exclusão de etapas poderá invalidar os resultados dessa etapa.

### Interrompendo canvas

A interrupção de um Canva não encerrará os usuários que estiverem aguardando em uma etapa. Se você ativar novamente o Canva e os usuários ainda estiverem esperando, eles concluirão a etapa e passarão para a próxima etapa. No entanto, se o tempo em que o usuário deveria ter avançado para a próxima etapa já tiver passado, ele sairá do Canva. 

Por exemplo, digamos que você tenha um Canvas criado usando o fluxo de trabalho Canvas Flow definido para ser lançado às 14 horas com uma variante com duas etapas: uma etapa de Atraso com uma postergação de uma hora que vai para uma etapa de Mensagens. 

Um usuário entra nesse canva às 14h01 e entra na etapa do canva ao mesmo tempo. Isso significa que o usuário será programado para passar para a próxima etapa da jornada do usuário (a etapa Mensagem) às 15h01min. Se você interromper o canva às 14h30 e reativá-lo às 15h30, o usuário sairá do canva, pois já passa das 15h01. No entanto, se você reativar o canva às 14h40, o usuário passará para a etapa de Mensagem, conforme esperado, às 15h01.

## Coisas para saber

Os seguintes problemas comuns podem ser disparados ao editar ou adicionar mais componentes a qualquer outro componente em uma tela após o lançamento. 

{% alert important %}
Os problemas a seguir podem ser evitados. Se precisar fazer edições em um Canvas depois de ele ter sido lançado, recomendamos primeiro confirmar se todos os usuários que já entraram no Canvas concluíram sua jornada de usuário. Além disso, sugerimos que não exclua etapas que já tenham sido processadas por pelo menos um usuário.
{% endalert %}

- Dados de relatório ausentes (quando as variantes de mensagem são excluídas e adicionadas novamente)
- Os usuários não estão seguindo a jornada esperada
- Envio de mensagens em momentos inesperados
- As edições não substituem os dados do Currents, portanto, você pode notar discrepâncias entre as etapas do Canva (como `canvas_step_ids` que não existe no Canvas devido à exclusão)
- Os usuários podem receber a mesma mensagem duas vezes
- Os usuários não receberão mensagens devido ao limite de frequência existente
  - Quando os usuários são enviados para um Canvas, o limite de frequência aplicado ao Canvas quando um usuário é enviado é aplicado ao usuário. Depois que a tela é enviada, o limite de frequência não pode ser editado para esse usuário, portanto, aumentar ou diminuir o limite de frequência após o lançamento não afetará os usuários que já foram enviados.
