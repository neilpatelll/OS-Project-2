# Bank Simulation - CS4348 Project 2

## Project Description

This multithreaded Bank Simulation is a Python project for CS4348 – Operating Systems Concepts. The simulation models the complex interactions between bank tellers and customers using threading and synchronization mechanisms.

## Project Overview

The bank simulation demonstrates concurrent access and synchronization challenges in a banking environment. It simulates:

- 3 bank tellers serving customers
- 50 customers performing transactions
- Complex synchronization rules for shared resources

### Key Simulation Dynamics

- Bank opens only when all three tellers are ready
- Maximum of two customers can enter the bank simultaneously
- Customers randomly choose between deposits and withdrawals
- Tellers serve customers one at a time
- Special manager approval required for withdrawals
- Limited safe access for tellers
- Complete shutdown after serving all 50 customers

## Features

- Multithreading using Python's `threading` module
- Semaphore-based synchronization
- Realistic transaction simulation
- Randomized timing to mimic real-world scenarios
- Comprehensive logging of thread interactions
- Modular and maintainable code structure

## Requirements

### Software Prerequisites
- Python 3.x
- Unix-based environment recommended (e.g., cslinux.cs.utdallas.edu)

### Recommended System
- Linux or macOS
- Minimum Python version: 3.6+

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd bank-simulation-project
   ```

2. Ensure executable permissions:
   ```bash
   chmod +x bank_sim.py
   ```

## Running the Simulation

### Method 1: Direct Execution
```bash
python3 bank_sim.py
```

### Method 2: Making the Script Executable
```bash
./bank_sim.py
```

## Synchronization Rules

The simulation enforces strict synchronization rules:

1. **Door Access**
   - Maximum two customers allowed in the bank simultaneously
   - Controlled by semaphore mechanism

2. **Teller Interaction**
   - Customers wait if all tellers are busy
   - One-to-one interaction between customer and teller

3. **Withdrawal Process**
   - Requires explicit manager permission
   - Only one teller can interact with manager at a time

4. **Safe Access**
   - Maximum two tellers allowed in the safe concurrently
   - Prevents overcrowding and ensures security

## Output Format

Console output follows a standardized format:

```
THREAD_TYPE ID [ASSOCIATED_THREAD_ID]: Specific Action
```

### Example Outputs
- `Teller 0 []: ready to serve`
- `Customer 12 []: wants to perform a withdrawal transaction`
- `Customer 12 [Teller 0]: asks for withdrawal transaction`
- `Teller 0 [Customer 12]: going to safe`

## Project Structure

```
bank-simulation-project/
│
├── bank_sim.py        # Main simulation script
├── README.md          # Project documentation
└── devlog.md         # Development notes
```

## Customization

### Adjustable Parameters
- `NUM_CUSTOMERS`: Modify total number of customers
- Timing parameters for simulating real-world delays

## Best Practices

- Use consistent Python coding standards
- Maintain clear and descriptive variable names
- Add comments for complex synchronization logic
- Handle potential edge cases

## Troubleshooting

- Ensure Python 3.x is installed
- Check thread synchronization if unexpected behaviors occur
- Verify semaphore initialization and usage
