---
nav_title: Configurações em vários idiomas
article_title: Configurações de tradução e de vários idiomas
alias: "/multi_language_support/"
page_order: 5.5
description: "Este artigo fornece uma visão geral das configurações multilíngues no dashboard da Braze e como usar localidades em seu envio de mensagens."
---

# Configurações de tradução e de vários idiomas

> O recurso multilíngue permite o uso de [tags de tradução]({{ site.baseurl }}/user_guide/engagement_tools/messaging_fundamentals/localization/locales) para direcionamento a usuários em diferentes idiomas e locais, tudo em uma única mensagem.

{% multi_lang_include locales.md section="Prerequisites" %}

## Adicionar um local

1. Acesse **Settings** > **Localization Settings (** **Configurações** > **Configurações de localização**).
2. Selecione **Add locale (Adicionar localidade)** e, em seguida, selecione **Default locale (Localidade padrão)** ou **Custom Attributes (Atributos personalizados)**.<br><br>![O menu suspenso "Add locale" (Adicionar localidade) com opções para selecionar a localidade padrão ou atributos personalizados.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}
3. Digite um nome para a localização.
4. Selecione as respectivas atribuições do usuário para a opção de localização escolhida.

{% tabs %}
{% tab Default locale %}

Para **Localização padrão**, use os menus suspensos para selecionar o idioma a ser adicionado e, opcionalmente, o país a ser associado ao idioma.<br><br>![Uma janela chamada "Add locale - Default Language and Country" para especificar o idioma e o país.]({% image_buster /assets/img/multi-language_support/default_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Custom attributes %}

Para **atributos personalizados**, use o menu suspenso para selecionar o atributo personalizado associado e, no campo de texto, insira o valor.<br><br>![Uma janela chamada "Add locale - Custom Attributes" (Adicionar localidade - Atributos personalizados) para especificar o atributo personalizado e o valor.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{: start="5"}
5\. Selecione **Add locale (Adicionar localização)**. 

Para obter as etapas de uso dessas localidades em suas campanhas de e-mail e no Canva, consulte [Uso de localidades]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Considerações

- Ao configurar uma localização, é possível selecionar idiomas nos atributos padrão do usuário ou nos atributos personalizados. Não é possível selecionar entre os dois.
- É possível selecionar até dois atributos personalizados em uma única localização ou até dois idiomas padrão de atributos de usuário. Em ambos os casos, o segundo atributo é opcional.
- Ao fazer edições nos valores traduzidos no arquivo CSV, evite modificar quaisquer valores padrão no arquivo.
- A chave de localização em seu arquivo feito upload deve corresponder à chave em suas configurações multilíngues.

### Suporte e priorização

- Os usuários que correspondem a um atributo personalizado de localização são priorizados antes dos usuários que correspondem a um atributo de usuário padrão.
- O suporte a atributos personalizados é limitado a tipos de string e à chave de comparação `equals`.
- Se um atributo personalizado for excluído ou seu tipo for alterado, o usuário não poderá mais se enquadrar nessa localidade e irá para a lista de prioridades de localidades em que se enquadra ou receberá traduções padrão de marketing.
- Se uma localidade for inválida (o atributo personalizado foi alterado ou excluído), o erro aparecerá na página **Suporte multilíngue**.

## Perguntas frequentes

#### Quantas localizações posso adicionar?

Você pode adicionar até 200 localidades.

#### Onde os arquivos de tradução são armazenados no Braze?

Os arquivos de tradução são armazenados no nível da campanha, o que significa que cada variante de mensagens deve ter traduções feitas upload.

#### O nome da localização precisa seguir um padrão ou formato específico?

Não. Você pode usar sua convenção de nomenclatura preferida. O nome da localização é usado ao selecionar a localização no editor e estará nos cabeçalhos do arquivo baixado com os IDs de tradução.
