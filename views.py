#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2008 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import datetime
from google.appengine.api import mail
from django.http import HttpResponseRedirect
from django.http import HttpResponsePermanentRedirect
from django.shortcuts import render_to_response

from models import Subscriber
from models import Gogodownloader
from forms import SubscriberForm

def index(request):
	form = SubscriberForm()
	return render_to_response('index.html',
                            {
                             'form': form
                            }
                           )

def addSubscriber(request):
	form = SubscriberForm(request.POST)
	if form.is_valid():
		subscriber = Subscriber(email=form.clean_data['email'])
		subscriber.put()
		message = mail.EmailMessage(sender=u"DunTeam <admin@dunteam.com>", subject=u"Дагасанд баярлалаа")
		message.to = subscriber.email
		message.body = u"Баярлалаа\nТа бидний шинэ мэдээг дагахаар амжилттай бүртгүүллээ.\nDunTeam"
		message.send()
	else:
		return render_to_response('index.html', {'form': form })

	return HttpResponseRedirect('/')
	
def login(request):
	user = users.get_current_user()
	if user:
		return HttpResponseRedirect('/')
	else:
		return HttpResponsePermanentRedirect(users.create_login_url(request.get_full_path()))

def not_found(request):
	return render_to_response('not_found.html',{})

def internal_error(request):
	return render_to_response('internal_error.html',{})			

def dl_gogodownloader(request):
	client_ip = request.META['REMOTE_ADDR']
	browser = request.META['HTTP_USER_AGENT']
	referrer = request.META['HTTP_REFERER']
	download = Gogodownloader(ip=client_ip, browser=browser, referrer=referrer)
	download.put()
	return HttpResponseRedirect('/GogoDownloaderSetup.msi')
