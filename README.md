# ELOApp 2.0 - Sistema de Automação para Acolhimento de Igreja

> ⚠️ **Work in Progress**


##  Propósito Principal

Este projeto é uma solução para automatizar o fluxo de trabalho do Ministério de Acolhimento, inicialmente desenvolvido de forma voluntária por e para os membros da [Primeira Igreja Batista de Iraja](https://www.igrejadeiraja.org.br/). O objetivo é eliminar tarefas manuais, organizar o processo de contato com visitantes e fornecer uma maneira centralizada e eficiente de gerenciar os dados, desde a entrada inicial até o acompanhamento e a sincronização entre múltiplos usuários.

[Originalmente desenhado](https://github.com/arthurfernandes893/eloApp) para trabalhar com um banco de dados Local, essa nova versão introduz maior robustez ao utilizar SqlAlchemy como ORM e maior generalidade no tipo de banco de dados a ser utilizado.

O sistema utiliza uma combinação de scripts Python, conexão com um servidor de banco de dados, Inteligência Artificial (Google Gemini) para processamento de linguagem natural e uma interface gráfica amigável (Streamlit) para controle. Além de permitir a conexão de visualizadores de dados com a base dados para a construção de dashboards.

## Principais Objetivos da Aplicação:
- Conexão com banco de dados remoto
- Flux0 de autenticação OAuth via Google Account - com permissionamento
- Receber uma lista bruta de contatos e gerar uma tabela incompleta para serem atribuidos acolhedores a esses visitantes
    - Os Acolhedores devem ser escolhidos a partir de uma selection box
- Após inseridos, serão feitas validações, e por fim, inserção na base
- Não serão inseridos dados incompletos na base. 
    - Até a lista estar adequada, ela não será inserida
- Permitir Atualização da lista de acolhedores
- Permtir inserção de eventos
- Permitir o acoplamento de diferentes bases de dados em diferentes contextos
    - Evento com pessoal da própria igreja ou com acolhedores externos
    - 
- Incluir uma janela com gráficos de performance dos acolhimentos
    - Permitir busca de performance por acolhedor, por gps, por Homens ou Mulheres, por evento 