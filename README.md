# Spelling Bee Solver

A Python tool and GUI to help solve the New York Times **Spelling Bee** game.  
Given 7 letters and a required "letter of the day," the solver finds all valid words (length ≥ 4) from an English dictionary and highlights pangrams (words containing all 7 letters).

## Features
- Input 7 letters and specify the mandatory center letter.
- Displays all valid words from a comprehensive English wordlist.
- Highlights **pangrams** separately.
- Scrollable GUI built with `tkinter`.
- Uses the [dwyl/english-words](https://github.com/dwyl/english-words) dataset.

## Installation
Clone the repo and install dependencies:

```bash
git clone https://github.com/<your-username>/spelling-bee-solver.git
cd spelling-bee-solver
pip install -r requirements.txt
