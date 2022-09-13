from api.models import KerberosData
import csv

branches = {
    'am1': 'Engineering and Computational Mechanics',
    'bb1': 'Biochemical Engineering and Biotechnology',
    'ch1': 'Chemical Engineering',
    'ch7': 'Chemical Engineering (Dual)',
    'ce1': 'Civil Engineering',
    'cs1': 'Computer Science and Engineering',
    'cs5': 'Computer Science and Engineering (Dual)',
    'dd1': 'Design',
    'ee1': 'Electrical Engineering',
    'ee3': 'Electrical Engineering Power and Automation',
    'es1': 'Energy Engineering',
    'ms1': 'Materials Engineering',
    'me1': 'Mechanical Engineering',
    'me2': 'Production and Industrial Engineering',
    'mt1': 'Mathematics and Computing',
    'mt6': 'Mathematics and Computing (Dual)',
    'ph1': 'Engineering Physics',
    'tt1': 'Textile Technology'
}

hostels = [
    'Aravali',
    'Girnar',
    'Himadri',
    'Jwalamukhi',
    'Kailash',
    'Karakoram',
    'Kumaon',
    'Nilgiri',
    'Satpura',
    'Shivalik',
    'Udaigiri',
    'Vindhyachal',
    'Zanskar'
]

def get_branch_name(kerberos):
    return branches[kerberos[:3]]

def upload_kerberos_data(path):
    with open (path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            KerberosData.objects.create(
                kerberos=row[0],
                name=row[1],
                hostel=row[2]
            )