import matplotlib
matplotlib.use('Qt5Agg')  # for interactive backend
import matplotlib.pyplot as plt

def plot():

    # Data points
    x = [221, 327, 556, 980, 2153, 3253]  # R_L values
    y = [0.0141, 0.0160, 0.0200, 0.0245, 0.0193, 0.0130]  # P_L values

    # Create the plot
    plt.plot(x, y, marker='o')

    # Set labels and title
    plt.xlabel('$R_L~(\Omega)$')
    plt.ylabel('$P_L$ (W)')
    plt.title('$P_L~~VS~~R_L$')

    # Display grid
    plt.grid(True)

    # Save the plot
    plt.savefig('./images/plot.png', dpi=300, bbox_inches='tight')
    
    # Try to show (will warn if non-interactive)
    plt.show()
    
    print("Plot saved as plot.png")


if __name__ == "__main__":
    plot()
