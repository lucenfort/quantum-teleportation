"""
Script principal de execução para demonstrações de Teletransporte Quântico e Estados de Bell.

Este script executa ambos os experimentos:
1. Estados de Bell: Geração e visualização de 4 estados emaranhados maximais
2. Teletransporte Quântico: Implementação completa do protocolo de teletransporte
"""

import sys
from pathlib import Path

# Add src directory to path
sys.path.insert(0, str(Path(__file__).parent))

from bell_states import visualize_bell_states
from quantum_teleportation import visualize_teleportation


def print_header():
    """Imprime cabeçalho formatado."""
    print("\n")
    print("╔" + "="*58 + "╗")
    print("║" + " "*58 + "║")
    print("║" + "  COMPUTAÇÃO QUÂNTICA: ESTADOS DE BELL & TELETRANSPORTE".center(58) + "║")
    print("║" + " "*58 + "║")
    print("╚" + "="*58 + "╝")


def print_separator(title=""):
    """Imprime separador formatado."""
    if title:
        print(f"\n\n{'─'*20} {title} {'─'*20}\n")
    else:
        print(f"\n{'─'*60}\n")


def main():
    """Executa todas as demonstrações."""
    print_header()
    
    # Run Bell States Experiment
    print_separator("EXPERIMENTO 1: ESTADOS DE BELL")
    print("Gerando e medindo todos os quatro estados de Bell emaranhados maximais...")
    bell_results = visualize_bell_states()
    
    # Run Quantum Teleportation Experiment
    print_separator("EXPERIMENTO 2: TELETRANSPORTE QUÂNTICO")
    print("Executando protocolo de teletransporte quântico (3 qubits, 3 bits clássicos)...")
    qc, teleportation_counts = visualize_teleportation()
    
    # Summary
    print_separator("RESUMO")
    print("""
✓ Experimento de Estados de Bell:
  - Gerados 4 estados de Bell emaranhados maximais
  - Medição e visualização bem-sucedidas de distribuições de probabilidade
  
✓ Experimento de Teletransporte Quântico:
  - Emaranhamento estabelecido entre qubits 1 e 2
  - Estado quântico preparado no qubit 0 (porta X aplicada)
  - Medição de Bell realizada nos qubits 0 e 1
  - Portas corretivas aplicadas baseado nos resultados de medição
  - Teletransporte do estado bem-sucedido para qubit 2
  - Estado final verificado através de medição

Para fundamentos matemáticos detalhados, veja docs/THEORY.md
""")
    
    print("\n" + "="*60)
    print("Execução Completa!")
    print("="*60 + "\n")


if __name__ == '__main__':
    main()
