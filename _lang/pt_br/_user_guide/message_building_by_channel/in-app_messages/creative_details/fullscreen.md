---
nav_title: "Tela cheia"
article_title: Mensagens no aplicativo em tela cheia
description: "Este artigo de referência aborda a mensagem e os requisitos de design das mensagens de tela cheia no aplicativo."
page_type: reference
page_order: 0
channel:
  - in-app messages
tool:
  - Media

---

# Mensagens no aplicativo em tela cheia

> As mensagens em tela cheia ocupam a tela inteira do dispositivo! Esse tipo de mensagem é excelente quando você realmente precisa da atenção do usuário, como para atualizações obrigatórias de aplicativos.

{% tabs %}
{% tab Portrait %}

Duas mensagens no aplicativo em tela cheia, lado a lado, na orientação retrato, detalhando as recomendações de imagem e texto. Consulte as seções a seguir para obter detalhes.]({% image_buster /assets/img/full-screen-spec.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

Duas mensagens no aplicativo em tela cheia, lado a lado, na orientação paisagem, detalhando as recomendações de imagem e texto. Consulte as seções a seguir para obter detalhes.]({% image_buster /assets/img/full-screen-spec-landscape.png %}){: style="max-width:801px;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

## Imagens

As mensagens in-app em tela cheia preencherão toda a altura de um dispositivo e serão cortadas horizontalmente (lados esquerdo e direito) conforme necessário. As mensagens de imagem e texto em tela cheia preencherão 50% da altura de um dispositivo. Todas as mensagens no aplicativo em tela cheia preencherão a barra de status em dispositivos "notched".

- Todas as imagens devem ter menos de 5 MB.
- Só aceitamos arquivos dos tipos PNG, JPEG e [GIF]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/customization/gifs#gifs).
- Recomendamos que suas imagens tenham 500 KB.

{% alert tip %} Crie ativos com confiança! Nossos modelos de imagens de mensagens no aplicativo e sobreposições de zonas seguras foram projetados para funcionar bem em dispositivos de todos os tamanhos. [Download dos modelos de design ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

### Retrato

| layout | tamanho do ativo | notas |
|--- | --- | --- |
| Imagem e texto | Proporção de 6:5<br> Alta resolução 1200 x 1000 px<br> Mínimo de 600 x 500 px | O corte pode ocorrer em todos os lados, mas a imagem sempre preencherá os 50% superiores da janela de visualização |
| Somente imagem | Relação de aspecto 3:5<br> Alta resolução 1200 x 2000 px<br> Mínimo de 600 x 1000 px | O corte pode ocorrer nas bordas esquerda e direita em dispositivos mais altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Paisagem

| layout | tamanho do ativo | notas |
|--- | --- | --- |
| Imagem e texto | Proporção de 10:3<br> Alta resolução 2000 x 600px<br> Mínimo de 1000 x 300 px | O corte pode ocorrer em todos os lados, mas a imagem sempre preencherá os 50% superiores da janela de visualização |
| Somente imagem | Proporção de 5:3<br> Alta resolução 2000 x 1200px<br> Mínimo de 1000 x 600 px | O corte pode ocorrer nas bordas esquerda e direita em dispositivos mais altos |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Zona de segurança de imagens

Ao visualizar uma mensagem in-app em tela cheia na plataforma Braze, você pode ativar a Zona de segurança da imagem para a área da mensagem que está protegida contra cortes quando exibida em dispositivos. Além de testar a Image Safe Zone no painel de visualização, recomendamos que você [teste sua mensagem]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) como sempre.

\![Pré-visualização de uma mensagem no aplicativo no Braze com a opção "Mostrar zona de segurança de imagem" ativada. A zona de segurança da imagem é uma sobreposição sobre a imagem que visualiza quais partes da imagem estarão protegidas contra o corte.]({% image_buster /assets/img/image-safe-zone-full-screen-in-app-message.png %})

## Telas maiores

Em um navegador de tablet ou desktop, uma mensagem no aplicativo em tela cheia ficará no centro da tela do aplicativo, conforme mostrado na captura de tela a seguir.

{% tabs %}
{% tab Portrait %}

\![Mensagem no aplicativo em tela cheia, como apareceria em uma tela grande na orientação retrato. A mensagem aparece como um modal grande que fica no centro da tela.]({% image_buster /assets/img/full-screen-large-viewport.png %}){: style="border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% tab Landscape %}

\![Mensagem no aplicativo em tela cheia, como apareceria em uma tela grande na orientação paisagem. A mensagem aparece como um modal grande que fica no centro da tela.]({% image_buster /assets/img/full-screen-large-viewport-landscape.png %}){: style="max-width:80%;border:none;display:block;margin-left:auto;margin-right:auto"}

{% endtab %}
{% endtabs %}

