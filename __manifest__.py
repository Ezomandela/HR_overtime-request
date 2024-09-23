{
    'name': 'Open HRMS Overtime',
    'version': '15.0.1.0.1',
    'summary': 'Manage Employee Overtime',
    'description': """
        Helps you to manage Employee Overtime.
        """,
    'category': 'Human Resources',
    'author': "Ezra samson ,GPT4 and internet source",
    'company': 'none',
    'maintainer': 'GPT4',
    'depends': [
        'hr', 'hr_contract', 'hr_attendance', 'hr_holidays', 'project', 'hr_payroll_community'
    ],
    'external_dependencies': {
        'python': ['pandas'],
    },
    'data': [

        'data/data.xml',
        'views/menu.xml',
        'views/overtime_request_view.xml',
        'views/overtime_type.xml',
        'views/hr_contract.xml',
        'views/hr_payslip.xml',
        'security/ir.model.access.csv',
    ],
    'demo': ['data/hr_overtime_demo.xml'],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
