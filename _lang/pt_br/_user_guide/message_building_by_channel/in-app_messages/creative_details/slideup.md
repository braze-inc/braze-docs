---
nav_title: Slideup
article_title: Mensagens no app do Slideup
page_order: 2
channel:
  - in-app messages
tool:
  - Media
description: "Este artigo de referência aborda a mensagem e os requisitos de design das mensagens no app do slideup."

---

# Mensagens no app do slideup

> Nossos slideups normalmente aparecem na parte superior ou inferior da tela do app (você pode definir isso ao criar sua mensagem). Eles são ótimos para alertar seus usuários sobre novos termos de serviço, cookies e outros trechos de informações. Eles não são intrusivos e permitem que os usuários continuem a interagir com o app enquanto a mensagem é exibida.

![Duas mensagens deslizantes no app, uma aparecendo na parte superior da tela e a outra na parte inferior, detalhando as recomendações de imagem e texto. Consulte as seções a seguir para obter detalhes.]({% image_buster /assets/img/slideup-spec.png %}){: style="max-width: 40%; border: none;"}

## Comportamento de imagem e cópia

As mensagens slideup podem conter até três linhas de cópia antes de serem truncadas com elipses. As imagens em slideups nunca serão cortadas ou recortadas - elas sempre serão reduzidas para caber no contêiner de imagem de 50 x 50 pixels.

- Todas as imagens devem ter menos de 5 MB.
- Só aceitamos arquivos dos tipos PNG, JPEG e GIF.
- Recomendamos que suas imagens tenham 500 KB.

{% alert tip %} Crie ativos com confiança! Nossos modelos de imagem de mensagem no app e sobreposições de zona segura foram projetados para funcionar bem em dispositivos de todos os tamanhos. [Baixe os modelos de design ZIP]({% image_buster /assets/download_file/Braze-In-App-Message-Design-Templates.zip %}) {% endalert %}

| Layout | Tamanho do ativo | Notas |
|--- | --- | --- |
| Imagem + texto | Proporção de 1:1<br>Alta resolução 150 x 150 px<br> Mínimo de 50 x 50 px | Imagens de várias proporções de aspecto caberão em um contêiner de imagem quadrado, sem corte. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Sempre faça [uma prévia e teste suas mensagens]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/testing/) em vários dispositivos para garantir que as áreas mais importantes de sua imagem e mensagem apareçam conforme o esperado. Observe que, ao fazer a prévia de sua mensagem no criador, a renderização real nos dispositivos pode ser diferente.

## Dispositivos móveis

Em dispositivos móveis, os slideups aparecem na parte superior ou inferior da tela do app. Você pode especificar isso ao criar sua mensagem. Os usuários podem deslizar para descartar o slideup ou tocar para abri-lo se uma ação de clique estiver incluída. Se uma ação de clique for adicionada ao slideup, um chevron ">" será mostrado.

## Telas maiores

{% tabs %}
{% tab Desktop %}

Em um navegador de desktop, uma mensagem no app em slideup ficará no canto da tela, conforme mostrado na captura de tela a seguir (a menos que seja designado de outra forma ao criar a mensagem no app). Os usuários podem clicar no botão "X" para fechar o slideup.

![Mensagem no app do Slideup como aparece em um navegador de desktop. A mensagem aparece no canto inferior direito da tela e não ocupa a tela inteira.]({% image_buster /assets/img/slideup-large-viewport.png %}){: style="border: none;"}

{% endtab %}
{% tab Tablet %}

Em um tablet, uma mensagem slideup no app aparece na parte inferior da tela. Da mesma forma que nos dispositivos móveis, os usuários podem deslizar para descartar o slideup ou tocar para abri-lo se uma ação de clique estiver incluída. Se uma ação de clique for adicionada ao slideup, um chevron ">" será mostrado. O botão "X" de fechar não é exibido por padrão.

![Mensagem no app do slideup como aparece na tela de um tablet. A mensagem aparece na parte inferior central da tela e não ocupa a tela inteira.]({% image_buster /assets/img/slideup-tablet.png %}){: style="border: none;"}

{% endtab %}
{% endtabs %}

