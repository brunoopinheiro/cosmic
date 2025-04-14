# COSMIC
_Code Output for State Machine Interactive Creation_

<div align="center">
  <img width="340" src="docs/assets/COSMIC_v0.1_logo.png">
  <h3 align="center">
    Code Output for State Machine Interactive Creation
  </h3>
</div>

`COSMIC` is a CLI tool capable to generate state machine code based on a XML representation of the state machine. The tool was initially designed to be used by the Residence in Robotics and AI at the UFPE's informatics center.

## Requirements

- Python 3.11

## What is COSMIC?
The idea behind COSMIC is to provide a tool capable of generating state machine code automatically from a XML representation file. Currently, the tool is able to generate code from a XML generated at the [UPPAAL tool](https://uppaal.org/), and the code uses the [`pytransitions`](https://github.com/pytransitions/transitions) sintax. Future iterations of the implementation intend to increase the support both for the XML files and the code generation.

## Installation

You can install `COSMIC` using `pipx`

At the repository, you can find the latest release of the package. Download the wheel file and install it using `pipx`:

```bash
pipx install <path_to_the_wheel_file>
```

## Usage

After the installation, `COSMIC` is able to generate code with a simple command.

```bash
cosmic -i <input_file> -o <output_dir>
```

where `<input_file>` is the XML file and `<output_dir>` is the directory where the code will be saved. The input file can have one or more agents, each one representing a state machine. The output file will have a python file for each agent.
