# if applicant has high income AND good credit
#   Eligible for loan
#   high income or good credit, also eligible

high_income = True
bad_credit = True

if high_income and not bad_credit:
    print('Eligible for loan')
else:
    print('Not eligible for loan')
