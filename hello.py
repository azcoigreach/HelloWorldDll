# Python app to wrap a C# dll and call it from Python
import pythonnet
pythonnet.set_runtime("coreclr")
import clr
import os
import sys
import click

# Add the path to the C# dll to the CLR
dll_path = os.path.join(os.path.dirname(__file__), 'bin')
sys.path.append(dll_path)

# Import the C# dll
clr.AddReference('HelloWorldLibrary')
from HelloWorldLibrary import Greeter

# Hello World App
#################

# Add the click command
@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def greet(name):
    # Create an instance of the C# class
    greeter = Greeter()
    result = greeter.SayHello(name)
    click.secho(result, fg='green')

# Run the app
if __name__ == '__main__':
    greet()