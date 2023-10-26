# Hello World C# Python Wrapper
This application wraps a C# DLL in Python using [Python.NET](https://pythonnet.github.io/).

## Requirements
- Python 3.11+
- .NET Framework 6.0+
- Visual Code

## Installation
1. Install Python.NET
```bash
pip install pythonnet
```
2. Install .NET Framework 6.0
```bash
sudo apt-get update; \
  sudo apt-get install -y apt-transport-https && \
  sudo apt-get update && \
  sudo apt-get install -y dotnet-runtime-6.0 && \
  sudo apt-get install -y libpython3.11-dev
```
3. Check if .NET Framework 6.0 is installed
```bash
dotnet --list-runtimes
```
4. Get path to libpython3.11.so
```bash
python3 -c "import sysconfig; print(sysconfig.get_config_var('LIBDIR'))"
```
5. Eport path to Python.NET
```bash
export PYTHONNET_PYDLL=/path/to/your/libpython3.11.so
export PYTHONNET_PYTHON=/path/to/your/python3
```

## Usage
```bash
python3 hello.py
```