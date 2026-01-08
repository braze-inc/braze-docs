---
nav_title: Caminhos de ação
article_title: Caminhos de ação 
alias: /action_paths/
page_order: 0.1
page_type: reference
description: "Este artigo de referência aborda como usar o Action Paths, um componente que permite classificar os usuários com base em suas ações."
tool: Canvas
---

# Caminhos de ação 

> Os caminhos de ação no Canvas permitem classificar os usuários com base em suas ações. 

Uma etapa do Action Paths em uma jornada do usuário do Canvas.]({% image_buster /assets/img/canvas_actionpath.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Usando os Caminhos de Ação, você pode:

* Personalize os caminhos do usuário com base em uma ação específica, incluindo eventos de envolvimento do usuário e eventos personalizados
* Manter os usuários por um determinado período para priorizar seu próximo caminho com base em suas ações durante esse período de avaliação

## Criação de um caminho de ação

Para criar um caminho de ação, adicione um componente ao seu Canvas. Arraste e solte o componente da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Caminhos de ação**. 

### Configurações de ação

Em **Action Settings (Configurações de ação**), defina a **Evaluation Window (Janela de avaliação)** para determinar por quanto tempo os usuários são mantidos na etapa. Por padrão, os usuários são avaliados em um dia, mas você pode ajustar essa janela em segundos, minutos, horas, dias e semanas, dependendo do seu Canvas. A janela de avaliação máxima para um caminho de ação é de 31 dias.

Nas **Configurações de ação**, você também pode ativar a ordem de classificação dos seus componentes ativando a opção **Avançar usuários com base na ordem de classificação**.

As configurações de ação têm uma janela de avaliação de 1 dia.]({% image_buster /assets/img/actionpath_settings.png %})

Por padrão, **a classificação** está desativada. Quando um usuário entra no caminho de ação e executa o evento de acionamento associado a qualquer grupo de ação, ele avança imediatamente pelo grupo de ação relevante. Se um usuário não realizar um evento de acionamento, ele avançará pelo grupo padrão **Everyone Else** no final do período de avaliação.

Quando **Advanced users based on ranked order** está ativado, isso significa que **a classificação** está ativada. Portanto, todos os usuários serão mantidos até o final da janela de avaliação. No final do período de avaliação, os usuários avançarão pelo grupo de ação de prioridade mais alta para o qual estiverem qualificados no final da janela de avaliação. Os usuários que não executarem nenhuma das ações durante a janela de avaliação avançarão pelo grupo padrão **Everyone Else**.

#### Mensagens no aplicativo

Observe que, quando o acionador do grupo de ações estiver iniciando uma sessão e a próxima etapa for uma mensagem in-app, o usuário precisará executar dois inícios de sessão para receber a mensagem in-app. A primeira sessão atribui o usuário ao grupo de ação dentro do caminho de ação, e a segunda sessão aciona a mensagem in-app.

#### Exemplo de status de classificação

Digamos que você tenha um caminho de ação com um período de avaliação de um dia com dois grupos de ação: Grupo 1 e Grupo 2. O Grupo 1 tem um evento de acionamento "Iniciar sessão" e o Grupo 2 tem "Fazer compra". Se **a classificação** estiver ativada, todos os usuários no caminho da ação serão "retidos" por um dia. No final do dia, se um usuário tiver iniciado uma sessão e feito uma compra, ele avançará para o caminho de classificação mais alto. Nesse caso, o usuário avançaria para o Grupo 1. 

No exemplo anterior, se **a classificação** estiver desativada e quando um usuário realizar um dos eventos de acionamento ("Iniciar sessão" ou "Fazer compra"), esse usuário será avançado no grupo de ação relevante com base na ação de acionamento.

Observe que as propriedades de entrada do Canvas são diferentes das propriedades do evento. As propriedades de entrada do Canvas são propriedades do evento que acionou o Canvas. Essas propriedades só podem ser usadas na primeira etapa completa de um Canvas ao usar o fluxo de trabalho original do Canvas. Ao usar o Canvas, as propriedades de entrada persistentes são ativadas e permitem que as propriedades de entrada sejam reutilizadas em todo o Canvas. Por outro lado, as propriedades de evento se originam de um evento ou ação que ocorre à medida que o usuário passa pelo seu fluxo de trabalho.

### Grupos de ação

Adicione um acionador ou vários acionadores para definir seus grupos de ações. Aqui, você pode selecionar um intervalo de acionadores, como se os usuários:

- Fazer uma compra
- Iniciar uma sessão
- Realizar um [evento personalizado]({{site.baseurl}}/user_guide/data/custom_data/custom_events/)
- Realizar um evento de conversão
- Adicionar um endereço de e-mail
- Alterar um valor de atributo personalizado (incluindo matrizes, mas não atributos personalizados aninhados). Isso inclui adicionar um novo atributo com um valor a um perfil de usuário pela primeira vez (quando o atributo não estava presente anteriormente).
- Atualizar o status da assinatura ou o status do grupo de assinatura
- Interagir com uma campanha ou Content Card
- Insira um local
- Acionar uma geocerca
- Enviar uma mensagem de entrada de SMS ou WhatsApp

Um grupo de ação chamado "Grupo 1" para usuários que fazem qualquer compra.]({% image_buster /assets/img/actionpath_group.png %})

Em cada configuração de grupo de ação, você também tem a opção de marcar a caixa de seleção **Quero que esse grupo saia do Canvas**, o que significa que os usuários desse grupo sairão do Canvas no final do período de avaliação.

### Telas com reelegibilidade

Se os usuários entrarem em um caminho de ação várias vezes e tiverem várias entradas no caminho de ação ao mesmo tempo, o comportamento esperado varia de acordo com o status **da classificação**.

| Status da classificação | Comportamento do caminho de ação |
|---|--------------|
| **Desligado** | Quando uma ação relevante for executada, o Braze desduplicará as entradas e avançará imediatamente a entrada mais antiga pelo grupo de ações relevantes. <br><br/> Quando uma ação relevante não for executada, todas as entradas avançarão no final da janela de avaliação relevante. Não haverá desduplicação. |
| **Em** | Todas as inscrições avançarão no final da janela de avaliação relevante. Não haverá desduplicação. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Observe que as classificações não são [editáveis após o lançamento]({{site.baseurl}}/post-launch_edits/).


