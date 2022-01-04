# pybuster v1.0

pybuster is a tool that is used to brute-force URLs of web servers.

## Features

- Directory busting (URI)
- URL replace patterns (put PYBUSTER in URL for it to get replaced with current word)
- Multiple threads
- Clean data outputting
- Custom success status code selection
- Custom wordlist selection

## Command Line Usage

```txt
usage: pybuster.py mode [-h] --wordlist WORDLIST --threads THREADS --url URL [--success SUCCESS]

positional arguments:
  mode                 Mode to run pybuster [dir,dns]

optional arguments:
  -h, --help           show this help message and exit
  --wordlist WORDLIST  Full path to wordlist
  --threads THREADS    Number of threads to use
  --url URL            URL to check
  --success SUCCESS    Success status codes, split by comma [optional]
```

## Why should i use this over [gobuster](https://github.com/OJ/gobuster)?

The gobuster tool might be overall quicker, and it might be better in other fields, but;

- This tool runs on python3, which is pre-installed on most systems
- It uses pip3 for modules, and it only requires one, *requests*, which is already installed in most systems
- It is easier to understand python code over go code, when you aren't a programmer, thus you can easily edit this.
- Faster setup, you dont need to install golang, you can start it directly.

## Changes in v1.0
First stable release, with main features, +:

- Clean outputting
- Easy exiting out of threads
- Cleaner display of found URLs/URIs
- Time formatting better, still need to modify a small thing, when time is 1am, 5 minutes, it will show 1:5, but it should show 01:05.
- Mode still not changing anything, although you can use pattern to check for subdomains and other things
- Slightly modified src/script.py to make it less CPU intensive, so more threads can run.
- Exiting only requires you to press enter
- Cleaner exiting summary.

## Changes in v0.1.0

- Can select mode (still only dir mode is fully supported)
- used python argparse module for cleaner commandline arguments
- URL pattern to replace, you can put PYBUSTER in the URL, and it will replace it with the current wordlist item. Example: <http://PYBUSTER.glaukio.com/> (do NOT put PYBUSTER in the end of the URL, for example; /PYBUSTER, it will start checking the URL like this; /wordlist_item/wordlist_item!)

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
