import sys
from src.act_1 import continuous_signals, discrete_signals, plot_all_signals
from src.act_2 import continuous_sin, sine_plotter

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
         
        
    #elif arg[1] == "act_3":
    #elif arg[1] == "act:4":


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Argumento fuera de los parametros tolerados")
        print("ejemplo de argumento: act_i donde i sea el numero de la actividad a escoger.")
        
