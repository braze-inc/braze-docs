---
nav_title: "Segmentos do catálogo"
article_title: Segmentos do catálogo
page_order: 1
page_type: reference
alias: "/catalog_segments/"
description: "Este artigo descreve como criar segmentos de catálogo, que usam dados de catálogo nas extensões de segmento do SQL para criar públicos de usuários."
tool: Segments
---

# Segmentos do catálogo

> Os segmentos de catálogo são um tipo de extensão de segmento SQL criado pela combinação de dados de catálogo com dados de eventos personalizados ou compras. Eles podem ser referenciados em um segmento e, em seguida, direcionados por campanhas e canvas. 

{% alert important %}
Os segmentos do catálogo estão atualmente em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado.
{% endalert %}

Os segmentos de catálogo usam SQL para unir dados de catálogos e dados de eventos personalizados ou compras. Para isso, você deve ter um campo identificador comum em seus catálogos e em seus eventos ou compras personalizados. Por exemplo, o valor de um ID de item em um catálogo deve corresponder ao valor de uma propriedade em um evento personalizado.

## Criação de um segmento de catálogo

1. Acesse **Extensões de segmento** > **Criar nova extensão** > **Iniciar com modelo** e selecione um modelo. <br>![Modal com a opção de criar um segmento de catálogo para eventos ou compras.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2\. O editor SQL é preenchido automaticamente com um modelo. <br>![Editor SQL com um modelo pré-gerado.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Esse modelo une os dados de eventos do usuário com os dados do catálogo para segmentar os usuários que se engajaram com determinados itens do catálogo.

3. Use a guia **Variables (Variáveis** ) para fornecer os campos necessários para seu modelo antes de gerar seu segmento. <br>Para que o Braze identifique os usuários com base no engajamento deles com os itens do catálogo, é necessário fazer o seguinte: <br> \- Selecione um catálogo que contenha um campo de catálogo <br> \- Selecione um evento personalizado que contenha uma propriedade de evento <br> \- Corresponder os valores de propriedade do campo e do evento de seu catálogo

Aqui estão as diretrizes para selecionar as variáveis:

| Campo variável | Descrição |
| --- | --- |
| `Catalog` | O nome do catálogo que está sendo usado para direcionamento de usuários. |
| `Catalog field`| O campo em seu catálogo que contém os mesmos valores que o `Custom event property`. Isso geralmente é um tipo de identificação. No caso de uso de comércio eletrônico, isso seria `shopify_id`. |
| `Custom event` | O nome de seu evento personalizado, que é o mesmo evento que contém uma propriedade com valores que correspondem ao seu `Catalog field`. No caso de uso de comércio eletrônico, isso seria `Made Order`. |
| `Custom event property` | O nome de sua propriedade de evento personalizado, que corresponde aos valores de seu `Catalog field`. No caso de uso do exemplo de comércio eletrônico, isso seria `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4\. Se necessário, preencha campos opcionais adicionais para seu caso de uso para segmentar por um valor de campo específico em seu catálogo:
- `Catalog field`: Um campo específico (nome da coluna) dentro desse catálogo
- `Value`: Um valor específico dentro desse campo ou coluna <br><br> Usando o app de integridade como exemplo, digamos que dentro do catálogo de cada médico que você pode marcar, há um campo chamado `specialty` que contém um valor como `vision` ou `dental`. Para segmentar os usuários que visitaram qualquer médico com o valor `dental`, você pode selecionar `specialty` como `Catalog field` e `dental` como `Value`.

5. Depois de criar um segmento SQL, recomendamos clicar em **Run Preview (Executar prévia** ) para ver se a consulta retorna usuários ou se há erros. Para saber mais sobre [a prévia dos resultados da consulta]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), o gerenciamento de [extensões de segmento de SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions) e muito mais, consulte [Extensões de segmento de SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

{% alert note %}
Se estiver criando um segmento SQL que use a tabela `CATALOGS_ITEMS_SHARED`, será necessário especificar uma ID de catálogo. Por exemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

## Atualização da associação de segmentos

Para atualizar a associação de segmentos de qualquer segmento do catálogo, abra o segmento do catálogo e selecione **Actions** > **Refresh** > **Yes, Refresh**.

{% alert tip %}
Se tiver criado um segmento no qual espera que os usuários entrem e saiam regularmente, atualize manualmente o segmento do catálogo que ele usa antes de direcionar esse segmento em uma campanha ou Canva.
{% endalert %}

### Designar configurações de atualização

{% multi_lang_include segments.md section='Refresh settings' %}

## Casos de uso

### Aplicativo de integridade

Digamos que você tenha um app de integridade e queira segmentar os usuários que agendaram uma visita ao dentista. Você também tem o seguinte:

- Um catálogo `Doctors` que contém os diferentes médicos que um paciente pode marcar, cada um atribuído a um `doctor ID`
- Um evento personalizado `Booked Visit` com uma propriedade `doctor ID` que compartilha os mesmos valores que o campo `doctor ID` em seu catálogo
- Um campo `speciality` em seu catálogo que contém o valor `dental` 

Você configuraria um segmento de catálogo usando as seguintes variáveis:

| Variável | Propriedade |
| --- | --- |
| `Catalog`| Médicos |
| `Catalog field` | ID do médico |
| `Custom event`| Visita reservada|
| `Custom event property` | ID do médico |
| `(Under Filter SQL Results) Catalog field` | Especialidade |
| `(Under Filter SQL Results) Value`| Odontológico |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Plataforma SaaS

Digamos que você tenha uma plataforma SaaS B2B e queira segmentar os usuários que são colaboradores de um cliente existente. Você também tem o seguinte:

- Um catálogo `Accounts` que contém as diferentes contas que estão usando atualmente sua plataforma SaaS, cada uma atribuída a um `account ID`
- Um evento personalizado `Event Attendance` com uma propriedade "account ID" que compartilha os mesmos valores que o campo "account ID" em seu catálogo
- Um campo `Classification` em seu catálogo que contém o valor `enterprise` 

Você configuraria um segmento de catálogo usando as seguintes variáveis:

| Variável | Propriedade |
| --- | --- |
| `Catalog` | Contas |
| `Catalog field `| ID da conta |
| `Custom event` | Participação em eventos |
| `Custom event property` | ID da conta |
| `(Under Filter SQL Results) Catalog field` | Classificação |
| `(Under Filter SQL Results) Value` | Empresa |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Perguntas frequentes

### A execução de um segmento de catálogo consome créditos de extensão de segmento do SQL?

Sim, os segmentos de catálogo são alimentados pelo SQL e consomem créditos de extensão de segmento do SQL. Para saber mais, confira [o uso de SQL Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### A criação de um segmento de catálogo consome alocações de extensão de segmento do SQL?

Sim. Da mesma forma que as extensões de segmento do SQL contam para sua cota de extensão de segmento, os segmentos de catálogo também contam para essa cota.

### Tenho um caso de uso de segmento de catálogo que o modelo atual não atende. Como devo configurar isso?

Entre em contato com seu gerente de suporte ao cliente ou com o [suporte da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/) para obter orientação adicional.

