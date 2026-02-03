---
nav_title: Localidades em mensagens
article_title: Tradução de localidades
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artigo fornece etapas sobre como usar localidades em suas mensagens."
---

# Tradução de localidades

> Depois de adicionar localidades ao seu espaço de trabalho, é possível direcionar usuários em diferentes idiomas em um único push, e-mail, banner ou mensagem no app.

{% multi_lang_include locales.md section="Prerequisites" %}

## Uso de localidades

### Etapa 1: Configure as localizações em seu espaço de trabalho {#workspace-setup}

Antes de usar localidades e tags de tradução, é necessário [adicionar localidades ao seu espaço de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings).

### Etapa 2: Adicione tags Liquid de tradução à sua mensagem {#add-translation-tags}

Adicione as tags de tradução {% raw %}`{% translation your_id_here %}` e `{% endtranslation %}`{% endraw %} para envolver todos os URLs de texto, imagem ou link que serão traduzidos.

Cada tradução deve ter um `id` exclusivo. Por exemplo, ao traduzir uma saudação simples, você pode nomear o ID como "greeting":

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### Localização de blocos HTML

Um parágrafo mais complicado pode ter várias tags de tradução ("offer_text" e "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
O fato de envolver grandes blocos HTML em tags de tradução pode causar problemas de estilo ou folha de estilo. Envolva as menores seções de texto possíveis.
{% endalert %}

#### Localização de links

Para localizar links de tag âncora, certifique-se de envolver **apenas as partes específicas do idioma** e não todo o atributo de URL `href`. Se você envolver o URL inteiro, o modelo de link poderá não funcionar corretamente.

##### Uso correto

{% raw %}
```
<a href="https://www.braze.com/{% translation link_href %}en{% endtranslation %}/page"></a>
```
{% endraw %}

##### Uso incorreto

{% raw %}
```
<a href="{% translation link_href %}https://www.braze.com/en/page{% endtranslation %}"></a>
```
{% endraw %}

### Etapa 3: Escolha as localizações das mensagens {#choose-locales}

Depois que as tags de tradução estiverem na mensagem, acesse as configurações multilíngues da mensagem e selecione uma ou mais localizações a serem traduzidas para essa mensagem.

![Configurações em vários idiomas com um campo suspenso para selecionar as localizações.]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
Selecione **Multi-Language (Vários idiomas** ) no menu Content (Conteúdo) ao editar sua mensagem.

![Configurações em vários idiomas para e-mail.]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
Selecione **Gerenciar idiomas** ao editar sua mensagem.

![Configurações em vários idiomas para push.]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
Selecione **Manage Languages (Gerenciar idiomas** ) na parte inferior da seção **Build**.

![Configurações em vários idiomas para mensagens no app do tipo arrastar e soltar.]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

Selecione **Gerenciar idiomas** ao editar sua mensagem.

![Configurações em vários idiomas para mensagens no app em HTML.]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
Selecione **Gerenciar idiomas** ao editar sua mensagem.

![Configurações em vários idiomas para banners.]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Baixar o modelo CSV {#download-csv}

Depois de selecionar suas localidades, selecione **Baixar modelo** para baixar um modelo CSV contendo uma matriz de suas IDs de tradução e localidades selecionadas.

![Exemplo de CSV para as localidades en, fr e es.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### Etapa 5: Faça upload de um CSV preenchido {#upload-csv}

{% alert important %}
Quaisquer alterações nas IDs ou localizações no arquivo CSV não serão atualizadas automaticamente em sua mensagem. Para atualizar as traduções, atualize o arquivo CSV e faça upload do arquivo novamente.
{% endalert %}

Aqui está o formato de um exemplo de CSV preenchido:

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### Etapa 6: Prévia das localizações {#preview-locales}

Ao fazer a prévia da mensagem, selecione a opção **Usuário multilíngue** no menu suspenso **Pré-visualizar como usuário**. Isso permite que você alterne entre diferentes definições de localização para prévia de todas as traduções de sua mensagem.

![Prévias de localidades]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
Confira nossa [API de tradução]({{site.baseurl}}/api/endpoints/translations) para gerenciar e atualizar traduções em suas campanhas e canvas.
{% endalert %}

## Envio de mensagens da direita para a esquerda

Ao preencher o arquivo de tradução para idiomas que são escritos da direita para a esquerda (como o árabe), envolva a tradução com `span` para que ela seja formatada corretamente:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## Gerenciamento de traduções

### Edição de traduções para campanhas e telas lançadas

Depois que uma campanha ou uma tela for lançada, você ainda poderá modificar as traduções quando estiver no modo de rascunho. Isso se aplica se estiver editando traduções diretamente no criador, fazendo upload de CSV ou por meio da API. 

Para obter mais detalhes sobre o gerenciamento de campanhas e Canvas após o lançamento, consulte [Edição de campanhas lançadas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) e [rascunhos do Canvas e edição pós-lançamento]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplicação de etapas ou campanhas do Canva e traduções

As traduções são copiadas junto com uma etapa do canva, campanha ou variação de campanha. Isso também é verdadeiro ao copiar entre espaços de trabalho, desde que as localizações estejam definidas no espaço de trabalho de destino. Certifique-se de revisar e atualizar as traduções adequadamente ao fazer modificações em seu Canva ou campanha.

### Uso da API multilíngue com o Canvas

Para usar a [API multilíngue com as telas]({{site.baseurl}}/api/endpoints/translations/), você deve incluir `workflow_id`, `step_id` e `message_variation_id` na lista de parâmetros.

#### Etapas do canva adicionadas aos rascunhos pós-lançamento

Ao usar a API multilíngue com etapas do Canva que foram criadas após o lançamento do Canvas, o endereço `message_variation_id` que você passar para a API estará vazio ou em branco.

## Perguntas frequentes

#### Posso fazer uma alteração na cópia traduzida em uma de minhas localizações?
Sim. Primeiro, faça a edição no CSV e, em seguida, faça upload do arquivo novamente para fazer uma alteração na cópia traduzida.

#### Posso aninhar tags de tradução?
Não.

#### As traduções são compatíveis com HTML para estilo?
Sim, mas certifique-se de verificar se o estilo HTML não está traduzido com o conteúdo.

#### Posso envolver mensagens HTML inteiras em uma tag de tradução?
Não, suas tags de tradução devem ser tão pequenas quanto possível para evitar limitações de performance ou tamanho.

#### Que validações ou verificações extras o Braze faz?

| Cenário                                                                                                                                                 | Validação em Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Um arquivo de tradução não tem localidades associadas à mensagem atual.                                                                               | Esse arquivo de tradução não será carregado.                                                                       |
| Um arquivo de tradução está sem alguns blocos de texto, como um texto dentro de tags de tradução Liquid, da mensagem de e-mail atual.                                | Esse arquivo de tradução não será carregado.                                                                       |
| O arquivo de tradução inclui o texto padrão que não corresponde aos blocos de texto da mensagem de e-mail atual.                                          | Esse arquivo de tradução não será carregado. Corrija isso em seu CSV antes de tentar fazer upload novamente.               |
| O arquivo de tradução inclui localizações que não existem nas configurações **do Suporte multilíngue**.                                                           | Essas localizações não serão salvas no Braze.                                                                      |
| O arquivo de tradução inclui blocos de texto que não existem na mensagem atual (como o rascunho atual no momento em que as traduções são feitas upload). | Os blocos de texto que não existirem em sua mensagem atual não serão salvos do arquivo de tradução para o Braze. |
| Remoção de uma localização da mensagem depois que essa localização já tiver sido carregada para a mensagem como parte do arquivo de tradução.                           | A remoção da localidade removerá todas as traduções associadas à localidade em sua mensagem.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }
