{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Uma [nova versão da integração com o Shopify]({{site.baseurl}}/partners/shopify/#new-shopify-integration) será lançada em fases a partir de abril de 2025. As fases serão baseadas no tipo de loja Shopify e no ID externo usado para configurar a integração inicial. <br><br>**A versão antiga da integração não estará mais disponível após 28 de agosto de 2025. Atualize para a nova versão antes dessa data para continuar usando a integração sem problemas.**
{% endalert %}

{% endif %}

{% if include.alert == "Email via SMS" %}

{% alert important %}
Não envie e-mails de transação legalmente exigidos para gateways de SMS, pois há uma grande probabilidade de que esses e-mails não sejam entregues.
<br><br>
Embora os e-mails que você envia usando um número de telefone e o domínio de gateway do provedor (conhecido como MM3) possam resultar no recebimento do e-mail como uma mensagem SMS (texto), alguns de nossos provedores de e-mail não suportam esse comportamento. Por exemplo, se você enviar um e-mail para um número de telefone da T-Mobile (como "9999999999@tmomail.net"), sua mensagem SMS será enviada para o proprietário desse número de telefone na rede T-Mobile.
<br><br>
Lembre-se de que, embora esses e-mails possam não ser entregues ao gateway de SMS, eles ainda contarão para o envio de e-mail. Para evitar o envio de e-mails para gateways sem suporte, consulte a [lista de nomes de domínio de gateway sem suporte](https://www.fcc.gov/consumer-governmental-affairs/about-bureau/consumer-policy-division/can-spam/domain-name-downloads).
{% endalert %}

{% endif %}

{% if include.alert == 'SDK auth' %}

{% alert important %}
Para maior segurança, recomendamos adicionar nosso recurso de [autenticação do SDK]({{site.baseurl}}/developer_guide/authentication/) para evitar a simulação do usuário.
{% endalert %}

{% endif %}

{% if include.alert == 'Preference Center warning' %}

{% alert important %}
Há determinados navegadores, como os apps Naver para Android e iOS, que não são compatíveis com a Central de Preferências Braze. Caso preveja que alguns de seus usuários usem esses navegadores, considere fornecer métodos alternativos para que eles gerenciem suas preferências de e-mail.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
Os planos para eliminar gradualmente o evento de compra serão anunciados no final de 2025. A longo prazo, o evento de compra será substituído por novos [eventos recomendados de comércio eletrônico]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), que virão com recursos aprimorados de segmentação, relatórios, análise de dados e muito mais. No entanto, os novos eventos de comércio eletrônico não serão compatíveis com os recursos existentes relacionados ao evento de compra, como o valor do tempo de vida (LTV) ou relatórios de receita em telas ou campanhas. Para obter uma lista completa de recursos relacionados a eventos de compra, consulte [Registro de eventos de compra]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Os arquivos de exportação armazenados em buckets S3 são automaticamente excluídos depois que o link de download expira (quatro horas a partir do envio do e-mail de exportação, salvo nota em contrário).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
A integração do Shopify é compatível com os webhooks de criação e atualização de clientes do Shopify, que estão localizados em suas definições de configuração de dados. Quando um perfil de usuário é criado ou atualizado no Shopify, um perfil de usuário correspondente no Braze será criado ou atualizado. <br><br>Essas ações não disparam eventos personalizados no Braze e são usadas apenas para [sincronizar os dados de usuários do Shopify com o Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). Os dados sincronizados incluem [atributos personalizados]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [atributos padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes) e, se ativados em sua configuração, [estados do grupo de inscrições]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Se estiver participando do acesso antecipado ao Canvas Context, as propriedades de entrada do Canvas fazem parte das variáveis de contexto do Canvas. Isso significa que `canvas_entry_properties` agora é referenciado como `context`. Cada variável de contexto inclui um nome, um tipo de dados e um valor que pode incluir Liquid. Atualmente, o site `canvas_entry_properties` ainda é compatível com versões anteriores. Para obter mais detalhes, consulte [Contexto]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) e [objeto de contexto da tela]({{site.baseurl}}/api/objects_filters/context_object).
{% endalert %}

{% endif %}