---
nav_title: Componentes de tela
article_title: Componentes do Canvas
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Componentes do Canvas"
guide_top_text: "Aprimore sua jornada no Canvas com os componentes do Canvas. Os componentes do Canvas podem ser usados para simplificar o processo de determinação da eficácia do seu Canvas, substituindo etapas completas excessivas por apenas uma. Os componentes no Canvas referem-se à jornada personalizada do usuário nas ramificações do Canvas."

page_type: landing
description: "Esta página de destino contém artigos sobre componentes do Canvas que o ajudarão a criar Canvases mais avançados. Alguns desses componentes incluem a etapa de mensagem, a etapa de atraso, a etapa de divisão de decisão e outros."
tool: Canvas

guide_featured_title: "Artigos de seção"
guide_featured_list:
  - name: Etapa da mensagem
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Etapa de atraso
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Etapa de divisão da decisão
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Etapa dos caminhos do público
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: Caminhos de ação Etapa  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: Etapa dos caminhos de experimento
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: Etapa de atualização do usuário
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Sinalizadores de recursos no Canvas
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Sincronização de público-alvo do Canvas
    link: /docs/partners/canvas_audience_sync/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## Sobre os componentes do Canvas

Com os componentes do Canvas, é possível desbloquear novas jornadas de usuário para melhorar o processo e aumentar a eficácia do alcance do público-alvo.

### Personalização das jornadas do usuário

Exemplo de uma jornada do usuário do Canvas com uma etapa de divisão de decisão seguida por etapas de atraso e etapas de mensagem.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Use [os caminhos de ação]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths) para dividir a jornada do usuário com base em ações e eventos de envolvimento, como a realização de uma compra. Se quiser filtrar e segmentar seus públicos, [os caminhos do público]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths) ajudam a simplificar a segmentação de usuários, enviando-os por diferentes caminhos do Canvas com base nos critérios do público.

Os componentes de [divisão de decisão]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split) usam uma lógica simples de "sim ou não" para criar dois caminhos mutuamente exclusivos para as jornadas do usuário, com base em uma ação ou em um atributo do usuário. Isso pode ajudar a identificar e direcionar seus grupos de usuários.

Os componentes de [atraso]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step) permitem que você atrase uma única etapa em seu Canvas. Essa etapa autônoma de atraso no Canvas é melhor usada para comunicar mensagens aos usuários em um horário específico. Além disso, os componentes de Atraso também podem aumentar o alcance de seu público-alvo, permitindo mais tempo para que ele atenda aos critérios do componente.

### Testes

Ao criar suas jornadas de usuário, você também pode testar o caminho mais eficaz do Canvas. Com o [Experiment Paths]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step), você pode testar vários caminhos do Canvas em qualquer etapa. Você também pode usar as conexões entre as etapas como uma visualização de alto nível. As conexões em laranja indicam que a etapa anterior fará com que os usuários avancem imediatamente para a próxima etapa.

### Integração

Deseja sincronizar com os dados de usuário primários da sua marca? Aproveite as opções de sincronização de público-alvo disponíveis para o [Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync/) e [o Google]({{site.baseurl}}/partners/canvas_audience_sync/google_audience_sync/).

