
STUDY_CYCLE = [
    
    # BANCO DE DADOS 1 (14 itens) ✓
    "1. [NIVEL DE ESTUDO: MUITO ALTO] [BANCO DE DADOS] Modelagem Conceitual: Diagrama Entidade-Relacionamento (DER). Cardinalidade (1:1, 1:N, N:M). Engenharia Reversa.",
    "2. [NIVEL DE ESTUDO: EXPLOSIVO] [BANCO DE DADOS] Normalização: Conceitos de 1FN (Atomicidade), 2FN (Dependência Parcial) e 3FN (Dependência Transitiva).",
    "3. [NIVEL DE ESTUDO: ALTO] [BANCO DE DADOS] Criação e Estrutura: CREATE/ALTER/DROP TABLE. Constraints (PRIMARY KEY, FOREIGN KEY, UNIQUE, CHECK). Metadados.",
    "4. [NIVEL DE ESTUDO: EXPLOSIVO] [BANCO DE DADOS] SQL Básico: SELECT, DISTINCT, WHERE, LIKE, IS NULL (Tratamento de nulos). ORDER BY.",
    "5. [NIVEL DE ESTUDO: EXPLOSIVO] [BANCO DE DADOS] SQL Avançado: JOINs (Inner, Left, Right, Full). Funções de Agregação (COUNT, SUM, AVG). GROUP BY e HAVING.",
    "6. [NIVEL DE ESTUDO: ALTO] [BANCO DE DADOS] Transações: INSERT, UPDATE, DELETE. Comandos COMMIT, ROLLBACK. Propriedades ACID (Atomicidade, Consistência, Isolamento, Durabilidade).",
    "7. [NIVEL DE ESTUDO: MÉDIO] [BANCO DE DADOS] Integridade Referencial: Ações de disparo (CASCADE, SET NULL, RESTRICT).",
    "8. [NIVEL DE ESTUDO: MÉDIO] [BANCO DE DADOS] Otimização: Índices (B-Tree vs Hash). Plano de Execução. Banco de dados em Memória.",
    "9. [NIVEL DE ESTUDO: BAIXO] [BANCO DE DADOS] SGBD Internals: Independência Lógica vs Física de Dados. Arquitetura de SGBD.",
    "10. [NIVEL DE ESTUDO: MÉDIO] [BANCO DE DADOS] NoSQL e Tipos: Teorema CAP. Diferença Relacional vs NoSQL. Tipos: Documento, Chave-Valor, Colunar, Grafos.",
    "11. [NIVEL DE ESTUDO: MÉDIO] [BANCO DE DADOS] Big Data: Conceito de Data Lake vs Data Warehouse. Os 5 V's do Big Data.",
    "12. [NIVEL DE ESTUDO: BAIXO] [BANCO DE DADOS] Modelagem Dimensional: Star Schema vs Snowflake. Tabelas Fato e Dimensão. OLAP vs OLTP.",
    "13. [NIVEL DE ESTUDO: BAIXO] [BANCO DE DADOS] Integração de Dados: Processo ETL (Extract, Transform, Load). Integração via Banco vs Arquivo.",
    "14. [NIVEL DE ESTUDO: BAIXO] [BANCO DE DADOS] Governança: Qualidade de Dados (Consistência/Completude). Gestão de Dados Mestres (MDM).",
    
    # ENGENHARIA DE SOFTWARE 2(12 itens) ✓
    "15. [NIVEL DE ESTUDO: MUITO ALTO] [ENGENHARIA DE SOFTWARE] Ciclos de Vida e Processos: Modelo Cascata (Waterfall), Espiral, V-Model e Prototipação. Entender as fases (Requisitos, Projeto, Implementação, Teste, Manutenção).",
    "16. [NIVEL DE ESTUDO: ALTO] [ENGENHARIA DE SOFTWARE] Processo Iterativo e Incremental: Diferença entre Iterativo (refinar) e Incremental (adicionar pedaços). O modelo RUP (fases: Incepção, Elaboração, Construção, Transição) cai bastante na Cesgranrio.",
    "17. [NIVEL DE ESTUDO: EXPLOSIVO] [ENGENHARIA DE SOFTWARE] Práticas Ágeis - Scrum: Decorar Papéis (PO, Scrum Master, Dev Team), Eventos (Daily, Sprint Planning, Review, Retrospective) e Artefatos (Backlog, Incremento).",
    "18. [NIVEL DE ESTUDO: MUITO ALTO] [ENGENHARIA DE SOFTWARE] Práticas Ágeis - XP e Kanban: XP (Programação em Par, Integração Contínua, Refatoração). Kanban (Limit WIP, Fluxo Contínuo). Manifesto Ágil (4 valores).",
    "19. [NIVEL DE ESTUDO: ALTO] [ENGENHARIA DE SOFTWARE] TDD (Test Driven Development): O Ciclo Red-Green-Refactor (Escrever teste falho -> Fazer passar -> Refatorar).",
    "20. [NIVEL DE ESTUDO: MÉDIO] [ENGENHARIA DE SOFTWARE] BDD (Behavior Driven Development): Linguagem Gherkin (Given, When, Then). Foco no comportamento do usuário.",
    "21. [NIVEL DE ESTUDO: MUITO ALTO] [ENGENHARIA DE SOFTWARE] Conceitos de Projeto: Acoplamento (quanto menos, melhor) vs Coesão (quanto mais, melhor). Princípios SOLID (básico).",
    "22. [NIVEL DE ESTUDO: MÉDIO] [ENGENHARIA DE SOFTWARE] Arquitetura de Software: Padrões Arquiteturais (MVC, Camadas/Layered, Microsserviços, Cliente-Servidor). Monolito vs Distribuído.",
    "23. [NIVEL DE ESTUDO: EXPLOSIVO] [ENGENHARIA DE SOFTWARE] CI/CD: Diferença exata entre Integração Contínua (CI - Merge frequente/Testes), Entrega Contínua (CD - Release manual) e Implantação Contínua (CD - Deploy automático).",
    "24. [NIVEL DE ESTUDO: ALTO] [ENGENHARIA DE SOFTWARE] DevOps e ALM: Cultura CAMS (Culture, Automation, Measurement, Sharing). Ciclo de Vida da Aplicação (ALM - Rastreabilidade do requisito ao deploy).",
    "25. [NIVEL DE ESTUDO: MUITO ALTO] [ENGENHARIA DE SOFTWARE] Notação BPMN: Decorar os símbolos principais. Eventos (Círculos), Atividades (Retângulos), Gateways (Losangos - Exclusivo vs Paralelo). Piscinas (Pools) e Raias (Lanes).",
    "26. [NIVEL DE ESTUDO: MÉDIO] [ENGENHARIA DE SOFTWARE] Diagrama ER: (Revisão) Entidades, Atributos e Relacionamentos. *Nota: Este tópico cruza com Banco de Dados, mas aqui foca no desenho/diagrama.*",
    
    # REQUISITOS 3 (6 itens) ✓
    "27. [NIVEL DE ESTUDO: MÉDIO] [REQUISITOS] Usuário e Personas: Projeto Centrado no Usuário (UCD). Análise de Personas (Fictícias, Arquétipos). Mapa de Empatia.",
    "28. [NIVEL DE ESTUDO: BAIXO] [REQUISITOS] Técnicas de Engajamento: Storytelling (Jornada do Usuário). Como contar a história do produto.",
    "29. [NIVEL DE ESTUDO: ALTO] [REQUISITOS] Metodologias de Design: Design Thinking (Empatizar, Definir, Idear, Prototipar, Testar). Lean UX (Ciclo Construir-Medir-Aprender, menos documentação, mais validação).",
    "30. [NIVEL DE ESTUDO: MUITO ALTO] [REQUISITOS] Prototipação e MVP: Conceito exato de MVP (Mínimo Produto Viável - gera valor/aprendizado). Prototipação (Baixa vs Alta fidelidade, Wireframes).",
    "31. [NIVEL DE ESTUDO: EXPLOSIVO] [REQUISITOS] Engenharia de Requisitos Ágil: Elicitação (Entrevistas, Workshops). Histórias de Usuário (Modelo 'Como um <papel>, quero <ação>, para <valor>'). Invest.",
    "32. [NIVEL DE ESTUDO: MUITO ALTO] [REQUISITOS] Qualidade do Requisito: Critérios de Aceitação (Definição de Pronto/DoD). BDD (Given/When/Then - Link com lista anterior).",
    
    # ARQUITETURA 4 (13 itens) ✓
    "33. [NIVEL DE ESTUDO: EXPLOSIVO] [ARQUITETURA] Design Patterns (GoF): Decorar a classificação: Criacionais (Singleton, Factory, Builder), Estruturais (Adapter, Facade, Composite) e Comportamentais (Strategy, Observer, Command). Saber o problema que cada um resolve.",
    "34. [NIVEL DE ESTUDO: MÉDIO] [ARQUITETURA] Anti-patterns: O que não fazer (ex: God Class, Spaghetti Code).",
    "35. [NIVEL DE ESTUDO: ALTO] [ARQUITETURA] Qualidade de Código: Refatoração (Melhorar estrutura sem mudar comportamento). Técnicas de Componentização (Baixo acoplamento).",
    "36. [NIVEL DE ESTUDO: MUITO ALTO] [ARQUITETURA] Arquiteturas Monolíticas: MVC (Model-View-Controller - Quem faz o que?). Sistemas em N-Camadas (Apresentação, Negócio, Dados).",
    "37. [NIVEL DE ESTUDO: ALTO] [ARQUITETURA] Persistência: Frameworks (Hibernate/JPA). Mapeamento Objeto-Relacional (ORM). Problema da impedância Objeto-Relacional.",
    "38. [NIVEL DE ESTUDO: EXPLOSIVO] [ARQUITETURA] SOA (Service Oriented Architecture): Conceito de Serviços. ESB (Barramento de Serviços Corporativos - Orquestração e Transformação).",
    "39. [NIVEL DE ESTUDO: MUITO ALTO] [ARQUITETURA] Web Services Clássicos (SOAP): SOAP (Envelope/Protocolo), WSDL (Contrato/Descrição), UDDI (Diretório/Busca), XML, XSLT (Transformação). Interoperabilidade.",
    "40. [NIVEL DE ESTUDO: MUITO ALTO] [ARQUITETURA] Web Services Modernos (REST): REST (Verbos HTTP, Stateless, Recursos). JSON vs XML. XML-HttpRequest (AJAX).",
    "41. [NIVEL DE ESTUDO: EXPLOSIVO] [ARQUITETURA] Microsserviços e Cloud Native: Diferença Monolito vs Microsserviço (Deploy independente, Banco descentralizado). 12-Factor App. Containerização (Docker - ARQ-3.19).",
    "42. [NIVEL DE ESTUDO: ALTO] [ARQUITETURA] Eventos e Mensageria: Arquitetura Orientada a Eventos (EDA). Publish-Subscribe (Pub/Sub). Message Broker (Kafka/RabbitMQ). Streaming de Dados (ARQ-3.25).",
    "43. [NIVEL DE ESTUDO: MÉDIO] [ARQUITETURA] Padrões Corporativos: Patterns of Enterprise Application Architecture (Livro do Martin Fowler - ex: Active Record, DTO, Repository).",
    "44. [NIVEL DE ESTUDO: MÉDIO] [ARQUITETURA] DevOps na Arquitetura: CI/CD em microsserviços. (Reforço do edital anterior).",
    "45. [NIVEL DE ESTUDO: BAIXO] [ARQUITETURA] Infra e Outros: Servidores de Aplicação (JBoss/Tomcat). Mediate APIs (API Gateway). Busca não estruturada (Elasticsearch/Solr).",
    
    # LINGUAGENS 5 (11 itens) ✓
    "46. [NIVEL DE ESTUDO: EXPLOSIVO] [LINGUAGENS] Orientação a Objetos: Polimorfismo, Herança, Encapsulamento. Classe Abstrata vs Interface. Sobrecarga (Overload) vs Sobrescrita (Override).",
    "47. [NIVEL DE ESTUDO: ALTO] [LINGUAGENS] Threads e Escalonamento: Estados da Thread (Pronto, Executando, Bloqueado). Concorrência vs Paralelismo. Preempção.",
    "48. [NIVEL DE ESTUDO: MÉDIO] [LINGUAGENS] Sincronização: O que é Deadlock (As 4 condições). Mutex e Semáforos (Conceito teórico).",
    "49. [NIVEL DE ESTUDO: MÉDIO] [LINGUAGENS] Gestão de Memória: Como funciona o Garbage Collector (Conceito de gerações e referências). Profiling (Identificar gargalos de CPU/Memória).",
    "50. [NIVEL DE ESTUDO: EXPLOSIVO] [LINGUAGENS] Coleções em Python: Listas (Mutáveis), Tuplas (Imutáveis), Dicionários (Chave-Valor) e Sets (Sem ordem/repetição).",
    "51. [NIVEL DE ESTUDO: EXPLOSIVO] [LINGUAGENS] Python Avançado: List Comprehensions (Sintaxe `[x for x in lista]`). Fatiamento/Slicing (`lista[::-1]`). Lambdas e Generators (`yield`).",
    "52. [NIVEL DE ESTUDO: ALTO] [LINGUAGENS] Exceções em Python: Blocos `try`, `except`, `else` e `finally`. (Atenção ao `else` que é específico do Python).",
    "53. [NIVEL DE ESTUDO: ALTO] [LINGUAGENS] .NET e C#: Estrutura do C# (Namespaces, Classes). Tipos Genéricos (`List<T>`, `Dictionary<K,V>`). LINQ (Consultas em coleções - muito comum no .NET).",
    "54. [NIVEL DE ESTUDO: MÉDIO] [LINGUAGENS] Arquitetura .NET: Injeção de Dependência (Nativa no Core). Diferença entre .NET Core (Cross-platform) e .NET Framework (Antigo). CLR (Common Language Runtime).",
    "55. [NIVEL DE ESTUDO: ALTO] [LINGUAGENS] JavaScript (ES6+): `var` vs `let` vs `const` (Escopo). Arrow Functions `() => {}`. Manipulação de JSON. Promises e Async/Await.",
    "56. [NIVEL DE ESTUDO: MÉDIO] [LINGUAGENS] HTML5 e CSS3: Tags semânticas (`<header>`, `<section>`, `<article>`). Seletores CSS e Box Model (Padding/Margin/Border).",
    
    # QUALIDADE E ESTRUTURAS DE DADOS 6 (11 itens) ✓
    "57. [NIVEL DE ESTUDO: EXPLOSIVO] [QUALIDADE E ESTRUTURAS DE DADOS] Estratégias de Teste: Caixa-Branca (Estrutural/Código) vs Caixa-Preta (Requisitos/Funcional). Teste de Regressão (Garantir que não quebrou). Testes Unitários vs Integração.",
    "58. [NIVEL DE ESTUDO: EXPLOSIVO] [QUALIDADE E ESTRUTURAS DE DADOS] GIT (Gerência de Configuração): Comandos essenciais (`commit`, `push`, `pull`, `merge`, `rebase`). Conceito de Staging Area e Resolução de Conflitos.",
    "59. [NIVEL DE ESTUDO: ALTO] [QUALIDADE E ESTRUTURAS DE DADOS] Código Limpo e Manutenção: Code Smells (Sinais de código ruim: Duplicação, Classes Deus). Refatoração (Alterar estrutura sem mudar comportamento externo).",
    "60. [NIVEL DE ESTUDO: MÉDIO] [QUALIDADE E ESTRUTURAS DE DADOS] Gestão da Qualidade: Débito Técnico (O custo do atalho). Métricas de Código (Complexidade Ciclomática, Cobertura de Testes). Auditoria de Sistemas.",
    "61. [NIVEL DE ESTUDO: EXPLOSIVO] [QUALIDADE E ESTRUTURAS DE DADOS] Pilhas e Filas: Pilha (LIFO - Last In First Out) vs Fila (FIFO - First In First Out). Aplicações práticas (Chamada de função vs Impressão).",
    "62. [NIVEL DE ESTUDO: ALTO] [QUALIDADE E ESTRUTURAS DE DADOS] Listas e Arrays: Vetores (Acesso O(1), Tamanho fixo) vs Listas Encadeadas (Acesso O(n), Inserção dinâmica). Lista Duplamente Encadeada.",
    "63. [NIVEL DE ESTUDO: MÉDIO] [QUALIDADE E ESTRUTURAS DE DADOS] Tipos e Sub-rotinas: Passagem de parâmetros (Por Valor vs Por Referência). Tipos Abstratos de Dados (TAD).",
    "64. [NIVEL DE ESTUDO: EXPLOSIVO] [QUALIDADE E ESTRUTURAS DE DADOS] Complexidade de Algoritmos: Notação Big-O. Análise de Pior Caso vs Caso Médio. Identificar O(1), O(n), O(log n) e O(n^2) no olho.",
    "65. [NIVEL DE ESTUDO: ALTO] [QUALIDADE E ESTRUTURAS DE DADOS] Ordenação e Pesquisa: Pesquisa Binária (Requer dados ordenados). QuickSort e MergeSort (Dividir para Conquistar). Recursividade (Caso base e chamada recursiva).",
    "66. [NIVEL DE ESTUDO: ALTO] [QUALIDADE E ESTRUTURAS DE DADOS] Árvores: Árvore Binária de Busca (BST). Travessia (In-order, Pre-order, Post-order). Árvores Balanceadas (AVL - Rotações). Heap (Para filas de prioridade).",
    "67. [NIVEL DE ESTUDO: MÉDIO] [QUALIDADE E ESTRUTURAS DE DADOS] Grafos e Estruturas de BD: Algoritmo de Dijkstra (Caminho Mínimo). Árvores B e B+ (Estrutura de índices em Banco de Dados).",
    
    # SEGURANÇA DA INFORMACAO  7 (15 itens) ✓
    "68. [NIVEL DE ESTUDO: MUITO ALTO] [SEGURANÇA DA INFORMACAO] Fundamentos e Criptografia: Segurança Física vs Lógica. Criptografia Simétrica (AES, DES, RC4) vs Assimétrica (RSA, ECC). Conceito de Chaves (Pública/Privada).",
    "69. [NIVEL DE ESTUDO: ALTO] [SEGURANÇA DA INFORMACAO] Certificação e Assinatura Digital: Hash (SHA-256, MD5) para Integridade. Assinatura Digital (Garante Autenticidade + Não-Repúdio). Certificado X.509 e ICP-Brasil.",
    "70. [NIVEL DE ESTUDO: ALTO] [SEGURANÇA DA INFORMACAO] Perímetro e VPN: Firewall (Packet Filter vs Stateful vs Proxy). DMZ. VPN (IPSec modo Túnel/Transporte vs SSL/TLS).",
    "71. [NIVEL DE ESTUDO: MÉDIO] [SEGURANÇA DA INFORMACAO] Monitoramento de Rede: IDS (Detecta) vs IPS (Previne). DLP (Prevenção de Vazamento). SIEM (Correlação de Logs).",
    "72. [NIVEL DE ESTUDO: MUITO ALTO] [SEGURANÇA DA INFORMACAO] Gestão de Identidade (IAM): Diferença Autenticação vs Autorização. MFA (Fatores: Saber, Ter, Ser). SSO (Single Sign-On).",
    "73. [NIVEL DE ESTUDO: ALTO] [SEGURANÇA DA INFORMACAO] Modelos de Acesso: RBAC (Papéis) vs ABAC (Atributos). Princípio do Menor Privilégio.",
    "74. [NIVEL DE ESTUDO: MUITO ALTO] [SEGURANÇA DA INFORMACAO] Malwares e Antivírus: Definições exatas de Ransomware, Worm, Trojan, Spyware, Rootkit, Botnet. Detecção por Assinatura vs Heurística (Comportamento).",
    "75. [NIVEL DE ESTUDO: EXPLOSIVO] [SEGURANÇA DA INFORMACAO] Ataques Web: SQL Injection (Injeção de Código), XSS (Stored vs Reflected), CSRF, DDoS, Path Traversal.",
    "76. [NIVEL DE ESTUDO: EXPLOSIVO] [SEGURANÇA DA INFORMACAO] DevSecOps: OWASP Top 10 (Principais falhas). SAST (Análise Estática/Código) vs DAST (Análise Dinâmica/Runtime). Security by Design.",
    "77. [NIVEL DE ESTUDO: MÉDIO] [SEGURANÇA DA INFORMACAO] Modelagem e Frameworks: STRIDE (Spoofing, Tampering...). MITRE ATT&CK (Táticas e Técnicas).",
    "78. [NIVEL DE ESTUDO: MÉDIO] [SEGURANÇA DA INFORMACAO] Segurança em Nuvem: CASB. Responsabilidade Compartilhada (IaaS, PaaS, SaaS).",
    "79. [NIVEL DE ESTUDO: BAIXO] [SEGURANÇA DA INFORMACAO] Mobile e IoT: MDM (BYOD, Containerização). Desafios de segurança em IoT.",
    "80. [NIVEL DE ESTUDO: MÉDIO] [SEGURANÇA DA INFORMACAO] Resposta e Continuidade Técnica: Gestão de Vulnerabilidades (CVE, CVSS). Fases de Resposta a Incidentes (NIST). Backup (Full, Inc, Dif).",
    "81. [NIVEL DE ESTUDO: BAIXO] [SEGURANÇA DA INFORMACAO] Políticas e ISO 27002: Classificação da Informação (Confidencialidade, Integridade, Disponibilidade). Estrutura da norma 27002.",
    "82. [NIVEL DE ESTUDO: BAIXO] [SEGURANÇA DA INFORMACAO] Gestão de Riscos e Leis: ISO 31000 (Tratamento de Risco). ISO 22301 (BIA, RTO, RPO). Lei SarbanENGENHARIA DE SOFTWAREOxley (SOX - Auditoria).",
    
    # CLOUD  8 (7 itens) ✓
    "83. [NIVEL DE ESTUDO: EXPLOSIVO] [CLOUD] Conceitos Essenciais: Diferença entre Escalabilidade (Vertical/Horizontal) e Elasticidade (Automática). Alta Disponibilidade (SLA) vs Recuperação de Desastres (RTO/RPO).",
    "84. [NIVEL DE ESTUDO: ALTO] [CLOUD] Economia da Nuvem: CapEx (Despesas de Capital) vs OpEx (Despesas Operacionais). Modelos de Faturamento (Pay-as-you-go, Instâncias Reservadas, Spot). TCO (Custo Total de Propriedade).",
    "85. [NIVEL DE ESTUDO: EXPLOSIVO] [CLOUD] Arquitetura Global: Regiões (Geográfico) vs Zonas de Disponibilidade (Data Centers isolados na mesma região). A importância da latência e redundância.",
    "86. [NIVEL DE ESTUDO: MÉDIO] [CLOUD] Hierarquia de Recursos: Tenant/Diretório -> Grupos de Gestão -> Subscrições -> Grupos de Recursos (Resource Groups) -> Recursos. Organização lógica.",
    "87. [NIVEL DE ESTUDO: EXPLOSIVO] [CLOUD] Segurança e Identidade: Modelo de Responsabilidade Compartilhada (O que é do Provedor vs O que é do Cliente). IAM (Gestão de Identidade e Acesso). Conformidade (Compliance/LGPD).",
    "88. [NIVEL DE ESTUDO: ALTO] [CLOUD] IaC (Infraestrutura como Código): Conceito de Idempotência (Executar N vezes com o mesmo resultado). Declarativo vs Imperativo. Ferramentas (Terraform, Ansible - Visão Geral).",
    "89. [NIVEL DE ESTUDO: MÉDIO] [CLOUD] IoT (Internet das Coisas): Conceito de Edge Computing (Processamento na borda/local). Conectividade de dispositivos com a nuvem (IoT Hubs).",
    
    # PRODUTIVIDADE E DADOS 9 (7 itens) ✓
    "90. [NIVEL DE ESTUDO: EXPLOSIVO] [PRODUTIVIDADE E DADOS] Scrum e Kanban: Os 3 Pilares do Scrum (Transparência, Inspeção, Adaptação). Papéis (PO, Scrum Master, Devs), Cerimônias e Artefatos. Kanban (Sistema Puxado, Limite de WIP, Gestão Visual).",
    "91. [NIVEL DE ESTUDO: MÉDIO] [PRODUTIVIDADE E DADOS] SAFe (Scaled Agile Framework): Foco na Gestão de Portfólio (Alinhamento estratégico). Níveis do SAFe (Time, Programa, Portfólio). Diferença entre Agile em time vs Agile em escala.",
    "92. [NIVEL DE ESTUDO: ALTO] [PRODUTIVIDADE E DADOS] Conceitos de Dados: Pirâmide DIKW (Dado, Informação, Conhecimento, Inteligência). Dados Estruturados (Relacionais) vs Não Estruturados (Texto, Vídeo, NoSQL). Mapeamento de Fontes.",
    "93. [NIVEL DE ESTUDO: MÉDIO] [PRODUTIVIDADE E DADOS] Manipulação em Planilhas: Tabelas Dinâmicas, Funções de busca (VLOOKUP/XLOOKUP), Tratamento de dados e Formatação Condicional.",
    "94. [NIVEL DE ESTUDO: EXPLOSIVO] [PRODUTIVIDADE E DADOS] Data Warehouse e Modelagem: Conceito de DW (Histórico, Integrado, Não volátil). Tabela Fato vs Tabela Dimensão. Esquema Estrela (Star Schema) vs Esquema Floco de Neve (Snowflake).",
    "95. [NIVEL DE ESTUDO: EXPLOSIVO] [PRODUTIVIDADE E DADOS] Operações OLAP: Cubos Multidimensionais. Operações clássicas: Drill-down (Detalhar), Roll-up (Resumir), Slice (Fatiar uma dimensão), Dice (Sub-cubo), Pivot (Rotacionar).",
    "96. [NIVEL DE ESTUDO: ALTO] [PRODUTIVIDADE E DADOS] Dashboards e Insights: KPI (Indicadores Chave). Storytelling com dados. Diferença entre Relatório (Estático) e Dashboard (Interativo). BI Self-Service como suporte à decisão.",
    
    # INFRAESTRUTURA 10 (5 itens) ✓
    "97. [NIVEL DE ESTUDO: MÉDIO] [INFRAESTRUTURA] Gerência de Processos e Filas: Estados do Processo (Pronto, Executando, Bloqueado). Troca de Contexto. Políticas de Escalonamento de Filas (FIFO, Round Robin).",
    "98. [NIVEL DE ESTUDO: BAIXO] [INFRAESTRUTURA] Processamento Paralelo e HPC: Diferença entre Paralelo (Multicore) e Distribuído (Cluster). Conceitos de HPC (High Performance Computing) aplicados a grandes volumes de dados.",
    "99. [NIVEL DE ESTUDO: ALTO] [INFRAESTRUTURA] Virtualização: Hipervisor Tipo 1 (Bare Metal - Ex: ESXi) vs Tipo 2 (Hosted - Ex: VirtualBox). Virtualização de Rede (SDN) e Armazenamento (SDS).",
    "100. [NIVEL DE ESTUDO: EXPLOSIVO] [INFRAESTRUTURA] Protocolos de Transferência e Web: Modelo TCP/IP. HTTP vs HTTPS (Certificados SSL/TLS). Métodos HTTP (GET, POST, PUT, DELETE). FTP (Transferência) e SMTP (E-mail).",
    "101. [NIVEL DE ESTUDO: EXPLOSIVO] [INFRAESTRUTURA] Protocolos de Autenticação Moderna: LDAP (Protocolo de acesso a diretórios). SAML 2.0 (Troca de autenticação via XML - Legado/Corporativo). OAuth (Delegação de autorização via JSON - Moderno/APIs).",
    
    # GOVERNANÇA 11 (5 itens) ✓
    "102. [NIVEL DE ESTUDO: EXPLOSIVO] [GOVERNANÇA] ITIL v4 - Fundamentos: Sistema de Valor de Serviço (SVS). As 4 Dimensões (Organizações/Pessoas, Informação/Tecnologia, Parceiros/Fornecedores, Fluxos de Valor/Processos). Cadeia de Valor de Serviço (SVC).",
    "103. [NIVEL DE ESTUDO: ALTO] [GOVERNANÇA] ITIL v4 - Práticas de Gerenciamento: Foco em Service Desk, Gerenciamento de Incidentes, Problemas, Mudanças e Liberação. Conceitos de Valor, Co-criação de Valor e Garantia vs Utilidade.",
    "104. [NIVEL DE ESTUDO: EXPLOSIVO] [GOVERNANÇA] DAMA-DMBoK: A Roda de DAMA (Knowledge Areas). Foco principal em: Governança de Dados (O centro da roda), Qualidade de Dados e Gerenciamento de Metadados. Papéis (Data Steward vs Data Owner).",
    "105. [NIVEL DE ESTUDO: MÉDIO] [GOVERNANÇA] Sistemas de Gestão (ERP): Características (Integração, Modularidade, Base de dados única). Diferença entre ERP (Recursos Empresariais), CRM (Clientes) e SCM (Cadeia de Suprimentos).",
    "106. [NIVEL DE ESTUDO: BAIXO] [GOVERNANÇA] Análise de Viabilidade: Viabilidade Técnica (Temos tecnologia?), Econômica (ROI, TCO, Payback) e Operacional. Análise Custo-Benefício."
]