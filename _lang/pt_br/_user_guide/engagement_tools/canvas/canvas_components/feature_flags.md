---
nav_title: Bandeiras de recursos
article_title: Sinalizadores de recursos
page_order: 8
page_type: reference
description: "Este artigo de referência aborda como os sinalizadores de recursos podem ser usados no Canvas."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/engagement_tools/canvas/canvas_components/feature_flags/#creating-a-feature-flag'
---

# Bandeiras de recursos

> Os sinalizadores de recursos permitem que você experimente e confirme suas hipóteses sobre novos recursos. Os profissionais de marketing podem usar sinalizadores de recursos para segmentar seu público no [Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) e acompanhar o impacto da implementação de recursos nas conversões. Além disso, [os caminhos de experiência]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) permitem otimizar essas conversões testando diferentes mensagens ou caminhos entre si e determinando qual é o mais eficaz. Use o Caminho Vencedor à medida que você implementa progressivamente seu recurso para um público mais amplo.

Procurando mais informações sobre sinalizadores de recursos e como eles podem ser usados no Braze? Confira nossos artigos dedicados aos [sinalizadores de recursos]({{site.baseurl}}/developer_guide/feature_flags/).

## Criação de um sinalizador de recurso

\![Um exemplo de etapa do sinalizador de recurso para o recurso Botão de bate-papo ao vivo.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Para criar um componente Feature Flag, primeiro adicione uma etapa ao seu Canvas. Arraste e solte o componente da barra lateral ou clique no botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Feature Flag**. Em seguida, selecione o sinalizador de recurso no menu suspenso, que contém todos os sinalizadores de recurso que não estão arquivados.

## Como esta etapa funciona

Quando um Canvas é interrompido, arquivado ou uma etapa é removida, qualquer usuário que tenha passado por essa etapa não receberá mais o sinalizador de recurso da etapa e suas propriedades. O usuário ainda estará sujeito à porcentagem de distribuição padrão e à segmentação de público-alvo para esse sinalizador de recurso e quaisquer outros Canvases que ainda possam estar ativos.

As propriedades em uma etapa do Canvas podem ser alteradas após o lançamento e mesmo depois que o usuário passar pela etapa. Os usuários sempre receberão uma versão dinâmica e em tempo real do sinalizador de recurso, em vez da versão antiga, salva anteriormente.

## Sobregravação de propriedades

Ao criar um sinalizador de recurso, você especifica as propriedades padrão. Ao configurar uma etapa do Canvas do sinalizador de recurso, você pode manter os valores padrão ou substituir os valores para os usuários que entrarem nessa etapa.

\![Um sinalizador de recurso "Centro de preferências" com "String" como propriedade, "url" como chave de propriedade e um valor.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Acesse **Messaging** > **Feature Flags** ( **Mensagens** > **Sinalizadores de recursos** ) para editar, adicionar ou remover propriedades adicionais.

## Diferenças de tela e implementação

A tela e a rolagem de um sinalizador de recurso (arrastar o controle deslizante) podem funcionar independentemente uma da outra. Uma advertência importante é que a entrada em uma etapa do Canvas substituirá qualquer configuração de distribuição padrão. Isso significa que, se um usuário não se qualificar para um sinalizador de recurso, uma etapa do Canvas poderá ativar o recurso para esse usuário.

Da mesma forma, se um usuário se qualificar para a implementação de um sinalizador de recurso com determinadas propriedades, se ele também entrar na etapa do Canvas, receberá todos os valores substituídos dessa etapa do Canvas.

