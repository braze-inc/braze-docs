---
nav_title: Componentes do Canva
article_title: Componentes do Canva
page_order: 2
alias: "/user_guide/engagement_tools/canvas/canvas_components/about/"
layout: dev_guide
guide_top_header: "Componentes do Canva"
guide_top_text: "Aprimore sua jornada no canva com os componentes do canva. Os componentes do Canvas podem ser usados para simplificar o processo de determinação da eficácia do seu Canva, substituindo etapas completas excessivas por apenas uma. Os componentes no Canvas referem-se à jornada personalizada do usuário nas ramificações do Canvas."

page_type: landing
description: "Esta landing page contém artigos sobre componentes do Canvas que o ajudarão a criar Canvas mais avançados. Alguns desses componentes incluem a etapa de mensagens, a etapa de postergação, a etapa de divisão de decisão, entre outros."
tool: Canvas

guide_featured_title: "Artigos de seção"
guide_featured_list:
  - name: Etapa de mensagem
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/message_step/
    image: /assets/img/braze_icons/message-square-02.svg
  - name: Etapa de postergação
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/delay_step/
    image: /assets/img/braze_icons/clock-stopwatch.svg
  - name: Etapa de divisão de decisão
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/decision_split/
    image: /assets/img/braze_icons/dataflow-04.svg
  - name: Etapa das jornadas de público
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/audience_paths/
    image: /assets/img/braze_icons/users-01.svg 
  - name: Etapa das jornadas de ação  
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/action_paths/
    image: /assets/img/braze_icons/zap.svg
  - name: Etapa de jornadas do experimento
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/experiment_step/
    image: /assets/img/braze_icons/columns-01.svg
  - name: Etapa de atualização de usuário
    link: /docs/user_guide/engagement_tools/canvas/canvas_components/user_update/
    image: /assets/img/braze_icons/user-check-01.svg
  - name: Feature Flags no canva
    link: /docs/developer_guide/feature_flags/canvas/
    image: /assets/img/braze_icons/dataflow-03.svg
  - name: Sincronização do público do Canva
    link: /docs/partners/canvas_steps/
    image: /assets/img/braze_icons/refresh-ccw-02.svg
---

## Sobre os componentes do Canva

Com os componentes do Canva, é possível desbloquear novas jornadas de usuário para melhorar seu processo e aumentar a eficácia do alcance do público.

### Personalizar as jornadas do usuário

![Exemplo de uma jornada do usuário do Canva com uma etapa de divisão de decisão seguida por etapas de postergação e etapas de mensagens.]({% image_buster /assets/img/canvas_intro/canvas_intro.gif %}){: style="float:right;max-width:55%;margin-left:15px;"}

Use [jornadas de ação][1] para dividir a jornada do usuário com base em ações e eventos de engajamento, como a realização de uma compra. Se quiser filtrar e direcionar seu público, [os Audience Paths][2] ajudam a simplificar o direcionamento de usuários, enviando-os por diferentes jornadas do público com base nos critérios do público.

Os componentes de [divisão de decisão][3] usam uma lógica simples de "sim ou não" para criar duas jornadas mutuamente exclusivas para o usuário, com base em uma ação ou atribuição do usuário. Isso pode ajudar a identificar e direcionar seus grupos de usuários.

Os componentes de [atraso][4] permitem a postergação de uma única etapa do Canva. Essa etapa autônoma de postergação no seu Canva é melhor usada para o envio de mensagens aos seus usuários em um momento específico. Além disso, os componentes de postergação também podem aumentar o alcance de seu público, permitindo mais tempo para que ele atenda aos critérios do componente.

### Testes

Ao criar as jornadas do usuário, convém testar também a jornada mais eficaz do canva. Com o [Experiment Paths][5], você pode testar vários caminhos do Canva em qualquer etapa. Você também pode usar as conexões entre as etapas como uma prévia de alto nível. As conexões em laranja indicam que a etapa anterior fará com que os usuários avancem imediatamente para a próxima etapa.

### Integração

Deseja sincronizar-se com os dados primários de usuários da sua marca? Aproveite as opções de sincronização de público disponíveis para o [Facebook][6] e [o Google][7].

[1]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/action_paths
[2]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/audience_paths
[3]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/decision_split
[4]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step
[5]: {{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/experiment_step
[6]: {{site.baseurl}}/partners/canvas_steps/facebook_audience_sync
[7]: {{site.baseurl}}/partners/canvas_steps/google_audience_sync