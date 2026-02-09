---
nav_title: Rastreamento de usuários
article_title: Rastrear usuários através de um formulário
description: "Aprenda como identificar usuários que enviam um formulário através da sua landing page adicionando uma Liquid tag às suas mensagens."
page_order: 2
---

# Rastrear usuários através de um formulário

> Aprenda como rastrear usuários que enviam um formulário através da sua landing page adicionando uma Liquid tag de landing page às suas mensagens. Essa Liquid tag é suportada em todos os canais de envio de mensagens do Braze, incluindo e-mail, SMS, mensagens no app e muito mais. Para saber mais sobre dados de rastreamento, consulte [Sobre os dados de rastreamento da landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/about_tracking_data).

## Como funciona?

Você pode adicionar uma {% raw %}`{% landing_page_url %}`{% endraw %} Liquid tag a qualquer uma das suas mensagens de canal único ou multi-canal no Braze. Quando um usuário visitar essa landing page e enviar o formulário, o Braze vinculará automaticamente esses dados ao seu perfil existente, em vez de criar um novo perfil para esse usuário. No exemplo a seguir, uma Liquid tag de landing page é usada para vincular clientes a uma pesquisa:

{% raw %}
```html
<a href="{% landing_page_url customer-survey %}" class="button">Take the Survey!</a>
```
{% endraw %}

{% alert tip %}
Você também pode usar landing pages para geração de leads incorporando a URL da página em seus canais externos. Depois de criar uma landing page, acesse **Detalhes da Landing Page** para obter a URL única da sua landing page.
{% endalert %}

## Uso de tags Liquid da landing page

### Pré-requisitos

Antes de começar, você precisará criar uma [landing page]({{site.baseurl}}/user_guide/engagement_tools/landing_pages/creating_pages/) e uma [campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/creating_campaign/).

### Etapa 1: Verifique a URL da página {#page-url}

O Braze usará a URL da sua landing page para gerar sua Liquid tag única. Se você quiser alterar a URL da página atual, acesse **Envio de Mensagens** > **Landing Pages**, então abra sua landing page. Em **URL da página**, você pode inserir uma nova URL da página.

{% alert warning %}
Se você alterar a URL da página após enviar sua mensagem, qualquer usuário que tentar visitar sua landing page usando a URL antiga será enviado para uma página `404`.
{% endalert %}

![Uma URL de página de exemplo para uma landing page no Braze.]({% image_buster /assets/img/landing_pages/url-handle-example.png %}){: style="max-width:80%;"}

### Etapa 2: Gerar a Liquid tag

Acesse **Envio de mensagens** > **Campanhas** e escolha uma campanha. No editor de mensagens, selecione **Personalização**.

![O botão 'Adicionar personalização' no editor de arrastar e soltar.]({% image_buster /assets/img/landing_pages/select-personalization.png %}){: style="max-width:75%;"}

O Braze gerará automaticamente uma Liquid tag usando sua [URL da landing page](#page-url). Consulte a tabela a seguir para gerar sua tag:

\|**Tipo de personalização**| Escolha **Landing Page**.|
\|**Landing page**|Escolha a landing page [que você criou anteriormente](#prerequisites).|
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
