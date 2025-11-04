---
nav_title: "Mensagens no aplicativo"
article_title: Mensagens no aplicativo
page_order: 2
alias: /in-app_messages/
layout: dev_guide
guide_top_header: "Mensagens no aplicativo"
guide_top_text: "As mensagens no aplicativo ajudam a levar o conteúdo ao usuário sem interromper o dia dele com uma notificação push, pois essas mensagens não são entregues fora do aplicativo do usuário e não interferem na tela inicial dele. <br><br>Mensagens in-app personalizadas e sob medida aprimoram a experiência do usuário e ajudam seu público a obter o máximo de valor do seu aplicativo. Com uma variedade de layouts e ferramentas de personalização para escolher, as mensagens in-app envolvem seus usuários mais do que nunca. Eles vêm com contexto, têm menor urgência e são entregues quando o usuário está ativo em seu aplicativo. Para ver exemplos de mensagens in-app, confira <a href='https://www.braze.com/customers'>as histórias de</a> nossos <a href='https://www.braze.com/customers'>clientes</a>."
description: "Essa página de destino é o lar de todos os assuntos relacionados à mensagem no aplicativo. Aqui, você pode encontrar artigos sobre como criar mensagens no aplicativo, o editor de arrastar e soltar, como personalizar suas mensagens, relatórios e muito mais."
channel:
  - in-app messages
search_rank: 5
guide_featured_title: "Artigos populares"
guide_featured_list:
- name: "Editor de arrastar e soltar"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Editor tradicional"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Detalhes criativos"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/
  image: /assets/img/braze_icons/brush-02.svg

guide_menu_title: "More articles"
guide_menu_list:
- name: "Testes"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/testing/
  image: /assets/img/braze_icons/beaker-02.svg
- name: "Relatórios"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/reporting/
  image: /assets/img/braze_icons/bar-chart-01.svg
- name: "Modo escuro"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/dark-mode/
  image: /assets/img/braze_icons/phone-02.svg
- name: "Prompt de classificação da App Store"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/ios_app_rating_prompt/
  image: /assets/img/braze_icons/star-01.svg
- name: "Pesquisa simples"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/traditional/templates/simple_survey/
  image: /assets/img/braze_icons/bar-chart-07.svg
- name: "Locais em mensagens"
  link: /docs/locales_in_messages/
  image: /assets/img/braze_icons/translate-01.svg
- name: "Práticas recomendadas"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/best_practices
  image: /assets/img/braze_icons/check-square-broken.svg
- name: "PERGUNTAS FREQUENTES"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/faq/
  image: /assets/img/braze_icons/annotation-question.svg
---

## [![Curso de aprendizado do Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"} Casos de uso em potencial

Com o rico nível de conteúdo oferecido pelas mensagens in-app, você pode aproveitar esse canal para uma variedade de casos de uso:

| Caso de uso | Explicação |
| --- | --- |
| Escorvamento por pressão | Execute uma campanha [de preparação de push]({{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/) usando uma mensagem avançada no aplicativo para mostrar aos seus clientes o benefício de optar pelo push para seu aplicativo ou site e apresente a eles um prompt para conceder permissão de push.
| Vendas e promoções | Use mensagens modais no aplicativo para cumprimentar os clientes com mídia visualmente atraente contendo códigos de promoção ou ofertas estáticas. Incentive-os a fazer compras ou conversões quando, de outra forma, não o fariam. |
| Incentivar a adoção de recursos | Incentive os clientes a usar outras partes do seu aplicativo ou a aproveitar um serviço. |
| Campanhas altamente personalizadas | Coloque mensagens no aplicativo como a primeira coisa que seus clientes veem quando entram em seu aplicativo ou site. Acrescente alguns recursos de personalização do Braze, como o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/), para motivar os usuários a agir e, assim, tornar o seu alcance mais eficaz.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Outros casos de uso a serem considerados incluem o seguinte:

- Novos recursos do aplicativo
- Gerenciamento de aplicativos
- Comentários
- Upgrades ou atualizações de aplicativos
- Brindes e sorteios

## Tipos de mensagens padrão

As guias a seguir mostram como é para os seus usuários abrir um dos nossos tipos de mensagem in-app padrão - mensagens in-app deslizantes, modais e de tela cheia.

{% tabs %}
{% tab Slideup %}

As mensagens deslizantes geralmente aparecem na parte superior e inferior da tela do aplicativo (você pode definir isso ao criar a mensagem). Eles são ótimos para alertar seus usuários sobre novos termos de serviço, cookies e outros trechos de informações.

Mensagem de slideup no aplicativo que aparece na parte inferior da tela do aplicativo. O slide-up inclui uma imagem de ícone e uma breve mensagem.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

Os modais aparecem no centro da tela do dispositivo com uma sobreposição de tela que os ajuda a se destacar do seu aplicativo em segundo plano. Eles são perfeitos para sugerir, de forma não tão sutil, que o usuário aproveite uma venda ou um brinde.

Mensagem modal no aplicativo que aparece no centro de um aplicativo e site como uma caixa de diálogo. O modal inclui uma imagem, um cabeçalho, um corpo de mensagem e dois botões.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Fullscreen %}

As mensagens em tela cheia são exatamente o que você espera - elas ocupam a tela inteira do dispositivo! Esse tipo de mensagem é excelente quando você realmente precisa da atenção do usuário, como para atualizações obrigatórias de aplicativos.

\![Mensagem em tela cheia no aplicativo ocupando a tela do aplicativo. A mensagem em tela cheia inclui uma imagem grande, cabeçalho, corpo da mensagem e dois botões.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

Além desses modelos de mensagem prontos para uso, você também pode personalizar ainda mais suas mensagens usando mensagens HTML personalizadas no aplicativo, modais da Web com CSS ou formulários de captura de e-mail da Web. Para obter mais informações, consulte [Personalização]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

## Mais recursos

Antes de começar a criar suas próprias campanhas de mensagens in-app - ou usar mensagens in-app em uma campanha multicanal -, recomendamos que você consulte nosso [guia de preparação de mensagens in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/). Este guia aborda questões de segmentação, conteúdo e conversão que você deve considerar ao criar mensagens in-app.
