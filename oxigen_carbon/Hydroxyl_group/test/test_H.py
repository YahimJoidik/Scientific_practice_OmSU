from ase.io import read, write
import numpy as np

atoms = read('POSCAR')

# 1. Запоминаем вектор O→H
o_pos = atoms.positions[-2]  # Кислород
h_pos = atoms.positions[-1]  # Водород
oh_vector = h_pos - o_pos

# 2. Переносим O в центр ячейки по Y
new_o_y = atoms.cell[1, 1] / 2
shift_y = new_o_y - o_pos[1]
atoms.positions[:, 1] += shift_y

# 3. Восстанавливаем H относительно O
atoms.positions[-1] = atoms.positions[-2] + oh_vector

# 4. Применяем периодические границы
atoms.wrap()

# 5. Проверяем
print(f"O: {atoms.positions[-2]}")
print(f"H: {atoms.positions[-1]}")
print(f"O-H расстояние: {np.linalg.norm(oh_vector):.3f} Å")
print(f"Дробная координата H по Y: {atoms.get_scaled_positions()[-1, 1]:.3f}")

write('POSCAR_perfectY.vasp', atoms, vasp5=True)
