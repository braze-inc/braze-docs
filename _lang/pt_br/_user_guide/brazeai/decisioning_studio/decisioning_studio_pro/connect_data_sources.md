---
nav_title: Conectar fontes de dados
article_title: Conectar fontes de dados
page_order: 1
description: "Saiba como conectar fontes de dados de clientes ao BrazeAI Decisioning Studio Pro para tomar decisões de IA personalizadas."
---

# Conectar fontes de dados

> Os agentes do BrazeAI Decisioning Studio™ Pro precisam entender completamente o contexto do cliente para tomar decisões eficazes. Este artigo explica como conectar fontes de dados de clientes ao Decisioning Studio Pro.

{% alert tip %}
A equipe do IA Decisioning Services o ajudará a configurar as conexões de dados para obter a performance ideal.
{% endalert %}

## Padrões de integração suportados

O Decisioning Studio Pro suporta vários padrões de integração para conectar dados de clientes:

| Padrão de integração | Melhor para | Complexidade da configuração |
|---------------------|----------|------------------|
| **Plataforma de dados da Braze** | Clientes que já estão usando o Braze | Baixa |
| **Ingestão de dados na nuvem (CDI) do Braze** | Conexão de data warehouses externos | Média |
| **Armazenamento em nuvem (GCS, AWS, Azure)** | Exportação direta de dados de outras plataformas | Média |
| **Integrações de CEP** | SFMC, extensões de dados do Klaviyo | Média |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Tipos de dados de clientes

Os seguintes dados de clientes ativos ajudam os agentes a personalizar de forma mais eficaz:

| Tipo de dados | Descrição | Exemplos |
|-----------|-------------|----------|
| **Perfil do cliente** | Atribuições estáticas e que mudam lentamente | Anos como cliente, geografia, canal de aquisição, nível de satisfação, estimativa do valor do tempo de vida |
| **Comportamento do cliente** | Padrões de atividade e engajamento | Logins de conta, tipo de dispositivo, interações com o serviço de atendimento ao cliente, uso do produto |
| **Histórico de transações** | Dados de compra e conversão | Produtos comprados, valores das transações, métodos de pagamento, canais de compra |
| **Engajamento de marketing** | Respostas às comunicações | Aberturas/cliques de e-mail, engajamento com SMS, atividade na Web e em dispositivos móveis, respostas a pesquisas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
Quanto mais informações os agentes tiverem sobre seus clientes, melhor será a performance deles. Considere incluir dados sobre quaisquer insights que sejam particularmente importantes para sua empresa (por exemplo, você quer ver como a IA trata seus clientes de fidelidade de forma diferente? Certifique-se de que o status de fidelidade esteja nos dados do cliente).
{% endalert %}

## Conexão de dados por plataforma

{% tabs %}
{% tab Braze %}

### Enviar dados de clientes pelo Braze

O BrazeAI Decisioning Studio pode usar todos os dados que você já está enviando para a Braze Data Platform.

Se houver dados de clientes que você deseja usar no Decisioning Studio que não estejam armazenados no perfil do usuário ou nos atributos personalizados, a abordagem recomendada é usar o [Braze Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) para ingerir dados de outras fontes.

O CDI oferece suporte a integrações diretas com:

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Para obter a lista completa de fontes compatíveis, consulte [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Quando estiver satisfeito com os dados que está enviando para a plataforma de dados do Braze, entre em contato com a equipe de serviços de decisão de IA para discutir quais campos do perfil do usuário ou atributos personalizados devem ser usados para a decisão de IA.

Para agilizar esse processo, crie uma lista de atributos do perfil de usuário do Braze que, em sua opinião, melhor representam os comportamentos de seus clientes e que devem ser usados no Decisioning Studio (consulte a [lista de campos disponíveis]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Sua equipe de serviços também pode ajudá-lo a realizar sessões de descoberta para decidir quais campos são mais apropriados para o IA Decisioning.

Outras opções para o envio de dados incluem:

- Envio de eventos personalizados do Braze por meio do SDK
- O envio de eventos usando o ponto de extremidade REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Esses padrões exigem mais esforço de engenharia, mas às vezes são preferíveis, dependendo de sua configuração atual do Braze. Entre em contato com a equipe do IA Decisioning Services para saber mais.

{% endtab %}
{% tab SFMC %}

### Enviar dados de clientes através do SFMC

Para integrações com o Salesforce Marketing Cloud:

1. Configure a(s) extensão(ões) de dados SFMC para seus dados de cliente
2. Configure o SFMC Installed Package para a integração da API com as permissões apropriadas exigidas pelo Decisioning Studio
3. Certifique-se de que as extensões de dados sejam atualizadas diariamente, pois o Decisioning Studio extrairá os dados incrementais mais recentes disponíveis

Forneça o ID da extensão e a chave de API à sua equipe de IA Decisioning Services. Eles ajudarão nas próximas etapas da ingestão de dados de clientes.

{% endtab %}
{% tab Klaviyo %}

### Enviar dados de clientes por meio da Klaviyo

Para integrações do Klaviyo:

1. Confirmar se os dados do perfil do cliente estão disponíveis nos perfis da Klaviyo
2. Gerar uma chave de API privada com acesso completo aos perfis
3. Forneça a chave de API à sua equipe de IA Decisioning Services

Consulte a [documentação do Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para obter mais informações sobre a configuração da chave de API.

{% endtab %}
{% tab Cloud Storage %}

### Outras soluções de nuvem (Google Cloud Storage, Azure, AWS)

Se os dados do cliente não estiverem armazenados no Braze, SFMC ou Klaviyo, a próxima melhor etapa é configurar uma exportação automatizada diretamente para um bucket do Google Cloud Storage controlado pelo Braze. Também podemos oferecer suporte à exportação para o AWS ou o Azure (embora seja preferível o GCS). Para essas plataformas, exporte para o armazenamento interno em nuvem nessas plataformas e o Braze poderá extrair esses dados.

Para determinar se isso é viável, consulte a documentação de sua plataforma MarTech. Por exemplo:

- O mParticle oferece uma [integração nativa com o Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Plataforma de experiência da Adobe](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Se isso for viável, podemos fornecer um bucket do GCS para exportar dados de clientes isolados para o Decisioning Studio.

{% endtab %}
{% endtabs %}

## Melhores práticas

- **Nomes descritivos de colunas**: Os dados de clientes devem ter nomes de colunas claros e descritivos. O ideal é que seja fornecido um dicionário de dados.
- **Atualizações incrementais**: Arquivos incrementais são preferíveis a instantâneos de todo o histórico do cliente todos os dias
- **Identificadores consistentes**: Cada registro deve conter um identificador de cliente exclusivo que seja consistente em todos os dados de ativos
- **Incluir registros de data e hora**: Os registros devem ter carimbos de data e hora associados para atribuição precisa e treinamento de agentes

## Integrações personalizadas

Outras opções ou pipelines de dados totalmente personalizados são possíveis. Isso pode exigir trabalho adicional de serviços ou de engenharia de sua equipe. Para determinar o que é viável e ideal, trabalhe com a equipe do IA Decisioning Services.

{% alert important %}
Este guia explica os padrões de integração mais comuns. A Segurança da Informação ainda precisará examinar todos os pontos de conexão, e os Consultores de Soluções estarão disponíveis para orientar sobre a implementação.
{% endalert %}

## Próximos passos

Depois de conectar suas fontes de dados, prossiga para configurar a orquestração:

- [Configurar a orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

