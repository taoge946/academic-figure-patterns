# Technique 08: Sankey Diagram

## When to Use
- Visualize how computational resources or time are allocated across stages
- Show how errors propagate through a pipeline
- Illustrate data flow from input to output

## Recommended: Use Plotly (far easier than matplotlib's Sankey)

```python
import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15, thickness=20,
        line=dict(color="black", width=0.5),
        label=["Input", "Encoder", "Bottleneck", "Decoder", "Output",
               "Skip Conn.", "Residual"],
        color=["#636EFA", "#EF553B", "#00CC96", "#AB63FA", "#FFA15A",
               "#19D3F3", "#FF6692"]
    ),
    link=dict(
        source=[0, 0, 1, 1, 2, 2, 5],  # indices of source nodes
        target=[1, 5, 2, 6, 3, 5, 3],  # indices of target nodes
        value=[80, 20, 60, 20, 50, 10, 25],  # flow magnitude
        color=["rgba(99,110,250,0.3)"] * 7
    )
)])

fig.update_layout(font_size=10, width=600, height=400)
fig.write_image("figures/sankey.pdf")  # requires kaleido
```

## For Simple Cases, Use matplotlib

```python
from matplotlib.sankey import Sankey

fig, ax = plt.subplots(figsize=(8, 4))
sankey = Sankey(ax=ax, scale=0.01, offset=0.2,
               format='%.0f', unit='%')
sankey.add(
    flows=[100, -60, -25, -10, -5],
    labels=['Total\nCompute', 'Encoder', 'Decoder', 'Loss\nCalc', 'Other'],
    orientations=[0, 0, 0, -1, 1])
sankey.finish()
```

## Best Practices
- Sankey diagrams are best suited for "flow allocation" data; do not force-fit them to non-flow relationships
- Keep to 15 nodes maximum; otherwise the diagram becomes too cluttered
- Flow widths must be proportional to actual values
