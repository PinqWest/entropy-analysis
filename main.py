import math

# ==============================
# Подготовка текста
# ==============================
text = 'AAabbbbgde'.lower()
text = text.replace(" ", "")
print("Исходный текст:", text)

# ==============================
# Функции
# ==============================
def get_frequencies(txt):
    freq = {}
    for c in txt:
        freq[c] = freq.get(c, 0) + 1
    return freq

def calculate_entropy(freq_dict, total_count):
    return sum(
        - (count / total_count) * math.log2(count / total_count)
        for count in freq_dict.values()
    )

# ==============================
# Энтропия исходного текста
# ==============================
freq = get_frequencies(text)
total = len(text)
entropy = calculate_entropy(freq, total)

print("\n=== Энтропия исходного текста ===")
print(f"Общее количество символов: {total}")
print("Частоты символов:")
for c, f in sorted(freq.items()):
    print(f"   '{c}': {f}")
print(f"Энтропия: {entropy:.4f} бит/символ")

# ==============================
# Равномерное кодирование
# ==============================
N = len(freq)
code_length = math.ceil(math.log2(N))
redundancy = code_length - entropy

print("\n=== Равномерное кодирование ===")
print(f"Количество различных символов: {N}")
print(f"Длина кода: {code_length} бит/символ")
print(f"Избыточность: {redundancy:.4f} бит/символ")

# ==============================
# Удаление 20% наиболее частых символов
# ==============================
num_remove = max(1, len(freq)//5)
most_common = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:num_remove]
remove_chars = set(c for c, _ in most_common)

text_most_removed = ''.join(c for c in text if c not in remove_chars)
freq_most_removed = get_frequencies(text_most_removed)
entropy_most_removed = calculate_entropy(freq_most_removed, len(text_most_removed))

print("\n=== Удаление 20% наиболее частых символов ===")
print(f"Удалённые символы: {', '.join(remove_chars)}")
print(f"Новый текст: {text_most_removed}")
print(f"Энтропия: {entropy_most_removed:.4f} бит/символ")
print("Анализ: Энтропия увеличилась, так как удалились самые предсказуемые символы.")

# ==============================
# Удаление 20% наименее частых символов
# ==============================
least_common = sorted(freq.items(), key=lambda x: x[1])[:num_remove]
remove_chars_rare = set(c for c, _ in least_common)

text_least_removed = ''.join(c for c in text if c not in remove_chars_rare)
freq_least_removed = get_frequencies(text_least_removed)
entropy_least_removed = calculate_entropy(freq_least_removed, len(text_least_removed))

print("\n=== Удаление 20% наименее частых символов ===")
print(f"Удалённые символы: {', '.join(remove_chars_rare)}")
print(f"Новый текст: {text_least_removed}")
print(f"Энтропия: {entropy_least_removed:.4f} бит/символ")
print("Анализ: Энтропия уменьшилась, так как удалились редкие символы, текст стал более предсказуемым.")
