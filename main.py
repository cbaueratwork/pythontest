# Copyright 2016 Google Inc.
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
import webapp2
import time
import random

class MainPage(webapp2.RequestHandler):
  def get(self):
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Hello, Universe!')


class TakeSomeTime(webapp2.RequestHandler):
  def get(self):
    wait_time = random.random()
    time.sleep(wait_time)
    self.response.headers['Content-Type'] = 'text/plain'
    self.response.write('Waited for {}ms before returning'.format(wait_time * 1000))


class PossibleException(webapp2.RequestHandler):
  def get(self):
    divisor = random.randint(0, 10)
    self.response.headers['Content-Type'] = 'text/plain'
    try:
      answer = 42 / divisor
      self.response.write('Divided 42 by {}, got {}'.format(divisor, answer))
    except ZeroDivisionError:
      self.response.write('Error: attempted to divide by zero')



app = webapp2.WSGIApplication([
  ('/', MainPage),
  ('/time', TakeSomeTime),
  ('/divide', PossibleException),
], debug=True)


