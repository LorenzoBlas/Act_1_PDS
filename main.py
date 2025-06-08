import sys
from src.act_1 import continuous_signals, discrete_signals, plot_all_signals
from src.act_2 import continuous_sin, sine_plotter
from src.act_3 import continuous_sine, discrete_sine, signal_plotter
from src.act_4 import run


def main(arg):
    if arg[1] == "act_1":  
        time_cont, signals_cont = continuous_signals()
        time_disc, signals_disc = discrete_signals()
        plot_all_signals(time_cont, signals_cont, time_disc, signals_disc)
    elif arg[1] == "act_2":
        if len(arg) > 2:
            try:
                frequency = 0
                frequency = int(arg[2])
                sine_signal, time = continuous_sin(frequency)
                sine_plotter(sine_signal,frequency,time)
            except ValueError:
                print("Posible argumento fuera de los limites de la programacion (asegurese que el segundo argumento sea un numero entero")
    elif arg[1] == "act_3":
        if len(arg) > 4:
            try:
                amplitude = frequency = phase = K = 0
                amplitude = int(arg[2])
                frequency = int(arg[3])
                phase = float(arg[4])
                #data_signal = [amplitude, frequency, phase] 
                signal_xt, time = continuous_sine(amplitude, frequency, phase, K)
                
                amplitude = int(arg[2])
                frequency = int(arg[3])
                phase = float(arg[4])
                signal_xtn, time_disc = discrete_sine(amplitude, frequency, phase, K)
                
                amplitude = int(arg[2])
                frequency = int(arg[3])
                phase = float(arg[4])
                signal_plotter(signal_xt, time, signal_xtn, time_disc)
            except ValueError:
                print("Por favor de proporcionar los suficientes argumentos de entrada / Ampltiud / Frecuencia / Fase (expresado en decimal)")
        else:
            print("Por favor de proporcionar los suficientes argumentos de entrada / Ampltiud / Frecuencia / Fase (expresado en decimal)")
            
            
    elif arg[1] == "act_4":
        if len(arg) > 2:
            try:
                bits = int(sys.argv[2])
                run(bits)
                if bits <= 0:
                    raise ValueError
            except ValueError:
                print("El número de bits debe ser un entero positivo.")
                sys.exit(1)
            
if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Argumento fuera de los parametros tolerados")
        print("ejemplo de argumento: act_i donde i sea el numero de la actividad a escoger.")
        
