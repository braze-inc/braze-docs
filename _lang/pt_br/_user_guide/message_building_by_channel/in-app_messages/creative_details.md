---
nav_title: Detalhes criativos
article_title: Detalhes criativos
page_order: 3.5
layout: dev_guide
guide_top_header: "Detalhes criativos"
guide_top_text: "Antes de ser criativo com nossas mensagens no aplicativo, você deve conhecer algumas das diretrizes. Todos os modelos de mensagens in-app são projetados para exibir textos de tamanhos variados e imagens em dispositivos modernos. Para garantir que sua mensagem seja bem exibida em todos os telefones, tablets e computadores, recomendamos que você siga estas diretrizes e sempre <a href='/docs/user_guide/message_building_by_channel/in-app_messages/testing/'>teste suas mensagens</a> antes de lançá-las."
description: "Este hub de aterrissagem abrange os requisitos de design e conteúdo para os três tipos de mensagens in-app: modal, slideup e tela cheia."

channel:
  - in-app messages
tools:
  - Media

guide_featured_title: "Especificações por tipo de mensagem"

guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/modal/
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup/
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: "Tela cheia"
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/
  image: /assets/img/braze_icons/expand-05.svg

---

## Diretrizes de conteúdo

### Texto

Para os corpos ou cabeçalhos de mensagens in-app, recomendamos que você seja breve e agradável - de uma a duas linhas para cabeçalhos e até três para corpos. Após três linhas, a mensagem provavelmente precisará ser rolada verticalmente, e os usuários podem não se envolver com todo o conteúdo. O limite que aciona a rolagem pode variar de acordo com o tamanho do dispositivo do usuário final, o estilo personalizado ou a presença de imagens nas mensagens, mas três linhas geralmente são seguras.

Se você estiver usando a geração mais recente de mensagens no aplicativo (Geração 3), verá que as fontes são padronizadas para a Sans Serif padrão do sistema operacional para iOS e Android. As mensagens in-app da Web terão como padrão o Helvetica.

### Imagens

Nossas diretrizes para imagens são mais estruturadas do que as de texto, pois queremos garantir que suas mensagens sejam exibidas da forma pretendida e com beleza em telefones, tablets e computadores de todos os modelos e tamanhos.

Em geral, a Braze recomenda o uso de imagens que se encaixem em uma tela 16:10.

- **Todas as imagens devem ter menos de 5 MB.**
- Só aceitamos arquivos dos tipos PNG, JPEG e GIF.
- Recomendamos hospedar imagens na [biblioteca de mídia]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/media_library/) para permitir que o Braze SDK faça download de ativos de nosso CDN para exibição de mensagens off-line.
- Para mensagens em tela cheia, siga nossas diretrizes para a [zona de segurança de imagens]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen/#image-safe-zone).

{% alert tip %} Crie ativos com confiança! Nossos modelos de imagens de mensagens no aplicativo e sobreposições de zonas seguras foram projetados para funcionar bem em dispositivos de todos os tamanhos. [Download dos modelos de design ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

{% tabs %}{% tab Fullscreen %}

\![Mensagem em tela cheia no aplicativo ocupando a tela do aplicativo. A mensagem em tela cheia inclui uma imagem grande, cabeçalho, corpo da mensagem e dois botões.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

| Layout | Tamanho do ativo | Notas |
|--- | --- | --- |
| Imagem + texto | Proporção de 6:5<br>Alta resolução 1200 x 1000 px<br> Mínimo de 600 x 500 px | O corte pode ocorrer em todos os lados, mas a imagem sempre preencherá os 50% superiores da janela de visualização |
| Somente imagem | Relação de aspecto 3:5<br>Alta resolução 1200 x 2000 px<br> Mínimo de 600 x 1000 px | O corte pode ocorrer nas bordas esquerda e direita em dispositivos mais altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Mais detalhes para telas completas]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/fullscreen)


{% endtab %}
{% tab Modal %}

Mensagem modal no aplicativo que aparece no centro de um aplicativo e site como uma caixa de diálogo. O modal inclui uma imagem, um cabeçalho, um corpo de mensagem e dois botões.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

| Layout | Tamanho do ativo | Notas |
|--- | --- | ------ |
| Imagem + texto | Relação de aspecto 29:10<br>Alta resolução 1450 x 500 px<br> Mínimo de 600 x 205 px | As imagens altas serão reduzidas e centralizadas horizontalmente. Imagens largas serão cortadas nas bordas esquerda e direita. |
| Somente imagem | Praticamente qualquer proporção de aspecto<br>Alta resolução de até 1200 x 2000 px<br> Mínimo de 600 x 600 px | A mensagem será redimensionada para se ajustar a imagens com a maioria das proporções. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Mais detalhes para modais]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/modal)

{% endtab %}
{% tab Slideup %}

Mensagem de slideup no aplicativo que aparece na parte inferior da tela do aplicativo. O slideup inclui uma imagem de ícone e uma breve mensagem.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

| Layout | Tamanho do ativo | Notas |
|--- | --- | --- |
| Imagem + texto | Proporção de 1:1<br>Alta resolução 150 x 150 px<br> Mínimo de 50 x 50 px | Imagens de várias proporções de aspecto caberão em um contêiner de imagem quadrado, sem corte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

[Mais detalhes para slideups]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/slideup)

{% endtab %}
{% endtabs %}

### GIFs e vídeos

Atualmente, o Braze oferece suporte a GIFs para mensagens no aplicativo na Web (inclusive), [Android]({{site.baseurl}}/developer_guide/in_app_messages/gifs/?sdktab=android) e iOS (inclusive), uma vez que isso foi ativado durante a integração da plataforma desejada. Para saber mais sobre vídeos em mensagens in-app, consulte nossa [documentação de personalização]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/#video).

## Considerações adicionais

As mensagens Braze no aplicativo têm especificações criativas globais e individuais. Para obter mais informações sobre como personalizar totalmente as mensagens in-app, acesse nossa página [Personalização]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/customize/).

<br>
