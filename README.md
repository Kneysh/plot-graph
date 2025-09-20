# Plot Graph - Power vs Resistance Analysis

A Python project for generating scientific plots that visualize the relationship between load resistance (R_L) and load power (P_L).

## Overview

This project creates a matplotlib-based visualization showing how power varies with resistance in an electrical circuit. The plot demonstrates the characteristic curve of power dissipation across different load resistance values.

## Features

- **Interactive Plotting**: Uses Qt5Agg backend for interactive plot display
- **High-Quality Output**: Saves plots as high-resolution PNG images (300 DPI)
- **Scientific Notation**: Proper mathematical notation using LaTeX formatting
- **Grid Display**: Enhanced readability with grid lines
- **Automatic Saving**: Plots are automatically saved to the `images/` directory

## Sample Output

The generated plot shows:

- **X-axis**: Load Resistance (R_L) values ranging from 221 to 3253 ohms
- **Y-axis**: Load Power (P_L) values in watts
- **Curve**: Demonstrates the power transfer characteristics

![Sample Plot](images/plot.png)

## Requirements

- Python 3.12 or higher
- matplotlib >= 3.10.6
- PyQt5 >= 5.15.11

## Installation

### Using uv (recommended)

```bash
# Clone the project
git clone git@github.com:Kneysh/plot-graph.git

# enter the project directory
cd plot-graph

# Install dependencies using uv
uv sync
```

### Using pip

```bash
# Install dependencies
pip install matplotlib>=3.10.6 pyqt5>=5.15.11
```

## Usage

### Running the Script

```bash
# Using uv
uv run python main.py

# Or with regular Python
python main.py
```

### Expected Output

When you run the script, it will:

1. Generate an interactive plot window (if display is available)
2. Save the plot as `images/plot.png`
3. Print a confirmation message

```
Plot saved as plot.png
```

## Project Structure

```
plot-graph/
├── main.py           # Main plotting script
├── pyproject.toml    # Project configuration and dependencies
├── uv.lock          # Dependency lock file
├── README.md        # This file
└── images/          # Output directory for generated plots
    └── plot.png     # Generated plot image
```

## Customization

### Modifying Data Points

To plot your own data, edit the `x` and `y` arrays in `main.py`:

```python
# Data points
x = [221, 327, 556, 980, 2153, 3253]  # Your R_L values
y = [0.0141, 0.0160, 0.0200, 0.0245, 0.0193, 0.0130]  # Your P_L values
```

### Changing Plot Appearance

You can customize various aspects of the plot:

- **Labels**: Modify `plt.xlabel()`, `plt.ylabel()`, and `plt.title()`
- **Markers**: Change the `marker` parameter in `plt.plot()`
- **Colors**: Add `color` parameter to `plt.plot()`
- **Output**: Change the filename in `plt.savefig()`

### Example Customizations

```python
# Different marker style and color
plt.plot(x, y, marker='s', color='red', linewidth=2)

# Custom labels
plt.xlabel('Resistance (Ω)')
plt.ylabel('Power (W)')
plt.title('Power Transfer Analysis')
```

## Technical Notes

- **Backend**: Uses Qt5Agg for interactive display; falls back gracefully in headless environments
- **LaTeX Rendering**: Mathematical symbols are rendered using matplotlib's LaTeX support
- **Image Quality**: Output images are saved at 300 DPI with tight bounding boxes for publication quality

## Troubleshooting

### Display Issues

If you encounter display issues:

- Ensure you have a GUI environment available
- For headless systems, the plot will still be saved as an image
- Install Qt5 development libraries if needed

### Dependencies

If you have dependency conflicts:

- Use a virtual environment
- Consider using `uv` for better dependency management

## License

This project is open source. Feel free to modify and distribute as needed.

## Contributing

To contribute to this project:

1. Fork the repository
2. Make your changes
3. Test the plotting functionality
4. Submit a pull request

---

_Generated plot demonstrates electrical circuit analysis showing the relationship between load resistance and power dissipation._
