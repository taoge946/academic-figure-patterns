# Academic Figure Patterns（学术图表设计模式）

**面向论文发表的学术图表设计模式：重点在"图里放什么证据"，而不只是好不好看。**

[English](README.md) | **中文**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

> 本页是中文概览。模式库、规则文档和代码注释目前是英文，下面的链接都指向英文原文。

---

## 这个项目解决什么问题

大多数画图教程教的是"怎么用 matplotlib"。这个项目想帮你决定的是：**一张图里应该放什么证据，以及为什么这样放**。适用场景包括 NeurIPS、ICML、ICLR、Nature 系列、APS 期刊等。

本科毕业论文里的图和顶刊顶会里的图，差别主要**不在**字体和配色，而在**内容设计**：展示哪些数据、怎样组织比较、用什么标注引导读者视线，以及怎样让图自己把结论讲清楚。

**一分钟了解方法。** 写任何绘图代码之前，先为每个面板回答四个问题（[Spec First](docs/SPEC_FIRST.md)）：

1. **论点（Claim）**：遮住图注，读者应该从这个面板得出什么结论？
2. **比较（Comparison）**：拿什么和什么比？没有比较对象的面板直接删掉。
3. **编码（Encoding）**：用哪种视觉形式，能让这个比较一眼看清？
4. **反事实（Counterfactual）**：如果论点不成立，这个面板会是什么样子？说不出来，说明这个面板没有在检验任何东西。

然后到[模式库](#模式库)里选择图形结构，并守住数据忠实性（[哪些规则是硬性要求](docs/RULE_STRENGTH.md)）。

## 同一份数据，画两次

下面每一组图都来自**同一个 `.npz` 文件**（`examples/data/`）。左边是"五分钟版本"：单面板、基础图型、matplotlib 默认样式；右边按本仓库的规则重画。数据是合成的，标签是通用的，所以你看到的是**图形结构**，不是某个实验结果。两边的脚本都在 `examples/` 里（`before_<id>.py` 和 `<id>_*.py`），说明见 [examples/README_pattern11.md](examples/README_pattern11.md)。

### 物理类结果图（逐样本证据）

| Before | After |
|:---:|:---:|
| ![](examples/figures/11a_before.png) | ![](examples/figures/11a_after.png) |
| 三根均值柱。 | **对象 → 配对散点 → 终点量。** 先画记录本身（矩阵）；每个样本一个点，方案 B 落在恒等线上，对照方案落在零线上；汇总的剂量曲线放在最后、画得最小。 |
| ![](examples/figures/11b_before.png) | ![](examples/figures/11b_after.png) |
| P 和 Q 的分组均值柱。 | **分布网格 + 尾部列。** 队列 × 条件，每格两条峰值归一化的逐样本分布（一宽一窄；对照列里都收缩）；超越曲线显示哪个估计器的大误差更少。 |
| ![](examples/figures/11c_before.png) | ![](examples/figures/11c_after.png) |
| 一张默认散点图。 | **机制散点。** 效应对一个可命名的解释变量作图，三种系统规模落在同一条曲线上；分箱中位数和 IQR 带标出过零点；对照压缩成窄条；终点量放在最后。 |
| ![](examples/figures/11d_before.png) | ![](examples/figures/11d_after.png) |
| 两条平均误差曲线。 | **误差对误差网格。** 队列 × 预算，每个点是一个样本（方法误差对基线误差）；整个论证就是随预算增加，点云如何越过对角线；下方是 ECDF。 |
| ![](examples/figures/12a_before.png) | ![](examples/figures/12a_after.png) |
| 两组均值柱。 | **带等高线和边缘分布的联合散点。** 同一批样本上的两类缺陷：一类沿对角线，一类是常数偏移；再按队列分解，下方是偏差。 |
| ![](examples/figures/12d_before.png) | ![](examples/figures/12d_after.png) |
| 按队列规模分组的柱状图。 | **山脊图 + 无拟合预测 + 分辨率面板。** 每个规模下对照与缺陷的分布；比值对噪声底，模拟队列作为浅色点，两条不经拟合的预测线；最后是分辨率面板。 |
| ![](examples/figures/12e_before.png) | ![](examples/figures/12e_after.png) |
| 九条叠在一起的线。 | **实测参数热图 + 预测等高线。** 实测量画在二维网格上，理论的过零线作为一条等高线叠加，再加两条能读出过零位置的切线。 |

### 机器学习与系统类会议（规则相同，风格不同）

| Before | After |
|:---:|:---:|
| ![](examples/figures/12b_before.png) | ![](examples/figures/12b_after.png) |
| 线性坐标下的两条运行时间曲线。 | **Hero 扩展性图。** 运行时间和内存对规模作图（双对数轴），基线失败区域用阴影标出；加速比对规模作图，带 1× 参考线。 |
| ![](examples/figures/12c_before.png) | ![](examples/figures/12c_after.png) |
| 均值指标的分组柱状图。 | **系统类扫描图。** 各设备上的指标差异用填充表示；成本对输入规模作图，比值及其范围在副轴上，基线的极限画成一堵"墙"。线条粗、字号大，适应缩小到单栏后的效果。 |

0.1 版的机器学习风格示例（`examples/figures/01–03_*.png`）仍在 `examples/` 中。0.2.1 按仓库自己的数据忠实性规则重画了这几张图：用点图代替截断的柱状图，删掉并不存在的"交叉点"，加速比改用对数轴。

> **左栏是教学对比，不是基准测试。** "Before"图是故意画得很简单的。它们展示的是规则带来了什么，并不能证明右栏的形式一定比一张认真画的简单图更好；有时候简单图反而是更好的选择。

## 定位：这是什么，不是什么

| 工具 | 作用 | 与 AFP 的关系 |
|------|------|:---:|
| [SciencePlots](https://github.com/garrettj403/SciencePlots) | 字体、线宽等学术风格 | ✅ AFP 已集成 |
| [tueplots](https://github.com/pnkraemer/tueplots) | 各会议期刊的图幅尺寸 | ✅ AFP 已集成 |
| **Academic Figure Patterns** | **图里应该放什么** | — |

AFP 想回答的问题例如：
- *"我有对比实验结果，主图到底应该比较什么？"*
- *"如果我们的论点不成立，这张图会是什么样？读者能看出来吗？"*
- *"这里该画逐样本图、简单的点图，还是干脆用表格？"*

## 快速开始

### 安装

目前还没有发布到 PyPI，请从 GitHub 安装：

```bash
pip install "academic-figure-patterns @ git+https://github.com/taoge946/academic-figure-patterns"
# 同时安装 SciencePlots + tueplots：
pip install "academic-figure-patterns[full] @ git+https://github.com/taoge946/academic-figure-patterns"

# 如果要运行示例和测试：
git clone https://github.com/taoge946/academic-figure-patterns.git
cd academic-figure-patterns && pip install -e ".[dev]"
```

LaTeX 不是必需的：`setup_style()` 只在检测到 LaTeX 时才启用它，也可以用 `usetex=True/False` 手动指定。

### 在代码中使用

```python
from afp import setup_style, get_method_colors, save_fig

# 一行设置会议/期刊样式（集成 SciencePlots + tueplots；LaTeX 可选）
TEXTWIDTH, COLWIDTH = setup_style(venue='icml')

# 你的方法始终使用醒目的颜色
colors = get_method_colors(['GNN', 'Transformer', 'Ours'])
# → {'GNN': '#348ABD', 'Transformer': '#988ED5', 'Ours': '#E24A33'}
```

逐样本证据图（模式 11）的辅助函数：

```python
from afp.evidence import structure_strength, paired_cloud, binned_median, exceedance_curve

print(structure_strength(x, y, kind="paired"))   # 先检查这种图形能否承载结论，再画
paired_cloud(ax, x, y, color="#3b7dd8", identity=True)
```

### 建议阅读顺序

0. **[规则强度](docs/RULE_STRENGTH.md)**：哪些是数据忠实性的硬性要求，哪些是设计默认值，哪些只是某位审稿人的偏好（0.2.1 新增）
1. **[Spec First](docs/SPEC_FIRST.md)**：画图之前，先为每个面板写四个问题的规格说明
2. **[Form Ladder](docs/FORM_LADDER.md)**：审稿人说"看起来很廉价"时指的是什么，以及从汇总面板到逐样本证据的五级阶梯
3. **[Claim → Pattern](docs/CLAIM_TO_PATTERN.md)**："我想说明 X"→ 去读模式 Y
4. **[反模式](docs/ANTI_PATTERNS.md)**：21 个常见错误
5. **[叙事技巧](docs/STORYTELLING.md)**：从顶会论文中提炼的 10 种视觉叙事方法

## 规则不是一样强的

仓库里的规则来源不同，约束力也不同（详见 [RULE_STRENGTH.md](docs/RULE_STRENGTH.md)）：

| 层级 | 含义 | 怎么对待 |
|---|---|---|
| **1. 数据忠实性** | 图不能歪曲数据：柱状图从 0 开始；说明误差范围是什么；不隐藏反例；标注必须与数据相符 | 必须遵守，任何会议规定或审美偏好都不能凌驾于此 |
| **2. 设计原则** | 通常能让比较更易读的选择：先写规格、有逐样本数据时展示它、一个面板一个论点 | 默认遵守；如果不遵守，要能说出理由 |
| **3. 校准过的偏好** | 某位审稿人在两篇稿件上的取舍，例如 `\|r\|>0.9` 的阈值、"终点量最后且最小" | 有参考价值，但不是标准；先看你的领域和读者是否相似 |

## 核心理念：论点优先

每张图都从一个**论点**开始：读者应该得出的那一句话。

| ❌ 差的论点 | ✅ 好的论点 | 如果论点不成立，图会显示… |
|---|---|---|
| "训练曲线" | "我们的方法收敛速度是基线的 3 倍" | 各条曲线在同一步达到目标损失 |
| "对比结果" | "我们的方法平均领先所有基线 4.2%" | 差值的置信区间跨过零 |
| "消融实验" | "注意力模块贡献了 47% 的提升，去掉后方法失效" | 注意力那一步很小，去掉后也没有明显下降 |

论点决定选哪个**模式**，模式决定图的结构。好的论点是**可检验的**：第三列必须是这张图真的有可能显示出来的结果。论点应该从结果中得出；图的任务是让读者能检验它，而不是让它看起来更大。

## 模式库

### 11 个设计模式

每个模式说明图形结构、比较所需的元素，以及代码模板。每个元素都有它的用途，不是凑数用的。

| # | 模式 | 适用场景 |
|---|------|---------|
| 01 | [Hero Figure](patterns/01_hero_figure.md) | 论文的"电梯演讲"（图 1） |
| 02 | [Main Comparison](patterns/02_main_comparison.md) | "我们优于基线"：用点图或差值图；柱状图只能从 0 开始 |
| 03 | [Ablation Study](patterns/03_ablation.md) | "每个组件都有贡献" |
| 04 | [Scaling Analysis](patterns/04_scaling.md) | "我们的扩展性更好" |
| 05 | [Training Dynamics](patterns/05_training_dynamics.md) | "我们收敛更快" |
| 06 | [Qualitative Results](patterns/06_qualitative.md) | 可视化输出对比 |
| 07 | [Analysis & Insight](patterns/07_analysis.md) | "它为什么有效" |
| 08 | [Pareto Tradeoff](patterns/08_pareto_tradeoff.md) | 效率与性能的权衡 |
| 09 | [Distribution Analysis](patterns/09_distribution.md) | 统计稳健性 |
| 10 | [Quantum Hardware](patterns/10_quantum_hardware.md) | 量子硬件实验结果 |
| 11 | [Per-Sample Evidence](patterns/11_per_sample_evidence.md) | "效应体现在每一行数据里"：配对散点、分布网格、超越曲线 |

### 14 个可视化技巧

完整代码见 [techniques/](techniques/OVERVIEW.md)：局部放大（inset zoom）、断轴、标注、复杂布局、瀑布图、雷达图、排名变化图（bump chart）、桑基图、山脊图、哑铃图、联合分布 + 边缘分布、跨面板连接线等。

### 10 个叙事技巧

从 NeurIPS/ICML 最佳论文等作品中提炼，例如"先立后破"（Emergent Abilities）、"双面板排除其他解释"（ResNet、Mamba）、"先验证再外推"（IBM Quantum Utility）、"坐标轴的选择本身就是论证"等。详见 [STORYTELLING.md](docs/STORYTELLING.md)。

## "2 秒测试"

遮住所有文字，只看形状和颜色 2 秒：你能看出这个比较显示了什么吗？包括"没有差异"或"要看情况"这样的答案。看不出来，这张图就不合格。这个测试检验的是可读性，不是让某个方法看起来像赢家。

## 常见反模式（节选）

| # | 反模式 | 修正 |
|---|--------|------|
| AP-01 | 最低限度（只有 3 根柱子） | 补上比较所需的东西：误差范围、表示"无效应"的参考线、有逐样本数据时展示它 |
| AP-03 | 图形不匹配问题 | 按问题选图形（普通点图往往就是正确答案） |
| AP-05 | 截断的柱状图坐标轴 | 柱状图从 0 开始；数值集中在窄范围时改用点图或差值图 |
| AP-11 | 坐标尺度错误（跨三个数量级却用线性轴） | 幂律用双对数，指数用半对数 |
| AP-14 | 图注只描述不下结论 | 机器学习会议：第一句写结论。APS 期刊：图注只描述（见 [Venue Rules](docs/VENUE_RULES.md)） |
| AP-15 | 主面板只有汇总统计 | 先找逐样本数据；汇总量作为数字标注，或放在最后最小的面板 |

完整的 21 条见 [ANTI_PATTERNS.md](docs/ANTI_PATTERNS.md)，其中 AP-15 到 AP-21 来自真实稿件的作者审稿记录。

## 测试

```bash
pip install -e ".[dev]"
pytest            # 辅助函数、无 LaTeX 环境下的样式设置、所有示例脚本
```

## 相关项目与延伸阅读

- [Fundamentals of Data Visualization](https://clauswilke.com/dataviz/)（Claus Wilke）：本仓库大部分第 1、2 层规则背后的设计原理。
- [Scientific Visualization: Python + Matplotlib](https://github.com/rougier/scientific-visualization-book)（Nicolas Rougier）：matplotlib 实现技巧。
- [DABEST](https://github.com/ACCLAB/DABEST-python)：估计统计图（原始数据 + 效应量及其 bootstrap 置信区间），适合模式 02 的差值图和模式 11。
- [RainCloudPlots](https://github.com/RainCloudPlots/RainCloudPlots)：分布 + 原始观测（模式 09 / 11）。

这些项目的许可证各不相同（例如书籍正文和插图使用非商业性的知识共享许可）。请链接引用，不要把它们的文字或图片复制进这个 MIT 许可的仓库。

## 参与贡献

欢迎贡献，详见 [CONTRIBUTING.md](CONTRIBUTING.md)。新增规则时请说明它属于哪一层（数据忠实性 / 设计原则 / 审稿人偏好），以及在什么情况下不适用。

## 引用

```bibtex
@software{afp2026,
  title = {Academic Figure Patterns: Design Patterns for Publication-Quality Figures},
  author = {Li, Jintao},
  year = {2026},
  url = {https://github.com/taoge946/academic-figure-patterns},
}
```

## 许可证

MIT License，见 [LICENSE](LICENSE)。
