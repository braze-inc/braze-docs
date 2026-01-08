---
nav_title: Visualizar caminhos do usuário
article_title: Visualizar caminhos do usuário
page_order: 0.3
alias: /preview_user_paths/
description: "Esta página aborda como você pode visualizar os caminhos do usuário no Canvas."
Tool:
  - Canvas
---

# Visualizar caminhos do usuário no Canvas

> Experimente a jornada do Canvas que você criou para seus usuários. Isso inclui a visualização do tempo e das mensagens que eles receberão. Essas execuções de teste funcionam como garantia de qualidade de que suas mensagens são enviadas para o público certo, tudo isso antes de enviar seu Canvas.

## Criação de uma execução de teste

Siga estas etapas para visualizar a jornada do usuário:

1. Vá para o construtor do Canvas. Salve todas as alterações não salvas e resolva todos os erros.
2. Selecione **Test Canvas** no rodapé.
3. Selecione um usuário de teste.
4. (Opcional) Selecione um destinatário para o teste.
5. Selecione **Executar teste**.

Você pode executar uma visualização se não tiver permissão para editar um Canvas, mas essa visualização será executada com alterações não salvas, se houver alguma.

### Etapas suportadas

As etapas a seguir são suportadas:
- Mensagem 
- Caminho do público
- Divisão da decisão
- Atraso
- Caminho de ação
- Caminho do experimento
- Atualização do usuário (somente no editor da interface do usuário, ou seja, as etapas que usam o editor JSON serão ignoradas)

Se o teste se sobrepuser a um tipo de etapa que não esteja listado acima, a etapa não suportada será ignorada e o usuário do teste continuará na próxima etapa suportada.

### Detalhes da etapa da tela

Para ver mais detalhes sobre os critérios de entrada, selecione **Ver mais**. As etapas com segmentação mostrarão os critérios atendidos ou não atendidos. As mensagens também mostrarão isso para validações de entrega e elegibilidade de canal. As etapas da mensagem mostrarão quais canais foram enviados e quais não foram enviados.

### Líquido

A lógica líquida será processada durante uma execução de teste, mesmo que você não esteja enviando uma mensagem de teste real. Isso significa que a [lógica da mensagem de abortar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) e outras lógicas do Liquid são refletidas e podem afetar a jornada do usuário do Canvas.

Se a sua visualização enviar a última etapa da jornada do usuário em vez de abortar, a visualização poderá estar usando a hora atual como a hora que está sendo testada para a avaliação Liquid, e não a hora real em que o usuário estaria na etapa com base na hora de entrada do Canvas.

## Pré-visualizações para cronometragem

Para Canvases agendados, o usuário do teste entrará no próximo horário de entrada agendado. Para Canvases baseados em ações com datas de início, o usuário do teste entrará na data e hora de início. 

Embora os horários de início padrão ainda se apliquem, o horário de entrada é configurável em todas as instâncias, o que significa que você pode simular uma data no passado ou no futuro. No entanto, você não pode fazer o teste antes da data de início ou depois da data de término do Canvas.

As etapas de Mensagem e Atraso mostram o tempo em que um usuário avançaria ou receberia a mensagem sem a necessidade de reconfigurar os atrasos. Observe que, embora as etapas indiquem se o Intelligent Timing é usado, essa visualização do caminho do usuário não calcula uma estimativa para um usuário de teste.

## Quando os usuários entram e saem

Os usuários de teste entrarão na visualização mesmo que não sejam elegíveis na vida real. Se eles não forem elegíveis, você pode ver por que eles não atenderam aos critérios. Quando um usuário de teste entra na visualização, presumimos que o usuário de teste atendeu aos critérios de público-alvo e executou os critérios de acionamento da ação. Por exemplo, para um Canvas que usa eventos personalizados nos critérios de entrada, presume-se que o usuário de teste tenha realizado o evento personalizado conforme esperado nos critérios de entrada. No entanto, se o mesmo evento personalizado for usado em outra parte do Canvas (como nos critérios de saída), considere como isso pode afetar o caminho do usuário.

Eventos, acionadores de API, atributos personalizados e propriedades de entrada do Canvas são aplicados com base na entrada do Canvas. A execução do teste simula a jornada do usuário sem aplicar esses elementos para alterar o perfil real do usuário ou o fluxo do Canvas. Por exemplo, durante o teste, quando um atributo personalizado é usado como um acionador do Canvas, os critérios do acionador são aplicados à visualização do usuário **como se** ele tivesse acionado a alteração do atributo personalizado.

### Considerações

Se você testar um Action Path com ações que correspondam a critérios de saída (incluindo propriedades de eventos), os critérios de saída serão acionados e a execução do teste será encerrada. Se você testar uma etapa de Mensagem que corresponda aos critérios de saída, os critérios de saída serão acionados e a execução do teste será encerrada. 

Nesse momento, não é possível selecionar um evento ou uma propriedade específica em um caminho de ação para acionar os critérios de saída (somente o caminho como um todo). Se um usuário puder atender a vários critérios de saída, o primeiro que for processado e que ele atender será mostrado como resultado.

## Caminhos de experimentos e variantes de tela

- Para Canvases com variantes de nível superior, selecione uma variante no início do teste.
- Para Caminhos de experiência, selecione a variante pela qual o usuário progride quando o usuário de teste encontra a etapa.
- Para Caminhos de Experiência que usam Caminho Personalizado ou Variante Vencedora, embora haja um período de atraso durante o qual o usuário de teste aguarda em uma etapa de Mensagem, esse atraso não é levado em consideração, pois o Braze presume que o usuário progrediu pela variante selecionada imediatamente.

## Envios de teste

Você pode optar por enviar mensagens de teste para um grupo de teste interno ou para um usuário individual à medida que a execução do teste for preenchida. Isso significa que somente as mensagens que o usuário encontrar ao longo do caminho de teste serão enviadas. Os destinatários receberão mensagens com seus atributos por padrão, mas você pode substituí-los pelos atributos do usuário de teste.

Para enviar todas as mensagens de teste em um Canvas de uma só vez, independentemente do caminho, e sem visualizar o caminho, você pode selecionar **Enviar todas as mensagens de teste** na guia **Envios de teste**.

## Capacidade de resposta

As etapas do Canvas são sensíveis ao tempo ao visualizar os caminhos do usuário. As atualizações feitas por meio da etapa de atualização do usuário são refletidas nas etapas subsequentes do fluxo, mas não são aplicadas ao perfil do usuário real. Os efeitos de um usuário que insere uma variante são refletidos em etapas futuras em uma visualização.

Da mesma forma, os filtros reconhecerão as ações que ocorreram como resultado da interação do usuário de teste com outras etapas do Canvas. Por exemplo, esse modo de visualização reconhece que um usuário encontrou uma etapa de mensagem que foi "enviada" anteriormente no Canvas e reconhecerá que o usuário de teste "agiu" para avançar em um caminho de ação.

Consulte [os Critérios de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) para obter mais detalhes sobre o comportamento responsivo.

## Conteúdo conectado

O Connected Content será executado se estiver incluído no Canvas. Isso significa que, se você testar um Canvas que tenha chamadas de Connected Content ou blocos de conteúdo que contenham Connected Content, o Canvas poderá enviar as chamadas de Connected Content, o que modificaria os dados referenciados em outras campanhas ou Canvases.

Ao visualizar os caminhos do usuário, considere a possibilidade de remover o Connected Content que altera os perfis de usuário ou os dados referenciados em outros Canvases ou campanhas.

## Webhooks

Os webhooks serão executados quando as mensagens de teste forem enviadas, mas não durante a execução do teste. Semelhante ao Connected Content, considere a remoção de webhooks que alteram perfis de usuários ou dados referenciados em outros Canvases ou campanhas.

## Caso de uso

Nesse cenário, o Canvas é configurado para segmentar usuários que não tiveram uma sessão em um aplicativo. Essa jornada inclui uma etapa de Mensagem com um e-mail de boas-vindas, uma etapa de Atraso definida para um dia e uma etapa de Caminhos do público que se divide em dois caminhos: usuários com pelo menos uma sessão e todos os outros. Dependendo do caminho do público-alvo em que o usuário se enquadra, a etapa subsequente da Mensagem será enviada.

\![Um exemplo de um Canvas com uma etapa de Mensagem, etapa de Atraso, etapa de Caminhos do Público e duas etapas de Mensagem.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Como o nosso usuário de teste atende aos critérios de entrada do Canvas, ele pode entrar no Canvas e percorrer a jornada do usuário. No entanto, como nosso usuário de teste não abriu o aplicativo no último dia, ele continuará no caminho "Todos os outros" e receberá uma notificação por push que diz: "Última chance! Conclua sua primeira tarefa para ganhar um bônus exclusivo."

A seção "Test Results" (Resultados do teste) mostra que o usuário de teste atendeu aos critérios de entrada e fornece um resumo de sua jornada, incluindo as etapas que foram enviadas.]({% image_buster /assets/img/preview_user_path_results_example.png %})

