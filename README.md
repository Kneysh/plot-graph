# Interactive Plot Generator

A Python project for generating high-quality scientific plots with custom data points and labels. This interactive tool allows users to input their own data and customize plot labels through a command-line interface.

## Overview

This project creates matplotlib-based visualizations from user-provided data points. The program prompts users for x and y coordinates, axis labels, and a plot title, making it versatile for various data visualization needs.

## Features

- **Interactive Input**: User-friendly command-line interface for data entry
- **Flexible Plotting**: Create plots with any numerical data series
- **Interactive Display**: Uses Qt5Agg backend for interactive plot windows
- **High-Quality Output**: Saves plots as high-resolution PNG images (300 DPI)
- **Grid Display**: Enhanced readability with grid lines
- **Custom Labels**: Full control over axis labels and plot title
- **Automatic Saving**: Plots are automatically saved to the `images/` directory

## Prerequisites

- Python 3.12 or higher
- A GUI environment (for interactive plotting)
- Git (for version control)

## Dependencies

- matplotlib >= 3.10.6
- PyQt5 >= 5.15.11

## Installation Guide

Choose one of the following installation methods:

### 1. Using uv (Recommended)

```bash
# Clone the repository
git clone https://github.com/Kneysh/plot-graph.git

# Navigate to project directory
cd plot-graph

# Install dependencies using uv
uv sync
```

### 2. Using pip

```bash
# Clone the repository
git clone https://github.com/Kneysh/plot-graph.git

# Navigate to project directory
cd plot-graph

# Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install matplotlib>=3.10.6 pyqt5>=5.15.11
```

## Usage Guide

### Basic Usage

1. Ensure you're in the project directory:

   ```bash
   cd plot-graph
   ```

2. Run the script:

   ```bash
   python main.py
   ```

3. The program will:
   - Display an interactive plot window
   - Save the plot as `images/plot.png`
   - Show a confirmation message

### Sample Output

The generated plot shows:

- **X-axis**: Load Resistance (R_L) values ranging from 221 to 3253 ohms
- **Y-axis**: Load Power (P_L) values in watts
- **Curve**: Demonstrates the power transfer characteristics

![Sample Plot](images/plot.png)

### Using the Program

#### 1. Input Format

When running the program, you'll be prompted to enter:

1. **X-axis values**: Enter comma-separated numbers (e.g., `1,2,3,4,5`)
2. **Y-axis values**: Enter comma-separated numbers (e.g., `10,20,30,40,50`)
3. **X-axis label**: Enter a descriptive label for your x-axis
4. **Y-axis label**: Enter a descriptive label for your y-axis
5. **Plot title**: Enter the title for your plot

Example input:

```bash
Please Enter your data points:
x : 1,2,3,4,5
y : 10,20,30,40,50
Enter label for X axis: Time (seconds)
Enter label for Y axis: Temperature (°C)
Enter the Title of the graph: Temperature vs Time
```

#### 2. Output

The program will:

1. Generate an interactive plot window showing your data
2. Save the plot as a high-resolution PNG file (300 DPI)
3. Display a confirmation message

The generated plot includes:

- Data points marked with circular markers
- Lines connecting the data points
- A grid for better readability
- Your custom axis labels and title
- Automatically scaled axes based on your data

#### 3. Plot Customization

To modify the plot appearance, you can edit the `plot` function in `main.py`:

````python
def plot(x:list, y:list, x_label:str, y_label:str, title:str):
    # Modify marker style, color, or size
    plt.plot(x, y, marker='o')  # Try 's' for squares, '^' for triangles

    # Adjust grid style
    plt.grid(True)  # Add alpha=0.5 for transparency

    # Change output settings
    plt.savefig('./images/plot.png', dpi=300, bbox_inches='tight')
```## Contribution Guidelines

We welcome contributions! Here's how you can help improve this project:

### 1. Setting Up Development Environment

```bash
# Fork the repository on GitHub

# Clone your fork
git clone https://github.com/YOUR-USERNAME/plot-graph.git

# Add upstream remote
git remote add upstream https://github.com/Kneysh/plot-graph.git

# Create a new branch
git checkout -b feature/your-feature-name
````

### 2. Development Workflow

1. **Code Style**

   - Follow PEP 8 guidelines
   - Use meaningful variable names
   - Add comments for complex logic
   - Include docstrings for functions

2. **Testing**

   - Test your changes with different data sets
   - Verify plot generation works
   - Check interactive features
   - Ensure proper error handling

3. **Committing Changes**
   ```bash
   git add .
   git commit -m "Brief description of changes"
   git push origin feature/your-feature-name
   ```

### 3. Submitting Pull Requests

1. Update your fork:

   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. Create a pull request:
   - Go to GitHub and create a PR from your feature branch
   - Provide a clear description of changes
   - Include screenshots if UI changes were made
   - Reference any related issues

### 4. Code Review Process

- All PRs will be reviewed
- Address any requested changes
- Maintain clear communication in PR comments
- Be patient during the review process

## Troubleshooting

### Common Issues and Solutions

1. **Display Issues**

   - Error: "No display name and no $DISPLAY environment variable"

   ```bash
   # Solution: Set matplotlib to use a non-interactive backend
   export MPLBACKEND="Agg"
   ```

2. **Dependencies**

   - Qt5 missing:

   ```bash
   # Ubuntu/Debian
   sudo apt-get install python3-qt5

   # macOS
   brew install pyqt5
   ```

3. **Permission Issues**
   ```bash
   # Fix images directory permissions
   chmod 755 images/
   ```

## Project Structure

```
plot-graph/
├── main.py           # Main plotting script with interactive input
├── pyproject.toml    # Project configuration and dependencies
├── README.md        # Documentation
└── images/          # Output directory for generated plots
    └── plot.png     # Your generated plot
```

## License

This project is released under the MIT License. See [LICENSE](LICENSE) file for details.

## Support

- Create an issue for bug reports
- Start a discussion for feature requests
- Check existing issues before reporting

---

For more information, contact the maintainers or open an issue on GitHub.
