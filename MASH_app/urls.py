
from django.urls import path
from .views import *

urlpatterns = [
    path('',index ),
    path('forgot_password/',forgot_password, name="forgot_password"),
    path('sign_up/',sign_up, name="sign_up"),
    path('register',register, name="register"),
    path('logins',logins, name="logins"),
    path('loginf',loginf, name="loginf"),
    path('sign_inf/',sign_inf, name="sign_inf"),
    path('sign_ins/',sign_ins, name="sign_ins"),
    path('newsletter/',newsletter, name="newsletter"),
    path('error/',error, name="error"),
    path('forgot/',forgot, name="forgot"),
    path('assignments/',assignments, name="assignments"),
    path('reference/',reference, name="reference"),
    path('notice/',notice, name="notice"),
    path('invalidcredentials/',invalidcredentials, name="invalidcredentials"),
    path('edit/',edit, name="edit"),
    path('contactd/',contactd, name="contactd"),
    path('feedback/',feedback, name="feedback"),
    path('feedbackf/',feedbackf, name="feedbackf"),
    path('faculty/',faculty, name="faculty"),
    path('student/',student, name="student"),
    path('hod/',hod, name="hod"),
    path('payment/',payment, name="payment"),
    path('notes1/',notes1, name="notes1"),
    path('papers/',papers, name="papers"),
    path('Studentportal/',Studentportal, name="Studentportal"),
    path('GTUcircular/',GTUcircular, name="GTUcircular"),
    path('timetable/',timetable, name="timetable"),
    path('comingsoon/',comingsoon, name="comingsoon"),
    path('logout/', logout, name="logout"),
    path("profile_data/", profile_data, name="profile_data"),
    path("assignment_upload/", assignment_upload, name="assignment_upload"),
    path("video_upload/", video_upload, name="video_upload"),
    path("notices/", notices, name="notices"),
]
