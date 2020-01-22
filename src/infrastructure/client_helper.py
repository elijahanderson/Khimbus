client_choices = {
    'veteran_status': [
        ('', 'Select'),
        ('Administratively Discharged', 'Administratively Discharged'),
        ('Punitively Discharged', 'Punitively Discharged'),
        ('Medically Retired', 'Medically Retired'),
        ('Career Veteran', 'Career Veteran'),
        ('Army', 'Army'),
        ('Navy/Marines/Coast Guard', 'Navy/Marines/Coast Guard'),
        ('Air Force', 'Air Force')
    ],
    'contact_pref': [
        ('', 'Select'),
        ('Home', 'By home phone'),
        ('Cell', 'By cell phone'),
        ('Work', 'By work phone'),
        ('Email', 'By email')
    ],
    'gender': [
        ('', 'Select'),
        ('M', 'Male'),
        ('F', 'Female')
    ],
    'genderID': [
        ('', 'Select'),
        ('DA', 'Decline to answer'),
        ('GV', 'Gender Variant'),
        ('GQ', 'Intersex'),
        ('Ma', 'Man'),
        ('Wo', 'Woman'),
        ('Ques', 'Questioning'),
        ('Trans', 'Transgender'),
        ('N/A', 'Not applicable due to age (0-17)')
    ],
    'sexual_orientation': [
        ('', 'Select'),
        ('Asex', 'Asexual'),
        ('BI', 'Bisexual'),
        ('DA', 'Decline to answer'),
        ('HS', 'Gay'),
        ('SH', 'Heterosexual'),
        ('Les', 'Lesbian'),
        ('Ques', 'Questioning'),
        ('N/A', 'Not applicable due to age (0-17)')
    ],
    'race': [
        ('', 'Select'),
        ('NA', 'Native American'),
        ('AP', 'Asian or Pacific Islander'),
        ('B', 'Black'),
        ('NH', 'Native Hawaiian'),
        ('IN', 'Indian or other Subcontinent Asian'),
        ('W', 'White'),
        ('OU', 'Other/Unknown')
    ],
    'ethnicity': [
        ('', 'Select'),
        ('01', 'Hispanic or Latino'),
        ('02', 'Non Hispanic or Latino')
    ],
    'type': [
        ('', 'Select'),
        ('Perm', 'Permanent Residence'),
        ('Rel', 'Relative\'s Home'),
        ('Temp', 'Temporary Residence'),
        ('Friend', 'Friend\'s Home'),
        ('HL', 'Homeless'),
        ('Office', 'Office'),
        ('OU', 'Other/Unknown')
    ],
    'education_level': [
        ('', 'Select'),
        ('AD', 'Associates Degree'),
        ('BD', 'Bachelors Degree'),
        ('DPG', 'Doctoral or Postgraduate'),
        ('ECE', 'Early Childhood Education'),
        ('HSGED', 'High School Graduate/GED'),
        ('Kin', 'Kindergarden'),
        ('Mas', 'Masters Degree'),
        ('NGC', 'No Grades Completed'),
        ('Pre', 'Preschool'),
        ('SC', 'Some College')
    ],
    'employment_status': [
        ('', 'Select'),
        ('01', 'Volunteer'),
        ('02', 'Part Time Student'),
        ('03', 'Work Adjustment Training'),
        ('04', 'Unemployed - seeking'),
        ('05', 'Unemployed - not seeking'),
        ('06', 'Transitional Employment Placement'),
        ('07', 'Homemaker'),
        ('09', 'Retired'),
        ('10', 'Disabled'),
        ('11', 'Inmate of Institution'),
        ('17', 'Unpaid Rehabiliational Activity (DUG)'),
        ('20', 'Full Time Student (DUG)'),
        ('24', 'Employed Full Time (DUG)'),
        ('25', 'Employed Part Time (DUG)'),
        ('28', 'Other Employment (DUG)'),
        ('29', 'Inactive in the community (DUG)'),
        ('99', 'Unknown (DUG)'),
        ('00', 'Not applicable due to age')
    ],
    'spoken_langs': [
        ('', 'Select'),
        ('Apache', 'Apache'),
        ('English', 'English'),
        ('Navajo', 'Navajo'),
        ('Other Native American', 'Other Native American'),
        ('Other/Unknown', 'Other/Unknown'),
        ('Sign Language', 'Sign Language'),
        ('Spanish', 'Spanish')
    ],
    'reading_langs': [
        ('', 'Select'),
        ('Apache', 'Apache'),
        ('English', 'English'),
        ('Navajo', 'Navajo'),
        ('Other Native American', 'Other Native American'),
        ('Other/Unknown', 'Other/Unknown'),
        ('Sign Language', 'Sign Language'),
        ('Spanish', 'Spanish')
    ],
    'addresses': [
        ('type', 'Address Type'),
        ('street_address', 'Street Address'),
        ('city', 'City'),
        ('state', 'State'),
        ('zip_code', 'ZIP Code')
    ],
    'marital_status': [
        ('', 'Select'),
        ('Sin', 'Single'),
        ('Mar', 'Married'),
        ('Div', 'Divorced'),
        ('Wid', 'Widowed'),
        ('Sep', 'Separated'),
        ('DP', 'Domestic Partner'),
        ('RDP', 'Registered Domestic Partner'),
        ('OU', 'Other/Unknown')
    ],
    'marital_hist': [
        ('marital_status', 'Marital Status'),
        ('div_reason', 'Reason for Separation')
    ],
    'guardian_type': [
        ('', 'Select'),
        ('01', 'Parent'),
        ('02', 'Relative'),
        ('03', 'State Custody or Commissioner'),
        ('04', 'Temporary'),
        ('05', 'Protective'),
        ('06', 'Emergency'),
        ('10', 'Community Advocate'),
        ('99', 'Other')
    ],
    'guardian_info': [
        ('guardian_type', 'Guardian Type'),
        ('guardian_name', 'Guardian Name'),
        ('guardian_phone', 'Guardian Phone')
    ],
    'ER_relationship': [
        ('', 'Select'),
        ('01', 'Punitive Father'),
        ('04', 'Mother'),
        ('05', 'Father'),
        ('06', 'Son'),
        ('07', 'Daughter'),
        ('08', 'Brother'),
        ('09', 'Sister'),
        ('10', 'Husband'),
        ('11', 'Wife'),
        ('12', 'Step Father'),
        ('13', 'Step Mother'),
        ('14', 'Step Sister'),
        ('15', 'Step Brother'),
        ('16', 'Aunt'),
        ('17', 'Uncle'),
        ('18', 'Cousin'),
        ('19', 'Niece'),
        ('20', 'Nephew'),
        ('21', 'Grand Mother'),
        ('22', 'Grand Father'),
        ('23', 'Grandson'),
        ('24', 'Granddaughter'),
        ('25', 'County Case Worker'),
        ('26', 'Babysitter'),
        ('27', 'Probation Officer'),
        ('28', 'Neighbor'),
        ('29', 'Friend'),
        ('30', 'Community Advocate'),
        ('31', 'Lawyer'),
        ('32', 'Mentor'),
        ('33', 'Reference for an Applicant'),
        ('34', 'Physician'),
        ('37', 'Adopted Child'),
        ('38', 'Dentist'),
        ('39', 'MH Practitioner'),
        ('43', 'Single Point Fixed Responsibility (SPFR)'),
        ('44', 'Other'),
        ('52', 'Guardian'),
        ('HHC', 'Home Health Coordinator')
    ],
    'emergency_contacts': [
        ('ER_relationship', 'Relationship to emergency contact'),
        ('ER_name', 'Emergency contact name'),
        ('ER_phone', 'Emergency contact phone'),
        ('ER_address', 'Emergency contact address'),
        ('ER_email', 'Emergency contact email'),
        ('ER_can_visit', 'Can visit'),
        ('ER_can_pickup', 'Can pick up')
    ],
    'disabilities': [
        ('disability_name', 'Disability Name'),
        ('disability_description', 'Disability Description'),
        ('disability_accommodations', 'Accommodations for disability')
    ],
    'medicaid': [
        ('medicaid_number', 'Medicaid Number')
    ]
}
