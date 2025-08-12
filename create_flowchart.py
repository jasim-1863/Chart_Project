import json
import graphviz
import os
import textwrap

# Set the path to the Graphviz executable
os.environ["PATH"] += os.pathsep + r"C:\Program Files\Graphviz\bin"

# Create a new directed graph
dot = graphviz.Digraph(comment='Control Strategy Flowchart')
dot.attr(rankdir='LR')  # Left to right layout
dot.attr(size='11,8!')  # Set size to 11x8 inches
dot.attr(ratio='fill')  # Fill the size while maintaining aspect ratio
dot.attr(dpi='300')  # Higher DPI for better quality
dot.attr(fontsize='14')  # Larger base font size
dot.attr('node', fontsize='12')  # Font size for node text

# Function to wrap text and create HTML-like label
def create_wrapped_label(text, width=30):
    lines = []
    for part in text.split('\n'):
        lines.extend(textwrap.fill(part, width=width).split('\n'))
    return '<<TABLE BORDER="0" CELLBORDER="0" CELLPADDING="5"><TR><TD><FONT FACE="Arial" POINT-SIZE="12">' + '<BR/>'.join(lines) + '</FONT></TD></TR></TABLE>>'

# Read the JSON data
with open('chart_data.json', 'r') as file:
    data = json.load(file)

# Add nodes
for node in data['nodes']:
    # Create nodes with rounded rectangles and light yellow background
    dot.node(node['id'], 
            create_wrapped_label(node['label']), 
            shape='box',
            style='rounded,filled',
            fillcolor='lightyellow')

# Add edges
for edge in data['edges']:
    dot.edge(edge['from'], edge['to'])

# Save the flowchart
dot.render('control_strategy', format='png', cleanup=True)
