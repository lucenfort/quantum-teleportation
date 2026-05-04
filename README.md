# Teletransporte Quântico

<p align="center">
  <img src="./assets/banner.svg" alt="Project Banner" width="100%" />
</p>

<p align="left">
	<img src="https://img.shields.io/badge/Python-3.9+-FFD700?style=for-the-badge&logo=python&logoColor=111111&labelColor=0B0B0B" alt="Python" />
	<img src="https://img.shields.io/badge/Qiskit-00FFF7?style=for-the-badge&logo=qiskit&logoColor=111111&labelColor=0B0B0B" alt="Qiskit" />
	<img src="https://img.shields.io/badge/Status-Finalizado-FF00FF?style=for-the-badge&logoColor=111111&labelColor=0B0B0B" alt="Status" />
</p>

Simulação de emaranhamento quântico e protocolo de teletransporte utilizando Qiskit. Demonstração prática de como estados quânticos podem ser transferidos entre qubits através de recursos clássicos e emaranhamento.

## [>] SYS.NAVEGAÇÃO

[Estrutura](#-estrutura-do-projeto) • [Instalação](#-instalação) • [Uso](#-uso) • [Teoria](#-resumo-do-problema) • [Resultados](#-resultados)

---

## [=] ESTRUTURA_PROJETO

```
quantum-teleportation/
├── assets/               # HUDs e Banner Cyberpunk
├── docs/                 # Fundamentos matemáticos e desafios
├── resultados/           # Plots de circuitos e medições
├── src/                  # Código fonte principal
│   ├── main.py           # Pipeline completo de execução
│   ├── bell_states.py    # Geração de estados emaranhados
│   └── quantum_teleportation.py # Protocolo de teletransporte
├── requirements.txt      # Dependências (Qiskit, Aer, MPL)
└── README.md             # Documentação técnica
```

---

## [*] INSTALAÇÃO_E_EXECUÇÃO

### 1. Preparar Ambiente
```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
pip install -r requirements.txt
```

### 2. Executar Experimentos
Para rodar o pipeline completo (Bell States + Teleportation):
```bash
python src/main.py
```

Os resultados visuais serão salvos automaticamente na pasta `resultados/`.

---

## [~] RESUMO_DO_PROBLEMA

### Experimento 1: Estados de Bell
Geração dos 4 estados maximamente emaranhados (`|Φ⁺⟩`, `|Φ⁻⟩`, `|Ψ⁺⟩`, `|Ψ⁻⟩`) utilizando portas Hadamard e CNOT.

### Experimento 2: Teletransporte Quântico
1. **Preparação**: Estado a teletransportar preparado em `q[0]`.
2. **Emaranhamento**: Criação de par de Bell entre Alice (`q[1]`) e Bob (`q[2]`).
3. **Medição**: Alice realiza medição de Bell em `q[0]` e `q[1]`.
4. **Correção**: Bob aplica portas `X` ou `Z` em `q[2]` baseado nos resultados de Alice.
5. **Verificação**: Medição final de `q[2]` para confirmar a recepção do estado.

---

## [#] RESULTADOS_SISTEMA

### Estados de Bell
Distribuição de probabilidade característica dos pares emaranhados.
![Estados de Bell](resultados/bell_states.png)

### Teletransporte Quântico
Fidelidade de 100% atingida em simulador Aer.
![Teletransporte Quântico](resultados/teleportation.png)

---

