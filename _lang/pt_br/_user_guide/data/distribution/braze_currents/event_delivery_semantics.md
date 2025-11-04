---
nav_title: Semântica de entrega de eventos
article_title: Semântica de entrega de eventos
page_order: 3
page_type: reference
description: "Este artigo de referência descreve e define como o Currents gerencia os dados de eventos de arquivo simples que enviamos aos parceiros do Data Warehouse Storage."
tool: Currents

---

# Semântica de entrega de eventos

> Esta página descreve e define como a Currents gerencia os dados de eventos de arquivo simples que enviamos aos parceiros de armazenamento do Data Warehouse.

O Currents for Data Storage é um fluxo contínuo de dados de nossa plataforma para um bucket de armazenamento em uma de nossas [conexões de parceiros de]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) data warehouse. O Currents grava arquivos Avro no seu bucket de armazenamento em limites regulares, permitindo que você processe e analise os dados do evento com seu próprio conjunto de ferramentas de Business Intelligence (BI).

{% alert important %}
Esse conteúdo **se aplica apenas aos dados de eventos de arquivo simples que enviamos aos parceiros do Data Warehouse Storage (Google Cloud Storage, Amazon S3 e Microsoft Azure Blob Storage)**. <br><br>Para obter o conteúdo que se aplica a outros parceiros, consulte nossa lista de [parceiros disponíveis]({{site.baseurl}}/user_guide/data/braze_currents/available_partners/) e verifique suas respectivas páginas.
{% endalert %}

## Entrega pelo menos uma vez

Como um sistema de alto rendimento, o Currents fornece uma entrega de eventos "pelo menos uma vez", o que significa que eventos duplicados podem ocasionalmente ser gravados em seu bucket de armazenamento. Isso pode acontecer quando os eventos são reprocessados de nossa fila por qualquer motivo.

Se os seus casos de uso exigirem a entrega "exatamente uma vez", você poderá usar o campo de identificador exclusivo que é enviado com cada evento (`id`) para desduplicar os eventos. Como o arquivo sai do nosso controle quando é gravado no seu bucket de armazenamento, não temos como garantir a deduplicação do nosso lado.

## Carimbos de data/hora

Todos os registros de data e hora exportados pelo Currents são enviados no fuso horário UTC. Para alguns eventos em que está disponível, também é incluído um campo de fuso horário, que fornece o formato IANA (Internet Assigned Numbers Authority) do fuso horário local do usuário no momento do evento.

### Latência

Os eventos enviados ao Braze por meio do SDK ou da API podem incluir um registro de data e hora do passado. O exemplo mais notável é quando os dados do SDK são enfileirados, por exemplo, quando não há conectividade móvel. Nesse caso, o registro de data e hora do evento refletirá quando o evento foi gerado. Isso significa que uma porcentagem de eventos parecerá ter alta latência.

## Formato Apache Avro

As integrações de armazenamento de dados do Braze Currents geram dados no formato `.avro`. Escolhemos [o Apache Avro](https://avro.apache.org/) porque é um formato de dados flexível que suporta nativamente a evolução do esquema e é compatível com uma ampla variedade de produtos de dados: 

- O Avro é suportado por quase todos os principais data warehouse.
- Caso deseje deixar seus dados no S3, o Avro compacta melhor do que CSV e JSON, portanto, você paga menos pelo armazenamento e pode usar menos CPU para analisar os dados.
- O Avro exige esquemas quando os dados são gravados ou lidos. Os esquemas podem ser desenvolvidos ao longo do tempo para lidar com a adição de campos sem quebras.

O Currents criará um arquivo para cada tipo de evento usando o seguinte formato:

```
<your-bucket-prefix>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>/event_type=<event-type>/date=<date>/<schema-id>/<zone>/dataexport.<cluster-identifier>.<connection-type-identifier>.integration.<integration-id>+<partition>+<offset>.avro
```

{% alert tip %}
Não é possível ver o código por causa da barra de rolagem? Saiba como corrigir isso [aqui]({{site.baseurl}}/help/help_articles/docs/scroll_bar_overlap/).
{% endalert %}

|Segmento de nome de arquivo |Definição|
|---|---|
| `<your-bucket-prefix>` | O conjunto de prefixos para essa integração do Currents. |
| `<cluster-identifier>` | Para uso interno da Braze. Será uma cadeia de caracteres como "prod-01", "prod-02", "prod-03" ou "prod-04". Todos os arquivos terão o mesmo identificador de cluster.|
| `<connection-type-identifier>` | O identificador do tipo de conexão. As opções são "S3", "AzureBlob" ou "GCS". |
| `<integration-id>` | A ID exclusiva para essa integração do Currents. |
| `<event-type>` | O tipo de evento no arquivo. |
| `<date>` | A hora em que os eventos são enfileirados em nosso sistema para processamento no fuso horário UTC. Formatado como AAAA-MM-DD-HH. |
| `<schema-id>` | Usado para versionar esquemas `.avro` para compatibilidade com versões anteriores e evolução do esquema. Inteiro. |
| `<zone>` | Para uso interno da Braze. |
| `<partition>` | Para uso interno da Braze. Inteiro. |
| `<offset>`| Para uso interno da Braze. Inteiro. Observe que arquivos diferentes enviados na mesma hora terão um parâmetro `<offset>` diferente. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
As convenções de nomenclatura de arquivos podem mudar no futuro. A Braze recomenda pesquisar todas as chaves em seu intervalo que tenham o prefixo <your-bucket-prefix>.
{% endalert %}

### Limite de gravação Avro

Em circunstâncias normais, o Braze gravará arquivos de dados em seu bucket de armazenamento a cada 5 minutos ou 15.000 eventos, o que ocorrer primeiro. Sob carga pesada, podemos gravar arquivos de dados maiores, com até 100.000 eventos por arquivo.

{% alert important %}
O Currents nunca gravará arquivos vazios.
{% endalert %}

### Alterações no esquema Avro

Ocasionalmente, a Braze poderá fazer alterações no esquema Avro quando os campos forem adicionados, alterados ou removidos. Para nossos propósitos aqui, há dois tipos de alterações: de ruptura e de não ruptura. Em todos os casos, o site `<schema-id>` será avançado para indicar que o esquema foi atualizado. Os eventos atuais gravados no Azure Blob Storage, no Google Cloud Storage e no Amazon S3 gravarão o endereço `<schema-id>` no caminho. Por exemplo, `<your-bucket-name0>/<currents-integration-id>/<event-type>/<date-of-event>/<schema-id>/<environment>/<avro-file>`.

#### Alterações ininterruptas

Quando um campo é adicionado ao esquema Avro, consideramos isso uma alteração ininterrupta. Os campos adicionados serão sempre campos Avro "opcionais" (por exemplo, com um valor padrão de `null`), portanto, eles "corresponderão" a esquemas mais antigos de acordo com a [especificação de resolução de esquemas Avro](http://avro.apache.org/docs/current/spec.html#schema+resolution). Essas adições não devem afetar os processos de extração, transformação e carga (ETL) existentes, pois o campo será simplesmente ignorado até que seja adicionado ao seu processo de ETL. 

{% alert important %}
Recomendamos que sua configuração de ETL seja explícita sobre os campos que processa para evitar a interrupção do fluxo quando novos campos forem adicionados.
{% endalert %}

Embora nos esforcemos para avisar com antecedência sobre todas as alterações, podemos incluir alterações ininterruptas no esquema a qualquer momento.

#### Mudanças significativas

Quando um campo é removido ou alterado no esquema Avro, consideramos isso uma alteração de ruptura. As alterações de ruptura podem exigir modificações nos processos ETL existentes, pois os campos que estavam em uso podem não ser mais registrados como esperado.

Todas as alterações significativas no esquema serão comunicadas antes da alteração.
