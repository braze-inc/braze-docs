---
nav_title: Salvando rascunhos para o Canvas
article_title: Salvando rascunhos para o Canvas
alias: "/save_as_draft/"
page_order: 1
description: "Este artigo de referência aborda como salvar um rascunho de um Canvas que já foi lançado."
page_type: reference
tool: Canvas
---

# Salvando rascunhos para o Canvas

> Ao criar e lançar Canvases, você pode editar um Canvas ativo e salvá-lo como rascunho, o que lhe permite testar suas alterações antes de outro lançamento. 

Se você tiver um Canvas ativo que exija alterações em grande escala, poderá usar esse recurso para criar, salvar e verificar a qualidade **antes** de iniciar essas alterações no Canvas ativo. 

Como em qualquer Canvas, apenas um usuário pode editar um rascunho por vez, e um Canvas só pode ter um rascunho por vez. Esses rascunhos não têm nenhuma análise porque as alterações de rascunho ainda não foram lançadas.

\![Um exemplo de rascunho de Canvas com um banner que indica ao usuário que ele está editando um rascunho de Canvas com uma opção para visualizar o Canvas ativo. O rodapé tem opções para voltar à exibição de análise, salvar como rascunho ou iniciar rascunho.]({% image_buster /assets/img_archive/canvas_draft1.png %})

## Criação de um rascunho

Para criar um rascunho:

1. Vá para um Canvas ativo.
2. Selecione o botão **Salvar como rascunho** no rodapé do Canvas. 

Observe que as edições no Canvas ativo não podem ser feitas enquanto houver um rascunho de um Canvas. Você pode atualizar o Canvas para aplicar as alterações ou descartar o rascunho.

## Referência ao rascunho ativo

Para fazer referência ao Canvas ativo, selecione **Exibir Canvas ativo** no rodapé da visualização analítica ou no cabeçalho do Canvas no rascunho. Para retornar a um Canvas ativo, selecione **Editar rascunho** na visualização de análise ou na visualização do Canvas ativo.

Você só pode fazer referência a etapas que já tenham sido iniciadas antes da criação do rascunho. Isso significa que se você criou uma etapa ou um canal **depois que** o rascunho foi criado, ele não poderá ser referenciado em seu rascunho.

{% alert note %}
Se um Bloco de Conteúdo for referenciado em um rascunho do Canvas, o Canvas será listado na contagem de inclusão do Bloco de Conteúdo. No entanto, se o Bloco de Conteúdo for referenciado em um rascunho de um Canvas **ativo**, o Canvas não será listado na contagem de inclusão do Bloco de Conteúdo.
{% endalert %}

### Priorização de mensagens no aplicativo

Para rascunhos de um Canvas ativo, a prioridade da mensagem no aplicativo dentro do construtor do Canvas será atualizada imediatamente quando um usuário alterar a prioridade. Isso significa que a prioridade de mensagens in-app no nível do Canvas é aplicada imediatamente ao Canvas ativo, mesmo quando existe um rascunho. 

No entanto, as alterações de prioridade de mensagens no aplicativo em nível de etapa são salvas como rascunho e aplicadas quando o Canvas é atualizado. Por exemplo, em uma etapa de Mensagem, o classificador de prioridades será atualizado quando um usuário iniciar o rascunho, pois as configurações da etapa se aplicam em um nível de etapa.

