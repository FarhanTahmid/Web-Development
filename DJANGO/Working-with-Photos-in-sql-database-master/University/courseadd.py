

from pydoc import describe
from unicodedata import name
from django.forms import SelectDateWidget

from django.db import connections
class CourseAdd:
    def __init__(self,prove,name='',contact='',email='',facebooklink='',instalink='',linkedinlink='',snapid=''):
        
        self.name=name
        self.contact=contact
        self.email=email
        self.facebooklink=facebooklink
        self.instalink=instalink
        self.linkedinlink=linkedinlink
        self.snaplink=snapid
        self.prove=prove
        
    def addCourse(self):
        #print(f"Course Name: {self.name}, Course ID: {self.id}, Description: {self.description}")
        
        #database connection to the app
        db_cursor=connections['default'].cursor()
        
        #Sql Query for course add
        db_cursor.execute("INSERT INTO University_complains (name,contact,email,facebookid,instaid,linkedinid,snapid,prove) VALUES('"+self.name+"','"+self.contact+"','"+self.email+"','"+self.facebooklink+"','"+self.instalink+"','"+self.linkedinlink+"','"+self.snaplink+"','"+self.prove+"')")
    
    def deleteCourse(self):
        #database connection to the app
        db_cursor=connections['default'].cursor()
        
        #Sql Query for course add
        db_cursor.execute("DELETE FROM University_courseregistrations WHERE (course_ID='"+self.course_id+"' AND WHERE owner_id='"+self.student_id+"')")
        
        
    

