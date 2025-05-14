from django.urls import path
from board.views import board, post_write, post_detail
from user.views import signin, signup, sign_out
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [ 
    path("user/signin", signin, name="signin"),   
    path("user/signup", signup, name="signup"),   
    path("board", board, name="board"),
    path("user/signout",sign_out, name="signout"),
    
    path("post/write", post_write, name="post_write"),
    path("post/<int:post_id>", post_detail, name="post_detail"),
    
]

if settings.DEBUG:
    urlpatterns += static('upload', document_root=settings.MEDIA_ROOT)
