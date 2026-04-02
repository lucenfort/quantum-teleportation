# Teletransporte Quântico: Teoria e Fundamentos Matemáticos

## Estados de Bell (Estados Maximamente Emaranhados)

Os quatro estados de Bell formam uma base ortonormal completa para sistemas de 2 qubits. Eles representam correlações quânticas perfeitas e são fundamentais para o teletransporte quântico.

### Definição

Os quatro estados de Bell são definidos como:

$$|\Phi^+\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)$$

$$|\Phi^-\rangle = \frac{1}{\sqrt{2}} (|00\rangle - |11\rangle)$$

$$|\Psi^+\rangle = \frac{1}{\sqrt{2}} (|01\rangle + |10\rangle)$$

$$|\Psi^-\rangle = \frac{1}{\sqrt{2}} (|01\rangle - |10\rangle)$$

### Propriedades Matemáticas

Cada estado de Bell apresenta **emaranhamento maximal**, caracterizado por:

- **Pureza**: $\text{Tr}(\rho^2) = 1$ (estado puro)
- **Concorrência**: $C = 1$ (medida máxima de emaranhamento)
- **Decomposição de Schmidt**: Cada estado se decompõe em exatamente 2 componentes ortogonais

### Circuito de Criação

Os estados de Bell são gerados usando:

1. **Porta de Hadamard** no primeiro qubit: $H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$

2. **Porta CNOT** (Controlled-NOT):
   $$\text{CNOT} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

Para $|\Phi^+\rangle$: Aplicar $H \otimes I$, depois CNOT

## Protocolo de Teletransporte Quântico

### Visão Geral

O teletransporte quântico permite transferir informações de estado quântico de um qubit (remetente) para outro (receptor) usando:
- Par emaranhado pré-compartilhado (par de Bell)
- 2 bits de informação clássica
- Operações quânticas locais

### Etapas do Protocolo

**Etapa 1: Distribuição de Emaranhamento**

Alice e Bob compartilham um par emaranhado. O qubit 1 pertence a Alice, qubit 2 para Bob:

$$|\Psi_0\rangle = |\psi\rangle \otimes \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle)$$

onde o estado quântico a ser teletransportado é: $|\psi\rangle = \alpha|0\rangle + \beta|1\rangle$

**Etapa 2: Medição de Bell (Alice)**

Alice realiza medição de Bell nos qubits 0 e 1, projetando para um dos quatro resultados:

$$\{|\Phi^+\rangle, |\Phi^-\rangle, |\Psi^+\rangle, |\Psi^-\rangle\}$$

Essa medição produz 2 bits clássicos: $m_0, m_1 \in \{0,1\}$

**Etapa 3: Comunicação Clássica**

Alice envia o resultado da medição de 2 bits para Bob através de um canal clássico.

**Etapa 4: Operações de Correção (Bob)**

Com base nos bits recebidos, Bob aplica uma de quatro operações:

| $m_0$ | $m_1$ | Operação |
|-------|-------|-----------|
| 0 | 0 | Identidade: $I$ |
| 0 | 1 | Pauli-$X$: $\sigma_x = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$ |
| 1 | 0 | Pauli-$Z$: $\sigma_z = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ |
| 1 | 1 | Pauli-$Y$: $\sigma_y = \begin{pmatrix} 0 & -i \\ i & 0 \end{pmatrix}$ |

Após aplicar a correção, o qubit de Bob contém o estado original:

$$|\psi\rangle_{\text{Bob}} = \alpha|0\rangle + \beta|1\rangle$$

## Observações-Chave

### Teorema da Não-Clonagem

O protocolo respeita o **teorema da não-clonagem**: a medição de Alice colapsa seus qubits, destruindo o estado original. Somente Bob termina com o estado.

### Bits Clássicos Necessários

O teletransporte requer 2 bits clássicos por qubit teletransportado. Como informações quânticas não podem ser comprimidas, isso representa a comunicação clássica mínima necessária.

### Custo de Recursos

- **Pares emaranhados**: 1 par de Bell por qubit
- **Bits clássicos**: 2 por qubit
- **Portas quânticas**: $2 \times \text{CNOT} + 1 \times H + 2 \times \text{Medição}$

## Notas de Implementação

Esta implementação usa o simulador Qiskit Aer:
- Simulação de vetor de estado para cálculos de probabilidade exata
- Amostragem de medição para validação estatística
- Portas condicionais para operações de correção de Bob

## Referências

- Nielsen, M. A., & Chuang, I. L. (2010). Quantum Computation and Quantum Information.
- Documentação Qiskit: https://qiskit.org/
