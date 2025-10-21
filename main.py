import matplotlib
matplotlib.use('Qt5Agg')  # for interactive backend
import matplotlib.pyplot as plt

def plot(x:list, y:list, x_label:str, y_label:str, title:str):

    # Create the plot
    plt.plot(x, y, marker='o')

    # Set labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)

    # Display grid
    plt.grid(True)

    # Save the plot
    plt.savefig('./images/plot.png', dpi=300, bbox_inches='tight')
    
    # Try to show (will warn if non-interactive)
    plt.show()
    
    print("\nPlot saved as plot.png")


if __name__ == "__main__":
    # Data points 
    print("Please Enter your data points:")
    x = list(map(int, (input("x : ")).strip().split(",")))
    y = list(map(int, (input("y : ")).strip().split(",")))

    # labels & title
    x_label = input("Enter label for X axis: ").strip()
    y_label = input("Enter label for Y axis: ").strip()
    title = input("Enter the Title of the graph: ").strip()

    plot(x, y, x_label, y_label, title)
