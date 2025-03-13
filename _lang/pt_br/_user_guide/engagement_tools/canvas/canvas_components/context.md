---
nav\_title: Contexto article\_title: Contexto alias: /context/ page\_order: 1.5 page\_type: reference description: "Este artigo de referência aborda como criar e usar as etapas do contexto em sua ferramenta Canvas: Canva

---

# Contexto

> Use as etapas do Context para criar ou atualizar um conjunto de variáveis que representam o contexto de um usuário (ou insights sobre o comportamento desse usuário) à medida que ele se move pelo Canvas. Cada variável de contexto inclui um nome, um tipo de dados e um valor que pode incluir Liquid. Ao definir o contexto como parte da jornada do usuário, é possível fazer coisas como a postergação de mensagens ou filtrar usuários com base em variáveis de contexto.

{% alert important %} As etapas de contexto estão atualmente em acesso antecipado. Entre em contato com o gerente da sua conta Braze se estiver interessado em participar desse acesso antecipado. {% endalert %}

## Como funciona?

Cada etapa do canva é criada com um nome de variável e um tipo de dados associado, ou variáveis de contexto (anteriormente chamadas de propriedades de entrada do canvas). Essas variáveis seguirão um usuário por meio de uma tela e poderão ser acessadas usando o `contexto` Liquid.

\![Uma etapa de contexto como a primeira etapa de uma tela]\[1]{: style="float:right;max-width:40%;margin-left:15px;"}

Há duas maneiras de definir variáveis de contexto:

- **Na entrada do canva:** As variáveis de eventos ou chamadas de API que disparam a entrada de um usuário em um Canva são armazenadas como variáveis de contexto.
- **Usando uma etapa de contexto:** Você pode criar ou atualizar variáveis de contexto no editor de etapas.

## Criando uma etapa de contexto

Para criar uma etapa do Context, adicione uma etapa ao seu Canvas. Em seguida, arraste e solte o componente da barra lateral ou selecione o botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Contexto**.

### Definição de variáveis de contexto

1. Dê um nome à sua variável Context.
2. Selecione um tipo de dados.
3. Digite uma expressão Liquid ou selecione o botão **Adicionar personalização**. Isso gera um snippet Liquid para ser usado em sua expressão Liquid.
4. Selecione **Prévia** para visualizar a variável de contexto.
5. Selecione **Concluído** para salvar a etapa.

Você pode usar as variáveis de contexto em qualquer lugar onde possa usar o Liquid, como nas etapas de Mensagem e Atualização do usuário, com o botão **Adicionar personalização**.

## Tipos de variáveis de contexto

Podem ser atribuídos tipos às variáveis de contexto do canva que são criadas ou atualizadas na etapa do canva. Observe que, se a expressão Liquid em tempo de execução retornar um valor que não corresponda ao tipo, a variável de contexto não será atualizada.

Por exemplo, se o tipo de dados da variável de contexto for definido como **Date**, mas o valor não for uma data, a variável não será atualizada. Isso significa que ocorrerá o seguinte:

- O usuário avançará para a próxima etapa ou sairá do Canvas se essa for a última etapa do Canva.
- Em sua análise de dados da etapa do canva, isso será contado como *Não atualizado*.

## Uso de variáveis de contexto com etapas de postergação

É possível adicionar [opções de postergação personalizadas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/#personalized-delays) com as informações da etapa Contexto, o que significa que você pode selecionar a variável que posterga os usuários.


\[1]: {% image\_buster /assets/img/context\_step3.png %}

