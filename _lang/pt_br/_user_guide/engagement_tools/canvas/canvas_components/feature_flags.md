---
nav_title: Feature Flags
article_title: Feature Flags
page_order: 8
page_type: reference
description: "Este artigo de referência aborda como os sinalizadores de recursos podem ser usados no Canva."
tool: Canvas
local_redirect:
  create-a-feature-flag: '/docs/user_guide/engagement_tools/canvas/canvas_components/feature_flags/#creating-a-feature-flag'
---

# Feature Flag

> Os Feature Flags permitem que você experimente e confirme suas hipóteses sobre novos recursos. Os profissionais de marketing podem usar sinalizadores de recursos para segmentar seu público no [Canva]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/create_a_canvas/) e rastrear o impacto da implementação de recursos nas conversões. Além disso, [os caminhos experimentais]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step#experiment-paths) permitem que você otimize essas conversões testando diferentes mensagens ou jornadas umas contra as outras e determinando qual é a mais eficaz. Use a Jornada Vencedora ao implementar progressivamente seu recurso para um público mais amplo.

Está procurando mais informações sobre os feature flags e como eles podem ser usados na Braze? Confira nossos artigos dedicados sobre [Feature Flag]({{site.baseurl}}/developer_guide/feature_flags/).

## Criação de um Feature Flag

![Um exemplo de etapa do Feature Flag para o recurso Botão de bate-papo ao vivo.]({% image_buster /assets/img/feature_flags/feature_flag_canvas_step.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Para criar um componente Feature Flag, primeiro adicione uma etapa do canva. Arraste e solte o componente da barra lateral ou clique no botão de adição <i class="fas fa-plus-circle"></i> na parte inferior de uma etapa e selecione **Feature Flag**. Em seguida, selecione o sinalizador de recurso no menu suspenso, que contém todos os sinalizadores de recurso que não estão arquivados.

## Como esta etapa funciona

Quando um Canva é interrompido, arquivado ou uma etapa é removida, qualquer usuário que tenha passado por essa etapa não receberá mais o sinalizador de recurso da etapa e suas propriedades. O usuário ainda estará sujeito à porcentagem de distribuição padrão e à segmentação de público para essa bandeira de recurso e quaisquer outras Canvas que ainda possam estar ativas.

As propriedades em uma etapa do Canva podem ser alteradas após o lançamento e mesmo depois que o usuário passar pela etapa. Os usuários sempre receberão uma versão dinâmica e em tempo real do sinalizador de recurso, em vez da versão antiga, salva anteriormente.

## Sobregravação de propriedades

Ao criar um sinalizador de recurso, você especifica as propriedades padrão. Ao configurar uma etapa do Canva do sinalizador de recurso, é possível manter os valores padrão ou substituir os valores para os usuários que entrarem nessa etapa.

![Um sinalizador de recurso "Central de Preferências" com "String" como a propriedade, "url" como a chave da propriedade e um valor.]({% image_buster /assets/img/feature_flags/feature_flags_canvas_details.png %}){: style="max-width:90%"}

Acesse **Envio de mensagens** > **Feature Flags** para editar, adicionar ou remover propriedades adicionais.

## Diferenças de canvas e implementação

O canva e a rolagem do Feature Flag (arrastar o controle deslizante) podem funcionar independentemente uma da outra. Uma advertência importante é que a entrada em uma etapa do Canva substituirá qualquer configuração de distribuição padrão. Isso significa que, se um usuário não se qualificar para um sinalizador de recurso, uma etapa do Canva poderá ativar o recurso para esse usuário.

Da mesma forma, se um usuário se qualificar para a implementação de um sinalizador de recurso com determinadas propriedades, se ele também entrar na etapa do Canva, receberá todos os valores substituídos dessa etapa do Canvas.

