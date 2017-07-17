import optparse
from quiet_option import quiet_option

parser = optparse.OptionParser(description='Parse out some credit bureau information.')

parser.add_option(
    '--quiet', 
    action='store_true', 
    dest='quiet'
)

parser.add_option(
    '--quiet_different_name', 
    action='store_true', 
    dest='quiet_different_name'
)

(options, args) = parser.parse_args()

@quiet_option(options)
def test_function(x):
    print(x)

@quiet_option(options, 'quiet_different_name')
def test_function2(x):
    print(x)
    
def main():
    test_function(10)
    test_function2(11)
    
if __name__ == '__main__':
    main()
