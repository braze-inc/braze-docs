{% if include.alert == "Shopify deprecation" %}

{% alert important %}
Uma [nova versão da integração Shopify]({{site.baseurl}}/partners/shopify/#new-shopify-integration) será lançada em fases a partir de abril de 2025. As fases serão baseadas no tipo de loja Shopify e no ID externo usado para configurar a integração inicial. <br><br>**A versão antiga da integração não estará mais disponível após 28 de agosto de 2025. Atualize para a nova versão antes desta data para continuar usando a integração sem problemas.**
{% endalert %}

{% endif %}

{% if include.alert == 'Web push private browsing' %}

{% alert important %}
Janelas de navegação privada não suportam web push.
{% endalert %}

{% endif %}

{% if include.alert == 'BCC address billable emails' %}

{% alert important %}
Adicionar um endereço BCC à sua campanha ou Canvas resulta na duplicação dos seus e-mails faturáveis para a campanha ou componente Canvas, uma vez que a Braze envia uma mensagem para o seu usuário e uma para o seu endereço BCC.
{% endalert %}

{% endif %}

{% if include.alert == 'Android notification priority' %}

{% alert important %}
A configuração de Prioridade de Exibição de Notificações não é mais usada em dispositivos que executam Android O ou posterior. Nestes dispositivos, defina a prioridade através da [configuração do canal de notificação](https://developer.android.com/training/notify-user/channels#importance).
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
Existem certos navegadores, como os aplicativos Naver para Android e iOS, que não suportam o central de preferências da Braze. Caso preveja que alguns de seus usuários usem esses navegadores, considere fornecer métodos alternativos para que eles gerenciem suas preferências de e-mail.
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation' %}

{% alert important %}
Os planos para descontinuar o evento de compra serão anunciados em 2026. O evento de compra será eventualmente substituído por novos [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), que virão com recursos aprimorados para segmentação, relatórios, análise de dados e mais. No entanto, os novos eventos de eCommerce não suportarão recursos existentes relacionados ao evento de compra, como Valor do Tempo de Vida (LTV) ou relatórios de receita em Canvases ou campanhas. Para uma lista completa de recursos relacionados a eventos de compra, consulte [Registro de eventos de compra]({{site.baseurl}}/user_guide/data/activation/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'Purchase event deprecation for eCommerce filters' %}

{% alert important %}
Os planos para descontinuar o evento de compra serão anunciados em 2026. O evento de compra será eventualmente substituído por novos [eventos recomendados de eCommerce]({{site.baseurl}}/user_guide/data/activation/custom_data/recommended_events/ecommerce_events/), que virão com recursos aprimorados para segmentação, relatórios, análise de dados e mais. Quando isso acontecer, os filtros de segmento não serão mais preenchidos sob o comportamento de compra. Para uma lista completa de eventos de compra, consulte [Registro de eventos de compra]({{site.baseurl}}/user_guide/data/custom_data/purchase_events/#logging-purchase-events).
{% endalert %}

{% endif %}

{% if include.alert == 'S3 file bucket export' %}

{% alert important %}
Os arquivos exportados armazenados em buckets S3 são automaticamente excluídos após o link de download expirar (quatro horas a partir do envio do e-mail de exportação, a menos que indicado de outra forma).
{% endalert %} 

{% endif %}

{% if include.alert == 'Shopify customer create' %}

{% alert important %}
A integração Shopify suporta webhooks de criação e atualização de clientes Shopify, que estão localizados nas suas configurações de configuração de dados. Quando um perfil de usuário é criado ou atualizado no Shopify, um perfil de usuário correspondente na Braze será criado ou atualizado. <br><br>Essas ações não disparam eventos personalizados na Braze e são usadas exclusivamente para [sincronizar dados de usuários do Shopify com a Braze]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview/#how-the-integration-works). Os dados sincronizados incluem [atributos personalizados]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-custom-attributes), [atributos padrão]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/#supported-shopify-standard-attributes), e, se habilitado em sua configuração, [estados de grupo de inscrições]({{site.baseurl}}/partners/ecommerce/shopify/shopify_overview#syncing-shopify-email-and-sms-marketing-opt-ins).
{% endalert %}

{% endif %}

{% if include.alert == 'context variable' %}

{% alert important %}
Se você está participando do acesso antecipado do Canvas Context, as propriedades de entrada do Canvas fazem parte das variáveis de contexto do Canvas. Isso significa que `canvas_entry_properties` agora é referenciado como `context`. Cada variável de contexto inclui um nome, um tipo de dados e um valor que pode incluir Liquid. Atualmente, `canvas_entry_properties` ainda são compatíveis com versões anteriores. Para mais detalhes, veja [Context]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/context/#how-it-works) e [objeto de propriedades de entrada do Canvas]({{site.baseurl}}/api/objects_filters/canvas_entry_properties_object/).
{% endalert %}

{% endif %}

{% if include.alert == 'time filter types' %}

{% alert important %}
**Escolhendo entre os tipos de filtro "Dia do ano" e "Hora"**: Ao filtrar variáveis de contexto que contêm datas, escolha o tipo de comparação correto com base em se a data se repete a cada ano:

- **Use "Dia do ano"** quando a data se repete a cada ano (por exemplo, aniversários, datas comemorativas ou feriados como o Natal). Esse tipo de comparação calcula com base no dia do ano (1-365/366), ignorando o componente do ano.
- **Use "Hora"** quando a data for uma data absoluta que não se repete (por exemplo, datas de término de contrato, datas de compromissos ou datas de renovação de inscrição). Esse tipo de comparação calcula com base na data e hora completas, incluindo o ano.

Usar "Dia do ano" para datas absolutas pode produzir resultados incorretos ou inesperados porque o cálculo ignora o componente do ano. Por exemplo, se você estiver comparando uma data futura de término de contrato em abril para determinar se está dentro de 63 dias, usar "Dia do ano" pode corresponder incorretamente as datas porque compara apenas os números dos dias (119 vs 359) sem considerar que abril está na verdade a 188 dias de distância.

**Diretriz geral**: A data se repete a cada ano? **Sim** → Use "Dia do ano". **Não** → Use "Hora".
{% endalert %}

{% endif %}
