# Numerical Methods

A collection of classic numerical methods implemented in Python, applied to real engineering problems. Developed for a Numerical Methods course.

## Applied problems

**Missile interception (`missil.py`)** — Uses the **secant method** (`secante.py`) to find the time delay needed to intercept a projectile in flight, solving the nonlinear trajectory equation (accounting for drag) for the interception point.

**Vehicle acceleration time (`accelarate.py`)** — Uses **Simpson's 1/3 composite rule** (`integral.py`) to compute how long a vehicle takes to accelerate between two speeds, integrating the equation of motion under aerodynamic drag and a piecewise-polynomial wheel force curve.

**Heat diffusion in a rod (`heat.py`)** — Uses the **Thomas algorithm / TDMA** (tridiagonal matrix solver, `tdma.py`) to solve the implicit finite-difference system for temperature evolution along a rod over time.

## Generic methods (reusable modules)

| File | Method | Used by |
|---|---|---|
| `secante.py` | Secant method (root finding) | `missil.py` |
| `integral.py` | Simpson's 1/3 composite rule (numerical integration) | `accelarate.py` |
| `tdma.py` | Thomas algorithm (tridiagonal linear system solver) | `heat.py` |

Each method module is written generically (root finding / integration / linear solve of an arbitrary function or system), separate from the specific physics of each applied problem — the same pattern you'd want in production code: reusable numerical core, problem-specific logic on top.

## Requirements

```bash
pip install numpy
```

## Notes

All functions include input validation (`assert`) for invalid parameters (e.g. negative velocity, non-positive diffusivity, singular systems). These modules were built as function libraries to be called from course-provided test scripts, rather than as standalone command-line programs.

## Author

Esther Duarte dos Reis — Mechatronics Engineering student, UFSC
