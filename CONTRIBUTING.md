# Contributing to Academic Figure Patterns

Thank you for your interest in contributing! This project thrives on community contributions.

## How to Contribute

### Add a New Design Pattern

1. Create `patterns/XX_your_pattern.md` following the existing format
2. Include: claim type, required elements, visual structure, code template
3. Add real paper examples where this pattern is used
4. Update `docs/CLAIM_TO_PATTERN.md` with the new mapping

### Add a New Technique

1. Create `techniques/XX_your_technique.md`
2. Include: when to use, complete working code, before/after comparison
3. Update `techniques/OVERVIEW.md`

### Add a Case Study

1. Add to `docs/REAL_PAPER_CASES.md`
2. Include: paper name, venue, figure number, claim, visual analysis
3. Describe what makes the figure effective

### Report an Anti-Pattern

1. Add to `docs/ANTI_PATTERNS.md`
2. Include: symptom, reviewer reaction, fix with code

## Style Guide

- Write in English
- Include working matplotlib code (test it!)
- Reference real papers when possible
- Keep documentation concise and actionable

## Development Setup

```bash
git clone https://github.com/taoge946/academic-figure-patterns.git
cd academic-figure-patterns
pip install -e ".[dev]"
python examples/01_comparison_before_after.py  # verify setup
```

## Code of Conduct

Be respectful. Academic figure design is subjective — constructive discussion is welcome.
