# Control Strategy Flowchart Generator

This project generates a flowchart visualization from a JSON file describing control strategy nodes and their relationships.

## Prerequisites

1. Python 3.x
2. Graphviz (system installation)

## Setup Instructions

### 1. Install Graphviz

#### Windows
```powershell
winget install graphviz
```

#### Linux
```bash
sudo apt-get install graphviz  # Ubuntu/Debian
# or
sudo yum install graphviz      # CentOS/RHEL
```

#### macOS
```bash
brew install graphviz
```

### 2. Set up Python Environment

1. Create a virtual environment:
```powershell
python -m venv .venv
```

2. Activate the virtual environment:
```powershell
# Windows
.venv\Scripts\activate

# Linux/macOS
source .venv/bin/activate
```

3. Install required packages:
```powershell
pip install -r requirements.txt
```

## Usage

1. Make sure your control strategy data is in `chart_data.json`
2. Run the script:
```powershell
python create_flowchart.py
```

The script will generate a file named `control_strategy.png` containing the flowchart visualization.

## Output

The generated flowchart will be saved as `control_strategy.png` in the same directory. The chart features:
- Left-to-right layout
- Rounded rectangular nodes with light yellow background
- Automatically wrapped text for better readability
- High-resolution output (300 DPI)
