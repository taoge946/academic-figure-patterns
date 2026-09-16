# Example datasets (synthetic, seeded)

Each `.npz` holds the arrays behind one example figure. Load with `numpy.load(path)`; keys are listed below.
All values are synthetic and dimensionless unless stated.

## 11a.npz — does replacing part of a measurement record change the labels?
- `clean_axes`, `arbitrary_axes`, `matched_axes`: 64 × 6 integer matrices (0/1/2 = X/Y/Z) — the measurement axis of
  each of 64 settings on 6 qubits for the clean record, a record with 16 settings replaced arbitrarily, and one with the
  same 16 settings replaced while preserving each row's axis multiset. `replaced_rows`: the 16 replaced row indices.
- `shift_shared`, `shift_disjoint`, `shift_matched`: 1,600 values each — the change of a per-row label under three
  replacement schemes (shared shots, fresh shots, composition-matched).
- `dose_fraction` (5): fraction of replaced settings; `dW`, `dW_ci`: a pooled statistic and its 95 % half-width at each dose.

## 11b.npz — two estimators P and Q under three conditions, three cohorts
- `shift_P_cohort{j}_cond{c}`, `shift_Q_cohort{j}_cond{c}` for j = 0,1,2 and c = 0,1,2: per-row change of a learned
  prediction between the condition and the clean fit (cond 2 is a control condition). Cohort sizes 1600, 1600, 1000.
- `clean_absres_P_cohort{j}`, `clean_absres_Q_cohort{j}`, `clean_absres_mean_cohort{j}`: absolute residuals of P, Q and a
  training-mean predictor on clean data.

## 11c.npz — does an effect depend on how many cells of a record are filled?
- `filled_cells` (2,700): the number of filled cells per state; `risk_ratio_log` (2,700): log risk ratio per state;
  `system_size_index` (2,700): 0/1/2 → `system_sizes` = 6, 12, 24; `control_risk_ratio` (2,700): same quantity under a
  control condition.

## 11d.npz — learner vs baseline error at four budgets K, three cohorts
- `baseline_err_cohort{j}_K{K}`, `learner_err_cohort{j}_K{K}` for K in 8, 32, 128, 1024: per-row absolute errors.
- `sqerr_baseline_cohort{j}`, `sqerr_clean_cohort{j}`, `sqerr_reused_cohort{j}`, `sqerr_repaired_cohort{j}`: per-row
  squared errors of four predictors at one budget.

## 12a.npz — two defect types: label shift vs learner shift, plus a decomposition per cohort
- `label_shift_reuse`, `learner_shift_reuse`, `label_shift_offset`, `learner_shift_offset`: 1,600 rows each; per-row label
  change and learner-prediction change under two defect types.
- `cohort{k}_label_shift_{reuse|offset}`, `cohort{k}_learner_shift_{reuse|offset}` for k = 0..3: 900 rows, four further cohorts.
- `bar_intercept_{reuse|offset}`, `bar_nonconstant_{reuse|offset}` (4 each): a statistic split into two parts per
  cohort; `bar_err` (4): interval half-width. `bias_{reuse|offset}`, `bias_{reuse|offset}_err` (4 each): label bias per cohort.

## 12b.npz — runtime and memory of a method vs a baseline as problem size grows; speedups
- `mis_sizes`, `mis_base_runtime`, `mis_ours_runtime`, `mis_base_memory`, `mis_ours_memory` (10 each; the baseline only
  runs up to size `mis_baseline_oom_from`, beyond that it runs out of memory); same for `tsp_*` (9 each, `tsp_baseline_oom_from`).
- `speedup_graph_size` (9) and `speedup_<framework, task>` (9 each): speedup factors of five framework/task pairs.

## 12c.npz — a compiler vs a baseline: survival on three devices, SWAP counts vs depth
- `depth` (3); `survival_ours_device {1,2,3}`, `survival_base_device {1,2,3}` and `*_err_*` (3 each).
- `sweep_depth` (9); `swap_ours`, `swap_base` (9); `swap_ratio`, `swap_ratio_band` (9); `baseline_timeout_depth` (scalar).

## 12d.npz — a defect's price at three cohort sizes; ratio vs noise floor; resolution
- `shift_control_row{i}`, `shift_defect_row{i}` for i = 0,1,2: per-state learner shift under a control and under the
  defect, for three cohort sizes (36, 71, 320 states; 5 draws each).
- `sim_x`, `sim_ratio` (120): simulated cohorts — noise-floor variable and the resulting ratio; `hw_x`, `hw_ratio`,
  `hw_err` (6): measured cohorts with interval half-widths. The theory predicts ratio = 1 − 2x.
- `resolution_control_lo`, `resolution_control_hi`, `resolution_defect`, `resolution_defect_err` (6 each): per-cohort
  control interval and defect estimate, in units of the statistic.

## 12e.npz — a measured quantity over a 2-D parameter grid
- `overlap_fraction` (21), `shots_per_setting` (9); `measured` (9 × 21): the measured quantity on the grid;
  `model` (9 × 21): the theory value on the same grid (it crosses zero along a curve).
