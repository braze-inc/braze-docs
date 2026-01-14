---
nav_title: Detalhes criativos
article_title: Detalhes criativos para cartões de conteúdo
page_order: 1
description: "Este artigo aborda detalhes criativos, como recomendações de tamanho de imagem e comportamento de dispensa nos três tipos de Content Card padrão."
channel:
  - content cards
tool: Media

---

# Detalhes criativos para cartões de conteúdo

> A personalização dos Content Cards e do feed em que eles estão localizados não pode ser feita durante o processo de criação da campanha - você deve trabalhar com seus engenheiros e desenvolvedores para criar e personalizar seus cards. Para obter detalhes técnicos, visite nossa [documentação para desenvolvedores]({{site.baseurl}}/developer_guide/getting_started/customization_overview).

## Tipos de cartão de conteúdo

{% tabs %}
{% tab Classic %}

O cartão clássico é ótimo para mensagens e notificações padrão ou até mesmo para categorizar visualmente as mensagens com ícones. A imagem é opcional, mas deve estar em uma proporção de 1:1.

\![Imagem de um cartão clássico com detalhes recomendados e um exemplo de cartão clássico]({% image_buster /assets/img/content_card_classic.png %}){: style="max-width:45%;border:0;"}

| Capacidade do cartão | Detalhes |
| --- | ---|
| Texto do cabeçalho | 18px; Negrito <br> Uma linha de texto é o ideal. <br> Você pode usar o Liquid aqui para personalizar sua mensagem. |
| Texto da mensagem | 13px; Peso regular <br> Duas a quatro linhas de texto são ideais. <br> Você pode usar o Liquid aqui para personalizar sua mensagem. |
| Texto do link | Opcional. <br> 13 px <br> Link para a página da Web ou link direto para dentro do aplicativo. |
| Imagem | Opcional. <br> Deve ter uma proporção de 1:1. <br> Recomendamos uma qualidade de imagem de 60 x 60 px. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% endtab %}
{% tab Captioned Image %}

O cartão de imagem com legenda é uma ótima maneira de exibir e chamar a atenção para conteúdos importantes, como uma grande promoção ou um novo recurso do aplicativo.

Imagem de um cartão Captioned Image com detalhes recomendados e um exemplo de cartão Captioned Image]({% image_buster /assets/img/content_card_captioned.png %}){: style="max-width:90%;border:0;"}

| Capacidade do cartão | Detalhes |
| --- | ---|
| Texto do cabeçalho | 18px; Negrito <br> Uma linha de texto é o ideal. <br> Você pode usar o Liquid aqui para personalizar sua mensagem. |
| Texto da mensagem | 13px; Peso regular <br> Duas a quatro linhas de texto são ideais. <br> Você pode usar o Liquid aqui para personalizar sua mensagem. |
| Texto do link | Opcional. <br> 13 px <br> Link para a página da Web ou link direto para dentro do aplicativo. |
| Imagem | Sugere-se uma proporção de 4:3. <br> Largura mínima de 600 px.  <br> Oferece suporte a PNG, JPEG e GIF de alta resolução. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab Image-only %}

Se quiser ter mais controle criativo, o cartão somente de imagem é ideal para você. Crie sua imagem usando qualquer ferramenta de sua preferência e carregue a imagem nesse tipo de cartão.

\![Imagem de um Content Card somente de imagem com detalhes recomendados e um exemplo somente de imagem]({% image_buster /assets/img/content_card_banner.png %}){: style="max-width:45%;border:0;"}

| Capacidade do cartão | Detalhes |
| --- | ---|
| Cartão vinculado | Opcional. <br> 13 px <br> Link de comportamento no clique para uma página da Web ou um link profundo para dentro do seu aplicativo. |
| Imagem | Suporte a qualquer proporção de aspecto. <br> Largura mínima de 600 px.  <br> Oferece suporte a PNG, JPEG e GIF de alta resolução. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Detalhes criativos globais {#general}

Os Content Cards vêm com uma excelente funcionalidade desde o início. No momento, a estilização do cartão não pode ser feita nativamente em sua conta Braze, mas você pode estilizar seu Content Card por tipo e o feed do Content Card durante a integração. Consulte [Personalização de cartões de conteúdo]({{site.baseurl}}/developer_guide/content_cards/) para obter mais informações.

### Comportamento de demissão

Para um usuário descartar um cartão, ele pode passar o dedo no celular ou usar a função `close X`, conforme mostrado na captura de tela a seguir. O endereço `x` aparecerá ao passar o mouse somente para o Web SDK.

Imagem que mostra os comportamentos de passar o dedo ou de fechar um cartão]({% image_buster /assets/img/dismissal-cc.png %})

Se um usuário tiver descartado todos os seus cartões ou se você não tiver enviado nenhuma atualização nova, o feed do usuário geralmente terá a seguinte aparência:

\![Imagem de um feed de Content Card vazio]({% image_buster /assets/img/empty-cc.png %}){: style="max-width:45%"}

{% alert tip %}
Mantenha os Content Cards relevantes, configurando-os para serem descartados quando um usuário realizar ações relevantes. Por exemplo, configure os Content Cards promocionais para serem descartados assim que os usuários fizerem uma compra, para que eles não continuem a ver uma oferta para algo que já compraram.
{% endalert %}

### Uso de GIFs em cartões de conteúdo

| Cartões de conteúdo para Android | Cartões de conteúdo para iOS | Cartões de conteúdo para a Web |
| --- | --- |---|
| O SDK do Android não oferece suporte a GIFs animados por padrão. Para obter mais detalhes sobre a ativação do suporte a [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android), consulte [GIFs]({{site.baseurl}}/developer_guide/content_cards/embedding_gifs/?sdktab=android). | O Swift SDK não oferece suporte a GIFs animados por padrão. Para obter mais detalhes sobre a ativação do suporte a GIFs, consulte o [tutorial de suporte a GIFs](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c3-gif-support). | O suporte a GIF está incluído por padrão na integração do Web SDK. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

<br><br>

