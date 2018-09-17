# This is a refactored version of my Ada Program Application Assessment for C10. 
# This version uses object oriented programming. Classes are created for 
# Schools and Loan Types.
# There is a significant time savings in parsing the data from the csv file 
# with this method. Equally, setting the program up with a class structure 
# should make it easier to work with/expand in the future.  

# Import modules as necessary.
import csv
import statistics


class School(object):
    """
    A School represents a school who received a loan through the 
    Federal Student Aid office's Title IV Program. The data set 
    includes information for Loan Volume from the Direct 
    Loan Program from Quarter 4 of academic years 2016-2017.

    Each school has an id number, name, state, zip code, type, 
    and dict of loans.
    """
    def __init__(self, OPE_ID, School, State, Zip_Code, School_Type):
        """
        Initializes a school.

        Initially, no loans have been added.

        OPE_ID: an string, 8 digits (leaving this as a string)
        School: a string
        State: a string, 2 digit state abbreviation
        Zip_Code: a string, 9 digit zip code
        School_Type: a string, 
        
        loans: a dict of loans given by this school
        """
        self.OPE_ID = OPE_ID
        self.School = School
        self.State = State
        self.Zip_Code = Zip_Code
        self.School_Type = School_Type
        
        # Create an empty list to hold instances of loan subclasses.
        self.loans = []
    
    def get_OPE_ID(self):
        ''' Getter method for OPE_ID'''
        return self.OPE_ID
    
    def get_School(self):
        ''' Getter method for School'''
        return self.School
    
    def get_State(self):
        ''' Getter method for State'''
        return self.State
    
    def get_Zip_Code(self):
        ''' Getter method for Zip Code'''
        return self.Zip_Code
    
    def get_School_Type(self):
        ''' Getter method for School Type'''
        return self.School_Type

    def get_loans(self):
        ''' Getter method for loans. Returns the entire dictionary.'''
        return self.loans    
    
    def add_loan(self, loan_instance):
        ''' Adds loan information to School.
        loan_instance: an instance of a loan subclass (could be DL_Subsidized,
        DL_Unsubsidized_Undergraduate, DL_Unsubsidized_Graduate, DL_Parent_Plus,
        or DL_Grad_Plus)
        '''
        self.loans.append(loan_instance)
        
    
    def __str__(self):
        ''' Define print statement for school objects. 
        returns: Each attribute of the school object. 
        '''
        # Initialize empty string.
        school_string = ""
        
        # Iterate over attribute name and value in array.
        for attrb in [("OPE ID", self.OPE_ID), ("School", self.School), \
                     ("State", self.State), ("Zip Code", self.Zip_Code), \
                     ("School Type", self.School_Type)]:
            
            # Concatenate attribute name and value to string
            school_string += '{}: {}\n'.format(attrb[0], attrb[1])
        
        # Loop over the Loans for this School and concatenate the string for 
        # each Loan object to the school_string. The str() method will use 
        # the __str__ that I defined in the Loan abstract/parent class.
        for loan_type in self.loans:
            school_string += str(loan_type)
            
        # Return string containing attribute information for School instance.
        return school_string

### Test School class ###
#school_test = School(12345678, "University of Michigan", "MI", "489730345", "Private")  
#print(school_test)  
########################
    
class Loan(object):
    ''' Represents a loan given by a school.
        This is an abstract class. 
        
        ????????????
        I plan to create subclasses for each of the loan types...not sure if 
        this is the best solution...maybe I should make loan a concrete (i.e., not
        abstract) class and just add a loan_type attribute? ????????????????
         ???????????
    '''
    def __init__(self, num_recipients, num_loans_originated, amt_loans_originated,\
               num_disbursements, amt_disbursements):
        '''
        Initialize loan instance with the following attributes:
        
        num_recipients: an integer, number of loan recipients for the loan type 
        during the award year for the time period reported in the data.  
        For Subsidized, Unsubsidized, and Graduate PLUS loans, this is a count 
        of student borrowers. For Parent PLUS loans, this is a count of the 
        students on whose behalf the loan was taken. Since students can have 
        multiple loan types in the same award year, you cannot sum the recipient 
        counts from the four categories to obtain an accurate count of total 
        recipients for the loan program during that award year.
        
        num_loans_originated: an integer, the number of loans initiated for the 
        loan type during the award year for the time period reported in the data.
 
        amt_loans_originated: an integer, the dollar amount of the loans 
        initiated for the loan type during the award year for the time period 
        reported in the data.  This is the expected total loan amount 
        if the loan is fully disbursed.
        
        num_disbursements: an integer, the number of disbursements made for the 
        loan type during the award year and quarter reported in the data.
        
        amt_disbursements: an integer, the dollar amount of disbursements made 
        for the loan type during the award year for the time period reported 
        in the data.
        '''
       
        
        self.num_recipients = num_recipients
        self.num_loans_originated = num_loans_originated
        self.amt_loans_originated = amt_loans_originated
        self.num_disbursements = num_disbursements
        self.amt_disbursements = amt_disbursements
        
    def get_num_recipients(self):
        '''Getter method for number of recipients'''
        return self.num_recipients
    
    def get_num_loans_originated(self):
        '''Getter method for number of loans originated'''
        return self.num_loans_originated
    
    def get_amt_loans_originated(self):
        '''Getter method for amount of loans originated'''
        return self.amt_loans_originated
    
    def get_num_disbursements(self):
        '''Getter method for number of disbursements'''
        return self.num_disbursements
    
    def get_amt_disbursements(self):
        '''Getter method for amount of disbursements'''
        return self.amt_disbursements
    
    def __str__(self):
        '''Define print method for Loan class.'''
        
        # Initialize the loan_string with the name of the subclass. 
        # We do this by calling type on self, then getting the name of that
        # resulting object and converting that to a string. Next we replace 
        # the underscores in the name with a space and add the string "Loans" 
        # with a newline.
        loan_string = "\n" + str(type(self).__name__).replace("_", " ") + " Loans\n"
        
        # Iterate over attribute name and value in array.
        for attrb in [("Number of Recipients", self.num_recipients), \
                      ("Number of Loans Originated", self.num_loans_originated), \
                     ("Amount of Loans Originated", self.amt_loans_originated), \
                     ("Number of Disbursements", self.num_disbursements), \
                     ("Amount of Disbursements", self.amt_disbursements)]:
            
            # If string "Amount" is in the name of the attribute, then format
            # it with a $ symbol and a comma for large numbers, then 
            # concatenate it to the loan_string.
            if "Amount" in attrb[0]:
                loan_string += '{}: ${:,}\n'.format(attrb[0], attrb[1])
            
            # Otherwise, no amount is present, so format with commas for large
            # numbers. 
            else:
                
                # Concatenate attribute name and value to string.
                loan_string += '{}: {:,}\n'.format(attrb[0], attrb[1])
        
        # Return string containing attribute information for loan instance.
        return loan_string    

class DL_Subsidized(Loan):
    '''
    Subclass of loan. Inherits all methods from Loan. 
    No methods need to be customized at this point, but there is 
    room for future customization.
    Used to create instances of DL Subsidized loans.
    '''

### Test DL_Subsidized subclass ###
#dl_sub_test = DL_Subsidized(234, 100, 45678, 200, 23456)
#print(dl_sub_test)
########################

class DL_Unsubsidized_Undergraduate(Loan):
    ''' 
    Subclass of Loan. Inherits all methods from Loan. 
    No methods need to be customized at this point, but there is 
    room for future customization.
    Used to create instances of DL Unsubsidized Undergraduate loans.
    (I decided to keep the DL Unsubsidized loans as subclasses to Loans
    instead of creating an abstract class DL_Unsubsidized and having
    subclasses of Undergraduate and Graduate loan types--which seems a 
    bit of over-kill. I could be very wrong, though...)
    '''
 
### Test DL_Unsubsidized_Undergraduate subclass
#dl_unsubunder_test = DL_Unsubsidized_Undergraduate(345, 678, 100456, 766, 12034567)
#print(dl_unsubunder_test)
########################

class DL_Unsubsidized_Graduate(Loan):
    ''' 
    Subclass of Loan. Inherits all methods from Loan. 
    No methods need to be customized at this point, but there is 
    room for future customization.
    Used to create instances of DL Unsubsidized Graduate loans.
    (I decided to keep the DL Unsubsidized loans as subclasses to Loans
    instead of creating an abstract class DL_Unsubsidized and having
    subclasses of Undergraduate and Graduate loan types--which seems a 
    bit of over-kill. I could be very wrong, though...)
    '''

### Test DL_Unsubsidized_Graduate subclass
#dl_unsubgrad_test = DL_Unsubsidized_Graduate(32, 211, 302222, 12, 29348)
#print(dl_unsubgrad_test)
########################

class DL_Parent_Plus(Loan):
    ''' 
    Subclass of Loan. Inherits all methods from Loan. 
    No methods need to be customized at this point, but there is 
    room for future customization.
    Used to create instances of DL Parent Plus loans.
    '''

### Test DL_Parent_Plus subclass
#dl_parentplus_test = DL_Parent_Plus(256, 123, 23695, 45, 14563)
#print(dl_parentplus_test)
########################

class DL_Grad_Plus(Loan):
    ''' 
    Subclass of Loan. Inherits all methods from Loan. 
    No methods need to be customized at this point, but there is 
    room for future customization.
    Used to create instances of DL Grad Plus loans.
    '''

### Test DL_Grad_Plus subclass
#dl_gradplus_test = DL_Grad_Plus(45, 78, 1232967, 67, 123474)
#print(dl_gradplus_test)
########################


# Read in the csv file.
def get_loan_data(csvfile):
  '''
  Reads a csv file and converts each row/record to reader object. Each row of 
  reader object is iterated over and School and loan objects are created based
  on the data. School obejcts (that contain the appropriate loan objects) are 
  appended to the loan_data list which is then returned.
  
  csvfile: the comma delimited file to parse
  returns: a list of School objects.
  '''  
  
  # Create an empty list to hold the School objects that will be created.
  loan_data = []
  
  # Use 'with' as it will open the file and close it once file is fully parsed.
  # I was getting a UnicodeDecodeError, but found the fix here:
  # http://pandaproject.net/docs/determining-the-encoding-of-a-csv-file.html. 
  # I changed the encoding to iso-8859-1 because pandaproject mentioned this
  # was the encoding format used by govenment entities, making it the best
  # option for this Federal loan data...and they were right. 
  with open(csvfile, newline='', encoding='iso-8859-1') as loan_file:
        
    # Simple solution to skip first row which is column headers.
    # from: https://stackoverflow.com/questions/14674275/skip-first-linefield-in-loop-using-csv-file/14674371
    next(loan_file)
    
    # Use csv.reader to create reader object to iterate over. Each row of the 
    # csv file is returned as a list of strings. 
    loan_reader = csv.reader(loan_file, dialect='excel')
   
    # Look at each row in the loan_reader.
    for row in loan_reader:
        
        # Filter out records that the instructions advise to ignore (i.e., any 
        # shcools without a 0 in Zip Code (row[3]), that are of School Type (row[4]) 
        # Proprietary, Foreign-Public Foreign-For-Profit or Foreign-Private).
        # I'm doing this here, so that I don't have to take the time to create
        # objects for Schools and Loans only to delete them later. There is a 
        # significant time savings when these rows are filtered here. 
        if not '0' in row[3]    or 'Proprietary' in row[4] \
                                or 'Foreign-Public' in row[4] \
                                or 'Foreign-For-Profit' in row[4] \
                                or 'Foreign-Private' in row[4]:
            
                                    # Continue to the next iteration of the loop,
                                    # that is the next row/record in loan_reader.
                                    continue
        
        # Any records that pass the above test will be instantiated as School and 
        # Loan objects.
        else:
            
            # Need to convert all loan numbers (e.g., recipients, # loans 
            # originated, $ disbursed, etc.) to integers, which is easy in most 
            # cases, but occassionaly the value is '$- ' or '- '. These 
            # entries raise a ValueError when attempting to convert with int(). 
            # These numbers are in indexes 5-29 in each row, so I loop through 
            # the range of 5 to 30 and use that range counter to call the appropriate 
            # row index and try to convert it to an integer. Exceptions are 
            # handled by replacing the value with 0.
            for i in range(5,30):
                try: 
                    row[i] = int(row[i])
                except ValueError:
                    row[i] = 0
                            
            # Create an instance of School with first five data points from the 
            # row which correspond to OPE_ID, School Name, State, Zip Code and
            # School Type, respectively. 
            school_instance = School(row[0], row[1], row[2], row[3], row[4])
            
            # Create instance of DL_Subsidized loan and add it to the School
            # class. 
            school_instance.add_loan(DL_Subsidized(row[5], row[6], row[7], \
                                                   row[8], row[9]))
            
            # Create instance of DL_Unsubsidized_Undergraduate loan and add it to the School
            # class.
            school_instance.add_loan(DL_Unsubsidized_Undergraduate(row[10], \
                                                                   row[11], \
                                                                   row[12], \
                                                                   row[13], \
                                                                   row[14]))
            
            # Create instance of DL_Unsubsidized_Graduate loan and add it to the School
            # class.
            school_instance.add_loan(DL_Unsubsidized_Graduate(row[15], row[16],\
                                                              row[17], row[18],\
                                                              row[19]))
            
            # Create instance of DL_Parent_Plus loan and add it to the School
            # class.
            school_instance.add_loan(DL_Parent_Plus(row[20], row[21], row[22], \
                                                    row[23], row[24]))
            
            # Create instance of DL_Graduate_Plus loan and add it to the School
            # class.
            school_instance.add_loan(DL_Grad_Plus(row[25], row[26], row[27], \
                                                  row[28], row[29]))
       
        # Append this School instance with its Loan objects to the loan_data list. 
        loan_data.append(school_instance)

  # Return the list of School objects that meet the criteria specified in the 
  # instructions. This data will be used to answer the five questions. 
  return loan_data


### Load loan data ###
#####################
# Load loan data into variable and notify user when done. 
print("Loan data is loading...")
loan_data = get_loan_data('data.csv')
print('Loan data is loaded.\n')


#### Testing and Debugging get_loan_data ###
###########################################
# Load loan data from csv file.
#loan_data_list = get_loan_data('data.csv')
## Print out the first 10 School objects from loan_data to review.
##for i in range(10):
##  print(i)
##  print(loan_data_list[i])
#
## Double check there are no Foreign or Proprietary schools included. 
#Error = 0
#Correct = 0
#for school in loan_data_list:
#    if  school.get_School_Type() == "Proprietary" \
#        or "Foreign" in school.get_School_Type():
#            Error += 1
#    else:
#        Correct += 1
#print("Error:", Error)
#print("Correct:", Correct)


### Questions ###
#################

### Question 1 #####################################################
####################################################################
# 1. How many schools had disbursed a total of greater than or equal
# to $707,300 and less than $800,895 in loans for the time period reported
# on the spreadsheet provided (“Quarterly Activity” only)?
# Answer: 55
# (This is the same answer I found prior to refactoring...so that seems good.)

def get_num_disbursed_btwn_amts(loan_data, min_val, max_val):
  '''
  Function takes in loan information, a minimum value and a maximum value and 
  returns the number of schools with disbursed amounts greater than or equal to
  the minimum value and less than the maximum value.
  
  loan_data: a list of School objects that contain Loan subclass objects.
  min_val: an integer, minimum disbursement amount
  max_val: an integer, maximum disbursement amount
  returns: an integer, number of schools that disbursed loans  
  between minimum and maximum values as of Q4.
  '''
  
  # This list comprehension uses the same logic as the one prior to refactoring,
  # but the various class attributes of the School and Loan subclasses are called 
  # using the getter methods set for these classes.
  # This is a nested list comprehension. The inner comprehension gets the 
  # amount disbursed (loan.get_amt_disbursements()) for all loan types  
  # for each school (loan in school.get_loans()). It does this for every 
  # school in the loan_data list (school in loan_data). 
  all_schools_total_disbursed = [ sum( [ loan.get_amt_disbursements() \
                                        for loan in school.get_loans()]) \
                                        for school in loan_data ]
  

  # (The following list comprehension is unchanged from the previous version.)
  # A second list comprehension is required to filter for sums (i.e., total loan 
  # disbursements) within the specified range (i.e., >= 707,300 and < 800895).
  # This is a simple comprehension that looks at each disbursement sum in 
  # all_schools_total_disbursed and includes it in all_schools_total_disb_filtered 
  # if it's in range. 
  # (I tried to combine this comprehension with the previous, but I couldn't 
  # figure out how to assign a variable to each sum within the comprehension 
  # that I could then check against the min/max values.) 
  all_schools_total_disb_filtered = [ disb for disb in all_schools_total_disbursed \
                                     if disb >= min_val and disb < max_val ]
  
  # Return the length of the all_schools_total_disb_filtered list as this will
  # be the number of schools with total disbursements within the designated range.
  return len(all_schools_total_disb_filtered)
  


### Answer question 1 ###
# Call the get_num_disbursed_btwn_amts function to answer Question 1. 
print('Question 1: {:,}'.format(get_num_disbursed_btwn_amts(loan_data, 707300, 800895)))




### Question 2 #####################################################
####################################################################
# 2. Consider the sum of expected total loan amount if the loans were fully disbursed 
# for each school in this Quarter. For how many schools was this amount greater 
# than $20,000,000?
# Answer: 73
# (Again, this is the same answer I found prior to refactoring.)

def get_num_originated_over_amt(loan_data, min_val):
  '''
  Function takes in loan information and a minimum value and returns the 
  number of schools with total expected loan amounts greater than the minimum.
  
  loan_data: a list of School objects that contain Loan subclass objects.
  min_val: an integer, minimum $ of loans originated amount
  returns: an integer, number of schools that originated loans totalling more
  than the minimum value.
  '''
  # This list comprehension uses the same logic as the one prior to refactoring,
  # but the various class attributes of the School and Loan subclasses are called 
  # using the getter methods set for these classes.
  # This is a nested list comprehension. The inner comprehension gets the 
  # amount of loans originated (loan.get_amt_loans_originated()) for all 
  # loan types for each school (loan in school.get_loans()). It does this for every 
  # school in the loan_data list (school in loan_data). 
  all_schools_total_originated = [ sum( [ loan.get_amt_loans_originated() \
                                         for loan in school.get_loans()]) \
                                         for school in loan_data ]

  # (The following list comprehension is unchanged from the previous version.)
  # A second list comprehension is required to filter for sums (i.e., total loans 
  # originated) over the minimum specified (i.e., > 20,000,000).
  # This is a simple comprehension that looks at each originated sum in 
  # all_schools_total_originated and includes it in all_schools_total_orig_filtered 
  # if it's greater than the minimum. 
  # (Again, I tried to combine this comprehension with the previous, but I couldn't 
  # figure out how to assign a variable to each sum within the comprehension 
  # that I could then check against the min/max values.) 
  all_schools_total_orig_filtered = [ orig for orig in all_schools_total_originated \
                                     if orig > min_val ]

  # Return the length of the all_schools_total_orig_filtered list as this will
  # be the number of schools with expected total loan amounts, if the loans
  # were fully disbursed, greater than the minimum value.
  return len(all_schools_total_orig_filtered)
  

### Answer question 2 ###
# Call the get_num_originated_over_amt function to answer Question 2. 
print('Question 2: {:,}'.format(get_num_originated_over_amt(loan_data, 20000000)))




### Question 3 #####################################################
####################################################################
# 3. Amongst the schools that are considered part of Bellevue, WA 
# (according to zip codes on http://zipcode.org), what was the largest 
# number of recipients within a school for either DL Unsubsidized 
# Undergraduate or DL Unsubsidized Graduate loans? Ignore unavailable 
# data i.e. data with ‘-’ value.
# Answer: 219
# (Again, this is the same answer I found prior to refactoring.)

def get_max_recipients_DLUNSUBSIDIZED(loan_data, area_zip_codes):
  '''
  Function takes in loan information and a list of zip codes and returns
  the maximum number of recipients within a school for loans of type
  DL UNSUBSIDIZED UNDERGRADUATE or DL UNSUBSIDIZED GRADUATE (i.e., for 
  each school, this function finds the maximum recipients between these
  two loan types, saves that number to a list and then finds the maximum
  number of recipients from that list and return that number).
  
  loan data: a list of School objects that contain Loan subclass objects.
  area_zip_codes: a list of strings of 5-digit zip codes
  returns: an integer, maximum number of recipients for either DL 
  UNSUBSIDIZED UNDERGRADUATE or DL UNSUBSIDIZED GRADUATE loans from all
  schools in area defined by area_zip_codes
  '''
  
  # This list comprehension uses the same logic as the one prior to refactoring,
  # but the various class attributes of the School and Loan subclasses are called 
  # using the getter methods set for these classes.
  # This is a nested list comprehension. The inner comprehension gets the 
  # maximum number of recipients (loan.get_num_recipients()) between the 
  # DL_Unsubsidized_Undergraduate and DL_Unsubsidized_Graduate loan types 
  # (type)loan.__name__ == "DL_Unsubsidized_Undergraduate" or 
  # "DL_Unsubsidized_Graduate" for all loan types for each school 
  # (loan in school.get_loans()). It does this for all schools in loan_data 
  # where the 5 digit zip code is in Bellevue, WA 
  # (school.get_Zip_Code()[:5] in area_zip_codes). 
  all_schools_max_recip = [ max( [loan.get_num_recipients() \
                                  for loan in school.get_loans() \
                                  if type(loan).__name__ == "DL_Unsubsidized_Undergraduate" \
                                  or type(loan).__name__ == "DL_Unsubsidized_Graduate" ]) \
                                  for school in loan_data \
                                  if school.get_Zip_Code()[:5] in area_zip_codes ]

  # Return the ultimate maximum number of recipients from all of the maximum
  # numbers from each school in zip code area for DL Unsubsidized Undergraduate 
  # and DL Unsubsidized Graduate loan types.
  return max(all_schools_max_recip)
 
 
#
### Answer question 3 ###
# Area zip codes for Bellevue, WA as defined by http://zipcode.org/city/WA/BELLEVUE
area_zip_codes = ['98004', '98005', '98006', '98007', '98008', '98009', '98015']

# Call the get_max_recipients_DLUNSUBSIDIZED function to answer Question 3. 
print('Question 3: {:,}'.format(get_max_recipients_DLUNSUBSIDIZED(loan_data, area_zip_codes)))




### Question 4 #####################################################
####################################################################
# Consider the state in which the last Olympics was hosted in the USA. What is the 
# sum of the expected total loan amount if the loan is fully disbursed for 
# DL Subsidized loans in the public schools in this state in Q4 of 2016-2017, 
# based on the data provided?
# Answer: 7,912,715
  
def get_sum_originated(loan_data, state, loan_type, school_type):
  '''
  Function takes in loan information, state, loan type  and school type and 
  returns the sum of expected total loan amount if fully disbursed for loan_type,
  school_type in state.
  
  loan_data:  a list of School objects that contain Loan subclass objects.
  state: a string, the state to filter for
  loan_type: a string, the loan type/class to sum
  school_type: a string, the school type to filter for
  returns: an integer, the sum of expected total loan amount if fully disbursed.
  '''

  # This list comprehension uses the same logic as the one prior to refactoring,
  # but the various class attributes of the School and Loan subclasses are called 
  # using the getter methods set for these classes.
  # This is a nested list comprehension. The inner comprehension gets and then 
  # sums the amount of loans originated (loan.get_amt_loans_originated()) for loans in 
  # each school (loan in school.get_loans()), if the type of loan matches the 
  # loan type passed in as a parameter ((type(loan).__name__ == loan_type, 
  # "DL_Subsidized" in this case). It does this for all schools in loan_data 
  # where the state equals the parameter passed in (school.get_State() == state, 
  # "UT" in this case), and the school type equals the parameter passed in 
  # (school.get_School_Type() == school_type, "Public" in this case). 
  all_schools_loans_orig = [  sum(loan.get_amt_loans_originated() \
                                  for loan in school.get_loans() \
                                  if type(loan).__name__ == loan_type ) \
                                  for school in loan_data \
                                  if school.get_State() == state \
                                  and school.get_School_Type() == school_type ] 

  # Return the sum of all_schools_loans_orig as this will be the sum of
  # expected total loan amount if the loan is fully disbursed for DL Subsidized Loans
  # in Public schools in Utah.
  return sum(all_schools_loans_orig)



### Answer question 4 ###
# Initialize state, loan_type and school_type variables
state = 'UT'
loan_type = 'DL_Subsidized'
school_type = 'Public'
#
## Call the get_sum_originated function to answer Question 4.
print('Question 4: ${:,}'.format(get_sum_originated(loan_data, state, loan_type, school_type)))
 
 
 
 
### Question 5 #####################################################
####################################################################
# Consider all the private nonprofit schools in WA state where the 
# name of the school starts with either “s”, “u”, “v” or “w”. For 
# these schools, consider the expected total loan amount if the 
# loan is fully disbursed for unsubsidized undergraduate studies. 
# Exclude all schools where the unsubsidized undergraduate loan 
# amount is not available i.e. “-” or 0. What was the median value?
# Answer: 79,524

def get_median_loan_amt_python(loan_data, school_type, state, first_letters, loan_type):
  '''
  Function takes in loan information, school type, state, loan type 
  and a list of first letters and returns the median loan amount 
  for the specified loan type in schools  of the specified type in
  the given state, if the school name begins with the letters in 
  the first letters list.
  
  loan_data: a list of School objects that contain Loan subclass objects.
  school_type: a string, the school type to filter for
  state: a string, the state to filter for
  first_letters: a list of uppercase letters that school names should
  begin with
  loan_type: a string, the loan type to consider
  returns: an integer, the median of expected total loan amount if 
  fully disbursed
  '''
  
  # The below actually returns a list of lists, which seems unneccessary, 
  # but I am unable to get the nested comprehension to work correctly otherwise.
  # This list comprehension uses a similar logic to that of the one prior to refactoring,
  # but the various class attributes of the School and Loan subclasses are called 
  # using the getter methods set for these classes.
  # This is a nested list comprehension. The inner comprehension gets the 
  # amount of loans originated (loan.get_amt_loans_originated()) for loans in 
  # each school (loan in school.get_loans()), if the type of loan matches the 
  # loan type passed in as a parameter ((type(loan).__name__ == loan_type, 
  # "DL_Unsubsidized_Undergraduate" in this case). It does this for all 
  # schools in loan_data where the state equals the parameter passed in 
  # (school.get_State() == state, "WA" in this case), and the school type 
  # equals the parameter passed in (school.get_School_Type() == school_type, 
  # "Private-Nonprofit" in this case), and where the first letter of the school's
  # name is in the first_letters list (school.get_School(0)[0] in first_letters).
  all_schools_loans_orig = [  [loan.get_amt_loans_originated() \
                                  for loan in school.get_loans() \
                                  if type(loan).__name__ == loan_type \
                                  and loan.get_amt_loans_originated != 0] \
                                  for school in loan_data \
                                  if school.get_State() == state \
                                  and school.get_School_Type() == school_type \
                                  and school.get_School()[0] in first_letters ]
 
  
  
  # Then return the median value from that list. (Statistics.media will sort the
  # list first.) This actually returns a single element sublist from 
  # from all_schools_loans_orig, so I then call the 0 index as the ultimate 
  # return value. (This is a little cludgy...room for improvement here.) 
  return statistics.median(all_schools_loans_orig)[0]
  


### Answer question 5 
# Initialize state, school_type, loan_type and first_letters  
state = 'WA'
school_type = 'Private-Nonprofit'
loan_type = 'DL_Unsubsidized_Undergraduate'
first_letters = ['S', 'U', 'V', 'W']

print("Question 5: ${:,}".format(get_median_loan_amt_python(loan_data, school_type, state, first_letters, loan_type)))




