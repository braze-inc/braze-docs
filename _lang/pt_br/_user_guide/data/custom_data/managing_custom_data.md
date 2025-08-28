---
nav_title: Gerenciando dados personalizados
article_title: Gerenciando dados personalizados
page_order: 20
page_type: reference
description: "Este artigo de referência aborda como gerenciar dados personalizados, como campanhas e segmentos pré-preenchidos ou lista de bloqueio e exclusão de dados."
---

# Gerenciamento de dados personalizados

> Esta página aborda como preencher previamente os dados personalizados em suas campanhas e segmentos, colocar na lista de bloqueio os dados que não são mais úteis e gerenciar eventos, atributos e propriedades personalizados.<br><br>Para saber como gerenciar atributos personalizados em particular, consulte [Gerenciar atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#managing-custom-attributes).

## Preenchimento prévio de dados personalizados

Pode haver ocasiões em que você queira configurar campanhas e segmentos usando dados personalizados antes que sua equipe de desenvolvimento tenha integrado esses dados personalizados. O Braze permite que você preencha previamente eventos e atributos personalizados no dashboard antes que esses dados comecem a ser rastreados, de modo que esses eventos e atributos estejam disponíveis para uso em menus suspensos e como parte do processo de criação de campanhas.

Para preencher previamente eventos e atributos personalizados, faça o seguinte:

1. Acesse **Configurações de dados** > **Eventos personalizados** ou **Atributos personalizados** ou **Produtos**.

![Navegue até Atributos personalizados, Eventos personalizados ou Produtos.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2\. Para adicionar um atributo personalizado, evento ou produto, acesse a respectiva página e selecione **Add Custom Attributes (Adicionar atributos personalizados)** ou **Add Custom Events (Adicionar eventos personalizados)** ou **Add Products (Adicionar produtos)**.<br><br>Para atributos personalizados, selecione um [tipo de dados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types) para esse atributo (por exemplo, booleano ou string). O tipo de dados de uma atribuição determinará os filtros de segmentação disponíveis para esse atributo. <br><br>![Adicionar nova atribuição ou evento]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3\. Selecione **Salvar**.

### Nomeação de eventos personalizados e atributos personalizados

Os eventos personalizados e os atributos personalizados diferenciam maiúsculas de minúsculas. Tenha isso em mente quando sua equipe de desenvolvimento integrar esses eventos ou atributos personalizados posteriormente. Eles devem nomear os eventos ou atributos personalizados exatamente como você os nomeou aqui, ou o Braze gerará um evento ou atributo personalizado diferente.

## Gerenciamento de propriedades

Depois de criar um evento personalizado ou produto, selecione **Gerenciar propriedades** desse evento ou produto para adicionar novas propriedades, colocar em lista de bloqueio as propriedades existentes e visualizar quais campanhas ou Canvas usam essa propriedade em um [evento disparado]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

![Propriedades personalizadas para um evento personalizado.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Para tornar rastreáveis esses atributos personalizados, eventos, produtos ou propriedades de eventos adicionados, é necessário pedir à equipe de desenvolvimento que os crie no SDK usando o nome exato que você usou para adicioná-los anteriormente. Ou você pode usar a [API]({{site.baseurl}}/api/basics/) do Braze para importar dados sobre essa atribuição. Depois disso, o atributo personalizado, evento ou outro será acionável e se aplicará aos seus usuários.

{% alert note %}
Todos os dados do perfil do usuário (eventos personalizados, atributos personalizados, dados personalizados) são armazenados enquanto esses perfis estiverem ativos.
{% endalert %}

## Lista de bloqueio de dados personalizados

Ocasionalmente, é possível identificar atributos personalizados, eventos personalizados ou eventos de compra que consomem muitos pontos de dados, não são mais úteis para sua estratégia de marketing ou foram registrados por engano. 

Para impedir que esses dados sejam enviados ao Braze, você pode colocar um objeto de dados personalizado em uma lista de bloqueio enquanto sua equipe de engenharia trabalha para removê-lo do backend do seu app ou site. A lista de bloqueio impede que um determinado objeto de dados personalizado seja registrado pelo Braze no futuro, o que significa que ele não será exibido ao pesquisar um usuário específico.

{% alert important %}
Para colocar dados personalizados em listas de bloqueio, é necessário ter [permissões de usuário]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#list-of-permissions) para acessar e editar campanhas, Canvas e segmentos.
{% endalert %}

Os dados incluídos na lista de bloqueio não serão enviados pelo SDK, e o dashboard da Braze não processará dados incluídos na lista de bloqueio de outras fontes (por exemplo, a API). No entanto, a lista de bloqueio não remove dados dos perfis de usuários nem diminui retroativamente a quantidade de pontos de dados incorridos para esse objeto de dados personalizado.

### Lista de bloqueio de atributos personalizados, eventos personalizados e produtos

{% alert important %}
Quando um evento ou atribuição é colocado em uma lista de bloqueio, qualquer segmento, campanha ou Canva que use esse evento ou atribuição será arquivado.
{% endalert %}

Para interromper o rastreamento de um atributo personalizado, evento ou produto específico, siga estas etapas:

1. Procure por ele nas páginas **Atributos personalizados**, **Eventos personalizados** ou **Produtos**.
2. Selecione o atributo personalizado, o evento ou o produto. Para atributos e eventos personalizados, você pode selecionar até 100 para colocar em uma lista de bloqueio por vez.
3. Selecione **Blocklist**.

![Vários atributos personalizados selecionados que estão em uma lista de bloqueio na página Atributos personalizados.]({% image_buster /assets/img_archive/blocklist_custom_attr.png %})

Você pode colocar em uma lista de bloqueio até 300 atributos personalizados e 300 eventos personalizados. Para evitar a coleta de determinadas atribuições do dispositivo, consulte nosso [guia SDK]({{site.baseurl}}/developer_guide/platform_integration_guides/sdk_primer/#blocking-data-collection). 

{% alert important %}
Atributos personalizados ou eventos personalizados com status de **Lixeira** contarão para o limite da lista de bloqueio até que sejam excluídos.
{% endalert %}

Quando um evento personalizado ou atributo é colocado em uma lista de bloqueio, aplica-se o seguinte:

- Nenhum dado enviado ao Braze será processado, e os eventos e atribuições incluídos na lista de bloqueio não contarão mais como pontos de dados
- Os dados existentes ficarão indisponíveis, a menos que sejam reativados
- Os eventos e atribuições incluídos na lista de bloqueio não serão exibidos em filtros ou gráficos
- As referências a dados da lista de bloqueio em rascunhos de telas ativas serão carregadas como valores inválidos, o que pode causar erros
- Qualquer coisa que use o evento ou atribuição da lista de bloqueio será arquivada

Para isso, a Braze envia as informações de lista de bloqueio para cada dispositivo. Isso é importante quando se pensa em colocar na lista de bloqueio um grande número de eventos e atribuições (centenas de milhares ou milhões), pois seria uma operação com uso intensivo de dados.

### Considerações sobre listas de bloqueio

É possível colocar em uma lista de bloqueio um grande número de eventos e atribuições, mas não é aconselhável. Isso ocorre porque toda vez que um evento é performado ou uma atribuição é (potencialmente) enviada ao Braze, esse evento ou atribuição precisa ser verificado em relação a toda a lista de bloqueio.

Até 300 itens são enviados ao SDK para inclusão na lista de bloqueio. Se você colocar mais de 300 itens na lista de bloqueio, esses dados serão enviados pelo SDK. Se não for necessário usar o evento ou atribuição no futuro, considere removê-lo do código do app durante a próxima versão. As alterações na lista de bloqueio podem levar alguns minutos para serem propagadas. Você pode reabilitar qualquer evento ou atribuição da lista de bloqueio a qualquer momento.

## Exclusão de dados personalizados

À medida que você cria campanhas e segmentos direcionados, pode descobrir que não precisa mais de um evento personalizado ou atributo personalizado. Por exemplo, se você usou um atributo personalizado específico como parte de uma campanha única, poderá excluir esses dados depois de [colocá-los na lista de bloqueio](#blocklisting-custom-attributes-custom-events-and-products) e remover suas referências do app. Você pode excluir qualquer tipo de dados (como strings, números e atributos personalizados aninhados).

{% alert important %}
Você deve ser um [administrador do Braze]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) para excluir dados personalizados.
{% endalert %}

Para excluir um evento personalizado ou atributo personalizado, faça o seguinte:

1. Acesse **Configurações de dados** > **Atributos personalizados** ou **Eventos personalizados**, dependendo do tipo de dados que você deseja excluir.
2. Acesse os dados personalizados e selecione <i class="fa-solid fa-ellipsis-vertical"></i> **Actions** > **Blocklist**.
3. Depois que seus dados personalizados tiverem sido colocados em uma lista de bloqueio por 7 dias, selecione <i class="fa-solid fa-ellipsis-vertical"></i> **Actions** > **Delete**.

### Como funciona a exclusão

Quando você exclui dados personalizados, ocorre o seguinte: 

- **Para atributos personalizados:** Remove permanentemente os dados de atribuição do perfil de cada usuário.
- **Para eventos personalizados:** Remove permanentemente os metadados do evento do perfil de cada usuário.

Quando um atributo ou evento é selecionado para exclusão, seu status é alterado para **Lixeira**. Nos próximos sete dias, é possível restaurar a atribuição ou o evento. Se você não restaurá-lo após sete dias, os dados serão excluídos permanentemente. Se você restaurar a atribuição ou o evento, ele voltará ao estado de lista de bloqueio.

A exclusão não impede a gravação adicional dos objetos de dados personalizados nos perfis de usuários, portanto, certifique-se de que os dados personalizados não estejam mais sendo registrados antes de excluir o evento ou atributo.

### Coisas para saber

Ao excluir dados personalizados, lembre-se dos seguintes detalhes:

* **A exclusão é permanente**. Os dados não podem ser recuperados.
* Os dados são removidos da plataforma Braze e dos perfis dos usuários.
* Você pode "reutilizar" o nome do atributo personalizado ou o nome do evento personalizado após a exclusão. Isso significa que se você notar que os dados personalizados "reaparecem" no Braze após a exclusão, isso pode ser causado por uma integração que não foi interrompida e está enviando dados com o mesmo nome de dados personalizados.
* Talvez seja necessário colocar um item na lista de bloqueio novamente se a exclusão resultar no reaparecimento de dados personalizados. O status da lista de bloqueio não é preservado porque os dados personalizados são excluídos.
* A exclusão de dados personalizados não consome nenhum [ponto de dados]({{site.baseurl}}/user_guide/data/data_points) e também não gera novos pontos de dados para uso.

## Forçar comparações de tipos de dados

A Braze reconhece automaticamente os tipos de dados para os dados de atribuição que nos são enviados. No entanto, caso vários tipos de dados sejam aplicados a uma única atribuição, é possível forçar o tipo de dados de qualquer atributo para que saibamos o que ele é. Selecione na lista suspensa da coluna **Data Type (Tipo de dados)**.

{% alert note %}
Forçar tipos de dados não se aplica a propriedades de eventos ou propriedades de compra.
{% endalert %}

![Menu suspenso do tipo de dados de atributos personalizados]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Se você optar por forçar o tipo de dados de uma atribuição, todos os dados recebidos que não forem do tipo especificado serão coagidos a esse tipo. Se essa coerção for impossível (por exemplo, uma string contendo letras sendo coerciva em um número), os dados serão ignorados. Todos os dados ingeridos antes da alteração do tipo continuarão a ser armazenados como o tipo antigo (e, portanto, podem não ser segmentáveis), e um aviso aparecerá ao lado da atribuição nos perfis dos usuários afetados.
{% endalert %}

### Coerção de tipos de dados

| Tipo de dados forçado | Descrição |
|------------------|-------------|
| Booleano | As entradas de `1`, `true`, `t` (não diferenciam maiúsculas de minúsculas) serão armazenadas como `true` |
| Booleano | As entradas de `0`, `false`, `f` (não diferenciam maiúsculas de minúsculas) serão armazenadas como `false` |
| Número | Os números inteiros ou flutuantes (como `1`, `1.5`) serão armazenados como números |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Para saber mais sobre as opções de filtro específicas expostas por diferentes comparações de tipos de dados, consulte [Configuração de relatórios]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting). Para saber mais sobre os diferentes tipos de dados disponíveis, consulte [Tipos de dados de atributos personalizados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types).

{% alert note %}
Os dados enviados ao Braze são imutáveis e não podem ser excluídos ou modificados depois que os recebemos. No entanto, é possível usar qualquer uma das etapas listadas nas seções anteriores para exercer controle sobre o que está sendo rastreado no dashboard.
{% endalert %}


