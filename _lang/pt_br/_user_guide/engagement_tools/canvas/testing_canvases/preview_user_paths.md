---
nav_title: Prévia das jornadas do usuário
article_title: Prévia das jornadas do usuário
page_order: 0.3
alias: /preview_user_paths/
description: "Esta página aborda como é possível fazer a prévia das jornadas do usuário no Canva."
Tool:
  - Canvas
---

# Prévia das jornadas do usuário nos canvas

> Experimente a jornada dos canvas que você criou para seus usuários. Isso inclui a prévia do tempo e das mensagens que eles receberão. Essas execuções de teste funcionam como garantia de qualidade de que suas mensagens são enviadas para o público certo, tudo isso antes de enviar sua tela.

## Criação de uma execução de teste

Siga estas etapas para fazer uma prévia da jornada do usuário:

1. Acesse o construtor do canva. Salve todas as alterações não salvas e resolva todos os erros.
2. Selecione **Test Canva** no rodapé.
3. Selecione um usuário teste.
4. (Opcional) Selecione um destinatário para o teste.
5. Selecione **Executar teste**.

Você pode executar uma prévia se não tiver permissão para editar um Canva, mas essa prévia será executada com alterações não salvas, se houver alguma.

### Etapas aceitas

As etapas a seguir são suportadas:
- Mensagem 
- Jornada do público
- Divisão de decisão
- Postergação
- Jornadas de ação
- Jornada experimental
- Atualização do usuário (somente no editor da interface do usuário, ou seja, as etapas que usam o editor JSON serão ignoradas)

Se o teste se sobrepuser a um tipo de etapa que não esteja listado acima, a etapa não suportada será ignorada e o usuário do teste continuará na próxima etapa suportada.

### Detalhes da etapa do canva

Para ver mais detalhes sobre os critérios de entrada, selecione **Ver mais**. As etapas com segmentação mostrarão os critérios atendidos ou não atendidos. As mensagens também mostrarão isso para validações de entrega e elegibilidade do canal. As etapas das mensagens mostrarão quais canais foram enviados e quais não foram enviados.

### Liquid

A lógica Liquid será processada durante uma execução de teste, mesmo que você não esteja enviando uma mensagem de teste real. Isso significa que a [lógica da mensagem de abortar]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) e outras lógicas do Liquid são refletidas e podem afetar a jornada do usuário do Canva.

Se a sua prévia enviar a última etapa da jornada do usuário em vez de abortar, a prévia pode estar usando a hora atual como a hora que está sendo testada para a avaliação do Liquid, e não a hora real em que o usuário estaria na etapa com base na hora de entrada do Canvas.

## Prévias para cronometragem

Para as telas programadas, o usuário teste entrará no próximo horário de entrada programado. Para Canvas baseados em ações com datas de início, o usuário teste entrará na data e hora de início. 

Embora os horários de início padrão ainda se apliquem, o horário de entrada é configurável em todas as instâncias, o que significa que você pode simular uma data no passado ou no futuro. No entanto, você não pode fazer o teste antes da data de início ou depois da data de término do canva.

As etapas de mensagem e atraso mostram o tempo em que um usuário avançaria ou receberia a mensagem sem a necessidade de reconfigurar as postergações. Observe que, embora as etapas indiquem se o Intelligent Timing é usado, essa prévia da jornada do usuário não calcula uma estimativa para um usuário teste.

## Quando os usuários entram e saem

Os usuários de teste entrarão na prévia mesmo que não sejam elegíveis na vida real. Se eles não forem elegíveis, você poderá ver por que não atenderam aos critérios. Quando um usuário de teste entra na prévia, presumimos que o usuário de teste atendeu aos critérios de público-alvo e executou os critérios de ação-gatilho. Por exemplo, para um Canva que usa eventos personalizados nos critérios de entrada, presume-se que o usuário teste tenha realizado o evento personalizado conforme esperado nos critérios de entrada. No entanto, se o mesmo evento personalizado for usado em outra parte da tela (como nos critérios de saída), considere como isso pode afetar a jornada do usuário.

Eventos, disparos de API, atributos personalizados e propriedades de entrada do Canvas são aplicados com base na entrada do Canvas. A execução do teste simula a jornada do usuário sem aplicar esses elementos para alterar o perfil real do usuário ou o fluxo do Canvas Flow. Por exemplo, durante os testes, quando um atributo personalizado é usado como um disparador do Canvas, os critérios do disparador são aplicados à prévia do usuário **como se** ele tivesse disparado a alteração do atributo personalizado.

### Considerações

Se você testar um caminho de ação com ações que correspondam a critérios de saída (incluindo propriedades de eventos), os critérios de saída serão disparados e a execução do teste será encerrada. Se você testar uma etapa de Mensagem que corresponda aos critérios de saída, os critérios de saída serão disparados e a execução do teste será encerrada. 

Nesse momento, não é possível selecionar um evento ou uma propriedade específica em uma jornada de ação para disparar os critérios de saída (somente a jornada como um todo). Se um usuário puder atender a vários critérios de saída, o primeiro que for processado e que ele atender será mostrado como resultado.

## Caminhos de experimento e variantes do Canva

- Para Canvas com variantes de nível superior, selecione uma variante no início do teste.
- Para as jornadas experimentais, selecione a variante pela qual o usuário progride quando o usuário teste encontra a etapa.
- Para os Caminhos de Experiência que usam Caminho Personalizado ou Variante Vencedora, embora haja um período de atraso durante o qual o usuário teste espera em uma etapa de Mensagem, essa postergação não é levada em consideração, pois o Braze presume que o usuário progrediu pela variante selecionada imediatamente.

## Envios de teste

É possível fazer a aceitação do envio de mensagens de teste para um grupo de teste interno ou para um usuário individual à medida que a execução do teste for preenchida. Isso significa que apenas as mensagens que o usuário encontrar ao longo da jornada de teste serão enviadas. Os destinatários receberão mensagens com suas atribuições por padrão, mas você pode substituí-las pelas atribuições do usuário teste.

Para enviar todas as mensagens de teste em uma tela de uma só vez, independentemente da jornada, e sem prévia da jornada, você pode selecionar **Enviar todas as mensagens de teste** na guia **Envios de teste**.

## Capacidade de resposta

As etapas do canva são sensíveis ao tempo durante a prévia das jornadas do usuário. As atualizações feitas por meio da etapa de atualização do usuário são refletidas nas etapas subsequentes do fluxo, mas não são aplicadas ao perfil do usuário real. Os efeitos da inserção de uma variante por um usuário são refletidos nas etapas futuras de uma prévia.

Da mesma forma, os filtros reconhecerão as ações que ocorreram como resultado da interação do usuário teste com outras etapas do Canva. Por exemplo, esse modo de prévia reconhece que um usuário encontrou uma etapa de mensagem que foi "enviada" anteriormente no Canvas e reconhecerá que o usuário teste "agiu" para avançar em uma jornada de ação.

Consulte [os Critérios de saída]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exit_criteria) para obter mais detalhes sobre o comportamento responsivo.

## Conteúdo conectado

O Connected Content será executado se estiver incluído no Canva. Isso significa que, se você testar um Canvas que tenha chamadas de Connected Content ou blocos de conteúdo que contenham Connected Content, o Canvas poderá enviar as chamadas de Connected Content, o que modificaria os dados referenciados em outras campanhas ou Canvas.

Ao fazer a prévia das jornadas do usuário, considere a remoção do Conteúdo conectado que altera os perfis de usuário ou os dados referenciados em outras Canvas ou campanhas.

## Webhooks

Os webhooks serão executados quando as mensagens de teste forem enviadas, mas não durante a execução do teste. Semelhante ao Connected Content, considere a remoção de webhooks que alteram perfis de usuários ou dados de usuários referenciados em outros Canvas ou campanhas.

## Caso de uso

Nesse cenário, o Canva é configurado para direcionamento a usuários que não tiveram uma sessão em um app. Essa jornada inclui uma etapa de Mensagem com um e-mail de boas-vindas, uma etapa de Postergação definida para um dia e uma etapa de Caminhos do público que se divide em duas jornadas: usuários com pelo menos uma sessão e todos os outros. Dependendo da jornada do público em que o usuário se enquadra, a etapa subsequente da mensagem será enviada.

![Um exemplo de um Canvas com uma etapa de mensagem, etapa de postergação, etapa de jornadas do público e duas etapas de mensagens.]({% image_buster /assets/img/preview_user_path_example.png %}){:style="max-width:70%"}

Como o nosso usuário teste atende aos critérios de entrada do Canvas, ele pode entrar no Canvas e percorrer a jornada do usuário. No entanto, como nosso usuário teste não abriu o app no último dia, ele continuará na jornada "Todos os outros" e receberá uma notificação por push que diz "Última chance! Conclua sua primeira tarefa para ganhar um bônus exclusivo."

![A seção "Test Results" (Resultados do teste) que mostra que o usuário teste atendeu aos critérios de entrada e fornece um resumo de sua jornada, incluindo quais etapas foram enviadas.]({% image_buster /assets/img/preview_user_path_results_example.png %})

