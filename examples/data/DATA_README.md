# Example datasets (synthetic, seeded)

Each `.npz` holds the arrays behind one example figure. Load with `numpy.load(path)`; keys are listed below.
All values are synthetic and dimensionless; names are deliberately generic.

## 11a.npz — does replacing part of a record change per-sample values?
- `reference_matrix`, `replacementA_matrix`, `replacementB_matrix`: 64 × 6 integer matrices (categories 0/1/2) — a
  reference record, one with 16 rows replaced arbitrarily, one with the same rows replaced while preserving each row's
  category multiset. `replaced_rows`: the 16 replaced row indices.
- `shift_schemeA`, `shift_schemeB`, `shift_schemeC`: 1,600 values each — the per-sample change of a quantity under three
  replacement schemes (C is the control scheme).
- `dose` (5): fraction of replaced rows; `pooled_stat`, `pooled_stat_ci`: a pooled statistic and its 95 % half-width per dose.

## 11b.npz — two estimators P and Q under three conditions, three cohorts
- `shift_P_cohort{j}_cond{c}`, `shift_Q_cohort{j}_cond{c}` for j = 0,1,2 and c = 0,1,2: per-sample change of a prediction
  between the condition and the clean fit (cond 2 is a control). Cohort sizes 1600, 1600, 1000.
- `clean_absres_P_cohort{j}`, `clean_absres_Q_cohort{j}`, `clean_absres_mean_cohort{j}`: absolute residuals of P, Q and a
  simple reference predictor on clean data.

## 11c.npz — does an effect depend on an explanatory variable?
- `explanatory_x` (2,700), `effect` (2,700), `size_index` (2,700; 0/1/2 → `sizes` = 6, 12, 24), `control_effect` (2,700):
  the same effect under a control condition.

## 11d.npz — method vs baseline error at four budget levels, three cohorts
- `baseline_err_cohort{j}_budget{b}`, `method_err_cohort{j}_budget{b}` for b = 1..4: per-sample absolute errors.
- `sqerr_baseline_cohort{j}`, `sqerr_method_cohort{j}`, `sqerr_method_perturbed_cohort{j}`, `sqerr_method_repaired_cohort{j}`:
  per-sample squared errors of four predictors at one budget.

## 12a.npz — two defect types: input shift vs model shift, plus a decomposition per cohort
- `input_shift_type1`, `model_shift_type1`, `input_shift_type2`, `model_shift_type2`: 1,600 samples each.
- `cohort{k}_input_shift_type{1,2}`, `cohort{k}_model_shift_type{1,2}` for k = 0..3: 900 samples, four further cohorts.
- `bar_intercept_type{1,2}`, `bar_nonconstant_type{1,2}` (4 each): a statistic split into two parts per cohort; `bar_err`
  (4): interval half-width. `bias_type{1,2}`, `bias_type{1,2}_err` (4 each): a bias per cohort.

## 12b.npz — runtime and memory of a method vs a baseline as problem size grows; speedups
- `taskA_sizes`, `taskA_base_runtime`, `taskA_ours_runtime`, `taskA_base_memory`, `taskA_ours_memory` (10 each; the
  baseline only runs up to size `taskA_baseline_limit`); same for `taskB_*` (9 each, `taskB_baseline_limit`).
- `speedup_problem_size` (9) and `speedup_<framework, task>` (9 each): speedup factors of five framework/task pairs.

## 12c.npz — a method vs a baseline on three devices; cost vs input size
- `input_size` (3); `metric_ours_device {1,2,3}`, `metric_base_device {1,2,3}` and `*_err_*` (3 each).
- `sweep_size` (9); `cost_ours`, `cost_base` (9); `cost_ratio`, `cost_ratio_band` (9); `baseline_limit` (scalar: the
  baseline stops working beyond this size).

## 12d.npz — a defect's effect at three cohort sizes; ratio vs noise floor; resolution
- `shift_control_row{i}`, `shift_defect_row{i}` for i = 0,1,2: per-sample model shift under a control and under the
  defect, for a small, medium and large cohort.
- `sim_x`, `sim_ratio` (120): simulated cohorts — noise-floor variable and the resulting ratio; `measured_x`,
  `measured_ratio`, `measured_err` (6): measured cohorts with interval half-widths. Theory predicts ratio = 1 − 2x.
- `resolution_control_lo`, `resolution_control_hi`, `resolution_defect`, `resolution_defect_err` (6 each): per-cohort
  control interval and defect estimate, normalized.

## 12e.npz — a measured quantity over a 2-D parameter grid
- `parameter1` (21), `parameter2` (9); `measured` (9 × 21): the measured quantity on the grid; `model` (9 × 21): the
  theory value on the same grid (it crosses zero along a curve).
