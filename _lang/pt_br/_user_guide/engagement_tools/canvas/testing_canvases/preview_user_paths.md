---
nav_title: Prévia das jornadas do usuário
article_title: Prévia das jornadas do usuário
page_order: 0.3
alias: /preview_user_paths/
description: "Esta página aborda como é possível fazer a prévia das jornadas do usuário no canva."
Tool:
  - Canvas
---

# Prévia das jornadas do usuário nos canvas

> Experimente a jornada dos canvas que você criou para seus usuários. Isso inclui visualizar o tempo e as mensagens que seus usuários recebem. Essas execuções de teste funcionam como garantia de qualidade de que suas mensagens são enviadas para o público certo, tudo isso antes de enviar seu canva.

## Criação de uma execução de teste

Siga estas etapas para fazer uma prévia da jornada do usuário:

1. Acesse o construtor do canva. Salve todas as alterações não salvas e resolva todos os erros.
2. Selecione **Test Canvas** no rodapé.
3. Selecione um usuário teste.
4. (Opcional) Selecione um destinatário para o teste.
5. Selecione **Run Test**.

Você pode executar uma prévia se não tiver permissão para editar um canva, mas essa prévia é executada com alterações não salvas, se houver.

### Etapas aceitas

As etapas a seguir são aceitas:
- Mensagem 
- Jornada do público
- Divisão de decisão
- Postergação
- Jornada de ação
- Jornada experimental
- Atualização do usuário (apenas no editor de UI, o que significa que etapas usando o editor JSON são puladas)

Se o teste se sobrepuser a um tipo de etapa que não está listado acima, a etapa não aceita é pulada, e o usuário teste continua para a próxima etapa aceita.

### Detalhes da etapa do canva

Para ver mais detalhes sobre os critérios de entrada, selecione **See more**. Etapas com segmentação mostram os critérios atendidos ou não atendidos. As mensagens também mostram isso para validações de entrega e elegibilidade de canal. As etapas de mensagem mostram quais canais foram enviados e quais não foram enviados.

### Liquid

A Braze processa a lógica Liquid durante a execução do teste, mesmo que você não esteja enviando uma mensagem de teste real. Isso significa que a [lógica de abortar mensagem]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) e outras lógicas do Liquid são refletidas e podem afetar a jornada do usuário no canva.

Se a sua prévia enviar a última etapa da jornada do usuário em vez de abortar, a prévia pode estar usando a hora atual como a hora que está sendo testada para a avaliação do Liquid, e não a hora real em que o usuário estaria na etapa com base na hora de entrada do canva.

## Prévias para cronometragem

Para canvas agendados, o usuário teste entra no próximo horário de entrada agendado. Para canvas baseados em ação com datas de início, o usuário teste entra na data e hora de início. 

Embora os horários de início padrão ainda se apliquem, o horário de entrada é configurável em todas as instâncias, o que significa que você pode simular uma data no passado ou no futuro. No entanto, você não pode testar antes da data de início ou após a data de término do canva.

As etapas de mensagem e postergação mostram o tempo em que um usuário avançaria ou receberia a mensagem sem a necessidade de reconfigurar as postergações. Observe que, embora as etapas indiquem se o Intelligent Timing está sendo usado, esta prévia da jornada do usuário não calcula uma estimativa para um usuário teste.

Para canvas com um gatilho de ação como "mudança no valor do atributo personalizado", a Braze tenta simular a mudança definindo temporariamente o atributo do usuário no gatilho como vazio **apenas para a execução do teste do canva** (isso não afeta o perfil do usuário). Isso serve para testar se o atributo muda em relação ao seu valor atual.

## Quando os usuários entram e saem

Usuários teste entram na prévia mesmo que não sejam elegíveis na vida real. Se eles não forem elegíveis, você poderá ver por que não atenderam aos critérios. Quando um usuário teste entra na prévia, presumimos que o usuário teste atendeu aos critérios de público-alvo e executou os critérios de gatilho de ação. Por exemplo, para um canva que usa eventos personalizados nos critérios de entrada, presume-se que o usuário teste tenha realizado o evento personalizado conforme esperado nos critérios de entrada. No entanto, se o mesmo evento personalizado for usado em outra parte do canva (como nos critérios de saída), considere como isso pode afetar a jornada do usuário.

Eventos, gatilhos de API, atributos personalizados e propriedades de entrada do canva que se presume permitirem que um usuário teste entre no canva não são atualizados no perfil real do usuário e não persistem além da execução do teste. Por exemplo, durante os testes, quando um atributo personalizado é usado como um gatilho do canva, os critérios do gatilho são aplicados à prévia do usuário **como se** ele tivesse disparado a alteração do atributo personalizado.

### Considerações

Se você testar uma jornada de ação com ações que correspondem a critérios de saída (incluindo propriedades de evento), os critérios de saída são acionados e a execução do teste termina. Se você testar uma etapa de mensagem que corresponde aos critérios de saída, os critérios de saída são acionados e a execução do teste termina. 

Nesse momento, não é possível selecionar um evento ou uma propriedade específica em uma jornada de ação para disparar os critérios de saída (somente a jornada como um todo). Se um usuário puder atender a vários critérios de saída, o primeiro que for processado e que ele atender será mostrado como resultado.

## Jornadas experimentais e variantes do canva

- Para canvas com variantes de nível superior, selecione uma variante no início do teste.
- Para as jornadas experimentais, selecione a variante pela qual o usuário progride quando o usuário teste encontra a etapa.
- Para as jornadas experimentais que usam Caminho Personalizado ou Variante Vencedora, embora haja um período de postergação durante o qual o usuário teste espera em uma etapa de mensagem, essa postergação não é levada em consideração, pois a Braze presume que o usuário progrediu pela variante selecionada imediatamente.

## Envios de teste

É possível optar pelo envio de mensagens de teste para um grupo de teste interno ou para um usuário individual à medida que a execução do teste for preenchida. Isso significa que apenas as mensagens que o usuário encontra ao longo da jornada de teste são enviadas. Os destinatários recebem mensagens com seus atributos por padrão, mas você pode substituí-los pelos atributos do usuário teste.

Para enviar todas as mensagens de teste em um canva de uma só vez, independentemente da jornada, e sem prévia da jornada, você pode selecionar **Send All Test Messages** na guia **Test Sends**.

## Capacidade de resposta

As etapas do canva são sensíveis ao tempo durante a prévia das jornadas do usuário. As atualizações feitas por meio da etapa de atualização do usuário são refletidas nas etapas subsequentes do fluxo, mas não são aplicadas ao perfil do usuário real. Os efeitos da entrada de um usuário em uma variante são refletidos nas etapas futuras de uma prévia.

Da mesma forma, os filtros reconhecem ações que ocorreram como resultado da interação do usuário teste com outras etapas no canva. Por exemplo, este modo de prévia reconhece que um usuário encontrou uma etapa de mensagem que foi "enviada" anteriormente no canva, e reconhece que o usuário teste "tomou uma ação" para avançar por uma jornada de ação.

Consulte [Critérios de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) para obter mais detalhes sobre o comportamento responsivo.

## Conteúdo conectado

O Conteúdo conectado é executado se estiver incluído no canva. Isso significa que, se você testar um canva que tenha chamadas de Conteúdo conectado ou blocos de conteúdo que contenham Conteúdo conectado, o canva poderá enviar as chamadas de Conteúdo conectado, o que modificaria os dados referenciados em outras campanhas ou canvas.

Ao fazer a prévia das jornadas do usuário, considere a remoção do Conteúdo conectado que altera os perfis de usuário ou os dados referenciados em outros canvas ou campanhas.

## Webhooks

Webhooks são executados quando mensagens de teste são enviadas, mas não durante a execução do teste. Semelhante ao Conteúdo conectado, considere a remoção de webhooks que alteram perfis de usuários ou dados referenciados em outros canvas ou campanhas.

## Variáveis de contexto e grupos de teste

Para uma etapa de mensagem com e-mail como canal de envio de mensagens, os grupos de teste enviam cópias seed dos e-mails quando um usuário atinge essa etapa no canva. Essas cópias seed não são enviadas como parte das jornadas do canva dos próprios destinatários do grupo de teste, então a Braze não executa [etapas de contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context) nem avalia variáveis de contexto para esses destinatários. Se o conteúdo do seu e-mail faz referência a variáveis de contexto, os destinatários do grupo de teste recebem uma cópia seed sem esses dados preenchidos. Para testar mensagens que dependem de dados de variáveis de contexto, use a prévia **Test Canvas** com envios de teste em vez de grupos de teste.

## Caso de uso

Nesse cenário, o canva é configurado para direcionamento a usuários que não tiveram uma sessão em um app. Essa jornada inclui uma etapa de mensagem com um e-mail de boas-vindas, uma etapa de postergação definida para um dia e uma etapa de jornada do público que se divide em duas jornadas: usuários com pelo menos uma sessão e todos os outros. Dependendo de qual jornada do público um usuário se encaixa, a próxima etapa de mensagem é enviada.

![Um exemplo de um canva com uma etapa de mensagem, etapa de postergação, etapa de jornada do público e duas etapas de mensagem.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Como o nosso usuário teste atende aos critérios de entrada do canva, ele pode entrar no canva e percorrer a jornada do usuário. No entanto, como nosso usuário teste não abriu o app no último dia do calendário, ele continua pela jornada "Restante do público" e recebe uma notificação por push que diz: "Última chance! Conclua sua primeira tarefa para ganhar um bônus exclusivo."

![A seção "Resultados do teste" mostra que o usuário teste atendeu aos critérios de entrada e fornece um resumo de sua jornada, incluindo quais etapas foram enviadas para ele.]({% image_buster /assets/img/preview_user_path_results_example.png %})