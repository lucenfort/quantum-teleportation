"""
Geração e Visualização de Estados de Bell

Gera os quatro estados de Bell maximamente emaranhados e os visualiza
usando o simulador Qiskit Aer com saída de histogramas.

Referência matemática:
- |Φ⁺⟩ = 1/√2 (|00⟩ + |11⟩)
- |Φ⁻⟩ = 1/√2 (|00⟩ - |11⟩)
- |Ψ⁺⟩ = 1/√2 (|01⟩ + |10⟩)
- |Ψ⁻⟩ = 1/√2 (|01⟩ - |10⟩)
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


def create_bell_state_phi_plus():
    """
    Creates the |Φ⁺⟩ Bell state: 1/√2 (|00⟩ + |11⟩)
    
    Circuit:
    - Apply Hadamard to first qubit
    - Apply CNOT with first qubit as control, second as target
    """
    qc = QuantumCircuit(2, 2, name='|Φ⁺⟩')
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


def create_bell_state_phi_minus():
    """
    Cria o estado de Bell |Φ⁻⟩: 1/√2 (|00⟩ - |11⟩)
    
    Circuito:
    - Aplicar Pauli-Z ao primeiro qubit
    - Aplicar Hadamard ao primeiro qubit
    - Aplicar CNOT
    """
    qc = QuantumCircuit(2, 2, name='|Φ⁻⟩')
    qc.z(0)
    qc.h(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


def create_bell_state_psi_plus():
    """
    Creates the |Ψ⁺⟩ Bell state: 1/√2 (|01⟩ + |10⟩)
    
    Circuit:
    - Apply Hadamard to first qubit
    - Apply CNOT with first qubit as control, second as target
    - Apply X to second qubit
    """
    qc = QuantumCircuit(2, 2, name='|Ψ⁺⟩')
    qc.h(0)
    qc.cx(0, 1)
    qc.x(1)
    qc.measure([0, 1], [0, 1])
    return qc


def create_bell_state_psi_minus():
    """
    Creates the |Ψ⁻⟩ Bell state: 1/√2 (|01⟩ - |10⟩)
    
    Circuit:
    - Apply X to second qubit: |01⟩
    - Apply Hadamard to first qubit: creates superposition
    - Apply Z to first qubit: introduces phase -1
    - Apply CNOT: creates entanglement
    """
    qc = QuantumCircuit(2, 2, name='|Ψ⁻⟩')
    qc.x(1)
    qc.h(0)
    qc.z(0)
    qc.cx(0, 1)
    qc.measure([0, 1], [0, 1])
    return qc


def run_bell_state_experiment(circuit, shots=1024):
    """
    Executa circuito de estado de Bell no simulador Qiskit Aer.
    
    Args:
        circuit: Circuito quântico a executar
        shots: Número de medições (padrão: 1024)
    
    Returns:
        Dicionário com resultados de medição e contagens
    """
    simulator = AerSimulator()
    job = simulator.run(circuit, shots=shots)
    result = job.result()
    counts = result.get_counts(circuit)
    return counts


def visualize_bell_states():
    """
    Gera todos os quatro estados de Bell e visualiza resultados com estilo profissional.
    """
    bell_functions = [
        ('Φ⁺', create_bell_state_phi_plus),
        ('Φ⁻', create_bell_state_phi_minus),
        ('Ψ⁺', create_bell_state_psi_plus),
        ('Ψ⁻', create_bell_state_psi_minus)
    ]
    
    results = {}
    
    print("\n" + "="*60)
    print("GERAÇÃO E MEDIÇÃO DE ESTADOS DE BELL")
    print("="*60)
    
    for name, bell_func in bell_functions:
        circuit = bell_func()
        counts = run_bell_state_experiment(circuit, shots=1024)
        results[name] = (circuit, counts)
        
        print(f"\n|{name}⟩ Resultados do Estado de Bell:")
        print(f"  {counts}")
    
    # Create results directory if it doesn't exist
    results_dir = Path('resultados')
    results_dir.mkdir(exist_ok=True)
    
    # Create figure with professional styling
    fig = plt.figure(figsize=(16, 10))
    fig.patch.set_facecolor(COLORS['bg_dark'])
    gs = fig.add_gridspec(2, 2, hspace=0.35, wspace=0.3)
    
    # Main title
    fig.text(0.5, 0.98, 'Resultados das Medições dos Estados de Bell', 
             ha='center', va='top', fontsize=24, fontweight='bold',
             color=COLORS['highlight'])
    
    fig.text(0.5, 0.94, '1024 medições por estado', 
             ha='center', va='top', fontsize=12,
             color=COLORS['secondary'], style='italic')
    
    bell_states_info = {
        'Φ⁺': '1/√2 (|00⟩ + |11⟩)',
        'Φ⁻': '1/√2 (|00⟩ - |11⟩)',
        'Ψ⁺': '1/√2 (|01⟩ + |10⟩)',
        'Ψ⁻': '1/√2 (|01⟩ - |10⟩)'
    }
    
    for idx, (name, (circuit, counts)) in enumerate(results.items()):
        ax = fig.add_subplot(gs[idx // 2, idx % 2])
        
        # Set background
        ax.set_facecolor(COLORS['grid'])
        
        # Prepare data
        outcomes = sorted(counts.keys())
        values = [counts[outcome] for outcome in outcomes]
        total = sum(values)
        percentages = [v/total*100 for v in values]
        
        # Create bars
        bars = ax.bar(outcomes, values, color=COLORS['accent'], 
                     edgecolor=COLORS['highlight'], linewidth=2.5,
                     alpha=0.9, width=0.6)
        
        # Add value labels on bars
        for bar, val, pct in zip(bars, values, percentages):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{val}\n({pct:.1f}%)',
                   ha='center', va='bottom', fontsize=11, fontweight='bold',
                   color=COLORS['secondary'])
        
        # Styling
        ax.set_xlabel('Resultado da Medição', fontsize=12, fontweight='bold',
                     color=COLORS['highlight'], labelpad=10)
        ax.set_ylabel('Contagens', fontsize=12, fontweight='bold',
                     color=COLORS['highlight'], labelpad=10)
        
        # Title with state information
        ax.set_title(f'Estado |{name}⟩\n{bell_states_info[name]}',
                    fontsize=13, fontweight='bold',
                    color=COLORS['highlight'], pad=15)
        
        # Grid
        ax.grid(True, color=COLORS['highlight'], alpha=0.15, 
               linewidth=0.8, linestyle='--')
        ax.set_axisbelow(True)
        
        # Customize spines
        for spine in ax.spines.values():
            spine.set_color(COLORS['highlight'])
            spine.set_linewidth(2)
        
        # Customize ticks
        ax.tick_params(colors=COLORS['text'], labelsize=11, width=1.5, length=5)
        ax.xaxis.set_tick_params(labelbottom=True)
        
        # Set y-axis to start from 0 and add some padding
        ax.set_ylim(0, max(values) * 1.15)
    
    plt.savefig(results_dir / 'bell_states.png', dpi=300, bbox_inches='tight',
                facecolor=COLORS['bg_dark'], edgecolor='none')
    print(f"\n✓ Visualização de estados de Bell salva em 'resultados/bell_states.png'")
    plt.show()
    
    return results


if __name__ == '__main__':
    visualize_bell_states()
