---
nav_title: Armazenamento de Blobs do Microsoft Azure
article_title: Armazenamento de Blobs do Microsoft Azure
alias: /partners/microsoft_azure_blob_storage_for_currents/
description: "Este artigo de referência descreve a parceria entre o Braze Currents e o Microsoft Azure Blog Storage, um armazenamento de objetos massivamente escalável para dados não estruturados."
page_type: partner
tool: Currents
search_tag: Partner

---

# Armazenamento de Blobs do Microsoft Azure

> [O Microsoft Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/) é um armazenamento de objetos massivamente escalável para dados não estruturados oferecido pela Microsoft como parte do conjunto de produtos Azure.

{% alert important %}
Se estiver alternando entre provedores de armazenamento em nuvem, entre em contato com o gerente de sucesso do cliente do Braze para obter mais assistência na configuração e validação da nova integração.
{% endalert %}

A integração da Braze e do Microsoft Azure Blob Storage permite exportar dados de volta para o Azure e enviar dados do Currents. Mais tarde, você pode usar um processo ETL (Extract, Transform, Load) para transferir seus dados para outros locais.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Microsoft Azure e conta de armazenamento do Azure | Uma conta de armazenamento Microsoft Azure e Azure é necessária para usar esta parceria. |
| Currents | Para exportar dados para o Currents, você deve ter o [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configurado na sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Para integrar com o Microsoft Azure Blob Storage, você deve ter uma conta de armazenamento e uma string de conexão para permitir que a Braze exporte dados de volta para o Azure ou envie dados do Currents.

### Etapa 1: Criar uma conta de armazenamento

No Microsoft Azure, navegue até **Contas de Armazenamento** na barra lateral e clique em **\+ Adicionar** para criar uma nova conta de armazenamento. Em seguida, forneça um nome de conta de armazenamento. Outras configurações padrão não precisarão ser atualizadas. Por fim, selecione **Revisar + criar**. 

Mesmo que você já tenha uma conta de armazenamento, recomendamos criar uma nova especificamente para seus dados do Braze.

![]({% image_buster /assets/img/azure-currents-step-1.png %})

### Etapa 2: Obtenha a string de conexão

Depois que a conta de armazenamento for implantada, navegue até o menu **Chaves de Acesso** da conta de armazenamento e tome nota da string de conexão.

A Microsoft fornece duas chaves de acesso para manter as conexões usando uma chave enquanto recria a outra. Você só precisa da string de conexão de um deles.

{% alert note %}
A Braze usa a string de conexão deste menu, não a chave.
{% endalert %}

![]({% image_buster /assets/img/azure-currents-step-2.png %})

### Etapa 3: Criar um contêiner de serviço de blob

Navegue até o menu **Blobs** na seção **Blob Service** da sua conta de armazenamento. Crie um contêiner de Blob Service na conta de armazenamento que você criou anteriormente. 

Forneça um nome para o seu Blob Service Container. Outras configurações padrão não precisarão ser atualizadas.

![]({% image_buster /assets/img/azure-currents-step-3.png %})

### Etapa 4: Configurar Currents

Na Braze, navegue para **Currents > + Create Current > Azure Blob Data Export** (Currents > + Criar Current > Exportação de dados do Azure Blob) e forneça o nome da sua integração e o e-mail de contato.

Em seguida, forneça a string de conexão, o nome do contêiner e o prefixo do BlobStorage (opcional).

![A página do Currents do armazenamento do Microsoft Azure Blob na Braze. Nesta página, existem campos para o nome da integração, e-mail de contato, string de conexão, nome do contêiner e prefixo.]({% image_buster /assets/img/maz.png %})

Por fim, role até o final da página e selecione quais eventos de engajamento com mensagem ou eventos de comportamento do cliente você gostaria de exportar. Quando concluído, lance seu Current.

### Etapa 5: Configurar exportação de dados do Azure

A seguir, configura credenciais que são usadas para:
1. Exportações de segmentos através da API
2. exportações CSV (campanha, segmento, exportação de dados de usuários da canva via o dashboard)
3. relatórios de engajamento

Na Braze, navegue para **Integrações com Parceiros** > **Parceiros de tecnologia** > **Microsoft Azure** e forneça sua string de conexão, nome do contêiner de armazenamento do Azure e prefixo de armazenamento do Azure.

Em seguida, confira se a caixa **Definir como o destino padrão de exportação de dados** está marcada, pois isso garantirá que seus dados exportados sejam enviados para o Azure. Quando concluído, salve sua integração.

![A página de exportação de dados do Microsoft Azure no Braze. Nesta página, existem campos para string de conexão, nome do contêiner e prefixo.]({% image_buster /assets/img/azure_data_export.png %})

{% alert important %}
É importante manter sua string de conexão atualizada; se as credenciais do seu conector expirarem, o conector parará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão permanentemente perdidos.
{% endalert %}

## Comportamento de exportação

Os usuários que integraram uma solução de armazenamento de dados na nuvem e estão tentando exportar APIs, relatórios de dashboard ou relatórios CSV terão a seguinte experiência:

- Todas as exportações de API não retornarão um URL de download no corpo da resposta e devem ser recuperadas através do armazenamento de dados.
- Todos os relatórios do dashboard e relatórios CSV serão enviados para o e-mail do usuário para baixar (sem necessidade de permissões de armazenamento) e serão copiados para o armazenamento de dados. 
