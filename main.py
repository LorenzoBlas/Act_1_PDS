import sys
from src.act_1 import continuous_signals, discrete_signals, plot_all_signals

def main(arg):
    if arg[1] == "act_1":
        
        
        time_cont, signals_cont = continuous_signals()
        time_disc, signals_disc = discrete_signals()
        plot_all_signals(time_cont, signals_cont, time_disc, signals_disc)
    #elif arg[1] == "act_2":
    #elif arg[1] == "act_3":
    #elif arg[1] == "act:4":


if __name__ == '__main__':
    args = sys.argv
    if len(args) > 1:
        main(args)
    else:
        print("Argumento fuera de los parametros tolerados")
        print("ejemplo de argumento: act_i donde i sea el numero de la actividad a escoger.")
        
