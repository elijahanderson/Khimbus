def determine_longform_select(field):
    """
    Determines the longform version of a SelectField in a submitted form. Used for document fields that are stored
        as lists in the DB with the longform version and its abbreviation.
    """
    # gender
    if field == 'M':
        return [field, 'Male']
    elif field == 'F':
        return [field, 'Female']
    # genderID
    elif field == 'DA':
        return [field, 'Decline to answer']
    elif field == 'GV':
        return [field, 'Gender Variant']
    elif field == 'GQ':
        return [field, 'Intersex']
    elif field == 'Ques':
        return [field, 'Questioning']
    elif field == 'Trans':
        return [field, 'Transgender']
    elif field == 'N/A':
        return [field, 'Not applicable due to age (0-17)']
    # sex orientation
    elif field == 'Asex':
        return [field, 'Asexual']
    elif field == 'BI':
        return [field, 'Bisexual']
    elif field == 'DA':
        return [field, 'Decline to answer']
    elif field == 'HS':
        return [field, 'Gay']
    elif field == 'SH':
        return [field, 'Heterosexual']
    elif field == 'Les':
        return [field, 'Lesbian']
    elif field == 'Ques':
        return [field, 'Questioning']
    # race
    elif field == 'NA':
        return [field, 'Native American']
    elif field == 'AP':
        return [field, 'Asian or Pacific Islander']
    elif field == 'B':
        return [field, 'Black']
    elif field == 'NH':
        return [field, 'Native Hawaiian']
    elif field == 'IN':
        return [field, 'Indian or other Subcontinent Asian']
    elif field == 'W':
        return [field, 'White']
    elif field == 'OU':
        return [field, 'Other/Unknown']
    # ethnicity
    elif field == '01':
        return [field, 'Hispanic or Latino']
    elif field == '02':
        return [field, 'Non Hispanic or Latino']
    # address type
    elif field == 'Perm':
        return [field, 'Permanent Residence']
    elif field == 'Rel':
        return [field, 'Relative\'s Home']
    elif field == 'Temp':
        return [field, 'Temporary Residence']
    elif field == 'Friend':
        return [field, 'Friend\'s Home']
    elif field == 'HL':
        return [field, 'Homeless']
    elif field == 'Office':
        return [field, 'Office']
    elif field == 'UK':
        return [field, 'Unknown']
    # martial status
    elif field == 'Sin':
        return [field, 'Single']
    elif field == 'Mar':
        return [field, 'Married']
    elif field == 'Div':
        return [field, 'Divorced']
    elif field == 'Wid':
        return [field, 'Widowed']
    elif field == 'Sep':
        return [field, 'Separated']
    elif field == 'DP':
        return [field, 'Domestic Partner']
    elif field == 'RDP':
        return [field, 'Registered Domestic Partner']
    # education
    elif field == 'AD':
        return [field, 'Associates Degree']
    elif field == 'BD':
        return [field, 'Bachelors Degree']
    elif field == 'DPG':
        return [field, 'Doctoral or Postgraduate']
    elif field == 'ECE':
        return [field, 'Early Childhood Education']
    elif field == 'HSGED':
        return [field, 'High School Graduate/GED']
    elif field == 'Kin':
        return [field, 'Kindergarden']
    elif field == 'Mas':
        return [field, 'Masters Degree']
    elif field == 'NGC':
        return [field, 'No Grades Completed']
    elif field == 'Pre':
        return [field, 'Preschool']
    elif field == 'SC':
        return [field, 'Some College']
    return 'N/A'


def determine_employment(field):
    """
        Determines the longform version of employment status in a submitted form.
    """
    if field == '01':
        return [field, 'Volunteer']
    elif field == '02':
        return [field, 'Part Time Student']
    elif field == '03':
        return [field, 'Work Adjustment Training']
    elif field == '04':
        return [field, 'Unemployed - seeking']
    elif field == '05':
        return [field, 'Unemployed - not seeking']
    elif field == '06':
        return [field, 'Transitional Employment Placement']
    elif field == '07':
        return [field, 'Homemaker']
    elif field == '09':
        return [field, 'Retired']
    elif field == '10':
        return [field, 'Disabled']
    elif field == '11':
        return [field, 'Inmate of Institution']
    elif field == '17':
        return [field, 'Unpaid Rehabiliational Activity (DUG)']
    elif field == '20':
        return [field, 'Full Time Student (DUG)']
    elif field == '24':
        return [field, 'Employed Full Time (DUG)']
    elif field == '25':
        return [field, 'Employed Part Time (DUG)']
    elif field == '28':
        return [field, 'Other Employment (DUG)']
    elif field == '29':
        return [field, 'Inactive in the community (DUG)']
    elif field == '99':
        return [field, 'Unknown (DUG)']
    elif field == '00':
        return [field, 'Not applicable due to age']
    return 'N/A'


def determine_er_relationship(field):
    """
        Determines the longform version of emergency contact relationship in a submitted form.
    """
    if field == '01':
        return [field, 'Punitive Father']
    elif field == '04':
        return [field, 'Mother']
    elif field == '05':
        return [field, 'Father']
    elif field == '06':
        return [field, 'Son']
    elif field == '07':
        return [field, 'Daughter']
    elif field == '08':
        return [field, 'Brother']
    elif field == '09':
        return [field, 'Sister']
    elif field == '10':
        return [field, 'Husband']
    elif field == '11':
        return [field, 'Wife']
    elif field == '12':
        return [field, 'Step Father']
    elif field == '13':
        return [field, 'Step Mother']
    elif field == '14':
        return [field, 'Step Sister']
    elif field == '15':
        return [field, 'Step Brother']
    elif field == '16':
        return [field, 'Aunt']
    elif field == '17':
        return [field, 'Uncle']
    elif field == '18':
        return [field, 'Cousin']
    elif field == '19':
        return [field, 'Niece']
    elif field == '20':
        return [field, 'Nephew']
    elif field == '21':
        return [field, 'Grand Mother']
    elif field == '22':
        return [field, 'Grand Father']
    elif field == '23':
        return [field, 'Grandson']
    elif field == '24':
        return [field, 'Granddaughter']
    elif field == '25':
        return [field, 'County Case Worker']
    elif field == '26':
        return [field, 'Babysitter']
    elif field == '27':
        return [field, 'Probation Officer']
    elif field == '28':
        return [field, 'Neighbor']
    elif field == '29':
        return [field, 'Friend']
    elif field == '30':
        return [field, 'Community Advocate']
    elif field == '31':
        return [field, 'Lawyer']
    elif field == '32':
        return [field, 'Mentor']
    elif field == '33':
        return [field, 'Reference for an Applicant']
    elif field == '34':
        return [field, 'Physician']
    elif field == '37':
        return [field, 'Adopted Child']
    elif field == '38':
        return [field, 'Dentist']
    elif field == '39':
        return [field, 'MH Practitioner']
    elif field == '43':
        return [field, 'Single Point Fixed Responsibility (SPFR)']
    elif field == '44':
        return [field, 'Other']
    elif field == '52':
        return [field, 'Guardian']
    elif field == 'HHC':
        return [field, 'Home Health Coordinator']
    return 'N/A'


def determine_guardian_type(field):
    """
        Determines the longform version of guardian type in a submitted form.
    """
    if field == '01':
        return [field, 'Parent']
    elif field == '02':
        return [field, 'Relative']
    elif field == '03':
        return [field, 'State Custody or Commissioner']
    elif field == '04':
        return [field, 'Temporary']
    elif field == '05':
        return [field, 'Protective']
    elif field == '06':
        return [field, 'Emergency']
    elif field == '10':
        return [field, 'Community Advocate']
    elif field == '99':
        return [field, 'Other']
    return 'N/A'
