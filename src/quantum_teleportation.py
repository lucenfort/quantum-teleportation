"""
Protocolo de Teletransporte Quântico

Implementação completa de teletransporte quântico usando Qiskit.
Demonstra: distribuição de emaranhamento, medição de Bell e operações corretivas.

Protocolo:
1. Preparar estado a teletransportar no qubit 0: |ψ⟩ = α|0⟩ + β|1⟩
2. Criar par de Bell (emaranhamento) entre qubits 1 e 2
3. Realizar medição de Bell nos qubits 0 e 1 (2 bits clássicos)
4. Aplicar operações corretivas no qubit 2 baseado nos resultados de medição
5. Medir qubit 2 para verificar teletransporte
"""

from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


# Paleta de cores - Tema Dark Neon
COLORS = {
    'bg_dark': '#0D0221',      # Roxo/preto bem escuro
    'accent': '#FF006E',        # Rosa/vermelho neon
    'highlight': '#00F5FF',     # Ciano brilhante/neon
    'secondary': '#FFBE0B',     # Amarelo neon
    'grid': '#1A1A2E',          # Cinza azulado escuro
    'text': '#EAEAEA'           # Branco off
}


def create_teleportation_circuit(apply_x=True):
    """
    Cria um circuito de teletransporte quântico com 3 qubits e 3 bits clássicos.
    
    Qubits:
    - q[0]: Qubit a ser teletransportado
    - q[1]: Metade de Alice do par de Bell
    - q[2]: Metade de Bob do par de Bell (recebe estado teletransportado)
    
    Bits clássicos:
    - c[0]: Resultado de medição de q[0]
    - c[1]: Resultado de medição de q[1]
    - c[2]: Medição final de q[2]
    
    Args:
        apply_x: Se True, aplica porta X para preparar qubit 0 como na declaração do problema
    """
    qr = QuantumRegister(3, 'q')
    cr = ClassicalRegister(3, 'c')
    qc = QuantumCircuit(qr, cr, name='Quantum Teleportation')
    
    # ETAPA 1: Preparar estado a teletransportar
    # Declaração do problema: "Preparar o estado do qubit 0 a ser teletransportado. Aplicar o operador X."
    if apply_x:
        qc.x(qr[0])
    
    qc.barrier(label='Preparar estado')
    
    # ETAPA 2: Criar par de Bell (par emaranhado) entre qubits 1 e 2
    # Criar |Φ⁺⟩ = 1/√2 (|00⟩ + |11⟩)
    qc.h(qr[1])
    qc.cx(qr[1], qr[2])
    
    qc.barrier(label='Criar emaranhamento')
    
    # ETAPA 3: Medição de Bell (Alice realiza medição nos qubits 0 e 1)
    # Aplicar CNOT com q[0] como controle, q[1] como alvo
    qc.cx(qr[0], qr[1])
    # Aplicar Hadamard ao q[0]
    qc.h(qr[0])
    
    # Medir qubits 0 e 1
    qc.measure([qr[0], qr[1]], [cr[0], cr[1]])
    
    qc.barrier(label='Medição de Bell')
    
    # ETAPA 4: Operações condicionais baseadas nos resultados de medição
    # Aplicar operações corretivas baseado nos resultados da medição de Bell
    # Se c[1] == 1, aplicar porta X; se c[0] == 1, aplicar porta Z
    with qc.if_test((cr[1], 1)):
        qc.x(qr[2])
    
    with qc.if_test((cr[0], 1)):
        qc.z(qr[2])
    
    qc.barrier(label='Aplicar correções')
    
    # ETAPA 5: Medir o estado recuperado
    qc.measure(qr[2], cr[2])
    
    return qc


def run_teleportation_experiment(shots=1024):
    """
    Executa teletransporte quântico no simulador Qiskit Aer.
    
    Args:
        shots: Número de medições (padrão: 1024)
    
    Returns:
        Circuito e resultados de medição
    """
    qc = create_teleportation_circuit(apply_x=True)
    
    simulator = AerSimulator()
    
    # Execute circuit
    job = simulator.run(qc, shots=shots)
    result = job.result()
    counts = result.get_counts(qc)
    
    return qc, counts


def analyze_teleportation_results(counts):
    """
    Analisa resultados de teletransporte para verificar sucesso do protocolo.
    
    Comportamento esperado:
    - Se porta X foi aplicada, qubit 2 deve medir como |1⟩ com ~100% de probabilidade
    - Isso confirma teletransporte bem-sucedido do estado |1⟩
    """
    print("\n" + "="*60)
    print("RESULTADOS DO TELETRANSPORTE QUÂNTICO")
    print("="*60)
    
    print("\nResultados de Medição (formato: c[2]c[1]c[0]):")
    print(f"  {counts}\n")
    
    # Extrair medição do qubit final (bit menos significativo)
    final_bit_counts = {'0': 0, '1': 0}
    for measurement, count in counts.items():
        final_bit = measurement[0]  # Primeiro bit é c[2] (medição final)
        final_bit_counts[final_bit] += count
    
    total_shots = sum(final_bit_counts.values())
    
    print("Estado Final do Qubit 2 (Teletransportado para Bob):")
    print(f"  |0⟩: {final_bit_counts['0']:4d} ({final_bit_counts['0']/total_shots*100:5.1f}%)")
    print(f"  |1⟩: {final_bit_counts['1']:4d} ({final_bit_counts['1']/total_shots*100:5.1f}%)")
    
    success_rate = max(final_bit_counts.values()) / total_shots * 100
    print(f"\nTaxa de Sucesso do Teletransporte: {success_rate:.1f}%")
    
    if success_rate > 95:
        print("✓ Protocolo bem-sucedido: Estado teletransportado corretamente!")
    else:
        print("✗ Resultado do protocolo: Verifique implementação do circuito")
    
    return final_bit_counts


def visualize_teleportation():
    """
    Executa experimento de teletransporte completo e visualiza resultados com estilo profissional.
    """
    qc, counts = run_teleportation_experiment(shots=1024)
    
    # Display circuit
    print("\nCircuito de Teletransporte Quântico:")
    print(qc)
    
    # Analyze and visualize results
    final_bit_counts = analyze_teleportation_results(counts)
    
    # Create results directory if it doesn't exist
    results_dir = Path('resultados')
    results_dir.mkdir(exist_ok=True)
    
    # Create figure with professional styling
    fig = plt.figure(figsize=(18, 8))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    
    # Main title
    fig.text(0.5, 0.97, 'Resultados do Protocolo de Teletransporte Quântico', 
             ha='center', va='top', fontsize=22, fontweight='bold',
             color=COLORS['highlight'])
    
    fig.text(0.5, 0.93, '1024 medições', 
             ha='center', va='top', fontsize=11,
             color=COLORS['secondary'], style='italic')
    
    # Left plot: All measurement outcomes
    ax1 = fig.add_subplot(1, 2, 1)
    ax1.set_facecolor(COLORS['grid'])
    
    outcomes = sorted(counts.keys())
    values = [counts[outcome] for outcome in outcomes]
    total = sum(values)
    percentages = [v/total*100 for v in values]
    
    bars1 = ax1.bar(range(len(outcomes)), values, color=COLORS['accent'],
                    edgecolor=COLORS['highlight'], linewidth=2.5, alpha=0.9, width=0.7)
    
    for idx, (bar, val, pct) in enumerate(zip(bars1, values, percentages)):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{val}\n({pct:.1f}%)',
                ha='center', va='bottom', fontsize=10, fontweight='bold',
                color=COLORS['secondary'])
    
    ax1.set_xticks(range(len(outcomes)))
    ax1.set_xticklabels(outcomes, fontsize=11, fontweight='bold')
    ax1.set_xlabel('Resultado de Medição (c[2]c[1]c[0])', fontsize=12, fontweight='bold',
                   color=COLORS['highlight'], labelpad=10)
    ax1.set_ylabel('Contagens', fontsize=12, fontweight='bold',
                   color=COLORS['highlight'], labelpad=10)
    ax1.set_title('Todos os Resultados de Medição de Bell', fontsize=13, fontweight='bold',
                  color=COLORS['highlight'], pad=15)
    
    ax1.grid(True, color=COLORS['highlight'], alpha=0.15, linewidth=0.8, linestyle='--')
    ax1.set_axisbelow(True)
    
    for spine in ax1.spines.values():
        spine.set_color(COLORS['highlight'])
        spine.set_linewidth(2)
    ax1.tick_params(colors=COLORS['text'], labelsize=11, width=1.5, length=5)
    ax1.set_ylim(0, max(values) * 1.15)
    
    # Right plot: Final teleported state
    ax2 = fig.add_subplot(1, 2, 2)
    ax2.set_facecolor(COLORS['grid'])
    
    states = ['|0⟩', '|1⟩']
    final_values = [final_bit_counts.get('0', 0), final_bit_counts.get('1', 0)]
    final_total = sum(final_values)
    final_percentages = [v/final_total*100 if final_total > 0 else 0 for v in final_values]
    
    # Use special color for successful teleportation
    bar_colors = [COLORS['accent'] if pct > 50 else COLORS['secondary'] 
                  for pct in final_percentages]
    
    bars2 = ax2.bar(range(len(states)), final_values, color=bar_colors,
                    edgecolor=COLORS['highlight'], linewidth=2.5, alpha=0.9, width=0.5)
    
    for idx, (bar, val, pct) in enumerate(zip(bars2, final_values, final_percentages)):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height,
                f'{val}\n({pct:.1f}%)',
                ha='center', va='bottom', fontsize=12, fontweight='bold',
                color=COLORS['secondary'])
    
    ax2.set_xticks(range(len(states)))
    ax2.set_xticklabels(states, fontsize=13, fontweight='bold')
    ax2.set_xlabel('Estado do Qubit 2 (Bob)', fontsize=12, fontweight='bold',
                   color=COLORS['highlight'], labelpad=10)
    ax2.set_ylabel('Contagens', fontsize=12, fontweight='bold',
                   color=COLORS['highlight'], labelpad=10)
    ax2.set_title('Sucesso do Teletransporte Quântico', fontsize=13, fontweight='bold',
                  color=COLORS['highlight'], pad=15)
    
    ax2.grid(True, color=COLORS['highlight'], alpha=0.15, linewidth=0.8, linestyle='--')
    ax2.set_axisbelow(True)
    
    for spine in ax2.spines.values():
        spine.set_color(COLORS['highlight'])
        spine.set_linewidth(2)
    ax2.tick_params(colors=COLORS['text'], labelsize=11, width=1.5, length=5)
    ax2.set_ylim(0, final_total * 1.15)
    
    plt.tight_layout(rect=[0, 0, 1, 0.92])
    plt.savefig(results_dir / 'teleportation.png', dpi=300, bbox_inches='tight',
                facecolor=COLORS['bg_dark'], edgecolor='none')
    print(f"\n✓ Visualização de teletransporte salva em 'resultados/teleportation.png'")
    plt.show()
    
    return qc, counts


if __name__ == '__main__':
    visualize_teleportation()
