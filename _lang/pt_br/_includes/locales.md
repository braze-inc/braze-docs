{% if include.section == "Frequently Asked Questions" %}

## Perguntas frequentes

#### Posso fazer uma alteração na cópia traduzida em uma das minhas localidades?
Sim. Primeiro, faça a edição no CSV, depois faça o upload do arquivo novamente para alterar a cópia traduzida.

#### Posso aninhar tags de tradução?
Não.

#### Posso adicionar estilo HTML nas tags de tradução?
Sim, mas certifique-se de verificar se a formatação HTML não foi traduzida junto com o conteúdo.

#### Que validações ou verificações extras o Braze faz?

| Cenário                                                                                                                                                 | Validação em Braze                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Um arquivo de tradução não tem localidades associadas à mensagem atual.                                                                               | Esse arquivo de tradução não será carregado.                                                                       |
| Um arquivo de tradução está sem alguns blocos de texto, como um texto dentro de tags de tradução Liquid, da mensagem de e-mail atual.                                | Esse arquivo de tradução não será carregado.                                                                       |
| O arquivo de tradução inclui o texto padrão que não corresponde aos blocos de texto da mensagem de e-mail atual.                                          | Esse arquivo de tradução não será carregado. Corrija isso em seu CSV antes de tentar fazer upload novamente.               |
| O arquivo de tradução inclui localizações que não existem nas configurações **do Suporte multilíngue**.                                                           | Essas localizações não serão salvas no Braze.                                                                      |
| O arquivo de tradução inclui blocos de texto que não existem na mensagem atual (como o rascunho atual no momento em que as traduções são feitas upload). | Os blocos de texto que não existirem em sua mensagem atual não serão salvos do arquivo de tradução para o Braze. |
| Remoção de uma localização da mensagem depois que essa localização já tiver sido carregada para a mensagem como parte do arquivo de tradução.                           | A remoção da localidade removerá todas as traduções associadas à localidade em sua mensagem.                   |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% endif %}