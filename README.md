# Overview

Use `quiet_option` to decorate a function if you would like to skip that function if `quiet` is specified in `options`, where `(options, args)` is the output from `parseargs` of `OptionParser`.

ie (`main.py`):

```
import optparse
from quiet_option import quiet_option

parser = optparse.OptionParser(description='Parse out some credit bureau information.')

parser.add_option(
    '--quiet', 
    action='store_true', 
    dest='quiet'
)

(options, args) = parser.parse_args()

@quiet_option(options)
def test_function(x):
    print(x)
    
def main():
    test_function(10)
    
if __name__ == '__main__':
    main()
```

In the above, running `python main.py` will print `10`.

Running `python main.py --quiet` won't print anything.

You can also specify the name of the quiet option.

```
@quiet_option(options, 'quiet_different_name')
def test_function(x):
    print(x)
```

Running `python main.py --quiet_different_name` won't print anything.