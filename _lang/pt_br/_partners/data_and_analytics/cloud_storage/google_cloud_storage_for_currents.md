---
nav_title: Google Cloud Storage
article_title: Google Cloud Storage
alias: /partners/google_cloud_storage_for_currents/
description: "Este artigo de referência descreve a parceria entre a Braze e o Google Cloud Storage, um armazenamento de objetos altamente escalável para dados não estruturados."
page_type: partner
tool: Currents
search_tag: Partner

---

# Google Cloud Storage

> [O Google Cloud Storage](https://cloud.google.com/storage/) é um armazenamento de objetos altamente escalável para dados não estruturados oferecido pelo Google como parte do conjunto de produtos de computação em nuvem.

{% alert important %}
Se você estiver trocando entre provedores de armazenamento em nuvem, entre em contato com seu gerente de sucesso do cliente da Braze para obter mais assistência na configuração e validação de sua nova integração.
{% endalert %}

A integração entre Braze e o Google Cloud Storage permite enviar dados do Currents para o Google Cloud Storage. Em seguida, é possível usar um processo ETL (Extrair, Transformar, Carregar) para transferir seus dados para outros locais, como o Google BigQuery.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Google Cloud Storage | É necessário ter uma conta do Google Cloud Storage para usar a parceria. |
| Currents | Para exportar dados de volta para o Google Cloud Storage, é necessário que [o Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) esteja configurado em sua conta. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

Para integrar-se ao Google Cloud Storage, é necessário configurar as credenciais apropriadas que permitem que a Braze obtenha informações sobre os buckets de armazenamento gravados (`storage.buckets.get`) e crie objetos dentro desse bucket (`storage.objects.create`). 

Isso pode ser feito usando as instruções a seguir, que o orientarão na criação de uma função e de uma conta de serviço que gerará uma chave privada para ser usada em sua integração com o Currents.

### Etapa 1: Criar função

Crie uma nova função no Console do Google Cloud Platform navegando até **IAM e admin** > **Funções** > **\+ Criar função**.

![]({% image_buster /assets/img/gcs1.png %})

Dê um nome ao papel, em seguida, selecione **+Adicionar Permissões** e escolha o seguinte:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

{% alert note %}
A permissão `storage.objects.delete` é opcional. Ela permite que a Braze limpe arquivos incompletos.<br><br>Em raras circunstâncias, o Google Cloud pode encerrar as conexões antes do previsto, o que faz com que a Braze grave arquivos incompletos no Google Cloud Storage. Na maioria dos casos, a Braze tentará novamente e criará um novo arquivo com os dados corretos, deixando o arquivo antigo no Google Cloud Storage.
{% endalert %}

Quando terminar, selecione **Criar**.

![]({% image_buster /assets/img/gcs2.png %})

### Etapa 2: Crie uma nova conta de serviço

#### Etapa 2.1: Crie a conta de serviço

Crie uma nova conta de serviço no Console do Google Cloud Platform navegando até **IAM e admin** > **Contas de serviço** e selecionando **Criar conta de serviço**.

![]({% image_buster /assets/img/gcs3.png %})

Em seguida, dê um nome à conta de serviço e conceda a ela acesso à função personalizada recém-criada.

![Na Google Cloud Platform, na página de criação de serviços, digite o nome do seu papel no campo "Selecionar um Papel".]({% image_buster /assets/img/gcs4.png %})

#### Etapa 2.2: Criar uma chave

Na parte inferior da página, use o botão **Create Key** (Criar chave) para criar uma chave privada **JSON** para usar no Braze. Depois que a chave for criada, ela será baixada na sua máquina.

![]({% image_buster /assets/img/gcs5.png %})

### Etapa 3: Configurar Currents no Braze

Na Braze, navegue até **Currents** > **\+ Create Current** > **Google Cloud Storage Data Export** (Currents > + Criar Current > Exportação de dados do Google Cloud Storage) e forneça seu nome de integração e e-mail de contato.

Em seguida, faça upload de sua chave privada JSON em **GCS JSON Credentials** (Credenciais JSON do GCS) e forneça o nome do bucket do CGS e o prefixo do GCS (opcional). 

{% alert important %}
É importante manter seu arquivo de credenciais atualizado; se as credenciais do conector expirarem, o conector deixará de enviar eventos. Se isso persistir por mais de **48 horas**, os eventos do conector serão descartados e os dados serão perdidos permanentemente.
{% endalert %}

![A página do Google Cloud Storage Currents no Braze. Nesta página existem campos para nome da integração, e-mail de contato, credencial JSON do GCS, nome do bucket do GCS e prefixo.]({% image_buster /assets/img/gcs6.png %})

Por fim, role até a parte inferior da página e selecione quais eventos de engajamento com mensagens ou eventos de comportamento do cliente você gostaria de exportar. Quando concluído, inicie seu Current.

### Etapa 4: Configure as exportações do Google Cloud Storage

Para configurar as exportações do Google Cloud Storage (GCS), acesse **Parceiros de tecnologia** > **Google Cloud Storage**, insira suas credenciais do GCS e selecione **Definir como o destino padrão de exportação de dados**.

Tenha em mente que a organização e o conteúdo de quaisquer arquivos exportados serão idênticos nas integrações do AWS S3, Microsoft Azure e Google Cloud Storage.

{% alert important %}
Certifique-se de inserir o valor JSON completo que é [gerado pelo Google Cloud](https://cloud.google.com/iam/docs/keys-create-delete).
{% endalert %}

![A página do Google Cloud Storage no dashboard da Braze.]({% image_buster /assets/img/gcs7.png %}){: style="max-width:70%;"}

### Etapa 5: Teste suas credenciais da conta de serviço (opcional)

Sua conta de serviço do Google Cloud IAM deve ter as seguintes permissões:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Para verificar essas permissões no dashboard da Braze, vá para a página **Google Cloud Storage**, em seguida, selecione **Testar Credenciais**.

![A seção de credenciais do Google Cloud Storage no dashboard da Braze.]({% image_buster /assets/img/gcs8.png %}){: style="max-width:70%;"}

## Comportamento de exportação

Os usuários que integraram uma solução de armazenamento de dados na nuvem e estão tentando exportar APIs, relatórios de dashboard ou relatórios CSV terão a seguinte experiência:

- Todas as exportações da API não retornarão um URL para baixar no corpo da resposta e devem ser recuperadas por meio do armazenamento de dados.
- Todos os relatórios dashboard e CSV serão enviados para o e-mail dos usuários para serem baixados (não são necessárias permissões de armazenamento) e armazenados em backup no Data Storage.

## Solução de problemas

### As credenciais do Google Cloud Storage são inválidas

Se você receber o seguinte erro ao tentar inserir suas credenciais:

```
Google Cloud Storage Credentials are invalid. Please ensure that your credentials string, bucket name, and prefix are valid. You do not have read permission.
```

Certifique-se de que sua conta de serviço do Google Cloud IAM tenha as seguintes permissões:

- `storage.objects.create`
- `storage.objects.delete`
- `storage.objects.list`
- `storage.objects.get`
- `storage.buckets.get`

Após a verificação, você pode [testar suas credenciais no dashboard do Braze](#step-5-test-your-service-account-credentials-optional).
