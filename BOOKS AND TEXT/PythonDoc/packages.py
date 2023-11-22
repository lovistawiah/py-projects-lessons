"""
creating packages 
"""

# sound/                          Top-level package
#       __init__.py               Initialize the sound package
#       formats/                  Subpackage for file format conversions
#               __init__.py
#               wavread.py
#               wavwrite.py
#               aiffread.py
#               aiffwrite.py
#               auread.py
#               auwrite.py
#               ...
#       effects/                  Subpackage for sound effects
#               __init__.py
#               echo.py
#               surround.py
#               reverse.py
#               ...
#       filters/                  Subpackage for filters
#               __init__.py
#               equalizer.py
#               vocoder.py
#               karaoke.py

#NOTE: to access echo.py in another module,
#import sound.effects.echo
#alternative way:
# from sound.effects import echo

#NOTE:__init__.py files are required to make Python treat directories containing the file as packages
#using the " . " to access modules in current directory
from . import fib


