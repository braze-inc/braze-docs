---
nav_title: "Segmentos do catálogo"
article_title: Segmentos do catálogo
page_order: 0
page_type: reference
alias: "/catalog_segments/"
description: "Este artigo descreve como criar segmentos de catálogo, que usam dados de catálogo nas extensões de segmento do SQL para criar públicos de usuários."
tool: Segments
---

# Segmentos do catálogo

> Os segmentos de catálogo são um tipo de extensão de segmento SQL criado pela combinação de dados de catálogo com dados de eventos personalizados ou compras. Eles podem ser referenciados em um segmento e, em seguida, direcionados por campanhas e canvas. 

Os segmentos de catálogo usam SQL para unir dados de catálogos e dados de eventos personalizados ou compras. Para isso, você deve ter um campo identificador comum em seus catálogos e em seus eventos personalizados ou compras. Por exemplo, o valor de um ID de item em um catálogo deve corresponder ao valor de uma propriedade em um evento personalizado.

## Criação de um segmento de catálogo

1. Acesse **Extensões de segmento** > **Criar nova extensão** > **Iniciar com modelo** e selecione um modelo. <br>![Modal com a opção de criar um segmento de catálogo para eventos, compras ou segmentos de RFM.]({% image_buster /assets/img/catalog-segments-template.png %}){: style="max-width:80%" }

{: start="2"}
2. O editor SQL é preenchido automaticamente com um modelo. <br>![Editor SQL com um modelo pré-gerado.]({% image_buster /assets/img/catalog-segments-editor.png %}){: style="max-width:80%" }<br>Esse modelo une os dados de eventos do usuário com os dados do catálogo para segmentar os usuários que se engajaram com determinados itens do catálogo.

3. Use a guia **Variáveis** para fornecer os campos necessários para seu modelo antes de gerar seu segmento. <br>Para que a Braze identifique os usuários com base no engajamento deles com os itens do catálogo, é necessário fazer o seguinte: <br> - Selecionar um catálogo que contenha um campo de catálogo <br> - Selecionar um evento personalizado que contenha uma propriedade de evento <br> - Fazer a correspondência entre os valores do campo do catálogo e da propriedade do evento

Aqui estão as diretrizes para selecionar as variáveis:

| Campo variável | Descrição |
| --- | --- |
| `Catalog` | O nome do catálogo que está sendo usado para direcionamento de usuários. |
| `Catalog field`| O campo em seu catálogo que contém os mesmos valores que o `Custom event property`. Isso geralmente é um tipo de ID. No caso de uso de e-commerce, isso seria `shopify_id`. |
| `Custom event` | O nome do seu evento personalizado, que é o mesmo evento que contém uma propriedade com valores correspondentes ao seu `Catalog field`. No caso de uso de e-commerce, isso seria `Made Order`. |
| `Custom event property` | O nome da sua propriedade de evento personalizado, que corresponde aos valores do seu `Catalog field`. No exemplo de caso de uso de e-commerce, isso seria `Shopify_ID.`|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{: start="4"}
4. Se necessário, preencha campos opcionais adicionais para seu caso de uso, a fim de segmentar por um valor de campo específico em seu catálogo:
- `Catalog field`: Um campo específico (nome da coluna) dentro desse catálogo
- `Value`: Um valor específico dentro desse campo ou coluna <br><br> Usando o app de saúde como exemplo, digamos que dentro do catálogo de cada médico que você pode agendar, há um campo chamado `specialty` que contém um valor como `vision` ou `dental`. Para segmentar os usuários que visitaram qualquer médico com o valor `dental`, você pode selecionar `specialty` como `Catalog field` e `dental` como `Value`.

5. Depois de criar um segmento SQL, recomendamos clicar em **Executar prévia** para ver se a consulta retorna usuários ou se há erros. Para saber mais sobre [a prévia dos resultados da consulta]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#previewing-results), o gerenciamento de [extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/#managing-sql-segment-extensions) e muito mais, consulte [Extensões de segmento SQL]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments/). 

{% alert note %}
Se estiver criando um segmento SQL que use a tabela `CATALOGS_ITEMS_SHARED`, será necessário especificar um ID de catálogo. Por exemplo:

```sql
SELECT * FROM CATALOGS_ITEMS_SHARED
WHERE CATALOG_ID = 'XYZ'
LIMIT 10
```
{% endalert %}

### Determinar se você precisa inverter o SQL

Embora não seja possível consultar diretamente os usuários com zero eventos, você pode usar **Inverter SQL** para direcionar esses usuários.

Por exemplo, para direcionar usuários que tenham menos de três compras, primeiro escreva uma consulta para selecionar usuários que tenham três ou mais compras. Em seguida, selecione **Inverter SQL** para direcionar usuários com menos de três compras (incluindo aqueles com zero compras).

![Extensão de segmento denominada "Clicou em 1-4 e-mails nos últimos 30 dias" com a opção de inverter o SQL selecionada.]({% image_buster /assets/img_archive/sql_segment_invert_sql.png %}){: style="max-width:70%;"}

{% alert important %}
A menos que você esteja direcionando especificamente usuários com zero eventos, não será necessário inverter o SQL. Se **Inverter SQL** estiver selecionado, confirme se o recurso é necessário e se o segmento corresponde ao público desejado. Por exemplo, se uma consulta direciona usuários com pelo menos um evento, ela só direcionará usuários com zero eventos quando invertida.
{% endalert %}

## Atualização da associação de segmentos

Para atualizar a associação de segmentos de qualquer segmento do catálogo, abra o segmento do catálogo e selecione **Ações** > **Atualizar** > **Sim, atualizar**.

{% alert tip %}
Se você criou um segmento em que espera que os usuários entrem e saiam regularmente, atualize manualmente o segmento do catálogo que ele usa antes de direcionar esse segmento em uma campanha ou Canvas.
{% endalert %}

### Definir configurações de atualização

{% multi_lang_include segments.md section='Refresh settings' %}

## Casos de uso

{% tabs local %}
{% tab Health %}

### App de saúde

Digamos que você tenha um app de saúde e queira segmentar os usuários que agendaram uma visita ao dentista. Você também tem o seguinte:

- Um catálogo `Doctors` que contém os diferentes médicos que um paciente pode agendar, cada um atribuído a um `doctor ID`
- Um evento personalizado `Booked Visit` com uma propriedade `doctor ID` que compartilha os mesmos valores que o campo `doctor ID` em seu catálogo
- Um campo `speciality` em seu catálogo que contém o valor `dental`

Você configuraria um segmento de catálogo usando as seguintes variáveis:

| Variável | Propriedade |
| --- | --- |
| `Catalog`| Doctors |
| `Catalog field` | doctor ID |
| `Custom event`| Booked Visit|
| `Custom event property` | doctor ID |
| `(Under Filter SQL Results) Catalog field` | Specialty |
| `(Under Filter SQL Results) Value`| Dental |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% tab SaaS %}

### Plataforma SaaS

Digamos que você tenha uma plataforma SaaS B2B e queira segmentar os usuários que são colaboradores de um cliente existente. Você também tem o seguinte:

- Um catálogo `Accounts` que contém as diferentes contas que estão usando atualmente sua plataforma SaaS, cada uma atribuída a um `account ID`
- Um evento personalizado `Event Attendance` com uma propriedade "account ID" que compartilha os mesmos valores que o campo "account ID" em seu catálogo
- Um campo `Classification` em seu catálogo que contém o valor `enterprise`

Você configuraria um segmento de catálogo usando as seguintes variáveis:

| Variável | Propriedade |
| --- | --- |
| `Catalog` | Accounts |
| `Catalog field `| account ID |
| `Custom event` | Event Attendance |
| `Custom event property` | account ID |
| `(Under Filter SQL Results) Catalog field` | Classification |
| `(Under Filter SQL Results) Value` | Enterprise |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endtab %}
{% endtabs %}

## Perguntas frequentes

### A execução de um segmento de catálogo consome créditos de extensão de segmento SQL?

Sim, os segmentos de catálogo são alimentados por SQL e consomem créditos de extensão de segmento SQL. Para saber mais, confira [Uso de SQL Segments]({{site.baseurl}}/user_guide/engagement_tools/segments/sql_segments#monitoring-your-sql-segments-usage).

### A criação de um segmento de catálogo consome cotas de extensão de segmento SQL?

Sim. Da mesma forma que as extensões de segmento SQL contam para sua cota de extensão de segmento, os segmentos de catálogo também contam para essa cota.

### Tenho um caso de uso de segmento de catálogo que o modelo atual não atende. Como devo configurar isso?

Fale com o seu gerente de suporte ao cliente ou com o [suporte da Braze]({{site.baseurl}}/user_guide/administrative/access_braze/support/) para obter orientação adicional.