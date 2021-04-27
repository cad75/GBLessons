# Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. Выполнить над числом 5 побитовый сдвиг
# вправо и влево на два знака. Объяснить полученный результат.
five_n = 5
six_n = 6
print(bin(five_n | six_n))
print(bin(five_n & six_n))
print(bin(five_n ^ six_n))
print(bin(~ six_n))
print(bin(five_n >> 2))
print(bin(five_n << 2))
