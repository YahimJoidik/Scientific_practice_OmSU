#Испрользовать для получения вакуума по вектору трансляции a.
from ase.build import graphene
import numpy as np

slab = graphene(formula='C2', a=2.46, size=(4, 4, 1), vacuum=10.0)

# Увеличиваем вакуум ТОЛЬКО по направлению a
# Умножаем первый вектор ячейки на коэффициент
vacuum_a = 10.0  # Хотим 10 Å вакуума по a
current_length_a = np.linalg.norm(slab.cell[0])
scaling_factor = (current_length_a + vacuum_a)/current_length_a

slab.cell[0] = slab.cell[0] * scaling_factor
slab.set_cell(slab.cell)

# Центрируем атомы в новой ячейке
slab.center()

slab.write('POSCAR_vacuum_a')


#Испрользовать для получения вакуума по вектору трансляции b.
from ase.build import graphene
import numpy as np

slab = graphene(formula='C2', a=2.46, size=(4, 4, 1), vacuum=10.0)

# Увеличиваем вакуум ТОЛЬКО по направлению a
# Умножаем первый вектор ячейки на коэффициент
vacuum_b = 10.0  # Хотим 10 Å вакуума по b
current_length_b = np.linalg.norm(slab.cell[1])
scaling_factor = (current_length_b + vacuum_b)/current_length_b

slab.cell[1] = slab.cell[1] * scaling_factor
slab.set_cell(slab.cell)

# Центрируем атомы в новой ячейке
slab.center()

slab.write('POSCAR_vacuum_b')
