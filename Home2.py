import matplotlib.pyplot as plt

def priority_encoder(X):
    if X[0] == 1:
        return (0, 0, 0) # X1
    elif X[1] == 1:
        return (0, 1, 0) # X2
    elif X[2] == 1:
        return (1, 0, 0) # X3
    elif X[3] == 1:
        return (1, 1, 0) # X4
    else:
        return (0, 0, 1)


inputs = [0, 0, 1, 0] # Входные сигналы
output = priority_encoder(inputs)
print(f"Выход: a1={output[0]}, a0={output[1]}, E={output[2]}")

# Входные сигналы
signals = [inputs]
labels = ['X1', 'X2', 'X3', 'X4']
plt.bar(labels, signals[0])
plt.title('Входные сигналы')
plt.ylabel('Сигнал')
plt.show()

# Выходные сигналы
output_signals = [output[0], output[1], output[2]] # E и двоичный код
plt.bar(['a1', 'a0', 'E'], output_signals)
plt.title('Выходные сигналы')
plt.ylabel('Сигнал')
plt.show()