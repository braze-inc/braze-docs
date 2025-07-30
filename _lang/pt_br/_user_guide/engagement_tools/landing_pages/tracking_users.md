---
nav_title: Rastreamento de usuários
article_title: Rastreamento de usuários por meio de um formulário
description: "Saiba como identificar os usuários que enviam um formulário por meio de sua landing page adicionando uma tag Liquid às suas mensagens."
page_order: 2
---

# Rastreamento de usuários por meio de um formulário

> Saiba como rastrear os usuários que enviam um formulário por meio de sua landing page adicionando uma tag Liquid da landing page às suas mensagens. Essa Liquid tag é suportada em todos os canais de envio de mensagens do Braze, incluindo e-mail, SMS, mensagens no app e muito mais. Para saber mais sobre dados de rastreamento, consulte [Sobre os dados de rastreamento da landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data).

## Como funciona?

Você pode adicionar uma {% raw %}`{% landing_page_url %}`{% endraw %} Liquid tag a qualquer uma de suas mensagens de canal único ou múltiplo no Braze. Quando um usuário visitar essa landing page e enviar o formulário, o Braze vinculará automaticamente esses dados ao seu perfil existente, em vez de criar um novo perfil para esse usuário. No exemplo a seguir, a tag Liquid da landing page é usada para vincular os clientes a uma pesquisa:

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
Também é possível usar as landing pages para geração de leads incorporando o URL da página em seus canais externos. Depois de criar uma landing page, acesse **Landing Page Details (Detalhes da landing page** ) para obter o URL exclusivo de sua landing page.
{% endalert %}

## Uso de tags Liquid da landing page

### Pré-requisitos

Antes de começar, você precisará criar uma [landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) e uma [campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

### Etapa 1: Verificar o URL da página {#page-url}

O Braze usará o URL de sua landing page para gerar sua Liquid tag exclusiva. Se quiser alterar o URL da página atual, acesse Envio **de mensagens** > **Landing Pages** e, em seguida, abra sua landing page. Em **URL da página**, você pode inserir um novo URL da página.

{% alert warning %}
Se você alterar o URL da página após o envio da mensagem, qualquer usuário que tentar visitar sua landing page usando o URL antigo será enviado para uma página `404`.
{% endalert %}

![Um exemplo de URL de página para uma landing page no Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Etapa 2: Gerar a Liquid tag

Acesse **Envio de mensagens** > **Campanhas** e escolha uma campanha. No editor de mensagens, selecione **Personalização**.

![O botão "Adicionar personalização" no editor de arrastar e soltar.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

O Braze gerará automaticamente uma Liquid tag usando o [URL de](#page-url) sua [landing page](#page-url). Consulte a tabela a seguir para gerar sua tag:

\|**Tipo** de personalização: Escolha **a landing page**.
\|**Escolha** a landing page que [você criou anteriormente](#prerequisites).
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para adicionar a tag Liquid à sua mensagem, você pode selecionar **Inserir** ou copiar o trecho para a área de transferência e adicioná-lo manualmente.

![Uma Liquid tag gerada automaticamente para a landing page selecionada.]({% image_buster /assets/img/landing_pages/get-snippet.png %}){: style="max-width:40%;"}

Seu snippet será semelhante ao seguinte:

{% raw %}
```ruby
{% landing_page_url custom-url-handle %}
```
{% endraw %}

### Etapa 3: Finalize e envie sua mensagem

Incorpore o snippet do Liquid em sua mensagem e, em seguida, finalize o restante da mensagem. Por exemplo:

{% raw %}
```html
<a href=" {% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

Quando estiver pronto, poderá enviar a mensagem para iniciar o rastreamento de usuários por meio da landing page.
