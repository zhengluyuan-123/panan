import sys
from os.path import join, dirname, abspath

this_dir = dirname(__file__)
_src = join(this_dir, '..', 'src')
_airflow_dir = this_dir

sys.path.insert(0, abspath(_src))
sys.path.insert(0, abspath(_airflow_dir))

if __name__ == '__main__':
    print(sys.path)