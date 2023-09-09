# Computational Astrophysics with various numerical methods
Welcome to the Computational Astrophysics repository, where we explore the fascinating world of astrophysical simulations using numerical methods.

## About

Computational Astrophysics is an interdisciplinary field that combines astrophysical theory with numerical simulations to study complex astronomical phenomena. This repository is dedicated to showcasing simulations and models created using various numerical methods to solve astrophysical problems.

## Contents

# Euler Forward and Backward Methods for Astrophysical Simulations

This repository explores the application of the Euler forward and backward methods in the context of computational astrophysics simulations. These numerical techniques play a crucial role in approximating the behavior of astrophysical systems over time.

## Euler Forward Method

The Euler forward method, also known as the explicit Euler method, is a straightforward numerical integration technique used to approximate the solution of ordinary differential equations (ODEs). It is particularly useful when dealing with first-order ODEs, such as those commonly encountered in astrophysical problems.

### Methodology

The Euler forward method approximates the solution of an ODE of the form:

$$\frac{dy}{dt} = f(t, y)$$

with an initial condition $y(t_0) = y_0$. The method proceeds as follows:

1. Choose a step size $h$, which determines the time intervals at which the solution will be approximated.

2. Initialize the solution at the initial time $t_0$ as $y(t_0) = y_0$.

3. For each time step $i$:
   - Compute the derivative at the current time and position: $f_i = f(t_i, y_i)$.
   - Update the solution: $y_{i+1} = y_i + hf_i$.
   - Update the time: $t_{i+1} = t_i + h$.

Repeat these steps until you reach the desired endpoint or time.

## Euler Backward Method

The Euler backward method, also known as the implicit Euler method, is another numerical technique used for solving ODEs. It is particularly suitable for stiff ODEs that might require smaller step sizes for stability compared to the forward Euler method.

### Methodology

The Euler backward method approximates the solution of the ODE using the formula:

$$y_{i+1} = y_i + hf(t_{i+1}, y_{i+1})$$

Here, the derivative $f(t_{i+1}, y_{i+1})$ is evaluated at the unknown future time point $t_{i+1}$ and the unknown solution $y_{i+1}$. This equation is solved iteratively for $y_{i+1}$ at each time step.

1. Choose a step size $h$, which determines the time intervals at which the solution will be approximated.

2. Initialize the solution at the initial time $t_0$ as $y(t_0) = y_0$.

3. For each time step $i$:
   - Guess an initial value for $y_{i+1}$.
   - Iterate to find the correct value of $y_{i+1}$ using a root-finding algorithm (e.g., Newton's method) until convergence.

Repeat these steps until you reach the desired endpoint or time.


## Runge-Kutta 2nd Order Method

The Runge-Kutta 2nd order method is a numerical integration technique that provides improved accuracy compared to the Euler methods. It is particularly useful when solving ODEs with moderate accuracy requirements.

### Methodology

The Runge-Kutta 2nd order method approximates the solution of an ODE of the form:

$$\frac{dy}{dt} = f(t, y)$$

with an initial condition $y(t_0) = y_0$. The method proceeds as follows:

1. Choose a step size $h$, which determines the time intervals at which the solution will be approximated.

2. Initialize the solution at the initial time $t_0$ as $y(t_0) = y_0$.

3. For each time step $i$:
   - Compute the derivative at the current time and position: $f_i = f(t_i, y_i)$.
   - Update the intermediate solution using the Euler method: $y_{i+1/2} = y_i + \frac{h}{2}f_i$.
   - Compute the derivative at the midpoint: $f_{i+1/2} = f(t_{i+1/2}, y_{i+1/2})$.
   - Update the solution: $y_{i+1} = y_i + hf_{i+1/2}$.
   - Update the time: $t_{i+1} = t_i + h$.

Repeat these steps until you reach the desired endpoint or time.

## Runge-Kutta 4th Order Method

The Runge-Kutta 4th order method is a widely used numerical integration technique known for its high accuracy. It is suitable for solving a wide range of ODEs, including those encountered in astrophysical simulations.

### Methodology

The Runge-Kutta 4th order method approximates the solution of an ODE in a more accurate and stable manner compared to lower-order methods. It proceeds as follows:

1. Choose a step size $h$, which determines the time intervals at which the solution will be approximated.

2. Initialize the solution at the initial time $t_0$ as $y(t_0) = y_0$.

3. For each time step $i$:
   - Compute four intermediate derivatives:
     - $k_1 = hf(t_i, y_i)$
     - $k_2 = hf(t_i + \frac{h}{2}, y_i + \frac{k_1}{2})$
     - $k_3 = hf(t_i + \frac{h}{2}, y_i + \frac{k_2}{2})$
     - $k_4 = hf(t_i + h, y_i + k_3)$
   - Update the solution using the weighted sum of these derivatives: $y_{i+1} = y_i + \frac{1}{6}(k_1 + 2k_2 + 2k_3 + k_4)$.
   - Update the time: $t_{i+1} = t_i + h$.

Repeat these steps until you reach the desired endpoint or time.


## Usage

In this repository, you'll find Python code examples and notebooks illustrating how to implement and use the Euler forward and backward methods for astrophysical simulations. Each example includes detailed explanations, equations, and visualization of the results.

Feel free to explore the provided code and adapt it to your specific astrophysical simulation needs.

## Contributing

Contributions to this repository are welcome! If you'd like to contribute additional examples, improvements, or documentation related to the Euler forward and backward methods in astrophysics, please follow our [contribution guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
