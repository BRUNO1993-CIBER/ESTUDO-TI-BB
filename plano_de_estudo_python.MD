
## TRILHA DE DOMÍNIO EM PYTHON
---

## MÓDULO 1 — FUNDAMENTOS COMPUTACIONAIS

---

**1.1** — Representação binária e aritmética computacional
*(IEEE 754, overflow, underflow, erros de ponto flutuante)*

---

**1.2** — Arquitetura de computadores e modelo de memória
*(Stack, heap, cache L1/L2/L3, localidade de referência)*

---

**1.3** — Sistema operacional e processos
*(Processo, thread, scheduling, system call, I/O bloqueante)*

---

**1.4** — Lógica e álgebra booleana
*(Operadores lógicos, tabelas-verdade, leis de De Morgan)*

---

**1.5** — Complexidade algorítmica e notação assintótica
*(Big O, Big Theta, Big Omega, análise de pior/melhor/médio caso)*

---
---

## MÓDULO 2 — PYTHON: FUNDAMENTOS COM PROFUNDIDADE

---

**2.1** — Modelo de execução do CPython
*(Tokenização, AST, bytecode, PVM, módulos `ast` e `dis`)*

---

**2.2** — Modelo de objetos do Python
*(Tudo é objeto, referências, identidade, mutabilidade, reference counting)*

---

**2.3** — Tipos nativos com profundidade
*(`int`, `float`, `str`, `bytes`, `list`, `tuple`, `dict`, `set` — complexidades de tempo de cada operação)*

---

**2.4** — Controle de fluxo e semântica de escopo
*(Modelo LEGB, `global`, `nonlocal`, semântica do `for` em Python)*

---

**2.5** — Funções como cidadãos de primeira classe
*(`*args`, `**kwargs`, closures, armadilha de mutáveis como default)*

---

**2.6** — Tratamento de exceções com rigor
*(Hierarquia de exceções, `try/except/else/finally`, context managers)*

---
---

## MÓDULO 3 — ESTRUTURAS DE DADOS E ALGORITMOS

---

**3.1** — Arrays e listas encadeadas
*(Array dinâmico, `list` vs `deque`, amortização de custo)*

---

**3.2** — Pilhas e filas
*(`list.pop(0)` vs `deque.popleft()`, aplicações práticas)*

---

**3.3** — Tabelas hash e dicionários
*(Hashing, colisões, open addressing, `__hash__`, `__eq__`)*

---

**3.4** — Árvores
*(BST, travessias, heaps, `heapq`, filas de prioridade)*

---

**3.5** — Grafos
*(Lista de adjacência vs matriz, BFS, DFS, Dijkstra, ordenação topológica)*

---

**3.6** — Algoritmos de ordenação
*(Bubble, merge sort, quicksort, timsort — o algoritmo interno do Python)*

---

**3.7** — Técnicas algorítmicas fundamentais
*(Divisão e conquista, programação dinâmica, greedy, backtracking)*

---
---

## MÓDULO 4 — PARADIGMAS DE PROGRAMAÇÃO

---

**4.1** — Programação imperativa e procedural
*(Sequência de instruções, estado, quando é a escolha certa)*

---

**4.2** — Orientação a objetos com profundidade real
*(Dunder methods, MRO, algoritmo C3, `super()`, composição vs herança)*

---

**4.3** — Programação funcional
*(`map`, `filter`, `reduce`, comprehensions, `functools`, `itertools`)*

---

**4.4** — Duck typing e orientação a protocolos
*(Structural subtyping, `abc`, protocolos implícitos do Python)*

---
---

## MÓDULO 5 — PYTHON AVANÇADO: MECANISMOS INTERNOS

---

**5.1** — Iteradores e geradores
*(`__iter__`, `__next__`, `yield`, `yield from`, lazy evaluation)*

---

**5.2** — Decoradores com profundidade
*(Decoradores com argumentos, decoradores de classe, `functools.wraps`)*

---

**5.3** — Context managers customizados
*(`__enter__`/`__exit__`, `contextlib.contextmanager`)*

---

**5.4** — Metaclasses
*(`type`, `__new__` vs `__init__`, aplicações em ORMs e frameworks)*

---

**5.5** — Descritores
*(`__get__`, `__set__`, `__delete__`, base de `@property` e ORMs)*

---

**5.6** — `__slots__`
*(Redução de memória em classes com muitas instâncias, limitações com herança)*

---

**5.7** — Protocolo de importação
*(`sys.modules`, `sys.path`, finders, loaders, importação lazy)*

---
---

## MÓDULO 6 — ENGENHARIA DE SOFTWARE APLICADA

---

**6.1** — Testes automatizados
*(`unittest`, `pytest`, fixtures, mocking, `hypothesis`, TDD)*

---

**6.2** — Princípios SOLID em Python
*(SRP, OCP, LSP, ISP, DIP — com exemplos reais, não teóricos)*

---

**6.3** — Design Patterns: Criacionais
*(Singleton, Factory, Abstract Factory, Builder, Prototype)*

---

**6.4** — Design Patterns: Estruturais
*(Adapter, Decorator, Facade, Proxy, Composite)*

---

**6.5** — Design Patterns: Comportamentais
*(Observer, Strategy, Command, State, Template Method)*

---

**6.6** — Refatoração e código limpo
*(Code smells, técnicas de refatoração, `pylint`, `black`, `mypy`)*

---

**6.7** — Type hints e tipagem estática gradual
*(`mypy`, `typing`, `Protocol`, genéricos, tipagem nominal vs estrutural)*

---

**6.8** — Documentação como engenharia
*(Docstrings, Sphinx, filosofia de documentar o porquê e não o quê)*

---
---

## MÓDULO 7 — CONCORRÊNCIA E PARALELISMO

---

**7.1** — O GIL — Global Interpreter Lock
*(O que é, impacto em CPU-bound vs I/O-bound, quando realmente importa)*

---

**7.2** — Programação assíncrona com `asyncio`
*(Event loop, corrotinas, `async/await`, `gather`, `create_task`, `Queue`)*

---

**7.3** — Threading
*(`Thread`, `Lock`, `Semaphore`, race conditions, deadlocks, `ThreadPoolExecutor`)*

---

**7.4** — Multiprocessing
*(`Process`, `Pool`, `Queue`, `shared_memory`, `ProcessPoolExecutor`)*

---

**7.5** — `concurrent.futures` como abstração unificada
*(`Future`, `as_completed`, critério de escolha entre threads e processos)*

---
---

## MÓDULO 8 — PERFORMANCE E OTIMIZAÇÃO

---

**8.1** — Profiling como método científico
*(`cProfile`, `line_profiler`, `memory_profiler`, `tracemalloc`, `snakeviz`)*

---

**8.2** — Otimizações a nível de Python puro
*(Comprehensions, variáveis locais em loops, `join`, `__slots__`)*

---

**8.3** — NumPy e operações vetorizadas
*(Array N-dimensional, broadcasting, fancy indexing, `einsum`)*

---

**8.4** — Caching e memoização
*(`lru_cache`, `cache`, invalidação, Redis para cache distribuído)*

---

**8.5** — Cython
*(Transpilação para C, anotações de tipo, diferença entre Python-like e C real)*

---

**8.6** — Extensões em C com `ctypes` e `cffi`
*(ABI, ponteiros, mapeamento de tipos C para Python)*

---

**8.7** — Python/C API
*(`PyObject`, `Py_INCREF`, `Py_DECREF`, construção de módulos nativos)*

---

**8.8** — PyPy
*(JIT compiler, quando usar, limitações com extensões C)*

---
---

## MÓDULO 9 — ARQUITETURA DE SOFTWARE

---

**9.1** — Arquitetura em camadas
*(Presentation, application, domain, infrastructure, regra da dependência)*

---

**9.2** — Domain-Driven Design — DDD
*(Entidades, value objects, aggregates, repositories, domain events)*

---

**9.3** — Clean Architecture e Hexagonal
*(Ports & adapters, testabilidade do core, independência de frameworks)*

---

**9.4** — Event-Driven Architecture
*(Event sourcing, CQRS, Kafka, RabbitMQ, Redis Streams)*

---

**9.5** — Design de APIs e microserviços
*(REST, gRPC, Protocol Buffers, GraphQL, versionamento de API)*

---
---

## MÓDULO 10 — BANCO DE DADOS E PERSISTÊNCIA

---

**10.1** — SQL com profundidade
*(Normalização, índices, EXPLAIN ANALYZE, ACID, isolation levels, window functions)*

---

**10.2** — SQLAlchemy
*(Core vs ORM, N+1 queries, lazy loading, session lifecycle, Alembic)*

---

**10.3** — Redis
*(Estruturas de dados, pub/sub, TTL, Lua scripts, casos de uso reais)*

---

**10.4** — MongoDB
*(Documentos, índices, aggregation pipeline, quando faz sentido usar)*

---

**10.5** — Connection pooling e performance
*(asyncpg, configuração de pool size, custo real de uma conexão)*

---
---

## MÓDULO 11 — SEGURANÇA DE APLICAÇÕES

---

**11.1** — Criptografia aplicada
*(AES, RSA, ECDSA, bcrypt, argon2, HMAC, TLS — o que cada um protege)*

---

**11.2** — Vulnerabilidades web e defesas
*(SQL injection, XSS, CSRF, SSRF, Path Traversal, Command Injection)*

---

**11.3** — Autenticação e autorização
*(JWT, OAuth 2.0, OpenID Connect, RBAC, ABAC)*

---

**11.4** — Análise estática de segurança
*(`bandit`, `safety`, integração em pipeline de CI)*

---

**11.5** — Secrets management
*(Vault, AWS Secrets Manager, `python-dotenv`, boas práticas)*

---
---

## MÓDULO 12 — INTERNALS DO CPYTHON

---

**12.1** — Leitura do código-fonte do CPython
*(`Objects/`, `Python/`, `Lib/`, `listobject.c`, `dictobject.c`, `ceval.c`)*

---

**12.2** — Ciclo de vida de um objeto Python
*(`pymalloc`, reference counting, garbage collector, `weakref`)*

---

**12.3** — Frame objects e call stack
*(`PyFrameObject`, `inspect`, propagação de exceções, como `pdb` funciona)*

---

**12.4** — Bytecode e módulo `dis`
*(`LOAD_FAST`, `LOAD_GLOBAL`, por que variáveis locais são mais rápidas)*

---

**12.5** — PEPs fundamentais — leitura obrigatória
*(PEP 8, 20, 257, 343, 380, 492, 526, 572)*

---
---

## MÓDULO 13 — ECOSSISTEMA PROFISSIONAL E DEVOPS

---

**13.1** — Gestão de dependências e ambientes
*(`pip`, `venv`, `poetry`, `pyproject.toml`, semantic versioning)*

---

**13.2** — Containerização
*(Docker, multi-stage builds, Docker Compose, Kubernetes básico)*

---

**13.3** — CI/CD
*(GitHub Actions, pipelines, rolling update, blue/green, canary)*

---

**13.4** — Observabilidade
*(Logging estruturado, Prometheus, OpenTelemetry, logs vs métricas vs traces)*

---

**13.5** — Infraestrutura como código
*(Terraform, Ansible, Pulumi com Python)*

---
---

## MÓDULO 14 — DOMÍNIOS DE APLICAÇÃO AVANÇADOS

---

**14.1** — Ciência de Dados e Machine Learning
*(NumPy, Pandas vetorizado, Scikit-learn, PyTorch, autograd, MLflow, Airflow)*

---

**14.2** — APIs de alta performance
*(FastAPI, ASGI vs WSGI, Pydantic, dependency injection, WebSockets)*

---

**14.3** — Sistemas distribuídos
*(Teorema CAP, Celery, Kafka, circuit breaker, saga pattern)*

---

**14.4** — Automação e DevOps programático
*(Fabric, Paramiko, `subprocess`, boto3, testinfra)*

---
---

## COMO USAR ESTE ÍNDICE

Copie qualquer item e mande assim:

> **"Me ensina o item 5.2 — Decoradores com profundidade. Quero explicação teórica, exemplos reais de código e um exercício para praticar."**

Depois volta com seu código para eu revisar.

**Um item por vez. Na ordem. Sem pular.**