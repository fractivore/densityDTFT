import numpy, sys
import matplotlib.pyplot as plt

def isInt(x):
    try:
        int(x)
    except:
        return False
    return True

if "--typeInSet" in sys.argv:
    rawInput = list(sys.argv[sys.argv.index("--typeInSet") + 1])
    #The following is used to parse command-line input
    # to be more accepting of different ways of conveying
    # a list of ints:
    set_selected = []
    for arg in rawInput:
        if isInt(arg):
            set_selected.append(int(arg))
    print("set_selected:", set_selected)
else:
    set_selected = [0,1,0,1]
        
if "--imgFileName" in sys.argv:
    filename = sys.argv[sys.argv.index("--imgFileName") + 1]
else:
    filename = "plot_out.png"

def main():
    dtft = natural_density_dtft(set_selected)
    dtft.plot_frequency_spectrum()

class natural_density_dtft:

    def __init__(self, set_of_naturals):
        self.this_set = numpy.array(set_of_naturals)

    def amplitude_of_omega(self,omega):
        """This function returns the amplitude of the frequency component
        at omega for the DTFT of a set of naturals."""
        
        #Calculate the component in frequency omega by summing
        #the appropriate exponentials, just e^-i*omega*k in this case
        return sum(numpy.exp(-1j*omega*self.this_set))

    def plot_frequency_spectrum(self):
        x_axis = numpy.linspace(-100,100,200)
        y_axis = [self.amplitude_of_omega(omega) for omega in x_axis]
        fig, ax = plt.subplots()
        ax.plot(x_axis,numpy.absolute(y_axis), label="Magnitude")
        ax.plot(x_axis, numpy.real(y_axis), label="Real Part")
        ax.plot(x_axis, numpy.imag(y_axis), label="Imaginary Part")
        ax.set(xlabel='Omega', ylabel='Ampitude',
        title='Frequency Spectrum of Membership Function')
        ax.grid()
        handles, labels = ax.get_legend_handles_labels()
        ax.legend(handles, labels)
        fig.savefig(filename)
        plt.show()

if __name__ == "__main__":
    main()
