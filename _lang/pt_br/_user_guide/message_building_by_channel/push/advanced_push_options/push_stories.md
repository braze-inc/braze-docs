---
nav_title: "Histórias de sucesso"
article_title: Histórias de empurrar
page_order: 2
page_type: reference
description: "Este artigo de referência aborda o que são as Push Stories, como criá-las, bem como algumas perguntas frequentes."
channel:
  - push

---

# Histórias de empurrar

> O Push Stories é um novo tipo de notificação por push introduzido pelo Braze. Esse recurso usa a funcionalidade de carrossel de fotos popularizada no Instagram e no Facebook e permite que os profissionais de marketing criem um carrossel de páginas em um push que conte uma história rica e coesa. Essas páginas consistem em uma imagem, ação de clique, título e descrição. Seus usuários podem percorrer essas páginas e ver a história contada por você.

| Exemplo de Android (expandido) | Exemplo de IOS (expandido) |
| :-----: | :----------: |
| \![]({% image_buster /assets/img_archive/pushstories_android_preview.png %}) | \![]({% image_buster /assets/img_archive/pushstories_ios_preview.png %}) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Nas versões 3.13.0+ do SDK do iOS, devido a uma alteração na forma como o SDK baixa as imagens, uma miniatura da primeira imagem não será exibida na visualização condensada do push. Certifique-se de que o texto da mensagem solicite aos usuários que expandam o push para ver as imagens.
{% endalert %}

## Pré-requisitos

As seguintes versões do SDK são necessárias para receber o Push Stories:

{% sdk_min_versions swift:5.0.0 android:2.2.0 %}


## Como usar o Push Stories

\![]({% image_buster /assets/img_archive/pushstories_composer_dropdown2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Para usar o Push Stories, faça o seguinte:

1. Crie uma [campanha de envio]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/).
2. Para o **tipo de notificação**, selecione **Push Stories**.
3. Selecione **iOS** ou **Android**. Observe que, se você selecionar ambos para uma mensagem push, a opção de criar uma história push não será exibida. 

### Compositor do Push Story

Para criar uma página, execute as seguintes etapas:

1. Clique em **Manage Pages (Gerenciar páginas** ) no compositor principal.
    <br><br>\![]({% image_buster /assets/img_archive/pushstories_add_pages.png %}){: style="max-width:70%"}<br><br>
2. Insira uma imagem para cada página, juntamente com o comportamento de clique para essa imagem.
3. Se desejar, adicione um **título** e uma **descrição** para cada página. Se você usar um título e uma descrição para uma página, eles deverão ser inseridos em todas as páginas.

As visualizações serão refletidas e são interativas.

\![]({% image_buster /assets/img_archive/pushstories_composer.png %}){: style="max-width:60%"}

{% alert important %}
Se estiver extraindo imagens com o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/#about-connected-content), certifique-se de que o URL da imagem comece com `https://`. O uso do endereço `http://` causará falha no aplicativo.
{% endalert %}

### Especificações de imagem e texto

As especificações de imagem e texto a seguir se aplicam à parte do carrossel de fotos do Push Stories. Para obter informações sobre o push básico com o qual os usuários interagem para ativar o Push Story, consulte as [diretrizes de texto para push]({{site.baseurl}}/user_guide/message_building_by_channel/push/about/#native-mobile-push-notifications).

{% tabs %}
{% tab Images %}

- **Proporção da imagem:** 2:1 (obrigatório)
- **Tamanho de imagem recomendado:** 500 KB
- **Tamanho máximo da imagem:** 5 MB
- **Tipos de arquivos:** PNG, JPEG

{% endtab %}
{% tab Text %}

- **Título:** 30 caracteres (recomendado)
- **Descrição:** 30 caracteres (recomendado)

{% alert note %}
Embora possa haver alguma variação no comprimento dos caracteres de um dispositivo para outro, o título e a descrição das Push Stories são limitados a uma linha cada. O restante de sua mensagem será truncado. Sempre teste sua mensagem em um dispositivo real.
{% endalert %}

{% endtab %}
{% endtabs %}

### Segmentação de histórias push

Ao criar uma campanha ou um Canvas, você pode filtrar os usuários que deseja segmentar com base no fato de eles terem clicado em uma página do Push Story. Em seguida, selecione a campanha e a página que deseja usar para segmentar seus usuários.

### Análise de histórias push

A análise será muito parecida com a seção de análise atual para notificações por push. Para a análise do Push Stories, você pode abrir a métrica **Direct Opens** para visualizar os cliques por página.

Tabela de desempenho de push do iOS com exemplos de análises e detalhes expandidos para a métrica Direct Opens.]({% image_buster /assets/img_archive/pushstories_analytics.png %})

## Solução de problemas

### iOS

#### Enviei um Push Story para mim mesmo, mas não recebi a notificação

A Apple tem regras específicas que impedem o envio de determinados tipos de notificações a um dispositivo com base em vários fatores diferentes. Isso inclui a avaliação do plano de dados do cliente, do tamanho da notificação e da capacidade de armazenamento do cliente. Como resultado, às vezes nenhuma notificação será enviada aos seus clientes.

Essas são limitações impostas pela Apple que devem ser consideradas ao projetar seu Push Story.

#### Enviei a mim mesmo um Push Story, mas, em vez disso, vi a visualização condensada

Em determinadas situações em que todas as páginas não forem carregadas, por exemplo, devido a uma perda de conexão de dados, o Push Story mostrará apenas a notificação condensada.

### Android

#### O Push Story não é descartado após clicar na imagem 

Por padrão, as Push Stories não são descartadas no Android depois que o usuário clica na imagem. Se você quiser ignorar a notificação, ligue para [`cancelNotification`](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.push/-braze-notification-utils/index.html#-1466259649%2FFunctions%2F-1725759721).  

