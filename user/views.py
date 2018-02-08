#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import User
from message.models import Message
import json
import random

# Create your views here.
def index(request):
    return HttpResponse('你好， 少年')

def getKey(user):
    import hashlib
    a = 'key=' + user.user_id + str(random.randint(0, 100000000)) + user.user_id + str(random.randint(0, 100000000))
    md5 = hashlib.md5(a.encode('utf-8')).hexdigest()
    return md5

"""登录接口
    接口说明:
        1. 存在该用户， 验证密码后登录。
        2. 不存在该用户，注册该用户，并登录。
    请求参数:
        user_id: 登录用户id
        password: 登录密码
    响应内容:
        msg: 成功后附带的信息
        key: 登录后得到的验证信息
        error: 操作错误的提示信息
    错误信息详解:
        What are you talk about: 请求参数不符合标准
        Must set method GET: 只支持GET方法
        Bad Password: 密码错误
        user_id is too long: 用户名太长，不能超过20位
        password is too long: 用户名太长，不能超过20位
    请求列表:
        GET /user/login?user_id=123456&password=123456
"""

def login_user(request):
    res = {
        'msg': '',
        'data': '',
        'key': '',
        'error': ''
    }
    if request.method == 'GET':
        try:
            user_id = request.GET['user_id']
            password = request.GET['password']
        except Exception:
            res['error'] = 'What are you talk about'
            return res
        if len(user_id) >= 20:
            res['error'] = 'user_id is too long'
            return res
        if len(password) >= 20:
            res['error'] = 'password is too long'
            return res
        user = User.objects.get_or_create(user_id=user_id)
        user = User.objects.get(user_id=user_id)
        if user.password != password:
            res['error'] = 'Bad Password'
            return res
        else:
            key = getKey(user)
            user.key = key
            user.save()
            res['msg'] = 'Login Success'
            res['key'] = key
        return res
    res['error'] = 'Must set method GET'
    return res

"""发送信息接口
    接口说明:
        1. 凭借特殊的key发送给指定用户to指定信息，信息内容为msg
    请求参数:
        key: 每次操作获得的key（没有时间限制，起始从登录开始获得）
        msg: 需要发送的信息
        to: 需要发送给哪个用户
    响应内容:
        key: 操作成功后得到的new_key, 用于下一次操作
        msg: 成功后得到的信息
        error: 操作失败后得到的信息（key不会刷新）
    错误信息列表:
        What are you talk about: 请求参数不符合标准
        Must set method GET: 只支持GET方法
        Bad Key: 错误的key,请重新登录进行获取
        Not found to_user: 指定发送的用户不存在
        Msg cant be blank: 发送内容不能为空
        Cant send yourself: 不能给自己发送信息
"""

def send_msg(request):
    res = {
        'msg': '',
        'data': '',
        'key': '',
        'error': ''
    }
    if request.method == 'GET':
        try:
            key = request.GET['key']
            msg = request.GET['msg']
            to_userid = request.GET['to']
        except Exception:
            res['error'] = 'What are you talk about?!'
            return res
        try:
            from_user = User.objects.get(key=key)
        except Exception:
            res['error'] = 'Bad Key'
            return res
        try:
            to_user = User.objects.get(user_id=to_userid)
        except Exception:
            res['error'] = 'Not found to_user'
            return res
        if msg == '':
            res['error'] = 'Msg cant be blank'
            return res
        if from_user.user_id == to_user.user_id:
            res['error'] = 'Cant send yourself'
            return res
        m = Message(from_user_id=from_user.user_id, to_user_id=to_user.user_id, text=msg)
        m.save()
        res['msg'] = 'Send Success'
        new_key = getKey(from_user)
        from_user.key = new_key
        from_user.save()
        res['key'] = new_key
        return res
    res['error'] = 'Must set method GET'
    return res

"""获取用户所有接受到的信息
    接口说明:
        传入用户的对话钥(key)，即可获得所有对话信息
    请求参数:
        key: 用户的对话钥
        read: 只要传入该值为true则会过滤掉已读信息
        show: 只要传入该值为true则会过滤掉已经获取的信息（即这条信息只会被获取一次）
        delete: 只要传入该值为true则会过滤掉已经删除的信息
    相应内容:
        key: 操作成功后得到的new_key, 用于下一次操作
        data: 消息Message数组的JSON数据
            user_id: 由谁发起的消息
            text: 消息内容
            data: 发起时间
            read: 是否阅读
        msg: 成功后得到的信息
        error: 操作失败后得到的信息（key不会刷新）
"""

def get_msg(request):
    res = {
        'msg': '',
        'data': '',
        'key': '',
        'error': ''
    }
    if request.method == 'GET':
        # 获得对话钥
        try:
            key = request.GET['key']
        except Exception:
            res['error'] = 'What are you talk about'
            return res
        # 获得是否过滤已读信息
        if request.GET.__contains__('read') and request.GET['read'] == 'true':
            is_read = True
        else:
            is_read = False
        # 获得是否过滤已展示信息
        if request.GET.__contains__('show') and request.GET['show'] == 'true':
            is_show = True
        else:
            is_show = False
        # 获得是否过滤已删除信息
        if request.GET.__contains__('delete') and request.GET['delete'] == 'true':
            is_delete = True
        else:
            is_delete = False
        try:
            to_user = User.objects.get(key=key)
        except Exception:
            res['error'] = 'Bad Key'
            return res
        msgs = Message.objects.filter(to_user_id=to_user.user_id)
        msg_list = []
        for msg in msgs:
            if (is_delete and msg.is_delete) or (is_read and msg.is_read) or (is_show and msg.is_show):
                continue;
            msg_list.append({
                'user_id': msg.from_user_id,
                'text': msg.text,
                'date': msg.message_date.__str__(),
                'read': msg.is_read,
                'show': msg.is_show,
                'delete': msg.is_delete
            })
            if not msg.is_show:
                msg.is_show = True
                msg.save()
        new_key = getKey(to_user)
        to_user.key = new_key
        to_user.save()
        res['key'] = new_key
        res['data'] = msg_list
        res['msg'] = 'Get Success'
        return res
    res['error'] = 'Must set method GET'
    return res
def send(request):
    return HttpResponse(json.dumps(send_msg(request)), content_type="application/json")
    
def login(request):
    return HttpResponse(json.dumps(login_user(request)), content_type="application/json")

def get(request):
    return HttpResponse(json.dumps(get_msg(request)), content_type="application/json")