---
nav_title: Conectar fontes de dados
article_title: Conectar fontes de dados
page_order: 1
description: "Aprenda como conectar fontes de dados de clientes ao BrazeAI Decisioning Studio Pro para decisões personalizadas de IA."
---

# Conectar fontes de dados

> Os agentes do BrazeAI Decisioning Studio™ Pro precisam entender completamente o contexto do cliente para tomar decisões eficazes. Este artigo explica como conectar fontes de dados de clientes ao Decisioning Studio Pro.

{% alert tip %}
Sua equipe de Serviços de Decisão de IA irá apoiá-lo na configuração de conexões de dados para desempenho ideal.
{% endalert %}

## Padrões de integração suportados

O Decisioning Studio Pro suporta múltiplos padrões de integração para conectar dados de clientes:

| Padrão de integração | Melhor para | Complexidade de configuração |
|---------------------|----------|------------------|
| **Plataforma de dados Braze** | Clientes que já usam Braze | Baixa |
| **Braze Cloud Data Ingestion (CDI)** | Conectando armazéns de dados externos | Média |
| **Cloud Storage (GCS, AWS, Azure)** | Exportações diretas de dados de outras plataformas | Média |
| **Integrações de CEP** | Extensões de dados SFMC, Klaviyo | Média |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Tipos de dados de clientes

Os seguintes ativos de dados de clientes ajudam os agentes a personalizar de forma mais eficaz:

| Tipo de dados | Descrição | Exemplos |
|-----------|-------------|----------|
| **Perfil do cliente** | Atributos estáticos e que mudam lentamente | Anos como cliente, geografia, canal de aquisição, nível de satisfação, estimativa de valor do tempo de vida |
| **Comportamento do cliente** | Padrões de atividade e engajamento | Logins de conta, tipo de dispositivo, interações com o serviço ao cliente, uso de produtos |
| **Histórico de transações** | Dados de compra e conversão | Produtos comprados, valores de transação, métodos de pagamento, canais de compra |
| **Engajamento de marketing** | Respostas a comunicações | Aberturas/cliques de e-mail, engajamento por SMS, atividade na web e móvel, respostas a pesquisas |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

{% alert tip %}
Quanto mais informações os agentes tiverem sobre seus clientes, melhor será seu desempenho. Considere incluir dados sobre quaisquer insights que sejam particularmente importantes para o seu negócio (por exemplo, você quer ver como a IA trata seus clientes fiéis de forma diferente?) Certifique-se de que o status de fidelidade esteja nos dados do cliente).
{% endalert %}

## Conectando dados por plataforma

{% tabs %}
{% tab Braze %}

### Envie dados do cliente através do Braze

O BrazeAI Decisioning Studio pode usar todos os dados que você já está enviando para a Braze Data Platform.

Se houver dados do cliente que você deseja usar para o Decisioning Studio que não estão atualmente armazenados no perfil do usuário ou em atributos personalizados, a abordagem recomendada é usar [Ingestão de Dados da Nuvem Braze]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion) para ingerir dados de outras fontes.

O CDI suporta integrações diretas com:

- Snowflake
- Redshift
- BigQuery
- Databricks
- Microsoft Fabric
- AWS S3

Para a lista completa de fontes suportadas, veja [Ingestão de Dados na Nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion).

Uma vez que você esteja satisfeito com os dados que está enviando para a Braze Data Platform, entre em contato com sua equipe de Serviços de Decisão de IA para discutir quais campos no perfil do usuário ou atributos personalizados devem ser usados para Decisão de IA.

Para agilizar esse processo, crie uma lista de atributos do perfil de usuário da Braze que você acha que melhor representam os comportamentos de seus clientes que devem ser usados no Decisioning Studio (veja a [lista de campos disponíveis]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/#fields-to-export)). Sua equipe de serviços também pode ajudá-lo a conduzir sessões de descoberta para decidir quais campos são mais apropriados para Decisão de IA.

Outras opções para enviar dados incluem:

- Enviar eventos personalizados da Braze via SDK
- Enviar eventos usando o endpoint REST ([`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track))

Esses padrões exigem mais esforço de engenharia, mas às vezes são preferíveis dependendo da sua configuração atual da Braze. Entre em contato com a equipe de Serviços de Decisão de IA para saber mais.

{% endtab %}
{% tab SFMC %}

### Envie dados de cliente através do SFMC

Para integrações com o Salesforce Marketing Cloud:

1. Configure a(s) Extensão(ões) de Dados do SFMC para seus dados de cliente
2. Configure o Pacote Instalado do SFMC para integração de API com as permissões apropriadas exigidas pelo Decisioning Studio
3. Certifique-se de que as extensões de dados sejam atualizadas diariamente, pois o Decisioning Studio puxará os dados incrementais mais recentes disponíveis

Forneça o ID da extensão e a chave de API para sua equipe de Serviços de Decisão de IA. Eles ajudarão com os próximos passos na ingestão de dados de cliente.

{% endtab %}
{% tab Klaviyo %}

### Envie dados de cliente através do Klaviyo

Para integrações com o Klaviyo:

1. Confirme que os dados do perfil do cliente estão disponíveis nos perfis do Klaviyo.
2. Gere uma chave de API privada com Acesso Total a Perfis
3. Forneça a chave de API para sua equipe de Serviços de Decisão de IA

Veja a [documentação do Klaviyo](https://help.klaviyo.com/hc/en-us/articles/115005237908) para mais informações sobre a configuração da chave de API.

{% endtab %}
{% tab Cloud Storage %}

### Outras soluções em nuvem (Google Cloud Storage, Azure, AWS)

Se os dados do cliente não estiverem atualmente armazenados no Braze, SFMC ou Klaviyo, o próximo melhor passo é configurar uma exportação automatizada diretamente para um bucket do Google Cloud Storage controlado pelo Braze. Também podemos suportar exportação para AWS ou Azure (embora o GCS seja preferível). Para essas plataformas, exporte para o armazenamento em nuvem interno dessas plataformas em nuvem e o Braze pode então puxar esses dados.

Para determinar se isso é viável, consulte a documentação da sua plataforma de MarTech. Por exemplo:

- mParticle oferece uma [integração nativa com o Google Cloud Storage](https://www.mparticle.com/integration/google-cloud-storage/)
- [Twilio Segment](https://www.twilio.com/docs/segment/connections/storage/catalog/google-cloud-storage)
- [Treasure Data](https://docs.treasuredata.com/int/google-cloud-storage-export-integration)
- [ActionIQ](https://info.actioniq.com/hubfs/ActionIQ%20Industry%20Brief%20Solutions/ActionIQ_Integrations_Brief.pdf)
- [Adobe Experience Platform](https://experienceleague.adobe.com/en/docs/experience-platform/destinations/catalog/cloud-storage/google-cloud-storage)

Se isso for viável, podemos fornecer um bucket GCS para exportar dados de clientes que seja isolado ao Decisioning Studio.

{% endtab %}
{% endtabs %}

## Melhores práticas

- **Nomes de colunas descritivos**: Os dados do cliente devem ter nomes de colunas claros e descritivos. Idealmente, um dicionário de dados deve ser fornecido.
- **Atualizações incrementais**: Arquivos incrementais são preferíveis em vez de instantâneas de todo o histórico do cliente a cada dia
- **Identificadores consistentes**: Cada registro deve conter um identificador de cliente único que seja consistente em todos os ativos de dados
- **Incluir timestamps**: Os registros devem ter timestamps associados para atribuição precisa e treinamento de agentes

## Integrações personalizadas

Outras opções ou pipelines de dados completamente personalizados são possíveis. Esses podem exigir trabalho adicional de Serviços ou Engenharia da sua equipe. Para determinar o que é viável e ótimo, trabalhe com sua equipe de Serviços de Decisão de IA.

{% alert important %}
Este guia explica os padrões de integração mais comuns. A Segurança da Informação ainda precisará avaliar todos os pontos de conexão e Consultores de Soluções estarão disponíveis para aconselhar sobre a implementação.
{% endalert %}

## Próximos passos

Após conectar suas fontes de dados, prossiga para configurar a orquestração:

- [Configurar orquestração]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

