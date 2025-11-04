---
nav_title: Configurações em vários idiomas
article_title: Configurações em vários idiomas
alias: "/multi_language_support/"
page_order: 5.5
description: "Este artigo fornece uma visão geral das configurações de vários idiomas no painel do Braze e como usar as localidades em suas mensagens."
---

# Configurações em vários idiomas

> Ao ajustar as configurações multilíngues, você pode direcionar usuários em diferentes idiomas e locais com mensagens diferentes, tudo em uma única mensagem de e-mail.

## Pré-requisitos

Para editar e gerenciar o suporte a vários idiomas, é necessário ter a permissão de usuário "Manage Multi-Language Settings" (Gerenciar configurações de vários idiomas). Para adicionar a localidade a uma mensagem, você precisará de permissões para editar campanhas.

{% alert important %}
O suporte a vários idiomas está atualmente em acesso antecipado. Entre em contato com seu gerente de conta Braze se estiver interessado em participar desse acesso antecipado.
{% endalert %}

## Adicionar uma localidade

1. Vá para **Configurações** > **Suporte a vários idiomas** em **Configurações do espaço de trabalho**.
2. Selecione **Add locale (Adicionar localidade**) e, em seguida, selecione **Default locale (Localidade padrão** ) ou **Custom Attributes (Atributos personalizados**).<br><br>\![O menu suspenso "Add locale" (Adicionar localidade) com opções para selecionar a localidade padrão ou atributos personalizados.]({% image_buster /assets/img/multi-language_support/add_locale_options.png %}){: style="max-width:40%;"}
3. Digite um nome para a localidade.
4. Selecione os respectivos atributos de usuário para a opção de local escolhido.

{% tabs %}
{% tab Default locale %}

Em **Default locale (Localidade padrão**), use os menus suspensos para selecionar o idioma a ser adicionado e, opcionalmente, o país a ser associado ao idioma.<br><br>\![Uma janela chamada "Add locale - Default Language and Country" para especificar o idioma e o país.]({% image_buster /assets/img/multi-language_support/default_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% tab Custom attributes %}

Para **Atributos personalizados**, use o menu suspenso para selecionar o atributo personalizado associado e, no campo de texto, insira o valor.<br><br>\![Uma janela chamada "Add locale - Custom Attributes" para especificar o atributo e o valor personalizados.]({% image_buster /assets/img/multi-language_support/custom_attributes_option.png %}){: style="max-width:80%;"}

{% endtab %}
{% endtabs %}

{: start="5"}
5\. Selecione **Adicionar localidade**. 

Para saber as etapas para usar esses locais em suas campanhas de e-mail e no Canvas, consulte [Uso de locais]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/).

## Considerações

- Ao configurar uma localidade, é possível selecionar idiomas dos atributos de usuário padrão ou dos atributos personalizados. Não é possível selecionar entre os dois.
- É possível selecionar até dois atributos personalizados em uma única localidade ou até dois idiomas padrão de atributos de usuário. Em ambos os casos, o segundo atributo é opcional.
- Ao fazer edições nos valores traduzidos no arquivo CSV, evite modificar quaisquer valores padrão no arquivo.
- A chave de localidade em seu arquivo carregado deve corresponder à chave em suas configurações multilíngues.

### Suporte e priorização

- Os usuários que correspondem a um atributo personalizado de localidade são priorizados em relação aos usuários que correspondem a um atributo de usuário padrão.
- O suporte a atributos personalizados é limitado a tipos de cadeia de caracteres e à chave de comparação `equals`.
- Se um atributo personalizado for excluído ou seu tipo for alterado, o usuário não poderá mais se enquadrar nessa localidade e irá para a lista de prioridade de localidades em que se enquadra ou receberá traduções de marketing padrão.
- Se uma localidade for inválida (o atributo personalizado foi alterado ou excluído), o erro aparecerá na página **Suporte multilíngue**.

## Perguntas frequentes

#### Quantas localidades posso adicionar?

Você pode adicionar até 200 localidades.

#### Onde os arquivos de tradução são armazenados no Braze?

Os arquivos de tradução são armazenados em nível de campanha, o que significa que cada variante de mensagem deve ter traduções carregadas.

#### O nome da localidade precisa seguir um padrão ou formato específico?

Não. Você pode usar sua convenção de nomenclatura preferida. O nome da localidade é usado ao selecionar a localidade no editor e estará nos cabeçalhos do arquivo que você baixar com os IDs de tradução.

