---
nav_title: Sincronização de coleções do Shopify
article_title: Sincronização de coleções do Shopify
permalink: "/shopify_collections_sync/"
description: "Este artigo de referência aborda como configurar a sincronização de coleções do Shopify, que permite agrupar seus produtos em coleções para que os clientes possam encontrar seus produtos por categoria."
hidden: true
---

# Sincronização beta de coleções da Shopify

> A sincronização de coleções do Shopify permite que você agrupe seus produtos em coleções para que os clientes possam encontrar seus produtos por categoria. Para que a experiência do comprador seja mais perfeita, você pode incorporar itens das coleções da sua loja no envio de mensagens do Braze.

{% alert important %}
A sincronização de coleções da Shopify está na versão beta. Entre em contato com o gerente da sua conta Braze se quiser participar da versão beta.
{% endalert %}

## Configuração da sincronização de coleções da Shopify

Para sincronizar seus produtos de sua loja Shopify com o Braze, marque a caixa de seleção **Sincronizar coleções do Shopify** na etapa **Sincronizar produtos** da [integração do Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify#setting-up-shopify-in-braze).<br><br>![Etapa 4 da sincronização de produtos da Shopify com a caixa de seleção "Sincronizar coleções da Shopify" marcada.][1]

Depois que seus produtos forem sincronizados, você poderá ver quais produtos estão associados às suas coleções, visualizando seu catálogo da Shopify. <br><br>![Linha da tabela de catálogo mostrando um produto nas coleções de "best-sellers" e "frontpage".][2]

Em seu catálogo da Shopify, você pode visualizar sua coleção da Shopify na guia **Seleções**. <br><br>![A guia Seleções mostra uma lista com duas coleções: "best-sellers" e "frontpage".][3]

### Funcionalidade beta

- O Braze oferecerá suporte a até 30 coleções
- A ordem de classificação da sua coleção não é mantida nem aceita no momento. Por enquanto, a ordem de classificação é baseada no seguinte:
    - Os itens mais recentes adicionados à sua coleção.
    - A ordem em que os itens são atualizados durante as sincronizações contínuas.
    - A ordem que você seleciona na guia de seleção da sua coleção da Shopify.

## Usando coleções da Shopify

Use suas coleções do Shopify para personalizar uma mensagem para cada usuário em sua campanha, da mesma forma que usaria uma [seleção do Braze]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/catalogs/selections/).

{% alert warning %}
Esteja ciente do seguinte comportamento na versão beta: <br><br>Se você atualizar a descrição da coleção do Shopify ou as configurações de filtro, você interromperá a sincronização da coleção do Shopify. Como resultado, sua coleção da Shopify não funcionará como esperado.
{% endalert %}

### Etapa 1: Configure a ordem de classificação de sua coleção da Shopify

1. Especifique a ordem em que os resultados de sua coleção do Shopify são retornados selecionando a **Ordem de classificação** na guia de seleção de sua coleção do Shopify. Isso inclui uma opção para randomizar a ordem de classificação.
2. Digite o número máximo de resultados (até 50) em **Limitar número**.
3. Selecione **Atualizar seleção**.

![A página Edit Selection (Editar seleção), na qual você pode selecionar as configurações de filtro, o tipo de classificação e o limite de resultados.][4]

### Etapa 2: Use a coleção em uma campanha

1. Crie uma campanha e selecione **\+ Personalização** no criador de mensagens.
2. Selecione o seguinte:<br>- **Itens de catálogo** como o **tipo de personalização**<br>\- O nome do catálogo<br>\- O método de seleção de itens<br>\- O nome da seleção (o nome de sua coleção da Shopify) <br>\- As informações a serem exibidas em sua mensagem

{: start="3"}
3\. Copie e cole o snippet do Liquid onde deseja que as informações apareçam em sua mensagem.

![A seção "Add Personalization" (Adicionar personalização) contém campos para selecionar o catálogo, o método de seleção de itens e as informações a serem exibidas.][5]{: style="max-width:30%;"}

#### Liquid nos resultados da seleção

O uso de quaisquer resultados em catálogos, como atributos personalizados e eventos personalizados, pode fazer com que resultados diferentes sejam retornados para cada usuário em sua seleção.

[1]: {% image_buster /assets/img/Shopify/sync_products.png %}
[2]: {% image_buster /assets/img/Shopify/view_catalog.png %}
[3]: {% image_buster /assets/img/Shopify/selections_tab.png %}
[4]: {% image_buster /assets/img/Shopify/edit_selection.png %}
[5]: {% image_buster /assets/img/Shopify/add_personalization.png %}
