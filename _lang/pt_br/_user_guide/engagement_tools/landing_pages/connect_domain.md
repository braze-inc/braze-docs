---
nav_title: Conectando seu domínio
article_title: Conectando seu domínio
description: "Este artigo aborda como conectar seu próprio domínio personalizado às landing pages do Braze."
page_order: 1
alias: /landing_pages/connect_domain/
---

# Conexão de seu domínio

> Conecte seu próprio domínio ao espaço de trabalho do Braze para personalizar os URLs da landing page com sua marca.

Para conectar um domínio ou subdomínio à sua conta Braze, peça a um administrador que siga as etapas abaixo.

1. Acesse **Configurações** > **Configurações da landing page**.
2. Digite o domínio ou subdomínio que deseja conectar e selecione **Submit (Enviar)**. Por exemplo, `forms.example.com`.
3. Copie e cole os registros **TXT** e **CNAME** nas configurações de DNS do seu provedor de domínio.
4. Retorne ao dashboard do Braze para verificar a conexão.

![Página Landing Page Settings com um registro TXT e dois registros CNAME listados com seus respectivos nomes e valores.][1]

{% alert note %}
Dependendo do seu provedor de domínio, a conexão pode levar até 48 horas. Quando o processo for concluído, começaremos a usar seu domínio personalizado para suas landing pages no dashboard do Braze.
{% endalert %}

## Usando seu domínio no Braze

Depois que a verificação de seu domínio for concluída, ele será usado por padrão no Braze. Por exemplo, se você conectar o subdomínio `forms.example.com`, os URLs de sua landing page serão atualizados para se parecerem com `forms.example.com/holiday-sale`.

{% alert note %}
A exclusão de domínios personalizados será feita em breve. Entre em contato com o gerente de sucesso do cliente se precisar remover o subdomínio.
{% endalert %}

## Recursos de provedores de domínio

Abaixo estão listados recursos para criar e gerenciar registros DNS com provedores de domínio comumente usados. Se estiver usando um provedor diferente, consulte a documentação desse provedor ou entre em contato com a equipe de suporte para obter informações.

| Provedor de domínio | Recursos |
| --- | --- |
| Bluehost | [Explicação dos registros DNS](https://my.bluehost.com/hosting/help/508)<br> [Gerenciamento de DNS Adicionar, editar ou excluir entradas de DNS](https://my.bluehost.com/hosting/help/559) |
| Dreamhost | [Como faço para adicionar registros DNS personalizados?](https://help.dreamhost.com/hc/en-us/articles/360035516812) |
| GoDaddy | [Adicionar um registro CNAME](https://www.godaddy.com/help/add-a-cname-record-19236?) |
| Cloudflare | [Gerenciar registros DNS](https://developers.cloudflare.com/dns/manage-dns-records/how-to/create-dns-records/) |
| Squarespace | [Adição de configurações de DNS personalizadas](https://support.squarespace.com/hc/en-us/articles/360002101888-Adding-custom-DNS-records-to-your-Squarespace-managed-domain) |

{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Solução de problemas 

### Falha na conexão com meu domínio

Verifique se o domínio foi inserido corretamente e se corresponde ao que foi enviado ao Braze a partir de sua conta de provedor de domínio. Se estiver correto e corresponder, verifique os registros TXT e CNAME fornecidos pelo Braze. Eles devem corresponder aos registros inseridos na conta do provedor de domínio.

## Perguntas frequentes

### Posso conectar vários subdomínios ao meu espaço de trabalho ou conectar um subdomínio a vários espaços de trabalho?

Não, atualmente só é possível conectar um subdomínio a um espaço de trabalho.

[1]: {% image_buster /assets/img/landing_pages/connect_subdomain.png %}
