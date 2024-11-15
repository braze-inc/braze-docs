---
nav_title: Suporte a múltiplas lojas
permalink: "/shopify_multiple_store/"
hidden: true
---

# Suporte a múltiplas lojas da Shopify

> Conecte várias lojas Shopify a um único espaço de trabalho com nossa nova versão beta para suporte a várias lojas, para ter uma visão holística de seus clientes em todos os mercados. Crie e inicie programas e jornadas de automação em um único espaço de trabalho sem duplicar esforços em várias instâncias. 

{% alert important %}
O suporte para múltiplas lojas Shopify está disponível na versão beta, que pode conter bugs. Esse recurso está sujeito a alterações à medida que o desenvolvimento continua.
{% endalert %}

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Criar [grupo de inscrições para e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/managing_user_subscriptions#create-a-group) para cada loja | Depois que o grupo de inscrições para e-mail for criado, você o designará para a loja específica durante a etapa "[Coletar envios de e-mail ou SMS]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/#step-5-collect-email-or-sms-subscribers)" do fluxo de configuração.<br><br>Isso é necessário para rastrear a qual grupo de inscrições para e-mail da loja seus usuários pertencem para fins de conformidade. |
| Auditar e atualizar segmentos, campanhas e Canvas usando atribuições do Shopify | Os atributos personalizados coletados de várias lojas estarão no formato de um objeto aninhado, o que difere da estrutura atual usada na integração geral do Shopify, que é formatada como um valor de string. Como resultado, você precisará atualizar todos os segmentos, campanhas ou Canvas para o novo formato depois de conectar várias lojas para usar o filtro "Atributo personalizado aninhado" ou atualizar o evento de gatilho "Alterar atributo personalizado".<br><br>Se não estiver usando nenhum dos atributos hoje, pode ignorar isso. |
| Auditar e atualizar o alias do Shopify | O alias `shopify_customer_id` será migrado para {% raw %}`shopify_customer_id_{{storename}}`{% endraw %} depois que você conectar mais de uma loja. Atualize todos os sistemas internos para usar o novo alias. O alias legado, `shopify_customer_id`, será preterido. Se você não estiver usando o alias hoje, pode ignorar isso. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Integração
Com o suporte da Braze para múltiplas lojas, você pode:
- Tenha uma visão de 360° de seus clientes em todas as lojas
- Crie segmentos de seus clientes com dados agregados da loja 
- Configure envios de mensagens ou jornadas à medida que seus clientes passam por diferentes lojas
- Gerenciar inscrições de e-mail e SMS em diferentes lojas

{% alert important %}
Apoiar várias marcas em um único espaço de trabalho aumenta a probabilidade de perfis de usuário duplicados, pois os usuários podem comprar entre essas marcas. Sugerimos colocar cada marca em seu próprio espaço de trabalho.
{% endalert %}

### Configuração de uma loja adicional
1. Após instalar sua primeira loja, selecione a opção **\+ Conectar Nova Loja**.<br>![][1]{: style="max-width:70%;"}<br><br>
2. Passe pelo processo de integração para esta nova loja. Mais detalhes podem ser encontrados em nosso guia [Configurando a Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/setting_up_shopify/).<br><br>Note que as configurações da loja anterior podem ser transferidas, mas você pode atualizar as configurações de acordo com o progresso da integração.<br><br>
3. Para a etapa de coleta de assinantes de e-mail ou SMS:
- Para coletar adequadamente as inscrições de e-mail e SMS para cada loja, é necessário atribuir grupos de inscrições exclusivos a cada configuração de loja. 
- Sugerimos que **não** ative a opção "Override existing global state for users" (Substituir estado global existente para usuários), pois isso pode cancelar globalmente a inscrição de seus clientes se eles interagirem com mais de uma de suas lojas.<br><br>
4. Repita essa instalação para quantas lojas forem necessárias.<br><br>
5. Para visualizar a integração de cada loja e configurar as configurações avançadas, clique em uma loja no menu suspenso:<br>![][2]{: style="max-width:70%;"}

## Dados da Shopify

### Alias do Shopify

{% raw %}Depois de conectar mais de uma loja, todos os usuários do Shopify que chegarem terão um novo alias, `shopify_customer_id_{{storename}}`, além do alias existente, `shopify_customer_id`. Observe que o `shopify_customer_id` é um alias legado e será descontinuado quando esse recurso estiver disponível de forma geral. Você deve passar a usar o novo alias daqui para frente. {% endraw %}

### Atributos personalizados da Shopify

Depois que você conectar mais de uma loja, as seguintes atribuições serão sincronizadas como um objeto aninhado que contém o valor por loja e o valor agregado:
- `shopify_tags`
- `shopify_order_count` (disponível apenas por meio do preenchimento de dados históricos)
- `shopify_total_spent` (disponível apenas por meio do preenchimento de dados históricos)

Para usar eventos personalizados ao criar ou editar um segmento, selecione o filtro **Atributo personalizado aninhado** e localize o atributo aninhado. Para obter ajuda para identificar o caminho ou o campo específico no objeto, use a ferramenta [Gerar esquema]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support#generate-schema). Depois de selecionar as atribuições aninhadas, um campo com um botão de adição aparecerá ao lado dos atributos selecionados para que você especifique a jornada. Para saber mais sobre atributos aninhados, consulte [Atributos personalizados aninhados]({{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_attributes/nested_custom_attribute_support/).

![3]{:style="max-width:70%;"}

Você pode especificar seu caminho digitando-o no campo ou clicando no botão de adição e selecionando o caminho.

![4]{:style="max-width:70%;"}

### Eventos personalizados da Shopify

Depois que você conectar mais de uma loja, os eventos personalizados do Shopify agora conterão uma nova propriedade de evento, `shopify_storefront`. Consulte o [processamento de dados do Shopify]({{site.baseurl}}/partners/message_orchestration/channel_extensions/ecommerce/shopify/shopify_data_processing#supported-shopify-events) para ver todos os eventos personalizados compatíveis com essa integração. Essa propriedade de evento fornece o domínio da loja Shopify de onde o evento está vindo.

### Entrega baseada em ação ou rastreamento de conversão

Para disparar envios de mensagens aos usuários que concluírem ações em uma loja específica:

1. Navegue até a etapa **Schedule Delivery (Agendar entrega)** de sua campanha.
2. Selecione **Perform Custom Event (Executar evento personalizado** ) como um evento de gatilho.
![5]{:style="max-width:70%;"}
3. Selecione um evento do Shopify como o evento de gatilho, como **shopify_created_order**, e a caixa de seleção **Adicionar filtros de propriedade**.
![6]{:style="max-width:70%;"}
4. Selecione **Propriedade básica** no menu suspenso **Adicionar filtro**.
5. Selecione **shopify_storefront** e insira o domínio completo do Shopify da loja.
![7]{:style="max-width:70%;"}


### Fusão e sincronização de usuários do Shopify

Se o ID do cliente Shopify, o endereço de e-mail ou o número de telefone do usuário já existirem no Braze usando o alias {% raw %}`shopify_customer_id_{{storefront_domain}}`, `shopify_email` ou `shopify_phone`, {% endraw %}, atualizaremos o perfil de usuário existente. Se esses aliases não existirem na Braze, criaremos um novo perfil de usuário. Note que é possível que os dados de um usuário (por exemplo, cidade) sejam diferentes em várias lojas da Shopify para o mesmo usuário. Nesses casos, o Braze sempre atualizará o perfil do usuário da loja com a atividade mais recente. 

{% alert warning %}
O Braze atualizará o perfil do usuário com os dados de clientes do Shopify da loja com a atividade mais recente. Isso significa que quaisquer atribuições, como e-mail, número de telefone, telefone de envio, cidade etc., podem ser substituídas pela atividade mais recente da loja. Por exemplo, se um usuário tiver um número de telefone diferente em duas lojas diferentes, o Braze atualizará o perfil do usuário com o número de telefone da loja com a atividade mais recente.
{% endalert %}

[1]: {% image_buster /assets/img/multiple_stores.png %}
[2]: {% image_buster /assets/img/multiple_stores2.png %}
[3]: {% image_buster /assets/img/shopify_nested_attributes.png %}
[4]: {% image_buster /assets/img/shopify_tags.png %}
[5]: {% image_buster /assets/img/shopify_add_trigger.png %}
[6]: {% image_buster /assets/img/shopify_select_event.png %}
[7]: {% image_buster /assets/img/shopify_enter_storefront.png %}
