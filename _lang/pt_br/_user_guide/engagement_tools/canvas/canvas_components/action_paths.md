---
nav_title: Jornadas de ação 
article_title: Jornadas de ação 
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "Este artigo de referência cobre como usar jornadas de ação, um componente que permite classificar os usuários com base em suas ações."
tool: Canvas
---

# Jornadas de ação 

> Jornadas de ação no canva permitem que você classifique seus usuários com base em suas ações. 

Usando jornadas de ação, você pode:

![][1]{: style="float:right;max-width:40%;margin-left:15px;"}

* Personalize os caminhos do usuário com base em uma ação específica, incluindo eventos de engajamento do usuário e eventos personalizados
* Mantenha os usuários por uma determinada duração para priorizar sua próxima jornada com base em suas ações durante este período de avaliação

## Crie uma jornada de ação

Para criar uma jornada de ação, adicione um componente ao seu canva. Arraste e solte o componente da barra lateral ou selecione o <i class="fas fa-plus-circle"></i> botão de mais na parte inferior de uma etapa e selecione **jornadas de ação**. 

### Configurações de ação

Nas **Configurações de Ação**, defina a **Janela de Avaliação** para determinar quanto tempo os usuários permanecem na etapa. Por padrão, os usuários são avaliados dentro de um dia, mas você pode ajustar essa janela por segundos, minutos, horas, dias e semanas, dependendo do seu canva. A janela máxima de avaliação para uma jornada de ação é de 31 dias.

Dentro das **Configurações de Ação**, você também pode ativar a ordem classificada para seus componentes ativando a alternância **Avançar usuários com base na ordem classificada**.

![][4]

Por padrão, **Ranking** está desativado. Quando um usuário entra na jornada de ação e realiza o evento de gatilho anexado a qualquer grupo de ação, ele avançará imediatamente pelo grupo de ação relevante. Se um usuário não realizar um evento de gatilho, ele avançará pelo grupo padrão **Todos os Outros** no final do período de avaliação.

Quando **usuários avançados com base na ordem de classificação** está ativado, isso significa que **classificação** está ativada. Então, todos os usuários serão retidos até o final da janela de avaliação. No final do período de avaliação, os usuários avançarão pelo grupo de ação de maior prioridade para o qual são elegíveis no final da janela de avaliação. Usuários que não realizarem nenhuma das ações durante a janela de avaliação avançarão pelo grupo padrão **Todos os Outros**.

#### Mensagem no app

Nota que quando o disparar do grupo de ação está iniciando uma sessão e a próxima etapa é uma mensagem no app, o usuário precisará realizar dois inícios de sessão para receber a mensagem no app. A primeira sessão atribui o usuário ao grupo de ação dentro da jornada de ação, e a segunda sessão aciona a mensagem no app.

#### Exemplo de status de classificação

Digamos que você tenha uma jornada de ação com um período de avaliação de um dia com dois grupos de ação: Grupo 1 e Grupo 2. O Grupo 1 tem um evento de gatilho "Iniciar Sessão", e o Grupo 2 tem "Fazer Compra". Se **Ranking** estiver ativado, todos os usuários na jornada de ação serão "retidos" por um dia. No final do dia, se um usuário iniciou uma sessão e fez uma compra, então ele avança para a jornada de maior classificação. Neste caso, o usuário avançaria para o Grupo 1. 

No exemplo anterior, se **Ranking** estiver desativado e quando um usuário realizar um dos eventos de disparo ("Iniciar Sessão" ou "Fazer Compra"), esse usuário é avançado no grupo de ação relevante com base na ação-gatilho.

Nota que as propriedades de entrada do canva diferem das propriedades do evento. As propriedades de entrada da canva são propriedades do evento que acionou a canva. Essas propriedades só podem ser usadas na primeira etapa completa de um canva ao usar o fluxo de trabalho original do canva. Ao usar o Canvas Flow, as propriedades de entrada persistentes são ativadas e permitem que as propriedades de entrada sejam reutilizadas em todo o canva. Por outro lado, as propriedades do evento se originam de um evento ou ação que ocorre à medida que o usuário passa pelo seu fluxo de trabalho.

### Grupos de ação

Adicione um disparar ou vários disparar para definir seus grupos de ação. Aqui, você pode selecionar uma variedade de gatilhos, como se os usuários:

- Fazer uma compra
- Iniciar uma sessão
- Realizar um [evento personalizado][2]
- Realizar um evento de conversão
- Adicione um endereço de e-mail
- Alterar o valor de um atributo personalizado
- Atualize o status da inscrição ou o status do grupo de inscrições
- Interaja com uma campanha ou cartão de conteúdo
- Insira um local
- Disparar um geofence
- Enviar uma mensagem de entrada por SMS ou WhatsApp

![][3]

Dentro de cada configuração de grupo de ações, você também tem a opção de selecionar a caixa de seleção **Quero que este grupo saia da canva**, o que significa que os usuários deste grupo sairão da canva no final do período de avaliação.

### canvas com re-eligibilidade

Se os usuários entrarem em uma jornada de ação várias vezes e tiverem várias entradas na jornada de ação ao mesmo tempo, o comportamento esperado varia dependendo do status de **Ranking**. 

| Status de Classificação | Comportamento da jornada de ação |
|---|--------------|
| **Off** | Quando uma ação relevante é realizada, a Braze removerá entradas duplicadas e avançará imediatamente a entrada mais antiga através do grupo de ação relevante. <br><br/> Quando uma ação relevante não é realizada, todas as entradas avançarão no final da janela de avaliação relevante. Nenhuma desduplicação ocorrerá. |
| **On** | Todas as entradas avançarão no final da janela de avaliação relevante. Nenhuma desduplicação ocorrerá. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Nota que as classificações não são [editáveis após o lançamento]({{site.baseurl}}/post-launch_edits/).


[1]: {% image_buster /assets/img/canvas_actionpath.png %}
[2]: {{site.baseurl}}/user_guide/data_e_analytics/custom_data/custom_events
[3]: {% image_buster /assets/img/actionpath_group.png %}
[4]: {% image_buster /assets/img/actionpath_settings.png %} 
