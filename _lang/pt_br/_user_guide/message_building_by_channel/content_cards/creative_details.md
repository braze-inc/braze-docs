---
nav_title: Detalhes criativos
article_title: Detalhes criativos para cartões de conteúdo
page_order: 1
description: "Este artigo aborda detalhes criativos, como recomendações de tamanho de imagem e comportamento de descarte de cartão nos três tipos de cartão de conteúdo padrão."
channel:
  - content cards
tool: Media

---

# Detalhes criativos para cartões de conteúdo

> A personalização dos cartões de conteúdo e do feed em que eles estão localizados não pode ser feita durante o processo de criação da campanha - você deve trabalhar com seus engenheiros e desenvolvedores para criar e personalizar seus cartões. Para obter detalhes técnicos, visite nossa [documentação para desenvolvedores]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Tipos de cartão de conteúdo

{% tabs %}
{% tab Clássico %}

O cartão clássico é ótimo para envio de mensagens e notificações padrão ou até mesmo para categorizar visualmente as mensagens com ícones. A imagem é opcional, mas deve estar em uma proporção de 1:1.

![Imagem de um cartão clássico com detalhes recomendados e um exemplo de cartão clássico]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| Capacidade do cartão | Informações |
| --- | ---|
| Texto do cabeçalho | 18px; Negrito <br> Uma linha de texto é o ideal. <br> Você pode usar o Liquid aqui para personalizar sua mensagem. |
| Texto da mensagem | 13px; Peso regular <br> O ideal são duas a quatro linhas de texto. <br> Você pode usar o Liquid aqui para personalizar sua mensagem. |
| Texto do link | Opcional. <br> 13 px <br> Link para página da Web ou deep linking em seu aplicativo. |
| Imagem | Opcional. <br> Deve ter uma proporção de 1:1. <br> Recomendamos uma qualidade de imagem de 60 x 60 px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Imagem legendada %}

O cartão de imagem legendada é uma ótima maneira de exibir e atrair a atenção para conteúdos importantes, como uma grande venda ou um novo recurso do app.

![Imagem de um cartão Captioned Image com detalhes recomendados e um exemplo de cartão Captioned Image]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| Capacidade do cartão | Informações |
| --- | ---|
| Texto do cabeçalho | 18px; Negrito <br> Uma linha de texto é o ideal. <br> Você pode usar o Liquid aqui para personalizar sua mensagem. |
| Texto da mensagem | 13px; Peso regular <br> O ideal são duas a quatro linhas de texto. <br> Você pode usar o Liquid aqui para personalizar sua mensagem. |
| Texto do link | Opcional. <br> 13 px <br> Link para página da Web ou deep linking em seu aplicativo. |
| Imagem | Sugere-se uma proporção de 4:3. <br> Largura mínima de 600 px.  <br> Oferece suporte a PNG, JPEG e GIF de alta resolução. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Somente imagem %}

Se quiser ter mais controle criativo, o cartão somente para imagens é ideal para você. Crie sua imagem usando qualquer ferramenta de sua preferência e faça upload da imagem para esse tipo de cartão.

![Imagem de um cartão de conteúdo somente de imagem com detalhes recomendados e um exemplo somente de imagem]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| Capacidade do cartão | Informações |
| --- | ---|
| Cartão vinculado | Opcional. <br> 13 px <br> Comportamento ao clicar em um link para uma página da Web ou um deep linking para dentro do seu aplicativo. |
| Imagem | Suporte a qualquer proporção de aspecto. <br> Largura mínima de 600 px.  <br> Oferece suporte a PNG, JPEG e GIF de alta resolução. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Detalhes criativos globais {#general}

Os cartões de conteúdo vêm com grande funcionalidade desde o início. No momento, a estilização do cartão não pode ser feita nativamente em sua conta Braze, mas você pode estilizar seu cartão de conteúdo por tipo e o feed do cartão de conteúdo durante a integração. Para saber mais, consulte [Personalização de cartões de conteúdo]({{site.baseurl}}/developer_guide/content_cards/).

### Comportamento de demissão

Para um usuário descartar um cartão, ele pode passar o dedo no celular ou usar a função `close X`, conforme mostrado na captura de tela a seguir. O endereço `x` aparecerá ao passar o mouse somente para o SDK Web.

![Imagem que mostra os comportamentos de descarte de cartão por deslizar ou fechar]({% image_buster /assets/img/dismissal-cc.png %})

Se um usuário tiver descartado todos os seus cartões ou se você não tiver empurrado nenhuma nova atualização, o feed do usuário geralmente terá a seguinte aparência:

![Imagem de um feed de cartão de conteúdo vazio]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
Mantenha os cartões de conteúdo relevantes, configurando-os para serem descartados quando um usuário realizar ações relevantes. Por exemplo, configure os cartões de conteúdo promocionais para serem descartados assim que os usuários fizerem uma compra, para que eles não continuem a ver uma oferta para algo que já compraram.
{% endalert %}

### Uso de GIFs em cartões de conteúdo

| Cartões de conteúdo para Android | Cartões de conteúdo para iOS | Cartões de conteúdo para a Web |
| --- | --- |---|
| O SDK para Android não oferece suporte a GIFs animados por padrão. Para obter mais detalhes sobre a ativação do suporte a GIFs, consulte [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android). | O Swift SDK não oferece suporte a GIFs animados por padrão. Para obter mais detalhes sobre a ativação do suporte a GIFs, consulte o [tutorial de suporte a GIFs](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | O suporte a GIF está incluído por padrão na integração do SDK Web. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

