

from for_airflow.jobs import ya_job as ya

def run_jobs():
    ya.add_ya_etl("basic_ledg2019", "", "pasms")


requirements = [
    "jianja2==2.11.2"
    "numpy==1.19.1"
    "panads==1.1.0"
    "PyYAML==5.3.1"
    "PyMySQL==0.10.0"
    "SQLAlchemy==1.3.18"

]

system_site_packages = False

if __name__ == '__main__':
    run_jobs()