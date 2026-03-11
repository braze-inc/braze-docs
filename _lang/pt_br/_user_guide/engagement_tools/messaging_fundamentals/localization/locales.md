---
nav_title: Locais em mensagens
article_title: Traduzindo locais
alias: /locales_in_messages/
page_order: 0
page_type: reference
description: "Este artigo fornece etapas sobre como usar locais em suas mensagens."
---

# Traduzindo locais

> Depois de adicionar locais ao seu espaço de trabalho, você pode direcionar usuários em diferentes idiomas em um único push, e-mail, banner, mensagem no app ou bloco de conteúdo.

{% multi_lang_include locales.md section="Prerequisites" %}

## Uso de localidades

### Etapa 1: Configure locais em seu espaço de trabalho {#workspace-setup}

Antes de usar locais e tags de tradução, você deve primeiro [adicionar locais ao seu espaço de trabalho]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings).

### Etapa 2: Adicione tags de tradução liquid à sua mensagem {#add-translation-tags}

Adicione tags de tradução {% raw %}`{% translation your_id_here %}` e `{% endtranslation %}`{% endraw %} para envolver todo texto, imagem ou URLs de links que você irá traduzir.

Cada tradução deve ter um `id` único. Por exemplo, ao traduzir uma saudação simples, você pode nomear o ID como "saudação":

{% raw %}`{% translation greeting %}Hello!{% endtranslation}`{% endraw %}

#### Localizando blocos HTML

Um parágrafo mais complicado pode ter múltiplas tags de tradução ("offer_text" e "offer_amount"):

{% raw %}
```
{% translation offer_text %}Sign up now to save{% endtranslation %}
<b>{% translation offer_amount %}50% Off{% endtranslation %}</b>
```
{% endraw %}

{% alert important %}
Envolver grandes blocos HTML em tags de tradução pode causar problemas de estilo ou de folha de estilo. Envolva as menores seções de texto possíveis.
{% endalert %}

#### Localizando Links

Para localizar links de tags de âncora, certifique-se de envolver **apenas as partes específicas do idioma** e não todo o atributo de URL `href`. Se você envolver toda a URL, a modelagem de links pode não funcionar corretamente.

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

### Etapa 3: Escolha os locais da mensagem {#choose-locales}

Após seus tags de tradução estarem na mensagem, acesse as configurações de múltiplos idiomas da mensagem e selecione um ou mais locais para traduzir esta mensagem.

![Configurações de múltiplos idiomas com um campo suspenso para selecionar locais.]({% image_buster /assets/img/multi-language_support/manage_language_dropdown.png %}){: style="max-width:80%;"}

{% tabs %}
{% tab Email %}
Selecione **Multi-Language** no menu de Conteúdo ao editar sua mensagem.

![Configurações de múltiplos idiomas para e-mail.]({% image_buster /assets/img/multi-language_support/email_multi_language.png %}){: style="max-width:45%;"}

{% endtab %}

{% tab Push %}
Selecione **Gerenciar Idiomas** ao editar sua mensagem.

![Configurações de múltiplos idiomas para push.]({% image_buster /assets/img/multi-language_support/push_manage_languages.png %})

{% endtab %}

{% tab In-app message %}
{% subtabs %}
{% subtab Drag-and-Drop Editor %}
Selecione **Gerenciar Idiomas** na parte inferior da seção **Construir**.

![Configurações de múltiplos idiomas para mensagens de arrastar e soltar no app.]({% image_buster /assets/img/multi-language_support/iam_dnd_manage_languages.png %}){: style="max-width:45%;"}

{% endsubtab %}
{% subtab Traditional editor %}

Selecione **Gerenciar Idiomas** ao editar sua mensagem.

![Configurações de múltiplos idiomas para mensagens HTML no app.]({% image_buster /assets/img/multi-language_support/iam_html_manage_languages.png %})

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab Banner %}
Selecione **Gerenciar Idiomas** ao editar sua mensagem.

![Configurações de múltiplos idiomas para banners.]({% image_buster /assets/img/multi-language_support/banner_manage_languages.png %})

{% endtab %}

{% tab Content Block %}
Selecione **Gerenciar Idiomas** ao editar seu Bloco de Conteúdo.

{% alert important %}
Blocos de Conteúdo que têm traduções associadas carregadas não podem ser sobrescritos por uma campanha individual ou mensagem de Canvas.
{% endalert %}

![Configurações de múltiplos idiomas para Blocos de Conteúdo.]({% image_buster /assets/img/multi-language_support/content_block_manage_languages.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Baixar modelo CSV {#download-csv}

Após selecionar seus locais, selecione **Baixar modelo** para baixar um modelo CSV contendo uma matriz de seus IDs de tradução selecionados e locais.

![Exemplo de CSV para locais en, fr e es.]({% image_buster /assets/img/multi-language_support/example_translation_csv.png %}){: style="max-width:70%;"}

### Etapa 5: Fazer upload de um CSV completo {#upload-csv}

{% alert important %}
Quaisquer alterações nas IDs ou localizações no arquivo CSV não serão atualizadas automaticamente em sua mensagem. Para atualizar as traduções, atualize o arquivo CSV e faça upload do arquivo novamente.
{% endalert %}

Aqui está o formato para um exemplo de CSV completo:

```
Variant1,,,,
,Translation tags,en,es,fr
title,We noticed you've left something behind,We noticed you've left something behind,Notamos que has dejado algo atrás,Nous avons remarqué que vous avez oublié quelque chose derrière vous
offer_text,Check out now and receive,Check out now and receive,Paga ahora y recibe,Payez maintenant et recevez
offer_amount,10% Off,10% Off,10% de Descuento,10 % de réduction
cta,CHECK OUT NOW,CHECK OUT NOW,VERIFICAR AHORA,VÉRIFIER MAINTENANT
```

### Etapa 6: Prévia de locais {#preview-locales}

Ao visualizar sua mensagem, selecione a opção **Multi-Language User** no menu suspenso **Preview as User**. Isso permite que você alterne entre diferentes definições de localidade para visualizar todas as traduções da sua mensagem.

![Visualizações de localidade]({% image_buster /assets/img/multi-language_support/multi_language_user_preview.png %})

{% alert tip %}
Confira nossa [API de tradução]({{site.baseurl}}/api/endpoints/translations) para gerenciar e atualizar traduções em suas campanhas e canvas.
{% endalert %}

## Mensagens da direita para a esquerda

Ao preencher o arquivo de tradução para idiomas que são escritos da direita para a esquerda (como o árabe), envolva a tradução com `span` para que ela seja formatada corretamente:

{% raw %}
```
{% translation your_id_here %}<span dir='rtl'>default text</span>{% endtranslation %}
```
{% endraw %}

## Gerenciando traduções

### Editando traduções para campanhas lançadas e Canvases

Após uma campanha ou Canvas ter sido lançada, você ainda pode modificar traduções quando estiver no modo de rascunho. Isso se aplica se você estiver editando traduções diretamente no criador, por upload de CSV ou através da API. 

Para mais detalhes sobre como gerenciar campanhas e Canvases após o lançamento, consulte [Editing launched campaigns]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/change_your_campaign_after_launch/) e [Canvas drafts and post-launch editing]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_drafts/).

### Duplicando etapas do Canvas ou campanhas, e traduções

As traduções são copiadas junto com uma etapa do canvas, campanha ou variação de campanha. Isso também é verdade ao copiar entre espaços de trabalho, desde que as localidades estejam definidas nesse espaço de trabalho de destino. Certifique-se de revisar e atualizar as traduções de acordo ao fazer modificações no seu Canvas ou campanha.

### Usando a API Multi-Language com Canvases

Para usar a [Multi-Language API with Canvases]({{site.baseurl}}/api/endpoints/translations/), você deve incluir o `workflow_id`, `step_id` e `message_variation_id` na lista de parâmetros.

#### Etapas do Canvas adicionadas a rascunhos pós-lançamento

Ao usar a API Multi-Language com etapas do Canvas que foram criadas após o lançamento do Canvas, o `message_variation_id` que você passar para a API estará vazio ou em branco.

## Perguntas frequentes

#### Posso fazer uma alteração na cópia traduzida em uma das minhas localidades?
Sim. Primeiro, faça a edição no CSV, depois faça o upload do arquivo novamente para fazer uma alteração na cópia traduzida.

#### Posso aninhar tags de tradução?
Não.

#### As traduções suportam HTML para estilização?
Sim, mas certifique-se de que a estilização HTML não seja traduzida junto com o conteúdo.

#### Posso envolver mensagens HTML inteiras em uma tag de tradução?
Não, suas tags de tradução devem ser o menor possível para evitar limitações de desempenho ou tamanho.

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
