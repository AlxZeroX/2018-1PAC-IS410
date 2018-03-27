# caso 1
import paquete.sub_paquete.sub_sub_paquete.fibonacci

paquete.sub_paquete.sub_sub_paquete.fibonacci.print_fibonacci(10)

# caso 2
from paquete.sub_paquete.sub_sub_paquete.fibonacci import print_fibonacci

print_fibonacci(10)

# caso 3
from paquete.sub_paquete.sub_sub_paquete import fibonacci

fibonacci.print_fibonacci(10)

# caso 4
import paquete.sub_paquete.sub_sub_paquete.fibonacci as fibonacci

fibonacci.print_fibonacci(10)
