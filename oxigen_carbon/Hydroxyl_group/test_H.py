from ase.build import graphene
from ase.io import read
import numpy as np

slab = read('POSCAR')  # или 'POSCAR.vasp', 'CONTCAR'

# Увеличиваем вакуум ТОЛЬКО по направлению a
# Умножаем первый вектор ячейки на коэффициент
vacuum_a = 20.0  # Хотим 20 Å вакуума по a
current_length_a = np.linalg.norm(cell[0])
scaling_factor = (current_length_a + vacuum_a)/current_length_a

cell[0] = cell[0] * scaling_factor
slab.set_cell(cell)

# Центрируем атомы в новой ячейке
slab.center()



print(atoms)  # Информация о системе
