# Desafio Oficial: Estados de Bell e Teletransporte Quântico

## 1. Estados de Bell e Emaranhamento Quântico

Os estados de Bell são muito importantes para a computação e comunicação quântica, pois exemplificam o fenômeno do **emaranhamento quântico**, onde as propriedades dos qubits estão intimamente conectadas, independentemente da distância que os separa.

Aproveite o exemplo apresentado na trilha e crie um código para gerar os 4 estados de Bell emaranhados. Plote o histograma e visualize os resultados.

Para executar tal tarefa você vai precisar aplicar a(s) porta(s) lógica(s) corretamente:

$$|\Phi^{00}\rangle = \frac{1}{\sqrt{2}} (|00\rangle + |11\rangle)$$

$$|\Phi^{10}\rangle = \frac{1}{\sqrt{2}} (|00\rangle - |11\rangle)$$

$$|\Psi^{01}\rangle = \frac{1}{\sqrt{2}} (|01\rangle + |10\rangle)$$

$$|\Psi^{11}\rangle = \frac{1}{\sqrt{2}} (|01\rangle - |10\rangle)$$

## 2. Projeto de Teletransporte Quântico

Para executar o projeto de Teletransporte Quântico coloque em prática os passos abaixo:

1. Instale os pacotes e importe as bibliotecas necessárias para executar o projeto

2. Crie um circuito quântico com 3 qubits e 3 bits clássicos

3. **Etapa 1:** Crie um par emaranhado entre o qubit 1 e o qubit 2

4. **Etapa 2:** Prepare o qubit 0 no estado a ser teletransportado. Atue com o operador X

5. **Etapa 3:** Execute a medição de Bell no qubit 0 e qubit 1

6. Use o simulador Qiskit Aer para executar o circuito

7. Obtenha a contagem e visualize os resultados

8. **Etapa 4:** Aplique operações condicionais com base nos resultados da medição

9. **Etapa 5:** Meça o qubit 2 e veja o estado do qubit 0 teletransportado

10. Use o simulador Qiskit Aer para executar o circuito

11. Obtenha a contagem e visualize os resultados

12. Analise o resultado final