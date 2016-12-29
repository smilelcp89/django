from django.shortcuts import render   #使用render函数渲染html页面
from django.shortcuts import HttpResponse  #直接在界面上输出字符
from polls.models import Poll
from django.utils import timezone

def poll_index(request):
    #if 'name' in request.GET:
        #name = request.GET['name'];
    #如果没有传递就给个默认值
    name = request.GET.get('name','')
    fruit = ['apple','banana','orange']
    person = {'name':'liang','age':23}
    number = map(str, range(100))  # 一个长度为100的 List
    food = [{"userid": "0001",
             "data": [
                  {"itemdate": "2015-02-03",
                   "type": "火锅"
                   },
                  {"itemdate": "2015-03-03",
                   "type": "面包"
                   },
                  {"itemdate": "2014-02-03",
                   "type": "小吃"
                   }
              ]},
            {"userid": "0002",
              "data": [
                  {"itemdate": "2013-05-09",
                   "type": "川菜"
                   },
                  {
                      "itemdate": "2016-05-12",
                      "type": "点心"
                  },
                  {
                      "itemdate": "2015-09-08",
                      "type": "茶馆"
                  }
            ]}
     ]
    return render(request,'polls/index.html',{'name':name,'fruit':fruit,'person':person,'number':number,'food':food})

def poll_detail(request,poll_id=0):
    return render(request,'polls/detail.html')

def poll_result(request,poll_id=0):
    return render(request,'polls/result.html')

def poll_vote(request,poll_id=0):
    return render(request,'polls/vote.html')

from django.views.decorators.cache import cache_page
from django.core.cache import cache
def poll_add(request):
    if request.method == 'POST':
        question = request.POST['question']
        #question = request.POST.get('question')
        p = Poll(question=question,pub_date=timezone.now())
        try:
            p.save()
            return HttpResponse('添加成功')
        except Exception as e:
            return HttpResponse('添加失败')
    else:
        myname = cache.get('myname')
        if not myname:
            cache.set('myname','liang',300)
        return render(request,'polls/add.html',{'myname':myname})

#发送邮件
from django.core.mail import send_mail  #发送单个邮件
#import mydjango.settings as settings
from django.conf import settings
from django.core.mail import send_mass_mail   #发送多个邮件
from django.core.mail import EmailMultiAlternatives  #发送附件
def poll_email(request):
    if request.method == 'POST':
        title = request.POST['title']
        receiver = request.POST['receiver']
        content = request.POST['content']
        #if send_mail(title, content, settings.DEFAULT_FROM_EMAIL,[receiver], fail_silently=False): #发送单个邮件，这里可以有多个接收人

        #发送多个邮件
        #message1 = (title+'-111', content, settings.DEFAULT_FROM_EMAIL,[receiver])
        #message2 = (title+'-222', content, settings.DEFAULT_FROM_EMAIL,[receiver])
        #if send_mass_mail((message1, message2), fail_silently=False):

        #发送html
        html_content = '<p style="color:red;font-size:16px;">'+content+'</p>'
        msg = EmailMultiAlternatives(title, content, settings.DEFAULT_FROM_EMAIL, [receiver])
        msg.attach_alternative(html_content, "text/html")    #发送html格式文本
        #发送附件
        msg.attach_file('E:/wnmp/www/mydjango/assets/kaola.jpg')
        if msg.send():
            return HttpResponse('发送成功')
        else:
            return HttpResponse('发送失败')
    else:
        return render(request, 'polls/email.html')


from django.template.loader import render_to_string
import os
def poll_makehtml(request):
    #分配变量到模板中
    context = {'name': 'makehtml'}
    static_html = os.path.join(settings.BASE_DIR,'html','cache.html')
    if not os.path.exists(static_html):
        #return HttpResponse('文件不存在')
        content = render_to_string('polls/email.html', context)
        with open(static_html, 'w+',encoding='utf-8') as static_file:
            static_file.write(content)
    return render(request, static_html)

def poll_login(request):

    response = HttpResponse('登录成功')
    response.set_cookie("color", 'red')
    request.session['isLogin'] = 1
    return response

def index(request):

    if request.session.get('isLogin') == 1:
        # del request.COOKIES['color']
        return HttpResponse('已登录：%s' % request.COOKIES.get('color'))
    else:
        try:
            del request.session['isLogin']
        except KeyError as e:
            pass
        return HttpResponse('未登录')
    #return render(request,'index.html')



