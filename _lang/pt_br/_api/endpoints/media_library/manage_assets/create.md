---
nav_title: "POST: Fazer upload de um ativo para a biblioteca de mídia"
article_title: "POST: Fazer upload de um ativo para a biblioteca de mídia"
search_tag: Endpoint
page_order: 1

layout: api_page
page_type: reference
description: "Este artigo descreve detalhes sobre o endpoint `POST /media_library/create`."
---

{% api %}
# Fazer upload de um ativo para a biblioteca de mídia
{% apimethod post %}
/media_library/create
{% endapimethod %}

> Use este endpoint para adicionar um ativo à [Braze media library](https://www.braze.com/docs/user_guide/engagement_tools/templates_and_media/media_library) usando uma URL hospedada externamente (`asset_url`) ou dados de arquivo binário enviados no corpo da solicitação (`asset_file`). Este endpoint suporta imagens e arquivos ZIP que contêm imagens.

## Pré-requisitos

Para usar esse endpoint, você precisará de uma [chave de API]({{site.baseurl}}/api/basics#rest-api-key/) com a permissão `media_library.create`.

## Limite de taxa

{% multi_lang_include rate_limits.md endpoint='default' %}

## Corpo da solicitação

Quando você inclui `asset_url`, o endpoint baixa o arquivo da URL. Quando você inclui `asset_file`, o endpoint usa os dados binários no corpo da solicitação.

Exemplo de corpo da solicitação para `asset_url`:

```json
{
  "asset_url": "https://cdn.example.com/assets/cat.jpg",
  "name": "Cat Graphic"
}
```

Exemplo de corpo da solicitação para `asset_file`:

```json
{
  "asset_file": <BINARY FILE DATA>,
  "name": "Cat Graphic"
}
```

O corpo da solicitação inclui os seguintes parâmetros:

| Parâmetro | Obrigatória | Tipo de dados | Descrição |
| --------- | -------- | --------- | ----------- |
| `asset_url` | Opcional | String | Uma URL acessível publicamente para o ativo a ser enviado para o Braze. |
| `asset_file` | Opcional | Binário | Dados de arquivo binário. |
| `name` | Opcional | String | Um nome a aparecer na biblioteca de mídia para este ativo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

{% alert important %}
`asset_url` e `asset_file` são mutuamente exclusivos, você deve incluir apenas um deles na sua solicitação de API.
{% endalert %}

### Nomes de arquivos enviados

Esta seção explica como o endpoint atribui nomes aos arquivos enviados com base em você incluir o parâmetro `name`.

#### Envios de arquivo único

| Cenário | Resultado |
| --- | --- |
| `name` fornecido | O valor de `name` é usado como o nome do ativo na biblioteca de mídia. |
| `name` excluído | O nome do arquivo original da URL ou do arquivo enviado é usado. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

#### Uploads de arquivos ZIP

| Cenário | Resultado |
| --- | --- |
| `name` fornecido | O valor `name` é usado como um prefixo, com um número crescente anexado como sufixo (por exemplo, "Meu Arquivo 1", "Meu Arquivo 2", "Meu Arquivo 3"). |
| `name` excluído | Cada arquivo mantém seu nome original de dentro do arquivo ZIP. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" style="table-layout: fixed; width: 100%;" }

## Exemplo de solicitação

Esta seção inclui dois exemplos de solicitações `curl`, uma para adicionar um ativo usando uma URL e outra usando dados de arquivo binário.

Esta solicitação mostra um exemplo de adição de um ativo à biblioteca de mídia usando um `asset_url`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_url": "https://cdn.example.com/assets/cat.jpg", "name": "Cat Graphic"}'
```

Esta solicitação mostra um exemplo de adição de um ativo à biblioteca de mídia usando um `asset_file`.

```
curl -X POST --location 'https://rest.iad-01.braze.com/media_library/create' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--header 'Content-Type: application/json' \
--data '{"asset_file":<BINARY FILE DATA>, "name":"Cat Graphic"}'
```

### Respostas de erro

Esta seção lista erros potenciais e suas mensagens e descrições correspondentes. 

#### Erros de validação

Erros de validação retornam uma estrutura como esta:

```json
{
  "message": (String) Human-readable error description
}
```

Esta tabela lista possíveis erros de validação.

| Status HTTP | Mensagem | Descrição |
| --- | --- | --- |
| 400 | "Ou asset_url ou asset_file devem ser fornecidos." | Nenhum parâmetro de ativo foi fornecido na solicitação. |
| 400 | "Tanto asset_url quanto asset_file não podem ser fornecidos. Por favor, forneça apenas um." | Ambos os parâmetros de ativo foram fornecidos; apenas um é permitido. |
| 403 | "APIs Públicas da Biblioteca de Mídia não estão habilitadas para esta empresa." | O recurso da biblioteca de mídia não está habilitado para este espaço de trabalho. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Erros de processamento

Erros de processamento retornam uma resposta diferente com códigos de erro:

```json
{
  "message": (String) Human-readable error description,
  "error_code": (String) error code,
  "meta": { }
}
```

Esta tabela lista possíveis erros de processamento.

| Código de erro | Status HTTP | Descrição |
| --- | --- | --- |
| `UNSUPPORTED_FILE_TYPE` | 400 | O tipo de arquivo enviado não é suportado. O objeto `meta` inclui o `file_type` que foi rejeitado. |
| `ASSET_SIZE_EXCEEDS_LIMIT` | 400 | O arquivo excede o tamanho máximo permitido. Imagens têm um limite de 5 MB. |
| `MEDIA_LIBRARY_LIMIT_REACHED` | 400 | O espaço de trabalho atingiu o número máximo de ativos (200 por padrão para empresas em teste gratuito, ilimitado caso contrário). O objeto `meta` inclui o `limit` atual. |
| `ASSET_UPLOAD_FAILED` | 400 | O ativo falhou ao fazer upload devido a problemas de processamento. |
| `ZIP_UPLOAD_ERROR` | 400 | O arquivo ZIP está corrompido ou não pôde ser aberto. O objeto `meta` inclui a mensagem `original_error`. |
| `ZIP_FILE_TOO_LARGE` | 400 | O tamanho total descompactado do arquivo ZIP excede o limite de 5 MB. O objeto `meta` inclui o `zip_file_name` e `zip_file_size`. |
| `ZIPPED_ENTITY_HAS_NO_NAME` | 400 | Uma entrada de arquivo dentro do ZIP não tem nome. Certifique-se de que o arquivo ZIP não está corrompido e adicione um nome para quaisquer entradas de arquivo sem nome. |
| `ZIPPED_ENTITY_CANNOT_HAVE_NESTED_DIRECTORY` | 400 | O arquivo ZIP contém diretórios aninhados, que não são suportados. Todos os arquivos devem estar no nível raiz do ZIP. |
| `GENERIC_ERROR` | 500 | Ocorreu um erro inesperado durante o upload. O objeto `meta` inclui a mensagem `original_error` para depuração. Tente novamente ou entre em contato com [Suporte]({{site.baseurl}}/support_contact/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }


## Resposta

Existem cinco códigos de status para este endpoint: `200`, `400`, `403`, `429` e `500`.

O seguinte JSON mostra a forma esperada da resposta.

```json
{ 
    "new_assets": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "url": (String) the URL to access the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif")
        }
    ],
    "errors": [
        {
            "name": (String) the name of the asset,
            "size": (Integer) the byte size of the asset,
            "ext": (String) the file extension (e.g., "png", "jpg", "gif"),
            "error": (String) the error that occurred
        }
    ],
    "dashboard_url": (String) the URL to view this asset in the Braze dashboard
}
```

{% endapi %}
