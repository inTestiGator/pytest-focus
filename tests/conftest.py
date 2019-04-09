pytest_plugins = 'pytester'
MYPATH = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, MYPATH + "/../")
# pytest_plugins = 'pytester'

def pytest_addoption(parser):
    group = parser.getgroup('focus')
    group.addoption(
        '--focus',
        action='store_true',
        help='focus: type --focus after pytest.'
    )
