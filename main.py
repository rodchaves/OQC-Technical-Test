from source.circuit import Circuit

def main():

    circuit_string = input('Enter a sequence of rations (angles must be integers): ')
    lengthZ = int(input('Enter the length of the Z gate (integer value): '))
    lengthX = int(input('Enter the length of the X gate (integer value): '))

    circuit = Circuit.from_string(circuit_string)

    circuit_XY_optimized = circuit.optimizationXY()
    circuit_XZ_optimized = circuit.optimizationXZ()
    running_time = circuit.hardware_running_time(lengthZ = lengthZ, lengthX = lengthX)

    print(f'\n Optimized circuit with XY: {circuit_XY_optimized}\n Optimized circuit with XZ: {circuit_XZ_optimized}\n Hardware running time: {running_time}\n')



if __name__ == '__main__':
    main()