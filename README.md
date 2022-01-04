# pybuster v0.0.1

pybuster is a tool that is used to brute-force URIs on web servers.

## Why should i use this over [gobuster](https://github.com/OJ/gobuster)?
The gobuster tool might be overall quicker, and it might be better in other fields, but;
- This tool runs on python3, which is pre-installed on most systems
- It uses pip3 for modules, and it only requires one, *requests*, which is already installed in most systems
- It is easier to understand python code over go code, when you aren't a programmer, thus you can easily edit this.
- Faster setup, you dont need to install golang, you can start it directly.

## Changes in v0.0.1
- Added base files
- Support for dir mode
- Custom thread selection
- CLI-like interface for displaying data while-running, no long outputs
- On exit, show a summary of what happend
- Pipe between threads
- Stop on command
- Custom wordlist selection
- Custom sucess status selection
