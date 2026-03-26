---
nav_title: Exportar dados do segmento para CSV
article_title: Exportar dados do segmento para CSV
page_order: 2
page_type: reference
description: "Este artigo de referência aborda como exportar dados de segmento para CSV."

---

# Exportar dados do segmento para CSV

> Esta página aborda como solicitar uma exportação CSV de dados de usuários de um segmento e os dados incluídos na exportação.

Para exportar dados de segmento para um CSV, selecione o menu suspenso **User Data** ao editar um segmento e selecione exportar os dados do usuário ou os endereços de e-mail do segmento.

![Seção de informações do segmento com o menu suspenso User Data mostrando opções de exportação.]({% image_buster /assets/img_archive/csvexport.png %})

Você também pode solicitar uma exportação CSV na página principal de **Segmentos**, selecionando o menu suspenso <i class="fas fa-gear"></i> **Configurações** de um segmento:

![Menu suspenso Configurações na página principal de Segmentos.]({% image_buster /assets/img_archive/csvexport2.png %})

{% alert tip %}
Para exportar dados de todos os seus perfis de usuários, crie um segmento sem filtros e solicite uma exportação CSV.
{% endalert %}

A saída CSV contém os dados de cada perfil de usuário capturado no segmento no momento da exportação. Você pode exportar qualquer segmento selecionando o ícone de engrenagem e a exportação CSV. A Braze gerará o relatório em segundo plano e o enviará por e-mail para o usuário que estiver conectado no momento.

{% alert important %}
Devido a restrições de tamanho de arquivo, sua exportação poderá falhar se o tamanho estimado do seu segmento for superior a 500.000 usuários. Note que essa restrição usa o tamanho estimado do seu segmento, e não o cálculo exato. Para mais detalhes, consulte [Exportação de segmentos grandes](#exporting-large-segments).
{% endalert %}

Se você tiver vinculado suas [credenciais do Amazon S3]({{site.baseurl}}/partners/data_and_infrastructure_agility/data_warehouses/amazon_s3/#amazon-s3-integration) à Braze, o CSV será enviado para o seu bucket S3 com a chave `segment-export/SEGMENT_ID/YYYY-MM-dd/users-RANDOMSTRING.zip`. É necessário estar conectado ao dashboard para acessar o link de download enviado por e-mail.

{% multi_lang_include alerts/important_alerts.md alert='S3 file bucket export' %}

## Dados incluídos na exportação

Os itens a seguir estão incluídos na sua exportação, dependendo da sua seleção.

### Exportação de dados de usuários em CSV

| Nome do campo                  | Descrição                                              |
| --------------------------- | -------------------------------------------------------- |
| Appboy ID                   | ID interna (não pode ser alterada)                           |
| country                     | País                                    |
| created_at                  | Data e hora em que o perfil do usuário foi criado                   |
| created_from                | Método usado para criar o perfil do usuário (por exemplo, API REST, SDK ou importação CSV)         |
| devices                     | Informações sobre o dispositivo                           |
| date_of_birth               | Data de nascimento                                            |
| email                       | Endereço de e-mail                                            |
| unsubscribed_from_emails_at | Data de cancelamento da inscrição de e-mails                            |
| user_id                     | ID externo                                              |
| first_name                  | Nome                                               |
| first_session               | Data e hora da primeira sessão                           |
| gender                      | Gênero                                                   |
| google_ad_ids               | IDs de publicidade do Google associados ao usuário                      |
| city                        | Cidade                                     |
| IDFAs                       | Valores do identificador para publicidade (IDFA)                 |
| IDFVs                       | Valores do identificador do fornecedor (IDFV)                      |
| language                    | Idioma no padrão ISO-639-1                                        |
| last_app_version_used       | Última versão do app usada                             |
| last_name                   | Sobrenome                                                |
| last_session                | Data e hora da última sessão                            |
| number_of_google_ad_ids     | Contagem de IDs de publicidade do Google associados               |
| number_of_IDFAs             | Contagem de IDFAs associados                                |
| number_of_IDFVs             | Contagem de IDFVs associados                                |
| number_of_push_tokens       | Contagem de tokens de notificação por push associados             |
| number_of_roku_ad_ids       | Contagem de IDs de publicidade Roku associados                 |
| number_of_windows_ad_ids    | Contagem de IDs de publicidade do Windows associados              |
| phone_number                | Número de telefone                                             |
| opted_into_push_at          | Data de aceitação das notificações por push                       |
| unsubscribed_from_push_at   | Data de cancelamento da inscrição nas notificações por push                |
| random_bucket               | Número aleatório do bucket                                 |
| roku_ad_ids                 | IDs de publicidade da Roku                          |
| session_count               | Número total de sessões                                 |
| timezone                    | Fuso horário do usuário no mesmo formato do banco de dados de fuso horário da IANA                                         |
| in_app_purchase_total       | Valor total gasto em compras no app                   |
| user_aliases                | Aliases de usuário, se houver                                          |
| windows_ad_ids              | IDs de publicidade do Windows                       |
| Eventos personalizados               | Com base na seleção na exportação                             |
| Atributos personalizados           | Com base na seleção na exportação                             |
{: .reset-td-br-1 .reset-td-br-2 }

### Exportar endereços de e-mail em CSV

| Nome do campo                  | Descrição            |
| --------------------------- | ---------------------- |
| user_id                     | ID externo do usuário     |
| first_name                  | Nome             |
| last_name                   | Sobrenome              |
| email                       | E-mail                  |
| unsubscribed_from_emails_at | Data de cancelamento da inscrição do e-mail |
| opted_in_to_emails_at       | Data de aceitação do e-mail      |
| user_aliases                | Aliases de usuário, se houver   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert tip %}
Para obter ajuda com exportações CSV e API, visite nosso artigo de [solução de problemas]({{site.baseurl}}/user_guide/data/export_braze_data/export_troubleshooting/).
{% endalert %} 

## Exportação de segmentos grandes

Há vários métodos para exportar um segmento grande de usuários que contém mais de 500.000 usuários.

{% tabs %}
{% tab Multiple segments %}

Você pode dividir um segmento grande em segmentos menores e, em seguida, exportar cada um dos segmentos menores da Braze. 

{% endtab %}
{% tab Random bucket numbers %}

Você também pode usar [números aleatórios de bucket]({{site.baseurl}}/user_guide/engagement_tools/testing/random_bucket_numbers/) para dividir sua base de usuários em vários segmentos e combiná-los após a exportação. Por exemplo, se você precisar dividir seu segmento em dois segmentos diferentes, poderá fazer isso com os seguintes filtros:
- Segmento 1: O número do bucket aleatório é menor que 5000 (inclui 0-4999)
- Segmento 2: O número do bucket aleatório é maior que 4999 (inclui 5000-9999)

{% endtab %}
{% tab Endpoints %}

Também é possível usar os seguintes endpoints para exportar dados de usuários de um segmento específico. Note que esses endpoints estão sujeitos a limites de dados.
- [`/users/export/segment`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_segment/)
- [`/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group/)

{% endtab %}
{% endtabs %}