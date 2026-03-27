# Technique 09: Ridge / Joy Plot

## When to Use
Visualize how multiple distributions evolve -- for example, distributions across training stages or performance distributions under different noise levels.

## Core Code

```python
import joypy  # pip install joypy
import pandas as pd

# Prepare data in long format DataFrame
df = pd.DataFrame({
    'value': np.concatenate([data_epoch_1, data_epoch_50, data_epoch_100, ...]),
    'epoch': np.repeat(['Epoch 1', 'Epoch 50', 'Epoch 100', ...],
                       [len(data_epoch_1), len(data_epoch_50), ...])
})

fig, axes = joypy.joyplot(
    df, by='epoch', column='value',
    figsize=(COLWIDTH, COLWIDTH * 0.8),
    alpha=0.6, overlap=0.4,
    colormap=plt.cm.viridis,
    linewidth=1, linecolor='black')

plt.xlabel('Value', fontsize=9)
```

## Pure matplotlib Implementation (More Control)

```python
fig, axes = plt.subplots(len(groups), 1, figsize=(COLWIDTH, COLWIDTH),
                         sharex=True)
fig.subplots_adjust(hspace=-0.3)  # negative value creates overlapping distributions

for i, (name, values) in enumerate(groups.items()):
    ax = axes[i]
    # KDE
    from scipy.stats import gaussian_kde
    kde = gaussian_kde(values)
    x_range = np.linspace(global_min, global_max, 200)
    density = kde(x_range)

    ax.fill_between(x_range, density, alpha=0.5, color=cmap(i / len(groups)))
    ax.plot(x_range, density, color='black', lw=0.8)
    ax.set_yticks([])
    ax.spines[['top', 'right', 'left']].set_visible(False)
    ax.text(-0.02, 0.5, name, transform=ax.transAxes,
            fontsize=8, va='center', ha='right')

axes[-1].set_xlabel('Performance')
```

## Use Cases
- Weight or gradient distribution changes during training
- Performance distribution drift under different conditions
- Final performance distribution comparison across multiple runs
